#include "global.h"
#include "roaming_tutor.h"
#include "event_data.h"
#include "move.h"
#include "malloc.h"
#include "script_menu.h"
#include "string_util.h"
#include "constants/species.h"

// Reviewable mechanics, no online service or runtime randomness. Anatomical
// technique flags are separate from type affinity; neither alone grants a move.
enum TutorTechnique
{
    TUTOR_BODY = 1 << 0, TUTOR_JAWS = 1 << 1, TUTOR_LIMBS = 1 << 2,
    TUTOR_MIND = 1 << 3, TUTOR_SPIRIT = 1 << 4, TUTOR_MINERAL = 1 << 5,
    TUTOR_WATER = 1 << 6, TUTOR_COLD = 1 << 7, TUTOR_FIRE = 1 << 8,
    TUTOR_ELECTRIC = 1 << 9, TUTOR_PLANT = 1 << 10, TUTOR_WINGS = 1 << 11,
    TUTOR_BUG = 1 << 12, TUTOR_VENOM = 1 << 13, TUTOR_DRAGON = 1 << 14,
    TUTOR_CHARM = 1 << 15, TUTOR_THROW = 1 << 16,
};
struct TutorLesson { u16 move; u8 level; u32 technique; const u8 *reason; };
struct TutorProfile { u32 types; u32 techniques; };
#define TYPE_BIT(type) (1u << (type))
#define LESSON(move, level, technique, reason) {MOVE_##move, level, technique, COMPOUND_STRING(reason)}
#include "data/roaming_tutor_lessons.h"

static bool32 HasType(u32 species, u32 type)
{
    return gSpeciesInfo[species].types[0] == type || gSpeciesInfo[species].types[1] == type;
}

static bool32 HasEggGroup(u32 species, u32 group)
{
    return gSpeciesInfo[species].eggGroups[0] == group || gSpeciesInfo[species].eggGroups[1] == group;
}

