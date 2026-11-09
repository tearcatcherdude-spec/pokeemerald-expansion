#include "global.h"
#include "companion_dialogue.h"
#include "pip.h"
#include "cast.h"
#include "parallel_watch.h"
#include "event_data.h"
#include "event_object_movement.h"
#include "field_player_avatar.h"
#include "follower_npc.h"
#include "script.h"
#include "script_movement.h"
#include "string_util.h"
#include "constants/event_objects.h"
#include "constants/map_types.h"
#include "constants/region_map_sections.h"

#if FNPC_ENABLE_NPC_FOLLOWERS
extern const u8 Cozy_EventScript_Companion[];
extern const u8 LivingKanto_Scene0_After[];
extern const u8 LivingKanto_Scene1_After[];
extern const u8 LivingKanto_Scene2_After[];
extern const u8 LivingKanto_Scene3_After[];
extern const u8 LivingKanto_Scene4_After[];
extern const u8 LivingKanto_Scene5_After[];
extern const u8 LivingKanto_Scene6_After[];
extern const u8 LivingKanto_Scene7_After[];
extern const u8 LivingKanto_Scene8_After[];
extern const u8 LivingKanto_Scene9_After[];
extern const u8 LivingKanto_Scene10_After[];
extern const u8 LivingKanto_Scene11_After[];

extern const u8 Text_PictureBookShelf[], Text_BookShelf[], Text_PokemonCenterBookShelf[];
extern const u8 Text_Vase[], Text_EmptyTrashCan[], Text_ShopShelf[], Text_Blueprint[];
extern const u8 Cozy_Text_PictureBookShelf[], Cozy_Text_BookShelf[], Cozy_Text_Vase[];
extern const u8 Cozy_Text_EmptyTrashCan[], Cozy_Text_ShopShelf[], Cozy_Text_Blueprint[];

static EWRAM_DATA bool8 sSceneSuspended = FALSE;
static EWRAM_DATA bool8 sKantoReactionHandled = FALSE;
static EWRAM_DATA bool8 sKantoInteractionActive = FALSE;
static EWRAM_DATA u8 sKantoTalkGroup = 0;
static EWRAM_DATA u8 sKantoTalkMap = 0;
static EWRAM_DATA u8 sKantoTalkLocalId = 0;
static EWRAM_DATA u16 sSavedResult = 0;
static EWRAM_DATA u16 sSavedLastTalked = 0;
static EWRAM_DATA const u8 *sPendingReaction = NULL;
static EWRAM_DATA u32 sSavedMessage = 0;
static EWRAM_DATA bool8 sSavedTextValid = FALSE;
static EWRAM_DATA u8 sSavedText[sizeof(gStringVar4)] = {0};
static EWRAM_DATA u8 sSavedSpeaker[sizeof(gStringVar1)] = {0};

struct PipLocationDialogue
{
    u16 section;
    const u8 *lines[2];
};

#include "data/pip_dialogue.h"
#include "data/pip_living_dialogue.h"
#include "data/pip_kanto_dialogue.h"
#include "data/pip_kanto_scenes.h"
#include "data/pip_kanto_objects.h"
#include "data/pip_kanto_routes.h"
#include "data/pip_memory_catalogue.h"

static struct ObjectEvent *GetPipObject(void)
{
    u32 id = GetFollowerNPCData(FNPC_DATA_OBJ_ID);
    if (id >= OBJECT_EVENTS_COUNT || !gObjectEvents[id].active
     || gObjectEvents[id].localId != OBJ_EVENT_ID_NPC_FOLLOWER)
        return NULL;
    return &gObjectEvents[id];
}

static u32 NextComment(void)
{
    u16 counter = VarGet(VAR_PIP_COMMENT_COUNTER);
    VarSet(VAR_PIP_COMMENT_COUNTER, counter + 1);
    return counter;
}

static u32 BadgeCount(void)
{
    u32 count = 0;
    for (u32 i = 0; i < NUM_BADGES; i++)
        count += FlagGet(gBadgeFlags[i]) != 0;
    return count;
}

