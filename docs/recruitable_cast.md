# Recruitable travelling cast

This update starts at the tested full-Kanto build, commit
`ba1f1f5f2173fc450fba6c0aae76c6c3ecac6ef3` (PR #8). It retains expanded starter
selection, Living Hoenn, rare encounters, Pip's supplied Morph artwork, the watch,
Kanto's campaign and existing save memory. It adds friends, not a romance system.

Each character first explains a small personal request. Complete it, accept their
four-Pokemon challenge, and win to unlock their friendship. Joining immediately is
optional. A donated item is taken only after accepting the challenge, once; losing
does not require another donation. Shown Pokemon stay in the player's party.
Walking requests count actual on-foot steps after the first conversation, including
ordinary travel, and persist through normal saves.

| Character | First meeting | Levels | Request | Team |
| --- | --- | --- | --- | --- |
| Silas | Oldale | 7 | Show Wurmple | Magnemite, Porygon, Ralts, Budew |
| Emi | Route 102 | 7 | Walk 64 steps | Hoothoot, Ralts, Murkrow, Buneary |
| Nico | Route 104 | 10 | Give one Oran Berry | Slugma, Shroomish, Cherubi, Munchlax |
| Kade | Kanto Route 2, southern section | 10 | Show Rattata | Sandshrew, Rattata, Houndour, Machop |
| Ashe | Kanto Route 3 | 13 | Walk 160 steps | Kricketot, Whismur, Chingling, Zubat |
| Vera | Slateport | 18 | Give one Paralyze Heal | Electrike, Magnemite, Voltorb, Pachirisu |
| Lume | Verdanturf | 19 | Show Nincada | Nincada, Duskull, Spoink, Hoothoot |
| Mochi | Kanto Cerulean | 19 | Give one Poke Ball | Buneary, Skitty, Combee, Roselia |
| Riven | Kanto Vermilion | 21 | Show Abra | Kadabra, Sableye, Misdreavus, Mr. Mime |
| Zuri | Kanto Celadon | 27 | Give one Potion | Smeargle, Chatot, Aipom, Spinda |

Emi and Silas are three levels above the maximum nearby native grass encounter.
The other eight are five levels above it. Teams use existing first-four-generation
Pokemon data. No terrain, original event positions, warps or connections change.

Talk to the active companion and choose **Change company** to select an unlocked
friend or Pip. One person follows at a time; they do not occupy a Pokemon party
slot or become an automatic battle partner. **Head home** lets a cast member
return to their original meeting place. Story escorts cannot be replaced by this
menu. Switching people preserves everyone's friendship, commentary and lore.

The supplied indexed walking sprites and all eight portrait expressions per person
are preserved exactly. A 64x64 portrait appears above the normal dialogue window
for cast dialogue and changes to the line's assigned expression. It uses a separate
sprite/palette allocation and is removed when dialogue closes or a battle starts.
Their neutral portraits also identify the trainers on the battle introduction.

The ten voices cover the same 402 live Pip source contexts in both regions: places,
NPCs, leaders, objects, travel, milestones and resolved living-world scenes. The
current authored set contains 940 distinct reactions plus 60 backstory passages.
Equivalent wording shares a canonical memory bit within that character. A heard
or declined offer is spent; moving to a similar shelf or cycling companions does
not produce the same line again. When nothing is fresh they remain quiet.

Each backstory has six ordered revelations. Further revelations require new spoken
observations (thresholds 0, 4, 9, 15, 22 and 30), and arise at related subjects or
when explicitly talking with the companion. They are never a rotating fallback.
Topics include belonging, creative confidence, grief, responsibility and community;
comic observations coexist with quieter comments. Nobody explains the watch.

Full authored scenes, personalities, teams and backstories are reviewable in
`data/cast/characters.json`; per-character lines and assigned expressions are in
`data/cast/dialogue_review.json`.

SaveBlock3 retains its entire released 1004-byte prefix and appends a 604-byte cast
bank, for 1608 bytes within the 1624-byte limit. Old cast-less saves initialize only
the new suffix. Existing dynamic NPC graphics IDs are explicitly reserved so that
appending characters does not reinterpret old saved graphic variables.

Checks: `validate_project_baseline.py`, `validate_kanto_campaign.py`,
`validate_cast.py`, `verify_pip_rom.py`, `verify_kanto_rom.py` and
`verify_cast_rom.py`. Runtime verification and CI results must accompany delivery;
source validation alone is not a claim of an in-game playthrough.