static struct TutorProfile Profile(u32 species)
{
    struct TutorProfile p = {TYPE_BIT(TYPE_NORMAL), 0};
    u32 i;
    for (i = 0; i < 2; i++) p.types |= TYPE_BIT(gSpeciesInfo[species].types[i]);
    if (!HasEggGroup(species, EGG_GROUP_AMORPHOUS) || HasEggGroup(species, EGG_GROUP_HUMAN_LIKE)) p.techniques |= TUTOR_BODY;
    if (HasEggGroup(species, EGG_GROUP_FIELD) || HasEggGroup(species, EGG_GROUP_MONSTER)
     || HasEggGroup(species, EGG_GROUP_DRAGON) || HasEggGroup(species, EGG_GROUP_WATER_2)
     || HasEggGroup(species, EGG_GROUP_BUG)) p.techniques |= TUTOR_JAWS;
    if (HasEggGroup(species, EGG_GROUP_HUMAN_LIKE) || HasEggGroup(species, EGG_GROUP_MONSTER)) p.techniques |= TUTOR_LIMBS;
    // These insects/crustaceans have actual striking limbs or cutting forelegs.
    switch (species)
    {
    case SPECIES_SCYTHER: case SPECIES_SCIZOR: case SPECIES_PINSIR:
    case SPECIES_HERACROSS: case SPECIES_KRICKETUNE: case SPECIES_KABUTOPS:
    case SPECIES_ANORITH: case SPECIES_ARMALDO: p.techniques |= TUTOR_LIMBS; break;
    }
    if (HasType(species, TYPE_PSYCHIC) || HasType(species, TYPE_GHOST))
    { p.techniques |= TUTOR_MIND | TUTOR_SPIRIT; p.types |= TYPE_BIT(TYPE_PSYCHIC) | TYPE_BIT(TYPE_GHOST) | TYPE_BIT(TYPE_DARK); }
    if (HasType(species, TYPE_DARK) || HasEggGroup(species, EGG_GROUP_AMORPHOUS))
    { p.techniques |= TUTOR_SPIRIT; p.types |= TYPE_BIT(TYPE_DARK) | TYPE_BIT(TYPE_GHOST); }
    if (HasEggGroup(species, EGG_GROUP_FIELD) || HasEggGroup(species, EGG_GROUP_MONSTER) || HasEggGroup(species, EGG_GROUP_DRAGON))
    { p.types |= TYPE_BIT(TYPE_DARK) | TYPE_BIT(TYPE_GHOST); p.techniques |= TUTOR_SPIRIT; }
    if (HasType(species, TYPE_STEEL) || HasType(species, TYPE_ROCK) || HasType(species, TYPE_GROUND) || HasEggGroup(species, EGG_GROUP_MINERAL))
    { p.techniques |= TUTOR_MINERAL; p.types |= TYPE_BIT(TYPE_STEEL) | TYPE_BIT(TYPE_ROCK) | TYPE_BIT(TYPE_GROUND); }
    if (HasEggGroup(species, EGG_GROUP_MONSTER) || HasType(species, TYPE_FIGHTING))
    { p.techniques |= TUTOR_MINERAL; p.types |= TYPE_BIT(TYPE_ROCK) | TYPE_BIT(TYPE_GROUND); }
    if (HasType(species, TYPE_WATER) || HasEggGroup(species, EGG_GROUP_WATER_1) || HasEggGroup(species, EGG_GROUP_WATER_2) || HasEggGroup(species, EGG_GROUP_WATER_3))
    { p.techniques |= TUTOR_WATER | TUTOR_COLD; p.types |= TYPE_BIT(TYPE_WATER) | TYPE_BIT(TYPE_ICE); }
    if (HasType(species, TYPE_ICE))
    { p.techniques |= TUTOR_COLD | TUTOR_WATER; p.types |= TYPE_BIT(TYPE_WATER); }
    if (HasType(species, TYPE_FIRE) || HasType(species, TYPE_DRAGON))
    { p.techniques |= TUTOR_FIRE; p.types |= TYPE_BIT(TYPE_FIRE); }
    if (HasType(species, TYPE_ELECTRIC))
    { p.techniques |= TUTOR_ELECTRIC; p.types |= TYPE_BIT(TYPE_STEEL); }
    if (HasType(species, TYPE_GRASS) || HasEggGroup(species, EGG_GROUP_GRASS))
    { p.techniques |= TUTOR_PLANT | TUTOR_VENOM; p.types |= TYPE_BIT(TYPE_GRASS) | TYPE_BIT(TYPE_POISON); }
    if (HasType(species, TYPE_FLYING) || HasEggGroup(species, EGG_GROUP_FLYING))
    { p.techniques |= TUTOR_WINGS; p.types |= TYPE_BIT(TYPE_FLYING); }
    if (species == SPECIES_DRIFLOON || species == SPECIES_DRIFBLIM || species == SPECIES_GYARADOS) p.techniques &= ~TUTOR_WINGS;
    if (HasType(species, TYPE_BUG) || HasEggGroup(species, EGG_GROUP_BUG))
    { p.techniques |= TUTOR_BUG | TUTOR_VENOM; p.types |= TYPE_BIT(TYPE_BUG) | TYPE_BIT(TYPE_POISON); }
    if (HasType(species, TYPE_POISON)) p.techniques |= TUTOR_VENOM;
    if (HasType(species, TYPE_DRAGON) || HasEggGroup(species, EGG_GROUP_DRAGON))
    { p.techniques |= TUTOR_DRAGON; p.types |= TYPE_BIT(TYPE_DRAGON); }
    if (HasType(species, TYPE_FAIRY) || HasEggGroup(species, EGG_GROUP_FAIRY))
    { p.techniques |= TUTOR_CHARM | TUTOR_MIND; p.types |= TYPE_BIT(TYPE_FAIRY) | TYPE_BIT(TYPE_PSYCHIC); }
    if (HasType(species, TYPE_FIGHTING) || HasEggGroup(species, EGG_GROUP_HUMAN_LIKE)) p.types |= TYPE_BIT(TYPE_FIGHTING) | TYPE_BIT(TYPE_DARK);
    if (p.techniques & TUTOR_MINERAL) p.techniques |= TUTOR_THROW;
    if (p.techniques & TUTOR_WINGS) { p.techniques |= TUTOR_THROW; p.types |= TYPE_BIT(TYPE_ROCK); }
    if (p.techniques & TUTOR_JAWS) p.types |= TYPE_BIT(TYPE_DARK);
    if (HasType(species, TYPE_FIGHTING)) p.techniques |= TUTOR_LIMBS;
    return p;
}

static bool32 NormallyLearns(u32 species, u16 move)
{
    const struct LevelUpMove *levelMoves = GetSpeciesLevelUpLearnset(species);
    const u16 *eggMoves = GetSpeciesEggMoves(species);
    u32 i;
    if (CanLearnTeachableMove(species, move)) return TRUE;
    for (i = 0; levelMoves[i].move != LEVEL_UP_MOVE_END; i++) if (levelMoves[i].move == move) return TRUE;
    for (i = 0; eggMoves[i] != MOVE_UNAVAILABLE; i++) if (eggMoves[i] == move) return TRUE;
    return FALSE;
}

