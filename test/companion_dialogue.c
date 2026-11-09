#include "global.h"
#include "companion_dialogue.h"
#include "cast.h"
#include "pokemon_storage_system.h"
#include "malloc.h"
#include "test/test.h"

extern const u8 OldaleTown_Text_DiscoveredFootprints[], OldaleTown_Text_FinishedSketchingFootprints[];
extern const u8 ViridianCity_Text_GymClosedWonderWhoLeaderIs[], ViridianCity_Text_ViridiansGymLeaderReturned[];
extern const u8 gText_ObtainedTheItem[], gText_PutItemInPocket[], gText_TheBagIsFull[];
extern const u8 gText_TooBadBagIsFull[], gText_NoRoomLeftForAnother[];
extern const u8 Text_BookShelf[], Text_PokemonCenterBookShelf[];

TEST("Successful item receipts preserve the speaker but bag-full failures are not receipts")
{
    EXPECT_EQ(CompanionDialogue_IsSystemReceipt(gText_ObtainedTheItem), TRUE);
    EXPECT_EQ(CompanionDialogue_IsSystemReceipt(gText_PutItemInPocket), TRUE);
    EXPECT_EQ(CompanionDialogue_IsSystemReceipt(gText_TheBagIsFull), FALSE);
    EXPECT_EQ(CompanionDialogue_IsSystemReceipt(gText_TooBadBagIsFull), FALSE);
    EXPECT_EQ(CompanionDialogue_IsSystemReceipt(gText_NoRoomLeftForAnother), FALSE);
    EXPECT_EQ(CompanionDialogue_IsSystemReceipt(NULL), FALSE);
}

TEST("Receipt classification never guesses from an NPC mentioning an obtained item")
{
    static const u8 npc[] = _("Obtained the {STR_VAR_2}!$");
    EXPECT_EQ(CompanionDialogue_IsSystemReceipt(npc), FALSE);
    EXPECT_EQ(CompanionDialogue_IsSystemReceipt(OldaleTown_Text_DiscoveredFootprints), FALSE);
}

TEST("Dialogue settings migrate only the new suffix and preserve PC, bond and cast progress")
{
    u8 *prefix = Alloc(34560);
    struct SaveBlock3 *oldSave = Alloc(sizeof(*oldSave));
    struct CompanionDialogueProgress *old = Alloc(sizeof(*old));
    *old = gPokemonStoragePtr->companionDialogue;
    memcpy(prefix, gPokemonStoragePtr, 34560);
    *oldSave = *gSaveBlock3Ptr;
    memset(&gPokemonStoragePtr->companionDialogue, 0, sizeof(*old));
    EXPECT_EQ(CompanionDialogue_GetMode(), COMPANION_DIALOGUE_NORMAL);
    EXPECT_EQ(gPokemonStoragePtr->companionDialogue.version, 2);
    EXPECT_EQ(memcmp(prefix, gPokemonStoragePtr, 34560), 0);
    EXPECT_EQ(memcmp(oldSave, gSaveBlock3Ptr, sizeof(*oldSave)), 0);
    EXPECT_EQ(CompanionDialogue_HasSpent(10, 735), FALSE);
    gPokemonStoragePtr->companionDialogue = *old;
    Free(old); Free(oldSave); Free(prefix);
}

TEST("Dialogue silencer accepts three modes and cancellation preserves mode and all memory")
{
    struct CompanionDialogueProgress *old = Alloc(sizeof(*old));
    *old = gPokemonStoragePtr->companionDialogue;
    CompanionDialogue_Reset();
    gPokemonStoragePtr->companionDialogue.spent[5][17] = 0x45;
    for (u32 mode = 0; mode <= COMPANION_DIALOGUE_SILENT; mode++)
    {
        EXPECT_EQ(CompanionDialogue_SetMode(mode), TRUE);
        EXPECT_EQ(CompanionDialogue_GetMode(), mode);
        EXPECT_EQ(gPokemonStoragePtr->companionDialogue.spent[5][17], 0x45);
    }
    EXPECT_EQ(CompanionDialogue_SetMode(3), FALSE); // Cancel menu item.
    EXPECT_EQ(CompanionDialogue_SetMode(127), FALSE); // B button.
    EXPECT_EQ(CompanionDialogue_GetMode(), COMPANION_DIALOGUE_SILENT);
    EXPECT_EQ(gPokemonStoragePtr->companionDialogue.spent[5][17], 0x45);
    gPokemonStoragePtr->companionDialogue = *old;
    CompanionDialogue_ResetSession(); Free(old);
}

