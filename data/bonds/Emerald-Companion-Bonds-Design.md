# Emerald companion bonds and optional romance — design handoff

**Brainstorm proposal • November 8, 2026 • NOT implemented**

This package is for the main project conversation. It makes the ideas concrete enough to review, especially where to find relationship events. It does not authorize coding, uploading, merging, or replacing current work. The scene titles, balancing numbers, rewards, and locations below are proposed defaults, not previously approved final designs.

## What the user has asked for

- A young adult protagonist who did not start a journey when others did and is now setting out for the first time. Leave the reason open; do not assume failure, trauma, or laziness.
- Ten recruitable companions with numeric relationship EXP and levels, visible hearts, personal events, affection rewards, lore, and stronger optional battles.
- Progress through traveling together, listening to new comments, gifts, and meaningful shared experiences. Companions remain quiet when they have nothing new to say.
- Clearly named, recognizable special-event destinations with enough direction that the player does not get lost.
- A cozy, funny Emerald adventure. Adult characters do not require explicit sexual content. Every romanceable character must be explicitly an adult; existing child characters remain outside romance.

## The proposed player-facing system

Each character has Bond Level 1–20 and five hearts. EXP raises the level; completing personal events fills the hearts. Friendship gets the same practical rewards and a complete story. Romance is an explicit, optional branch, never an automatic result of walking or giving gifts. One human companion follows at a time, as currently implemented; the Pokémon party remains separate.

Example status screen:

> EMI — Bond Lv. 7 — 85 / 130 EXP to next level  
> ♥♡♡♡♡ — One personal event completed  
> Next event: Something Worth Keeping — Reach Bond Lv. 8

The EXP bar measures progress within the current level. Total accumulated EXP is available on the detail screen. Hearts count completed events, not purchases or romantic consent. Choosing friendship does not reduce EXP or close future ordinary dialogue.

### Exact EXP curve

EXP from current level L to the next is **60 + 10L**. Total EXP required for level L is **5 × (L−1) × (L+12)**. Level 20 caps at 3,040 total EXP. Further meaningful interactions still receive dialogue; the UI states MAX instead of pretending to award unusable EXP.

| Level | Total EXP | Level | Total EXP |
|---|---:|---|---:|
| 1 | 0 | 11 | 1,150 |
| 2 | 70 | 12 | 1,320 |
| 3 | 150 | 13 | 1,500 |
| 4 | 240 | 14 | 1,690 |
| 5 | 340 | 15 | 1,890 |
| 6 | 450 | 16 | 2,100 |
| 7 | 570 | 17 | 2,320 |
| 8 | 700 | 18 | 2,550 |
| 9 | 840 | 19 | 2,790 |
| 10 | 990 | 20 | 3,040 |

Pending events never discard EXP. Events occur in order even if the player already reached a higher level. Before the first event, zero hearts is normal. At most five hearts can be completed.

### Concrete ways to gain EXP

| Action | Proposed EXP | Repeat rule |
|---|---:|---|
| Walk 256 on-foot steps with active companion | +5 | Maximum +40 per travel leg; bicycle, surfing and forced movement do not count |
| Hear a distinct authored reaction to its end | +10 | Once per canonical reaction ID, not per object or visit |
| Hear an existing/new ordered personal lore passage | +25 | Once; no automatic replay to farm EXP |
| Finish a companion request or small shared scene | +40 | Once per objective ID |
| Reach a designated new exploration landmark together | +30 | Once per designated landmark, not every map boundary |
| Give neutral / liked / favorite gift | +5 / +15 / +30 | One EXP-bearing gift per travel leg; at most 150 gift EXP in each heart band |
| Finish a personal event | +60 | Once; event 5 gives its reward and ending, since EXP is already MAX |
| Complete the stage-4 rematch or alternate challenge | +100 | Once, instead of the normal +60 personal-event award |

**Travel leg:** starts on recruitment and renews after a first-time trainer victory, first-time designated exploration landmark, or unique quest/personal-event completion while that companion is active. These are unique completed objectives, not repeated rematches. Door cycling, changing companions, reloading, and repeated comments never renew it. Show “Walking EXP this leg: 25/40; gift EXP available” on the details screen. A pending event remains available even after the leg cap. For completed saves with few fresh objectives left, reaching 2,048 eligible walking steps also unlocks an explicit “Rest together / Start another outing” journal action at any accessible Pokémon Center exterior. This quiet rest costs nothing, awards no EXP itself, and renews the leg only after confirmation. It does not repeat old comments or change event flags. Thus walking can always advance a late-recruited companion; looping doors or switching companions still cannot reset a leg. Deliberate walking remains a slow, valid option, rather than becoming permanently capped. This replaces an earlier loose daily-cap idea: there is no real-world clock requirement.

