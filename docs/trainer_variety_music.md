# Trainer variety and battle music

Built on PR #12 commit `12123aa77d3f572e08110bbe195b9ee3b790322e`.

Thirty-two new characters appear once in Hoenn and once in Kanto, for 64 independently saved battles. Existing terrain, actors, rare encounters, cast, bonds, starters and save layouts are retained. These trainers are additional encounters, not recruitable companions.

Walk up and press A to challenge. They never spot the player from a distance. Talking starts a battle without another Yes/No prompt. A victory leaves the trainer available for their post-battle conversation; it does not force another battle. Losing leaves the challenge available. Defeating one regional appearance unlocks a personal reunion greeting at the other; each regional team still has its own defeat flag.

Early teams have two Pokemon, middle teams three, and later teams four. Teams use the first four generations, local levels 8–36, ordinary 12 IVs and level-up moves. Strong early-game moves and balance still require native playtesting. Original trainers have not been replaced.

All six friends gather together on the open floor of the Celadon restaurant: Hugo, Otis, Bastian, Monty, Florian and Orson. They discuss soup, poetry, plants and lunch; paths, exits and the Coin Case man remain available. Fen uses the supplied wheelchair sprite and no footprint track effect.

Every new character has 11 individually written companion responses to their post-battle speech (352 replies). The two appearances share that exact speech and one remembered context per companion, so traveling to the other region does not repeat the same reaction. Existing Normal / Only when asked / Silent controls apply. These extended contexts use the existing mGBA helper; no new helper setup or save format is introduced.

## Music

Ordinary trainer battles draw from an eight-entry shuffle bag: the seven new scores and the original battle theme for the current region. Every entry plays once before reshuffling; adjacent repeats are prevented across bag boundaries. One selection is cached for the entire battle. Selection uses private RAM state, not gameplay RNG, and resets only at the start of a new trainer battle. The shuffle starts fresh after a reset; no new save data is required.

Wild battles, Gym Leaders, rivals, villains, champions, legendary battles, link/recorded battles and facilities keep their assigned music. Town and route music are unchanged.

All seven arrangements use the existing FRLG trainer instrument bank: no external samples. They have a two-bar introduction and a 32-bar loop. The source MIDI and deterministic score builder are included.

| Theme | Mood | BPM |
|---|---|---:|
| Friendly Rivalry | steady | 136 |
| Running on Sparks | brisk | 154 |
| One More Try | wistful | 104 |
| Pocketful of Sunshine | cheerful | 124 |
| Absolutely According to Plan | silly | 112 |
| A Narrow Escape | tense | 120 |
| No Need to Rush | laidback | 108 |

## Encounters

Coordinates below are map tiles, counting from zero. Levels are the team maximum; some opening Pokemon are one level lower.

