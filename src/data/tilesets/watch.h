// Selected Kanto tilesets with Emerald behavior IDs. Original assets remain untouched.
#if !IS_FRLG

const u32 gTilesetTiles_Watch_Building_Frlg[] = INCGFX_U32("data/tilesets/primary/building_frlg/tiles.png", ".4bpp.smol");

const u16 gTilesetPalettes_Watch_Building_Frlg[][16] =
{
    INCGFX_U16("data/tilesets/primary/building_frlg/palettes/00.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/primary/building_frlg/palettes/01.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/primary/building_frlg/palettes/02.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/primary/building_frlg/palettes/03.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/primary/building_frlg/palettes/04.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/primary/building_frlg/palettes/05.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/primary/building_frlg/palettes/06.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/primary/building_frlg/palettes/07.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/primary/building_frlg/palettes/08.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/primary/building_frlg/palettes/09.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/primary/building_frlg/palettes/10.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/primary/building_frlg/palettes/11.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/primary/building_frlg/palettes/12.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/primary/building_frlg/palettes/13.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/primary/building_frlg/palettes/14.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/primary/building_frlg/palettes/15.pal", ".gbapal"),
};

const u16 gMetatiles_Watch_Building_Frlg[] = INCBIN_U16("data/tilesets/primary/building_frlg/metatiles.bin");

const u16 gMetatileAttributes_Watch_Building_Frlg[] = INCBIN_U16("data/tilesets/watch/BuildingFrlg/metatile_attributes.bin");

const struct Tileset gTileset_Watch_BuildingFrlg =
{
    .isCompressed = TRUE,
    .isSecondary = FALSE,
    .tiles = gTilesetTiles_Watch_Building_Frlg,
    .palettes = gTilesetPalettes_Watch_Building_Frlg,
    .metatiles = gMetatiles_Watch_Building_Frlg,
    .metatileAttributes = gMetatileAttributes_Watch_Building_Frlg,
    .callback = NULL,
};

const u32 gTilesetTiles_Watch_General_Frlg[] = INCGFX_U32("data/tilesets/primary/general_frlg/tiles.png", ".4bpp.smol");

const u16 ALIGNED(4) gTilesetPalettes_Watch_General_Frlg[][16] =
{
    INCGFX_U16("data/tilesets/primary/general_frlg/palettes/00.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/primary/general_frlg/palettes/01.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/primary/general_frlg/palettes/02.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/primary/general_frlg/palettes/03.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/primary/general_frlg/palettes/04.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/primary/general_frlg/palettes/05.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/primary/general_frlg/palettes/06.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/primary/general_frlg/palettes/07.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/primary/general_frlg/palettes/08.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/primary/general_frlg/palettes/09.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/primary/general_frlg/palettes/10.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/primary/general_frlg/palettes/11.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/primary/general_frlg/palettes/12.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/primary/general_frlg/palettes/13.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/primary/general_frlg/palettes/14.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/primary/general_frlg/palettes/15.pal", ".gbapal"),
};

const u16 gMetatiles_Watch_General_Frlg[] = INCBIN_U16("data/tilesets/primary/general_frlg/metatiles.bin");

const u16 gMetatileAttributes_Watch_General_Frlg[] = INCBIN_U16("data/tilesets/watch/General_Frlg/metatile_attributes.bin");

const struct Tileset gTileset_Watch_General_Frlg =
{
    .isCompressed = TRUE,
    .isSecondary = FALSE,
    .tiles = gTilesetTiles_Watch_General_Frlg,
    .palettes = gTilesetPalettes_Watch_General_Frlg,
    .metatiles = gMetatiles_Watch_General_Frlg,
    .metatileAttributes = gMetatileAttributes_Watch_General_Frlg,
    .callback = InitTilesetAnim_General_Frlg,
};

const u32 gTilesetTiles_Watch_GenericBuilding1[] = INCGFX_U32("data/tilesets/secondary/generic_building_1_frlg/tiles.png", ".4bpp.fastSmol");

const u16 gTilesetPalettes_Watch_GenericBuilding1[][16] =
{
    INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/00.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/01.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/02.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/03.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/04.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/05.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/06.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/07.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/08.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/09.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/10.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/11.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/12.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/13.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/14.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/15.pal", ".gbapal"),
};