Gift bands are events completed 0, 1, 2, 3, or 4; each has its own 150 EXP limit. The preview displays whether the gift can currently grant EXP, its amount, and whether the item will be consumed. Cancel consumes nothing. Declined gifts consume nothing. Gifts after a cap are optional flavor and explicitly show +0 EXP. Each character's favorite/liked item list needs authoring and review before implementation; do not infer preferences from gender.

Progress stays with benched companions. No neglect decay, penalty for silence, penalty for skipping dialogue, or jealousy for traveling with another friend. Give fresh actions stable IDs. Never award multiple overlapping comment/lore bonuses for the same passage. At a milestone threshold, a small notification says the event is available, rather than interrupting a battle or scene.

## Finding events without guesswork

Add a Companion Journal entry with **region → city/route → named landmark → meeting point**. A ready event has Track, Meet here (when already at the site), and Later options. Tracking highlights the destination on that region's map and shows a nonblocking heart marker on the exact meeting tile when the player arrives. These are proposed UI features, not existing features.

Example journal entry:

> EMI — Something Worth Keeping — Heart Event 2  
> **Hoenn → Rustboro City → Pokémon Center**  
> **Meet outside, beside the front entrance. Look for the heart marker.**  
> Ready: Bond Lv. 8; The Streetlamp Moon completed.  
> Bring: Nothing. No payment. Any time, any weather.  
> Objective: Help Emi choose which draft poem to keep.  
> Reward: 2 Rare Candies; +60 Bond EXP.  
> [Track destination] [Later]

If locked, show the actual unmet requirements: “Reach Bond Lv. 8,” “Complete The Streetlamp Moon,” or “Visit Rustboro City first.” For another region, label Kanto/Hoenn explicitly. Journal tracking uses the selected region's map; it does not reveal the watch or make characters discuss it. Ordinary route guidance may list connected, already visited towns; do not invent a magical navigation power.

No time-of-day windows, random appearances, weather checks, one-day-only invitations, or hidden approval tests. An evening atmosphere can be staged after the player chooses Begin, without waiting for the clock. Late-game areas remain subject to normal story access; the journal names the area and says it has not been reached. No teleporting past plot gates.

At the site, interacting with the marker offers Begin / Later and temporarily stages the companion and scene actors. The follower must not duplicate itself. Restore ordinary followers, actors, weather and controls on completion, cancellation, map exit and load recovery. Markers never occupy doors, stairs, warps, mandatory paths, or existing NPC tiles. Do not redesign maps to fit these events.

**Placement precision:** the map folders and map IDs in this package were checked against the local current cast checkout. Landmark descriptions are proposed meeting sites. Exact X/Y tiles have intentionally not been invented: `marker_tile: null` means the implementing conversation must inspect the map, place the marker on a safe adjacent tile, and verify the approach and exit. Before release, replace every null with validated coordinates and show a marked screenshot. Final in-game wording must match the actual marker, including a side of the entrance if necessary.

## Five event stages

| Stage | Unlock | Purpose | Additional gates | One-time practical reward |
|---|---|---|---|---|
| 1 | Lv.4 / 240 EXP | Small outing; comfort and personality | Recruitment, reached destination | 1 Rare Candy; +60 Bond EXP |
| 2 | Lv.8 / 700 EXP | Trust and a concrete shared task | Stage 1 | 2 Rare Candies; +60 Bond EXP |
| 3 | Lv.12 / 1,320 EXP | Explicit interest conversation | Stage 2 | Thematic move unlock; +60 Bond EXP |
| 4 | Lv.16 / 2,100 EXP | Resolve rematch OR meaningful nonbattle challenge | Stage 3; four badges in either region | Powerful move unlock; +100 Bond EXP |
| 5 | Lv.20 / 3,040 EXP | Mutual commitment OR close-friend conclusion | Stage 4; existing six lore passages heard in order | Personal keepsake; 3 Rare Candies; recurring follow-up dialogue |

