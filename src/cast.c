#include "global.h"
#include "cast.h"
#include "pip.h"
#include "pokemon.h"
#include "event_data.h"
#include "event_object_movement.h"
#include "field_player_avatar.h"
#include "follower_npc.h"
#include "item.h"
#include "battle_setup.h"
#include "script.h"
#include "string_util.h"
#include "sprite.h"
#include "constants/event_objects.h"
#include "constants/follower_npc.h"
#include "constants/kanto_progress.h"

#if FNPC_ENABLE_NPC_FOLLOWERS && !IS_FRLG
#define CAST_VERSION 1
#define CAST_PORTRAIT_TAG 0x7C50
extern const u8 Cast_EventScript_Companion[], Cozy_EventScript_Companion[];
enum { CAST_REQ_STEPS, CAST_REQ_SPECIES, CAST_REQ_ITEM };
struct CastCharacter {
    u16 graphics, trainer, requirement, value;
    u8 walkSlot;
    const u8 *name, *intro, *request, *ready, *join;
    const u8 *lore[6];
    u8 loreExpression[6];
};
struct CastComment { const u8 *text; u8 expression; u16 topic; };
#include "data/cast_characters.h"
#include "data/cast_dialogue.h"
static EWRAM_DATA u8 sRecruitId = 0;
static EWRAM_DATA u16 sPending = CAST_CONTEXT_CAPACITY;
static EWRAM_DATA u8 sPendingCharacter = 0;
static EWRAM_DATA u8 sPortraitSprite = MAX_SPRITES;
static const struct OamData sPortraitOam = { .shape = 0, .size = 3, .priority = 0 };
static const struct SpriteTemplate sPortraitTemplate = {
    .tileTag = CAST_PORTRAIT_TAG, .paletteTag = CAST_PORTRAIT_TAG,
    .oam = &sPortraitOam, .anims = gDummySpriteAnimTable,
    .affineAnims = gDummySpriteAffineAnimTable, .callback = SpriteCallbackDummy,
};
static void ShowPortrait(u32 who, u32 expression)
{
    struct SpriteSheet sheet;
    struct SpritePalette palette;
    Cast_HidePortrait();
    if (who >= CAST_COUNT || expression >= 8)
        return;
    sheet = (struct SpriteSheet){sCastPortraits[who] + expression * 2048, 2048, CAST_PORTRAIT_TAG};
    palette = (struct SpritePalette){sCastPortraitPalettes[who], CAST_PORTRAIT_TAG};
    if (LoadSpriteSheet(&sheet) == 0xFFFF)
        return;
    if (LoadSpritePalette(&palette) == 0xFF)
    {
        FreeSpriteTilesByTag(CAST_PORTRAIT_TAG);
        return;
    }
    // 64x64, entirely above the normal dialogue window; independent OBJ palette.
    sPortraitSprite = CreateSprite(&sPortraitTemplate, 40, 72, 0);
    if (sPortraitSprite == MAX_SPRITES)
    {
        FreeSpriteTilesByTag(CAST_PORTRAIT_TAG);
        FreeSpritePaletteByTag(CAST_PORTRAIT_TAG);
    }
}
static void Say(u32 who, const u8 *text, u32 expression)
{
    StringCopy(gStringVar4, text);
    ShowPortrait(who, expression);
}
static bool32 HasRequirement(u32 who)
{
    const struct CastCharacter *c = &sCastCharacters[who];
    struct CastProgress *p = &gSaveBlock3Ptr->cast;
    if (p->ready & (1 << who))
        return TRUE;
    if (c->requirement == CAST_REQ_STEPS)
        return p->steps - p->walkStart[c->walkSlot] >= c->value;
    if (c->requirement == CAST_REQ_ITEM)
        return CheckBagHasItem(c->value, 1);
    for (u32 i = 0; i < gPartiesCount[B_TRAINER_PLAYER]; i++)
        if (!GetMonData(&gParties[B_TRAINER_PLAYER][i], MON_DATA_IS_EGG)
         && GetMonData(&gParties[B_TRAINER_PLAYER][i], MON_DATA_SPECIES) == c->value)
            return TRUE;
    return FALSE;
}
static bool32 SwitchTo(u32 selected)
{
    u16 flag;
    u32 gfx;
    if (selected > CAST_COUNT || (selected && !(gSaveBlock3Ptr->cast.recruited & (1 << (selected - 1))))
     || (!selected && !FlagGet(FLAG_MET_PIP)))
        return FALSE;
    if (PlayerHasFollowerNPC() && !Pip_IsFollowing())
        return FALSE; // Never replace a story escort.
    if (selected && gSaveBlock3Ptr->cast.active == selected && Cast_IsFollowing())
        return TRUE;
    // Dismiss the previous companion; they become available at their original map.
    if (PlayerHasFollowerNPC())
        DestroyFollowerNPC();
    FlagClear(FLAG_HIDE_COZY_COMPANION);
    gSaveBlock3Ptr->cast.hidden = 0;
    gSaveBlock3Ptr->cast.active = selected;
    flag = selected ? CAST_FLAG_BASE + selected - 1 : FLAG_HIDE_COZY_COMPANION;
    gfx = selected ? sCastCharacters[selected - 1].graphics : OBJ_EVENT_GFX_PIP;
    // Remove the destination's stationary actor before creating the follower.
    for (u32 i = 0; i < gMapHeader.events->objectEventCount; i++)
        if (gMapHeader.events->objectEvents[i].flagId == flag)
            RemoveObjectEventByLocalIdAndMap(gMapHeader.events->objectEvents[i].localId,
                gSaveBlock1Ptr->location.mapNum, gSaveBlock1Ptr->location.mapGroup);
    for (u32 i = 0; i < OBJECT_EVENTS_COUNT; i++)
        if (!gObjectEvents[i].active)
        {
            FlagSet(flag);
            CreateFollowerNPC(gfx, FNPC_ALL_LAND | FNPC_ALL_WATER,
                selected ? Cast_EventScript_Companion : Cozy_EventScript_Companion);
            SetFollowerNPCData(FNPC_DATA_EVENT_FLAG, flag);
            return TRUE;
        }
    gSaveBlock3Ptr->cast.active = 0;
    return FALSE;
}
#endif

