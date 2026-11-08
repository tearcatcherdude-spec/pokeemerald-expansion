# Living Hoenn and a quieter Pip

Pip now remembers spoken lines and declined offers in the save. Wording is deduplicated across locations. When nothing fresh fits the context, he says nothing and standard interactions do not offer an empty reaction. His menu separates Talk, Head home and Keep walking. New badges, places, travel modes and authored scenes provide fresh material.

The first worldwide pass adds **21 paired scenes (42 people)** and **16 rare Pokémon** across **29 maps**. The previous Littleroot neighbors remain. Existing terrain, original NPC positions, story triggers, doors, exits and starter code are preserved. New pairs have before/after dialogue, with four exchanges and five one-time gifts; reward flags are only set after an item is successfully given.

## Rare encounters

These are actual overworld species sprites. Their descriptions infer motives from behavior rather than giving every Pokémon human speech. Ask to join opens a catchable wild battle. Declining leaves them alone. Catching sets a permanent hide flag; fainting or fleeing leaves them resting until a later map visit. No healthy party means no battle. All have **31 in every IV**, a species-appropriate legal EV spread totaling **510**, and an area-specific fixed level. They are outside Hoenn-origin species and are special hand-placed encounters, not additions to the random encounter tables.

| Location | Pokémon | Level |
|---|---|---|
| OldaleTown | Sentret | 5 |
| Route103 | Shinx | 7 |
| RustboroCity | Eevee | 10 |
| Route116 | Mareep | 12 |
| DewfordTown | Riolu | 15 |
| VerdanturfTown | Togepi | 17 |
| Route117 | Wooper | 18 |
| LavaridgeTown | Houndour | 23 |
| Route114 | Gible | 25 |
| Route118 | Munchlax | 26 |
| Route119 | Dratini | 29 |
| Route120 | Croagunk | 32 |
| LilycoveCity | Porygon | 33 |
| MossdeepCity | Elekid | 35 |
| Route123 | Larvitar | 38 |
| VictoryRoad_1F | Deino | 42 |

## Scene locations

OldaleTown, PetalburgCity, RustboroCity, DewfordTown, SlateportCity, MauvilleCity, VerdanturfTown, FallarborTown, LavaridgeTown, FortreeCity, LilycoveCity, MossdeepCity, SootopolisCity, PacifidlogTown_PokemonCenter_1F, EverGrandeCity, Route102, Route104, Route110, Route111, Route113, Route119.

## Save and editing constraints

The original four-byte SaveBlock3 prefix and follower offset remain unchanged. Dialogue memory appends at byte 28; the companion block is now 160 bytes. Older unused tail bytes initialize the memory schema on first use. This is a deliberate save extension, not certification of arbitrary legacy saves. Keep backups and use a separate test save until save migration has been checked in the emulator.

`src/data/pip_memory_catalogue.h` has **248 stable line IDs**. Append new entries; never reorder or reuse IDs. Heard and offered bits are separate so declining a joke does not count as hearing it and does not cause repeated prompts. Changing maps, resetting scene state and saving must not clear these bits.

## Validation

Build, automated tests and actual emulator checks are required for this revision. In particular verify silence after exhausting a location, a fresh comment after a new milestone, declined offers, persistent memory after Continue, pair progression/reward safety, rare refusal and catch/retry paths, retained IV/EVs after capture, and sprite/object-slot availability. Do not use the earlier Pip build results to certify this change.
