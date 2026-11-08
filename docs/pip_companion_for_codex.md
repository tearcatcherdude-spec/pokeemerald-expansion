# Pip: Echo World companion sprite

Pip's supplied assets, registered as a distinct Emerald NPC on the companion feature branch.
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

## Registration reference
1. `gObjectEventPic_Pip` is registered in `src/data/object_events/object_event_graphics.h` using the standard human sprite conversion.
2. `sPicTable_Pip` uses `overworld_ascending_frames(gObjectEventPic_Pip, 2, 4)`.
3. `gObjectEventGraphicsInfo_Pip` has width 16, height 32, size 256, `sAnimTable_Standard` and the standard 16x32 OAM/subsprite layout.
4. `OBJ_EVENT_PAL_TAG_PIP` is distinct from the shared NPC palettes and registered in the palette table.
5. `OBJ_EVENT_GFX_PIP` is connected to the existing follower system, with its own identity and scene safeguards.

Build/runtime verification remains necessary: all four cardinal directions, movement, warp transitions, save/reload, travel modes and shadows. This coding branch covers normal Emerald; the separate Echo maps are preserved without being merged here.

**Integration:** `OBJ_EVENT_GFX_PIP` uses these exact nine frames and its own palette tag. The original shared Boy sprite/palette is unchanged. Pip's travelling dialogue covers all Hoenn towns and routes, major landmarks, badges and postgame. Standard NPC conversations offer an optional reaction, preserving the original script's result, message pointer and expanded text. Scripted movement temporarily hides Pip and removes his collision with actors; he regroups when controls return.

The supplied walking sheet is reused during travel. Dedicated bicycle, surfing and diving artwork was not supplied and has not been invented. The follower engine provides its existing movement and surf-blob behavior.

**Validation:** Source integration is complete; compilation and emulator checks are pending for this revision. Keep existing saves backed up. The previous companion ROM's test results do not certify this new asset/worldwide-dialogue revision.
