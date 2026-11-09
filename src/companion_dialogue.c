#include "global.h"
#include "companion_dialogue.h"
#include "pokemon_storage_system.h"
#include "pip.h"
#include "cast.h"
#include "bonds.h"
#include "script.h"
#include "event_data.h"
#include "string_util.h"

#if FNPC_ENABLE_NPC_FOLLOWERS && !IS_FRLG

#define DIALOGUE_MAGIC 0x474C4443
#define NO_CONTEXT COMPANION_CONTEXT_CAPACITY

struct ContextReply { const u8 *text; u8 expression; };
struct ContextMessage { const u8 *message; u16 context; };
#include "data/companion_contexts.h"

extern const u8 Cozy_EventScript_Companion[], Cast_EventScript_Companion[];
extern const u8 CompanionDialogue_EventScript_React[];

static EWRAM_DATA bool8 sActive = FALSE;
static EWRAM_DATA bool8 sOffering = FALSE;
static EWRAM_DATA bool8 sFinishPending = FALSE;
static EWRAM_DATA bool8 sHasRecent = FALSE;
static EWRAM_DATA u8 sGroup = 0, sMap = 0, sVoice = 0;
static EWRAM_DATA u16 sContext = 0; // ResetSession installs the sentinel.
static EWRAM_DATA const u8 *sMessage = NULL;
static EWRAM_DATA const u8 *sLegacy = NULL;
static EWRAM_DATA u16 sResult = 0, sLastTalked = 0;
static EWRAM_DATA u8 sComparison = 0;
static EWRAM_DATA u32 sData[4] = {0};
static EWRAM_DATA u8 sText[sizeof(gStringVar4)] = {0};
static EWRAM_DATA u8 sSpeaker[sizeof(gStringVar1)] = {0};

