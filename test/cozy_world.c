#include "global.h"
#include "battle.h"
#include "cozy_world.h"
#include "pokemon.h"
#include "event_data.h"
#include "test/test.h"

#if !IS_FRLG
TEST("Hoenn and Kanto rare encounters have perfect IVs and legal tailored full EVs")
{
    struct Pokemon oldEnemy[PARTY_SIZE];
    u8 oldCount = gPartiesCount[B_TRAINER_OPPONENT_A];
    memcpy(oldEnemy, gParties[B_TRAINER_OPPONENT_A], sizeof(oldEnemy));
    static const u8 ivFields[] = {MON_DATA_HP_IV, MON_DATA_ATK_IV, MON_DATA_DEF_IV, MON_DATA_SPEED_IV, MON_DATA_SPATK_IV, MON_DATA_SPDEF_IV};
    static const u8 evFields[] = {MON_DATA_HP_EV, MON_DATA_ATK_EV, MON_DATA_DEF_EV, MON_DATA_SPEED_EV, MON_DATA_SPATK_EV, MON_DATA_SPDEF_EV};
    EXPECT_EQ(CozyWorld_RareCount(), 32);
    for (u32 i = 0; i < CozyWorld_RareCount(); i++)
    {
        const struct CozyRareDefinition *entry = CozyWorld_GetRare(i);
        EXPECT_EQ(CozyWorld_CreateRare(i), TRUE);
        struct Pokemon *mon = &gParties[B_TRAINER_OPPONENT_A][0];
        EXPECT_EQ(GetMonData(mon, MON_DATA_SPECIES), entry->species);
        EXPECT_EQ(GetMonData(mon, MON_DATA_LEVEL), entry->level);
        EXPECT(entry->level >= 5 && entry->level <= 42);
        u32 total = 0;
        for (u32 stat = 0; stat < 6; stat++)
        {
            EXPECT_EQ(GetMonData(mon, ivFields[stat]), 31);
            EXPECT_EQ(GetMonData(mon, evFields[stat]), entry->evs[stat]);
            EXPECT(entry->evs[stat] <= 252);
            total += entry->evs[stat];
        }
        EXPECT_EQ(total, 510);
        EXPECT(GetMonData(mon, MON_DATA_HP) > 0);
    }
    memcpy(gParties[B_TRAINER_OPPONENT_A], oldEnemy, sizeof(oldEnemy));
    gPartiesCount[B_TRAINER_OPPONENT_A] = oldCount;
}
TEST("Invalid living-world encounter IDs cannot overwrite the enemy party")
{
    struct Pokemon oldEnemy[PARTY_SIZE];
    u8 oldCount = gPartiesCount[B_TRAINER_OPPONENT_A];
    memcpy(oldEnemy, gParties[B_TRAINER_OPPONENT_A], sizeof(oldEnemy));
    EXPECT_EQ(CozyWorld_GetRare(0xFFFF), NULL);
    EXPECT_EQ(CozyWorld_CreateRare(0xFFFF), FALSE);
    EXPECT_EQ(memcmp(oldEnemy, gParties[B_TRAINER_OPPONENT_A], sizeof(oldEnemy)), 0);
    gPartiesCount[B_TRAINER_OPPONENT_A] = oldCount;
}
TEST("Living-world encounters refuse a battle when the player has no healthy team")
{
    struct Pokemon oldParty[PARTY_SIZE];
    memcpy(oldParty, gParties[B_TRAINER_PLAYER], sizeof(oldParty));
    u16 oldResult = gSpecialVar_Result;
    u16 oldIndex = gSpecialVar_0x8004;
    memset(gParties[B_TRAINER_PLAYER], 0, sizeof(oldParty));
    gSpecialVar_0x8004 = 0;
    Script_CozyWorldPrepareRare(NULL);
    EXPECT_EQ(gSpecialVar_Result, FALSE);
    memcpy(gParties[B_TRAINER_PLAYER], oldParty, sizeof(oldParty));
    gSpecialVar_Result = oldResult;
    gSpecialVar_0x8004 = oldIndex;
}
#endif
