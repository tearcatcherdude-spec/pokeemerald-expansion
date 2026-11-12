#ifndef GUARD_PARALLEL_WATCH_H
#define GUARD_PARALLEL_WATCH_H
struct ScriptContext;
bool32 ParallelWatch_IsKanto(u32 group, u32 num);
bool32 ParallelWatch_IsOutdoor(u32 group, u32 num);
bool32 ParallelWatch_IsSafeAnchor(const struct ParallelWatchAnchor *anchor, u32 world);
void Script_ParallelWatchCheck(struct ScriptContext *ctx);
void Script_ParallelWatchSwitch(struct ScriptContext *ctx);
void Script_VoidWatchIsHere(struct ScriptContext *ctx);
void Script_VoidWatchEnter(struct ScriptContext *ctx);
void Script_VoidWatchReturn(struct ScriptContext *ctx);
#endif
