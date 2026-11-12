"""Authored NPC replies across both regions, in the established eleven-voice order.

Read the actual scripts before binding a label. Each entry answers its specific
conversation/outcome; intermediate questions and unfinished choices stay unbound.
"""
ROWS = []

def add(key, labels, subject, lines):
    replies = [line.strip() for line in lines.strip().split('|')]
    assert len(replies) == 11, (key, len(replies))
    ROWS.append(dict(key=key, labels=labels.split(), subject=subject, replies=replies))

add('ship_scanner_search', 'AbandonedShip_CaptainsOffice_Text_NoSuccessFindingScanner',
    "Stern's aide has been searching the wreck for a scanner without success.", '''
Looking for a scanner in a wreck. I lose things in a bag with one pocket, so I respect the ambition.|
He has kept searching despite the conditions. A systematic sweep might help more than another hopeful lap.|
He could use another pair of eyes. We should check rooms carefully, including the way back out.|
He sounds tired of finding everything except the thing he came for. I know that feeling with lost verses.|
I hope he brought something to eat. Searching a whole ship on an empty stomach makes every room longer.|
The assignment was probably shorter when Stern described it. They usually leave out the flooded corridors.|
A missing instrument, a ruined ship, a patient researcher. I would read his notebook before his report.|
A scanner could slip behind a lot of broken fittings here. I would start with places the floor tilts toward.|
This ship has held on to plenty of things. We can search without disturbing everything that stayed behind.|
His expedition could use a dry place to put the things he does find. Even discovery needs somewhere to sit.|
We should compare the rooms he searched with the ones he missed. A rough sketch would give us somewhere to begin.
''')

add('ship_scanner_delivery', 'AbandonedShip_CaptainsOffice_Text_OhCanYouDeliverScanner',
    "The aide recognizes the scanner we carry and asks us to take it to Stern while he investigates.", '''
We found the scanner, and he found someone to deliver it. Everybody's expedition is going beautifully.|
Stern should receive the instrument while his aide records the site. That is a sensible division of the work.|
We have the scanner and he has more ship to check. Taking it to Stern seems fair.|
He wants to finish looking around. I understand wanting one more minute somewhere that keeps asking questions.|
We can carry it back. He should still come ashore before the ship makes that decision for him.|
Our reward for finding important equipment is becoming its courier. An unexpectedly practical plot twist.|
He looked at the scanner like a missing line had finally come back to him. Let us get it to Stern safely.|
I want to inspect it, but Stern gets the intact version first. I am practicing this particular kind of restraint.|
An old ship has finally given up what he was seeking. We should see the little journey through.|
He is trusting us with the delivery. I would wrap the scanner before our bag introduces it to the rocks.|
We know where it belongs now. A clear destination is a lovely improvement over another locked room.
''')

add('ship_cactus_name', 'AbandonedShip_CaptainsOffice_Text_ThisIsSSCactus',
    'The aide identifies the old wreck as the S.S. Cactus.', '''
The S.S. Cactus. I feel someone in the naming department had a very optimistic understanding of watering.|
The name gives us something to look for in older shipping records. A vessel deserves more history than its wreck.|
S.S. Cactus. Strange name for a ship, but somebody used to be proud to see it come into port.|
It had a name long before it was a place to search. That makes the empty rooms feel a little different.|
I wonder what the crew ate on long voyages. There were ordinary dinners here before all this.|
S.S. Cactus is an excellent name for a ship in a story. I wish this one had received a gentler ending.|
There is something stubborn about that name. Even wrecked, the ship still has people asking after it.|
An older vessel means older construction methods. Some of these joints have lasted better than the rest of the ship.|
A name helps us remember that people belonged here. We should move through it kindly.|
The name sounds almost cheerful. I hope somebody still remembers what it looked like with fresh paint.|
I would like to find a picture of it afloat. The wreck tells us how it ended, but there was a whole voyage before that.
''')

add('celadon_gym_spectator', 'CeladonCity_Text_GymIsGreatFullOfWomen',
    'An old man outside the gym leers at the women inside.', '''
He has mistaken a Gym for an invitation. I hope the first thing they teach him is how to leave.|
The women inside are training. His commentary contributes remarkably little to that activity.|
They came here to train. He can find somewhere else to stand.|
I would rather hear about their Pokemon. They probably have more interesting things to say than he does.|
They deserve to do their work without an audience like that. Let us give them some room.|
He has volunteered for the role of unpleasant man outside a building. Nobody needed that role filled.|
I hope the flowers by that window have thorns and very good aim.|
That window could use a blind. I suddenly feel very motivated to install one.|
Being welcome in a place is something you should care about. He seems to have missed that part.|
He has spent all this time looking and still failed to notice that these are people with things to do.|
I would ask the trainers what they think of their Gym. Their view of the place matters rather more.
''')

add('celadon_corner_reputation', 'CeladonCity_Text_GameCornerIsBadForCitysImage',
    "A resident says the Game Corner damages Celadon's beautiful image.", '''
They polish the city, then put a place here where people lose their lunch money. That is a complicated shine.|
I would ask how the Game Corner affects residents as well as how it looks beside the gardens.|
If it is hurting people, that matters more than whether it spoils the view.|
A city can look lovely while somebody inside it is having a terrible evening. Both things deserve noticing.|
Pretty streets are good. People being able to afford their next meal is good too.|
The flowers make a convincing first impression. I would still like to hear what the neighbors say after closing time.|
She wants her city to be beautiful. I hope that includes being gentle with the people who live in it.|
You cannot fix what a place does by repainting its sign. I have tried smaller versions of that mistake.|
A beautiful place should be somewhere people feel safe coming home to.|
Celadon has put thought into its appearance. I would like the same attention paid to what happens behind the doors.|
The Game Corner belongs in the picture of this city too. Cropping it out would not tell us much.
''')

add('celadon_slots_loss', 'CeladonCity_Text_BlewItAllAtSlots',
    'A man regrets losing all his coins at the slots instead of exchanging them for prizes.', '''
He looks miserable. I think the best thing the machine could give him now is a reason to stop feeding it.|
Each loss does not make the next turn kinder. I hope he can step away before trying to recover everything.|
He has lost enough. Walking away now is allowed, even if it feels like leaving something unfinished.|
He keeps hearing the moment when he could have stopped. That is a hard bit of noise to sit with.|
I would rather help him find a meal than another coin. He needs something that will actually stay with him.|
That is an awful ending to an evening. He does not have to buy another chance at a better one.|
Regret can make a very convincing argument for doing the same thing again. I hope he gets some distance first.|
The machine has no reason to care how much he has lost. He should get advice from somebody who does.|
We can be kind to him without helping him keep playing.|
He wanted a prize and ended up paying for a very unpleasant memory. Let us avoid making him feel smaller.|
I wish I had met him before the last coin. Since we did not, we can at least listen now.
''')

add('celadon_poliwrath_friend', 'CeladonCity_Text_MyTrustedPalPoliwrath',
    'A trainer proudly introduces his trusted Poliwrath and explains using a Water Stone.', '''
He calls Poliwrath his trusted pal before explaining the Water Stone. I think he has the important bits in order.|
He remembers how it evolved, but he introduces it as a friend. The stone was only one part of their history.|
Poliwrath looks like someone he can count on. That is worth being proud of.|
I like an introduction that tells us they trust each other. The evolution detail can be the second verse.|
He sounds fond of the Poliwhirl it was as well as the Poliwrath it became. I like that.|
One Water Stone, a dramatic transformation, and still the same trusted pal. A very good character arc.|
It changed shape and kept its place beside him. There is a comforting story in that.|
A Water Stone did the evolving. Keeping a friend took a little more work than picking up a stone.|
It is lovely to hear someone talk about an evolved Pokemon without treating its earlier self as a mistake.|
He is proud of his friend. Poliwrath is wearing the introduction rather well.|
That sounds like a picture they have taken more than once, with a different Pokemon shape beside the same smile.
''')

