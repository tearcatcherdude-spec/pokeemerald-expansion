"""Sevii 6-7 human NPC and trainer terminal branches from registered maps."""
ROWS=[]
EMOTIONS=dict(N='neutral',S='soft_smile',A='annoyed',F='flustered',D='sad',U='surprised',M='smug',L='laughing')
def add(key,labels,subject,lines):
    replies=[]
    for line in lines.strip().split('|'):
        line=line.strip()
        if len(line)>1 and line[1]=='~' and line[0]in EMOTIONS:line=EMOTIONS[line[0]]+line[1:]
        replies.append(line)
    assert len(replies)==11,(key,len(replies))
    ROWS.append(dict(key='sevii67_'+key,labels=labels.split(),subject=subject,replies=replies))

add('six_directions','SixIsland_Text_ThatWayToWaterPathRuinValley',
    "A boy gives directions through Water Path to Ruin Valley.",'''
S~A path with another place waiting behind its name. Useful directions.|
N~The sequence of landmarks gives us a clear route to follow.|
N~Worth checking supplies before taking the longer stretch.|
S~A little certainty makes a new island feel less daunting.|
N~We can plan the return while the directions are clear.|
S~The local guide neatly supplies the next two settings.|
S~A few small words can make a strange road less strange.|
N~Route sequence recorded. Now check the terrain.|
S~The way through has acquired two familiar-sounding names.|
N~Clear directions are always a welcome bit of hospitality.|
S~I wonder which part of that route the boy likes most.
''')
add('six_night_sky','SixIsland_Text_SkyAtNightIsFantastic',
    "A hiker praises the night sky far from city lights.",'''
S~The stars get more room when the streetlights stop interrupting.|
S~Reduced artificial light can reveal much more of the night sky.|
S~Worth finding a safe place to sit and look.|
S~A quiet dark sky sounds like a lovely reason to stay awhile.|
S~A warm drink and a patient evening would fit that view.|
S~The island offers a grand performance with no stage lights required.|
S~Darkness can be generous when it is not hiding a staircase.|
S~Less glare, better observations. Excellent conditions.|
S~The sky has kept far more little lights than the town allowed us to see.|
S~A view does not have to be bright to feel inviting.|
S~I wonder which stars the hiker looks for first.
''')
add('six_nature_history','SixIsland_House_Text_GoodPlaceForNatureAndHistory',
    "An older local assumes young people find the island dull but recommends nature and history.",'''
S~Nature and history sound like quite a full afternoon already.|
N~Age is a weak predictor of whether those subjects will interest a visitor.|
N~Plenty to see. Quiet is not the same as empty.|
S~I like a place that lets you notice things without hurrying.|
S~A slow day somewhere interesting can be exactly what the journey needs.|
S~The host dismisses the program before revealing two excellent acts.|
S~An old place need not become loud to be worth visiting.|
S~Field observations and old structures. A strong itinerary.|
S~A little island holding old stories beside growing things.|
N~He could trust visitors to have more varied tastes than that.|
S~I wonder which local detail he would show somebody curious first.
''')
add('six_agatha_example','SixIsland_Mart_Text_AgathaOldestEverEliteFourMember',
    "An older woman finds inspiration in Agatha\'s long and formidable career.",'''
S~A good reminder that a birthday does not cancel an interesting next plan.|
S~A visible older role model can challenge assumptions about later-life capability.|
S~Good for her. Keep learning at a pace that suits her.|
S~It is lovely hearing somebody's future get larger instead of smaller.|
S~A life with partners you enjoy can keep giving you reasons to begin things.|
S~The formidable elder has become an encouraging example far beyond her own room.|
S~A long life still allowed its sharp edges and new ambitions.|
N~Age is one variable, not a complete capability specification.|
S~An old branch can still put out leaves nobody expected.|
S~An inspiration that leaves her feeling more possible. Good.|
S~I wonder what bigger thing she is thinking of trying next.
''')
add('six_letter','SixIsland_Mart_Text_ShouldBuyMailAndWriteLetter',
    "A shopper considers buying Mail to write to someone.",'''
S~A little blank paper is about to become something meant for one person.|
S~A written message can preserve thoughts more carefully than an improvised conversation.|
S~Good idea if there is something worth saying. Keep it honest.|
S~I like the quiet moment before someone chooses the first word.|
S~A simple note can make a distant ordinary day much warmer.|
S~The stationery counter has acquired the beginning of a personal story.|
S~A small page can carry a surprising amount of unsaid time.|
N~A clear purpose makes the purchase easy. Writing is the next task.|
S~A little voice looking for a place to wait in someone else's hands.|
S~Thoughtful mail always has more character than an expensive envelope alone.|
S~I wonder which thing the shopper most wants him to know.
''')
add('six_long_search','SixIsland_PokemonCenter_1F_Text_SomethingHiddenOnThisIsland',
    "A ruins seeker revises ten years to twenty and still feels the island hides something.",'''
U~Twenty years is a very long relationship with a suspicious patch of map.|
N~The duration shows commitment, not proof of the hidden thing's existence.|
N~Hope the search leaves room for an ordinary good life too.|
N~It must be hard to separate a long hope from what you actually know.|
N~A careful next step matters more than adding another year of wandering.|
N~The mystery has acquired a remarkably long-running sole investigator.|
S~A place can keep somebody curious for longer than they intended.|
N~Long search history. I would review the evidence and failed approaches.|
S~An old question has become one of the island's familiar footsteps.|
N~He sounds certain of the feeling, less certain of the facts.|
N~I wonder which actual clue has kept him looking all this time.
''')
add('six_trade_items','SixIsland_PokemonCenter_1F_Text_SomeMonsEvolveByTradingWithHeldItem',
    "An older trainer explains that certain evolutions need both trading and a held item.",'''
N~A change with a very particular packing list. Worth checking before the handoff.|
N~Some triggers require multiple conditions rather than the trade alone.|
N~Know the requirements before asking a friend to help.|
N~It is easy to miss one small condition in a complicated change.|
N~A little preparation saves disappointment for both trainers.|
N~The transformation scene has added a specific prop requirement.|
S~Some futures need a meeting and the right small thing carried into it.|
S~Compound condition. Both inputs have to be present.|
S~A journey can depend on what travels quietly beside the traveler.|
N~Good detail to share before someone assumes every trade works the same way.|
N~I wonder which species taught the trainer to check the held item.
''')
add('six_rival_leaving','SixIsland_PokemonCenter_1F_Text_RivalImpossibleToGetAllMonsAroundHere',
    "The rival accepts that the islands cannot complete the Pokedex and chooses to collect at his pace, with a final jab.",'''
N~A sensible plan has nearly made it through an entire rival speech without an elbow attached.|
N~He recognizes geographic limits and proposes sustainable progress. The comparison with us is unnecessary.|
N~His pace is his. Ours is ours. Good to hear he is not forcing the whole job.|
N~There is a little relief in the decision beneath all the familiar bravado.|
N~A routine that cares for the team is better than a desperate collection sprint.|
M~The rival discovers moderation and hurriedly disguises it as another declaration of superiority.|
N~A quieter plan is allowed to be wise without being everybody else's defeat.|
N~Sampling limits recognized, objective revised. Sound adjustment under noisy packaging.|
S~The map has become large enough to let the next step be small again.|
N~He could leave the insult behind and keep the useful part.|
N~I wonder what partner he will spend time training when he gets home.
''')
add('sapphire_theft','SixIsland_DottedHole_SapphireRoom_Text_SellToTeamRocketTellPassword',
    "The scientist steals the Sapphire, plans to sell it, and gives a warehouse password before leaving.",'''
A~Knowing where a stone is does not make stealing it clever or fair. At least he spilled a lead.|
N~He asserts ownership without a valid basis, then supplies actionable information about the warehouse.|
A~Remember the password. His request for a good opinion can wait until he earns one.|
N~It is ugly to hear someone narrate taking the thing we worked to reach.|
N~A useful lead does not make his theft a favor. We should follow it prepared.|
N~The opportunist exits with a stolen prop and the extraordinary request that the audience review him kindly.|
A~A pocket can hold a gem without holding a decent reason for taking it.|
N~Resource stolen, recovery route partially disclosed. Record the credential accurately.|
N~A blue little thing has been pulled into a very small-minded plan.|
A~He wants the profitable part of being cruel without the uncomfortable part of being judged.|
N~I wonder whether the buyers are as trustworthy as he imagines.
''')
add('ruin_blocked_scientist','SixIsland_RuinValley_Text_CantFigureOutHowToGetInside',
    "The scientist admits he cannot enter the ruins.",'''
N~A closed door has found somebody very determined to keep frowning at it.|
N~The access method remains unknown. Closer observation is a better next step than force.|
N~Look for the mechanism before trying to break anything.|
N~It is frustrating to stand so close to something you came to understand.|
N~A patient look can save the place from a frustrated decision.|
N~The eager explorer has reached a rather literal limit in the opening chapter.|
N~A door is allowed to remain a question for a while.|
N~Unknown interface. Inspect the markings before choosing an input.|
N~Old stone keeping its answer behind a familiar-looking shape.|
N~He could ask for help without needing to look certain first.|
N~I wonder which approaches he has already tried.
''')
add('heracross_song','SixIsland_WaterPath_House1_Text_LoveItNeedItHeracross',
    "The Heracross enthusiast sings her devotion when no measuring attempt begins.",'''
S~A remarkably specific little anthem. Heracross has a committed publicity department.|
S~A narrow interest can inspire close attention, though size should not eclipse individual care.|
N~Nothing wrong with a favorite. Keep the actual partner comfortable.|
S~It is sweet to hear enthusiasm that is not trying to sound sophisticated.|
S~She has made a whole cheerful moment out of one Pokemon she loves.|
M~The local Heracross society opens with its enthusiastic national song.|
S~A strange small joy, worn without embarrassment. I respect that.|
S~Clear subject expertise, strong user enthusiasm. Unusually musical introduction.|
S~A little shining creature has filled her room with a tune.|
S~She knows her theme and commits to it completely.|
S~I wonder whether the tune changes when a particularly big one visits.
''')
add('heracross_record','SixIsland_WaterPath_House1_Text_WantToSeeBiggerOne',
    "After rewarding a record Heracross, the enthusiast immediately hopes to see a larger one.",'''
M~A record falls, and her imagination grows a bigger horn at once.|
N~The record has advanced. The next target remains optional, not a measure of every future catch.|
N~Good result. No need to make the partner keep proving its size.|
S~Her joy is obvious, even if the next wish arrives very quickly.|
N~We can enjoy the good catch before making the day another search.|
M~The reigning champion receives applause and an immediate request for a larger sequel.|
N~A living creature should be more than a mark somebody wants to move up a wall.|
N~Benchmark updated. Further improvement is not compulsory.|
S~A little number has made her picture something even larger.|
N~Enthusiasm is charming. Knowing when to be pleased with what is here helps too.|
S~I wonder whether she keeps a drawing of each new record holder.
''')
add('heracross_tie','SixIsland_WaterPath_House1_Text_ItsXSizeSameAsBefore',
    "The measured Heracross equals the existing record.",'''
N~An equally impressive bug has somehow produced a disappointed noise. Tough judging room.|
N~The measurement matches the previous record rather than exceeding it.|
N~Still a fine partner. A tie is not a flaw.|
N~It seems unfair for matching something remarkable to sound like a failure.|
N~A good outing does not need an ever-larger ruler mark.|
M~The exclusive size competition has found a perfectly matched rival and declined to celebrate.|
N~A little living sameness can still be interesting.|
N~Repeated measurement at the benchmark. Useful, even without a new maximum.|
N~The same height can hold an entirely different little life.|
N~She might notice more if she looked beyond the figure on the page.|
N~I wonder how different the two partners are in every way she did not measure.
''')
add('heracross_smaller','SixIsland_WaterPath_House1_Text_ItsXSizeYSizeWasBiggest',
    "The enthusiast dismisses the Heracross as smaller than the recorded best.",'''
N~A shorter horn is still attached to a whole worthy Pokemon. The ruler can relax.|
N~The size comparison establishes only that this one is below the current maximum.|
N~No record. No reason to make the partner feel unwanted.|
N~I would hate for the little one to hear only disappointment in the greeting.|
N~Care should not depend on being the biggest arrival in the room.|
N~The critic has confused a narrow contest result with a complete character review.|
N~A living thing does not need a superlative before it deserves warmth.|
N~Below benchmark is a measurement, not a defect report.|
N~Smallness has not made the life inside any less complete.|
N~A real eye for a creature should notice something besides the one feature it prefers.|
N~I wonder what this one does that would make its own trainer smile.
''')
add('heracross_wrong_species','SixIsland_WaterPath_House1_Text_ThisWontDo',
    "The enthusiast rejects another species and describes the Heracross appearance she expects.",'''
N~Wrong contest, perfectly good Pokemon. It can leave without adopting the required horn.|
N~The selected species does not qualify for this particular comparison.|
N~That partner is fine as it is. Select the right one if we want the measurement.|
F~An awkward mistake does not need quite that much dramatic disappointment.|
N~We can correct the selection without making the Pokemon part of the joke.|
M~The exclusive casting call insists on a horn and an exceptionally specific silhouette.|
N~An unfamiliar shape has been told it is wrong for being itself. Unhelpful.|
N~Species mismatch detected. No need to insult the input.|
N~The narrow doorway belongs to the contest, not to the world's idea of worth.|
N~She knows what she asked for. A kinder refusal would still work.|
N~I wonder whether she notices the difference between excitement and making another partner feel small.
''')
add('heracross_no_room','SixIsland_WaterPath_House1_Text_YourBagIsFull',
    "The Heracross reward cannot fit in our bag.",'''
N~The measuring was ready. The bag was the part that failed the size test.|
N~The reward transfer did not complete because of capacity.|
N~Make room before another handoff. No need to hurry the partner around.|
F~An awkward little finish to something she was so excited about.|
N~A moment of sorting can spare everyone another failed exchange.|
N~The size competition has been unexpectedly defeated by a different small container.|
N~A crowded bag turning somebody's enthusiasm into a sigh.|
N~Capacity check failed. Keep the reward separate from the completed measurement.|
N~A little offered thing has no place left to sit in our pockets.|
N~We should manage our own belongings before making her repeat the offer.|
N~I wonder what has been taking up that last bit of space.
''')
add('neighbor_height','SixIsland_WaterPath_House2_Text_MyNeighborMeasuredMe',
    "A neighbor reports his exact height because the Heracross enthusiast measured him too.",'''
M~The measuring project has escaped the insect category and reached the neighbors.|
M~A precise figure, though the circumstances of the measurement are more memorable than the number.|
N~Hope he agreed to be measured. A hobby still needs boundaries.|
F~I would be surprised to become part of the local record book that way.|
N~At least he seems willing to tell the story without much annoyance.|
M~The nearby measurement office has expanded its services with remarkable geographic efficiency.|
M~A small town is a dangerous place to stand near an enthusiast with a ruler.|
N~An exact reported value. I would still ask about the method and repeatability.|
N~A familiar person reduced, briefly, to a very specific mark on the wall.|
M~An unexpected form of neighborhood participation. At least he knows his number now.|
S~I wonder whether the neighbor gets asked to confirm the measuring equipment regularly.
''')
add('seven_origin_story','SevenIsland_Text_IslandsMadeInSevenDays',
    "An elder contrasts the island-count explanation with a legend of creation in seven days.",'''
S~Seven islands, seven days, and at least two opinions waiting by the same sign.|
N~He offers a traditional naming account. A legend is not the same as verified geological history.|
N~Interesting story. Let it stay a story until there is evidence for more.|
S~I like hearing the older meaning a familiar name has for someone.|
S~A name can carry several generations' different ways of belonging to a place.|
S~The island's title receives competing editorial notes from two generations.|
S~A little old tale still tucked inside an ordinary name.|
N~Alternative etymology reported. Needs a historical source for confirmation.|
S~Seven pieces of land, held together by a story as well as water.|
S~The elder wants the old account remembered, even if the young use a simpler one.|
S~I wonder who first told him that version.
''')
add('seven_natural_trails','SevenIsland_Text_IslandVirtuallyUntouched',
    "A local warns that the island\'s largely natural state makes hiking harder.",'''
N~A beautiful place can still decline to provide convenient stairs. We should dress accordingly.|
N~Limited development changes accessibility and route conditions. Preparation matters.|
N~Watch the ground. An open view does not promise an easy trail.|
S~I like that the wildness is described honestly, without pretending it is effortless.|
N~Water, time, and a way back belong in the plan.|
S~The setting has retained its own design rather than accepting the visitor's preferred floor plan.|
N~A place does not have to be easy for us to be worth leaving intact.|
N~Low infrastructure, higher navigation demand. Check equipment.|
S~The island still lets its paths grow in their own handwriting.|
N~Good guidance tells you about the difficult part as well as the lovely view.|
S~I wonder which section locals find most rewarding to walk slowly.
''')
add('seven_retired_battler','SevenIsland_House_Room1_Text_OnlyEnjoymentWatchingBattles',
    "The retired battler remembers traveling widely and now enjoys watching matches.",'''
S~A long road has become a comfortable chair with a very lively view.|
S~A continuing interest can change form as a person's circumstances change.|
S~Good to keep enjoying the thing without needing to do it the old way.|
S~I would like to hear one of the journeys behind that quiet introduction.|
S~A shared match can make an ordinary afternoon feel full again.|
S~The former performer has taken a well-informed seat in the audience.|
S~A life does not have to stop being interesting when its footsteps slow down.|
N~Participation mode changed. The experience and interest remain useful.|
S~An old path still moves when someone else's battle brings it to mind.|
S~It is nice when enthusiasm lasts beyond the role everyone once knew.|
S~I wonder which match from those traveling years stays clearest in memory.
''')
add('seven_pikachu_nature','SevenIsland_Mart_Text_MonHavePersonalitiesOfTheirOwn',
    "A customer links Pikachu\'s hasty personality with its Speed.",'''
S~A little personality that apparently arrives before the rest of the room is ready.|
N~Individual nature can influence growth, though the partner is more than that mechanical effect.|
N~Learn the Pokemon's habits. A stat is not its whole character.|
S~It is lovely to hear someone notice a familiar partner as an individual.|
N~A fast little companion still needs a calm routine and proper rest.|
S~The compact biography includes both temperament and a remarkably brisk entrance.|
S~A small creature with its own way of occupying the afternoon.|
N~Individual parameters matter. They still do not replace observing the actual partner.|
S~A little hurry has learned a yellow shape.|
S~Personality is often what makes a familiar companion recognizable in a crowd.|
S~I wonder which tiny impatient habit makes the customer smile most.
''')
add('seven_ruins_ready','SevenIsland_Mart_Text_PreparationsCompleteForRuins',
    "A shopper has finished preparing to explore the ruins.",'''
S~A full checklist is a very satisfying kind of departure music.|
N~Preparation reduces avoidable uncertainty, though the site still requires careful attention.|
N~Good. Check the route back as well as the supplies going in.|
S~It is nice to hear excitement with a little practical steadiness under it.|
N~A good outing starts before the first interesting stone.|
S~The expedition has reached the point where the props are ready and the road can begin.|
S~A bag packed for questions instead of emergencies alone.|
S~Prepared kit, clear destination. Strong start.|
S~The little things are gathered so the larger old place can be met calmly.|
N~Planning can be part of enjoying something, not just the boring delay before it.|
S~I wonder which part of the ruins the shopper most wants to see.
''')
add('seven_fishing_tour','SevenIsland_Mart_Text_NeedToFishOnSevenIsland',
    "An angler buys supplies for the last island of a Sevii fishing tour.",'''
S~The final shore in a very splashy travel journal. Good reason to stock up.|
S~A comparative island tour could reveal interesting differences in catches and conditions.|
N~Prepare for this water, not just the six places before it.|
S~The last planned stop can feel exciting and a little sad at once.|
N~Leave time to enjoy the day instead of turning the last entry into a rush.|
S~The extensive angling series approaches its final scheduled episode.|
S~A collection of quiet places, tied together by one patient habit.|
N~Final sampling site pending. Check the consumables before departure.|
S~Seven shores gathered along one little line cast into the sea.|
S~The supplies are practical; the personal project gives them character.|
S~I wonder which island has been the angler's favorite so far.
''')
add('seven_connections','SevenIsland_PokemonCenter_1F_Text_EventsDependingOnConnections',
    "A visitor hints that different connections lead to different island experiences, leaving discovery to us.",'''
N~A helpful-sounding mystery with all the directions carefully removed.|
N~The claim is broad and offers no particular event or method we can verify yet.|
N~We can explore without pretending we know exactly what the hint means.|
S~It is nice to leave a little room for meetings we could not plan.|
N~A small conversation can matter without being the start of a grand secret.|
M~The local oracle has provided an intriguing premise and declined to write the next scene.|
S~A life does change through the people it happens to touch. No prophecy needed.|
N~Vague dependency statement. We will need actual observations.|
S~Some roads are made by the voices that meet along them.|
N~An invitation to be curious is pleasant, even without an answer attached.|
S~I wonder which connection the visitor is remembering while saying that.
''')
add('seven_ferries','SevenIsland_PokemonCenter_1F_Text_DidYouRideSeagallopHere',
    "A traveler marvels at the many fast Seagallop ferries without knowing all their destinations.",'''
U~A whole fleet of fast boats! Our little crossing was one page of a much larger timetable.|
N~The number and routes are reported imperfectly. The traveler admits not knowing the full network.|
N~Use the actual schedule before choosing a boat. Admiration is not a map.|
S~It is strange realizing how many other journeys are passing just beyond your own.|
N~A reliable ferry can make distant places part of an ordinary day.|
S~The local transport system has a much larger recurring cast than our own ticket revealed.|
S~Many little moving rooms keeping the islands from feeling quite so separate.|
S~A coordinated fleet is serious infrastructure. I would love to see the route diagram.|
S~The water holds more paths than the shore lets us see at once.|
N~A useful reminder to ask the crew instead of guessing where every ship goes.|
S~I wonder which route the traveler would take simply to see the view.
''')
add('seven_tower_advice','SevenIsland_PokemonCenter_1F_Text_CheckOutTrainerTower',
    "A visitor recommends Trainer Tower to confident trainers.",'''
N~A tall place for testing a big feeling. Confidence should bring a supply plan.|
N~A specialized challenge may be useful, but confidence alone does not establish readiness.|
N~Check the team before trying it. Nobody needs to prove anything while tired.|
N~I would like to know the rules before deciding how brave I feel.|
N~A good challenge is one we can leave with the partners still cared for.|
N~The competitive itinerary has acquired an optional vertical chapter.|
N~A tower is a very visible way to ask whether someone wants more battles.|
N~Need specifications and entry rules before committing resources.|
N~A high doorway waiting for a particular kind of determined footstep.|
N~A recommendation can stay an option. We do not need to answer it immediately.|
N~I wonder which part of the Tower keeps people coming back.
''')
add('seven_training_partners','SevenIsland_SevaultCanyon_Text_BrunoTrainedWithBrawly',
    "A martial artist explains that even Bruno trained with Brawly and values partnership as well as solo practice.",'''
S~Strong people still learn from someone standing beside them. Good to hear.|
S~A training partner can provide feedback and challenges unavailable in solitary practice.|
S~Work alone when it helps. Ask someone else when that helps more.|
S~It is reassuring to hear help spoken of as part of strength.|
N~A good partner notices when the effort needs a rest as well as a push.|
S~The formidable fighter's biography includes a valuable second voice in the rehearsal room.|
S~Ambition need not make a person lonely by design.|
S~External feedback improves testing. A trusted partner is a very useful resource.|
S~Two paths can help each other find steadier ground.|
S~A good example without making either way of training the only respectable one.|
S~I wonder what Bruno and Brawly each learned from the other's approach.
''')
add('chansey_dance_repeat','SevenIsland_SevaultCanyon_House_Text_ChanseyDanceJoinIn',
    "On a return interaction after dancing, the host cheerfully repeats the invitation.",'''
S~The dance has survived our first performance and is requesting another audience. Brave little dance.|
S~A familiar shared routine can be enjoyable without needing a new outcome each time.|
S~Good fun if everyone wants to join. No need to rush the day.|
F~It is easier the second time when you already know nobody expects perfection.|
S~A happy little house can be a welcome rest along the road.|
S~The local troupe retains its signature number with commendable enthusiasm.|
S~A strange small ritual, kept warm by repetition.|
S~Repeatable recreational protocol. Much more inviting than that description sounds.|
S~A few familiar steps holding a little brightness in the room.|
S~The confidence to enjoy a silly routine is quite charming.|
S~I wonder whether every visitor adds one slightly different mistake to the dance.
''')
add('chansey_dance_no','SevenIsland_SevaultCanyon_House_Text_ComeOnDance',
    "The host keeps encouraging us after we decline the dance.",'''
N~The enthusiasm can stay. Our feet are still allowed to say no.|
N~An invitation should remain voluntary after the answer.|
N~Not now. He can keep enjoying it without recruiting us.|
F~Being urged again makes it harder to stay comfortable about an honest no.|
N~A tired traveler may prefer a seat to a routine, however cheerful.|
N~The eager director has missed the part where the guest declined the role.|
N~A harmless dance can become less harmless to the mood when it will not accept a refusal.|
N~Request declined. Repeating it does not change consent.|
N~A happy room should still leave a quiet corner for somebody who will not dance.|
N~The welcome would be warmer if it left room for different ways to enjoy the visit.|
N~I wonder whether he knows some visitors are happiest simply watching.
''')
add('chansey_dance_done','SevenIsland_SevaultCanyon_House_Text_YoureAllChipperNow',
    "After the dance and recovery, the host happily notices our renewed energy.",'''
S~A strange little dance has left the day lighter. Excellent use of feet.|
S~The shared activity has concluded with practical recovery and a cheerful acknowledgment.|
S~Good rest, unexpected method. The team looks better.|
F~I may have been embarrassed, but it is difficult not to smile now.|
S~A little play and a little care make a good stop on a long route.|
S~The curious performance earns its happy closing line through a genuinely useful result.|
S~A small silly thing can make a serious tiredness feel less absolute.|
S~Recreation and recovery in one routine. Efficiently delightful.|
S~The room has put a little spring back where the road had taken it.|
S~It is lovely when the odd local custom turns out to be welcoming.|
S~I wonder how the host first decided this dance belonged with this place.
''')
add('green_jaclyn','SixIsland_GreenPath_Text_JaclynPostBattle',
    "Jaclyn needs to focus so she can Teleport home.",'''
N~A wandering thought is inconvenient when the rest of you plans to follow it.|
N~A transport technique requiring concentration should wait until she feels steady.|
N~Pause and get focused. No need to risk an uncertain jump.|
N~I understand the worry of having your mind drift at the wrong moment.|
N~A quiet rest might help before attempting the way home.|
N~The next scene depends on its performer remembering the correct destination.|
N~A scattered mind is allowed to ask the body to wait a little.|
N~Destination certainty first. The operation can follow.|
N~The thought of home should be clear before the feet try to arrive there.|
N~She has noticed the problem. That is better than pretending confidence.|
N~I wonder what familiar detail of home helps her concentrate.
''')
add('outcast_rocket','SixIsland_OutcastIsland_Text_RocketPostBattle',
    "The defeated Rocket asks if we have seen any rare Pokemon.",'''
N~That is not a sightseeing report I feel eager to provide him.|
N~Given his affiliation, sharing locations could expose the Pokemon to harm.|
A~No leads for him. The rare partners can stay out of his reach.|
N~I dislike how casually he returns to looking for something to take.|
N~The residents here deserve more privacy than his question does.|
N~The defeated antagonist resumes his shopping inquiry with remarkable persistence.|
N~A curious question can be an unkind tool in the wrong mouth.|
N~Sensitive habitat information. Do not distribute to a known risk.|
N~Some small lives are safer remaining outside his map.|
N~He has not given us any reason to help with that search.|
N~I wonder how many travelers have answered without thinking where the information goes.
''')
add('outcast_tylor','SixIsland_OutcastIsland_Text_TylorPostBattle',
    "Tylor feels he cannot go home without catching something.",'''
N~Home is not going to inspect the bag for proof the day was worthwhile.|
N~A self-imposed catch requirement can turn a manageable outing into unnecessary risk.|
N~He can go home tired and empty-handed. Better than pushing too far.|
N~It is hard when a plan becomes a rule you feel ashamed to change.|
N~A safe return can be the good outcome even without a new partner.|
N~The traveler has mistaken the intended ending for a binding contract.|
N~An unfinished list is lighter than an exhausted person.|
N~Stop conditions should include fatigue, not just goal completion.|
N~A road home should remain open even when the water gives nothing back.|
N~He does not owe anyone a trophy from every afternoon outside.|
N~I wonder what he would tell a friend in the same situation.
''')
add('outcast_mymo','SixIsland_OutcastIsland_Text_MymoPostBattle',
    "Mymo is exhausted despite reaching only the halfway point.",'''
N~Half the route has used more than half the person. Time to revise the plan.|
N~Remaining distance should be compared with actual stamina, not the original schedule.|
N~Rest or turn back while there is enough strength to do it safely.|
N~It sounds daunting to see the rest of the way while already spent.|
N~A shorter day is better than making the last stretch an emergency.|
N~The itinerary has become substantially more optimistic than its traveler.|
N~A halfway mark is useful precisely because it lets you reconsider.|
N~Energy budget insufficient for the current plan. Adjust now.|
N~The distance ahead should not drown out what the tired body is saying.|
N~There is nothing stylish about pretending exhaustion is imaginary.|
N~I wonder whether there is a safe shore nearby for a proper stop.
''')
add('outcast_nicole','SixIsland_OutcastIsland_Text_NicolePostBattle',
    "Nicole found the farther island uninteresting and asks whether we are heading there.",'''
N~Her idea of interesting may not be ours. Still useful to hear the trip was uneventful.|
N~The evaluation is subjective. A quiet site can still merit observation.|
N~We can decide after checking the route and why we want to go.|
S~Sometimes a place becomes interesting through the little things someone else overlooked.|
N~A long trip should have a reason beyond proving a stranger wrong.|
N~The destination has received a brief unfavorable notice from one returning critic.|
S~An empty-looking island may still have quite a lot of quiet in it.|
N~Single-user report. Check against our own objective before accepting the conclusion.|
S~A small shore can be enough when the point is looking closely.|
N~An honest opinion is welcome when it stays an opinion.|
S~I wonder what Nicole had hoped to find there.
''')
add('outcast_ava','SixIsland_OutcastIsland_Text_AvaPostBattle',
    "Ava prefers swimming in the sea to a pool.",'''
S~The sea has a much larger ceiling and a considerably less tidy edge. I see the appeal.|
N~Open water offers variety along with conditions that require more judgment.|
N~Her preference. Keep the current in mind while enjoying it.|
S~It must be lovely knowing a stretch of water well enough to feel at home.|
N~A beautiful swim still needs energy left for the way back.|
S~The swimmer favors the grand natural venue over the controlled rehearsal room.|
S~A pool ends where the sea keeps beginning. A convincing difference.|
N~Variable environment, richer experience, greater preparation needs.|
S~The wide water refuses to hold the same shape around every stroke.|
S~A strong preference can still leave room to respect the limits of the place.|
S~I wonder which little stretch of coast made her decide that.
''')
add('outcast_geb','SixIsland_OutcastIsland_Text_GebPostBattle',
    "Geb holds onto his sister because the water is too deep to stand.",'''
N~Then staying together is not optional play. He needs reliable support.|
N~Inability to stand changes the immediate risk. Adequate flotation matters.|
N~Get him somewhere safe and shallow before asking for anything else.|
N~That sounds frightening if she moves faster than he can follow.|
N~A safe outing should fit the smaller swimmer too.|
N~The sibling partnership has a very practical meaning in deep water.|
N~A familiar hand is important. It should not be the only safety plan.|
N~Insufficient footing. Add proper flotation or change location.|
N~The water has become too large for his own feet to answer.|
N~He should be able to enjoy the day without needing to cling for safety.|
N~I wonder whether his sister knows how much he depends on that hold.
''')
add('pattern_bethany','SixIsland_PatternBush_Text_BethanyPostBattle',
    "Bethany compares raising Pokemon lovingly with a mother raising a child.",'''
S~A useful comparison when it means patience rather than just telling the little one what to do.|
N~Consistent care is essential, though family experience varies between people.|
S~Look after the partners because they depend on us. Simple enough.|
S~A familiar kind of kindness can be something you choose to pass on.|
S~Daily food, rest, and patience say more than one grand promise of love.|
S~The lesson asks the traveler to become a source of the care they once received.|
S~A small safe life grows from many ordinary gentle days.|
N~Stable supportive environment. A good foundation for any developing partner.|
S~A shelter once given can become something the hands learn to offer.|
N~A kind principle, without needing everyone's home story to be the same.|
S~I wonder which little act of care Bethany most remembers.
''')
add('pattern_allison','SixIsland_PatternBush_Text_AllisonPostBattle',
    "Allison clarifies that she wants responsible Pokemon care rather than no catching.",'''
N~Catch thoughtfully, care properly. A much clearer request than a blanket argument.|
N~She distinguishes acquiring partners from meeting the responsibilities that follow.|
N~Fair point. The job starts when the ball stops moving.|
S~It is reassuring that the concern leaves room for a good way to do things.|
N~A safe home and a workable routine should come before another catch.|
N~The critic supplies a constructive revision instead of canceling the whole premise.|
N~Wanting a creature is the smallest part of making room for its life.|
N~Acquisition and ongoing maintenance are different tasks. Both need planning.|
N~A closed ball should open onto something kinder than an empty promise.|
N~Clear standards are better than assuming every trainer is careless.|
N~I wonder which responsibility she most often sees people forget.
''')
add('pattern_garret','SixIsland_PatternBush_Text_GarretPostBattle',
    "Garret points us to the Heracross measurer near Pattern Bush.",'''
S~A specialist with a very particular ruler. The local bug news travels well.|
N~A nearby measuring service can provide consistent comparison if the method is reliable.|
N~Worth a visit if the partner is comfortable being handled.|
S~It is nice that such a small interest can have its own local expert.|
N~An odd little hobby can still be kind when the Pokemon's comfort stays first.|
S~The field expedition receives directions to an unusually exclusive review panel.|
S~A little enthusiasm has become a landmark people can point toward.|
S~Specialized measurement station! I would ask how the scale is calibrated.|
S~The path has a place for someone who notices the small differences in a horn.|
N~A clear recommendation is useful. A record should remain a game, not a judgment of the partner.|
S~I wonder whether Garret has brought a Heracross to be measured.
''')
add('pattern_jonah','SixIsland_PatternBush_Text_JonahPostBattle',
    "Jonah plays with the possible sounds and meanings of the word appeal.",'''
M~An orange peel ringing like a bell is exactly the kind of thought I wanted from this walk.|
M~Similar sounds can suggest unrelated meanings. English enjoys being inconvenient.|
N~A harmless puzzle. Better than another threat about losing.|
S~I like somebody noticing how strange an ordinary word can become.|
M~If the orange starts ringing, I am taking it out of the fruit bowl.|
S~A roadside linguist has discovered that language will gladly trip over its own shoes.|
M~Words are very old things with surprisingly loose floorboards.|
N~Sound similarity does not imply shared function. Still an entertaining test.|
S~A familiar little word has opened its coat to reveal two unrelated objects.|
S~A playful question can make a dull stretch much more memorable.|
S~I wonder whether he has been turning that word around all afternoon.
''')
add('pattern_vance','SixIsland_PatternBush_Text_VancePostBattle',
    "Vance plans to bring his younger brother to Pattern Bush.",'''
S~A good place becomes even better when you know someone else would love seeing it.|
S~A shared outing can introduce a younger child to a habitat with useful guidance.|
N~Good plan if he keeps the pace safe for the younger one.|
S~It is lovely to picture someone enjoying a place before they have even arrived.|
N~Bring enough water and time for little legs and long questions.|
S~The field trip receives an enthusiastic advance booking for a smaller guest.|
S~A familiar path can become new again through someone else's first look.|
N~Adapt the route for the least experienced participant.|
S~One person's wonder is being kept ready for another pair of eyes.|
S~A thoughtful invitation is better than simply buying a souvenir.|
S~I wonder which little part Vance most wants to point out first.
''')
add('pattern_nash','SixIsland_PatternBush_Text_NashPostBattle',
    "Nash compares the ground patterns with his grandfather\'s clothes.",'''
S~The mysterious forest floor has accidentally borrowed Grandfather's wardrobe.|
N~An association can help notice a pattern without establishing how it formed.|
N~Good eye. The resemblance is worth remembering, even if it explains nothing yet.|
S~I like how a strange place can suddenly connect to something familiar at home.|
S~A small family memory can make the unknown feel less distant.|
S~The ancient-looking design receives an unexpected domestic costume reference.|
S~A familiar shape hiding inside something unfamiliar. A pleasant kind of strange.|
N~Pattern recognition triggered. Now compare the actual structures.|
S~The ground has worn a little echo of somebody's old coat.|
S~A repeating design is a repeating design, whether it is on cloth or beneath the grass.|
S~I wonder whether his grandfather would see the resemblance too.
''')
add('pattern_cordell','SixIsland_PatternBush_Text_CordellPostBattle',
    "Cordell admires our hat and asks us to give it to him.",'''
M~The hat has attracted another very ambitious compliment. My head would like to keep its roof.|
N~Admiration does not require transferring ownership of the item.|
N~Nice that he likes it. We are allowed to keep our own hat.|
F~I would find that request much harder to answer than a simple compliment.|
N~A practical bit of shade is still something the traveler needs.|
M~The costume review unexpectedly becomes a request to acquire the wardrobe.|
N~A small personal belonging need not leave every time somebody asks brightly.|
N~Property request optional. No technical need to comply.|
N~The shade over one pair of eyes need not become someone else's souvenir.|
M~He has good taste. His assumption about the gift policy needs work.|
S~I wonder which hat he would choose if he went looking for his own.
''')
add('pattern_dalia','SixIsland_PatternBush_Text_DaliaPostBattle',
    "Dalia enthusiastically describes a deep breath of fresh air.",'''
S~A very simple local attraction, with unlimited space around the ticket booth.|
N~A comfortable breath and a quiet pause can feel refreshing without becoming a cure-all.|
N~Fine to slow down a moment. No need to strain at breathing.|
S~I like the little pause when the place becomes something you can feel, not just see.|
S~A quiet rest in clean air can be a lovely part of the walk.|
S~The outdoors receives a recommendation based entirely on its most portable feature.|
S~A little room inside the day, made by stopping for a breath.|
N~Simple recovery pause. Much easier than overengineering the moment.|
S~The trees have left something gentle in the space between the words.|
S~An ordinary pleasure does not need a complicated explanation to be worth noticing.|
S~I wonder whether she has a favorite quiet spot for that pause.
''')
add('pattern_joana','SixIsland_PatternBush_Text_JoanaPostBattle',
    "Joana worries whether she is the only girl who loves collecting Bug Pokemon.",'''
S~She is certainly not the only person allowed to love a small many-legged neighbor.|
N~An interest is not restricted by gender. Absence of nearby examples does not imply she is alone.|
S~Like what she likes. The bugs do not require a membership category.|
S~It is hard when you cannot see someone like yourself enjoying the same thing.|
S~I hope she finds a friend who is just as excited to compare the tiny details.|
S~The specialist's genuine enthusiasm deserves a wider cast than she currently knows.|
S~An unusual joy is not a mistake just because it feels lonely.|
N~Population sample too small for that conclusion. Keep the interest.|
S~A little creature can be a perfectly good reason to step outside any expected shape.|
S~She gets to make the interest look like her, rather than copy someone else's idea.|
S~I wonder which Bug Pokemon she would show another interested girl first.
''')
add('pattern_riley','SixIsland_PatternBush_Text_RileyPostBattle',
    "Riley plans to observe the night sky from Pattern Bush.",'''
S~A day with a second view waiting after sunset. Good planning.|
S~An observation session benefits from checking conditions and choosing a safe position beforehand.|
N~Know the way back before the light goes. Then enjoy the sky.|
S~A quiet night outside sounds lovely with the right company or a little safe solitude.|
N~A warm layer and something to drink will make the wait kinder.|
S~The daytime explorer stays for the setting's less brightly lit second act.|
S~The ground has offered its patterns; the sky may have a few of its own.|
S~Excellent dark-site potential. I would check cloud cover and glare.|
S~A little patch of land waiting for the enormous ceiling to change.|
N~A deliberate evening plan is better than simply realizing it got dark.|
S~I wonder which part of the sky Riley hopes will be clearest tonight.
''')
add('pattern_marcy','SixIsland_PatternBush_Text_MarcyPostBattle',
    "Marcy dismisses a cut and suggests spit will cure it.",'''
N~A small cut deserves a cleaner plan than that.|
N~Saliva is not an appropriate substitute for cleaning a wound. Use clean water and proper care.|
N~Clean it properly. Small does not mean ignore it.|
N~I hope she is not brushing it off because somebody taught her to hide pain.|
N~A clean rinse and a proper dressing make more sense than a boast.|
N~The confident folk remedy could use a substantially better editor.|
N~A little care is not an embarrassing amount of care.|
N~Contamination is not a repair method. Clean the injury.|
N~A small hurt should not need to grow before it is allowed attention.|
N~Looking unbothered is less useful than actually looking after the cut.|
N~I wonder whether someone nearby has a proper first-aid kit.
''')
add('pattern_layton','SixIsland_PatternBush_Text_LaytonPostBattle',
    "Layton wonders why grass will not grow in certain patterned areas.",'''
S~A patch of missing grass can be a very interesting thing when the rest of the place is growing.|
S~Soil, disturbance, moisture, and other conditions could explain it. The pattern is worth recording.|
N~Look carefully before digging it up. The clue may be in the undisturbed shape.|
S~I like a question that begins with noticing something absent.|
N~A patient look can tell us more than an eager handful of soil.|
S~The curious observer has discovered a mystery written in negative space.|
S~A blank place can have more to say than the crowded part around it.|
S~Control samples! Compare the bare ground with the grass beside it.|
S~The growing things have left a little silence with edges.|
S~An unusual pattern deserves attention without a rushed dramatic explanation.|
S~I wonder whether the shape changes with the seasons.
''')
add('ruin_stanly','SixIsland_RuinValley_Text_StanlyPostBattle',
    "Stanly recommends considering the mysteries of the world every day.",'''
S~One mystery a day sounds manageable. Unless today's mystery is where yesterday went.|
S~Regular curiosity is an excellent habit, provided an unanswered question is allowed to stay open.|
N~A little thought before assuming we understand a place. Fair advice.|
S~I like that he makes room for wondering in an ordinary day.|
S~Something to turn over while dinner simmers. No need to solve it before eating.|
S~A daily appointment with the unexplained. I admire his scheduling.|
S~Some questions make good company even without an answer.|
S~A daily puzzle could keep a notebook wonderfully untidy.|
S~The world has no shortage of small doors that open inward.|
N~Curiosity is appealing. Pretending every hunch is a discovery is less so.|
S~He seems to find something worth noticing wherever he stops.
''')
add('ruin_foster','SixIsland_RuinValley_Text_FosterPostBattle',
    "Foster notes that most of the ruins scattered around Sevii are very old.",'''
U~The islands have been keeping old things in lots of different corners.|
S~Several sites could offer useful comparisons, though age alone does not establish a shared origin.|
N~Plenty to explore. We should leave the old stone where it belongs.|
S~It is strange to stand somewhere that has outlasted so many lives.|
N~A long history deserves more patience than a quick poke around.|
S~These islands have quite a back catalogue beneath the holiday scenery.|
S~Old walls do not need to be empty of meaning just because their builders are gone.|
S~Different sites, different construction methods. That could fill several notebooks.|
N~Time leaves its belongings scattered rather generously here.|
S~The islands wear their age in interesting places.|
S~I wonder what details would connect one ruin to another.
''')
add('ruin_larry','SixIsland_RuinValley_Text_LarryPostBattle',
    "Larry has found the ruins but cannot work out how to enter them.",'''
N~Finding the door and finding how it opens are apparently separate adventures.|
N~A visible entrance does not always reveal its mechanism. Careful observation comes first.|
N~No reason to force it before we understand the entrance.|
N~He sounds like he has been circling the same question for a while.|
N~We can take a proper look without turning the door into rubble.|
S~The building has supplied a setting and withheld its invitation.|
N~A closed door can be impressively stubborn without saying a word.|
S~Let's study the seams and markings before testing any theories.|
N~Some thresholds make visitors introduce themselves very slowly.|
N~Prying something open is rarely the most elegant first impression.|
S~I wonder which detail he has been walking past without noticing.
''')
add('ruin_daryl','SixIsland_RuinValley_Text_DarylPostBattle',
    "Daryl encourages the player to enjoy climbing.",'''
S~He makes going uphill sound like a party with unusually tired legs.|
S~The view and the exercise are convincing benefits. Sensible footing remains essential.|
N~Enjoy the climb. Keep enough strength for getting down.|
S~It feels good when the effort itself becomes part of the pleasure.|
S~A climb gives the packed lunch a remarkably appreciative audience.|
S~An enthusiastic recommendation from a man already above ground level.|
S~I appreciate a hobby that lets you pause and stare into the distance.|
S~Finding a stable route up is a satisfying problem in motion.|
N~The hill has not moved, yet reaching it changes the afternoon.|
S~He has the unmistakable glow of someone enjoying his own difficult idea.|
S~I like how a familiar landscape rearranges itself as we gain height.
''')
add('ruin_hector','SixIsland_RuinValley_Text_HectorPostBattle',
    "Hector cannot interpret the strange patterns engraved on the ruin door.",'''
U~The door has writing and neither of us has brought its reading glasses.|
S~The repeated marks may form a writing system. Recording their arrangement would be useful.|
N~Copy the markings accurately before guessing what they mean.|
N~Somebody meant those marks to be understood. That makes the silence stranger.|
N~A careful copy will last longer than trying to memorize the whole door.|
S~A message with its reader missing. The door has excellent dramatic restraint.|
S~Words can become ornaments when everyone forgets how to read them.|
S~Look for repeated groups. A pattern can give us a foothold without a translation.|
N~Stone remembers a message more patiently than people remember a language.|
N~Even an unreadable inscription deserves better than careless rubbing and scratches.|
S~I would compare the marks before deciding they are only decoration.
''')
add('water_rose','SixIsland_WaterPath_Text_RosePostBattle',
    "Rose would like to visit the woods but is frightened of Bug Pokemon.",'''
S~Wanting to visit the woods while fearing its tiny residents is a tricky invitation.|
N~Learning which species live there may make the uncertainty less intimidating.|
N~She can choose a short path with company. No need to prove anything.|
S~Wanting to go and feeling afraid can happen at the same time.|
S~A gentle first visit sounds better than marching her straight into a swarm.|
S~The woods have attracted a visitor who objects to part of the cast.|
S~I understand admiring a place from a very deliberate distance.|
S~Knowing where the bugs tend to gather might help her plan a comfortable route.|
S~The woods can wait while she makes acquaintance with its smaller neighbours.|
N~Someone laughing at her fear would make a poor walking companion.|
S~I wonder whether one calm encounter would change the way she sees them.
''')
add('water_edward','SixIsland_WaterPath_Text_EdwardPostBattle',
    "Edward prefers audiences not to see the effort behind a polished performance.",'''
S~So the trick is to work very hard at looking like you did not work very hard.|
S~Concealing preparation can shape an audience's experience. It does not diminish the practice.|
N~He put in the work. No shame in that, whether people see it or not.|
S~I understand wanting the finished thing to speak before the nerves do.|
S~A smooth meal has a very messy preparation table somewhere behind it.|
S~The illusion of effortlessness is a remarkably demanding profession.|
S~I suspect the hidden effort deserves a comfortable chair afterward.|
S~A clean result can hide a mountain of revisions. I know that mountain.|
N~Some kinds of grace have very tired feet beneath them.|
S~Polish works best when you cannot see someone anxiously checking it.|
S~Backstage tells one story; the audience sees the one he chose to share.
''')
add('water_samir','SixIsland_WaterPath_Text_SamirPostBattle',
    "Samir feels unable to escape the expectations attached to being a Swimmer.",'''
N~A swimsuit should not come with a permanent description of your whole personality.|
N~A trainer category is a useful shorthand, but a poor account of an individual.|
N~He can choose a different approach. The label does not get a vote.|
N~It sounds tiring to feel people have decided who you are before you speak.|
N~Nobody should be stuck with one specialty just because it is what people remember.|
N~A typecast man is asking for a wider range of material. Fair enough.|
N~Being recognizable can become a very small room.|
S~Try something that surprises him first. Other people's expectations can catch up.|
N~Water is a place to swim, not a shape a person must keep.|
N~One look should never do all the work of knowing somebody.|
N~I would like to hear what he enjoys when nobody is sorting him into a group.
''')
add('water_denise','SixIsland_WaterPath_Text_DenisePostBattle',
    "Denise spends time with the Pokemon her boyfriend gave her when they are apart.",'''
S~A gift that can keep you company has a pretty unfair advantage over a souvenir mug.|
S~A shared association can make companionship especially meaningful during an absence.|
S~Good that the Pokemon gets real time with her, too.|
S~The gift has become part of her everyday life. That feels tender.|
S~Time spent together is a lovely way to care for a living gift.|
S~A memento with its own personality inevitably improves the love story.|
S~Missing one person does not have to make the whole room empty.|
S~That is a gift with a relationship of its own to build.|
S~Affection has found a warm little place to wait between visits.|
S~She seems fond of the Pokemon for more than who gave it to her.|
S~I like that the ordinary hours together matter as much as the giving did.
''')
add('water_earl','SixIsland_WaterPath_Text_EarlPostBattle',
    "Earl asks whether there are mountains nearby.",'''
S~Surrounded by water and already shopping for the opposite direction.|
N~A local map would answer that more reliably than guessing from this stretch of shore.|
N~Best ask a local before setting off with climbing gear.|
S~He has a very clear idea of what would make the visit better.|
N~A mountain trip needs a bit more planning than spotting a hill over lunch.|
S~The traveller requests a change in scenery with considerably more altitude.|
S~Some people arrive on an island and immediately look for somewhere higher to stand.|
S~We should check the terrain before recommending a climb.|
N~Even beside the sea, his thoughts have gone uphill.|
S~His holiday preferences are refreshingly specific.|
S~I wonder what makes a mountain worth visiting to him.
''')
add('water_miu','SixIsland_WaterPath_Text_MiuPostBattle',
    "Miu admits that losing makes her feel sad.",'''
S~Aw. Losing can sit in your middle like a very unwelcome pebble.|
N~Disappointment is a normal response to an outcome she cared about. It will not define her next battle.|
N~Let her be disappointed without making the loss bigger than it was.|
S~She can say she is sad. She does not have to smile for us.|
N~A quiet break might be more welcome than immediate advice.|
N~A small defeat can feel enormous from inside it. No need to review it aloud.|
S~There is nothing embarrassing about caring how something turns out.|
N~Once the sting eases, she can choose one thing to try differently.|
S~The little cloud may stay for a while. We can leave gently.|
N~A gracious winner should know when to stop celebrating.|
S~I hope her sister gives her room to feel it, then helps her laugh again.
''')
add('water_mia','SixIsland_WaterPath_Text_MiaPostBattle',
    "Mia apologizes to her Pokemon after losing.",'''
S~She is checking on her Pokemon before finding someone to blame. I like that.|
N~Concern for the team is valuable. The result alone does not establish that she failed them.|
N~Get them rested. She does not need to carry the whole loss as guilt.|
S~They may want her beside them more than they want an apology.|
S~Care after a hard battle means more than finding the perfect words.|
S~A tender apology from a trainer whose team already knows she cares.|
S~I would rather hear that than see someone turn their hurt on the Pokemon.|
N~Rest first, then review what could help next time. In that order.|
S~Her concern is reaching them, even through the disappointment.|
N~A loss is rough enough without deciding it makes her unworthy of her team.|
S~That little apology says a great deal about how she sees them.
''')
add('entrance_miah','SevenIsland_SevaultCanyon_Entrance_Text_MiahPostBattle',
    "Miah says acting unlike her appearance is a deliberate strategy.",'''
L~She has weaponized the surprise of being a whole person. Excellent.|
S~Expectations can affect decisions. Deliberately confounding them is a plausible tactic.|
S~Anyone judging her by a glance gave her that opening.|
S~I like that she enjoys catching people off guard.|
S~A little surprise can make people pay proper attention.|
M~She has made the audience's lazy assumptions part of her material.|
S~Being difficult to summarize is a respectable advantage.|
S~A strategy that makes the opponent supply their own wrong information. Clever.|
S~A face is a poor map of what someone might do next.|
M~She knows precisely what people assume, and charges them for it.|
S~That is a useful reminder to keep looking after the first impression.
''')
add('entrance_mason','SevenIsland_SevaultCanyon_Entrance_Text_MasonPostBattle',
    "Mason sings about sending out Pokemon and making girls cheer.",'''
L~He has written the cheering into the song. Saves waiting for reviews.|
N~The projected audience response is rather more confident than the available evidence.|
N~He seems capable of providing his own applause.|
F~He certainly does not have trouble singing where people can hear him.|
L~That much confidence could season a very large pot.|
M~A chorus that helpfully informs its audience when to become besotted.|
N~I admire how little outside encouragement his fantasy requires.|
L~Built-in cheering. Efficient, though the audience may want an override.|
N~The hills have been given a very specific idea of romance.|
M~Confidence is charming until it starts writing other people's reactions.|
S~He seems to be having a wonderful time with his own soundtrack.
''')
add('entrance_nicolas','SevenIsland_SevaultCanyon_Entrance_Text_NicolasPostBattle',
    "Nicolas recognizes strong visiting trainers and asks about Trainer Tower.",'''
S~We apparently look like people on the way to more battling. Not an unreasonable guess.|
S~He may be noticing a pattern among visitors headed toward the Tower.|
N~The Tower can wait until the team is ready.|
S~He sounds curious about where the visiting trainers are going.|
N~Worth checking our supplies before turning one battle into several more.|
S~Our reputation has acquired an itinerary before we have settled on one.|
S~A destination can gather a very particular sort of traveller around it.|
S~A challenge attracting skilled visitors would give the locals plenty to observe.|
N~The road carries rumours of its travellers ahead of them.|
S~He has picked up on the look of someone who came prepared.|
S~I wonder how many Tower challengers he has met along this path.
''')
add('entrance_madeline','SevenIsland_SevaultCanyon_Entrance_Text_MadelinePostBattle',
    "Madeline says Pokemon understand kindness from their trainers.",'''
S~They notice the gentle things even when nobody gives those things a score.|
S~Consistent treatment gives Pokemon much more evidence than a single affectionate gesture.|
N~Be kind when it is inconvenient, too. That is when it matters.|
S~I think they hear it in how someone handles an ordinary mistake.|
S~Daily care says a great deal without needing a speech.|
S~A relationship has more dialogue in its actions than its grand declarations.|
S~Quiet kindness is still quite visible to the one receiving it.|
S~The little repeated choices are doing important work.|
S~Gentleness leaves a trace even where hands leave no mark.|
S~It is lovely when care is part of the routine rather than a display.|
S~Watch a trainer between battles and you learn a different part of the story.
''')
add('entrance_eve','SevenIsland_SevaultCanyon_Entrance_Text_EvePostBattle',
    "Eve intends to work harder alongside Jon.",'''
S~They have a next step and someone to take it with. That helps.|
S~Practising together should give them useful information about coordinating their choices.|
N~Good. Give the team a rest before the next session.|
S~She sounds determined without turning against her partner.|
S~Working at it together can make even the awkward attempts worth something.|
S~The partnership has survived its review and booked another rehearsal.|
S~A shared plan is a pleasant thing to leave a loss with.|
S~They can test combinations instead of simply trying everything harder.|
S~Two people can tend the same small spark of resolve.|
S~I like that she puts the next effort in the plural.|
S~I wonder which part of their teamwork they will try changing first.
''')
add('entrance_jon','SevenIsland_SevaultCanyon_Entrance_Text_JonPostBattle',
    "Jon feels happy with Eve whether they win or lose.",'''
S~He has found a way to come out smiling regardless of the score.|
S~Companionship appears to contribute more to his enjoyment than the result itself.|
S~Good company makes a rough battle easier to take.|
F~He sounds very sure about the part that matters to him.|
S~That is a rather lovely reason to look forward to practice.|
S~The romance subplot has quietly overruled the tournament standings.|
S~A loss has failed to make much of an impression on that particular happiness.|
S~An excellent source of motivation. Eve may still want him to learn the tactics.|
S~Some kinds of warmth travel well through a disappointing afternoon.|
S~He is making no attempt whatsoever to look less smitten.|
S~Eve could probably tell how he feels without hearing a word of that.
''')
add('canyon_cyndy','SevenIsland_SevaultCanyon_Text_CyndyPostBattle',
    "Cyndy considers postponing Trainer Tower until she improves.",'''
S~The Tower will still be tall after a little more practice.|
S~Reassessing readiness after new evidence is sensible planning.|
N~Better to prepare than force a challenge she does not feel ready for.|
S~Waiting can be a choice she makes for herself, too.|
N~Rest and practice are a useful part of the trip, not a wasted detour.|
S~She has moved the grand challenge to a later chapter with better preparation.|
S~An unfinished ambition need not become an urgent punishment.|
S~A few focused improvements could make the next attempt feel very different.|
N~The tower is patient stone. It need not set her pace.|
S~Knowing when to pause is its own kind of confidence.|
S~I wonder what she will want to feel stronger about before returning.
''')
add('canyon_evan','SevenIsland_SevaultCanyon_Text_EvanPostBattle',
    "Evan says trainers must develop their own judgment instead of relying on strong Pokemon.",'''
N~A mighty team still needs somebody making sensible decisions at the front.|
S~Resources cannot fully compensate for poor judgment. Experience matters on both sides of the partnership.|
N~The trainer has work to do as well. Fair point.|
N~It must feel lonely to be trusted with all the strength and none of the guidance.|
N~The best ingredients still need someone paying attention to the pan.|
N~An impressive cast cannot rescue a director who has not read the scene.|
N~Power is a rather poor substitute for knowing what you are doing.|
S~Learning to use what you have is its own substantial skill.|
N~A strong companion should not have to carry an inattentive mind as well.|
N~An impressive lineup loses its shine when the trainer stops thinking.|
N~You learn a lot by watching who adjusts when a plan goes wrong.
''')
add('canyon_jackson','SevenIsland_SevaultCanyon_Text_JacksonPostBattle',
    "Jackson says the tiny world seen from the stars still deserves protection.",'''
S~A drop of water can hold a lot of people who need somewhere to stand.|
S~Scale does not determine value. A small world can contain everything important to its inhabitants.|
N~Small from far away. Still our home to look after.|
S~Thinking of everyone living on that little dot makes it feel more precious.|
N~Looking after a place starts with what we leave behind here.|
S~A vast perspective that arrives at a very practical obligation. I like it.|
S~The dark around a small light does not make the light less worth keeping.|
S~We can begin protecting the whole by taking care of the part within reach.|
S~A tiny blue thing is still large enough to hold every familiar voice.|
S~Perspective suits him. It has made his concern larger rather than colder.|
S~I would like more people to look at a beautiful place and think about its future.
''')
add('canyon_katelyn','SevenIsland_SevaultCanyon_Text_KatelynPostBattle',
    "Katelyn recognizes the Running Shoes as a sign of the player's mother's affection.",'''
S~A pair of shoes can say please go explore and please come home at the same time.|
S~A practical gift can express close attention to someone's needs.|
S~Good shoes. A good person thinking ahead for us.|
S~It is sweet that she notices the affection in something so ordinary.|
S~Useful gifts keep taking care of a journey long after the giving.|
S~A mother's good wishes have been travelling at ground level all along.|
S~Love can be very quiet and still survive an unreasonable amount of walking.|
S~Excellent design, and an even better reason for choosing it.|
S~Some blessings have laces and sensible soles.|
S~She has noticed the story behind something people usually glance past.|
S~Every scuff now belongs to a journey someone helped make possible.
''')
add('canyon_leroy','SevenIsland_SevaultCanyon_Text_LeroyPostBattle',
    "Leroy thanks the player for useful battle data.",'''
S~We have become an educational experience. I hope the notes include the exciting bits.|
S~A battle is more informative when the observations lead to a testable adjustment.|
N~He learned something. Good use of a loss.|
S~I like that he can sound grateful while still wanting to improve.|
S~A result worth thinking over is something useful to take home.|
S~The reviewer has found the experience instructive. A gracious notice.|
S~Defeat has been filed under research. A comfortable shelf for it.|
S~Now comes the fun part: changing one thing and seeing what happens.|
S~A difficult moment has left him with something he can use.|
S~He makes a much better impression thanking someone than finding excuses.|
S~I wonder what he noticed in our choices that surprised him.
''')
add('canyon_michelle','SevenIsland_SevaultCanyon_Text_MichellePostBattle',
    "Michelle recognizes her tendency to anger and tries deep breathing.",'''
S~Taking a breath gives the next angry sentence a chance to miss its appointment.|
N~A deliberate pause can help interrupt a response before it becomes automatic.|
N~She noticed the problem. Taking a moment is a solid start.|
S~It can be hard to hear yourself getting sharp before the words are out.|
N~Stepping back for a breath is better than making someone else absorb the temper.|
S~She has wisely introduced a pause before the next dramatic outburst.|
S~A little silence is useful when the alternative has teeth.|
S~That brief delay gives her another choice besides the first impulse.|
N~Air has no opinion about the argument. That can be helpful.|
N~Knowing your own temper is useful; choosing what to do with it matters more.|
S~I respect that she says it plainly instead of dressing it up as someone else's fault.
''')
add('canyon_lex','SevenIsland_SevaultCanyon_Text_LexPostBattle',
    "Lex appreciates the battle as experience for his student Nya.",'''
S~A lesson with actual surprises in it. Much harder to nap through.|
S~A varied opponent can expose assumptions that familiar practice leaves untested.|
N~Useful experience, if he gives her room to learn from it.|
S~I hope he asks what she noticed before explaining everything himself.|
S~A good teacher can help turn the difficult bits into a next step.|
S~The mentor has welcomed an unscheduled guest lecturer.|
N~Experience teaches more gently when someone helps untangle it afterward.|
S~They have fresh examples to work through instead of only repeating theory.|
S~A lesson can arrive wearing the face of a stranger.|
N~His gratitude is welcome. Nya should get some credit for her effort, too.|
S~I wonder whether teacher and student noticed the same turning point.
''')
add('canyon_nya','SevenIsland_SevaultCanyon_Text_NyaPostBattle',
    "Nya wants further tutoring and hopes to continue studying with Lex.",'''
S~More seasoning, she says. Learning apparently comes with a spice rack.|
S~Recognizing room to improve is useful, particularly when she has specific guidance available.|
N~Keep learning. She can still trust her own observations.|
S~Wanting to stay says something kind about how safe she feels asking questions.|
S~A little seasoning takes time. Dumping the whole jar in rarely helps.|
S~The apprentice has requested an extension to her character development.|
S~It is pleasant to hear someone ask to continue rather than pretend to be finished.|
S~A mentor worth keeping should welcome her growing independence, too.|
S~There is still a path ahead, and she has chosen company for it.|
S~She sounds eager to grow, even if she is a little unsure of the invitation.|
S~I hope she gets to say which skills she most wants to work on next.
''')
add('tanoby_brandon','SevenIsland_TanobyRuins_Text_BrandonPostBattle',
    "Brandon dates the ruins to at least fifteen hundred years ago but cannot explain their purpose.",'''
U~Fifteen hundred years is a long time to keep a place's purpose to itself.|
N~Dating a site and interpreting its function are separate questions. His distinction is useful.|
N~Old enough to deserve a careful look. Keep our hands off anything fragile.|
N~So much time, and we are still asking what someone meant to build.|
N~A place can outlast every ordinary explanation people once gave visitors.|
S~The date survives; the premise remains stubbornly unavailable.|
S~Age has preserved the question more thoroughly than the answer.|
S~Construction details might tell us what the missing written record cannot.|
N~The stones have kept their years and lost their introductions.|
N~An honest unknown is more interesting than a confident story made up on the spot.|
S~I wonder what an ordinary day here looked like when the walls were new.
''')
add('tanoby_benjamin','SevenIsland_TanobyRuins_Text_BenjaminPostBattle',
    "Benjamin wonders if these ruins and others he has heard of shelter mystical Pokemon.",'''
S~An old ruin makes a very impressive bedroom, if that is actually what it is.|
N~That is an interesting hypothesis. Similar-looking ruins alone would not establish the same function.|
N~Could be. Better to observe than disturb whatever may be here.|
S~I like hearing what people imagine, as long as there is room to be surprised.|
N~If anything does rest here, barging in would be poor manners.|
S~A promising theory with the important word perhaps still attached.|
S~An abandoned-looking place may simply have unfamiliar residents.|
S~We can compare the sites without assuming they share a purpose.|
N~Some old rooms may be less empty than their visitors think.|
N~It is a good story to investigate, rather than a fact to repeat carelessly.|
S~I wonder who first connected the ruins with those Pokemon.
''')
add('tanoby_edna','SevenIsland_TanobyRuins_Text_EdnaPostBattle',
    "Edna came with Clifford to paint the old buildings.",'''
S~The ruins have acquired a portrait appointment. I hope they hold still.|
S~Painting can encourage sustained observation of details a passing visitor misses.|
S~A quiet reason to make a long trip. Hope she finds a good spot.|
S~I like the idea of spending enough time here for the light to change.|
S~A painting gives the visit something to become after they go home.|
S~The old architecture has finally met someone interested in its better angles.|
S~Old stone and patient attention seem well suited to each other.|
S~The changing shadows could make the same wall look completely different.|
S~She is borrowing a little afternoon light to take home.|
S~The worn surfaces should give her far more to work with than a perfect new wall.|
S~I would love to see which part she chooses to leave inside the frame.
''')
add('tanoby_clifford','SevenIsland_TanobyRuins_Text_CliffordPostBattle',
    "Clifford admires the player's independent exploration and study of Pokemon.",'''
F~That is a generous description of us walking around with questions and spare snacks.|
S~Independent observation has value, though it improves further when findings can be checked.|
S~Kind of him. Still plenty for us to learn.|
F~It is nice when someone sees effort in a thing we are still figuring out.|
S~A warm compliment can make the long way here feel even more worthwhile.|
S~An unexpectedly glowing review from a fellow traveller. I shall accept gracefully.|
S~He has noticed the curiosity rather than only the results. That is kind.|
S~Exploring does teach things a diagram cannot quite prepare you for.|
S~A stranger has offered a small bright thing to carry onward.|
S~He gives a compliment without trying to make himself part of it. Lovely manners.|
S~I like meeting someone who is pleased to see another person's curiosity.
''')
add('tower_dario','SevenIsland_TrainerTower_Text_DarioPostBattle',
    "Dario reflects on future encounters and the connections between people.",'''
S~A path can introduce you to someone your entire plan forgot to include.|
S~Repeated chance encounters can have lasting effects without being predictable in advance.|
N~We will meet more people. Worth treating this meeting well, too.|
S~Some brief conversations stay with you longer than you expect.|
S~A stranger can become someone you are glad you stopped for.|
S~A traveller's future is crowded with characters who have not introduced themselves yet.|
S~It is strange how a small meeting can leave a long shadow, sometimes a kind one.|
S~A connection can begin with something as ordinary as asking directions.|
S~Paths cross quietly before anyone knows what the crossing will mean.|
S~He seems interested in people beyond what they can do for him.|
S~I wonder which brief encounter made him start thinking about that.
''')
add('tower_rodette','SevenIsland_TrainerTower_Text_RodettePostBattle',
    "Rodette wonders about a peculiar Pokemon sleeping somewhere on the island.",'''
U~Somewhere out there, a mysterious Pokemon may be having a very undisturbed nap.|
N~An intriguing report, though we should distinguish a local story from a confirmed sighting.|
N~If it is sleeping, we need not rush to bother it.|
N~She makes the island feel as though it has a secret breathing quietly nearby.|
N~A sleeping Pokemon deserves a gentler search than shouting into every cave.|
S~An excellent rumour: a hidden resident, an uncertain location, and no forwarding address.|
S~The possibility is interesting enough without making promises about what we will find.|
S~I would start by asking what anyone has actually observed.|
N~A sleeper need not be waiting for an audience, whatever the story says.|
N~Mystery is appealing. Claiming it is waiting specifically for us feels a little presumptuous.|
S~I wonder whether the story changes depending on who tells it.
''')
