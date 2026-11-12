#include "global.h"
#include "constants/characters.h"
#include "companion_dialogue.h"
#include "companion_packed_text.h"
#include "companion_packed_text_golden.h"
#include "test/test.h"

#if FNPC_ENABLE_NPC_FOLLOWERS && !IS_FRLG
TEST("All packed companion replies and expressions match the original catalogue")
{
    u8 text[1000], expression;
    u32 context, voice, i, count = 0, hash = 2166136261u;
    for (context = 0; context < PACKED_CONTEXT_COUNT; context++)
        for (voice = 0; voice < COMPANION_VOICE_COUNT; voice++)
            if (CompanionDialogue_CopyCatalogReply(context, voice, text, sizeof(text), &expression))
            {
                count++;
                for (i = 0; i < sizeof(text); i++)
                {
                    hash = (hash ^ text[i]) * 16777619u;
                    if (text[i] == EOS) break;
                }
                EXPECT(i < sizeof(text));
                hash = (hash ^ expression) * 16777619u;
            }
    EXPECT_EQ(count, PACKED_REPLY_COUNT);
    EXPECT_EQ(hash, PACKED_REPLY_FNV);
}

TEST("Packed companion text rejects invalid references and respects destination capacity")
{
    u8 text[4] = {0, 0x12, 0x34, 0x56};
    EXPECT(!CompanionPackedText_Copy(COMPANION_TEXT_NONE, text, sizeof(text)));
    EXPECT_EQ(text[0], EOS);
    EXPECT(!CompanionPackedText_Copy(0, text, 1));
    EXPECT_EQ(text[0], EOS);
    EXPECT_EQ(text[1], 0x12);
    EXPECT_EQ(text[2], 0x34);
    EXPECT_EQ(text[3], 0x56);
    EXPECT(!CompanionPackedText_Copy(0, text, 0));
}
#endif