add('celadon_poliwrath_greeting', 'CeladonCity_Text_Poliwrath',
    'The trainer-owned Poliwrath responds when greeted.', '''
Ribi ribit to you too. I have decided to assume that was friendly and not a critique of my posture.|
That is a confident greeting. I shall answer politely and leave the translation to someone qualified.|
It seems comfortable beside its trainer. We can say hello without making it an interview.|
There is a nice little rhythm to that call. I will resist answering at full volume indoors.|
Hello, Poliwrath. I hope we have not interrupted an important part of standing peacefully with your friend.|
A short introduction with excellent projection. It has the stage presence for a longer speech if it wants one.|
It has said its piece. I respect a conversation that knows when it has finished.|
That sounded energetic. I am keeping my measuring tape well away from those arms.|
We have been acknowledged. A small greeting can be enough.|
Poliwrath carries itself very well. That spiral is quite a statement without any help from us.|
I like that it answered for itself after its trainer introduced it. Everyone gets a turn.
''')

add('celadon_direct_threat', 'CeladonCity_Text_GetLostOrIllPunchYou',
    'A Rocket grunt threatens to punch the player for looking at him.', '''
That escalated quickly. I would like to cancel the staring contest before he invents an entry fee.|
We looked in his direction and he threatened violence. I see no reason to continue collecting evidence of his character.|
Stay beside me. We can move away without giving him the confrontation he wants.|
He has made a lot of noise over being noticed. Let us find a quieter stretch of pavement.|
You did not deserve that. We can keep some distance and keep each other company.|
He has prepared one line and it is a threat. I would decline the rest of the performance.|
We do not have to be brave for his benefit. Come on, let us get out of reach.|
I am annoyed, but I am also staying outside punching distance. Both seem sensible.|
Threatening someone does not make the street his. We can still choose a safer part of it.|
He has confused having fists with having something worth saying. We should leave him to untangle that.|
I saw what happened. You were looking at a person on a street; he chose to make it ugly.
''')

add('celadon_rocket_obstruction', 'CeladonCity_Text_KeepOutOfTeamRocketsWay',
    'A grunt orders the player to keep out of Team Rocket\'s way.', '''
Apparently the pavement has an executive board now. I was happier when it was just pavement.|
Their instructions are very clear about what they want and entirely silent about anyone else's needs.|
They are trying to make everyone step aside for them. We can keep our distance without agreeing with them.|
He talks like the whole street belongs to his uniform. I hope the neighbors are tired of hearing it too.|
There are people here trying to get through an ordinary day. Rocket could start by keeping out of their way.|
He is blocking a street while complaining about obstructions. That is almost a complete little comedy.|
They make every doorway feel narrower. I would like this city better without that.|
If they want clear routes, perhaps they could stop standing in all of them.|
We should notice who has to make themselves small whenever Rocket passes. They deserve their street back.|
That uniform seems to come with an extraordinary opinion of its own importance.|
I am going to remember the people they keep pushing aside. They belong in the story of this street too.
''')

add('celadon_hot_tea', 'CeladonCity_Text_ScaldedTongueOnTea',
    'A boy burned his tongue on hot tea from the mansion and says it needs to cool.', '''
The tea came with a lesson. Unfortunately the lesson went directly onto his tongue.|
He has discovered the difference between being offered tea and being offered drinkable-temperature tea.|
He should let it cool. The cup will still be there after his tongue stops regretting it.|
There is a particular silence after burning your tongue. Your mouth has a lot to say and no wish to say it.|
Small sips, once it cools. Good tea should not require a recovery period.|
A gift, a moment of enthusiasm, a tragic reversal. All accomplished before the first proper sip.|
I understand accepting warmth a little too eagerly. His tongue has been more literal about it than mine.|
We could give the cup a handle marked WAIT. I suspect I would occasionally ignore it too.|
Something kind can still need a little patience before it is ready for you. In this case, a cup of tea.|
He has the tea and the wisdom now. I hope he gets to enjoy them together after it cools.|
I was going to ask how the tea tasted. I think that question will have to wait with the tea.
''')

add('celadon_stolen_scope', 'CeladonCity_Text_SomeoneStoleSilphScope',
    'A scientist lost sight of the person who stole the Silph Scope.', '''
He lost a whole piece of lab equipment to someone running past. I would like our next exciting discovery to be its return.|
He saw which way the thief ran. We should keep that detail separate from guesses about where they went next.|
He sounds shaken. If we find anything, we should bring him something firmer than another rumor.|
He keeps returning to the moment he lost sight of the thief. I hope we can give that thought somewhere to go.|
The missing equipment matters, and so does the person left standing here worrying about it.|
The thief made a dramatic exit. I would prefer an equally clear entrance with the stolen equipment returned.|
His work has been turned into a search. That is a cruel way to interrupt someone's ordinary day.|
I want that instrument recovered intact. Whoever took it has already demonstrated poor laboratory manners.|
We should remember what he actually saw. Frightened people should not have to compete with exciting guesses.|
He has lost the Scope and his sense of where to begin. We can at least take his account seriously.|
He had a direction to point in until the thief disappeared. I would start there, then ask who else saw them.
''')

add('saffron_claimed_city', 'SaffronCity_Text_BossTakeTownForTeamRocket SaffronCity_Text_SaffronBelongsToTeamRocket',
    'Rocket grunts claim Saffron as territory for their organization.', '''
They talk about owning a whole city. I would struggle to keep track of its keys.|
A city is full of people with their own work and lives. Calling it property leaves out almost everything important.|
People live here. Rocket does not get to make them into part of its haul.|
I wonder how many people have heard that line on the way home. Once would be enough for me.|
They are talking about somebody's home as if it is a thing to pocket. I hate that.|
They have announced ownership of the setting. The people living in it might have revisions.|
There are ordinary names on these doors. I would like those names to matter more than Rocket's.|
You cannot put a city under your name and call all its problems somebody else's responsibility.|
A place belongs to the lives being lived in it. A shouted claim cannot replace them.|
Their name is on their uniforms already. I see no reason it needs to be on everyone's home as well.|
I would rather make a record of Saffron's residents than another picture of Rocket claiming the street.
''')

add('saffron_criminal_thrill', 'SaffronCity_Text_CriminalLifeMakesMeFeelAlive',
    'A Rocket grunt boasts that criminal life makes him feel alive.', '''
He could have tried a brisk walk. Much less paperwork for everyone else.|
He is describing excitement without mentioning who has to suffer for it. That is a rather important omission.|
He can find a hobby that does not leave other people frightened.|
I understand needing to feel something. I do not understand deciding that everyone else must pay for it.|
He could learn to cook for people. There is plenty of panic available without robbing anybody.|
He has confused making a dramatic entrance with giving anyone a reason to be glad he arrived.|
Feeling alive is a poor excuse for making a place harder to live in.|
I have felt very alive repairing something while it was smoking. I still recommend safer hobbies.|
He is treating other people's fear like a cure for his boredom.|
If being memorable is the aim, he has chosen a very unfortunate way to achieve it.|
He gets to call this exciting. The people avoiding his uniform probably have other words for it.
''')

