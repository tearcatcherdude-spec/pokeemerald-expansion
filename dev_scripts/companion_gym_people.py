"""Source-reviewed Gym conversations; each row follows a distinct final message."""
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

add('rustboro_josh_rock_power', 'RustboroCity_Gym_Text_JoshPostBattle',
    'Josh insists the player has not seen the terrifying power of Rock Pokemon after losing.', '''
M~He is saving the terrifying part for later. Very considerate of him.|
N~We have seen one result. He is correct that it does not describe every Rock Pokemon.|
M~He can defend his team without pretending that battle did not happen.|
S~Maybe we frightened the terrifying rocks a little.|
S~He still believes in his team. I like that more than the threat.|
M~The rocks have requested a more flattering first impression.|
M~Terrifying power. Currently taking a short break on the floor.|
N~A failed demonstration is still useful information. Someone should tell him.|
S~Even a fallen stone has weight. He need not shout on its behalf.|
M~He is committed to the Rock brand through a difficult review.|
S~I wonder whether he encourages his Pokemon this loudly when nobody is watching.
''')
add('rustboro_tommy_roxanne_warning', 'RustboroCity_Gym_Text_TommyPostBattle',
    'Tommy warns that Roxanne is several times stronger than him.', '''
U~Several Tommys of strength. I hope she does not also have several Tommys of elbows.|
N~A useful warning, although he has not supplied a unit for strength.|
N~Good. We will check the team before going further.|
N~He sounds less interested in boasting now. I can listen to that.|
N~We have time to heal. There is no prize for arriving hurt.|
M~An unusually honest introduction to the person who signs his paychecks.|
M~Several times stronger. I admire a warning with room for uncertainty.|
N~Then this was a test run. We should use what it taught us.|
N~He is sending us onward with a warning rather than resentment.|
S~That is more useful than claiming he nearly won.|
N~He knows her battles better than we do. Worth hearing him out.
''')
add('rustboro_marc_roxanne_choice', 'RustboroCity_Gym_Text_MarcPostBattle',
    'Marc admires Roxanne for choosing Rock Pokemon at a young age.', '''
S~She found her calling early. I spent that age deciding which pocket was for crumbs.|
N~Choosing a specialty matters less than continuing to study it. Roxanne appears to do both.|
N~She earned his respect. That says more than her age does.|
S~It is nice when someone takes a young person's interest seriously.|
S~Having people believe in your choice helps you grow into it.|
M~A firm career foundation. I am being very brave about the obvious pun.|
S~He sounds proud of her. That survived losing to us.|
N~A clear specialty gives her room to investigate the details.|
N~Some people find their stone early. Others carry several before one fits.|
S~Knowing your taste that young is impressive. Keeping it yours is harder.|
S~I would rather hear him tell her that than tell every visitor.
''')
add('rustboro_rock_tomb_explained', 'RustboroCity_Gym_Text_ExplainRockTomb',
    'Roxanne gives Rock Tomb and explains its slowing effect and single-use TM.', '''
U~A rock falls on you and you become slower. Finally, science I can follow.|
N~Damage and reduced Speed together can change who acts first next turn. A useful combination.|
N~One use. We should choose the Pokemon before opening it.|
N~A slower opponent gives our team a little more breathing room.|
N~Let us see who can learn it before deciding. A gift deserves some thought.|
M~An educational prize with a surprisingly literal lesson in falling behind.|
M~It teaches patience by dropping a rock on the impatient.|
N~A single-use teaching device. I have several questions about the business model.|
N~The stone leaves a consequence after the first impact. That is worth remembering.|
N~She explained the catch before we used it. I appreciate that.|
S~She is still teaching after the battle. That seems to be the part she enjoys most.
''')
add('rustboro_roxanne_keep_learning', 'RustboroCity_Gym_Text_RoxannePostBattle',
    'Roxanne encourages the player to challenge other leaders and learn from trainers.', '''
S~Our reward for passing the lesson is more lessons. She really was a good student.|
S~A different opponent can expose an assumption this battle never tested.|
N~We can be proud of this win and still have work ahead.|
S~She makes leaving sound less like goodbye and more like being trusted.|
S~We will meet people worth knowing between the Gyms, too.|
S~She is sending her challenger into the sequel with excellent professional grace.|
S~She lost and immediately assigned us an education. I respect the recovery.|
N~Testing the same plan against different teams will show us where it fails.|
S~She wants the road to change us. I think it already has.|
S~A badge and permission to keep figuring ourselves out. A decent afternoon.|
S~We should remember the trainers who helped us get here, not only the leaders.
''')
add('rustboro_roxanne_rematch_learning', 'RustboroCity_Gym_Text_RoxannePostRematch',
    'After the rematch Roxanne says having more to learn makes her love battling.', '''
S~Losing gave her more homework, and she is delighted. An extraordinary species of student.|
S~Finding a gap in what you know can be exciting when it is safe to admit it.|
S~She wants another chance to improve. I like battling someone who means that.|
S~It is easier to keep practicing when mistakes are allowed to belong there.|
S~She sounds happy with the work ahead. I hope her team gets a rest first.|
S~The defeat has become an opening chapter. She is quick with revisions.|
S~She found something to love about losing. I am still working on tolerating it.|
S~A result that challenges your model is the interesting result. I understand her.|
S~The mountain grew taller, and she smiled at it.|
S~She does not need to pretend she won to feel good about being here.|
S~That is the expression I would want to remember from a rematch.
''')
add('rustboro_roxanne_two_required', 'RustboroCity_Gym_Text_RoxanneRematchNeedTwoMons',
    'Roxanne refuses the double rematch because the player has only one Pokemon.', '''
M~We have brought a soloist to a duet. A bold administrative choice.|
N~A double battle requires two eligible partners. We should check the party.|
N~We need another teammate. No reason to make one Pokemon do two jobs.|
F~I counted us as a pair for a second. That is apparently not how this works.|
N~Let us bring a second Pokemon and make sure both are ready.|
M~Our dramatic entrance was defeated by the attendance sheet.|
M~I am flattered, but I will not fit inside your second Poke Ball.|
N~One missing component. Easily fixed before we attempt the whole system.|
N~There is an empty place beside our Pokemon. Let us fill it kindly.|
M~We coordinated our arrival better than our team list.|
N~We can come back. She is asking for a fair battle, not sending us away for good.
''')
add('dewford_takao_technique', 'DewfordTown_Gym_Text_TakaoPostBattle',
    'Takao compliments the technique that overcame his strength.', '''
M~Technique wins! My technique is standing safely behind you. Unbeaten so far.|
S~He noticed how we won instead of dismissing it as luck.|
S~A clean compliment after a hard fight. He handled that well.|
S~It feels good to have the work recognized, not just the result.|
S~Our Pokemon worked for that compliment. They should get to hear it.|
S~An opponent gracious enough to review the choreography after being hit by it.|
S~He has a strong grip on losing gracefully.|
N~Power needs a way to reach its target. He is already thinking about the next adjustment.|
S~Strength listened, and learned another language.|
S~That sounded earned. You can accept it without shrinking it.|
S~He was watching carefully even while losing. That makes a good rival.
''')
add('dewford_jocelyn_champion_ambition', 'DewfordTown_Gym_Text_JocelynPostBattle',
    'Jocelyn upgrades her goal from Gym Leader to Champion while discussing her loss.', '''
U~We beat her and accidentally promoted her ambitions. Is that a battle effect?|
S~She revised her goal upward remarkably quickly. I hope she gives herself time to reach it.|
S~Good ambition. She will need rest as well as resolve.|
S~She said the bigger dream before she could talk herself out of it.|
S~I like her spirit. I also hope someone makes sure she eats between training sessions.|
M~The Gym Leader draft was rejected for insufficient grandeur. Straight to Champion.|
S~One loss and she is applying for the top job. I respect the nerve.|
S~A useful failure can change the plan. Hers has acquired several extra milestones.|
S~She reached for a larger horizon while still catching her breath.|
S~That correction sounded like the dream she had been editing down for other people.|
S~Remember her name. It would be lovely to meet her again much further along.
''')
add('dewford_laura_dark_face', 'DewfordTown_Gym_Text_LauraPostBattle',
    'Laura trains her heart in darkness but complains she cannot see Brawly.', '''
M~The heart is getting stronger. The eyes have submitted a complaint.|
N~Darkness may test concentration. It also makes recognizing your instructor unnecessarily difficult.|
M~Learning your leader's face should not require winning enough battles to install lighting.|
F~I know that feeling. Wanting to look at someone, then being grateful nobody can see you.|
N~She can be brave and still ask for a lamp.|
M~Her mentor is a powerful influence and a largely hypothetical face.|
M~An excellent place to admire someone without making eye contact. Finally, a facility for me.|
N~We could solve the visibility problem without abandoning the entire training method.|
S~She wants courage and a glimpse of him. Two quite different kinds of light.|
M~All that dedication, and she could walk past him in daylight.|
S~I wonder whether he knows the darkness is making him this mysterious.
''')
add('dewford_lilith_sour_loss', 'DewfordTown_Gym_Text_LilithPostBattle',
    'Lilith wishes the player would get lost and return to the entrance.', '''
A~I was going to get lost for free. Now it would feel like doing her a favor.|
N~She is upset. That does not make her directions worth following.|
A~We won the battle. We do not owe her an argument afterward.|
D~I know losing hurts. I wish she had not tried to hand the hurt to us.|
N~Let us give her space and keep going.|
M~The defeated guardian has placed a small curse on our sense of direction.|
M~Bold of her to assume I needed help getting lost.|
A~I prefer a floor plan to hostile navigation advice.|
N~She can wish it. Our feet remain our own.|
A~That is a lot of effort to spend on someone who is already leaving.|
N~One bad response does not need to become the whole memory of this Gym.
''')
add('dewford_brenden_worthy', 'DewfordTown_Gym_Text_BrendenPostBattle',
    'Brenden says the player is worthy of seeing Brawly.', '''
M~Permission to meet the man at the back of the dark room. We are moving up in society.|
N~We passed his test. Brawly will present a different one.|
S~We earned our way through. Let us make sure the team is ready.|
S~Being told we belong here helps more than I expected.|
S~He gave us his approval. Our Pokemon deserve a little praise, too.|
M~The gatekeeper grants an audience. I shall try to walk with appropriate importance.|
M~Worthy of seeing him. The lighting may still have reservations.|
N~One checkpoint cleared. No need to rush the final preparation.|
S~A stranger opened a door with a few kind words.|
S~I like an opponent who can welcome you after trying to stop you.|
S~He sounds pleased to send a good challenger to his leader.
''')
add('dewford_cristian_badge_encouragement', 'DewfordTown_Gym_Text_CristianPostBattle',
    'Cristian acknowledges the win and urges the player to get the badge.', '''
S~Our former obstacle has become a cheerleader. Efficient use of staff.|
S~A clear result and a generous response. We can move forward.|
S~That is the right way to lose. Give the other team their due.|
S~It is nice to leave a battle with someone on our side.|
S~He is cheering for us now. Let us give the team a moment before the next fight.|
S~He has changed sides for the finale. A very welcome plot development.|
S~Short, kind, and no excuse. An unexpectedly difficult combination.|
N~He sees our next objective clearly. We should check our resources before attempting it.|
S~He did not keep the door closed just because he could not win.|
S~That is a compliment with no awkward little condition attached.|
S~I hope he gets to see the badge when we leave.
''')
add('dewford_bulk_up_lesson', 'DewfordTown_Gym_Text_ExplainBulkUp',
    'Brawly explains that Bulk Up raises both Attack and Defense.', '''
U~Stronger and tougher in one move. I have been trying two separate breakfasts.|
N~Improving offense and defense together can reward a turn spent preparing.|
N~Useful if we choose the moment well. Setting up still gives the opponent a turn.|
N~Sometimes taking a breath first changes how the rest of the fight feels.|
S~Strength with something to protect it. I like that pairing.|
M~A preparation montage compressed into one move. Very considerate of the audience.|
M~Becoming harder to hurt sounds like an excellent hobby.|
N~Two improvements from one action. The timing is the part we still have to solve.|
N~It builds a shelter and a way to step beyond it.|
M~I appreciate a workout that does not require buying a new outfit.|
N~We should see which teammate actually benefits before teaching it.
''')
add('dewford_brawly_talent_wave', 'DewfordTown_Gym_Text_BrawlyPostBattle',
    'Brawly predicts the player will become a giant wave of talent.', '''
U~A giant wave! Please remember I am travelling without a flotation device.|
S~That is quite a prediction. It need not become a deadline.|
S~He believes in you. Keep the confidence and leave room to grow.|
F~I never know where to look when someone gives a compliment that large.|
S~He sees a future for you. We can still take the next part one town at a time.|
M~The review is in: a promising newcomer, likely to cause coastal astonishment.|
F~A giant wave of talent. I will quietly stand somewhere above the tide line.|
S~He thinks we have momentum. Let us keep improving the decisions behind it.|
S~Even a great wave is made of smaller movements. Today's was enough.|
S~You do not need to become spectacular immediately to deserve that compliment.|
S~I want to remember how you looked hearing that. You earned it.
''')