// Memory belongs to the save, not the current map or a rotating counter.
static void EnsureMemory(void)
{
    if (gSaveBlock3Ptr->pipMemoryVersion != 1)
    {
        memset(gSaveBlock3Ptr->pipHeard, 0, sizeof(gSaveBlock3Ptr->pipHeard));
        memset(gSaveBlock3Ptr->pipOffered, 0, sizeof(gSaveBlock3Ptr->pipOffered));
        gSaveBlock3Ptr->pipMemoryVersion = 1;
    }
}
static u32 MemoryIndex(const u8 *text)
{
    if (text != NULL)
        for (u32 i = 0; i < ARRAY_COUNT(sPipMemoryCatalogue); i++)
            if (sPipMemoryCatalogue[i] != NULL && StringCompare(text, sPipMemoryCatalogue[i]) == 0)
                return i; // Identical wording shares one canonical remembered ID.
    return ARRAY_COUNT(sPipMemoryCatalogue);
}
static const u8 *Fresh(const u8 *text)
{
    return text != NULL && !Pip_HasHeard(text) ? text : NULL;
}
static const u8 *FreshNPCOffer(const u8 *text)
{
    u32 id = MemoryIndex(text);
    EnsureMemory();
    if (id >= ARRAY_COUNT(sPipMemoryCatalogue) || Pip_HasHeard(text)
     || (!Cast_IsFollowing() && (gSaveBlock3Ptr->pipOffered[id / 8] & (1 << (id % 8)))))
        return NULL;
    return text;
}
static const u8 *FreshKantoLocationFor(bool32 npcOffer)
{
    if (!ParallelWatch_IsKanto(gSaveBlock1Ptr->location.mapGroup, gSaveBlock1Ptr->location.mapNum))
        return NULL;
    for (u32 i = 0; i < ARRAY_COUNT(sPipAdventureLocations); i++)
        if (sPipAdventureLocations[i].section == gMapHeader.regionMapSectionId)
            for (u32 j = 0; j < 2; j++)
            {
                const u8 *text = sPipAdventureLocations[i].lines[j];
                if ((npcOffer ? FreshNPCOffer(text) : Fresh(text)) != NULL)
                    return text;
            }
    for (u32 i = 0; i < ARRAY_COUNT(sPipKantoRoutes); i++)
        if (sPipKantoRoutes[i].section == gMapHeader.regionMapSectionId)
            for (u32 j = 0; j < 2; j++)
            {
                const u8 *text = sPipKantoRoutes[i].lines[j];
                if ((npcOffer ? FreshNPCOffer(text) : Fresh(text)) != NULL)
                    return text;
            }
    for (u32 i = 0; i < ARRAY_COUNT(sPipLivingLocations); i++)
        if (sPipLivingLocations[i].section == gMapHeader.regionMapSectionId)
            for (u32 j = 0; j < 2; j++)
            {
                const u8 *text = sPipLivingLocations[i].lines[j];
                if ((npcOffer ? FreshNPCOffer(text) : Fresh(text)) != NULL)
                    return text;
            }
    return NULL;
}
static const u8 *FreshKantoLocation(void)
{
    return FreshKantoLocationFor(FALSE);
}
static const u8 *FreshLocation(void)
{
    const u8 *kanto = FreshKantoLocation();
    if (kanto != NULL)
        return kanto;
    for (u32 i = 0; i < ARRAY_COUNT(sPipLocations); i++)
        if (sPipLocations[i].section == gMapHeader.regionMapSectionId)
            for (u32 j = 0; j < 2; j++)
                if (Fresh(sPipLocations[i].lines[j]) != NULL)
                    return sPipLocations[i].lines[j];
    for (u32 i = 0; i < ARRAY_COUNT(sPipLivingLocations); i++)
        if (sPipLivingLocations[i].section == gMapHeader.regionMapSectionId)
            for (u32 j = 0; j < 2; j++)
                if (Fresh(sPipLivingLocations[i].lines[j]) != NULL)
                    return sPipLivingLocations[i].lines[j];
    return NULL;
}
static void BeginReaction(struct ScriptContext *ctx)
{
    Cast_ClearPending();
    sSavedResult = gSpecialVar_Result;
    sSavedLastTalked = gSpecialVar_LastTalked;
    sSavedMessage = ctx->data[0];
    sSavedTextValid = FALSE;
    sPendingReaction = NULL;
    gSpecialVar_Result = FALSE;
    if (!Pip_IsFollowing() || sSceneSuspended
     || CompanionDialogue_IsInteractionActive()
     || CompanionDialogue_GetMode() != COMPANION_DIALOGUE_NORMAL)
        return;
    memcpy(sSavedText, gStringVar4, sizeof(gStringVar4));
    memcpy(sSavedSpeaker, gStringVar1, sizeof(gStringVar1));
    sSavedTextValid = TRUE;
}
static void OfferReaction(const u8 *text)
{
    u32 id = MemoryIndex(text);
    EnsureMemory();
    if (id >= ARRAY_COUNT(sPipMemoryCatalogue) || Pip_HasHeard(text)
     || (!Cast_IsFollowing() && (gSaveBlock3Ptr->pipOffered[id / 8] & (1 << (id % 8)))))
        return;
    if (Cast_IsFollowing())
    {
        if (!Cast_Offer(id)) return;
    }
    else
        gSaveBlock3Ptr->pipOffered[id / 8] |= 1 << (id % 8);
    sPendingReaction = text;
    gSpecialVar_Result = TRUE;
}

