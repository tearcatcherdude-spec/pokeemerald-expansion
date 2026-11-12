"""Remaining reviewed Hoenn conversations and early-town NPC endings."""
ROWS = []
EMOTIONS = dict(N='neutral', S='soft_smile', A='annoyed', F='flustered', D='sad', U='surprised', M='smug', L='laughing')
def add(key, labels, subject, lines):
    replies = [x.strip() for x in lines.strip().split('|')]
    replies = [EMOTIONS[x[0]] + x[1:] for x in replies]
    assert len(replies)==11, (key,len(replies))
    ROWS.append(dict(key='hir_'+key,labels=labels.split(),subject=subject,replies=replies))

add('rust_cut_neighbor', 'RustboroCity_PokemonCenter_1F_Text_HMCutNextDoor', 'A girl reports obtaining Cut from the neighbor and teaching her Pokemon.', '''
S~A useful neighbor can turn a blocked path into a rather short errand.|
N~Her experience gives us a specific local source for the HM.|
N~Next door. Easy enough to ask about it ourselves.|
N~I like hearing somebody pleased with a new thing they learned together.|
N~I'd ask what path she finally managed to open.|
N~A useful neighbor and a remarkably short trip. I could become enthusiastic about this sort of errand.|
S~A neighborhood service specializing in inconvenient vegetation.|
N~We should learn the conditions for using it before trying it outside.|
N~A small doorway nearby may lead to several more distant openings.|
S~She sounds pleased to pass the useful tip along.|
N~I'd ask which partner she taught and how it took to the task.
''')
add('rust_sex_question', 'RustboroCity_PokemonCenter_1F_Text_MaleAndFemalePokemon', 'A boy wonders about differences between male and female Pokemon.', '''
N~That's a question worth asking carefully instead of filling the gaps with guesses.|
N~Differences vary by species. One general assumption won't describe them all.|
N~Get to know the individual partner. A category won't tell us everything.|
N~I like that there is still something to learn about familiar Pokemon.|
N~I'd start by asking someone who has raised that particular species.|
N~A grand question for a waiting room. We may need more than the nearest chair to answer it.|
N~An excellent opportunity to admit that certainty would be premature.|
N~We can compare actual observations instead of assuming a visible rule.|
N~Two names for a distinction do not reveal every life inside them.|
N~Curiosity is good when it leaves room for individuals to surprise us.|
N~I'd ask what difference first made him wonder.
''')
add('rydel_stored_bike', 'MauvilleCity_BikeShop_Text_OhYourBikeIsInPC', 'Rydel cannot exchange the bicycle until the player brings it from storage.', '''
F~We brought the wish to exchange a bike and forgot the bike-shaped part.|
N~The exchange requires the existing bicycle to be physically available.|
N~Get the bike, then come back. Straightforward fix.|
N~I'm glad he explained it without making the mistake feel enormous.|
N~An errand is easier when you bring the thing the errand is about.|
N~Rydel is admirably patient with a bicycle exchange to which we have brought no bicycle.|
N~A bicycle transaction impeded by a total absence of bicycles on our side.|
N~We should retrieve the original before asking for the replacement.|
N~A journey can wait while we return for what we meant to carry.|
N~His friendly farewell leaves room for us to return less forgetful.|
N~I'd check the bag before making the trip back again.
''')
add('charcoal_initial_gift', 'LavaridgeTown_HerbShop_Text_YouveComeToLookAtHerbalMedicine', 'The old man rewards interest in herbal medicine with Charcoal; bag-full failure replaces the gift source.', '''
S~He likes a curious visitor enough to share something useful.|
S~Interest in his subject prompted a tangible expression of approval.|
S~Kind of him. Let's remember who gave it to us.|
S~It's nice when asking about someone's interest brightens the whole meeting.|
S~I'd hear him out before deciding what to do with the gift.|
S~He rewards curiosity very promptly. I should remember to ask the next question before admiring the gift.|
S~An agreeable exchange rate between attention and charcoal.|
N~We should learn its use so the gift doesn't become unexplained luggage.|
S~A simple question can open a generous hand.|
S~He seems pleased to share the interest as much as the object.|
S~I'd ask what first drew him to herbal medicine.
''')
add('museum_admission', 'SlateportCity_OceanicMuseum_1F_Text_PleaseEnjoyYourself', 'The museum attendant welcomes the visitor after admission or during an ordinary greeting.', '''
S~Permission to be curious in a room full of things ready for it.|
S~The invitation is to observe and learn at our own pace.|
S~Good. Let's look around without getting in anybody's way.|
S~I like an unhurried welcome before a place asks for our attention.|
N~We can take our time with the exhibits that interest us most.|
S~A welcome with room to wander afterward. The attendant has excellent instincts about visitors.|
S~An official invitation to browse quietly. Excellent.|
N~I'd start with the display that explains what the instruments are measuring.|
S~A little room can open onto an ocean of questions.|
S~The greeting makes looking around feel welcome instead of intrusive.|
S~I'd ask which exhibit the staff member enjoys showing visitors.
''')
add('soothe_bell_gift', 'SlateportCity_PokemonFanClub_Text_PokemonAdoresYou', 'The woman recognizes affection and gives a Soothe Bell when the bag permits.', '''
S~Our partner's fondness was noticed, and now there's a little bell to remember it by.|
S~She is responding to observed affection rather than a claimed training record.|
S~Good to know the partner feels that way. The gift is a bonus.|
S~I like praise that notices the quiet parts of being together.|
S~The ordinary care has become visible to someone else.|
S~The Pokemon has given us an excellent reference. I shall try to remain worthy of the recommendation.|
S~A favorable review with an unexpectedly musical enclosure.|
N~We can appreciate the item while keeping the routine that earned the compliment.|
S~A little sound can accompany something that was already warm.|
S~The best part is knowing the partner is happy beside us.|
S~I'd thank her for seeing that, as well as for the bell.
''')
add('space_crisis_launch_pending', 'MossdeepCity_SpaceCenter_1F_Text_HaywireButRocketLaunchImminent', 'Amid the center crisis, staff report the rocket launch is still imminent.', '''
N~The launch clock is continuing while the rest of the room has developed a very bad day.|
N~The launch status and the security situation are distinct but interacting concerns.|
N~Check that proceeding is safe. A schedule doesn't outrank the people here.|
N~It must be difficult to concentrate with all this happening around them.|
N~I'd want the crew to have enough calm and support for those final checks.|
N~The rocket is punctual. I wish the criminals had chosen a less inconvenient day to be criminals.|
N~A launch and a crisis sharing a timetable. Unhelpful coordination.|
N~They should reassess the risk rather than continue only because the clock says so.|
N~A bright wish needs careful hands, especially when the room is shaking.|
N~I hope the staff can say stop if something no longer feels safe.|
N~I'd ask where visitors should wait so the team has space to work.
''')
add('space_crisis_launch_safe', 'MossdeepCity_SpaceCenter_1F_Text_HaywireButSuccessfulLaunchNumber', 'Despite the crisis, staff confirm the numbered rocket launch succeeded safely.', '''
S~One thing reached the sky safely in the middle of all this trouble. That's worth a breath.|
S~A safe launch is confirmed even though the facility has other unresolved problems.|
S~Good work. Now keep the staff and the rest of the center safe too.|
S~That must be a difficult sort of relief, with the room still unsettled.|
S~The crew deserves to know that careful work mattered today.|
S~A safe launch in the middle of this mess. Someone here deserves a quiet chair and an extravagant compliment.|
S~A successful departure despite an excessively eventful ground floor.|
N~They can preserve the result and still review how the disruption affected procedures.|
S~A small clear light can remain true inside a troubled day.|
S~I'd make room for their relief without pretending everything else is settled.|
S~I'd ask the team about it when they finally have a calm moment afterward.
''')
add('lottery_tomorrow', 'LilycoveCity_DepartmentStore_1F_Text_ComeBackTomorrow', 'The daily lottery draw is already used and the clerk asks the player to return tomorrow.', '''
N~Today's numbers have done their day's work. Tomorrow can have a turn later.|
N~The daily opportunity is exhausted. Repeating the request won't alter the result.|
N~We're done for today. Plenty else to do.|
N~A clear limit makes it easier to stop wondering about one more try.|
N~We can let a small part of the day stay small.|
N~Tomorrow remains surprisingly immune to being asked for sooner. Best let the clerk get on with the afternoon.|
N~The clerk has assigned the next attempt to time itself. Sensible.|
N~We should note the interval rather than make the same check repeatedly.|
N~A little chance can wait beside the next sunrise.|
N~No need to build the whole day around a possible prize.|
N~I'd take the reminder and go enjoy the rest of the store.
''')
add('lottery_declined', 'LilycoveCity_DepartmentStore_1F_Text_PleaseVisitAgain', 'The player declines the lottery draw and receives a polite farewell.', '''
S~No ticket today. Our afternoon can remain gloriously unnumbered.|
N~No draw was taken. The visit ended without a result to interpret.|
S~Fine choice. We can keep moving.|
S~It's nice when choosing not to take part stays simple.|
N~A little chance doesn't have to be part of every shopping trip.|
S~I enjoy a little suspense. I also enjoy deciding I have had quite enough suspense without taking any.|
S~An uneventful outcome requiring no investigation. Lovely.|
N~We can use the visit for the things we actually came to do.|
S~An unopened possibility can remain unopened.|
S~The clerk kept the welcome after the answer became no.|
S~I'd say thanks and leave room for the next visitor.
''')
add('lottery_finished', 'LilycoveCity_DepartmentStore_1F_Text_PleaseVisitAgain2', 'The lottery visit ends after a completed draw; this shared farewell does not distinguish wins from misses.', '''
N~The numbers have had their moment. We can let the rest of the day begin again.|
N~The brief suspense is over. We can return our attention to the rest of the outing.|
N~Done here. Let's move on without chasing the moment.|
N~I like having a clear end to a little suspense.|
N~A lottery can be one small stop instead of the whole outing.|
N~The suspense has ended, and the rest of the afternoon is still ours. A pleasantly generous arrangement.|
N~A tidy closing line after an unusually numerical conversation.|
N~Let's check our shopping list before choosing another floor to visit.|
N~A chance has passed through the day and left the road continuing.|
N~Whatever the result, we can keep the rest of the visit pleasant.|
N~I'd give the next person room at the counter.
''')
add('lottery_no_room', 'LilycoveCity_DepartmentStore_1F_Text_NoRoomForThis', 'A lottery prize is held because the player lacks bag space.', '''
N~The prize has our name on it, but the bag hasn't found a little room for that name.|
N~The entitlement is recorded; the item has not yet transferred.|
N~Make space, then collect it. No need to rush or buy another ticket.|
N~It's reassuring that the prize won't vanish just because the bag is awkward.|
N~A tidy pocket can be a surprisingly useful part of good fortune.|
N~Good fortune has encountered bad packing. A deeply unheroic obstacle, but at least we know how to fix it.|
N~A winning number has encountered an unwinnably full pocket.|
N~We should free capacity before returning to collect the held item.|
N~Something promised can remain safe while a place is made for it.|
N~The clerk made the next step clear without making the delay embarrassing.|
N~I'd ask where to collect it after sorting our supplies.
''')
add('lottery_held_collected', 'LilycoveCity_DepartmentStore_1F_Text_PrizeWeveBeenHolding', 'A previously held lottery prize is delivered; a repeated storage failure replaces this source.', '''
S~A little piece of earlier good luck has finally found its way into our hands.|
S~The recorded prize is now collected after the earlier capacity problem.|
S~Good. We followed up instead of leaving it forgotten.|
S~It's nice to be remembered when you return for something.|
S~The clerk kept the promise while we dealt with the practical part.|
S~The clerk remembered us and the prize. I appreciate competence most when it quietly makes my day easier.|
S~An unresolved prize has ceased being administrative history.|
N~We should check the received item and keep the bag organized afterward.|
S~A small postponed kindness has reached the day it was waiting for.|
S~I appreciate how ordinary and welcoming the handoff feels.|
S~I'd make sure to thank the clerk for holding it safely.
''')
add('ornament_gift', 'LilycoveCity_LilycoveMuseum_2F_Text_TokenOfGratitude', 'The curator awards the Glass Ornament for completing the collection; no-room branch replaces this source.', '''
S~A little bright thank-you for helping put so much life on the walls.|
S~The ornament acknowledges a completed contribution to the public collection.|
S~Kind of him. Give it a safe place when we get home.|
S~I think his happiness about the paintings is the part I'd remember most.|
S~A thoughtful reward can keep a shared accomplishment close.|
S~The curator has excellent taste in thank-yous. We should find somewhere that does not invite a tragic tumble.|
S~A fragile award for a fortunately less fragile achievement.|
N~We should place it somewhere steady, away from a busy edge.|
S~A bright object can hold the memory of a room coming alive.|
S~It will look nicest where we can see it without having to fuss over it.|
S~I'd tell the artist and the team how happy the curator sounded.
''')

