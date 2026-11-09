#include "global.h"
#include "pip.h"
#include "malloc.h"
#include "fieldmap.h"
#include "event_object_movement.h"
#include "event_data.h"
#include "follower_npc.h"
#include "string_util.h"
#include "test/test.h"
#include "constants/event_objects.h"
#include "constants/map_types.h"
#include "constants/region_map_sections.h"
#include "script.h"

#if FNPC_ENABLE_NPC_FOLLOWERS
static void SetUpPipMemory(void)
{
    SetFollowerNPCData(FNPC_DATA_IN_PROGRESS, TRUE);
    SetFollowerNPCData(FNPC_DATA_EVENT_FLAG, FLAG_HIDE_COZY_COMPANION);
    gSaveBlock3Ptr->pipMemoryVersion = 0;
    Pip_ResetSceneState();
}
TEST("Pip remembers a spoken line across scene resets and saved-memory restoration")
{
    // Two full save snapshots outgrew the small GBA stack after the cast suffix.
    struct SaveBlock3 *previous = Alloc(sizeof(*previous));
    struct SaveBlock3 *saved = Alloc(sizeof(*saved));
    EXPECT_NE(previous, NULL);
    EXPECT_NE(saved, NULL);
    *previous = *gSaveBlock3Ptr;
    u8 oldText[sizeof(gStringVar4)];
    memcpy(oldText, gStringVar4, sizeof(oldText));
    SetUpPipMemory();
    const u8 *line = Pip_GetLocationDialogue(MAPSEC_ROUTE_101, 0);
    EXPECT_EQ(Pip_HasHeard(line), FALSE);
    EXPECT_EQ(Pip_TrySay(line), TRUE);
    EXPECT_EQ(Pip_TrySay(line), FALSE);
    Pip_ResetSceneState();
    EXPECT_EQ(Pip_HasHeard(line), TRUE);
    *saved = *gSaveBlock3Ptr;
    memset(gSaveBlock3Ptr->pipHeard, 0, sizeof(gSaveBlock3Ptr->pipHeard));
    *gSaveBlock3Ptr = *saved;
    EXPECT_EQ(Pip_TrySay(line), FALSE);
    *gSaveBlock3Ptr = *previous;
    Free(saved);
    Free(previous);
    memcpy(gStringVar4, oldText, sizeof(oldText));
}
TEST("Pip declines unknown lines and absent followers do not consume fresh dialogue")
{
    struct SaveBlock3 previous = *gSaveBlock3Ptr;
    SetUpPipMemory();
    const u8 *line = Pip_GetLocationDialogue(MAPSEC_ROUTE_102, 0);
    SetFollowerNPCData(FNPC_DATA_IN_PROGRESS, FALSE);
    EXPECT_EQ(Pip_TrySay(line), FALSE);
    EXPECT_EQ(Pip_HasHeard(line), FALSE);
    SetFollowerNPCData(FNPC_DATA_IN_PROGRESS, TRUE);
    EXPECT_EQ(Pip_TrySay(COMPOUND_STRING("Unregistered line")), FALSE);
    EXPECT_EQ(Pip_TrySay(line), TRUE);
    *gSaveBlock3Ptr = previous;
}
TEST("Pip stops speaking when local dialogue runs out instead of cycling")
{
    struct SaveBlock3 previous = *gSaveBlock3Ptr;
    struct MapHeader oldMap = gMapHeader;
    u16 oldResult = gSpecialVar_Result;
    u16 oldCounter = VarGet(VAR_PIP_COMMENT_COUNTER);
    u8 oldText[sizeof(gStringVar4)];
    memcpy(oldText, gStringVar4, sizeof(oldText));
    SetUpPipMemory();
    gMapHeader.regionMapSectionId = MAPSEC_LITTLEROOT_TOWN;
    gMapHeader.mapType = MAP_TYPE_TOWN;
    u32 spoken = 0;
    for (u32 i = 0; i < 12; i++)
    {
        Script_PipChooseDialogue(NULL);
        spoken += gSpecialVar_Result == TRUE;
    }
    EXPECT(spoken >= 4 && spoken <= 8);
    u16 counter = VarGet(VAR_PIP_COMMENT_COUNTER);
    for (u32 i = 0; i < 5; i++)
    {
        Script_PipChooseDialogue(NULL);
        EXPECT_EQ(gSpecialVar_Result, FALSE);
        EXPECT_EQ(VarGet(VAR_PIP_COMMENT_COUNTER), counter);
    }
    *gSaveBlock3Ptr = previous;
    gMapHeader = oldMap;
    gSpecialVar_Result = oldResult;
    VarSet(VAR_PIP_COMMENT_COUNTER, oldCounter);
    memcpy(gStringVar4, oldText, sizeof(oldText));
}
TEST("Declining an exact bookshelf reaction prevents a repeated offer without marking it heard")
{
    struct SaveBlock3 previous = *gSaveBlock3Ptr;
    struct ScriptContext ctx = {0};
    u16 oldTalked = gSpecialVar_LastTalked;
    u16 oldResult = gSpecialVar_Result;
    SetUpPipMemory();
    extern const u8 Text_BookShelf[];
    ctx.data[0] = (u32)Text_BookShelf;
    gSpecialVar_LastTalked = 77;
    gSpecialVar_Result = 41;
    Script_PipBeginObjectReaction(&ctx);
    EXPECT_EQ(gSpecialVar_Result, TRUE);
    Script_PipEndNPCReaction(&ctx); // No choice to hear the line was made.
    EXPECT_EQ(gSpecialVar_Result, 41);
    Pip_ResetSceneState();
    Script_PipBeginObjectReaction(&ctx);
    EXPECT_EQ(gSpecialVar_Result, FALSE);
    Script_PipEndNPCReaction(&ctx);
    u32 heard = 0;
    for (u32 i = 0; i < sizeof(gSaveBlock3Ptr->pipHeard); i++)
        heard |= gSaveBlock3Ptr->pipHeard[i];
    EXPECT_EQ(heard, 0);
    *gSaveBlock3Ptr = previous;
    gSpecialVar_LastTalked = oldTalked;
    gSpecialVar_Result = oldResult;
}
#endif
