#ifndef GUARD_ROAMING_TUTOR_H
#define GUARD_ROAMING_TUTOR_H
#include "pokemon.h"
u32 RoamingTutor_Offers(struct Pokemon *mon, u16 offers[4]);
bool32 RoamingTutor_CanTeach(struct Pokemon *mon);
bool32 RoamingTutor_Teach(struct Pokemon *mon, u16 move, u32 slot);
#endif
