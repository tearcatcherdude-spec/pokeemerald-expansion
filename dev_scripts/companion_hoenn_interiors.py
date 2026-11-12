"""Individually authored Hoenn interior NPC endings, in canonical cast order.

Gift offers, intermediate questions and native menu callbacks are deliberately
not treated as completed outcomes. Labels were reviewed against map scripts.
"""
ROWS = []
EMOTIONS = dict(N='neutral', S='soft_smile', A='annoyed', F='flustered',
                D='sad', U='surprised', M='smug', L='laughing')

def add(key, labels, subject, lines):
    replies = [line.strip() for line in lines.strip().split('|')]
    replies = [EMOTIONS.get(line[0], line[0]) + line[1:] for line in replies]
    assert len(replies) == 11, (key, len(replies))
    ROWS.append(dict(key='hi_' + key, labels=labels.split(), subject=subject, replies=replies))

add('fortree_trade_decline', 'FortreeCity_House1_Text_YouWontTradeMe',
    'The passionate Volbeat owner is disappointed that the player declined the trade.', '''
F~His heart was very loud, but our answer still counts.|
N~A strong preference is not an obligation for the other person.|
N~He can be disappointed. We can still keep our partner.|
F~That was rather a lot of feeling to put on a stranger.|
N~He offered a trade, not a debt. Saying no is allowed.|
M~A magnificent declaration, sadly defeated by an ordinary refusal.|
N~He bared his heart. We did not sign for delivery.|
N~Perhaps next time he can start with the actual proposal.|
N~A wish spoken loudly does not become someone else's promise.|
N~He made declining sound rude. It really wasn't.|
N~He certainly made his feelings clear. We were clear too.
''')
add('fortree_trade_wrong', 'FortreeCity_House1_Text_ThisIsntAMon',
    'The trader rejects a Pokemon of the wrong requested species.', '''
F~We brought a perfectly good Pokemon to the wrong appointment.|
N~The species does not match his request. That settles this attempt.|
N~Wrong partner for this trade. No need to force it.|
F~I think we both heard his request a little differently.|
S~That one wasn't on his shopping list, apparently.|
N~An excellent entrance for entirely the wrong candidate.|
N~Rejected on a technicality. A fairly substantial technicality.|
N~We should check the species before trying the exchange again.|
N~It is still itself, even when someone wanted something else.|
S~An unsuitable match says nothing bad about our Pokemon.|
N~Specific tastes! At least he told us exactly what went wrong.
''')
add('fortree_trade_after', 'FortreeCity_House1_Text_GoingToMakeVolbeatStrong',
    'After the completed trade, the new Volbeat owner promises to train it and asks the same for Plusle.', '''
S~Volbeat and Plusle both have people cheering for them now.|
S~He has turned his enthusiasm into a concrete commitment. Good.|
N~He's serious about raising Volbeat. Let's do right by Plusle.|
S~It helps to hear that goodbye wasn't the end of caring.|
S~Two new homes, and both promising to do their best.|
S~The exchange has become a pair of promises. A better ending.|
S~He still sounds loud. Volbeat seems to have acquired a fan.|
S~His next project is training, and he has plenty of motivation.|
S~They have different paths now, with someone beside each of them.|
S~Plusle wasn't an afterthought in his goodbye. I liked that.|
S~We should remember this enthusiasm when Plusle needs encouragement.
''')
add('fortree_memories', 'FortreeCity_House1_Text_TradingMemoriesWithOthers',
    'A resident sees Pokemon trades as exchanging memories with other people.', '''
S~A traded Pokemon arrives with stories we haven't heard yet.|
N~Its experiences do not reset when its traveling companion changes.|
N~Someone trusted us with a partner they knew. That matters.|
S~I like thinking the old memories still have somewhere to stay.|
S~A new home can make room for an old favorite habit.|
S~A character arrives with a whole unwritten first chapter.|
N~The past comes along. It rarely packs lightly.|
N~Learning how they were raised could help us understand them.|
S~A memory can travel without leaving its first home empty.|
S~That makes asking about the previous Trainer feel rather important.|
S~I'd listen to the stories before adding a few of our own.
''')
add('fortree_coin_wrong', 'FortreeCity_House2_Text_YouGuessedWrong',
    'The player guessed the wrong hand in the Hidden Power test.', '''
F~My hidden power appears to be picking the empty hand.|
N~A wrong guess is weak evidence about anyone's hidden abilities.|
N~Missed a coin. We'll survive the setback.|
F~I couldn't tell either. Her hands gave very little away.|
S~Well, we haven't misplaced the coin. She still has it.|
M~Our mysterious gift has elected to remain mysterious.|
N~My talent for uncertainty remains undefeated.|
N~We could watch her hands more closely on another attempt.|
N~Sometimes a closed hand is simply a closed hand.|
S~She delivered the verdict rather briskly, didn't she?|
N~Now I'm curious whether anyone notices her switching it.
''')
add('fortree_hidden_power', 'FortreeCity_House2_Text_ExplainHiddenPower',
    'The Hidden Power giver explains that its effect changes with the Pokemon.', '''
U~One move with a different surprise inside each Pokemon!|
N~The user matters as much as the move's name. Worth testing.|
N~Check what it does before relying on it in a hard fight.|
S~I like that the same lesson can come out differently.|
S~Same recipe card, very different ingredients doing the work.|
S~A single title concealing several possible plots. Intriguing.|
N~Even the move refuses to be easily categorized. Fair enough.|
U~We should compare results instead of assuming the name tells us everything.|
N~Something particular to each Pokemon answers through that move.|
S~A shared name with an individual expression. Lovely little detail.|
N~I'd like to see how different two uses of it can look.
''')
add('fortree_steven', 'FortreeCity_House3_Text_MetStevenHadAmazingPokemon',
    'A stone seeker recalls Steven and his exceptionally well trained Pokemon.', '''
U~He went looking for rare stones and found a terrifying Trainer attached.|
N~Rarity and training are separate qualities. Steven apparently supplies both.|
N~That sounds like a team you prepare for properly.|
N~He seemed more struck by their training than their rarity.|
N~Finding something rare is one thing. Raising it well takes longer.|
S~A stone hunt interrupted by an encounter with local legend.|
N~Terrifyingly well trained. A compliment with sensible distance built in.|
N~I'd ask what their training actually involved. That's the useful part.|
N~He remembers the strength more clearly than the stones.|
N~Steven made quite an impression without having to announce himself.|
U~I love how a conversation about rocks became this story.
''')
add('fortree_pokedex', 'FortreeCity_House3_Text_OhYouHavePokedex',
    'A child is impressed on learning that the player carries a Pokedex.', '''
S~We have been carrying something awesome around like an ordinary pocket lump.|
S~A portable record of Pokemon is impressive. Familiarity hides that.|
S~Nice to see someone excited about what we learn out there.|
S~I forget it can look extraordinary the first time.|
S~That little introduction made his whole face brighten.|
S~Behold, the glamorous life of carrying field notes.|
S~An enthusiastic audience for a very small encyclopedia.|
S~That's exactly the response a useful invention deserves.|
S~A small object can open a rather large door.|
S~He asked, listened, and was delighted. Excellent conversation.|
S~I'd show him an entry about a Pokemon he knows.
''')
add('fortree_friends', 'FortreeCity_House4_Text_BringsWorldCloserTogether',
    'A resident values the friendships people make through Pokemon.', '''
S~Pokemon are very good at introducing people who were minding their own business.|
S~A shared interest lowers the difficulty of that first conversation.|
S~A good partner can help you find good people.|
S~It is easier to say hello when they have already started.|
S~There is always something to talk about when a Pokemon joins in.|
S~The finest social organizer may have feathers and no schedule.|
S~Accidental friendship is one of their less advertised talents.|
S~The Wingull next door is doing practical work toward her theory.|
S~Little meetings can tie distant places together.|
S~She's noticed how often affection gives strangers common ground.|
S~That's how so many good conversations start: asking about someone's Pokemon.
''')
add('fortree_errand', 'FortreeCity_House4_Text_AskedWingullToRunErrand',
    'The boy says his absent Wingull is away running an errand.', '''
S~Wingull has errands. I feel slightly underorganized beside a bird.|
N~An airborne messenger can cross terrain that slows us considerably.|
N~Sounds like he's waiting for his partner to return.|
N~The room feels quieter while the bird is away.|
S~Sending Wingull is probably quicker than sending us up those ladders.|
S~A small courier somewhere in the middle of a large assignment.|
N~Even birds have chores. A sobering discovery.|
S~I wonder how they agreed on the destination. Training must matter.|
N~Someone elsewhere may be looking up for a familiar pair of wings.|
S~He sounds quite pleased with his little arrangement.|
N~I'd ask who Wingull is visiting. Errands connect interesting people.
''')
add('fortree_far_friends', 'FortreeCity_House4_Text_FriendsFarAwayThanksToWingull',
    'After Wingull has returned, the boy credits it for his distant friendships.', '''
S~Wingull makes far away sound like somewhere just down the branch.|
S~Reliable communication changes which friendships distance can sustain.|
S~Good bird. Keeping people connected is useful work.|
S~It must be nice to recognize those wings coming home.|
S~A letter carried back makes the distance feel less empty.|
S~One bird, several friendships, and an excellent sense of direction.|
S~The post has feathers and a social life. Good for it.|
S~His messenger route has become a real little network.|
S~A returning bird brings more than whatever it holds.|
S~He remembers to credit Wingull for making those connections possible.|
S~There must be wonderful stories at both ends of that flight.
''')
add('fortree_trees', 'FortreeCity_House5_Text_TreeHousesAreGreat',
    'A resident praises Fortree tree houses as a way to live with Pokemon.', '''
S~A town where upstairs begins before you enter the house!|
N~Their homes use the forest's vertical space remarkably well.|
S~Good homes. I'd still watch those steps in the rain.|
S~You can hear the leaves from almost anywhere in here.|
S~Carrying groceries home must count as the day's exercise.|
S~She has a strong claim for the finest address among the branches.|
S~Living in a tree does make being indoors wonderfully ambiguous.|
S~The supports and walkways make this much more than a charming idea.|
S~The trees remain neighbors, even with houses around them.|
S~She is proud of the way her home fits its surroundings.|
S~I'd love to hear what mornings sound like up here.
''')
add('fortree_adapt', 'FortreeCity_House5_Text_AdaptedToNature',
    'A resident argues for adapting human homes to nature rather than forcing nature to fit.', '''
N~The trees were here first. Building around them seems polite.|
N~Adaptation can reduce how much a settlement must disrupt.|
N~Work with the land. Fighting it gets expensive.|
S~I like a house that leaves room for the things already living there.|
N~You learn a place's limits before deciding what to build.|
N~An unusually reasonable demand that the scenery retain its role.|
S~The forest has declined our renovation proposal. Wisely.|
N~Constraints can lead to good designs. These houses are evidence.|
S~A home can belong somewhere without making everything else leave.|
N~Making space for neighbors includes the ones with roots.|
N~I'd ask what they changed after their first rainy season.
''')
add('fortree_dolls', 'FortreeCity_DecorationShop_Text_BuyingDeskForDolls',
    'A shopper wants a desk to protect Secret Base dolls from dirt and splinters.', '''
S~Even dolls deserve a seat without splinters in it.|
N~A raised surface protects the fabric from debris and abrasion.|
S~Solid reason to buy a desk. Keep the little things safe.|
S~She has already pictured where each doll will sit.|
S~A clean place for treasured things is worth making.|
S~The dolls have acquired both furniture and a devoted estate manager.|
S~A tiny gathering with remarkably strict seating standards.|
N~She should check the desk's finish too. Splinters can be sneaky.|
S~Small belongings can make a hidden place feel like home.|
S~She's furnishing for the dolls' comfort. I respect that commitment.|
S~I'd love to see the little arrangement when she's finished.
''')
add('fortree_delivery', 'FortreeCity_DecorationShop_Text_MerchandiseSentToPC',
    'A shopper envies the furniture delivery service and wishes it could deliver them home.', '''
S~I also become interested in delivery whenever stairs are involved.|
N~Transporting merchandise and transporting people are rather different problems.|
S~After carrying furniture, I'd ask the same question.|
S~It does sound tempting after a long day in town.|
L~Buy a chair, then ask if you can ride home on it.|
M~An inspired request to include the customer in the purchase.|
S~The desk gets a convenient journey. We get legs. Unfair.|
N~An efficient delivery service creates ambitious expectations.|
S~Getting home is sometimes the hardest part of an outing.|
S~The furniture has a better travel arrangement than its owner.|
S~I'd enjoy hearing the clerk try to answer that request.
''')
add('cozmo_absent', 'FallarborTown_CozmosHouse_Text_CozmoWentToMeteorFalls',
    'Cozmo is away at Meteor Falls with Team Magma.', '''
N~A meteorite trip sounds exciting. The company sounds less promising.|
N~His research may be genuine; his companions' motives deserve scrutiny.|
N~Team Magma is involved. We should check on him.|
N~She says it casually. I wish that made it sound safer.|
N~I don't like hearing who offered to accompany him.|
N~An innocent research trip has acquired a worrying supporting cast.|
N~Rocks are usually the safer part of field research. Usually.|
N~Meteor Falls gives us somewhere specific to look for him.|
N~Curiosity can lead someone through a door they should inspect first.|
N~He may see research partners where we see warning signs.|
N~I'd rather ask Cozmo himself how this expedition came together.
''')
add('cozmo_conned', 'FallarborTown_CozmosHouse_Text_MeteoriteWillNeverBeMineNow',
    'Cozmo regrets being deceived into revealing meteorite locations to Team Magma.', '''
D~He wanted to share something wonderful. They took advantage of that.|
N~Sharing research was not the wrongdoing. Exploiting his trust was.|
N~They used him. That fault belongs to Team Magma.|
D~He sounds as if losing trust hurt almost as much as losing the stone.|
D~It's miserable when helping someone becomes the thing you regret.|
N~The villains borrowed his expertise and left him the blame. Typical.|
D~A bad audience for a good enthusiasm. I hate that.|
N~His knowledge is still valuable, despite how they misused it.|
D~A stolen stone has left a heavier absence than its size suggests.|
N~He deserves to be angry with them, not only himself.|
D~I'd listen before asking him to tell the whole story again.
''')
add('cozmo_decline', 'FallarborTown_CozmosHouse_Text_CrushedWithDisappointment',
    'Cozmo is disappointed after the player refuses to exchange the meteorite.', '''
D~He had already imagined that stone on his desk, hadn't he?|
N~He was invested in the exchange. It remains a choice.|
N~We declined. No need to make the disappointment worse.|
D~That sounded very small after all his excitement.|
N~We can be gentle even when the answer stays no.|
D~His entire bright prospect collapsed into one short sentence.|
N~Disappointment has made itself quite at home in this room.|
N~He may accept the same exchange later if we reconsider.|
D~Something almost within reach can hurt more than something distant.|
N~He didn't hide how much it mattered to him.|
D~Let's give him a moment rather than hovering over that answer.
''')
add('cozmo_research', 'FallarborTown_CozmosHouse_Text_ReallyGoingToHelpMyResearch',
    'The meteorite exchange has succeeded and Cozmo is delighted to resume research.', '''
S~That space rock has finally reached someone who wants to study it!|
S~He has the specimen and a genuine research question again. Excellent.|
S~Good. The meteorite is where it can do some good.|
S~He sounds lighter already. I am glad we heard this part.|
S~That's the sound of someone getting their work back.|
S~A stolen discovery returns to the story it should have had.|
S~The room is less gloomy. I shall try not to take it personally.|
S~Now he can investigate the actual material instead of losing sleep over it.|
S~A little fallen piece of sky has given him his footing back.|
S~That happiness looks thoroughly unpolished. The best kind.|
S~I'd come back later and ask what he learned from it.
''')
add('cozmo_wife_sad', 'FallarborTown_CozmosHouse_Text_FeelSorryForCozmo',
    'Cozmo wife worries about his depression after the Team Magma incident.', '''
D~She can't fix the missing meteorite just by worrying beside him.|
N~She sees the effect on him every day. That is difficult too.|
N~He's not the only person this has been hard on.|
D~She sounds tired of not knowing how to help.|
D~Watching someone lose their enthusiasm can quiet a whole house.|
D~Even the person outside the adventure has to live with its aftermath.|
N~There isn't a clever remark that makes this less sad.|
N~Getting his research moving again could give him something concrete to do.|
D~She has been keeping company with his disappointment.|
D~It matters that someone noticed how badly he was hurt.|
N~I'd ask how he's been doing, and let her answer at her own pace.
''')
add('cozmo_wife_happy', 'FallarborTown_CozmosHouse_Text_CozmoIsSoHappy',
    'Cozmo wife affectionately celebrates his happiness after the meteorite is returned.', '''
S~She's enjoying his happiness almost as much as he is!|
S~A restored specimen has improved the mood of an entire household.|
S~She's relieved. Good to see them both smiling.|
S~It is sweet that she wants us to notice him being happy.|
S~Some good news belongs to everyone at home.|
S~The researcher's joy has received a glowing domestic review.|
S~Apparently enthusiasm is contagious. This case seems harmless.|
S~The meteorite has already produced one very visible result.|
S~She sees the person glowing behind all the talk about stones.|
S~That fond little observation says a great deal about them.|
S~I like seeing the people around a discovery enjoy it too.
''')
add('fallarbor_fossils', 'FallarborTown_PokemonCenter_1F_Text_FossilManiacEdgeOfTown',
    'A visitor wonders about ancient Pokemon and suggests asking the Fossil Maniac.', '''
U~An ancient Pokemon might have had an ancient version of a very silly face.|
S~Fossils let us compare curiosity with physical evidence. I'd ask him.|
N~Someone nearby studies this. Good place to start.|
N~It is strange to imagine familiar ground with entirely different lives on it.|
S~I wonder what they needed to get through an ordinary day.|
S~The oldest characters have left us a difficult manuscript to read.|
N~Finally, a neighbor with an appropriate interest in old bones.|
N~I'd ask what the fossils can show, and what remains a guess.|
N~The ground remembers shapes no living eye has seen.|
N~There must have been beautiful forms we can only partly reconstruct.|
S~A local expert and a good question. That sounds like a worthwhile visit.
''')
add('fallarbor_trees', 'FallarborTown_PokemonCenter_1F_Text_PlantHardyTrees',
    'Fallarbor residents plant trees hardy enough for volcanic ash.', '''
S~Little trees setting up home in a giant dust problem!|
N~Choosing ash-tolerant seedlings is more effective than ignoring the soil.|
S~They know what grows here and put the work in.|
S~It must feel good to see those first leaves survive.|
N~A good planting starts with knowing the ground you're working.|
S~A town insisting on a green future, one stubborn seedling at a time.|
S~Hardy little trees. Sensible neighbors for this weather.|
N~I'd ask which species take root best and how they protect new growth.|
S~Soft new leaves can belong to a harsh landscape.|
S~They chose plants that suit the place. There is care in that.|
S~I'd like to see how those fields change as the trees grow.
''')
add('lavaridge_bitter', 'LavaridgeTown_HerbShop_Text_HerbalMedicineWorksButMonWillDislike',
    'Herbal medicine is effective but bitter enough to upset Pokemon.', '''
F~A medicine can win the battle and lose the taste contest spectacularly.|
N~Effectiveness and tolerability are separate qualities. He is warning us about both.|
N~Useful in a pinch. Remember how our partner feels afterward.|
F~That sounds like the sort of taste you remember for years.|
N~Cheap and effective still leaves a very unhappy mouth to deal with.|
N~A cure whose review reads: effective, unforgivable, never again.|
N~Bitter medicine. The adjective appears to be doing serious work.|
N~Knowing the drawback helps us choose rather than being surprised later.|
N~A healed body can still have a grievance. Understandably.|
N~I'd rather know that cost before handing it to someone I care about.|
F~His expression makes me believe he has heard some strong complaints.
''')
add('lavaridge_charcoal', 'LavaridgeTown_HerbShop_Text_ExplainCharcoal',
    'After giving Charcoal, the old man explains its herbal use and Fire move boost.', '''
U~Charcoal has a job here and a much hotter job with Pokemon.|
N~One material serves two distinct uses. Its origin doesn't limit its application.|
N~Good to know what it does before handing it to a partner.|
N~I wouldn't have guessed that from something so plain-looking.|
S~I knew charcoal was useful. This is a different sort of useful.|
S~A humble black object with unexpectedly dramatic potential.|
N~Dark, unassuming, and helpful. An admirable combination.|
S~That is a practical explanation I can actually use.|
N~A little remnant of fire keeps another kind of fire company.|
N~It doesn't need to look impressive to earn its place.|
N~I'd ask which Pokemon he has seen put it to best use.
''')
add('lavaridge_egg', 'LavaridgeTown_House_Text_WifeWarmingEggInHotSprings',
    'A husband says his wife is warming the Egg discovered at the Day Care.', '''
S~That Egg is having a spa day before it has even met anybody.|
N~She has found a warm place to wait for it to hatch.|
N~Sounds like she's keeping it close and watching over it.|
S~She must be wondering what is inside every time it moves.|
S~Someone is already fussing over its comfort. Good start.|
S~Our smallest unseen guest enjoys the town's finest amenities.|
S~An excellent excuse to stay in warm water for another hour.|
N~I'd still want to make sure the Egg wasn't getting too hot.|
S~A quiet beginning, held in warm hands.|
S~He tells it like ordinary household news. I find that lovely.|
S~I'd love to hear from them when that Egg finally opens.
''')
add('lavaridge_soak', 'LavaridgeTown_PokemonCenter_1F_Text_HotSpringCanInvigorate',
    'A bather enjoys the restorative hot springs and wishes Pokemon could soak too.', '''
S~The water gets all the credit while we just sit there. Excellent arrangement.|
N~Warmth and rest can feel remarkably restorative after travel.|
S~A good soak sounds sensible after the road here.|
S~I like the part where nobody needs you to hurry.|
S~Warm water, tired feet, and no dishes afterward. Tempting.|
S~A rare local attraction that asks the visitor to accomplish less.|
S~Sitting quietly in warm water. My ambition has found its subject.|
N~They should check which Pokemon are comfortable with hot water first.|
S~Some kinds of magic are just being warm long enough.|
S~Feeling better and wanting to share it is rather sweet.|
S~Everyone coming out of the springs seems to talk a little slower.
''')
add('lavaridge_time', 'LavaridgeTown_PokemonCenter_1F_Text_TrainersPokemonSpendTimeTogether',
    'A resident believes time spent together strengthens Pokemon friendships.', '''
S~Even an uneventful walk can count as a good day together.|
N~Repeated, comfortable contact gives trust something to develop around.|
N~Showing up consistently does more than a grand gesture.|
S~You don't always need something interesting to say.|
S~The ordinary parts matter: meals, rests, being there again tomorrow.|
S~A convincing defense of the chapters where nobody saves the world.|
S~Quiet company is still company. I appreciate that.|
N~Shared time lets you notice small changes before they become problems.|
S~Familiar footsteps can become a kind of home.|
S~It takes time to learn what makes someone comfortable beside you.|
S~Long trips leave room for the little habits you start recognizing.
''')
add('lavaridge_rest', 'LavaridgeTown_PokemonCenter_1F_Text_TrainersShouldRestToo',
    'A resident reminds Trainers to rest alongside their Pokemon and points toward the springs.', '''
S~We've been prescribed sitting in warm water. I can follow that instruction.|
N~A tired Trainer makes poorer decisions. Rest serves the whole team.|
N~He's right. Take care of the person making the calls too.|
S~It's nice when someone remembers to ask us to rest.|
S~Being responsible doesn't require being exhausted. Let's sit down.|
S~At last, an elder's advice that involves fewer ordeals.|
S~A medical opinion in favor of doing very little. Approved.|
N~There's a convenient place to recover right here. We should use it.|
S~The one leading the journey is allowed to stop walking.|
S~He has clearly watched a lot of Trainers forget themselves.|
S~We might enjoy the next stretch more with rested feet.
''')
add('evergrande_believe', 'EverGrandeCity_PokemonCenter_1F_Text_BelieveInYourPokemon',
    'A visitor compares Victory Road to a life journey and encourages trust in Pokemon.', '''
S~That road gave us plenty to remember, including several very stubborn rocks.|
N~We have practical evidence of what our team can overcome together.|
N~We've come through difficult ground. Trust the partners who did it with us.|
S~Looking back makes the distance feel real all at once.|
N~A breath, a proper rest, and then we give the next part our best.|
S~The long road has earned its place in the story. So has the team.|
N~A harrowing life comparison, conveniently located beside a healing counter.|
N~We can carry what we learned through that road into the next challenge.|
S~The path behind us is full of small acts of trust.|
S~They see how far we have come. We should let ourselves see it too.|
S~I want to remember the faces beside us at this point.
''')
add('evergrande_continue', 'EverGrandeCity_PokemonCenter_1F_Text_LeagueAfterVictoryRoad',
    'A visitor says the League is close after Victory Road and urges the player onward.', '''
S~We have other choices, but this one has been waiting at the end of the road.|
N~We can continue after confirming that the team is ready.|
N~Close now. Rest first, then go in prepared.|
N~Being this close makes it feel bigger, somehow.|
S~We can be excited and still stop long enough to eat.|
S~An excellent dramatic location for a final check of our supplies.|
N~The destination has stopped being theoretical. Slightly inconvenient for my nerves.|
N~A short distance doesn't tell us how demanding the next part will be.|
N~A threshold can feel longer than the road that brought us there.|
S~There's encouragement in how certain they are we belong here.|
S~I'd take one look back at the road before going forward.
''')
add('evergrande_scott', 'EverGrandeCity_PokemonCenter_1F_Text_ScottHappyForYou',
    'Scott celebrates the player reaching the League and promises contact if they become Champion.', '''
S~Scott has saved up a whole League's worth of cheering for us.|
N~His promised contact is conditional. For now, we have a challenge ahead.|
S~He kept an eye on our progress. Let's make a solid attempt.|
F~That is quite a lot of confidence to receive just before going in.|
S~A familiar face cheering here takes some of the chill out of it.|
S~Scott offers a tantalizing sequel. We must finish this chapter first.|
S~He sounds delighted. Apparently our difficult walk had a spectator.|
N~Whatever he has planned can wait until we've handled the League.|
S~Someone has been hoping we would reach this door.|
S~He made his pride in us quite clear. That's generous.|
S~I'd like to tell him how it goes after we've actually tried.
''')
add('evergrande_badges_missing', 'EverGrandeCity_PokemonLeague_1F_Text_HaventObtainedAllBadges',
    'The League attendant denies entry because the player lacks all required badges.', '''
F~We reached the door before we finished collecting the keys.|
N~The entry requirement remains unmet. Traveling here doesn't replace it.|
N~We know what is missing. Let's finish that work.|
F~A long trip to hear a short answer. At least it is clear.|
N~Better to find out here than walk into something we're not ready for.|
N~The grand entrance has been postponed by the admissions office.|
N~The door is unmoved by our impressive arrival. Understandable.|
N~Let's check the badge case and plan the remaining stops.|
N~A closed door can still tell you which path to take next.|
N~He was firm without making it personal. That's fair.|
N~We can return with a different answer in our badge case.
''')
add('evergrande_admitted', 'EverGrandeCity_PokemonLeague_1F_Text_GoForth',
    'After checking all badges, the League attendant admits the player and encourages the team.', '''
U~The door says yes! My stomach appears to be saying several things.|
S~All requirements are satisfied. The rest depends on our decisions together.|
N~We're cleared to enter. One battle at a time.|
F~I knew the door would open. Hearing it still feels enormous.|
S~We've prepared what we can. Let's look after one another in there.|
S~Our introduction is complete. Now comes the part worth remembering.|
F~An open door. A surprisingly effective source of nerves.|
N~Final checks are done. We can focus on the challenge itself now.|
N~Carry the trust that brought us here across that threshold.|
S~A simple welcome, earned one badge at a time.|
S~Take a breath. This is a moment we'll want to remember clearly.
''')

