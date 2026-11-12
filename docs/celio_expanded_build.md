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

## Verified build

Commit `24a71a34ae2761c344b062e7f461385a258bfc10`, CI run `43241954371`,
artifact `13955042688`: Emerald/release and alternate builds passed. Compiled
Pip, cast, Kanto, trainer/music and history bridge checks passed.
The ROM SHA-256 is `2e3a1b0580f3aab88a550dd1b19125d06ec375a49dde6e7989192921522a89a9`.
It contains 33,550,856 linked bytes and 33,558,008 free bytes in the 64 MiB target.
Linked content currently fits just below 32 MiB; padding is not counted as content.
A separate small ARM program executed a real emulated CPU load from 0x0A000100
and stored the expected word in EWRAM using this exact Celio release.

The exact game binary loaded a copied synthetic legacy normal-save fixture in
Celio, wrote through native TrySavingData, reset, and continued. All 600 party
bytes and the current region/map matched after reload. Screenshots were captured
from native emulation. The history helper was supplied through --script.
This is a prepared-fixture compatibility smoke test, not a continuous campaign,
complete venue/tutor/battle regression, or proof of every history interaction.
The full unit suite was still running when this package was prepared.
No player-owned save or original emulator was modified.
