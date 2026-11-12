#if !IS_FRLG
const u16 gVoidTownPalettes[][16] = {
    INCGFX_U16("data/void_oldale/Town/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Town/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Town/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Town/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Town/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Town/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Town/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Town/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Town/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Town/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Town/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Town/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Town/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Town/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Town/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Town/palette.pal", ".gbapal"),
};
const u32 gVoidTownPrimaryTiles[] = INCBIN_U32("data/void_oldale/Town/Primary.4bpp.smol");
const u16 gVoidTownPrimaryMetatiles[] = INCBIN_U16("data/void_oldale/Town/PrimaryMetatiles.bin");
const u16 gVoidTownPrimaryAttributes[] = INCBIN_U16("data/void_oldale/Town/PrimaryAttributes.bin");
const struct Tileset gTileset_VoidTownPrimary = {.isCompressed=TRUE,.isSecondary=FALSE,.tiles=gVoidTownPrimaryTiles,.palettes=gVoidTownPalettes,.metatiles=gVoidTownPrimaryMetatiles,.metatileAttributes=gVoidTownPrimaryAttributes,.callback=NULL};
const u32 gVoidTownSecondaryTiles[] = INCBIN_U32("data/void_oldale/Town/Secondary.4bpp.smol");
const u16 gVoidTownSecondaryMetatiles[] = INCBIN_U16("data/void_oldale/Town/SecondaryMetatiles.bin");
const u16 gVoidTownSecondaryAttributes[] = INCBIN_U16("data/void_oldale/Town/SecondaryAttributes.bin");
const struct Tileset gTileset_VoidTownSecondary = {.isCompressed=TRUE,.isSecondary=TRUE,.tiles=gVoidTownSecondaryTiles,.palettes=gVoidTownPalettes,.metatiles=gVoidTownSecondaryMetatiles,.metatileAttributes=gVoidTownSecondaryAttributes,.callback=NULL};
const u16 gVoidCottagePalettes[][16] = {
    INCGFX_U16("data/void_oldale/Cottage/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Cottage/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Cottage/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Cottage/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Cottage/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Cottage/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Cottage/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Cottage/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Cottage/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Cottage/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Cottage/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Cottage/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Cottage/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Cottage/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Cottage/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Cottage/palette.pal", ".gbapal"),
};
const u32 gVoidCottagePrimaryTiles[] = INCBIN_U32("data/void_oldale/Cottage/Primary.4bpp.smol");
const u16 gVoidCottagePrimaryMetatiles[] = INCBIN_U16("data/void_oldale/Cottage/PrimaryMetatiles.bin");
const u16 gVoidCottagePrimaryAttributes[] = INCBIN_U16("data/void_oldale/Cottage/PrimaryAttributes.bin");
const struct Tileset gTileset_VoidCottagePrimary = {.isCompressed=TRUE,.isSecondary=FALSE,.tiles=gVoidCottagePrimaryTiles,.palettes=gVoidCottagePalettes,.metatiles=gVoidCottagePrimaryMetatiles,.metatileAttributes=gVoidCottagePrimaryAttributes,.callback=NULL};
const u32 gVoidCottageSecondaryTiles[] = INCBIN_U32("data/void_oldale/Cottage/Secondary.4bpp.smol");
const u16 gVoidCottageSecondaryMetatiles[] = INCBIN_U16("data/void_oldale/Cottage/SecondaryMetatiles.bin");
const u16 gVoidCottageSecondaryAttributes[] = INCBIN_U16("data/void_oldale/Cottage/SecondaryAttributes.bin");
const struct Tileset gTileset_VoidCottageSecondary = {.isCompressed=TRUE,.isSecondary=TRUE,.tiles=gVoidCottageSecondaryTiles,.palettes=gVoidCottagePalettes,.metatiles=gVoidCottageSecondaryMetatiles,.metatileAttributes=gVoidCottageSecondaryAttributes,.callback=NULL};
const u16 gVoidWorkshopPalettes[][16] = {
    INCGFX_U16("data/void_oldale/Workshop/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Workshop/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Workshop/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Workshop/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Workshop/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Workshop/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Workshop/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Workshop/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Workshop/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Workshop/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Workshop/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Workshop/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Workshop/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Workshop/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Workshop/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Workshop/palette.pal", ".gbapal"),
};
const u32 gVoidWorkshopPrimaryTiles[] = INCBIN_U32("data/void_oldale/Workshop/Primary.4bpp.smol");
const u16 gVoidWorkshopPrimaryMetatiles[] = INCBIN_U16("data/void_oldale/Workshop/PrimaryMetatiles.bin");
const u16 gVoidWorkshopPrimaryAttributes[] = INCBIN_U16("data/void_oldale/Workshop/PrimaryAttributes.bin");
const struct Tileset gTileset_VoidWorkshopPrimary = {.isCompressed=TRUE,.isSecondary=FALSE,.tiles=gVoidWorkshopPrimaryTiles,.palettes=gVoidWorkshopPalettes,.metatiles=gVoidWorkshopPrimaryMetatiles,.metatileAttributes=gVoidWorkshopPrimaryAttributes,.callback=NULL};
const u32 gVoidWorkshopSecondaryTiles[] = INCBIN_U32("data/void_oldale/Workshop/Secondary.4bpp.smol");
const u16 gVoidWorkshopSecondaryMetatiles[] = INCBIN_U16("data/void_oldale/Workshop/SecondaryMetatiles.bin");
const u16 gVoidWorkshopSecondaryAttributes[] = INCBIN_U16("data/void_oldale/Workshop/SecondaryAttributes.bin");
const struct Tileset gTileset_VoidWorkshopSecondary = {.isCompressed=TRUE,.isSecondary=TRUE,.tiles=gVoidWorkshopSecondaryTiles,.palettes=gVoidWorkshopPalettes,.metatiles=gVoidWorkshopSecondaryMetatiles,.metatileAttributes=gVoidWorkshopSecondaryAttributes,.callback=NULL};
const u16 gVoidRestHousePalettes[][16] = {
    INCGFX_U16("data/void_oldale/RestHouse/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/RestHouse/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/RestHouse/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/RestHouse/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/RestHouse/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/RestHouse/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/RestHouse/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/RestHouse/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/RestHouse/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/RestHouse/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/RestHouse/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/RestHouse/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/RestHouse/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/RestHouse/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/RestHouse/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/RestHouse/palette.pal", ".gbapal"),
};
const u32 gVoidRestHousePrimaryTiles[] = INCBIN_U32("data/void_oldale/RestHouse/Primary.4bpp.smol");
const u16 gVoidRestHousePrimaryMetatiles[] = INCBIN_U16("data/void_oldale/RestHouse/PrimaryMetatiles.bin");
const u16 gVoidRestHousePrimaryAttributes[] = INCBIN_U16("data/void_oldale/RestHouse/PrimaryAttributes.bin");
const struct Tileset gTileset_VoidRestHousePrimary = {.isCompressed=TRUE,.isSecondary=FALSE,.tiles=gVoidRestHousePrimaryTiles,.palettes=gVoidRestHousePalettes,.metatiles=gVoidRestHousePrimaryMetatiles,.metatileAttributes=gVoidRestHousePrimaryAttributes,.callback=NULL};
const u32 gVoidRestHouseSecondaryTiles[] = INCBIN_U32("data/void_oldale/RestHouse/Secondary.4bpp.smol");
const u16 gVoidRestHouseSecondaryMetatiles[] = INCBIN_U16("data/void_oldale/RestHouse/SecondaryMetatiles.bin");
const u16 gVoidRestHouseSecondaryAttributes[] = INCBIN_U16("data/void_oldale/RestHouse/SecondaryAttributes.bin");
const struct Tileset gTileset_VoidRestHouseSecondary = {.isCompressed=TRUE,.isSecondary=TRUE,.tiles=gVoidRestHouseSecondaryTiles,.palettes=gVoidRestHousePalettes,.metatiles=gVoidRestHouseSecondaryMetatiles,.metatileAttributes=gVoidRestHouseSecondaryAttributes,.callback=NULL};
const u16 gVoidShopPalettes[][16] = {
    INCGFX_U16("data/void_oldale/Shop/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Shop/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Shop/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Shop/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Shop/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Shop/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Shop/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Shop/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Shop/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Shop/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Shop/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Shop/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Shop/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Shop/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Shop/palette.pal", ".gbapal"),
    INCGFX_U16("data/void_oldale/Shop/palette.pal", ".gbapal"),
};
const u32 gVoidShopPrimaryTiles[] = INCBIN_U32("data/void_oldale/Shop/Primary.4bpp.smol");
const u16 gVoidShopPrimaryMetatiles[] = INCBIN_U16("data/void_oldale/Shop/PrimaryMetatiles.bin");
const u16 gVoidShopPrimaryAttributes[] = INCBIN_U16("data/void_oldale/Shop/PrimaryAttributes.bin");
const struct Tileset gTileset_VoidShopPrimary = {.isCompressed=TRUE,.isSecondary=FALSE,.tiles=gVoidShopPrimaryTiles,.palettes=gVoidShopPalettes,.metatiles=gVoidShopPrimaryMetatiles,.metatileAttributes=gVoidShopPrimaryAttributes,.callback=NULL};
const u32 gVoidShopSecondaryTiles[] = INCBIN_U32("data/void_oldale/Shop/Secondary.4bpp.smol");
const u16 gVoidShopSecondaryMetatiles[] = INCBIN_U16("data/void_oldale/Shop/SecondaryMetatiles.bin");
const u16 gVoidShopSecondaryAttributes[] = INCBIN_U16("data/void_oldale/Shop/SecondaryAttributes.bin");
const struct Tileset gTileset_VoidShopSecondary = {.isCompressed=TRUE,.isSecondary=TRUE,.tiles=gVoidShopSecondaryTiles,.palettes=gVoidShopPalettes,.metatiles=gVoidShopSecondaryMetatiles,.metatileAttributes=gVoidShopSecondaryAttributes,.callback=NULL};
#endif