add('rustboro_land', 'RustboroCity_CuttersHouse_Text_DadHelpedClearLandOfTrees',
    'A child proudly recalls their father helping clear trees for Rustboro expansion.', '''
S~His dad helped make room for the city. That's a big thing to point at.|
N~Pokemon labor was part of the city's growth. I'd ask what stood here before.|
N~He's proud of his father doing useful work. I get that.|
N~It must be odd to remember trees where there are houses now.|
S~A child can see a whole town and think of their dad.|
N~A family's little story fits inside the city's larger one.|
N~The city's history has stumps beneath the paving.|
N~Clearing land changes drainage too. Expansion takes more than cutting.|
N~A growing town leaves memories of the forest it replaced.|
N~He knows a piece of the city through someone he loves.|
N~I'd ask which part his father helped build room for.
''')
add('rustboro_cut', 'RustboroCity_CuttersHouse_Text_ExplainCut',
    'The Cutter explains reusable Cut HM and the Stone Badge needed to use it in the field.', '''
S~A useful lesson that doesn't disappear after one Pokemon learns it!|
N~Learning the move and having permission to use it outside battle are separate.|
N~Useful for a blocked path. Check the badge requirement first.|
N~I like having the explanation after the excitement settles down.|
N~One tool we can keep teaching from. That's generous.|
S~An obstacle-removal lesson with surprisingly durable teaching material.|
N~A thin tree is about to have an inconvenient afternoon.|
N~Reusable instructions make it easier to train the right partner.|
N~A path can open, but the choice to cut still belongs to us.|
N~He made the limits clear along with the possibilities.|
N~I would check which paths it opens around the city.
''')
add('rustboro_devon_shoes', 'RustboroCity_DevonCorp_1F_Text_ThoseShoesAreOurProduct',
    'A Devon employee is pleased to see the player wearing their Running Shoes.', '''
S~Our muddy feet just gave somebody a professional compliment.|
S~Seeing a product used is a satisfying form of feedback.|
S~They work. We've put enough distance on them to know.|
S~He looks happy to know they made it out into the world.|
S~Something he helped make is making our day easier. Nice.|
S~Our shoes have become traveling ambassadors with terrible manners.|
S~A touching reunion between an employee and some very worn footwear.|
S~Actual use tells you things a demonstration never will.|
S~He sees a little of his work in our journey.|
S~A well-made everyday thing deserves that kind of pride.|
S~I'd tell him which part of the journey they've helped with most.
''')
add('rustboro_devon_access', 'RustboroCity_DevonCorp_1F_Text_OnlyAuthorizedPeopleEnter',
    'A Devon attendant refuses entry to unauthorized visitors.', '''
N~Our enthusiastic face doesn't seem to count as authorization.|
N~A research workplace has reasonable reasons to restrict access.|
N~Private area. We can ask who handles visitors.|
F~I think we have reached the end of this particular hallway.|
N~Fair enough. People are trying to work back there.|
N~Curiosity meets the employee responsible for saying no.|
N~The boundary is admirably clear. I can respect a closed door.|
N~We need permission from someone responsible for the site.|
N~Some thresholds are kept for ordinary reasons.|
N~A polite refusal is still a refusal. We can move along.|
N~I'd ask if there is a public area where visitors can learn more.
''')
add('rustboro_devon_recovered', 'RustboroCity_DevonCorp_1F_Text_SoundsLikeStolenGoodsRecovered',
    'An employee has heard that the stolen Devon Goods were recovered.', '''
S~Good news is finally making its way around the building.|
N~The report has reached the staff. Recovery eases more than one concern.|
S~The parcel's back. One less thing for them to worry about.|
S~Even secondhand relief sounds different from the worry before.|
S~Work probably feels a little more normal with that settled.|
S~The building's rumor network has received a welcome update.|
N~At last, office gossip with a tolerable conclusion.|
N~Now they can check the goods and resume the interrupted work.|
S~Something missing has returned to the shape of their day.|
S~A small sentence carrying quite a lot of relief.|
S~I'd be curious how quickly that news reached every floor.
''')
add('rustboro_devon_robber', 'RustboroCity_DevonCorp_1F_Text_RobberWasntVeryBright',
    'An employee says the stolen specialist parcel would be useless to an ordinary thief.', '''
N~Stealing a thing before knowing what it does is a very crooked shopping plan.|
N~It may require specialized knowledge. That does not make the theft harmless.|
N~Useless to the thief still means missing from the people who need it.|
N~He sounds more insulted by the thief's judgment than anything else.|
N~An important parcel doesn't have to be useful to everybody.|
M~A theft whose research phase appears to have been omitted.|
N~A specialized disappointment for an unspecialized criminal.|
N~Unless the thief was acting for someone else. I'd avoid assuming too much.|
N~They carried away a purpose they did not understand.|
N~I wouldn't mistake their ignorance for a reason to relax.|
N~I'd ask who actually knows how those goods are used.
''')
add('rustboro_ability', 'RustboroCity_Flat1_1F_Text_EveryPokemonHasAbility',
    'A resident explains that each Pokemon has a special ability.', '''
U~Every Pokemon comes with its own little surprise clause.|
N~Abilities can matter even when no move is being selected.|
N~Know your partner's ability. Know the opponent may have one too.|
N~Some of the important things aren't obvious at first glance.|
N~It's worth learning what helps each partner do well.|
N~Every character arrives with something absent from the move list.|
N~An unseen advantage. Naturally, that also means unseen trouble.|
N~I'd examine the ability before planning how to use a move.|
N~What a creature is can change what happens around it.|
N~Two similar-looking Pokemon can still bring different strengths.|
N~I'd ask which ability first made them notice this.
''')
add('rustboro_strange', 'RustboroCity_Flat1_1F_Text_PokemonStrange',
    'A resident simply marvels at the strangeness of Pokemon.', '''
S~Some of them are tiny, some are enormous, and all of them get hungry.|
S~Familiarity has not made them any less worthy of investigation.|
S~Strange, yes. Reliable company all the same.|
S~I still notice something unexpected when I think I know one.|
S~They can astonish you and steal your lunch in the same minute.|
S~A concise review of a very complicated subject.|
S~A world full of odd creatures. I feel appropriately at home.|
S~The more you learn, the better your questions get.|
S~A familiar face can still hold a little mystery.|
S~That is a perfectly fair reaction to looking around here.|
S~I'd love to know which Pokemon started that thought.
''')
add('rustboro_travel', 'RustboroCity_House1_Text_AllSortsOfPlaces',
    'A resident travels to meet the varied people and Pokemon of different places.', '''
S~That's a good reason to travel. The snacks can be a second reason.|
S~Different environments offer different encounters. A fine incentive for fieldwork.|
S~Travel with open eyes. Plenty worth meeting out there.|
S~I like hearing a place described through who lives there.|
S~You learn a town quickly when someone invites you to their table.|
S~A sensible objection to spending one's entire story in one room.|
S~A compelling argument, despite the unfortunate amount of walking.|
N~I'd ask what surprised them most between two neighboring towns.|
S~Some places become dear because of who met us there.|
S~They seem interested in differences without judging them. I like that.|
S~That is exactly the kind of travel story I want to hear.
''')
add('rustboro_cute', 'RustboroCity_House1_Text_AnyPokemonCanBeCute',
    'After trading, the owner says care and kindness can make any Pokemon cute.', '''
S~Even a very grumpy face gets cuter when you know who's making it.|
S~Affection changes what details an observer notices.|
S~Treat them well. You start seeing the little things.|
S~Knowing someone can make a plain moment feel lovely.|
S~A familiar appetite can become surprisingly endearing.|
S~A persuasive defense of the charm hidden outside the usual casting choices.|
S~Some of us require a generous interpretation of cute. Appreciated.|
S~Care lets their comfortable habits show. That's useful to remember.|
S~Kindness gives small, guarded things room to unfold.|
S~Cute is often a relationship before it is a look.|
S~I'd ask what habit made them first feel that way.
''')
add('rustboro_trade_decline', 'RustboroCity_House1_Text_YouDontWantToThatsOkay',
    'The Rustboro trader accepts a refusal while remaining proud of their Pokemon.', '''
S~No trade, and the Pokemon still gets a compliment. Good result.|
S~They accept our decision without withdrawing their affection.|
S~That is a fair way to take no for an answer.|
S~I'm glad nobody had to feel awkward for very long.|
S~They like their partner either way. That's reassuring.|
S~The proposal ends gracefully, with one final advertisement for cuteness.|
S~A refusal survived without catastrophe. Refreshing.|
S~No exchange needed if the arrangement doesn't suit both Trainers.|
S~Their affection hasn't depended on our answer.|
S~A little pride, without trying to make us feel guilty.|
S~I like how easily we can keep talking after that.
''')
add('rustboro_trade_wrong', 'RustboroCity_House1_Text_DoesntLookLikeMonToMe',
    'The Rustboro trader rejects the offered Pokemon because it is not the requested species.', '''
F~The Pokemon is here. The correct Pokemon is apparently elsewhere.|
N~A species mismatch prevents the proposed exchange.|
N~Wrong species for this trade. Simple enough to correct.|
F~That was a very understandable bit of confusion.|
S~Wrong item on the counter, so to speak. Nobody's fault to fix now.|
N~Our candidate has arrived at the wrong audition.|
N~An identity dispute resolved with admirable speed.|
N~Let's verify the request before selecting another partner.|
N~Being wanted elsewhere would not change what this Pokemon is.|
N~They know what they are looking for. That's fair.|
N~At least they explained the mismatch immediately.
''')
add('rustboro_trade_care', 'RustboroCity_House1_Text_PleaseBeGoodToMyPokemon',
    'The trader asks the player to care well for their Pokemon after a successful trade.', '''
S~That little request weighs more than the whole trade machine.|
N~The exchange is complete; responsibility for its welfare continues.|
N~We'll take good care of it. That is the important part.|
S~You can hear that saying goodbye wasn't entirely easy.|
S~We'll learn what makes this partner comfortable with us.|
S~A quiet line that matters more than any sales pitch.|
S~A new beginning with someone else's trust packed inside.|
N~We should give it time to settle into a new routine.|
S~An old kindness is asking to continue through new hands.|
S~They remembered the Pokemon's future after making the exchange.|
S~I'd ask about a favorite habit before we leave.
''')
add('rustboro_pekachu', 'RustboroCity_House3_Text_NamingPikachuPekachu',
    'A resident questions whether naming Pikachu Pekachu is meaningfully original.', '''
L~Pekachu! The extra originality must be hiding inside the E.|
N~The name remains recognizable. Its novelty is modest.|
S~Easy to call across a room. That counts for something.|
S~It sounds like a name someone would say fondly.|
S~A small change is still enough if the family likes it.|
M~A bold revision whose author has altered exactly one letter.|
S~Rebellion, restrained by the fear of confusing the neighbors.|
N~A clear name is useful. Originality is a separate requirement.|
S~Sometimes a familiar shape only needs a small personal mark.|
S~It is a tiny flourish. I wouldn't demand a full reinvention.|
S~I'd ask whether Pikachu answers to it. That's a useful review.
''')
add('rustboro_nickname_pride', 'RustboroCity_House3_Text_IGivePerfectlySuitedNicknames',
    'A resident proudly claims perfectly suited Pokemon nicknames as an expression of originality.', '''
S~The pause before originality suggests the name is doing some heavy lifting.|
N~A suitable name need not also be a uniquely inventive one.|
S~If they both like the name, that's enough.|
S~He wants us to understand the thought he put into it.|
S~People get attached to the small choices they make for a partner.|
M~An artist's statement, delivered while the ink is still drying.|
S~Originality has requested a moment to compose itself.|
N~I'd ask how he decided which name suited which Pokemon.|
S~A name can be a small way of noticing someone.|
S~He's proud of making it personal, however modest the change.|
S~Now I want to hear every nickname he has chosen.
''')
add('rustboro_roxanne', 'RustboroCity_House2_Text_RoxanneKnowsALot',
    'A child admires Roxanne knowledge as well as her strength.', '''
S~Strong and good at answering questions. That's an excellent combination.|
S~Knowledge gives her strength a basis beyond sheer force.|
N~Someone worth learning from before challenging.|
S~It's nice that he admires what she knows too.|
S~A good teacher can make a tough opponent.|
S~A local hero with both an impressive team and reliable explanations.|
N~An informed opponent. Always more inconvenient than a loud one.|
N~Understanding how Pokemon work makes practice much more effective.|
S~He sees learning as part of strength. That is promising.|
S~She's given him more to admire than a badge on a wall.|
S~I'd ask what she taught him that he still remembers.
''')
add('rustboro_school_praise', 'RustboroCity_House2_Text_TrainerSchoolExcellent',
    'A resident praises the Trainer School as a possible beginning for future Gym Leaders.', '''
U~A classroom today, your own Gym someday. That's quite a school brochure.|
N~Strong fundamentals can support much more advanced training later.|
N~Start with the basics. Even strong Trainers had to learn them.|
S~It helps when someone thinks a small beginning can lead somewhere.|
S~Everyone has a first lesson they didn't know yet.|
S~An ambitious ending offered to a room full of beginnings.|
S~Homework with unusually formidable career prospects.|
N~I'd look at how they teach decisions, not just facts.|
S~A school gives possibility somewhere ordinary to begin.|
S~They sound proud of what students can become here.|
S~I'd like to hear from a student who has just started.
''')
add('rustboro_natures', 'RustboroCity_PokemonCenter_1F_Text_PokemonHavePersonalities',
    'A Trainer compares their naive Pokemon with a friend jolly Pokemon.', '''
S~Same adventure, very different opinions about how to enjoy it!|
S~Individual temperament is worth observing alongside species.|
N~Get to know the one beside you. A species name isn't the whole story.|
S~A little difference in how they react can tell you a lot.|
S~You notice personalities quickly when everybody wants different things.|
S~Two excellent characters refusing to be interchangeable.|
S~A naive one and a jolly one. That sounds like trouble with good intentions.|
N~Different temperaments may call for different approaches to training.|
S~Every familiar kind of creature can hold an unfamiliar someone.|
S~They noticed who their Pokemon is, not just what it is.|
S~I'd ask what each one does when meeting a stranger.
''')
add('rustboro_held_berry', 'RustboroCity_PokemonSchool_Text_PokemonHealItselfWithBerry',
    'A student struggles to record the many held items after learning about berries.', '''
S~The Berry lesson grew more branches than the notebook expected.|
S~Grouping items by what they do may make the notes easier to follow.|
N~One useful fact at a time. The rest can wait for the next page.|
F~I know that feeling when the next sentence starts before your pen catches up.|
S~Start with the Berry. At least that lesson comes with a snack.|
S~The syllabus has overtaken its faithful chronicler.|
N~Knowledge is plentiful. Margins, tragically, are finite.|
N~A small chart of item and effect would save a lot of writing.|
S~A crowded page is proof someone is trying to keep hold of things.|
S~I'd leave some blank space. There is always one more exception.|
S~We could ask the teacher to repeat the bit they missed.
''')
add('rustboro_manmade_items', 'RustboroCity_PokemonSchool_Text_PokemontCantUseManMadeItems',
    'A student explains why Pokemon cannot simply use held Potions or Antidotes themselves.', '''
F~Holding a bottle is not quite the same as understanding the bottle.|
N~Possessing an item does not supply the knowledge needed to apply it.|
N~Some jobs still need a Trainer paying attention.|
N~That's an easy mistake to make if nobody explains it.|
N~We should keep the medicine where we can actually use it.|
N~An excellent prop cannot perform its own instructions.|
N~A cure sitting uselessly in someone's paws is rather bleak.|
N~Packaging and application matter as much as the contents.|
N~A helpful thing still needs a helpful hand.|
N~They aren't being difficult. It simply isn't a tool they understand.|
N~I'd check what a held item actually does before a battle.
''')
add('rustboro_quickclaw', 'RustboroCity_PokemonSchool_Text_ExplainQuickClaw',
    'The teacher explains Quick Claw occasional priority and the breadth of held item study.', '''
U~A little claw can make a big surprise at the start of a turn.|
N~Its benefit is occasional. Planning should account for that uncertainty.|
N~Useful when it works. Don't build the whole plan around it.|
N~I would remember the word occasionally before counting on it.|
N~A helpful bonus still isn't a promise.|
N~A small accessory with impeccable dramatic timing, on certain days.|
N~The claw offers punctuality without committing to a schedule.|
N~Compare its occasional benefit against a more consistent item.|
N~A small chance can turn an otherwise certain moment.|
N~He gave us an example and a whole new subject to investigate.|
N~I'd watch for the moment it changes the order of a battle.
''')

