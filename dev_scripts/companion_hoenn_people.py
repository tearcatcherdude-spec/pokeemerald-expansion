"""Further Hoenn NPC conversations; authored responses, not runtime templates."""
ROWS = []
EMOTIONS = dict(N='neutral', S='soft_smile', A='annoyed', F='flustered', D='sad',
                U='surprised', M='smug', L='laughing')

def add(key, labels, subject, lines):
    replies = []
    for line in lines.strip().split('|'):
        line = line.strip()
        if len(line)>1 and line[1]=='~' and line[0] in EMOTIONS:
            line = EMOTIONS[line[0]] + line[1:]
        replies.append(line)
    assert len(replies)==11, (key,len(replies))
    ROWS.append(dict(key=key,labels=labels.split(),subject=subject,replies=replies))

add('petalburg_wally_missing', 'PetalburgCity_Text_WhereIsWally',
    'Wally\'s mother is looking for him because they must soon leave for Verdanturf.', '''
N~She has a departure to organize and a Wally to locate. I think I know which part is less predictable.|
N~She needs to know where he is before they leave. We should tell her what we actually know.|
N~She is worried about getting everyone together. Let us keep an eye out for him.|
N~I hope he knows she is waiting. Being eager to explore can make time disappear rather quietly.|
S~Getting ready to leave is easier when you know everybody is safe. I hope he comes back soon.|
N~An entire departure held up by one absent person. I recognize the essential structure of a rehearsal.|
N~I dislike the part where someone is looking for you and you do not know it yet.|
N~We should work out where he went before suggesting ten different ways to find him.|
N~She has somewhere to go and someone she needs beside her. I hope they find each other without more worry.|
N~I imagine she has already checked the obvious places twice. We can help by looking somewhere else.|
N~I would ask where she last saw him. A particular starting point is better than a whole town to worry about.
''')

add('rustboro_fire_rock_matchup', 'RustboroCity_Text_GymLeaderIsntEasyWithFire',
    'A trainer is struggling against Roxanne because Fire attacks fare poorly against Rock types.', '''
M~Trying to beat rocks with fire sounds like opening a quarry with a very stubborn candle.|
N~Rock resists Fire. She may need a different move or a teammate who can cover that matchup.|
N~A difficult matchup does not mean her Pokemon is bad. She needs to give it a plan it can use.|
S~Sometimes the partner is fine and the approach needs changing. I hope she does not confuse those two things.|
S~I hope she is taking good care of her Pokemon between attempts. Trying hard can still leave somebody exhausted.|
M~Her fire is receiving a rather firm review from the rocks. A change of approach might earn a better reception.|
N~It is hard when you want your favorite partner to do everything. It does not have to.|
N~She has identified what is going wrong. That gives her something useful to adjust before another attempt.|
S~A partner can be worth trusting without being the answer to every obstacle.|
S~She should keep the Pokemon she loves and make room for some help. The two ideas go together quite well.|
N~I would ask which part of the battle gave her trouble. The type matchup tells us where to begin, not the whole story.
''')

add('rustboro_badge_expectations', 'RustboroCity_Text_HaveYouChallengedGym',
    'A resident says earning a gym badge helps trainers understand what is expected of them.', '''
M~I hope the badge comes with the expectations written down. My bag already contains several mysterious responsibilities.|
N~A challenge can teach us something about our preparation. The metal afterward is a reminder, not the whole lesson.|
N~I think what we do for our team matters before anyone gives us a badge, too.|
N~I wonder whether the badge makes you feel different, or whether it helps you notice how much you have already changed.|
S~I hope those expectations include feeding everyone and noticing when they need a rest.|
M~A small shiny object with a surprisingly large job description. Very economical administration.|
N~I would rather understand what we are trying to become than only count what we have won.|
N~I like having a practical test. I would also like people to explain the standards before we walk through the door.|
N~Recognition can matter. So can the work someone does when nobody is there to award anything for it.|
S~It is nice to have something tangible to show for the effort. I hope we remember the effort as clearly as the shine.|
N~I would like to hear what his first badge taught him. That would tell us more than the general advice.
''')

add('rustboro_badge_local_pride', 'RustboroCity_Text_HeyThatsRustborosGymBadge',
    'A resident recognizes our Rustboro badge and declares it the coolest badge.', '''
S~We have found the badge's most enthusiastic local supporter. I hope every town supplies one.|
S~He recognized it immediately. It is nice to see the work mean something to somebody outside the Gym.|
S~He is proud of his town's badge. We can let him enjoy seeing someone who earned it.|
S~It feels good when somebody notices a small thing that took us a lot of work.|
S~That is a lovely welcome for the new badge. I hope our team gets a share of the congratulations.|
M~An excellent review, with a charmingly visible local bias. I shall accept it in the spirit intended.|
S~I like people being fond of the place they live. Even when it comes out as a very firm opinion about metal.|
S~I am curious about the design now. Somebody in Rustboro clearly managed to make it memorable.|
S~He has found a little piece of his home on our journey. I like that connection.|
M~He has excellent confidence in local accessories. I can respect a person who commits to a favorite.|
S~We should get a picture of it somewhere in Rustboro before we leave. That would be a good place to remember earning it.
''')

add('rustboro_briney_tunnel_walks', 'RustboroCity_Text_MrBrineyWalksInTheTunnel',
    'A boy says Briney lives by the sea and sometimes walks in the tunnel.', '''
S~A seaside cottage and occasional tunnel walks. Briney appears to have found hobbies for several kinds of weather.|
N~That gives us a useful idea of where he spends time. We can ask around without assuming he is always at home.|
S~It sounds as though people here know his usual route. That is a good place to start looking for someone.|
N~I wonder what he likes hearing in the tunnel. The sea and a cave have very different kinds of quiet.|
S~I hope he has someone to walk with when he wants company. Familiar routes can be nicer that way.|
M~The retired sailor has acquired a regular walking route. I appreciate a character who has a life between entrances.|
S~A place by the sea and somewhere dim to wander. I can see the appeal of both.|
N~I would like to know which parts of the tunnel are open before following anyone's walking route through it.|
S~He has made a small routine on land after so much traveling. That sounds peaceful.|
S~People remembering where you like to walk is a quiet sort of belonging.|
N~The boy noticed a familiar person going about his day. Those are useful little details to remember.
''')

add('rustboro_briney_shops_for_peeko', 'RustboroCity_Text_MrBrineyLovesPeeko',
    'A resident says Briney goes shopping in Slateport for Peeko.', '''
S~Peeko has a personal sailor doing the shopping. I am choosing to admire this arrangement rather than become jealous.|
S~He puts real effort into caring for Peeko. That says rather more about their bond than a grand introduction would.|
S~He knows what his partner needs and goes out to get it. I like that.|
S~I wonder whether Peeko recognizes the sound of the bags when he gets home.|
S~That is a very affectionate reason to make a shopping trip. I hope he remembers to get something for himself too.|
M~A celebrated seafarer, now on an important supply mission for one bird. I think his priorities are excellent.|
S~It is nice to hear a grand old sailor talked about in terms of someone he looks after.|
S~A sea trip for the right supplies makes sense if you know exactly what you are looking for. Peeko sounds well provided for.|
S~Love can look like knowing what to bring home. I like that version of the story.|
S~I hope Peeko approves of his purchases. There is clearly a great deal of devotion behind the selection.|
S~I would love a picture of the moment he returns and Peeko sees what he brought.
''')

add('rustboro_child_travel_dream', 'RustboroCity_Text_WowYouHavePokemon',
    'A child wants to travel with Pokemon when older.', '''
S~I hope the first big trip is full of wonderful discoveries and only a manageable number of wet socks.|
S~Curiosity is a good start. I hope someone helps them learn how to look after a partner before the journey begins.|
S~I hope they get a kind partner and somebody they can come home to.|
S~It is lovely to hear somebody imagine a future with so much room in it.|
S~I hope their first packed lunch has something from home in it. Big journeys can begin gently.|
S~They already have the opening line of an adventure. There is plenty of time to discover the rest.|
S~I remember wanting the world to be bigger than the roads I knew. I hope it is kind when they go looking.|
S~I hope they get to learn useful things before they have to improvise them far from home.|
S~Wanting to see somewhere new with a friend beside you is a good dream to keep.|
S~I hope they find their own way of traveling. Looking like the people who inspired you is only the beginning.|
S~I wonder which place they picture first when they talk about going somewhere.
''')