add('petal_adventure_wish', 'PetalburgCity_House1_Text_GoOnAdventure', 'A resident romantically imagines difficult travel, including homesickness.', '''
S~Even the homesick bit made the imaginary itinerary. That's a thoroughly imagined adventure.|
N~They recognize discomfort as part of travel, though experiencing it may feel different.|
N~Good dream. Pack for the damp grass, not only the grand view.|
N~I like that wanting to leave doesn't mean forgetting what home feels like.|
N~A cold night becomes more manageable when you actually prepared a warm meal.|
S~They have even romanticized damp socks. I admire the enthusiasm and recommend a short trial journey.|
N~A romantic appreciation of discomfort best tested in small doses.|
N~I'd start with a short trip and learn what the equipment needs to handle.|
N~A far road can be dear even before we learn the weight of its weather.|
N~The dream can stay lovely while becoming a little more practical.|
S~I'd ask which place they would choose for the first real outing.
''')
add('petal_traveled_young', 'PetalburgCity_House1_Text_TravelingIsWonderful', 'An older resident remembers roaming the seas and mountains in youth.', '''
S~Some of those journeys are still taking a happy little walk through their voice.|
S~Remembered travel often preserves particular encounters more strongly than distances.|
S~Sounds like they have stories worth sitting down for.|
S~I wonder which quiet moment stayed after the difficult miles faded.|
S~I'd ask about the meal that tasted best after a long day.|
S~Someone should ask for the long version. A person who smiles like that at an old trip has earned a listener.|
S~A veteran traveler has found an excellent way to cross mountains without standing up.|
N~I'd ask what their equipment was like when they first went out.|
S~A far landscape can remain near inside a familiar voice.|
S~It's lovely when remembering doesn't become a demand that everyone travel the same way.|
S~I'd ask which place they would most like to see again.
''')
add('petal_norman_once', 'PetalburgCity_House2_Text_BattledNormanOnce', 'A former challenger remembers Norman strength and dedication.', '''
N~Norman apparently made his point without needing the challenger to remember every move.|
N~The experience left an impression of sustained commitment rather than only power.|
N~Worth learning from. Dedication shows in the decisions.|
N~It sounds like losing still left them with something to admire.|
N~I'd be curious about the routine behind that much confidence.|
N~Norman seems to make an impression that survives the loss. An irritatingly effective kind of opponent.|
N~A man who lives for Pokemon sounds inconvenient to challenge before lunch.|
N~I'd ask what specific choice made the dedication so obvious.|
N~A practiced life can leave its shape in a single encounter.|
N~They saw something about the person behind the strong team.|
N~I'd ask what they changed in their own training after that match.
''')
add('petal_norman_family_move', 'PetalburgCity_House2_Text_NormanBecameGymLeader', 'A resident connects Norman new Gym role with his family moving from far away.', '''
N~A new Gym Leader means a new home for more people than the badge case suggests.|
N~A professional move can reshape the daily lives of an entire household.|
N~Hope the family gets time to settle as well as the Leader does.|
N~A long move can make ordinary introductions feel surprisingly important.|
N~Someone should show them the good place to buy dinner before praising the new Gym.|
N~The new Leader has a family to settle, too. The town should offer directions to groceries as well as the Gym.|
N~A new job, a new town, and presumably several boxes that refuse to unpack themselves.|
N~A family's practical needs are part of making that transition work.|
N~One person's new door can move a whole home's horizon.|
N~I'd welcome the family as people, not only as extensions of the job.|
N~I'd ask whether anybody has helped them get to know the neighborhood.
''')
add('petal_repel_hurry', 'PetalburgCity_Mart_Text_RepelIsUseful', 'A shopper recommends Repel when traveling quickly.', '''
N~Sometimes we want new introductions. Sometimes we want to reach the next town before dinner.|
N~Avoiding incidental encounters can make a route's travel time more predictable.|
N~Useful when we're in a hurry. Still watch the route.|
N~An uninterrupted walk can be nice when everybody needs a quiet stretch.|
N~I'd save it for the days when arriving matters more than exploring.|
N~I am delighted to learn that reaching a destination need not require greeting every creature along the way.|
N~A little bottle of fewer interruptions. Persuasive.|
N~We should use it for a specific stretch rather than spray without a plan.|
N~Passing quietly can be a choice without being a rejection of the place.|
N~It's fine to decide what kind of outing we have energy for.|
N~I'd ask which part of the route usually slows that shopper down.
''')
add('petal_antidotes', 'PetalburgCity_Mart_Text_TakeSomeAntidotesWithYou', 'A shopper advises carrying Antidotes rather than leaving a Pokemon poisoned while walking.', '''
N~A partner shouldn't have to carry poison along with the rest of the trip.|
N~An unresolved status can continue causing harm after the encounter ends.|
N~Treat it promptly. Don't ask the partner to walk it off.|
D~I wouldn't want them trying to keep up while feeling worse with every step.|
N~Keeping the right cure handy is a simple bit of care.|
N~The argument for packing Antidotes is persuasive enough that I would rather not arrange a demonstration.|
N~An excellent product recommendation supported by an unpleasantly convincing reason.|
N~We should check status after an encounter, not only remaining HP.|
N~A journey should not ask an injured creature to suffer silently beside it.|
N~Good advice notices what the partner feels after the excitement ends.|
N~I'd check our supply before heading back into the grass.
''')
add('petal_weak_grow', 'PetalburgCity_Mart_Text_WeakWillGrowStronger', 'A shopper emphasizes care for Pokemon who are presently weak.', '''
S~Small strength is still strength with somewhere to grow.|
S~Present ability is not a fixed limit on future development.|
N~Care for them and train at a pace they can handle.|
S~It's good to hear somebody speak kindly about the beginning.|
N~Affection needs practical shape: food, rest, patience, and sensible practice.|
S~Nobody begins impressively. It is helpful when people remember that before addressing a beginner.|
S~An encouraging refusal to treat a beginner as a failed expert.|
N~We should choose challenges that build confidence rather than overwhelm.|
S~A little shoot needs tending before anyone asks it for shade.|
N~Loving them also means noticing who they are, not only what they might become.|
S~I'd ask about a partner that surprised this shopper as it grew.
''')
add('petal_types', 'PetalburgCity_PokemonCenter_1F_Text_ManyTypesOfPokemon', 'A visitor explains type strengths and weaknesses.', '''
N~Even a very strong partner can meet a problem that wants a different answer.|
N~Matchup effects change the value of otherwise similar moves and stats.|
N~Learn the matchups. Have another option ready.|
N~I like knowing there is a reason a battle suddenly feels harder.|
N~Sharing the work between different partners makes a lot of sense.|
N~A formidable partner is excellent. A formidable partner with a second plan is considerably less exhausting.|
N~An excellent system for making confidence occasionally inconvenient.|
N~We should check both types before assuming a single advantage settles it.|
N~A strength can meet its boundary without becoming worthless.|
N~No one partner needs to be the best answer to everything.|
N~I'd ask which matchup first caught the visitor by surprise.
''')
add('petal_oran', 'PetalburgCity_PokemonCenter_1F_Text_OranBerryRegainedHP', 'A visitor observed an Oran Berry restoring Pokemon HP.', '''
S~A Berry with a helpful second job after being a Berry.|
S~A consumed held Berry can provide recovery without a separate Trainer action.|
N~Useful little backup. Don't rely on one to solve every injury.|
S~It's nice when a partner has a little help ready before it needs to ask.|
S~A useful snack is a wonderful invention the tree already worked out.|
S~A snack that helps at the right moment. I respect an item with the courtesy to make itself useful.|
S~A snack with measurable benefits. Delightfully direct.|
N~We should know when it activates and replace it after use.|
S~A small fruit can carry a moment of relief.|
N~A caring little detail, especially if the Trainer remembers to prepare another.|
S~I'd ask which Pokemon tried it and what its first reaction was.
''')
add('petal_storage_wizard', 'PetalburgCity_PokemonCenter_1F_Text_PCStorageSystem', 'A visitor marvels at the Pokemon Storage System inventor.', '''
U~A scientific wizard is a very good title for making something this useful.|
S~The system's convenience hides a substantial amount of design work.|
S~Good work deserves recognition, even when we don't know the maker yet.|
S~It's nice when someone wonders about the person behind an everyday thing.|
N~A useful service can make a long journey easier in ways you stop noticing.|
S~Scientific wizard seems a reasonable compliment. I trust the actual inventor receives a little time off, too.|
S~A wizard whose spell probably involved a remarkable quantity of testing.|
U~I'd love to know which problems they had to solve before it felt so simple.|
N~A quiet machine can carry the trace of many patient days.|
S~Convenience is worth appreciating when somebody worked hard to make it possible.|
S~I'd ask what part first made the visitor stop and marvel.
''')
add('petal_starter_types', 'PetalburgCity_PokemonCenter_1F_Text_StarterTypes', 'A visitor recommends checking the chosen starter own types and experimenting with moves.', '''
S~Our first partner gets to be itself, rather than whatever the first lesson expected.|
N~The individual starter's actual typing is more informative than a generic assumption.|
N~Know the partner we've got. Build from there.|
S~I like being told to learn this particular Pokemon instead of memorize a ready-made story.|
N~Trying a few suitable moves can teach us what feels comfortable together.|
S~I approve of advice that begins by noticing which Pokemon is actually standing beside us.|
N~A useful reminder to inspect the actual creature before applying the familiar theory.|
N~We can compare its types and available moves before choosing how to train.|
S~A first meeting can open a path nobody else would take in quite the same way.|
N~The best beginning is paying attention to the partner beside us.|
S~I'd ask which move the starter seems most confident using so far.
''')
add('wally_father_first_thanks', 'PetalburgCity_WallysHouse_Text_ThanksForPlayingWithWally', 'Wally father thanks the player and explains the move to relatives for his health.', '''
N~A short outing with Wally meant a lot more to this house than we could see.|
N~His parents are weighing a familiar history of illness against a promising change.|
N~Glad we could help. We should give them clear news when we have it.|
D~He sounds grateful and worried in the same breath.|
N~A happy first Pokemon doesn't make the family stop worrying overnight.|
N~A first catch can be a very large event to the family waiting at home. We should remember that.|
N~A parent's gratitude tends to arrive carrying several unspoken questions.|
N~Reliable contact would help them adjust to him being away.|
N~Hope can move into a home without immediately sending fear away.|
N~I'd listen to the concern without reducing Wally to being frail.|
N~I'd ask what kind of updates would help them feel closer to his trip.
''')
add('wally_father_wonder', 'PetalburgCity_WallysHouse_Text_WonderHowWallyIsDoing', 'Wally father quietly wonders how his absent son is doing.', '''
D~A short question that probably visits him many times a day.|
N~Uncertainty becomes tiring when someone important is out of contact.|
N~If we hear something solid, we should pass it along.|
D~I know how a familiar room can feel full of someone who isn't there.|
N~A little message could mean more to him than the sender realizes.|
N~I suspect he has asked that question while doing nearly everything else today. A message would be a kindness.|
D~Distance is especially rude when it refuses to provide updates.|
N~A regular check-in would do more than repeated reassurance without new information.|
D~A far road can echo inside a quiet house.|
N~He doesn't need a grand report, just something real.|
N~I'd ask when he last heard directly from Wally.
''')
add('wally_home_soon', 'PetalburgCity_WallysHouse_Text_WallyIsComingHomeSoon', 'Wally father looks forward to his son expected return.', '''
S~Soon is a lovely word when somebody you miss is inside it.|
S~An expected return gives the waiting a more definite shape.|
S~Good. Wally will have a lot to tell them.|
S~I imagine the house already feels different just from knowing that.|
S~I'd ask what meal he wants ready for the homecoming.|
S~His son coming home is clearly the event he most wants to attend. Some priorities are beautifully straightforward.|
S~An approaching end to the parent's least favorite pastime: waiting.|
N~I'd confirm the plan so they know when to expect him.|
S~A doorway can seem warmer before anyone steps through it.|
S~He sounds pleased about the ordinary company, not only the news Wally will bring.|
S~I'd love to hear what Wally chooses to share first.
''')
add('wally_far_disbelief', 'PetalburgCity_WallysHouse_Text_YouMetWallyInEverGrandeCity', 'Wally father cannot believe his son traveled as far as Ever Grande alone.', '''
N~His picture of Wally is still standing much nearer home than Wally actually is.|
N~New evidence conflicts with a long-established expectation of limited independence.|
N~He needs to hear it clearly. Wally earned that journey.|
D~It must be hard to let an old fear make room for a new truth.|
N~I'd explain what we actually saw instead of arguing about what should be possible.|
N~Wally has traveled farther than his father can quite imagine. We can offer details without making it an argument.|
N~Reality has delivered an update his expectations are declining to install.|
N~Specific details may help him revise the assumption without feeling cornered.|
N~Someone can travel beyond the size of another person's worry.|
N~He is underestimating Wally out of a habit built from concern. It can still change.|
N~I'd want him to hear the whole story from Wally himself too.
''')
add('wally_smile', 'PetalburgCity_WallysHouse_Text_WallyWasReallyHappy', 'Wally mother remembers his rare bright smile after catching his first Pokemon.', '''
S~That first Pokemon brought home a smile the whole family had missed.|
S~She noticed a meaningful change in his mood, not merely the successful catch.|
S~Good. A partner can give someone a reason to look ahead.|
S~I like that she remembers his face more than the event itself.|
S~A happy little story can feed a parent's hope for a long time.|
S~That is a lovely thing to have helped happen. The family remembers a smile rather than a number in a record.|
S~A small Pokemon has made a remarkably large difference to this room.|
N~I'd ask what he has enjoyed doing with his partner since then.|
S~A little joy can return light to a face people know by heart.|
S~Her happiness about his happiness says more than any grand praise.|
S~I'd make sure Wally knows how fondly she remembers that moment.
''')
add('wally_mother_secret', 'PetalburgCity_WallysHouse_Text_WallyLeftWithoutTelling', 'Wally mother privately reveals his unannounced departure and trusts his determination.', '''
N~She knows he left quietly and is trying to let hope speak louder than worry.|
N~Her confidence in his will is distinct from knowing his present safety.|
N~He should send word. Independence doesn't need to leave everyone guessing.|
D~Keeping the worry private probably makes it heavier.|
N~I'd encourage a real message from Wally rather than another round of hoping alone.|
N~Her confidence is trying very hard to sound effortless. Wally could spare her some work by sending a message.|
N~A determined young Trainer has created an exceptionally anxious information shortage.|
N~A simple contact plan could respect his freedom and reduce the worry at home.|
N~Trust can open a hand while fear keeps checking the empty palm.|
N~She sees his strength. It would be kind if he gave her something solid to hold onto too.|
N~I'd ask whether there is a way for him to contact the family directly.
''')
add('wally_surf', 'PetalburgCity_WallysHouse_Text_SurfGoAllSortsOfPlaces', 'After the Surf gift, Wally father describes travel opportunities across water.', '''
U~The water on the map has just become a collection of possible roads.|
S~A new movement capability changes which destinations are accessible.|
N~Plan the crossing and the return. New access still needs good judgment.|
N~It is exciting when a familiar shore stops being the edge of everything.|
N~We should pack for the trip beyond the water, not only the first crossing.|
S~A useful gift, followed by an unusually large choice of where to go. I recommend deciding before entering the water.|
N~The map has become larger without the paper increasing. Inconveniently clever.|
N~We should find safe entry points and understand the currents.|
N~An old boundary can become a path with a trusted companion beside us.|
N~A new freedom is nicest when the partner is comfortable sharing it.|
S~I'd ask which water route local travelers would recommend trying first.
''')
add('oldale_free_center', 'OldaleTown_PokemonCenter_1F_Text_PokemonCentersAreGreat', 'A visitor appreciates freely available Pokemon Center healing.', '''
S~A long road feels kinder when getting help doesn't depend on the coin purse.|
S~Accessible care removes a significant barrier to treating injury promptly.|
N~Use it when the team needs it. No reason to make them push through.|
S~It's comforting to know a safe stop is there even on an awkward day.|
S~A place that helps tired travelers without making them choose against dinner is wonderful.|
S~Free recovery is a splendid idea. I see no reason to test whether we can manage without something this helpful.|
S~A free rest, offered without an elaborate speech. Civilization at its best.|
N~We should know the Center locations along the planned route.|
S~A little light in a window can mean help without a price.|
S~Being able to ask for care easily is worth appreciating.|
S~I'd ask whether the visitor has a particular nurse they remember helping them.
''')
add('oldale_public_pc', 'OldaleTown_PokemonCenter_1F_Text_TrainersCanUsePC', 'A visitor explains that the Center PC is available to any Trainer.', '''
S~An intimidating-looking machine with a surprisingly welcoming invitation.|
S~Clear public access matters when a service looks like it might belong to staff.|
N~Good to know. Use it carefully and leave it ready for the next person.|
N~It's nice when someone says explicitly that you're allowed to be there.|
N~A shared useful thing works best when everybody leaves it tidy.|
N~An explicit welcome to use the machine saves a great deal of standing beside it looking meaningfully uncertain.|
S~A reassuring clarification before curiosity becomes an awkward apology.|
N~I'd look at the available functions before making a change.|
N~A familiar corner can become less closed with one kind sentence.|
S~That small welcome makes learning a new thing much less uncomfortable.|
N~I'd ask where first-time users can find the instructions.
''')
add('oldale_wireless_wait', 'OldaleTown_PokemonCenter_1F_Text_WirelessClubNotAvailable', 'The new Wireless Club is still being adjusted and is not available yet.', '''
N~The new room is nearly ready, but nearly isn't an invitation to press every button.|
N~Completion of the structure does not imply the service has finished testing.|
N~Let them get it working properly. We can return later.|
N~I would rather wait than have the first visit turn into a confusing problem.|
N~A safe opening is better than a hurried one.|
N~Waiting is tiresome. Discovering why a service needed more testing would probably be worse.|
N~New and usable have not yet agreed to mean the same thing.|
N~Final adjustments are part of delivering a service that people can trust.|
N~A closed door can be protecting the beginning that waits behind it.|
N~Clear expectations make the delay easier to understand.|
N~I'd ask how they'll let visitors know when the room is ready.
''')
add('oldale_wireless_trade', 'OldaleTown_PokemonCenter_1F_Text_TradedInWirelessClub', 'After the Club opens, a visitor reports trading there immediately.', '''
S~They waited for the doors to open and made a new introduction straight away.|
S~The completed service has already supported an actual exchange.|
S~Good. Hope the new partner is settling in well.|
S~A first visit can become memorable very quickly when a Pokemon comes home with you.|
S~I'd ask what familiar routine will help the new partner feel welcome.|
S~The room opens, and someone immediately makes a friend-shaped change to their journey. An excellent beginning.|
S~An opening ceremony with remarkably tangible souvenirs.|
N~I'd ask whether using the service felt clear to a first-time visitor.|
S~A room can make a new bond possible on its very first day.|
S~The excitement should leave room for the Pokemon's own change of surroundings.|
S~I'd ask about the person they traded with and what they learned from each other.
''')
add('oldale_buy_balls', 'OldaleTown_Mart_Text_ImGoingToBuyPokeBalls', 'A shopper plans to buy many Poke Balls and meet many Pokemon.', '''
S~An enthusiastic shopping list with a whole crowd of future introductions imagined inside it.|
N~The equipment supports the plan, but each new partner also creates care responsibilities.|
N~Prepare to look after them as well as catch them.|
N~I'd want time to learn the little habits of the first one too.|
N~A growing team needs more than a growing pile of Balls.|
S~An ambitious plan. I would ask who is doing the feeding before applauding the projected size of the household.|
N~A large collection begins with a bag. Maintaining it is a larger subject.|
N~I'd plan for supplies and training time alongside capture equipment.|
N~Many meetings can be wonderful when each life remains more than a number.|
N~Enthusiasm is a good beginning if it leaves room for thoughtful choices.|
S~I'd ask which Pokemon they most hope to meet first.
''')
add('oldale_balls_soldout', 'OldaleTown_Mart_Text_PokeBallsAreSoldOut', 'A shopper cannot buy Poke Balls because the Mart is sold out.', '''
F~The adventure shopping list has found a shelf-shaped hole in its plans.|
N~The limitation is stock availability, not the shopper's preparation.|
N~Ask when the next delivery comes. No point blaming the clerk.|
N~It's disappointing when the thing you came for is the one missing thing.|
N~A short wait might be easier if they have another errand to do meanwhile.|
N~The shelf is empty, and taking offense will not restock it. We can ask a useful question instead.|
N~Demand has successfully outrun the box in the back room.|
N~We can find another supplier or return after the next shipment.|
N~A beginning can pause without closing.|
N~The clerk probably isn't enjoying having the same disappointing conversation all day either.|
N~I'd ask whether they know another nearby shop with stock.
''')
add('oldale_potion_prevent', 'OldaleTown_Mart_Text_RestoreHPWithPotion', 'A shopper recommends Potions before injury leads to fainting.', '''
N~A little help now is nicer than waiting for a partner to stop standing.|
N~Preventive recovery can reduce the risk of an avoidable faint.|
N~Don't wait until the last safe moment to act.|
N~A partner should not have to look desperate before we notice.|
N~Keeping supplies handy makes it easier to respond when somebody needs help.|
N~If a little help prevents a dramatic collapse, I favor the little help. Drama is overrated when it hurts.|
N~A modest intervention before a more inconvenient collapse. Sensible.|
N~We should estimate the likely incoming damage, not stare only at the current number.|
N~Care can arrive before the hurt becomes a crisis.|
N~Their trust grows when they see us act before the situation becomes frightening.|
N~I'd check our stock before making the next stretch of road.
''')