Every event requires the destination to have been visited and its normal entrance to be accessible. No other badge gates are proposed. Stage-4's four-badge gate also applies to stage 5. The journal lists these requirements exactly. If old lore is pending, offer an explicit “Hear their story” option while together; do not require guessing which sign activates it. Continue existing lore rather than replacing it or exposing later revelations early. Previously heard lore on an old save counts immediately; do not make the player rehear it or award retroactive duplicate rewards.

At stage 3: “I'd like this to be a date,” “I'm glad we're friends,” “I'm not sure yet.” At stage 5, ask for mutual commitment explicitly. No kiss or dating label without the player's choice and a positive character response. “Not yet” leaves a journal option to revisit the conversation at the same named location. A later, explicit change of mind can reopen interest without repeating rewards. Friendship is never written as a failure ending. Do not assume exclusivity: the default proposal permits only one committed romance, explains that before commitment, and allows a respectful breakup without losing friendship or completed rewards. This exclusivity rule is a proposal needing approval, not an existing user requirement.

### Reward moves and personal keepsakes

These are proposed **move-name unlocks**; do not assign numeric TM IDs without auditing the expanded project's existing items. Prefer a reusable tutor entitlement if duplicate TM IDs would conflict. No unlimited repeat item rewards.

| Companion | Stage 3 | Stage 4 | Stage 5 keepsake |
|---|---|---|---|
| Silas | Light Screen | Psychic | Annotated Field Notebook |
| Emi | Protect | Shadow Ball | Handwritten Poem |
| Nico | Sunny Day | Flamethrower | Spare-Chair Recipe Card |
| Kade | Dig | Earthquake | Courier Route Card |
| Ashe | Rest | Hyper Voice | Footsteps Score |
| Vera | Thunder Wave | Thunderbolt | Folding-Seat Blueprint |
| Lume | Calm Mind | Dream Eater | Collected Stories Booklet |
| Mochi | Substitute | Dazzling Gleam | Working-Pockets Sketch |
| Riven | Reflect | Dazzling Gleam | Signed Honest Trick Card |
| Zuri | Rain Dance | Energy Ball | Travel Mural Print |

Friendship and romance receive identical move/item rewards, with different personal text on keepsakes. Keepsakes should be journal collectibles, not ten new mandatory bag objects. Check move legality and existing availability during implementation; any replacement requires review. These unlocks are an extra acquisition route, not a reason to remove existing TM sources. No mandatory power is locked behind dating. Duplicate access to Dazzling Gleam is intentional.

### Stage-4 trials and continuing battles

Preview the complete team, battle level, rules, and reward before accepting. Use each companion's existing four Pokémon as the basis for a stronger evolved team. Do not alter the early recruitment battles. Suggested uniform trial levels: 40 with 4–6 badges in the more advanced region; 50 with 7–8; 60 after either regional League; 70 after both. Use the highest applicable band and recheck on acceptance. These are battle levels, entirely separate from Bond Level. Difficulty still needs playtesting; level 40 may require the player to return later, which the preview must make clear.

Every character also has the named nonbattle challenge in their stage-4 outline. It gives the same event progress, +100 EXP and reward, with the same story gate. A battle loss does not remove affection, gifts, money, or items; recover the party and allow a free retry or switch to the alternate challenge. Selecting a challenge does not select romance. Battle staging must not warp the player behind progression gates. Neither approach includes a reaction-time test or permanently wrong answer.

After the story concludes, an opt-in “Train together” rematch can use the current level band. It awards ordinary battle experience as deliberately balanced, but never repeats relationship EXP, heart rewards or Rare Candies. No forced perfect-IV/510-EV upgrade of these teams is implied; the user's earlier perfect-IV/EV request applied to rare catchable encounters. Moves, held items and trainer stats need a separate reviewed team sheet.

## All 50 proposed events and meeting points

Each row is one event, in order. All sites are outdoor meeting points to avoid tickets, disappearing ships, private-room locks, or guessing which interior floor. Scene staging is temporary. No rare consumable is required; any task materials are supplied and cleaned up afterward.

### Silas

Voice: Earnest field scientist; precise, unintentionally funny, learning to listen.

**1. Attendance of Two — Bond Lv. 4**  
**Hoenn → Oldale Town → Outside the Pokémon Center, beside the entrance.**  
Help Silas observe a Wurmple without interrupting it. His report concludes that sitting quietly counts as fieldwork.  
Map: `MAP_OLDALE_TOWN`. Event: `bond_silas_01`.

