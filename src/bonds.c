#include "global.h"
#include "bonds.h"
#include "cast.h"
#include "pip.h"
#include "pokemon_storage_system.h"
#include "field_player_avatar.h"

static EWRAM_DATA u8 sObservationWho = 0;
static EWRAM_DATA u8 sObservationExp = 0;

struct BondProgress *Bonds_GetProgress(void)
{
    if (gPokemonStoragePtr == NULL)
        return NULL;
    return &gPokemonStoragePtr->bonds;
}

void Bonds_Reset(void)
{
    struct BondProgress *p = Bonds_GetProgress();
    if (p == NULL)
        return;
    memset(p, 0, sizeof(*p));
    p->magic = BOND_SAVE_MAGIC;
    p->version = BOND_SAVE_VERSION;
    Bonds_CancelMessage();
}

void Bonds_EnsureInitialized(void)
{
    struct BondProgress *p = Bonds_GetProgress();
    // Released saves wrote zero to the unused PC sector tail. Only this new
    // suffix is initialized; old reaction/lore history earns no duplicate EXP.
    if (p != NULL && (p->magic != BOND_SAVE_MAGIC || p->version == 0))
        Bonds_Reset();
}

u32 Bonds_TotalForLevel(u32 level)
{
    level = max(1, min(level, BOND_LEVEL_CAP));
    return 5 * (level - 1) * (level + 12);
}

u32 Bonds_Level(u32 who)
{
    u32 level = 1;
    Bonds_EnsureInitialized();
    if (who >= BOND_COUNT || Bonds_GetProgress() == NULL)
        return level;
    while (level < BOND_LEVEL_CAP && Bonds_GetProgress()->people[who].exp >= Bonds_TotalForLevel(level + 1))
        level++;
    return level;
}

u32 Bonds_AddExp(u32 who, u32 amount)
{
    struct BondPerson *p;
    u32 awarded;
    Bonds_EnsureInitialized();
    if (who >= BOND_COUNT || Bonds_GetProgress() == NULL)
        return 0;
    p = &Bonds_GetProgress()->people[who];
    if (p->exp >= BOND_EXP_CAP)
        return 0;
    awarded = min(amount, BOND_EXP_CAP - p->exp);
    p->exp += awarded;
    return awarded;
}

void Bonds_OnStep(void)
{
    u32 active;
    struct BondPerson *p;
    if (!Cast_IsFollowing() || Pip_IsSceneSuspended()
     || !TestPlayerAvatarFlags(PLAYER_AVATAR_FLAG_ON_FOOT))
        return;
    active = Cast_Active();
    if (active == 0 || active > BOND_COUNT)
        return;
    Bonds_EnsureInitialized();
    p = &Bonds_GetProgress()->people[active - 1];
    if (p->outingSteps < 2048)
    {
        p->outingSteps++;
        if (p->outingSteps % 256 == 0 && p->walkingExp < 40)
        {
            p->walkingExp += Bonds_AddExp(active - 1, min(5,40-p->walkingExp));
        }
    }
}

static void Renew(u32 who)
{
    struct BondPerson *p = &Bonds_GetProgress()->people[who];
    p->outingSteps = 0;
    p->walkingExp = 0;
    p->giftUsed = FALSE;
}

void Bonds_RenewOuting(void)
{
    u32 active;
    if (!Cast_IsFollowing() || Pip_IsSceneSuspended())
        return;
    active = Cast_Active();
    Bonds_EnsureInitialized();
    if (active && active <= BOND_COUNT)
        Renew(active - 1);
}

bool32 Bonds_Rest(u32 who, bool32 atCenter)
{
    Bonds_EnsureInitialized();
    if (who >= BOND_COUNT || Bonds_GetProgress() == NULL || !atCenter
     || !Cast_IsFollowing() || Cast_Active() != who + 1
     || Bonds_GetProgress()->people[who].outingSteps < 2048)
        return FALSE;
    Renew(who);
    return TRUE;
}

static bool32 Mark(u8 *bits, u32 id, u32 count)
{
    if (id >= count || (bits[id / 8] & (1 << (id % 8))))
        return FALSE;
    bits[id / 8] |= 1 << (id % 8);
    return TRUE;
}