#endif

bool32 Pip_IsFollowing(void)
{
#if FNPC_ENABLE_NPC_FOLLOWERS
    return Cast_IsFollowing() || (PlayerHasFollowerNPC() && GetFollowerNPCData(FNPC_DATA_EVENT_FLAG) == FLAG_HIDE_COZY_COMPANION);
#else
    return FALSE;
#endif
}

bool32 Pip_IsSceneSuspended(void)
{
#if FNPC_ENABLE_NPC_FOLLOWERS
    return sSceneSuspended && Pip_IsFollowing();
#else
    return FALSE;
#endif
}

void Pip_RefreshIdentity(void)
{
#if FNPC_ENABLE_NPC_FOLLOWERS
    Cast_RefreshIdentity();
    if (Cast_IsFollowing())
        return;
    if (Pip_IsFollowing())
    {
        // Rebind saved ROM pointers and upgrade the former placeholder graphic.
        SetFollowerNPCData(FNPC_DATA_GFX_ID, OBJ_EVENT_GFX_PIP);
        SetFollowerNPCScriptPointer(Cozy_EventScript_Companion);
        FlagSet(FLAG_MET_PIP);
    }
#endif
}

void Pip_ResetSceneState(void)
{
#if FNPC_ENABLE_NPC_FOLLOWERS
    sSceneSuspended = FALSE;
    CompanionDialogue_ResetSession();
#endif
}

void Pip_BeforeScriptedMovement(u8 localId)
{
#if FNPC_ENABLE_NPC_FOLLOWERS
    struct ObjectEvent *pip;
    if (!Pip_IsFollowing() || localId == OBJ_EVENT_ID_NPC_FOLLOWER || localId == OBJ_EVENT_ID_FOLLOWER)
        return;
    pip = GetPipObject();
    if (pip == NULL || sSceneSuspended)
        return;
    sSceneSuspended = TRUE;
    ObjectEventClearHeldMovement(pip);
    HideNPCFollower();
    SetFollowerNPCData(FNPC_DATA_WARP_END, FNPC_WARP_NONE);
#endif
}

void Pip_TryRegroupAfterScene(void)
{
#if FNPC_ENABLE_NPC_FOLLOWERS
    struct ObjectEvent *pip;
    struct ObjectEvent *player;
    if (!sSceneSuspended || ArePlayerFieldControlsLocked() || ScriptContext_IsEnabled()
     || !ScriptMovement_IsAllObjectMovementFinished())
        return;
    sSceneSuspended = FALSE;
    if (!Pip_IsFollowing() || (pip = GetPipObject()) == NULL)
        return;
    player = &gObjectEvents[gPlayerAvatar.objectEventId];
    MoveObjectEventToMapCoords(pip, player->currentCoords.x - 7, player->currentCoords.y - 7);
    pip->invisible = TRUE;
    SetFollowerNPCData(FNPC_DATA_COME_OUT_DOOR, FNPC_DOOR_NONE);
    SetFollowerNPCData(FNPC_DATA_WARP_END, FNPC_WARP_REAPPEAR);
#endif
}

const u8 *Pip_GetLocationDialogue(u16 mapSection, u32 variant)
{
#if FNPC_ENABLE_NPC_FOLLOWERS
    for (u32 i = 0; i < ARRAY_COUNT(sPipLocations); i++)
        if (sPipLocations[i].section == mapSection)
            return sPipLocations[i].lines[variant % 2];
    return sPipGeneral[variant % ARRAY_COUNT(sPipGeneral)];
#else
    return NULL;
#endif
}

const u8 *Pip_GetProgressDialogue(u32 badges, bool32 champion)
{
#if FNPC_ENABLE_NPC_FOLLOWERS
    if (champion)
        return sPipChampion;
    return sPipProgress[badges < NUM_BADGES ? badges : NUM_BADGES];
#else
    return NULL;
#endif
}

void Script_PipCheckFollowing(struct ScriptContext *ctx)
{
    gSpecialVar_Result = Pip_IsFollowing();
}