add('saffron_rude_pedestrian', 'SaffronCity_Text_WatchWhereYoureWalking',
    'A grunt complains that the player walked into him.', '''
All right, we will leave him more room. I had not realized his temper needed its own lane.|
We can give him space. I would prefer the correction without the shouting, but the space is easy enough.|
Let us step around him. A crowded pavement does not need help becoming an argument.|
He is loud enough that I should have noticed him before we got that close.|
Sorry about the bump. We can keep moving before everybody on the street gets a turn to comment.|
A brief collision and a very committed delivery. We can exit this scene gracefully.|
I would like enough pavement for both of us to pass without acquiring a new enemy.|
I can avoid him. Avoiding the volume might take a wider route.|
We can acknowledge a bump without accepting a whole quarrel along with it.|
He has made his preferred walking distance clear. I am happy to add a little extra.|
I will look ahead. We have both had enough surprises from people in that uniform.
''')

add('saffron_global_exploitation', 'SaffronCity_Text_WeCanExploitMonsAroundWorld',
    'A grunt boasts that controlling Silph will let Rocket exploit Pokemon worldwide.', '''
He has said the horrible part out loud as if it is the selling point. That makes this very easy to dislike.|
He understands the reach of the technology and has chosen the worst possible use for it.|
He means hurting Pokemon on a bigger scale. We should take that threat seriously.|
He says it so casually. I keep thinking about all the Pokemon who would never know why this happened to them.|
Pokemon have people and places they trust. He is talking about taking that away for money.|
There is no clever interpretation that makes his plan less ugly. He has been quite specific.|
I wish he sounded less pleased with himself. This is a frightening thing to hear someone want.|
Silph's machines could help Pokemon. I am furious that he sees better tools and thinks only of bigger cages.|
He is imagining a world where being powerful is enough to make taking things acceptable.|
He has reduced living creatures to something he expects to profit from. They deserve better than that.|
I am remembering those words exactly. Nobody should get to soften this plan into something harmless afterward.
''')

add('saffron_suspect_guard', 'SaffronCity_Text_ImASecurityGuard',
    'The Rocket door guard claims to exclude suspicious children.', '''
His security policy appears to be deciding we look easier to stop than his coworkers.|
He has supplied a job title, but very little reason to trust his judgment.|
He is using the doorway to decide who gets heard. Let us remember who he is keeping out.|
He sounds very certain about strangers and rather quiet about the people already inside.|
People should feel safer because a guard is there. I do not think he is having that effect.|
He has a title and a doorway. He seems to think the combination removes the need for an explanation.|
He is very interested in whether we belong here. I have a few questions about him, too.|
I would like to see a security plan that includes checking the people in Rocket uniforms.|
Protecting a place should include caring about the people who need to enter it.|
He has put a lot of confidence into that introduction. The uniform is undermining the rest of it.|
I would ask somebody from Silph whether they recognize their own supposed guard.
''')

add('saffron_sleeping_guard', 'SaffronCity_Text_HesTakingASnooze',
    'The previously obstructive door guard is asleep.', '''
He is inspecting the backs of his eyelids. Apparently the building passed.|
His attention has moved elsewhere. I suggest we take the opening without waking him to discuss it.|
He is asleep. We can get past without turning that into another confrontation.|
I have no wish to contribute a loud note to this particular silence.|
Let him rest. He has finally found a way to stand there without making everyone else's day worse.|
An imposing guard defeated by an ordinary nap. I appreciate a modest plot development.|
He has become significantly easier to be near. We can leave the snoring undisturbed.|
I am usually in favor of a backup system. Today I am pleased this guard appears to have none.|
A quiet doorway is a welcome change. Let us make gentle use of it.|
He is wearing the same uniform with a much less demanding attitude. I prefer this version.|
I will remember his face. For now, I am happy to remember it with his eyes closed.
''')

add('saffron_victory_praise', 'SaffronCity_Text_YouBeatTeamRocket',
    'A resident praises the trainer for defeating Team Rocket alone.', '''
All alone? Your Pokemon might want a small amendment. Probably delivered by everybody at once.|
You did difficult work, and your team stood beside you through it. I would put all of that in the account.|
You earned that thanks. You also deserve a chance to rest instead of immediately proving yourself again.|
It sounds different when someone says it out here in the street. We can let the good part sink in.|
You helped people feel safe again. I hope you remember to let somebody look after you for a little while.|
That is a wonderful review. I would add the Pokemon to the credits before printing it.|
You did something that matters to people you may never meet. It is all right to feel proud of that.|
You dealt with Rocket, and he has noticed. I would like that followed by a comfortable chair for you.|
Accept the thanks. People need a way to say what their safety means to them.|
You can stand a little taller for that. I will handle being embarrassing about how proud I am later.|
He is putting a face to the person who helped his city. I am glad he got to tell you.
''')

add('saffron_safe_streets', 'SaffronCity_Text_SafeToGoOutAgain',
    'A youngster is relieved that Rocket is gone and it is safe to go outside.', '''
Being able to go outside should be an ordinary thing to celebrate. I am glad it gets to be ordinary again.|
That is what the fighting changed for someone here: an open door without fear on the other side.|
Good. He should get to think about where he wants to go, instead of whether he is allowed to feel safe.|
I would like to hear the city fill up with little conversations like that one.|
I hope he has a lovely, completely uneventful walk. He has waited long enough for one.|
A happy ending expressed as a trip outside. It does not need to be grander to matter.|
He can go out again. A small sentence with a great deal of relief inside it.|
That is a result I can appreciate without taking anything apart to check it.|
Safety lets people have ordinary wishes again. I hope he gets a day full of them.|
I am very much in favor of his next outing being memorable for something pleasantly boring.|
I would rather photograph that relief than any of Rocket's dramatic poses.
''')

add('saffron_returning_residents', 'SaffronCity_Text_PeopleComingBackToSaffron',
    'A resident hopes people who fled Rocket will return to Saffron.', '''
I hope they get to come home to something as boring and wonderful as having to unpack.|
It may take time before everyone trusts the streets again. I hope they are welcomed at whatever pace they need.|
Getting Rocket out was one thing. Helping people feel they can return is the next part.|
I wonder which familiar sound people will notice first when they come home.|
I hope someone is keeping a place at the table for the people who left.|
The city is waiting for its people to return. I would like the next chapter to take its time with that.|
Coming home can be frightening after you had to leave. I hope nobody rushes them through the feeling.|
There will be doors to fix and belongings to bring back. I can think of useful things to do here now.|
A place is still changing after the danger ends. The returning people should get a say in how.|
I hope they find familiar things waiting for them. An ordinary room can mean a great deal after being away.|
I would like to see the same street in a few weeks, when the people who know it best are back in it.
''')

add('saffron_late_reporter', 'SaffronCity_Text_FlewHereOnPidgeot',
    'A visitor flew in after reading about Silph and regrets missing the media action.', '''
He missed the frightening part and still has a Pidgeot ride to talk about. That seems like a very decent afternoon.|
He could still ask residents what happened. The end of the commotion is not the end of the story.|
People here had to live through it. I would prefer a little more relief and a little less disappointment from him.|
He arrived after the loudest part. There are still people worth listening to now that it is quiet.|
His Pidgeot brought him here safely. I hope the bird gets a better review than the timing of the trip.|
He wanted the dramatic scene and arrived for the consequences. Those are usually worth staying for.|
Missing someone else's worst afternoon does not seem like a terrible loss to me.|
There is probably plenty to learn about how Silph gets working again. That might involve less posing for cameras.|
The people who are recovering from this should not have to apologize for being less exciting now.|
He still has the chance to be useful. Arriving late does not prevent arriving kindly.|
A camera can record people rebuilding their day, too. You have to be interested in them after the headline.
''')

