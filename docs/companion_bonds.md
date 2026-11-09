# Companion bonds

Development on `feature/companion-bonds`, draft PR #10, extends the tested cast and
full-Kanto build from PR #9. The handoff's original proposal is preserved under
`data/bonds`; actual authored runtime content is in `events.json`,
`dialogue_review.json` and `trial_teams.json` in that directory.

The protagonist and ten cast members are adults; exact ages are unspecified.
Pip remains a friend with his existing artwork and dialogue. Romance is optional.
One committed relationship is allowed at a time. A respectful breakup retains
friendship, event hearts, bond EXP and practical rewards.

## Journal

Talk to your companion and choose Companion Journal. Select an unlocked cast
member to see Bond Level, within-level EXP, five event hearts, relationship, event
directions and unmet requirements. More contains EXP details, rest, reusable move
rewards, the final keepsake and optional training. Choosing someone in the journal
does not replace the active follower; use Change company to do that.

Events name the region, town and landmark. Track destination displays a
nonblocking tile heart when that companion is following and the event is ready.
Face it and press A, or choose Meet here while at the tile. The journal can also
show the destination region's map without moving the player. Its map is read-only;
it cannot fly or skip any story gate. Existing NPCs, warps and map terrain remain.
Emerald's Battle Tents are named accurately instead of calling them Contest Halls.

## Progress

Bond Level is 1–20. Total EXP for level L is `5 * (L - 1) * (L + 12)`;
level 20 caps at 3040. Hearts count five ordered events, unlocked at levels
4/8/12/16/20. Reaching a later level never consumes an earlier event.

* 256 eligible on-foot steps: +5, at most +40 per outing.
* A newly heard authored reaction: +10, after the text finishes. Declining or
  cancelling earns nothing. Existing spent reaction IDs never repeat for EXP.
* A newly heard ordered lore passage: +25 instead of the reaction bonus.
* A designated destination first explored together: +30, once per companion.
* A unique existing Hoenn/Kanto neighbor request: +40, once per objective.
* Neutral/liked/favorite gifts: +5/+15/+30, one EXP-bearing gift per outing,
  at most 150 gift EXP per heart band. The preview always shows consumption and
  actual EXP, including zero. Confirmation is required; cancel takes nothing.
* Events one/two/three: +60; event four: +100; event five is already at MAX.

A first trainer victory, new landmark or unique completed objective renews an
outing. Switching, loading, repeating dialogue and rematches do not. After 2048
eligible steps, rest near a Pokemon Center exterior to start another outing.
Rest costs nothing and grants no EXP, so late-recruited companions cannot become
permanently capped. There is no real-world clock, decay or neglect penalty.

Hear their story offers the next existing lore passage at appropriate bond levels;
it preserves old heard stages and never replays earlier revelations. Existing
observation-based lore also remains available.

## Events, choices and rewards

All ten characters have five authored scenes, including comedy and serious
reflection. Stage three explicitly offers a date, friendship or not yet. Stage five
offers commitment, close friendship or more time. Interest can be revisited at
the named meeting place without repeating item rewards. Friendship is complete,
with identical practical rewards. Children elsewhere in the game are not romance
candidates.

Stage one gives one Rare Candy, stage two two, and stage five three plus a journal
keepsake. Stage three and four unlock two thematic reusable tutor moves, with
normal Pokemon compatibility. No existing TM source is removed. A full bag keeps
the event pending rather than losing or duplicating the reward.

Stage four requires four badges in either region. Choose a previewed four-Pokemon
practice battle or a three-part nonbattle challenge for identical progress and
rewards. Battle levels are 40 at 4–6 badges, 50 at 7–8, 60 after either League,
70 after both, using the more advanced region. The early recruitment teams remain
unchanged. Trial teams use 20 IVs, no EV training and no held items. Free retries
and nonbattle alternatives remain available after a loss; practice restores team,
bag supplies and money. After the final event, opt-in practice rematches grant
ordinary Pokemon battle EXP but no repeat bond/event/item rewards.

## Save compatibility and validation

SaveBlocks 1/2/3 and the released 34144-byte PC/fusion prefix keep their layouts.
Bond v1 appends 396 bytes to the PC block, using its final sector's zero-filled
tail; total PC block size is 34540 of 35712 available. Existing normal saves retain
their checksums because the newly included legacy bytes are zero. Initialize only
the new suffix. Both rotating save slots cover bond data with the normal checksum
and save counter; Hall of Fame, Trainer Hill and recorded battle sectors remain.

Normal-save migration and save/Continue passed on the first foundation ROM,
including ten independent bond records and preserved cast/Kanto/Pip/PC data.
The full journal/event build is still undergoing build and native game validation.
Do not treat static tile placement as proof of a playable route. Final delivery
must identify the exact tested commit and remaining limitations.