static struct CompanionDialogueProgress *Progress(void)
{
    return gPokemonStoragePtr == NULL ? NULL : &gPokemonStoragePtr->companionDialogue;
}
void CompanionDialogue_ResetSession(void)
{
    sActive = sOffering = sHasRecent = sFinishPending = FALSE;
    sContext = NO_CONTEXT;
    sMessage = sLegacy = NULL;
}
void CompanionDialogue_Reset(void)
{
    struct CompanionDialogueProgress *p = Progress();
    if (p != NULL)
    {
        memset(p, 0, sizeof(*p));
        p->magic = DIALOGUE_MAGIC;
        p->version = 1;
    }
    CompanionDialogue_ResetSession();
}
static void EnsureInitialized(void)
{
    struct CompanionDialogueProgress *p = Progress();
    if (p != NULL && (p->magic != DIALOGUE_MAGIC || p->version == 0))
    {
        // Initialize only the appended suffix, never the released history.
        memset(p, 0, sizeof(*p));
        p->magic = DIALOGUE_MAGIC;
        p->version = 1;
    }
}
u32 CompanionDialogue_GetMode(void)
{
    EnsureInitialized();
    struct CompanionDialogueProgress *p = Progress();
    return p == NULL || p->mode > COMPANION_DIALOGUE_SILENT ? COMPANION_DIALOGUE_NORMAL : p->mode;
}
bool32 CompanionDialogue_SetMode(u32 mode)
{
    EnsureInitialized();
    if (Progress() == NULL || mode > COMPANION_DIALOGUE_SILENT)
        return FALSE;
    Progress()->mode = mode;
    CompanionDialogue_ResetSession();
    Cast_ClearPending();
    return TRUE;
}
bool32 CompanionDialogue_IsInteractionActive(void)
{
    return sActive || sOffering;
}
static u32 Voice(void)
{
    return Cast_IsFollowing() ? Cast_Active() : 0;
}
void CompanionDialogue_BeginInteraction(const u8 *script)
{
    // Talking to a companion must retain the most recent subject for Ask mode.
    if (script == Cozy_EventScript_Companion || script == Cast_EventScript_Companion)
        return;
    CompanionDialogue_ResetSession();
    if (!Pip_IsFollowing() || CompanionDialogue_GetMode() == COMPANION_DIALOGUE_SILENT)
        return;
    sActive = sHasRecent = TRUE;
    sGroup = gSaveBlock1Ptr->location.mapGroup;
    sMap = gSaveBlock1Ptr->location.mapNum;
    sVoice = Voice();
}
void CompanionDialogue_RecordMessage(struct ScriptContext *ctx, const u8 *message)
{
    if (sActive && !sOffering && ScriptContext_IsGlobal(ctx))
    {
        // Always replace, including unknown/dynamic messages: do not react to
        // an earlier branch after the NPC has gone on to say something else.
        sMessage = message;
    }
}
u32 CompanionDialogue_ContextForMessage(const u8 *message)
{
    if (message != NULL)
        for (u32 i = 0; i < ARRAY_COUNT(sContextMessages); i++)
            if (sContextMessages[i].message == message)
                return sContextMessages[i].context;
    return NO_CONTEXT;
}
bool32 CompanionDialogue_HasSpent(u32 voice, u32 context)
{
    EnsureInitialized();
    return voice >= COMPANION_VOICE_COUNT || context >= COMPANION_CONTEXT_CAPACITY
        || Progress() == NULL
        || (Progress()->spent[voice][context / 8] & (1 << (context % 8))) != 0;
}
static bool32 SameSituation(void)
{
    return Pip_IsFollowing() && !Pip_IsSceneSuspended() && sVoice == Voice()
        && sGroup == gSaveBlock1Ptr->location.mapGroup
        && sMap == gSaveBlock1Ptr->location.mapNum;
}
static bool32 Offer(void)
{
    if (!SameSituation())
        return FALSE;
    if (sContext < ARRAY_COUNT(sContextReplies))
    {
        if (CompanionDialogue_HasSpent(sVoice, sContext))
            return FALSE;
        Progress()->spent[sVoice][sContext / 8] |= 1 << (sContext % 8);
        return TRUE;
    }
    return sLegacy != NULL && Pip_TryOfferExact(sLegacy);
}
static bool32 Say(void)
{
    if (!SameSituation())
        return FALSE;
    if (sContext < ARRAY_COUNT(sContextReplies))
    {
        const struct ContextReply *reply = &sContextReplies[sContext][sVoice];
        if (reply->text == NULL)
            return FALSE;
        // ShowPortrait cancels old pending EXP; queue this observation after it.
        if (sVoice != 0)
            Cast_ShowPortrait(sVoice - 1, reply->expression);
        StringCopy(gStringVar4, reply->text);
        if (sVoice != 0)
        {
            if (gSaveBlock3Ptr->cast.spoken[sVoice - 1] < 255)
                gSaveBlock3Ptr->cast.spoken[sVoice - 1]++;
            Bonds_QueueObservation(sVoice - 1, FALSE);
        }
        return TRUE;
    }
    return sLegacy != NULL && Pip_TrySay(sLegacy);
}
bool32 CompanionDialogue_FinishInteraction(struct ScriptContext *ctx)
{
    if (!sActive || !ScriptContext_IsGlobal(ctx))
        return FALSE;
    sActive = FALSE;
    sContext = CompanionDialogue_ContextForMessage(sMessage);
    sLegacy = Pip_GetExactObjectReaction(sMessage);
    if (CompanionDialogue_GetMode() != COMPANION_DIALOGUE_NORMAL
     || (sContext >= ARRAY_COUNT(sContextReplies) && sLegacy == NULL))
        return FALSE;
    sFinishPending = TRUE;
    sResult = gSpecialVar_Result;
    sLastTalked = gSpecialVar_LastTalked;
    sComparison = ctx->comparisonResult;
    memcpy(sData, ctx->data, sizeof(sData));
    memcpy(sText, gStringVar4, sizeof(sText));
    memcpy(sSpeaker, gStringVar1, sizeof(sSpeaker));
    // Let the original context actually stop and the follower regroup first.
    return FALSE;
}
void CompanionDialogue_AfterScript(void)
{
    if (!sFinishPending)
        return;
    sFinishPending = FALSE;
    if (CompanionDialogue_GetMode() != COMPANION_DIALOGUE_NORMAL || !Offer())
        return;
    sHasRecent = FALSE;
    sOffering = TRUE;
    ScriptContext_SetupScript(CompanionDialogue_EventScript_React);
}
u32 CompanionDialogue_TryManualTalk(void)
{
    if (CompanionDialogue_GetMode() == COMPANION_DIALOGUE_SILENT)
        return 2;
    if (!sHasRecent || CompanionDialogue_GetMode() != COMPANION_DIALOGUE_ASK)
        return 0;
    sHasRecent = FALSE;
    if (!SameSituation() || !Offer())
        return 2;
    return Say() ? 1 : 2;
}
void Script_CompanionDialogueChoose(struct ScriptContext *ctx)
{
    gSpecialVar_Result = sOffering && Say();
}
void Script_CompanionDialogueRestore(struct ScriptContext *ctx)
{
    if (!sOffering)
        return;
    Cast_HidePortrait();
    Cast_ClearPending();
    gSpecialVar_Result = sResult;
    gSpecialVar_LastTalked = sLastTalked;
    ctx->comparisonResult = sComparison;
    memcpy(ctx->data, sData, sizeof(sData));
    memcpy(gStringVar4, sText, sizeof(sText));
    memcpy(gStringVar1, sSpeaker, sizeof(sSpeaker));
    CompanionDialogue_ResetSession();
}
void Script_CompanionDialogueSetMode(struct ScriptContext *ctx)
{
    // Cancel/B leave both the setting and memory untouched.
    CompanionDialogue_SetMode(gSpecialVar_Result);
}
void Script_CompanionDialogueBufferMode(struct ScriptContext *ctx)
{
    static const u8 normal[] = _("Dialogue: NORMAL\nRelevant reactions offer a prompt.\lChoose Only when asked to use Talk,\lor Silent to mute travel comments.$");
    static const u8 ask[] = _("Dialogue: ONLY WHEN ASKED\nTalk to your companion after an\linteraction to hear their response.\lNo automatic reaction prompts.$");
    static const u8 silent[] = _("Dialogue: SILENT\nTravel comments and Talk are muted.\lCompany, quests and the journal\lremain available.$");
    u32 mode = CompanionDialogue_GetMode();
    StringCopy(gStringVar4, mode == COMPANION_DIALOGUE_ASK ? ask : mode == COMPANION_DIALOGUE_SILENT ? silent : normal);
}

