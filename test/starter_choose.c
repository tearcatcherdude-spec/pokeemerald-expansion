#include "global.h"
#include "event_data.h"
#include "battle.h"
#include "battle_setup.h"
#include "dma3.h"
#include "main.h"
#include "malloc.h"
#include "pokemon.h"
#include "task.h"
#include "starter_choose.h"
#include "test/test.h"

TEST("Expanded starters preserve the legacy choices and reject invalid indices")
{
    EXPECT_EQ(GetStarterPokemon(0), IS_FRLG ? SPECIES_BULBASAUR : SPECIES_TREECKO);
    EXPECT_EQ(GetStarterPokemon(1), IS_FRLG ? SPECIES_CHARMANDER : SPECIES_TORCHIC);
    EXPECT_EQ(GetStarterPokemon(2), IS_FRLG ? SPECIES_SQUIRTLE : SPECIES_MUDKIP);
    EXPECT_EQ(GetStarterPokemon(IS_FRLG ? 3 : 14), GetStarterPokemon(0));
    EXPECT_EQ(GetStarterPokemon(0xFFFF), GetStarterPokemon(0));
    if (!IS_FRLG)
    {
        EXPECT_EQ(GetStarterPokemon(9), SPECIES_TURTWIG);
        EXPECT_EQ(GetStarterPokemon(10), SPECIES_CHIMCHAR);
        EXPECT_EQ(GetStarterPokemon(11), SPECIES_PIPLUP);
        EXPECT_EQ(GetStarterPokemon(12), SPECIES_BELDUM);
        EXPECT_EQ(GetStarterPokemon(13), SPECIES_LARVITAR);
    }
}

TEST("Expanded starters always select an existing rival and story branch")
{
    u16 i;
    for (i = 0; i < 12; i++)
        EXPECT_EQ(GetStarterStoryId(i), i % 3);
    EXPECT_EQ(GetStarterStoryId(12), 1);
    EXPECT_EQ(GetStarterStoryId(13), 1);
}

TEST("Expanded starter identity survives separately from the rival branch")
{
    u16 oldSpecies = VarGet(VAR_CHOSEN_STARTER_SPECIES);
    u16 oldStory = VarGet(VAR_STARTER_MON);
    VarSet(VAR_STARTER_MON, 1);
    VarSet(VAR_CHOSEN_STARTER_SPECIES, SPECIES_BELDUM);
    EXPECT_EQ(GetPlayerStarterPokemon(), IS_FRLG ? SPECIES_CHARMANDER : SPECIES_BELDUM);
    VarSet(VAR_CHOSEN_STARTER_SPECIES, SPECIES_NONE);
    EXPECT_EQ(GetPlayerStarterPokemon(), IS_FRLG ? SPECIES_CHARMANDER : SPECIES_TORCHIC);
    VarSet(VAR_CHOSEN_STARTER_SPECIES, oldSpecies);
    VarSet(VAR_STARTER_MON, oldStory);
}

static u32 sStarterFrame;

static void CheckStarterHeap(void)
{
    const struct MemBlock *head = HeapHead();
    const struct MemBlock *block = head;
    do
    {
        if (block->magic != MALLOC_SYSTEM_ID)
            Test_MgbaPrintf("Starter frame %d: bad heap block %p magic %d size %d next %p", sStarterFrame, block, block->magic, block->size, block->next);
        EXPECT_EQ(block->magic, MALLOC_SYSTEM_ID);
        EXPECT(EWRAM_START <= (uintptr_t)block->next && (uintptr_t)block->next < EWRAM_END);
        EXPECT(block->next > block || block->next == head);
        block = block->next;
    } while (block != head);
}

static void RunStarterFrame(u16 keys)
{
    sStarterFrame++;
    gMain.newKeys = keys;
    gMain.newAndRepeatedKeys = keys;
    gMain.callback2();
    // Drive the same palette-transfer acknowledgement as the real VBlank.
    // Do not transfer palettes directly: that would hide a missing callback.
    if (gMain.vblankCallback != NULL)
        gMain.vblankCallback();
    ProcessDma3Requests();
    CheckStarterHeap();
}

static void CheckStarterRescueTransition(bool32 chooseBeldum)
{
    MainCallback oldCallback = gMain.callback2;
    MainCallback oldSavedCallback = gMain.savedCallback;
    IntrCallback oldVBlank = gMain.vblankCallback;
    u8 oldState = gMain.state;
    u32 oldBattleTypeFlags = gBattleTypeFlags;
    u32 i;

    if (IS_FRLG)
        return;

    sStarterFrame = 0;
    CheckStarterHeap();
    ZeroPlayerPartyMons();
    gBattleTypeFlags = 0;
    ChooseStarter();
    for (i = 0; i < 80; i++)
        RunStarterFrame(0);

    if (chooseBeldum)
        for (i = 0; i < 3; i++)
            RunStarterFrame(DPAD_DOWN);

    RunStarterFrame(A_BUTTON); // Open confirmation.
    RunStarterFrame(0);
    RunStarterFrame(A_BUTTON); // Confirm Yes.
    for (i = 0; i < 300 && !(gBattleTypeFlags & BATTLE_TYPE_FIRST_BATTLE); i++)
        RunStarterFrame(0);

    EXPECT(gBattleTypeFlags & BATTLE_TYPE_FIRST_BATTLE);
    EXPECT_EQ(GetPlayerStarterPokemon(), chooseBeldum ? SPECIES_BELDUM : SPECIES_BULBASAUR);
    EXPECT_EQ(GetMonData(&gParties[B_TRAINER_PLAYER][0], MON_DATA_SPECIES), chooseBeldum ? SPECIES_BELDUM : SPECIES_BULBASAUR);
    EXPECT_EQ(GetMonData(&gParties[B_TRAINER_PLAYER][0], MON_DATA_LEVEL), 5);
    if (chooseBeldum)
        EXPECT_EQ(GetMonData(&gParties[B_TRAINER_PLAYER][0], MON_DATA_MOVE1), MOVE_TACKLE);

    ResetTasks();
    gMain.callback2 = oldCallback;
    gMain.savedCallback = oldSavedCallback;
    gMain.state = oldState;
    gMain.newKeys = 0;
    gMain.newAndRepeatedKeys = 0;
    SetVBlankCallback(oldVBlank);
    gBattleTypeFlags = oldBattleTypeFlags;
}

TEST("Expanded starter Beldum confirmation reaches the rescue battle")
{
    CheckStarterRescueTransition(TRUE);
}

TEST("Expanded starter Bulbasaur confirmation reaches the rescue battle")
{
    CheckStarterRescueTransition(FALSE);
}