**2. Voices in Broken Things — Bond Lv. 8**  
**Hoenn → Rustboro City → Outside the Devon Corporation front entrance.**  
Sort three harmless discarded components with Silas. He talks about his mother repairing radios and asks for help instead of pretending to know everything.  
Map: `MAP_RUSTBORO_CITY`. Event: `bond_silas_02`.

**3. No Report Required — Bond Lv. 12**  
**Hoenn → Slateport City → Outside the Oceanic Museum front entrance.**  
Let Silas enjoy an outing without taking notes. He asks whether this is a date; choose romance, friendship, or not yet.  
Map: `MAP_SLATEPORT_CITY`. Event: `bond_silas_03`.

**4. Peer Review — Bond Lv. 16**  
**Hoenn → Oldale Town → Outside the Pokémon Center, beside the entrance.**  
Take an optional research-team rematch or solve a three-observation field exercise together. Silas accepts that listening matters as much as being right.  
Map: `MAP_OLDALE_TOWN`. Event: `bond_silas_04`.

**5. A Letter Home — Bond Lv. 20**  
**Hoenn → Lilycove City → Outside the Department Store main entrance.**  
Help finish a letter about the journey. Romance offers a mutual commitment conversation; friendship offers a promise to keep doing fieldwork together.  
Map: `MAP_LILYCOVE_CITY`. Event: `bond_silas_05`.

### Emi

Voice: Goth poet with bone-dry humour; attentive to small kindnesses, quietly courageous.

**1. The Streetlamp Moon — Bond Lv. 4**  
**Hoenn → Petalburg City → Outside the Pokémon Center, beside the entrance.**  
Hear Emi admit that her first moon poem described a streetlamp. Choose to listen without demanding a punchline.  
Map: `MAP_PETALBURG_CITY`. Event: `bond_emi_01`.

**2. Something Worth Keeping — Bond Lv. 8**  
**Hoenn → Rustboro City → Outside the Pokémon Center, beside the entrance.**  
Help Emi decide which of three draft verses to keep. She recalls her aunt keeping the original poem, and explains why being taken seriously is frightening.  
Map: `MAP_RUSTBORO_CITY`. Event: `bond_emi_02`.

**3. No Punchline — Bond Lv. 12**  
**Hoenn → Verdanturf Town → Outside the Contest Hall main entrance.**  
Emi reads a short honest poem. Ask whether she means it romantically, say you value her friendship, or take time to think.  
Map: `MAP_VERDANTURF_TOWN`. Event: `bond_emi_03`.

**4. Read It Anyway — Bond Lv. 16**  
**Hoenn → Verdanturf Town → Outside the Contest Hall main entrance.**  
Support a small voluntary poetry reading, or accept her optional four-Pokémon rematch. The challenge is sharing something sincere, not becoming louder.  
Map: `MAP_VERDANTURF_TOWN`. Event: `bond_emi_04`.

**5. The Next Page — Bond Lv. 20**  
**Hoenn → Lilycove City → Outside the Lilycove Museum main entrance.**  
Emi offers an unfinished travel journal. Agree on a future together or as close friends; she keeps her own voice and ambitions.  
Map: `MAP_LILYCOVE_CITY`. Event: `bond_emi_05`.

### Nico

Voice: Playful baker; irreverent food metaphors, generous without treating people as projects.

**1. Emergency Spare Chair — Bond Lv. 4**  
**Hoenn → Route 104 → Outside Pretty Petal Flower Shop, on its front path.**  
Help Nico set out a small picnic and invite a tired traveler. The scene introduces the spare-chair tradition without adding an impassable table.  
Map: `MAP_ROUTE104`. Event: `bond_nico_01`.

**2. Not Her Recipe — Bond Lv. 8**  
**Hoenn → Rustboro City → Outside the Pokémon Center, beside the entrance.**  
Taste two imperfect batches and help Nico choose his own direction rather than copying his grandmother exactly.  
Map: `MAP_RUSTBORO_CITY`. Event: `bond_nico_02`.

**3. Two Seats Reserved — Bond Lv. 12**  
**Hoenn → Slateport City → At the northern entrance to the outdoor market.**  
Nico asks whether a shared meal is a date. Give a clear romance, friendship, or not-yet answer before the scene continues.  
Map: `MAP_SLATEPORT_CITY`. Event: `bond_nico_03`.