add('rustboro_school_rare_pokemon', 'RustboroCity_Text_CatchRarePokemonIfIGoToSchool',
    'A prospective student wonders whether school will make rare Pokemon easier to catch.', '''
M~I hope the rare Pokemon have agreed to attend the practical lesson. Otherwise this could become a very long field trip.|
S~School can help with preparation and technique. Finding something rare still involves looking carefully and being patient.|
N~Learning is worth doing even before it gives you the thing you wanted most.|
S~A good lesson might make an ordinary encounter feel more interesting, too. I hope they get that part.|
S~I would like the school to teach care alongside catching. Rare Pokemon still need ordinary meals and kindness.|
M~They have already chosen the most exciting part of the prospectus. The school will now have to explain the homework.|
S~I hope they stay curious when the answer takes more work than they expected.|
S~Good instruction saves a lot of avoidable mistakes. I am a late but enthusiastic supporter of this principle.|
N~I hope they learn to notice the Pokemon they meet, even when those Pokemon are not difficult to find.|
S~There is nothing wrong with having a particular goal. A school may still have more to offer than the quickest route to it.|
N~I would ask the teacher what students actually practice. It would make the hope a little more concrete.
''')

add('rustboro_evolution_observer', 'RustboroCity_Text_PokemonCanChangeLookFromExp',
    'A resident explains that some Pokemon change appearance as they gain battle experience.', '''
U~A few battles and somebody can become a completely different shape. My own training has mainly changed the shape of my shoes.|
N~Some species evolve as they gain experience. I would be interested in how the trainer notices the approach of that change.|
N~We should pay attention to how a partner feels about changing, as well as how strong it might become.|
N~It must be a strange thing to wake up to a voice that comes out a little differently.|
S~I hope a Pokemon gets the same affection before and after it changes. Growth should not feel like earning permission to be loved.|
M~The cast member may return in an entirely new costume, with no time allowed for alterations. Pokemon have demanding transitions.|
N~I would want someone familiar beside me for a change that large.|
U~I would love to understand how all those parts reorganize. I will begin by keeping an observation notebook, not by poking anyone.|
N~A new shape is still someone we already know. We should leave room for both the difference and the familiarity.|
S~I wonder which familiar habits stay exactly the same afterward. That would make the new appearance feel less strange.|
N~I would like a record of the little things around an evolution, not just the bright moment itself.
''')

add('rustboro_evolution_surprise', 'RustboroCity_Text_PokemonChangeShape',
    'A resident is astonished at the idea of Pokemon changing shape.', '''
M~I hope somebody is sitting beside him when he first sees an evolution. That seems like a useful precaution.|
S~It is a reasonable thing to be astonished by, even when it has become familiar to the rest of us.|
S~He is hearing something new. We can let him be surprised without making him feel foolish.|
S~I like hearing the wonder come back into a thing we have started taking for granted.|
S~I hope his first experience of it is a happy one for the Pokemon, too.|
M~He has reached the part of the explanation where the imagination needs a chair. I rather like his honesty.|
S~He has allowed himself to say that it sounds extraordinary. It does, when you stop and think about it.|
S~I would be happy to answer questions. I would also completely understand if the first question were just how.|
S~A familiar fact can still be remarkable. He has reminded us of that.|
S~Somebody should let him finish being amazed before giving him three more facts to absorb.|
S~I would like to see his face when he encounters it for himself. Some discoveries deserve that much attention.
''')

add('rustboro_traded_partner_obedience', 'RustboroCity_Text_TradePokemonGrowFast',
    'A resident explains faster growth and possible disobedience for traded Pokemon without enough badges.', '''
N~Growing quickly and listening carefully are apparently separate qualifications. I have known a few people like that too.|
N~Growth does not automatically produce trust or readiness. We should prepare for the partner we are receiving, not just the level it might reach.|
N~I would rather understand what the Pokemon needs than rely on it being impressed by a badge.|
N~It is a lot to ask of a partner: a new home, a new trainer, and instructions from someone it just met.|
S~We should make the new Pokemon feel secure before expecting everything to work smoothly.|
M~A remarkable growth rate and a strongly independent opinion of the director. That could make rehearsal interesting.|
N~Being new somewhere can make even simple instructions feel more difficult. I hope trainers remember that.|
N~Fast growth sounds useful until it outruns your ability to look after it. Planning matters here.|
N~A badge can mark experience. It should not replace the patience involved in getting to know a new partner.|
N~I would rather have a team that is comfortable with us than one that only looks impressive on paper.|
N~I would ask the previous trainer about the Pokemon's habits. Some useful things will never fit on a badge.
''')

add('rustboro_double_challenge', 'RustboroCity_Text_YouCanHave2On2Battle',
    'A resident explains that two trainers can jointly challenge a lone trainer with at least two Pokemon.', '''
U~Two trainers can challenge us at once. I would like a sign I can carry saying ONE CONVERSATION AT A TIME.|
N~Two opponents change the number of interactions we must account for. We should think about how our partners support each other.|
N~Taking on two people is less impressive if we have not prepared our team for it. We can choose our battles.|
N~It sounds like trying to follow two parts at once. You need to hear what they are doing together.|
N~I hope the person walking into that challenge knows they are allowed to get everyone healed first.|
M~Two challengers, one trainer, and no indication that the invitation was carefully scheduled. A busy scene.|
N~I think I would like a little warning before an ordinary walk becomes a coordinated argument with Pokemon.|
S~Now that is a situation where two individual plans can turn into a third, much messier plan. I would prepare for that.|
N~Having two partners beside us should mean giving both of them the attention they need.|
N~I would like to know whether the two opponents have practiced together. Matching enthusiasm does not necessarily make a team.|
N~I would watch the cooperation as closely as the individual moves. That is where the interesting part will be.
''')

add('rustboro_school_newcomer', 'RustboroCity_Text_YoureNewAroundHere',
    'A Devon employee notices a new face and asks whether we transferred to the Trainer School.', '''
M~Our school transfer has been inferred from standing near a school. I hope nobody has already assigned us a desk.|
S~He noticed somebody unfamiliar and offered a plausible place to begin the conversation. We can introduce ourselves.|
S~We are a new face here. It is nice to be asked who we are before someone decides what we need.|
F~I always need a moment to remember how to introduce myself when someone asks unexpectedly.|
S~He is making room for a newcomer in his picture of the town. We can answer kindly.|
M~A new arrival has entered the scene and is immediately offered an educational backstory. Very efficient exposition.|
N~I like being new somewhere better when people sound curious instead of suspicious.|
S~We should ask what the school teaches. Being mistaken for a student is a perfectly good excuse to learn something.|
S~Every familiar person in a town was a new face once. He seems to remember that.|
S~I hope the school is as welcoming to its actual new students as he sounds.|
S~I like hearing how people place a newcomer in their town. It tells us something about the life already here.
''')

add('rustboro_corner_witness', 'RustboroCity_Text_SneakyLookingManWentAroundCorner',
    'A resident remembers a suspicious person going around the corner.', '''
N~Around the corner is considerably more useful than somewhere over there. We are making progress toward actual directions.|
N~He has a particular sighting, rather than a general impression. We should keep the route clear in our notes.|
N~We can check the corner without treating everyone we meet beyond it as the same person.|
N~He remembered a small moment that suddenly matters. I hope it helps somebody.|
N~We should thank him for stopping to think. People can notice useful things without realizing it at the time.|
M~The witness has supplied a direction. I shall resist demanding an atmospheric description of the corner as well.|
N~A corner is at least something we can actually go and look at.|
N~We should follow the information we have before inventing a complicated explanation for where he went.|
N~A specific observation is worth treating carefully. We should not let our guesses take its place.|
N~I hope we can come back with news that makes the interruption to his day feel worthwhile.|
N~I would ask which corner before setting off. It is an important detail in a town that has rather a lot of them.
''')