add('lab_fieldwork_first', 'LittlerootTown_ProfessorBirchsLab_Text_BirchAwayOnFieldwork', 'The aide explains Birch absence and preference for research outdoors.', '''
S~The laboratory is missing its professor because the professor has gone to the actual Pokemon.|
S~Field observations can answer questions the controlled room cannot.|
N~Makes sense. Ask where he went before searching the whole countryside.|
N~I like the thought of somebody caring enough to go see the place for themselves.|
N~He probably needs someone to remind him to eat while he's out there.|
N~Birch seems reliably located wherever the comfortable chair is not. I imagine the aide gives these directions often.|
N~A scientist who can leave his chair. A startlingly mobile discipline.|
N~The notes still matter when he gets back. Fieldwork needs a good record.|
N~A question can lead a person beyond the walls where it began.|
N~The aide sounds used to explaining why the busiest desk is empty.|
N~I'd ask what part of the local habitat he is investigating today.
''')
add('lab_fieldwork_repeat', 'LittlerootTown_ProfessorBirchsLab_Text_BirchIsntOneForDeskWork', 'The aide reiterates Birch preference for firsthand outdoor work.', '''
S~His chair must have a very restful job.|
N~Firsthand experience is valuable when it is recorded and compared carefully.|
N~Good to get out there. Good to finish the paperwork afterward too.|
N~Some people understand a place better after standing quietly inside it.|
N~A working day outdoors still needs an ordinary lunch break.|
N~Experience is valuable. So are the notes that let somebody else understand what the experience showed.|
S~An admirable affection for reality over the desk where it gets summarized.|
N~I'd want his observations organized so other people can use them too.|
N~The grass may offer a question the page has not learned to ask.|
N~I hope the aide's own work is appreciated while the professor is away.|
N~I'd ask what surprising thing he brought back from the last trip.
''')
add('lab_family_help', 'LittlerootTown_ProfessorBirchsLab_Text_BirchEnjoysRivalsHelpToo', 'The aide describes Birch research and warm enjoyment of his child help.', '''
S~Research with somebody you love sounds like a good reason to keep coming back muddy.|
S~A shared task can make time together productive without making it less personal.|
S~Good. Hope they both enjoy the work, not only the results.|
S~It's nice that somebody notices the fondness around all those facts.|
S~Working together can leave you little ordinary memories no report includes.|
S~The work sounds useful, but the fondness is the detail that makes me want to hear more.|
S~A laboratory with affection in the observations. Not an invalidating variable.|
N~I'd ask which part of the fieldwork the child likes helping with.|
S~A question shared kindly can become a way of being close.|
S~They see each other doing something they care about. That's valuable.|
S~I'd love to hear about a discovery they made together.
''')
add('lab_teach_beginner', 'LittlerootTown_ProfessorBirchsLab_Text_GetRivalToTeachYou', 'After the player agrees to meet the rival, Birch recommends learning Trainer basics from them.', '''
S~A new neighbor can also be someone who knows which beginner mistakes have sharp edges.|
N~A peer with experience can translate the basics into practical examples.|
N~Listen, ask questions, and learn the partner we've actually got.|
F~It's easier to meet somebody when there is a small thing to do together.|
N~A friendly lesson could spare us a very uncomfortable first trip.|
S~A helpful neighbor with experience is a fine beginning. Nobody sensible expects us to know everything already.|
N~A sensible plan: locate the person who has already made some of the mistakes.|
N~We can ask for one useful lesson rather than pretend to understand everything.|
S~A first road feels kinder when someone can point out its turns.|
N~Being related to a Trainer doesn't remove the right to be a beginner.|
S~I'd ask what they wish someone had explained on their first day.
''')
add('lab_catch_cute', 'LittlerootTown_ProfessorBirchsLab_Text_CatchCutePokemonWithPokeBalls', 'May describes exploring for different Pokemon she finds cute; this does not prove the preceding Ball gift succeeded.', '''
S~May has a whole journey planned around meeting faces that make her smile.|
N~A personal interest can motivate broad field exploration without determining every choice.|
N~Find good partners and learn what they need. Cute comes with responsibilities too.|
S~I like how much she is looking forward to the meetings themselves.|
N~A growing team means a growing amount of ordinary daily care.|
S~May has a splendidly candid reason for exploring. I would rather hear that than an unnecessarily grand justification.|
S~A scientific tour guided partly by the urge to say aww. Understandable.|
N~I'd ask how she prepares for a species she hasn't raised before.|
S~A fond glance can be the start of learning someone carefully.|
N~What feels cute becomes deeper once you know the particular Pokemon.|
S~I'd ask which unexpected encounter made her happiest so far.
''')
add('lab_catch_cool', 'LittlerootTown_ProfessorBirchsLab_Text_CatchCoolPokemonWithPokeBalls', 'Brendan describes seeking diverse Pokemon he finds cool; the preceding gift may have failed.', '''
S~Brendan has turned cool into a perfectly serviceable reason to go exploring.|
N~Interest can drive observation, though careful care must follow any capture.|
N~Good to be eager. Think past the exciting first encounter too.|
N~I'd like hearing what makes a Pokemon stand out to him.|
N~The impressive newcomer will still need a familiar routine afterward.|
S~Cool is a fine first impression. I should like to hear what he notices once the Pokemon feels at home.|
S~Cool remains a scientifically broad category with excellent travel potential.|
N~I'd ask what he learns from a partner after the first impression settles.|
N~Wonder can invite a meeting; attention turns it into knowledge.|
N~An exciting collection works best when the individual partners remain visible.|
S~I'd ask which Pokemon changed his mind after he got to know it.
''')
add('lab_rival_next_may', 'LittlerootTown_ProfessorBirchsLab_Text_MayWhereShouldIGoNext', 'May considers where to search for Pokemon next.', '''
S~The map has too many promising corners for one afternoon. A nice kind of problem.|
N~A useful destination would depend on which habitats or species she wants to investigate.|
N~Pick one route and prepare for it. The rest can wait.|
N~Sometimes choosing the next place feels harder than walking there.|
N~I'd ask where she can stop for a meal along the way.|
S~The terrible inconvenience of several appealing destinations. She should choose one before the afternoon leaves without her.|
S~An excellent question to ask before leaving through the nearest door.|
N~A short list of unanswered questions could help choose the next field site.|
N~A road can wait patiently while curiosity chooses its direction.|
N~She doesn't need to see everything on one trip for it to count.|
S~I'd ask what she most hopes will surprise her next.
''')
add('lab_rival_next_brendan', 'LittlerootTown_ProfessorBirchsLab_Text_BrendanWhereShouldIGoNext', 'Brendan considers where to search for Pokemon next.', '''
N~A whole region of possibilities and only one pair of shoes.|
N~Comparing missing observations with known habitats would narrow the choice.|
N~Go where there's something useful to learn, not merely farther away.|
N~I like having a moment between arriving home and planning to leave again.|
N~I'd check what needs restocking before committing to the next long route.|
S~There is plenty of region left. I suggest he pick a question before attempting to walk through all of it.|
N~An itinerary would give the restless feet some useful supervision.|
N~I'd pick the site that answers the most interesting current question.|
N~The next place need not be distant to be unfamiliar.|
N~A good destination suits the kind of day he actually wants.|
N~I'd ask which place he keeps thinking about even after returning here.
''')
add('lab_may_break', 'LittlerootTown_ProfessorBirchsLab_Text_MayTakeBreakFromFieldwork', 'May pauses outdoor research to help at the lab.', '''
S~A journey can have a useful indoor chapter without becoming less of a journey.|
N~Lab work can organize and interpret the observations fieldwork gathers.|
N~Good change of pace. Rest the feet and finish some useful work.|
S~I like the thought of a familiar room after so many unfamiliar roads.|
N~A steadier day might make proper meals a little easier too.|
N~The professor gets some help, and May gets a little less mud. I hope she also gets a proper chance to rest.|
S~A temporary truce with being indoors. Promising.|
N~I'd ask which field notes she most wants to make sense of.|
S~Something learned far away can take root in a quiet room.|
N~Helping here can be a choice rather than a retreat from what she enjoys.|
S~I'd ask what she is looking forward to learning on this side of the work.
''')
add('lab_brendan_break', 'LittlerootTown_ProfessorBirchsLab_Text_BrendanTakeBreakFromFieldwork', 'Brendan takes a fieldwork break to assist Birch in the lab.', '''
S~Brendan has found a way to keep helping without adding another layer of road dust.|
N~Research benefits from alternating collection with analysis.|
N~A break from the road can still be time well used.|
N~I wonder whether the quiet feels strange after moving around so much.|
N~I'd let the break include actual rest as well as another kind of work.|
N~A useful change of work, provided he remembers that a different task does not automatically count as a holiday.|
S~The chair has finally recruited an investigator.|
N~He can compare results across trips instead of gathering more before reviewing any.|
N~A returning traveler can carry many places into one room.|
N~It's good to see helping the professor treated as its own worthwhile thing.|
N~I'd ask what question he brought home that he wants the lab to answer.
''')
add('lab_may_future', 'LittlerootTown_ProfessorBirchsLab_Text_MayWhatNextImStayingHere', 'May asks about the player future plans and chooses to remain helping Birch.', '''
S~May has chosen her next chapter and leaves ours open for us to choose.|
N~Battling, collecting data, and supporting research are distinct valid goals.|
N~We'll pick our own next step. Glad she has one she wants.|
S~It's nice when friends can take different paths without making it a goodbye forever.|
N~A plan can be worthwhile even when it looks quieter from the outside.|
S~May knows what she wants to do and still asks what interests us. A considerably nicer habit than prescribing our future.|
S~A future with options rather than a compulsory escalation. Civilized.|
N~We can choose according to what interests us, not simply what comes next on a list.|
S~A familiar room and a far road can each hold a living wish.|
N~She asks without trying to make our choice match hers.|
S~I'd ask which part of helping here she wants to get better at.
''')
add('lab_brendan_one_partner', 'LittlerootTown_ProfessorBirchsLab_Text_BrendanPreferCollectingSlowly', 'Brendan prefers patiently raising his chosen partner over broad collecting.', '''
S~One companion can make a very large adventure without a very large head count.|
N~Depth of experience and breadth of sampling are different interests.|
S~Fair choice. Put the time into the partner he knows.|
S~I like hearing somebody enjoy the unhurried part of getting to know a Pokemon.|
S~The familiar everyday habits are a real part of raising someone.|
S~One well-known partner can be excellent company. He need not turn a personal preference into a competitive quantity.|
S~A respectable preference for one known individual over a rapidly expanding guest list.|
N~He can study progress carefully when he keeps returning to the same partner.|
S~Roots grow deep by staying, not only by reaching farther.|
N~That sounds like his own preference rather than a judgment on everyone else's.|
S~I'd ask what small change he has noticed in that partner lately.
''')
add('lab_may_frontier', 'LittlerootTown_ProfessorBirchsLab_Text_MayHaveYouGoneToBattleFrontier', 'May asks whether the player has visited the Battle Frontier.', '''
S~May has heard about another place with a lot of possible stories inside it.|
N~She is asking about a destination, not assuming we have already experienced it.|
N~Worth learning the rules before planning a visit.|
N~I'd want to know what it felt like there before hearing only the results.|
N~A new destination means another reason to check the travel supplies.|
S~She asks as if there is something interesting to hear, not a box we should already have ticked. I like that.|
N~Another location with the word battle in its invitation. How restful.|
N~I'd compare what the facilities offer before deciding which to try.|
N~A distant place begins to feel nearer when a familiar person asks about it.|
N~We can answer honestly without making visiting another obligation.|
S~I'd ask what May has heard that made her curious about the place.
''')
add('lab_brendan_frontier', 'LittlerootTown_ProfessorBirchsLab_Text_BrendanHaveYouGoneToBattleFrontier', 'Brendan asks whether the player has visited the Battle Frontier.', '''
N~The Frontier has apparently reached home in the form of everybody asking about it.|
N~A new challenge merits learning its constraints before treating it like the familiar ones.|
N~We'll go when we're prepared and interested.|
N~It's nice to compare plans without needing to have already been everywhere.|
N~I'd ask where visitors usually rest between the different challenges.|
S~Another tempting destination. I am pleased that the question does not come with an immediate departure time.|
N~The region has found another way to make the itinerary longer.|
N~I'd ask which facility he thinks tests a genuinely different skill.|
N~A new door can wait while we finish looking at the room we're in.|
N~No need to make the answer impressive. It is a conversation, not a progress report.|
N~I'd ask whether Brendan has been and what surprised him most.
''')
add('lab_complete_choice', 'LittlerootTown_ProfessorBirchsLab_Text_CompletedDexChoosePokemon', 'Birch confirms the completed Hoenn Pokedex and offers a choice of rare regional partners; no choice is yet made.', '''
U~All those meetings have become a completed book, and now there may be one new hello.|
S~He has verified the completed regional record and offers a separate future responsibility.|
N~That's real work recognized. Take time choosing the new partner.|
S~I think I'd want a quiet moment to take in the finished record first.|
N~A living thank-you deserves a proper place in our plans.|
S~A wonderful acknowledgment, and a decision worth making carefully. The Pokemon is a future companion, not a ceremonial accessory.|
S~A remarkably substantial reward with substantially more needs than a medal.|
N~We should learn about each species before accepting the care of one.|
S~An ending can offer a new life beside the road rather than close the road.|
N~The achievement is ours already. We don't need to hurry the next decision.|
S~I'd ask Birch what each partner is like in an ordinary day.
''')
add('lab_choice_repeat', 'LittlerootTown_ProfessorBirchsLab_Text_CanHaveAnyOneOfRarePokemon', 'Birch reiterates the still-open choice among three rare regional Pokemon.', '''
S~Three possible new friends, and thankfully nobody has put a timer beside them.|
N~The offer remains open. No species has been selected by this conversation.|
N~Meet them, learn what they need, then decide.|
N~It is a big choice even after a very long journey.|
N~I'd think about the home and routine we can actually offer.|
N~There is no prize for answering fastest. There may be a very happy partner if we answer thoughtfully.|
N~Three excellent candidates for a responsibility larger than a collection slot.|
N~Compare temperament and care needs, not only battle possibilities.|
N~A willing companion is a life, not punctuation at the end of a record.|
N~There is room to appreciate all three without pretending we can accept everyone.|
N~I'd ask which one Birch thinks enjoys traveling most.
''')
add('lab_choice_time', 'LittlerootTown_ProfessorBirchsLab_Text_TakeYourTimeAllInvaluable', 'After declining a particular Johto choice, Birch encourages an unhurried decision.', '''
S~He knows a good partner is worth more than a quick answer.|
N~An irreversible responsibility benefits from an unhurried comparison.|
N~Good. No need to choose while we're unsure.|
S~I like being allowed to care about the decision without looking indecisive.|
N~We should choose when the plan for looking after them feels clear.|
S~A professor recommending patience. I shall cherish this rare encounter with sensible authority.|
N~A rare authority figure correctly prescribing more time.|
N~We can ask another practical question instead of treating hesitation as failure.|
S~A patient hand is a kinder beginning than a hurried reach.|
N~Every option can be precious without one being right for us today.|
N~I'd spend a little time noticing how each Pokemon responds around people.
''')
add('lab_after_johto', 'LittlerootTown_ProfessorBirchsLab_Text_GrassyPatchWaiting', 'After a successful Johto partner gift, Birch says the completed regional record does not end the journey.', '''
S~The book is complete, but the grass outside has never learned to stop being interesting.|
S~A completed catalog does not exhaust what can be observed about its subjects.|
N~Good reason to keep learning. No reason to rush.|
S~I like a finished task that still leaves us somewhere gentle to go tomorrow.|
N~A new partner also gives familiar places something new to teach us.|
S~An achievement can be finished while curiosity remains active. A merciful alternative to inventing another urgent deadline.|
S~The world has regrettably refused to become fully explained by a checklist.|
N~We can revisit a known habitat with better questions and a different team.|
S~The same green patch can hold a new meeting on another morning.|
N~Finishing something doesn't mean we have to stop enjoying it.|
S~I'd choose one familiar place to visit again without a list to complete.
''')
add('lab_after_champion', 'LittlerootTown_ProfessorBirchsLab_Text_GrassyPatchWaiting2', 'After the National upgrade, Birch reminds the Champion that Pokemon journeys continue.', '''
S~Champion sounds enormous, but there's still ordinary grass willing to surprise us.|
S~A title marks an achievement without removing future opportunities to learn.|
N~We can set the next goal ourselves now.|
S~It is a relief to hear the journey can keep being curious instead of always grand.|
N~Maybe the next good day can be a walk, a meal, and a quiet new meeting.|
S~I approve of the next adventure being allowed to begin in ordinary grass rather than somewhere dramatically inconvenient.|
S~A prestigious title has failed to frighten the grass into predictability.|
N~New records can begin from close observation instead of another bigger challenge.|
S~A high peak does not use up every small path below it.|
N~We can enjoy being here without turning the title into a daily performance.|
S~I'd like to hear which ordinary place Birch would revisit first.
''')
add('lab_rest_home', 'LittlerootTown_ProfessorBirchsLab_Text_BirchRivalGoneHome', 'Birch guesses where the rival is and recommends resting at home when tired.', '''
N~His directions contain a little uncertainty, but the rest advice is perfectly clear.|
N~He offers two possible locations and one dependable recovery option.|
N~Check home if we need rest. We don't have to keep searching tired.|
S~It's nice when the answer includes remembering we're people who get worn out.|
N~A familiar doorstep and a meal can improve the next part of the day.|
N~Birch is uncertain about his child and certain about the value of rest. We can use the reliable half of the answer.|
N~An ambiguous location paired with an excellent excuse to sit down.|
N~We can separate the search for the rival from our own need to recover.|
N~A road can wait while home takes us in for a little while.|
N~He makes taking a break sound ordinary, which it should be.|
N~I'd check in at home before setting out on another guess.
''')
add('lab_birch_restless', 'LittlerootTown_ProfessorBirchsLab_Text_CountlessPokemonAwait', 'Birch encourages exploration and admits he is eager to return to fieldwork himself.', '''
S~He's trying to send us exploring, but his own feet seem to be volunteering first.|
S~His enthusiasm for new observations remains active despite his experience.|
S~Good to see him still curious. We can take the next route at our own pace.|
S~I like it when someone's work still makes them want to get up and go.|
N~I'd make sure he packs lunch before following that itch into the grass.|
S~He is enthusiastically recommending the precise activity he would rather be doing himself. Refreshingly transparent.|
S~A scientist visibly resisting an argument with his own chair.|
N~I'd ask which unanswered question is pulling him outside today.|
S~A familiar world can keep offering a new reason to look closely.|
N~His enthusiasm is inviting as long as we still get room to choose.|
S~I'd love to hear where he would go if he could leave right now.
''')