add('mauville_bike_switch', 'MauvilleCity_BikeShop_Text_ComeBackToSwitchBikes',
    'Rydel invites the player to return if they want to exchange bicycle types.', '''
S~We can change our mind without having to grow a second pair of legs!|
S~He allows the choice to adapt to the terrain we encounter.|
S~Good service. We aren't stuck with the first decision.|
S~That takes some of the worry out of choosing.|
S~Nice to have someone say come back and mean it helpfully.|
S~Rydel offers revisions after the first edition leaves the shop.|
S~A decision with an exit clause. How civilized.|
S~Different routes need different capabilities. The exchange is practical.|
S~A path can ask for a different way of moving.|
S~He wants us happy with the bike after we leave too.|
S~I'd tell him how the last ride went when we come back.
''')
add('mauville_bike_keep', 'MauvilleCity_BikeShop_Text_HappyYouLikeIt',
    'Rydel is pleased when the player chooses to keep their current bicycle.', '''
S~The bike stays with us, and Rydel gets a happy answer.|
S~Our continued preference gives him useful feedback about the bike.|
S~It suits us. No reason to change what works.|
S~He sounds genuinely pleased that it has been useful.|
S~The best recommendation is someone still enjoying it later.|
S~A merchant delighted by the absence of a transaction. Charming.|
S~The bicycle has survived our latest review.|
S~We know this model's handling now. Familiarity has value.|
S~Some choices settle comfortably beside us.|
S~He isn't trying to talk us into a different taste.|
S~I'd share which part of riding it we enjoyed most.
''')
add('mauville_no_bike', 'MauvilleCity_BikeShop_Text_GuessYouDontNeedBike',
    'Rydel concludes that the player does not need a bicycle after their answer.', '''
F~Our feet may wish we had explained that differently.|
N~His conclusion follows our answer, though walking distance isn't the only need.|
N~No bike this time. We can keep moving on foot.|
F~I think that conversation ended sooner than I expected.|
N~We can always return if the walk changes our mind.|
N~A generous offer has vanished into a conversational misunderstanding.|
N~Our shoes have received another assignment.|
N~We should speak to him again if we do want to ride.|
N~For now, the road will meet our own footsteps.|
N~He took us at our word. That is fair enough.|
F~I wonder if he realizes we might want one anyway.
''')
add('mauville_manuals', 'MauvilleCity_BikeShop_Text_HandbooksAreInBack',
    'A bike shop worker is learning while working and directs riders to manuals in back.', '''
S~A shop with bikes, lessons, and someone learning alongside us!|
S~Accessible instructions are useful even when the worker is still training.|
N~Read before attempting the difficult tricks. Saves bruises.|
S~I like that they didn't pretend to know everything already.|
S~Good to know where to find an answer when you need one.|
S~The apprentice wisely introduces us to the resident paper experts.|
N~A manual: advice that waits patiently while I recover my dignity.|
S~Practice and a reference nearby are a good learning arrangement.|
S~There is no shame in keeping instructions within reach.|
S~An honest answer is much nicer than confident guessing.|
N~I'd ask which technique they found hardest to learn.
''')
add('mauville_rocks_wild', 'MauvilleCity_House1_Text_MonCanFlyOutOfSmashedRock',
    'The Rock Smash enthusiast warns that Pokemon may emerge from broken rocks.', '''
U~The boulder may have a tenant! That seems important before the smashing.|
N~Breaking a rock can disturb an animal sheltering inside it.|
N~Be ready for company when the rock breaks.|
N~That would be a rather startling way to meet someone.|
N~A useful warning before we open anybody's stone pantry.|
N~A blocked path may conceal a very offended resident.|
N~The rock may object through a representative.|
N~Keep the team ready. Breaking the obstacle may begin another encounter.|
N~Something quiet can be living in what looks empty.|
N~He sounds excited by a surprise I'd prefer to anticipate.|
N~I'd look carefully before choosing which rock to break.
''')
add('verdanturf_league_sequence', 'VerdanturfTown_House_Text_DefeatEliteFourInARow',
    'A resident explains the consecutive Elite Four challenge and restart after a loss.', '''
U~Four battles in a row. I would like four rows of supplies.|
N~Success requires conserving resources across the entire sequence.|
N~Prepare for the whole challenge, not just its first opponent.|
N~Starting over after coming close must be difficult.|
N~That calls for proper supplies and a plan for the rests between.|
N~A demanding structure: four acts, with no skipping the earlier pages.|
N~An institution with a very firm opinion about starting again.|
N~We should budget healing for several different kinds of opponent.|
N~Endurance will matter alongside the strength of each battle.|
N~One setback doesn't erase what you learn for the next attempt.|
N~I'd ask someone who tried how they prepared the second time.
''')
add('verdanturf_wally_goal', 'VerdanturfTown_WandasHouse_Text_StrongerSpeech VerdanturfTown_WandasHouse_Text_StrongerSpeechShort',
    'Wally confidently promises to grow stronger and challenge the player again.', '''
S~He's turned losing into a reason to keep going. That's a sturdy kind of brave.|
S~He has made a goal he can work toward with Ralts.|
S~Good. We'll take him seriously when he's ready.|
S~His voice sounds more certain when he talks about the next battle.|
S~A purpose can put a little strength back into your day.|
S~A rival has announced his return before leaving the room. Excellent spirit.|
S~He is planning to be a problem for us. I approve of the ambition.|
S~Training gives that confidence somewhere useful to go.|
S~He is looking forward instead of staying inside the loss.|
S~That challenge asks us to believe he can grow. I do.|
S~I'd like to see how he and Ralts change together.
''')
add('verdanturf_wanda_intro', 'VerdanturfTown_WandasHouse_Text_MeetWanda',
    'Wanda recognizes the player from Wally stories and says he is healthier and livelier.', '''
S~Wally has been telling stories about us. I hope my imaginary height was reasonable.|
S~She has noticed an encouraging change in his energy and health.|
S~Good to hear he's doing better here.|
F~It is a strange feeling when someone knows you through another person's stories.|
S~He sounds like he's found somewhere he can breathe more easily.|
S~We arrive already introduced by a very enthusiastic narrator.|
S~Our reputation reached the room first. Mercifully, it seems friendly.|
N~A supportive place can make a real difference to someone's daily life.|
S~She speaks of him as someone unfolding, little by little.|
S~She noticed his liveliness as much as his health. That's affectionate.|
S~I'd ask what he has been enjoying most since arriving.
''')
add('verdanturf_wanda_trust', 'VerdanturfTown_WandasHouse_Text_DontWorryAboutWally',
    'Wanda trusts Wally abilities and the Pokemon traveling with him.', '''
S~She knows the worried parts of him and still sees the brave parts.|
N~Her confidence comes from knowing him, rather than knowing nothing can happen.|
S~She trusts him. We can give him room to prove himself.|
S~Hearing that from someone close to him means a lot.|
S~It's good that his family can see what he is learning to do.|
S~Wanda declines to cast him as the helpless child in his own story.|
S~A quiet vote of confidence can be surprisingly formidable.|
N~He isn't traveling without support. His Pokemon are part of his preparation.|
S~Care can open its hand without disappearing.|
S~She lets him be capable while still being fond of him.|
S~I'd like Wally to know she speaks about him this way.
''')
add('verdanturf_boyfriend_done', 'VerdanturfTown_WandasHouse_Text_CanSeeGirlfriendEveryDay',
    'Wanda boyfriend thanks the player because the cleared tunnel lets them meet daily.', '''
S~A tunnel full of rocks became an ordinary way to say hello every day.|
S~Removing a physical barrier has made a daily relationship easier.|
S~Glad we could help. He certainly put the work in.|
S~He sounds happiest about the small, everyday part.|
S~Now meeting her doesn't have to be a whole expedition.|
S~A grand labor earns its finest reward: an unremarkable daily visit.|
S~Romance has acquired a significantly better commute.|
S~Opening the route made his effort useful to the whole town too.|
S~An open path can make two homes feel closer.|
S~No elaborate declaration. Just happiness at seeing her often.|
S~That's a lovely thing to hear after all that digging.
''')
add('verdanturf_boyfriend_work', 'VerdanturfTown_WandasHouse_Text_DaughtersBoyfriendDriven',
    'Wanda mother describes his relentless tunnel digging and Wanda concern for him.', '''
F~Digging to see someone is devoted. Forgetting to stop digging sounds less useful.|
N~Sustained manual work needs rest, however strong the motivation.|
N~His determination is clear. Someone should make sure he takes breaks.|
N~She goes to see him because she worries. He might not notice that part.|
N~I'd send a meal before sending another shovel.|
N~A love story whose central obstacle is also its occupational hazard.|
N~Passion has a shovel. Sensible rest appears unarmed.|
N~A plan and proper tools would help that effort go further.|
N~Devotion should leave room for the person doing the devoting.|
N~Wanda cares enough to worry about the way he is trying.|
N~I'd ask whether anyone has offered to help him finish safely.
''')
add('verdanturf_boyfriend_praise', 'VerdanturfTown_WandasHouse_Text_DaughtersBoyfriendWasDigging',
    'After the tunnel is cleared, Wanda mother marvels that he had been digging by hand.', '''
U~By hand! My hands became tired just hearing that.|
N~An extraordinary amount of manual effort, even before the final barrier.|
N~He earned that praise. I'm glad the route is open now.|
S~She sounds as if she still can't quite believe the work he did.|
N~I would make sure those hands get a good long rest.|
S~A story the family will be telling at every gathering for years.|
N~Love is patient. His hands must be considerably less patient.|
N~Determination got him a long way. Suitable tools still matter.|
N~The finished passage hides how slowly he made it.|
S~She's clearly found a new reason to think well of him.|
U~I'd want to hear which part of the digging he remembers most.
''')
add('verdanturf_uncle_hope', 'VerdanturfTown_WandasHouse_Text_WallysNextDoor',
    'Wally uncle credits the environment and Pokemon with improving his health and hope.', '''
S~The air helps, and Ralts gives him a reason to look ahead.|
N~Several changes may be helping. His uncle wisely leaves room for that.|
S~Better surroundings and a partner beside him. Good foundations.|
S~Hope can show in the way someone carries themselves.|
S~It's good to hear the family noticing his better days.|
S~An improvement large enough to interrupt an ordinary introduction.|
S~A small Pokemon has become a surprisingly substantial source of courage.|
N~He has more support now, both in his surroundings and his routine.|
S~Something in his future has begun to feel possible.|
S~His uncle sees a happier child, not just a healthier one.|
S~I'd like to hear Wally tell us what feels different.
''')
add('verdanturf_uncle_far', 'VerdanturfTown_WandasHouse_Text_WallyGoneThatFar',
    'After Victory Road, Wally uncle admires how far Wally has traveled alone.', '''
S~He's proud and surprised enough to borrow a little family credit.|
N~The distance Wally covered is evidence of real growing independence.|
S~Wally earned that respect. That was no small trip.|
S~You can hear the worry making room for pride.|
S~He'll have a lot to tell them when he comes home.|
S~The family has discovered its quiet boy was writing an adventure.|
S~A deserved compliment with a small hereditary claim attached.|
N~He should hear about the planning and battles behind that distance too.|
S~Someone he remembers as small has reached a far horizon.|
S~His picture of Wally is catching up with who Wally has become.|
S~I'd love to hear the family ask Wally about that journey.
''')
add('mossdeep_taste_none', 'MossdeepCity_House1_Text_DoesntLikeOrDislikePokeblocks',
    'The taste assessor finds no particular Pokeblock flavor preference in the lead Pokemon.', '''
S~An unbiased snack judge! That is a rare and powerful talent.|
N~No clear flavor preference was identified. Neutrality is a useful result too.|
N~No favorite flavor. We can work with that.|
S~It doesn't have to pick a favorite just because we ask.|
S~An easygoing eater makes serving everybody a little simpler.|
S~Our critic has issued the most even-handed review imaginable.|
N~A passionate commitment to having no strong opinion. Respectable.|
N~Then we should choose for the effect we need, rather than a favorite taste.|
S~Some palates do not divide the world into favorites.|
S~A neutral answer can be just as honest as an enthusiastic one.|
N~I'd still watch how it reacts when we offer different kinds.
''')
add('mossdeep_taste_yes', 'MossdeepCity_House1_Text_ItLikesXPokeblocks',
    'The taste assessor confidently identifies the lead Pokemon preferred Pokeblock flavor.', '''
U~A whole favorite snack detected with one look! My face must be full of menus.|
N~That is a specific prediction. Our Pokemon's response can confirm it.|
N~Useful to know. We can pay attention next time we offer one.|
S~Small preferences make it easier to know someone.|
S~Now that's a detail I can use when preparing a treat.|
S~He has delivered a culinary verdict with remarkable conviction.|
N~He knows what it likes. I am relieved someone is certain.|
N~Let's remember the flavor and compare how it responds.|
S~A favorite taste is a small doorway into another creature's world.|
S~Knowing a preference is such an easy way to be thoughtful.|
S~I'd ask how he learned to recognize that at a glance.
''')
add('mossdeep_taste_wife', 'MossdeepCity_House1_Text_HusbandCanTellPokeblockMonLikes',
    'A wife proudly describes her husband ability to identify Pokemon taste preferences.', '''
S~That's a useful household talent. Can he identify what I want for lunch?|
N~I'd be interested in which visual cues inform his assessment.|
S~She's proud of what he can do. Sounds useful.|
S~She has probably watched him get it right a lot.|
U~I usually have to offer a few bites before I learn that much.|
S~An expert supplied with an enthusiastic local endorsement.|
S~An oddly specific gift. Those are often the best ones.|
N~I'd ask whether he explains the reasoning to people who want to learn.|
S~She has made room for his unusual knowledge in her affection.|
S~That is the sound of somebody enjoying their partner's little brilliance.|
S~I'd ask her which prediction surprised her most.
''')
add('mossdeep_mail', 'MossdeepCity_House2_Text_PokemonCarriesMailBackAndForth',
    'A resident stays close to a Fortree friend through Pokemon-carried mail.', '''
S~The sea between them has a very reliable Wingull-shaped bridge.|
S~Regular letters can sustain familiarity across substantial distance.|
S~They found a way to keep in touch. Good for them.|
S~A familiar letter can make a faraway person feel close for a while.|
S~I imagine the arrival is a happy part of the day.|
S~Two people refuse to let geography edit each other out.|
S~A letter doesn't have to be loud to fill an empty room.|
S~A dependable messenger makes the arrangement possible. Credit to the Pokemon.|
S~Something crosses the water, and the distance becomes gentler.|
S~She sounds secure in the connection. That's lovely.|
S~I'd love to hear how their first letter found its way across.
''')
add('mossdeep_sister', 'MossdeepCity_House2_Text_SisterMailsBoyfriendInFortree',
    'A resident insists she does not envy her sister mail relationship with a Fortree boyfriend.', '''
S~No envy at all, announced with unusually careful emphasis.|
N~The additional denial suggests the subject has some emotional importance.|
N~She can feel how she feels. No need to press her on it.|
F~I don't think she'd enjoy us asking that question again.|
S~A little envy doesn't mean she isn't happy for her sister.|
M~A denial so emphatic it has volunteered to become the evidence.|
S~I believe she has successfully convinced absolutely one person. Possibly.|
N~We could ask about her own interests instead of teasing her.|
N~A feeling can be present without needing an audience.|
S~I recognize that tone. Let's give her some dignity.|
N~I'd rather get to know her than make her defend that sentence.
''')
add('mossdeep_rod_decline', 'MossdeepCity_House3_Text_DontYouLikeToFish',
    'The fisherman is surprised when the player declines his Super Rod.', '''
F~He sounds as if we declined the existence of the sea.|
N~Declining equipment doesn't establish a dislike of the activity.|
N~Not right now is a perfectly good answer.|
F~I think he expected everyone to be as excited as he is.|
S~A generous offer can still arrive on a day you aren't interested.|
N~Our refusal has disturbed a fundamental article of his faith.|
N~Fishing has discovered a dissenting opinion.|
N~We can return if the equipment becomes useful later.|
N~The water will still be here when curiosity arrives.|
N~He means well. His enthusiasm just skipped a possible answer.|
N~I'd ask him about a good catch instead of arguing about preferences.
''')
add('mossdeep_rod_received', 'MossdeepCity_House3_Text_TryDroppingRodInWater',
    'After receiving the Super Rod, the fisherman urges the player to try different waters.', '''
U~A new rod and an ocean full of possible introductions!|
S~Different waters may yield different species. Observation will help.|
N~Try a safe spot first and keep a steady grip.|
S~Waiting to see what answers sounds rather peaceful.|
S~We should bring something to eat if we plan to wait a while.|
S~A simple invitation to let the sea provide the next surprise.|
S~A socially acceptable reason to stare into water in silence.|
N~We can compare a few locations rather than assuming they are alike.|
N~Lower a line into an unseen place and something may answer.|
S~He wants us to discover the pleasure of it ourselves.|
S~I'd ask which local spot gave him his most surprising bite.
''')
add('mossdeep_rod_after', 'MossdeepCity_House3_Text_GoAfterSeafloorPokemon',
    'The fisherman recommends using the acquired Super Rod for deep-dwelling Pokemon.', '''
U~Our line can introduce us to neighbors who live a very long way downstairs.|
N~That equipment opens encounters beyond what the simpler rods allow.|
N~Deep-water Pokemon. Be ready before you bring one up.|
N~It's strange to wait above a place you can't see.|
S~The sea has a lot more going on than the surface admits.|
S~Our next visitor may have traveled farther vertically than we did horizontally.|
N~Something from the depths. At least we have been warned.|
N~Stronger equipment gives us different opportunities, not guaranteed easy catches.|
N~The seafloor is distant even while it lies beneath us.|
N~A whole different kind of encounter, hidden below ordinary water.|
N~I'd like to hear which deep-dwelling Pokemon he's met himself.
''')
add('mossdeep_base_find', 'MossdeepCity_House4_Text_MakeSecretBase',
    'A child enthusiastically promises to find a Secret Base the player builds.', '''
S~Our secret base has already acquired a very determined future visitor.|
N~Its secrecy may be less durable than its walls.|
S~A visitor is fine. Knocking first would be better.|
F~I might need a moment to tidy before he finds it.|
S~I'd better make room for a guest, apparently.|
M~A hideaway announced to its future discoverer. A challenging premise.|
S~Secret in the same sense as a surprise everyone knows about.|
N~A good location should be comfortable as well as hard to spot.|
S~Hidden places can still welcome a friendly knock.|
S~He has turned decorating into an invitation without asking.|
S~I'd ask what clues he follows when looking for one.
''')
add('mossdeep_abilities', 'MossdeepCity_PokemonCenter_1F_Text_AbilitiesMightChangeMoves',
    'A Trainer warns that abilities can change moves or prevent them from working.', '''
N~The move might be right, but the Pokemon on the other end has opinions.|
N~A move's normal effect is conditional on the target's abilities.|
N~If something fails, work out why before trying it again.|
N~A quiet ability can change the whole moment.|
N~It's worth knowing what went wrong before blaming a partner.|
N~A hidden condition can overturn the most confident declaration.|
N~The plan has encountered fine print with teeth.|
N~Watch the result carefully. An unexpected interaction gives us information.|
N~What cannot be seen may still change the path of a thing.|
N~Appearances alone won't tell us what a move can accomplish.|
N~I'd ask for an example they've actually run into.
''')