add('mauville_crossroads', 'MauvilleCity_Text_AllSortsOfPeopleComeThrough',
    'A resident says Mauville\'s four-way roads bring people from many places.', '''
S~Four directions to arrive from and plenty of people to ask for directions. Mauville seems prepared for my usual navigation method.|
N~A crossroads collects people who might never otherwise meet. I would like to hear what has traveled here with them.|
S~It sounds like a good place to find someone who knows the road ahead.|
S~You could sit here and hear the day arrive in several different accents.|
S~I wonder what everybody is carrying for lunch. A crossroads must have excellent ideas passing through it.|
S~A town where new characters can enter from every side. I imagine the local gossip requires careful filing.|
S~I like places where people can be passing through without having to explain why they are there.|
S~Four routes mean a lot of wear on the roads and a lot of interesting repairs. I would get distracted here.|
S~People can share a place briefly and still leave something with one another.|
S~I would enjoy seeing how people from different places dress for the same journey.|
S~I could spend a whole afternoon here listening to where people have come from. The crossroads would do most of the arranging.
''')

add('mauville_recover_after_battle', 'MauvilleCity_Text_NurseHurtMonBackToHealth',
    'A resident reminds trainers to heal Pokemon hurt in battle.', '''
S~That is the part of winning I would hate to forget. Nobody should have to limp through the celebration.|
N~A battle result is only one thing to check afterward. We should pay attention to how every partner is recovering.|
N~Our team trusts us to notice when it hurts. That responsibility does not end when the other trainer loses.|
N~The quiet after a battle is a good time to listen for who is not quite all right.|
S~Yes. Healing, food, water, and a little patience. They should get care without having to ask perfectly.|
N~The dramatic finish should be followed by somebody checking that the whole cast is comfortable.|
N~I like that someone here thought to say it plainly. Care should be part of the routine.|
N~We should fix the damage before setting off to collect any more of it.|
N~A partner is still our responsibility after the exciting part has ended.|
N~I would rather spend extra time getting everyone comfortable than hurry along looking like we have had a productive day.|
N~I want to remember the Pokemon looking well afterward, too. That matters as much as the moment of the win.
''')

add('mauville_bike_wild_encounters', 'MauvilleCity_Text_PokemonCanJumpYouOnBike',
    'A resident warns that riding a bike does not prevent wild Pokemon encounters.', '''
M~The Pokemon have not agreed to respect bicycle traffic. I hope somebody has at least explained the bell.|
N~The bike changes how we travel, not whether Pokemon occupy the route. We still need to pay attention.|
N~We should keep the team ready and our eyes ahead. Moving faster is not the same as being out of trouble.|
N~I would prefer to meet a wild Pokemon after I have stopped trying to balance.|
N~We should leave enough room to stop. Startling a Pokemon and falling off a bike sounds unpleasant for everyone involved.|
M~A bicycle does not exempt us from the local cast of surprise encounters. I appreciate the advance notice.|
N~I would like both feet on the ground before negotiating a sudden meeting in the grass.|
S~Good brakes belong on the preparation list. So does remembering that the grass is somebody else's home.|
N~We can move through a place quickly and still owe its inhabitants a little care.|
N~I would rather arrive a little slower than introduce my outfit to the road.|
N~I would watch the path as carefully as the distance we are making. A fast trip still has things in front of it.
''')

add('mauville_rydel_generosity', 'MauvilleCity_Text_RydelVeryGenerous',
    'A resident recommends Rydel\'s Cycles because its owner is generous.', '''
S~A generous bicycle shop owner sounds like somebody we should meet before my feet write a formal complaint.|
S~I would like to hear what he has done to earn that reputation. People tend to remember practical kindness.|
S~It is good to hear somebody recommend a person, rather than just a price.|
S~I like a town where somebody else's kindness turns into advice given to a newcomer.|
S~I hope he knows people talk about him that fondly when he is not in the room.|
M~The bicycle merchant has received excellent word of mouth before making an entrance. A promising introduction.|
S~It is nice to be directed toward someone because they might make the day easier.|
S~I would enjoy looking at his bikes. I will try not to interpret generosity as permission to rearrange the workshop.|
S~A useful gift can change how much of the world someone gets to see. I would like to meet him.|
S~A good reputation is a lovely thing for a shop to have that cannot simply be painted over the door.|
S~We should ask him how the shop began. I would like to know the person behind the recommendation.
''')

add('mauville_television_enthusiast', 'MauvilleCity_Text_ExplainTV',
    'An enthusiast likes new TV shows, recognizes friends on screen, and hopes to appear on TV too.', '''
M~He would like to appear on television. I would first like to know whether my embarrassing moments have already signed a contract.|
N~Recognizing friends sounds exciting. I am rather more interested in the part about being shown without being told.|
N~I hope people get a choice about being on screen. Being noticed is not always what somebody wanted.|
N~It is strange to imagine your ordinary day turning into a program in somebody else's room.|
S~I hope he gets the sort of appearance he would actually enjoy, with enough warning to tell the people who care about him.|
M~He has declared his availability to an entire medium. I admire the ambition of the audition.|
F~I would like to be asked before becoming somebody's unexpected evening viewing.|
N~The shows sound interesting. I would still prefer advance notice before a camera decides my workbench needs an audience.|
N~A familiar face can make a screen feel friendly. The person on it should get to feel comfortable too.|
F~If I ever appear on television unexpectedly, I would like the courtesy of having dressed on purpose that morning.|
N~I like recognizing people in pictures. I also like asking them whether the picture is one they want shared.
''')

add('mauville_wattson_generator_directions', 'MauvilleCity_Text_WattsonWontBeChallenge',
    'Wattson gives directions to New Mauville and expresses confidence in us for the generator task.', '''
N~He has made the dangerous generator sound like a short errand. I would like us to keep the directions and bring our own caution.|
N~We know where the entrance is. His confidence is encouraging, but it does not replace checking what is unsafe down there.|
N~We can take the job seriously even if he makes it sound easy. Nobody needs us to be careless to prove we can do it.|
N~I appreciate being trusted. I would also appreciate knowing which noises mean we should leave immediately.|
N~We should get everyone ready before going underground. Confidence is easier to carry when the team is comfortable.|
M~A malfunctioning underground generator has received a wonderfully cheerful introduction. I am adding a more cautious stage direction.|
N~I am willing to help. I am also allowed to be a little concerned about the word generator.|
N~I want the power off safely. I do not want to become the interesting sound somebody hears from the next room.|
N~Being trusted with something is a reason to prepare carefully, rather than a reason to stop being afraid of it.|
N~I would like our return to be as reassuring as his send-off. Let us take the practical preparations seriously.|
N~I will remember the entrance route clearly. An unfamiliar underground place deserves a good plan for getting back out.
''')

add('mauville_wattson_completed_task', 'MauvilleCity_Text_WattsonYoungTakeCharge',
    'After the generator task and reward, Wattson praises younger people taking responsibility.', '''
S~He is pleased with us. I am pleased we get to discuss the generator from somewhere above it.|
S~It is good to have the work recognized. I hope the safer system stays that way after we leave.|
S~We handled something that needed doing. We can accept the praise without volunteering for the next emergency immediately.|
S~I like hearing that laugh when the difficult part is over. It sounds rather less like a challenge now.|
S~I hope the next part of taking charge is making sure everyone gets a good rest.|
M~A successful return and enthusiastic applause from the person who sent us. I prefer this arrangement to a dramatic rescue.|
S~We did something useful and got to come back. That is a good ending to hold on to for a moment.|
S~I am glad he is happy. I am also glad we can now call that equipment a completed job.|
S~He put trust in us, and we brought care back to the task. It is nice when those meet properly.|
S~We may enjoy that compliment for a little while before finding something else that needs our attention.|
S~I would like the story to include the preparation as well as the brave part. That is what made the return possible.
''')

