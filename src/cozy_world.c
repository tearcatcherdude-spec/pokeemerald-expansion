#include "global.h"
#include "cozy_world.h"
#include "pip.h"
#include "pokemon.h"
#include "battle.h"
#include "event_data.h"
#include "script_pokemon_util.h"
#include "constants/items.h"

#if !IS_FRLG
static const struct CozyRareDefinition sRareEncounters[] = {
    {SPECIES_SENTRET, 5, {6, 252, 0, 252, 0, 0}},
    {SPECIES_SHINX, 7, {6, 252, 0, 252, 0, 0}},
    {SPECIES_EEVEE, 10, {6, 252, 0, 252, 0, 0}},
    {SPECIES_MAREEP, 12, {252, 0, 0, 6, 252, 0}},
    {SPECIES_RIOLU, 15, {6, 252, 0, 252, 0, 0}},
    {SPECIES_TOGEPI, 17, {252, 0, 252, 0, 0, 6}},
    {SPECIES_WOOPER, 18, {252, 0, 252, 0, 0, 6}},
    {SPECIES_HOUNDOUR, 23, {6, 0, 0, 252, 252, 0}},
    {SPECIES_GIBLE, 25, {6, 252, 0, 252, 0, 0}},
    {SPECIES_MUNCHLAX, 26, {252, 252, 6, 0, 0, 0}},
    {SPECIES_DRATINI, 29, {6, 252, 0, 252, 0, 0}},
    {SPECIES_CROAGUNK, 32, {6, 252, 0, 252, 0, 0}},
    {SPECIES_PORYGON, 33, {252, 0, 0, 6, 252, 0}},
    {SPECIES_ELEKID, 35, {6, 252, 0, 252, 0, 0}},
    {SPECIES_LARVITAR, 38, {6, 252, 0, 252, 0, 0}},
    {SPECIES_DEINO, 42, {6, 252, 0, 252, 0, 0}},
#include "data/kanto_rare_definitions.h"
};
extern const u8 World_Pip_0[];
extern const u8 World_Pip_1[];
extern const u8 World_Pip_2[];
extern const u8 World_Pip_3[];
extern const u8 World_Pip_4[];
extern const u8 World_Pip_5[];
extern const u8 World_Pip_6[];
extern const u8 World_Pip_7[];
extern const u8 World_Pip_8[];
extern const u8 World_Pip_9[];
extern const u8 World_Pip_10[];
extern const u8 World_Pip_11[];
extern const u8 World_Pip_12[];
extern const u8 World_Pip_13[];
extern const u8 World_Pip_14[];
extern const u8 World_Pip_15[];
extern const u8 World_Pip_16[];
extern const u8 World_Pip_17[];
extern const u8 World_Pip_18[];
extern const u8 World_Pip_19[];
extern const u8 World_Pip_20[];
extern const u8 World_Pip_21[];
extern const u8 World_Pip_22[];
extern const u8 World_Pip_23[];
extern const u8 World_Pip_24[];
extern const u8 World_Pip_25[];
extern const u8 World_Pip_26[];
extern const u8 World_Pip_27[];
extern const u8 World_Pip_28[];
extern const u8 World_Pip_29[];
extern const u8 World_Pip_30[];
extern const u8 World_Pip_31[];
extern const u8 World_Pip_32[];
extern const u8 World_Pip_33[];
extern const u8 World_Pip_34[];
extern const u8 World_Pip_35[];
extern const u8 World_Pip_36[];
static const u8 *const sScenePipLines[] = {
    World_Pip_0,
    World_Pip_1,
    World_Pip_2,
    World_Pip_3,
    World_Pip_4,
    World_Pip_5,
    World_Pip_6,
    World_Pip_7,
    World_Pip_8,
    World_Pip_9,
    World_Pip_10,
    World_Pip_11,
    World_Pip_12,
    World_Pip_13,
    World_Pip_14,
    World_Pip_15,
    World_Pip_16,
    World_Pip_17,
    World_Pip_18,
    World_Pip_19,
    World_Pip_20,
    World_Pip_21,
    World_Pip_22,
    World_Pip_23,
    World_Pip_24,
    World_Pip_25,
    World_Pip_26,
    World_Pip_27,
    World_Pip_28,
    World_Pip_29,
    World_Pip_30,
    World_Pip_31,
    World_Pip_32,
    World_Pip_33,
    World_Pip_34,
    World_Pip_35,
    World_Pip_36,
};
#endif

u32 CozyWorld_RareCount(void)
{
#if !IS_FRLG
    return ARRAY_COUNT(sRareEncounters);
#else
    return 0;
#endif
}
const struct CozyRareDefinition *CozyWorld_GetRare(u32 index)
{
#if !IS_FRLG
    if (index < ARRAY_COUNT(sRareEncounters))
        return &sRareEncounters[index];
#endif
    return NULL;
}
static bool32 TrainRare(const struct CozyRareDefinition *entry)
{
    static const u8 ivFields[] = {MON_DATA_HP_IV, MON_DATA_ATK_IV, MON_DATA_DEF_IV, MON_DATA_SPEED_IV, MON_DATA_SPATK_IV, MON_DATA_SPDEF_IV};
    static const u8 evFields[] = {MON_DATA_HP_EV, MON_DATA_ATK_EV, MON_DATA_DEF_EV, MON_DATA_SPEED_EV, MON_DATA_SPATK_EV, MON_DATA_SPDEF_EV};
    u8 iv = 31;
    if (entry == NULL)
        return FALSE;
    for (u32 i = 0; i < ARRAY_COUNT(ivFields); i++)
    {
        SetMonData(&gParties[B_TRAINER_OPPONENT_A][0], ivFields[i], &iv);
        SetMonData(&gParties[B_TRAINER_OPPONENT_A][0], evFields[i], &entry->evs[i]);
    }
    CalculateMonStats(&gParties[B_TRAINER_OPPONENT_A][0]);
    return TRUE;
}
bool32 CozyWorld_CreateRare(u32 index)
{
    const struct CozyRareDefinition *entry = CozyWorld_GetRare(index);
    if (entry == NULL)
        return FALSE;
    CreateScriptedWildMon(entry->species, entry->level, ITEM_NONE);
    return TrainRare(entry);
}
void Script_CozyWorldTrainRare(struct ScriptContext *ctx)
{
    const struct CozyRareDefinition *entry = CozyWorld_GetRare(gSpecialVar_0x8004);
    gSpecialVar_Result = entry != NULL && TrainRare(entry);
}
void Script_CozyWorldPrepareRare(struct ScriptContext *ctx)
{
    gSpecialVar_Result = FALSE;
    for (u32 i = 0; i < PARTY_SIZE; i++)
        if (GetMonData(&gParties[B_TRAINER_PLAYER][i], MON_DATA_SPECIES) != SPECIES_NONE
         && !GetMonData(&gParties[B_TRAINER_PLAYER][i], MON_DATA_IS_EGG)
         && GetMonData(&gParties[B_TRAINER_PLAYER][i], MON_DATA_HP) != 0)
        {
            gSpecialVar_Result = CozyWorld_GetRare(gSpecialVar_0x8004) != NULL;
            return;
        }
}
void Script_CozyWorldPipReaction(struct ScriptContext *ctx)
{
    gSpecialVar_Result = FALSE;
#if !IS_FRLG
    if (gSpecialVar_0x8004 < ARRAY_COUNT(sScenePipLines))
        gSpecialVar_Result = Pip_TrySay(sScenePipLines[gSpecialVar_0x8004]);
#endif
}
