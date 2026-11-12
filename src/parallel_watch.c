#include "global.h"
#include "main.h"
#include "kanto_progress.h"
#include "safari_zone.h"
#include "heal_location.h"
#include "constants/heal_locations.h"
#include "parallel_watch.h"
#include "overworld.h"
#include "field_player_avatar.h"
#include "field_screen_effect.h"
#include "event_object_movement.h"
#include "event_data.h"
#include "pokemon.h"
#include "battle.h"
#include "script.h"
#include "string_util.h"
#include "constants/maps.h"
#include "constants/metatile_behaviors.h"

#if FNPC_ENABLE_NPC_FOLLOWERS
#define WATCH_VERSION 1
static EWRAM_DATA u8 sArrivalFacing = 0;
static const u16 sKantoOutdoorMaps[] = {
#include "data/kanto_outdoors.h"
};
// All members of an imported map group belong to Kanto. The topology validator
// checks this compact index against the complete manifest before every build.
static const u8 sKantoMapGroupCounts[] = {
#include "data/kanto_map_group_counts.h"
};
bool32 ParallelWatch_IsKanto(u32 group, u32 num)
{
    return group < ARRAY_COUNT(sKantoMapGroupCounts)
        && num < sKantoMapGroupCounts[group];
}

bool32 ParallelWatch_IsOutdoor(u32 group, u32 num)
{
    if (GetSafariZoneFlag())
        return FALSE;
    for (u32 i = 0; i < ARRAY_COUNT(sKantoOutdoorMaps); i++)
        if (MAP_GROUP(sKantoOutdoorMaps[i]) == group && MAP_NUM(sKantoOutdoorMaps[i]) == num)
            return TRUE;
    return group == MAP_GROUP(MAP_LITTLEROOT_TOWN)
        && num <= MAP_NUM(MAP_ROUTE134)
        && IsMapTypeOutdoors(Overworld_GetMapHeaderByGroupAndId(group, num)->mapType);
}

bool32 ParallelWatch_IsSafeAnchor(const struct ParallelWatchAnchor *a, u32 world)
{
    const struct MapHeader *h;
    const struct MapLayout *l;
    const struct Tileset *t;
    u32 id, behavior, block;
    if (!a->valid || world > 1 || !ParallelWatch_IsOutdoor(a->mapGroup, a->mapNum)
     || ParallelWatch_IsKanto(a->mapGroup, a->mapNum) != world
     || a->facing < DIR_SOUTH || a->facing > DIR_EAST)
        return FALSE;
    h = Overworld_GetMapHeaderByGroupAndId(a->mapGroup, a->mapNum);
    l = h->mapLayout;
    if (a->x < 0 || a->y < 0 || a->x >= l->width || a->y >= l->height)
        return FALSE;
    block = l->map[a->y * l->width + a->x];
    if (block & MAPGRID_COLLISION_MASK)
        return FALSE;
    id = block & MAPGRID_METATILE_ID_MASK;
    t = l->primaryTileset;
    if (id >= (l->isFrlg ? 640 : 512))
    {
        id -= l->isFrlg ? 640 : 512;
        t = l->secondaryTileset;
    }
    behavior = l->isFrlg ? ((const u32 *)t->metatileAttributes)[id] & 0x1ff
                         : t->metatileAttributes[id] & 0xff;
    // A small explicit whitelist excludes water, ledges, warps, bridges,
    // currents and forced-movement tiles even when their collision is clear.
    if (behavior != MB_NORMAL && behavior != MB_TALL_GRASS
     && behavior != MB_SHORT_GRASS && behavior != MB_SAND)
        return FALSE;
    for (u32 i = 0; i < h->events->warpCount; i++)
        if (h->events->warps[i].x == a->x && h->events->warps[i].y == a->y)
            return FALSE;
    for (u32 i = 0; i < h->events->coordEventCount; i++)
        if (h->events->coordEvents[i].x == a->x && h->events->coordEvents[i].y == a->y)
            return FALSE;
    for (u32 i = 0; i < h->events->objectEventCount; i++)
    {
        const struct ObjectEventTemplate *o = &h->events->objectEvents[i];
        if ((!o->flagId || !FlagGet(o->flagId))
         && a->x >= o->x - o->movementRangeX && a->x <= o->x + o->movementRangeX
         && a->y >= o->y - o->movementRangeY && a->y <= o->y + o->movementRangeY)
            return FALSE;
    }
    return TRUE;
}

