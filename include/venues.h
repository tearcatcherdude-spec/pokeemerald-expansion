#ifndef GUARD_VENUES_H
#define GUARD_VENUES_H
struct Tileset;
const struct Tileset *Venue_BaseTileset(const struct Tileset *tileset);
void Venues_MigrateSavedLayout(void);
#endif
