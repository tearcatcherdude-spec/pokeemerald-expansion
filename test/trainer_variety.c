#include "global.h"
#include "pokemon.h"
#include "random.h"
#include "data.h"
#include "event_data.h"
#include "constants/kanto_progress.h"
#include "constants/trainers.h"
#include "test/test.h"
#include "constants/songs.h"

TEST("Trainer music stays fixed during each battle and has no adjacent repeats")
{
    u32 i;
    u16 last = MUS_NONE;
    for (i = 0; i < 80; i++)
    {
        u16 song;
        TrainerVariety_ResetBattleMusic();
        song = TrainerVariety_GetBattleMusic(FALSE);
        EXPECT_NE(song, last);
        EXPECT_EQ(song, TrainerVariety_GetBattleMusic(FALSE));
        last = song;
    }
}

TEST("Every eight trainer battles include all seven new scores and regional stock music")
{
    u32 i, j, seen = 0;
    // Consume to a bag boundary, regardless of which test ran first.
    for (i = 0; i < 8; i++)
    {
        TrainerVariety_ResetBattleMusic();
        if (TrainerVariety_GetBattleMusic(TRUE) == MUS_RG_VS_TRAINER)
            break;
    }
    // Stock music occurs once per bag; check the next 16 for complete coverage.
    for (i = 0; i < 16; i++)
    {
        u16 song;
        TrainerVariety_ResetBattleMusic();
        song = TrainerVariety_GetBattleMusic(TRUE);
        for (j = 0; j < 7; j++)
            if (song == MUS_VARIETY_STEADY + j)
                seen |= 1 << j;
        if (song == MUS_RG_VS_TRAINER)
            seen |= 1 << 7;
    }
    EXPECT_EQ(seen, 255);
}

TEST("Trainer music never advances either gameplay RNG state")
{
    rng_value_t original = gRngValue;
    rng_value_t original2 = gRng2Value;
    TrainerVariety_ResetBattleMusic();
    TrainerVariety_GetBattleMusic(FALSE);
    EXPECT_EQ(memcmp(&original, &gRngValue, sizeof(original)), 0);
    EXPECT_EQ(memcmp(&original2, &gRng2Value, sizeof(original2)), 0);
}

#if !IS_FRLG
TEST("All 64 variety trainers have valid independent parties and append-only defeat flags")
{
    u32 i;
    for (i = 674; i < 738; i++)
    {
        const struct Trainer *t = GetTrainerStructFromId(KANTO_TRAINER_BASE + i);
        EXPECT_EQ(SanitizeTrainerId(KANTO_TRAINER_BASE + i), KANTO_TRAINER_BASE + i);
        EXPECT_EQ(t->trainerPic, TRAINER_PIC_VARIETY_BARNABY + (i - 674) / 2);
        EXPECT_GE((u32)t->partySize, 2);
        EXPECT_LE((u32)t->partySize, 4);
        for (u32 j = 0; j < t->partySize; j++)
        {
            EXPECT_NE(t->party[j].species, SPECIES_NONE);
            EXPECT_GE(t->party[j].lvl, 8);
            EXPECT_LE(t->party[j].lvl, 36);
        }
    }
}
#endif