bool32 Pip_HasHeard(const u8 *text)
{
#if FNPC_ENABLE_NPC_FOLLOWERS
    u32 id = MemoryIndex(text);
    if (Cast_IsFollowing()) return Cast_HasUsed(id);
    EnsureMemory();
    return id >= ARRAY_COUNT(sPipMemoryCatalogue)
        || (gSaveBlock3Ptr->pipHeard[id / 8] & (1 << (id % 8))) != 0;
#else
    return TRUE;
#endif
}
bool32 Pip_TrySay(const u8 *text)
{
#if FNPC_ENABLE_NPC_FOLLOWERS
    u32 id = MemoryIndex(text);
    if (CompanionDialogue_GetMode() == COMPANION_DIALOGUE_SILENT)
        return FALSE;
    if (Cast_IsFollowing())
        return text != NULL && !sSceneSuspended && Cast_TrySay(id);
    if (!Pip_IsFollowing() || sSceneSuspended || id >= ARRAY_COUNT(sPipMemoryCatalogue) || Pip_HasHeard(text))
        return FALSE;
    gSaveBlock3Ptr->pipHeard[id / 8] |= 1 << (id % 8);
    StringCopy(gStringVar4, text);
    NextComment();
    return TRUE;
#else
    return FALSE;
#endif
}
void Script_PipChooseDialogue(struct ScriptContext *ctx)
{
    gSpecialVar_Result = FALSE;
#if FNPC_ENABLE_NPC_FOLLOWERS
    u32 mode = CompanionDialogue_GetMode();
    u32 recent = CompanionDialogue_TryManualTalk();
    if (recent != 0 || mode == COMPANION_DIALOGUE_SILENT)
    {
        gSpecialVar_Result = recent == 1;
        return;
    }
    if (!sSceneSuspended && Cast_TryPersonalTalk())
    {
        gSpecialVar_Result = TRUE;
        return;
    }
    const u8 *text = Fresh(Pip_GetProgressDialogue(BadgeCount(), FlagGet(FLAG_SYS_GAME_CLEAR)));
    if (text == NULL && TestPlayerAvatarFlags(PLAYER_AVATAR_FLAG_BIKE))
        text = Fresh(sPipBike);
    if (text == NULL && gMapHeader.mapType == MAP_TYPE_UNDERWATER)
        text = Fresh(sPipUnderwater);
    if (text == NULL && TestPlayerAvatarFlags(PLAYER_AVATAR_FLAG_SURFING))
        text = Fresh(sPipSurf);
    if (text == NULL)
        text = FreshLocation();
    gSpecialVar_Result = Pip_TrySay(text);
#endif
}
void Pip_BeginKantoNPCInteraction(void)
{
#if FNPC_ENABLE_NPC_FOLLOWERS
    sKantoInteractionActive = Cast_IsFollowing() || ParallelWatch_IsKanto(gSaveBlock1Ptr->location.mapGroup, gSaveBlock1Ptr->location.mapNum);
    sKantoReactionHandled = FALSE;
    sKantoTalkGroup = gSaveBlock1Ptr->location.mapGroup;
    sKantoTalkMap = gSaveBlock1Ptr->location.mapNum;
    sKantoTalkLocalId = gSpecialVar_LastTalked;
#endif
}
void Script_PipBeginKantoNPCReaction(struct ScriptContext *ctx)
{
    if (!ParallelWatch_IsKanto(gSaveBlock1Ptr->location.mapGroup, gSaveBlock1Ptr->location.mapNum) && !Cast_IsFollowing())
    {
#if FNPC_ENABLE_NPC_FOLLOWERS
        BeginReaction(ctx);
#else
        gSpecialVar_Result = FALSE;
#endif
        return;
    }
    Script_PipBeginNPCReaction(ctx);
}
void Script_PipBeginNPCReaction(struct ScriptContext *ctx)
{
#if FNPC_ENABLE_NPC_FOLLOWERS
    u32 id;
    const u8 *text = NULL;
    BeginReaction(ctx);
    id = GetObjectEventIdByLocalId(gSpecialVar_LastTalked);
    if (!sSavedTextValid || gSpecialVar_LastTalked == OBJ_EVENT_ID_NPC_FOLLOWER
     || id >= OBJECT_EVENTS_COUNT || !gObjectEvents[id].active)
        return;
    if (Cast_IsFollowing() || ParallelWatch_IsKanto(gSaveBlock1Ptr->location.mapGroup, gSaveBlock1Ptr->location.mapNum))
    {
        if (!sKantoInteractionActive || sKantoReactionHandled
         || sKantoTalkGroup != gSaveBlock1Ptr->location.mapGroup
         || sKantoTalkMap != gSaveBlock1Ptr->location.mapNum
         || sKantoTalkLocalId != gSpecialVar_LastTalked)
            return;
        sKantoReactionHandled = TRUE;
    }
    const u8 *personScript = GetObjectEventScriptPointerByObjectEventId(id);
    for (u32 i = 0; i < ARRAY_COUNT(sPipKantoScenes); i++)
        if (sPipKantoScenes[i].script == personScript)
        {
            text = FlagGet(sPipKantoScenes[i].resolvedFlag) ? sPipKantoScenes[i].text : NULL;
            break;
        }
    OfferReaction(text);
#else
    gSpecialVar_Result = FALSE;
#endif
}
const u8 *Pip_GetExactObjectReaction(const u8 *original)
{
#if FNPC_ENABLE_NPC_FOLLOWERS
    const u8 *text = NULL;
    if (original == Text_PictureBookShelf) text = Cozy_Text_PictureBookShelf;
    else if (original == Text_BookShelf || original == Text_PokemonCenterBookShelf) text = Cozy_Text_BookShelf;
    else if (original == Text_Vase) text = Cozy_Text_Vase;
    else if (original == Text_EmptyTrashCan) text = Cozy_Text_EmptyTrashCan;
    else if (original == Text_ShopShelf) text = Cozy_Text_ShopShelf;
    else if (original == Text_Blueprint) text = Cozy_Text_Blueprint;
    for (u32 i = 0; i < ARRAY_COUNT(sPipKantoObjects); i++)
        if (original == sPipKantoObjects[i].original)
        {
            text = sPipKantoObjects[i].comment;
            break;
        }
    // Preserve the released paired-scene replies, bound to the actual final
    // dialogue rather than merely noticing that a quest flag is set.
    static const u8 *const completedScenes[] = {
        LivingKanto_Scene0_After,
        LivingKanto_Scene1_After,
        LivingKanto_Scene2_After,
        LivingKanto_Scene3_After,
        LivingKanto_Scene4_After,
        LivingKanto_Scene5_After,
        LivingKanto_Scene6_After,
        LivingKanto_Scene7_After,
        LivingKanto_Scene8_After,
        LivingKanto_Scene9_After,
        LivingKanto_Scene10_After,
        LivingKanto_Scene11_After,
    };
    for (u32 i = 0; i < ARRAY_COUNT(completedScenes); i++)
        if (original == completedScenes[i] && FlagGet(sPipKantoScenes[i * 2].resolvedFlag))
            return sPipKantoScenes[i * 2].text;
    return text;
#else
    return NULL;
#endif
}
bool32 Pip_TryOfferExact(const u8 *text)
{
#if FNPC_ENABLE_NPC_FOLLOWERS
    u16 result = gSpecialVar_Result;
    sPendingReaction = NULL;
    OfferReaction(text);
    bool32 offered = sPendingReaction != NULL;
    gSpecialVar_Result = result;
    return offered;
#else
    return FALSE;
#endif
}