void Cast_EnsureInitialized(void)
{
#if FNPC_ENABLE_NPC_FOLLOWERS && !IS_FRLG
    if (gSaveBlock3Ptr && gSaveBlock3Ptr->cast.version != CAST_VERSION)
    {
        // Only the new suffix is initialized. Kanto, watch, Pip and PC remain intact.
        memset(&gSaveBlock3Ptr->cast, 0, sizeof(gSaveBlock3Ptr->cast));
        gSaveBlock3Ptr->cast.version = CAST_VERSION;
    }
#endif
}
u32 Cast_Active(void)
{
#if FNPC_ENABLE_NPC_FOLLOWERS && !IS_FRLG
    Cast_EnsureInitialized();
    if (gSaveBlock3Ptr && gSaveBlock3Ptr->cast.active <= CAST_COUNT)
        return gSaveBlock3Ptr->cast.active;
#endif
    return 0;
}
u8 *Cast_GetFlagPointer(u16 id)
{
#if FNPC_ENABLE_NPC_FOLLOWERS && !IS_FRLG
    Cast_EnsureInitialized();
    if (gSaveBlock3Ptr && id >= CAST_FLAG_BASE && id < CAST_FLAG_BASE + CAST_COUNT)
        return (u8 *)&gSaveBlock3Ptr->cast.hidden + (id - CAST_FLAG_BASE) / 8;
#endif
    return NULL;
}
bool32 Cast_IsFollowing(void)
{
#if FNPC_ENABLE_NPC_FOLLOWERS && !IS_FRLG
    u32 active = Cast_Active();
    return active && PlayerHasFollowerNPC()
        && GetFollowerNPCData(FNPC_DATA_EVENT_FLAG) == CAST_FLAG_BASE + active - 1;
#else
    return FALSE;
#endif
}
void Cast_RefreshIdentity(void)
{
#if FNPC_ENABLE_NPC_FOLLOWERS && !IS_FRLG
    if (Cast_IsFollowing())
    {
        SetFollowerNPCData(FNPC_DATA_GFX_ID, sCastCharacters[Cast_Active() - 1].graphics);
        SetFollowerNPCScriptPointer(Cast_EventScript_Companion);
    }
#endif
}
void Cast_OnStep(void)
{
#if FNPC_ENABLE_NPC_FOLLOWERS && !IS_FRLG
    if (gSaveBlock3Ptr->cast.version == CAST_VERSION
     && TestPlayerAvatarFlags(PLAYER_AVATAR_FLAG_ON_FOOT)
     && gSaveBlock3Ptr->cast.steps != 0xFFFFFFFF)
        gSaveBlock3Ptr->cast.steps++;
#endif
}
bool32 Cast_HasUsed(u32 id)
{
#if FNPC_ENABLE_NPC_FOLLOWERS && !IS_FRLG
    u32 active = Cast_Active();
    if (active && id < CAST_SOURCE_COUNT)
    {
        id = sCastContextMemoryId[active - 1][id];
        return (gSaveBlock3Ptr->cast.used[active - 1][id / 8] & (1 << (id % 8))) != 0;
    }
#endif
    return TRUE;
}
bool32 Cast_Offer(u32 id)
{
#if FNPC_ENABLE_NPC_FOLLOWERS && !IS_FRLG
    u32 active = Cast_Active(), memoryId;
    if (!active || id >= CAST_SOURCE_COUNT || Cast_HasUsed(id))
        return FALSE;
    memoryId = sCastContextMemoryId[active - 1][id];
    gSaveBlock3Ptr->cast.used[active - 1][memoryId / 8] |= 1 << (memoryId % 8);
    sPending = id;
    sPendingCharacter = active;
    return TRUE;
#endif
    return FALSE;
}
bool32 Cast_TrySay(u32 id)
{
#if FNPC_ENABLE_NPC_FOLLOWERS && !IS_FRLG
    struct CastProgress *p = &gSaveBlock3Ptr->cast;
    const struct CastComment *comment;
    static const u8 thresholds[] = {0, 4, 9, 15, 22, 30};
    u32 active = Cast_Active(), who, stage, memoryId;
    if (!Cast_IsFollowing() || !active || id >= CAST_SOURCE_COUNT)
        return FALSE;
    who = active - 1;
    if (Cast_HasUsed(id) && !(sPending == id && sPendingCharacter == active))
        return FALSE;
    Cast_ClearPending();
    comment = &sCastComments[who][id];
    if (comment->text == NULL)
        return FALSE;
    memoryId = sCastContextMemoryId[active - 1][id];
    p->used[who][memoryId / 8] |= 1 << (memoryId % 8);
    stage = p->loreStage[who];
    // Ordered revelations emerge during actual conversations, never a rotating fallback.
    if (stage < ARRAY_COUNT(thresholds) && p->spoken[who] >= thresholds[stage]
     && (comment->topic & sCastLoreTriggers[who][stage]))
    {
        Say(who, sCastCharacters[who].lore[stage], sCastCharacters[who].loreExpression[stage]);
        p->loreStage[who]++;
    }
    else
        Say(who, comment->text, comment->expression);
    if (p->spoken[who] < 255)
        p->spoken[who]++;
    return TRUE;
#else
    return FALSE;
#endif
}
void Cast_ClearPending(void)
{
#if FNPC_ENABLE_NPC_FOLLOWERS && !IS_FRLG
    sPending = CAST_CONTEXT_CAPACITY;
    sPendingCharacter = 0;
#endif
}
void Cast_HidePortrait(void)
{
#if FNPC_ENABLE_NPC_FOLLOWERS && !IS_FRLG
    if (sPortraitSprite < MAX_SPRITES && gSprites[sPortraitSprite].inUse
     && gSprites[sPortraitSprite].template == &sPortraitTemplate)
        DestroySprite(&gSprites[sPortraitSprite]);
    sPortraitSprite = MAX_SPRITES;
    FreeSpriteTilesByTag(CAST_PORTRAIT_TAG);
    FreeSpritePaletteByTag(CAST_PORTRAIT_TAG);
#endif
}
void Script_CastRecruitStatus(struct ScriptContext *ctx)
{
    gSpecialVar_Result = 0;
#if FNPC_ENABLE_NPC_FOLLOWERS && !IS_FRLG
    struct CastProgress *p;
    const struct CastCharacter *c;
    Cast_EnsureInitialized();
    if (gSpecialVar_0x8004 >= CAST_COUNT)
        return;
    sRecruitId = gSpecialVar_0x8004;
    p = &gSaveBlock3Ptr->cast;
    c = &sCastCharacters[sRecruitId];
    if (HasTrainerBeenFought(c->trainer))
    {
        gSpecialVar_Result = 2;
        return;
    }
    if (!(p->met & (1 << sRecruitId)))
    {
        p->met |= 1 << sRecruitId;
        if (c->requirement == CAST_REQ_STEPS)
            p->walkStart[c->walkSlot] = p->steps;
        Say(sRecruitId, c->intro, 0);
    }
    else if (HasRequirement(sRecruitId))
    {
        Say(sRecruitId, c->ready, 1);
        gSpecialVar_Result = 1;
    }
    else
        Say(sRecruitId, c->request, 0);
#endif
}
void Script_CastCommitRequirement(struct ScriptContext *ctx)
{
    gSpecialVar_Result = FALSE;
#if FNPC_ENABLE_NPC_FOLLOWERS && !IS_FRLG
    struct CastProgress *p = &gSaveBlock3Ptr->cast;
    const struct CastCharacter *c = &sCastCharacters[sRecruitId];
    Cast_HidePortrait();
    if (!HasRequirement(sRecruitId))
        return;
    if (!(p->ready & (1 << sRecruitId)) && c->requirement == CAST_REQ_ITEM
     && !RemoveBagItem(c->value, 1))
        return;
    p->ready |= 1 << sRecruitId;
    gSpecialVar_Result = TRUE;
#endif
}
void Script_CastAfterBattle(struct ScriptContext *ctx)
{
    gSpecialVar_Result = FALSE;
#if FNPC_ENABLE_NPC_FOLLOWERS && !IS_FRLG
    if (HasTrainerBeenFought(sCastCharacters[sRecruitId].trainer))
    {
        gSaveBlock3Ptr->cast.recruited |= 1 << sRecruitId;
        Say(sRecruitId, sCastCharacters[sRecruitId].join, 1);
        gSpecialVar_Result = TRUE;
    }
#endif
}
void Script_CastJoin(struct ScriptContext *ctx)
{
    gSpecialVar_Result = FALSE;
#if FNPC_ENABLE_NPC_FOLLOWERS && !IS_FRLG
    Cast_HidePortrait();
    gSpecialVar_Result = SwitchTo(sRecruitId + 1);
#endif
}
void Script_CastSwitchRoster(struct ScriptContext *ctx)
{
#if FNPC_ENABLE_NPC_FOLLOWERS && !IS_FRLG
    u32 selected = gSpecialVar_Result;
    Cast_EnsureInitialized();
    gSpecialVar_Result = SwitchTo(selected);
#else
    gSpecialVar_Result = FALSE;
#endif
}
void Script_CastDismiss(struct ScriptContext *ctx)
{
#if FNPC_ENABLE_NPC_FOLLOWERS && !IS_FRLG
    Cast_HidePortrait();
    if (Cast_IsFollowing())
    {
        DestroyFollowerNPC();
        gSaveBlock3Ptr->cast.hidden = 0;
        gSaveBlock3Ptr->cast.active = 0;
    }
#endif
}
void Script_CastBufferSpeaker(struct ScriptContext *ctx)
{
#if FNPC_ENABLE_NPC_FOLLOWERS && !IS_FRLG
    u32 active = Cast_Active();
    StringCopy(gStringVar1, active ? sCastCharacters[active - 1].name : COMPOUND_STRING("PIP"));
#else
    StringCopy(gStringVar1, COMPOUND_STRING("PIP"));
#endif
}
void Script_CastHidePortrait(struct ScriptContext *ctx) { Cast_HidePortrait(); }

bool32 Cast_TryPersonalTalk(void)
{
#if FNPC_ENABLE_NPC_FOLLOWERS && !IS_FRLG
    static const u8 thresholds[] = {0, 4, 9, 15, 22, 30};
    u32 active = Cast_Active(), who, stage;
    if (!Cast_IsFollowing() || !active)
        return FALSE;
    who = active - 1;
    stage = gSaveBlock3Ptr->cast.loreStage[who];
    if (stage >= ARRAY_COUNT(thresholds) || gSaveBlock3Ptr->cast.spoken[who] < thresholds[stage])
        return FALSE;
    Say(who, sCastCharacters[who].lore[stage], sCastCharacters[who].loreExpression[stage]);
    gSaveBlock3Ptr->cast.loreStage[who]++;
    return TRUE;
#else
    return FALSE;
#endif
}

void Cast_ShowPortrait(u32 who, u32 expression)
{
#if FNPC_ENABLE_NPC_FOLLOWERS && !IS_FRLG
    ShowPortrait(who, expression);
#endif
}
