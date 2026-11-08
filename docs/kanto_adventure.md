# Full Kanto adventure integration

Work in progress on top of the corrected watch/Morph Pip baseline. This is not a
finished campaign release. All 417 existing regional maps and native scripts are
imported with separate persistent flag/variable and trainer ID namespaces. The
11 released watch map IDs remain stable. Native map data and original source
assets are retained, including eight gyms, dungeons, League and island maps.

Kanto save progress appends after the released 180-byte SaveBlock3 prefix. Hoenn
badges, starter selection, Pip memory, party, bag and PC are not reset. Existing
Pip catalogue IDs 0–259 stay fixed; 64 authored Kanto remarks append at 260–323.
NPCs and Pip must never explain the watch. Kanto begins with an existing trainer
and party; the forced second starter selection is skipped.

Validation: `python dev_scripts/validate_kanto_campaign.py` checks topology,
layout sizes, eight gym roots, source event bounds and unique script labels.
`python dev_scripts/validate_project_baseline.py` guards accepted Pip artwork,
starters and saved dialogue IDs. Native tests cover bank isolation and trainer
party resolution. Build/runtime campaign verification remains required.

Remaining integration includes regional field-move/quest engine adapters,
League completion, travel/respawn behavior, authored living-world scenes,
full Pip coverage and end-to-end campaign playtests. Do not distribute a build
as the full adventure until those checks pass.