#else
// This project feature belongs to Emerald. Keep the upstream alternate targets
// buildable without linking Emerald-only cast, map or text symbols.
void CompanionDialogue_Reset(void) {}
u32 CompanionDialogue_GetMode(void) { return COMPANION_DIALOGUE_NORMAL; }
bool32 CompanionDialogue_SetMode(u32 mode) { return FALSE; }
void CompanionDialogue_BeginInteraction(const u8 *script) {}
void CompanionDialogue_RecordMessage(struct ScriptContext *ctx, const u8 *message) {}
bool32 CompanionDialogue_FinishInteraction(struct ScriptContext *ctx) { return FALSE; }
void CompanionDialogue_AfterScript(void) {}
bool32 CompanionDialogue_IsInteractionActive(void) { return FALSE; }
void CompanionDialogue_ResetSession(void) {}
u32 CompanionDialogue_TryManualTalk(void) { return 0; }
void Script_CompanionDialogueChoose(struct ScriptContext *ctx) {}
void Script_CompanionDialogueRestore(struct ScriptContext *ctx) {}
void Script_CompanionDialogueSetMode(struct ScriptContext *ctx) {}
void Script_CompanionDialogueBufferMode(struct ScriptContext *ctx) {}
u32 CompanionDialogue_ContextForMessage(const u8 *message) { return COMPANION_CONTEXT_CAPACITY; }
bool32 CompanionDialogue_HasSpent(u32 voice, u32 context) { return TRUE; }
#endif
