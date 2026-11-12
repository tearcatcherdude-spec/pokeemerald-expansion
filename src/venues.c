#include "global.h"
#include "fieldmap.h"
#include "tilesets.h"
#include "venues.h"
const struct Tileset *Venue_BaseTileset(const struct Tileset *tileset)
{
#if !IS_FRLG
    if (tileset == &gTileset_VenueHoennTutor) return &gTileset_Petalburg;
    if (tileset == &gTileset_VenueHoennBakery) return &gTileset_Rustboro;
    if (tileset == &gTileset_VenueHoennTea) return &gTileset_Slateport;
    if (tileset == &gTileset_VenueHoennGlitch) return &gTileset_Mauville;
    if (tileset == &gTileset_VenueHoennBloom) return &gTileset_Mauville;
    if (tileset == &gTileset_VenueHoennRave) return &gTileset_Lilycove;
    if (tileset == &gTileset_VenueKantoBakery) return &gTileset_Kanto_ViridianCity;
    if (tileset == &gTileset_VenueKantoGlitch) return &gTileset_Kanto_PewterCity;
    if (tileset == &gTileset_VenueKantoTea) return &gTileset_Kanto_VermilionCity;
    if (tileset == &gTileset_VenueKantoTutor) return &gTileset_Kanto_CeruleanCity;
    if (tileset == &gTileset_VenueKantoRave) return &gTileset_Kanto_VermilionCity;
    if (tileset == &gTileset_VenueKantoBloom) return &gTileset_Kanto_CeladonCity;
#endif
    return tileset;
}
