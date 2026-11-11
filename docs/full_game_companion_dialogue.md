Current writing checkpoint (2026-11-11): 3,963 authored situations, bound to
4,057 exact message labels, with eleven independently authored voices (43,593
replies). Full-game coverage remains unfinished. Remaining work includes final
service branches, objects and native/dynamic interactions. These counts describe
authored bindings, not a percentage of NPCs or a completed playthrough.

The 914-situation commit `bf2386d98cd7210d11f6437e8d155e724650574b`
has compiled as Emerald. The earlier 330-situation commit
`7a3acaeebc8b6493930042ff4ba14b6d14dfcdeb` passed its full GitHub CI and
starter regression. On that exact ROM, native interpreter fixtures verified all
1,100 replies in the newly appended 100-situation Kanto module, including exact
wording, portrait-expression pixels, finished-print EXP and spent memory. Separate
physical-field fixtures passed a trainer-sight approach/native victorious battle
and Oldale's coordinate-triggered blocked-path scene. Those fixtures use prepared
parties, positions and story flags; they are not a continuous playthrough. On the 914-situation ROM, all 990 interpreter replies across contexts 700-789
passed with the actual Lua adapter, spanning the original 736-context boundary.
An actual Kanto NPC above that boundary also retained Silas's spent comment
after normal save/reset/Continue while Emi remained independently fresh. The 1,470-situation commit cff113cec1c0b9bacf03a84e8c87801362a630f7
has compiled. Native checks passed the actual museum map-frame introduction and
a physical-step scheduled Roxanne call, plus companion-menu Ask and Silent
behavior for automatic scenes. Later writing awaits its own compiled/native
checks. The 1,700-situation ROM additionally passed all 132 Berry-state reply
fixtures and actual watering/harvest interactions. A real Kanto Name Rater
party-selection/refusal flow passed on the 1,470-situation ROM. Native Birch
rating table addresses are now explicit inventory edges; conditional Berry text
variants retain their whole assembly guards for review and source-drift checks.

Standalone successful item notices can now provide their own authored topic when
they are the first field message. Any earlier NPC/dynamic message, including an
unknown one, prevents a receipt from replacing it. The 2,246-situation ROM passed actual Potion pickup, receipt precedence,
unknown/dynamic invalidation, bag-full failure and interaction-reset checks.
Actual Birch regional and National rating conversations also passed. The 3,323-situation ROM additionally passed actual Old Amber handoff and
scheduled Roxanne call checks, thirteen exact receipt/unknown-precedence checks,
and a prepared native Brawly TM/contact sequence. The 3,415-situation ROM passed all four actual Day Care compatibility outcomes
across Hoenn and Four Island, plus all 1,012 replies in contexts 3,323-3,414
through native text/portrait/EXP fixtures. Its full CI and starter regression
passed. New writing and the additional three named receipts await another build.
Apprentice terminal templates are still being authored and need native checks.

The full-game companion expansion continues from tested PR #11 commit
79ec91c79bd03c426c64f824415befdfe99d351d. It is one project with one intended
completed expansion, not an early-game-only scope or a sequence of pilot releases.
Internal writing, commits and tests do not constitute completion of the request.

Scope includes Hoenn and the complete imported Kanto adventure, later towns,
gyms, routes, dungeons, League, postgame and available Sevii/Battle Frontier
content. Preserve the supplied sprites/portraits, Pip, starters, recruitment,
bonds, quests, regional story, items, party, PC/fusions and mysterious watch.

The worklist lives in `data/companion_dialogue/full_game`. It inventories actors,
background events, shared metatile dispatch, coordinate-triggered scenes and map
lifecycle scripts. It follows explicit script references through every branch;
therefore it includes intermediate messages, system text, conditional/unreachable
variants and non-speaking scripts. It is a conservative writing/hook worklist,
not the exact number of required final responses or proof of executed coverage.
Native printers, callbacks and dynamically constructed text need explicit review.