bool32 Bonds_Objective(u32 who, u32 objective)
{
    Bonds_EnsureInitialized();
    if (who >= BOND_COUNT || Bonds_GetProgress() == NULL
     || !Mark(Bonds_GetProgress()->people[who].objectives, objective, 128))
        return FALSE;
    Bonds_AddExp(who, 40);
    Renew(who);
    return TRUE;
}

void Bonds_OnObjectiveFlag(u16 id)
{
#if !IS_FRLG
    u32 objective,active;
    if(id>=FLAG_WORLD_SCENE_0 && id<=FLAG_WORLD_SCENE_20)
        objective=id-FLAG_WORLD_SCENE_0;
    else if(id==FLAG_COZY_BERRY_TRADE)
        objective=21;
    else if(id>=0xA8E0 && id<0xA8EC)
        objective=32+id-0xA8E0;
    else return;
    if(!Cast_IsFollowing() || !(active=Cast_Active())) return;
    Bonds_Objective(active-1,objective);
#endif
}

bool32 Bonds_Landmark(u32 who, u32 landmark)
{
    Bonds_EnsureInitialized();
    if (who >= BOND_COUNT || Bonds_GetProgress() == NULL
     || !Mark(Bonds_GetProgress()->people[who].landmarks, landmark, 64))
        return FALSE;
    Bonds_AddExp(who, 30);
    Renew(who);
    return TRUE;
}

u32 Bonds_GiftPreview(u32 who, u32 value)
{
    struct BondPerson *p;
    Bonds_EnsureInitialized();
    if (who >= BOND_COUNT || Bonds_GetProgress() == NULL || (value != 5 && value != 15 && value != 30))
        return 0;
    p = &Bonds_GetProgress()->people[who];
    if (p->giftUsed || p->hearts >= 5 || p->giftExp[p->hearts] >= 150 || p->exp >= BOND_EXP_CAP)
        return 0;
    return min(value, min(150 - p->giftExp[p->hearts], BOND_EXP_CAP - p->exp));
}

bool32 Bonds_RecordGift(u32 who, u32 value)
{
    u32 amount = Bonds_GiftPreview(who, value);
    struct BondPerson *p;
    if (!amount)
        return FALSE;
    p = &Bonds_GetProgress()->people[who];
    p->giftExp[p->hearts] += amount;
    p->giftUsed = TRUE;
    Bonds_AddExp(who, amount);
    return TRUE;
}

bool32 Bonds_CompleteEvent(u32 who, u32 stage)
{
    static const u8 levels[] = {4, 8, 12, 16, 20};
    struct BondPerson *p;
    Bonds_EnsureInitialized();
    if (who >= BOND_COUNT || stage >= 5 || Bonds_GetProgress() == NULL)
        return FALSE;
    p = &Bonds_GetProgress()->people[who];
    if (p->hearts != stage || Bonds_Level(who) < levels[stage])
        return FALSE;
    p->hearts++;
    Bonds_AddExp(who, stage == 3 ? 100 : stage == 4 ? 0 : 60);
    Renew(who);
    return TRUE;
}

bool32 Bonds_SetInterest(u32 who, u32 interest)
{
    struct BondProgress *p;
    Bonds_EnsureInitialized();
    p = Bonds_GetProgress();
    if (who >= BOND_COUNT || p == NULL || interest > BOND_COMMITTED || p->people[who].hearts < 2)
        return FALSE;
    if (interest == BOND_COMMITTED)
    {
        if (p->people[who].hearts < 4 || (p->committed && p->committed != who + 1))
            return FALSE;
        p->committed = who + 1;
    }
    else if (p->committed == who + 1)
        p->committed = 0;
    p->people[who].interest = interest;
    return TRUE;
}

void Bonds_QueueObservation(u32 who, bool32 lore)
{
    sObservationWho = who < BOND_COUNT ? who + 1 : 0;
    sObservationExp = lore ? 25 : 10;
}

void Bonds_MessageFinished(void)
{
    if (sObservationWho)
        Bonds_AddExp(sObservationWho - 1, sObservationExp);
    Bonds_CancelMessage();
}

void Bonds_CancelMessage(void)
{
    sObservationWho = 0;
    sObservationExp = 0;
}
