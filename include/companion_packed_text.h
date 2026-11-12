#ifndef GUARD_COMPANION_PACKED_TEXT_H
#define GUARD_COMPANION_PACKED_TEXT_H
#define COMPANION_TEXT_NONE 0xFFFFFFFFu
#define COMPANION_TEXT_BLOCK_SIZE 4096
bool32 CompanionPackedText_Copy(u32 reference, u8 *destination, u32 capacity);
#endif