**4. A Kitchen That Listens — Bond Lv. 16**  
**Hoenn → Slateport City → At the northern entrance to the outdoor market.**  
Complete a small food-preference request using supplied ingredients, or accept a cooking-themed team rematch. No rare ingredient hunt is required.  
Map: `MAP_SLATEPORT_CITY`. Event: `bond_nico_04`.

**5. The Spare Chair Stays — Bond Lv. 20**  
**Hoenn → Lilycove City → Outside the Department Store main entrance.**  
Sketch a future café plan while keeping Nico’s travels open. Romance adds a shared future; friendship makes the player the first invited guest.  
Map: `MAP_LILYCOVE_CITY`. Event: `bond_nico_05`.

### Kade

Voice: Dry courier with a protective streak; treats ridiculous logistics very seriously.

**1. Parcel With Feelings — Bond Lv. 4**  
**Kanto → Vermilion City → Outside the Pokémon Center, beside the entrance.**  
Walk one short delivery with Kade. The package is ordinary; his customer-service smile is the comedy.  
Map: `MAP_KANTO_VERMILION_CITY`. Event: `bond_kade_01`.

**2. Ask for Help — Bond Lv. 8**  
**Kanto → Cerulean City → Outside the Pokémon Center, beside the entrance.**  
Help Kade ask a local courier for directions. Discuss the late delivery without revealing a hidden disaster or making the player fix his past.  
Map: `MAP_KANTO_CERULEAN_CITY`. Event: `bond_kade_02`.

**3. Off the Clock — Bond Lv. 12**  
**Kanto → Celadon City → Outside the Department Store main entrance.**  
Kade planned an outing with no delivery deadline. Clarify whether it is a date, friendly company, or something to revisit later.  
Map: `MAP_KANTO_CELADON_CITY`. Event: `bond_kade_03`.

**4. Shared Load — Bond Lv. 16**  
**Kanto → Vermilion City → Outside the Pokémon Center, beside the entrance.**  
Accept an optional courier-team rematch, or plan a safe three-stop delivery using a simple menu. Asking a partner for help is the turning point.  
Map: `MAP_KANTO_VERMILION_CITY`. Event: `bond_kade_04`.

**5. Going Forward — Bond Lv. 20**  
**Kanto → Cerulean City → Outside the Gym front entrance.**  
Kade makes plans because he wants a future, not to repay a mistake. Agree on romance or a lasting traveling friendship.  
Map: `MAP_KANTO_CERULEAN_CITY`. Event: `bond_kade_05`.

### Ashe

Voice: Soft-spoken musician; observant, awkward jokes, understated warmth.

**1. Applause, Carefully — Bond Lv. 4**  
**Kanto → Pewter City → Outside the Museum main entrance.**  
Listen to a tiny practice performance. Whismur’s enthusiastic applause is the joke, with no forced humiliation.  
Map: `MAP_KANTO_PEWTER_CITY`. Event: `bond_ashe_01`.

**2. The Name on the Noticeboard — Bond Lv. 8**  
**Kanto → Cerulean City → Outside the Pokémon Center, beside the entrance.**  
Ashe shares the missed audition and the uncle who kept a place open. Help pick a manageable first performance.  
Map: `MAP_KANTO_CERULEAN_CITY`. Event: `bond_ashe_02`.

**3. A Part for Footsteps — Bond Lv. 12**  
**Kanto → Vermilion City → Outside the Pokémon Fan Club entrance.**  
Hear the piece inspired by traveling together. Ashe asks permission to dedicate it; choose romantic meaning, friendship, or not yet.  
Map: `MAP_KANTO_VERMILION_CITY`. Event: `bond_ashe_03`.

**4. One Song Is Enough — Bond Lv. 16**  
**Kanto → Vermilion City → Outside the Pokémon Fan Club entrance.**  
Support a small performance with three forgiving encouragement choices, or take an optional sound-themed rematch. A wrong menu choice cannot destroy the relationship.  
Map: `MAP_KANTO_VERMILION_CITY`. Event: `bond_ashe_04`.

**5. An Encore by Choice — Bond Lv. 20**  
**Kanto → Celadon City → Outside the Pokémon Center, beside the entrance.**  
Attend a second modest performance. Discuss continuing together without requiring Ashe to become a famous performer.  
Map: `MAP_KANTO_CELADON_CITY`. Event: `bond_ashe_05`.

### Vera

Voice: Enthusiastic mechanic; bold problem solver, gadget comedy, respects boundaries.