add('mauville_kirk_rock_heart', 'MauvilleCity_Gym_Text_KirkPostBattle',
    'Kirk says Pokemon and rock music are all about heart.', '''
S~Heart is important. So is knowing which end of the guitar makes the noise.|
S~He enjoys both enough to put his whole self into them. That counts for something.|
S~Keep that heart. Give the team time to recover, too.|
S~Yes. Though practicing the difficult parts is one way to show you mean it.|
S~You can hear that he loves it. I hope his Pokemon feel that, too.|
M~He has delivered his entire artistic manifesto at concert volume.|
M~I believe him. Mostly because I can feel his heart speech in my teeth.|
N~Enthusiasm is a good starting power source. Practice makes it useful.|
S~There is room for a loud heart here. I am glad he found it.|
S~He is having a good time even after losing. That is a look worth keeping.|
S~The battle is over, and he is still giving us the encore.
''')
add('mauville_shawn_wattson_experience', 'MauvilleCity_Gym_Text_ShawnPostBattle',
    'Shawn says Wattson was battling before the player father was born.', '''
U~He has been battling since before Dad existed. That is a very long tutorial.|
N~Experience can preserve a great many lessons. I wonder which changed his approach most.|
N~Then we should expect him to recognize the obvious tricks.|
S~I like that he still seems excited about it after all those years.|
S~He must have helped a lot of young teams find their feet.|
M~A career so long the local families serve as units of measurement.|
M~That is an impressive amount of time to spend laughing near live electricity.|
N~Decades of practical testing. I would like to see his earliest designs.|
S~A long life of battles, and he still welcomes another.|
S~He has kept his enthusiasm longer than some people keep a hairstyle.|
N~Shawn sounds proud to learn from someone with that much history.
''')
add('mauville_ben_switch_traps', 'MauvilleCity_Gym_Text_BenPostBattle',
    'Ben says Wattson enjoys making switch traps.', '''
M~A nice quiet hobby. Except for the electricity and trapped visitors.|
N~He appears to enjoy observing how people solve a problem he constructed.|
M~Everyone needs a hobby. His requires an evacuation route.|
N~I hope he can tell the difference between a puzzled visitor and a frightened one.|
N~I prefer surprises that do not stand between tired people and the exit.|
M~He built a captive audience and thoughtfully supplied all the switches.|
M~Some people knit. Some people make the hallway judge you.|
S~I understand the appeal. I would label the emergency shutoff first.|
M~The building is full of little decisions he wants strangers to make.|
M~An eccentricity with its own floor plan.|
S~I wonder whether he watches people work them out with that same huge grin.
''')
add('mauville_vivian_founder', 'MauvilleCity_Gym_Text_VivianPostBattle',
    'Vivian credits Wattson with founding Mauville and admires his knowledge.', '''
U~He founded the city? I cannot even found the correct pocket for my keys.|
N~He would be a valuable source on how this place changed. We should ask about specifics.|
N~Building a city takes more than winning battles. He must have worked with plenty of people.|
S~There must be places here that remind him of people nobody else remembers.|
S~I hope the people who built it with him are remembered, too.|
M~The leader has an unusually strong answer to complaints about the neighborhood.|
M~He can honestly tell the entire city he was here first. Dangerous power.|
U~Now I want to know which came first: the streets or his electrical plans.|
S~He has watched a whole town grow around the years of his own life.|
S~That is a legacy you can actually walk through.|
N~I would ask what the first street looked like. Big histories begin somewhere small.
''')
add('mauville_angelo_forehead', 'MauvilleCity_Gym_Text_AngeloPostBattle',
    'Angelo says Wattson shiny forehead makes him happy.', '''
L~Finally, someone has identified the Gym's backup lighting.|
N~That is an unusually specific source of happiness. It seems harmless.|
M~If that makes his day, I am not taking it from him.|
F~Now I am going to notice it, and I will have to pretend I did not.|
S~There are worse ways to brighten someone's afternoon.|
M~An admiring review of the leader's reflective qualities.|
M~A glowing endorsement. Unfortunately, I understand why.|
M~I had been looking for the light fixture. That explains a few readings.|
S~A small bright thing was enough. I envy that a little.|
M~I would ask permission before offering him powder. It might ruin Angelo's day.|
M~I cannot unnotice that now. We have been given a very powerful observation.
''')
add('mauville_shock_wave_lesson', 'MauvilleCity_Gym_Text_ExplainShockWave',
    'Wattson explains that Shock Wave does not miss.', '''
U~A move that will not miss. Can it teach me to put things in the bin?|
N~Reliable accuracy is useful when a battle leaves little room for uncertainty.|
N~Dependable. We still need to choose an opponent it can actually affect.|
S~One less thing to worry about when everything else is moving quickly.|
N~Knowing a move will connect can help a nervous team settle into its plan.|
M~The attack has been excused from the dramatic near miss.|
M~A rare promise that arrives with fewer excuses than a person.|
S~Repeatable performance. Those are two of my favorite words.|
N~It finds its path. We still choose where to send it.|
S~I appreciate a gift that advertises reliability instead of spectacle.|
N~He sounds proud of how dependable it is, not only how strong.
''')
add('mauville_wattson_optimism', 'MauvilleCity_Gym_Text_WattsonPostBattle',
    'Wattson says a promising young trainer fills him with optimism.', '''
S~We defeated him and improved his mood. That is a very efficient victory.|
S~He sees a good result for someone else as good news for the future.|
S~That is a leader who wants the next generation to get stronger.|
S~He makes being promising feel like encouragement instead of a debt.|
S~I hope we can be that happy for someone else's progress someday.|
S~Our challenger has become the happy ending in his afternoon.|
S~He has every excuse to grumble and picked laughing instead.|
S~He is pleased the test found someone who could pass it. Good design philosophy.|
S~Some people make room for the future by cheering as it arrives.|
S~He did not make our win about how impressive he used to be. I like him.|
S~That laugh is going to stay with me longer than the switches.
''')
add('lavaridge_cole_sand_joints', 'LavaridgeTown_Gym_1F_Text_ColePostBattle',
    'Cole explains that hot sand helps circulation and aching joints.', '''
U~I thought he was setting an ambush. Apparently this is a health appointment.|
N~Heat can be soothing. I would still watch the temperature and duration carefully.|
M~A joint treatment with surprise trainer battles. Unusual package.|
N~I hope the battle did not interrupt the part that was helping him.|
N~Warmth, a rest, and someone making sure you can get back out. That last part matters.|
M~His ambush has been reclassified as a wellness retreat.|
M~I came expecting danger and found a man taking very aggressive time off.|
N~I would like a temperature gauge before agreeing to become part of the floor.|
S~The ground holds warmth for him. A kinder reason to stay buried than I expected.|
M~I am relieved there is a purpose beyond exfoliating the entire trainer.|
S~He has found comfort in a place that keeps surprising visitors.
''')
add('lavaridge_axle_tired_sand', 'LavaridgeTown_Gym_1F_Text_AxlePostBattle',
    'Axle says spending too long buried in hot sand is exhausting.', '''
U~We have found a way to get tired while lying down. Humanity has gone too far.|
N~The heat is taking a toll. He should get out and cool down.|
N~Then he needs a break somewhere that is not the source of the problem.|
N~He sounds worn out. I would rather he rested than tried to impress us.|
N~Water and a cooler place first. Another battle can wait.|
M~The restorative treatment has developed a small plot complication.|
M~The relaxation is exhausting him. I finally feel understood by a spa.|
N~If the process leaves you worse off, adjust the process. Preferably from outside the sand.|
N~He has stayed past the comfortable part. His body is trying to tell him.|
N~He does not have to finish being buried just because he started.|
N~I hope someone checks on these trainers between challengers.
''')
add('lavaridge_gerald_magma_claim', 'LavaridgeTown_Gym_1F_Text_GeraldPostBattle',
    'Gerald wrongly claims beating him proves the Pokemon could survive magma.', '''
U~Winning a battle is not a certificate that says lava-proof. Please do not issue those.|
A~His temperature claim is wrong, and the conclusion is dangerous. Winning here proves no magma tolerance.|
A~No. Our Pokemon are not going into magma to settle his theory.|
U~I thought that was a joke until he kept explaining. Please tell me it was a joke.|
A~We are keeping every member of this team safely away from magma.|
A~A spirited performance has been mistaken for an entirely different experiment. Cancel that experiment.|
M~That is the sort of confidence I prefer to observe from a safe, nonmolten distance.|
A~Incorrect temperature, invalid inference, catastrophic proposed test. An impressively complete failure.|
N~A victory does not remove a creature's need for safety.|
A~Our Pokemon did not win the right to be treated like cookware.|
N~I would rather remember their battle than have to explain why anyone believed him.
''')
add('lavaridge_danielle_flannery_goal', 'LavaridgeTown_Gym_1F_Text_DaniellePostBattle',
    'Danielle wants to be a pretty and strong trainer like Flannery.', '''
S~Two goals. Very economical to have a role model who covers both.|
S~She knows what she admires. Now she can decide which parts to make her own.|
N~She can become strong without becoming a copy of someone else.|
S~It helps to see someone being the kind of person you hoped was possible.|
S~I hope she is kind to herself while she gets there.|
S~A clear inspiration. Her own version should make an interesting entrance.|
S~She is allowed to admire Flannery and still take up her own space.|
N~A role model is a starting design, not a specification you must reproduce.|
S~She has seen a possible future. It need not wear exactly the same face.|
S~Pretty and strong are allowed to mean her version of both.|
S~I wonder whether Flannery knows she has already inspired someone.
''')
add('lavaridge_jeff_coal_boast', 'LavaridgeTown_Gym_B1F_Text_JeffPostBattle',
    'Jeff boasts he can walk on hot coals but tells the player not to try.', '''
M~He lost the battle but retains the prestigious title of Foot Champion.|
N~I am pleased the warning arrived before anyone attempted to reproduce the result.|
N~We can let him keep that victory. Keep your shoes on.|
N~He sounds like he needs one thing to still feel proud of. I can leave him that.|
N~No need to prove anything with burned feet. We will take the safe path.|
M~Defeated in battle, undefeated in the emergency supplementary talent round.|
M~I will honor his request by refusing to do that extremely thoroughly.|
N~A demonstration I am comfortable declining without further data.|
N~Pain is an unusual thing to offer as proof of worth.|
M~The shoes and I have discussed it. We will not be participating.|
N~He remembered to warn us even while showing off. I am glad of that part.
''')
add('lavaridge_overheat_lesson', 'LavaridgeTown_Gym_1F_Text_ExplainOverheat',
    'Flannery explains Overheat strong damage and sharply reduced Special Attack.', '''
U~A huge burst, then a much smaller burst. Like me agreeing to run up the stairs.|
N~Immediate power trades away later Special Attack. We should plan what follows it.|
N~A strong opener can leave a bad second turn. Do not use it without an exit plan.|
N~It gives a lot at once. I would not ask a Pokemon to keep producing the same intensity afterward.|
N~A powerful effort needs room to recover. We should remember the team behind the move.|
M~A spectacular opening number with a very demanding intermission.|
M~It burns through its own enthusiasm. A deeply relatable move.|
N~High output, steep performance drop. Useful when the timing justifies the cost.|
N~Fire spends something of itself. The next moment must make room for that.|
N~I like that she told us what it costs before we committed.|
N~That drawback matters as much as the impressive first hit.
''')
add('lavaridge_flannery_norman_resemblance', 'LavaridgeTown_Gym_1F_Text_FlanneryPostBattle',
    'Flannery realizes the player battles like Norman.', '''
U~You battle like your dad. He will either be proud or ask for the move back.|
N~People learn patterns from those they watch closely. Your own choices still belong to you.|
N~There may be a resemblance. You earned this win yourself.|
S~Does hearing that feel good, or a little complicated? You do not have to answer now.|
S~Family leaves little habits in us. You still chose what to do with them.|
M~A family resemblance discovered through competitive combat. Quite a reunion photograph.|
N~You can sound like your father and still be saying something of your own.|
N~I wonder which decision reminded her of him. That would be useful to know.|
N~An old thread in a new pattern. It does not make the pattern less yours.|
N~She recognized him in your style. I hope she also remembers your name.|
S~I would like to hear what Norman notices when he sees you battle now.
''')

