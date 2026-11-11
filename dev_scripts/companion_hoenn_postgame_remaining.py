"""Remaining verified Frontier advice, readings, and human NPC endings."""
ROWS = []
EMOTIONS = dict(N='neutral', S='soft_smile', A='annoyed', F='flustered', D='sad', U='surprised', M='smug', L='laughing')

def add(key, labels, subject, lines):
    replies = [x.strip() for x in lines.strip().split('|')]
    replies = [EMOTIONS[x[0]] + x[1:] for x in replies]
    assert len(replies) == 11, (key, len(replies))
    ROWS.append(dict(key='hpr_'+key, labels=labels.split(), subject=subject, replies=replies))

add('maiden_identity', 'BattleFrontier_Lounge2_Text_SalonMaidenIsThere', 'The Maniac identifies the mysterious Salon Maiden as the Tower leader.', '''
N~A mysterious trainer at the top of a very obvious tower. Interesting balance.|
N~We have a title and a responsibility. Her battle methods remain unspecified.|
N~She's responsible for the Tower. Worth remembering.|
N~I wonder whether she enjoys being called mysterious or just doesn't talk much.|
N~I'd rather meet her than build an opinion from the title alone.|
S~A grand title, a tall building, and remarkably little personal information. A tidy introduction.|
N~The mystery has been labeled. Apparently that counts as reducing it.|
N~I'd like to know how she shaped the Tower's challenges.|
N~A name can make a distant figure feel nearer without revealing much at all.|
N~Mysterious might mean private. I'd give her room to introduce herself.|
N~I'd ask someone who's actually met her what the conversation was like.
''')
add('maiden_silver_team', 'BattleFrontier_Lounge2_Text_SalonMaidenSilverMons', 'The Maniac reports the Salon Maiden testing roster of Psychic, Fire, and Normal partners.', '''
N~A thinking one, a blazing one, and a sleeping one. That last job sounds suspiciously attractive.|
N~The reported Psychic, Fire, and Normal coverage gives us several distinct matchups to consider.|
N~Don't underestimate the sleeping partner. Plan for all three.|
N~I wonder how the quiet-looking one fits with the other two.|
N~A calm appearance can hide plenty of strength. I'd prepare before deciding who's easiest.|
N~An impressive spread of talents, including the highly refined art of looking asleep.|
N~The sleeper has made the intimidating roster. A professional inspiration.|
N~We can compare our coverage against the reported types before entering.|
N~Stillness stands beside fire and thought. I wouldn't mistake it for absence.|
N~It's useful information, though I wouldn't let the labels replace watching the actual partners.|
N~I'd ask which of the three surprised his source most.
''')
add('maiden_gold_team', 'BattleFrontier_Lounge2_Text_SalonMaidenGoldMons', 'The Maniac describes the Salon Maiden serious Dragon-Psychic, Electric, and Normal roster.', '''
U~She's changed the first two and kept the sleeper. Apparently naps survive every promotion.|
N~That reported roster changes the coverage substantially. The Normal partner remains a constant.|
N~Different threats now. Recheck the plan instead of replaying the old one.|
N~The familiar partner might be the one I'd be most careful not to overlook.|
N~A repeated partner probably has a good reason to stay. I'd respect that.|
N~The serious roster has arrived, and the sleeping specialist has retained its position.|
N~Lightning, dragons, and a nap. A surprisingly coherent threat.|
N~We need answers to the new type combinations, not merely stronger versions of the old approach.|
N~Something quiet remains while the bright dangers change around it. Worth noticing.|
N~Keeping one familiar face can make the new lineup feel safer than it really is.|
N~I'd compare what changed with what stayed. Both choices tell us something about her approach.
''')
add('dome_identity', 'BattleFrontier_Lounge2_Text_DomeAceIsThere', 'The Maniac identifies the flamboyant Dome Ace as the Dome leader.', '''
S~Flamboyant sounds well matched to a building that wants everyone looking at it.|
N~His title establishes the facility connection. His style is a separate description.|
N~The Dome has a showman in charge. Skill still decides the battle.|
N~I wonder whether he's quieter when the audience has gone home.|
S~A lively host can make a place welcoming. I'd like to see how he treats a nervous challenger.|
S~A grand venue has acquired a leader unwilling to let the architecture do all the showing off.|
S~The Dome has apparently hired personality on the same scale as its roof.|
N~I'd ask how his strategies use the tournament format. That's the practical question.|
N~Some people step into bright spaces as though the light has been expecting them.|
S~He sounds conscious of presentation. I'm curious whether the whole place reflects his taste.|
S~I'd like to hear him explain what he enjoys about an audience.
''')
add('dome_silver_team', 'BattleFrontier_Lounge2_Text_DomeAceSilverMons', 'The Maniac reports the Dome Ace initial Dragon-Flying, Water-Ground, and Fire-Flying roster.', '''
N~Two flying dangers and one grounded-looking surprise. I'd keep my feet and my guesses careful.|
N~The reported dual types create distinct weaknesses. A single broad label won't describe the roster.|
N~Check the matchups before choosing. That's what the Dome gives us time for.|
N~Treating an opponent lightly doesn't sound like the same thing as bringing weak partners.|
N~I'd plan around the whole trio instead of picking the one that looks easiest.|
N~His supposedly casual welcome includes an alarming amount of wings and elemental force.|
N~Being treated lightly is apparently still a substantial physical experience.|
N~We should examine which pair handles the possible matchups with the fewest gaps.|
N~Air, water, and fire leave little room for a careless step.|
N~The casual attitude might be the least useful part of this information to trust.|
N~I'd ask how opponents usually choose against that mix. The selection itself sounds difficult.
''')
add('dome_gold_team', 'BattleFrontier_Lounge2_Text_DomeAceGoldMons', 'The Maniac describes the Dome Ace serious Dragon-Flying, Water-Ground, and Steel-Psychic lineup.', '''
N~The flame has made room for iron legs. His serious plans have a very heavy footstep.|
N~Steel and Psychic coverage replaces the earlier Fire-Flying component. That changes our selection problem.|
N~A new lineup needs a fresh choice. Don't just reuse the last pair.|
N~I wonder which partner he trusts when the strategy starts going wrong.|
N~We'll want a plan with room to adapt, rather than one perfect-looking opening.|
N~The grand strategy now includes something with iron legs. Subtlety has developed considerable weight.|
N~An imposing roster has become more imposing in a different direction. Helpful of it.|
N~I'd compare coverage across all three before deciding what to leave in reserve.|
N~A changed shape can hide a familiar intention. We need to observe both.|
N~He seems to change the impression as well as the matchups. That can unsettle a challenger.|
N~I'd ask what choice made people realize he was taking them seriously.
''')
add('factory_identity', 'BattleFrontier_Lounge2_Text_FactoryHeadIsThere', 'The Maniac identifies the eccentric Factory Head as the rental facility leader.', '''
N~The Factory Head is described as freaky. I'd prefer at least one useful measurement with that.|
N~That's a subjective characterization, not an explanation of his methods.|
N~An unusual manner doesn't tell us how he'll battle.|
N~I'd rather hear what he's like from someone who spoke with him kindly.|
N~People call unfamiliar things strange quickly. Let's meet him before deciding.|
N~A title, a building, and one unhelpfully broad adjective. The report could use revision.|
N~The mystery has received a rude nickname instead of a description.|
N~His handling of unfamiliar rentals interests me more than his manner.|
N~An odd shape to another person's eye may be entirely comfortable from within.|
N~Calling someone freaky says a little about the speaker, too.|
N~I'd ask what he actually did. Specific behavior tells a better story.
''')
add('factory_silver_team', 'BattleFrontier_Lounge2_Text_FactoryHeadSilverMons', 'The Maniac says the Factory Head uses three rentals under similar conditions to challengers.', '''
S~He gets unfamiliar partners too. Nobody has hidden a lifelong best friend behind the counter.|
N~Comparable rental conditions shift the contest toward evaluation and adaptive decision-making.|
N~Same kind of uncertainty for both sides. Learn the team quickly.|
N~That makes me curious how he introduces himself to each new partner.|
N~He has to work with the team he's given. There's something fair about that.|
S~The expert has agreed to use the same unpredictable ingredients as the guests. Admirable confidence.|
N~No private super-team in the cupboard. Only considerable expertise.|
N~His advantage may be how efficiently he assesses unfamiliar combinations.|
N~A stranger can become a partner quickly when someone knows how to listen.|
N~Similar conditions don't erase experience, but they do make his choices interesting to watch.|
N~I'd ask which rental combination challenged him to think differently.
''')
add('factory_gold_team', 'BattleFrontier_Lounge2_Text_FactoryHeadGoldMons', 'The Maniac confirms the serious Factory Head still battles with rental Pokemon.', '''
U~Even the serious version gets rentals. He hasn't upgraded to bringing his own certainty.|
N~The higher-stakes encounter preserves the rental constraint. Expertise remains the distinguishing factor.|
N~Same rental system. Expect better decisions, not a fixed familiar team.|
N~His confidence must come from understanding new partners rather than knowing them beforehand.|
N~That takes a lot of attention. A borrowed team still deserves to be understood.|
N~When serious, he continues obeying the inconvenient part of his own challenge. A respectable commitment.|
N~The training wheels were never hidden in his office. Slightly alarming news.|
N~We shouldn't expect a memorized roster to solve this. Adaptation is the task.|
N~He trusts his ability to begin again with someone unfamiliar. That's a particular strength.|
N~Consistency in the rules makes the stronger performance more impressive.|
N~I'd love to hear how his first minute with a rental team differs from an ordinary challenger's.
''')
add('pike_identity', 'BattleFrontier_Lounge2_Text_PikeQueenIsThere', 'The Maniac identifies the intimidating Pike Queen as the Pike leader.', '''
N~A scary trainer inside the giant snake. The building is doing very consistent introductions.|
N~The description suggests an imposing manner. It doesn't establish her actual temperament toward visitors.|
N~Be respectful. Intimidation isn't a battle result.|
N~I wonder whether she's tired of strangers arriving already afraid of her.|
N~I'd give her the chance to be a person before turning her into a warning.|
N~The title and venue have cooperated on a rather thorough first impression.|
N~A frightening reputation has found suitably unsubtle architecture.|
N~We need to learn how she battles, not only how people describe meeting her.|
N~A guarded face can collect stories it never chose to tell.|
N~People may confuse a reserved expression with an invitation to gossip.|
N~I'd ask somebody for an actual encounter rather than one more alarming adjective.
''')
add('pike_silver_team', 'BattleFrontier_Lounge2_Text_PikeQueenSilverMons', 'The Maniac reports the Pike Queen good-mood Poison, Bug-Rock, and Water team.', '''
N~That's the good-mood team? I'd hate to learn which face the snake makes when annoyed.|
N~The mood explanation is hearsay. The reported types still offer practical preparation clues.|
N~Poison, Bug and Rock, then Water. Prepare for the mix.|
N~I wouldn't count on her being gentle just because someone says she's in a good mood.|
N~A pleasant mood doesn't mean she'll stop caring for her own team's chances.|
N~Her allegedly cheerful reception still arrives with fangs and formidable defenses.|
N~Good mood is a relative term. The opponents appear fully equipped regardless.|
N~We can assess status protection and coverage against that reported lineup.|
N~A calm surface doesn't promise a soft welcome beneath it.|
N~I'd use the roster details and leave the speculation about her feelings aside.|
N~I'd ask what happened in the battle itself. Her expression can't tell the whole story.
''')
add('pike_gold_team', 'BattleFrontier_Lounge2_Text_PikeQueenGoldMons', 'The Maniac reports the Pike Queen serious Poison, Steel-Ground, and Water-Flying lineup.', '''
N~The snake now has a second, iron snake for company. That's a very firm commitment to snakes.|
N~The reported substitutions alter both defensive profiles and offensive coverage substantially.|
N~New team, different problems. Check our answers to each one.|
N~I wish he described her choices without deciding exactly how angry she must be.|
N~We'll prepare better by thinking about the partners than by worrying about her mood.|
N~An already imposing roster has acquired iron and an additional reputation for menace.|
N~The serious team has doubled down on long bodies and alarming introductions.|
N~We need to account for the new dual types rather than repeat the earlier plan.|
N~Iron changes the weight of a threat even when the shadow looks familiar.|
N~Her intensity may be real. The rumor has still decorated it quite enthusiastically.|
N~I'd compare the actual matchups before letting those descriptions decide how afraid to feel.
''')
add('arena_identity', 'BattleFrontier_Lounge2_Text_ArenaTycoonIsThere', 'The Maniac identifies the Arena Tycoon while emphasizing her cute appearance.', '''
N~I'd rather know how she battles than how successfully she impressed his eyes.|
N~Appearance is not evidence of strategic ability. Her leadership role is the relevant fact.|
N~She runs the Arena. Take her seriously.|
N~I wonder how often she has to get past that introduction before people listen.|
N~Being cute doesn't make the job easier. She's still responsible for a hard challenge.|
N~A formidable specialist has been introduced using the least useful item on her qualifications list.|
N~An expert has been reduced to an adjective. Efficiently uninformative.|
N~I'd ask what she values under the Arena judging rules.|
N~A small face can hold a very large intention. Neither needs explaining away.|
N~A compliment can still leave out the part of a person that matters to the conversation.|
N~I'd ask someone who's battled her what choice surprised them.
''')
add('arena_silver_team', 'BattleFrontier_Lounge2_Text_ArenaTycoonSilverMons', 'The Maniac reports the Arena Tycoon Bug-Fighting, Dark, and Bug-Ghost testing team.', '''
N~That last combination sounds like a very small surprise with very firm opinions about being hit.|
N~The reported Bug-Ghost partner makes appropriate coverage particularly important.|
N~Have a way to handle every partner. No room to switch around a bad opening.|
N~I think the unusual little one would make me pause longest.|
N~The order matters as much as the list. We should think through who follows whom.|
N~A compact roster with plenty of opportunity to punish an overconfident entrance.|
N~The small stranger may be the reason a large plan stops functioning.|
N~We need to examine coverage and sequence under the Arena's fixed-order rules.|
N~An apparently slight thing can decide which doors stay closed.|
N~The lineup rewards attention to details that an impressive first glance could miss.|
N~I'd ask how challengers usually handle the partner they least expected to struggle with.
''')
add('arena_gold_team', 'BattleFrontier_Lounge2_Text_ArenaTycoonGoldMons', 'The Maniac reports the Arena Tycoon serious Dark, Ghost-Poison, and Grass-Fighting roster.', '''
N~Shadows, poison, and a mushroom ready for a fight. That's a crowded little list of worries.|
N~The serious roster changes the coverage requirements while retaining the Dark partner.|
N~Plan the sequence again. Familiarity with one member won't cover the rest.|
N~The same quiet-looking partner stays while the others change. I'd remember that.|
N~We should choose a team that can handle trouble after the first matchup goes wrong.|
N~Her serious approach has provided several entirely different ways to spoil a comfortable plan.|
N~A mushroom has entered the serious roster. People underestimate mushrooms at their convenience.|
N~I'd test the proposed order against the full set of reported threats.|
N~A familiar shadow remains among new ones. Recognition isn't the same as safety.|
N~It's a good reminder to look again instead of assuming we've already understood somebody.|
N~I'd ask which matchup people found hardest to recover from under those Arena rules.
''')
add('palace_identity', 'BattleFrontier_Lounge2_Text_PalaceMavenIsThere', 'The Maniac calls the Palace Maven sinister while identifying the facility leader.', '''
N~Sinister is a big word to hand somebody before we've even said good afternoon.|
N~That characterization is subjective. We know his role, not the basis for the description.|
N~Let's meet him before borrowing the rumor's opinion.|
N~A quiet older person can look strange to someone who doesn't know them.|
N~I'd judge him by how he treats the Pokemon in his care.|
N~The report supplies an ominous adjective where a useful observation ought to be.|
N~A sinister reputation may simply be a private person surrounded by inventive visitors.|
N~I'd like to know how his team is prepared for autonomous battles.|
N~A face in shade isn't proof of what lives behind it.|
N~People sometimes make a whole costume out of somebody else's first impression.|
N~I'd ask for a story from someone who's actually spoken with him.
''')
add('palace_silver_team', 'BattleFrontier_Lounge2_Text_PalaceMavenSilverMons', 'The Maniac reports the Palace Maven Poison-Flying, Normal, and Water-Ice roster.', '''
N~A bat, a sleepy sort, and a water traveler. I'd like to hear how they all spend an ordinary morning.|
N~The reported types matter, but Palace behavior also depends on natures and available moves.|
N~We need a suitable partner, not just a favorable type chart.|
N~They sound like such different companions. I wonder what he likes about each one.|
N~I'd pay attention to what they choose without commands. That's the Palace's real complication.|
N~An unusual household, introduced as a formidable test. Both descriptions may fit perfectly well.|
N~The lazy partner has an important job. I support accessible career opportunities.|
N~Our preparation needs to account for autonomous choices as well as these matchups.|
N~Three different temperaments may share a quiet understanding we haven't seen yet.|
N~The description gives shapes and types. How they behave will make the encounter personal.|
N~I'd ask how challengers adjusted after seeing the first uncommanded move.
''')
add('palace_gold_team', 'BattleFrontier_Lounge2_Text_PalaceMavenGoldMons', 'The Maniac describes the Palace Maven serious Fire, Normal, and Water lineup.', '''
N~Fire and water have changed, but the lazy partner kept the position. Must be a very effective nap.|
N~The reported Fire and Water replacements alter coverage. The retained Normal partner deserves attention.|
N~Prepare for the changed team. Don't treat the familiar one as harmless.|
N~I wonder whether his partners feel the difference when he takes a match seriously.|
N~I'd focus on a reliable fit for our own partner before worrying about the impressive descriptions.|
N~His entire might apparently still includes an expert in conserving effort. Sensible delegation.|
N~The lazy one remains employed at the highest level. Strong evidence for the value of rest.|
N~The moves and natures may matter more than the roster's imposing titles suggest.|
N~A still center can remain while the surrounding weather changes completely.|
N~Repeated choices tell us something about trust. He seems to have plenty in that familiar partner.|
N~I'd compare how the returning partner behaves now with the earlier encounter.
''')
add('pyramid_identity', 'BattleFrontier_Lounge2_Text_PyramidKingIsThere', 'The Maniac identifies the fiery Pyramid King as the expedition facility leader.', '''
N~A fiery king inside a dark pyramid. At least he should be easy to notice when he arrives.|
N~His reported intensity suggests a forceful manner. It doesn't yet explain his battle strategy.|
N~He runs the expedition challenge. Take the route and the trainer seriously.|
N~I wonder whether that energy makes the dark feel less lonely or more alarming.|
N~I'd rather know how he prepares his partners for the long climb.|
S~A king, a pyramid, and a temperament that seems unlikely to go unnoticed in either.|
N~A fiery presence in a dark building. The atmosphere has been thoroughly organized.|
N~I'd ask what skills he designed the expedition to test.|
N~Some people carry a flame into a room without making it any warmer. We haven't met him yet.|
N~The title makes a strong impression. I'm more curious about the person doing the work.|
N~I'd ask an explorer what his arrival felt like after all those floors.
''')
add('pyramid_silver_team', 'BattleFrontier_Lounge2_Text_PyramidKingSilverMons', 'The Maniac reports the Pyramid King Rock, Ice, and Steel testing roster.', '''
N~Rock, ice, and iron. His team sounds as though somebody ordered three very stubborn landmarks.|
N~The reported elemental spread presents three distinct defensive profiles. Prepare specific answers.|
N~Three tough matchups. Save enough strength for whoever waits at the top.|
N~Meeting that team after a long climb sounds rather overwhelming.|
N~Our supplies and condition before the encounter may matter as much as the team choice.|
N~The summit reception appears to have been assembled from exceptionally unyielding materials.|
N~A geological committee has been convened to object to our arrival.|
N~We need coverage without assuming we'll reach the encounter at full resources.|
N~Stone, frost, and metal wait at the end of a tiring path. The climb is part of their weight.|
N~He chose a memorable trio. I'd rather remember the useful weaknesses than just the imposing shapes.|
N~I'd ask what condition successful explorers reached him in. That changes the whole story.
''')
add('pyramid_gold_team', 'BattleFrontier_Lounge2_Text_PyramidKingGoldMons', 'The Maniac reports the Pyramid King serious Ice-Flying, Electric-Flying, and Fire-Flying roster.', '''
U~The solid landmarks have taken flight and brought three kinds of weather with them.|
N~All three reported partners share Flying typing while differing strongly in their other coverage.|
N~Different team at the summit. Recheck the plan before another climb.|
N~Looking up after reaching the top would feel rather unfairly appropriate.|
N~I'd prepare the whole journey around having enough left for that encounter.|
N~The king has replaced three immovable objects with three extremely mobile objections.|
N~Having climbed to the top, we are apparently expected to look higher still.|
N~A shared type may offer a route through the matchup, but the secondary types complicate it.|
N~The summit has acquired wings. A finished climb doesn't promise stillness.|
N~The whole impression changes. I'd avoid letting the spectacle distract from the details.|
N~I'd ask which partner changed the pace of the battle most sharply.
''')
add('doubles_begin', 'BattleFrontier_Lounge2_Text_DoubleBattleAdvice1', 'The Maniac recommends Tower Doubles as a foundation for learning Frontier double battles.', '''
S~A place to learn two-at-once thinking before we try two-at-once panicking elsewhere.|
N~A stable format provides a useful baseline before adding other facilities' special rules.|
N~Learn the basics here. Then take them somewhere harder.|
S~I like a clear place to begin. The whole island feels less overwhelming that way.|
N~Getting comfortable with cooperation first sounds better than piling on every rule at once.|
S~A rare piece of guidance that begins with a manageable first step rather than a grand destiny.|
N~The basics have a building. Convenient, though rather tall.|
S~We can isolate the coordination problem before introducing additional constraints.|
S~Two paths are easier to follow when the ground beneath them stays familiar.|
S~A good starting place can make an unfamiliar format feel much more welcoming.|
N~I'd ask which mistake beginners make most often. That would be a useful first lesson.
''')
add('doubles_specialists', 'BattleFrontier_Lounge2_Text_DoubleBattleAdvice2', 'The Maniac warns that opponents develop strategies specifically for double battles.', '''
N~Two partners aren't just one battle with an extra pair of elbows. People have made plans about this.|
N~Interactions between active partners create strategies unavailable in a single battle.|
N~Expect teamwork from the opponent. Build some of our own.|
N~I think the surprising part would be realizing both opposing moves were one idea.|
N~A partner can help another partner in ways that don't look impressive alone.|
N~The second opponent is not decorative. An important clarification for the overconfident.|
N~Two minds may be conspiring. Best not to treat them as separate inconveniences.|
N~We should examine combined effects and avoid evaluating each move in isolation.|
N~Two small actions can cast one much larger shadow.|
N~The relationship between the choices may matter more than either choice by itself.|
N~I'd ask for an example of a combination that surprised him.
''')
add('doubles_expand', 'BattleFrontier_Lounge2_Text_DoubleBattleAdvice3', 'The Maniac suggests trying other double-battle facilities after mastering the Tower basics.', '''
S~Once two-at-once feels normal, the island has kindly prepared several fresh ways to confuse us.|
N~Transfer the established coordination skills, then account for each new facility's rules.|
N~Get comfortable first. Then choose a new challenge deliberately.|
S~I like being allowed to feel ready before moving on.|
S~A new setting can keep a familiar skill interesting. No need to rush there today.|
S~Graduation from the basics comes with a delightful brochure of further complications.|
S~Competence has earned the right to become slightly bewildered somewhere new.|
N~We can add one unfamiliar rule set at a time and see how the existing plan adapts.|
S~A familiar step can carry you somewhere the path has changed.|
N~Confidence should make room for curiosity instead of assuming the next place works the same way.|
S~I'd ask which facility he recommends next and why. The reason matters more than the title.
''')
add('multi_salon', 'BattleFrontier_Lounge2_Text_MultiBattleAdvice', 'The Maniac suggests looking carefully for familiar trainers or followers in the Battle Salon.', '''
S~A familiar face among all those possible partners would be a very pleasant surprise.|
N~The Salon's available trainers can include people connected with earlier encounters. Worth checking.|
N~Look at the trainers and their teams. Familiarity is useful, but fit still matters.|
S~I'd feel less nervous if someone I knew was waiting there.|
S~It would be nice to see how someone has grown since the last time we met.|
S~An ordinary partner search may unexpectedly turn into a reunion. A superior use of a waiting room.|
S~The crowd may contain someone who already knows our peculiarities. Efficient matchmaking.|
N~We should inspect the partner's available Pokemon and moves before committing.|
S~Paths cross again in odd rooms. It's worth looking up before passing through.|
S~A familiar person can change the whole feeling of an unfamiliar place.|
S~I'd like to hear what brought them back. A reunion deserves more than a quick team check.
''')
add('link_multi', 'BattleFrontier_Lounge2_Text_LinkMultiBattleAdvice', 'The Maniac recommends the Link Multi challenge for battling beside a strong friend.', '''
S~Bring a strong friend and the Tower supplies a stronger reason to talk tactics together.|
N~A known partner allows deliberate coordination, though the opposition scales into a serious challenge.|
N~Agree on the plan before the first battle. Friendship won't read minds.|
S~It sounds easier to face a tough room with someone I already trust beside me.|
S~I'd want us both comfortable saying when the plan needs to change.|
S~A friendship offered the opportunity to conduct a very organized disagreement with strangers.|
S~A fine test of companionship, provided neither mistakes blame for strategy.|
N~We can coordinate complementary partners and avoid conflicting moves before entering.|
S~Trust is a good beginning. Listening is how it survives the difficult part.|
S~A strong friend should also be someone you can talk honestly with after a mistake.|
S~I'd ask them how they work out a plan together. That's the part I'm most curious about.
''')
add('nature_attack_attack', 'BattleFrontier_Lounge5_Text_NatureGirlAttackHighAttackLow', 'The girl says this partner prefers attacking even when badly hurt.', '''
N~A determined little fighter. We'll have to notice when determination needs a pause.|
N~She describes a persistent attack preference under pressure, not immunity to injury.|
N~It may keep attacking. We still need to protect it.|
N~That sounds brave, but I'd want it to know stopping isn't disappointing us.|
N~Some partners don't ask for a break. We ought to pay attention anyway.|
N~A stirring commitment to battle, accompanied by an unfortunate lack of self-preservation paperwork.|
N~Stubborn courage. Useful, until it begins negotiating on behalf of an exhausted body.|
N~We can prepare suitable offensive options without assuming it'll choose recovery when needed.|
N~A flame can keep reaching upward after the wick has nearly gone. Watch closely.|
N~It's easy to admire that drive and forget the little creature carrying it.|
N~I'd compare her reading with what we've actually noticed when the partner is tired.
''')
add('nature_attack_defense', 'BattleFrontier_Lounge5_Text_NatureGirlAttackHighDefenseLow', 'The girl says this attacking partner becomes protective of itself when hurt.', '''
S~It likes a good fight and also has an opinion about when enough is enough. Sensible.|
N~Her reading predicts a shift from offense toward self-protection as its condition worsens.|
N~Expect the preference to change under pressure. Plan for both parts.|
S~I'm glad there's room for looking after itself in that brave little personality.|
S~Wanting to battle and wanting to be safe can belong to the same partner.|
S~An enthusiastic combatant with a functioning complaints department. Excellent.|
S~It has discovered that enthusiasm and preserving oneself aren't natural enemies.|
N~A defensive option may become more useful once its priorities shift.|
S~A bold step can become a careful one without ceasing to belong to the same creature.|
S~That change sounds understandable. I'd rather notice it than call it losing nerve.|
N~I'd watch for the first sign that it wants to protect itself. That could tell us plenty.
''')
add('nature_attack_support', 'BattleFrontier_Lounge5_Text_NatureGirlAttackHighSupportLow', 'The girl says this aggressive partner turns toward indirect tactics when hurt.', '''
S~It starts with a brawl and keeps a little bag of trouble for when the brawl gets uncomfortable.|
N~The reported preference shifts from direct attacks to interference under pressure.|
N~Give it useful options for both approaches.|
N~I wonder whether it looks different when it starts trying to outwit the opponent.|
S~Changing tactics can be wiser than simply trying to hit harder while worn out.|
S~A straightforward fighter with a concealed second opinion about straightforward fighting.|
S~When enthusiasm encounters pain, cunning has been asked to take over.|
N~We should account for the lower-condition preference when checking its available moves.|
N~A straight path can bend around a thorn. That is still a way forward.|
N~I'd be careful not to treat that shift as disobedience. It may be the partner adapting.|
N~I'd ask what she notices that tells her the difference between those two moods.
''')
add('nature_defense_attack', 'BattleFrontier_Lounge5_Text_NatureGirlDefenseHighAttackLow', 'The girl says a self-protective partner starts attacking when sufficiently hurt.', '''
N~A careful little one, right up until somebody spends too long testing its patience.|
N~She predicts a reversal from defensive choices toward attack under pressure.|
N~Cautious doesn't mean harmless. Remember that.|
N~I understand being quiet until something finally pushes too far.|
N~I'd rather keep it comfortable than rely on hurting it to bring that side out.|
N~A reserved partner with a rather emphatic final response to persistent inconvenience.|
N~The boundary is polite until it isn't. A familiar arrangement.|
N~Its offensive options should remain useful even if it seldom favors them at first.|
N~A sheltered creature may still have teeth behind the door.|
N~People mistake self-protection for weakness until the expression changes.|
N~I'd watch how it signals discomfort before that switch. There may be earlier clues.
''')
add('nature_defense_defense', 'BattleFrontier_Lounge5_Text_NatureGirlDefenseHighDefenseLow', 'The girl says this partner consistently favors protecting itself.', '''
S~This little one has read the safety instructions and intends to keep the booklet.|
N~The reading suggests a stable defensive preference across different levels of pressure.|
N~It values staying safe. Work with that instead of fighting it.|
S~I don't think wanting to protect itself is something to be embarrassed about.|
S~A careful partner deserves a plan that doesn't demand constant recklessness.|
S~A consistent philosophy, apparently untroubled by the audience's appetite for spectacle.|
S~Self-preservation remains in fashion through every stage of the encounter.|
N~We can check whether the moves give that preference productive options.|
S~Some creatures carry their shelter with them in the choices they make.|
N~I'd rather understand its caution than dress it up as a personality flaw.|
N~I'd compare the reading with how it behaves outside battles. The contrast could be interesting.
''')
add('nature_defense_support', 'BattleFrontier_Lounge5_Text_NatureGirlDefenseHighSupportLow', 'The girl says a protective partner turns to indirect interference when hurt.', '''
S~First it minds its own business. Then it makes the opponent's business considerably more difficult.|
N~The predicted shift is from self-protection toward disrupting the opponent under pressure.|
N~Cautious first, disruptive later. We can prepare around that.|
N~It sounds as though it changes from hiding the trouble to trying to control it.|
N~A good plan should give it useful choices before and after that change.|
S~A private little creature with a practical backup policy of becoming somebody else's problem.|
S~The careful partner keeps a small reserve of mischief for emergencies. Sensible.|
N~We should inspect the support options instead of assuming defensive moves cover both preferences.|
N~When the shelter stops feeling safe, the hands begin rearranging the shadows outside.|
N~I like knowing there's more to it than the first cautious impression.|
N~I'd ask how she distinguishes protective behavior from the later indirect tactics.
''')
add('nature_support_attack', 'BattleFrontier_Lounge5_Text_NatureGirlSupportHighAttackLow', 'The girl says an indirect tactician attacks directly when hurt.', '''
S~A sneaky start, then a very direct complaint if things get painful. Quite clear by the end.|
N~Her reading predicts a shift from interference toward direct offense under pressure.|
N~Don't leave it without an attack it can actually use.|
N~I wonder whether the opponent ever notices the change before it happens.|
N~I'd give that partner room for both cleverness and a straightforward answer.|
S~The subtle approach has a point at which it formally resigns and hands over to force.|
S~Mischief, followed by a firm rejection of further subtlety.|
N~The moves should support the change rather than leave the favored late approach unavailable.|
N~A winding path can end in one very straight line.|
N~It may look playful at first. That doesn't mean every later choice will stay playful.|
N~I'd watch for the point where its attention changes. The transition might be easy to miss.
''')
add('nature_support_defense', 'BattleFrontier_Lounge5_Text_NatureGirlSupportHighDefenseLow', 'The girl says an indirect tactician becomes self-protective when hurt.', '''
S~It enjoys making trouble until trouble gets personal. Then it quite reasonably checks the exits.|
N~The described preference changes from disruption toward self-protection under pressure.|
N~A defensive option matters once it's worn down.|
S~It can be clever and still need somewhere safe when the battle turns hard.|
N~I'd rather help it protect itself than expect the mischief to last forever.|
S~A cunning opening, with a sensible clause reserving the right to look after oneself.|
S~The prankster has discovered personal consequences and adjusted the program.|
N~We should plan for both preferences instead of giving it only interference moves.|
S~A creature can enjoy stirring the water and still seek a quiet bank afterward.|
N~Its playful side doesn't cancel the need for care when it's struggling.|
N~I'd ask whether her reading matches the partner's habits in unfamiliar places, too.
''')
add('nature_support_support', 'BattleFrontier_Lounge5_Text_NatureGirlSupportHighSupportLow', 'The girl says this partner prefers indirect tactics even when hurt.', '''
S~A committed little schemer. Even a difficult afternoon apparently can't interrupt the plotting.|
N~She reports a consistent interference preference regardless of the pressure state.|
N~Give it useful indirect options. Still watch its condition.|
N~I wonder whether it enjoys the clever part more than the battle itself.|
N~Keeping a familiar approach may help it feel steady. We still need to know when to stop.|
S~A dedicated specialist, unwilling to abandon the elegant nuisance even under duress.|
S~Mischief has survived the emergency review and remains official policy.|
N~We should check that the available support moves can accomplish something under Palace rules.|
N~Some creatures keep tying knots even while the wind pulls hard at the thread.|
N~It's a distinct little personality. I'd want the plan to respect it without demanding too much.|
N~I'd watch which tactics it returns to most often. Repetition can reveal a preference clearly.
''')
add('tower_no_interview', 'BattleFrontier_BattleTowerLobby_Text_DontThinkMuchAboutIt', 'The interviewer interprets declining to discuss battle feelings as cool detachment.', '''
N~We've said very little and somehow acquired an entire calm personality. Quick work.|
N~Declining an interview doesn't establish an absence of strong feelings.|
N~Not talking about it isn't the same as not caring.|
N~Sometimes I feel too much to explain it neatly to a stranger.|
N~We can keep a feeling to ourselves without needing a flattering explanation for it.|
N~An unanswered question has been converted into a character study. Economical journalism.|
N~Silence has been assigned a fashionable interpretation without consulting its owner.|
N~The information wasn't collected. A conclusion about temperament goes beyond the evidence.|
N~A closed mouth can hold an entire storm. Stillness isn't a weather report.|
N~Cool customer sounds nice. It still isn't something we actually told him.|
N~I'd rather leave the question open than have a quick label stand in for an answer.
''')
add('tower_cancel_interview', 'BattleFrontier_BattleTowerLobby_Text_ChangedYourMind', 'The interviewer calls the player fickle after a canceled answer.', '''
N~Changing one answer has apparently changed our whole reputation. That's an efficient notebook.|
N~A canceled response may reflect uncertainty or privacy. Fickleness is only one interpretation.|
N~We're allowed to change our mind about an interview.|
F~I don't always find the right words on the first try. That shouldn't be a fault.|
N~If someone can't answer comfortably, pushing a label onto them won't help.|
N~The interview has ended with an unsolicited review of our decision-making character.|
N~A blank answer has displeased the questionnaire. The questionnaire will recover.|
N~Stopping an incomplete answer is better than recording something misleading.|
N~Some words don't want to be set down just because a box is waiting.|
N~He could leave room for hesitation without making it sound like a flaw.|
N~I'd rather give a considered answer later than force a quick one now.
''')
add('tower_interview_done', 'BattleFrontier_BattleTowerLobby_Text_ThatsHowYouFeel', 'The interviewer thanks the player after receiving a battle-feelings answer.', '''
S~The feeling has been safely delivered to the notebook. I hope it behaves in there.|
S~He has accepted the response without demanding a different emotional account. Good.|
S~Question answered. Nice to get a simple thanks.|
S~I'm glad he let the answer belong to us instead of explaining it back.|
S~A small honest answer can be enough. Not every interview needs a grand revelation.|
S~An original contribution to the public record of people being nervous about battles.|
S~The emotion has been documented. It may now return to ordinary employment.|
N~The answer is submitted. We can see whether our feelings change after more experience.|
S~A feeling put into words can look slightly different once it's resting outside us.|
S~He noticed the answer as an individual one. That's a pleasant way to close.|
S~I'd be interested to compare what people say before and after their first difficult match.
''')
add('tower_record_shame', 'BattleFrontier_BattleTowerLobby_Text_WinsInRowRecorded', 'A woman worries a recorded streak makes an embarrassing defeat more consequential.', '''
N~The record keeps the wins. Her imagination seems determined to keep an illustrated loss as well.|
N~The numerical record doesn't capture every detail of a defeat. Her concern adds an imagined audience.|
N~A loss is a result. It doesn't have to become a public disgrace.|
N~I understand worrying about how a mistake will look. It can make the room feel crowded.|
N~She might enjoy the battles more if she leaves a little room to be human.|
N~A simple streak counter has acquired an exceptionally severe critic living inside it.|
N~The number is recorded. The embarrassment appears to be self-administered.|
N~She can use the record to measure progress rather than predict humiliation.|
N~A tally can become a mirror if you stare at it too long.|
N~I'd hate for the fear of looking awkward to keep her from trying something useful.|
N~I'd ask what she considers embarrassing. The standard may be much harsher than anyone else's.
''')
add('tower_commitment', 'BattleFrontier_BattleTowerLobby_Text_CanLeaveUntilLossOrSevenWins', 'A boy advises being ready for the Tower round commitment.', '''
N~That's a longer appointment than just poking our heads through the door. Good to know.|
N~A full round requires planning, with formal suspension distinct from simply leaving.|
N~Know the commitment before entering. Don't wander in half-ready.|
N~I like being warned before finding out I can't simply step away.|
N~We should settle food, rest, and whatever else needs doing before starting.|
N~The Tower asks that curiosity make an actual appointment before entering.|
N~A casual visit has discovered a rather firm closing clause.|
N~We can prepare for the full sequence and learn the proper suspension procedure.|
N~A doorway can ask more of us than the first room reveals.|
N~Clear expectations make it easier to choose without feeling trapped later.|
N~I'd ask the attendant exactly how to pause properly before we begin.
''')
add('reception_wish', 'BattleFrontier_ReceptionGate_Text_EnjoyBattleFrontier', 'The greeter or information guide ends by wishing the visitor enjoyment of the Frontier.', '''
S~Seven big challenges and permission to enjoy ourselves between them. I'll keep both parts.|
S~The guide leaves the destination to us after providing the available information.|
S~Good. We can choose our own pace from here.|
S~I like that the farewell is about enjoying the visit, not proving something.|
S~A good day can include a challenge and a quiet break. No need to fill every minute.|
S~A pleasantly broad assignment. I intend to include something comfortable in our interpretation.|
S~Enjoy everything is ambitious. I'll begin with one manageable thing.|
N~We can choose a facility after checking its rules and our team's readiness.|
S~An open welcome is a gentler threshold than a demand to be impressive.|
S~They've made space for the visit to mean different things to different people.|
S~I'd take a little time to look around before choosing where to start.
''')
add('reception_scott', 'BattleFrontier_ReceptionGate_Text_ScottGreatToSeeYouHere', 'Scott welcomes the player, encourages exploration, and invites a visit to his quarters.', '''
S~Scott's dream has actual doors now, and he's invited us through several of them.|
S~His personal welcome connects the facilities to the long project that brought him here.|
S~We'll look around. No need to sprint straight into a challenge.|
S~He seems genuinely happy we came. That's a nice way to enter an unfamiliar place.|
S~I'd visit him after settling in. He must have plenty of stories about getting this ready.|
S~A proud host has remembered to include visiting his own cramped quarters in the grand itinerary.|
S~The invitation has finally grown into an entire island. Scott seems pleased with the proportions.|
U~I'd like to ask how the place went from an idea to all these working facilities.|
S~A long-carried wish has become somewhere other people can walk. He deserves a moment to enjoy that.|
S~He wants us to see the whole place instead of just chasing a result immediately.|
S~I'd ask which corner he'd show a first-time visitor himself. The answer would tell us what he loves.
''')
add('scott_silver_reward', 'BattleFrontier_ScottsHouse_Text_YouveCollectedAllSilverSymbols', 'Scott recognizes the complete silver Symbol set and successfully gives a Lansat Berry.', '''
U~Seven silver Symbols have turned Scott's ordinary greeting into a very excited inspection.|
S~The complete set represents success across seven distinct formats. A substantial breadth of skill.|
S~Every silver Symbol earned. Good work deserves a quiet moment.|
S~I like how genuinely surprised he sounds, even after saying he believed in us.|
S~A little Berry carries a lot of effort behind it now. We'll look after the gift.|
S~Scott suspected greatness and is still rather delighted to encounter the evidence in person.|
S~Seven hard-earned marks have produced one very enthusiastic man and a Berry.|
S~Success across different rules means the team adapted repeatedly. That's worth recognizing.|
S~Seven small signs hold a very long path between them.|
S~He noticed the whole set before we needed to announce it. That feels good.|
S~I'd ask which accomplishment surprised him most. He sounds ready to tell us.
''')
add('scott_gold_reward', 'BattleFrontier_ScottsHouse_Text_YouveCollectedAllGoldSymbols', 'Scott recognizes the complete gold Symbol set and successfully gives a Starf Berry.', '''
U~Scott has checked his eyes, checked the pass, and apparently run out of ordinary compliments.|
S~Completing every gold Symbol demonstrates repeated success under the Frontier's strongest tests.|
S~The whole gold set. We know what each one cost to earn.|
S~He went quiet for a moment. I think that was the most sincere part.|
S~That's a gift worth keeping carefully. Not because it replaces all the work behind it.|
U~A collector of exceptional trainers has encountered evidence that briefly exceeds his prepared vocabulary.|
S~The pass has startled the man responsible for inventing reasons to fill it.|
S~The complete set reflects adaptability and persistence, not just one favorable matchup.|
S~Gold doesn't show every tired step. We remember those even when the light catches it.|
S~I like the moment when his practiced confidence turns into genuine astonishment.|
S~I'd want to hear everyone's memory of the hardest part. The set means something different from each angle.
''')
add('scott_berry_full', 'BattleFrontier_ScottsHouse_Text_BerryPocketStuffed', 'Scott cannot give the achievement Berry because the Berry pocket is full.', '''
N~The achievement fits on the pass. Its Berry reward is having a harder time fitting anywhere.|
N~The reward wasn't delivered. Capacity, rather than eligibility, is blocking it.|
N~Make room in the Berry pocket. We can collect it later.|
N~It's a small delay after a big achievement. Nothing we've earned has changed.|
N~Let's sort the Berries carefully. No reason to waste something useful just because we're excited.|
N~A remarkable accomplishment has been briefly stalled by a very ordinary inventory problem.|
N~The celebration has encountered the practical limits of fruit storage.|
N~We need a suitable free slot before repeating the collection step.|
N~A full pocket can pause a gift without diminishing the hands that earned it.|
N~I appreciate a clear explanation. We don't have to wonder whether the reward disappeared.|
N~I'd check what we can use or store before returning. A simple plan should settle it.
''')
add('scott_after_berry', 'BattleFrontier_ScottsHouse_Text_SoGladIBroughtYouHere', 'After the Berry reward, Scott congratulates himself for recognizing the player talent.', '''
S~He's proud of us and has very kindly saved a second serving of pride for himself.|
N~His invitation helped create the opportunity. The performance still belongs to the trainer and team.|
S~He made a good call. We did the battles. Both can be true.|
S~He sounds happy to have been right about someone. That's rather human.|
S~I'm glad his welcome led somewhere good. The team still deserves most of this praise.|
L~An excellent achievement, now featuring a brief commemorative tribute to Scott's judgment.|
S~Our success has earned Scott a small personal trophy in his own mind.|
N~Spotting talent matters, but so does what happened after the invitation.|
S~He planted the welcome. Many other hands tended what grew after it.|
S~He's slipping himself into the congratulations. At least he's cheerful about it.|
S~I'd ask what first caught his attention. Now would be a good time for a specific answer.
''')
add('scott_shield_end', 'BattleFrontier_ScottsHouse_Text_ExpectingToHearEvenGreaterThings', 'After the shield reward, Scott expresses expectations for future achievements.', '''
S~We've received a shield and immediately been assigned a larger supply of expectations. Busy gift.|
N~He acknowledges the current achievement while predicting further progress. The prediction isn't an obligation.|
N~Good to be recognized. We can still choose the next goal ourselves.|
N~I'm glad he's pleased. I hope we can enjoy this before thinking about being greater again.|
S~A reward deserves a little time to be simply enjoyed, without becoming the next deadline.|
S~The congratulations have barely sat down before the expectations are standing up again.|
S~The shield blocks attacks. Its effectiveness against ambitious compliments remains untested.|
N~We can evaluate the next challenge after reviewing the effort that earned this recognition.|
S~A milestone can be a resting place before it becomes a sign pointing onward.|
N~Belief is encouraging when it leaves someone room to set their own pace.|
S~I'd take time to remember what we just accomplished before asking what comes next.
''')
add('scott_shield_full', 'BattleFrontier_ScottsHouse_Text_ComeBackForThisLater', 'Scott postpones the shield gift because decoration storage has no room.', '''
N~A shield waiting for a place to stand. Even an honor needs a little floor space.|
N~The decoration hasn't been received. Scott explicitly leaves collection open for later.|
N~We'll make room and return. The achievement isn't going anywhere.|
N~I'm glad he made it sound like a delay instead of losing the chance.|
N~We can look through what we already have before deciding where the shield belongs.|
N~A hard-earned honor is waiting in the temporary department of furniture logistics.|
N~The shield has been defeated by a complete lack of shelf space. A humiliating matchup.|
N~We should free a decoration slot, then repeat the gift collection.|
N~A place must be made before a new memory can sit among the old ones.|
N~I'd rather choose its place thoughtfully than cram it into whatever corner happens to open.|
S~A return visit will give us another chance to hear Scott sound proud. That's no hardship.
''')
add('scott_points_explain', 'BattleFrontier_ScottsHouse_Text_ExplainBattlePoints', 'After giving introductory points, Scott explains earning and spending Battle Points.', '''
S~A little starting help and directions to the prize counter. Scott understands a welcoming packet.|
N~The points are credited, and the Pass provides a way to check the balance. Useful orientation.|
N~We have the points. We'll choose what to spend them on.|
S~I like that he leaves the choice with us after explaining it.|
S~We don't need to spend them immediately. A useful thing later can be a good first choice.|
S~The grand welcome has acquired a practical allowance and a clear set of spending instructions.|
S~A small purse of possibilities. The cushions are presumably already campaigning.|
N~We can compare rewards with their costs before setting a longer-term point goal.|
S~A gift can remain a possibility for a while. It needn't become an object at once.|
S~Choose as we see fit is a pleasant thing to hear from someone giving a gift.|
N~I'd look through the exchange choices before deciding which points goal feels worthwhile.
''')
add('scott_points_repeat', 'BattleFrontier_ScottsHouse_Text_ExpectingGreatThings', 'After the introductory gift, Scott enthusiastically expects future achievements.', '''
S~Scott's optimism has apparently booked a very long stay. We'll take the first challenge first.|
N~He is expressing confidence rather than reporting a future result. The work remains ahead.|
N~We'll do the work at our own pace.|
N~It's nice to be believed in. It's also a little heavy when someone says it that confidently.|
S~I'd like us to enjoy the visit while we discover what we're actually ready for.|
S~A concise statement containing an impressively large quantity of future pressure.|
S~Great things are expected. Ordinary lunch remains necessary in the meantime.|
N~A useful next step is choosing one facility and learning its specific rules.|
N~A hopeful gaze can feel warm and weighty at the same time.|
N~He means it kindly. We still get to decide what success should look like for us.|
S~I'd ask what he enjoys seeing in a first-time challenger besides the final result.
''')
add('scott_brains_comment', 'BattleFrontier_ScottsHouse_Text_HaveYouMetFrontierBrain', 'Scott praises his handpicked Frontier Brains and expects the player to impress them.', '''
S~He picked the toughest people he could find, then invited us to surprise them. Mischievous host.|
N~His confidence suggests a serious test, but it doesn't replace information about each specialist.|
N~They were chosen for a reason. We'll prepare instead of relying on his confidence.|
N~I wonder which of them was hardest for him to persuade to come here.|
S~He seems proud of everyone involved. I'd like the challengers to feel welcome as well as tested.|
S~The proud organizer is preparing to watch his carefully selected experts be startled by his other discovery.|
S~He has assembled both sides of the problem and seems delighted with himself.|
N~I'd ask how their specialties shaped the different facilities. That could guide our preparation.|
N~Seven strong wills gathered by one persistent invitation. The meetings must have been interesting.|
N~He makes the place sound like a collection of people he genuinely admires.|
S~I'd ask him to tell us about recruiting one of them. Those stories won't appear on a record board.
''')
add('scott_wild_hint', 'BattleFrontier_ScottsHouse_Text_MayFindWildMonsInFrontier', 'Scott hints that wild Pokemon can be found somewhere within the Frontier.', '''
S~He's hidden a little nature walk inside his enormous battle invitation. Sneaky hospitality.|
N~A useful habitat lead, though he hasn't specified the species or exact location.|
N~We'll look carefully. No reason to charge after an unknown encounter.|
S~I'm glad there's something here that didn't come just to enter a tournament.|
S~A quiet search could be a welcome change from the buildings and crowds.|
S~An island of organized contests has retained a few residents who declined to register.|
S~The wildlife has apparently ignored the admission criteria. Admirable independence.|
N~We can investigate accessible areas and note any actual sightings rather than assume the species.|
S~Even a place built for people has corners that answer to something else.|
S~He remembered another interest of ours. That makes the hint feel personal.|
U~I'd ask where people last saw something unusual, then explore without disturbing its shelter.
''')
add('pike_hint_decline', 'BattleFrontier_BattlePikeThreePathRoom_Text_ApologizeForImpertinence', 'The Pike hint attendant apologizes after the player declines advice.', '''
S~An offer, a no, and a perfectly polite retreat. A very well-behaved fork in the road.|
S~The attendant accepts the refusal without insisting that guidance is needed.|
S~No offense taken. We can choose for ourselves.|
S~I like that saying no doesn't make the room uncomfortable.|
S~It's considerate to offer help and just as considerate to let someone decline.|
S~Advice withdrawn with such elaborate courtesy that I feel we ought to thank the punctuation.|
S~The guidance has stepped back without haunting us about it.|
N~We can use our own judgment. The declined hint doesn't reveal anything about the rooms.|
S~A hand offered and gently withdrawn leaves the path open.|
S~They left our choice intact. Good manners can be that simple.|
S~I'd remember the offer if we wanted advice on another visit.
''')
add('pike_hint_aroma', 'BattleFrontier_BattlePikeThreePathRoom_Text_AromaOfPokemon', 'The attendant reports a Pokemon scent from the indicated path without guaranteeing its outcome.', '''
N~A Pokemon smell is a clue. My nose would probably submit the much less useful report of smells indoors.|
N~The scent is a hint category, not a complete account of what the room contains.|
N~A clue, not a promise. Stay prepared.|
N~I wonder how long they've worked here to recognize a path by its smell.|
N~I'd use the hint without treating the room as safe before we've seen it.|
N~The report is fragrant and deliberately incomplete. A distinctive information service.|
N~The corridor has offered an aroma instead of a guarantee. Sensible of it.|
N~We can weigh this clue against the team's current condition before choosing.|
N~A scent arrives before its source. It doesn't always tell the whole story.|
N~The uncertainty is part of the advice. I wouldn't trim it away just to feel confident.|
N~I'd ask what they've actually smelled there before. Experience may make the hint more useful.
''')
add('pike_hint_people', 'BattleFrontier_BattlePikeThreePathRoom_Text_PresenceOfPeople', 'The attendant senses people or a possible trainer down the indicated path.', '''
N~Someone ahead. Whether they brought a battle or just conversation remains annoyingly important.|
N~The attendant reports a human presence while remaining uncertain about the role.|
N~People ahead. Keep the team ready without assuming a fight.|
N~I think the pause before trainer matters. They aren't certain.|
N~It might be help or a challenge. We should choose with enough strength for either.|
N~The report confirms possible company while declining to guarantee the quality of the visit.|
N~A person may be waiting. Humanity continues its excellent record of being ambiguous.|
N~A human presence narrows the possibilities without settling the encounter.|
N~A presence behind a door can be a welcome or a weight. We haven't heard its voice yet.|
N~I'd listen to the uncertainty instead of remembering only the word trainer.|
N~I'd be curious what made them sense a person rather than a Pokemon.
''')
add('pike_hint_whisper', 'BattleFrontier_BattlePikeThreePathRoom_Text_HeardWhispering', 'The attendant reports possible whispering from the indicated path.', '''
N~The room is whispering and the hint is whispering about the whispering. Very discreet confusion.|
N~A tentative auditory report. It doesn't establish who produced the sound or why.|
N~Could be voices. Don't turn a sound into a certainty.|
N~I'd probably stop and listen, too. Quiet voices make me curious and nervous at once.|
N~We'll keep the team prepared. A soft sound doesn't mean a gentle encounter.|
N~A possibly whispered message has been relayed with appropriately whispered confidence.|
N~The uncertainty is quiet, but admirably persistent.|
N~We have an observation to consider, not enough detail to deduce the room's result.|
N~A wall can make an ordinary voice sound as though it belongs to a secret.|
N~I'd avoid filling the quiet with a story more certain than what they actually heard.|
N~I'd ask whether the sound repeated. One little detail could change how we read it.
''')
add('pike_hint_nostalgia', 'BattleFrontier_BattlePikeThreePathRoom_Text_WaveOfNostaliga', 'The attendant describes an unexplained feeling of nostalgia from the indicated path.', '''
N~A corridor that feels like an old memory. I wonder whether it also remembers where we left our lunch.|
N~The reported sensation is subjective. Its meaning within this challenge still requires caution.|
N~An odd clue. We'll judge the room when we reach it.|
N~I wonder what kind of memory it brought back. They sounded surprised by it.|
N~A familiar feeling can be comforting without being a reliable promise.|
N~The directions have become unexpectedly sentimental. I hadn't packed for a reunion with a hallway.|
S~Nostalgia from an unopened room. Even the past is being coy today.|
N~We can consider the hint without assigning it an outcome we haven't observed.|
N~Sometimes a place touches a memory before we find its name. That doesn't tell us what's waiting.|
N~It's an evocative description. I'd be careful not to mistake the feeling for evidence of safety.|
N~I'd ask what felt familiar. The answer might tell us more about the attendant than the room.
''')
add('pike_hint_dread', 'BattleFrontier_BattlePikeThreePathRoom_Text_DreadfulPresence', 'The attendant senses something dreadful down every path near the Pike Queen encounter.', '''
N~All three doors have received the same unsettling review. That does simplify the comparison.|
N~The warning applies across the available paths. It doesn't identify a safer alternative.|
N~Check the team before moving. There isn't a clearly safe choice here.|
N~I don't like hearing every path described that way. At least we know to be careful.|
N~I'd take a moment to see how everyone's doing before stepping into another room.|
N~A choice of three distinct routes to one thoroughly consistent atmosphere.|
N~The doors have formed a united front of bad impressions.|
N~With no differentiated hint, preparation matters more than trying to infer a favored door.|
N~Three shadows can belong to the same waiting shape.|
N~A warning that clear deserves attention without letting it decide how frightened we have to be.|
N~I'd ask whether anything can be checked before we proceed. Practical details help when the mood turns ominous.
''')
add('pike_hint_event', 'BattleFrontier_BattlePikeThreePathRoom_Text_TerrifyingEvent', 'The attendant approaches to warn of an especially difficult event ahead.', '''
N~That's the sort of warning that makes the whole corridor sit up straighter.|
N~The attendant has singled out the next event as unusually difficult. Prepare rather than assume the result.|
N~Stop and check what we can. A warning is useful only if we act on it.|
N~They came over to tell us. That makes me take the concern seriously.|
N~I'd rather spend an extra moment getting ready than rush to look fearless.|
N~An exceptionally emphatic warning from a place that already considers giant snakes welcoming.|
N~The ordinary uncertainty has been upgraded to an official ominous announcement.|
N~We should review the team's condition and available protections before continuing.|
N~A careful voice has stepped into our path. It's worth becoming still enough to hear it.|
N~They're trying to help us prepare. We don't need to turn that into a prediction of failure.|
N~I'd focus on what we can still check instead of imagining the worst in elaborate detail.
''')
add('pike_full_heal', 'BattleFrontier_BattlePikeRoomNormal_Text_EnjoyRestOfChallenge', 'A fortunate room restores the whole team and the attendant sends the player onward.', '''
S~Everyone restored, and no battle bill attached. That's a room I'd happily recommend.|
S~The healing is complete. The next choices can be made from a much stronger condition.|
S~Whole team restored. Good break. Don't waste it by getting careless.|
S~It's a relief seeing everyone steadier before we move on.|
S~A little help at the right time can change the whole journey. Thank the attendant.|
S~A rare room whose hospitality includes precisely what tired visitors were hoping for.|
S~Good fortune has briefly become tangible and extremely welcome.|
S~We can reassess the route now that the team's immediate condition has improved.|
S~A hard path has offered a gentle hand for once.|
S~The farewell feels warmer when everyone is actually better off for the visit.|
S~I'd remember this room after the challenge. Helpful surprises deserve a place beside the difficult ones.
''')
add('pike_hard_heal', 'BattleFrontier_BattlePikeRoomNormal_Text_EnjoyRestOfChallenge2', 'After defeating the tough trainer, the team receives full healing and a farewell.', '''
S~A hard fight, then a proper recovery. Nice when a room remembers the second half.|
S~The victory was followed by full restoration. That removes the immediate condition cost of the encounter.|
S~Won the fight and recovered. Ready to think about the next choice.|
S~I'm glad the effort didn't leave everyone carrying the same exhaustion onward.|
S~A tough test is easier to appreciate after somebody helps the team recover.|
S~The demanding reception has redeemed itself with excellent aftercare.|
S~A difficult room has concluded by returning what the battle borrowed. Much appreciated.|
S~We should use the improved condition while still preparing for varied rooms ahead.|
S~A bruise can fade before its lesson does. This room has allowed that.|
S~The recovery makes the congratulations feel practical instead of merely decorative.|
S~I'd ask which choice helped us most in that fight while the details are still clear.
''')
add('pike_partial_heal', 'BattleFrontier_BattlePikeRoomNormal_Text_BestOfLuckFarewell', 'After healing one or two partners, the attendant bids the player farewell.', '''
S~Some welcome help, though we should check exactly who still needs a rest.|
N~The partial restoration has finished. This shared farewell doesn't specify whether one or two were healed.|
N~Check the team. The farewell doesn't mean everyone is restored.|
S~I'm glad somebody got help. I'd want to make sure nobody else is quietly struggling.|
N~A little recovery helps. Let's not assume it covered every partner.|
S~A courteous departure after a useful but limited amount of hospitality.|
S~Luck has provided assistance rather than a complete renovation.|
N~We need to inspect the remaining condition before selecting another path.|
S~A hand can help part of the burden without lifting all of it.|
N~I'd appreciate the help and still take stock. Both responses fit.|
N~I'd look over each partner before moving. The detail matters more than the broad farewell.
''')
add('pike_startled_attack', 'BattleFrontier_BattlePikeRoomNormal_Text_AttacksWhenStartled', 'After a startled Pokemon attacks, its trainer explains and asks whether the team is all right.', '''
N~Being startled explains the sudden attack. It doesn't check our poor team's condition for us.|
N~The explanation identifies a trigger. We should still assess the actual effects on each partner.|
N~Check the team first. Then give that Pokemon more space.|
D~It sounds frightened rather than cruel. Our partners still need looking after.|
N~I'd make sure everyone is settled before having a long conversation about what happened.|
N~A useful explanation, arriving rather late in the ideal sequence for avoiding an ambush.|
N~The apology has arrived after the damage. Timing remains a difficult art.|
N~Knowing the trigger should help prevent another incident. It doesn't undo the first one.|
N~Fear can strike outward before anyone finds its name. We should tend what it touched.|
N~I appreciate being asked. I'd also like them to keep visitors from startling it again.|
N~I'd answer after checking the team. A polite reassurance shouldn't hide a real problem.
''')
add('pike_repeat_apology', 'BattleFrontier_BattlePikeRoomNormal_Text_ApologizeHopeMonsAreFine', 'The trainer apologizes again for the earlier startled-Pokemon incident.', '''
N~The apology is kind. I'd also welcome a plan that keeps the next visitor out of the splash zone.|
N~The repeated apology acknowledges the incident, but doesn't establish that its effects are gone.|
N~We should check our partners rather than assume they're fine.|
N~I think they feel bad. I also don't want to pretend nothing happened just to comfort them.|
N~A sincere apology is a start. Helping prevent another accident would make it stronger.|
N~Regret is welcome. A little practical prevention would make an excellent companion to it.|
N~The remorse appears genuine. Unfortunately, remorse isn't a healing move.|
N~They could give the Pokemon more space and warn people before another close approach.|
N~A frightened creature needs care. So do the ones caught in its fear.|
N~We can accept the apology without calling the whole situation harmless.|
N~I'd ask how they plan to help the Pokemon feel safer around visitors.
''')
add('partner_keep_searching', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_PleaseFindPartner2', 'After declining to quit, the attendant asks the player to continue choosing a tag partner.', '''
S~The search continues. Somewhere in this room is a pair of Pokemon waiting for our very careful introduction.|
N~We chose to remain. The next task is comparing potential partners and their available teams.|
N~Take the time to choose well. No need to grab the nearest volunteer.|
N~I'd like to hear how each person talks about their partners, not just which moves they know.|
N~A good match should make both sides comfortable with the plan.|
S~The committee has declined to leave and must now resume the difficult work of choosing company.|
S~The partner search has survived its first attempt to become an exit.|
N~We can compare move interactions before committing to a team.|
S~Staying leaves the possibility open. We still have to walk toward someone.|
N~I'd choose someone we can communicate with, as well as a useful pair of Pokemon.|
S~I'd ask a little more before deciding. This room is full of potential stories and teammates.
''')
