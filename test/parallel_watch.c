#include "global.h"
#include "parallel_watch.h"
#include "overworld.h"
#include "test/test.h"
#include "constants/maps.h"

#if FNPC_ENABLE_NPC_FOLLOWERS
TEST("Parallel Watch limits switching to ordinary outdoor maps")
{
    EXPECT(ParallelWatch_IsOutdoor(MAP_GROUP(MAP_LITTLEROOT_TOWN), MAP_NUM(MAP_LITTLEROOT_TOWN)));
    EXPECT(ParallelWatch_IsOutdoor(MAP_GROUP(MAP_ROUTE134), MAP_NUM(MAP_ROUTE134)));
    EXPECT(ParallelWatch_IsOutdoor(MAP_GROUP(MAP_WATCH_PALLET), MAP_NUM(MAP_WATCH_PALLET)));
    EXPECT(ParallelWatch_IsOutdoor(MAP_GROUP(MAP_WATCH_VIRIDIAN), MAP_NUM(MAP_WATCH_VIRIDIAN)));
    EXPECT(!ParallelWatch_IsOutdoor(MAP_GROUP(MAP_WATCH_CENTER), MAP_NUM(MAP_WATCH_CENTER)));
    EXPECT(!ParallelWatch_IsOutdoor(255, 255));
    EXPECT(!ParallelWatch_IsOutdoor(0, 255));
}
TEST("Parallel Watch rejects corrupt positions and anchors from the wrong world")
{
    struct ParallelWatchAnchor a = {MAP_GROUP(MAP_WATCH_PALLET), MAP_NUM(MAP_WATCH_PALLET), 10, 14, DIR_SOUTH, TRUE};
    EXPECT(ParallelWatch_IsSafeAnchor(&a, 1));
    EXPECT(!ParallelWatch_IsSafeAnchor(&a, 0));
    a.x = -1;
    EXPECT(!ParallelWatch_IsSafeAnchor(&a, 1));
    a.x = 32767;
    EXPECT(!ParallelWatch_IsSafeAnchor(&a, 1));
    a.x = 10; a.valid = FALSE;
    EXPECT(!ParallelWatch_IsSafeAnchor(&a, 1));
    a.valid = TRUE; a.facing = 255;
    EXPECT(!ParallelWatch_IsSafeAnchor(&a, 1));
    a.facing = DIR_SOUTH; a.mapGroup = 127;
    EXPECT(!ParallelWatch_IsSafeAnchor(&a, 1));
}
TEST("Parallel Watch never lands on a door or a closed trial boundary")
{
    struct ParallelWatchAnchor a = {MAP_GROUP(MAP_WATCH_PALLET), MAP_NUM(MAP_WATCH_PALLET), 6, 7, DIR_SOUTH, TRUE};
    EXPECT(!ParallelWatch_IsSafeAnchor(&a, 1));
    a.x = 12; a.y = 19;
    EXPECT(!ParallelWatch_IsSafeAnchor(&a, 1));
    a.mapNum = MAP_NUM(MAP_WATCH_VIRIDIAN); a.x = 20; a.y = 0;
    EXPECT(!ParallelWatch_IsSafeAnchor(&a, 1));
}
TEST("Parallel Watch has a safe fallback in Hoenn")
{
    struct ParallelWatchAnchor a = {MAP_GROUP(MAP_LITTLEROOT_TOWN), MAP_NUM(MAP_LITTLEROOT_TOWN), 10, 16, DIR_SOUTH, TRUE};
    EXPECT(ParallelWatch_IsSafeAnchor(&a, 0));
}
#endif
