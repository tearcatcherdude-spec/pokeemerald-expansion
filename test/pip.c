#include "global.h"
#include "pip.h"
#include "event_data.h"
#include "event_object_movement.h"
#include "follower_npc.h"
#include "script.h"
#include "sprite.h"
#include "string_util.h"
#include "test/test.h"
#include "constants/event_objects.h"
#include "constants/region_map_sections.h"

#if FNPC_ENABLE_NPC_FOLLOWERS
TEST("Pip has a distinct nine-frame Emerald sprite and palette")
{
    const struct ObjectEventGraphicsInfo *info = GetObjectEventGraphicsInfo(OBJ_EVENT_GFX_PIP);
    EXPECT_EQ(info->width, 16);
    EXPECT_EQ(info->height, 32);
    EXPECT_EQ(info->size, 256);
    EXPECT_EQ(info->paletteTag, OBJ_EVENT_PAL_TAG_PIP);
    EXPECT_NE(info->paletteTag, OBJ_EVENT_PAL_TAG_NPC_3);
    // Emerald stores ascending frames in one relative-frame descriptor.
    EXPECT_EQ(info->images[0].size, 256);
    EXPECT(info->images[0].relativeFrames);
}

TEST("Pip recognises his follower identity without taking over other NPC followers")
{
    struct SaveBlock3 previous = *gSaveBlock3Ptr;
    SetFollowerNPCData(FNPC_DATA_IN_PROGRESS, TRUE);
    SetFollowerNPCData(FNPC_DATA_EVENT_FLAG, FLAG_HIDE_COZY_COMPANION + 1);
    EXPECT_EQ(Pip_IsFollowing(), FALSE);
    SetFollowerNPCData(FNPC_DATA_EVENT_FLAG, FLAG_HIDE_COZY_COMPANION);
    EXPECT_EQ(Pip_IsFollowing(), TRUE);
    SetFollowerNPCData(FNPC_DATA_IN_PROGRESS, FALSE);
    EXPECT_EQ(Pip_IsFollowing(), FALSE);
    *gSaveBlock3Ptr = previous;
}

TEST("Pip location dialogue covers all Hoenn towns and routes")
{
    const u8 *fallback = Pip_GetLocationDialogue(0xFFFF, 0);
    for (u32 section = MAPSEC_LITTLEROOT_TOWN; section <= MAPSEC_ROUTE_134; section++)
    {
        EXPECT(Pip_GetLocationDialogue(section, 0) != NULL);
        EXPECT_NE(Pip_GetLocationDialogue(section, 0), fallback);
    }
    EXPECT_NE(Pip_GetLocationDialogue(MAPSEC_ROUTE_101, 0), Pip_GetLocationDialogue(MAPSEC_ROUTE_134, 0));
    EXPECT_NE(Pip_GetLocationDialogue(MAPSEC_LITTLEROOT_TOWN, 0), Pip_GetLocationDialogue(MAPSEC_LITTLEROOT_TOWN, 1));
    EXPECT_EQ(Pip_GetLocationDialogue(MAPSEC_LITTLEROOT_TOWN, 0), Pip_GetLocationDialogue(MAPSEC_LITTLEROOT_TOWN, 2));
}

TEST("Pip progress dialogue changes across badges and after the League")
{
    for (u32 badges = 0; badges < NUM_BADGES; badges++)
        EXPECT_NE(Pip_GetProgressDialogue(badges, FALSE), Pip_GetProgressDialogue(badges + 1, FALSE));
    EXPECT_EQ(Pip_GetProgressDialogue(NUM_BADGES, FALSE), Pip_GetProgressDialogue(0xFFFF, FALSE));
    EXPECT_NE(Pip_GetProgressDialogue(NUM_BADGES, FALSE), Pip_GetProgressDialogue(NUM_BADGES, TRUE));
}