add('verdanturf_clean_air', 'VerdanturfTown_Text_AirCleanHere',
    'A resident says the winds keep volcanic ash away and praises the clean air for people needing rest.', '''
S~Delicious air. I like that this town has given me a local specialty I cannot accidentally drop.|
N~The wind keeping ash away is useful to know. I would still be careful about promising that a pleasant place can cure everything.|
S~I hope people who come here to recover get the time and support they need, as well as the fresh air.|
S~It does feel easier to take a quiet breath here. I would like to stay still long enough to notice that.|
S~Clean air and somewhere gentle to rest sound like a good beginning for someone who has had a hard time.|
M~The town has successfully marketed a breeze. For once, I think I understand the enthusiasm.|
S~I like that people describe living here as something that can feel good. Not every place has to be exciting.|
N~Knowing which way the ash travels matters. I hope the houses have good ventilation as well as a favorable wind.|
S~A peaceful place can give someone room to recover at their own pace. I hope the people here make that room.|
S~I would enjoy spending an afternoon somewhere that takes being comfortable seriously.|
S~I would like to record how this place feels as well as how it looks. The quiet is part of why people come.
''')

add('verdanturf_quiet_tunnel_work', 'VerdanturfTown_Text_ManTryingToDigTunnel',
    'A child explains that machinery frightened the tunnel\'s timid Pokemon and a lone man continues digging.', '''
N~He is digging by himself because the Pokemon could not stand the noise. That is a lot of work to do thoughtfully.|
N~The project had a real effect on the Pokemon living there. I am glad somebody noticed before simply using louder equipment.|
N~I hope he has help and time to rest. Caring about the Pokemon should not mean he has to carry every part of the job alone.|
N~A loud tunnel is somebody else's whole home. It is easy to forget that when you are only passing through.|
S~I would like someone to bring the man a meal while he works. Quiet determination still gets hungry.|
N~An entire construction project stopped for frightened Pokemon, and one man kept looking for a gentler way. That is a story worth hearing.|
N~I understand wanting a route open. I also understand the creatures who cannot simply move away from the noise.|
N~A quieter method may be slower, but the animals living around the work are part of the engineering problem.|
S~He is trying to make room for people without taking all the room away from the Pokemon already there.|
N~I hope the people who eventually use the tunnel know why the work took care and time.|
N~I would like to record the work while it is happening. A finished tunnel might hide how carefully someone tried to make it.
''')

add('verdanturf_tunnel_for_love', 'VerdanturfTown_Text_ManDugTunnelForLove',
    'A child has heard that a man dug the tunnel to reach the woman he loves.', '''
S~He wanted to see someone and moved a great deal of rock about it. I hope she appreciated the visit.|
S~Wanting to reach someone can be a powerful reason to keep working. I hope the tunnel is remembered as a shared achievement too.|
S~He found a way to get closer to someone he cares about. That is easier to understand than the amount of digging involved.|
S~It is a love story you can walk through. I rather like that it has ended up useful to other people too.|
S~I hope they get some peaceful time together after all that work. A grand effort should still leave room for an ordinary evening.|
S~A romantic gesture with a measurable reduction in travel time. I am impressed by its range of benefits.|
S~Someone cared enough to make the distance smaller. I think I understand that part.|
S~I admire a romantic gesture that also becomes a useful piece of public infrastructure.|
S~He made a path toward someone he loved, and other people can share it. That is a lovely thing to leave in a place.|
S~I hope the relationship receives as much care as the dramatic part of the story. The visits afterward matter too.|
S~I would like to photograph both ends of the tunnel. It is a connection, and the story belongs on both sides.
''')

add('verdanturf_tunnel_hopes', 'VerdanturfTown_Text_GuyTryingToBustThroughCave',
    'A boy hopes the man breaking the cave\'s boulders can make a route to Rustboro.', '''
M~He sees a pile of boulders and imagines a convenient trip to Rustboro. That is a very optimistic approach to a rock.|
N~A route through would change how people here travel. I hope the work is planned around the Pokemon in the cave as well.|
N~It would help a lot of people. I hope the person doing the work knows that, and gets some help in return.|
S~It is interesting how a blocked passage can sit in the middle of several people's plans for their day.|
S~An easier way to visit people and get supplies would mean a great deal to the town.|
M~The boy has already planned the sequel in Rustboro. First, somebody needs to finish the rather substantial opening obstacle.|
N~I would like that path to open gently. The people waiting and the Pokemon living there both have reasons to care about it.|
N~I want to see what is actually blocking it. A good solution starts with more detail than a general dislike of boulders.|
N~A little distance on a map can be a very large distance in someone's ordinary life.|
S~I can see why he is eager. Convenient travel changes what you can do without turning a whole day into an expedition.|
N~I would ask him what he would go to Rustboro for first. That would tell us what the tunnel means to him.
''')

add('verdanturf_open_tunnel_shopping', 'VerdanturfTown_Text_EasyToGetToRustboroNow',
    'With the tunnel open, a resident is pleased that Devon shopping in Rustboro is easier.', '''
S~The tunnel is open, and his first great expedition is shopping. I respect a journey with a clearly defined bag at the end.|
S~The benefit is already part of somebody's routine. That is a useful way to measure whether a route matters.|
S~It is good when a difficult piece of work makes ordinary days easier for people.|
S~The route has become familiar enough to be part of a shopping plan. I like hearing what happens after the grand opening.|
S~I hope it also makes visits to friends easier. Groceries are important, but they should not get all the new route to themselves.|
M~A tunnel built with considerable feeling has begun its second career in retail convenience. Places can contain more than one story.|
S~Somebody worked hard, and now he can think about a simple trip instead of a difficult journey. That is a good change.|
S~I would like the builders to hear that. It is satisfying when a finished job starts being useful without needing an explanation.|
S~A path between towns can make both places feel a little less far away from one another.|
S~I hope he enjoys the shopping and gets home without finding that he bought more than he can comfortably carry.|
S~I would like to see what kinds of trips people start making now. The tunnel will keep changing the town in little ways.
''')

add('verdanturf_battle_tent_debut', 'VerdanturfTown_Text_MakeBattleTentDebut',
    'A trainer plans a Battle Tent debut after a winning streak with their Pokemon.', '''
S~A winning streak and a new venue. I hope they have packed the confidence somewhere it cannot squash the sensible preparations.|
N~A different battle format may ask different things of the team. Recent wins are encouraging, but preparation should fit the place.|
S~I hope they can enjoy the challenge without feeling that one loss would erase everything they have done.|
S~A first appearance somewhere new can make even familiar skills feel different. I hope they get a kind start.|
S~I hope the Pokemon get a rest before their debut. A streak can make people forget how much work each win took.|
S~A debut with momentum behind it. I am pleased for them, though I would still rehearse the entrance.|
N~I hope the new experience matters more to them than keeping the record perfect.|
S~Trying a new format is a good way to discover which parts of a plan are actually doing the work.|
S~They have something to feel proud of and somewhere new to grow. I hope both feelings get room.|
S~I hope they remember their first appearance fondly even if the streak ends there. A debut can offer more than a number.|
S~I would like to hear what feels different about this place after their first battle here.
''')

add('fallarbor_cozmo_concern', 'FallarborTown_Text_ShadyCharactersCozmosHome',
    'A resident is worried about suspicious visitors around Professor Cozmo\'s home.', '''
N~He has noticed something wrong around Cozmo's home. I would rather check on the professor than turn the worry into a rumor contest.|
N~He has seen people arriving and leaving. We should ask what happened without deciding the rest of the account for him.|
N~Somebody should make sure Cozmo is all right. A person's home is a poor place to feel surrounded by strangers.|
N~I dislike hearing that someone has begun to feel uneasy about a familiar doorway.|
N~He sounds genuinely concerned. We can take that seriously without frightening him further with guesses.|
N~The neighbors have noticed an unsettling change in the professor's visitors. That seems worth following up quietly and promptly.|
D~I hope Cozmo has somebody he can ask for help. Being worried about your own home can make it hard to know where to begin.|
N~We should find out what the visitors actually want. There is no useful repair to make from a vague suspicion alone.|
N~A neighbor noticing that something feels wrong can matter a great deal. We should listen carefully.|
N~I would like the professor to have the chance to tell his own part of what is happening.|
N~I would ask when the visitors started coming. A change in routine is sometimes the most useful detail someone has noticed.
''')

