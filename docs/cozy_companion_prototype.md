# Cozy upperworld: Littleroot prototype

Local branch: `feature/cozy-companion-littleroot`

Based on starter-selection commit `a50394c0c1d0f77bd8a1c07922cb7a8a9265d3af`.
This branch retains that starter implementation and does not contain the Echo World map changes.

## What is implemented in source

- A human companion using Emerald's existing `BOY_1` overworld sprite. This is temporary art, not a final name, gender, or character design.
- Recruit at (10,12) in Littleroot after receiving the running shoes. Say no to leave them there. Existing followers cannot be replaced by recruitment.
- Follows using the expansion's existing NPC follower system. No battle partner, automatic healing, or double wild battles are enabled by this character.
- Talk to the follower for rotating remarks and an option to send them home. After dismissal, leave and re-enter Littleroot to see them at their recruitment spot again.
- Original descriptions remain. With this companion present, ten inspection hooks offer a separate yes/no choice to ask for a remark: four Littleroot signs and six existing furniture categories (picture books, bookshelves, vases, trash cans, shop shelves, blueprints). Furniture hooks also apply outside Littleroot wherever Emerald uses those standard scripts. This is not coverage of every object in the game.
- Two pairs of neighbors: a welcome committee at (10,17)/(11,17) offers a one-time Potion; gardeners at (16,3)/(15,3) exchange one Oran Berry for one Pecha Berry once. Declining, lacking the berry, or having a full bag does not complete the request. The outgoing berry is removed only after the reward succeeds.
- Town terrain, collisions, exits, warps, starter choice, and native opening scripts are unchanged.

## Save and testing limitations

**Use a separate new test save. Do not overwrite an existing starter-selection save.**
Enabling `FNPC_ENABLE_NPC_FOLLOWERS` changes `SaveBlock3` layout. Old-save migration is not implemented or verified. This is a source prototype, not a released ROM.

The follower engine supports stairs, doors, cycling and water movement, but its tutorial warns that vanilla scripted movements are not universally follower-aware. Recruitment is gated until after the opening/running-shoes scenes. Later story scenes still need emulator review; use the dismissal option before testing them. No custom cycling/surfing sprite frames are supplied yet.

Static checks verified NPC collision tiles and approach reachability, door approaches and north exit, script label/macro references, text character encoding and line widths, and byte-for-byte preservation of starter selection and the town's terrain. ROM compilation and emulator tests have **not** been run: GNU make and the ARM compiler are not installed in this environment.

## Runtime acceptance checks still required

1. Build using the repository's documented Emerald toolchain.
2. Start a separate save; finish the normal opening with both player genders and select a starter. Confirm the companion declines recruitment before running shoes.
3. Recruit; walk into Route 101, enter/exit houses, save/reload, and return to Littleroot. Confirm no duplicate companion and no changes to ordinary battles.
4. Inspect signs/furniture with and without the companion; choose yes/no and cancel. Confirm controls return and original descriptions remain available.
5. Dismiss in town and on another map; re-enter Littleroot and recruit again.
6. Try both neighbor scenes repeatedly, with no Oran Berry and a full bag. Confirm gifts/trades occur once and items are never consumed on a failed exchange.
7. Review later scripted story scenes with the follower before expanding the prototype beyond Littleroot.

## Editing the character

Dialogue is in `data/scripts/cozy_companion.inc`; placements are in `data/maps/LittlerootTown/map.json`. Persistent state uses flags 0x20-0x22 and variable 0x404E, previously unused on the starter branch.

An eventual custom human sprite should reuse Emerald's native dimensions, palette limits, transparency and direction/walk animation layout. Replace the temporary graphic only after inspecting the actual sprite sheet in-game.