add('pacifidlog_regi_story', 'PacifidlogTown_House1_Text_RegiStory',
    'A resident retells a childhood story of three cave-hidden Pokemon representing rock, ice, and steel.', '''
U~Three kinds of power, each with a cave to call home. That's a sturdy old story.|
N~An oral account gives us leads, though not confirmation of each detail.|
N~Old cave stories deserve respect and a little caution.|
N~He has carried that story since childhood. It must have stayed vivid.|
S~I like hearing what people remember being told when they were small.|
S~Three hidden figures and three materials. A story built to survive retelling.|
N~Ancient cave residents. I trust nobody plans to knock carelessly.|
N~I'd compare that account with any ruins or inscriptions we find.|
N~Stone, frost, metal. Three different ways for time to hold still.|
N~The way he remembers it matters, even before we know what's true.|
N~I'd ask who first told him, and whether they named the caves.
''')
add('pacifidlog_dots', 'PacifidlogTown_House1_Text_SixDotsOpenThreeDoors',
    'A resident remembers her grandfather cryptic saying about six dots and three doors.', '''
U~A door that wants dots instead of a key. I would have packed incorrectly.|
N~A repeated pattern of six dots may carry information rather than decoration.|
N~Keep the wording in mind. It may mean something somewhere else.|
N~A small sentence can outlast the person who explained it.|
N~I would write that down before the numbers get muddled.|
N~An inherited riddle, waiting for the right page of the story.|
N~Grandpa left an interestingly unhelpful set of instructions.|
N~I'd look for grouped marks near any unusual doors. Carefully.|
N~An old voice can leave a question open for another generation.|
N~She remembers the exact words even without understanding them.|
N~I'd ask whether he said it while showing her something.
''')
add('pacifidlog_yes_town', 'PacifidlogTown_House4_Text_YesTown',
    'The boy interprets the player yes answer as the name of their hometown.', '''
L~Yes Town! Convenient place for people who agree on everything.|
N~He interpreted an answer category as a location. A reasonable confusion here.|
S~We should try that introduction again with an actual place name.|
F~I don't think either of us answered the question we thought we heard.|
S~I'd hate to give directions from Yes Town to Maybe Village.|
M~A new settlement has been founded by conversational accident.|
S~Yes Town sounds exhausting. No quiet dissent anywhere.|
N~The question and the available answer clearly didn't fit each other.|
S~A place invented in the little gap between two meanings.|
S~He is being perfectly sincere, which makes it rather sweet.|
L~Now I want to hear what he thinks Yes Town looks like.
''')
add('pacifidlog_nowhere', 'PacifidlogTown_House4_Text_YouHaveToComeFromSomewhere',
    'The boy is confused by the player no answer and jokes about a seafloor birthplace.', '''
L~Born under the sea would make the first walk to school quite ambitious.|
N~He has correctly rejected nowhere, then selected a rather unusual alternative.|
S~Let's give the kid a straight answer before this gets stranger.|
F~I think he is doing his best with a very unhelpful answer.|
S~An underwater birthday party would complicate the cake considerably.|
M~Our mysterious origin has acquired gills through a clerical misunderstanding.|
S~From nowhere to the seafloor. An impressively rapid escalation.|
N~We should clarify the town name rather than extend this faulty premise.|
S~Every path begins somewhere, even one arriving over water.|
S~I admire how hard he is trying to make the answer work.|
S~I'd tell him about home before he invents anything deeper.
''')
add('pacifidlog_mirage_absent', 'PacifidlogTown_House5_Text_CantSeeMirageIslandToday',
    'The watcher cannot see Mirage Island today.', '''
N~No island today. The horizon is keeping its special guest list private.|
N~Today's observation is negative. It does not settle whether visibility can change.|
N~Nothing to see from here today. We can check another time.|
D~He sounds as if he has spent a long time looking.|
N~A patient job, staring at water that usually stays water.|
N~The elusive island has declined another appearance.|
N~An absence with a very dedicated audience.|
N~I would keep a record of when he checks and what he sees.|
N~Some mornings the sea offers only distance.|
N~That little disappointment sounds very familiar to him.|
N~I'd ask what it looked like the last time he saw it.
''')
add('pacifidlog_mirage_present', 'PacifidlogTown_House5_Text_CanSeeMirageIslandToday',
    'The watcher excitedly reports that Mirage Island is visible today.', '''
U~Today is an island day! I didn't know days could have that category.|
U~A positive observation. We should note where he is looking.|
N~If we plan to investigate, check the route while it is visible.|
U~All that watching finally found something. Listen to his voice.|
S~That is a good reason to put everything down and look.|
U~The absent guest has arrived, to the delight of its faithful host.|
U~An island has chosen to be conspicuous. How unlike it.|
N~We should record the conditions before they change.|
U~A hidden place has entered the ordinary daylight.|
S~He's earned the right to be that excited about a horizon.|
U~Show me where! I want to see what he has waited for.
''')
add('pacifidlog_mirage_theory', 'PacifidlogTown_House5_Text_MirageIslandAppearDependingOnWeather',
    'A resident considers weather and a genuinely appearing island as competing explanations.', '''
N~Either the air is playing tricks or the island has very unusual manners.|
N~Those are different hypotheses. Repeated observations could help distinguish them.|
N~Interesting question. Best not treat either answer as settled.|
N~I like that he leaves room for not knowing.|
N~I'd listen to the people who spend every day watching this water.|
N~An optical explanation competes with a much more dramatic island.|
N~Weather is strange enough without land developing a schedule.|
N~Comparing sightings with weather records would be a useful start.|
N~Seeing a thing and understanding its arrival are separate mysteries.|
N~He lets his neat explanation stay a question. Sensible.|
N~I'd gather a few different accounts before choosing a story.
''')
add('sootopolis_orbs_soothe', 'SootopolisCity_House2_Text_YesTwoOrbsSideBySide',
    'The old woman finds the paired orbs at Mt Pyre soothing.', '''
S~Two little circles making a whole mountain feel a bit calmer.|
N~The paired arrangement has an emotional significance for her.|
N~Some sights make people feel things they can't easily explain.|
S~I understand remembering how a place feels more than what it looks like.|
S~A quiet place can leave you with something peaceful to carry home.|
N~She offers a feeling rather than an explanation. Sometimes that is enough.|
S~An appreciation of still objects in a quiet place. Understandable.|
N~I'd be interested in how the orbs were placed there originally.|
S~Two shapes keeping each other company at the summit.|
S~Something about them together matters more to her than either alone.|
N~I'd ask what else she remembers about that visit.
''')
add('sootopolis_orbs_visit', 'SootopolisCity_House2_Text_OughtToVisitAndSee',
    'The old woman recommends visiting Mt Pyre to see its two orbs.', '''
N~Some things don't quite fit into a description from a living room.|
N~A visit would let us observe the setting she is describing.|
N~Worth seeing respectfully if our route takes us there.|
N~She sounds like she wants us to understand the place for ourselves.|
N~I'd leave time for a quiet visit instead of rushing through.|
N~A recommendation to let the location tell its own part of the story.|
N~A mountaintop visit. Quiet, probably, though less convenient than this chair.|
N~We can look without disturbing what people have placed there.|
N~Some meanings wait where the stones stand.|
N~I'd remember that it is a place other people visit for serious reasons.|
N~I'd ask what a first-time visitor should be mindful of.
''')
add('sootopolis_ruins', 'SootopolisCity_House4_Text_AncientTreasuresWaitingInSea',
    'A resident speculates that local underwater ruins may contain ancient treasure.', '''
U~Old ruins under the sea! Even finding the front door sounds exciting.|
N~The ruins and the treasure are claims with different levels of certainty.|
N~Plan the dive before getting carried away by treasure talk.|
N~I wonder who last walked there when it was dry.|
N~A fascinating trip still needs enough supplies to come home.|
S~A rumor has supplied us with both a setting and a temptation.|
N~Ancient rooms underwater. At least the dust problem is solved.|
N~We should learn the currents and exits before exploring a ruin.|
N~A place beneath water may hold more history than gold.|
N~I would be curious about what people left, not only what it is worth.|
U~I'd ask who first found the ruins and what they actually saw.
''')
add('sootopolis_stroll', 'SootopolisCity_House4_Text_StrollUnderwaterWithPokemon',
    'A resident values an underwater walk with Pokemon even without finding treasure.', '''
S~A beautiful walk counts as finding something good, even if it doesn't fit in a bag.|
S~The environment itself can make exploration worthwhile.|
S~A good partner and a safe route. Plenty of reason to go.|
S~That sounds like a quiet memory I'd keep for a long time.|
S~An outing doesn't need a prize at the end to be a good one.|
S~A satisfying expedition that refuses to require a treasure chest.|
S~A walk where nobody can insist on conversation. Intriguing.|
N~I'd still check where we can surface before choosing a path.|
S~Light moving through water can be worth the journey alone.|
S~She has a lovely idea of what makes time well spent.|
S~I'd want to know what caught her eye first down there.
''')
add('sootopolis_volcano', 'SootopolisCity_House7_Text_CityFromEruptedVolcano',
    'An elder explains how an emerged volcanic crater filled with rainwater to form Sootopolis.', '''
U~The sea got a mountain, the mountain got a bowl, and the bowl got a town!|
S~Volcanic uplift created a basin that could collect rainwater. Remarkable setting.|
N~Good to know what we're standing on. This town has strong walls for a reason.|
N~It makes the quiet water look different when you imagine what came before.|
N~People found a place to live inside the remains of something enormous.|
S~A city occupying the peaceful aftermath of an astonishing entrance.|
N~A volcanic crater becomes a neighborhood. People are persistent.|
N~I'd ask how they manage water levels inside a basin like this.|
N~Violence made the hollow; rain taught it another life.|
N~The shape of the town tells a story much older than its buildings.|
U~I'd love to hear what the earliest settlers found here.
''')
add('slateport_need_veteran', 'SlateportCity_SternsShipyard_1F_Text_CouldUseAdviceFromVeteran',
    'Dock says calculations alone are insufficient and wants an experienced sailor advice.', '''
N~A ship should listen to someone who has actually been tossed around in one.|
S~Calculations benefit from observations gathered under real operating conditions.|
N~Ask the people who will trust it with their lives.|
N~It's good that he can say what he doesn't know yet.|
N~You learn things doing the work that no neat page quite explains.|
N~The designer seeks a reader who has survived the sea's harsher edits.|
N~The sea is unlikely to honor a convincing diagram.|
S~Exactly. Design needs feedback from the people using the finished machine.|
N~Experience remembers the wave that arrived unlike all the others.|
N~Knowing when to ask for help makes his confidence more credible.|
N~I'd ask which part of the ferry he most wants a sailor to inspect.
''')
add('slateport_briney_joined', 'SlateportCity_SternsShipyard_1F_Text_BrineyJoinedUs',
    'Dock reports steady ferry construction after experienced sailor Briney joins the project.', '''
S~They found the missing part of the plan, and it wears a sailor's hat.|
S~Practical experience is helping convert the design into a working vessel.|
S~Good team. One knows the build, the other knows the water.|
S~Dock sounds less alone with the problem now.|
S~Sometimes the best help is somebody who knows what to look for.|
S~The stalled project has acquired exactly the supporting character it needed.|
S~The ferry progresses. The doohickeys may finally have names.|
S~That's a useful collaboration: design knowledge and experience in service.|
S~Two kinds of knowing have found a common task.|
S~He gives Briney credit openly. That makes a good partnership.|
S~I'd love to hear what changed after Briney first looked it over.
''')
add('slateport_ferry_done', 'SlateportCity_SternsShipyard_1F_Text_FerryIsReady',
    'The S.S. Tidal is completed and Dock is already considering further improvements.', '''
S~The ferry is ready, and his next idea is already trying to climb aboard.|
S~A completed design can still suggest the questions for its successor.|
S~Finish well, celebrate it, then think about the next one.|
S~I hope he gives himself a moment to see what he has made.|
S~Get everyone a good meal before beginning the next enormous project.|
S~The triumphant ending has immediately sprouted a sequel.|
S~The boat is finished. The engineer is apparently not.|
U~I'd love to ask what he wants to improve and what this version taught him.|
S~A finished thing can become the beginning of another thought.|
S~He's proud without becoming too comfortable. That's a useful balance.|
S~I'd like to see his face when the first passengers come aboard.
''')
add('slateport_briney_team', 'SlateportCity_SternsShipyard_1F_Text_DecidedToHelpDock',
    'Briney credits meeting the player for renewed energy and joins Dock ferry project.', '''
S~Briney's next adventure is helping build everybody else's ride.|
S~He recognizes how his experience complements Dock's technical skills.|
S~Glad he's found good work with someone who values him.|
S~He sounds excited about having something new to be part of.|
S~Putting old experience toward a new purpose can feel wonderful.|
S~A veteran returns with renewed vigor and an excellent collaborator.|
S~Retirement appears to have lost its argument with a ferry.|
S~He is thinking about the passengers as well as the machine. I like that.|
S~A little renewed spirit can carry work toward a distant shore.|
S~His praise for Dock is as warm as his pride in his own experience.|
S~I'd love to hear the stories those two tell while working.
''')
add('slateport_seasick', 'SlateportCity_SternsShipyard_1F_Text_GetSeasickEasily',
    'A shipyard worker gets seasick and contributes from land instead.', '''
S~Helping the boat from a floor that stays put. An excellent compromise.|
S~He has found a role that uses his effort without triggering the problem.|
S~Still useful work. No need to suffer to prove he belongs.|
S~I'm glad there is a place for him here too.|
S~The people on the water need plenty done by people on land.|
S~A sensible character who has negotiated with his principal weakness.|
S~An admirable commitment to boats at a medically respectful distance.|
S~A working ship depends on far more than its crew.|
S~You can help a journey without taking the same path.|
S~He adjusted the role instead of giving up something he cares about.|
N~I'd ask what part he most enjoys working on here.
''')
add('slateport_living_sea', 'SlateportCity_SternsShipyard_1F_Text_SeaIsLikeLivingThing',
    'A shipyard worker describes sea conditions changing with weather, seasons, and moon.', '''
N~The sea has moods, and none of them agree to our timetable.|
S~Several interacting conditions make a single description insufficient.|
N~Check today's water. Yesterday's crossing isn't a guarantee.|
N~It can look familiar and sound different the next morning.|
N~The people who work here must learn to notice tiny changes.|
N~An immense, unpredictable presence with no obligation to explain itself.|
N~A living thing that is mostly water. We should get along famously.|
N~A vessel needs to handle changing conditions, not just a calm demonstration.|
N~The moon moves far away, and the water answers here.|
N~He knows the sea through changes most visitors might miss.|
S~I'd ask which change he notices before anyone else does.
''')
add('lilycove_motel_quiet', 'LilycoveCity_CoveLilyMotel_1F_Text_NoGuestsWithTeamAqua',
    'The motel owner says Team Aqua presence has driven away tourists.', '''
D~Empty rooms are another kind of mess Team Aqua has left behind.|
N~Perceived danger can damage a town's livelihood without a direct attack.|
N~People don't take holidays where they feel unsafe.|
D~A quiet motel sounds different when nobody chose the quiet.|
D~Buying food for guests who never come must be a difficult gamble.|
N~The villains have disrupted even the stories that aren't about them.|
N~Empty rooms are peaceful only when the owner can afford them.|
N~Removing the danger is the first step toward getting visitors back.|
D~A town can feel absence long before anything is broken.|
D~He's trying to watch television while worrying about the business.|
N~I'd ask how long the regular visitors have been staying away.
''')
add('lilycove_motel_booking', 'LilycoveCity_CoveLilyMotel_1F_Text_HeardAquaHideoutBusted',
    'After the hideout is cleared, the motel receives a large company reservation.', '''
S~One big booking sounds like fresh air coming into an empty building.|
S~Improved safety is already producing a visible local benefit.|
S~Good. The town can start getting back to ordinary business.|
S~He sounds distracted, but relieved underneath it.|
S~Time to check the pantry before that big group arrives.|
S~A defeated hideout produces a remarkably practical happy ending.|
S~The villains depart; a reservation arrives. Good exchange.|
N~He should write the company name down before the next distraction.|
S~Doors that stayed empty are expecting footsteps again.|
S~The name can wait a second. The relief is the real news.|
S~I'd like to hear how the town feels when visitors return.
''')
add('lilycove_motel_dinner', 'LilycoveCity_CoveLilyMotel_1F_Text_BetterGetWorkingOnGuestsDinner',
    'The motel owner remembers the arrived Game Freak group needs dinner after watching television.', '''
F~The television won't make dinner, even if the program has excellent snacks.|
N~His attention needs to return to the guests' immediate needs.|
N~We should let him work. A big group won't feed itself.|
F~I think he remembered the kitchen at exactly the right moment.|
N~First count the guests, then check what can be cooked in time.|
S~A room full of game makers faces its greatest challenge: a distracted host.|
N~The dinner has yet to become more than a concept. Concerning.|
N~A reminder by the television might prevent this particular scheduling problem.|
N~Hungry people have a way of bringing wandering thoughts home.|
N~Enthusiasm is lovely. Hospitality also needs something on the table.|
S~I'd leave him to it before our conversation becomes another delay.
''')
add('lilycove_motel_tv', 'LilycoveCity_CoveLilyMotel_1F_Text_CantSeeTheTV',
    'The motel owner complains when the player blocks his television and moves them aside.', '''
F~We have accidentally become the least popular show on television.|
N~We obstructed his view. The remedy seems straightforward.|
N~Let's move aside. No need to make a thing of it.|
F~I would rather not become the center of attention this way.|
N~Fair enough. I wouldn't stand between someone and their dinner either.|
M~Our unexpected appearance has received a brisk cancellation.|
N~My talent for blocking light has finally found an audience.|
N~A small change of position fixes the whole problem.|
N~We stood in the path of someone else's little escape.|
F~He has made his seating priorities extremely clear.|
S~I'd rather ask what he's watching from somewhere beside the screen.
''')