add('fallarbor_meteor_history', 'FallarborTown_Text_RegionKnownForMeteors',
    'A resident recounts the area\'s meteor history and the origin story of Meteor Falls.', '''
U~A falling rock made a landmark people still talk about. I am grateful my dropped belongings have shown less ambition.|
N~The landscape may preserve evidence of that event. I would enjoy comparing the local account with what the rock formations tell us.|
N~It is strange to think an ordinary-looking place can carry the trace of something that sudden and enormous.|
N~People have been telling that story for a long time. I wonder what the first person to hear the impact thought it was.|
N~I hope the area has had quieter days since. It is easier to admire a meteor when it is already part of the ground.|
M~An arrival from the sky with a very enduring effect on the setting. Most dramatic entrances have shorter consequences.|
S~I like places with a history older than anyone who can explain it to us. There is room to wonder there.|
U~I would like to examine what the impact left behind. From a respectful distance, until I know what is stable.|
N~Something that traveled so far has become part of the place people call home. That is an interesting kind of belonging.|
N~The name gives the landscape a story before we have even seen it. I would like to look carefully when we do.|
N~I would try to show the scale in a picture. The interesting part is how much of the old event is still here.
''')

add('fallarbor_proud_azurill_owner', 'FallarborTown_Text_MyPreciousAzurill',
    'A girl proudly describes her Azurill as smooth and plushy.', '''
S~She has delivered a very enthusiastic review of her Pokemon. I hope Azurill is equally pleased with the arrangement.|
S~She clearly notices the small details of a partner she loves. It is nice to hear that kind of attention.|
S~She is proud of Azurill. We can appreciate it without assuming an introduction is permission to pick it up.|
S~She sounds as if every detail is another reason to be fond of it. I like hearing someone talk that way.|
S~I hope Azurill gets as much thoughtful care as enthusiastic praise. They look like happy company for one another.|
M~A complete introduction built around being exceptionally pleasant to hold. Azurill has a very clear public image.|
S~I can see why she wanted to tell someone. Having a little friend can make ordinary details feel worth announcing.|
S~I am keeping my questions about the tail's mechanics to myself for a moment. This is clearly a proud introduction.|
S~She has made it very clear that this Pokemon matters to her. That is the part I would like to remember.|
S~She has described Azurill with excellent attention to texture. I think the little model deserves a break afterward.|
S~I would like a picture of the two of them together. Her expression is as much a part of this introduction as Azurill's.
''')

add('fallarbor_azurill_greeting', 'FallarborTown_Text_Azurill',
    'The girl\'s Azurill responds to a greeting.', '''
S~Rooreelooo to you too. That was a much better greeting than anything I had prepared.|
S~It seems happy to answer. We can let a short, comfortable greeting be enough.|
S~Hello, Azurill. We will leave your feet on the ground while we get acquainted.|
S~That little call has a lovely rise to it. I would probably recognize it again after hearing it once.|
S~I hope it gets plenty of quiet time between all the people admiring it. Being adorable can be a busy job.|
M~An extremely brief appearance with considerable charm. I believe the audience is satisfied.|
S~I like the way it answered. There is no need to ask it to do anything else for us.|
S~I am resisting several questions about balance. For now, hello is a perfectly good contribution.|
S~It has greeted us on its own terms. That is a nice beginning.|
S~A delightful little voice. I hope we have not interrupted an important part of enjoying its day.|
S~I would rather let it move naturally than ask it to pose. The little things it chooses to do are interesting enough.
''')

add('fallarbor_flannery_expectations', 'FallarborTown_Text_HaveYouChallengedFlannery',
    'A resident mentions Flannery\'s accomplished grandfather and hopes she becomes great in her own right.', '''
N~I hope people ask Flannery about her own battles as often as they mention her grandfather's.|
N~A family history can be interesting without being a complete account of someone's ability. I would like to see her own approach.|
N~She deserves the chance to become good at the job without every step being compared to somebody else.|
N~I know how difficult it can be to hear somebody else's name in the introduction to your own work.|
S~I hope she has people who encourage her when she is learning, not just people waiting to see how she measures up.|
N~A famous predecessor is an impressive introduction and a rather heavy curtain to walk out from behind.|
N~I hope she gets to be herself loudly enough that people learn to begin the conversation with her.|
N~Experience can be passed on. The work of learning what to do with it still belongs to her.|
N~It is kind that he hopes she will succeed. I hope that leaves room for her to succeed in her own way.|
N~A person can inherit a reputation before having any say in it. I would like to hear what she wants to make of hers.|
N~I would like to document her work without making the family comparison the whole caption.
''')

add('pacifidlog_floating_hometown', 'PacifidlogTown_Text_NeatHousesOnWater',
    'A child proudly points out the houses built on water and says they were born here.', '''
S~He was born in a town that floats. I imagine learning to find your sea legs happens rather early here.|
S~Living above the water must shape a great many ordinary routines. I would like to hear which things he takes for granted.|
S~He is proud of his home. We should let him show us what matters to him about it.|
S~I wonder which sounds tell him he is home before he even looks up.|
S~I would like to know what a family meal feels like with the water moving underneath the house.|
S~He has introduced his hometown and his own beginning in the same breath. A very economical origin story.|
S~Something that feels extraordinary to us has always been home to him. I like remembering that difference.|
U~I want to see how the supports move with the water. I will ask before crawling underneath anything.|
S~A familiar home can be remarkable without needing to feel unusual to the person who grew up in it.|
S~I like the confidence with which he points it out. He knows his home has something worth showing people.|
S~I would ask him which view he likes most. The person who grew up here will notice things a visitor walks straight past.
''')

add('pacifidlog_strong_current_warning', 'PacifidlogTown_Text_FastRunningCurrent',
    'A resident warns that the fast current toward Slateport can sweep surfers off course.', '''
N~The sea has its own travel plans. I would like to read them before contributing us to the itinerary.|
N~We should plan the route around the current rather than assume effort alone will take us where we intended.|
N~We need a way through and a plan for where we could end up. Our partner should not have to solve that alone.|
N~I would like to know the quiet water before learning about the fast water in person.|
N~We should make sure the Pokemon carrying us is ready for that crossing. A warning is a good reason to prepare.|
N~An unexpected destination is entertaining in a story and considerably less charming when your bag is full of seawater.|
N~I prefer surprise changes of plan to happen somewhere I can stand up.|
N~A current is doing work whether we appreciate it or not. We should understand the direction before adding our own effort.|
N~The water does not know where we want to go. We should not mistake it for a path that was laid out for us.|
N~I would rather arrive dry and slightly later than become a cautionary example told by this same person.|
N~I want to look at a map before we set off. A picture of the destination is less useful if we cannot actually reach it.
''')

add('pacifidlog_sky_pillar_heights', 'PacifidlogTown_Text_SkyPillarTooScary',
    'A fisherman knows Sky Pillar but prefers sea-level life to climbing it.', '''
M~He has heard of the very tall tower and chosen the very sensible sea level. I appreciate a clearly stated preference.|
N~Knowing about a place does not oblige him to climb it. We can ask for information without turning it into a dare.|
N~He knows what makes him uncomfortable. I am not going to argue him into a height he does not want.|
N~I can imagine the wind sounding different the farther you climb. I also understand being happy to imagine it from here.|
S~He seems content with the life he has by the water. I am glad he feels able to say so.|
M~He has declined an imposing tower in favor of remaining comfortable. That is a perfectly serviceable character decision.|
N~I would not like to explain my fear of heights to someone who only wanted to talk me out of it.|
N~If we climb it, I want to know the condition of the way up. Height is not the only practical question.|
S~A place can be important without being somewhere everybody needs to go.|
N~I respect a person who can admire a landmark while also having firm plans to remain below it.|
N~A picture from below can still tell us something. We do not need to put him somewhere frightening to hear his view of the place.
''')

