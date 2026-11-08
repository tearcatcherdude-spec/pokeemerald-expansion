#ifndef GUARD_PIP_H
#define GUARD_PIP_H

struct ScriptContext;

bool32 Pip_IsFollowing(void);
bool32 Pip_HasHeard(const u8 *text);
bool32 Pip_TrySay(const u8 *text);
bool32 Pip_IsSceneSuspended(void);
void Pip_RefreshIdentity(void);
void Pip_BeforeScriptedMovement(u8 localId);
void Pip_TryRegroupAfterScene(void);
void Pip_ResetSceneState(void);
const u8 *Pip_GetLocationDialogue(u16 mapSection, u32 variant);
const u8 *Pip_GetProgressDialogue(u32 badges, bool32 champion);
void Script_PipCheckFollowing(struct ScriptContext *ctx);
void Script_PipChooseDialogue(struct ScriptContext *ctx);
void Script_PipBeginNPCReaction(struct ScriptContext *ctx);
void Script_PipChooseNPCDialogue(struct ScriptContext *ctx);
void Script_PipBeginObjectReaction(struct ScriptContext *ctx);
void Script_PipChooseObjectDialogue(struct ScriptContext *ctx);
void Script_PipEndNPCReaction(struct ScriptContext *ctx);

void Pip_BeginKantoNPCInteraction(void);
void Script_PipBeginKantoNPCReaction(struct ScriptContext *ctx);
#endif
