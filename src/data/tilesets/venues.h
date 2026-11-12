#if !IS_FRLG
const u32 gTileset_VenueHoennTutorTiles[] = INCBIN_U32("data/venues/HoennTutor/exterior/tiles.bin.smol");
const u16 gTileset_VenueHoennTutorMetatiles[] = INCBIN_U16("data/venues/HoennTutor/exterior/metatiles.bin");
const u16 gTileset_VenueHoennTutorAttributes[] = INCBIN_U16("data/venues/HoennTutor/exterior/attributes.bin");
const struct Tileset gTileset_VenueHoennTutor = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueHoennTutorTiles, .palettes=gTilesetPalettes_Petalburg, .metatiles=gTileset_VenueHoennTutorMetatiles, .metatileAttributes=gTileset_VenueHoennTutorAttributes, .callback=InitTilesetAnim_Petalburg};
const u32 gTileset_VenueHoennTutorRoomTiles[] = INCBIN_U32("data/venues/HoennTutor/interior/tiles.bin.smol");
const u16 gTileset_VenueHoennTutorRoomMetatiles[] = INCBIN_U16("data/venues/HoennTutor/interior/metatiles.bin");
const u16 gTileset_VenueHoennTutorRoomAttributes[] = INCBIN_U16("data/venues/HoennTutor/interior/attributes.bin");
const struct Tileset gTileset_VenueHoennTutorRoom = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueHoennTutorRoomTiles, .palettes=gTilesetPalettes_GenericBuilding, .metatiles=gTileset_VenueHoennTutorRoomMetatiles, .metatileAttributes=gTileset_VenueHoennTutorRoomAttributes, .callback=NULL};
const u32 gTileset_VenueHoennBakeryTiles[] = INCBIN_U32("data/venues/HoennBakery/exterior/tiles.bin.smol");
const u16 gTileset_VenueHoennBakeryMetatiles[] = INCBIN_U16("data/venues/HoennBakery/exterior/metatiles.bin");
const u16 gTileset_VenueHoennBakeryAttributes[] = INCBIN_U16("data/venues/HoennBakery/exterior/attributes.bin");
const struct Tileset gTileset_VenueHoennBakery = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueHoennBakeryTiles, .palettes=gTilesetPalettes_Rustboro, .metatiles=gTileset_VenueHoennBakeryMetatiles, .metatileAttributes=gTileset_VenueHoennBakeryAttributes, .callback=InitTilesetAnim_Rustboro};
const u32 gTileset_VenueHoennBakeryRoomTiles[] = INCBIN_U32("data/venues/HoennBakery/interior/tiles.bin.smol");
const u16 gTileset_VenueHoennBakeryRoomMetatiles[] = INCBIN_U16("data/venues/HoennBakery/interior/metatiles.bin");
const u16 gTileset_VenueHoennBakeryRoomAttributes[] = INCBIN_U16("data/venues/HoennBakery/interior/attributes.bin");
const struct Tileset gTileset_VenueHoennBakeryRoom = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueHoennBakeryRoomTiles, .palettes=gTilesetPalettes_GenericBuilding, .metatiles=gTileset_VenueHoennBakeryRoomMetatiles, .metatileAttributes=gTileset_VenueHoennBakeryRoomAttributes, .callback=NULL};
const u32 gTileset_VenueHoennTeaTiles[] = INCBIN_U32("data/venues/HoennTea/exterior/tiles.bin.smol");
const u16 gTileset_VenueHoennTeaMetatiles[] = INCBIN_U16("data/venues/HoennTea/exterior/metatiles.bin");
const u16 gTileset_VenueHoennTeaAttributes[] = INCBIN_U16("data/venues/HoennTea/exterior/attributes.bin");
const struct Tileset gTileset_VenueHoennTea = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueHoennTeaTiles, .palettes=gTilesetPalettes_Slateport, .metatiles=gTileset_VenueHoennTeaMetatiles, .metatileAttributes=gTileset_VenueHoennTeaAttributes, .callback=InitTilesetAnim_Slateport};
const u32 gTileset_VenueHoennTeaRoomTiles[] = INCBIN_U32("data/venues/HoennTea/interior/tiles.bin.smol");
const u16 gTileset_VenueHoennTeaRoomMetatiles[] = INCBIN_U16("data/venues/HoennTea/interior/metatiles.bin");
const u16 gTileset_VenueHoennTeaRoomAttributes[] = INCBIN_U16("data/venues/HoennTea/interior/attributes.bin");
const struct Tileset gTileset_VenueHoennTeaRoom = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueHoennTeaRoomTiles, .palettes=gTilesetPalettes_GenericBuilding, .metatiles=gTileset_VenueHoennTeaRoomMetatiles, .metatileAttributes=gTileset_VenueHoennTeaRoomAttributes, .callback=NULL};
const u32 gTileset_VenueHoennGlitchTiles[] = INCBIN_U32("data/venues/HoennGlitch/exterior/tiles.bin.smol");
const u16 gTileset_VenueHoennGlitchMetatiles[] = INCBIN_U16("data/venues/HoennGlitch/exterior/metatiles.bin");
const u16 gTileset_VenueHoennGlitchAttributes[] = INCBIN_U16("data/venues/HoennGlitch/exterior/attributes.bin");
const struct Tileset gTileset_VenueHoennGlitch = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueHoennGlitchTiles, .palettes=gTilesetPalettes_Mauville, .metatiles=gTileset_VenueHoennGlitchMetatiles, .metatileAttributes=gTileset_VenueHoennGlitchAttributes, .callback=InitTilesetAnim_Mauville};
const u32 gTileset_VenueHoennGlitchRoomTiles[] = INCBIN_U32("data/venues/HoennGlitch/interior/tiles.bin.smol");
const u16 gTileset_VenueHoennGlitchRoomMetatiles[] = INCBIN_U16("data/venues/HoennGlitch/interior/metatiles.bin");
const u16 gTileset_VenueHoennGlitchRoomAttributes[] = INCBIN_U16("data/venues/HoennGlitch/interior/attributes.bin");
const struct Tileset gTileset_VenueHoennGlitchRoom = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueHoennGlitchRoomTiles, .palettes=gTilesetPalettes_GenericBuilding, .metatiles=gTileset_VenueHoennGlitchRoomMetatiles, .metatileAttributes=gTileset_VenueHoennGlitchRoomAttributes, .callback=NULL};
const u32 gTileset_VenueHoennBloomTiles[] = INCBIN_U32("data/venues/HoennBloom/exterior/tiles.bin.smol");
const u16 gTileset_VenueHoennBloomMetatiles[] = INCBIN_U16("data/venues/HoennBloom/exterior/metatiles.bin");
const u16 gTileset_VenueHoennBloomAttributes[] = INCBIN_U16("data/venues/HoennBloom/exterior/attributes.bin");
const struct Tileset gTileset_VenueHoennBloom = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueHoennBloomTiles, .palettes=gTilesetPalettes_Mauville, .metatiles=gTileset_VenueHoennBloomMetatiles, .metatileAttributes=gTileset_VenueHoennBloomAttributes, .callback=InitTilesetAnim_Mauville};
const u32 gTileset_VenueHoennBloomRoomTiles[] = INCBIN_U32("data/venues/HoennBloom/interior/tiles.bin.smol");
const u16 gTileset_VenueHoennBloomRoomMetatiles[] = INCBIN_U16("data/venues/HoennBloom/interior/metatiles.bin");
const u16 gTileset_VenueHoennBloomRoomAttributes[] = INCBIN_U16("data/venues/HoennBloom/interior/attributes.bin");
const struct Tileset gTileset_VenueHoennBloomRoom = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueHoennBloomRoomTiles, .palettes=gTilesetPalettes_GenericBuilding, .metatiles=gTileset_VenueHoennBloomRoomMetatiles, .metatileAttributes=gTileset_VenueHoennBloomRoomAttributes, .callback=NULL};
const u32 gTileset_VenueHoennRaveTiles[] = INCBIN_U32("data/venues/HoennRave/exterior/tiles.bin.smol");
const u16 gTileset_VenueHoennRaveMetatiles[] = INCBIN_U16("data/venues/HoennRave/exterior/metatiles.bin");
const u16 gTileset_VenueHoennRaveAttributes[] = INCBIN_U16("data/venues/HoennRave/exterior/attributes.bin");
const struct Tileset gTileset_VenueHoennRave = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueHoennRaveTiles, .palettes=gTilesetPalettes_Lilycove, .metatiles=gTileset_VenueHoennRaveMetatiles, .metatileAttributes=gTileset_VenueHoennRaveAttributes, .callback=InitTilesetAnim_Lilycove};
const u32 gTileset_VenueHoennRaveRoomTiles[] = INCBIN_U32("data/venues/HoennRave/interior/tiles.bin.smol");
const u16 gTileset_VenueHoennRaveRoomMetatiles[] = INCBIN_U16("data/venues/HoennRave/interior/metatiles.bin");
const u16 gTileset_VenueHoennRaveRoomAttributes[] = INCBIN_U16("data/venues/HoennRave/interior/attributes.bin");
const struct Tileset gTileset_VenueHoennRaveRoom = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueHoennRaveRoomTiles, .palettes=gTilesetPalettes_GenericBuilding, .metatiles=gTileset_VenueHoennRaveRoomMetatiles, .metatileAttributes=gTileset_VenueHoennRaveRoomAttributes, .callback=NULL};
const u32 gTileset_VenueKantoBakeryTiles[] = INCBIN_U32("data/venues/KantoBakery/exterior/tiles.bin.smol");
const u16 gTileset_VenueKantoBakeryMetatiles[] = INCBIN_U16("data/venues/KantoBakery/exterior/metatiles.bin");
const u16 gTileset_VenueKantoBakeryAttributes[] = INCBIN_U16("data/venues/KantoBakery/exterior/attributes.bin");
const struct Tileset gTileset_VenueKantoBakery = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueKantoBakeryTiles, .palettes=gTilesetPalettes_Kanto_ViridianCity, .metatiles=gTileset_VenueKantoBakeryMetatiles, .metatileAttributes=gTileset_VenueKantoBakeryAttributes, .callback=NULL};
const u32 gTileset_VenueKantoBakeryRoomTiles[] = INCBIN_U32("data/venues/KantoBakery/interior/tiles.bin.smol");
const u16 gTileset_VenueKantoBakeryRoomMetatiles[] = INCBIN_U16("data/venues/KantoBakery/interior/metatiles.bin");
const u16 gTileset_VenueKantoBakeryRoomAttributes[] = INCBIN_U16("data/venues/KantoBakery/interior/attributes.bin");
const struct Tileset gTileset_VenueKantoBakeryRoom = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueKantoBakeryRoomTiles, .palettes=gTilesetPalettes_Kanto_GenericBuilding1, .metatiles=gTileset_VenueKantoBakeryRoomMetatiles, .metatileAttributes=gTileset_VenueKantoBakeryRoomAttributes, .callback=NULL};
const u32 gTileset_VenueKantoGlitchTiles[] = INCBIN_U32("data/venues/KantoGlitch/exterior/tiles.bin.smol");
const u16 gTileset_VenueKantoGlitchMetatiles[] = INCBIN_U16("data/venues/KantoGlitch/exterior/metatiles.bin");
const u16 gTileset_VenueKantoGlitchAttributes[] = INCBIN_U16("data/venues/KantoGlitch/exterior/attributes.bin");
const struct Tileset gTileset_VenueKantoGlitch = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueKantoGlitchTiles, .palettes=gTilesetPalettes_Kanto_PewterCity, .metatiles=gTileset_VenueKantoGlitchMetatiles, .metatileAttributes=gTileset_VenueKantoGlitchAttributes, .callback=NULL};
const u32 gTileset_VenueKantoGlitchRoomTiles[] = INCBIN_U32("data/venues/KantoGlitch/interior/tiles.bin.smol");
const u16 gTileset_VenueKantoGlitchRoomMetatiles[] = INCBIN_U16("data/venues/KantoGlitch/interior/metatiles.bin");
const u16 gTileset_VenueKantoGlitchRoomAttributes[] = INCBIN_U16("data/venues/KantoGlitch/interior/attributes.bin");
const struct Tileset gTileset_VenueKantoGlitchRoom = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueKantoGlitchRoomTiles, .palettes=gTilesetPalettes_Kanto_GenericBuilding1, .metatiles=gTileset_VenueKantoGlitchRoomMetatiles, .metatileAttributes=gTileset_VenueKantoGlitchRoomAttributes, .callback=NULL};
const u32 gTileset_VenueKantoTeaTiles[] = INCBIN_U32("data/venues/KantoTea/exterior/tiles.bin.smol");
const u16 gTileset_VenueKantoTeaMetatiles[] = INCBIN_U16("data/venues/KantoTea/exterior/metatiles.bin");
const u16 gTileset_VenueKantoTeaAttributes[] = INCBIN_U16("data/venues/KantoTea/exterior/attributes.bin");
const struct Tileset gTileset_VenueKantoTea = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueKantoTeaTiles, .palettes=gTilesetPalettes_Kanto_VermilionCity, .metatiles=gTileset_VenueKantoTeaMetatiles, .metatileAttributes=gTileset_VenueKantoTeaAttributes, .callback=NULL};
const u32 gTileset_VenueKantoTeaRoomTiles[] = INCBIN_U32("data/venues/KantoTea/interior/tiles.bin.smol");
const u16 gTileset_VenueKantoTeaRoomMetatiles[] = INCBIN_U16("data/venues/KantoTea/interior/metatiles.bin");
const u16 gTileset_VenueKantoTeaRoomAttributes[] = INCBIN_U16("data/venues/KantoTea/interior/attributes.bin");
const struct Tileset gTileset_VenueKantoTeaRoom = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueKantoTeaRoomTiles, .palettes=gTilesetPalettes_Kanto_GenericBuilding1, .metatiles=gTileset_VenueKantoTeaRoomMetatiles, .metatileAttributes=gTileset_VenueKantoTeaRoomAttributes, .callback=NULL};
const u32 gTileset_VenueKantoTutorTiles[] = INCBIN_U32("data/venues/KantoTutor/exterior/tiles.bin.smol");
const u16 gTileset_VenueKantoTutorMetatiles[] = INCBIN_U16("data/venues/KantoTutor/exterior/metatiles.bin");
const u16 gTileset_VenueKantoTutorAttributes[] = INCBIN_U16("data/venues/KantoTutor/exterior/attributes.bin");
const struct Tileset gTileset_VenueKantoTutor = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueKantoTutorTiles, .palettes=gTilesetPalettes_Kanto_CeruleanCity, .metatiles=gTileset_VenueKantoTutorMetatiles, .metatileAttributes=gTileset_VenueKantoTutorAttributes, .callback=NULL};
const u32 gTileset_VenueKantoTutorRoomTiles[] = INCBIN_U32("data/venues/KantoTutor/interior/tiles.bin.smol");
const u16 gTileset_VenueKantoTutorRoomMetatiles[] = INCBIN_U16("data/venues/KantoTutor/interior/metatiles.bin");
const u16 gTileset_VenueKantoTutorRoomAttributes[] = INCBIN_U16("data/venues/KantoTutor/interior/attributes.bin");
const struct Tileset gTileset_VenueKantoTutorRoom = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueKantoTutorRoomTiles, .palettes=gTilesetPalettes_Kanto_GenericBuilding1, .metatiles=gTileset_VenueKantoTutorRoomMetatiles, .metatileAttributes=gTileset_VenueKantoTutorRoomAttributes, .callback=NULL};
const u32 gTileset_VenueKantoRaveTiles[] = INCBIN_U32("data/venues/KantoRave/exterior/tiles.bin.smol");
const u16 gTileset_VenueKantoRaveMetatiles[] = INCBIN_U16("data/venues/KantoRave/exterior/metatiles.bin");
const u16 gTileset_VenueKantoRaveAttributes[] = INCBIN_U16("data/venues/KantoRave/exterior/attributes.bin");
const struct Tileset gTileset_VenueKantoRave = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueKantoRaveTiles, .palettes=gTilesetPalettes_Kanto_FuchsiaCity, .metatiles=gTileset_VenueKantoRaveMetatiles, .metatileAttributes=gTileset_VenueKantoRaveAttributes, .callback=NULL};
const u32 gTileset_VenueKantoRaveRoomTiles[] = INCBIN_U32("data/venues/KantoRave/interior/tiles.bin.smol");
const u16 gTileset_VenueKantoRaveRoomMetatiles[] = INCBIN_U16("data/venues/KantoRave/interior/metatiles.bin");
const u16 gTileset_VenueKantoRaveRoomAttributes[] = INCBIN_U16("data/venues/KantoRave/interior/attributes.bin");
const struct Tileset gTileset_VenueKantoRaveRoom = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueKantoRaveRoomTiles, .palettes=gTilesetPalettes_Kanto_GenericBuilding1, .metatiles=gTileset_VenueKantoRaveRoomMetatiles, .metatileAttributes=gTileset_VenueKantoRaveRoomAttributes, .callback=NULL};
const u32 gTileset_VenueKantoBloomTiles[] = INCBIN_U32("data/venues/KantoBloom/exterior/tiles.bin.smol");
const u16 gTileset_VenueKantoBloomMetatiles[] = INCBIN_U16("data/venues/KantoBloom/exterior/metatiles.bin");
const u16 gTileset_VenueKantoBloomAttributes[] = INCBIN_U16("data/venues/KantoBloom/exterior/attributes.bin");
const struct Tileset gTileset_VenueKantoBloom = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueKantoBloomTiles, .palettes=gTilesetPalettes_Kanto_CeladonCity, .metatiles=gTileset_VenueKantoBloomMetatiles, .metatileAttributes=gTileset_VenueKantoBloomAttributes, .callback=InitTilesetAnim_CeladonCity};
const u32 gTileset_VenueKantoBloomRoomTiles[] = INCBIN_U32("data/venues/KantoBloom/interior/tiles.bin.smol");
const u16 gTileset_VenueKantoBloomRoomMetatiles[] = INCBIN_U16("data/venues/KantoBloom/interior/metatiles.bin");
const u16 gTileset_VenueKantoBloomRoomAttributes[] = INCBIN_U16("data/venues/KantoBloom/interior/attributes.bin");
const struct Tileset gTileset_VenueKantoBloomRoom = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueKantoBloomRoomTiles, .palettes=gTilesetPalettes_Kanto_GenericBuilding1, .metatiles=gTileset_VenueKantoBloomRoomMetatiles, .metatileAttributes=gTileset_VenueKantoBloomRoomAttributes, .callback=NULL};
const u32 gTileset_VenueKantoSaffronPrimaryTiles[] = INCBIN_U32("data/venues/SaffronFacades/primary/tiles.bin.smol");
const struct Tileset gTileset_VenueKantoSaffronPrimary = {.isCompressed=TRUE, .isSecondary=FALSE, .tiles=gTileset_VenueKantoSaffronPrimaryTiles, .palettes=gTilesetPalettes_Kanto_General_Frlg, .metatiles=gMetatiles_Kanto_General_Frlg, .metatileAttributes=gMetatileAttributes_Kanto_General_Frlg, .callback=InitTilesetAnim_General_Frlg};
const u32 gTileset_VenueKantoSaffronSecondaryTiles[] = INCBIN_U32("data/venues/SaffronFacades/secondary/tiles.bin.smol");
const u16 gTileset_VenueKantoSaffronSecondaryMetatiles[] = INCBIN_U16("data/venues/SaffronFacades/secondary/metatiles.bin");
const u16 gTileset_VenueKantoSaffronSecondaryAttributes[] = INCBIN_U16("data/venues/SaffronFacades/secondary/attributes.bin");
const struct Tileset gTileset_VenueKantoSaffronSecondary = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueKantoSaffronSecondaryTiles, .palettes=gTilesetPalettes_Kanto_SaffronCity, .metatiles=gTileset_VenueKantoSaffronSecondaryMetatiles, .metatileAttributes=gTileset_VenueKantoSaffronSecondaryAttributes, .callback=NULL};
const u16 sVenuePalette0[] = INCGFX_U16("graphics/custom_buildings/pastel_pack/modules/hoenn/tutor/exterior/palette-00.pal", ".gbapal");
const u16 sVenuePalette1[] = INCGFX_U16("data/venues/HoennTutor/interior/07.pal", ".gbapal");
const u16 sVenuePalette2[] = INCGFX_U16("data/venues/HoennTutor/interior/11.pal", ".gbapal");
const u16 sVenuePalette3[] = INCGFX_U16("graphics/custom_buildings/pastel_pack/modules/hoenn/bakery/exterior/palette-00.pal", ".gbapal");
const u16 sVenuePalette4[] = INCGFX_U16("data/venues/HoennBakery/interior/07.pal", ".gbapal");
const u16 sVenuePalette5[] = INCGFX_U16("data/venues/HoennBakery/interior/11.pal", ".gbapal");
const u16 sVenuePalette6[] = INCGFX_U16("graphics/custom_buildings/pastel_pack/modules/hoenn/tea/exterior/palette-00.pal", ".gbapal");
const u16 sVenuePalette7[] = INCGFX_U16("data/venues/HoennTea/interior/07.pal", ".gbapal");
const u16 sVenuePalette8[] = INCGFX_U16("data/venues/HoennTea/interior/11.pal", ".gbapal");
const u16 sVenuePalette9[] = INCGFX_U16("graphics/custom_buildings/pastel_pack/modules/hoenn/glitch/exterior/palette-00.pal", ".gbapal");
const u16 sVenuePalette10[] = INCGFX_U16("data/venues/HoennGlitch/interior/07.pal", ".gbapal");
const u16 sVenuePalette11[] = INCGFX_U16("data/venues/HoennGlitch/interior/11.pal", ".gbapal");
const u16 sVenuePalette12[] = INCGFX_U16("graphics/custom_buildings/pastel_pack/modules/hoenn/bloom/exterior/palette-00.pal", ".gbapal");
const u16 sVenuePalette13[] = INCGFX_U16("data/venues/HoennBloom/interior/07.pal", ".gbapal");
const u16 sVenuePalette14[] = INCGFX_U16("data/venues/HoennBloom/interior/11.pal", ".gbapal");
const u16 sVenuePalette15[] = INCGFX_U16("graphics/custom_buildings/pastel_pack/modules/hoenn/rave/exterior/palette-00.pal", ".gbapal");
const u16 sVenuePalette16[] = INCGFX_U16("data/venues/HoennRave/interior/07.pal", ".gbapal");
const u16 sVenuePalette17[] = INCGFX_U16("data/venues/HoennRave/interior/11.pal", ".gbapal");
const u16 sVenuePalette18[] = INCGFX_U16("graphics/custom_buildings/pastel_pack/modules/kanto/bakery/exterior/palette-00.pal", ".gbapal");
const u16 sVenuePalette19[] = INCGFX_U16("data/venues/KantoBakery/interior/07.pal", ".gbapal");
const u16 sVenuePalette20[] = INCGFX_U16("data/venues/KantoBakery/interior/08.pal", ".gbapal");
const u16 sVenuePalette21[] = INCGFX_U16("graphics/custom_buildings/pastel_pack/modules/kanto/glitch/exterior/palette-00.pal", ".gbapal");
const u16 sVenuePalette22[] = INCGFX_U16("data/venues/KantoGlitch/interior/07.pal", ".gbapal");
const u16 sVenuePalette23[] = INCGFX_U16("data/venues/KantoGlitch/interior/08.pal", ".gbapal");
const u16 sVenuePalette24[] = INCGFX_U16("graphics/custom_buildings/pastel_pack/modules/kanto/tea/exterior/palette-00.pal", ".gbapal");
const u16 sVenuePalette25[] = INCGFX_U16("data/venues/KantoTea/interior/07.pal", ".gbapal");
const u16 sVenuePalette26[] = INCGFX_U16("data/venues/KantoTea/interior/08.pal", ".gbapal");
const u16 sVenuePalette27[] = INCGFX_U16("graphics/custom_buildings/pastel_pack/modules/kanto/tutor/exterior/palette-00.pal", ".gbapal");
const u16 sVenuePalette28[] = INCGFX_U16("data/venues/KantoTutor/interior/07.pal", ".gbapal");
const u16 sVenuePalette29[] = INCGFX_U16("data/venues/KantoTutor/interior/08.pal", ".gbapal");
const u16 sVenuePalette30[] = INCGFX_U16("graphics/custom_buildings/pastel_pack/modules/kanto/rave/exterior/palette-00.pal", ".gbapal");
const u16 sVenuePalette31[] = INCGFX_U16("data/venues/KantoRave/interior/07.pal", ".gbapal");
const u16 sVenuePalette32[] = INCGFX_U16("data/venues/KantoRave/interior/08.pal", ".gbapal");
const u16 sVenuePalette33[] = INCGFX_U16("graphics/custom_buildings/pastel_pack/modules/kanto/bloom/exterior/palette-00.pal", ".gbapal");
const u16 sVenuePalette34[] = INCGFX_U16("data/venues/KantoBloom/interior/07.pal", ".gbapal");
const u16 sVenuePalette35[] = INCGFX_U16("data/venues/KantoBloom/interior/08.pal", ".gbapal");
const u16 sVenuePalette36[] = INCGFX_U16("graphics/custom_buildings/pastel_pack/modules/saffron/glitch/exterior/palette-00.pal", ".gbapal");
static const struct { const struct Tileset *tileset; const u16 *palette; u16 slot; } sVenuePalettes[] = {
 {&gTileset_VenueHoennTutor, sVenuePalette0, 7},
 {&gTileset_VenueHoennTutorRoom, sVenuePalette1, 7},
 {&gTileset_VenueHoennTutorRoom, sVenuePalette2, 11},
 {&gTileset_VenueHoennBakery, sVenuePalette3, 6},
 {&gTileset_VenueHoennBakeryRoom, sVenuePalette4, 7},
 {&gTileset_VenueHoennBakeryRoom, sVenuePalette5, 11},
 {&gTileset_VenueHoennTea, sVenuePalette6, 12},
 {&gTileset_VenueHoennTeaRoom, sVenuePalette7, 7},
 {&gTileset_VenueHoennTeaRoom, sVenuePalette8, 11},
 {&gTileset_VenueHoennGlitch, sVenuePalette9, 12},
 {&gTileset_VenueHoennGlitchRoom, sVenuePalette10, 7},
 {&gTileset_VenueHoennGlitchRoom, sVenuePalette11, 11},
 {&gTileset_VenueHoennBloom, sVenuePalette12, 7},
 {&gTileset_VenueHoennBloomRoom, sVenuePalette13, 7},
 {&gTileset_VenueHoennBloomRoom, sVenuePalette14, 11},
 {&gTileset_VenueHoennRave, sVenuePalette15, 6},
 {&gTileset_VenueHoennRaveRoom, sVenuePalette16, 7},
 {&gTileset_VenueHoennRaveRoom, sVenuePalette17, 11},
 {&gTileset_VenueKantoBakery, sVenuePalette18, 7},
 {&gTileset_VenueKantoBakeryRoom, sVenuePalette19, 7},
 {&gTileset_VenueKantoBakeryRoom, sVenuePalette20, 8},
 {&gTileset_VenueKantoGlitch, sVenuePalette21, 7},
 {&gTileset_VenueKantoGlitchRoom, sVenuePalette22, 7},
 {&gTileset_VenueKantoGlitchRoom, sVenuePalette23, 8},
 {&gTileset_VenueKantoTea, sVenuePalette24, 7},
 {&gTileset_VenueKantoTeaRoom, sVenuePalette25, 7},
 {&gTileset_VenueKantoTeaRoom, sVenuePalette26, 8},
 {&gTileset_VenueKantoTutor, sVenuePalette27, 7},
 {&gTileset_VenueKantoTutorRoom, sVenuePalette28, 7},
 {&gTileset_VenueKantoTutorRoom, sVenuePalette29, 8},
 {&gTileset_VenueKantoRave, sVenuePalette30, 7},
 {&gTileset_VenueKantoRaveRoom, sVenuePalette31, 7},
 {&gTileset_VenueKantoRaveRoom, sVenuePalette32, 8},
 {&gTileset_VenueKantoBloom, sVenuePalette33, 7},
 {&gTileset_VenueKantoBloomRoom, sVenuePalette34, 7},
 {&gTileset_VenueKantoBloomRoom, sVenuePalette35, 8},
 {&gTileset_VenueKantoSaffronSecondary, sVenuePalette36, 7},
};
#endif
void Venues_LoadPaletteOverrides(const struct Tileset *tileset, bool32 skipFaded)
{
#if !IS_FRLG
    u32 i;
    for (i=0; i<ARRAY_COUNT(sVenuePalettes); i++)
        if (sVenuePalettes[i].tileset == tileset)
        {
            if (skipFaded) CpuCopy16(sVenuePalettes[i].palette, &gPlttBufferUnfaded[sVenuePalettes[i].slot * 16], 32);
            else LoadPalette(sVenuePalettes[i].palette, sVenuePalettes[i].slot * 16, 32);
        }
#endif
}
