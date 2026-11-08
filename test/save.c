#include "global.h"
#include "pokemon_storage_system.h"
#include "test/test.h"

// If you would like to ensure save compatibility, update the values below with those for your hack. You can find these through the debug menu.
// Please note that this simple check is not 100% foolproof, but should be able to catch most unintended shifts.
#define T_SAVEBLOCK1_SIZE 15568
#define T_SAVEBLOCK2_SIZE 3884
#define T_SAVEBLOCK3_SIZE 4
#define T_SAVEBLOCK3_WITH_FOLLOWER_SIZE 1000
#define T_POKEMONSTORAGE_SIZE 34144

TEST("SaveBlock1 is backwards compatible")
{
    EXPECT_EQ(sizeof(struct SaveBlock1), T_SAVEBLOCK1_SIZE);
}

TEST("SaveBlock2 is backwards compatible")
{
    EXPECT_EQ(sizeof(struct SaveBlock2), T_SAVEBLOCK2_SIZE);
}

TEST("SaveBlock3 is backwards compatible")
{
#if FNPC_ENABLE_NPC_FOLLOWERS
    // Follower storage deliberately extends this block. Its legacy data must
    // retain its original offset; changing only the size baseline misses that.
    EXPECT_EQ(offsetof(struct SaveBlock3, dexNavChain), 0);
    EXPECT_EQ(offsetof(struct SaveBlock3, NPCfollower), T_SAVEBLOCK3_SIZE);
    EXPECT_EQ(offsetof(struct SaveBlock3, pipMemoryVersion), 28);
    EXPECT_EQ(offsetof(struct SaveBlock3, pipHeard), 30);
    EXPECT_EQ(offsetof(struct SaveBlock3, pipOffered), 94);
    EXPECT_EQ(offsetof(struct SaveBlock3, watchMemoryVersion), 160);
    EXPECT_EQ(offsetof(struct SaveBlock3, watchAnchors), 164);
    EXPECT_EQ(sizeof(struct ParallelWatchAnchor), 8);
    EXPECT_EQ(offsetof(struct SaveBlock3, kanto), 180);
    EXPECT_EQ(sizeof(struct KantoProgress), 820);
    EXPECT_EQ(sizeof(struct SaveBlock3), T_SAVEBLOCK3_WITH_FOLLOWER_SIZE);
#else
    EXPECT_EQ(sizeof(struct SaveBlock3), T_SAVEBLOCK3_SIZE);
#endif
}

TEST("PokemonStorage is backwards compatible")
{
    EXPECT_EQ(sizeof(struct PokemonStorage), T_POKEMONSTORAGE_SIZE);
}

#undef T_SAVEBLOCK1_SIZE
#undef T_SAVEBLOCK2_SIZE
#undef T_SAVEBLOCK3_SIZE
#undef T_SAVEBLOCK3_WITH_FOLLOWER_SIZE
#undef T_POKEMONSTORAGE_SIZE
