#include "global.h"
#include "companion_dialogue.h"
#include "companion_packed_text.h"
#include "pokemon_storage_system.h"
#include "pip.h"
#include "cast.h"
#include "bonds.h"
#include "script.h"
#include "event_data.h"
#include "string_util.h"

#if FNPC_ENABLE_NPC_FOLLOWERS && !IS_FRLG

#define DIALOGUE_MAGIC 0x474C4443
#define NO_CONTEXT COMPANION_NO_CONTEXT

struct ContextReply { u32 packed; u8 expression; };
struct ContextMessage { const u8 *message; u16 context; };
#include "data/companion_contexts.h"

// Read-only catalogue metadata for compiled-data validation and future loaders.
const struct { u32 magic, version; const void *replies; u32 contexts, voices, entrySize; }
gCompanionPackedCatalogue = {0x50435458, 1, sContextReplies, ARRAY_COUNT(sContextReplies), COMPANION_VOICE_COUNT, sizeof(struct ContextReply)};

extern const u8 Cozy_EventScript_Companion[], Cast_EventScript_Companion[];
extern const u8 CompanionDialogue_EventScript_React[];
extern const u8 gText_ObtainedTheItem[];
extern const u8 gText_ObtainedTheItems[];
extern const u8 gText_PutItemInPocket[];
extern const u8 gText_PlayerPutItemInBag[];
extern const u8 gText_ObtainedTheDecor[];
extern const u8 gText_TheDecorWasTransferredToThePC[];
extern const u8 gText_PlayerFoundOneItem[];
extern const u8 gText_PlayerFoundItems[];
extern const u8 gText_RegisteredTrainerinPokeNav[];
extern const u8 PewterCity_Museum_1F_Text_ReceivedOldAmberFromMan[];
extern const u8 CeladonCity_Restaurant_Text_ReceivedCoinCaseFromMan[];
extern const u8 CeladonCity_GameCorner_Text_Received10CoinsFromMan[];
extern const u8 CeladonCity_GameCorner_Text_Received20CoinsFromNiceGuy[];
extern const u8 CeladonCity_GameCorner_Text_Received20CoinsFromMan[];
extern const u8 TwoIsland_JoyfulGameCorner_Text_ReceivedMoonStoneFromLostellesDaddy[];
extern const u8 RustboroCity_Gym_Text_RegisteredRoxanne[];
extern const u8 DewfordTown_Gym_Text_RegisteredBrawly[];
extern const u8 MauvilleCity_Gym_Text_RegisteredWattson[];
extern const u8 LavaridgeTown_Gym_1F_Text_RegisteredFlannery[];
extern const u8 FortreeCity_Gym_Text_RegisteredWinona[];
extern const u8 MossdeepCity_Gym_Text_RegisteredTateAndLiza[];
extern const u8 SootopolisCity_Gym_1F_Text_RegisteredJuan[];

extern const u8 PlayersHouse_1F_Text_RegisteredMom[];
extern const u8 MatchCall_Text_RegisteredBirch[];
extern const u8 FuchsiaCity_WardensHouse_Text_ReceivedHM04FromWarden[];

extern const u8 FourIsland_House2_Text_HoFStickerApplied[];
extern const u8 FourIsland_House2_Text_EggStickerApplied[];
extern const u8 FourIsland_House2_Text_VictoryStickerApplied[];

extern const u8 SlateportCity_Text_ReceivedEffortRibbon[];
extern const u8 SlateportCity_Text_PutEffortRibbonOnMon[];

extern const u8 LavaridgeTown_Text_ReceivedTheEgg[];