const u16 gMetatiles_Watch_GenericBuilding1[] = INCBIN_U16("data/tilesets/secondary/generic_building_1_frlg/metatiles.bin");

const u16 gMetatileAttributes_Watch_GenericBuilding1[] = INCBIN_U16("data/tilesets/watch/GenericBuilding1/metatile_attributes.bin");

const struct Tileset gTileset_Watch_GenericBuilding1 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Watch_GenericBuilding1,
    .palettes = gTilesetPalettes_Watch_GenericBuilding1,
    .metatiles = gMetatiles_Watch_GenericBuilding1,
    .metatileAttributes = gMetatileAttributes_Watch_GenericBuilding1,
    .callback = NULL,
};

const u32 gTilesetTiles_Watch_GenericBuilding2[] = INCGFX_U32("data/tilesets/secondary/generic_building_2_frlg/tiles.png", ".4bpp.fastSmol");

const u16 gTilesetPalettes_Watch_GenericBuilding2[][16] =
{
    INCGFX_U16("data/tilesets/secondary/generic_building_2_frlg/palettes/00.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/generic_building_2_frlg/palettes/01.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/generic_building_2_frlg/palettes/02.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/generic_building_2_frlg/palettes/03.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/generic_building_2_frlg/palettes/04.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/generic_building_2_frlg/palettes/05.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/generic_building_2_frlg/palettes/06.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/generic_building_2_frlg/palettes/07.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/generic_building_2_frlg/palettes/08.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/generic_building_2_frlg/palettes/09.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/generic_building_2_frlg/palettes/10.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/generic_building_2_frlg/palettes/11.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/generic_building_2_frlg/palettes/12.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/generic_building_2_frlg/palettes/13.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/generic_building_2_frlg/palettes/14.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/generic_building_2_frlg/palettes/15.pal", ".gbapal"),
};

const u16 gMetatiles_Watch_GenericBuilding2[] = INCBIN_U16("data/tilesets/secondary/generic_building_2_frlg/metatiles.bin");

const u16 gMetatileAttributes_Watch_GenericBuilding2[] = INCBIN_U16("data/tilesets/watch/GenericBuilding2/metatile_attributes.bin");

const struct Tileset gTileset_Watch_GenericBuilding2 =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Watch_GenericBuilding2,
    .palettes = gTilesetPalettes_Watch_GenericBuilding2,
    .metatiles = gMetatiles_Watch_GenericBuilding2,
    .metatileAttributes = gMetatileAttributes_Watch_GenericBuilding2,
    .callback = NULL,
};

const u32 gTilesetTiles_Watch_Lab_Frlg[] = INCGFX_U32("data/tilesets/secondary/lab_frlg/tiles.png", ".4bpp.fastSmol");

const u16 gTilesetPalettes_Watch_Lab_Frlg[][16] =
{
    INCGFX_U16("data/tilesets/secondary/lab_frlg/palettes/00.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/lab_frlg/palettes/01.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/lab_frlg/palettes/02.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/lab_frlg/palettes/03.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/lab_frlg/palettes/04.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/lab_frlg/palettes/05.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/lab_frlg/palettes/06.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/lab_frlg/palettes/07.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/lab_frlg/palettes/08.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/lab_frlg/palettes/09.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/lab_frlg/palettes/10.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/lab_frlg/palettes/11.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/lab_frlg/palettes/12.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/lab_frlg/palettes/13.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/lab_frlg/palettes/14.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/lab_frlg/palettes/15.pal", ".gbapal"),
};

const u16 gMetatiles_Watch_Lab_Frlg[] = INCBIN_U16("data/tilesets/secondary/lab_frlg/metatiles.bin");

const u16 gMetatileAttributes_Watch_Lab_Frlg[] = INCBIN_U16("data/tilesets/watch/Lab_Frlg/metatile_attributes.bin");

const struct Tileset gTileset_Watch_Lab_Frlg =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Watch_Lab_Frlg,
    .palettes = gTilesetPalettes_Watch_Lab_Frlg,
    .metatiles = gMetatiles_Watch_Lab_Frlg,
    .metatileAttributes = gMetatileAttributes_Watch_Lab_Frlg,
    .callback = NULL,
};