add('verdanturf_friend_none', 'VerdanturfTown_FriendshipRatersHouse_Text_DetestsYou',
    'The friendship assessor reports the lowest possible Pokemon friendship.', '''
D~That is hard to hear. Our partner is having an even harder time feeling it.|
N~The assessment points to a serious trust problem. Our routine needs to change.|
N~Take this seriously. Start treating that partner differently today.|
D~I don't want us to look away just because the answer hurts.|
N~A gentler routine matters more than finding a quick way to erase this.|
N~A painful review, and one that calls for action instead of excuses.|
D~That is a bleak result. A clever reply would not improve it.|
N~Let's identify what has been hurting trust and stop doing it.|
D~An open hand means little until it stops bringing hurt.|
N~This is information about how our partner feels, not an insult to dodge.|
D~We should watch their reactions and start earning something better.
''')
add('verdanturf_friend_wary', 'VerdanturfTown_FriendshipRatersHouse_Text_VeryWary',
    'The friendship assessor reports that the Pokemon remains deeply wary of its Trainer.', '''
D~That wary look isn't a challenge. It is a sign we've got work to do.|
N~Defensive behavior is consistent with low trust. Give it safer experiences.|
N~Don't crowd it. Show it that being with us can be safe.|
D~I wouldn't try to demand affection from that expression.|
N~Consistent care will mean more than one elaborate treat.|
N~Our next chapter needs fewer demands and better reasons to trust us.|
N~Wary eyes are entitled to keep their distance.|
N~We should review the routine and remove avoidable stress.|
N~A guarded creature needs reasons to lower its guard.|
N~Calling it vicious won't tell us why it feels this way.|
N~I'd give it space and pay attention to what makes it tense.
''')
add('verdanturf_friend_new', 'VerdanturfTown_FriendshipRatersHouse_Text_NotUsedToYou',
    'The friendship assessor says the Pokemon is unfamiliar with the Trainer and neutral.', '''
S~We are still in the learning-each-other's-weird-habits part.|
N~Neutral familiarity is a beginning, not evidence of rejection.|
N~Give it time. Trust isn't owed on the first day.|
S~It can be quiet between people who don't know each other yet.|
S~A steady routine is a good way to become familiar.|
N~We have been introduced. The relationship still needs to be written.|
S~A perfectly respectable initial opinion: undecided.|
N~Learn its signals instead of expecting it to know ours immediately.|
S~Roots do not appear the instant a seed meets soil.|
S~No need to force a closeness that hasn't had time to grow.|
S~We can start by noticing one small thing it likes.
''')
add('verdanturf_friend_growing', 'VerdanturfTown_FriendshipRatersHouse_Text_GettingUsedToYou',
    'The friendship assessor sees the Pokemon beginning to trust the Trainer.', '''
S~We're becoming a familiar face in the good way.|
S~Repeated contact is beginning to produce a trusting response.|
S~Good start. Keep giving it reasons to believe in us.|
S~A little trust can be a very big change.|
S~The small, ordinary things are starting to add up.|
S~A tentative friendship has found its first convincing lines.|
S~We have been promoted from stranger to probable ally.|
S~Consistency is working. We should keep the routine dependable.|
S~A cautious leaf has turned toward the light.|
S~It is beginning to expect good things from being with us.|
S~I'd pay attention to what it is comfortable doing beside us now.
''')
add('verdanturf_friend_fond', 'VerdanturfTown_FriendshipRatersHouse_Text_LikesYouQuiteALot',
    'The friendship assessor says the Pokemon is fond of the Trainer and wants extra affection.', '''
S~A formal request for a little extra fussing. I support the petition.|
S~It is comfortable enough to seek attention from us.|
S~We can spare a moment for our partner.|
S~It is nice when someone feels safe enough to ask for closeness.|
S~Some affection doesn't need to wait for a special occasion.|
S~Our devoted companion has submitted a modest demand for indulgence.|
S~A little pampering. A surprisingly reasonable ambition.|
S~Let's notice how it asks, so we recognize the signal next time.|
S~Being wanted can be as simple as staying a moment longer.|
S~There's confidence in asking to be treated tenderly.|
S~I'd put the next errand off for a small moment together.
''')
add('verdanturf_friend_happy', 'VerdanturfTown_FriendshipRatersHouse_Text_VeryHappy',
    'The friendship assessor reports a very happy Pokemon with strong affection.', '''
S~Our partner has given us a very good review without needing any words.|
S~A strongly positive assessment. Our day-to-day care appears to be working.|
S~Good. That's worth more than a lot of battle praise.|
S~I like knowing the happiness we see isn't just our imagination.|
S~A happy partner makes the ordinary parts of the trip better too.|
S~An excellent report from the one critic whose comfort matters most.|
S~Contentment. Quietly impressive, and much harder to fake than a pose.|
S~Let's keep doing what gives it that confidence and comfort.|
S~Something warm has settled into being together.|
S~That's the kind of praise you earn while nobody is watching.|
S~I'd like us to remember how it looks when it feels this safe.
''')
add('verdanturf_friend_max', 'VerdanturfTown_FriendshipRatersHouse_Text_AdoresYou',
    'The friendship assessor reports the highest affection and is delighted to witness it.', '''
S~So much fondness it spilled over and made the rater happy too!|
S~The strongest possible assessment. That reflects a well-established bond.|
S~Our partner feels at home with us. Let's keep deserving that.|
S~It is a little overwhelming to hear something so kind said plainly.|
S~All those ordinary days have become something wonderful.|
S~A love story with no need for a more dramatic witness.|
S~Even I have run out of gloomy qualifications for that result.|
S~The best outcome still needs everyday care. We're doing well.|
S~Some closeness becomes so steady it warms the room around it.|
S~The happiness on the rater's face says how clear it is to see.|
S~I'd treasure this moment without making our partner perform for it.
''')
add('devon_talking', 'RustboroCity_DevonCorp_2F_Text_DeviceForTalkingToPokemon',
    'A researcher says their device for talking to Pokemon has had little success.', '''
N~A machine for asking Pokemon questions. First question: was that really my lunch?|
N~Communication research needs a way to distinguish meaning from coincidence.|
N~Big goal. Keep listening to what Pokemon already tell us too.|
N~Even if it never works, I like that someone wants to understand.|
S~I'd be delighted to ask a partner what they actually want for dinner.|
S~Imagine interviewing a Pokemon and discovering it has notes about us.|
N~A device that could confirm exactly how unimpressed a Pokemon is. Dangerous.|
N~I'd ask what response they count as evidence of progress.|
N~A voice may be present long before we learn how to hear it.|
N~I wonder whether the hardest part is translation or paying attention.|
S~I'd want to hear what question made the researcher begin this project.
''')
add('devon_balls_pending', 'RustboroCity_DevonCorp_2F_Text_DevelopingNewBalls',
    'A researcher is struggling to develop new kinds of Poke Balls.', '''
N~A small round invention can contain a very large pile of failed ideas.|
N~A lack of visible progress is common when several constraints interact.|
N~Hard work takes time. Better to get it right.|
N~It sounds discouraging when the result won't show what you've tried.|
N~Some days you only learn what doesn't work yet.|
N~The brilliant invention has reached its unglamorous middle chapter.|
N~The prototypes are refusing to become achievements on demand.|
N~I'd ask which part is holding them up: materials, function, or reliability.|
N~An unfinished thing can still carry a great deal of thought.|
N~They sound tired of explaining the distance still left to go.|
N~I'd ask about the latest attempt, not just the finished result.
''')
add('devon_balls_ready', 'RustboroCity_DevonCorp_2F_Text_WeFinallyMadeNewBalls',
    'The researcher celebrates working Repeat and Timer Balls with different capture uses.', '''
U~One remembers who we've met; the other appreciates a long battle. Clever little spheres!|
S~Two designs for different conditions. Their value depends on the encounter.|
N~Know which one fits the situation before you throw it.|
S~They finally get to say it works. That must feel good.|
S~A long wait made into a tool for a different long wait.|
S~The prototypes have graduated to named, useful inventions.|
S~Patience has become a product. An unusually tidy development.|
U~They solved distinct problems with distinct designs. I'd love the details.|
N~Familiarity and passing time can each alter an encounter.|
S~The excitement sounds earned after hearing how hard it was before.|
S~I'd ask which successful test finally convinced the team.
''')
add('devon_dreams', 'RustboroCity_DevonCorp_2F_Text_DeviceToVisualizePokemonDreams',
    'A researcher is struggling with a machine to show Pokemon dreams.', '''
U~I wonder whether a Pokemon dreams about us dreaming about its dreams.|
N~Producing an image and verifying that it represents a dream are separate problems.|
N~Interesting work. Make sure the Pokemon can rest comfortably.|
N~Some dreams might be very quiet things to show another person.|
S~I'd love to know whether their favorite meals turn up there too.|
S~A machine proposing to publish a very private kind of story.|
N~I am uncertain any of us need our dreams presented without editing.|
N~I'd ask how they can test accuracy without asking the dreamer directly.|
N~The sleeping mind keeps a country no one else can walk into.|
N~A lovely idea, if the dreamer is comfortable with the looking.|
N~I'd want to hear what first made them curious about those dreams.
''')
add('devon_pokenav_pride', 'RustboroCity_DevonCorp_2F_Text_IMadePokenav',
    'The PokeNav inventor is proud and grateful to have made a useful invention.', '''
S~He made a thing that helps people get un-lost. That's worth smiling about.|
S~He can connect a finished invention to a clear benefit for its users.|
S~Useful work. He has earned some pride in it.|
S~He sounds happy just knowing it exists because of his work.|
S~Making something people carry on their journey must feel special.|
S~A creator allowing himself an entirely deserved moment of satisfaction.|
S~A successful project. I hear those exist occasionally.|
S~I understand that feeling: an idea finally becoming something someone can use.|
S~Something he imagined now travels farther than this room.|
S~He credits his good fortune as well as his skill. I like that.|
S~I'd ask which part he remembers finally getting right.
''')
add('devon_fossil_wait', 'RustboroCity_DevonCorp_2F_Text_FossilRegeneratorTakesTime',
    'The fossil scientist asks for patience while the regeneration machine works.', '''
N~Bringing back an ancient Pokemon probably deserves more time than boiling an Egg.|
N~A substantial process can be impressive without being fast.|
N~Let it work. We can use the time for something else.|
N~I would rather wait than ask him to rush something this delicate.|
N~Some important things simply aren't improved by standing over them.|
N~Prehistory has waited this long. We can manage a short interval.|
N~The ancient past is experiencing a minor delay.|
N~Speed isn't the only design goal. Reliability matters much more here.|
N~A very old beginning is taking its time to return.|
N~He is proud enough of the machine to admit its drawback.|
N~I'd ask when we should check back, then give him room to work.
''')
add('fallarbor_tutor_farewell', 'FallarborTown_MoveRelearnersHouse_Text_ComeBackWithHeartScale',
    'The move relearner ends the visit with a reminder that teaching costs a Heart Scale.', '''
N~A Heart Scale is his lesson fee. I should stop thinking of them as shiny pocket clutter.|
N~He has specified the resource required for another lesson.|
N~Keep a scale handy if a partner needs an old move back.|
N~It's good to know there is a way to revisit something forgotten.|
N~We'll know what to save when we find another one.|
N~A specialist whose tuition policy fits in one small sentence.|
N~A tiny object purchases a second chance at remembering. Reasonable.|
N~We should decide what move we need before spending the scale.|
N~A lost skill may be closer than it feels.|
N~I like that the door stays open for another visit.|
N~I'd keep track of which partners might benefit from coming back.
''')
add('fallarbor_lanette', 'FallarborTown_PokemonCenter_1F_Text_LanetteGreeting',
    'Lanette introduces herself as the Pokemon Storage System developer and invites a home visit.', '''
S~We met the person behind the PC, and she nearly forgot the person part.|
S~Her deduction was plausible. Her introduction arrived a little later.|
S~Useful system, friendly person. Good to put a face to the work.|
F~I understand getting caught up explaining something before saying your name.|
S~She's glad people use her work. That makes the invitation feel warm.|
S~An introduction that takes the scenic route through a proof.|
S~Social preliminaries have survived a brief encounter with deductive reasoning.|
U~I'd love to ask how she made the system manageable for so many Trainers.|
S~A familiar convenience has turned out to have a face and a home.|
S~She noticed the awkwardness and softened it herself. I like her.|
S~A visit to Route 114 might give us more time to hear her story.
''')
add('fortree_nav', 'FortreeCity_PokemonCenter_1F_Text_DoYouKnowAboutPokenav',
    'A Trainer enthusiastically explains PokeNav calls and rematch notices.', '''
S~A map, a conversation, and a way to learn who wants to battle us again. Busy little thing!|
N~Communication and rematch information are useful features in one portable tool.|
N~Good way to check in before walking all the way back.|
S~It's nice to talk to someone when the road has taken you far away.|
S~A quick call can save a long trip made on a guess.|
S~Our earlier opponents now have a convenient way to request an encore.|
S~A pocket full of people. Fortunately, they can be put away.|
S~Clear rematch notices solve a very practical travel problem.|
S~A familiar voice can find you between unfamiliar places.|
S~He likes the convenience, but he sounds happiest about staying connected.|
S~I'd ask who was the first person he called with it.
''')
add('fortree_safari_tip', 'FortreeCity_PokemonCenter_1F_Text_GoToSafariZone',
    'A visitor recommends the Safari Zone for Pokedex research.', '''
S~A place full of Pokemon we might not have met. That is a strong recommendation.|
S~A designated habitat can be useful for broadening our recorded observations.|
N~Worth checking the rules before heading inside.|
S~I'd enjoy looking around without rushing to the next town.|
N~We should find out what to bring before making the trip.|
S~A remarkably concise travel guide: go where the interesting creatures are.|
N~A destination with an admirably honest name.|
N~I'd ask which species made that visit worthwhile for him.|
N~A different stretch of land may answer different questions.|
N~His advice is specific enough to be useful.|
S~I'd love to hear what surprised him most when he visited.
''')
add('fortree_records', 'FortreeCity_PokemonCenter_1F_Text_RecordCornerIsNeat',
    'A Trainer enjoys mixing records while admitting not understanding the technical process.', '''
S~He doesn't know how it works, but he knows he had fun. Respectable review.|
N~Enjoying a system and understanding its implementation are separate things.|
S~Fair enough. You can use something without taking it apart.|
S~It's nice hearing someone sound excited without pretending to know everything.|
S~You don't need the whole recipe to know you enjoyed the dish.|
S~An unusually candid enthusiast. The mystery has not impaired the applause.|
S~A user who admits uncertainty. We should treasure this one.|
N~I'd ask what changed afterward. That tells us about the useful part.|
S~An exchange can leave a trace even when its workings remain hidden.|
S~He knows what he liked and where his explanation stops.|
N~I'd ask which part he would show a first-time visitor.
''')
add('sootopolis_fans_absent', 'SootopolisCity_House3_Text_LonesomeTryWorkingHarder',
    'A woman tells the player to work harder to acquire fans.', '''
N~We can have a good journey without appointing an official cheering section.|
N~A fan count is not a reliable measure of skill or companionship.|
N~We have people who matter to us. That is enough.|
F~I don't think I would be comfortable with a crowd following us anyway.|
N~A few good friends beat a room full of hungry expectations.|
N~The publicity department has mistaken obscurity for loneliness.|
N~A small audience sounds like a feature, personally.|
N~Training well is a better goal than trying to control who admires us.|
N~A quiet life can be full of people who care.|
N~Being liked and being watched are different kinds of attention.|
N~I'd rather know who she enjoys spending time with than count fans.
''')
add('sootopolis_fans_yes', 'SootopolisCity_House3_Text_YouMustBePrettyStrong',
    'A woman assumes the player must be strong because they have fans.', '''
S~People cheering is lovely. They still can't do the hard part for us.|
N~Popularity can follow strength, though it isn't proof of it.|
N~We'll let the battles answer that question.|
F~Being noticed does make every mistake feel a little louder.|
S~It's kind that people are interested in how we're doing.|
N~The audience has been accepted as evidence of the performance. Bold.|
N~A flattering inference with a few missing steps.|
N~Skill is something we can practice. Popularity is less predictable.|
N~Other people's attention does not change the weight of the next step.|
N~She means it as praise. We can receive it without making it a rule.|
N~I'd ask what makes her choose a Trainer to cheer for.
''')
add('sootopolis_fanclub_visit', 'SootopolisCity_House3_Text_TrainerFanClubWasWild',
    'A girl describes the passionate international fan crowd at Lilycove Trainer Fan Club.', '''
U~People cross the sea to argue about their favorite Trainer? That's committed arguing.|
N~A common interest can bring together people from a considerable distance.|
N~Sounds lively. I'd stay near a door if it got crowded.|
F~I might enjoy hearing about it more than standing in the middle.|
S~That many visitors probably keep the nearby cafes busy.|
S~A room where every spectator apparently brings a leading character.|
N~An international gathering of extremely certain opinions. Daunting.|
N~I'd be curious how they settle disagreements over different battle styles.|
N~Admiration can travel a very long way to find company.|
S~She enjoyed the energy. That is part of what makes a gathering work.|
S~I'd ask who she met there, as well as who they cheered for.
''')

