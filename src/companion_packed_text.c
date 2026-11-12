#include "global.h"
#include "constants/characters.h"
#include "companion_packed_text.h"
#include "decompress.h"

#if FNPC_ENABLE_NPC_FOLLOWERS && !IS_FRLG
#include "data/companion_packed_text.h"
static EWRAM_DATA u32 sTextCache[COMPANION_TEXT_BLOCK_SIZE / 4] = {0};
static EWRAM_DATA u32 sCachedBlockPlusOne = 0;
static EWRAM_DATA u32 sCachedLength = 0;

bool32 CompanionPackedText_Copy(u32 reference, u8 *destination, u32 capacity)
{
    const u8 *source;
    u32 block = reference >> 12, offset = reference & 4095;
    u32 i, header;
    if (capacity == 0 || destination == NULL) return FALSE;
    destination[0] = EOS;
    if (reference == COMPANION_TEXT_NONE || block >= ARRAY_COUNT(gCompanionPackedTextOffsets)) return FALSE;
    if (sCachedBlockPlusOne != block + 1)
    {
        source = (const u8 *)gCompanionPackedText + gCompanionPackedTextOffsets[block];
        header = *(const u32 *)source;
        if ((header & 255) != 0x10 || (header >> 8) > COMPANION_TEXT_BLOCK_SIZE || (header >> 8) == 0) return FALSE;
        DecompressDataWithHeaderWram((const u32 *)source, sTextCache);
        sCachedLength = header >> 8;
        sCachedBlockPlusOne = block + 1;
    }
    source = (const u8 *)sTextCache;
    for (i = 0; i < capacity && offset + i < sCachedLength; i++)
    {
        destination[i] = source[offset + i];
        if (destination[i] == EOS) return TRUE;
    }
    destination[0] = EOS;
    return FALSE;
}
#else
bool32 CompanionPackedText_Copy(u32 reference, u8 *destination, u32 capacity)
{
    if (capacity && destination) destination[0] = EOS;
    return FALSE;
}
#endif
