# Readability and species-aware tutor revision

This revision builds on tested graphics-fix commit 240f4343. It retains all game
progress formats and original art under graphics/readability_v2/originals.

## Artwork and placement

43 active custom battle sprites were reviewed: 41 use refined source art compiled
to 64x64 indexed PNGs, with readable faces, clean clusters and 15 visible colours.
Pip and Barnaby retain their original silhouettes/props with palette refinement
because their generated candidates drifted from those identifying details.
42 companion/trainer walkers retain their exact nine-frame pixel indices and
alignment with revised contrast palettes. Pip's original Morph walker and all
80 companion expressions remain byte-for-byte unchanged.

All 14 exterior modules have simpler signs/windows/colour blocks, including two
Saffron facades. All 12 interiors retain tile/furniture/warp geometry with adjusted
colour separation. Original palettes/art and source data remain recoverable.
The revised files are exact-hash pinned, not exempted from validation.

The bakery replaces Rustboro House3's 96x80 footprint, using its original animated
door at (26,46). Its three native residents/scripts remain in the bakery. The
nightclub replaces Fuchsia House1 at door (14,31), also retaining its three
residents/scripts. Both use the released private room IDs, so saves inside the
earlier venues remain valid. Route104 and KantoRoute11 regain their original maps
and events. Outdoor collision/behavior and existing doorway words remain exact.
Retired route layout IDs and cached venue views reload safely on normal Continue.

## Mr. Loophole

The previous implementation had a small Beldum-family pool, a small Magikarp pool
and one generic list for everything else. The new offline catalogue has separate
Beldum-family and Magikarp techniques plus typed/anatomical general candidates.
It does not access an online service while playing.

Candidates must be Gen I-IV moves, unlocked at the current level and within the
configured base-power cap. The caps are 40 below level15, 50 below25, 60 below35,
70 below45, 80 below55, then90. Conditional-power and support moves also have
individually reviewed minimum levels. No OHKO, fixed-damage, evasion or sleep-loop
lessons are included. The species' normal level-up, TM/tutor and egg moves are
excluded, as are already known moves.

Ranking rewards type fit, appropriate physical/special strength, missing attack
coverage and four different attack types where possible. Physical ambush/fast-body techniques are separate from psychic shadow energy.
A Fairy breeding group alone does not grant psychic techniques. Egg groups/types and
explicit anatomy exceptions determine which techniques are plausible; this is
a curated game policy, not a claim of mathematically optimal battle strategy.
Beldum's pool covers Steel, Psychic, Dark, Ghost, Ground and Rock through magnetic
movement, psychic projection and its existing metal prongs. Magikarp's pool uses
tail movement, water, river mud and swimming, without imaginary fists or wings.

The tutor never invents unrelated filler to force a menu. If fewer than four safe
extra moves qualify, no lesson is offered at that level. One lesson still starts
the existing per-individual 20-level cooldown, retained through boxing/evolution.
Moves and cooldown storage formats are unchanged; old pupils keep their progress.

Compile/check: python dev_scripts/build_roaming_tutor_catalog.py [--check].
Art checks: python dev_scripts/validate_readability.py, validate_venues.py and
validate_venue_connections.py. The focused C tests are named “Roaming tutor”.
Native emulator and normal-save checks must use the exact delivered ROM; source
previews are not ROM captures. Full campaign/audio regression is separate.