add('fortree_jared_turns', 'FortreeCity_Gym_Text_JaredPostBattle',
    'Jared says trainers must adapt to unexpected turns and asks if the player can reach Winona.', '''
M~Unexpected turns. In the building full of turning doors. He has prepared this speech.|
N~Adaptation matters. So does stopping to look at how these doors actually move.|
N~We can think our way through. There is no need to make it a race.|
N~I would like one quiet moment to remember which way we entered.|
N~Let us check the team, then the route. Both deserve attention.|
M~A test of wit delivered beside a large rotating metaphor.|
M~I would feel smarter if the architecture stopped rearranging its opinion.|
N~Each door follows a rule. We only need to observe it before pushing.|
N~An unexpected turn is still a path once you see where it leads.|
M~The challenge is convincing the doors that our destination matters.|
N~I am watching which passages change after each turn. We can work it out together.
''')
add('fortree_edwardo_wider_world', 'FortreeCity_Gym_Text_EdwardoPostBattle',
    'Edwardo wants to keep training because the world has countless strong trainers.', '''
S~A whole world of people who can beat us. Strangely, I still want to see it.|
S~There will always be something another trainer can teach us. That is not a failure.|
N~Train for the next step. The whole world is too much to fight at once.|
S~It makes the road feel longer in a good way. There are people we have not heard yet.|
S~I hope he finds friends among those strong trainers, too.|
S~He has discovered that the story continues beyond the local cast.|
S~A large world is comforting. It leaves room to be unfinished.|
N~Different opponents will test different weaknesses. Variety is worth seeking.|
S~There is more sky than any one pair of wings can cross.|
S~He sounds excited instead of threatened by people being better. Good for him.|
S~Maybe we will meet him somewhere new and have this conversation again with more miles behind us.
''')
add('fortree_flint_blushing', 'FortreeCity_Gym_Text_FlintPostBattle',
    'Flint calls Winona cute and strong and blushes.', '''
M~His battle strategy has been replaced by a very warm face.|
F~He appears to admire her. I do not think further analysis would help his composure.|
M~She is his leader. Hopefully he remembers the strong part when training starts.|
F~I was going to say something supportive, but now I am embarrassed for both of us.|
S~He seems happy just getting to train here. That is rather sweet.|
M~His praise began professionally and then lost control of its stage lighting.|
F~We can leave before his face develops a second shade.|
N~That explains the enthusiasm. It does not quite explain the battle plan.|
S~Some feelings insist on arriving before the words are ready.|
M~An honest compliment. The blush did not leave much room for denial.|
S~We should let him keep a little dignity. No teasing where she can hear.
''')
add('fortree_ashley_safety', 'FortreeCity_Gym_Text_AshleyPostBattle',
    'Ashley says Winona lets Fortree residents live without fear.', '''
S~A good leader protects the town even when nobody is handing out badges.|
N~That is a more meaningful measure of leadership than a battle record alone.|
S~Keeping people safe is work worth respecting.|
S~Feeling safe enough to live normally is easy to forget until it is missing.|
S~I hope Winona has someone looking after her when she is tired, too.|
N~The spectacular battles are only the part visitors get to watch.|
S~That makes her more than the person waiting at the end of a puzzle.|
N~A strong public safety record does not happen by accident.|
S~Someone has made this high place feel like solid ground.|
S~I like knowing what people appreciate about her outside the Gym.|
S~That tells me more about the town than another account of a winning move.
''')
add('fortree_humberto_distraction', 'FortreeCity_Gym_Text_HumbertoPostBattle',
    'Humberto warns the player not to get distracted staring at Winona.', '''
M~That warning has the texture of personal experience. Possibly a floor-shaped texture.|
N~Keeping attention on a battle is sensible. The oddly specific example is his own contribution.|
M~We were watching the battle. He seems to have had a different assignment.|
F~I had not been thinking about staring. Now I am thinking about where to put my eyes.|
N~Let us give her the courtesy of paying attention to her work.|
M~An experienced critic of the dramatic pratfall. One suspects a first-hand review.|
M~I will try to admire her without becoming a cautionary heap.|
M~I had planned to monitor the moving doors, which are already a substantial distraction.|
N~He warns us about a fall his words seem to remember.|
M~We can appreciate a strong woman without losing all control of our necks.|
M~He says that like someone who once looked up from the floor and learned a lesson.
''')
add('fortree_darius_serious_team', 'FortreeCity_Gym_Text_DariusPostBattle',
    'Darius acknowledges the win but warns Winona Pokemon are all business.', '''
M~All business. I hope they do not make us fill out a form before pecking.|
N~We should expect practiced coordination, not just individually strong Pokemon.|
N~Then we will take them seriously. We were going to anyway.|
N~It is useful to hear a warning without having our win taken away from us.|
N~A focused team deserves a focused challenger. Let us give ours a moment first.|
M~Our next opponents have cancelled small talk and gone directly to the agenda.|
M~Good. I was worried we might interrupt their recreational dive-bombing.|
N~Then we should identify what each team member contributes before committing to a plan.|
N~Feathers can be soft without making the talons less real.|
S~He gave us credit before the warning. I appreciate the order.|
N~He knows what her team can do. That makes his caution worth hearing.
''')
add('fortree_aerial_ace_lesson', 'FortreeCity_Gym_Text_ExplainAerialAce',
    'Winona explains that Aerial Ace is fast enough not to be evaded.', '''
U~Too fast to avoid. My thoughts have finally found a worthy opponent.|
N~A dependable hit can be more valuable than a stronger move we cannot land.|
N~Good reliability. We should still consider the matchup before using it.|
S~I like a move that does not need a second attempt to say what it means.|
N~Let us find the teammate who can make the most of it.|
M~Aerial excellence without the suspense of an unsuccessful entrance.|
M~It avoids the awkward part where everyone watches you miss. I understand the appeal.|
N~Accuracy removes one uncertainty. It does not remove every other variable.|
N~A clean line through the air, without hesitation at the end.|
S~A precise gift from someone who clearly values control.|
N~Her explanation is as economical as the move sounds.
''')
add('fortree_winona_birds_devotion', 'FortreeCity_Gym_Text_WinonaPostBattle',
    'Winona says losing does not change her devotion to bird Pokemon.', '''
S~Her birds lost a battle, not their person. Good.|
S~One result does not erase years of affection and study.|
S~She is not blaming the team for losing. That matters.|
S~It is good to know you are still wanted after a difficult day.|
S~I hope they hear that from her. They deserve to.|
S~A defeat has failed to rewrite the most important relationship in the room.|
S~They do not have to earn her affection back. I like her for that.|
N~Keep the commitment. Adjust the methods. Those are separate decisions.|
S~The wind changed. The bond did not.|
S~Loyalty that survives an unflattering result is the kind worth having.|
S~I would rather remember how she treats them now than how she looked before the match.
''')
add('fortree_winona_unbroken', 'FortreeCity_Gym_Text_WinonaPostRematch',
    'After the rematch Winona says her heart wings remain unbroken and she will rise again.', '''
S~She is ready to soar again. I would settle for finding the exit without meeting a door.|
S~She knows losing and being unable to continue are different things.|
S~She will come back stronger. We should be ready when she does.|
S~She sounds like she believes herself. I know that can take practice.|
S~A rest can be part of getting back up. I hope she allows herself one.|
S~A loss, a declaration, and the promise of another act. She knows how to end a scene.|
S~I like that she can admit the fall without accepting the ending.|
N~Confidence is useful when it survives contact with an unfavorable result.|
S~The ground is a place to begin again, too.|
S~Her certainty sounds earned, not painted over the disappointment.|
S~I hope we meet again after both teams have had more sky.
''')
add('mossdeep_blake_dust_bunny', 'MossdeepCity_Gym_Text_BlakePostBattle',
    'Blake claims to lift a dust bunny psychically and denies blowing on it.', '''
M~Remarkable. His psychic power appears to come out of his mouth.|
M~A controlled test should separate psychic influence from the rather obvious air current.|
M~I believe he moved the dust. The rest of the claim needs work.|
F~I want to let him have this, but he made the denial before we asked.|
S~He is trying very hard. Perhaps we can encourage the practicing part.|
M~The illusion was flawless until the magician cross-examined himself.|
M~A powerful mind. An even more powerful suspicious little exhale.|
M~We can test that under a glass. I suspect he will develop an urgent appointment.|
M~The dust heard his wish. It may also have felt his breath.|
M~I have seen less convincing things sold as premium treatments.|
M~If we stand on the other side, does the psychic wind change direction?
''')
add('mossdeep_hannah_positive', 'MossdeepCity_Gym_Text_HannahPostBattle',
    'Hannah says she will not put herself down for losing and will keep training.', '''
S~She lost the match and refused the optional self-insult. Excellent defensive play.|
S~A clear assessment is easier when it is not buried under punishment.|
S~She can own the loss without turning against herself. Good.|
S~I am trying to learn that part, too. She makes it sound possible.|
S~Training goes better when you are on your own side.|
S~The critic has been removed from the rehearsal room for unhelpful behavior.|
S~I admire that. My brain still likes to issue a full review of every mistake.|
N~Blame does not tell you what to change. Looking at the battle will.|
S~She has left a little kindness waiting at the place she fell.|
S~That is confidence I trust. It has room for an actual mistake.|
S~I hope the next challenger is as gracious to her as she is being to herself.
''')
add('mossdeep_nate_not_rattled', 'MossdeepCity_Gym_Text_NatePostBattle',
    'Nate stammers while insisting defeat does not rattle him.', '''
S~He is only slightly rattled. Like a cupboard falling down the stairs. We should be kind.|
N~He may need a moment before discussing the result. We can give him one.|
N~He does not have to convince us. The battle is over.|
S~I know how it feels when your voice gives you away. Let us not make him explain.|
N~A breath and some water might help more than another question.|
N~The brave closing line arrived before its performer was quite ready.|
S~I am going to believe the part where he is trying.|
N~We can resume the analysis after his hands stop shaking. No rush.|
N~A trembling voice can still belong to someone being brave.|
N~We do not need to catch him out on how he feels.|
S~Let us leave him a little space to recover without an audience.
''')
add('mossdeep_kathleen_vitality', 'MossdeepCity_Gym_Text_KathleenPostBattle',
    'Kathleen calls the player vitality contagious and asks them to leave quickly.', '''
U~We have been diagnosed with enthusiasm. Apparently it requires quarantine.|
M~I do not think energy is transmissible in quite the way she suggests.|
M~She asked us to leave. We can respect that without apologizing for being awake.|
F~I am usually the one worried about being too quiet. This is new.|
N~Perhaps she needs some peace. We can take our very lively team elsewhere.|
M~Our performance has exceeded the venue's permitted excitement level.|
M~At last, a medical excuse to leave a conversation.|
N~She seems overstimulated. Increasing the volume of our explanation would not help.|
N~Some rooms need a gentler flame. We can carry ours onward.|
M~A compliment and an eviction in one breath. Efficient.|
S~We will let her have the quiet. Not every good mood needs to fill the room.
''')
add('mossdeep_nicholas_invincible', 'MossdeepCity_Gym_Text_NicholasPostBattle',
    'Nicholas plans to develop an invincible Pokemon power.', '''
U~Invincible! Please let the testing phase include somebody saying no.|
N~An ambitious claim. He should define what would count as evidence against it.|
M~Everyone says invincible until the next challenger arrives.|
N~I hope a setback will still be allowed after he gives it that name.|
N~I would rather have a team that trusts him than one he expects never to lose.|
M~He has responded to criticism by commissioning an unreviewable sequel.|
M~A power with no weaknesses. Except, I suspect, being asked to demonstrate it.|
M~I recommend a prototype before the word invincible goes on the packaging.|
N~A shield against every loss can become a wall against learning.|
M~That is a difficult label to wear on an ordinary bad day.|
N~I hope he remembers to enjoy practicing before he starts demanding perfection.
''')

