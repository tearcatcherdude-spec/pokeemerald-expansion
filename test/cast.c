#include "global.h"
#include "cast.h"
#include "follower_npc.h"
#include "data.h"
#include "event_data.h"
#include "event_object_movement.h"
#include "field_player_avatar.h"
#include "battle_setup.h"
#include "test/test.h"
#include "constants/event_objects.h"
#include "constants/kanto_progress.h"

#if FNPC_ENABLE_NPC_FOLLOWERS && !IS_FRLG
TEST("Cast migration initializes only its suffix and preserves the complete released Kanto save prefix")
{
    struct SaveBlock3 previous = *gSaveBlock3Ptr;
    u8 prefix[1004];
    memcpy(prefix, gSaveBlock3Ptr, sizeof(prefix));
    memset(&gSaveBlock3Ptr->cast, 0xFF, sizeof(gSaveBlock3Ptr->cast));
    Cast_EnsureInitialized();
    EXPECT_EQ(memcmp(prefix, gSaveBlock3Ptr, sizeof(prefix)), 0);
    EXPECT_EQ(gSaveBlock3Ptr->cast.version, 1);
    EXPECT_EQ(gSaveBlock3Ptr->cast.active, 0);
    EXPECT_EQ(gSaveBlock3Ptr->cast.recruited, 0);
    *gSaveBlock3Ptr = previous;
}
TEST("Cast identity flags occupy their own bank without overwriting Hoenn or Kanto bits")
{
    struct SaveBlock3 previous = *gSaveBlock3Ptr;
    bool32 old = FlagGet(0x20);
    Cast_EnsureInitialized();
    FlagSet(CAST_FLAG_BASE);
    FlagSet(CAST_FLAG_BASE + 9);
    EXPECT(FlagGet(CAST_FLAG_BASE));
    EXPECT(FlagGet(CAST_FLAG_BASE + 9));
    EXPECT_EQ(FlagGet(0x20), old);
    FlagClear(CAST_FLAG_BASE);
    EXPECT_EQ(FlagGet(CAST_FLAG_BASE), FALSE);
    EXPECT(FlagGet(CAST_FLAG_BASE + 9));
    EXPECT_EQ(Cast_GetFlagPointer(CAST_FLAG_BASE + CAST_COUNT), NULL);
    *gSaveBlock3Ptr = previous;
}
TEST("Companion reaction memory is independent and identical wording cannot reoffer under another source ID")
{
    struct SaveBlock3 previous = *gSaveBlock3Ptr;
    u8 pipMemory[128];
    memcpy(pipMemory, gSaveBlock3Ptr->pipHeard, sizeof(pipMemory));
    memset(&gSaveBlock3Ptr->cast, 0, sizeof(gSaveBlock3Ptr->cast));
    Cast_EnsureInitialized();
    gSaveBlock3Ptr->cast.active = 1;
    EXPECT(Cast_Offer(0));
    EXPECT(Cast_HasUsed(0));
    EXPECT_EQ(Cast_Offer(1), FALSE); // The same place observation, another Pip variant.
    gSaveBlock3Ptr->cast.active = 2;
    EXPECT_EQ(Cast_HasUsed(0), FALSE);
    EXPECT(Cast_Offer(0));
    gSaveBlock3Ptr->cast.active = 1;
    EXPECT(Cast_HasUsed(0));
    EXPECT_EQ(memcmp(pipMemory, gSaveBlock3Ptr->pipHeard, sizeof(pipMemory)), 0);
    Cast_ClearPending();
    *gSaveBlock3Ptr = previous;
}
TEST("Cast progress is not reinitialized when changing the active companion")
{
    struct SaveBlock3 previous = *gSaveBlock3Ptr;
    Cast_EnsureInitialized();
    gSaveBlock3Ptr->cast.recruited = 0x201;
    gSaveBlock3Ptr->cast.loreStage[0] = 3;
    gSaveBlock3Ptr->cast.active = 10;
    Cast_EnsureInitialized();
    EXPECT_EQ(gSaveBlock3Ptr->cast.recruited, 0x201);
    EXPECT_EQ(gSaveBlock3Ptr->cast.loreStage[0], 3);
    EXPECT_EQ(Cast_Active(), 10);
    *gSaveBlock3Ptr = previous;
}
TEST("Cast recruitment walking counts foot steps and excludes cycling")
{
    struct SaveBlock3 previous = *gSaveBlock3Ptr;
    u32 flags = gPlayerAvatar.flags;
    Cast_EnsureInitialized();
    gSaveBlock3Ptr->cast.steps = 100;
    gPlayerAvatar.flags = PLAYER_AVATAR_FLAG_ON_FOOT;
    Cast_OnStep();
    EXPECT_EQ(gSaveBlock3Ptr->cast.steps, 101);
    gPlayerAvatar.flags = PLAYER_AVATAR_FLAG_BIKE;
    Cast_OnStep();
    EXPECT_EQ(gSaveBlock3Ptr->cast.steps, 101);
    gPlayerAvatar.flags = flags;
    *gSaveBlock3Ptr = previous;
}
TEST("All ten recruitable trainers resolve four Pokemon at their native area plus three or five levels")
{
    static const u8 levels[] = {7, 10, 13, 10, 21, 7, 18, 19, 19, 27};
    for (u32 i = 0; i < CAST_COUNT; i++)
    {
        const struct Trainer *t = GetTrainerStructFromId(KANTO_TRAINER_BASE + 624 + i);
        EXPECT_EQ((u32)t->partySize, 4);
        EXPECT_EQ(SanitizeTrainerId(KANTO_TRAINER_BASE + 624 + i), KANTO_TRAINER_BASE + 624 + i);
        for (u32 j = 0; j < 4; j++)
        {
            EXPECT_NE(t->party[j].species, SPECIES_NONE);
            EXPECT_EQ(t->party[j].lvl, levels[i]);
        }
    }
}
TEST("New cast graphics preserve the released dynamic NPC graphics range")
{
    u16 previous = VarGet(VAR_OBJ_GFX_ID_0);
    EXPECT_EQ(OBJ_EVENT_GFX_VAR_0, OBJ_EVENT_GFX_PIP + 2);
    EXPECT_EQ(OBJ_EVENT_GFX_VAR_F, OBJ_EVENT_GFX_PIP + 17);
    EXPECT_GT(OBJ_EVENT_GFX_CAST_SILAS, OBJ_EVENT_GFX_VAR_F);
    VarSet(VAR_OBJ_GFX_ID_0, OBJ_EVENT_GFX_PIP);
    EXPECT_EQ(GetObjectEventGraphicsInfo(OBJ_EVENT_GFX_VAR_0), GetObjectEventGraphicsInfo(OBJ_EVENT_GFX_PIP));
    VarSet(VAR_OBJ_GFX_ID_0, previous);
}
extern const u8 Cast_EventScript_Companion[], Cozy_EventScript_Companion[];

