#include "global.h"
#include "pokemon.h"
#include "roaming_tutor.h"
#include "move.h"
#include "test/test.h"

TEST("Roaming tutor gives Beldum and Magikarp four distinct Gen IV or earlier choices")
{
    struct Pokemon mon;
    u16 offers[4];
    u32 species, i, j;
    for (species = 0; species < 2; species++)
    {
        CreateMon(&mon, species ? SPECIES_BELDUM : SPECIES_MAGIKARP, 6, 0x12345678, OTID_STRUCT_PRESET(123));
        EXPECT_EQ(RoamingTutor_Offers(&mon, offers), 4);
        for (i = 0; i < 4; i++)
        {
            EXPECT(offers[i] < MOVES_COUNT_GEN4);
            for (j = 0; j < i; j++) EXPECT(offers[i] != offers[j]);
        }
    }
}

TEST("Roaming tutor cooldown belongs to the individual and survives boxed copy and evolution")
{
    struct Pokemon mon, other;
    struct BoxPokemon boxed;
    u16 offers[4], species = SPECIES_METANG;
    u8 level = 25;
    CreateMon(&mon, SPECIES_BELDUM, 6, 0x12345678, OTID_STRUCT_PRESET(123));
    CreateMon(&other, SPECIES_BELDUM, 6, 0x87654321, OTID_STRUCT_PRESET(123));
    EXPECT_EQ(GetMonData(&mon, MON_DATA_ROAMING_TUTOR_LEVEL), 0);
    EXPECT_EQ(RoamingTutor_Offers(&mon, offers), 4);
    EXPECT(RoamingTutor_Teach(&mon, offers[0], 3));
    EXPECT_EQ(GetMonData(&mon, MON_DATA_ROAMING_TUTOR_LEVEL), 7);
    EXPECT(!RoamingTutor_CanTeach(&mon));
    EXPECT(RoamingTutor_CanTeach(&other));
    boxed = mon.box;
    other.box = boxed;
    SetMonData(&other, MON_DATA_SPECIES, &species);
    SetMonData(&other, MON_DATA_LEVEL, &level);
    EXPECT(!RoamingTutor_CanTeach(&other));
    level = 26;
    SetMonData(&other, MON_DATA_LEVEL, &level);
    EXPECT(RoamingTutor_CanTeach(&other));
    EXPECT_EQ(GetMonData(&other, MON_DATA_OT_ID), 123);
    EXPECT_EQ(GetMonData(&other, MON_DATA_PERSONALITY), 0x12345678);
}

TEST("Roaming tutor rejects invalid lesson and slot without consuming cooldown")
{
    struct Pokemon mon;
    u16 offers[4];
    CreateMon(&mon, SPECIES_MAGIKARP, 6, 0x12345678, OTID_STRUCT_PRESET(123));
    EXPECT(!RoamingTutor_Teach(&mon, MOVE_FISSURE, 0));
    EXPECT_EQ(RoamingTutor_Offers(&mon, offers), 4);
    EXPECT(!RoamingTutor_Teach(&mon, offers[0], 4));
    EXPECT_EQ(GetMonData(&mon, MON_DATA_ROAMING_TUTOR_LEVEL), 0);
}

TEST("Roaming tutor level 100 cooldown cannot wrap and Pokémon substruct size stays compatible")
{
    struct Pokemon mon;
    u16 offers[4];
    CreateMon(&mon, SPECIES_MAGIKARP, 100, 0x12345678, OTID_STRUCT_PRESET(123));
    EXPECT_EQ(sizeof(struct PokemonSubstruct1), 12);
    EXPECT_EQ(RoamingTutor_Offers(&mon, offers), 4);
    EXPECT(RoamingTutor_Teach(&mon, offers[0], 3));
    EXPECT(!RoamingTutor_CanTeach(&mon));
    EXPECT_EQ(GetMonData(&mon, MON_DATA_ROAMING_TUTOR_LEVEL), 101);
}

TEST("Roaming tutor preserves HM access and resets only the replaced slot PP bonuses")
{
    struct Pokemon mon;
    u16 offers[4];
    u8 bonuses = 255;
    CreateMon(&mon, SPECIES_MAGIKARP, 6, 0x12345678, OTID_STRUCT_PRESET(123));
    SetMonMoveSlot(&mon, MOVE_SURF, 2);
    EXPECT_EQ(RoamingTutor_Offers(&mon, offers), 4);
    EXPECT(!RoamingTutor_Teach(&mon, offers[0], 2));
    EXPECT_EQ(GetMonData(&mon, MON_DATA_ROAMING_TUTOR_LEVEL), 0);
    EXPECT_EQ(GetMonData(&mon, MON_DATA_MOVE3), MOVE_SURF);
    SetMonData(&mon, MON_DATA_PP_BONUSES, &bonuses);
    EXPECT(RoamingTutor_Teach(&mon, offers[0], 3));
    EXPECT_EQ(GetMonData(&mon, MON_DATA_PP_BONUSES), 63);
}