static struct ParallelWatchAnchor CurrentAnchor(void)
{
    struct ParallelWatchAnchor a = {
        .mapGroup = gSaveBlock1Ptr->location.mapGroup,
        .mapNum = gSaveBlock1Ptr->location.mapNum,
        .x = gSaveBlock1Ptr->pos.x, .y = gSaveBlock1Ptr->pos.y,
        .facing = GetPlayerFacingDirection(), .valid = TRUE,
    };
    return a;
}
static bool32 Deny(const u8 *text)
{
    StringCopy(gStringVar4, text);
    return FALSE;
}
static bool32 IsVoidMap(void)
{
    return gSaveBlock1Ptr->location.mapGroup == MAP_GROUP(MAP_VOID_OLDALE_TOWN)
        && gSaveBlock1Ptr->location.mapNum <= MAP_NUM(MAP_VOID_OLDALE_SHOP);
}
static bool32 IsSafeVoidSpot(void)
{
    const struct MapLayout *l = gMapHeader.mapLayout;
    s32 x = gSaveBlock1Ptr->pos.x, y = gSaveBlock1Ptr->pos.y;
    if (!IsVoidMap() || gSaveBlock1Ptr->location.mapNum != MAP_NUM(MAP_VOID_OLDALE_TOWN)
     || x < 0 || y < 0 || x >= l->width || y >= l->height
     || (l->map[y * l->width + x] & MAPGRID_COLLISION_MASK))
        return FALSE;
    for (u32 i = 0; i < gMapHeader.events->warpCount; i++)
        if (gMapHeader.events->warps[i].x == x && gMapHeader.events->warps[i].y == y)
            return FALSE;
    return TRUE;
}
static bool32 CanSwitch(void)
{
    struct ParallelWatchAnchor a = CurrentAnchor();
    bool32 healthy = FALSE;
    if (gMain.inBattle || IsOverworldLinkActive())
        return Deny(COMPOUND_STRING("The hands are still.$"));
    for (u32 i = 0; i < PARTY_SIZE; i++)
        if (GetMonData(&gParties[B_TRAINER_PLAYER][i], MON_DATA_SPECIES) != SPECIES_NONE
         && !GetMonData(&gParties[B_TRAINER_PLAYER][i], MON_DATA_IS_EGG)
         && GetMonData(&gParties[B_TRAINER_PLAYER][i], MON_DATA_HP))
            healthy = TRUE;
    if (!healthy)
        return Deny(COMPOUND_STRING("The hands are still.$"));
    if (!TestPlayerAvatarFlags(PLAYER_AVATAR_FLAG_ON_FOOT))
        return Deny(COMPOUND_STRING("The hands will not turn.$"));
    if (!ParallelWatch_IsSafeAnchor(&a, ParallelWatch_IsKanto(a.mapGroup, a.mapNum)) && !IsSafeVoidSpot())
        return Deny(COMPOUND_STRING("The hands will not turn here.$"));
    return TRUE;
}
void Script_ParallelWatchCheck(struct ScriptContext *ctx)
{
    gSpecialVar_Result = CanSwitch();
}
static void WatchArrival(void)
{
    FieldCB_DefaultWarpExit(); // Includes the normal companion warp-end hook.
    PlayerFaceDirection(sArrivalFacing);
}
void Script_VoidWatchIsHere(struct ScriptContext *ctx)
{
    gSpecialVar_Result = IsVoidMap();
}
void Script_VoidWatchEnter(struct ScriptContext *ctx)
{
    struct ParallelWatchAnchor from = CurrentAnchor();
    gSpecialVar_Result = FALSE;
    if (IsVoidMap() || !CanSwitch()) return;
    if (gSaveBlock3Ptr->watchMemoryVersion != WATCH_VERSION)
    {
        memset(gSaveBlock3Ptr->watchAnchors, 0, sizeof(gSaveBlock3Ptr->watchAnchors));
        gSaveBlock3Ptr->watchMemoryVersion = WATCH_VERSION;
    }
    // Existing two-world anchors keep their released offsets. The Void is an
    // Oldale side-world with a fixed entry and a return to the safe Hoenn anchor.
    gSaveBlock3Ptr->watchAnchors[ParallelWatch_IsKanto(from.mapGroup, from.mapNum)] = from;
    SetWarpDestinationToCoords(MAP_GROUP(MAP_VOID_OLDALE_TOWN), MAP_NUM(MAP_VOID_OLDALE_TOWN), 10, 10);
    sArrivalFacing = DIR_SOUTH;
    gSpecialVar_Result = TRUE;
    DoWarp();
    gFieldCallback = WatchArrival;
    ResetInitialPlayerAvatarState();
}
void Script_VoidWatchReturn(struct ScriptContext *ctx)
{
    struct ParallelWatchAnchor target = gSaveBlock3Ptr->watchAnchors[0];
    gSpecialVar_Result = FALSE;
    if (!IsVoidMap() || !CanSwitch()) return;
    if (gSaveBlock3Ptr->watchMemoryVersion != WATCH_VERSION || !ParallelWatch_IsSafeAnchor(&target, 0))
        target = (struct ParallelWatchAnchor){.mapGroup=MAP_GROUP(MAP_OLDALE_TOWN),.mapNum=MAP_NUM(MAP_OLDALE_TOWN),.x=10,.y=10,.facing=DIR_SOUTH,.valid=TRUE};
    if (!ParallelWatch_IsSafeAnchor(&target, 0)) { Deny(COMPOUND_STRING("The hands spin, then stop.$")); return; }
    SetWarpDestinationToCoords(target.mapGroup, target.mapNum, target.x, target.y);
    sArrivalFacing = target.facing;
    gSpecialVar_Result = TRUE;
    DoWarp();
    gFieldCallback = WatchArrival;
    ResetInitialPlayerAvatarState();
}
void Script_ParallelWatchSwitch(struct ScriptContext *ctx)
{
    struct ParallelWatchAnchor from = CurrentAnchor();
    struct ParallelWatchAnchor target;
    u32 world = ParallelWatch_IsKanto(from.mapGroup, from.mapNum);
    if (IsVoidMap()) { Script_VoidWatchReturn(ctx); return; }
    gSpecialVar_Result = FALSE;
    if (!CanSwitch())
        return;
    if (gSaveBlock3Ptr->watchMemoryVersion != WATCH_VERSION)
    {
        memset(gSaveBlock3Ptr->watchAnchors, 0, sizeof(gSaveBlock3Ptr->watchAnchors));
        gSaveBlock3Ptr->watchMemoryVersion = WATCH_VERSION;
    }
    target = gSaveBlock3Ptr->watchAnchors[!world];
    if (!ParallelWatch_IsSafeAnchor(&target, !world))
    {
        target = (struct ParallelWatchAnchor){
            .mapGroup = world ? MAP_GROUP(MAP_LITTLEROOT_TOWN) : MAP_GROUP(MAP_WATCH_PALLET),
            .mapNum = world ? MAP_NUM(MAP_LITTLEROOT_TOWN) : MAP_NUM(MAP_WATCH_PALLET),
            .x = world ? 10 : 10, .y = world ? 16 : 14,
            .facing = DIR_SOUTH, .valid = TRUE,
        };
        if (!ParallelWatch_IsSafeAnchor(&target, !world))
        {
            Deny(COMPOUND_STRING("The hands spin, then stop.$"));
            return;
        }
    }
    if (!KantoProgress_EnsureInitialized())
        return;
    // Seed old watch saves from their existing heal point, which may belong
    // to either world. Never turn a Hoenn center into a Kanto respawn point.
    const struct WarpData *lastHeal = &gSaveBlock1Ptr->lastHealLocation;
    u32 healWorld = ParallelWatch_IsKanto(lastHeal->mapGroup, lastHeal->mapNum);
    if (GetHealLocationIndexByWarpData((struct WarpData *)lastHeal) != HEAL_LOCATION_NONE)
    {
        memcpy(&gSaveBlock3Ptr->kanto.healLocations[healWorld], lastHeal, sizeof(struct WarpData));
        gSaveBlock3Ptr->kanto.healValid[healWorld] = TRUE;
    }
    struct WarpData targetHeal;
    memcpy(&targetHeal, &gSaveBlock3Ptr->kanto.healLocations[!world], sizeof(targetHeal));
    if (gSaveBlock3Ptr->kanto.healValid[!world]
     && GetHealLocationIndexByWarpData(&targetHeal) != HEAL_LOCATION_NONE
     && ParallelWatch_IsKanto(targetHeal.mapGroup, targetHeal.mapNum) == !world)
        gSaveBlock1Ptr->lastHealLocation = targetHeal;
    else if (!world)
        SetLastHealLocationWarp(HEAL_LOCATION_PALLET_TOWN);
    else
        SetLastHealLocationWarp(gSaveBlock2Ptr->playerGender == MALE
            ? HEAL_LOCATION_LITTLEROOT_TOWN_BRENDANS_HOUSE_2F
            : HEAL_LOCATION_LITTLEROOT_TOWN_MAYS_HOUSE_2F);
    gSaveBlock3Ptr->watchAnchors[world] = from;
    SetWarpDestinationToCoords(target.mapGroup, target.mapNum, target.x, target.y);
    sArrivalFacing = target.facing;
    gSpecialVar_Result = TRUE;
    DoWarp();
    gFieldCallback = WatchArrival;
    ResetInitialPlayerAvatarState();
}
#else
bool32 ParallelWatch_IsKanto(u32 group, u32 num) { return FALSE; }
bool32 ParallelWatch_IsOutdoor(u32 group, u32 num) { return FALSE; }
bool32 ParallelWatch_IsSafeAnchor(const struct ParallelWatchAnchor *a, u32 world) { return FALSE; }
void Script_ParallelWatchCheck(struct ScriptContext *ctx) { gSpecialVar_Result = FALSE; }
void Script_ParallelWatchSwitch(struct ScriptContext *ctx) { gSpecialVar_Result = FALSE; }
void Script_VoidWatchIsHere(struct ScriptContext *ctx) { gSpecialVar_Result = FALSE; }
void Script_VoidWatchEnter(struct ScriptContext *ctx) { gSpecialVar_Result = FALSE; }
void Script_VoidWatchReturn(struct ScriptContext *ctx) { gSpecialVar_Result = FALSE; }
#endif