add('saffron_pidgeot_greeting', 'SaffronCity_Text_Pidgeot',
    'The visitor\'s Pidgeot responds to being greeted.', '''
Pidgeot has made its statement. I think it is the only person here entitled to complain about the flight.|
That bird did the actual traveling work. I hope its trainer has planned a proper rest for it.|
Pidgeot looks ready for a break. We can keep the greeting short.|
That is a fine voice to arrive on. I would like to hear it somewhere without so much street noise.|
Hello, Pidgeot. I hope there is water and a good meal in your immediate plans.|
An impressive entrance followed by a very brief interview. Pidgeot understands pacing.|
It has crossed a lot of sky to stand here. That seems like enough work for one conversation.|
I am keeping my hands away from those flight feathers. They have had a busy day.|
We can greet it without asking it for anything. It has already carried someone a long way.|
Those feathers have survived the trip beautifully. I hope it gets somewhere comfortable to settle them.|
I would ask permission before taking a picture. After that flight, it may prefer a quiet patch of shade.
''')

add('saffron_boss_escape', 'SaffronCity_Text_SawRocketBossEscaping',
    'A witness says the Rocket boss escaped from Silph.', '''
I wish he had been running toward a new and honest profession. I am not putting much money on that.|
That is a witness account worth keeping. We should distinguish seeing him escape from knowing where he went.|
He got away. That does not undo the people who are safer because his operation here ended.|
It is hard to know someone responsible can simply leave the noise behind him.|
The city still deserves its relief. His escape is something to take seriously without taking that away from everyone.|
The villain has exited. I would like somebody to stop giving him doors.|
He left the people here to live with what happened. I hope they get to decide what comes next.|
I would like to know which exit he used. A useful security review could begin with that actual question.|
An escape means there is unfinished harm to answer for. It also means the people here have room to breathe today.|
He may have made his getaway, but he has left quite a few people who can describe him.|
I would ask the witness where he was standing and which way the boss went. The details matter now.
''')

add('saffron_dismissive_grunt', 'SaffronCity_Text_WhatDoYouWantGetLost',
    'A grunt dismisses the player and orders them to leave.', '''
He asked what we wanted and dismissed us before we could answer. A remarkably efficient waste of a question.|
I do not think he was collecting answers. We can spend our time with someone who is.|
We heard him. We can keep moving and remember who is making this street unpleasant.|
That was more an instruction than a conversation. I would rather find someone interested in the second kind.|
We can leave him alone. There are plenty of people here who might actually need someone to talk to.|
He has ended the scene before the other character's first line. A very limited approach to dialogue.|
I have been dismissed by better doors than this one. Come on.|
He seems determined to be an obstacle. I am not going to spend the afternoon explaining the problem to him.|
We can choose to leave without deciding he had the right to chase us away.|
He has made a rather poor introduction. I am comfortable allowing it to stay that brief.|
That tells us how he wants to be remembered. I would rather spend the next conversation learning about someone else.
''')

add('museum_fine_arts_and_battles', 'LilycoveCity_LilycoveMuseum_1F_Text_MustntForgetLoveForFineArts',
    'A schoolkid says enjoying Pokemon battles should leave room for the fine arts.', '''
I can enjoy battles and paintings. My bag already contains both healing items and a very flattened museum ticket.|
He is right that training need not use up all our curiosity. I rather like being reminded of that here.|
We can have more than one thing we care about. It helps to spend a day remembering that.|
I am glad he said that. A battle tells us something about a Pokemon; a painting can notice something else.|
There is room in a day for battling, good food, and looking at something someone made with care.|
I agree with his artistic principles. I am slightly alarmed by how confidently he has issued them.|
We do not have to turn everything we love into a competition. This is a pleasant room to remember that in.|
I build things to do jobs. It is good to look at things someone made simply because they wanted them to exist.|
Spending time with something beautiful is a way of paying attention, too.|
He has a strong opinion about how we should spend our afternoon. For once, I think I will take the suggestion.|
Looking at how other people see Pokemon might help us notice our own team differently.
''')

add('museum_artist_inspiration', 'LilycoveCity_LilycoveMuseum_1F_Text_ThisMuseumIsInspiration',
    'An artist praises the museum\'s paintings and its supportive curator.', '''
I like a museum that sends artists home wanting to make things. I may leave with a much less impressive sketch.|
The curator has helped make a place where artists want to learn from one another. That is valuable work.|
It sounds like the people here make it easier to keep trying. I can understand coming back for that.|
Some rooms make you hear the next thing you want to write. I think this room does that for him in color.|
He talks about the curator as warmly as the paintings. Someone has made him feel welcome here.|
He has found a room full of work that makes him want to begin his own. I know how precious that can be.|
I like hearing an artist sound encouraged. We should get to hear that more often.|
Seeing how somebody solved a problem can make your hands itch to try. I suspect he knows that feeling.|
Good work can give other people permission to begin. This museum seems to have done that for him.|
He admires the work and the person who made space for it. I think that is a very fair compliment.|
I would love to ask which painting first made him want to pick up his own tools again.
''')

add('museum_child_sees_mother', 'LilycoveCity_LilycoveMuseum_1F_Text_ThisLadyIsPretty',
    'A child likes a portrait because its subject reminds him of his mother.', '''
He has found his favorite person in a painting. That is a very strong recommendation for the painting.|
He connected the portrait with someone he loves. That is a rather lovely thing for an image to do.|
It reminded him of his mother. He does not need a longer reason to like it.|
Sometimes a face in a painting feels familiar before you can explain why. He found his explanation immediately.|
I hope he tells his mother that. It sounds like the sort of thing she would keep for a long time.|
The critics can finish their essays. He has delivered his entire review in two sentences, and it works.|
He looked at a stranger's face and found something that felt like home.|
I think we can leave his analysis exactly as it is. He has explained the important part.|
He is seeing the painting through the person who makes him feel loved. I like that way of looking.|
The artist has acquired a very enthusiastic little admirer. His mother has an even better compliment waiting for her.|
That is why I like pictures of ordinary people. Somebody can recognize a little of their own life in them.
''')

add('museum_mother_sees_son', 'LilycoveCity_LilycoveMuseum_1F_Text_ThisPokemonIsAdorable',
    'A mother says the Pokemon in a painting is adorable like her little boy.', '''
The family resemblance appears to be concentrated entirely in being adorable. I accept the finding.|
She sees something of her son in that Pokemon. People bring their own little histories to a painting.|
She sounds fond of her boy. I am happy to let the painting take a share of the compliment.|
She has found somebody she loves in the picture too. I hope they compare notes on the way home.|
I hope her boy gets to hear himself described that kindly when they are away from the painting, too.|
The painting has become a family portrait through sheer parental enthusiasm. An excellent transformation.|
That is a sweet way to look at a picture. I would like to be described with that much uncomplicated fondness.|
I am choosing not to ask which features they share. I suspect the answer is simply that she loves him.|
Love makes people notice little familiar things. The painting has given hers somewhere to land.|
She has made her opinion of her son wonderfully clear. I think the Pokemon can be pleased with the comparison.|
I would rather remember the way she said that than try to work out an actual physical resemblance.
''')

