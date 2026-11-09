#ifndef GUARD_COMPANION_HISTORY_H
#define GUARD_COMPANION_HISTORY_H

#define COMPANION_HISTORY_CONTEXTS 12288
#define COMPANION_HISTORY_VOICES 11
#define COMPANION_HISTORY_BANK_BYTES (COMPANION_HISTORY_CONTEXTS / 8)
#define COMPANION_HISTORY_LEGACY_CONTEXTS 736

// Appended to SaveBlock2. Every existing field retains its released offset.
// This block participates in normal AND partial link/Frontier saves.
struct CompanionHistoryAnchor
{
    u32 magic;
    u32 version;
    u8 identity[16];
    u8 digest[32];
};

// Bridge ABI v1. The host must validate the descriptor and entire request before
// writing anything. It may write only responseDigest, status, heartbeat and,
// for LOAD, the snapshot buffer. Status is written last.
struct CompanionHistoryMailbox
{
    u32 magic;
    u32 version;
    volatile u32 heartbeat;
    volatile u32 request;
    volatile u32 status;
    const void *snapshot;
    u32 size;
    u8 digest[32];
    u8 responseDigest[32];
};

void CompanionHistory_Reset(void);
void CompanionHistory_OnLoad(void);
bool32 CompanionHistory_HasSpent(u32 voice, u32 context);
bool32 CompanionHistory_Spend(u32 voice, u32 context);

#endif