add('mossdeep_space_origins', 'MossdeepCity_SpaceCenter_1F_Text_DidPokemonComeFromSpace',
    'A visitor wonders whether the claim that Pokemon originated in space is true.', '''
U~If Pokemon came from space, that is the longest trip to meet a friend I've heard of.|
N~A compelling question needs evidence beyond the fact that someone proposed it.|
N~Interesting theory. I'd ask what makes people think so.|
N~Looking up makes the things we don't know feel very large.|
S~Wherever they began, I am glad we get to know them here.|
N~A grand opening chapter in search of reliable witnesses.|
N~An extraterrestrial origin would explain some things. It would raise rather more.|
N~We'd need observations that distinguish it from other explanations.|
N~The sky is a tempting place to put an unanswered beginning.|
N~I like that she asks instead of presenting a rumor as certainty.|
N~I'd ask the researchers what evidence they find most interesting.
''')
add('mossdeep_space_wonder', 'MossdeepCity_SpaceCenter_1F_Text_RocketsBoggleMyMind',
    'An elder marvels that a huge metal rocket can reach space.', '''
U~A giant metal thing gets to leave the sky. My little legs have no such ambition.|
S~The scale is striking, but controlled thrust can overcome its weight.|
N~Takes a lot of careful work to make that look possible.|
S~I don't think understanding it completely would make it less wonderful.|
S~All that effort lifts something no person could carry.|
S~An improbable sight becomes ordinary through a vast amount of extraordinary work.|
S~An enormous metal object refusing to remain sensibly on the ground.|
U~Every system has to work together. That's what makes the whole thing amazing.|
S~Something made from the earth reaches beyond the clouds.|
S~His amazement feels fresh, however many times he has watched.|
U~I'd ask what he remembers about seeing his first launch.
''')
add('mossdeep_space_dream_threat', 'MossdeepCity_SpaceCenter_1F_Text_MagmaWantsToSpoilMyDream',
    'The rocket enthusiast resents Team Magma threatening the spaceflight dream.', '''
N~Team Magma has picked a very large dream to kick over.|
N~Stealing fuel threatens the work and aspirations of the people here.|
N~He's right to be angry. They have no claim to this place.|
D~Something that made him happy has become something to worry about.|
N~There are real people behind the supplies they're trying to steal.|
N~A thief sees fuel where an entire room sees a future.|
N~A remarkably efficient way to become unwelcome on an island.|
N~That fuel belongs in a controlled launch, not in their hands.|
N~A dream does not become disposable because someone else wants its materials.|
N~He isn't merely protecting an attraction. It means something to him.|
N~I'd like to hear him talk about a launch again when this is safe.
''')
add('mossdeep_aqua_alternative', 'MossdeepCity_SpaceCenter_1F_Text_AquaShouldBeatMagma',
    'A visitor realizes using Team Aqua against Magma could embolden another criminal team.', '''
N~Replacing one enormous problem with another enormous problem seems like poor tidying.|
N~She has recognized the flaw in relying on a competing threat.|
N~Neither team needs more power over this town.|
N~I am glad she stopped to think through what would follow.|
N~You don't fix a spoiled meal by handing the kitchen to another troublemaker.|
N~A proposed rescue acquires a suspiciously similar second act.|
N~Two disasters do not reliably cancel each other out.|
N~The useful goal is securing the center, not helping either group win.|
N~One shadow is not sunlight simply because it covers another.|
N~She wants help badly enough to consider it, then sees the cost.|
N~I'd ask what support the center has from people it can actually trust.
''')
add('mossdeep_launch_wait', 'MossdeepCity_SpaceCenter_1F_Text_RocketLaunchImminent',
    'The launch counter staff reports that a rocket launch is imminent.', '''
U~A launch soon! I would like to stand where the ground is least surprised by it.|
S~The preparations are nearing their final stage. A good time to observe carefully.|
N~Let's stay clear of the staff and follow their instructions.|
U~Knowing it is almost time makes this room feel different.|
S~I'd hate to be the person who picked this moment to wander off.|
U~A short announcement with a truly extravagant event attached.|
N~The sky is about to receive a very noisy visitor.|
U~Final checks must be intense. I'll leave the team room to work.|
N~A thousand careful tasks are approaching one bright moment.|
S~That is an announcement worth putting other plans aside for.|
U~I'd ask where visitors can watch without getting in the way.
''')
add('mossdeep_launch_success', 'MossdeepCity_SpaceCenter_1F_Text_SuccessfulLaunchNumber',
    'The launch counter staff confirms a safe launch and records its numbered success.', '''
S~Another safe launch! The number sounds small beside all the work inside it.|
S~A recorded success is the result of many systems working within their requirements.|
S~Safely done. That's the word that matters.|
S~I wonder how the room felt in the first quiet moment afterward.|
S~Someone ought to make that crew a proper celebration meal.|
S~An entire ascent compressed into one number and a very good piece of news.|
S~A safe departure into space. I find that reassuringly improbable.|
S~Every successful launch is still worth checking and learning from.|
S~A light has gone beyond sight, and a roomful of people can breathe again.|
S~That plain report must carry enormous relief for the people who built it.|
S~I'd ask how the team marks a successful launch afterward.
''')
add('sootopolis_refuge', 'SootopolisCity_PokemonCenter_1F_Text_EveryoneTakenRefuge',
    'During the weather crisis, a resident explains that townspeople are sheltering inside.', '''
N~People are staying inside for good reason. Let's not give them another worry.|
N~Sheltering reduces exposure while conditions remain dangerous.|
N~Stay indoors if you can. We shouldn't urge anyone out into this.|
D~A whole town listening to the weather from behind closed doors.|
N~We should check that people have what they need without sending them outside.|
N~The grand catastrophe is also a hundred interrupted ordinary days.|
N~Today, remaining indoors is less a preference than a strategy.|
N~A safe building and reliable information matter most right now.|
D~A familiar street can become somewhere frightening to step into.|
N~There is no shame in choosing shelter while the danger lasts.|
N~I'd ask whether anyone nearby still needs help getting somewhere safe.
''')
add('sootopolis_friends_crisis', 'SootopolisCity_PokemonCenter_1F_Text_ArentPokemonOurFriends',
    'During the crisis, a woman is distressed that Pokemon could cause such destruction.', '''
D~She knows Pokemon as friends. This must feel impossible to fit beside that.|
N~Pokemon friendship doesn't mean every creature is harmless in every situation.|
N~Being afraid right now doesn't erase the good she knows.|
D~I don't think she is asking for a clever explanation. She sounds hurt.|
N~Her own friends are still her friends, even with this happening outside.|
D~An enormous conflict has shaken a very personal certainty.|
D~Something trusted has become frightening. That is a hard thing to hold.|
N~We need to respond to the actual danger without blaming every Pokemon for it.|
D~A kind memory can remain true beside a terrible present.|
N~She is trying to understand the crisis through the relationships she knows.|
D~I'd stay with the question for a moment instead of dismissing it.
''')
add('sootopolis_friends_ordinary', 'SootopolisCity_PokemonCenter_1F_Text_AlwaysBeFriendsWithPokemon',
    'Outside the crisis, a woman affirms lasting friendship with Pokemon because they are good company.', '''
S~Being together is a perfectly good reason to keep being together.|
S~She values the relationship itself, beyond any practical advantage.|
S~Good company is worth staying loyal to.|
S~I like how simple she lets that feeling be.|
S~You don't need a grand reason to enjoy someone beside you.|
S~A lifelong declaration grounded in the radical pleasure of liking your friends.|
S~Enjoyable company. A rare quality, and a sensible basis for loyalty.|
S~A relationship can be valuable without solving a particular problem.|
S~Some promises begin with the quiet fact of being glad someone is here.|
S~She sounds comfortable in that affection. It suits her.|
S~I'd ask which ordinary thing she most enjoys doing with them.
''')