add('root_pc_science', 'LittlerootTown_Text_CanUsePCToStoreItems', 'A townsman admires PC storage for items and Pokemon.', '''
U~Science has given traveling pockets a rather impressive set of assistants.|
S~Remote storage is useful precisely because a traveler cannot carry everything comfortably.|
N~Useful system. Keep track of what we actually have with us.|
N~It is easy to forget how strange an everyday convenience seemed the first time.|
N~Not carrying the whole pantry is a real improvement to a journey.|
S~An ordinary errand receives an unexpectedly grand tribute to human ingenuity.|
S~A remarkable machine devoted partly to the ancient problem of too much stuff.|
N~A good interface should make the location of each thing clear.|
N~A small corner can offer a little more room to a crowded journey.|
N~A useful thing deserves appreciation even after it becomes familiar.|
S~I'd ask what he first stored when he learned the system existed.
''')
add('root_birch_home', 'LittlerootTown_Text_BirchSpendsDaysInLab', 'A boy wonders when Birch makes time for home between lab work and field research.', '''
N~The professor's schedule sounds full enough to need its own map.|
N~Alternating work locations is not necessarily the same as taking time away from work.|
N~A busy job still needs room for home.|
N~It's a thoughtful question to ask about someone who's always doing something.|
N~I hope somebody reminds him that a meal at home counts as a worthwhile plan.|
N~The tireless researcher may need an appointment with his own front door.|
N~Two workplaces are not a holiday from either.|
N~He could schedule actual time off instead of calling a change of location a break.|
N~A familiar light may be waiting while a curious mind keeps following another question.|
N~His family probably wants some of the ordinary person behind the important work.|
N~I'd ask whether Birch ever talks about what he enjoys doing at home.
''')
add('root_grass_warning', 'LittlerootTown_Text_IfYouGoInGrassPokemonWillJumpOut', 'The twin warns that wild Pokemon emerge from tall grass.', '''
N~The grass is not empty scenery. It apparently has a guest list with surprise arrivals.|
N~Vegetation provides cover for creatures that may not be visible from the path.|
N~Look ahead and keep a safe way back.|
N~Something familiar-looking can feel different when you know someone might be inside it.|
N~A little warning helps a beginner prepare instead of panic.|
N~The scenery has been introduced as an active participant in the outing.|
N~Grass with occupants. An important footnote to a peaceful walk.|
N~We should know the route before stepping into an unfamiliar patch.|
N~A green surface can keep many small lives from view.|
N~The child is trying to make sure we know what other people assume.|
N~I'd ask which Pokemon they've actually seen near the edge of town.
''')
add('root_no_partner', 'LittlerootTown_Text_DangerousIfYouDontHavePokemon', 'The twin keeps an unaccompanied beginner from entering dangerous grass.', '''
N~The little guard is taking a very large responsibility seriously.|
N~The warning concerns a lack of support in an environment with wild encounters.|
N~Listen to the warning. We can prepare before going out.|
N~I'd rather be stopped kindly than discover the risk alone.|
N~There is no shame in waiting until we have the help we need.|
N~The shortest person present has supplied the most sensible travel policy.|
N~A safety lecture with an unusually small lecturer. Still correct.|
N~We need a safer plan rather than a way around the person warning us.|
N~A path can wait until the traveler is ready to meet it.|
N~They're trying to protect us, not embarrass us.|
N~I'd ask who nearby can help us prepare properly.
''')
add('root_cries_help', 'LittlerootTown_Text_CanYouGoSeeWhatsHappening', 'The twin hears alarming Pokemon cries and asks the player to investigate.', '''
N~The child heard something wrong and had the sense to ask for help.|
N~An unusual sound is evidence of a disturbance, though its cause is not yet known.|
N~We should check carefully. Don't send the kid toward it.|
D~I don't like hearing fear from somewhere I can't quite see.|
N~Let's find out whether somebody needs help before guessing at the noise.|
N~A quiet town has acquired a problem loud enough to interrupt an ordinary afternoon.|
N~An alarming sound and an honest admission of limited equipment. Sensible child.|
N~Approach with a clear view and keep an escape route available.|
N~A cry can pull a thread from one small life toward another.|
N~They were right to say they couldn't handle it alone.|
N~I'd listen for where the sound is coming from before we move closer.
''')
add('root_birch_saved', 'LittlerootTown_Text_YouSavedBirch', 'After the rescue, the twin expresses relief that Birch is safe.', '''
S~The scary sound has become a happy little piece of news.|
S~The child now knows the person in danger received help.|
S~Good. No need for them to keep worrying at the edge of town.|
S~You can hear the relief more clearly than the words.|
S~I'm glad somebody came back with an answer the child could feel good about.|
S~The worried witness has finally been allowed a favorable ending.|
S~An anxious question has received a much better answer than more noise.|
N~They helped by noticing the problem and asking for support.|
S~A frightened little moment has found its way back toward ordinary daylight.|
S~They should know asking for help mattered too.|
S~I'd tell them Birch is safe without making the danger sound exciting to imitate.
''')
add('root_good_luck', 'LittlerootTown_Text_GoodLuckCatchingPokemon', 'Once the adventure begins, the twin wishes the player luck.', '''
S~Our very small town guard has become our very small cheering section.|
S~A simple good wish can mark a change from concern to confidence.|
S~Thanks. We'll take care out there.|
S~I like a goodbye that makes the road feel a little friendlier.|
S~A kind little send-off is a good thing to carry into the day.|
S~The former gatekeeper now endorses the adventure. Excellent progression.|
S~A brief blessing from the local authority on grass hazards.|
N~We can keep the earlier safety advice alongside the encouragement.|
S~A voice from home can remain warm after the town is out of sight.|
S~They look happy that we get to try something new.|
S~I'd wave back so they know we heard them.
''')
add('mom_new_room', 'PlayersHouse_2F_Text_HowDoYouLikeYourRoom', 'After moving in, Mom admires the tidy room and asks the player to check the desk belongings.', '''
S~A new room gets familiar one little thing on the desk at a time.|
N~Checking belongings after a move is a sensible final step before assuming everything arrived.|
S~Good. Let's make sure the important things are here.|
S~It is nice when a strange new place starts having your own small corners.|
N~The movers did the hard part. We can finish by noticing what might be missing.|
S~The unfamiliar setting has been furnished with the beginnings of a home.|
S~A neat desk. A temporary but admirable condition.|
N~We should check the essentials before settling everything permanently in place.|
S~A room becomes ours through the little things that recognize our hands.|
S~She wants us comfortable here, not merely unpacked.|
S~I'd take a quiet look around before the next busy part begins.
''')
add('mom_movers', 'PlayersHouse_1F_Text_MoversPokemonGoSetClock', 'Mom credits the Pokemon movers and sends the player upstairs to set a new clock.', '''
S~The movers carried a whole household, and our assignment is to help time move in too.|
N~A clock is a small practical anchor when the rest of a routine has changed.|
N~Thank the movers. Then we can sort the room upstairs.|
S~A new clock feels like the house is ready to start sharing our days.|
N~I hope the Pokemon who did the heavy work get a proper break.|
S~The move concludes with the modest ceremony of telling the new room what time it is.|
N~An impressive labor force rewarded, I trust, with more than compliments.|
N~Check the time carefully once so it won't be a nuisance later.|
S~An unfamiliar house can begin to keep familiar hours.|
N~Convenience should include care for the ones doing the carrying.|
N~I'd ask whether there is anything small we can help tidy before going upstairs.
''')
add('mom_see_room', 'PlayersHouse_1F_Text_ArentYouInterestedInRoom', 'Mom encourages the player to look at their new room.', '''
S~She has been waiting to show us a little place that's especially ours.|
N~A personal space can make a larger move feel more manageable.|
S~Worth a look. We've come a long way to get here.|
F~I might linger at the door for a moment before it feels like my room.|
S~There is comfort in knowing where you'll put your bag at the end of the day.|
S~The host requests an audience for the most personal part of the new setting.|
S~A room without an audience. A promising invitation.|
N~We can check the layout before deciding where everyday things should go.|
S~A new threshold can feel gentle when someone is glad to show it to us.|
S~She sounds excited about giving us somewhere comfortable.|
S~I'd notice what she thought to put there before we arrived.
''')
add('mom_nice_house', 'PlayersHouse_1F_Text_IsntItNiceInHere', 'Mom enjoys the new house and invites the player to appreciate it.', '''
S~She wants the unfamiliar walls to hear a friendly first opinion.|
S~Shared approval can make settling into a new environment easier.|
S~Looks like a good place to come home to.|
S~It takes a little time, but I can see what she means.|
S~A house feels nicer once you can imagine the ordinary mornings in it.|
S~The new household receives an enthusiastic review from its first resident critic.|
S~A pleasant room before daily clutter develops its full ambitions.|
N~The space looks workable. I'd ask which practical detail she is happiest with.|
S~Warmth often arrives before familiarity does.|
S~I like that she wants us to enjoy the move, not just endure the boxes.|
S~I'd ask which little part made it feel like home to her first.
''')
add('mom_neighbor_intro', 'PlayersHouse_1F_Text_GoIntroduceYourselfNextDoor', 'After the missed television report, Mom recommends meeting Professor Birch next door.', '''
S~A whole new neighborhood starts with one hello through the next door.|
N~An existing family connection can make the first introduction less uncertain.|
N~Easy place to start. We can introduce ourselves politely.|
F~Next door is a manageable distance for meeting someone new.|
N~I'd avoid arriving at the exact moment they're trying to eat.|
S~The next scene is conveniently located within one neighborly walk.|
S~A social obligation with excellent geographic restraint.|
N~We can ask who is home rather than assume the professor is there.|
S~A short path can begin a long acquaintance.|
N~A familiar connection helps, but we still get to make our own impression.|
S~I'd ask Mom what Birch is like before knocking.
''')
add('mom_birch_met', 'PlayersHouse_1F_Text_DidYouMeetProfBirch', 'Mom asks whether the player introduced themselves to Birch.', '''
N~The first neighborly errand has become a perfectly ordinary question from home.|
N~She is checking whether a specific introduction happened, not demanding an accomplishment.|
N~Tell her how it went. She wanted us to have a friendly contact nearby.|
S~It is nice when somebody cares about the small beginning of your day.|
S~An ordinary update can help a new place feel less unfamiliar for both people.|
N~The introductory mission receives a brief domestic follow-up.|
S~A mercifully simple request for a progress report.|
N~If he was out, we can say so and ask when to try again.|
S~A little shared news can tie a house to the street around it.|
S~She wants to know we aren't quite strangers here anymore.|
N~I'd tell her one detail from the visit rather than just yes or no.
''')
add('mom_home_open', 'PlayersHouse_1F_Text_DontPushYourselfTooHard', 'Mom encourages the journey while reminding the player they can always return home.', '''
S~Home isn't a place we have to earn our way back into. That's good to remember.|
S~A reliable place to recover makes exploration less costly when plans go badly.|
N~Listen to her. Come back before exhaustion makes the decision for us.|
S~I like knowing the door stays open even on the days we don't have a proud story.|
S~A meal and a familiar chair can be a very important part of an adventure.|
S~The journey receives permission to pause without being judged unfinished.|
S~A standing invitation to retreat into comfort. Sensible family policy.|
N~We should treat home as a real option, not only an emergency fallback.|
S~A path can stretch far while one doorway remains near inside us.|
S~Her encouragement leaves room for us to be tired, which makes it kinder.|
S~I'd make sure she knows we heard the offer, not only the send-off.
''')
add('mom_after_rest', 'PlayersHouse_1F_Text_TakeCareHoney', 'After healing the team at home, Mom sends the player off with care.', '''
S~Rested partners, a warm goodbye, and one less reason to hurry.|
S~The recovery is complete; the next stretch can begin from a better condition.|
S~Good break. Let's take that care onto the road too.|
S~A familiar voice makes leaving a little easier.|
S~The ordinary comforts have done their work. We should let ourselves appreciate it.|
S~The domestic interlude ends with a small blessing rather than a grand command.|
S~A well-rested departure. I approve of the improvement.|
N~We can check the route calmly now that everyone has recovered.|
S~A little warmth can follow us past the threshold.|
S~I like that she makes caring sound ordinary instead of exceptional.|
S~I'd turn back for a proper goodbye before walking off.
''')
add('mom_brief_goodbye', 'PlayersHouse_1F_Text_SeeYouHoney', 'Mom offers a simple goodbye during the early home visit.', '''
S~A little goodbye with the next hello already tucked inside it.|
S~An expected return changes the feeling of a departure.|
S~We'll be back. Take the road carefully.|
S~I like the quiet certainty in see you.|
S~A familiar person expecting you back is a good reason to look after yourself.|
S~The scene closes without pretending the relationship has ended.|
S~A concise farewell. Even I can leave that without an awkward reply.|
N~We can let her know if the day's plans change.|
S~A door can stay open in the sound of a goodbye.|
S~It is warm without trying to hold us in place.|
S~I'd wave so she doesn't have to wonder whether we heard.
''')
add('mom_unknown_world', 'PlayersHouse_1F_Text_StillUnknownPokemon', 'After the flying Pokemon broadcast and color choice, Mom marvels that unknown Pokemon remain.', '''
U~Even the familiar sky still has somebody nobody can quite introduce yet.|
S~A well-known region can retain undocumented or poorly understood life.|
N~Interesting report. We'll keep our eyes open without chasing every rumor.|
S~I like that a quiet evening at home can suddenly make the outside feel enormous.|
N~A good discovery starts with noticing, not deciding the answer before meeting it.|
S~The world interrupts a domestic evening to announce an unfinished cast list.|
S~The catalog has failed to eliminate surprise. Excellent news.|
N~We should distinguish the actual sighting from the uncertain identification.|
S~A familiar window can still open onto something unnamed.|
N~Her delight makes the unknown feel inviting rather than something to possess.|
S~I'd ask what she imagines when she hears about it.
''')
add('root_mom_shoes_sendoff', 'LittlerootTown_Text_ComeHomeIfAnythingHappens', 'After giving Running Shoes, Mom celebrates the first partner and offers home as a refuge.', '''
S~She is proud, worried, and helping our feet anyway. That's a lot of love in one goodbye.|
S~Her support combines practical equipment with an available place to recover.|
N~Take the encouragement and the warning. We don't have to be brave every minute.|
S~I like being sent out without being made to feel we have to stay away.|
N~We should bring ourselves and the partner home for a good rest sometimes.|
S~The departure is blessed by someone who also keeps the return path open.|
S~An adventure approved with a sensible right of withdrawal.|
N~Good shoes help, but the pace should still fit the team's condition.|
S~A loving hand can help tie the shoes and still let the road begin.|
S~Her pride doesn't make her forget the ordinary person doing the walking.|
S~I'd look back once before the house slips out of sight.
''')

