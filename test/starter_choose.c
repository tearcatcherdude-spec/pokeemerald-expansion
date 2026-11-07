#include "global.h"
#include "event_data.h"
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
