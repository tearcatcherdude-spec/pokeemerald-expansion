# Pastel buildings and transformed furniture

Six themed buildings with Hoenn and Kanto footprints, each with an exterior and a furnished interior (24 modules), plus two Saffron-specific mid-rise facades (26 modules total). This is an asset and integration-source pack; no live map or game script is replaced.

- Rainbow Crumb Bakery: strawberry, mint and cream; pastry display, mixer and oven.
- Illegal Move Tutor's House: patched purple/moss workshop; scroll cabinet and improvised training equipment.
- Prism Relay Studio: restrained cyan/lavender glitch panels; servers, consoles and relay machines.
- Pulse Nightclub: dark purple, cyan and pink; speakers, DJ console and light-mixing equipment.
- Bloom & Books: sage/lavender book and flower shop; wrapping and arranging stations.
- Cloudcup Tea House: peach/sky-blue tea shop; tea caddies, sweets and brewing equipment.

The original exterior silhouette and entrance cell are fixed. Roofs, walls and windows are redesigned within the outline. Furniture uses exact masks extracted from native Emerald furniture, painted into different objects and placed in a new room arrangement. This makes a table-shaped mixer or oven, rather than requiring it to remain a table.

## Preview and files

`previews/hoenn-lineup.png`, `previews/kanto-lineup.png` and `previews/saffron-midrise-lineup.png` show the final compiled-palette art at integer scale. These are rendered from tile references and palette banks, not high-resolution source illustrations.

Each `modules/<region>/<theme>/<exterior|interior>/` contains:

- `preview.png`: native-resolution composite with the native ground / exit pixels.
- `art.png`: indexed PNG; exterior has the exact native transparent silhouette. The PNG can contain both custom and retained native colours; it is not a single GBA 16-colour tile bank.
- `tiles.png`, `tiles.4bpp`: indexed 8x8 tile atlas and GBA packed tile bytes. The atlas displays bank 0 for inspection; the metatile references select the actual palette per tile.
- `palette-00.pal` (and interior `palette-01.pal`), `palette.gbapal`: 16-entry JASC palettes and RGB555 data. Entry 0 is transparent in upper tiles. Exteriors use one custom bank; interiors two. Retained native doors/exits use their existing native banks.
- `metatiles.local.bin`: eight little-endian u16 tile references per 16x16 metatile, lower four then upper four.
- `custom-reference-mask.bin`: bits 0..7 mark tile IDs that require relocation.
- `custom-palette-mask.bin`: independent bits mark local palette-bank numbers that require relocation. A copied native tile can still use its native palette.
- `map.local.bin`: local metatile IDs with collision/elevation bits; `map.source.bin` is the unchanged original rectangle.
- `metatile_attributes.bin`: Emerald u16 / FRLG-layout u32 attributes, never interchangeable.
- `editable_source.json`, `module.json`: full unpacked indices, palettes, metatiles, masks, source geometry and integration state.
- Interiors additionally include seven transparent furniture sprites in `furniture/`, with exact original silhouette masks.

`templates/` records the native silhouettes, doors, original maps/events, new room collision grid, furniture placements and native furniture masks. `prompts.json` records the built-in imagegen prompts. `sources/` holds the generated painting sources in the downloadable pack; these are not ready-to-use game tiles.

## Source geometry

Source branch: `feature/trainer-variety-music-20261112`, commit `6fdfec3469776fd5a509ed5eb432673db510be56`.

| Variant | Exterior source rectangle (metatiles) | Size | Interior source / size |
| --- | --- | --- | --- |
| Hoenn | PetalburgCity, x9 y16, 4x4 | 64x64 | PetalburgCity_House1, 10x9 (160x144) |
| Kanto | SaffronCity_Frlg, x41 y34, 5x5 | 80x80 | SaffronCity_House_Frlg, 11x9 (176x144) |

The final native entrance cell is retained byte-for-byte. Surrounding architecture is new. Door animation transitions and any upper door-animation cells still need checking in the actual ROM. Interior warp coordinates and warp graphics are preserved, but the room floor/furniture arrangement and collision grid are new. The retained original actor coordinates are reachable; their scripts are reference data, not new shop interactions.

An optional Saffron ordinary-house target (x25 y17, 5x5, door x27 y21) is documented by `templates/kanto/saffron-target.png`. Its right edge is partly occluded by Silph Co. Preserve that occlusion if installing; do not paint over Silph Co. No skyscraper replacement is included.

