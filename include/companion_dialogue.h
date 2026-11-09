#ifndef GUARD_COMPANION_DIALOGUE_H
#define GUARD_COMPANION_DIALOGUE_H

struct ScriptContext;
enum { COMPANION_DIALOGUE_NORMAL, COMPANION_DIALOGUE_ASK, COMPANION_DIALOGUE_SILENT };
#define COMPANION_CONTEXT_CAPACITY 736
#define COMPANION_VOICE_COUNT 11

// Appended after Bond v1. Never resize/reorder the released PC or bond prefix.
struct CompanionDialogueProgress
{
    u32 magic;
    u8 version;
    u8 mode;
    u8 reserved[2];
    u8 spent[COMPANION_VOICE_COUNT][COMPANION_CONTEXT_CAPACITY / 8];
};

void CompanionDialogue_Reset(void);
u32 CompanionDialogue_GetMode(void);
bool32 CompanionDialogue_SetMode(u32 mode);
void CompanionDialogue_BeginInteraction(const u8 *script);
void CompanionDialogue_RecordMessage(struct ScriptContext *ctx, const u8 *message);
bool32 CompanionDialogue_FinishInteraction(struct ScriptContext *ctx);
bool32 CompanionDialogue_IsInteractionActive(void);
void CompanionDialogue_ResetSession(void);
// 0 = no recent interaction, 1 = spoke, 2 = deliberately quiet.
u32 CompanionDialogue_TryManualTalk(void);
void Script_CompanionDialogueChoose(struct ScriptContext *ctx);
void Script_CompanionDialogueRestore(struct ScriptContext *ctx);
void Script_CompanionDialogueSetMode(struct ScriptContext *ctx);
void Script_CompanionDialogueBufferMode(struct ScriptContext *ctx);
u32 CompanionDialogue_ContextForMessage(const u8 *message);
bool32 CompanionDialogue_HasSpent(u32 voice, u32 context);

#endif
