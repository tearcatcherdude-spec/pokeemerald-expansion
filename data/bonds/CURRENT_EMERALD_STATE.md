# Current Emerald project context

Read-only GitHub/context refresh on November 8, 2026. No game code or GitHub state was changed.

## Current work

- Repository: `tearcatcherdude-spec/pokeemerald-expansion`.
- Latest development: PR #9, `feature/recruitable-cast`, commit `abca44ff33711c59df08e0734d41e658263c6128`.
- The local `work/full-kanto` checkout is clean at this same commit. The older `work/cozy-emerald` checkout is stale and must not be used as the starting point for new project work.
- PR #9 builds on the tested full-Kanto PR #8, commit `ba1f1f5f2173fc450fba6c0aae76c6c3ecac6ef3`.
- The work remains in stacked, open draft PRs rather than being merged into master. Accepted work can therefore exist outside master.

## Already integrated

- Expanded starters, Living Hoenn scenes, all sixteen rare encounters, and remembered/quiet Pip dialogue remain included.
- Pip now uses Morph's accepted blue-haired/red-glasses walking sprite and exact palette from PR #6, incorporated into the watch/full-Kanto chain. Do not restore the older Pip artwork.
- The Strange Watch connects Hoenn to Kanto, with shared party, bag, money, PC and Pokédex, but separate regional story, badge, trainer and healing state.
- Full Kanto imports 417 maps with the eight gyms, Rocket locations, League and included island maps. PR #8 additionally has Living Kanto scenes and remembered Pip comments.
- The watch is a silent mystery: characters must not acknowledge it or explain world switching/shared mechanics. Controls may be documented outside the game.

## Recruitable cast and portraits

- Ten friends: Silas, Emi, Nico, Kade, Ashe, Vera, Lume, Mochi, Riven and Zuri.
- Each has a request and an optional four-Pokémon Gen 1–4 battle before friendship/recruitment. One human follows at a time; Pip stays selectable through Change company.
- The ten supplied walking sheets and eighty portrait expressions are integrated. Cast dialogue has 64×64 portraits and assigned expression changes. This is implemented for the new cast; do not assume Pip has an expression portrait just because he remains selectable.
- Actual source review contains 940 distinct authored reactions and sixty ordered lore passages. The older PR description's 910 count is stale.
- Per-character memory, declined offers, friendship, readiness after losing, and ordered lore persist without a rotating fallback.

## Validation status at refresh

- PR #8 commit ba1f1f5: CI run 42533662284 completed successfully; 5,468 tests passed with zero unexpected failures. Its PR documents extensive native emulator fixtures, not a continuous full-story playthrough.
- Latest PR #9 commit abca44f: CI run 42545934228 was still running. Baseline, Kanto topology, cast source checks and documentation had passed; latest Emerald compilation/artwork checks and full tests were not yet complete.
- Local recruitable-cast validation records 93 native checks for an earlier candidate, commit 599c3ef7cf6031dfa387fab1bdce34777162d807. Do not attribute those results to the newer abca44f binary without checking its final artifact.
- Recheck live GitHub status before reporting or changing the newest build.

## Save/artwork continuity

- Read current `work/full-kanto/AGENTS.md` before edits.
- Preserve the released 1004-byte prefix. The cast appends 604 bytes for a 1608-byte SaveBlock3, close to the 1624-byte limit. Do not clear or reorder existing banks to add features.
- Existing Pip dialogue slots, map-group prefixes, regional flags and dynamic graphic IDs are guarded. Append IDs; retire dialogue entries with NULL tombstones instead of recycling them.
- Required checks include baseline, Kanto and cast source validators plus actual compiled artwork verification and normal-save migration tests.

References: PR #8 https://github.com/tearcatcherdude-spec/pokeemerald-expansion/pull/8; PR #9 https://github.com/tearcatcherdude-spec/pokeemerald-expansion/pull/9.