**1. Official Sit-Down Consultant — Bond Lv. 4**  
**Hoenn → Slateport City → Outside Stern’s Shipyard front entrance.**  
Test a folding rest seat. The device remains a small temporary scene prop and Vera asks before involving a Pokémon.  
Map: `MAP_SLATEPORT_CITY`. Event: `bond_vera_01`.

**2. What Problem Does It Solve? — Bond Lv. 8**  
**Hoenn → Mauville City → Outside the Bike Shop entrance.**  
Compare three travel-tool sketches and prioritize actual accessibility. Vera recalls her father’s advice.  
Map: `MAP_MAUVILLE_CITY`. Event: `bond_vera_02`.

**3. A Walk Without a Test Run — Bond Lv. 12**  
**Hoenn → Slateport City → Outside the Oceanic Museum front entrance.**  
Vera deliberately leaves the prototypes packed. Ask whether this is a date; friendship and not-yet are equally respected.  
Map: `MAP_SLATEPORT_CITY`. Event: `bond_vera_03`.

**4. Trust Before Voltage — Bond Lv. 16**  
**Hoenn → Mauville City → Outside the Bike Shop entrance.**  
Take an optional electric-team rematch, or inspect a supplied nonfunctional demonstration circuit. Vera listens to Electrike before proceeding.  
Map: `MAP_MAUVILLE_CITY`. Event: `bond_vera_04`.

**5. Built to Make Room — Bond Lv. 20**  
**Hoenn → Slateport City → Outside Stern’s Shipyard front entrance.**  
Finish a small accessible rest-stop proposal. Romance and friendship both preserve Vera’s independent work and the player’s journey.  
Map: `MAP_SLATEPORT_CITY`. Event: `bond_vera_05`.

### Lume

Voice: Gentle folklorist; eerie deadpan, patient curiosity, distinguishes stories from evidence.

**1. The Haunted Hinge — Bond Lv. 4**  
**Hoenn → Verdanturf Town → Outside the Pokémon Center, beside the entrance.**  
Investigate a supposedly haunted sound. The answer is a squeaky portable prop; Lume can still enjoy the story without inventing evidence.  
Map: `MAP_VERDANTURF_TOWN`. Event: `bond_lume_01`.

**2. Two Endings — Bond Lv. 8**  
**Hoenn → Fallarbor Town → Outside the Contest Hall main entrance.**  
Hear two versions of a grandmother’s story and choose to record both. Memories need not match to matter.  
Map: `MAP_FALLARBOR_TOWN`. Event: `bond_lume_02`.

**3. A Story for Two — Bond Lv. 12**  
**Hoenn → Verdanturf Town → Outside the Contest Hall main entrance.**  
Lume asks how the player wants to be described in a travel story. State romantic interest, friendship, or uncertainty explicitly.  
Map: `MAP_VERDANTURF_TOWN`. Event: `bond_lume_03`.

**4. Who the Story Helps — Bond Lv. 16**  
**Hoenn → Fallarbor Town → Outside the Contest Hall main entrance.**  
Help revise a story that unfairly blames someone, or take an optional folklore-team rematch. No supernatural claim about the watch is made.  
Map: `MAP_FALLARBOR_TOWN`. Event: `bond_lume_04`.

**5. Kind Enough to Remember — Bond Lv. 20**  
**Hoenn → Lilycove City → Outside the Lilycove Museum main entrance.**  
Read an ordinary, kind entry about traveling together. Decide what continuing companionship means without replacing grief with romance.  
Map: `MAP_LILYCOVE_CITY`. Event: `bond_lume_05`.

### Mochi

Voice: Cheerful designer; precise fashion wit, practical empathy, refuses appearance-based judgement.

**1. The Pocket Inspection — Bond Lv. 4**  
**Kanto → Cerulean City → Outside the Pokémon Center, beside the entrance.**  
Test a travel pouch with a lunch parcel. Mochi asks about comfort before appearance.  
Map: `MAP_KANTO_CERULEAN_CITY`. Event: `bond_mochi_01`.

**2. The Wrong Prize — Bond Lv. 8**  
**Kanto → Celadon City → Outside the Department Store main entrance.**  
Discuss the contest outfit that won approval but felt wrong. Help choose a useful design rather than judging anyone’s body.  
Map: `MAP_KANTO_CELADON_CITY`. Event: `bond_mochi_02`.