add('lavaridge_geothermal_springs', 'LavaridgeTown_Text_HotSpringsNeverRunDry',
    'A resident explains that magma heats underground water to supply the springs.', '''
S~The volcano is heating the bathwater. I appreciate it doing something sociable for once.|
S~He has explained the heat source as well as admiring the result. I like his approach.|
S~I can enjoy the warm water while remaining very glad the magma stays underneath it.|
S~All that warmth rising through the ground. It makes sitting still feel connected to something enormous.|
S~Warm water that keeps arriving. I can see why people make a comforting routine of this.|
M~The volcano has accepted a supporting role in a very peaceful afternoon.|
S~I like knowing where the warmth comes from. It makes the quiet here more interesting.|
S~A natural heat supply. I have several engineering questions and a strong desire to sit down first.|
S~Something fierce underground has become a gentle place for people to rest.|
S~I am happy to appreciate the result while keeping a polite distance from the source.|
S~I would like to show the steam against the mountain. They belong in the same picture.
''')

add('lavaridge_flannery_bather', 'LavaridgeTown_Text_BatheInHotSpringsEveryDay',
    'A girl bathes daily and hopes to become a strong, beautiful Gym Leader like Flannery.', '''
M~If bathing were the whole qualification, the Gym queue would contain several very wrinkled champions.|
S~Admiring Flannery is a good beginning. I hope she enjoys learning the training part too.|
S~I hope she gets to become someone she likes, rather than an exact copy of somebody else.|
S~I like hearing someone say who has made the future seem exciting to them.|
S~She sounds happy with her routine. I hope her Pokemon enjoy the rest of their day together too.|
M~She has committed admirably to the warmest part of the training program.|
S~I hope she finds out what she brings to the idea herself. That is the interesting part.|
S~The bath might help her relax. Practice will have to take responsibility for the battles.|
S~A role model can show you a possibility without choosing your whole path.|
S~I hope she keeps that confidence when the preparation becomes less comfortable than a bath.|
S~I would like to ask what she admires most about Flannery besides the obvious first impression.
''')

add('lavaridge_pokemon_baths', 'LavaridgeTown_Text_IfPokemonInHotSprings',
    'A bather imagines electric, bubble or lava baths if different Pokemon joined the springs.', '''
U~I would prefer to select my bath before the Pokemon accidentally select it for me.|
N~Different Pokemon would need different conditions. The existing bathers would also deserve a say.|
N~We should ask what is safe before inviting the team into somebody else's bath.|
N~I can picture the bubble bath. My imagination is declining the lava option.|
N~Everyone should be comfortable. That includes checking the water rather than assuming warmth suits every Pokemon.|
M~A relaxing bath with an unusually dramatic list of possible special effects.|
N~I would like to keep the surprising part of the bath limited to how relaxed I feel afterward.|
U~An electric bath is an idea I would like to investigate exclusively on paper.|
N~Sharing a space means thinking about what our presence changes for everyone else.|
N~I have already spent enough time choosing my clothes. I am not adding emergency lava-proofing.|
N~I would ask the people who maintain the springs before arranging any aquatic group portraits.
''')

add('lavaridge_extravagant_claims', 'LavaridgeTown_Text_HotSpringsClaims',
    'A bather lists claims that the springs relieve tension, fix romance and attract money.', '''
M~If the money is attracted to the bath, I would like it to stop hiding in the changing room.|
M~Warm water may be pleasant. The financial and romantic claims could use rather more evidence.|
N~A bath can give us time to think. It is unlikely to do the difficult conversation for us.|
S~I would settle for leaving with my shoulders lower than my ears. The rest sounds ambitious.|
S~Rest is already a good thing to offer. They do not need to promise somebody a whole new life.|
M~Relaxation, romance, and a sudden fortune. The bath has a remarkably demanding contract.|
M~I would be suspicious of water that claimed to understand my romantic problems better than I do.|
M~If it attracts money, I should be able to fund repairs by soaking my invoices.|
N~A little calm might help someone choose what to do next. It does not make the choice disappear.|
M~If wealth arrives, I hope it has the courtesy to wait until I am dressed.|
N~I would ask what people actually enjoy about the springs. That sounds more interesting than the advertisement.
''')

add('lavaridge_bathing_age_surprise', 'LavaridgeTown_Text_OhYouLikeHotSprings',
    'A bather is surprised that someone our age enjoys hot springs.', '''
M~Apparently enjoying warm water has an age requirement. I hope nobody asks for a membership card.|
S~People can enjoy the same comfort at different ages. It is a useful thing to have in common.|
S~I do not think liking a good rest needs much of an explanation.|
S~Sometimes a quiet afternoon is appealing before anybody thinks it ought to be.|
S~A comfortable bath can be a lovely part of a day at any age.|
M~Our appreciation of warm water has become a surprising character revelation.|
M~I intend to enjoy being comfortable before I receive official permission to look tired.|
S~I have carried tools up enough stairs to appreciate this without waiting any longer.|
S~It is nice when people discover a small pleasure they can share with someone unexpected.|
S~I would rather be surprising in a bath than predictable and aching elsewhere.|
S~I like the idea that this place brings together people who might otherwise never sit and talk.
''')

add('lavaridge_egg_declined', 'LavaridgeTown_Text_AsYouWishThen',
    'The woman accepts our decision not to take the Egg and offers to wait.', '''
S~She is willing to wait. I am glad the Egg's future does not depend on us answering quickly.|
N~Taking responsibility for an Egg deserves a considered decision. She seems to understand that.|
N~We should take it when we are ready to care for it properly, not because saying no feels awkward.|
S~It is easier to make a kind decision when someone leaves room to think.|
S~She wants it looked after. Being honest about our readiness is part of doing that.|
S~A very small future has been offered a patient pause. I approve of the pacing.|
N~I like that we can come back after thinking about it.|
N~We can prepare before accepting a responsibility that will eventually hatch.|
S~Waiting can be a thoughtful choice when another life is involved.|
S~She has made the offer without making us feel trapped by it.|
S~I hope she finds the right person, whether that turns out to be us or someone else.
''')

add('lavaridge_egg_party_full', 'LavaridgeTown_Text_NoRoomForThisEgg',
    'The Egg cannot be accepted because the traveling party is full.', '''
N~No room for the Egg. I am glad we checked before attempting creative stacking.|
N~We need an open party space before accepting it. This is a logistical problem with a clear solution.|
N~We can make room carefully and come back. There is no need to rush the team around.|
N~I would rather find out here than halfway down the road with nowhere comfortable to put it.|
N~Let us make sure everyone has a proper place before bringing someone new along.|
M~The arrival has been delayed by a full traveling company. Even an Egg needs a place in the cast.|
N~It is all right to get ready first. The woman is not going anywhere immediately.|
N~This is a capacity limit we should respect without attempting an ingenious workaround.|
N~Making space for someone can take a little thought. We have time to do that kindly.|
N~A safe place for the Egg matters more than pretending our bag is endlessly accommodating.|
N~We know what needs sorting out. Let us do that and return without making a fuss.
''')

add('lavaridge_egg_daycare_rumor', 'LavaridgeTown_Text_EverySoOftenEggFoundAtDayCare',
    'The woman mentions rumors of Eggs appearing at the Pokemon Day Care.', '''
M~The Day Care apparently has occasional surprise residents. I hope its lost-property system is very gentle.|
N~She is careful to call it a rumor. I would ask the people who work there what they have observed.|
N~An Egg appearing means somebody will need to care for it. That part matters whichever account is right.|
N~I wonder how the staff react when they discover a new little possibility in the middle of a normal day.|
S~I hope every Egg they find has someone ready to keep it safe.|
M~A rumor with a small, warm, and potentially very time-consuming conclusion.|
N~I am more interested in who looks after the Egg than in people making the discovery sound mysterious.|
N~The Day Care staff would be better people to ask than a chain of guesses.|
S~However it arrives, it deserves a thoughtful welcome.|
N~I hope the staff get asked about their work as often as they get asked about that rumor.|
N~I would like to hear an actual account from somebody who found one.
''')