static u32 PowerCap(u32 level)
{
    return level < 15 ? 40 : level < 25 ? 50 : level < 35 ? 60 : level < 45 ? 70 : level < 55 ? 80 : 90;
}

static EWRAM_DATA u16 sOffers[4] = {0};
static EWRAM_DATA u8 sMonSlot = 0;
static EWRAM_DATA u16 sChosenMove = 0;
static EWRAM_DATA u32 sPersonality = 0;
static EWRAM_DATA u32 sOtId = 0;

static const struct TutorLesson *Lessons(struct Pokemon *mon, u32 *count)
{
    u32 species = GetMonData(mon, MON_DATA_SPECIES);
    switch (species)
    {
    case SPECIES_MAGIKARP:
        *count = ARRAY_COUNT(sFishLessons); return sFishLessons;
    case SPECIES_BELDUM:
    case SPECIES_METANG:
    case SPECIES_METAGROSS:
        *count = ARRAY_COUNT(sMetalLessons); return sMetalLessons;
    default:
        *count = ARRAY_COUNT(sGeneralLessons); return sGeneralLessons;
    }
}

bool32 RoamingTutor_CanTeach(struct Pokemon *mon)
{
    u32 last = GetMonData(mon, MON_DATA_ROAMING_TUTOR_LEVEL);
    u32 species = GetMonData(mon, MON_DATA_SPECIES);
    u32 level = GetMonData(mon, MON_DATA_LEVEL);
    if (species == SPECIES_NONE || GetMonData(mon, MON_DATA_IS_EGG)
     || GetMonData(mon, MON_DATA_SANITY_IS_BAD_EGG)
     || species == SPECIES_DITTO)
        return FALSE;
    // last is encoded +1; arithmetic stays wide so level 100 never wraps.
    return last == 0 || level >= last - 1 + 20;
}

u32 RoamingTutor_Offers(struct Pokemon *mon, u16 offers[4])
{
    u32 i, j, pick, count, found = 0, level = GetMonData(mon, MON_DATA_LEVEL);
    u32 species = GetMonData(mon, MON_DATA_SPECIES);
    u32 selectedTypes = 0, knownTypes = 0;
    struct TutorProfile profile;
    const struct TutorLesson *lessons;
    if (!RoamingTutor_CanTeach(mon) || level < 5) return 0;
    profile = Profile(species);
    lessons = Lessons(mon, &count);
    for (i = 0; i < 4; i++)
    {
        u16 move = GetMonData(mon, MON_DATA_MOVE1 + i);
        offers[i] = MOVE_NONE;
        if (move != MOVE_NONE && GetMoveCategory(move) != DAMAGE_CATEGORY_STATUS) knownTypes |= TYPE_BIT(GetMoveType(move));
    }
    // Rank genuine extra techniques by safe power, STAB, physical/special fit,
    // missing coverage and menu type diversity. Never pad with generic lessons.
    for (pick = 0; pick < 4; pick++)
    {
        s32 bestScore = -100000;
        u32 best = count;
        for (i = 0; i < count; i++)
        {
            u16 move = lessons[i].move;
            u32 type = GetMoveType(move), power = GetMovePower(move);
            s32 score;
            if (lessons[i].level > level || move >= MOVES_COUNT_GEN4 || power > PowerCap(level)) continue;
            if (lessons[i].technique && (!(profile.techniques & lessons[i].technique) || !(profile.types & TYPE_BIT(type)))) continue;
            if (NormallyLearns(species, move)) continue;
            for (j = 0; j < 4; j++) if (GetMonData(mon, MON_DATA_MOVE1 + j) == move || offers[j] == move) break;
            if (j != 4) continue;
            score = lessons[i].level + 20;
            if (GetMoveCategory(move) != DAMAGE_CATEGORY_STATUS)
            {
                u32 stat = GetMoveCategory(move) == DAMAGE_CATEGORY_PHYSICAL ? gSpeciesInfo[species].baseAttack : gSpeciesInfo[species].baseSpAttack;
                score += 80 + power * (60 + stat) / 60;
                if (HasType(species, type)) score += 45;
                if (!(knownTypes & TYPE_BIT(type))) score += 25;
            }
            if (selectedTypes & TYPE_BIT(type)) score -= 200;
            if (score > bestScore) { bestScore = score; best = i; }
        }
        if (best == count) break;
        offers[found++] = lessons[best].move;
        selectedTypes |= TYPE_BIT(GetMoveType(lessons[best].move));
    }
    return found == 4 ? 4 : 0;
}