add('museum_new_paintings_visitor', 'LilycoveCity_LilycoveMuseum_1F_Text_HeardMuseumGotNewPaintings',
    'A visitor hurried over after hearing about new paintings and asks whether they are upstairs.', '''
She heard there were new paintings and came running. I appreciate an emergency that can be solved by taking the stairs.|
The new collection has already drawn someone back. I hope the curator gets to hear how eager she was to see it.|
It is nice to see someone this excited about something peaceful. We can point her toward the curator.|
She has been looking forward to seeing work she has not met yet. I like that kind of anticipation.|
I hope the paintings are worth the hurry. Either way, she should take a breath before doing the stairs.|
An audience arriving because it genuinely wants to be here. Someone should tell the artists how that feels.|
I understand hurrying somewhere because there is something new to look at. I tend to pretend I was walking casually.|
I would ask where the new exhibits are too. Otherwise I might inspect an old frame for twenty minutes and miss the point.|
She came back because the place still has things to show her. That is a good relationship to have with a museum.|
I hope she gets a little time to enjoy them after making such a determined entrance.|
I like returning to a familiar place when it has something new to tell me. She clearly does too.
''')

add('museum_cheerful_curator', 'LilycoveCity_LilycoveMuseum_1F_Text_CuratorHasBeenCheerful',
    'A visitor notices that the curator has seemed unusually cheerful lately.', '''
I hope it is something wonderful and ordinary, like finding exactly the right place for a painting.|
She noticed a change in him. It is nice to hear somebody observing a neighbor's happiness for once.|
Good. Looking after this place seems to matter to him. I hope it is giving him something back.|
Maybe he has something to look forward to when he opens the doors now. That can change how a whole day sounds.|
I hope whatever cheered him up lasts a while. People who welcome everyone else deserve good days too.|
The curator has become the museum's most discussed new exhibit. I hope he is enjoying the attention.|
People have noticed him being happy. I would like him to keep getting reasons to be.|
I hope a long-running problem finally got fixed. That sort of happiness can look suspiciously large from outside.|
It is kind that she noticed. We cannot always solve someone's difficulties, but we can notice when they ease.|
Whatever it is, it seems to suit him. Happiness is doing excellent work on his presentation.|
Somebody has seen him often enough to recognize a good stretch of days. I like that this place has regulars.
''')

add('museum_aspiring_exhibitor', 'LilycoveCity_LilycoveMuseum_1F_Text_AimToSeeGreatPaintings',
    'An aspiring artist studies the collection and dreams of exhibiting here someday.', '''
I hope we come back one day and he is standing beside a painting with his own name under it.|
He has a place he hopes to reach and examples he wants to learn from. That is a good beginning.|
I hope he keeps making things after he goes home. The wishing part deserves a chance to become work.|
It is brave to say where you hope your work will end up. I usually mumble that part.|
I would like him to have somebody who asks to see what he has made, even before it belongs in a museum.|
He has named his dream out loud. I know that can feel more dangerous than presenting the finished work.|
I hope he keeps some early attempts. It is easy to forget how far you have come when you only keep the good pages.|
He should study how they were made as well as how they look. There is a lot of useful work hiding behind a finished surface.|
He is looking at other people's achievements and finding room for his own future in them.|
I hope he knows his work can matter to somebody before a museum agrees to hang it.|
I would like to see what he is making now. The beginning of that story deserves a record too.
''')

add('museum_welcome_to_browse', 'LilycoveCity_LilycoveMuseum_1F_Text_NotDisturbYouTakeYourTime',
    'After we say we have not viewed the collection, the curator politely gives us time.', '''
Permission to wander slowly. I believe I have been training for this museum visit my entire life.|
He wants us to actually look before answering questions about the collection. I appreciate that order of operations.|
He is giving us room to enjoy the place. We can take him at his word.|
I like being allowed to spend time with a painting without having to explain what I think of it yet.|
That was kind. We can look around at whatever pace feels good.|
He has given the audience time to settle in. A surprisingly rare and considerate artistic decision.|
It is nice when an invitation to look does not come with a deadline.|
I will try to interpret taking our time as looking carefully, rather than inspecting how every frame is attached.|
We are allowed to be here before we know what to say about it. That feels welcoming.|
He is letting us discover what we like without choosing it for us. I think he is good at this.|
I would like to make another slow pass through the room. Some details only arrive after the first look.
''')

add('museum_uninterested_guest', 'LilycoveCity_LilycoveMuseum_1F_Text_HonoredYoudVisitInSpiteOfThat',
    'The curator remains welcoming after we say paintings are not our interest.', '''
We admitted we were not especially interested, and he was still pleased we came. That makes me want to look a little harder.|
He has left room for curiosity to develop without demanding that we already possess it.|
He took an honest answer kindly. I think we can return the favor by being considerate guests.|
He did not turn liking art into an entrance requirement. I am glad about that.|
There is room here for people who are still finding out what they enjoy. He has made that very clear.|
A host who can hear that and still make someone welcome has earned rather more of my interest.|
We did not have to pretend. I like this place better for that.|
He is happy we showed up before we understood what we might learn here. That is how quite a few of my interests started.|
An invitation can remain kind after someone says no. He seems to understand that.|
He has handled a fairly blunt answer with considerable grace. We should try to match it.|
Sometimes you come somewhere for company and discover an interest later. He is leaving that possibility open.
''')

add('museum_greeter', 'LilycoveCity_LilycoveMuseum_1F_Text_WelcomeToLilycoveMuseum',
    'The greeter welcomes visitors to the museum\'s Pokemon artwork collection.', '''
Pokemon paintings, a quiet room, and permission to linger. This is an unusually promising set of instructions.|
I would like to see which details the artists noticed first. We spend so much time looking for battle information.|
We have time for a look. The paintings are unlikely to demand a rematch.|
I like the hush in here. Everyone is having a conversation with something that does not need to interrupt.|
Somebody has made a comfortable place to look at things people cared about. I am glad we came in.|
I shall attempt to enjoy the art without mentally rehearsing an impressive opinion for the curator.|
I want to look around slowly. There is no need to have a favorite before we have seen anything.|
I will look at the paintings before I look at the fittings. You may remind me of that promise.|
It is lovely to enter somewhere that wants us to notice Pokemon without asking what we can get from them.|
I would like to see how the artists use color. It is such a generous room to borrow ideas from.|
I am interested in what caught each artist's eye. There are so many ways to look at the same Pokemon.
''')

add('museum_regional_pride', 'LilycoveCity_LilycoveMuseum_1F_Text_MuseumTouristDestination',
    'A resident praises the museum\'s regional appeal and reports a trainer supplied the upstairs paintings.', '''
One trainer filled an exhibit, and now people travel to see it. I am going to be more careful about throwing away my doodles.|
The paintings have given people another reason to visit Hoenn. I like seeing a trainer's work reach beyond the battlefield.|
Someone put a lot of effort into that collection. It is good to hear that people have noticed.|
I hope the visiting people spend a little time with each painting. It sounds as if the collection has earned it.|
The artists, the trainer, the people who keep this place open. I hope the good news reaches all of them.|
A lone trainer becomes an unlikely patron of the arts. I would absolutely read that story.|
It is nice that a trainer is being remembered here for bringing something beautiful into a room.|
Collecting paintings sounds simple until you try getting every last part of a collection into place. Someone stuck with it.|
A gift to one room has become something the whole region can enjoy. That is a lovely kind of consequence.|
People are coming to Lilycove for something they want to spend time looking at. The collection must be doing something right.|
I would like to meet the people who traveled here for the paintings. Each one will have arrived with a different expectation.
''')

