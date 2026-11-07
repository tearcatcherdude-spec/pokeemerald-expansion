#include "global.h"
#include "bg.h"
#include "gpu_regs.h"
#include "event_data.h"
#include "main.h"
#include "menu.h"
#include "palette.h"
#include "pokemon.h"
#include "pokemon_icon.h"
#include "scanline_effect.h"
#include "sound.h"
#include "sprite.h"
#include "starter_choose.h"
#include "string_util.h"
#include "task.h"
#include "text.h"
#include "text_window.h"
#include "trainer_pokemon_sprites.h"
#include "window.h"
#include "constants/rgb.h"
#include "constants/songs.h"

#define GRID_COLUMNS 4
#define CHOICE_COUNT 14
#define PREVIEW_X 184
#define PREVIEW_Y 55

// Display generations in order, while preserving the original saved indices.
static const u8 sChoiceIds[CHOICE_COUNT] = {3, 4, 5, 6, 7, 8, 0, 1, 2, 9, 10, 11, 12, 13};
static const u8 sText_Help[] = _("A: Choose");
static const u8 sText_Confirm[] = _("Choose {STR_VAR_1}?");
static const u8 sText_Return[] = _("Choose a POKÃ©MON to help BIRCH!");
static const u8 sTextColors[] = {TEXT_COLOR_WHITE, TEXT_COLOR_DARK_GRAY, TEXT_COLOR_LIGHT_GRAY};

static const struct BgTemplate sBgs[] =
{
    {.bg = 0, .charBaseIndex = 0, .mapBaseIndex = 31, .priority = 0},
};

// 224 tiles for the grid, 44 for the name, 56 for the prompt, then yes/no.
static const struct WindowTemplate sWindows[] =
{
    {.bg = 0, .tilemapLeft = 1, .tilemapTop = 1, .width = 16, .height = 14, .paletteNum = 14, .baseBlock = 1},
    {.bg = 0, .tilemapLeft = 18, .tilemapTop = 10, .width = 11, .height = 4, .paletteNum = 14, .baseBlock = 225},
    {.bg = 0, .tilemapLeft = 1, .tilemapTop = 17, .width = 28, .height = 2, .paletteNum = 14, .baseBlock = 269},
    DUMMY_WIN_TEMPLATE,
};

static const struct WindowTemplate sConfirmWindow =
{
    .bg = 0, .tilemapLeft = 23, .tilemapTop = 10, .width = 6, .height = 4,
    .paletteNum = 14, .baseBlock = 325,
};

static EWRAM_DATA u8 sIconIds[CHOICE_COUNT] = {0};
static EWRAM_DATA u16 sPreviewId = 0xFFFF;

static void Task_ExpandedStarter(u8 taskId);

static void VBlank_ExpandedStarter(void)
{
    LoadOam();
    ProcessSpriteCopyRequests();
    TransferPlttBuffer();
}

static void Main_ExpandedStarter(void)
{
    RunTasks();
    AnimateSprites();
    BuildOamBuffer();
    DoScheduledBgTilemapCopiesToVram();
    UpdatePaletteFade();
}

static u16 SelectedSpecies(u8 selection)
{
    return GetStarterPokemon(sChoiceIds[selection]);
}

static void DrawPrompt(const u8 *text)
{
    FillWindowPixelBuffer(2, PIXEL_FILL(1));
    AddTextPrinterParameterized3(2, FONT_SMALL, 0, 0, sTextColors, TEXT_SKIP_DRAW, text);
    CopyWindowToVram(2, COPYWIN_FULL);
}

static void DrawSelection(u8 selection)
{
    u8 i;
    u16 species = SelectedSpecies(selection);
    const u8 *name = GetSpeciesName(species);

    FillWindowPixelBuffer(0, PIXEL_FILL(1));
    // Border surrounds the highlighted icon without obscuring its sprite.
    i = selection % GRID_COLUMNS;
    FillWindowPixelRect(0, PIXEL_FILL(3), i * 32, (selection / GRID_COLUMNS) * 28, 32, 28);
    FillWindowPixelRect(0, PIXEL_FILL(1), i * 32 + 2, (selection / GRID_COLUMNS) * 28 + 2, 28, 24);
    CopyWindowToVram(0, COPYWIN_FULL);

    for (i = 0; i < CHOICE_COUNT; i++)
        gSprites[sIconIds[i]].y2 = (i == selection) ? -2 : 0;

    if (sPreviewId != 0xFFFF)
        FreeAndDestroyMonPicSprite(sPreviewId);
    sPreviewId = CreateMonPicSprite(species, FALSE, 0, TRUE, PREVIEW_X, PREVIEW_Y, 14, TAG_NONE);
    if (sPreviewId != 0xFFFF)
        gSprites[sPreviewId].oam.priority = 0;

    FillWindowPixelBuffer(1, PIXEL_FILL(1));
    AddTextPrinterParameterized3(1, FONT_NORMAL, GetStringCenterAlignXOffset(FONT_NORMAL, name, 88), 0,
                                sTextColors, TEXT_SKIP_DRAW, name);
    AddTextPrinterParameterized3(1, FONT_SMALL, 0, 17, sTextColors, TEXT_SKIP_DRAW, sText_Help);
    CopyWindowToVram(1, COPYWIN_FULL);
}

