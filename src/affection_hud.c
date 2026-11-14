#include "global.h"
#include "affection_hud.h"
#include "bonds.h"
#include "sprite.h"
#include "palette.h"
#include "main.h"
#include "overworld.h"
#include "script.h"
#include "map_name_popup.h"
#include "constants/rgb.h"

#include "data/affection_hud_panel.h"

#define HUD_TAG 0x7E50
#define HUD_WIDTH 128
#define HUD_BAR_WIDTH 112
#define HUD_HOLD_FRAMES 100
struct HudPending { u16 before, after; u32 order; };
static EWRAM_DATA struct HudPending sPending[BOND_COUNT] = {0};
static EWRAM_DATA u32 sOrder = 0;
static EWRAM_DATA struct AffectionHudState sHud = {0};
static EWRAM_DATA bool8 sCreated = FALSE;
static EWRAM_DATA u8 sIds[2] = {0};
static EWRAM_DATA u16 sTileStart = 0;
static EWRAM_DATA u8 ALIGNED(4) sPixels[2048] = {0};
static EWRAM_DATA struct AffectionHudState sLastDraw = {0};
static EWRAM_DATA bool8 sDrawValid = FALSE;

static const u16 sPalette[16] = {
    RGB(0,0,0), RGB(5,8,9), RGB(29,30,25), RGB(20,24,22),
    RGB(6,20,25), RGB(17,29,30), RGB(29,9,16), RGB(31,25,11),
    RGB(12,16,18), RGB(31,31,31), RGB(31,17,22), RGB(0,0,0),
    RGB(0,0,0), RGB(0,0,0), RGB(0,0,0), RGB(0,0,0)
};
static const char *const sNames[BOND_COUNT] = {"SILAS","KADE","ASHE","NICO","RIVEN","EMI","VERA","LUME","MOCHI","ZURI"};
// Tiny native tile glyphs; no BG window or text-printer/input state is allocated.
static const u8 sGlyphs[][5] = {
    {0x3E,0x51,0x49,0x45,0x3E},{0,0x42,0x7F,0x40,0},{0x42,0x61,0x51,0x49,0x46},
    {0x21,0x41,0x45,0x4B,0x31},{0x18,0x14,0x12,0x7F,0x10},{0x27,0x45,0x45,0x45,0x39},
    {0x3C,0x4A,0x49,0x49,0x30},{1,0x71,9,5,3},{0x36,0x49,0x49,0x49,0x36},{6,0x49,0x49,0x29,0x1E},
    {0x7E,0x11,0x11,0x11,0x7E},{0x7F,0x49,0x49,0x49,0x36},{0x3E,0x41,0x41,0x41,0x22},
    {0x7F,0x41,0x41,0x22,0x1C},{0x7F,0x49,0x49,0x49,0x41},{0x7F,9,9,9,1},
    {0x3E,0x41,0x49,0x49,0x7A},{0x7F,8,8,8,0x7F},{0,0x41,0x7F,0x41,0},{0x20,0x40,0x41,0x3F,1},
    {0x7F,8,0x14,0x22,0x41},{0x7F,0x40,0x40,0x40,0x40},{0x7F,2,0xC,2,0x7F},
    {0x7F,4,8,0x10,0x7F},{0x3E,0x41,0x41,0x41,0x3E},{0x7F,9,9,9,6},
    {0x3E,0x41,0x51,0x21,0x5E},{0x7F,9,0x19,0x29,0x46},{0x46,0x49,0x49,0x49,0x31},
    {1,1,0x7F,1,1},{0x3F,0x40,0x40,0x40,0x3F},{0x1F,0x20,0x40,0x20,0x1F},
    {0x3F,0x40,0x38,0x40,0x3F},{0x63,0x14,8,0x14,0x63},{7,8,0x70,8,7},{0x61,0x51,0x49,0x45,0x43},
    {8,8,0x3E,8,8},{0x20,0x10,8,4,2},{0,0x60,0x60,0,0},{0,0,0x5F,0,0}
};
static void HudSpriteCB(struct Sprite *sprite) {}
static const struct OamData sOam = {.shape=SPRITE_SHAPE(64x32),.size=SPRITE_SIZE(64x32),.priority=0};
static const struct SpriteTemplate sTemplate = {.tileTag=HUD_TAG,.paletteTag=HUD_TAG,.oam=&sOam,.anims=gDummySpriteAnimTable,.images=NULL,.affineAnims=gDummySpriteAffineAnimTable,.callback=HudSpriteCB};

