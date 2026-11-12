"""Additional source-reviewed Gym conversations, appended after the first Gym module."""
ROWS = []
EMOTIONS = dict(N='neutral', S='soft_smile', A='annoyed', F='flustered', D='sad',
                U='surprised', M='smug', L='laughing')

def add(key, labels, subject, lines):
    replies = []
    for line in lines.strip().split('|'):
        line = line.strip()
        if len(line) > 1 and line[1] == '~' and line[0] in EMOTIONS:
            line = EMOTIONS[line[0]] + line[1:]
        replies.append(line)
    assert len(replies) == 11, (key, len(replies))
    ROWS.append(dict(key=key, labels=labels.split(), subject=subject, replies=replies))

add('rustboro_guide_advice', 'RustboroCity_Gym_Text_GymGuideAdvice',
    'The guide volunteers to help us become Champion and explains Roxanne Rock weaknesses.', '''
M~We have acquired a very enthusiastic unpaid coach. He even came with useful advice.|
N~Water and Grass attacks are worth considering. Check our actual moves before choosing a lead.|
S~Useful information. You still get to decide how to use it.|
F~He believes in us very loudly for someone we just met.|
S~A stranger has decided to cheer us on. That is a nice welcome.|
M~He cast himself as our trusted adviser before we could hold auditions.|
M~I was not prepared to become a group project this morning.|
N~He identified the specialty and two weaknesses. A practical briefing under all the shouting.|
S~A long road begins with somebody insisting you can walk it.|
S~He gives advice freely. That is a good first impression.|
S~I wonder how many first-time challengers he has helped through that door.
''')
add('rustboro_guide_victory', 'RustboroCity_Gym_Text_GymGuidePostVictory',
    'The guide credits his cheering and tells us to check our first badge on the Trainer Card.', '''
M~His cheering won the battle! Our Pokemon would like a brief word about that.|
S~Checking the recorded badge is sensible. His causal explanation is more enthusiastic than rigorous.|
S~You and the team earned it. He can have a little credit for the encouragement.|
S~Seeing it on the card might make the whole thing feel real.|
S~Let us check the badge, then thank the team properly.|
M~The supporting cast has submitted a modest claim to authorship of the finale.|
M~I am happy he enjoyed his contribution from the very safe part of the room.|
N~Confirm the result is recorded. Celebrate after the paperwork. Then celebrate properly.|
S~A little mark on a card can hold the weight of a long first step.|
S~You should look at it for a moment. You only get a first badge once.|
S~I want to remember your face when you see it recorded there.
''')
add('dewford_guide_advice', 'DewfordTown_Gym_Text_GymGuideAdvice',
    'The guide warns about Fighting attacks and says winning battles brightens the dark Gym.', '''
U~Defeat trainers to turn on the lights. I have been paying an electricity bill like a fool.|
N~Keep Normal Pokemon away from unfavorable matchups. The changing visibility is a separate puzzle.|
N~Watch the team and the path. It is easy to lose track of either in here.|
N~I like the dimness. I like knowing where the exits are even more.|
N~Let us make sure everyone is comfortable before starting through the dark.|
M~The lighting designer has delegated the entire production to our battle record.|
M~A Gym where victory lets you see the person you just fought. Thoughtful.|
N~Performance-controlled lighting. I would prefer a normal switch for emergencies.|
S~Each challenge leaves a little more of the room visible.|
N~I appreciate the advice. I would also appreciate a railing.|
N~We should keep track of where we came from before the room changes around us.
''')
add('dewford_guide_victory', 'DewfordTown_Gym_Text_GymGuidePostVictory',
    'The guide jokes that both the Gym and player future are bright after victory.', '''
M~The future is bright. So is the room. My eyes would like both to adjust gradually.|
S~He is pleased for us. The room is also considerably easier to navigate now.|
S~Good win. Now we can find the exit without guessing.|
F~I forgot how visible we would all be at the end.|
S~A badge and a clear way home. Both good results.|
M~Our victory has received the full lighting budget.|
M~The future looks promising. The present is making me squint.|
S~The brightness change is decisive. At last I can see what the floor has been doing.|
S~The room kept a little sunrise for the end of the battle.|
S~He has been waiting for an excuse to say that. Let him enjoy it.|
S~I would like to remember this room with everyone finally visible.
''')
add('mauville_guide_advice', 'MauvilleCity_Gym_Text_GymGuideAdvice',
    'The guide warns Water Pokemon about Electric attacks and describes Wattson switch doors.', '''
N~Water and electricity are a bad introduction. So are visitors and unmarked switches.|
N~An Electric specialty and a switching puzzle. We should prepare for both independently.|
N~Choose the lead carefully. Then look before stepping on anything.|
N~The explanation helps. I would rather know what can happen before it happens.|
N~We can take our time. The team does not need to rush through a place this unfamiliar.|
M~The eccentric host has supplied danger, doors, and a man to shout the instructions.|
M~A cheerful warning that the building may zap us. Very welcoming.|
S~Switch-controlled doors! I have concerns, but I am listening.|
N~The bright room has a pattern beneath its noise. We can find it.|
N~I am keeping both feet well away from anything that looks decorative and electrified.|
N~His impression of the electricity was vivid enough. I would rather not hear the original.
''')
add('mauville_guide_victory', 'MauvilleCity_Gym_Text_GymGuidePostVictory',
    'The guide celebrates our electric victory and opened doors.', '''
M~We powered the door open! Please do not make us the building's permanent generator.|
S~The path is clear and the badge is earned. A satisfying pair of results.|
S~We are through. Give the team their due before the next stop.|
S~I am glad the room feels less threatening now.|
S~A good battle, and no need to solve another door on the way out.|
M~The building has accepted our performance and released its doors for the curtain call.|
M~Electrifying. I am choosing to treat that as figurative while standing very still.|
S~A successful test and an accessible exit. Both important acceptance criteria.|
S~The path opens after the noise. A good moment to breathe.|
S~We can enjoy being impressive once we are clear of the wiring.|
S~He sounds almost as pleased as Wattson. This Gym knows how to welcome a winner.
''')
add('lavaridge_guide_advice', 'LavaridgeTown_Gym_1F_Text_GymGuideAdvice',
    'The guide praises Flannery passion and recommends Water attacks with overheated metaphors.', '''
U~I assume he means Water moves. I would like that confirmed before anyone buys a hose.|
N~Fire matchups are useful information. The rest of his temperature forecast seems figurative.|
N~We can use the advice without underestimating her.|
F~I hope she is easier to talk to than that introduction makes her sound.|
N~A Water teammate may help. So will keeping everyone rested in this heat.|
M~The adviser has mistaken a tactical briefing for a municipal fire warning.|
M~I will admire her passion from the recommended nonflammable distance.|
N~A type recommendation, several alarming metaphors, and no explanation of the floor vents.|
N~Fire is more than heat. We should see how she actually tends hers.|
N~I would rather meet her than keep hearing how dramatically she burns.|
S~She must have made quite an impression on him. I wonder what she thinks of his version.
''')
add('lavaridge_guide_victory', 'LavaridgeTown_Gym_1F_Text_GymGuidePostVictory',
    'The guide calls the victorious battle scorching hot.', '''
M~Scorching! I am going to recover with an extremely ordinary temperature of water.|
S~A demanding battle. The team has earned a cooler place to recover.|
N~Good fight. Let us get everyone out of the heat for a while.|
S~I can feel my shoulders relaxing now that it is over.|
N~Water, shade, and some rest before the next journey.|
M~An enthusiastic review from a critic whose vocabulary has been thoroughly preheated.|
M~I am happy with the win and ready to stop marinating in the atmosphere.|
N~Successful, but we should still let everything cool before the next test.|
S~The flame has settled. We can set down the effort for a moment.|
N~A victory looks better on a team that has had a chance to recover.|
S~He felt the energy of it, too. I am glad somebody was cheering.
''')
add('fortree_guide_advice', 'FortreeCity_Gym_Text_GymGuideAdvice',
    'The guide introduces Winona Flying team and rotating doors.', '''
M~She waits behind rotating doors. A surprisingly complicated way to discourage drafty visitors.|
N~We know her specialty. The doors are a spatial problem, not a test of our Pokemon.|
N~Watch where each door sends us. We can work through it without rushing.|
N~I would rather take a little longer than pretend I know where I am going.|
N~Let us keep track of the way back in case the team needs a break.|
M~The leader awaits behind a moving set. A very committed entrance design.|
M~Trying to take wing. I am still trying to take the correct hallway.|
S~Rotating barriers! I want to see how the pivot clearance works. After we find the route.|
N~The door moves. The destination stays where it is.|
N~I am prepared for the Flying team. The building has been less forthcoming.|
N~We should look at the door positions before changing them. It will make the path easier to remember.
''')
add('fortree_guide_victory', 'FortreeCity_Gym_Text_GymGuidePostVictory',
    'The guide celebrates the win as achieving liftoff.', '''
M~Liftoff! I hope this does not mean the stairs are now optional.|
S~He has found a concise way to celebrate a difficult result.|
S~We did it. Let us give the team a rest before going anywhere.|
S~I still feel very much on the floor, but a little lighter.|
S~A good flight deserves a safe landing and something to eat.|
M~A triumphant launch, followed by the less celebrated task of finding the exit.|
M~We have achieved liftoff. My feet have chosen to remain professionally skeptical.|
S~A successful ascent through both the team and the door mechanism.|
S~Sometimes a victory is simply feeling able to go a little further.|
S~We can enjoy the height without immediately looking for a higher one.|
S~That is a fine moment to remember before the next part of the road.
''')
add('mossdeep_guide_advice', 'MossdeepCity_Gym_Text_GymGuideAdvice',
    'The guide warns about Psychic matchups and the twins coordinated double attacks.', '''
N~Two leaders with a shared plan. We should bring something more organized than two separate ideas.|
N~Avoid the unfavorable matchups and consider how our two Pokemon support each other.|
N~Pick a pair that works together. Individual strength is only part of this fight.|
N~It helps to know who is watching which part when everything happens at once.|
N~The team should feel like partners, not two strangers we put in the same room.|
N~A double act requires more than two performers arriving at the same address.|
M~Outstanding combinations. I hope ours include a plan and the ability to remember it.|
N~Check the interactions between our moves before discovering them during the battle.|
N~Two lives can make a third kind of strength when they move together.|
N~Coordination makes a pair look effortless. It is usually the part someone practiced hardest.|
N~I will watch for the moments one Pokemon makes room for the other.
''')
add('mossdeep_guide_victory', 'MossdeepCity_Gym_Text_GymGuidePostVictory',
    'The guide calls us an astounding trainer after beating the twins.', '''
S~Astounding! We should tell the team before the compliment develops a queue.|
S~That was good coordination. Everyone involved deserves the credit.|
S~You led them well. Make sure they know you noticed their work.|
F~I am glad he said it. You should hear something kind after working that hard.|
S~A good trainer and a good team. We should celebrate both.|
S~A glowing review with the ensemble credit left for us to supply.|
F~Accept it. I will stand here making being praised look only slightly awkward.|
S~The pair worked as intended. Better, in a few moments. Worth reviewing later.|
S~The trust held through the difficult part. That is worth a quiet smile.|
S~Enjoy the compliment before deciding what to improve next.|
S~He watched enough battles here to know a good one. I would let that mean something.
''')
add('petalburg_guide_advice', 'PetalburgCity_Gym_Text_GymGuideAdvice',
    'The guide explains Speed and Accuracy rooms and asks us not to attack him.', '''
M~He is not a trainer! The guide would like that distinction remembered before any attacks begin.|
N~The room names describe their tests. We can use that information to choose a route.|
N~Read the door, check the team, then choose. And leave the guide out of it.|
F~I hope somebody did not make him learn that warning the hard way.|
N~We can take the rooms one at a time. The team does not need every challenge at once.|
M~Our adviser has carefully excluded himself from the building's otherwise comprehensive battle policy.|
M~A man who has seen enough challengers to clarify he is not a door obstacle.|
N~Clearly labeled test conditions. I approve of that part of the design.|
N~A name on a door can tell us how to prepare for what waits behind it.|
N~I appreciate instructions with an actual choice at the end.|
N~We should remember where the routes divide. It makes the whole place less intimidating.
''')
add('petalburg_guide_victory', 'PetalburgCity_Gym_Text_GymGuidePostVictory',
    'The guide is astonished that the player beat their father.', '''
S~We defeated Dad. I hope this does not make dinner seating competitive.|
S~A significant result, especially with someone who knows your habits so well.|
S~You earned the win. It can matter as a battle and as something personal.|
N~How are you feeling? We do not have to match his excitement immediately.|
S~I hope you and your father get a quieter moment together after the cheering.|
S~The family story has acquired a new chapter, witnessed by a very enthusiastic man.|
S~You can be proud without having the entire room explain what this means for you.|
S~A familiar opponent can still be a difficult test. That was well handled.|
S~The child came back with a road of their own behind them.|
S~A big moment deserves whatever feeling is actually yours, not just the expected one.|
S~I would ask what you want to remember from it before I choose a picture.
''')
add('sootopolis_guide_advice', 'SootopolisCity_Gym_1F_Text_GymGuideAdvice',
    'The guide admits he knows only Juan Water specialty and the icy floor obstacle.', '''
M~He has run out of advice. A rare and precious announcement from an adviser.|
N~He separated what he knows from what he does not. I appreciate the honesty.|
N~Water team, ice puzzle. Enough to start paying attention, not enough to rush.|
N~I am glad he did not invent the rest to sound helpful.|
N~We can take a moment to look at the floor ourselves.|
M~The guide has reached the edge of his script and gracefully handed us the next scene.|
M~A professional who admits his limits. I almost want to frame the conversation.|
N~Then we observe the floor before moving. No need to replace missing information with guesses.|
N~He can point to the ice. We must learn how it holds our steps.|
N~An honest limit is much more useful than confident nonsense.|
N~I would rather look closely at what is here than arrive with the wrong story about it.
''')
add('sootopolis_guide_victory', 'SootopolisCity_Gym_1F_Text_GymGuidePostVictory',
    'The guide celebrates beating Juan and directs badge-complete trainers toward the League.', '''
S~Check the card. A whole journey has somehow fitted into eight very small spaces.|
S~We should verify the badges before setting out for the League. Then prepare the whole team.|
N~One important win. The League is another challenge, and we can take time before it.|
S~Seeing all those badges together might feel different from earning the last one.|
N~We should rest, stock up, and let the team enjoy getting this far.|
S~The local finale has opened the door to a much larger final act.|
S~We can be almost there without pretending the road so far was small.|
N~Milestones verified, next objective identified. Now comes the less glamorous supply check.|
S~Eight small signs of all the places that changed us.|
S~I hope you look at the card before hurrying to the next thing you have to prove.|
S~I want to remember this team before the League, exactly as it is now.
''')