static void CloseExpandedStarter(u8 taskId)
{
    u8 i;
    gSpecialVar_Result = sChoiceIds[gTasks[taskId].data[0]];
    for (i = 0; i < CHOICE_COUNT; i++)
        FreeAndDestroyMonIconSprite(&gSprites[sIconIds[i]]);
    FreeMonIconPalettes();
    if (sPreviewId != 0xFFFF)
        FreeAndDestroyMonPicSprite(sPreviewId);
    sPreviewId = 0xFFFF;
    FreeAllWindowBuffers();
    DestroyTask(taskId);
    SetVBlankCallback(NULL);
    SetMainCallback2(gMain.savedCallback);
}

static void Task_ExpandedStarter(u8 taskId)
{
    s16 *data = gTasks[taskId].data;
    u8 selection = data[0];
    s8 result;

    if (gPaletteFade.active)
        return;

    if (data[1] == 2)
    {
        CloseExpandedStarter(taskId);
        return;
    }
    if (data[1] == 1)
    {
        result = Menu_ProcessInputNoWrapClearOnChoose();
        if (result == 0)
        {
            BeginNormalPaletteFade(PALETTES_ALL, 0, 0, 16, RGB_BLACK);
            data[1] = 2;
        }
        else if (result == 1 || result == MENU_B_PRESSED)
        {
            PlaySE(SE_SELECT);
            PutWindowTilemap(1);
            DrawSelection(selection);
            DrawPrompt(sText_Return);
            data[1] = 0;
        }
        return;
    }

    if (JOY_NEW(A_BUTTON))
    {
        PlayCry_Normal(SelectedSpecies(selection), 0);
        StringCopy(gStringVar1, GetSpeciesName(SelectedSpecies(selection)));
        StringExpandPlaceholders(gStringVar4, sText_Confirm);
        DrawPrompt(gStringVar4);
        ClearWindowTilemap(1);
        CreateYesNoMenu(&sConfirmWindow, 400, 13, 0);
        data[1] = 1;
    }
    else
    {
        // Keep movement in the visible row/column, including the short last row.
        if (JOY_REPEAT(DPAD_LEFT) && selection % GRID_COLUMNS != 0)
            selection--;
        else if (JOY_REPEAT(DPAD_RIGHT) && selection % GRID_COLUMNS != GRID_COLUMNS - 1 && selection + 1 < CHOICE_COUNT)
            selection++;
        else if (JOY_REPEAT(DPAD_UP) && selection >= GRID_COLUMNS)
            selection -= GRID_COLUMNS;
        else if (JOY_REPEAT(DPAD_DOWN) && selection + GRID_COLUMNS < CHOICE_COUNT)
            selection += GRID_COLUMNS;
        if (selection != data[0])
        {
            PlaySE(SE_SELECT);
            data[0] = selection;
            DrawSelection(selection);
        }
    }
    ScheduleBgCopyTilemapToVram(0);
}

void CB2_ChooseExpandedStarter(void)
{
    u8 i;
    u8 taskId;
    u16 backdrop = RGB(20, 27, 18);

    SetVBlankCallback(NULL);
    SetGpuReg(REG_OFFSET_DISPCNT, 0);
    SetGpuReg(REG_OFFSET_BLDCNT, 0);
    DmaFill16(3, 0, VRAM, VRAM_SIZE);
    DmaFill32(3, 0, OAM, OAM_SIZE);
    DmaFill16(3, 0, PLTT, PLTT_SIZE);
    ResetBgsAndClearDma3BusyFlags(0);
    InitBgsFromTemplates(0, sBgs, ARRAY_COUNT(sBgs));
    ChangeBgX(0, 0, BG_COORD_SET);
    ChangeBgY(0, 0, BG_COORD_SET);
    InitWindows(sWindows);
    DeactivateAllTextPrinters();
    ClearScheduledBgCopiesToVram();
    ScanlineEffect_Stop();
    ResetTasks();
    ResetSpriteData();
    ResetPaletteFade();
    FreeAllSpritePalettes();
    ResetAllPicSprites();
    LoadPalette(&backdrop, 0, sizeof(backdrop));
    LoadPalette(GetOverworldTextboxPalettePtr(), BG_PLTT_ID(14), PLTT_SIZE_4BPP);
    LoadUserWindowBorderGfx(2, 400, BG_PLTT_ID(13));
    LoadMonIconPalettes();
    sPreviewId = 0xFFFF;

    for (i = 0; i < 3; i++)
    {
        FillWindowPixelBuffer(i, PIXEL_FILL(1));
        PutWindowTilemap(i);
    }
    for (i = 0; i < CHOICE_COUNT; i++)
    {
        sIconIds[i] = CreateMonIconNoPersonality(SelectedSpecies(i), SpriteCB_MonIcon,
                                               24 + (i % GRID_COLUMNS) * 32,
                                               22 + (i / GRID_COLUMNS) * 28, 0);
        gSprites[sIconIds[i]].oam.priority = 0;
    }
    taskId = CreateTask(Task_ExpandedStarter, 0);
    gTasks[taskId].data[0] = 0;
    DrawSelection(0);
    DrawPrompt(sText_Return);
    ScheduleBgCopyTilemapToVram(0);
    BeginNormalPaletteFade(PALETTES_ALL, 0, 16, 0, RGB_BLACK);
    SetGpuReg(REG_OFFSET_DISPCNT, DISPCNT_OBJ_ON | DISPCNT_OBJ_1D_MAP);
    ShowBg(0);
    SetVBlankCallback(VBlank_ExpandedStarter);
    SetMainCallback2(Main_ExpandedStarter);
}
