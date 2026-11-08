# Pip: a travelling companion across Emerald

Pip uses the supplied human sprite from `assets/pip-companion-20261107` as a distinct NPC graphic and palette. Existing NPC sprites and palettes are unchanged. His source assets and frame ordering are described in [Pip's asset notes](pip_companion_for_codex.md).

## Travelling together

Recruit Pip beside Birch's lab in Littleroot at (10,12), after receiving the running shoes. He follows across Hoenn, including map connections, buildings and the follower engine's cycling/water travel. There is no route, town or badge cutoff. He does not become a battle partner, heal the party automatically or cause double wild battles. Talking to him offers a location/progress remark and the option to return home. After dismissal, leave and re-enter Littleroot to recruit him again.

Pip has location dialogue for all Hoenn towns and routes, major landmarks, badge progress and the postgame, with general fallback dialogue for other areas. Standard NPC conversations, signs and furniture offer an optional reaction after their original text. Common furniture has object-specific comments; other signs use location context. NPC reactions vary by role and a rotating general pool. Special story scripts with custom dialogue remain intact; this is not a unique authored response to every line in Emerald.

Standard reaction hooks preserve the original script result, last talked-to ID, message pointer and expanded text. Pip's own remarks use the default message box to avoid recursively triggering reactions.

## Scripted scenes and artwork

When a scripted actor starts moving, Pip steps aside, becomes invisible and collision-exempt, and waits until the script/movement finishes and control returns. He regroups on the next player step. This avoids forcing existing actor paths to account for a second person. Later story scenes and special activities still need representative emulator checks; this mechanism does not replace a full-game playthrough.

Only Pip's nine walking cels were supplied. They are reused for travel at the follower engine's normal speeds; dedicated bicycle, surfing and diving artwork is not included. Do not substitute another human's riding sprites for Pip. His palette is registered separately rather than overwriting the shared Boy palette.

## Saves and starter work

Use a separate new test save and keep existing saves backed up. The companion build retains the starter branch's SaveBlock1/2 layouts and original SaveBlock3 prefix, appending follower storage after that prefix. Save-layout guards remain enabled. Pip's identity/script pointer is refreshed on map load for an existing placeholder follower, but arbitrary old saves and saves from earlier unreleased layouts are not certified.

The expanded-starter selection, battle setup, native terrain, warps and exits are preserved. The asset branch was not merged wholesale because it predates the working starter fixes; only Pip's three asset/note files were imported.

## State and editing

- `FLAG_HIDE_COZY_COMPANION` (0x20): original home object hidden while travelling.
- `FLAG_COZY_WELCOME_GIFT` (0x21), `FLAG_COZY_BERRY_TRADE` (0x22): original neighbor rewards.
- `FLAG_MET_PIP` (0x23): Pip has joined before.
- `VAR_PIP_COMMENT_COUNTER` (0x4083): rotating comments; previously unused.
- `src/pip.c`, `src/data/pip_dialogue.h`: identity, reactions, location/progress selection and scene safeguards.
- `data/scripts/cozy_companion.inc`: recruitment, companion conversation, reactions and neighbor scenes.

## Validation

The prior placeholder revision passed 5,440 automated tests and focused emulator checks. This Pip/worldwide revision adds tests for distinct sprite/palette registration, follower ownership, all-town/route dialogue coverage, badge/postgame selection, preserved NPC conversation state and scripted-actor collision safety. Its build and runtime verification are pending until the current CI run completes; do not treat the prior ROM's results as certification of this revision.
