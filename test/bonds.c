#include "global.h"
#include "bonds.h"
#include "malloc.h"
#include "pokemon_storage_system.h"
#include "test/test.h"

static struct BondProgress *Begin(void)
{
    struct BondProgress *previous = Alloc(sizeof(*previous));
    *previous = *Bonds_GetProgress();
    Bonds_Reset();
    return previous;
}
static void End(struct BondProgress *previous)
{
    *Bonds_GetProgress() = *previous;
    Bonds_CancelMessage();
    Free(previous);
}

TEST("Bond EXP uses the approved curve at every boundary and caps at level twenty")
{
    struct BondProgress *previous = Begin();
    EXPECT_EQ(Bonds_Level(0), 1);
    for (u32 level = 2; level <= 20; level++)
    {
        u32 boundary = Bonds_TotalForLevel(level);
        Bonds_GetProgress()->people[0].exp = boundary - 1;
        EXPECT_EQ(Bonds_Level(0), level - 1);
        Bonds_AddExp(0, 1);
        EXPECT_EQ(Bonds_Level(0), level);
    }
    EXPECT_EQ(Bonds_TotalForLevel(4), 240);
    EXPECT_EQ(Bonds_TotalForLevel(8), 700);
    EXPECT_EQ(Bonds_TotalForLevel(12), 1320);
    EXPECT_EQ(Bonds_TotalForLevel(16), 2100);
    EXPECT_EQ(Bonds_TotalForLevel(20), 3040);
    EXPECT_EQ(Bonds_AddExp(0, 60000), 0);
    EXPECT_EQ(Bonds_GetProgress()->people[0].exp, 3040);
    EXPECT_EQ(Bonds_GetProgress()->people[1].exp, 0);
    End(previous);
}

TEST("Bond initialization changes only the appended record and preserves existing PC and cast bytes")
{
    struct BondProgress *previous = Begin();
    // Heap snapshots avoid overflowing the small GBA test stack.
    u8 *pc = Alloc(34144);
    struct SaveBlock3 *old = Alloc(sizeof(*old));
    memcpy(pc, gPokemonStoragePtr, 34144);
    *old = *gSaveBlock3Ptr;
    memset(Bonds_GetProgress(), 0xFF, sizeof(struct BondProgress));
    Bonds_EnsureInitialized();
    EXPECT_EQ(memcmp(pc, gPokemonStoragePtr, 34144), 0);
    EXPECT_EQ(memcmp(old, gSaveBlock3Ptr, sizeof(*old)), 0);
    EXPECT_EQ(Bonds_GetProgress()->magic, BOND_SAVE_MAGIC);
    EXPECT_EQ(Bonds_GetProgress()->version, 1);
    EXPECT_EQ(Bonds_GetProgress()->people[9].exp, 0);
    Free(pc);
    Free(old);
    End(previous);
}

TEST("Bond gifts respect both outing and heart-band caps without altering benched friends")
{
    struct BondProgress *previous = Begin();
    struct BondPerson *p = &Bonds_GetProgress()->people[0];
    EXPECT_EQ(Bonds_GiftPreview(0, 30), 30);
    EXPECT(Bonds_RecordGift(0, 30));
    EXPECT_EQ(Bonds_GiftPreview(0, 30), 0);
    EXPECT_EQ(Bonds_RecordGift(0, 30), FALSE);
    EXPECT_EQ(p->exp, 30);
    p->giftUsed = FALSE;
    p->giftExp[0] = 145;
    EXPECT_EQ(Bonds_GiftPreview(0, 30), 5);
    EXPECT(Bonds_RecordGift(0, 30));
    EXPECT_EQ(p->giftExp[0], 150);
    p->giftUsed = FALSE;
    EXPECT_EQ(Bonds_GiftPreview(0, 30), 0);
    EXPECT_EQ(Bonds_GetProgress()->people[1].exp, 0);
    End(previous);
}

TEST("Bond events remain ordered when EXP is ahead and cannot repeat completion rewards")
{
    struct BondProgress *previous = Begin();
    Bonds_AddExp(0, BOND_EXP_CAP);
    EXPECT_EQ(Bonds_CompleteEvent(0, 4), FALSE);
    EXPECT(Bonds_CompleteEvent(0, 0));
    EXPECT_EQ(Bonds_CompleteEvent(0, 0), FALSE);
    EXPECT(Bonds_CompleteEvent(0, 1));
    EXPECT(Bonds_CompleteEvent(0, 2));
    EXPECT(Bonds_CompleteEvent(0, 3));
    EXPECT(Bonds_CompleteEvent(0, 4));
    EXPECT_EQ(Bonds_GetProgress()->people[0].hearts, 5);
    EXPECT_EQ(Bonds_GetProgress()->people[0].exp, 3040);
    End(previous);
}

TEST("Bond observations award only once after finished text and cancellation awards nothing")
{
    struct BondProgress *previous = Begin();
    Bonds_QueueObservation(0, FALSE);
    Bonds_CancelMessage();
    Bonds_MessageFinished();
    EXPECT_EQ(Bonds_GetProgress()->people[0].exp, 0);
    Bonds_QueueObservation(0, FALSE);
    Bonds_MessageFinished();
    Bonds_MessageFinished();
    EXPECT_EQ(Bonds_GetProgress()->people[0].exp, 10);
    Bonds_QueueObservation(0, TRUE);
    Bonds_MessageFinished();
    EXPECT_EQ(Bonds_GetProgress()->people[0].exp, 35);
    End(previous);
}

TEST("One committed romance is enforced while breakup preserves friendship and completed events")
{
    struct BondProgress *previous = Begin();
    for (u32 i = 0; i < 2; i++)
    {
        Bonds_GetProgress()->people[i].hearts = 4;
        Bonds_GetProgress()->people[i].exp = 3040;
    }
    EXPECT(Bonds_SetInterest(0, BOND_COMMITTED));
    EXPECT_EQ(Bonds_SetInterest(1, BOND_COMMITTED), FALSE);
    EXPECT(Bonds_SetInterest(0, BOND_FRIENDSHIP));
    EXPECT_EQ(Bonds_GetProgress()->people[0].hearts, 4);
    EXPECT_EQ(Bonds_GetProgress()->people[0].exp, 3040);
    EXPECT(Bonds_SetInterest(1, BOND_COMMITTED));
    EXPECT_EQ(Bonds_GetProgress()->committed, 2);
    End(previous);
}

TEST("Unique bond objectives and landmarks cannot renew outings or grant EXP twice")
{
    struct BondProgress *previous = Begin();
    struct BondPerson *p = &Bonds_GetProgress()->people[0];
    EXPECT(Bonds_Objective(0, 3));
    p->walkingExp = 40;
    p->giftUsed = TRUE;
    EXPECT_EQ(Bonds_Objective(0, 3), FALSE);
    EXPECT_EQ(p->walkingExp, 40);
    EXPECT_EQ(p->giftUsed, TRUE);
    EXPECT(Bonds_Landmark(0, 4));
    EXPECT_EQ(p->walkingExp, 0);
    EXPECT_EQ(p->giftUsed, FALSE);
    EXPECT_EQ(Bonds_Landmark(0, 4), FALSE);
    EXPECT_EQ(p->exp, 70);
    End(previous);
}
