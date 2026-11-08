#include "global.h"
#include "kanto_progress.h"
#include "constants/kanto_symbols.h"

#if FNPC_ENABLE_NPC_FOLLOWERS
static const u16 sInitialFlags[] = {
#include "data/kanto_initial_flags.h"
};
#endif

bool32 KantoProgress_EnsureInitialized(void)
{
#if FNPC_ENABLE_NPC_FOLLOWERS
    if (gSaveBlock3Ptr == NULL)
        return FALSE;
    if (gSaveBlock3Ptr->kanto.version != KANTO_PROGRESS_VERSION)
    {
        memset(&gSaveBlock3Ptr->kanto, 0, sizeof(gSaveBlock3Ptr->kanto));
        gSaveBlock3Ptr->kanto.version = KANTO_PROGRESS_VERSION;
        for (u32 i = 0; i < ARRAY_COUNT(sInitialFlags); i++)
        {
            u32 id = sInitialFlags[i] - KANTO_FLAG_BASE;
            gSaveBlock3Ptr->kanto.flags[id / 8] |= 1 << (id % 8);
        }
        // The visitor already has an Emerald starter. Skip the forced Oak
        // rescue and starter battle, retaining the parcel and local quest chain.
        gSaveBlock3Ptr->kanto.vars[KANTO_VAR_MAP_SCENE_PALLET_TOWN_OAK - KANTO_VAR_BASE] = 1;
        gSaveBlock3Ptr->kanto.vars[KANTO_VAR_MAP_SCENE_PALLET_TOWN_PROFESSOR_OAKS_LAB - KANTO_VAR_BASE] = 4;
        gSaveBlock3Ptr->kanto.vars[KANTO_VAR_MASSAGE_COOLDOWN_STEP_COUNTER - KANTO_VAR_BASE] = 500;
    }
    return TRUE;
#else
    return FALSE;
#endif
}

u8 *KantoProgress_GetFlagPointer(u16 id)
{
#if FNPC_ENABLE_NPC_FOLLOWERS
    // Native flag zero means no flag; preserve that convention in this bank.
    if (id <= KANTO_FLAG_BASE || id >= KANTO_FLAG_LIMIT || !KantoProgress_EnsureInitialized())
        return NULL;
    return &gSaveBlock3Ptr->kanto.flags[(id - KANTO_FLAG_BASE) / 8];
#else
    return NULL;
#endif
}

u16 *KantoProgress_GetVarPointer(u16 id)
{
#if FNPC_ENABLE_NPC_FOLLOWERS
    if (id < KANTO_VAR_BASE || id >= KANTO_VAR_LIMIT || !KantoProgress_EnsureInitialized())
        return NULL;
    return &gSaveBlock3Ptr->kanto.vars[id - KANTO_VAR_BASE];
#else
    return NULL;
#endif
}