add('lavaridge_egg_accepted', 'LavaridgeTown_Text_HopeYoullWalkPlentyWithEgg LavaridgeTown_Text_ReceivedTheEgg',
    'We accept the Egg; the woman hopes we will carry it on plenty of walks.', '''
S~We have acquired a very small walking companion with absolutely no opinion about the route yet.|
S~We should keep it safe and include it in our routine. Patient observation is a good beginning.|
S~We have time to give it a gentle start. Let us look after it properly.|
S~I wonder what sounds it will learn to recognize while we are carrying it.|
S~I am already thinking about a comfortable place to rest when we stop for meals.|
S~The company has gained a new arrival before we have even learned its entrance cue.|
S~There is someone new coming with us. That is a nice reason for a walk.|
S~I will keep the tools away from the Egg. This is an important improvement to our packing plan.|
S~We can make a welcoming little place in the journey for it.|
S~It should have a safe spot before we think about making that spot look charming.|
S~I would like to record some of these days, not just the moment it hatches.
''')

add('lavaridge_sand_nip', 'LavaridgeTown_Text_PokemonNippedBackside',
    'An old man relaxing in hot sand is suddenly nipped by a Pokemon.', '''
U~The sand treatment has acquired teeth. I would request a very specific explanation before booking it.|
U~That changed the experience abruptly. We should check whether he is hurt and what disturbed the Pokemon.|
N~Let us make sure he is all right before anyone starts laughing about it.|
U~He sounded so peaceful a moment ago. That was a remarkably abrupt ending to the relaxation.|
N~I hope it was only a fright. He should be able to rest without another surprise nip.|
M~A tranquil monologue interrupted by a very committed supporting performer.|
F~I have reconsidered my position on burying the parts of me I cannot easily inspect.|
U~I would like a better survey of the sand before becoming part of the terrain.|
N~We may have found somebody else's occupied patch of sand. I hope everyone can be comfortable again.|
U~I was considering that treatment. The latest testimonial has introduced a concern.|
N~I would put the camera down and see whether he needs help first.
''')

add('mossdeep_sea_and_dry_land', 'MossdeepCity_Text_FeelReliefOnLand',
    'A sailor loves the sea but feels relieved to reach land after a long voyage.', '''
S~You can love the sea and still be pleased when the floor stops arguing with your knees.|
S~A familiar profession can still be tiring. His relief makes perfect sense.|
S~Loving the journey does not mean you have to dislike coming home.|
S~I imagine the first quiet night on a floor that stays still feels wonderful.|
S~A proper meal at a table that stays level sounds like a very good welcome.|
S~The sailor has returned to an audience considerably less likely to move underneath him.|
S~I like hearing someone admit that their favorite thing can also wear them out.|
S~Stable ground is an excellent place to put down both your tools and your exhaustion.|
S~A safe return is part of what makes a journey worth loving.|
S~He can be fond of the sea without needing to prove it every waking moment.|
S~I would like a picture of the moment someone spots home from the boat.
''')

add('mossdeep_sea_land_cycle', 'MossdeepCity_Text_LifeNeedsSeaToLive',
    'A resident reflects on the connection between sea, living things and the land.', '''
N~He has given this shoreline a much larger job description than I expected.|
N~The connections matter. The boundary we can see is only one part of a much longer exchange.|
N~It is worth thinking about what happens beyond the edge of the place we are standing.|
N~I like the idea that a shoreline is somewhere things keep meeting, rather than simply ending.|
S~It makes looking after one little place feel connected to looking after a great deal more.|
N~A quiet view with an enormous amount of history arriving at its feet.|
N~I could stand here with that thought for a while.|
N~I want to know how the smaller processes work. Big ideas become more interesting when you can follow the parts.|
S~He is paying attention to a relationship people walk past every day.|
N~I like a view that gives you something to think about after you leave it.|
N~The waterline would make a good place to begin the picture, rather than the place to stop it.
''')

add('mossdeep_magma_space_center_warning', 'MossdeepCity_Text_MossdeepTargetedByMagma',
    'A sailor reports Magma trouble at Mossdeep and directs us toward the Space Center.', '''
N~One team has barely left the conversation before the other arrives. These uniforms are becoming a terrible travel guide.|
N~The Space Center gives us somewhere to verify the warning. We should learn what is actually happening there.|
N~If people are being threatened, we should find out what help they need.|
N~I would like one of these visits to begin with good news about the people who live here.|
N~We should check on the staff, not just ask what the villains are planning.|
N~The sailor has supplied an address for the trouble. I would prefer that to another ominous hint.|
D~People here deserve better than becoming the next place everyone is worried about.|
N~A Space Center is not somewhere I want Magma experimenting with equipment.|
N~We can take the warning seriously without filling in the unknown parts with panic.|
N~Let us find someone at the center who can tell us what they are facing.|
N~I will keep the sailor's account separate from anything we actually see when we get there.
''')

add('mossdeep_flower_world', 'MossdeepCity_Text_NiceIfWorldCoveredByFlowers',
    'A girl wishes the whole world were full of plants and flowers like Mossdeep.', '''
S~A world full of flowers sounds lovely. My nose would like a small seat at the planning meeting.|
S~I like her enthusiasm. Different places and Pokemon would need different kinds of growing things.|
S~She has found something she loves about home and wants other people to have it too.|
S~I would like to hear what all those places sound like when the wind moves through them.|
S~I hope there would be room for vegetable gardens among the flowers. Beauty and dinner can be neighbors.|
S~An ambitious proposal for the world's scenery. I would like to see her first sketch.|
S~I would keep a few quiet paths between the flowers. Somewhere to sit and look at them.|
S~There would be a lot to look after. I hope the plan includes the people doing the watering.|
S~Wanting more living things around us is a lovely wish to begin with.|
S~I would enjoy seeing how people made different kinds of beauty out of the same wish.|
S~I would like to see the places she would choose to plant first.
''')

add('mossdeep_scott_unconcerned', 'MossdeepCity_Text_ScottSomethingWrongWithTown',
    'Scott notices warnings concerning the Space Center but says they do not concern him.', '''
M~He noticed the warning and decided it belonged to somebody else's afternoon. A very portable talent.|
N~He has identified a possible problem. I would rather he followed that observation with a useful question.|
A~It concerns the people living here. That is enough reason to pay attention.|
N~It is a strange thing to hear somebody describe a town's worry and step neatly around it.|
N~I hope someone asks whether the Space Center staff are all right.|
M~He has introduced a serious subplot and declined his own involvement in the same speech.|
A~I wish he sounded as interested in worried people as he does in strong trainers.|
A~Equipment getting threatened at a Space Center concerns me quite a bit, actually.|
N~We do not have to be the person directly threatened to care what happens next.|
N~He has excellent confidence in the boundaries of his responsibilities. I would draw them a little differently.|
N~I would like to hear from the people whose warning he has just summarized.
''')

add('mossdeep_wallace_mentor', 'MossdeepCity_Text_SootopolisNewGymLeader',
    'A resident says Sootopolis has a new Gym Leader who once mentored Wallace.', '''
S~Wallace had a teacher. I like finding out that impressive people also had to ask where to begin.|
N~I would be interested in how teaching Wallace shaped the new leader's own approach.|
N~A good mentor can matter long after the student starts doing things differently.|
N~I wonder which habits Wallace kept and which ones he turned into something of his own.|
S~I hope they are both proud of the work they did together.|
S~A teacher steps back into the spotlight after the student has made a name. There is a good conversation there.|
N~It must be interesting to watch someone you taught become someone other people look up to.|
N~I would like to compare their methods. Teaching someone does not mean building an identical copy.|
S~Knowledge can keep moving between people, even after the formal lessons end.|
N~I would rather hear what the new leader wants to do than only measure them against their former student.|
N~I would like a portrait of them together if they wanted one. Their connection is part of both stories.
''')

