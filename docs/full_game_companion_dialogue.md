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

Two interaction issues are being addressed locally:

- Imported Kanto furniture must select its native interaction family from the
  current layout format, not solely the executable's Emerald/FRLG build flag.
- Explicit item/decor/contact-registration success receipts must not erase the
  last actual NPC speaker. Unknown NPC text and bag-full failures still invalidate
  earlier candidates. This uses exact receipt identities, never wording guesses.

These changes are not yet a compiled or delivered full-game build. Source checks
passing does not substitute for new exact-ROM/native interaction validation.

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
native-validated save format. The user has been asked whether new dialogue should use shared automatic no-repeat
memory with explicit alternative perspectives, or retain fully independent history
and require a larger save-storage redesign. This gameplay/storage choice is pending;
do not implement the dependent format until the user answers. Existing pilot
independent memory is preserved under either choice.

Release requires reviewed eligibility/bindings and voice coverage throughout the
intended game, source/artwork checks, successful builds/tests, native branch and
service/object checks, old normal-save migration, persistence and repetition/EXP
checks. Report remaining gaps honestly. Do not deliver another small batch as if
it completed the full-game expansion.
