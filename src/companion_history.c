#include "global.h"
#include "companion_history.h"
#include "main.h"

#if FNPC_ENABLE_NPC_FOLLOWERS && !IS_FRLG

#define HISTORY_MAGIC 0x31484345
#define MAILBOX_MAGIC 0x314D4345
#define REQUEST_LOAD 1
#define REQUEST_PREPARE 2
#define STATUS_OK 1
#define STATUS_ERROR 2

struct HistorySnapshot
{
    u8 magic[8];
    u16 version;
    u16 voices;
    u32 contexts;
    u8 identity[16];
    u8 spent[COMPANION_HISTORY_VOICES][COMPANION_HISTORY_BANK_BYTES];
};

EWRAM_DATA struct HistorySnapshot gCompanionHistorySnapshot = {0};
EWRAM_DATA struct CompanionHistoryMailbox gCompanionHistoryMailbox = {0};
static EWRAM_DATA bool8 sReady = FALSE;
static bool32 PrepareObservation(void);

// Locate this descriptor in ROM, then validate all pointers/sizes before access.
const struct
{
    u8 magic[8];
    u32 version;
    struct CompanionHistoryMailbox *mailbox;
    struct HistorySnapshot *snapshot;
    u32 snapshotSize;
    const u32 *frameCounter;
} gCompanionHistoryDescriptor =
{
    "ECHOBRD1", 1, &gCompanionHistoryMailbox,
    &gCompanionHistorySnapshot, sizeof(struct HistorySnapshot), &gMain.vblankCounter1,
};

STATIC_ASSERT(sizeof(struct CompanionHistoryAnchor) == 56, HistoryAnchorABI);
STATIC_ASSERT(sizeof(struct HistorySnapshot) == 16928, HistorySnapshotABI);
STATIC_ASSERT(offsetof(struct CompanionHistoryMailbox, responseDigest) == 60, HistoryMailboxABI);

static bool32 HasAnchor(void)
{
    return gSaveBlock2Ptr->companionHistory.magic == HISTORY_MAGIC
        && gSaveBlock2Ptr->companionHistory.version == 1;
}

static void InitMailbox(void)
{
    memset(&gCompanionHistoryMailbox, 0, sizeof(gCompanionHistoryMailbox));
    gCompanionHistoryMailbox.magic = MAILBOX_MAGIC;
    gCompanionHistoryMailbox.version = 1;
    gCompanionHistoryMailbox.snapshot = &gCompanionHistorySnapshot;
    gCompanionHistoryMailbox.size = sizeof(gCompanionHistorySnapshot);
}

void CompanionHistory_OnLoad(void)
{
    InitMailbox();
    sReady = FALSE;
    memset(&gCompanionHistorySnapshot, 0, sizeof(gCompanionHistorySnapshot));
    memcpy(gCompanionHistorySnapshot.magic, "ECHOMEM1", 8);
    gCompanionHistorySnapshot.version = 1;
    gCompanionHistorySnapshot.voices = COMPANION_HISTORY_VOICES;
    gCompanionHistorySnapshot.contexts = COMPANION_HISTORY_CONTEXTS;
    if (HasAnchor())
    {
        memcpy(gCompanionHistorySnapshot.identity, gSaveBlock2Ptr->companionHistory.identity, 16);
        memcpy(gCompanionHistoryMailbox.digest, gSaveBlock2Ptr->companionHistory.digest, 32);
        gCompanionHistoryMailbox.request = REQUEST_LOAD;
    }
    else
    {
        // No changes to game RNG; once saved this identity is immutable.
        memcpy(gCompanionHistorySnapshot.identity, gSaveBlock2Ptr->playerTrainerId, 4);
        memcpy(gCompanionHistorySnapshot.identity + 4, gSaveBlock2Ptr->playerName, 8);
        memcpy(gCompanionHistorySnapshot.identity + 12, &gSaveBlock2Ptr->encryptionKey, 4);
        sReady = TRUE;
    }
}

void CompanionHistory_Reset(void)
{
    memset(&gSaveBlock2Ptr->companionHistory, 0, sizeof(gSaveBlock2Ptr->companionHistory));
    CompanionHistory_OnLoad();
}

static bool32 Ready(void)
{
    if (gCompanionHistoryMailbox.magic != MAILBOX_MAGIC)
        CompanionHistory_OnLoad();
    if (!sReady && gCompanionHistoryMailbox.request == REQUEST_LOAD
        && gCompanionHistoryMailbox.status == STATUS_OK)
    {
        sReady = TRUE;
        gCompanionHistoryMailbox.request = 0;
    }
    // A failed/missing load is never converted to an empty history.
    return sReady && gCompanionHistoryMailbox.heartbeat != 0
        && (u32)(gMain.vblankCounter1 + 1 - gCompanionHistoryMailbox.heartbeat) < 120;
}

bool32 CompanionHistory_HasSpent(u32 voice, u32 context)
{
    if (voice >= COMPANION_HISTORY_VOICES || context < COMPANION_HISTORY_LEGACY_CONTEXTS
        || context >= COMPANION_HISTORY_CONTEXTS || !Ready())
        return TRUE;
    return (gCompanionHistorySnapshot.spent[voice][context / 8] & (1 << (context % 8))) != 0;
}

bool32 CompanionHistory_Spend(u32 voice, u32 context)
{
    if (CompanionHistory_HasSpent(voice, context))
        return FALSE;
    gCompanionHistorySnapshot.spent[voice][context / 8] |= 1 << (context % 8);
    // Prepare the immutable host snapshot BEFORE offering the new observation.
    // The next cartridge save simply writes its valid anchor, including partial
    // saves. No file IO or new failure branch is introduced into trade/save code.
    if (!PrepareObservation())
    {
        gCompanionHistorySnapshot.spent[voice][context / 8] &= ~(1 << (context % 8));
        return FALSE;
    }
    return TRUE;
}

static bool32 PrepareObservation(void)
{
    u32 frames = 0;
    u16 previousLine = REG_VCOUNT;
    if (!Ready())
        return FALSE;
    gCompanionHistoryMailbox.status = 0;
    gCompanionHistoryMailbox.request = REQUEST_PREPARE;
    // Emulator frame callbacks run even while the CPU is waiting here. Do not
    // depend on the game's IRQ or run gameplay/tasks during a save transaction.
    while (gCompanionHistoryMailbox.status == 0 && frames < 120)
    {
        u16 line = REG_VCOUNT;
        if (line < previousLine)
            frames++;
        previousLine = line;
    }
    if (gCompanionHistoryMailbox.status != STATUS_OK)
    {
        gCompanionHistoryMailbox.request = 0;
        return FALSE; // No anchor change; Spend restores the previous bit.
    }
    gSaveBlock2Ptr->companionHistory.magic = HISTORY_MAGIC;
    gSaveBlock2Ptr->companionHistory.version = 1;
    memcpy(gSaveBlock2Ptr->companionHistory.identity, gCompanionHistorySnapshot.identity, 16);
    memcpy(gSaveBlock2Ptr->companionHistory.digest, gCompanionHistoryMailbox.responseDigest, 32);
    gCompanionHistoryMailbox.request = 0;
    return TRUE;
}

#else
void CompanionHistory_Reset(void) {}
void CompanionHistory_OnLoad(void) {}
bool32 CompanionHistory_HasSpent(u32 voice, u32 context) { return TRUE; }
bool32 CompanionHistory_Spend(u32 voice, u32 context) { return FALSE; }
#endif
