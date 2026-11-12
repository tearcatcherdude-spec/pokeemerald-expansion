# Kanto rare encounters

Adds sixteen optional native Pokemon actors to the latest integrated Emerald build.
The released Hoenn encounters, existing actors, terrain, stories, saves and companion assets remain intact.

| Pokemon | Location | Level |
|---|---|---|
| Beldum | Viridian City | 6 |
| Shinx | Route22 | 5 |
| Riolu | Route4 | 12 |
| Mareep | Route24 | 14 |
| Buneary | Route5 | 15 |
| Espeon | Route8 | 20 |
| Umbreon | Route9 | 18 |
| Larvitar | Route10 | 17 |
| Heracross | Route11 | 17 |
| Dratini | Route12 | 27 |
| Misdreavus | LavenderTown | 22 |
| Absol | Route15 | 30 |
| Feebas | Route21_North | 32 |
| Rotom | PowerPlant | 33 |
| Gible | Route18 | 29 |
| Bagon | CinnabarIsland | 34 |

Each encounter has its own introduction, invitation, decline, rest and capture outcome.
Accepting starts a normal catchable wild battle. Capture alone permanently removes the actor.
Defeat or escape leaves it available after a map change; declining changes no capture flag.
Feebas occupies accessible water on Route 21 North and requires Surf.
All six IVs are 31. EVs total 510, with no stat above 252 and a species-suitable spread.
The normal engine supplies nature, ability, moves and catch rate; Beldum retains its difficult catch rate.

Capture flags use unused Kanto bits A8F0-A8FF; no save layout or version changes are made.
The sixteen original Hoenn rare-definition indices stay unchanged; Kanto appends indices 16-31.
The new capture scenes each have eleven distinct companion reactions; existing dialogue mode/history rules apply.
Their optional companion reactions need the existing mGBA helper; the encounters and battles do not.

The save-load companion script fix remains included. The unrelated-escort regression fixture was corrected
to use an actual non-companion identity rather than Pip's own flag.
Run build_kanto_rares.py, validate_kanto_rares.py and the existing project validators.
Native validation must check actual sprites, battles, catching, retry/removal, stats and normal-save reload.