| Character | Hoenn location, tile and level | Kanto location, tile and level |
|---|---|---|
| Barnaby Bargain | Route104 (32, 63), Lv. 9 | KantoRoute3 (70, 4), Lv. 12 |
| Vesper Vale | Route116 (7, 7), Lv. 13 | KantoRoute24 (7, 5), Lv. 18 |
| Marlo Mirth | SlateportCity (19, 2), Lv. 18 | KantoCeruleanCity (15, 34), Lv. 19 |
| Sir Clatter | Route110 (15, 2), Lv. 19 | KantoRoute6 (3, 9), Lv. 20 |
| Mosswick | PetalburgWoods (34, 35), Lv. 8 | KantoViridianForest (5, 32), Lv. 9 |
| Nyxie | Route113 (90, 8), Lv. 24 | KantoLavenderTown (20, 17), Lv. 27 |
| Sable | Route117 (2, 10), Lv. 22 | KantoRoute9 (37, 2), Lv. 24 |
| Opaline | VerdanturfTown (2, 16), Lv. 21 | KantoRoute25 (6, 4), Lv. 20 |
| Cinder | MauvilleCity (35, 7), Lv. 22 | KantoVermilionCity (36, 20), Lv. 22 |
| Dahlia Noct | Route104 (8, 7), Lv. 11 | KantoRoute8 (66, 13), Lv. 26 |
| Echo | RustboroCity (34, 9), Lv. 13 | KantoCeladonCity (5, 31), Lv. 29 |
| Briar | Route114 (36, 6), Lv. 25 | KantoRoute15 (68, 7), Lv. 32 |
| Fable | Route119 (28, 107), Lv. 30 | KantoRoute12 (15, 79), Lv. 28 |
| Taffy | Route110 (16, 94), Lv. 20 | KantoRoute5 (19, 30), Lv. 20 |
| Roux | LilycoveCity (9, 9), Lv. 36 | KantoRoute16 (44, 13), Lv. 31 |
| Hugo Boulder | Route112 (34, 49), Lv. 23 | KantoCeladonCity_Restaurant (4, 3), Lv. 29 |
| Otis Crumb | SlateportCity (7, 22), Lv. 18 | KantoCeladonCity_Restaurant (6, 3), Lv. 30 |
| Bastian Tide | Route109 (10, 8), Lv. 17 | KantoCeladonCity_Restaurant (8, 3), Lv. 29 |
| Monty Mallow | MauvilleCity (31, 6), Lv. 23 | KantoCeladonCity_Restaurant (4, 5), Lv. 31 |
| Florian Bloom | Route117 (54, 13), Lv. 22 | KantoCeladonCity_Restaurant (6, 5), Lv. 30 |
| Orson Velvet | FallarborTown (2, 12), Lv. 25 | KantoCeladonCity_Restaurant (8, 5), Lv. 32 |
| Kestrel | Route118 (75, 10), Lv. 28 | KantoRoute7 (5, 10), Lv. 28 |
| Juniper | Route115 (18, 77), Lv. 14 | KantoMtMoon_1F (30, 6), Lv. 13 |
| Solace | Route120 (3, 25), Lv. 33 | KantoRoute13 (27, 12), Lv. 29 |
| Idris | FortreeCity (36, 9), Lv. 32 | KantoRoute10 (9, 45), Lv. 25 |
| Fen | RustboroCity (30, 22), Lv. 12 | KantoPewterCity (21, 37), Lv. 11 |
| Taro | VerdanturfTown (15, 16), Lv. 21 | KantoFuchsiaCity (3, 8), Lv. 34 |
| Cosmo | Route111 (15, 133), Lv. 22 | KantoRoute11 (55, 4), Lv. 23 |
| Nettle | LavaridgeTown (15, 17), Lv. 27 | KantoSaffronCity (48, 33), Lv. 34 |
| Miri | DewfordTown (9, 2), Lv. 14 | KantoRoute6 (14, 9), Lv. 20 |
| Zephyr | Route119 (37, 126), Lv. 30 | KantoRoute18 (19, 8), Lv. 32 |
| Elden Glimmer | Route114 (31, 34), Lv. 26 | KantoRoute14 (2, 51), Lv. 31 |

## Validation status

Source validation passes for exact sprite fingerprints, all 64 registrations, unchanged existing map content/geometry, walkable approaches, separate trainer flags, existing Kanto rares, the complete cast/bond contracts, 352 new companion replies and seven reproducible scores. The preview recordings run through native mGBA with the existing instrument bank; they are audio auditions, not proof of the new integrated ROM.

Integrated ROM compilation, compiled artwork/song-table verification, focused test execution, cafe palette coexistence, physical A-button battles and normal-save checks remain required before delivery. No claim of a continuous campaign playthrough is made.

## Rebuilding the content

Run `python dev_scripts/build_variety_music.py`, `python dev_scripts/build_variety_encounters.py`, then `python dev_scripts/build_companion_contexts.py`. The original sprite importer accepts the supplied ZIP and never executes archive code. Run `validate_trainer_variety.py` and all existing project validators before building. After compilation run `verify_trainer_variety_rom.py pokeemerald.gba pokeemerald.map`.

The 674 preexisting trainer entries are retained; new entries append at 674–737. New actor IDs append after the existing templates on each map; named LOCALID_VARIETY constants resolve to those indices and remain below temporary cast/follower IDs. Art/picture IDs append after the existing Zuri entries. Palettes preserve ordered RGB555 colors; text palette fingerprints normalize line endings.
