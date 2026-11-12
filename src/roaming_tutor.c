#include "global.h"
#include "roaming_tutor.h"
#include "event_data.h"
#include "move.h"
#include "malloc.h"
#include "script_menu.h"
#include "string_util.h"
#include "constants/species.h"

// Deliberately small, reviewable lessons. No random moves, OHKO, fixed damage,
// weather, evasion, sleep, stat-boost sweepers or post-Gen-IV moves.
struct TutorLesson { u16 move; u8 level; const u8 *reason; };
#define LESSON(move, level, reason) {MOVE_##move, level, COMPOUND_STRING(reason)}
static const struct TutorLesson sBodyLessons[] = {
    LESSON(TACKLE, 5, "A controlled body bump.\nStart small; keep your balance.$"),
    LESSON(SPLASH, 5, "Practice a harmless body wiggle.\nDignity is optional. Safety is not.$"),
    LESSON(FOCUS_ENERGY, 10, "Settle your breathing and focus.\nNo secret muscle required.$"),
    LESSON(MUD_SLAP, 10, "A flick of loose mud, using the\nbody. No hands necessary.$"),
    LESSON(ENDURE, 20, "Brace for one hard moment.\nIt takes patience, not raw power.$"),
    LESSON(SWIFT, 30, "Shape a little focused energy.\nAccuracy before spectacle.$"),
    LESSON(HEADBUTT, 35, "A careful head-first bump.\nControl first. Headaches second.$"),
};
static const struct TutorLesson sFishLessons[] = {
    LESSON(TACKLE, 5, "Those swimming muscles can manage\na short, controlled body bump.$"),
    LESSON(TAIL_WHIP, 5, "A fish has a tail. Use its motion\nto distract, not to hit harder.$"),
    LESSON(WATER_SPORT, 5, "Splash water around the field.\nA fish already knows the material.$"),
    LESSON(MUD_SLAP, 5, "Flick river mud with your tail.\nNo hands. No suspicious machinery.$"),
    LESSON(WATER_GUN, 15, "A small mouthful of water.\nAim gently; this is not a cannon.$"),
    LESSON(FOCUS_ENERGY, 15, "Steady your swimming rhythm.\nA calm fish is still a fish.$"),
    LESSON(ENDURE, 25, "Use that stubborn survival instinct\nto hold on for one more moment.$"),
    LESSON(AQUA_JET, 35, "A quick swimming burst.\nSpeed, not a tidal wave.$"),
    LESSON(BOUNCE, 50, "A trained leap from the water.\nWe work on the landing first.$"),
};
static const struct TutorLesson sMetalLessons[] = {
    LESSON(TACKLE, 5, "A gentle bump with a metal body.\nNo need to risk TAKE DOWN recoil.$"),
    LESSON(HARDEN, 5, "Brace that rigid metal shell.\nUseful structure, no new limbs.$"),
    LESSON(LEER, 5, "You already have a very good eye.\nHold the stare. Very professional.$"),
    LESSON(MUD_SLAP, 5, "Magnetic motion can flick loose\ngrit. Keep it small and controlled.$"),
    LESSON(FOCUS_ENERGY, 5, "Align your attention like a magnet.\nA clear target beats brute force.$"),
    LESSON(CONFUSION, 15, "A gentle psychic nudge.\nYou are a psychic species, after all.$"),
    LESSON(METAL_CLAW, 25, "Use your existing metal prongs.\nTechnique, not imaginary hands.$"),
    LESSON(ENDURE, 25, "Brace the whole metal body.\nThat frame can take a careful knock.$"),
    LESSON(IRON_HEAD, 45, "A controlled strike with your\nmetal frame. Only after practice.$"),
    LESSON(ZEN_HEADBUTT, 50, "Combine your rigid frame and\npsychic focus. No shortcuts.$"),
};
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
        *count = ARRAY_COUNT(sBodyLessons); return sBodyLessons;
    }
}

bool32 RoamingTutor_CanTeach(struct Pokemon *mon)
{
    u32 last = GetMonData(mon, MON_DATA_ROAMING_TUTOR_LEVEL);
    u32 species = GetMonData(mon, MON_DATA_SPECIES);
    u32 level = GetMonData(mon, MON_DATA_LEVEL);
    if (species == SPECIES_NONE || GetMonData(mon, MON_DATA_IS_EGG)
     || GetMonData(mon, MON_DATA_SANITY_IS_BAD_EGG)
     || species == SPECIES_UNOWN || species == SPECIES_DITTO
     || species == SPECIES_WOBBUFFET || species == SPECIES_WYNAUT)
        return FALSE;
    // last is encoded +1; arithmetic stays wide so level 100 never wraps.
    return last == 0 || level >= last - 1 + 20;
}

u32 RoamingTutor_Offers(struct Pokemon *mon, u16 offers[4])
{
    u32 i, j, count, found = 0, level = GetMonData(mon, MON_DATA_LEVEL);
    const struct TutorLesson *lessons = Lessons(mon, &count);
    if (!RoamingTutor_CanTeach(mon)) return 0;
    // Prefer recently unlocked lessons, retain four distinct unknown choices.
    for (i = count; i > 0 && found < 4; i--)
    {
        u16 move = lessons[i - 1].move;
        if (lessons[i - 1].level > level || move >= MOVES_COUNT_GEN4) continue;
        for (j = 0; j < MAX_MON_MOVES; j++)
            if (GetMonData(mon, MON_DATA_MOVE1 + j) == move) break;
        if (j == MAX_MON_MOVES) offers[found++] = move;
    }
    // Never advertise an incomplete menu or silently pad it with duplicates.
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