Every eligible conversation/object branch needs an exact binding and meaningful
responses for all eleven voices. Authoring must address the actual conversation,
its outcome and relevant local facts. Do not guess from graphics, use runtime
keywords, wrap arbitrary quotations in personality slogans, or silently replace
unwritten content with generic area remarks. Identical/equivalent text can share
a response only after semantic review. Unknown work is a gap, not a completed
coverage disposition. Existing companion scenes retain their own authored speech.

The first 47 context IDs, their wording, sources and expressions are frozen in
`released_pilot_contract.json`. Source validation checks this prefix. Subsequent
whole-game object writing is appended in `dev_scripts/companion_world_objects.py`.
The original pilot and all original Pip/cast memory remain intact.

Dialogue progress v2 uses the existing two reserved metadata bytes for an
append-only count of contexts checked for legacy history. It imports old exact
object offers/heard bits for each voice once, without clearing any released
bank. This prevents upgraded wording from replaying a previously heard subject.
After import, newly visited contexts remain independent even when the old system
used one broad canonical object comment for several descriptions. Legacy queries
are read-only and do not initialize or reset old progress. All old exact-object
aliases must be assigned within the original 736-context record; later contexts
use the host bridge. Unknown newer history formats retain their anchor and stay
quiet rather than being treated as an empty save.

The following interaction fixes are implemented and covered by the earlier
exact-ROM storage milestone checks below:

- Imported Kanto furniture must select its native interaction family from the
  current layout format, not solely the executable's Emerald/FRLG build flag.
- Explicit item/decor/contact-registration success receipts must not erase the
  last actual NPC speaker. Unknown NPC text and bag-full failures still invalidate
  earlier candidates. This uses exact receipt identities, never wording guesses.

A compiled checkpoint does not constitute the completed full-game expansion.
Source validation and exact-ROM interaction validation are reported separately.

Save capacity is a real design constraint. The released normal save has 536
unused bytes per slot across all four storage areas; the existing 1012-byte
reaction bitmap reserves 736 contexts per voice. Assigning a separate permanent
bit to every reachable label for every voice would need over 12 KB before final
eligibility/alias review. Filling the existing unused space alone permits 1120
dense contexts per voice with an eight-byte extension header. Compressing arbitrary
independent histories cannot guarantee fitting them into a smaller fixed budget.

Do not solve this by shrinking PC/fusion storage, erasing old history, taking
Hall of Fame/special sectors, dropping the backup save, silently sharing independent
history, hashing away fresh comments, or claiming raw compression has no worst case.
A pure layout model (`dev_scripts/companion_memory_layout.py`) checks a shared
proposal with 11616 new state bits, retaining the released pilot bits/metadata
and standard save boundaries. This is a proposal test, not an implemented or
native-validated save format. The user selected fully independent permanent
memory for every companion and conversation; the shared proposal is rejected.
Existing pilot independent memory must be preserved. The user confirmed mGBA on
Windows. Its documented Lua API is available starting in 0.10; the installed
executable is 0.10.5. Target the standard emulator with a small external helper,
not an unsupported larger Flash bank.

Save-path review found that link/Frontier saving skips the PC sectors and has a
separate incremental full-save path. The WIP instead appends a 56-byte anchor to
SaveBlock2 at offset 3884 (new total 3940/3968). All released offsets stay fixed.
The 1020-byte pilot record and its 736 bits per voice stay unchanged. The new
12288-context/voice RAM bitmap uses immutable host snapshots, addressed by SHA-256.
Each extended observation prepares its snapshot BEFORE the offer and updates the
RAM anchor only on host success. File failures roll back that observation bit;
all cartridge save paths then write a reference that already has a host file.
Save failure leaves prior slot references usable. This adds no host IO or new
abort branch to trading, Frontier or normal saving. Missing history is never
recreated as empty; original dialogue and ordinary gameplay remain usable.