add('mossdeep_rocket_launches', 'MossdeepCity_Text_SpaceCenterLaunchingRockets',
    'A resident talks about the Space Center\'s large rockets.', '''
U~Huge rockets. I would like to be both close enough to see and far enough away to remain pleasantly attached to my shoes.|
S~A launch is the visible part of an enormous amount of careful work. I would like to learn about the preparation.|
S~I hope everybody working there gets to see something they are proud of go safely.|
U~I wonder how long you feel the sound after it has finished being a sound.|
S~I hope the staff get a quiet meal after a launch. That sounds like work that makes you forget lunch entirely.|
U~The island has built a way to make an exit genuinely spectacular.|
S~I would like to see a launch with someone who could explain the quiet moments before it.|
U~I have so many questions about the engines that I may need another notebook.|
S~There is something moving about people working together to send something beyond the place they know.|
U~I would choose a very secure hat before standing anywhere near launch day.|
S~I would love to photograph the people watching, as well as the rocket.
''')

add('mossdeep_warning_letter', 'MossdeepCity_Text_SpaceCenterReceivedLetter',
    'A resident says a recent letter has caused an uproar at the Space Center.', '''
N~A letter has managed to disturb a building full of rockets. I would like to know what it said.|
N~We should ask somebody who received it. The commotion alone will not tell us the contents.|
N~The people at the center deserve to have the warning taken seriously.|
N~I hope the staff have somebody helping them decide what to do, rather than just everyone worrying at once.|
N~I would ask whether anybody there needs support while they deal with it.|
N~A letter with a very large effect on the room. I would prefer to read the actual message before predicting the next act.|
D~It is unpleasant when an ordinary delivery changes how safe a place feels.|
N~I want to hear from the staff before assuming which part of the equipment is at risk.|
N~We can bring some calm to a worried place by listening before guessing.|
N~I hope the person who has to answer the letter is not having to deal with everything alone.|
N~I would like to know when it arrived and what changed afterward. Those are useful details to begin with.
''')

add('mossdeep_safe_launch_wish', 'MossdeepCity_Text_SpecialSpaceCenterRock',
    'A woman explains the white rock symbolizes wishes for safe launches and says she uses wish tags.', '''
S~A small rock carrying a very large hope. I would like the rockets to appreciate the effort.|
S~The wish does not replace the preparation. It gives people a way to express how much a safe return matters.|
S~I hope the people doing the dangerous work know the town is thinking about them.|
S~I like having something quiet to hold the feeling before all that noise begins.|
S~A safe launch means people getting to breathe again afterward. I can understand wanting a little ritual for it.|
S~The stone has no speaking part and still manages to say something important about the town.|
S~I would rather make a small honest wish than pretend not to care because I cannot control the outcome.|
S~I would check every fitting and still understand somebody wanting to leave a wish tag beside it.|
S~A little ritual can give care somewhere to go while we wait.|
S~I like that the wish is for safety. It tells us what people want most from something so impressive.|
S~I would like to photograph the tags with permission. Each one stands for somebody wanting a person to come home.
''')

add('mossdeep_surf_enthusiasm', 'MossdeepCity_Text_SurfExhilarating',
    'A resident loves crossing the sea with Pokemon using Surf.', '''
S~A trip with the sea right there instead of politely underneath a boat. I can see the appeal and feel the splash already.|
S~It must give a different sense of the water. I hope the rider pays as much attention to their partner as to the view.|
N~It sounds exciting. It is also a lot of trust to place in a Pokemon carrying you.|
S~I like the idea of moving at the water's own level for a while.|
S~I hope the Pokemon gets a proper break after carrying someone so far.|
S~A voyage where the traveling companion is also the vessel. That changes the meaning of looking after the company.|
S~I would like a calm patch of sea to begin with. Exhilaration can meet me there.|
S~I would secure the bag carefully before finding out how exhilarating the first wave is.|
S~Sharing a crossing with a partner sounds lovely when both of you are ready for it.|
N~I would prefer to plan my wet clothes in advance rather than discover them dramatically.|
S~The view would be wonderful. I would make sure looking at it did not take attention away from the Pokemon.
''')

add('mossdeep_wailmer_watching', 'MossdeepCity_Text_WailmerWatching',
    'A local struggles to remember the name of Wailmer watching.', '''
M~Wailmer watching. He has introduced it with enough suspense to make a second Wailmer seem necessary.|
S~I like that spotting wild Pokemon has become something people enjoy without needing to catch them.|
S~We could spend a little time looking. There is no need to turn every sighting into a battle.|
S~I would enjoy sitting quietly until one breaks the surface.|
S~That sounds like a good afternoon, especially if we bring lunch and leave the water undisturbed.|
M~A memorable title, eventually delivered. I am happy to wait just as patiently for the actual Wailmer.|
S~I like a hobby that mostly asks us to be still and notice when something wonderful arrives.|
S~I would like to know how close you can get without disturbing them. That seems like the first useful question.|
S~It is nice to enjoy a wild Pokemon while letting it keep its ordinary day.|
S~I would pick a comfortable place to wait. A magnificent sight is easier to appreciate without a cramp.|
S~I would love to try it. I would rather miss a picture than push a Wailmer away from somewhere it wanted to be.
''')

add('mossdeep_kings_rock_gift', 'MossdeepCity_Text_YouCanKeepIt',
    'After we accept the King\'s Rock, its owner lets us keep it and asks us not to tell Steven.', '''
M~We have acquired a mysterious rock and a surprisingly specific request about discussing the rock.|
N~Not knowing its use does not make it worthless. I hope we can put it to good use rather than simply pass the mystery along.|
N~We can thank him without making him feel foolish for not wanting it.|
S~I wonder what Steven hoped he would enjoy about it. Gifts can arrive with different meanings than the giver intended.|
S~I hope it finds a purpose with us. It is nicer to pass something on thoughtfully than leave it forgotten.|
M~A gift, a secret, and a rock with a royal title. I had expected a shorter transaction.|
N~I hope he knows he was allowed not to understand the present. Keeping that a secret sounds tiring.|
S~I am interested in finding out what it does. At least we have a name to begin with.|
N~Something can be useful to another person without its first owner having done anything wrong.|
M~I shall try not to announce our discreet acquisition at a volume audible from Steven's house.|
N~I would remember who gave it to us. Its story does not have to end with somebody feeling embarrassed.
''')

add('mossdeep_kings_rock_declined', 'MossdeepCity_Text_WhatToDoWithWeirdRock',
    'After we decline the King\'s Rock, its owner continues wondering what it is for.', '''
M~We have agreed that it is a strange rock. The mystery has survived the conversation completely intact.|
N~We could ask someone familiar with unusual stones. Agreeing that it is confusing has not supplied much new information.|
N~He does not have to keep something he does not want. I hope he finds someone who understands it.|
N~I wonder how many interesting things spend years waiting for someone to ask the right person about them.|
S~We can decline the gift kindly. The owner still deserves an answer to his question if we find one.|
M~A scene in which two people inspect a mystery and mutually decide to remain uninformed. Surprisingly believable.|
N~I hope he does not feel silly about asking. People learn things by being allowed not to know them first.|
N~Unknown purpose is an invitation to investigate, although I understand not wanting every investigation in your bag.|
N~He was willing to give it away. Perhaps somebody can offer him understanding in return.|
N~I would like him to find out what it is before deciding the gift was pointless.|
N~I would ask Steven about it if we had the chance. He is part of the account we have actually been given.
''')

add('mossdeep_steven_neighbor', 'MossdeepCity_Text_StevensHouseOverThere',
    'The boy points out Steven\'s house.', '''
S~A useful direction to Steven's house. I appreciate an important person being findable without an expedition.|
S~We know where to ask our questions now. I hope we arrive at a considerate time.|
N~We can knock. Knowing where somebody lives is not permission to surprise them inside it.|
S~I like learning where someone belongs when they are not out doing the things people know them for.|
S~I hope he gets ordinary quiet evenings here too.|
M~The celebrated trainer has a house over there. Fame occasionally has pleasantly practical geography.|
N~It is nice to think of someone impressive getting to close a familiar door behind them.|
S~I would enjoy hearing about his collection. I will ask before inspecting anything in it.|
S~Having a place to come back to matters, however far somebody travels.|
S~I hope visitors remember it is his home before treating it like a destination.|
N~I would ask him what he likes about living on this island. An address is only the beginning of that answer.
''')