add('rival_mom_intro', 'RivalsHouse_1F_Text_OhYoureTheNewNeighbor', 'The rival mother welcomes the new neighbor and points toward her child upstairs.', '''
S~Our arrival has been turned into somebody else's hoped-for new friend.|
S~A shared neighborhood and similar age offer a starting point, not a guaranteed friendship.|
S~Friendly welcome. We can go say hello without making it a big event.|
F~It's reassuring to know the other person may have been nervous about meeting us too.|
S~A kind introduction takes a little of the awkwardness out of a new door.|
S~The neighboring household has prepared a remarkably hopeful welcome for a stranger.|
S~A new acquaintance located one staircase away. Manageable.|
N~We should introduce ourselves instead of assuming they already know everything about us.|
S~Two unfamiliar days can meet through one open doorway.|
S~She makes us sound welcome before we've done anything impressive. I like that.|
S~I'd ask her child's name once more before going upstairs.
''')
add('rival_mom_family', 'RivalsHouse_1F_Text_LikeChildLikeFather', 'The rival mother describes Birch and their child shared enthusiasm for Pokemon.', '''
S~This family has apparently inherited a very strong urge to investigate the nearest grass.|
S~A shared interest can be learned and enjoyed across generations.|
N~Good that they share it. Hope they remember to come home too.|
S~She sounds fond of a habit that probably gets mud everywhere.|
N~I'd guess the household has become very good at packing lunches.|
S~The family resemblance is easiest to spot in the direction they both wander.|
S~A hereditary shortage of interest in sitting still.|
N~I'd ask which parts of the work they each enjoy differently.|
S~The same curiosity can grow in more than one familiar face.|
N~Shared interests still leave room for the child to choose a distinct path.|
S~I'd love to hear which one first taught the other something new.
''')
add('rival_mom_busy', 'RivalsHouse_1F_Text_TooBusyToNoticeVisit', 'The rival mother says Pokemon have distracted her child from the player visit.', '''
N~A very interesting Pokemon can make an entire visitor temporarily invisible.|
N~Focused attention sometimes excludes social signals that would otherwise be obvious.|
N~We can say hello clearly or leave them to the task. No need to take it personally.|
F~I know the feeling of looking up and discovering someone has been waiting.|
N~A gentle reminder works better than treating it like an insult.|
N~The engrossed scholar has accidentally edited the visitor out of the room.|
N~An impressive field of selective perception.|
N~We could ask when would be a less distracting time to visit.|
N~A mind following one bright thing may miss the quiet knock beside it.|
N~I would give them a chance to notice without making them feel scolded.|
N~I'd ask what has caught their attention so completely.
''')
add('rival_mom_route103', 'RivalsHouse_1F_Text_WentOutToRoute103', 'The rival mother directs the player to Route 103 and fondly notes the family restlessness.', '''
N~A specific route is much better than somewhere with grass.|
N~A recent departure and named destination provide a useful search lead.|
N~Route 103. We can prepare for the trip before following.|
N~It's nice to have someone know where the person we want went.|
N~I'd check our supplies rather than turn a visit next door into an unplanned hungry walk.|
N~The absent character has left us a reasonably specific next page.|
N~The family's outdoor tendency has once again outpaced the visitor.|
N~We should learn the route's layout before assuming it is a short errand.|
N~A friend's trail can lead a little beyond the familiar houses.|
N~She sounds used to the movement without being cross about it.|
N~I'd ask which way they usually enter the route.
''')
add('rival_mom_check_home', 'RivalsHouse_1F_Text_ShouldGoHomeEverySoOften', 'The rival mother encourages travel but advises reassuring the player mother with home visits.', '''
S~A short hello at home can be a very large answer to someone else's quiet worry.|
N~Regular contact reduces uncertainty without requiring the journey to stop.|
N~Good advice. We can let home know we're all right.|
S~It's easy to forget how long a quiet afternoon can feel to the person waiting.|
N~A message and a meal together can do both people good.|
N~The traveler is reminded that departure leaves another story running at home.|
N~A sensible requirement for occasionally reporting that we remain intact.|
N~We could agree on a check-in rather than leave the timing to chance.|
S~A far road can keep one small thread tied to a familiar door.|
N~Reassurance is kindest when we offer it before somebody has to ask.|
N~I'd ask when our mother last had a clear update from us.
''')
add('rival_sibling_partner', 'RivalsHouse_1F_Text_DoYouHavePokemon', 'The rival sibling asks whether the new neighbor already has a Pokemon.', '''
S~In this neighborhood, asking about your Pokemon seems to come right after hello.|
N~The question opens a concrete topic between unfamiliar people.|
S~Easy enough to answer. We can introduce the partner if they're comfortable.|
F~I like having something kind to talk about when names still feel new.|
S~A friendly question can make a doorway feel less like somebody else's territory.|
S~The new neighbor receives the locally standard preliminary interview.|
S~A social introduction with an appealingly specific subject.|
N~We can explain what we've learned about our particular partner so far.|
S~A small curious question can make room for a new friendship.|
S~They are interested without assuming what we should have done already.|
S~I'd ask whether they have a favorite Pokemon too.
''')
add('rival_may_first', 'RivalsHouse_1F_Text_MayWhoAreYou RivalsHouse_2F_Text_MayWhoAreYou', 'May nervously welcomes the new neighbor, hopes for friendship, then remembers helping Birch.', '''
S~She managed a hello, a whole dream, and an overdue errand in one nervous breath.|
S~She states a wish for friendship without pretending the relationship already exists.|
S~Friendly start. Let her get to her work; we can talk again.|
F~I understand saying too much because you really want the first meeting to go well.|
S~It's sweet that she hoped we'd be nice before she knew anything impressive about us.|
S~An earnest introduction briefly races ahead of its own confidence.|
S~A charmingly crowded sentence has remembered its appointment at last.|
N~We can meet again when neither person has somewhere else to rush.|
S~A small beginning can be bright without knowing what it will become.|
S~I'd meet the openness gently instead of teasing the nervousness.|
S~I'd remember the dream she chose to tell a stranger first.
''')
add('rival_brendan_first', 'RivalsHouse_1F_Text_BrendanWhoAreYou RivalsHouse_2F_Text_BrendanWhoAreYou', 'Brendan corrects his assumption about the neighbor gender, offers catching help, and remembers his errand.', '''
F~He guessed wrong, introduced himself, offered a Pokemon, and remembered work. Busy hello.|
N~The initial assumption was unsupported. At least the real introduction can begin now.|
N~Now he knows who we are. We can take the friendly offer in that spirit.|
F~I think we'd both do better with a quieter second conversation.|
N~Being a Gym Leader's child doesn't tell somebody everything about you.|
N~An introduction has survived several rapid revisions and an interrupted act of generosity.|
N~A remarkable amount of mistaken certainty in the opening minute. Recoverable.|
N~We can learn about each other directly instead of leaning on family descriptions.|
N~A first impression can be corrected while the door is still open.|
N~I'd let him move past the mistake while keeping room for us to be ourselves.|
N~I'd ask about the errand next time, when he isn't rushing to remember it.
''')
add('rival_may_packing', 'RivalsHouse_2F_Text_MayGettingReady', 'May checks her Pokemon and packed items before leaving.', '''
S~An adventure beginning with a checklist. My favorite kind of preventable disaster prevention.|
S~Checking readiness before departure reduces avoidable field problems.|
N~Good routine. Finish the check before getting distracted.|
N~It's a reassuring little sound, hearing someone make sure they're ready.|
N~I'd add something to eat before the list is declared complete.|
N~The thrilling expedition pauses for its deservedly boring preparations.|
S~A heroic inventory of basic competence. Refreshing.|
N~A consistent check helps more than trusting a vague feeling of readiness.|
N~The first careful step can happen before the front door.|
N~I'd let her finish rather than make her start the count again.|
N~I'd ask what she always checks twice before a long outing.
''')
add('rival_brendan_packing', 'RivalsHouse_2F_Text_BrendanGettingReady', 'Brendan checks restored Pokemon and equipment before leaving.', '''
N~His feet may be ready, but he's sensibly asking the bag and the team as well.|
S~Independent checks of team condition and equipment cover different failure modes.|
N~Good. An early check beats a late walk back.|
N~I like the quiet pause before a place stops feeling nearby.|
N~I'd make sure the water and food got the same attention as the Balls.|
N~The would-be explorer begins with the unromantic art of not forgetting things.|
S~Preparation has interrupted haste before haste becomes a story.|
N~I'd keep the checklist short enough to use every time.|
N~A journey is helped by the small things we remember before it begins.|
N~He is taking the partner's condition into account before his own eagerness.|
N~I'd ask what he learned to pack after the last unexpected problem.
''')
add('rival_may_dex_home', 'RivalsHouse_2F_Text_MayJustCheckingMyPokedex', 'May reviews uncaught and potentially evolving Pokemon while considering another trip.', '''
N~Her list contains both places to go and possibilities already sitting beside her.|
S~Missing observations may come from travel or from following the development of known partners.|
N~Good to review what she already has before rushing out for more.|
S~A quiet look at old notes can make the next day feel full of possibilities.|
N~I'd give the team time to settle before deciding on another long trip.|
S~The field notes suggest several next chapters, including one much closer to home.|
N~The catalog has become an itinerary with several competing destinations.|
N~We can separate what needs a different habitat from what needs patient raising.|
N~A familiar creature may still hold a future we haven't met.|
N~It's nice that growth counts as a discovery, not only the new arrival.|
N~I'd ask which possible evolution she is most curious to see.
''')
add('rival_brendan_dex_home', 'RivalsHouse_2F_Text_BrendanJustCheckingMyPokedex', 'Brendan takes pride in his growing Pokedex and feels eager to travel again.', '''
S~The pages have done the dangerous thing of reminding his shoes they have a job.|
S~Reviewing completed observations can motivate the next round of fieldwork.|
N~Good progress. Plan the next outing before the urge makes all the decisions.|
S~I like seeing someone pleased with what's there as well as curious about what's missing.|
N~Enjoy the return home long enough to restock and rest.|
S~The record of past adventures has begun recruiting him for another.|
S~An encyclopedia with a suspiciously effective ability to make people stand up.|
N~He can choose the next question from the notes rather than wander without a purpose.|
N~A small page can hold enough remembered road to make a room feel brief.|
N~Pride in the effort is healthy when it doesn't forbid a pause.|
S~I'd ask which entry brings back the clearest memory for him.
''')
add('rival_may_chance_meet', 'RivalsHouse_2F_Text_MayWhereShouldIGoNext', 'May wonders where to search and imagines unexpectedly meeting the player.', '''
S~A big region can suddenly feel small when a familiar face appears on the path.|
S~Overlapping interests make an unplanned meeting more plausible than pure chance.|
S~Could happen. We'd stop to say hello.|
S~I like the thought of somebody hoping to run into us out there.|
S~An unexpected friend is a good reason to pack one extra little snack.|
S~The next setting may include a pleasantly unscheduled reunion.|
S~A coincidence that would at least have sensible geographic reasons.|
N~We can tell her our rough plans without needing to turn it into an appointment.|
S~Two wandering paths can keep a little room for crossing.|
S~She makes the possible meeting sound warm rather than competitive.|
S~I'd ask where she'd most enjoy taking a quiet break if we did meet.
''')
add('rival_brendan_meet_battle', 'RivalsHouse_2F_Text_BrendanWhereShouldIGoNext', 'Brendan considers a catching trip and offers a friendly battle if paths cross.', '''
S~In Brendan's version of a chance meeting, hello comes with a battle attached.|
N~The offer is conditional and optional. No challenge has been accepted yet.|
S~A friendly battle's fine if both teams are ready when we meet.|
F~I'd like enough warning to make sure everyone is comfortable first.|
N~We can have a good meeting even if the partners need a break.|
S~The prospective reunion has an optional action scene penciled in.|
S~A social plan with remarkably predictable escalation.|
N~I'd check our partners' condition instead of treating the encounter itself as consent.|
N~Two paths can cross without either being required to clash.|
N~It's nice that he leaves room for whether we'd actually like to.|
S~I'd ask where he plans to explore, then see what the day brings.
''')

