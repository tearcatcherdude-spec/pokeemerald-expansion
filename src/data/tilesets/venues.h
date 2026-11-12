#if !IS_FRLG
const u32 gTileset_VenueHoennTutorTiles[] = INCBIN_U32("data/venues/HoennTutor/exterior/tiles.bin.smol");
const u16 gTileset_VenueHoennTutorPalettes[][16] = {
 INCGFX_U16("data/tilesets/secondary/petalburg/palettes/00.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/petalburg/palettes/01.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/petalburg/palettes/02.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/petalburg/palettes/03.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/petalburg/palettes/04.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/petalburg/palettes/05.pal", ".gbapal"),
 INCGFX_U16("graphics/custom_buildings/pastel_pack/modules/hoenn/tutor/exterior/palette-00.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/petalburg/palettes/07.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/petalburg/palettes/08.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/petalburg/palettes/09.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/petalburg/palettes/10.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/petalburg/palettes/11.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/petalburg/palettes/12.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/petalburg/palettes/13.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/petalburg/palettes/14.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/petalburg/palettes/15.pal", ".gbapal"),
};
const u16 gTileset_VenueHoennTutorMetatiles[] = INCBIN_U16("data/venues/HoennTutor/exterior/metatiles.bin");
const u16 gTileset_VenueHoennTutorAttributes[] = INCBIN_U16("data/venues/HoennTutor/exterior/attributes.bin");
const struct Tileset gTileset_VenueHoennTutor = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueHoennTutorTiles, .palettes=gTileset_VenueHoennTutorPalettes, .metatiles=gTileset_VenueHoennTutorMetatiles, .metatileAttributes=gTileset_VenueHoennTutorAttributes, .callback=InitTilesetAnim_Petalburg};
const u32 gTileset_VenueHoennTutorRoomTiles[] = INCBIN_U32("data/venues/HoennTutor/interior/tiles.bin.smol");
const u16 gTileset_VenueHoennTutorRoomPalettes[][16] = {
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/00.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/01.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/02.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/03.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/04.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/05.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/06.pal", ".gbapal"),
 INCGFX_U16("data/venues/HoennTutor/interior/07.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/08.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/09.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/10.pal", ".gbapal"),
 INCGFX_U16("data/venues/HoennTutor/interior/11.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/12.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/13.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/14.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/15.pal", ".gbapal"),
};
const u16 gTileset_VenueHoennTutorRoomMetatiles[] = INCBIN_U16("data/venues/HoennTutor/interior/metatiles.bin");
const u16 gTileset_VenueHoennTutorRoomAttributes[] = INCBIN_U16("data/venues/HoennTutor/interior/attributes.bin");
const struct Tileset gTileset_VenueHoennTutorRoom = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueHoennTutorRoomTiles, .palettes=gTileset_VenueHoennTutorRoomPalettes, .metatiles=gTileset_VenueHoennTutorRoomMetatiles, .metatileAttributes=gTileset_VenueHoennTutorRoomAttributes, .callback=NULL};
const u32 gTileset_VenueHoennBakeryTiles[] = INCBIN_U32("data/venues/HoennBakery/exterior/tiles.bin.smol");
const u16 gTileset_VenueHoennBakeryPalettes[][16] = {
 INCGFX_U16("data/tilesets/secondary/rustboro/palettes/00.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/rustboro/palettes/01.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/rustboro/palettes/02.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/rustboro/palettes/03.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/rustboro/palettes/04.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/rustboro/palettes/05.pal", ".gbapal"),
 INCGFX_U16("graphics/custom_buildings/pastel_pack/modules/hoenn/bakery/exterior/palette-00.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/rustboro/palettes/07.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/rustboro/palettes/08.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/rustboro/palettes/09.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/rustboro/palettes/10.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/rustboro/palettes/11.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/rustboro/palettes/12.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/rustboro/palettes/13.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/rustboro/palettes/14.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/rustboro/palettes/15.pal", ".gbapal"),
};
const u16 gTileset_VenueHoennBakeryMetatiles[] = INCBIN_U16("data/venues/HoennBakery/exterior/metatiles.bin");
const u16 gTileset_VenueHoennBakeryAttributes[] = INCBIN_U16("data/venues/HoennBakery/exterior/attributes.bin");
const struct Tileset gTileset_VenueHoennBakery = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueHoennBakeryTiles, .palettes=gTileset_VenueHoennBakeryPalettes, .metatiles=gTileset_VenueHoennBakeryMetatiles, .metatileAttributes=gTileset_VenueHoennBakeryAttributes, .callback=InitTilesetAnim_Rustboro};
const u32 gTileset_VenueHoennBakeryRoomTiles[] = INCBIN_U32("data/venues/HoennBakery/interior/tiles.bin.smol");
const u16 gTileset_VenueHoennBakeryRoomPalettes[][16] = {
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/00.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/01.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/02.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/03.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/04.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/05.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/06.pal", ".gbapal"),
 INCGFX_U16("data/venues/HoennBakery/interior/07.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/08.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/09.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/10.pal", ".gbapal"),
 INCGFX_U16("data/venues/HoennBakery/interior/11.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/12.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/13.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/14.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/15.pal", ".gbapal"),
};
const u16 gTileset_VenueHoennBakeryRoomMetatiles[] = INCBIN_U16("data/venues/HoennBakery/interior/metatiles.bin");
const u16 gTileset_VenueHoennBakeryRoomAttributes[] = INCBIN_U16("data/venues/HoennBakery/interior/attributes.bin");
const struct Tileset gTileset_VenueHoennBakeryRoom = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueHoennBakeryRoomTiles, .palettes=gTileset_VenueHoennBakeryRoomPalettes, .metatiles=gTileset_VenueHoennBakeryRoomMetatiles, .metatileAttributes=gTileset_VenueHoennBakeryRoomAttributes, .callback=NULL};
const u32 gTileset_VenueHoennTeaTiles[] = INCBIN_U32("data/venues/HoennTea/exterior/tiles.bin.smol");
const u16 gTileset_VenueHoennTeaPalettes[][16] = {
 INCGFX_U16("data/tilesets/secondary/slateport/palettes/00.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/slateport/palettes/01.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/slateport/palettes/02.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/slateport/palettes/03.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/slateport/palettes/04.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/slateport/palettes/05.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/slateport/palettes/06.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/slateport/palettes/07.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/slateport/palettes/08.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/slateport/palettes/09.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/slateport/palettes/10.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/slateport/palettes/11.pal", ".gbapal"),
 INCGFX_U16("graphics/custom_buildings/pastel_pack/modules/hoenn/tea/exterior/palette-00.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/slateport/palettes/13.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/slateport/palettes/14.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/slateport/palettes/15.pal", ".gbapal"),
};
const u16 gTileset_VenueHoennTeaMetatiles[] = INCBIN_U16("data/venues/HoennTea/exterior/metatiles.bin");
const u16 gTileset_VenueHoennTeaAttributes[] = INCBIN_U16("data/venues/HoennTea/exterior/attributes.bin");
const struct Tileset gTileset_VenueHoennTea = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueHoennTeaTiles, .palettes=gTileset_VenueHoennTeaPalettes, .metatiles=gTileset_VenueHoennTeaMetatiles, .metatileAttributes=gTileset_VenueHoennTeaAttributes, .callback=InitTilesetAnim_Slateport};
const u32 gTileset_VenueHoennTeaRoomTiles[] = INCBIN_U32("data/venues/HoennTea/interior/tiles.bin.smol");
const u16 gTileset_VenueHoennTeaRoomPalettes[][16] = {
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/00.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/01.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/02.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/03.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/04.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/05.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/06.pal", ".gbapal"),
 INCGFX_U16("data/venues/HoennTea/interior/07.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/08.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/09.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/10.pal", ".gbapal"),
 INCGFX_U16("data/venues/HoennTea/interior/11.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/12.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/13.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/14.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/15.pal", ".gbapal"),
};
const u16 gTileset_VenueHoennTeaRoomMetatiles[] = INCBIN_U16("data/venues/HoennTea/interior/metatiles.bin");
const u16 gTileset_VenueHoennTeaRoomAttributes[] = INCBIN_U16("data/venues/HoennTea/interior/attributes.bin");
const struct Tileset gTileset_VenueHoennTeaRoom = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueHoennTeaRoomTiles, .palettes=gTileset_VenueHoennTeaRoomPalettes, .metatiles=gTileset_VenueHoennTeaRoomMetatiles, .metatileAttributes=gTileset_VenueHoennTeaRoomAttributes, .callback=NULL};
const u32 gTileset_VenueHoennGlitchTiles[] = INCBIN_U32("data/venues/HoennGlitch/exterior/tiles.bin.smol");
const u16 gTileset_VenueHoennGlitchPalettes[][16] = {
 INCGFX_U16("data/tilesets/secondary/mauville/palettes/00.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/mauville/palettes/01.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/mauville/palettes/02.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/mauville/palettes/03.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/mauville/palettes/04.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/mauville/palettes/05.pal", ".gbapal"),
 INCGFX_U16("graphics/custom_buildings/pastel_pack/modules/hoenn/glitch/exterior/palette-00.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/mauville/palettes/07.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/mauville/palettes/08.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/mauville/palettes/09.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/mauville/palettes/10.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/mauville/palettes/11.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/mauville/palettes/12.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/mauville/palettes/13.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/mauville/palettes/14.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/mauville/palettes/15.pal", ".gbapal"),
};
const u16 gTileset_VenueHoennGlitchMetatiles[] = INCBIN_U16("data/venues/HoennGlitch/exterior/metatiles.bin");
const u16 gTileset_VenueHoennGlitchAttributes[] = INCBIN_U16("data/venues/HoennGlitch/exterior/attributes.bin");
const struct Tileset gTileset_VenueHoennGlitch = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueHoennGlitchTiles, .palettes=gTileset_VenueHoennGlitchPalettes, .metatiles=gTileset_VenueHoennGlitchMetatiles, .metatileAttributes=gTileset_VenueHoennGlitchAttributes, .callback=InitTilesetAnim_Mauville};
const u32 gTileset_VenueHoennGlitchRoomTiles[] = INCBIN_U32("data/venues/HoennGlitch/interior/tiles.bin.smol");
const u16 gTileset_VenueHoennGlitchRoomPalettes[][16] = {
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/00.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/01.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/02.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/03.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/04.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/05.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/06.pal", ".gbapal"),
 INCGFX_U16("data/venues/HoennGlitch/interior/07.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/08.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/09.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/10.pal", ".gbapal"),
 INCGFX_U16("data/venues/HoennGlitch/interior/11.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/12.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/13.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/14.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/15.pal", ".gbapal"),
};
const u16 gTileset_VenueHoennGlitchRoomMetatiles[] = INCBIN_U16("data/venues/HoennGlitch/interior/metatiles.bin");
const u16 gTileset_VenueHoennGlitchRoomAttributes[] = INCBIN_U16("data/venues/HoennGlitch/interior/attributes.bin");
const struct Tileset gTileset_VenueHoennGlitchRoom = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueHoennGlitchRoomTiles, .palettes=gTileset_VenueHoennGlitchRoomPalettes, .metatiles=gTileset_VenueHoennGlitchRoomMetatiles, .metatileAttributes=gTileset_VenueHoennGlitchRoomAttributes, .callback=NULL};
const u32 gTileset_VenueHoennBloomTiles[] = INCBIN_U32("data/venues/HoennBloom/exterior/tiles.bin.smol");
const u16 gTileset_VenueHoennBloomPalettes[][16] = {
 INCGFX_U16("data/tilesets/secondary/mauville/palettes/00.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/mauville/palettes/01.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/mauville/palettes/02.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/mauville/palettes/03.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/mauville/palettes/04.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/mauville/palettes/05.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/mauville/palettes/06.pal", ".gbapal"),
 INCGFX_U16("graphics/custom_buildings/pastel_pack/modules/hoenn/bloom/exterior/palette-00.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/mauville/palettes/08.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/mauville/palettes/09.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/mauville/palettes/10.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/mauville/palettes/11.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/mauville/palettes/12.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/mauville/palettes/13.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/mauville/palettes/14.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/mauville/palettes/15.pal", ".gbapal"),
};
const u16 gTileset_VenueHoennBloomMetatiles[] = INCBIN_U16("data/venues/HoennBloom/exterior/metatiles.bin");
const u16 gTileset_VenueHoennBloomAttributes[] = INCBIN_U16("data/venues/HoennBloom/exterior/attributes.bin");
const struct Tileset gTileset_VenueHoennBloom = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueHoennBloomTiles, .palettes=gTileset_VenueHoennBloomPalettes, .metatiles=gTileset_VenueHoennBloomMetatiles, .metatileAttributes=gTileset_VenueHoennBloomAttributes, .callback=InitTilesetAnim_Mauville};
const u32 gTileset_VenueHoennBloomRoomTiles[] = INCBIN_U32("data/venues/HoennBloom/interior/tiles.bin.smol");
const u16 gTileset_VenueHoennBloomRoomPalettes[][16] = {
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/00.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/01.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/02.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/03.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/04.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/05.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/06.pal", ".gbapal"),
 INCGFX_U16("data/venues/HoennBloom/interior/07.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/08.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/09.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/10.pal", ".gbapal"),
 INCGFX_U16("data/venues/HoennBloom/interior/11.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/12.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/13.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/14.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/15.pal", ".gbapal"),
};
const u16 gTileset_VenueHoennBloomRoomMetatiles[] = INCBIN_U16("data/venues/HoennBloom/interior/metatiles.bin");
const u16 gTileset_VenueHoennBloomRoomAttributes[] = INCBIN_U16("data/venues/HoennBloom/interior/attributes.bin");
const struct Tileset gTileset_VenueHoennBloomRoom = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueHoennBloomRoomTiles, .palettes=gTileset_VenueHoennBloomRoomPalettes, .metatiles=gTileset_VenueHoennBloomRoomMetatiles, .metatileAttributes=gTileset_VenueHoennBloomRoomAttributes, .callback=NULL};
const u32 gTileset_VenueHoennRaveTiles[] = INCBIN_U32("data/venues/HoennRave/exterior/tiles.bin.smol");
const u16 gTileset_VenueHoennRavePalettes[][16] = {
 INCGFX_U16("data/tilesets/secondary/lilycove/palettes/00.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/lilycove/palettes/01.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/lilycove/palettes/02.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/lilycove/palettes/03.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/lilycove/palettes/04.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/lilycove/palettes/05.pal", ".gbapal"),
 INCGFX_U16("graphics/custom_buildings/pastel_pack/modules/hoenn/rave/exterior/palette-00.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/lilycove/palettes/07.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/lilycove/palettes/08.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/lilycove/palettes/09.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/lilycove/palettes/10.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/lilycove/palettes/11.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/lilycove/palettes/12.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/lilycove/palettes/13.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/lilycove/palettes/14.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/lilycove/palettes/15.pal", ".gbapal"),
};
const u16 gTileset_VenueHoennRaveMetatiles[] = INCBIN_U16("data/venues/HoennRave/exterior/metatiles.bin");
const u16 gTileset_VenueHoennRaveAttributes[] = INCBIN_U16("data/venues/HoennRave/exterior/attributes.bin");
const struct Tileset gTileset_VenueHoennRave = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueHoennRaveTiles, .palettes=gTileset_VenueHoennRavePalettes, .metatiles=gTileset_VenueHoennRaveMetatiles, .metatileAttributes=gTileset_VenueHoennRaveAttributes, .callback=InitTilesetAnim_Lilycove};
const u32 gTileset_VenueHoennRaveRoomTiles[] = INCBIN_U32("data/venues/HoennRave/interior/tiles.bin.smol");
const u16 gTileset_VenueHoennRaveRoomPalettes[][16] = {
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/00.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/01.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/02.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/03.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/04.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/05.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/06.pal", ".gbapal"),
 INCGFX_U16("data/venues/HoennRave/interior/07.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/08.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/09.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/10.pal", ".gbapal"),
 INCGFX_U16("data/venues/HoennRave/interior/11.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/12.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/13.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/14.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building/palettes/15.pal", ".gbapal"),
};
const u16 gTileset_VenueHoennRaveRoomMetatiles[] = INCBIN_U16("data/venues/HoennRave/interior/metatiles.bin");
const u16 gTileset_VenueHoennRaveRoomAttributes[] = INCBIN_U16("data/venues/HoennRave/interior/attributes.bin");
const struct Tileset gTileset_VenueHoennRaveRoom = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueHoennRaveRoomTiles, .palettes=gTileset_VenueHoennRaveRoomPalettes, .metatiles=gTileset_VenueHoennRaveRoomMetatiles, .metatileAttributes=gTileset_VenueHoennRaveRoomAttributes, .callback=NULL};
const u32 gTileset_VenueKantoBakeryTiles[] = INCBIN_U32("data/venues/KantoBakery/exterior/tiles.bin.smol");
const u16 gTileset_VenueKantoBakeryPalettes[][16] = {
 INCGFX_U16("data/tilesets/secondary/viridian_city_frlg/palettes/00.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/viridian_city_frlg/palettes/01.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/viridian_city_frlg/palettes/02.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/viridian_city_frlg/palettes/03.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/viridian_city_frlg/palettes/04.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/viridian_city_frlg/palettes/05.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/viridian_city_frlg/palettes/06.pal", ".gbapal"),
 INCGFX_U16("graphics/custom_buildings/pastel_pack/modules/kanto/bakery/exterior/palette-00.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/viridian_city_frlg/palettes/08.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/viridian_city_frlg/palettes/09.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/viridian_city_frlg/palettes/10.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/viridian_city_frlg/palettes/11.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/viridian_city_frlg/palettes/12.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/viridian_city_frlg/palettes/13.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/viridian_city_frlg/palettes/14.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/viridian_city_frlg/palettes/15.pal", ".gbapal"),
};
const u16 gTileset_VenueKantoBakeryMetatiles[] = INCBIN_U16("data/venues/KantoBakery/exterior/metatiles.bin");
const u16 gTileset_VenueKantoBakeryAttributes[] = INCBIN_U16("data/venues/KantoBakery/exterior/attributes.bin");
const struct Tileset gTileset_VenueKantoBakery = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueKantoBakeryTiles, .palettes=gTileset_VenueKantoBakeryPalettes, .metatiles=gTileset_VenueKantoBakeryMetatiles, .metatileAttributes=gTileset_VenueKantoBakeryAttributes, .callback=NULL};
const u32 gTileset_VenueKantoBakeryRoomTiles[] = INCBIN_U32("data/venues/KantoBakery/interior/tiles.bin.smol");
const u16 gTileset_VenueKantoBakeryRoomPalettes[][16] = {
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/00.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/01.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/02.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/03.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/04.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/05.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/06.pal", ".gbapal"),
 INCGFX_U16("data/venues/KantoBakery/interior/07.pal", ".gbapal"),
 INCGFX_U16("data/venues/KantoBakery/interior/08.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/09.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/10.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/11.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/12.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/13.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/14.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/15.pal", ".gbapal"),
};
const u16 gTileset_VenueKantoBakeryRoomMetatiles[] = INCBIN_U16("data/venues/KantoBakery/interior/metatiles.bin");
const u16 gTileset_VenueKantoBakeryRoomAttributes[] = INCBIN_U16("data/venues/KantoBakery/interior/attributes.bin");
const struct Tileset gTileset_VenueKantoBakeryRoom = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueKantoBakeryRoomTiles, .palettes=gTileset_VenueKantoBakeryRoomPalettes, .metatiles=gTileset_VenueKantoBakeryRoomMetatiles, .metatileAttributes=gTileset_VenueKantoBakeryRoomAttributes, .callback=NULL};
const u32 gTileset_VenueKantoGlitchTiles[] = INCBIN_U32("data/venues/KantoGlitch/exterior/tiles.bin.smol");
const u16 gTileset_VenueKantoGlitchPalettes[][16] = {
 INCGFX_U16("data/tilesets/secondary/pewter_city_frlg/palettes/00.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/pewter_city_frlg/palettes/01.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/pewter_city_frlg/palettes/02.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/pewter_city_frlg/palettes/03.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/pewter_city_frlg/palettes/04.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/pewter_city_frlg/palettes/05.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/pewter_city_frlg/palettes/06.pal", ".gbapal"),
 INCGFX_U16("graphics/custom_buildings/pastel_pack/modules/kanto/glitch/exterior/palette-00.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/pewter_city_frlg/palettes/08.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/pewter_city_frlg/palettes/09.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/pewter_city_frlg/palettes/10.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/pewter_city_frlg/palettes/11.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/pewter_city_frlg/palettes/12.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/pewter_city_frlg/palettes/13.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/pewter_city_frlg/palettes/14.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/pewter_city_frlg/palettes/15.pal", ".gbapal"),
};
const u16 gTileset_VenueKantoGlitchMetatiles[] = INCBIN_U16("data/venues/KantoGlitch/exterior/metatiles.bin");
const u16 gTileset_VenueKantoGlitchAttributes[] = INCBIN_U16("data/venues/KantoGlitch/exterior/attributes.bin");
const struct Tileset gTileset_VenueKantoGlitch = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueKantoGlitchTiles, .palettes=gTileset_VenueKantoGlitchPalettes, .metatiles=gTileset_VenueKantoGlitchMetatiles, .metatileAttributes=gTileset_VenueKantoGlitchAttributes, .callback=NULL};
const u32 gTileset_VenueKantoGlitchRoomTiles[] = INCBIN_U32("data/venues/KantoGlitch/interior/tiles.bin.smol");
const u16 gTileset_VenueKantoGlitchRoomPalettes[][16] = {
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/00.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/01.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/02.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/03.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/04.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/05.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/06.pal", ".gbapal"),
 INCGFX_U16("data/venues/KantoGlitch/interior/07.pal", ".gbapal"),
 INCGFX_U16("data/venues/KantoGlitch/interior/08.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/09.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/10.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/11.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/12.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/13.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/14.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/15.pal", ".gbapal"),
};
const u16 gTileset_VenueKantoGlitchRoomMetatiles[] = INCBIN_U16("data/venues/KantoGlitch/interior/metatiles.bin");
const u16 gTileset_VenueKantoGlitchRoomAttributes[] = INCBIN_U16("data/venues/KantoGlitch/interior/attributes.bin");
const struct Tileset gTileset_VenueKantoGlitchRoom = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueKantoGlitchRoomTiles, .palettes=gTileset_VenueKantoGlitchRoomPalettes, .metatiles=gTileset_VenueKantoGlitchRoomMetatiles, .metatileAttributes=gTileset_VenueKantoGlitchRoomAttributes, .callback=NULL};
const u32 gTileset_VenueKantoTeaTiles[] = INCBIN_U32("data/venues/KantoTea/exterior/tiles.bin.smol");
const u16 gTileset_VenueKantoTeaPalettes[][16] = {
 INCGFX_U16("data/tilesets/secondary/vermilion_city_frlg/palettes/00.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/vermilion_city_frlg/palettes/01.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/vermilion_city_frlg/palettes/02.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/vermilion_city_frlg/palettes/03.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/vermilion_city_frlg/palettes/04.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/vermilion_city_frlg/palettes/05.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/vermilion_city_frlg/palettes/06.pal", ".gbapal"),
 INCGFX_U16("graphics/custom_buildings/pastel_pack/modules/kanto/tea/exterior/palette-00.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/vermilion_city_frlg/palettes/08.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/vermilion_city_frlg/palettes/09.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/vermilion_city_frlg/palettes/10.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/vermilion_city_frlg/palettes/11.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/vermilion_city_frlg/palettes/12.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/vermilion_city_frlg/palettes/13.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/vermilion_city_frlg/palettes/14.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/vermilion_city_frlg/palettes/15.pal", ".gbapal"),
};
const u16 gTileset_VenueKantoTeaMetatiles[] = INCBIN_U16("data/venues/KantoTea/exterior/metatiles.bin");
const u16 gTileset_VenueKantoTeaAttributes[] = INCBIN_U16("data/venues/KantoTea/exterior/attributes.bin");
const struct Tileset gTileset_VenueKantoTea = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueKantoTeaTiles, .palettes=gTileset_VenueKantoTeaPalettes, .metatiles=gTileset_VenueKantoTeaMetatiles, .metatileAttributes=gTileset_VenueKantoTeaAttributes, .callback=NULL};
const u32 gTileset_VenueKantoTeaRoomTiles[] = INCBIN_U32("data/venues/KantoTea/interior/tiles.bin.smol");
const u16 gTileset_VenueKantoTeaRoomPalettes[][16] = {
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/00.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/01.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/02.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/03.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/04.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/05.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/06.pal", ".gbapal"),
 INCGFX_U16("data/venues/KantoTea/interior/07.pal", ".gbapal"),
 INCGFX_U16("data/venues/KantoTea/interior/08.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/09.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/10.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/11.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/12.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/13.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/14.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/15.pal", ".gbapal"),
};
const u16 gTileset_VenueKantoTeaRoomMetatiles[] = INCBIN_U16("data/venues/KantoTea/interior/metatiles.bin");
const u16 gTileset_VenueKantoTeaRoomAttributes[] = INCBIN_U16("data/venues/KantoTea/interior/attributes.bin");
const struct Tileset gTileset_VenueKantoTeaRoom = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueKantoTeaRoomTiles, .palettes=gTileset_VenueKantoTeaRoomPalettes, .metatiles=gTileset_VenueKantoTeaRoomMetatiles, .metatileAttributes=gTileset_VenueKantoTeaRoomAttributes, .callback=NULL};
const u32 gTileset_VenueKantoTutorTiles[] = INCBIN_U32("data/venues/KantoTutor/exterior/tiles.bin.smol");
const u16 gTileset_VenueKantoTutorPalettes[][16] = {
 INCGFX_U16("data/tilesets/secondary/cerulean_city_frlg/palettes/00.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/cerulean_city_frlg/palettes/01.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/cerulean_city_frlg/palettes/02.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/cerulean_city_frlg/palettes/03.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/cerulean_city_frlg/palettes/04.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/cerulean_city_frlg/palettes/05.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/cerulean_city_frlg/palettes/06.pal", ".gbapal"),
 INCGFX_U16("graphics/custom_buildings/pastel_pack/modules/kanto/tutor/exterior/palette-00.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/cerulean_city_frlg/palettes/08.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/cerulean_city_frlg/palettes/09.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/cerulean_city_frlg/palettes/10.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/cerulean_city_frlg/palettes/11.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/cerulean_city_frlg/palettes/12.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/cerulean_city_frlg/palettes/13.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/cerulean_city_frlg/palettes/14.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/cerulean_city_frlg/palettes/15.pal", ".gbapal"),
};
const u16 gTileset_VenueKantoTutorMetatiles[] = INCBIN_U16("data/venues/KantoTutor/exterior/metatiles.bin");
const u16 gTileset_VenueKantoTutorAttributes[] = INCBIN_U16("data/venues/KantoTutor/exterior/attributes.bin");
const struct Tileset gTileset_VenueKantoTutor = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueKantoTutorTiles, .palettes=gTileset_VenueKantoTutorPalettes, .metatiles=gTileset_VenueKantoTutorMetatiles, .metatileAttributes=gTileset_VenueKantoTutorAttributes, .callback=NULL};
const u32 gTileset_VenueKantoTutorRoomTiles[] = INCBIN_U32("data/venues/KantoTutor/interior/tiles.bin.smol");
const u16 gTileset_VenueKantoTutorRoomPalettes[][16] = {
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/00.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/01.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/02.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/03.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/04.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/05.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/06.pal", ".gbapal"),
 INCGFX_U16("data/venues/KantoTutor/interior/07.pal", ".gbapal"),
 INCGFX_U16("data/venues/KantoTutor/interior/08.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/09.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/10.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/11.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/12.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/13.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/14.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/15.pal", ".gbapal"),
};
const u16 gTileset_VenueKantoTutorRoomMetatiles[] = INCBIN_U16("data/venues/KantoTutor/interior/metatiles.bin");
const u16 gTileset_VenueKantoTutorRoomAttributes[] = INCBIN_U16("data/venues/KantoTutor/interior/attributes.bin");
const struct Tileset gTileset_VenueKantoTutorRoom = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueKantoTutorRoomTiles, .palettes=gTileset_VenueKantoTutorRoomPalettes, .metatiles=gTileset_VenueKantoTutorRoomMetatiles, .metatileAttributes=gTileset_VenueKantoTutorRoomAttributes, .callback=NULL};
const u32 gTileset_VenueKantoRaveTiles[] = INCBIN_U32("data/venues/KantoRave/exterior/tiles.bin.smol");
const u16 gTileset_VenueKantoRavePalettes[][16] = {
 INCGFX_U16("data/tilesets/secondary/vermilion_city_frlg/palettes/00.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/vermilion_city_frlg/palettes/01.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/vermilion_city_frlg/palettes/02.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/vermilion_city_frlg/palettes/03.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/vermilion_city_frlg/palettes/04.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/vermilion_city_frlg/palettes/05.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/vermilion_city_frlg/palettes/06.pal", ".gbapal"),
 INCGFX_U16("graphics/custom_buildings/pastel_pack/modules/kanto/rave/exterior/palette-00.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/vermilion_city_frlg/palettes/08.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/vermilion_city_frlg/palettes/09.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/vermilion_city_frlg/palettes/10.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/vermilion_city_frlg/palettes/11.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/vermilion_city_frlg/palettes/12.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/vermilion_city_frlg/palettes/13.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/vermilion_city_frlg/palettes/14.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/vermilion_city_frlg/palettes/15.pal", ".gbapal"),
};
const u16 gTileset_VenueKantoRaveMetatiles[] = INCBIN_U16("data/venues/KantoRave/exterior/metatiles.bin");
const u16 gTileset_VenueKantoRaveAttributes[] = INCBIN_U16("data/venues/KantoRave/exterior/attributes.bin");
const struct Tileset gTileset_VenueKantoRave = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueKantoRaveTiles, .palettes=gTileset_VenueKantoRavePalettes, .metatiles=gTileset_VenueKantoRaveMetatiles, .metatileAttributes=gTileset_VenueKantoRaveAttributes, .callback=NULL};
const u32 gTileset_VenueKantoRaveRoomTiles[] = INCBIN_U32("data/venues/KantoRave/interior/tiles.bin.smol");
const u16 gTileset_VenueKantoRaveRoomPalettes[][16] = {
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/00.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/01.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/02.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/03.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/04.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/05.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/06.pal", ".gbapal"),
 INCGFX_U16("data/venues/KantoRave/interior/07.pal", ".gbapal"),
 INCGFX_U16("data/venues/KantoRave/interior/08.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/09.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/10.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/11.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/12.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/13.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/14.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/15.pal", ".gbapal"),
};
const u16 gTileset_VenueKantoRaveRoomMetatiles[] = INCBIN_U16("data/venues/KantoRave/interior/metatiles.bin");
const u16 gTileset_VenueKantoRaveRoomAttributes[] = INCBIN_U16("data/venues/KantoRave/interior/attributes.bin");
const struct Tileset gTileset_VenueKantoRaveRoom = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueKantoRaveRoomTiles, .palettes=gTileset_VenueKantoRaveRoomPalettes, .metatiles=gTileset_VenueKantoRaveRoomMetatiles, .metatileAttributes=gTileset_VenueKantoRaveRoomAttributes, .callback=NULL};
const u32 gTileset_VenueKantoBloomTiles[] = INCBIN_U32("data/venues/KantoBloom/exterior/tiles.bin.smol");
const u16 gTileset_VenueKantoBloomPalettes[][16] = {
 INCGFX_U16("data/tilesets/secondary/celadon_city_frlg/palettes/00.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/celadon_city_frlg/palettes/01.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/celadon_city_frlg/palettes/02.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/celadon_city_frlg/palettes/03.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/celadon_city_frlg/palettes/04.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/celadon_city_frlg/palettes/05.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/celadon_city_frlg/palettes/06.pal", ".gbapal"),
 INCGFX_U16("graphics/custom_buildings/pastel_pack/modules/kanto/bloom/exterior/palette-00.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/celadon_city_frlg/palettes/08.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/celadon_city_frlg/palettes/09.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/celadon_city_frlg/palettes/10.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/celadon_city_frlg/palettes/11.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/celadon_city_frlg/palettes/12.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/celadon_city_frlg/palettes/13.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/celadon_city_frlg/palettes/14.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/celadon_city_frlg/palettes/15.pal", ".gbapal"),
};
const u16 gTileset_VenueKantoBloomMetatiles[] = INCBIN_U16("data/venues/KantoBloom/exterior/metatiles.bin");
const u16 gTileset_VenueKantoBloomAttributes[] = INCBIN_U16("data/venues/KantoBloom/exterior/attributes.bin");
const struct Tileset gTileset_VenueKantoBloom = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueKantoBloomTiles, .palettes=gTileset_VenueKantoBloomPalettes, .metatiles=gTileset_VenueKantoBloomMetatiles, .metatileAttributes=gTileset_VenueKantoBloomAttributes, .callback=InitTilesetAnim_CeladonCity};
const u32 gTileset_VenueKantoBloomRoomTiles[] = INCBIN_U32("data/venues/KantoBloom/interior/tiles.bin.smol");
const u16 gTileset_VenueKantoBloomRoomPalettes[][16] = {
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/00.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/01.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/02.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/03.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/04.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/05.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/06.pal", ".gbapal"),
 INCGFX_U16("data/venues/KantoBloom/interior/07.pal", ".gbapal"),
 INCGFX_U16("data/venues/KantoBloom/interior/08.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/09.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/10.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/11.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/12.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/13.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/14.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/generic_building_1_frlg/palettes/15.pal", ".gbapal"),
};
const u16 gTileset_VenueKantoBloomRoomMetatiles[] = INCBIN_U16("data/venues/KantoBloom/interior/metatiles.bin");
const u16 gTileset_VenueKantoBloomRoomAttributes[] = INCBIN_U16("data/venues/KantoBloom/interior/attributes.bin");
const struct Tileset gTileset_VenueKantoBloomRoom = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueKantoBloomRoomTiles, .palettes=gTileset_VenueKantoBloomRoomPalettes, .metatiles=gTileset_VenueKantoBloomRoomMetatiles, .metatileAttributes=gTileset_VenueKantoBloomRoomAttributes, .callback=NULL};
const u32 gTileset_VenueKantoSaffronPrimaryTiles[] = INCBIN_U32("data/venues/SaffronFacades/primary/tiles.bin.smol");
const struct Tileset gTileset_VenueKantoSaffronPrimary = {.isCompressed=TRUE, .isSecondary=FALSE, .tiles=gTileset_VenueKantoSaffronPrimaryTiles, .palettes=gTilesetPalettes_Kanto_General_Frlg, .metatiles=gMetatiles_Kanto_General_Frlg, .metatileAttributes=gMetatileAttributes_Kanto_General_Frlg, .callback=InitTilesetAnim_General_Frlg};
const u32 gTileset_VenueKantoSaffronSecondaryTiles[] = INCBIN_U32("data/venues/SaffronFacades/secondary/tiles.bin.smol");
const u16 gTileset_VenueKantoSaffronSecondaryPalettes[][16] = {
 INCGFX_U16("data/tilesets/secondary/saffron_city_frlg/palettes/00.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/saffron_city_frlg/palettes/01.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/saffron_city_frlg/palettes/02.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/saffron_city_frlg/palettes/03.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/saffron_city_frlg/palettes/04.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/saffron_city_frlg/palettes/05.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/saffron_city_frlg/palettes/06.pal", ".gbapal"),
 INCGFX_U16("graphics/custom_buildings/pastel_pack/modules/saffron/glitch/exterior/palette-00.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/saffron_city_frlg/palettes/08.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/saffron_city_frlg/palettes/09.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/saffron_city_frlg/palettes/10.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/saffron_city_frlg/palettes/11.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/saffron_city_frlg/palettes/12.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/saffron_city_frlg/palettes/13.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/saffron_city_frlg/palettes/14.pal", ".gbapal"),
 INCGFX_U16("data/tilesets/secondary/saffron_city_frlg/palettes/15.pal", ".gbapal"),
};
const u16 gTileset_VenueKantoSaffronSecondaryMetatiles[] = INCBIN_U16("data/venues/SaffronFacades/secondary/metatiles.bin");
const u16 gTileset_VenueKantoSaffronSecondaryAttributes[] = INCBIN_U16("data/venues/SaffronFacades/secondary/attributes.bin");
const struct Tileset gTileset_VenueKantoSaffronSecondary = {.isCompressed=TRUE, .isSecondary=TRUE, .tiles=gTileset_VenueKantoSaffronSecondaryTiles, .palettes=gTileset_VenueKantoSaffronSecondaryPalettes, .metatiles=gTileset_VenueKantoSaffronSecondaryMetatiles, .metatileAttributes=gTileset_VenueKantoSaffronSecondaryAttributes, .callback=NULL};
#endif