u32 AffectionHud_LevelForExp(u32 exp)
{
    u32 level = 1;
    while (level < BOND_LEVEL_CAP && exp >= Bonds_TotalForLevel(level + 1)) level++;
    return level;
}
void AffectionHud_Progress(u32 exp, u32 *current, u32 *needed)
{
    u32 level = AffectionHud_LevelForExp(exp);
    if (level == BOND_LEVEL_CAP) { *current = BOND_EXP_CAP; *needed = BOND_EXP_CAP; }
    else { *current = exp - Bonds_TotalForLevel(level); *needed = Bonds_TotalForLevel(level + 1) - Bonds_TotalForLevel(level); }
}
const struct AffectionHudState *AffectionHud_GetState(void) { return &sHud; }
u32 AffectionHud_PendingCount(void)
{
    u32 i, count = sHud.phase != AFFECTION_HUD_IDLE;
    for (i=0; i<BOND_COUNT; i++) if (sPending[i].order) count++;
    return count;
}
u32 AffectionHud_PendingExp(u32 who)
{
    if (who >= BOND_COUNT) return 0;
    if (sHud.phase != AFFECTION_HUD_IDLE && sHud.who == who) return sHud.awarded;
    return sPending[who].order ? sPending[who].after-sPending[who].before : 0;
}
void AffectionHud_Notify(u32 who, u32 before, u32 after)
{
    if (who >= BOND_COUNT || after <= before || before >= BOND_EXP_CAP) return;
    after = min(after, BOND_EXP_CAP);
    if (sHud.phase != AFFECTION_HUD_IDLE && sHud.who == who)
    {
        sHud.awarded += after-before;
        sHud.targetExp = max(sHud.targetExp, after);
        if (sHud.phase == AFFECTION_HUD_HOLD || sHud.phase == AFFECTION_HUD_EXIT) { sHud.phase=AFFECTION_HUD_FILL; sHud.timer=0; }
        return;
    }
    if (!sPending[who].order)
    {
        if (++sOrder == 0) sOrder=1;
        sPending[who]=(struct HudPending){before,after,sOrder};
    }
    else sPending[who].after=max(sPending[who].after,after);
}
static void ReleaseSprites(void)
{
    u32 i;
    if (!sCreated) return;
    for (i=0; i<2; i++)
        if (sIds[i]<MAX_SPRITES && gSprites[sIds[i]].inUse && gSprites[sIds[i]].callback==HudSpriteCB) DestroySprite(&gSprites[sIds[i]]);
    FreeSpriteTilesByTag(HUD_TAG);
    FreeSpritePaletteByTag(HUD_TAG);
    sIds[0]=sIds[1]=MAX_SPRITES; sTileStart=TAG_NONE; sCreated=FALSE; sHud.visible=FALSE; sDrawValid=FALSE;
}
void AffectionHud_OnSpriteReset(void) { ReleaseSprites(); }
void AffectionHud_Clear(void)
{
    ReleaseSprites(); memset(sPending,0,sizeof(sPending)); memset(&sHud,0,sizeof(sHud)); sHud.who=BOND_NO_COMPANION; sOrder=0;
}
static bool32 UNUSED CreateHud(void)
{
    struct SpriteSheet sheet={sPixels,sizeof(sPixels),HUD_TAG};
    struct SpritePalette pal={sPalette,HUD_TAG};
    u32 i;
    if (sCreated) return TRUE;
    sTileStart=LoadSpriteSheet(&sheet);
    if (sTileStart==TAG_NONE) return FALSE;
    if (LoadSpritePalette(&pal)==0xFF) { FreeSpriteTilesByTag(HUD_TAG); return FALSE; }
    sCreated=TRUE;
    sIds[0]=sIds[1]=MAX_SPRITES;
    for (i=0; i<2; i++)
    {
        sIds[i]=CreateSprite(&sTemplate,88+i*64,22,0);
        if (sIds[i]==MAX_SPRITES) { ReleaseSprites(); return FALSE; }
        gSprites[sIds[i]].oam.tileNum=sTileStart+i*32;
        gSprites[sIds[i]].invisible=TRUE;
    }
    return TRUE;
}
static void Pixel(u32 x,u32 y,u32 color)
{
    u32 tile,at,shift;
    if (x>=128 || y>=32) return;
    tile=(x/64)*32+(y/8)*8+(x%64)/8;
    at=tile*32+(y%8)*4+(x%8)/2;shift=(x&1)*4;
    sPixels[at]=(sPixels[at]&~(15<<shift))|(color<<shift);
}
// Write contiguous packed nibbles within each tile row, instead of calling
// Pixel for every background/bar pixel on every frame.
static void Rect(u32 x,u32 y,u32 w,u32 h,u32 color)
{
    u32 yy,xx,end=min(x+w,128),chunk,count,tile;
    for (yy=y;yy<min(y+h,32);yy++)
    {
        xx=x;
        while (xx<end)
        {
            if (xx&1) { Pixel(xx++,yy,color);continue; }
            chunk=min(8-(xx&7),end-xx);count=chunk/2;
            tile=(xx/64)*32+(yy/8)*8+(xx%64)/8;
            if (count) memset(sPixels+tile*32+(yy%8)*4+(xx%8)/2,color*17,count);
            xx+=count*2;
            if (chunk&1) Pixel(xx++,yy,color);
        }
    }
}
static u32 Text(u32 x,u32 y,const char *text,u32 color)
{
    u32 c,i,j,index;
    while ((c=*text++))
    {
        if (c>='a' && c<='z') c-=32;
        if (c>='0' && c<='9') index=c-'0';
        else if (c>='A' && c<='Z') index=10+c-'A';
        else if (c=='+') index=36; else if (c=='/') index=37; else if (c=='.') index=38; else if (c=='!') index=39;
        else { x+=4; continue; }
        for (i=0;i<5;i++) for (j=0;j<7;j++) if (sGlyphs[index][i]&(1<<j)) Pixel(x+i,y+j,color);
        x+=6;
    }
    return x;
}
static u32 Number(u32 x,u32 y,u32 n,u32 color)
{
    char buffer[6];u32 count=0,i;
    do { buffer[count++]='0'+n%10;n/=10; } while (n && count<5);
    for (i=0;i<count/2;i++) { char c=buffer[i];buffer[i]=buffer[count-1-i];buffer[count-1-i]=c; }
    buffer[count]=0;return Text(x,y,buffer,color);
}
static void UNUSED Draw(void)
{
    static const u8 heart[]={0x66,0xFF,0xFF,0xFF,0x7E,0x3C,0x18,0};
    u32 x,y,current,needed,fill,px,scale=sHud.phase==AFFECTION_HUD_LEVEL_UP && sHud.timer%12<6 ? 10:8;
    if (sDrawValid && sHud.shownExp==sLastDraw.shownExp && sHud.awarded==sLastDraw.awarded
     && sHud.level==sLastDraw.level && sHud.who==sLastDraw.who && sHud.phase==sLastDraw.phase
     && sHud.phase!=AFFECTION_HUD_LEVEL_UP && sHud.phase!=AFFECTION_HUD_EXIT)
        return;
    // Fixed artwork is already tiled. Holding/sliding the HUD needs no redraw.
    memcpy(sPixels,sPanelTiles,sizeof(sPixels));
    if (sHud.phase==AFFECTION_HUD_LEVEL_UP)
    {
        Rect(4,1,120,1,7);Rect(4,3,10,10,2);
        for (y=0;y<scale;y++) for (x=0;x<scale;x++) if (heart[y*8/scale]&(1<<(7-x*8/scale))) Pixel(4+x,3+y,7);
    }
    Text(17,4,sNames[sHud.who],1);px=Text(62,4,"Lv.",1);Number(px,4,sHud.level,1);
    if (sHud.phase==AFFECTION_HUD_LEVEL_UP) Text(101,4,"UP!",6);
    else { px=Text(94,4,"+",1);Number(px,4,sHud.awarded,1); }
    if (sHud.level==BOND_LEVEL_CAP) { current=needed=BOND_EXP_CAP; Text(7,14,"MAX",1);Number(31,14,BOND_EXP_CAP,1);Text(57,14,"EXP",1); }
    else
    {
        current=sHud.shownExp-Bonds_TotalForLevel(sHud.level);needed=Bonds_TotalForLevel(sHud.level+1)-Bonds_TotalForLevel(sHud.level);
        px=Number(7,14,current,1);px=Text(px,14,"/",1);px=Number(px,14,needed,1);Text(px+4,14,"EXP",1);
    }
    fill=min(HUD_BAR_WIDTH,current*HUD_BAR_WIDTH/max(needed,1));sHud.fillPixels=fill;
    Rect(8,24,fill,4,4);Rect(8,24,fill,1,5);
    if (sHud.phase==AFFECTION_HUD_LEVEL_UP)
    {
        x=23+(sHud.timer*5)%95;Pixel(x,21,7);Pixel(x-1,20,7);Pixel(x+1,20,7);Pixel(x,19,7);
    }
    if (sHud.phase==AFFECTION_HUD_EXIT)
    {
        u32 tile,offset,mask0,mask1;
        for (y=0;y<8;y++)
        {
            mask0=mask1=255;
            if ((y&3)*4<sHud.timer) mask0&=0xF0;
            if ((y&3)*4+1<sHud.timer) mask0&=0x0F;
            if ((y&3)*4+2<sHud.timer) mask1&=0xF0;
            if ((y&3)*4+3<sHud.timer) mask1&=0x0F;
            for (tile=0;tile<64;tile++)
            {
                offset=tile*32+y*4;
                sPixels[offset]&=mask0;sPixels[offset+1]&=mask1;
                sPixels[offset+2]&=mask0;sPixels[offset+3]&=mask1;
            }
        }
    }
    sLastDraw=sHud;sDrawValid=TRUE;
    RequestSpriteCopy(sPixels,(u8 *)OBJ_VRAM0+sTileStart*32,sizeof(sPixels));
}
static bool32 UNUSED BeginNext(void)
{
    u32 i,best=BOND_COUNT,order=0xFFFFFFFF;
    for (i=0;i<BOND_COUNT;i++) if (sPending[i].order && sPending[i].order<order) { order=sPending[i].order;best=i; }
    if (best==BOND_COUNT) return FALSE;
    sHud=(struct AffectionHudState){.shownExp=sPending[best].before,.targetExp=sPending[best].after,.awarded=sPending[best].after-sPending[best].before,.level=AffectionHud_LevelForExp(sPending[best].before),.who=best,.phase=AFFECTION_HUD_ENTER};
    memset(&sPending[best],0,sizeof(sPending[best]));return TRUE;
}
void AffectionHud_Update(void)
{
#if FNPC_ENABLE_NPC_FOLLOWERS && !IS_FRLG
    u32 i,next,step;
    bool32 safe=gMain.callback2==CB2_Overworld && !gPaletteFade.active && !ScriptContext_IsEnabled() && !ArePlayerFieldControlsLocked() && !IsMapNamePopupActive();
    if (!safe)
    {
        for (i=0;i<2;i++) if (sCreated && sIds[i]<MAX_SPRITES) gSprites[sIds[i]].invisible=TRUE;
        sHud.visible=FALSE;return;
    }
    if (sHud.phase==AFFECTION_HUD_IDLE && !BeginNext()) return;
    if (!CreateHud()) return; // Retry later without spending input or losing EXP.
    sHud.visible=TRUE;
    switch (sHud.phase)
    {
    case AFFECTION_HUD_ENTER:
        if (++sHud.timer>=10) { sHud.timer=0;sHud.phase=AFFECTION_HUD_FILL; }
        break;
    case AFFECTION_HUD_FILL:
        if (sHud.level==BOND_LEVEL_CAP || sHud.shownExp>=sHud.targetExp) { sHud.phase=AFFECTION_HUD_HOLD;sHud.timer=0;break; }
        next=Bonds_TotalForLevel(sHud.level+1);step=max(1,(next-Bonds_TotalForLevel(sHud.level)+47)/48);
        sHud.shownExp=min(sHud.targetExp,min(next,sHud.shownExp+step));
        if (sHud.shownExp==next) { sHud.phase=AFFECTION_HUD_LEVEL_UP;sHud.timer=0; }
        break;
    case AFFECTION_HUD_LEVEL_UP:
        if (++sHud.timer>=24) { sHud.level++;sHud.phase=AFFECTION_HUD_FILL;sHud.timer=0; }
        break;
    case AFFECTION_HUD_HOLD:
        if (++sHud.timer>=HUD_HOLD_FRAMES) { sHud.phase=AFFECTION_HUD_EXIT;sHud.timer=0; }
        break;
    case AFFECTION_HUD_EXIT:
        if (++sHud.timer>=16) { ReleaseSprites();sHud.phase=AFFECTION_HUD_IDLE;sHud.who=BOND_NO_COMPANION;return; }
        break;
    }
    for (i=0;i<2;i++) { gSprites[sIds[i]].invisible=FALSE;gSprites[sIds[i]].y=sHud.phase==AFFECTION_HUD_ENTER ? -10+sHud.timer*32/10 : sHud.phase==AFFECTION_HUD_EXIT ? 22-sHud.timer*2 : 22; }
    Draw();
#endif
}