## Relocation and integration

Requirements for tools: Python 3, Pillow and NumPy.

Run `python tools/validate.py` from anywhere. It checks all 26 modules and writes `validation.json`. Run `python tools/check_relocation.py` for independent relocated-reference rendering against the native game resources. In the repository this finds the repository root automatically; for an extracted ZIP set `POKEEMERALD_ROOT` to the matching game source checkout. Temporary allocations are written beneath `.validation-work/`. The checks compare every rendered pixel and write `relocation-validation.json`; these are standalone allocations, not live-city installation tests.

`python tools/relocate.py MODULE OUTPUT --tile-base N --metatile-base N --palette-slots N [N]` creates relocated fragments without modifying a repository. Tile/metatile bases must be in the appropriate secondary bank and fit the 1024-entry total. Bounds are checked, but the tool cannot prove the destination allocation is unused.

- Emerald-layout primary boundary: 512; FRLG-layout boundary: 640. These are the current project's runtime layout rules, not a promise that one fragment can be copied between unmodified stock ROMs.
- Exterior modules can be appended to their respective native secondary tilesets after checking free tile/metatile space. A free custom palette bank is required (Saffron's unused secondary slot 7 is a candidate). Never replace a palette used by other city tiles.
- Interiors require a DEDICATED secondary tileset: the native Hoenn interior atlas is full. All retained native secondary exit tiles are copied into the module's tile pool, while primary references and native palette numbers remain native. Start the dedicated tile/metatile allocation at the region's primary boundary and preserve the original primary tileset. Choose two unused palette slots (Hoenn candidates 7/11; Kanto candidates 7/8), and copy retained native palette files as needed.
- Install matching attributes, palette assignments, blockdata and collision together. Keep local map IDs and old source-map words separate. Preserve original maps and assign themed rooms to new layouts/maps unless an explicit replacement has been reviewed.
- The tutor's intended sign text is `Illegal Move Tutor's House`. A native sign/bg-event and text-script proposal is in `integration-proposals/`; it is not registered in a live map. No working tutor mechanic is claimed by this asset pack.
- Add business scripts, entrances/exit destinations, event placement and music separately. Check the active camera, actor overlap, all door animation frames and transitions in mGBA. Test a normal save on the exact packaged ROM.

## Validation limits

The pack checks tile packing, index bounds, palette data, native silhouettes/backgrounds, entrance pixels, exit pixels/coordinates, furniture masks, collision footprints, connected walkable floor and reachability of retained native actor positions. Project baseline and cast source validators were also run against the unchanged source branch.

No ROM was built from these modules. Pip and cast compiled-artwork verifiers passed against the unchanged PR #13 baseline ROM (SHA-256 `3f8722bfe26d190d543671d3cd6a6011fa2465ab529806390ef9ddd9d2bef10a`). That baseline ROM does not contain these building modules. No emulator traversal, door animation, event/script integration or normal-save migration test has been run for this pack. `rom_integration_complete` is false for every module.

Artwork sources were generated with the built-in imagegen tool, then reduced, masked, palette-indexed and compiled locally. Existing project sprites, maps, saves and gameplay code remain unchanged.

## Saffron mid-rise buildings

Two additional 80x96 facade modules use the exact native 5x6 decorative block at x19 y25, beside Silph Co.: `modules/saffron/glitch/exterior` and `modules/saffron/bloom/exterior`. Their shared 16-colour custom palette permits one palette allocation for both designs. `previews/saffron-midrise-map-fit.png` places them at x19 y25 and x24 y25 without changing Silph Co., pavement or fences. This is an asset composite, not an emulator capture.

Those original blocks have no doors or interior warps, so the variants remain decorative. The furnished Kanto room modules belong to the small enterable house footprints, not to these decorative blocks.

The mid-rise modules require a rebuilt/repacked Saffron tileset variant. Each module fits the FRLG secondary-bank limit, but they do not fit in the current secondary atlas's 112 remaining tile slots by simple append. The relocation checks use a standalone secondary allocation to prove reference/palette correctness, not a conflict-free live-city allocation. Repack native and new tiles with the city map/metatiles, or create a city-specific primary/secondary pair, preserving original source assets. The preview showing both new facades together is not proof of a completed city resource allocation.