void Script_PipBeginObjectReaction(struct ScriptContext *ctx)
{
#if FNPC_ENABLE_NPC_FOLLOWERS
    const u8 *text = NULL;
    const u8 *original;
    BeginReaction(ctx);
    if (!sSavedTextValid)
        return;
    original = (const u8 *)sSavedMessage;
    text = Pip_GetExactObjectReaction(original);
    OfferReaction(text);
#else
    gSpecialVar_Result = FALSE;
#endif
}
void Script_PipChooseObjectDialogue(struct ScriptContext *ctx)
{
#if FNPC_ENABLE_NPC_FOLLOWERS
    gSpecialVar_Result = Pip_TrySay(sPendingReaction);
#endif
}
void Script_PipChooseNPCDialogue(struct ScriptContext *ctx)
{
    Script_PipChooseObjectDialogue(ctx);
}

void Script_PipEndNPCReaction(struct ScriptContext *ctx)
{
#if FNPC_ENABLE_NPC_FOLLOWERS
    gSpecialVar_Result = sSavedResult;
    gSpecialVar_LastTalked = sSavedLastTalked;
    ctx->data[0] = sSavedMessage;
    if (sSavedTextValid)
    {
        memcpy(gStringVar4, sSavedText, sizeof(gStringVar4));
        memcpy(gStringVar1, sSavedSpeaker, sizeof(gStringVar1));
    }
    Cast_ClearPending();
    Cast_HidePortrait();
    sSavedTextValid = FALSE;
#endif
}
