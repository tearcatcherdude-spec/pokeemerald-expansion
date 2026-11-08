#ifndef GUARD_COZY_WORLD_H
#define GUARD_COZY_WORLD_H
struct ScriptContext;
struct CozyRareDefinition { u16 species; u8 level; u8 evs[6]; };
u32 CozyWorld_RareCount(void);
const struct CozyRareDefinition *CozyWorld_GetRare(u32 index);
bool32 CozyWorld_CreateRare(u32 index);
void Script_CozyWorldTrainRare(struct ScriptContext *ctx);
void Script_CozyWorldPrepareRare(struct ScriptContext *ctx);
void Script_CozyWorldPipReaction(struct ScriptContext *ctx);
#endif