add('fortree_sky_witness', 'FortreeCity_Text_SawGiganticPokemonInSky',
    'A man reports a huge flying Pokemon heading toward Route 131, then notices our singed smell.', '''
An enormous Pokemon headed toward Route 131, and he has still found time to review our smell. A thorough witness.|
Route 131 gives his sighting a useful direction. Our smoky clothes are less relevant, but evidently quite persuasive.|
We should remember where it was heading. We can deal with smelling like a campfire afterward.|
He described something enormous in the sky, then brought us straight back down to our laundry.|
I hope he finds somebody who takes the sighting seriously. Meanwhile, we could probably use a wash and a meal.|
A gigantic creature crossing the sky, followed by a critique of the protagonist's scent. I admire the abrupt change of scale.|
I would like to hear more about the thing he saw. I would like to hear less about our current resemblance to burnt toast.|
I want details about how it moved. Unfortunately, he has become distracted by evidence that we have been near fire.|
We can listen without deciding what he saw yet. We can also admit that we could do with clean clothes.|
He may have witnessed something remarkable. We appear to have brought our own, considerably less glamorous evidence of adventure.|
I would ask which way he was facing and how long he saw it. Then I would find somewhere to wash this shirt.
''')

add('fortree_gym_challenger_ready', 'FortreeCity_Text_ThisTimeIllBeatWinona',
    'With the obstruction gone, the woman is eager to challenge Winona with her cherished Pokemon.', '''
She has her favorite Pokemon and another attempt in mind. I am rooting for a very proud walk back out of that Gym.|
She has clearly thought about this challenge before. I hope her confidence comes with a plan she and her Pokemon trust.|
She is ready to try again. That deserves some respect before anybody knows the result.|
She sounds glad just to have a clear way to the door. I hope the rest of her day keeps opening up.|
I like hearing how proud she is of her Pokemon. I hope they get a good rest afterward, however the battle goes.|
The path is clear and our challenger has returned with determination. I am invested in this local sequel.|
Trying again with a Pokemon she loves is a good reason to walk up those steps.|
She has her partner ready. I would like to know what she changed after her last attempt.|
She can reach the challenge she chose now. It is a small freedom worth enjoying.|
I hope she gets to keep that pride in her Pokemon through the whole battle, including the difficult bits.|
I would like to be here when she comes back out. Win or lose, she will have a story worth hearing.
''')

add('fortree_rain_and_roots', 'FortreeCity_Text_TreesGrowByDrinkingRainwater',
    'A girl explains that Fortree depends on rainwater, soil and the trees supporting its homes.', '''
The whole city depends on water and soil. I will try to remember that before complaining about another rainy day.|
She has followed the city all the way down to its foundations. The roots are doing much more work than the walkways suggest.|
People live up here because something below them keeps growing. It is worth remembering what needs looking after.|
It makes the rain sound less like an interruption when you think of everything it is keeping alive.|
These homes have living things under them that need water too. This city has quite a large household to look after.|
An entire city held up by trees drinking quietly beneath it. That is rather better than a decorative metaphor.|
I like that she sees the soil from all the way up here. It is easy to forget what a beautiful place rests on.|
These houses have foundations that grow. I would love to know how the builders leave room for the trees to change.|
Rain, roots, homes. She has noticed the relationship holding the whole place together.|
It is a lovely city, and she knows what lets it stay lovely. I appreciate that kind of attention.|
I should take a picture of the roots too. A photograph of the treetops would leave out half the story.
''')

add('fortree_lively_elder', 'FortreeCity_Text_EveryoneHealthyAndLively',
    'An old man credits treehouse living with making everyone lively and says he feels thirty years younger.', '''
Thirty years younger! I would settle for whatever these trees can do about the last staircase.|
He feels well, which is lovely. I would need more than one cheerful resident before assigning the credit to treehouses.|
He sounds happy living here. That is a better advertisement than any sign they could put at the entrance.|
He has the energy to make the claim convincingly. I will leave the exact number of years to him.|
Fresh air, movement, neighbors to talk to. I can see why he enjoys his days here.|
He has given the trees credit for thirty years of rejuvenation. I hope he also remembers whoever maintains the bridges.|
I would like to find somewhere I can grow older and still feel that pleased to wake up in it.|
I am glad the stairs are keeping him lively. They are currently making me reconsider how many tools I carry.|
He feels at home in his body and in this place. That is a good thing to hear someone say.|
He is wearing those claimed thirty years very confidently. I do not think he needs us to check the arithmetic.|
His enthusiasm would make a lovely portrait. I would label it with his own description of the place.
''')

add('fortree_window_bugs', 'FortreeCity_Text_BugPokemonComeThroughWindow',
    'A resident likes treehouse life but is startled when Bug Pokemon come through the windows.', '''
The windows apparently come with surprise residents. I hope the rent agreement is very clear about that.|
The homes share the trees with Pokemon that were already using them. Some careful window screens might help everyone coexist.|
I can enjoy a Pokemon and still prefer it to announce itself before landing beside my pillow.|
An unexpected wingbeat in a quiet room would startle me too. Especially if I had just put the instrument down.|
I hope they can guide the visitors back outside without hurting them. Then perhaps fit a screen.|
It is difficult to deliver a composed speech about life in harmony with nature when nature has just landed on your face.|
I like bugs much better when I know whether one is about to be on me.|
A light screen and a frame that fits the growing window space. I am already sketching something in my head.|
They are sharing a home with the tree's other inhabitants. It might help to agree on which parts have doors.|
I would rather choose my room's accents than have them fly in and choose me. A screen seems fair.|
The surprise is the difficult part. I could admire a visiting Pokemon much more easily after it lets me notice it arriving.
''')

add('fortree_trade_evolution_rumor', 'FortreeCity_Text_PokemonThatEvolveWhenTraded',
    'A boy has heard that some Pokemon evolve through trading.', '''
Some Pokemon evolve when traded. I wish changing my address made me taller and better at carrying groceries.|
Some species do respond to trading that way. It is worth learning what a particular partner needs before arranging a trade.|
We should think about the Pokemon and the person receiving it before making that decision.|
It is a strange sort of change to imagine: a new person waiting for you, and a new shape on the way.|
I hope every Pokemon making that trip has somebody kind waiting at the other end.|
An evolution brought on by an exchange. The Pokemon has a much more dramatic handover than the paperwork suggests.|
I would want to know I was going somewhere gentle before agreeing to a change that big.|
I would like to understand what part of the process causes the change. I am absolutely not volunteering anyone for an experiment.|
Some changes happen through a relationship with someone new. That does not make the old relationship unimportant.|
I hope trainers discuss what they actually want from the trade. A surprising evolution should not be the only thing they consider.|
I would like before-and-after pictures, with both trainers in them. There are two sides to that little history.
''')

add('dewford_fishing_instructions', 'DewfordTown_Text_ThrowInFishingAdvice DewfordTown_Text_FishingAdvice',
    'The fisherman explains facing the water and timing rod pulls when a Pokemon bites.', '''
Face the water, wait for a bite, and pull at the right moment. I am particularly pleased he specified the water part.|
He has given us a clear sequence to practice. Waiting for the right signal matters more than hauling at every twitch.|
We can learn the timing without rushing ourselves. He seems willing to explain it again if we need him.|
That sounds like listening for the beat before you come in. Except the beat may be an annoyed fish.|
I am glad he included advice with the encouragement. People need something to try, not just a demand to get better.|
There is a pause, a cue, and a decisive movement. I did not expect fishing to sound quite so much like rehearsal.|
I can manage the waiting. I suspect the sudden moment when I have to act will be where it becomes interesting.|
I will try the technique before redesigning the rod. Please remember that I have said this out loud.|
We can pay attention to what is happening at the other end of the line. Pulling harder at everything is rarely helpful.|
I appreciate instructions that tell us what to notice. It gives the waiting a little purpose.|
I want to learn the difference between a bite and the water moving. That seems like a better place to start than guessing.
''')

