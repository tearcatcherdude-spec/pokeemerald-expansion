#ifndef GUARD_BONDS_H
#define GUARD_BONDS_H

#define BOND_COUNT 10
#define BOND_LEVEL_CAP 20
#define BOND_EXP_CAP 3040
#define BOND_SAVE_MAGIC 0x444E4F42
#define BOND_SAVE_VERSION 1
#define BOND_NO_COMPANION 0xFF
enum { BOND_UNDECIDED, BOND_FRIENDSHIP, BOND_INTERESTED, BOND_COMMITTED };

// Append-only save extension. Existing PC, fusion and SaveBlock3 bytes stay fixed.
struct BondPerson
{
    u16 exp, outingSteps;
    u8 walkingExp, giftUsed, giftExp[5], hearts, interest, flags;
    u8 landmarks[8], objectives[16];
};
struct BondProgress
{
    u32 magic;
    u16 version;
    u8 committed, trackedEvent; // 0 means none; otherwise character/event index + 1.
    u8 visited[8];
    struct BondPerson people[BOND_COUNT];
};

void Bonds_Reset(void);
void Bonds_EnsureInitialized(void);
u32 Bonds_TotalForLevel(u32 level);
u32 Bonds_Level(u32 who);
u32 Bonds_AddExp(u32 who, u32 amount);
void Bonds_OnStep(void);
void Bonds_RenewOuting(void);
bool32 Bonds_Rest(u32 who, bool32 atCenter);
bool32 Bonds_Objective(u32 who, u32 objective);
bool32 Bonds_Landmark(u32 who, u32 landmark);
u32 Bonds_GiftPreview(u32 who, u32 value);
bool32 Bonds_RecordGift(u32 who, u32 value);
bool32 Bonds_CompleteEvent(u32 who, u32 stage);
bool32 Bonds_SetInterest(u32 who, u32 interest);
void Bonds_QueueObservation(u32 who, bool32 lore);
void Bonds_MessageFinished(void);
void Bonds_CancelMessage(void);
struct BondProgress *Bonds_GetProgress(void);
#endif
