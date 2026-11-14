#ifndef GUARD_AFFECTION_HUD_H
#define GUARD_AFFECTION_HUD_H

enum { AFFECTION_HUD_IDLE, AFFECTION_HUD_ENTER, AFFECTION_HUD_FILL, AFFECTION_HUD_LEVEL_UP, AFFECTION_HUD_HOLD, AFFECTION_HUD_EXIT };
struct AffectionHudState
{
    u16 shownExp, targetExp, awarded, level, timer;
    u8 who, phase, visible, fillPixels;
};
void AffectionHud_Clear(void);
void AffectionHud_Notify(u32 who, u32 before, u32 after);
void AffectionHud_Update(void);
void AffectionHud_OnSpriteReset(void);
u32 AffectionHud_LevelForExp(u32 exp);
void AffectionHud_Progress(u32 exp, u32 *current, u32 *needed);
u32 AffectionHud_PendingCount(void);
u32 AffectionHud_PendingExp(u32 who);
const struct AffectionHudState *AffectionHud_GetState(void);
#endif