add('birch_rating_cancel', 'gBirchDexRatingText_Cancel', 'The player declines a rating; Birch assumes the record is too small to review.', '''
N~We said not now, not please estimate the contents of our book without opening it.|
N~Declining a review doesn't establish how many observations we have collected.|
N~We can choose when to show him. No explanation needed.|
F~I might simply not feel like being assessed today.|
N~A quiet visit can stay a quiet visit without a report attached.|
N~A bold conclusion from a closed book. Even I usually open the first page.|
N~The unexamined record has received a remarkably confident preliminary review.|
N~We can return when we actually want the feedback.|
N~A page does not become empty because it isn't offered to another pair of eyes.|
N~He could let a refusal remain a refusal instead of dressing it as inadequacy.|
N~I'd tell him we'll ask when we're ready and leave it there.
''')
add('birch_rating_grass', 'gBirchDexRatingText_LessThan10', 'Birch recommends more careful observation in grassy habitats.', '''
N~The grass probably has more to show us if we stop treating every patch like a hallway.|
S~Slower observation can reveal species missed during a direct crossing.|
N~Look carefully and keep a safe path. No need to rush the early learning.|
S~A small movement is easier to see when you give the place a quiet moment.|
N~I'd take enough supplies to stay comfortably instead of hurrying back hungry.|
N~The advice costs nothing but attention, which is inconveniently easy to spend elsewhere.|
N~An invitation to stare at grass with academic intent. Acceptable.|
N~We can compare edges, dense patches, and different times rather than repeat one approach.|
N~A green place can become unfamiliar when we really begin to look.|
N~The useful part is care in looking, not making the first page seem embarrassing.|
S~I'd start by noting which sounds come from which parts of the grass.
''')
add('birch_rating_learning', 'gBirchDexRatingText_LessThan20', 'Birch recognizes emerging catching skill but warns later work becomes harder.', '''
S~We've learned the first handful of tricks. The Pokemon have apparently saved more tricks for later.|
N~Early fluency is progress, even when the remaining cases are less familiar.|
N~Good start. Keep preparing instead of assuming every meeting will be the same.|
N~I like being allowed to feel pleased before hearing what still lies ahead.|
N~The next difficult bit will be easier with a rested team and steady habits.|
S~An encouraging review with the sensible warning that the world has not run out of surprises.|
N~Competence has arrived. Convenient universal competence remains unavailable.|
N~We can build on the method while adapting it for different situations.|
N~A first sure step is still worth taking before the road bends.|
N~Growing confidence should leave room for questions.|
N~I'd ask which later challenge he thinks is most worth preparing for.
''')
add('birch_rating_places', 'gBirchDexRatingText_LessThan30', 'Birch advises persistence because some Pokemon inhabit particular places.', '''
N~The missing Pokemon may have very specific ideas about where to receive visitors.|
S~Distribution is uneven. Revisiting the same habitat won't answer every gap.|
N~Try the right place, then give it time.|
N~It helps to know not finding someone doesn't always mean you looked badly.|
N~I'd ask a local before spending all day searching the wrong patch.|
N~Persistence is admirable once it has stopped knocking at the wrong address.|
N~A rare guest cannot be expected at every ordinary doorway.|
N~We should compare habitat information before repeating the search.|
N~A particular life may belong to one small corner of a wide region.|
N~Careful searching includes knowing when the place needs to change.|
N~I'd ask which specific habitat the current record has overlooked.
''')
add('birch_rating_shape', 'gBirchDexRatingText_LessThan40', 'Birch says the growing record is starting to resemble a substantial Pokedex.', '''
S~The little list is beginning to stand up and look like a proper book.|
S~The record is gaining enough breadth to show a recognizable collection.|
N~Progress is progress. Keep the observations useful, not only numerous.|
N~I would enjoy noticing the page that first made it feel different.|
N~A lot of small good outings can quietly become something substantial.|
S~It has apparently passed the important examination of looking like itself.|
S~The encyclopedia has achieved a convincing resemblance to an encyclopedia.|
N~We can review which kinds of habitat are represented and which remain sparse.|
N~A pattern can begin to appear before the empty spaces are all filled.|
N~I'd let the praise land without making the missing quantity the whole subject.|
S~I'd look back at the first entry and see what we notice differently now.
''')
add('birch_rating_effort', 'gBirchDexRatingText_LessThan50', 'Birch praises the developing record and urges continued effort.', '''
S~A simple well done feels good after all those ordinary careful looks.|
S~Sustained effort is producing an observable increase in the record.|
N~Good work. Keep the pace one the team can actually sustain.|
S~I like praise that leaves the next step quiet enough to take.|
N~Keep going also needs to include meals and days with less walking.|
S~I accept this favorable review on behalf of our extremely hardworking shoes.|
S~Progress has been acknowledged without an elaborate additional demand. Pleasant.|
N~We can keep the useful habits and adjust whatever has become inefficient.|
S~Many small acts of attention can gather into a steady path.|
N~Effort is easier to continue when you let yourself recognize what it has done.|
S~I'd ask which part of the record he finds most interesting so far.
''')
add('birch_rating_fishing', 'gBirchDexRatingText_LessThan60', 'Birch suggests using fishing rods to investigate sea Pokemon.', '''
S~The shore has a whole second guest list underneath the part we can see.|
S~Fishing samples a habitat that walking through grass cannot cover.|
N~Bring the proper rod and choose a safe spot.|
N~A little waiting by the water might be a good change of pace.|
N~I'd pack something to eat if the plan includes patient sitting.|
S~The next research proposal arrives with an unusually good excuse to sit down.|
S~Fieldwork with a chair-adjacent possibility. Increasingly persuasive.|
N~Different rods and locations can produce different encounters.|
N~A quiet surface can keep a very busy world beneath it.|
N~An unfamiliar method can be worth trying without making every bite an obligation.|
S~I'd ask a local fisher what they've found in these waters recently.
''')
add('birch_rating_evolution', 'gBirchDexRatingText_LessThan70', 'Birch recommends observing Pokemon evolution as well as new captures.', '''
S~A familiar partner may still have a new introduction waiting inside its future.|
S~Following development adds information that sampling only new individuals would miss.|
N~Look after the team we have. Let growth happen with proper care.|
S~I like discovering more about someone we already know.|
N~We should learn what the change means before treating it as another box to fill.|
S~The next discovery may already be traveling beside us. Efficient casting.|
N~An investigation requiring less acquisition and considerably more patience.|
N~We can track development while keeping the partner's comfort at the center.|
S~One known shape can carry the beginning of another.|
N~A relationship deserves to remain more than a route to another entry.|
S~I'd ask what small signs of approaching change we might notice.
''')
add('birch_rating_promise', 'gBirchDexRatingText_LessThan80', 'Birch feels optimistic about the record eventual quality.', '''
S~He can see a bigger book in the small one we're carrying now.|
S~His confidence is a forecast based on progress, not a completed result.|
N~Good encouragement. We still choose the next step one at a time.|
S~It's nice when somebody can see possibility without asking us to hurry toward it.|
N~A steady routine will do more than trying to live up to the praise overnight.|
S~An encouraging review of a book still enjoying the right to be unfinished.|
S~A favorable prediction. We can accept it without turning it into a deadline.|
N~We should keep the work accurate as the collection grows.|
S~A half-grown thing can already offer a glimpse of its shape.|
N~I'd keep the warmth and leave the pressure out of it.|
S~I'd ask which part made him feel so hopeful.
''')
add('birch_rating_talent', 'gBirchDexRatingText_LessThan90', 'Birch praises the player talent after reviewing many collected entries.', '''
F~Talent sounds grand. My feet would also like credit for their repeated involvement.|
N~Skill contributes, alongside the accumulated work and opportunities behind the record.|
S~Good work recognized. Don't forget the team that helped us do it.|
S~I would like the quiet persistence to be seen alongside the impressive result.|
S~A lot of ordinary days are hiding inside that compliment.|
S~I shall accept the applause while reserving a generous share for stubborn persistence.|
S~A gratifying assessment of our unusual willingness to keep looking.|
N~We can identify the useful habits that made the results repeatable.|
S~An eye can learn to notice what it once walked past.|
N~Praise feels more solid when it leaves the effort visible.|
S~I'd remember one difficult entry and the little thing that finally helped us find it.
''')
add('birch_rating_safari', 'gBirchDexRatingText_LessThan100', 'Birch recommends Safari Zone species not commonly encountered elsewhere.', '''
S~Another habitat with its own neighbors. Our shoes have received an interesting suggestion.|
N~A distinctive environment can add species missing from more familiar sampling sites.|
N~Learn the local rules before visiting.|
N~I would enjoy seeing what makes the place different before deciding what to seek.|
N~We should pack for an outing rather than assume it will be a quick errand.|
N~A fresh setting may do more for the missing pages than another lap of the old one.|
N~The obvious place to look has apparently been elsewhere for a while.|
N~We can compare the site's habitat with gaps in our current observations.|
N~A different kind of shelter can keep a different kind of life.|
N~I'd want to know what makes the environment special, not only what can be found there.|
N~I'd ask recent visitors which encounter surprised them most.
''')
add('birch_rating_hundred', 'gBirchDexRatingText_LessThan110', 'Birch marks a major hundred-kind milestone and praises the record.', '''
U~That is a wonderfully large pile of different hellos.|
S~A major milestone makes the accumulated breadth of the record easier to appreciate.|
S~A lot of work went into this. Take a moment to be pleased.|
S~I like imagining all the little moments that became these pages.|
S~This deserves a calm celebration, not an immediate demand for the next number.|
S~I propose a brief ceremony in which we stop walking and admit we have done well.|
S~An impressive collection of evidence that we do occasionally leave the house.|
N~We can celebrate and still review the accuracy of what we have recorded.|
S~Many brief meetings have become a substantial little history.|
S~I'd make room for the pride without letting the milestone define the whole journey.|
S~I'd choose one entry that reminds us why looking was enjoyable in the first place.
''')
add('birch_rating_rocksmash', 'gBirchDexRatingText_LessThan120', 'Birch suggests Pokemon encounters inside breakable rocks.', '''
U~Some of the missing neighbors may live behind a very convincing rock-shaped front door.|
N~A different search method can reveal organisms hidden from ordinary surface observation.|
N~Check the surroundings before breaking anything. Be ready for an encounter.|
N~I wouldn't want the first meeting to be a complete surprise for both of us.|
N~A hidden resident still deserves some care in how we approach.|
N~The overlooked habitat has the unfortunate architectural feature of requiring a forceful entrance.|
N~Geology may contain an unexpectedly vocal objection.|
N~We should prepare the team before using Rock Smash repeatedly.|
N~A hard surface can shelter a small life from the world outside.|
N~Curiosity should leave room for the creature who was comfortable there first.|
N~I'd ask which kinds of rocks local people have seen Pokemon emerge from.
''')
add('birch_rating_trade', 'gBirchDexRatingText_LessThan130', 'Birch recommends exchanges with other Trainers to broaden the record.', '''
S~Someone else's ordinary companion may be the introduction our book hasn't had yet.|
S~Exchanges can connect observations gathered along different routes.|
N~Make a fair choice for both Trainers and both Pokemon.|
N~I like that learning more can begin with talking to someone.|
N~I'd ask about the partner's habits before making an exchange.|
N~The missing pages may belong to a conversation rather than a more distant expedition.|
N~A research method requiring the survival of a social interaction. Manageable.|
N~We can compare records first instead of treating every conversation as a proposed trade.|
S~A different journey can place a new familiar face beside our own.|
N~The exchange should feel comfortable to everyone involved, not merely fill a gap.|
S~I'd enjoy hearing where the other Trainer met the Pokemon.
''')
add('birch_rating_friendship', 'gBirchDexRatingText_LessThan140', 'Birch mentions Pokemon whose evolution follows strong affection for their Trainers.', '''
S~Some growth needs a friend-shaped reason to feel ready.|
S~The developmental condition concerns an established bond, not simply battle experience.|
N~Build the trust because the partner deserves it. Let the growth follow.|
S~I like the thought of feeling safe enough for something new.|
N~Quiet care, repeated patiently, matters more than demanding a quick result.|
S~A transformation has a relationship at its center rather than an impressive special effect.|
S~Affection produces an unusually tangible change of circumstances.|
N~We should learn the species-specific conditions without reducing care to a trigger.|
S~A living thing can unfold differently when it knows it belongs.|
N~The relationship still matters just as much after the visible change.|
S~I'd watch for comfort and trust even before anything evolves.
''')
add('birch_rating_diversity', 'gBirchDexRatingText_LessThan150', 'Birch expresses surprise at Hoenn recorded Pokemon diversity.', '''
U~Even the professor has looked at the list and discovered the region had more room than expected.|
S~Field results can exceed an expert's initial expectations. That is a useful outcome.|
S~Good reason to keep listening to what the actual world shows us.|
S~I like hearing someone experienced still sound surprised.|
N~There are a lot of different ordinary lives for us to look after properly.|
S~An expert admits the world has written a larger book than his first outline.|
S~Reality has declined to remain within the predicted page count.|
N~The next question is how the different habitats support that diversity.|
S~A familiar region can be wider in life than in miles.|
S~His surprise makes our observations feel like something he is genuinely learning from.|
S~I'd ask which finding changed his picture of Hoenn the most.
''')
add('birch_rating_outbreaks', 'gBirchDexRatingText_LessThan160', 'Birch advises noticing temporary outbreaks when Pokemon gather in unusual numbers.', '''
N~Some neighbors apparently choose the same day to become very easy to notice.|
S~Temporary abundance can make rare observations more accessible during a limited interval.|
N~Check reliable reports. Don't rush into unfamiliar ground just because the chance is brief.|
N~It must be striking to see a place suddenly full of one familiar shape.|
N~I'd prepare before going instead of letting the short window make every decision.|
N~The unusual gathering offers an opportunity, not an order to abandon the day's judgment.|
N~A species has briefly discovered the convenience of a group entrance.|
N~We should note time and location so the pattern can be studied afterward.|
N~A landscape can change its living pattern for a little while.|
N~The sight itself might be worth seeing even without adding a new partner.|
N~I'd ask the locals how this gathering differs from an ordinary day there.
''')
add('birch_rating_reference', 'gBirchDexRatingText_LessThan170', 'Birch praises the record as a useful picture of Hoenn Pokemon.', '''
S~Our little book has become something another curious person could actually learn from.|
S~A sufficiently broad record can support understanding beyond the observer's own memory.|
S~Good. Useful work matters more than merely a full list.|
S~I like the idea that our quiet notes could help somebody we haven't met.|
N~Clear details make it easier for the next person to care for a Pokemon well.|
S~The travel diary has become a book worth lending. A most respectable transformation.|
S~A collection that has developed a public use beyond being impressive.|
N~We should keep the information understandable to someone who wasn't on the trip.|
S~Attention offered in one place can give light to someone elsewhere.|
N~A useful record lets other people see the creatures, not only our achievement.|
S~I'd ask which page Birch would show a new researcher first.
''')
add('birch_rating_professor', 'gBirchDexRatingText_LessThan180', 'Birch compliments the player work by comparing them to a good Pokemon professor.', '''
F~Professor! I should probably acquire a second pencil before the title gets ideas.|
S~The compliment recognizes research competence, though there is always more to learn.|
S~Good praise. Keep doing the careful work that earned it.|
F~I'd be pleased and rather unsure where to put my hands.|
S~A title is lovely. Being useful to the next curious beginner would make it lovelier.|
M~At last, an academic appointment awarded without requiring me to sit through a committee.|
S~A promising qualification. I trust the lab coat is optional.|
N~We can use what we've learned to help other people make accurate observations.|
S~A patient eye can become a light another person learns beside.|
N~I'd accept the kindness without pretending the learning is finished.|
S~I'd ask Birch which question he still wishes he could answer himself.
''')
add('birch_rating_professional', 'gBirchDexRatingText_LessThan190', 'Birch praises the nearly complete record as professional work.', '''
S~Professional sounds tidy enough to hide how many muddy hems helped make the book.|
S~The assessment recognizes sustained, systematic work rather than a single lucky result.|
S~Well earned. Don't let the compliment make us skip the final checks.|
S~I like knowing the patient little parts were worth doing carefully.|
N~Good work stays good by leaving room for ordinary rest too.|
S~An excellent review of a project maintained long after its first burst of excitement.|
S~Professionalism: a respectable name for repeatedly doing the unglamorous part properly.|
N~We should audit the details as carefully as we pursued the missing entries.|
S~A steady hand leaves a different trace from a hurried one.|
N~The quality matters as much as how close the list looks to finished.|
S~I'd remember the habit that helped us keep going on the least exciting day.
''')
add('birch_rating_close', 'gBirchDexRatingText_LessThan200', 'Birch says the record is close to completion.', '''
U~The remaining blank spaces have become rare enough to look very loud.|
N~Approaching completion often leaves the least accessible cases. Careful planning matters.|
N~Close now. Don't hurry the last part and undo good habits.|
N~Being near the end can make it oddly harder to feel patient.|
N~I'd take a proper break before deciding the last few entries must happen today.|
N~The final pages deserve the same care as the first, despite their provocative emptiness.|
N~Almost finished: a condition notorious for producing unnecessary haste.|
N~We can identify each remaining requirement instead of searching broadly.|
N~A small gap can feel wide when we keep looking only at it.|
N~Let the progress be real without making the unfinished part a failure.|
N~I'd ask which remaining observation is most likely to need a different approach.
''')
add('birch_rating_complete', 'gBirchDexRatingText_DexCompleted', 'Birch confirms completion of the regional record.', '''
U~Every page found a neighbor. I think the book has earned a very gentle pat.|
S~The regional completion condition has been satisfied. That reflects substantial accumulated work.|
S~Done. Take a breath and let that count for something.|
S~I'd want a quiet moment with the team before saying anything grand.|
S~A celebration meal sounds right. Everyone who helped deserves a comfortable evening.|
S~The completed volume can finally be enjoyed without being held up against its missing pages.|
S~An astonishing defeat for blank space. Well done.|
S~Now we can use the record as a reference and ask deeper questions.|
S~Many small meetings have gathered into one full circle.|
S~Completion doesn't make the relationships behind the pages less alive.|
S~I'd look at the first entry once more and remember how the whole thing began.
''')
add('birch_rating_national', 'gBirchDexRatingText_OnANationwideBasis', 'With National mode active, Birch concludes by reviewing seen and caught counts beyond the regional record.', '''
U~The familiar book just unfolded a much larger map inside itself.|
N~The wider count concerns a broader set than the regional assessment.|
N~A larger goal is optional. We can decide what we want to learn next.|
N~I'd want time to enjoy the places we know before hurrying toward everything else.|
N~More possibilities shouldn't make an ordinary good day feel too small.|
N~The expanded edition arrives without erasing the value of the first volume.|
N~The catalog has developed a talent for remaining larger than our afternoon.|
N~We can compare regions carefully instead of treating the bigger total as the only useful fact.|
N~A wider horizon can open gently rather than pull us away.|
N~The counts are interesting, but the next meeting still deserves its own attention.|
N~I'd ask which unfamiliar habitat Birch would most like us to observe.
''')

