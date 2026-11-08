#include "global.h"
#include "kanto_progress.h"
#include "event_data.h"
#include "test/test.h"
#include "data.h"
#include "battle_setup.h"
#include "constants/kanto_symbols.h"

#if FNPC_ENABLE_NPC_FOLLOWERS
TEST("Kanto progress initializes without changing the released watch and Pip save prefix")
{
    struct SaveBlock3 previous = *gSaveBlock3Ptr;
    u8 prefix[180];
    memcpy(prefix, gSaveBlock3Ptr, sizeof(prefix));
    memset(&gSaveBlock3Ptr->kanto, 0xFF, sizeof(gSaveBlock3Ptr->kanto));
    EXPECT(KantoProgress_EnsureInitialized());
    EXPECT_EQ(memcmp(prefix, gSaveBlock3Ptr, sizeof(prefix)), 0);
    EXPECT_EQ(gSaveBlock3Ptr->kanto.version, KANTO_PROGRESS_VERSION);
    EXPECT_EQ(VarGet(KANTO_VAR_BASE), 0);
    EXPECT_EQ(VarGet(KANTO_VAR_LIMIT - 1), 0);
    EXPECT_EQ(FlagGet(KANTO_FLAG_LIMIT - 1), FALSE);
    *gSaveBlock3Ptr = previous;
}
TEST("Kanto flags and variables never alias Hoenn progress")
{
    struct SaveBlock3 previous = *gSaveBlock3Ptr;
    bool32 oldFlag = FlagGet(0x20);
    u16 oldVar = VarGet(0x4023);
    FlagClear(0x20);
    VarSet(0x4023, 1);
    FlagSet(KANTO_FLAG_BASE + 0x20);
    VarSet(KANTO_VAR_BASE + 0x23, 2);
    EXPECT_EQ(FlagGet(0x20), FALSE);
    EXPECT_EQ(FlagGet(KANTO_FLAG_BASE + 0x20), TRUE);
    EXPECT_EQ(VarGet(0x4023), 1);
    EXPECT_EQ(VarGet(KANTO_VAR_BASE + 0x23), 2);
    if (oldFlag) FlagSet(0x20); else FlagClear(0x20);
    VarSet(0x4023, oldVar);
    *gSaveBlock3Ptr = previous;
}
TEST("Kanto progress persists in memory without being reinitialized on another access")
{
    struct SaveBlock3 previous = *gSaveBlock3Ptr;
    FlagSet(KANTO_FLAG_LIMIT - 1);
    VarSet(KANTO_VAR_LIMIT - 1, 65535);
    EXPECT(KantoProgress_EnsureInitialized());
    EXPECT_EQ(FlagGet(KANTO_FLAG_LIMIT - 1), TRUE);
    EXPECT_EQ(VarGet(KANTO_VAR_LIMIT - 1), 65535);
    FlagClear(KANTO_FLAG_LIMIT - 1);
    EXPECT_EQ(FlagGet(KANTO_FLAG_LIMIT - 1), FALSE);
    *gSaveBlock3Ptr = previous;
}
TEST("Invalid Kanto bank IDs never fall through into unrelated save or testing memory")
{
    EXPECT_EQ(KantoProgress_GetFlagPointer(KANTO_FLAG_BASE), NULL);
    EXPECT_EQ(GetFlagPointer(KANTO_FLAG_LIMIT), NULL);
    EXPECT_EQ(GetFlagPointer(KANTO_FLAG_BASE + 0xFFF), NULL);
    EXPECT_EQ(GetVarPointer(KANTO_VAR_LIMIT), NULL);
    EXPECT_EQ(GetVarPointer(KANTO_VAR_BASE + 0xFFF), NULL);
}
TEST("Kanto Brock resolves to his original party without aliasing a Hoenn or partner trainer")
{
    const struct Trainer *trainer = GetTrainerStructFromId(KANTO_TRAINER_LEADER_BROCK);
    EXPECT_EQ(trainer->partySize, 2);
    EXPECT_EQ(trainer->party[0].species, SPECIES_GEODUDE);
    EXPECT_EQ(trainer->party[0].lvl, 12);
    EXPECT_EQ(trainer->party[1].species, SPECIES_ONIX);
    EXPECT_EQ(trainer->party[1].lvl, 14);
    EXPECT_EQ(IsPartnerTrainerId(KANTO_TRAINER_LEADER_BROCK), FALSE);
    EXPECT_EQ(IsKantoTrainerId(KANTO_TRAINER_BASE), FALSE);
    EXPECT_EQ(IsKantoTrainerId(KANTO_TRAINER_BASE + KANTO_TRAINER_COUNT), FALSE);
}
TEST("Kanto trainer defeat helpers preserve the corresponding Hoenn trainer flag")
{
    struct SaveBlock3 previous = *gSaveBlock3Ptr;
    u16 nativeId = KANTO_TRAINER_LEADER_BROCK - KANTO_TRAINER_BASE;
    bool32 old = HasTrainerBeenFought(nativeId);
    ClearTrainerFlag(nativeId);
    SetTrainerFlag(KANTO_TRAINER_LEADER_BROCK);
    EXPECT(HasTrainerBeenFought(KANTO_TRAINER_LEADER_BROCK));
    EXPECT(FlagGet(KANTO_FLAG_BASE + KANTO_NATIVE_TRAINER_FLAG_BASE + nativeId));
    EXPECT_EQ(HasTrainerBeenFought(nativeId), FALSE);
    ClearTrainerFlag(KANTO_TRAINER_LEADER_BROCK);
    if (old) SetTrainerFlag(nativeId);
    *gSaveBlock3Ptr = previous;
}
#endif