`tools/companion_history/mgba_history.lua` implements the adapter; the host test
executes this actual Lua source through Lua 5.4 with mocked documented mGBA APIs.
It checks SHA-256 against Python, dense independent data, both snapshot anchors,
missing/corrupt/wrong-game files, bad destination pointers, file write failures
and acknowledgement ordering. This is not yet proof of native ROM integration.
Lua flush/close/rename protects application-level transaction ordering; it is not
a guarantee against Windows power loss. Immutable full snapshots currently grow
by about 17 KB per new extended observation; packaging/retention needs review.
The helper is required for extended observations; do not ship it without setup
instructions, an existing writable history directory and explicit backup guidance
covering both the .sav and history files. Do not delete snapshots that old saves
or save states may reference.

Normal saves, Hall of Fame saves, link saves, incremental link saves, failed
writes and backup-slot recovery all need explicit transactional tests.

On development commit daf52c96f55a6450de868172cb8f1c71f5a21c5d, the compiled ROM
bridge/artwork checks passed. ROM SHA-256:
`358173ee01bc182a428c4c1163a03563094faad6cb8aab847239d07ee0c35d6d`.
The actual ROM and actual Lua helper passed 13 grouped native save-function
checks: accepted-pilot migration, independent banks up to context 12287, normal
and partial saves, both incremental link paths, Hall of Fame save path with no
record buffer, damaged-newest-slot fallback, earlier normal saves, save-state
rollback, missing-file recovery, write-failure rollback, helper-disappearance
timeout and absent-helper saving. Prepared save fixtures hold background field
callbacks idle; these are not whole-game playthroughs or desktop Scripting UI
tests. Separate real A-button tests passed all 16 existing behavior groups,
including both regions, all voices/portraits, modes, decline/repeat and EXP.
Final storage-milestone verification used commit
`c38a6b059f4e9caadb27b775daf6065fb24815b5`, including one-time legacy import and
unknown-format preservation. CI run 42631520818 passed every required job:
5493 passed, 19 upstream known failures, 9 expected failures, 419 TODOs, 5940
total, zero unexpected failures. ROM SHA-256:
`1cb3c287d6f479b66111641699a783ea8d5b46add70295eb821c5bbc6943acd5`.
The exact ROM passed 53 grouped native checks, including all 781 authored
replies executed via real interpreter fixtures, exact cast expression pixels,
completed-observation EXP, the 13 storage groups, three retained-object/scene
and migration groups, six native-printer groups, actual NPC/mode/state checks
and an actual imported Kanto TV tile accessed from walkable floor with A.
See `data/companion_dialogue/full_game/history_validation.json` for the grouped
evidence and limitations. Catalogue message fixtures are not physical visits to
781 NPCs. No continuous whole-game playthrough or desktop Scripting UI operation
is claimed.

The prepared helper now finds its history folder beside its own Lua file; its
generated wrapper passed a moved-folder test with spaces in the path. A packaged
helper does not need Python while playing. Migration uses normal .sav files;
load older emulator states in their original ROM and save in-game before moving
the .sav. Retain a pre-upgrade backup because older ROMs cannot reliably read the
new SaveBlock2 checksum. Matching-ROM save-state rollback was tested separately.

The current full expansion remains unfinished, with only 71 authored contexts.
`python dev_scripts/check_full_dialogue_readiness.py` deliberately fails while
final-message eligibility, interaction-root/native-hook reviews or eligible
bindings are incomplete. `--report-only` prints the gaps without failing a
development build. Successful build/storage tests cannot turn these unreviewed
source entries into completed whole-world dialogue coverage.

Release requires reviewed eligibility/bindings and voice coverage throughout the
intended game, source/artwork checks, successful builds/tests, native branch and
service/object checks, old normal-save migration, persistence and repetition/EXP
checks. Report remaining gaps honestly. Do not deliver another small batch as if
it completed the full-game expansion.
