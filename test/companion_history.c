#include "global.h"
#include "companion_history.h"
#include "malloc.h"
#include "test/test.h"

#if FNPC_ENABLE_NPC_FOLLOWERS && !IS_FRLG

extern struct CompanionHistoryMailbox gCompanionHistoryMailbox;

TEST("History migration preserves every released SaveBlock2 byte")
{
    struct SaveBlock2 *old = Alloc(sizeof(*old));
    *old = *gSaveBlock2Ptr;
    memset(&gSaveBlock2Ptr->companionHistory, 0, sizeof(struct CompanionHistoryAnchor));
    CompanionHistory_OnLoad();
    EXPECT_EQ(memcmp(gSaveBlock2Ptr, old, offsetof(struct SaveBlock2, companionHistory)), 0);
    EXPECT_EQ(gSaveBlock2Ptr->companionHistory.magic, 0);
    EXPECT_EQ(CompanionHistory_Spend(0, 736), FALSE); // No attached helper.
    EXPECT_EQ(gSaveBlock2Ptr->companionHistory.magic, 0);
    *gSaveBlock2Ptr = *old;
    CompanionHistory_OnLoad();
    Free(old);
}

TEST("Missing companion history cannot replay comments or erase its saved anchor")
{
    struct CompanionHistoryAnchor old = gSaveBlock2Ptr->companionHistory;
    gSaveBlock2Ptr->companionHistory.magic = 0x31484345;
    gSaveBlock2Ptr->companionHistory.version = 1;
    memset(gSaveBlock2Ptr->companionHistory.digest, 0xA5, 32);
    CompanionHistory_OnLoad();
    EXPECT_EQ(gCompanionHistoryMailbox.request, 1);
    gCompanionHistoryMailbox.status = 2; // Host reports missing/corrupt file.
    for (u32 voice = 0; voice < COMPANION_HISTORY_VOICES; voice++)
    {
        EXPECT_EQ(CompanionHistory_HasSpent(voice, 736), TRUE);
        EXPECT_EQ(CompanionHistory_Spend(voice, 12287), FALSE);
    }
    EXPECT_EQ(gSaveBlock2Ptr->companionHistory.digest[0], 0xA5);
    EXPECT_EQ(gSaveBlock2Ptr->companionHistory.digest[31], 0xA5);
    gSaveBlock2Ptr->companionHistory = old;
    CompanionHistory_OnLoad();
}

TEST("Extended history rejects legacy indexes and out of bounds voices")
{
    EXPECT_EQ(CompanionHistory_Spend(11, 736), FALSE);
    EXPECT_EQ(CompanionHistory_Spend(0, 735), FALSE);
    EXPECT_EQ(CompanionHistory_Spend(0, 12288), FALSE);
    EXPECT_EQ(CompanionHistory_Spend(0xFFFFFFFF, 0xFFFFFFFF), FALSE);
}
#endif
