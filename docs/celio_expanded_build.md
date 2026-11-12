# Expanded emulator build

The opt-in Windows Celio target retains the existing game engine, save layouts,
artwork and authored dialogue. It does not require the experimental dialogue
compression. Build with `make CELIO_ROM=1`; clean first when changing targets.
The ordinary target retains the GBA's 32 MiB limit and may overflow with this
project's growing content.

Celio rom128-4 maps an exactly 64 MiB ROM contiguously at 0x08000000â€“0x0BFFFFFF.
The linker allowance and ROM pointer range are extended for this target, and
the finalizer enforces the exact file size required by that emulator.
This is a 64 MiB target, not yet a 128 MiB banked target. Future 128 MiB content
needs an explicit resource bank loader; changing the linker length alone is unsafe.

Upstream release: https://github.com/pm-start/mGBA_celio_edition/releases/tag/rom128-4
Release archive SHA-256:
`12e5a1c5c803e4750f454fd20d1d715de755510c070f906eb665fc7ca127b7dd`.
The portable emulator lives separately from the user's ordinary mGBA.
Use a copied normal save for initial testing. Emulator save states are not a
save-migration mechanism. No existing save structure is enlarged by this change.

Downloading and verifying the emulator does not establish compatibility:
normal saving/reloading, battles, maps, dialogue, the history helper and reads
beyond 32 MiB must be exercised in the packaged emulator before release.

## Verified graphics correction (2026-11-12)

Source commit `7decb9ac833d3afa5fa5e1ca50a9523e92366314`, CI run
`43257783402`, artifact `13962981136`. Emerald, release and alternate builds
passed, including compiled artwork/bridge and expanded-pointer checks. The full
unit job was still running at delivery time.
ROM SHA-256: `eb5509fc01cd4fb9cf560d7555ff04c6d5577017cef446c07be37ecb81b8f5b6`.
There are 33,554,536 linked bytes and 33,554,328 free bytes. The game now contains
104 real linked bytes beyond the ordinary 32 MiB cartridge limit.

Celio maps the former first cartridge mirror at 0x0A000000 to expanded data.
Effect-tagged script function pointers therefore use its remaining first-bank
code mirror at 0x0C000000. The standard target retains 0x0A000000. A linker
assertion keeps code in the first bank; the compiled verifier checked 232 tagged
functions. Using the data bank as code previously misdirected map scripts into
unrelated window routines, producing unsolicited empty windows during walking.

Venue allocation now reserves resources used by every connected neighboring map
and native tileset animations. The source validator preserves all 29 connected-map
views around twelve venues, including the Rustboro lamp tiles.

Native muted Celio checks used a copied player normal save and matching history:
Pokémon Center entry/exit, Route 104 to Rustboro, walking past the lamps, and
Rustboro to Route 116. Seven sampled views had no unexpected active windows;
screenshots showed correct lamps and interiors and no unsolicited white/red boxes.
Some starting positions were arranged for testing; this was not a continuous
campaign playthrough.

Native normal saving, cold reset and Continue preserved all 600 party bytes,
region/map, released 1608-byte Pip/regional/cast record, 35580-byte PC/bonds/context
record, and 56-byte companion history anchor. All 25 sampled linked data words
beyond 32 MiB matched the compiled ROM. Tests were muted and normal CPU timing
(overclock=1) is packaged; complete audio/stuttering regression remains pending,
as do full venue, tutor-menu and companion-battle regressions.

Desktop delivery archived the previous build and transferred its valid normal
save and complete companion-history folder byte-for-byte. Private save paths,
identities, hashes and snapshots are excluded from the repository.
