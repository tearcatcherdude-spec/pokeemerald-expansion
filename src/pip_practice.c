#include "global.h"
#include "pip.h"
#include "cast.h"
#include "pokemon.h"
#include "battle.h"
#include "battle_setup.h"
#include "trainer_see.h"
#include "script.h"
#include "script_menu.h"
#include "event_data.h"
#include "string_util.h"
#include "constants/kanto_symbols.h"

#if FNPC_ENABLE_NPC_FOLLOWERS && !IS_FRLG
static EWRAM_DATA u8 sPreviewBand = 0;
static u32 PracticeBand(void)
{
    u32 i, hoenn = 0, kanto = 0;
    for (i = 0; i < 8; i++)
    {
        u32 flag = FLAG_BADGE01_GET + i;
        hoenn += !!(gSaveBlock1Ptr->flags[flag / 8] & (1 << (flag % 8)));
        kanto += !!FlagGet(KANTO_FLAG_BADGE01_GET + i);
    }
    i = max(hoenn, kanto);
    return i >= 7 ? 3 : i >= 4 ? 2 : i >= 2 ? 1 : 0;
}
static bool32 Ready(void)
{
    u32 i;
    if (!Pip_IsFollowing() || Cast_Active()) return FALSE;
    for (i = 0; i < gPartiesCount[B_TRAINER_PLAYER]; i++)
        if (GetMonData(&gParties[B_TRAINER_PLAYER][i], MON_DATA_HP)
         && !GetMonData(&gParties[B_TRAINER_PLAYER][i], MON_DATA_IS_EGG)) return TRUE;
    return FALSE;
}
#endif

void Script_PipPracticeRootMenu(struct ScriptContext *ctx)
{
    static const struct MenuAction items[] = {
        {COMPOUND_STRING("Talk")}, {COMPOUND_STRING("Head home")},
        {COMPOUND_STRING("Change company")}, {COMPOUND_STRING("Keep walking")},
        {COMPOUND_STRING("Companion Journal")}, {COMPOUND_STRING("Dialogue setting")},
        {COMPOUND_STRING("Practice battle")},
    };
    gSpecialVar_Result = 0xFF;
    DrawMultichoiceMenuInternal(0, 0, MULTI_PIP_COMPANION, FALSE, 0, items, ARRAY_COUNT(items));
}

void Script_PipPracticePreview(struct ScriptContext *ctx)
{
    gSpecialVar_Result = FALSE;
#if FNPC_ENABLE_NPC_FOLLOWERS && !IS_FRLG
    if (!Ready())
    {
        StringCopy(gStringVar4, COMPOUND_STRING("PIP: Bring a healthy POKEMON for\npractice. I will wait right here.$"));
        return;
    }
    sPreviewBand = PracticeBand();
    switch (sPreviewBand)
    {
    case 0: StringCopy(gStringVar1, COMPOUND_STRING("8")); break;
    case 1: StringCopy(gStringVar1, COMPOUND_STRING("18")); break;
    case 2: StringCopy(gStringVar1, COMPOUND_STRING("32")); break;
    default: StringCopy(gStringVar1, COMPOUND_STRING("48")); break;
    }
    StringExpandPlaceholders(gStringVar4, COMPOUND_STRING("PIP: Four POKEMON, level {STR_VAR_1}.\nA friendly practice battle.\pYour team is healed afterwards.\nItems you use are still used.\pWant to give it a try?$"));
    gSpecialVar_Result = TRUE;
#endif
}

void Script_PipPracticeStart(struct ScriptContext *ctx)
{
    gSpecialVar_Result = FALSE;
#if FNPC_ENABLE_NPC_FOLLOWERS && !IS_FRLG
    if (!Ready() || sPreviewBand != PracticeBand()) return;
    memset(&gTrainerBattleParameter, 0, sizeof(gTrainerBattleParameter));
    TRAINER_BATTLE_PARAM.opponentA = KANTO_TRAINER_BASE + 738 + sPreviewBand;
    TRAINER_BATTLE_PARAM.earlyRival = TRUE;
    TRAINER_BATTLE_PARAM.skipFlagCheck = TRUE;
    TRAINER_BATTLE_PARAM.rivalBattleFlags = RIVAL_BATTLE_HEAL_AFTER;
    TRAINER_BATTLE_PARAM.defeatTextA = (u8 *)COMPOUND_STRING("My glasses predicted none of that!$");
    TRAINER_BATTLE_PARAM.victoryText = (u8 *)COMPOUND_STRING("Good practice. We can try again\nwhenever you feel like it.$");
    gNoOfApproachingTrainers = 1;
    gSpecialVar_Result = TRUE;
#endif
}
