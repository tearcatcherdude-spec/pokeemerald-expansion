# Kanto adventure in Emerald

The Strange Watch connects the existing Emerald adventure to Kanto's campaign:
417 regional maps, eight gyms, the Rocket story, dungeons, the League, and the
included island maps. The source maps and tiles are imported into Emerald rather
than switching to a separate game or save.

Find the watch beside Birch's lab in Littleroot. Use it from Key Items, or
register it to Select, on clear outdoor ground on foot with a healthy Pokemon.
Each region remembers its own return position and healing destination. Safari
sessions, interiors, water and unsafe tiles do not permit a crossing.

Your party, bag, money, Pokedex and PC remain shared. Gym badges and story flags
remain regional. Obedience earned in either region carries over, and both Leagues
use the same Hall of Fame history. The opening recognizes that you already have
an Emerald starter: visit the Viridian shop and bring Oak his parcel instead of
choosing a second starter. Blue's starter variable is separate from yours.

Pip retains the accepted Morph sprite and palette from PR #6. His original saved
dialogue IDs remain unchanged. Kanto adds 148 remembered comments covering towns,
routes, leaders, the Elite Four, objects and new scenes. Scripted NPC conversations
and ordinary NPC message boxes both support optional reactions. An interaction
offers at most one reaction; heard and declined remarks are not offered again.
He stays quiet when there is nothing fresh to add. NPCs and Pip do not acknowledge
or explain the watch or the shared-save mechanism.

Twelve paired scenes add 24 people with connected dialogue and one-time item
rewards across cities, routes, Cinnabar's lab and One Island's Center. Their native
terrain is unchanged. Bag-full responses leave rewards available for a later visit.
Scene-specific Pip remarks become available after the scene has resolved.

Save compatibility preserves the released 180-byte Pip/watch prefix and appends
Kanto progress after it. The released eleven watch-map IDs stay fixed. Existing
Hoenn starters, Living Hoenn scenes, rare encounters, and dialogue memory remain.
Keep a backup of your normal `.sav` and use Continue when changing ROM versions;
an emulator state from another ROM version is not a supported migration path.

Validation tools:

- `python dev_scripts/validate_project_baseline.py`: accepted artwork, starters
  and stable saved dialogue IDs.
- `python dev_scripts/validate_kanto_campaign.py`: all map and warp destinations,
  layouts, script includes and roots, eight gyms, compact hidden-item encoding,
  and the added scene actors' walkable positions.
- `python dev_scripts/verify_pip_rom.py ROM.gba ROM.map`: every compiled Morph
  frame and palette entry matches the supplied artwork.
- `python dev_scripts/verify_kanto_rom.py ROM.gba ROM.map`: all 119 static NPC
  graphics used by the imported maps have compiled registrations.

Native tests cover progress-bank isolation, save offsets, original trainer teams,
trainer defeat flags, regional HM badge order, compact hidden items, cumulative
obedience and Hall of Fame continuity. Current build and emulator results are
recorded in [PR #8](https://github.com/tearcatcherdude-spec/pokeemerald-expansion/pull/8).
Runtime fixtures explicitly arrange positions, party and story prerequisites;
they do not substitute for a continuous complete playthrough. Optional accessory
menus and link play are not covered by the campaign runtime checks.
