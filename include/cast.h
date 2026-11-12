#ifndef GUARD_CAST_H
#define GUARD_CAST_H
#define CAST_COUNT 10
#define CAST_CONTEXT_CAPACITY 448
#define CAST_MEMORY_BYTES (CAST_CONTEXT_CAPACITY / 8)
#define CAST_FLAG_BASE 0xB000
struct ScriptContext;
void Cast_EnsureInitialized(void);
u8 *Cast_GetFlagPointer(u16 id);
bool32 Cast_IsFollowing(void);
u32 Cast_Active(void);
void Cast_RefreshIdentity(void);
void Cast_OnStep(void);
bool32 Cast_HasUsed(u32 id);
bool32 Cast_HasUsedBy(u32 who, u32 id);
bool32 Cast_Offer(u32 id);
bool32 Cast_TrySay(u32 id);
bool32 Cast_TryPersonalTalk(void);
bool32 Cast_TryBondStory(void);
void Cast_ClearPending(void);
void Cast_HidePortrait(void);
void Cast_ShowPortrait(u32 who, u32 expression);
void Script_CastRecruitStatus(struct ScriptContext *ctx);
void Script_CastCommitRequirement(struct ScriptContext *ctx);
void Script_CastAfterBattle(struct ScriptContext *ctx);
void Script_CastJoin(struct ScriptContext *ctx);
void Script_CastSwitchRoster(struct ScriptContext *ctx);
void Script_CastDismiss(struct ScriptContext *ctx);
void Script_CastFarewell(struct ScriptContext *ctx);
void Script_CastBufferSpeaker(struct ScriptContext *ctx);
void Script_CastHidePortrait(struct ScriptContext *ctx);
#endif