TEST("Optional Pip reactions preserve the NPC script result and message state")
{
    struct ScriptContext ctx = {0};
    struct SaveBlock3 previous = *gSaveBlock3Ptr;
    gSaveBlock3Ptr->pipMemoryVersion = 0;
    struct ObjectEvent oldNpc = gObjectEvents[1];
    u16 oldResult = gSpecialVar_Result;
    u16 oldTalked = gSpecialVar_LastTalked;
    u8 oldText[sizeof(gStringVar4)];
    memcpy(oldText, gStringVar4, sizeof(oldText));
    SetFollowerNPCData(FNPC_DATA_IN_PROGRESS, TRUE);
    SetFollowerNPCData(FNPC_DATA_EVENT_FLAG, FLAG_HIDE_COZY_COMPANION);
    Pip_ResetSceneState();
    gObjectEvents[1].active = TRUE;
    gObjectEvents[1].localId = 77;
    gObjectEvents[1].mapNum = gSaveBlock1Ptr->location.mapNum;
    gObjectEvents[1].mapGroup = gSaveBlock1Ptr->location.mapGroup;
    gObjectEvents[1].graphicsId = OBJ_EVENT_GFX_HIKER;
    gSpecialVar_LastTalked = 77;
    gSpecialVar_Result = 42;
    ctx.data[0] = 0x12345678;
    StringCopy(gStringVar4, COMPOUND_STRING("Original NPC message"));
    Script_PipBeginNPCReaction(&ctx);
    EXPECT_EQ(gSpecialVar_Result, TRUE);
    Script_PipChooseNPCDialogue(&ctx);
    ctx.data[0] = 0;
    gSpecialVar_LastTalked = 0;
    gSpecialVar_Result = 0;
    Script_PipEndNPCReaction(&ctx);
    EXPECT_EQ(gSpecialVar_Result, 42);
    EXPECT_EQ(gSpecialVar_LastTalked, 77);
    EXPECT_EQ(ctx.data[0], 0x12345678);
    EXPECT_EQ(StringCompare(gStringVar4, COMPOUND_STRING("Original NPC message")), 0);
    *gSaveBlock3Ptr = previous;
    gObjectEvents[1] = oldNpc;
    gSpecialVar_Result = oldResult;
    gSpecialVar_LastTalked = oldTalked;
    memcpy(gStringVar4, oldText, sizeof(oldText));
}

TEST("Pip steps aside for scripted actors without blocking their tiles")
{
    struct SaveBlock3 previous = *gSaveBlock3Ptr;
    struct ObjectEvent oldObject = gObjectEvents[15];
    struct Sprite oldSprite = gSprites[0];
    SetFollowerNPCData(FNPC_DATA_IN_PROGRESS, TRUE);
    SetFollowerNPCData(FNPC_DATA_EVENT_FLAG, FLAG_HIDE_COZY_COMPANION);
    SetFollowerNPCData(FNPC_DATA_OBJ_ID, 15);
    SetFollowerNPCData(FNPC_DATA_SURF_BLOB, FNPC_SURF_BLOB_NONE);
    memset(&gObjectEvents[15], 0, sizeof(gObjectEvents[15]));
    gObjectEvents[15].active = TRUE;
    gObjectEvents[15].localId = OBJ_EVENT_ID_NPC_FOLLOWER;
    Pip_BeforeScriptedMovement(LOCALID_PLAYER);
    EXPECT_EQ(Pip_IsSceneSuspended(), TRUE);
    EXPECT(gObjectEvents[15].invisible);
    EXPECT_EQ(FollowerNPC_IsCollisionExempt(&gObjectEvents[15], &gObjectEvents[1]), TRUE);
    Pip_ResetSceneState();
    EXPECT_EQ(Pip_IsSceneSuspended(), FALSE);
    *gSaveBlock3Ptr = previous;
    gObjectEvents[15] = oldObject;
    gSprites[0] = oldSprite;
}
#endif
