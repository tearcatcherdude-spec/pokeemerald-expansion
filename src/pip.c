#include "global.h"
#include "pip.h"
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
extern const u8 Text_PictureBookShelf[], Text_BookShelf[], Text_PokemonCenterBookShelf[];
extern const u8 Text_Vase[], Text_EmptyTrashCan[], Text_ShopShelf[], Text_Blueprint[];
extern const u8 Cozy_Text_PictureBookShelf[], Cozy_Text_BookShelf[], Cozy_Text_Vase[];
extern const u8 Cozy_Text_EmptyTrashCan[], Cozy_Text_ShopShelf[], Cozy_Text_Blueprint[];

static EWRAM_DATA bool8 sSceneSuspended = FALSE;
static EWRAM_DATA u16 sSavedResult = 0;
static EWRAM_DATA u16 sSavedLastTalked = 0;
static EWRAM_DATA u16 sReactionGraphics = 0;
static EWRAM_DATA u32 sSavedMessage = 0;
static EWRAM_DATA bool8 sSavedTextValid = FALSE;
static EWRAM_DATA u8 sSavedText[sizeof(gStringVar4)] = {0};

struct PipLocationDialogue
{
    u16 section;
    const u8 *lines[2];
};

#include "data/pip_dialogue.h"

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

static void BeginReaction(struct ScriptContext *ctx)
{
    sSavedResult = gSpecialVar_Result;
    sSavedLastTalked = gSpecialVar_LastTalked;
    sSavedMessage = ctx->data[0];
    sSavedTextValid = FALSE;
    gSpecialVar_Result = FALSE;
    if (!Pip_IsFollowing() || sSceneSuspended)
        return;
    memcpy(sSavedText, gStringVar4, sizeof(gStringVar4));
    sSavedTextValid = TRUE;
    gSpecialVar_Result = TRUE;
}
#endif

bool32 Pip_IsFollowing(void)
{
#if FNPC_ENABLE_NPC_FOLLOWERS
    return PlayerHasFollowerNPC() && GetFollowerNPCData(FNPC_DATA_EVENT_FLAG) == FLAG_HIDE_COZY_COMPANION;
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

void Script_PipChooseDialogue(struct ScriptContext *ctx)
{
#if FNPC_ENABLE_NPC_FOLLOWERS
    u32 counter = NextComment();
    const u8 *text;
    if ((counter % 4) == 2)
        text = Pip_GetProgressDialogue(BadgeCount(), FlagGet(FLAG_SYS_GAME_CLEAR));
    else if ((counter % 4) == 3 && TestPlayerAvatarFlags(PLAYER_AVATAR_FLAG_BIKE))
        text = sPipBike;
    else if ((counter % 4) == 3 && gMapHeader.mapType == MAP_TYPE_UNDERWATER)
        text = sPipUnderwater;
    else if ((counter % 4) == 3 && TestPlayerAvatarFlags(PLAYER_AVATAR_FLAG_SURFING))
        text = sPipSurf;
    else if ((counter % 4) == 3 && gMapHeader.mapType == MAP_TYPE_UNDERGROUND)
        text = sPipCave;
    else
        text = Pip_GetLocationDialogue(gMapHeader.regionMapSectionId, counter);
    StringCopy(gStringVar4, text);
#endif
}

void Script_PipBeginNPCReaction(struct ScriptContext *ctx)
{
#if FNPC_ENABLE_NPC_FOLLOWERS
    u32 id;
    BeginReaction(ctx);
    id = GetObjectEventIdByLocalId(gSpecialVar_LastTalked);
    if (!Pip_IsFollowing() || sSceneSuspended || gSpecialVar_LastTalked == OBJ_EVENT_ID_NPC_FOLLOWER
     || id >= OBJECT_EVENTS_COUNT || !gObjectEvents[id].active)
    {
        gSpecialVar_Result = FALSE;
        return;
    }
    sReactionGraphics = gObjectEvents[id].graphicsId;
    gSpecialVar_Result = TRUE;
#else
    gSpecialVar_Result = FALSE;
#endif
}

void Script_PipBeginObjectReaction(struct ScriptContext *ctx)
{
#if FNPC_ENABLE_NPC_FOLLOWERS
    BeginReaction(ctx);
#else
    gSpecialVar_Result = FALSE;
#endif
}

void Script_PipChooseObjectDialogue(struct ScriptContext *ctx)
{
#if FNPC_ENABLE_NPC_FOLLOWERS
    const u8 *original = (const u8 *)sSavedMessage;
    const u8 *text = sPipGeneral[NextComment() % ARRAY_COUNT(sPipGeneral)];
    if (original == Text_PictureBookShelf)
        text = Cozy_Text_PictureBookShelf;
    else if (original == Text_BookShelf || original == Text_PokemonCenterBookShelf)
        text = Cozy_Text_BookShelf;
    else if (original == Text_Vase)
        text = Cozy_Text_Vase;
    else if (original == Text_EmptyTrashCan)
        text = Cozy_Text_EmptyTrashCan;
    else if (original == Text_ShopShelf)
        text = Cozy_Text_ShopShelf;
    else if (original == Text_Blueprint)
        text = Cozy_Text_Blueprint;
    else
        text = Pip_GetLocationDialogue(gMapHeader.regionMapSectionId, VarGet(VAR_PIP_COMMENT_COUNTER));
    StringCopy(gStringVar4, text);
#endif
}

void Script_PipChooseNPCDialogue(struct ScriptContext *ctx)
{
#if FNPC_ENABLE_NPC_FOLLOWERS
    const u8 *text;
    switch (sReactionGraphics)
    {
    case OBJ_EVENT_GFX_HIKER: text = sPipHiker; break;
    case OBJ_EVENT_GFX_FISHERMAN: text = sPipFisherman; break;
    case OBJ_EVENT_GFX_SAILOR: text = sPipSailor; break;
    case OBJ_EVENT_GFX_SCIENTIST_1:
    case OBJ_EVENT_GFX_SCIENTIST_2: text = sPipScientist; break;
    case OBJ_EVENT_GFX_NURSE: text = sPipNurse; break;
    default: text = sPipNPC[NextComment() % ARRAY_COUNT(sPipNPC)]; break;
    }
    StringCopy(gStringVar4, text);
#endif
}

void Script_PipEndNPCReaction(struct ScriptContext *ctx)
{
#if FNPC_ENABLE_NPC_FOLLOWERS
    gSpecialVar_Result = sSavedResult;
    gSpecialVar_LastTalked = sSavedLastTalked;
    ctx->data[0] = sSavedMessage;
    if (sSavedTextValid)
        memcpy(gStringVar4, sSavedText, sizeof(gStringVar4));
    sSavedTextValid = FALSE;
#endif
}