const u32 gTilesetTiles_Watch_Mart[] = INCGFX_U32("data/tilesets/secondary/mart_frlg/tiles.png", ".4bpp.fastSmol");

const u16 gTilesetPalettes_Watch_Mart[][16] =
{
    INCGFX_U16("data/tilesets/secondary/mart_frlg/palettes/00.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/mart_frlg/palettes/01.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/mart_frlg/palettes/02.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/mart_frlg/palettes/03.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/mart_frlg/palettes/04.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/mart_frlg/palettes/05.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/mart_frlg/palettes/06.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/mart_frlg/palettes/07.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/mart_frlg/palettes/08.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/mart_frlg/palettes/09.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/mart_frlg/palettes/10.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/mart_frlg/palettes/11.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/mart_frlg/palettes/12.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/mart_frlg/palettes/13.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/mart_frlg/palettes/14.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/mart_frlg/palettes/15.pal", ".gbapal"),
};

const u16 gMetatiles_Watch_Mart[] = INCBIN_U16("data/tilesets/secondary/mart_frlg/metatiles.bin");

const u16 gMetatileAttributes_Watch_Mart[] = INCBIN_U16("data/tilesets/watch/Mart/metatile_attributes.bin");

const struct Tileset gTileset_Watch_Mart =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Watch_Mart,
    .palettes = gTilesetPalettes_Watch_Mart,
    .metatiles = gMetatiles_Watch_Mart,
    .metatileAttributes = gMetatileAttributes_Watch_Mart,
    .callback = NULL,
};

const u32 gTilesetTiles_Watch_PalletTown[] = INCGFX_U32("data/tilesets/secondary/pallet_town_frlg/tiles.png", ".4bpp.fastSmol");

const u16 gTilesetPalettes_Watch_PalletTown[][16] =
{
    INCGFX_U16("data/tilesets/secondary/pallet_town_frlg/palettes/00.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/pallet_town_frlg/palettes/01.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/pallet_town_frlg/palettes/02.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/pallet_town_frlg/palettes/03.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/pallet_town_frlg/palettes/04.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/pallet_town_frlg/palettes/05.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/pallet_town_frlg/palettes/06.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/pallet_town_frlg/palettes/07.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/pallet_town_frlg/palettes/08.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/pallet_town_frlg/palettes/09.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/pallet_town_frlg/palettes/10.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/pallet_town_frlg/palettes/11.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/pallet_town_frlg/palettes/12.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/pallet_town_frlg/palettes/13.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/pallet_town_frlg/palettes/14.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/pallet_town_frlg/palettes/15.pal", ".gbapal"),
};

const u16 gMetatiles_Watch_PalletTown[] = INCBIN_U16("data/tilesets/secondary/pallet_town_frlg/metatiles.bin");

const u16 gMetatileAttributes_Watch_PalletTown[] = INCBIN_U16("data/tilesets/watch/PalletTown/metatile_attributes.bin");

const struct Tileset gTileset_Watch_PalletTown =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Watch_PalletTown,
    .palettes = gTilesetPalettes_Watch_PalletTown,
    .metatiles = gMetatiles_Watch_PalletTown,
    .metatileAttributes = gMetatileAttributes_Watch_PalletTown,
    .callback = NULL,
};

const u32 gTilesetTiles_Watch_PokemonCenter_Frlg[] = INCGFX_U32("data/tilesets/secondary/pokemon_center_frlg/tiles.png", ".4bpp.fastSmol");

const u16 gTilesetPalettes_Watch_PokemonCenter_Frlg[][16] =
{
    INCGFX_U16("data/tilesets/secondary/pokemon_center_frlg/palettes/00.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/pokemon_center_frlg/palettes/01.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/pokemon_center_frlg/palettes/02.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/pokemon_center_frlg/palettes/03.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/pokemon_center_frlg/palettes/04.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/pokemon_center_frlg/palettes/05.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/pokemon_center_frlg/palettes/06.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/pokemon_center_frlg/palettes/07.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/pokemon_center_frlg/palettes/08.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/pokemon_center_frlg/palettes/09.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/pokemon_center_frlg/palettes/10.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/pokemon_center_frlg/palettes/11.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/pokemon_center_frlg/palettes/12.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/pokemon_center_frlg/palettes/13.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/pokemon_center_frlg/palettes/14.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/pokemon_center_frlg/palettes/15.pal", ".gbapal"),
};

