#include "global.h"
#include "fieldmap.h"
#include "tilesets.h"
#include "venues.h"
#include "overworld.h"
#include "load_save.h"
#include "constants/layouts.h"
#include "constants/maps.h"
#include "constants/map_event_ids.h"
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
    if (tileset == &gTileset_VenueKantoRave) return &gTileset_Kanto_FuchsiaCity;
    if (tileset == &gTileset_VenueKantoBloom) return &gTileset_Kanto_CeladonCity;
    if (tileset == &gTileset_VenueKantoSaffronPrimary) return &gTileset_Kanto_General_Frlg;
    if (tileset == &gTileset_VenueKantoSaffronSecondary) return &gTileset_Kanto_SaffronCity;
#endif
    return tileset;
}

#if !IS_FRLG
static void ReloadSavedVenue(void)
{
    CpuFill16(0, gSaveBlock1Ptr->mapView, sizeof(gSaveBlock1Ptr->mapView));
    if (!UseContinueGameWarp())
    {
        gSaveBlock1Ptr->continueGameWarp = gSaveBlock1Ptr->location;
        gSaveBlock1Ptr->continueGameWarp.warpId = WARP_ID_NONE;
        gSaveBlock1Ptr->continueGameWarp.x = gSaveBlock1Ptr->pos.x;
        gSaveBlock1Ptr->continueGameWarp.y = gSaveBlock1Ptr->pos.y;
        SetContinueGameWarpStatus();
    }
}
#endif