static EWRAM_DATA bool8 sActive = FALSE;
static EWRAM_DATA bool8 sOffering = FALSE;
static EWRAM_DATA bool8 sFinishPending = FALSE;
static EWRAM_DATA bool8 sHasRecent = FALSE;
static EWRAM_DATA bool8 sSawMessage = FALSE;
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
    sSawMessage = FALSE;
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
        p->version = 2;
        u32 count = min(ARRAY_COUNT(sContextReplies), COMPANION_CONTEXT_CAPACITY);
        p->reserved[0] = count;
        p->reserved[1] = count >> 8;
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
        p->version = 2;
    }
    if (p != NULL && p->version <= 2)
    {
        // Import released object history once for each appended context. New
        // observations thereafter spend their OWN context, not a broad legacy
        // category shared by several different object descriptions.
        u32 first = p->reserved[0] | (p->reserved[1] << 8);
        u32 limit = min(ARRAY_COUNT(sContextReplies), COMPANION_CONTEXT_CAPACITY);
        if (first < limit)
        {
            for (u32 i = 0; i < ARRAY_COUNT(sContextMessages); i++)
            {
                u32 id = sContextMessages[i].context;
                if (id >= first && id < limit)
                {
                    const u8 *legacy = Pip_GetExactObjectReaction(sContextMessages[i].message);
                    if (legacy != NULL)
                        for (u32 voice = 0; voice < COMPANION_VOICE_COUNT; voice++)
                            if (Pip_HasOfferedByVoice(legacy, voice))
                                p->spent[voice][id / 8] |= 1 << (id % 8);
                }
            }
            p->reserved[0] = limit;
            p->reserved[1] = limit >> 8;
        }
        p->version = 2;
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
bool32 CompanionDialogue_IsSystemReceipt(const u8 *message)
{
    // These are success notifications, not a new person speaking. In
    // particular, a bag-full error is NOT a receipt and must invalidate an
    // earlier gift offer rather than let us react as though it succeeded.
    static const u8 *const receipts[] = {
        gText_ObtainedTheItem, gText_ObtainedTheItems, gText_PutItemInPocket,
        gText_PlayerPutItemInBag, gText_ObtainedTheDecor,
        gText_TheDecorWasTransferredToThePC, gText_PlayerFoundOneItem,
        gText_PlayerFoundItems, gText_RegisteredTrainerinPokeNav,
        // Imported custom success notices have the same role as the generic
        // receipts. Their callers check space/coin capacity before displaying
        // them; failure messages remain ordinary candidate-invalidating text.
        PewterCity_Museum_1F_Text_ReceivedOldAmberFromMan,
        CeladonCity_Restaurant_Text_ReceivedCoinCaseFromMan,
        CeladonCity_GameCorner_Text_Received10CoinsFromMan,
        CeladonCity_GameCorner_Text_Received20CoinsFromNiceGuy,
        CeladonCity_GameCorner_Text_Received20CoinsFromMan,
        TwoIsland_JoyfulGameCorner_Text_ReceivedMoonStoneFromLostellesDaddy,
        RustboroCity_Gym_Text_RegisteredRoxanne,
        DewfordTown_Gym_Text_RegisteredBrawly,
        MauvilleCity_Gym_Text_RegisteredWattson,
        LavaridgeTown_Gym_1F_Text_RegisteredFlannery,
        FortreeCity_Gym_Text_RegisteredWinona,
        MossdeepCity_Gym_Text_RegisteredTateAndLiza,
        SootopolisCity_Gym_1F_Text_RegisteredJuan,
        PlayersHouse_1F_Text_RegisteredMom,
        MatchCall_Text_RegisteredBirch,
        FuchsiaCity_WardensHouse_Text_ReceivedHM04FromWarden,
        FourIsland_House2_Text_HoFStickerApplied,
        FourIsland_House2_Text_EggStickerApplied,
        FourIsland_House2_Text_VictoryStickerApplied,
        SlateportCity_Text_ReceivedEffortRibbon,
        SlateportCity_Text_PutEffortRibbonOnMon,
        LavaridgeTown_Text_ReceivedTheEgg,
    };
    for (u32 i = 0; i < ARRAY_COUNT(receipts); i++)
        if (message == receipts[i])
            return TRUE;
    return FALSE;
}
void CompanionDialogue_RecordMessage(struct ScriptContext *ctx, const u8 *message)
{
    if (ScriptContext_IsGlobal(ctx))
        CompanionDialogue_RecordNativeMessage(message);
}
void CompanionDialogue_RecordNativeMessage(const u8 *message)
{
    if (sActive && !sOffering)
    {
        // A standalone pickup can speak for itself. Once any NPC/dynamic text
        // has appeared, even unknown text, receipts must preserve that subject
        // rather than turn an unreviewed conversation into a generic gift line.
        if (!CompanionDialogue_IsSystemReceipt(message) || !sSawMessage)
        {
            sMessage = message;
            sSawMessage = TRUE;
        }
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
    if (voice >= COMPANION_VOICE_COUNT || Progress() == NULL || Progress()->version > 2)
        return TRUE;
    if (context >= COMPANION_CONTEXT_CAPACITY)
    {
        if (CompanionHistory_HasSpent(voice, context))
            return TRUE;
    }
    else if ((Progress()->spent[voice][context / 8] & (1 << (context % 8))) != 0)
        return TRUE;
    return FALSE;
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
        if (sContext >= COMPANION_CONTEXT_CAPACITY)
        {
            if (!CompanionHistory_Spend(sVoice, sContext))
                return FALSE;
        }
        else
            Progress()->spent[sVoice][sContext / 8] |= 1 << (sContext % 8);
        return TRUE;
    }
    return sLegacy != NULL && Pip_TryOfferExact(sLegacy);
}
bool32 CompanionDialogue_CopyCatalogReply(u32 context, u32 voice, u8 *destination, u32 capacity, u8 *expression)
{
    const struct ContextReply *reply;
    if (context >= ARRAY_COUNT(sContextReplies) || voice >= COMPANION_VOICE_COUNT) return FALSE;
    reply = &sContextReplies[context][voice];
    if (!CompanionPackedText_Copy(reply->packed, destination, capacity)) return FALSE;
    if (expression) *expression = reply->expression;
    return TRUE;
}

static bool32 Say(void)
{
    if (!SameSituation())
        return FALSE;
    if (sContext < ARRAY_COUNT(sContextReplies))
    {
        u8 expression;
        if (!CompanionDialogue_CopyCatalogReply(sContext, sVoice, gStringVar4, sizeof(gStringVar4), &expression))
            return FALSE;
        Cast_ClearPending(); // The new text supersedes any legacy offer payload.
        // ShowPortrait cancels old pending EXP; queue this observation after it.
        if (sVoice != 0)
            Cast_ShowPortrait(sVoice - 1, expression);
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
bool32 CompanionDialogue_CopyCatalogReply(u32 context, u32 voice, u8 *destination, u32 capacity, u8 *expression) { return FALSE; }
// This project feature belongs to Emerald. Keep the upstream alternate targets
// buildable without linking Emerald-only cast, map or text symbols.
void CompanionDialogue_Reset(void) {}
u32 CompanionDialogue_GetMode(void) { return COMPANION_DIALOGUE_NORMAL; }
bool32 CompanionDialogue_SetMode(u32 mode) { return FALSE; }
void CompanionDialogue_BeginInteraction(const u8 *script) {}
void CompanionDialogue_RecordMessage(struct ScriptContext *ctx, const u8 *message) {}
void CompanionDialogue_RecordNativeMessage(const u8 *message) {}
bool32 CompanionDialogue_FinishInteraction(struct ScriptContext *ctx) { return FALSE; }
void CompanionDialogue_AfterScript(void) {}
bool32 CompanionDialogue_IsInteractionActive(void) { return FALSE; }
void CompanionDialogue_ResetSession(void) {}
u32 CompanionDialogue_TryManualTalk(void) { return 0; }
void Script_CompanionDialogueChoose(struct ScriptContext *ctx) {}
void Script_CompanionDialogueRestore(struct ScriptContext *ctx) {}
void Script_CompanionDialogueSetMode(struct ScriptContext *ctx) {}
void Script_CompanionDialogueBufferMode(struct ScriptContext *ctx) {}
u32 CompanionDialogue_ContextForMessage(const u8 *message) { return COMPANION_NO_CONTEXT; }
bool32 CompanionDialogue_IsSystemReceipt(const u8 *message) { return FALSE; }
bool32 CompanionDialogue_HasSpent(u32 voice, u32 context) { return TRUE; }
#endif