TEST("Saved companion scripts are rebound on first interaction after a ROM upgrade")
{
    struct SaveBlock3 previous = *gSaveBlock3Ptr;
    const u8 *stale = (const u8 *)0x083D9964;
    bool32 wasMet = FlagGet(FLAG_MET_PIP);
    Cast_EnsureInitialized();
    gSaveBlock3Ptr->cast.recruited = 0x3FF;
    SetFollowerNPCData(FNPC_DATA_IN_PROGRESS, TRUE);
    for (u32 who = 1; who <= CAST_COUNT; who++)
    {
        gSaveBlock3Ptr->cast.active = who;
        gSaveBlock3Ptr->cast.loreStage[who - 1] = 4;
        SetFollowerNPCData(FNPC_DATA_EVENT_FLAG, CAST_FLAG_BASE + who - 1);
        SetFollowerNPCScriptPointer(stale);
        EXPECT_EQ(GetFollowerNPCScriptPointer(), Cast_EventScript_Companion);
        EXPECT_EQ(Cast_Active(), who);
        EXPECT_EQ(gSaveBlock3Ptr->cast.recruited, 0x3FF);
        EXPECT_EQ(gSaveBlock3Ptr->cast.loreStage[who - 1], 4);
    }
    gSaveBlock3Ptr->cast.active = 0;
    SetFollowerNPCData(FNPC_DATA_EVENT_FLAG, FLAG_HIDE_COZY_COMPANION);
    SetFollowerNPCScriptPointer(stale);
    EXPECT_EQ(GetFollowerNPCScriptPointer(), Cozy_EventScript_Companion);
    EXPECT_EQ(memcmp(&previous.kanto, &gSaveBlock3Ptr->kanto, sizeof(previous.kanto)), 0);
    EXPECT_EQ(memcmp(previous.pipHeard, gSaveBlock3Ptr->pipHeard, sizeof(previous.pipHeard)), 0);
    if (!wasMet)
        FlagClear(FLAG_MET_PIP);
    *gSaveBlock3Ptr = previous;
}

TEST("Refreshing a companion script does not replace a story escort script")
{
    struct SaveBlock3 previous = *gSaveBlock3Ptr;
    const u8 *escort = (const u8 *)0x08000001;
    Cast_EnsureInitialized();
    gSaveBlock3Ptr->cast.active = 6;
    SetFollowerNPCData(FNPC_DATA_IN_PROGRESS, TRUE);
    SetFollowerNPCData(FNPC_DATA_EVENT_FLAG, CAST_FLAG_BASE - 1);
    SetFollowerNPCScriptPointer(escort);
    EXPECT_EQ(GetFollowerNPCScriptPointer(), escort);
    EXPECT_EQ(gSaveBlock3Ptr->cast.active, 6);
    SetFollowerNPCData(FNPC_DATA_IN_PROGRESS, FALSE);
    EXPECT_EQ(GetFollowerNPCScriptPointer(), NULL);
    *gSaveBlock3Ptr = previous;
}
#endif