add('sootopolis_andrea_cracked_ice', 'SootopolisCity_Gym_B1F_Text_AndreaPostBattle',
    'Andrea invites us to see what happens when all ice tiles are cracked.', '''
M~That sounded like advice from someone standing safely on the lower floor.|
N~She is inviting an experiment. We should first consider where the floor would send us.|
N~Look at the whole path before stepping. Falling is not the only way to learn.|
N~I would rather understand the pattern before the room makes a loud point about it.|
N~Let us keep everyone steady and take this slowly.|
M~A tempting invitation to let the building deliver its punchline.|
M~The floor has already made its feelings about repeat visitors rather clear.|
N~Each tile changes state. We need a route that accounts for the entire sequence.|
N~The ice remembers each footstep. We should remember them, too.|
N~I prefer a plan to a surprise appointment with the basement.|
N~I am looking at the spaces between our steps as much as the next tile.
''')
add('sootopolis_crissy_survive_hit', 'SootopolisCity_Gym_B1F_Text_CrissyPostBattle',
    'Crissy says we may be strong enough not to lose to Juan in one hit.', '''
M~We have been promoted from doomed to possibly upright. Wonderful progress.|
N~That is a warning about his power, however faintly the compliment is phrased.|
N~We will prepare properly instead of settling for surviving the first hit.|
F~I think that was encouragement. It had a very small opening to escape through.|
N~Let us make sure the team is rested before testing her estimate.|
M~A glowing forecast of perhaps reaching the second line of dialogue.|
M~A compliment delivered wearing protective gloves.|
N~Surviving one hit is a threshold, not a complete battle plan.|
N~The first wave is only the beginning of the water.|
M~I have received kinder reviews from an ill-fitting mirror.|
N~I would like to know what makes his first attack so dangerous, not merely hear that it is.
''')
add('sootopolis_daphne_grace', 'SootopolisCity_Gym_B1F_Text_DaphnePostBattle',
    'Daphne praises our grace in battle and feels fortunate to have found Pokemon.', '''
S~We made someone glad Pokemon exist. That is a rather large compliment for one battle.|
S~She saw something she values in how we battled. I am glad the loss did not hide it.|
S~A strong battle can still be respectful. She noticed.|
S~It is lovely when watching someone else reminds you why you began.|
S~The team helped make that moment. I hope they feel our pride.|
S~An opponent left the scene more in love with the whole enterprise. A wonderful review.|
F~That is so kind I have temporarily forgotten how to stand normally.|
S~Good execution can be satisfying even to the person testing it.|
S~She found beauty in a difficult moment. That is a gift of its own.|
S~Grace is a lovely thing to be noticed for, especially here.|
S~I would like to remember her smile as well as the winning move.
''')
add('sootopolis_connie_ice_rule', 'SootopolisCity_Gym_B1F_Text_ConniePostBattle',
    'Connie explains we must walk on each ice tile once to reach Juan.', '''
N~Each tile once. Finally, a floor with a clear visiting policy.|
N~A route that covers every tile without revisiting one. We should plan before moving.|
N~Good rule to know. Now look at the entire pattern, not just the first few steps.|
N~I want to trace it quietly before my feet have an opinion.|
N~We can take a moment here. Nobody needs to hurry onto cracking ice.|
M~The set requires every square to receive exactly one performance.|
M~Even the floor is enforcing social limits. One visit per tile.|
N~We need a complete path, not a series of locally convenient choices.|
N~Every place asks to be touched once, and then left behind.|
N~Knowing the rule makes the puzzle much less personal.|
N~I am checking the corners first. They may determine how the rest of the route fits.
''')
add('sootopolis_bridget_travel', 'SootopolisCity_Gym_B1F_Text_BridgetPostBattle',
    'Bridget says travelling to train elsewhere would be stronger and more fun than staying in a strong Gym.', '''
S~A strong address does not automatically make you strong. Travel does provide better snacks.|
S~A familiar environment can stop testing your assumptions. New opponents help.|
S~She should try it when she is ready. There is more than one place to get stronger.|
S~Wanting to enjoy the road is enough of a reason to see it.|
S~I hope she finds good company as well as good battles.|
S~A supporting character has noticed the road continues past her assigned room.|
S~She is allowed to leave somewhere impressive for somewhere she actually wants to be.|
N~A different environment supplies tests this Gym cannot. Useful, and apparently more appealing.|
S~A sheltered place can still have an open door.|
S~Fun belongs in the plan. It does not make the plan less serious.|
S~I would love to run into her somewhere she chose for herself.
''')
add('sootopolis_olivia_invitation', 'SootopolisCity_Gym_B1F_Text_OliviaPostBattle',
    'Olivia sees potential and invites us to stay and train at Juan Gym.', '''
F~A job offer? I am not ready to become a permanent feature of this basement.|
S~She thinks we could learn here. It is a kind offer, not an obligation.|
N~Good to know we would be welcome. The road is still calling us, though.|
S~Being invited to stay feels different from being told to prove we belong.|
S~I like knowing there are places that would make room for us.|
M~Our guest appearance has become an invitation to join the resident cast.|
F~I am touched. I have also grown attached to visiting places with warmer floors.|
N~There would be useful things to learn here. There are useful things ahead, too.|
S~A door opened into a possible life. We can appreciate it without walking through.|
S~She made that offer after seeing us at our best. It sounds sincere.|
S~Maybe we will return for a quieter visit when the next destination is not pulling so hard.
''')
add('sootopolis_tiffany_age', 'SootopolisCity_Gym_B1F_Text_TiffanyPostBattle',
    'Tiffany says trainer strength has nothing to do with age.', '''
M~Excellent. I can stop training my birthday and focus on the Pokemon.|
N~Age alone tells us little about preparation, judgment, or the team's particular strengths.|
S~The work matters more than when you were born.|
S~I like being taken seriously without having to become older first.|
N~Different people learn at different times. They still deserve patience.|
M~The calendar has been dismissed from the judging panel.|
M~A welcome policy. I would hate to lose to someone on a clerical technicality.|
N~Review performance, not a convenient proxy for it. Sensible.|
N~A young branch and an old root can both hold their own kind of strength.|
S~It should be obvious. It is still nice when someone actually says it.|
N~I would rather hear about a person's choices than make a story out of their age.
''')
add('sootopolis_bethany_mistakes', 'SootopolisCity_Gym_B1F_Text_BethanyPostBattle',
    'Bethany wishes she could move past lost causes faster than she can say Oops.', '''
S~My Oops has usually finished before my brain has even found the problem.|
N~Recognizing that a plan is failing is a skill. Changing it promptly takes practice.|
N~You can stop a bad plan without turning it into a judgment on yourself.|
S~I know that feeling. My head likes to replay the part I already cannot fix.|
N~A little kindness makes it easier to start the next thing.|
M~She would like her inner editor to work before the entire scene has collapsed.|
S~If she discovers how, I would like to join the waiting list.|
N~Set a point for reevaluating the plan before committing more resources to it.|
N~Some things are ready to be set down before our hands are ready to open.|
S~Moving on quickly is not the only way to move on properly.|
N~I hope she remembers the attempts that taught her something, too.
''')
add('sootopolis_annika_juan_praise', 'SootopolisCity_Gym_B1F_Text_AnnikaPostBattle',
    'Annika joined because Juan praised her Pokemon and wishes she had met him when younger.', '''
S~One kind remark changed where she wanted to be. That is quite a powerful move.|
S~Feeling recognized can give an old interest a new direction. It is not too late for that.|
N~She is here now. Those years still have something to offer.|
S~I hope she gets to enjoy being seen now, instead of only mourning earlier chances.|
S~Her Pokemon have her, and she has found people who appreciate them. That matters today.|
S~A small compliment became the opening of a much longer chapter.|
N~She did not miss the only version of her life worth having.|
N~The invitation happened now. There are still things she can build from it.|
S~A late-blooming flower still belongs in the garden.|
S~I hope he knows how much that kindness meant to her.|
S~I would ask about her Pokemon first. That seems to be where the happy part began.
''')
add('sootopolis_brianna_dismissal', 'SootopolisCity_Gym_B1F_Text_BriannaPostBattle',
    'Brianna insists we could not touch Juan despite losing to us.', '''
M~She has promoted our next opponent to a completely untested level of untouchable.|
N~We can take Juan seriously without accepting her forecast as evidence.|
N~We will find out in the battle. No need to win this argument first.|
N~I would rather let the team answer when we get there.|
N~Let us prepare carefully instead of letting that push us into rushing.|
M~The defeated preview insists the main attraction cannot possibly be reviewed.|
M~She sounds certain. Fortunately, certainty does not take a turn in battle.|
N~A claim about another opponent needs a separate test. We are on our way to one.|
N~Her laughter is not a wall. We can keep walking.|
M~I will save my response until we have something more useful than a prediction.|
N~I wonder what she will say when we return. No need to decide it for her yet.
''')
add('sootopolis_water_pulse_lesson', 'SootopolisCity_Gym_1F_Text_ExplainWaterPulse',
    'Juan explains Water Pulse can confuse with ultrasonic waves.', '''
U~Water that makes your thoughts wobble. I had assumed that was just the bath being too hot.|
N~The confusion is a possible added effect, not something to count on every time.|
N~Use it for the attack we can plan around. Treat confusion as a bonus.|
N~It sounds gentle until you imagine being on the other side of it.|
N~We should see which teammate can use it comfortably before teaching it.|
M~A graceful wave with a distinctly ungraceful effect on the opponent's train of thought.|
M~I prefer my confusion self-generated. More predictable supply.|
N~An attack with a secondary disruption effect. We should not build the entire plan on chance.|
N~Still-looking water can carry something we cannot hear.|
N~He made the extra effect clear without promising it would happen every time.|
N~There is more going on in that move than the visible splash.
''')
add('sootopolis_juan_league_direction', 'SootopolisCity_Gym_1F_Text_JuanPostBattle',
    'Juan directs trainers with all Hoenn badges east to the League on Ever Grande.', '''
S~Ever Grande. A destination with a name that has very high expectations of itself.|
N~The eastern island is our next major destination. We should prepare before leaving.|
N~Check the route and supplies. Getting there is part of the challenge.|
S~We have talked about the League so long it feels strange to have actual directions.|
N~Let us rest the team before setting off for something this important.|
S~The final destination has acquired a place on the map instead of living only in our speeches.|
S~A big name for a real place we are finally allowed to approach.|
N~Destination identified. Now we need a route and a realistic supply plan.|
S~A far island has become the next step rather than the edge of a dream.|
S~We have earned the invitation. We can still take the time to arrive ready.|
S~I want to remember the team before the crossing, not only after the League.
''')
add('sootopolis_juan_coat_assumptions', 'SootopolisCity_Gym_1F_Text_JuanPostRematch',
    'Juan imagines us refusing apprenticeship and his coat, then praises that imagined refusal.', '''
U~He offered a coat, refused it for us, and complimented our answer. I barely had time to want it.|
M~He has constructed a complete exchange without collecting any actual responses.|
M~Generous of him to handle both sides. We appear to have passed.|
F~I might have wanted to see the coat. The conversation moved on without me.|
S~He seems pleased with us. I hope he knows an offer can wait for an answer.|
M~A flawless two-person scene, performed entirely by its most enthusiastic participant.|
M~I enjoy a conversation that lets me contribute absolutely nothing and calls it nobility.|
M~The response was assumed before the offer was tested. Efficient, but not informative.|
M~He has dressed us in an imagined virtue and kept the actual coat.|
U~I would at least like to inspect the coat before my imaginary refusal becomes official.|
M~He looked so pleased with the exchange. I wonder which version of us he was speaking to.
''')