const u16 gMetatiles_Watch_PokemonCenter_Frlg[] = INCBIN_U16("data/tilesets/secondary/pokemon_center_frlg/metatiles.bin");

const u16 gMetatileAttributes_Watch_PokemonCenter_Frlg[] = INCBIN_U16("data/tilesets/watch/PokemonCenterFrlg/metatile_attributes.bin");

const struct Tileset gTileset_Watch_PokemonCenterFrlg =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Watch_PokemonCenter_Frlg,
    .palettes = gTilesetPalettes_Watch_PokemonCenter_Frlg,
    .metatiles = gMetatiles_Watch_PokemonCenter_Frlg,
    .metatileAttributes = gMetatileAttributes_Watch_PokemonCenter_Frlg,
    .callback = NULL,
};

const u32 gTilesetTiles_Watch_School[] = INCGFX_U32("data/tilesets/secondary/school_frlg/tiles.png", ".4bpp.fastSmol");

const u16 gTilesetPalettes_Watch_School[][16] =
{
    INCGFX_U16("data/tilesets/secondary/school_frlg/palettes/00.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/school_frlg/palettes/01.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/school_frlg/palettes/02.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/school_frlg/palettes/03.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/school_frlg/palettes/04.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/school_frlg/palettes/05.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/school_frlg/palettes/06.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/school_frlg/palettes/07.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/school_frlg/palettes/08.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/school_frlg/palettes/09.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/school_frlg/palettes/10.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/school_frlg/palettes/11.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/school_frlg/palettes/12.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/school_frlg/palettes/13.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/school_frlg/palettes/14.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/school_frlg/palettes/15.pal", ".gbapal"),
};

const u16 gMetatiles_Watch_School[] = INCBIN_U16("data/tilesets/secondary/school_frlg/metatiles.bin");

const u16 gMetatileAttributes_Watch_School[] = INCBIN_U16("data/tilesets/watch/School/metatile_attributes.bin");

const struct Tileset gTileset_Watch_School =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Watch_School,
    .palettes = gTilesetPalettes_Watch_School,
    .metatiles = gMetatiles_Watch_School,
    .metatileAttributes = gMetatileAttributes_Watch_School,
    .callback = NULL,
};

const u32 gTilesetTiles_Watch_ViridianCity[] = INCGFX_U32("data/tilesets/secondary/viridian_city_frlg/tiles.png", ".4bpp.fastSmol");

const u16 gTilesetPalettes_Watch_ViridianCity[][16] =
{
    INCGFX_U16("data/tilesets/secondary/viridian_city_frlg/palettes/00.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/viridian_city_frlg/palettes/01.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/viridian_city_frlg/palettes/02.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/viridian_city_frlg/palettes/03.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/viridian_city_frlg/palettes/04.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/viridian_city_frlg/palettes/05.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/viridian_city_frlg/palettes/06.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/viridian_city_frlg/palettes/07.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/viridian_city_frlg/palettes/08.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/viridian_city_frlg/palettes/09.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/viridian_city_frlg/palettes/10.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/viridian_city_frlg/palettes/11.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/viridian_city_frlg/palettes/12.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/viridian_city_frlg/palettes/13.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/viridian_city_frlg/palettes/14.pal", ".gbapal"),
    INCGFX_U16("data/tilesets/secondary/viridian_city_frlg/palettes/15.pal", ".gbapal"),
};

const u16 gMetatiles_Watch_ViridianCity[] = INCBIN_U16("data/tilesets/secondary/viridian_city_frlg/metatiles.bin");

const u16 gMetatileAttributes_Watch_ViridianCity[] = INCBIN_U16("data/tilesets/watch/ViridianCity/metatile_attributes.bin");

const struct Tileset gTileset_Watch_ViridianCity =
{
    .isCompressed = TRUE,
    .isSecondary = TRUE,
    .tiles = gTilesetTiles_Watch_ViridianCity,
    .palettes = gTilesetPalettes_Watch_ViridianCity,
    .metatiles = gMetatiles_Watch_ViridianCity,
    .metatileAttributes = gMetatileAttributes_Watch_ViridianCity,
    .callback = NULL,
};

#endif