**3. Made With You in Mind — Bond Lv. 12**  
**Kanto → Cerulean City → Outside the Gym front entrance.**  
Mochi offers a practical sketch and asks whether this outing is a date. Choose romance, friendship, or not yet.  
Map: `MAP_KANTO_CERULEAN_CITY`. Event: `bond_mochi_03`.

**4. Room for Lunch — Bond Lv. 16**  
**Kanto → Celadon City → Outside the Department Store main entrance.**  
Solve a simple packing challenge with supplied objects, or accept an optional coordinated-team rematch. There is more than one successful arrangement.  
Map: `MAP_KANTO_CELADON_CITY`. Event: `bond_mochi_04`.

**5. A Place for What Matters — Bond Lv. 20**  
**Kanto → Fuchsia City → Outside the Pokémon Center, beside the entrance.**  
Mochi finishes the travel sketch with working pockets. Commit to romance or a lasting friendship without requiring a player clothing-system feature.  
Map: `MAP_KANTO_FUCHSIA_CITY`. Event: `bond_mochi_05`.

### Riven

Voice: Theatrical street magician; flamboyant wordplay, honest about consent and misdirection.

**1. A Bow Before the Trick — Bond Lv. 4**  
**Kanto → Vermilion City → Outside the Pokémon Fan Club entrance.**  
Help with a small public card trick. The audience is told it is a trick, and the joke lands on Riven’s excessive bow.  
Map: `MAP_KANTO_VERMILION_CITY`. Event: `bond_riven_01`.

**2. The Honest Explanation — Bond Lv. 8**  
**Kanto → Celadon City → Outside the Pokémon Center, beside the entrance.**  
Riven explains the old lie and slow repair of a friendship. The player listens without becoming a replacement for the person hurt.  
Map: `MAP_KANTO_CELADON_CITY`. Event: `bond_riven_02`.

**3. No Misdirection — Bond Lv. 12**  
**Kanto → Vermilion City → Outside the Pokémon Fan Club entrance.**  
Riven asks plainly about a date. Romance, friendship, and not-yet answers receive equally honest responses.  
Map: `MAP_KANTO_VERMILION_CITY`. Event: `bond_riven_03`.

**4. Resolve, No Hidden Cards — Bond Lv. 16**  
**Kanto → Celadon City → Outside the Pokémon Center, beside the entrance.**  
Accept an optional illusion-team rematch with its rules shown beforehand, or help prepare an openly explained stage routine. Winning is never consent.  
Map: `MAP_KANTO_CELADON_CITY`. Event: `bond_riven_04`.

**5. Unimpressive, Happily — Bond Lv. 20**  
**Kanto → Vermilion City → Outside the Pokémon Center, beside the entrance.**  
Share an ordinary outing with no performance. Riven chooses sincerity; the player chooses mutual commitment or close friendship.  
Map: `MAP_KANTO_VERMILION_CITY`. Event: `bond_riven_05`.

### Zuri

Voice: Charismatic mural artist; playful visual wit, community-minded, candid about uncertainty.

**1. Bent-Spoon Birds — Bond Lv. 4**  
**Kanto → Celadon City → Outside the Pokémon Center, beside the entrance.**  
Help choose a color for a portable practice board. Zuri explains why the ridiculous birds stay in the work.  
Map: `MAP_KANTO_CELADON_CITY`. Event: `bond_zuri_01`.

**2. Ask Before Painting — Bond Lv. 8**  
**Kanto → Fuchsia City → Outside the Pokémon Center, beside the entrance.**  
Collect three short opinions from temporary nearby scene actors. The community controls what is represented; no permanent map wall is overwritten.  
Map: `MAP_KANTO_FUCHSIA_CITY`. Event: `bond_zuri_02`.

**3. A Place in the Sketch — Bond Lv. 12**  
**Kanto → Celadon City → Outside the Department Store main entrance.**  
Zuri asks whether the player wants to join a personal outing. Make romantic interest, friendship, or uncertainty explicit.  
Map: `MAP_KANTO_CELADON_CITY`. Event: `bond_zuri_03`.

**4. More Than a Wall — Bond Lv. 16**  
**Kanto → Fuchsia City → Outside the Pokémon Center, beside the entrance.**  
Help preserve a small community story on a portable panel, or accept an optional expressive-team rematch. A lost wall is acknowledged without claiming paint can replace people.  
Map: `MAP_KANTO_FUCHSIA_CITY`. Event: `bond_zuri_04`.

