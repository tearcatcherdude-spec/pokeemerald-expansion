# Project continuity

Build each change on the latest accepted project state. Inspect relevant sibling
PRs before building: accepted work may still be in an unmerged draft. Do not reset
to an older branch or restore an older asset unless the user requests a revert.

Pip uses Morph's blue-haired, red-glasses sprite and matching palette from PR #6.
The accepted asset fingerprints and append-only dialogue IDs are recorded in
`data/project_baseline.json`. Preserve this artwork when adding regions or features.

The watch is a silent mystery. NPCs and Pip must not acknowledge the device,
explain world switching, or explain shared party/bag/PC mechanics in dialogue.
Keep item feedback brief and neutral. Controls can be documented outside the game.

Preserve expanded starter selection, Living Hoenn scenes, rare encounters, Pip's
remembered dialogue/silence and the working watch/save behavior. Retire dialogue
IDs with NULL tombstones; append new IDs instead of reusing or reordering them.

Before delivery run `python dev_scripts/validate_project_baseline.py`, relevant
build/tests, and verify Pip's actual compiled sprite and palette in the ROM.

# Full Kanto continuity

The current integrated work is PR #8, branch `feature/full-kanto-adventure`,
built on the accepted starter/Living Hoenn work and the PR #6 artwork via PR #7.
Continue from that integrated branch when extending this game, not the earlier
11-map watch trial. All 408 existing Pip memory slots and 116 map-group prefixes
are now guarded in `data/project_baseline.json`; append, never reorder or reuse.

SaveBlock3 keeps the released 180-byte Pip/watch prefix. Kanto version 1 occupies
an additional 824 bytes (total 1004, including ARM struct padding). Its flags, variables and per-world healing
locations have fixed offsets tested in `test/save.c`. Extend saves by appending
and migrating new fields. Do not increment the Kanto version and clear the whole
bank: that would erase the user's regional story, trainer and scene progress.
Keep badges/HM gates regional while preserving earned obedience and shared Hall
of Fame history/access. Keep watch item ID 874 and the eleven group-75 map IDs.

# Recruitable cast continuity

PR #9, `feature/recruitable-cast`, extends the complete PR #8 Kanto build. Preserve
all ten supplied walking sprites and all eighty expressions; their canonical
asset hashes live in `data/cast/asset_manifest.json`. Text palettes normalize line
endings for hashing; their ordered colour entries are exact. Portrait source
binaries are tracked `_expressions.bin` / `_palette.bin`, not generated targets.

The released 1004-byte prefix stays unchanged. Cast version 1 appends 604 bytes
(total 1608, maximum 1624). Never reset the regional or cast banks to add content.
Friendship, readiness after a lost battle, per-character canonical comment memory,
and ordered lore all persist. Keep original Pip memory and all source-context IDs.
Reserve the old dynamic graphic IDs at `OBJ_EVENT_GFX_PIP + 2 .. + 17`; appended
cast graphics start after them. Keep the native trainer entries 0..623 unchanged.
Run the cast source validator and actual compiled artwork verifier in addition to
the original baseline and Kanto checks. Native emulator checks must use the exact
packaged binary and normal-save migration; do not claim a continuous playthrough
from arranged test positions or parties.