void Venues_MigrateSavedLayout(void)
{
#if !IS_FRLG
    // The bakery moved off Route 104; discard only its retired map overlay.
    if (gSaveBlock1Ptr->location.mapGroup == MAP_GROUP(MAP_ROUTE104) && gSaveBlock1Ptr->location.mapNum == MAP_NUM(MAP_ROUTE104) && gSaveBlock1Ptr->mapLayoutId == LAYOUT_VENUE_HOENNBAKERY)
    { gSaveBlock1Ptr->mapLayoutId = LAYOUT_ROUTE104; ReloadSavedVenue(); return; }
    if (gSaveBlock1Ptr->location.mapGroup == MAP_GROUP(MAP_KANTO_ROUTE11) && gSaveBlock1Ptr->location.mapNum == MAP_NUM(MAP_KANTO_ROUTE11) && gSaveBlock1Ptr->mapLayoutId == LAYOUT_VENUE_KANTORAVE)
    { gSaveBlock1Ptr->mapLayoutId = LAYOUT_KANTO_ROUTE11; ReloadSavedVenue(); return; }
    if (gMapHeader.mapLayoutId == LAYOUT_VENUE_HOENNTUTOR && gSaveBlock1Ptr->mapLayoutId == LAYOUT_PETALBURG_CITY)
    {
        gSaveBlock1Ptr->mapLayoutId = LAYOUT_VENUE_HOENNTUTOR;
        ReloadSavedVenue();
        return;
    }
    if (gMapHeader.mapLayoutId == LAYOUT_VENUE_HOENNTUTOR_ROOM && gSaveBlock1Ptr->mapLayoutId == LAYOUT_HOUSE1)
    {
        gSaveBlock1Ptr->mapLayoutId = LAYOUT_VENUE_HOENNTUTOR_ROOM;
        gSaveBlock1Ptr->pos.x = 3; gSaveBlock1Ptr->pos.y = 7;
        ReloadSavedVenue();
        return;
    }
    if (gMapHeader.mapLayoutId == LAYOUT_VENUE_HOENNBAKERY && gSaveBlock1Ptr->mapLayoutId == LAYOUT_RUSTBORO_CITY)
    {
        gSaveBlock1Ptr->mapLayoutId = LAYOUT_VENUE_HOENNBAKERY;
        if (gSaveBlock1Ptr->pos.x >= 24 && gSaveBlock1Ptr->pos.x < 30 && gSaveBlock1Ptr->pos.y >= 42 && gSaveBlock1Ptr->pos.y < 47)
        { gSaveBlock1Ptr->pos.x = 26; gSaveBlock1Ptr->pos.y = 47; }
        ReloadSavedVenue();
        return;
    }
    if (gMapHeader.mapLayoutId == LAYOUT_VENUE_HOENNTEA && gSaveBlock1Ptr->mapLayoutId == LAYOUT_SLATEPORT_CITY)
    {
        gSaveBlock1Ptr->mapLayoutId = LAYOUT_VENUE_HOENNTEA;
        ReloadSavedVenue();
        return;
    }
    if (gMapHeader.mapLayoutId == LAYOUT_VENUE_HOENNTEA_ROOM && gSaveBlock1Ptr->mapLayoutId == LAYOUT_HOUSE2)
    {
        gSaveBlock1Ptr->mapLayoutId = LAYOUT_VENUE_HOENNTEA_ROOM;
        gSaveBlock1Ptr->pos.x = 3; gSaveBlock1Ptr->pos.y = 7;
        ReloadSavedVenue();
        return;
    }
    if (gMapHeader.mapLayoutId == LAYOUT_VENUE_HOENNGLITCH && gSaveBlock1Ptr->mapLayoutId == LAYOUT_MAUVILLE_CITY)
    {
        gSaveBlock1Ptr->mapLayoutId = LAYOUT_VENUE_HOENNGLITCH;
        ReloadSavedVenue();
        return;
    }
    if (gMapHeader.mapLayoutId == LAYOUT_VENUE_HOENNGLITCH_ROOM && gSaveBlock1Ptr->mapLayoutId == LAYOUT_HOUSE1)
    {
        gSaveBlock1Ptr->mapLayoutId = LAYOUT_VENUE_HOENNGLITCH_ROOM;
        gSaveBlock1Ptr->pos.x = 3; gSaveBlock1Ptr->pos.y = 7;
        ReloadSavedVenue();
        return;
    }
    if (gMapHeader.mapLayoutId == LAYOUT_VENUE_HOENNBLOOM && gSaveBlock1Ptr->mapLayoutId == LAYOUT_VERDANTURF_TOWN)
    {
        gSaveBlock1Ptr->mapLayoutId = LAYOUT_VENUE_HOENNBLOOM;
        ReloadSavedVenue();
        return;
    }
    if (gMapHeader.mapLayoutId == LAYOUT_VENUE_HOENNBLOOM_ROOM && gSaveBlock1Ptr->mapLayoutId == LAYOUT_HOUSE1)
    {
        gSaveBlock1Ptr->mapLayoutId = LAYOUT_VENUE_HOENNBLOOM_ROOM;
        gSaveBlock1Ptr->pos.x = 3; gSaveBlock1Ptr->pos.y = 7;
        ReloadSavedVenue();
        return;
    }
    if (gMapHeader.mapLayoutId == LAYOUT_VENUE_HOENNRAVE && gSaveBlock1Ptr->mapLayoutId == LAYOUT_LILYCOVE_CITY)
    {
        gSaveBlock1Ptr->mapLayoutId = LAYOUT_VENUE_HOENNRAVE;
        ReloadSavedVenue();
        return;
    }
    if (gMapHeader.mapLayoutId == LAYOUT_VENUE_HOENNRAVE_ROOM && gSaveBlock1Ptr->mapLayoutId == LAYOUT_HOUSE1)
    {
        gSaveBlock1Ptr->mapLayoutId = LAYOUT_VENUE_HOENNRAVE_ROOM;
        gSaveBlock1Ptr->pos.x = 3; gSaveBlock1Ptr->pos.y = 7;
        ReloadSavedVenue();
        return;
    }
    if (gMapHeader.mapLayoutId == LAYOUT_VENUE_KANTOBAKERY && gSaveBlock1Ptr->mapLayoutId == LAYOUT_KANTO_VIRIDIAN_CITY)
    {
        gSaveBlock1Ptr->mapLayoutId = LAYOUT_VENUE_KANTOBAKERY;
        if (gSaveBlock1Ptr->pos.x >= 35 && gSaveBlock1Ptr->pos.x < 40 && gSaveBlock1Ptr->pos.y >= 21 && gSaveBlock1Ptr->pos.y < 26)
        { gSaveBlock1Ptr->pos.x = 37; gSaveBlock1Ptr->pos.y = 26; }
        ReloadSavedVenue();
        return;
    }
    if (gMapHeader.mapLayoutId == LAYOUT_VENUE_KANTOGLITCH && gSaveBlock1Ptr->mapLayoutId == LAYOUT_KANTO_PEWTER_CITY)
    {
        gSaveBlock1Ptr->mapLayoutId = LAYOUT_VENUE_KANTOGLITCH;
        if (gSaveBlock1Ptr->pos.x >= 7 && gSaveBlock1Ptr->pos.x < 12 && gSaveBlock1Ptr->pos.y >= 22 && gSaveBlock1Ptr->pos.y < 27)
        { gSaveBlock1Ptr->pos.x = 9; gSaveBlock1Ptr->pos.y = 27; }
        ReloadSavedVenue();
        return;
    }
    if (gMapHeader.mapLayoutId == LAYOUT_VENUE_KANTOTEA && gSaveBlock1Ptr->mapLayoutId == LAYOUT_KANTO_VERMILION_CITY)
    {
        gSaveBlock1Ptr->mapLayoutId = LAYOUT_VENUE_KANTOTEA;
        if (gSaveBlock1Ptr->pos.x >= 24 && gSaveBlock1Ptr->pos.x < 29 && gSaveBlock1Ptr->pos.y >= 9 && gSaveBlock1Ptr->pos.y < 14)
        { gSaveBlock1Ptr->pos.x = 26; gSaveBlock1Ptr->pos.y = 14; }
        ReloadSavedVenue();
        return;
    }
    if (gMapHeader.mapLayoutId == LAYOUT_VENUE_KANTOTUTOR && gSaveBlock1Ptr->mapLayoutId == LAYOUT_KANTO_ROUTE4)
    {
        gSaveBlock1Ptr->mapLayoutId = LAYOUT_VENUE_KANTOTUTOR;
        if (gSaveBlock1Ptr->pos.x >= 78 && gSaveBlock1Ptr->pos.x < 83 && gSaveBlock1Ptr->pos.y >= 12 && gSaveBlock1Ptr->pos.y < 17)
        { gSaveBlock1Ptr->pos.x = 80; gSaveBlock1Ptr->pos.y = 17; }
        ReloadSavedVenue();
        return;
    }
    if (gMapHeader.mapLayoutId == LAYOUT_VENUE_KANTORAVE && gSaveBlock1Ptr->mapLayoutId == LAYOUT_KANTO_FUCHSIA_CITY)
    {
        gSaveBlock1Ptr->mapLayoutId = LAYOUT_VENUE_KANTORAVE;
        if (gSaveBlock1Ptr->pos.x >= 12 && gSaveBlock1Ptr->pos.x < 17 && gSaveBlock1Ptr->pos.y >= 27 && gSaveBlock1Ptr->pos.y < 32)
        { gSaveBlock1Ptr->pos.x = 14; gSaveBlock1Ptr->pos.y = 32; }
        ReloadSavedVenue();
        return;
    }
    if (gMapHeader.mapLayoutId == LAYOUT_VENUE_KANTOBLOOM && gSaveBlock1Ptr->mapLayoutId == LAYOUT_KANTO_ROUTE18)
    {
        gSaveBlock1Ptr->mapLayoutId = LAYOUT_VENUE_KANTOBLOOM;
        if (gSaveBlock1Ptr->pos.x >= 10 && gSaveBlock1Ptr->pos.x < 15 && gSaveBlock1Ptr->pos.y >= 2 && gSaveBlock1Ptr->pos.y < 7)
        { gSaveBlock1Ptr->pos.x = 12; gSaveBlock1Ptr->pos.y = 7; }
        ReloadSavedVenue();
        return;
    }
    if (gMapHeader.mapLayoutId == LAYOUT_VENUE_SAFFRON_FACADES && gSaveBlock1Ptr->mapLayoutId == LAYOUT_KANTO_SAFFRON_CITY)
    { gSaveBlock1Ptr->mapLayoutId = LAYOUT_VENUE_SAFFRON_FACADES; ReloadSavedVenue(); return; }
    if (gSaveBlock1Ptr->location.mapGroup == MAP_GROUP(MAP_OLDALE_TOWN) && gSaveBlock1Ptr->location.mapNum == MAP_NUM(MAP_OLDALE_TOWN))
    {
        u32 at = gMapHeader.events->objectEventCount - 1;
        if (gMapHeader.events->objectEvents[at].localId == LOCALID_ROAMING_TUTOR_OLDALETOWN && gSaveBlock1Ptr->objectEventTemplates[at].localId != LOCALID_ROAMING_TUTOR_OLDALETOWN) ReloadSavedVenue();
    }
    if (gSaveBlock1Ptr->location.mapGroup == MAP_GROUP(MAP_ROUTE110) && gSaveBlock1Ptr->location.mapNum == MAP_NUM(MAP_ROUTE110))
    {
        u32 at = gMapHeader.events->objectEventCount - 1;
        if (gMapHeader.events->objectEvents[at].localId == LOCALID_ROAMING_TUTOR_ROUTE110 && gSaveBlock1Ptr->objectEventTemplates[at].localId != LOCALID_ROAMING_TUTOR_ROUTE110) ReloadSavedVenue();
    }
    if (gSaveBlock1Ptr->location.mapGroup == MAP_GROUP(MAP_ROUTE120) && gSaveBlock1Ptr->location.mapNum == MAP_NUM(MAP_ROUTE120))
    {
        u32 at = gMapHeader.events->objectEventCount - 1;
        if (gMapHeader.events->objectEvents[at].localId == LOCALID_ROAMING_TUTOR_ROUTE120 && gSaveBlock1Ptr->objectEventTemplates[at].localId != LOCALID_ROAMING_TUTOR_ROUTE120) ReloadSavedVenue();
    }
    if (gSaveBlock1Ptr->location.mapGroup == MAP_GROUP(MAP_KANTO_ROUTE2) && gSaveBlock1Ptr->location.mapNum == MAP_NUM(MAP_KANTO_ROUTE2))
    {
        u32 at = gMapHeader.events->objectEventCount - 1;
        if (gMapHeader.events->objectEvents[at].localId == LOCALID_ROAMING_TUTOR_KANTOROUTE2 && gSaveBlock1Ptr->objectEventTemplates[at].localId != LOCALID_ROAMING_TUTOR_KANTOROUTE2) ReloadSavedVenue();
    }
    if (gSaveBlock1Ptr->location.mapGroup == MAP_GROUP(MAP_KANTO_ROUTE8) && gSaveBlock1Ptr->location.mapNum == MAP_NUM(MAP_KANTO_ROUTE8))
    {
        u32 at = gMapHeader.events->objectEventCount - 1;
        if (gMapHeader.events->objectEvents[at].localId == LOCALID_ROAMING_TUTOR_KANTOROUTE8 && gSaveBlock1Ptr->objectEventTemplates[at].localId != LOCALID_ROAMING_TUTOR_KANTOROUTE8) ReloadSavedVenue();
    }
    if (gSaveBlock1Ptr->location.mapGroup == MAP_GROUP(MAP_KANTO_ROUTE15) && gSaveBlock1Ptr->location.mapNum == MAP_NUM(MAP_KANTO_ROUTE15))
    {
        u32 at = gMapHeader.events->objectEventCount - 1;
        if (gMapHeader.events->objectEvents[at].localId == LOCALID_ROAMING_TUTOR_KANTOROUTE15 && gSaveBlock1Ptr->objectEventTemplates[at].localId != LOCALID_ROAMING_TUTOR_KANTOROUTE15) ReloadSavedVenue();
    }
    if (gMapHeader.mapLayoutId == LAYOUT_VENUE_HOENNTUTOR || gMapHeader.mapLayoutId == LAYOUT_VENUE_HOENNTUTOR_ROOM) { ReloadSavedVenue(); return; }
    if (gMapHeader.mapLayoutId == LAYOUT_VENUE_HOENNBAKERY || gMapHeader.mapLayoutId == LAYOUT_VENUE_HOENNBAKERY_ROOM) { ReloadSavedVenue(); return; }
    if (gMapHeader.mapLayoutId == LAYOUT_VENUE_HOENNTEA || gMapHeader.mapLayoutId == LAYOUT_VENUE_HOENNTEA_ROOM) { ReloadSavedVenue(); return; }
    if (gMapHeader.mapLayoutId == LAYOUT_VENUE_HOENNGLITCH || gMapHeader.mapLayoutId == LAYOUT_VENUE_HOENNGLITCH_ROOM) { ReloadSavedVenue(); return; }
    if (gMapHeader.mapLayoutId == LAYOUT_VENUE_HOENNBLOOM || gMapHeader.mapLayoutId == LAYOUT_VENUE_HOENNBLOOM_ROOM) { ReloadSavedVenue(); return; }
    if (gMapHeader.mapLayoutId == LAYOUT_VENUE_HOENNRAVE || gMapHeader.mapLayoutId == LAYOUT_VENUE_HOENNRAVE_ROOM) { ReloadSavedVenue(); return; }
    if (gMapHeader.mapLayoutId == LAYOUT_VENUE_KANTOBAKERY_ROOM && gSaveBlock1Ptr->pos.y == 7 && (gSaveBlock1Ptr->pos.x == 3 || gSaveBlock1Ptr->pos.x == 5)) { gSaveBlock1Ptr->pos.x = 4; gSaveBlock1Ptr->pos.y = 6; }
    if (gMapHeader.mapLayoutId == LAYOUT_VENUE_KANTOBAKERY || gMapHeader.mapLayoutId == LAYOUT_VENUE_KANTOBAKERY_ROOM) { ReloadSavedVenue(); return; }
    if (gMapHeader.mapLayoutId == LAYOUT_VENUE_KANTOGLITCH_ROOM && gSaveBlock1Ptr->pos.y == 7 && (gSaveBlock1Ptr->pos.x == 3 || gSaveBlock1Ptr->pos.x == 5)) { gSaveBlock1Ptr->pos.x = 4; gSaveBlock1Ptr->pos.y = 6; }
    if (gMapHeader.mapLayoutId == LAYOUT_VENUE_KANTOGLITCH || gMapHeader.mapLayoutId == LAYOUT_VENUE_KANTOGLITCH_ROOM) { ReloadSavedVenue(); return; }
    if (gMapHeader.mapLayoutId == LAYOUT_VENUE_KANTOTEA_ROOM && gSaveBlock1Ptr->pos.y == 7 && (gSaveBlock1Ptr->pos.x == 3 || gSaveBlock1Ptr->pos.x == 5)) { gSaveBlock1Ptr->pos.x = 4; gSaveBlock1Ptr->pos.y = 6; }
    if (gMapHeader.mapLayoutId == LAYOUT_VENUE_KANTOTEA || gMapHeader.mapLayoutId == LAYOUT_VENUE_KANTOTEA_ROOM) { ReloadSavedVenue(); return; }
    if (gMapHeader.mapLayoutId == LAYOUT_VENUE_KANTOTUTOR_ROOM && gSaveBlock1Ptr->pos.y == 7 && (gSaveBlock1Ptr->pos.x == 3 || gSaveBlock1Ptr->pos.x == 5)) { gSaveBlock1Ptr->pos.x = 4; gSaveBlock1Ptr->pos.y = 6; }
    if (gMapHeader.mapLayoutId == LAYOUT_VENUE_KANTOTUTOR || gMapHeader.mapLayoutId == LAYOUT_VENUE_KANTOTUTOR_ROOM) { ReloadSavedVenue(); return; }
    if (gMapHeader.mapLayoutId == LAYOUT_VENUE_KANTORAVE_ROOM && gSaveBlock1Ptr->pos.y == 7 && (gSaveBlock1Ptr->pos.x == 3 || gSaveBlock1Ptr->pos.x == 5)) { gSaveBlock1Ptr->pos.x = 4; gSaveBlock1Ptr->pos.y = 6; }
    if (gMapHeader.mapLayoutId == LAYOUT_VENUE_KANTORAVE || gMapHeader.mapLayoutId == LAYOUT_VENUE_KANTORAVE_ROOM) { ReloadSavedVenue(); return; }
    if (gMapHeader.mapLayoutId == LAYOUT_VENUE_KANTOBLOOM_ROOM && gSaveBlock1Ptr->pos.y == 7 && (gSaveBlock1Ptr->pos.x == 3 || gSaveBlock1Ptr->pos.x == 5)) { gSaveBlock1Ptr->pos.x = 4; gSaveBlock1Ptr->pos.y = 6; }
    if (gMapHeader.mapLayoutId == LAYOUT_VENUE_KANTOBLOOM || gMapHeader.mapLayoutId == LAYOUT_VENUE_KANTOBLOOM_ROOM) { ReloadSavedVenue(); return; }
    if (gMapHeader.mapLayoutId == LAYOUT_VENUE_SAFFRON_FACADES) ReloadSavedVenue();
#endif
}