**5. The People in the Picture — Bond Lv. 20**  
**Kanto → Celadon City → Outside the Pokémon Center, beside the entrance.**  
Reveal a travel mural sketch that includes people who helped along the way. Agree on a shared future or lasting friendship; Zuri’s community remains part of life.  
Map: `MAP_KANTO_CELADON_CITY`. Event: `bond_zuri_05`.

## Continuity and implementation handoff

This is a proposal against the November 8 context snapshot, not a claim that romance is implemented. The main conversation should recheck its current branch before integrating anything.

- Repository: tearcatcherdude-spec/pokeemerald-expansion. Current inspected cast work: draft PR #9, `feature/recruitable-cast`, commit `abca44ff33711c59df08e0734d41e658263c6128`, atop full-Kanto PR #8. Use the current development chain, not a stale cozy-Emerald checkout or master alone.
- Preserve expanded starters, Living Hoenn/Kanto scenes, the sixteen rare encounters, quiet remembered Pip dialogue, current Morph-derived Pip artwork/palette, all ten cast sprites, eighty expression portraits, recruitment requests, and existing six lore passages per character. There are 940 distinct authored cast reactions in the inspected source; do not replace them with a looping generic affection line.
- Preserve regional story/badge/healing state and the shared party/bag/PC rules. The watch remains a silent mystery. No character should explain it or refer to switching worlds.
- **Persistent storage is a prerequisite design problem.** Current SaveBlock3 is 1,608 bytes of a 1,624-byte allowance: only 16 bytes remain. Ten 16-bit EXP counters alone need 20 bytes, before event/gift/romance state. Do not squeeze this in by overwriting released fields. Audit viable storage and a normal-save migration plan before implementation. Preserve the released 1,004-byte prefix and the 604-byte cast appendage.
- Read the current AGENTS.md. Keep existing flag/dialogue/trainer/graphics IDs stable; use append-only additions and existing tombstones. Preserve protected Pip slots/map-group prefixes and exact supplied artwork. No resetting cast memory or regional banks to make room.
- Adult framing needs protagonist dialogue and age references audited across both regions; identify the ten cast members as adults without inventing exact ages here. Preserve voices, consent, independent goals, and friendship routes. Existing child NPCs stay non-romanceable.
- Proposed new scope includes the journal UI, region pins, event markers, EXP tracking, gifts, save migration, 50 scripted events, romance choices, move unlocks and trial encounters. None of those are confirmed implemented by this package. Stage art can reuse accepted expression portraits; do not generate replacement sprites automatically.

### Checks required before calling an implementation complete

1. Resolve persistent storage/migration first. Load normal existing saves, retain regional/cast state, save/reload, switch companions and regions, and verify every new counter and event choice persists independently.
2. For every one of the 50 events: finalize safe marker coordinates, capture a screenshot, walk from the named landmark to the marker, and verify clear entrance/exit, no warp collision, no duplicate follower, and no mandatory path blockage.
3. Test threshold boundaries, level-20 cap, pending lower events, event order, already-heard lore, declined romance, friendship completion, not-yet return, breakup, and reward-once guards. Stage 5 must never consume an unearned earlier event.
4. Test step/gift caps, unique-objective resets, bench/switch/load cases, repeated signs and battles. Display exactly what grants EXP. No gift is consumed without confirmation; cancellation and full bags cannot duplicate or lose rewards.
5. Test locked cities/regions, story gates, stage-4 badge gate, battle loss/retry, nonbattle route, menu cancel and interrupted-scene recovery. Markers hide during unrelated scripted scenes and reappear afterward.
6. Preserve required source/artwork/baseline validators and build checks from the current branch. Validate actual compiled artwork and normal-save migration, not only prepared fixtures. Test the journal on the GBA screen: long location names need pages/wrapping, not tiny text.
7. Report exactly what was built, what remains proposed, and which current commit was tested. The context snapshot's PR #9 CI was unfinished; this design package does not certify a newer build.

## Message to give the main conversation

Please read this package as a brainstorming/design handoff. I want the existing ten Emerald/Kanto companions to have concrete numeric Bond EXP and levels, optional adult romance, complete friendship routes, meaningful personal events and rewards, and clear event destinations. The attached document proposes the numbers and 50 events. Preserve the existing project and character work. Do not start implementation or publishing merely because this document exists. First review the proposed defaults, inspect the current branch, solve the save-storage constraint, and finalize safe marked meeting tiles. Tell me which design decisions still need approval before we turn this into an implementation task.