TEST("Footprint and gym reactions distinguish actual dialogue branches without guessing by sprite")
{
    u32 search = CompanionDialogue_ContextForMessage(OldaleTown_Text_DiscoveredFootprints);
    u32 reveal = CompanionDialogue_ContextForMessage(OldaleTown_Text_FinishedSketchingFootprints);
    u32 closed = CompanionDialogue_ContextForMessage(ViridianCity_Text_GymClosedWonderWhoLeaderIs);
    u32 open = CompanionDialogue_ContextForMessage(ViridianCity_Text_ViridiansGymLeaderReturned);
    EXPECT_LT(search, COMPANION_CONTEXT_CAPACITY);
    EXPECT_LT(reveal, COMPANION_CONTEXT_CAPACITY);
    EXPECT_LT(closed, COMPANION_CONTEXT_CAPACITY);
    EXPECT_LT(open, COMPANION_CONTEXT_CAPACITY);
    EXPECT_NE(search, reveal);
    EXPECT_NE(closed, open);
    EXPECT_EQ(CompanionDialogue_ContextForMessage(NULL), COMPANION_NO_CONTEXT);
    EXPECT_EQ(CompanionDialogue_ContextForMessage((const u8 *)"an unmapped conversation"), COMPANION_NO_CONTEXT);
}

TEST("A reaction spent by one companion does not silence another companion's perspective")
{
    struct CompanionDialogueProgress *old = Alloc(sizeof(*old));
    *old = gPokemonStoragePtr->companionDialogue;
    CompanionDialogue_Reset();
    u32 id = CompanionDialogue_ContextForMessage(OldaleTown_Text_FinishedSketchingFootprints);
    gPokemonStoragePtr->companionDialogue.spent[6][id / 8] |= 1 << (id % 8);
    EXPECT_EQ(CompanionDialogue_HasSpent(6, id), TRUE); // Emi.
    EXPECT_EQ(CompanionDialogue_HasSpent(1, id), FALSE); // Silas.
    EXPECT_EQ(CompanionDialogue_HasSpent(0, id), FALSE); // Pip.
    EXPECT_EQ(CompanionDialogue_HasSpent(11, id), TRUE);
    EXPECT_EQ(CompanionDialogue_HasSpent(0, COMPANION_CONTEXT_CAPACITY), TRUE);
    gPokemonStoragePtr->companionDialogue = *old;
    CompanionDialogue_ResetSession(); Free(old);
}

TEST("Released object history imports once without sharing future independent contexts")
{
    struct SaveBlock3 *saved = Alloc(sizeof(*saved));
    struct CompanionDialogueProgress *previous = Alloc(sizeof(*previous));
    *saved = *gSaveBlock3Ptr;
    *previous = gPokemonStoragePtr->companionDialogue;
    Cast_EnsureInitialized();
    memset(gSaveBlock3Ptr->cast.used, 0, sizeof(gSaveBlock3Ptr->cast.used));
    gSaveBlock3Ptr->cast.active = 1;
    EXPECT_EQ(Cast_Offer(174), TRUE); // Released Silas bookshelf source.
    CompanionDialogue_Reset();
    gPokemonStoragePtr->companionDialogue.version = 1;
    memset(gPokemonStoragePtr->companionDialogue.reserved, 0, 2);
    u32 books = CompanionDialogue_ContextForMessage(Text_BookShelf);
    u32 magazines = CompanionDialogue_ContextForMessage(Text_PokemonCenterBookShelf);
    EXPECT_EQ(CompanionDialogue_HasSpent(1, books), TRUE);
    EXPECT_EQ(CompanionDialogue_HasSpent(1, magazines), TRUE);
    EXPECT_EQ(CompanionDialogue_HasSpent(6, books), FALSE);
    EXPECT_EQ(CompanionDialogue_HasSpent(6, magazines), FALSE);
    // After migration, a fresh context bit does not spend another description.
    gPokemonStoragePtr->companionDialogue.spent[6][books / 8] |= 1 << (books % 8);
    EXPECT_EQ(CompanionDialogue_HasSpent(6, books), TRUE);
    EXPECT_EQ(CompanionDialogue_HasSpent(6, magazines), FALSE);
    // Later legacy changes cannot silently rerun a completed import.
    gSaveBlock3Ptr->cast.active = 6;
    EXPECT_EQ(Cast_Offer(174), TRUE);
    EXPECT_EQ(CompanionDialogue_HasSpent(6, magazines), FALSE);
    *gSaveBlock3Ptr = *saved;
    gPokemonStoragePtr->companionDialogue = *previous;
    Free(previous); Free(saved);
}
