#ifndef GUARD_KANTO_PROGRESS_H
#define GUARD_KANTO_PROGRESS_H
#include "constants/kanto_progress.h"
bool32 KantoProgress_EnsureInitialized(void);
u8 *KantoProgress_GetFlagPointer(u16 id);
u16 *KantoProgress_GetVarPointer(u16 id);
u16 KantoProgress_RegionalFlagId(u16 id);
#endif