bool32 RoamingTutor_Teach(struct Pokemon *mon, u16 move, u32 slot)
{
    u16 offers[4];
    u8 level;
    u32 i;
    if (slot >= MAX_MON_MOVES || RoamingTutor_Offers(mon, offers) != 4) return FALSE;
    for (i = 0; i < 4; i++) if (offers[i] == move) break;
    if (i == 4) return FALSE;
    if (!P_CAN_FORGET_HIDDEN_MOVE && IsMoveHM(GetMonData(mon, MON_DATA_MOVE1 + slot))) return FALSE;
    RemoveMonPPBonus(mon, slot);
    SetMonMoveSlot(mon, move, slot);
    level = GetMonData(mon, MON_DATA_LEVEL) + 1;
    SetMonData(mon, MON_DATA_ROAMING_TUTOR_LEVEL, &level);
    return TRUE;
}

static void Menu(const u16 *moves)
{
    u32 i;
    struct ListMenuItem *items = AllocZeroed(4 * sizeof(*items));
    if (items == NULL) { gSpecialVar_Result = 127; return; }
    for (i = 0; i < 4; i++)
    {
        u8 *name = Alloc(32);
        if (name == NULL)
        {
            while (i) Free((void *)items[--i].name);
            Free(items); gSpecialVar_Result = 127; return;
        }
        StringCopy(name, moves[i] == MOVE_NONE ? COMPOUND_STRING("Empty slot") : GetMoveName(moves[i]));
        items[i] = (struct ListMenuItem){name, i};
    }
    if (!ScriptMenu_MultichoiceDynamic(1, 1, 4, items, FALSE, 4, 0, DYN_MULTICHOICE_CB_NONE))
    {
        gSpecialVar_Result = 127; // The menu API already frees items on failure.
    }
}

void Script_RoamingTutorPrepare(void)
{
    struct Pokemon *mon;
    gSpecialVar_Result = 0;
    sChosenMove = MOVE_NONE;
    sMonSlot = gSpecialVar_0x8004;
    if (sMonSlot >= PARTY_SIZE) return;
    mon = &gParties[B_TRAINER_PLAYER][sMonSlot];
    StringCopy(gStringVar2, gSpeciesInfo[GetMonData(mon, MON_DATA_SPECIES)].speciesName);
    sPersonality = GetMonData(mon, MON_DATA_PERSONALITY);
    sOtId = GetMonData(mon, MON_DATA_OT_ID);
    if (RoamingTutor_Offers(mon, sOffers) != 4) return;
    gSpecialVar_Result = 1;
}

void Script_RoamingTutorMenu(void) { Menu(sOffers); }

void Script_RoamingTutorExplain(void)
{
    u32 i, count;
    const struct TutorLesson *lessons;
    sChosenMove = MOVE_NONE;
    if (gSpecialVar_Result >= 4) return;
    sChosenMove = sOffers[gSpecialVar_Result];
    StringCopy(gStringVar1, GetMoveName(sChosenMove));
    lessons = Lessons(&gParties[B_TRAINER_PLAYER][sMonSlot], &count);
    for (i = 0; i < count; i++) if (lessons[i].move == sChosenMove)
    {
        StringCopy(gStringVar4, lessons[i].reason); break;
    }
}

void Script_RoamingTutorSlotMenu(void)
{
    u16 moves[4];
    u32 i;
    for (i = 0; i < 4; i++) moves[i] = GetMonData(&gParties[B_TRAINER_PLAYER][sMonSlot], MON_DATA_MOVE1 + i);
    Menu(moves);
}

void Script_RoamingTutorCommit(void)
{
    struct Pokemon *mon = &gParties[B_TRAINER_PLAYER][sMonSlot];
    u32 slot = gSpecialVar_0x8005;
    gSpecialVar_Result = 0;
    if (GetMonData(mon, MON_DATA_PERSONALITY) != sPersonality || GetMonData(mon, MON_DATA_OT_ID) != sOtId) return;
    gSpecialVar_Result = RoamingTutor_Teach(mon, sChosenMove, slot);
    sChosenMove = MOVE_NONE;
}
