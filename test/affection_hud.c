#include "global.h"
#include "affection_hud.h"
#include "bonds.h"
#include "malloc.h"
#include "test/test.h"

TEST("Affection HUD numbers follow every saved level boundary")
{
    u32 current, needed;
    for (u32 level = 1; level < BOND_LEVEL_CAP; level++)
    {
        u32 start = Bonds_TotalForLevel(level);
        u32 next = Bonds_TotalForLevel(level + 1);
        AffectionHud_Progress(start, &current, &needed);
        EXPECT_EQ(AffectionHud_LevelForExp(start), level);
        EXPECT_EQ(current, 0);
        EXPECT_EQ(needed, next - start);
        AffectionHud_Progress(next - 1, &current, &needed);
        EXPECT_EQ(current, needed - 1);
        EXPECT_EQ(AffectionHud_LevelForExp(next), level + 1);
    }
    AffectionHud_Progress(BOND_EXP_CAP, &current, &needed);
    EXPECT_EQ(current, BOND_EXP_CAP);
    EXPECT_EQ(needed, BOND_EXP_CAP);
}

TEST("Affection HUD retains gains for all ten companions while gameplay is busy")
{
    AffectionHud_Clear();
    for (u32 who = 0; who < BOND_COUNT; who++)
    {
        AffectionHud_Notify(who, 0, 10 + who);
        AffectionHud_Notify(who, 10 + who, 25 + who);
    }
    EXPECT_EQ(AffectionHud_PendingCount(), BOND_COUNT);
    for (u32 who = 0; who < BOND_COUNT; who++)
        EXPECT_EQ(AffectionHud_PendingExp(who), 25 + who);
    AffectionHud_Clear();
    EXPECT_EQ(AffectionHud_PendingCount(), 0);
}

TEST("Affection HUD reports only actual awarded EXP and leaves saved progress intact")
{
    struct BondProgress *old = Alloc(sizeof(*old));
    *old = *Bonds_GetProgress();
    Bonds_Reset();
    Bonds_GetProgress()->people[2].exp = BOND_EXP_CAP - 3;
    EXPECT_EQ(Bonds_AddExp(2, 100), 3);
    EXPECT_EQ(AffectionHud_PendingExp(2), 3);
    EXPECT_EQ(Bonds_AddExp(2, 100), 0);
    EXPECT_EQ(AffectionHud_PendingExp(2), 3);
    AffectionHud_Notify(BOND_COUNT, 0, 20);
    AffectionHud_Notify(3, 20, 20);
    AffectionHud_Notify(4, 20, 0);
    EXPECT_EQ(AffectionHud_PendingCount(), 1);
    AffectionHud_Clear();
    EXPECT_EQ(Bonds_GetProgress()->people[2].exp, BOND_EXP_CAP);
    *Bonds_GetProgress() = *old;
    Free(old);
}