add('dewford_fishing_declined', 'DewfordTown_Text_ThatsTooBadThen',
    'The fisherman accepts our decision not to take up fishing.', '''
We have disappointed a fisherman by declining to become another fisherman. I think everyone will recover.|
He offered, and we answered honestly. We can be grateful for the offer without taking up the activity.|
We can decide how we want to spend the afternoon. He seems able to live with that.|
I would rather say no gently than stand beside the water pretending to have a wonderful time.|
It was kind of him to offer. We do not need to turn every kind offer into another thing to carry.|
A fishing career has ended before its first cast. I hope nobody had commissioned a commemorative portrait.|
It is a relief when declining something is allowed to be the whole conversation.|
One fewer tool in the bag today. I am trying to experience that as a positive development.|
We can leave a possibility open without agreeing to it now.|
He was hoping to share an interest. I hope he finds someone delighted to spend the afternoon on it.|
There are other things to do by the sea. We can appreciate the place without needing to catch anything in it.
''')

add('dewford_fishing_success', 'DewfordTown_Text_GreatHaulInSomeBigOnes',
    'After we report good fishing, the fisherman enthusiastically encourages us.', '''
He is pleased for us. I am pleased that a successful conversation about fishing did not require holding up a fish.|
He enjoys hearing that his advice has worked out. Sharing a skill can be satisfying long after the first lesson.|
He asked how we were doing and was glad to hear the answer. I like that.|
His enthusiasm has enough energy for both ends of the pier. I hope the catches have been worth it.|
It sounds as if our good news has improved his afternoon too. That is a nice result for a short conversation.|
He has promoted us directly to hauling in the big ones. I admire his confidence in a very brief progress report.|
I like being encouraged without having to prove every detail of what went well.|
He seems happy we are getting the hang of it. I shall resist turning that into a promise to catch something enormous.|
He has made room in his own enjoyment for somebody else's success.|
That was a generous reaction. We should tell people when their advice helped us more often.|
He sounds like he would enjoy hearing about the first catch as much as the biggest one.
''')

add('dewford_briney_waiting_letter', 'DewfordTown_Text_GoDeliverIllBeWaiting',
    'Briney offers to wait while we deliver the letter to Steven.', '''
Briney will wait while we deliver the letter. I am glad our timetable has room for us to find the right person.|
We have someone expecting a letter and someone willing to wait for us. The next part is pleasantly clear.|
He is giving us time to finish what we came for. Let us keep the letter safe and get it delivered.|
Knowing someone will still be here when we get back makes a strange island feel less strange.|
It is kind that he is willing to wait. I hope he and Peeko have somewhere comfortable to spend the time.|
The captain has allowed our important errand to proceed without an ominous deadline. I appreciate his taste in suspense.|
I like knowing there is a familiar face waiting for the return trip.|
We can finish one delivery before planning the next journey. An unfamiliar but promising approach to errands.|
He has offered us something useful and quiet: time to do what we said we would do.|
I would like to get back without the letter and with a thank-you ready for the person who waited.|
We have a small route through this place now: find Steven, deliver the letter, come back to Briney.
''')

add('dewford_briney_flexible_departure', 'DewfordTown_Text_JustTellMeWhenYouNeedToSetSail',
    'After we cancel the destination choice, Briney says he can sail when we are ready.', '''
A captain who lets us finish wandering first. This may be the most luxurious part of the voyage.|
We can decide when we have finished here instead of choosing a destination simply because the question came up.|
He is ready when we are. We can take a little time to work out where we actually want to go.|
I like a journey that has room for a pause before the next departure.|
We can have a look around without worrying that we have already kept the boat too long.|
Briney has paused the voyage without making the pause feel like a failure of the plot. A considerate captain.|
There is something comforting about being allowed to change your mind before leaving.|
Good. I would rather choose a destination before the boat starts moving than improvise one afterward.|
He is letting the next journey remain a choice. That is a kindness worth noticing.|
We can leave when we are ready. I hope that includes enough time to make sure nothing is missing from our bag.|
There is time to see the place we are in before we start thinking only about the next one.
''')

add('dewford_trend_agreement', 'DewfordTown_Text_YeahDefinitionOfInRightNow',
    'The trend enthusiast is delighted that we agree with his current favorite phrase.', '''
He is very pleased we agree. I hope the phrase survives the walk to the next street.|
He wanted to share an enthusiasm and found someone willing to listen. That is a pleasant use of a conversation.|
He likes it, we said we liked it, and everyone can carry on having a decent afternoon.|
I usually need a little longer before declaring something the sound of an entire moment. He has committed impressively quickly.|
I am glad our answer made him happy. I hope he enjoys it even after the next fashionable thing arrives.|
He has crowned the phrase ruler of the present moment. I expect the reign will be brief but passionately documented.|
I tend to like things quietly. He seems to enjoy liking them loudly enough for the rest of the island.|
He sounds ready to put it on a sign. I would suggest waiting until the paint from the last one dries.|
People can enjoy small things together. I hope he gets to keep that part even when the phrase changes.|
He is wonderfully confident about the current fashion. I would still give it a week before ordering matching accessories.|
I would like to hear what he thinks is fashionable when we come back. That could be a little history of its own.
''')

add('dewford_trend_sudden_expert', 'DewfordTown_Text_OfCourseIKnowAboutThat',
    'On hearing our new phrase, the enthusiast abruptly claims he knew it all along and rejects the old trend.', '''
That pause was the sound of him knowing it all along for the very first time.|
He has revised his opinion and immediately misdated the revision. I would accept a simple admission that he likes the new idea.|
He is allowed to change his mind. The elaborate story about never needing to is doing most of the work here.|
You can hear the exact moment he changes key and hopes nobody noticed.|
It would have been fine to say he had just learned something he liked. I hope he knows that.|
An astonishing performance of lifelong expertise, following several seconds of complete bewilderment.|
I recognized that pause. It is the gap between having no idea and deciding nobody can be allowed to know.|
I have had to admit to not knowing things much more loudly than that. He would survive saying it once.|
There is no shame in finding something new interesting. He is making discovery sound much more difficult than it needs to be.|
He changed fashions halfway through the conversation and would like the record to show he was already dressed for it.|
I would like to keep both versions of what he said. They make a more interesting portrait together.
''')

add('dewford_trend_disagreement', 'DewfordTown_Text_XHuhIThinkYIsCool',
    'After hearing our alternative phrase, the enthusiast says he still prefers his original trend.', '''
He heard our suggestion and still likes his own. I am relieved the island will not require a referendum.|
We offered an alternative, and he kept his preference. That is an entirely reasonable conclusion to the experiment.|
We do not have to agree about a favorite phrase. Neither of us needs to win this.|
Sometimes a different idea just does not have the sound someone wanted. He is allowed to keep his own.|
He knows what he enjoys. We can let him have that without turning the conversation sour.|
Our proposal has received a polite local review. I shall endeavor to survive without a dramatic public response.|
We can leave with different favorite things and still have had a perfectly good conversation.|
He considered the alternative and stuck with what works for him. I can respect that decision.|
An exchange of opinions does not have to end with somebody giving theirs away.|
I do not need everyone on this island to share my tastes. Keeping up with my own is already quite enough work.|
I would rather hear a preference he actually holds than a compliment he thinks we want.
''')

