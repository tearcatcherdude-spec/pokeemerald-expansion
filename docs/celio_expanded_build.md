# Expanded emulator build

The opt-in Windows Celio target retains the existing game engine, save layouts,
artwork and authored dialogue. It does not require the experimental dialogue
compression. Build with `make CELIO_ROM=1`; clean first when changing targets.
The ordinary target retains the GBA's 32 MiB limit and may overflow with this
project's growing content.

Celio rom128-4 maps an exactly 64 MiB ROM contiguously at 0x08000000–0x0BFFFFFF.
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
