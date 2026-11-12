// Session-only shuffle bag. Never consumes battle RNG or changes save layouts.
static EWRAM_DATA u8 sTrainerMusicBag[8] = {0};
static EWRAM_DATA u8 sTrainerMusicRemaining = 0;
static EWRAM_DATA u16 sTrainerMusicCached = 0;
static EWRAM_DATA u8 sTrainerMusicLast = 0;
static EWRAM_DATA u32 sTrainerMusicSeed = 0;
static EWRAM_DATA bool8 sTrainerMusicHasLast = FALSE;
static EWRAM_DATA bool8 sTrainerMusicCacheValid = FALSE;

static u32 TrainerMusicRandom(void)
{
    if (!sTrainerMusicSeed)
        sTrainerMusicSeed = gMain.vblankCounter1 ^ 0xA17E53C9;
    sTrainerMusicSeed = sTrainerMusicSeed * 1664525 + 1013904223;
    return sTrainerMusicSeed;
}

void TrainerVariety_ResetBattleMusic(void)
{
    sTrainerMusicCacheValid = FALSE;
}

u16 TrainerVariety_GetBattleMusic(bool32 kanto)
{
    static const u16 songs[7] = {
        MUS_VARIETY_STEADY, MUS_VARIETY_BRISK, MUS_VARIETY_WISTFUL,
        MUS_VARIETY_CHEERFUL, MUS_VARIETY_SILLY, MUS_VARIETY_TENSE,
        MUS_VARIETY_LAIDBACK,
    };
    u32 i, j;
    u8 temp, choice;

    if (sTrainerMusicCacheValid)
        return sTrainerMusicCached;
    if (!sTrainerMusicRemaining)
    {
        for (i = 0; i < ARRAY_COUNT(sTrainerMusicBag); i++)
            sTrainerMusicBag[i] = i;
        for (i = ARRAY_COUNT(sTrainerMusicBag) - 1; i > 0; i--)
        {
            j = (TrainerMusicRandom() >> 16) % (i + 1);
            temp = sTrainerMusicBag[i];
            sTrainerMusicBag[i] = sTrainerMusicBag[j];
            sTrainerMusicBag[j] = temp;
        }
        // Draw from the end. Avoid repeats across bag boundaries too.
        if (sTrainerMusicHasLast && sTrainerMusicBag[7] == sTrainerMusicLast)
        {
            temp = sTrainerMusicBag[7];
            sTrainerMusicBag[7] = sTrainerMusicBag[0];
            sTrainerMusicBag[0] = temp;
        }
        sTrainerMusicRemaining = ARRAY_COUNT(sTrainerMusicBag);
    }
    choice = sTrainerMusicBag[--sTrainerMusicRemaining];
    sTrainerMusicLast = choice;
    sTrainerMusicHasLast = TRUE;
    sTrainerMusicCacheValid = TRUE;
    sTrainerMusicCached = choice == 7 ? (kanto ? MUS_RG_VS_TRAINER : MUS_VS_TRAINER) : songs[choice];
    return sTrainerMusicCached;
}
