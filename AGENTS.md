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

# Companion bonds continuity

PR #10, `feature/companion-bonds`, extends PR #9 commit
abca44ff33711c59df08e0734d41e658263c6128. SaveBlocks 1/2/3 stay unchanged.
Bond v1 appends 416 bytes after the released 34144-byte PC/fusion prefix;
PokemonStorage is 34560 bytes of a 35712-byte allowance. Never move the prefix,
shrink boxes, erase fusion slots, or reuse Hall of Fame/special save sectors.
Normal legacy saves have zero bytes in the appended tail, preserving checksums.
Keep the magic/version and individual bond record offsets stable after release.

The 634 existing Kanto/cast trainer entries stay unchanged. Trial entries
634..673 are new, with separate practice behavior; never replace the early
recruitment teams. Gift consumption requires an explicit preview and confirmation.
Only newly finished observations award EXP; old heard/declined comments never
replay for farming. No companion-switch, save/load or door-loop outing resets.

Build authored bond data with `dev_scripts/build_bonds.py`; cast regeneration
also calls it so it cannot silently erase journal wiring or practice teams.
`data/bonds/events.json` is the runtime placement manifest; the original handoff
JSON remains a proposal snapshot. No existing map geometry/events are rewritten.
Temporary scene actors use local IDs F0..F2 and must be removed on cancel, finish
and map changes without removing original actors or duplicating the follower.
Run `validate_bonds.py` plus all previous source/artwork checks and native normal
save, marker-route, journal, reward-once, branch-choice and loss/retry checks.

# Contextual dialogue continuity

The contextual dialogue branch extends PR #10 commit
3c2db04c936104b9297e0ad22f9c589bf3a51baa. Keep the completed bond system,
artwork, starters and full regional progress. Do not substitute NPC sprite-type,
map observations or personal lore for actual NPC replies. Unknown last messages
must invalidate earlier candidate text; exact-label bindings require source review.
The first 47 new context IDs in data/companion_dialogue/contexts.json are append-only.
Keep original Pip/cast reaction memory, including exact furniture and paired scenes.

CompanionDialogueProgress appends 1020 bytes after offset 34560. PokemonStorage
is 35580/35712; its 11 independent 92-byte banks reserve 736 contexts/voice.
Do not resize that record, clear old banks, evict spent bits or repurpose the
remaining 132 bytes without a new reviewed format. Normal/Ask/Silent is global
and persistent. Muting must not remove a follower or block journal/story choices.

Regenerate with build_companion_contexts.py, run validate_companion_dialogue.py
and the existing validators. coverage.json is a conservative static inventory,
not proof that every actor has dialogue or that every branch ran. Do not call
the initial authored batch full-world completion. Validate the exact ROM with
actual NPC branch changes, unknown messages, deferred prompts, each mode,
independent spent memory, portraits, EXP-on-print and old normal-save migration.

# Full-game dialogue expansion

The user authorized one full-game expansion across both regions on top of PR #11
79ec91c79bd03c426c64f824415befdfe99d351d. Do not restrict the deliverable to early
game or ask for approval at every internal content batch. See
`docs/full_game_companion_dialogue.md` and the complete worklist under
`data/companion_dialogue/full_game`. The first 47 context IDs/wording/expressions
are frozen by released_pilot_contract.json. Unwritten/unknown branches are gaps,
not completed coverage. Source inventory alone does not establish native coverage.

The user selected fully independent permanent memory for every companion and
conversation. Shared memory is rejected. Existing pilot memory must survive.
The user confirmed mGBA on Windows. Target its documented Lua API (0.10+).
Do not resize/reset released banks, discard the backup save, or reuse
PC/fusion/Hall of Fame/special storage. A host-side snapshot protocol is only a
candidate until the actual adapter/ROM and migration tests pass. The current WIP
appends a 56-byte anchor at SaveBlock2 offset 3884, preserving the whole prefix.
Extended observations prepare an immutable host snapshot before being offered;
normal/partial save paths then write the already valid anchor without new IO.
No helper or missing history must suppress only extended observations, preserve
their anchor and keep normal gameplay, original history and normal saving usable.
Dialogue progress v2 keeps the same 1020-byte record and all bank offsets; its
two former reserved bytes count completed one-time legacy-context imports.
Import read-only, per voice, once for each appended context. Do not keep checking
legacy broad categories on every offer: that would silence fresh independent
descriptions. All exact legacy aliases must be bound below context 736.

# Standing desktop delivery preference (2026-11-12)

After each new playable build, automatically download/package and deliver it to
the Windows desktop using tools/build_delivery/deploy.py. Put the new build in
`Emerald Current Build` and move prior recognized build folders intact into
`past emerald builds`. Copy the most recently modified checksum-valid normal
save and its matching entire companion-history folder unless the user explicitly
opts out for that delivery. Never migrate an old emulator state or merge separate
playthroughs. Do not ask again for routine transfers/archiving already authorized
here. Stop if the emulator is running or required history is missing; preserve all
originals. See docs/build_delivery.md for verification, staging and rollback.

# Authorized readability and tutor revision (2026-11-12)

The user explicitly requested clearer custom buildings and NPC sprites. Active
revision v2 is pinned by graphics/readability_v2/revision.json. Every superseded
art file is retained below graphics/readability_v2/originals; old cast/variety
contracts remain frozen and validate the archived originals plus exact revised
hashes. Pip's original Morph walker and all 80 dialogue expressions stay exact.
Do not regenerate the AI sources or overwrite this revision without a new request.

The bakery uses Rustboro House3's full existing footprint; the nightclub uses
Fuchsia House1's existing footprint. Keep their native residents and scripts,
existing outdoor collision and animated doorway cells. Route104 and KantoRoute11
are restored completely. Released private venue map IDs/layout ordering remain
stable; retired saved route overlays migrate without changing any save layout.

Mr. Loophole must offer genuine extra moves, not one four-move fallback for all
species. Catalogue: data/roaming_tutor/lessons.json; compile/check with
dev_scripts/build_roaming_tutor_catalog.py. Rank safe unknown moves by species
type/anatomical technique, level, attack category and missing/type-diverse coverage.
Exclude the species' normal level-up, teachable and egg moves. Keep individual
20-level cooldown, HM protection, Gen-IV move limit and conservative power bands.
