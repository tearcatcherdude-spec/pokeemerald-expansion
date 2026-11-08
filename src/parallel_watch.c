#include "global.h"
#include "main.h"
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
static EWRAM_DATA u8 sArrivalFacing = DIR_SOUTH;

bool32 ParallelWatch_IsOutdoor(u32 group, u32 num)
{
    // Only ordinary Hoenn towns/routes and the three trial outdoor maps.
    // No facilities, interiors, caves, boats, link rooms or story-only maps.
    if (group == MAP_GROUP(MAP_WATCH_PALLET))
        return num <= MAP_NUM(MAP_WATCH_VIRIDIAN);
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
     || (a->mapGroup == MAP_GROUP(MAP_WATCH_PALLET)) != world
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
static bool32 CanSwitch(void)
{
    struct ParallelWatchAnchor a = CurrentAnchor();
    bool32 healthy = FALSE;
    if (gMain.inBattle || IsOverworldLinkActive())
        return Deny(COMPOUND_STRING("The watch is quiet for now.$"));
    for (u32 i = 0; i < PARTY_SIZE; i++)
        if (GetMonData(&gParties[B_TRAINER_PLAYER][i], MON_DATA_SPECIES) != SPECIES_NONE
         && !GetMonData(&gParties[B_TRAINER_PLAYER][i], MON_DATA_IS_EGG)
         && GetMonData(&gParties[B_TRAINER_PLAYER][i], MON_DATA_HP))
            healthy = TRUE;
    if (!healthy)
        return Deny(COMPOUND_STRING("Bring a healthy POKéMON before\ntrying the watch.$"));
    if (!TestPlayerAvatarFlags(PLAYER_AVATAR_FLAG_ON_FOOT))
        return Deny(COMPOUND_STRING("Step off your bike or out of the\nwater before using the watch.$"));
    if (!ParallelWatch_IsSafeAnchor(&a, a.mapGroup == MAP_GROUP(MAP_WATCH_PALLET)))
        return Deny(COMPOUND_STRING("Find clear ground outside, away from\ndoors and people, to use the watch.$"));
    return TRUE;
}
void Script_ParallelWatchCheck(struct ScriptContext *ctx)
{
    gSpecialVar_Result = CanSwitch();
}
static void WatchArrival(void)
{
    FieldCB_WarpExitFadeFromBlack();
    PlayerFaceDirection(sArrivalFacing);
}
void Script_ParallelWatchSwitch(struct ScriptContext *ctx)
{
    struct ParallelWatchAnchor from = CurrentAnchor();
    struct ParallelWatchAnchor target;
    u32 world = from.mapGroup == MAP_GROUP(MAP_WATCH_PALLET);
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
            Deny(COMPOUND_STRING("The other world has no safe landing.\nThe watch stays here with you.$"));
            return;
        }
    }
    gSaveBlock3Ptr->watchAnchors[world] = from;
    SetWarpDestinationToCoords(target.mapGroup, target.mapNum, target.x, target.y);
    sArrivalFacing = target.facing;
    gSpecialVar_Result = TRUE;
    DoWarp();
    gFieldCallback = WatchArrival;
    ScriptContext_Stop();
}
#else
bool32 ParallelWatch_IsOutdoor(u32 group, u32 num) { return FALSE; }
bool32 ParallelWatch_IsSafeAnchor(const struct ParallelWatchAnchor *a, u32 world) { return FALSE; }
void Script_ParallelWatchCheck(struct ScriptContext *ctx) { gSpecialVar_Result = FALSE; }
void Script_ParallelWatchSwitch(struct ScriptContext *ctx) { gSpecialVar_Result = FALSE; }
#endif
