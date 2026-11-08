# Pip: Echo World companion sprite

Game-ready **asset sources**, not yet registered in the ROM.
This branch adds the files in their intended locations without modifying game code or the player's ongoing Echo World/expanded starter work.

- `graphics/object_events/pics/people/pip.png` — native **144 × 32**, indexed-color PNG, 9 cels of **16 × 32**, 16-color palette.
- `graphics/object_events/palettes/pip.pal` — 16-entry JASC-PAL; index 0 is transparency key.

## Frame ordering — matches Emerald's `sAnimTable_Standard`
| Frame | Action |
| --- | --- |
| 0 | Face south |
| 1 | Face north |
| 2 | Face west (east is horizontally mirrored) |
| 3 | Walk south A |
| 4 | Walk south B |
| 5 | Walk north A |
| 6 | Walk north B |
| 7 | Walk west A |
| 8 | Walk west B |

The existing engine table handles right/east by horizontal mirroring. Foot/anchor positions and visual animation should be reviewed in mGBA after registration.

## Codex integration tasks
1. On a separate coding branch (merge these assets first or cherry-pick the asset commit), register `gObjectEventPic_Pip` using the pattern of `gObjectEventPic_Boy2` in `src/data/object_events/object_event_graphics.h`.
2. Register the frame table with `overworld_ascending_frames(gObjectEventPic_Pip, 2, 4)` in `src/data/object_events/object_event_pic_tables.h`.
3. Create a **new** `ObjectEventGraphicsInfo` with `width=16, height=32, size=256`, `sAnimTable_Standard`, compatible OAM, and a new graphics ID. Consult `src/data/object_events/object_event_graphics_info.h`, pointers, and object event constants.
4. Register a palette appropriately; do not overwrite an existing NPC palette or assume unallocated palette tags.
5. Use the existing follower system for Pip. Test all four cardinal directions, follower movement, warp transitions, normal and Echo maps, save/reload, and shadows.
6. Build/test on the repo's current working branch. Do not alter starter selection or existing Echo World map work without an explicit integration need.

**Status:** Frames and palette are prepared at GBA-compatible dimensions and indexed depth. Sprite is **not yet registered, compiled, or playtested** in Emerald Expansion.
