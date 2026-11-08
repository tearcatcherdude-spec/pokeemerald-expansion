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