add('oldale_may_home', 'OldaleTown_Text_MayLetsGoBack', 'May calls the player toward home after the first outing.', '''
S~A familiar voice has already made the way home sound like somewhere we share.|
S~Returning gives us a chance to review what the first outing taught us.|
S~Good time to head back and check on the team.|
S~It's comforting when somebody makes sure you aren't left behind.|
N~A return home can include a proper meal before the next idea arrives.|
S~May makes the return sound cheerful rather than an admission that the afternoon is over.|
S~A reasonable proposal with a pleasantly modest travel requirement.|
N~We can use the walk back to notice anything we missed on the way out.|
S~A path begins to feel familiar when a friend calls us along it.|
S~I like being included in let's instead of simply being told where to go.|
S~I'd walk alongside her and ask what she enjoyed about the outing.
''')
add('oldale_brendan_lab', 'OldaleTown_Text_BrendanLetsGoBack', 'Brendan heads to Birch lab and recommends that the player return too.', '''
N~The field trip has reached the useful part where we tell somebody what actually happened.|
N~Returning to the lab can connect the encounter with further instruction.|
N~Let's get back in good shape. No need to turn hustle into a race.|
N~I would enjoy a quieter walk after the first excitement settles.|
N~I'd make sure everyone has recovered before planning another outing immediately.|
N~He knows where he's going next. We can follow without pretending our legs require dramatic haste.|
N~The lab is unlikely to escape while we walk there sensibly.|
N~A brief check of the team is still worthwhile before the return trip.|
N~A small journey can leave enough new questions to fill the way back.|
N~His confidence can help a beginner as long as it leaves room to ask for a pause.|
N~I'd ask what he thinks the professor will want to hear first.
''')
add('petal_scott_talent', 'PetalburgCity_Text_ImLookingForTalentedTrainers', 'Scott explains his search for talented Trainers and politely ends the introduction.', '''
N~He is looking for talent. I hope he remembers clean clothes aren't a disqualification.|
N~An introduction can establish his purpose without establishing our ability.|
N~We'll keep learning. No need to prove something to a stranger on the street.|
F~Being inspected like that makes a simple walk feel a little less simple.|
N~I'd rather be noticed for how we treat the team than how muddy the shoes get.|
N~He seems interesting, though his clothing-based assessment could use another draft.|
N~Talent scouting conducted through laundry. A questionable research method.|
N~We can let our actual decisions show what we can do over time.|
N~A stranger's glance need not decide the size of our future.|
N~The apology is welcome. An early impression can remain small instead of becoming a label.|
N~I'd ask what he looks for once he gets the chance to watch a real battle.
''')
add('stern_expedition_departure', 'SlateportCity_OceanicMuseum_2F_Text_SternIveGotToGo', 'After the museum crisis and completed delivery, Stern resumes preparing his ocean-floor expedition.', '''
S~The parts arrived, the trouble left, and Stern finally gets to return to the thing he wanted to do.|
S~The immediate disruption is resolved, allowing the planned research expedition to proceed.|
N~Good. Let him get ready without another interruption.|
N~It is nice to see somebody's day begin moving forward again after all that.|
N~The crew probably has quite enough preparation to finish before leaving.|
S~The thieves are gone, and the researcher has reclaimed his own afternoon. A satisfying outcome.|
N~A hectic delivery followed by a man remembering his entire submarine schedule.|
N~They should finish their checks rather than hurry because the interruption took time.|
N~A troubled room has found its ordinary purpose again.|
S~He remembers to welcome us even while his mind is already on the expedition.|
S~I'd let him go, then ask the other staff what visitors can learn here.
''')