add('dewford_trend_future_news', 'DewfordTown_Text_HearOfAnyTrendsComeShareWithMe',
    'The enthusiast invites us to bring news of future trends.', '''
We have been appointed overseas correspondents for the island's favorite phrase. I hope the position includes snacks.|
He is curious about what people elsewhere are enjoying. We can bring him something we genuinely noticed on our travels.|
He has given us a reason to say hello again. I would rather bring a real story than make something up to impress him.|
I might bring him a tune somebody is humming somewhere else. I cannot promise it will still be fashionable when we arrive.|
I would enjoy telling him about something people were pleased to share with us. That seems worth bringing home.|
He wants news from the world, delivered one very enthusiastic conversation at a time. I can see the appeal.|
I will remember that somebody here wants to hear about little things we find interesting along the way.|
I should ask whether he wants working examples. My idea of a happening new thing may require a small demonstration.|
He has left the conversation open for our return. I like a goodbye that makes room for another visit.|
I may bring him news of a color everyone is wearing somewhere else. He can decide for himself whether it suits Dewford.|
I could bring a picture of something people have made popular in another town. It would give him more to ask about.
''')

add('sootopolis_brick_break_explanation', 'SootopolisCity_House1_Text_ExplainBrickBreak',
    'The martial artist identifies Brick Break but declares the move too horrible to describe.', '''
He has given the move a name and declined to describe it. I would like the wall's opinion before we try it indoors.|
He has identified the technique, but I would still appreciate actual instructions before calling the demonstration necessary.|
We can learn what it does without testing it on his furniture.|
That description leaves a great deal to the imagination. I am suddenly noticing how much of this room is breakable.|
I would like the Pokemon using it to know more about the plan than we currently do.|
He has achieved an impressive amount of suspense for a move with such a direct name.|
I think the name has already done most of the describing. The rest of the room would like us to stop there.|
I am interested in how it breaks through a barrier. I will investigate somewhere that is supposed to have broken things.|
Being able to break something is a reason to think carefully about when you use it.|
I hope the technique comes with more guidance than his sales presentation. I am becoming rather attached to intact doorways.|
I would ask for a demonstration in an appropriate training space. I have no wish to document the destruction of his home.
''')

add('sootopolis_kecleon_house_greeting', 'SootopolisCity_House1_Text_Kecleon',
    'The Kecleon living with the martial artist responds to a greeting.', '''
That sounded friendly. I am accepting it as permission to continue having no idea where Kecleon is looking.|
It seems comfortable sharing the house. I would like to learn how its routine fits around all that training.|
We can say hello and let it go back to its day. It does not need to perform for us.|
It has an interesting little call. I think I would recognize it even if I could not immediately spot the Pokemon.|
Hello, Kecleon. I hope living with a martial artist still involves plenty of peaceful meals.|
A brief reply from someone who could make an entrance almost anywhere. Such admirable restraint.|
I am glad it answered. A quiet Pokemon can still have something it wants to say.|
I would love to understand how it changes color. For now, I am keeping the questions out of its face.|
It gets to be at home here. We should be considerate visitors in its space too.|
Kecleon has more control over its color scheme than I will ever manage. I admire the flexibility.|
I would ask before taking a picture. Changing color should not mean losing the right to be left alone.
''')

# Authored expression choices, in Pip/Silas/Kade/Ashe/Nico/Riven/Emi/Vera/
# Lume/Mochi/Zuri order. These are reviewed with the lines, not inferred from
# words at runtime. A quiet neutral face is intentional where no change helps.
EXPRESSIONS = dict(N='neutral', S='soft_smile', A='annoyed', F='flustered',
                   D='sad', U='surprised', M='smug', L='laughing')
FACES = {
    'ship_scanner_search': 'S N N N N M N N N N N',
    'ship_scanner_delivery': 'M S N S S M S S S S S',
    'ship_cactus_name': 'M N D D S D N N D N N',
    'celadon_gym_spectator': 'A A A N A M A A A A A',
    'celadon_corner_reputation': 'N N A D N M N N N N N',
    'celadon_slots_loss': 'D N N D D D D A N D D',
    'celadon_poliwrath_friend': 'S S S S S S S S S S S',
    'celadon_poliwrath_greeting': 'S N S S S M N S S S S',
    'celadon_direct_threat': 'U A A D D M D A N A A',
    'celadon_rocket_obstruction': 'M A A A A M D M D A A',
    'celadon_hot_tea': 'M S N F S M F S S S S',
    'celadon_stolen_scope': 'N N D D D N D A N D N',
    'saffron_claimed_city': 'M A A D D A A A D A A',
    'saffron_criminal_thrill': 'M A A D A M A M A A A',
    'saffron_rude_pedestrian': 'M N N S S M N M N M N',
    'saffron_global_exploitation': 'A A A D D A D A D A A',
    'saffron_suspect_guard': 'A N A N D M M N A M N',
    'saffron_sleeping_guard': 'M S N S S M M S S M S',
    'saffron_victory_praise': 'S S S S S M S S S S S',
    'saffron_safe_streets': 'S S S S S S S S S S S',
    'saffron_returning_residents': 'S N N S S N D S S S S',
    'saffron_late_reporter': 'M N A N N M A N A N N',
    'saffron_pidgeot_greeting': 'M N S S S M N N S S S',
    'saffron_boss_escape': 'N N N D D M D N N N N',
    'saffron_dismissive_grunt': 'M N N N N M M A N M N',
    'museum_fine_arts_and_battles': 'S S S S S M S S S S S',
    'museum_artist_inspiration': 'S S S S S S S S S S S',
    'museum_child_sees_mother': 'S S S S S S S S S S S',
    'museum_mother_sees_son': 'S S S S S M S S S S S',
    'museum_new_paintings_visitor': 'S S S S S S F S S S S',
    'museum_cheerful_curator': 'S S S S S M S S S S S',
    'museum_aspiring_exhibitor': 'S S S F S N S S S S S',
    'museum_welcome_to_browse': 'M S S S S M S S S S S',
    'museum_uninterested_guest': 'S S N S S S S S S S S',
    'museum_greeter': 'S N S S S F S S S S S',
    'museum_regional_pride': 'M S S S S S S S S S S',
    'fortree_sky_witness': 'U N N M S M F U N M N',
    'fortree_gym_challenger_ready': 'S S S S S S S S S S S',
    'fortree_rain_and_roots': 'S N N S S S S U S S S',
    'fortree_lively_elder': 'M S S S S M S M S S S',
    'fortree_window_bugs': 'U N S U S M F N S M S',
    'fortree_trade_evolution_rumor': 'M N N N S S N U S N S',
    'dewford_fishing_instructions': 'M N S S S M F S N S N',
    'dewford_fishing_declined': 'M N N S S M S F S S S',
    'dewford_fishing_success': 'S S S S S M S S S S S',
    'dewford_briney_waiting_letter': 'S S N S S M S S S S S',
    'dewford_briney_flexible_departure': 'M S S S S M S S S S S',
    'dewford_trend_agreement': 'M S S S S M M S S M S',
    'dewford_trend_sudden_expert': 'M N M S S M M M N M S',
    'dewford_trend_disagreement': 'M N N S S M S S S M S',
    'dewford_trend_future_news': 'M S S S S S S U S S S',
    'sootopolis_brick_break_explanation': 'U N N U N M M U N M N',
    'sootopolis_kecleon_house_greeting': 'S N S S S M S U S S S',
}
assert set(FACES) == {row['key'] for row in ROWS}
for row in ROWS:
    moods = FACES[row['key']].split()
    assert len(moods) == 11, row['key']
    row['replies'] = [EXPRESSIONS[mood] + '~' + reply for mood, reply in zip(moods, row['replies'])]