add('dewford_brawly_deep_battling', 'DewfordTown_Gym_Text_BrawlyPostRematch',
    'Brawly compares the depth of battling with the Hoenn sea.', '''
S~A very deep subject. I am glad the lessons do not all require holding my breath.|
S~Every answer can expose another question. That is part of what keeps study interesting.|
N~There is more to learn. That does not make what we did today small.|
S~I like a familiar thing that can still surprise you after years.|
S~Deep enough to keep learning, wide enough to share with someone.|
S~The sea metaphor has outlasted the match and found a promising second career.|
S~A subject with no bottom. Finally, a respectable home for my overthinking.|
N~A simple set of rules can produce an enormous range of interactions.|
S~We need not reach the bottom to learn how to swim.|
N~I hope he enjoys what he already knows while chasing the next discovery.|
S~I would ask which recent battle surprised him. Even the teacher still has those.
''')
add('dewford_brawly_rematch_pair', 'DewfordTown_Gym_Text_BrawlyRematchNeedTwoMons',
    'Brawly welcomes our return but requires two battle-ready Pokemon for the rematch.', '''
M~The giant wave has returned with a rather small crew. Back to the party list.|
N~He needs two battle-ready Pokemon. We should check health as well as the count.|
N~We need another partner ready to fight. Let us sort that out first.|
F~His welcome was so enthusiastic I briefly forgot we had missed a requirement.|
N~We can return when both teammates are comfortable and ready.|
M~A stirring welcome, followed by the less stirring attendance check.|
M~The wave brought one Pokemon and a disappointing amount of paperwork.|
N~The proposed double battle has one missing participant. Straightforward correction.|
N~Even a returning wave needs enough water to reach the shore.|
N~He is still pleased to see us. We just need to bring the right team.|
S~A warm welcome can survive a second attempt. We will come back prepared.
''')
add('mauville_wattson_recharge', 'MauvilleCity_Gym_Text_WattsonPostRematch',
    'Wattson says his team will recharge and welcomes another future challenge.', '''
S~Recharging after a battle. I recommend a chair, a snack, and absolutely no wall socket.|
S~Recovery is part of preparation. He sounds happy to make room for it.|
S~Rest the team, then try again. A good plan for both sides.|
S~I like leaving with the feeling we would be welcome back.|
S~Their batteries deserve a proper break. So do ours.|
S~An enthusiastic host announces the interval and immediately books the next performance.|
S~He made resting sound like part of being strong. Good.|
S~A cooling period before another run. Sensible operating procedure.|
S~Even bright things need a quiet place to gather themselves.|
S~I like an invitation that gives everyone time to recover first.|
S~I hope he is still laughing when we return. It makes this place feel like his.
''')
add('mauville_wattson_rematch_pair', 'MauvilleCity_Gym_Text_WattsonRematchNeedTwoMons',
    'Wattson realizes we have only one usable Pokemon and asks for at least two.', '''
M~He knew what we wanted. Unfortunately, neither of us counted what we brought.|
N~One usable Pokemon is not enough for this format. Check the rest of the party.|
N~We will come back with a proper pair. There is no need to rush it.|
F~The laughter made the mistake feel less terrible. I appreciate that.|
N~Let us heal anyone who needs it before looking for a second teammate.|
M~The joyful reunion has encountered a small casting problem.|
M~I can supply a second opinion. Apparently that does not count.|
N~Two active participants required. We should verify before the next attempt.|
N~The spark is here. We still need another place for it to go.|
S~He managed to correct us without making the whole welcome disappear.|
N~A simple fix. He clearly still wants the battle when we are ready.
''')
add('lavaridge_keegan_warning', 'LavaridgeTown_Gym_B1F_Text_KeeganPostBattle',
    'Keegan acknowledges our skill but warns of serious burns against Flannery.', '''
N~A compliment and a burn warning. This Gym has a very consistent welcome package.|
N~He recognizes our skill without dismissing her strength. We should do the same.|
N~Take the warning seriously. Prepare the team before moving on.|
N~I am glad he said we did well before describing the frightening part.|
N~We have time to heal. No badge is worth treating the team carelessly.|
N~Our good review comes with a strongly worded preview of the main attraction.|
M~I would enjoy being complimented more in a room with fewer promised burns.|
N~Known hazard, strong opponent. Check the countermeasures.|
N~A flame deserves care even when we believe we can pass it.|
N~We can respect her power without letting the warning hurry us.|
N~He trains here. It is worth listening when he stops boasting and gives a real warning.
''')
add('lavaridge_jace_spirit', 'LavaridgeTown_Gym_B1F_Text_JacePostBattle',
    'Jace says our battling spirit may give us a chance against Flannery.', '''
S~Our spirit is burning. I hope it is the approved metaphorical kind.|
S~Determination helps when it supports careful decisions. We should bring both.|
N~A chance is enough. We will prepare and make the most of it.|
S~It is nice to hear that he saw more than the last attack.|
N~The team has the heart for it. Let us make sure they have the health, too.|
S~An early review has identified a promising spark in the visiting cast.|
S~I can handle a quiet kind of fire. It lasts surprisingly well.|
N~Motivation is available. Next check: resources and matchups.|
S~A small flame can travel far when someone tends it.|
S~He sounds like he wants us to give her a good challenge.|
S~I wonder whether Flannery will recognize the same thing when she sees us.
''')
add('lavaridge_eli_flannery_fan', 'LavaridgeTown_Gym_B1F_Text_EliPostBattle',
    'Eli stays in the Gym because he admires Flannery power.', '''
M~A fan who has chosen the hottest possible seat in the house.|
N~Admiration can be a reason to learn here. I hope he studies the methods as well as the results.|
N~If he wants to train with her, he should take the work seriously.|
N~It is good to be inspired. I hope he finds his own reasons to stay, too.|
S~He seems happy to be here. I hope the team enjoys the training as much.|
M~A devoted audience member has become a permanent part of the venue.|
M~Some fans send letters. This one has committed to the entire thermal environment.|
N~An impressive result should make him curious about how she produced it.|
N~A strong flame can draw people near. They still need a path of their own.|
N~Admiration is fine. She should get to be a person on an ordinary day, too.|
N~I would ask what he has learned from watching her, beyond how strong she is.
''')
add('lavaridge_flannery_happy_rematch', 'LavaridgeTown_Gym_1F_Text_FlanneryPostRematch',
    'Flannery says she enjoyed the heated rematch despite losing and wants another.', '''
S~She lost and had a wonderful time. The team should invoice us for entertainment.|
S~A satisfying challenge can be valuable to both sides, regardless of the result.|
S~Good fight, no hard feelings. I would come back for that.|
S~I like how much more like herself she sounds when she is enjoying the battle.|
S~I hope she and her team get a good rest with that happy feeling.|
S~The opponent has requested an encore before the applause has settled.|
S~She does not need to win to feel she belongs here. That is nice to hear.|
S~A useful test and an enjoyable one. Hard to improve on that combination.|
S~The flame burned brightly without leaving bitterness behind.|
S~She sounds comfortable in her own enthusiasm now. It suits her.|
S~I would like to remember that smile when we think back on this Gym.
''')
add('lavaridge_flannery_rematch_pair', 'LavaridgeTown_Gym_1F_Text_FlanneryRematchNeedTwoMons',
    'Flannery enthusiastically proposes a double rematch then notices only one Pokemon is ready.', '''
M~We brought half a battle to a full-sized welcome.|
N~Her enthusiasm does not change the format. We need two healthy participants.|
N~Another ready teammate first. She will still be here when we return.|
F~She was so excited. I feel bad that our party list interrupted.|
N~Let us take care of whoever cannot battle before trying again.|
M~The fire of anticipation has been briefly contained by a head count.|
M~I have enthusiasm and no battle moves. Apparently a fatal combination for volunteering.|
N~The minimum operating team is two. We currently have one.|
N~A warm invitation can wait while we gather the rest of the team.|
N~She sounds disappointed about the delay, not about us. That helps.|
S~We can give her the rematch she wants once our team is ready for it.
''')
add('fortree_winona_rematch_pair', 'FortreeCity_Gym_Text_WinonaRematchNeedTwoMons',
    'Winona gives a soaring welcome before noticing the double battle needs another Pokemon.', '''
M~Our full flight has been delayed by a missing wing on the team list.|
N~An inspiring speech, but a double battle still requires two usable Pokemon.|
N~We will return with a pair. Let us check the team first.|
F~I was almost moved enough to forget that we came unprepared.|
N~No one needs to carry both sides. We can come back with proper support.|
M~A grand ascent brought briefly to earth by the attendance record.|
M~Gravity won this round without even entering a Pokemon.|
N~The design calls for two participants. We should meet that requirement before testing it.|
N~Even a high ambition needs something beside it to hold steady.|
N~I like the welcome. Next time we should give it a complete team to greet.|
N~She still wants to see us battle. We have simply arrived a little early for our own party.
''')
add('sootopolis_juan_rematch_pair', 'SootopolisCity_Gym_1F_Text_JuanRematchNeedTwoMons',
    'Juan welcomes us as a typhoon then asks us to bring two Pokemon for the double rematch.', '''
M~The young typhoon has arrived understaffed. We will reschedule the weather.|
N~Two Pokemon ready to battle. We should confirm both before returning.|
N~Another teammate first. There is no prize for arriving with half a plan.|
F~I had barely adjusted to being called a typhoon before the attendance problem appeared.|
N~Let us check who needs healing. Then choose the pair together.|
M~Our dance has been postponed until both partners are actually present.|
M~I am relieved. Being a whole weather event sounded tiring.|
N~An enthusiastic invitation, but the input requirement remains unsatisfied.|
N~The tide can wait for the rest of the water.|
N~A pair that works well together will be worth the second trip.|
S~We should return properly prepared. He clearly enjoys having a challenger to welcome.
''')
add('petalburg_norman_rematch_pair', 'PetalburgCity_Gym_Text_NormanRematchNeedTwoMons',
    'Norman explains parent and child fight fairly but requires two usable Pokemon.', '''
M~Family privileges do not include skipping the second Pokemon. Good to know.|
N~He is keeping the same requirements for you as for any challenger. That is fair.|
N~We need a second teammate ready. He is not refusing you as a person.|
N~I think he wants this to be a real challenge for both of you.|
N~Let us care for the team first. An important battle deserves everyone ready.|
M~A solemn statement of family sporting ethics has met a very practical head count.|
M~We have been defeated by Dad's administrative formality. Briefly.|
N~The rules are clear and consistent. We can correct the party before returning.|
N~He has made a fair place to meet you. We still need to bring the full team.|
N~He is taking you seriously. That includes expecting you to arrive prepared.|
N~I would rather give him the battle he is asking for than hurry into a smaller one.
''')