add('mossdeep_preston_indecision', 'MossdeepCity_Gym_Text_PrestonPostBattle',
    'Preston warns that indecisive trainers lose.', '''
M~He said that very decisively. The scoreboard has a small objection.|
N~Deciding promptly helps, but a quick mistake is still a mistake.|
N~Take the time you need to choose well. Do not let him rush you after the battle.|
N~A pause is not always fear. Sometimes it is how you stop making the same mistake.|
N~We can prepare choices before a battle without pretending every decision is easy.|
M~A firm statement delivered from the losing side of the argument.|
M~I am still deciding whether to tell him how that sounds after losing.|
N~Commitment matters after the observations are in. Not before.|
N~Still water is not always stuck. Sometimes it is deep.|
N~Confidence is useful. So is leaving yourself time to notice something.|
N~I would rather know which moment he hesitated in than accept that as a rule for everyone.
''')
add('mossdeep_virgil_prodigies', 'MossdeepCity_Gym_Text_VirgilPostBattle',
    'Virgil calls the twins prodigies but thinks the player may be even more talented.', '''
F~More talented than the prodigies? My job is still carrying absolutely no trophies.|
S~A generous assessment. It should not erase the practice that made this possible.|
S~You did well. You do not have to turn that into a ranking of everyone in the room.|
F~That is a lot of praise to stand still underneath.|
S~I hope the team gets included in that compliment. They worked hard beside you.|
M~The review has escalated from promising challenger to possible disturbance in the genius rankings.|
F~I will accept the compliment on your behalf while you work out where to put your face.|
N~Talent is difficult to measure. The decisions in that battle are easier to examine.|
S~He sees something bright in you. You need not outshine anyone to keep it.|
S~You can enjoy praise without agreeing to be exceptional every single day.|
S~He was prepared to admire the twins and still made room to notice you.
''')
add('mossdeep_samantha_prediction', 'MossdeepCity_Gym_Text_SamanthaPostBattle',
    'Samantha predicts an intense leader battle but refuses to reveal the result.', '''
M~A prediction with all the useful details removed. Remarkably difficult to disprove.|
N~She has predicted a close contest and withheld the only testable outcome.|
M~Fine. We will find out by actually battling them.|
N~I am relieved, honestly. I would rather enter without somebody else's ending in my head.|
N~We can prepare the team ourselves. That is more useful than worrying over a prediction.|
M~A prophet with excellent spoiler etiquette.|
M~She knows the result, but it is apparently a premium service.|
M~An intense battle is a fairly safe forecast inside a Gym.|
N~Let the future keep something for us to choose.|
M~Mysterious enough to impress, vague enough to survive the review.|
S~I like getting to see it happen rather than being told how I am supposed to feel first.
''')
add('mossdeep_maura_deserved_future', 'MossdeepCity_Gym_Text_MauraPostBattle',
    'Maura claims diligent work guarantees a bright future while idleness ends in despair.', '''
N~Working hard helps. I do not think the universe checks everyone's homework that neatly.|
N~Effort matters, but circumstances do too. A bad outcome is not proof of laziness.|
N~People can work hard and still need help. I would not judge them by where they ended up.|
N~Some days getting through the day takes everything. It can look very quiet from outside.|
N~Rest is not a moral failure. People need it before they can keep going.|
N~A satisfying moral for a simple story. People are rarely given such simple lives.|
N~I do not like a rule that calls exhausted people guilty.|
N~Her model leaves out illness, resources, timing, and chance. Those are significant omissions.|
N~Not every seed gets the same rain. We should remember that before judging the harvest.|
N~A tired person does not need a prediction of despair. They might need lunch and some help.|
N~I would want to hear someone's story before deciding how they earned their circumstances.
''')
add('mossdeep_sylvia_threat', 'MossdeepCity_Gym_Text_SylviaPostBattle',
    'Sylvia resents losing and hints that something horrible may happen to the player.', '''
A~That is an unpleasant thing to say over a battle we both agreed to.|
A~An implied threat is not a useful response to losing. Let us leave her space.|
A~Stay beside me. We are done with this conversation.|
D~I wish she had stopped at being disappointed. We do not deserve the rest.|
A~We can leave without reassuring someone who just tried to frighten us.|
A~She has mistaken losing a scene for permission to become its villain.|
A~I prefer my ominous remarks fictional and considerably farther away.|
A~We do not need to test whether that was an empty threat. We can move on.|
N~Her anger does not get to choose what follows us out.|
A~Making us uncomfortable will not change who won.|
N~Let us remember the other people here, too. She does not get to define the whole visit.
''')
add('mossdeep_clifford_youth', 'MossdeepCity_Gym_Text_CliffordPostBattle',
    'Clifford attributes losing to the player youthful energy.', '''
M~Youthful energy. It powered several extremely deliberate button choices.|
N~Energy helped, perhaps. Our tactics also deserve some of the credit.|
N~You earned it through your decisions, not your birthday.|
S~I hope he does not think getting older means he has nothing left to learn.|
N~There is room for his experience and your energy without either being an excuse.|
M~A graceful concession with a small footnote addressed to the calendar.|
M~I would like to trade some youthful energy for his ability to remain standing this calmly.|
N~Age is a poor substitute for reviewing what actually happened in the battle.|
N~Different seasons bring different strengths. None make the whole story.|
N~I would rather hear what he noticed in our battle than what he noticed about our age.|
S~Maybe we can meet again and both bring something new to it.
''')
add('mossdeep_macey_brutal', 'MossdeepCity_Gym_Text_MaceyPostBattle',
    'Macey calls the player strong but too brutal to suit Psychic Pokemon.', '''
N~She can dislike our style. I would still like to know what she means by brutal.|
N~A specific criticism could help. Declaring an entire type unsuitable tells us very little.|
N~We should treat our team well. We do not need her permission to learn about Psychic Pokemon.|
D~That landed harder than a battle comment needed to. Let us think about the useful part later.|
N~If a Pokemon is uncomfortable, we listen to it. Her opinion is not a substitute for that.|
M~A victory with a strongly worded rejection from the local style committee.|
N~Being blunt is not the same as being cruel. I hope she means an actual choice we can examine.|
N~A training method can be reviewed. A vague label is harder to improve on.|
N~Listen for truth without letting the sharp edge decide your worth.|
N~A type is not a private club. There is more than one way to belong.|
N~I would ask what moment bothered her, if she were ready to have an actual conversation.
''')
add('mossdeep_calm_mind_lesson', 'MossdeepCity_Gym_Text_ExplainCalmMind',
    'The twins explain that Calm Mind increases Special Attack and Special Defense.', '''
U~A calmer mind makes you stronger and harder to hit. Mine currently has six chairs falling over.|
N~It improves both special offense and defense. A setup turn can benefit several later exchanges.|
N~A useful move when there is room to prepare. We should make that room deliberately.|
S~I like a strength that begins by getting quieter.|
S~Taking a moment to settle can help with more than the next attack.|
M~The twins have performed a two-person explanation of a one-Pokemon moment of peace.|
M~At last, a tactical reason to stop listening to everyone for a turn.|
N~Two linked improvements from one adjustment. We should consider which teammates use both.|
S~Stillness can hold a great deal of strength.|
S~Composure that protects as well as impresses. A useful thing to practice.|
N~Their explanation needed teamwork, too. They seem to do everything together.
''')
add('mossdeep_twins_player_bond', 'MossdeepCity_Gym_Text_TateAndLizaPostBattle',
    'The twins praise the player bond with Pokemon as stronger than their twin bond.', '''
F~Stronger than twins? I was proud when our team agreed on which way to walk.|
N~Their bond is not disproven by a battle result. They can admire ours without diminishing it.|
S~Your team trusted you. That is worth being proud of.|
S~I hope they know losing together does not mean they are less close.|
S~A bond shows in how we look after one another afterward, too.|
S~They have given our partnership a wonderful review, although I would spare theirs the unfavorable comparison.|
S~There is room for both teams to care about each other. It is not another competition.|
N~Coordination was decisive. We should remember the choices that helped our team work together.|
S~A bond can recognize another without becoming smaller.|
S~That is lovely praise. Their closeness does not need to lose so ours can win.|
S~The trust was visible. You and your Pokemon gave each other room to do your part.
''')
add('mossdeep_twins_two_needed', 'MossdeepCity_Gym_Text_TateAndLizaNeedTwoMons MossdeepCity_Gym_Text_TateAndLizaRematchNeedTwoMons',
    'The twins cannot start their double battle because the player has only one usable Pokemon.', '''
M~Two leaders, one Pokemon, and a very embarrassed head count.|
N~We need two Pokemon able to battle. A party slot alone is not enough.|
N~Let us heal and check the team. Nobody needs to handle both sides alone.|
F~They noticed the missing partner in perfect harmony. Somehow that makes it worse.|
N~We can come back with two healthy teammates. They are happy to wait.|
M~Our opening scene has been delayed by an incomplete cast.|
M~I would volunteer, but my strongest move is leaving the room.|
N~We have not met the input requirements. An easy error to correct before running the test.|
N~There needs to be someone standing beside our Pokemon, too.|
M~We remembered the dramatic arrival and forgot the second participant.|
N~The twins are right. We should bring a pair that can actually support each other.
''')
add('mossdeep_twins_support', 'MossdeepCity_Gym_Text_TateAndLizaPostRematch',
    'The twins say they always support each other and will rise after defeat.', '''
S~Two people ready to help each other up. That is a good rematch plan.|
S~Mutual support is a real advantage, particularly after the result disappoints them both.|
S~Good. Nobody gets left alone with the loss.|
S~I like hearing them say it out loud. Even familiar support deserves to be named.|
S~I hope their Pokemon get the same reassurance. They were part of this, too.|
S~The partnership survives the setback. That is the ending I was hoping for.|
S~Having someone stay beside you afterward is worth more than a flawless record.|
N~They can review the failure together instead of trying to hide it from each other.|
S~Two roots can hold when one would loosen.|
S~They are allowed to be disappointed and still know they have each other.|
S~That little exchange says more about their teamwork than any introduction could.
''')