TEST("Roaming tutor actual configured move power respects conservative level bands")
{
    const u16 species[] = {SPECIES_BELDUM, SPECIES_METANG, SPECIES_METAGROSS, SPECIES_MAGIKARP, SPECIES_EEVEE};
    struct Pokemon mon;
    u16 offers[4];
    u32 i, j, level, cap;
    for (i = 0; i < ARRAY_COUNT(species); i++)
    {
        for (level = 5; level <= 100; level++)
        {
            cap = level < 15 ? 40 : level < 25 ? 50 : level < 35 ? 60 : level < 45 ? 70 : level < 50 ? 80 : 90;
            CreateMon(&mon, species[i], level, 0x12345678, OTID_STRUCT_PRESET(123));
            if (RoamingTutor_Offers(&mon, offers) == 4)
                for (j = 0; j < 4; j++)
                {
                    EXPECT(offers[j] < MOVES_COUNT_GEN4);
                    EXPECT(GetMovePower(offers[j]) <= cap);
                }
        }
    }
}

TEST("Roaming tutor builds different extra-move menus for different species")
{
    const u16 species[] = {SPECIES_BELDUM, SPECIES_MAGIKARP, SPECIES_TOTODILE, SPECIES_CHARMANDER};
    struct Pokemon mon;
    u16 menus[4][4];
    u32 a, b, i;
    for (a = 0; a < ARRAY_COUNT(species); a++)
    {
        CreateMon(&mon, species[a], 25, 0x12345678, OTID_STRUCT_PRESET(123));
        EXPECT_EQ(RoamingTutor_Offers(&mon, menus[a]), 4);
    }
    for (a = 0; a < 4; a++) for (b = a + 1; b < 4; b++)
    {
        bool32 different = FALSE;
        for (i = 0; i < 4; i++) if (menus[a][i] != menus[b][i]) different = TRUE;
        EXPECT(different);
    }
}

TEST("Roaming tutor offers genuine extras rather than normal level TM tutor or egg moves")
{
    const u16 species[] = {SPECIES_BELDUM, SPECIES_MAGIKARP, SPECIES_TOTODILE, SPECIES_CHARMANDER,
        SPECIES_PIKACHU, SPECIES_RALTS, SPECIES_GASTLY, SPECIES_GEODUDE, SPECIES_PIDGEY, SPECIES_EEVEE};
    struct Pokemon mon;
    u16 offers[4];
    u32 s, level, i, j;
    for (s = 0; s < ARRAY_COUNT(species); s++) for (level = 15; level <= 65; level += 10)
    {
        const struct LevelUpMove *normal = GetSpeciesLevelUpLearnset(species[s]);
        const u16 *eggs = GetSpeciesEggMoves(species[s]);
        CreateMon(&mon, species[s], level, 0x12345678, OTID_STRUCT_PRESET(123));
        if (RoamingTutor_Offers(&mon, offers) != 4) continue;
        for (i = 0; i < 4; i++)
        {
            EXPECT(!CanLearnTeachableMove(species[s], offers[i]));
            for (j = 0; normal[j].move != LEVEL_UP_MOVE_END; j++) EXPECT(normal[j].move != offers[i]);
            for (j = 0; eggs[j] != MOVE_UNAVAILABLE; j++) EXPECT(eggs[j] != offers[i]);
            for (j = 0; j < 4; j++) EXPECT(GetMonData(&mon, MON_DATA_MOVE1 + j) != offers[i]);
        }
    }
}

TEST("Roaming tutor Beldum has steel psychic dark ghost ground and rock techniques across level bands")
{
    struct Pokemon mon;
    u16 offers[4];
    u32 level, i, types = 0;
    for (level = 5; level <= 65; level++)
    {
        CreateMon(&mon, SPECIES_BELDUM, level, 0x12345678, OTID_STRUCT_PRESET(123));
        EXPECT_EQ(RoamingTutor_Offers(&mon, offers), 4);
        for (i = 0; i < 4; i++) types |= 1u << GetMoveType(offers[i]);
    }
    EXPECT(types & (1u << TYPE_STEEL)); EXPECT(types & (1u << TYPE_PSYCHIC));
    EXPECT(types & (1u << TYPE_DARK)); EXPECT(types & (1u << TYPE_GHOST));
    EXPECT(types & (1u << TYPE_GROUND)); EXPECT(types & (1u << TYPE_ROCK));
}

TEST("Roaming tutor never gives Magikarp imaginary fists wings or fire techniques")
{
    struct Pokemon mon;
    u16 offers[4];
    u32 level, i;
    for (level = 5; level <= 100; level += 5)
    {
        CreateMon(&mon, SPECIES_MAGIKARP, level, 0x12345678, OTID_STRUCT_PRESET(123));
        EXPECT_EQ(RoamingTutor_Offers(&mon, offers), 4);
        for (i = 0; i < 4; i++)
        {
            EXPECT(offers[i] != MOVE_FIRE_PUNCH); EXPECT(offers[i] != MOVE_MACH_PUNCH);
            EXPECT(GetMoveType(offers[i]) != TYPE_FIRE); EXPECT(GetMoveType(offers[i]) != TYPE_FLYING);
        }
    }
}

TEST("Roaming tutor low level Beldum has a safe steel option instead of only generic support")
{
    struct Pokemon mon;
    u16 offers[4];
    u32 i;
    bool32 hasSteel = FALSE;
    CreateMon(&mon, SPECIES_BELDUM, 9, 0x12345678, OTID_STRUCT_PRESET(123));
    EXPECT_EQ(RoamingTutor_Offers(&mon, offers), 4);
    for (i = 0; i < 4; i++)
    {
        if (GetMoveType(offers[i]) == TYPE_STEEL) hasSteel = TRUE;
        EXPECT(GetMovePower(offers[i]) <= 40);
    }
    EXPECT(hasSteel);
}