add('petalburg_norman_four_badges', 'PetalburgCity_Gym_Text_NormanGoToRustboro',
    'Norman sends the inexperienced player to Rustboro and requires four badges before battling.', '''
N~Four badges before battling Dad. Family access has a surprisingly formal application process.|
N~He has set a clear threshold. Rustboro gives us a practical first step toward it.|
N~We have a destination and a goal. His wording does not decide how far you can go.|
N~Being told you are not ready by your father can sting. We can still begin.|
N~Let us learn at a pace that is good for the team, not only to prove him wrong.|
N~A father has placed the first chapter between himself and the inevitable family rematch.|
N~We can earn those badges for ourselves. They do not need to become an argument.|
N~A measurable requirement and a starting location. Now we need a training plan.|
N~The door is not closed forever. There is a road attached to its condition.|
N~I would have preferred a warmer send-off. We can still make the journey our own.|
N~I wonder what he will notice first when you come back with those badges.
''')
add('petalburg_norman_dewford_next', 'PetalburgCity_Gym_Text_NormanGoToDewford',
    'After the Rustboro win Norman directs the player across the sea to Brawly.', '''
M~One badge earned. Dad has responded by expanding the homework across an entire sea.|
N~A different specialty will test more than repeating the same successful matchup.|
N~New opponent, new plan. Check the route before we set out.|
N~I hope you get a moment to enjoy this win before it becomes only the thing before the next one.|
N~We should rest the team and prepare for the crossing. They earned that first badge, too.|
M~The successful first chapter has been returned with a note requesting a maritime sequel.|
N~His next suggestion can be useful without making your first win less worth celebrating.|
N~Brawly presents a different test. We should not assume the Rustboro approach transfers unchanged.|
N~The road has become water. It is still one step after the one we already took.|
N~A practical destination. I would have liked a little more congratulations with it.|
N~We can remember the first win properly even while looking toward Dewford.
''')
add('petalburg_norman_notices_progress', 'PetalburgCity_Gym_Text_YouHaveGottenStronger',
    'Norman acknowledges the player growing strength from their earned badges.', '''
S~He noticed! The badges have successfully carried the message past the Dad defenses.|
S~The badges are visible evidence of your progress. The work behind them is yours.|
S~You have put in the effort. It is good to hear him recognize it.|
S~That sounded small, but I can imagine wanting to hear it for quite a while.|
S~I hope the team hears that praise, too. They have grown beside you.|
S~A reserved review from someone whose approval has rather more weight than usual.|
S~You do not have to pretend that hearing it means nothing.|
S~He has recognized the changed result. I hope he gets to see the improved methods soon.|
S~A familiar voice has noticed the distance in your steps.|
S~He could say more. What he said still belongs to you.|
S~I would remember that little pause before he admitted how far you have come.
''')

