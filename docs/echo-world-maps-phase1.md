# Echo World — First-pass GBA maps
Three editable Emerald Expansion maps are added without changing the original Littleroot/Route101 maps.
- EchoLittlerootTown: 20x20 matching town structure, no original NPCs/house warps/story triggers. North links to EchoRoute101.
- EchoRoute101: 20x20 altered terrain with a laboratory exterior copied from compatible Littleroot exterior metatiles at source (3..10,12..16) to destination (11..18,7..11). Lab entrance warp at (15,11), approach tile (15,12). Both side corridors remain open at x=10 and x=19 across y=7..12; rear walkway is y=6, x=10..19, with only blocked cells (10..12,6) cleared. Original Littleroot/Route101 maps are not modified. The traversability was checked by flood-fill on the map's metatile collision bits. South links to EchoLittlerootTown; north intentionally has no connection until Dark Oldale exists.
- EchoAbandonedLab: 13x13 Birch lab interior structural placeholder, entrance return warps (6,12)/(7,12) -> EchoRoute101 entrance warp (16,12). No original Birch scripts/triggers.
## Remaining work for Codex
1. Build from this branch and inspect all three maps in Porymap. Validate the exterior collision, warp doorway, and west-side approach; fix as required.
2. Add temporary debug-only dimension switches with safe coordinates and save/reload tests; avoid modifications to expanded starter selection.
3. Add custom dark palettes and tile artwork. WEATHER_SHADE and abandoned ship music are provisional, NOT the final Neverway-inspired style.
4. Replace existing Birch exterior/interior metatiles with a genuinely abandoned laboratory.
5. Later add the ghost event, Phase Watch, companion and Echo Pokémon. These are NOT implemented in this map-only commit.
All default Emerald overworld assets, starter selection code, and original storyline remain untouched.
