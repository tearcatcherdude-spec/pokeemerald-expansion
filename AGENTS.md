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
an additional 820 bytes (total 1000). Its flags, variables and per-world healing
locations have fixed offsets tested in `test/save.c`. Extend saves by appending
and migrating new fields. Do not increment the Kanto version and clear the whole
bank: that would erase the user's regional story, trainer and scene progress.
Keep badges/HM gates regional while preserving earned obedience and shared Hall
of Fame history/access. Keep watch item ID 874 and the eleven group-75 map IDs.