add('petalburg_randall_room_choice', 'PetalburgCity_Gym_Text_RandallPostBattle',
    'Randall directs the player left to Confusion or right to Defense after the Speed room.', '''
N~Confusion on the left, Defense on the right. I brought confusion with me, so perhaps we save a trip.|
N~Status disruption or endurance. We can choose which problem our team handles better.|
N~Check the team before picking a door. We do not have to prove we can take every route.|
N~I like having the choice explained before the door closes behind us.|
N~Let us make sure the team is well before choosing what to ask of them next.|
M~Two further ordeals, clearly signposted. A courteous family establishment.|
M~A room dedicated to confusion. I usually manage it without special facilities.|
N~The two tests stress different parts of a plan. Choose deliberately.|
N~Two doors offer two lessons. Neither needs to become a judgment of us.|
N~I appreciate a warning that actually tells us what is on the other side.|
N~We should remember the room names. They describe the battles better than the doors do.
''')
add('petalburg_parker_strength', 'PetalburgCity_Gym_Text_ParkerPostBattle',
    'Parker warns that the next room tests brute strength.', '''
M~The next room is brute force. The building has run out of subtle suggestions.|
N~We should prepare for heavy damage rather than assume a longer setup will be safe.|
N~Heal first. A known hard hit is something we can prepare for.|
N~I am glad he warned us. I would rather be nervous with a plan than surprised.|
N~Our team does not need to enter exhausted just to show courage.|
M~The next act has dispensed with delicate dialogue and ordered a larger hammer.|
M~I admire a room that states its intentions before trying to flatten you.|
N~We know the load will be high. Time to check what can withstand it.|
N~A strong wall is not always the only way past a hard blow.|
N~There is no shame in checking our options before walking into something powerful.|
N~He is giving us a chance to prepare. We should use it.
''')
add('petalburg_george_earned_skill', 'PetalburgCity_Gym_Text_GeorgePostBattle',
    'George corrects himself: the player earned their abilities, then directs them to the One-Hit KO room.', '''
S~He remembered you did the work. Excellent correction. The next room's name is less comforting.|
S~He questioned his own assumption aloud. That is worth respecting. The next room deserves preparation.|
S~You earned this. Now heal up before we test what that next room actually does.|
S~I appreciated the correction. Being somebody's child should not swallow everything else you are.|
N~He gave you your effort back. Let us give the team a rest before that next challenge.|
S~A family resemblance was edited into proper credit. Then came the rather alarming door announcement.|
M~He withdrew the inherited-talent theory just before directing us toward the murderously named room.|
N~He revised a faulty explanation. Now we should investigate the next room instead of trusting its name.|
N~Your own steps brought you here. Take the next one with care.|
S~He caught himself. I like people who can fix what they say without making us do it for them.|
N~The correction matters. So does making sure the team is ready for the room he pointed out.
''')
add('petalburg_berke_family_glow', 'PetalburgCity_Gym_Text_BerkePostBattle',
    'Berke respects Norman and hopes the player and their father have a great battle.', '''
S~He is rooting for both of you. That is going to make keeping score complicated.|
S~Respect for your father has made him curious about what you can do. A fair starting point.|
S~We can give Norman a good battle without making it a contest over who matters more.|
N~Battling someone who knows you that well must feel different. I will stay beside you afterward.|
S~I hope it is a battle both of you can remember kindly.|
S~He is anticipating a family story he will be able to say he witnessed.|
N~There is room for you to resemble your father without being measured only against him.|
N~Familiar styles can make a battle especially interesting. Both sides know some of the assumptions.|
N~Two lights from one home need not burn the same way.|
S~He sounds fond of your father. I hope he gets to know you properly, too.|
S~I wonder which part of your battle will surprise Norman most.
''')
add('petalburg_mary_defense_recovery', 'PetalburgCity_Gym_Text_MaryPostBattle',
    'Mary directs the player to Defense or Recovery and says Attack will be tested.', '''
M~A choice between refusing to fall down and getting back up. Both sound exhausting to argue with.|
N~Defense reduces damage; recovery repairs it. Those require different answers.|
N~We should plan for staying power before choosing either door.|
N~A patient fight can be difficult in a different way from a loud one.|
N~Let us check our supplies. Long battles ask more of the whole team.|
M~Two opponents with different methods of declining to end the scene.|
M~One refuses to be hurt. The other refuses to stay hurt. Admirable, inconvenient people.|
N~Resistance and repair are distinct mechanisms. We should not approach them as the same problem.|
N~Some walls stand still. Others rebuild while you watch.|
N~Knowing the difference is more useful than simply hitting harder and hoping.|
N~She told us what is coming. We can decide which challenge suits our team today.
''')
add('petalburg_alexia_offense_doors', 'PetalburgCity_Gym_Text_AlexiaPostBattle',
    'Alexia acknowledges learning from the player and directs them to two offensive rooms.', '''
S~We taught a lesson! Apparently the curriculum now continues through two very aggressive doors.|
S~She recognized something worth learning, then helped us prepare for the next test.|
N~Both routes mean offense. We should not send a tired team through either.|
S~It is nice to know a battle can leave both sides with something useful.|
N~Let us tend to the team before asking them to stand through another hard fight.|
M~A gracious student sends the instructor onward to a much louder classroom.|
M~Both doors say someone intends to hit us hard. At least the architecture is honest.|
N~Two offensive tests. Check the party before committing to one.|
S~She kept the lesson, and gave us the path onward.|
N~I like the thanks. I am less enthusiastic about the menu of incoming damage.|
S~I wonder what she noticed in our choices. It is good when a loss becomes a conversation.
''')
add('petalburg_jody_norman_waiting', 'PetalburgCity_Gym_Text_JodyPostBattle',
    'Jody notices a resemblance to Norman battle style and says he is waiting ahead.', '''
N~Dad is waiting. We have done a remarkable amount of battling to arrange a family visit.|
N~She noticed a pattern in your style. Norman may notice how you have changed it.|
N~You got this far on your own decisions. Remember that when you face him.|
N~Take a moment before going in. You are allowed to feel more than ready or afraid.|
N~We should make sure the team is comfortable before such an important battle.|
N~The family resemblance has brought us to a scene only you can finish.|
N~We have heard how much you resemble him. Now he gets to see who arrived here.|
N~The next opponent knows your starting point. Let him see the improvements.|
N~The path came from home, and now bends back toward it. You are not the same traveler.|
N~You can be his child and still deserve to be taken seriously as his challenger.|
S~I will remember this quiet moment before you walk through the door.
''')
add('petalburg_norman_keep_training', 'PetalburgCity_Gym_Text_DadGoingToKeepTraining',
    'Norman asks the player to visit their mother and says he will train to avenge his loss.', '''
M~Visit Mom, defeat Dad again. Family errands have become unusually competitive.|
S~He wants to improve and wants you to stay connected to home. Those can coexist.|
S~We should visit your mother. And give him a real challenge when he is ready again.|
S~He sounds proud even while trying very hard to sound competitive.|
S~We can stop home between journeys. Being missed is a good reason all by itself.|
M~A father's reminder arrives wrapped in the declaration of a sworn sporting rival.|
S~He found a way to ask you to visit while insisting this is strictly Gym business.|
N~He has a training plan. We should keep developing ours rather than assume the next result.|
S~Home can hold a welcome and a challenge at the same time.|
S~I hope he follows his own advice and goes home sometimes, too.|
S~That sounded like two different parts of him trying to speak in the same sentence.
''')
add('petalburg_norman_deep_world', 'PetalburgCity_Gym_Text_DadNoAmountOfTrainingIsEnough',
    'After the League Norman says the Pokemon world is so deep training never feels sufficient.', '''
S~Even Dad has not reached the end of learning. That makes my unfinished list feel less personal.|
S~There is always another question. That does not make the work already done insufficient.|
N~He can keep improving without treating every rest as falling behind. So can you.|
S~I like knowing he still wonders about things after becoming so good at them.|
N~Enough for one day is allowed, even when there is more to learn tomorrow.|
S~The expert has discovered the subject is larger than his ending. A promising sequel.|
S~There is something comforting about not having to become finished.|
S~A deep subject keeps giving back when you examine it closely. I understand the fascination.|
S~The well does not need a bottom for the water to be worth drawing.|
N~I hope he lets himself be accomplished as well as ambitious.|
S~I would like to hear what still surprises him after all his years here.
''')
add('petalburg_norman_dream', 'PetalburgCity_Gym_Text_NormanPostRematch',
    'Norman asks the player dream and says his own has already come true.', '''
S~I think that laugh said something he could not quite fit into words.|
S~He seems content with something more personal than winning this battle.|
S~He is proud. You do not need to find a perfect answer immediately.|
F~That was very small and very important. I do not want to talk over it.|
S~It sounds like he is glad he gets to be here with you.|
S~A quiet line can carry more than the grandest victory speech.|
S~I think we should let that moment stay yours for a little while.|
S~His goal was evidently more complicated than a battle record. I am glad he reached it.|
S~Some dreams come home wearing a familiar face.|
S~He did not have to explain all of it for the feeling to reach us.|
S~That is the moment I would keep from today. If you wanted me to.
''')
