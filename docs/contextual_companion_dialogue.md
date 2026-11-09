Companion reactions now use the message the player actually saw. Sprite type,
map name and a rotating personal-story passage cannot substitute for an NPC
response. Original area observations and the six ordered personal revelations
remain in explicit Talk / journal conversations. The watch remains unexplained.

Open the companion menu and choose **Dialogue setting**:

- **Normal** offers a yes/no reaction prompt after a supported interaction ends.
- **Only when asked** offers no automatic prompts. Talk to the companion after
  examining an object or talking to someone. They respond to that recent subject
  if a suitable, unheard response exists; otherwise they stay quiet.
- **Silent** mutes travel reactions and the Talk option. The follower, recruitment,
  companion switching, bond journal, gifts and personal-event choices remain.

The setting applies to Pip and all ten cast members, persists with a normal save,
and defaults to Normal when loading an earlier save. Cancel/B change nothing.
The original five companion menu entries retain their indices; settings append
as entry six.

This is an initial authored coverage batch, not full-world dialogue completion.
There are 47 new contexts, 49 exact message-label bindings and 517 individually
written replies (one per context for each of eleven voices). Subjects include
Oldale's changing footprint investigation, saving/rest, party order, healing,
Route 101 grass, Route 102's sneezing traveller, Petalburg reflections/storage,
Viridian's closed/returned leader and coffee conversations, Pallet's copied sign,
forest advice, household objects and selected later Hoenn/Kanto conversations.
The existing exact-label furniture reactions remain available when no new reply
overrides them. The twelve completed Kanto paired-scene replies retain their
original dialogue and memory, now bound to the actual completed-scene text.
Unknown branches stay quiet. This batch does not give every NPC,
trainer or interactive object a new reaction.

Responses use eight supplied expressions. A serious threat receives concern,
not a random joke. A footprint search does not trigger the later revelation;
the closed Viridian gym does not trigger the returned-leader response. An
unmapped last message invalidates any earlier mapped line in that interaction.
Runtime routing never searches keywords or guesses a conversation from clothing.

The hook starts only for a successful player A-button interaction. It records
normal primary-context field messages, defers until the original `end` command,
and never interrupts the original choices, battle setup, gifts or movement.
Immediate map scripts cannot finish the primary interaction. Scene suspension,
map changes and companion changes invalidate the offered subject. Automatically
started cutscenes, phone calls, native-only text printers and dialogue paths
that end through other mechanisms need separate reviewed hooks before claiming
coverage. A reaction is not evidence of a continuous campaign playthrough.

New context IDs are append-only. Each voice has its own persistent spent bits;
aliases for the same meaning share one context. Offering/declining spends a
reaction; accepting that offer can print it once. Only a fully printed cast
observation earns bond EXP. Repeating, saving/loading, switching companions or
toggling the setting cannot renew a spent reaction. Ask mode spends only when
the player requests the response, not merely when hearing the original NPC.
Existing exact-object replies continue using their original memory IDs.

SaveBlocks 1/2/3, the 34144-byte PC/fusion prefix and Bond v1's 416 bytes retain
their released layouts. A 1020-byte suffix at offset 34560 contains a magic,
version, mode, two reserved bytes and 11 independent 92-byte memory banks. Total
PokemonStorage is 35580 of 35712 bytes, leaving 132 bytes. The bank reserves 736
new semantic contexts per voice. Filling that capacity requires a reviewed save
design, not eviction or reuse of old bits. Old reaction/lore progress is intact.

Author new responses in `dev_scripts/companion_context_content.py`, build with
`python dev_scripts/build_companion_contexts.py`, and review the original text
and every voice/expression in `data/companion_dialogue/contexts.json`. Run
`python dev_scripts/validate_companion_dialogue.py` with all existing project
validators. Source-text changes require renewed semantic review. The source
validator cannot establish literary quality; real NPC dialogue and game frames
must also be checked on the exact final ROM.
