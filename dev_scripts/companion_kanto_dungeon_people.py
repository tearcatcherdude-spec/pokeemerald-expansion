"""Kanto dungeon NPC conversations and terminal trainer follow-ups."""
ROWS=[]
EMOTIONS=dict(N='neutral',S='soft_smile',A='annoyed',F='flustered',D='sad',U='surprised',M='smug',L='laughing')
def add(key,labels,subject,lines):
    replies=[]
    for line in lines.strip().split('|'):
        line=line.strip()
        if len(line)>1 and line[1]=='~' and line[0] in EMOTIONS:line=EMOTIONS[line[0]]+line[1:]
        replies.append(line)
    assert len(replies)==11,(key,len(replies))
    ROWS.append(dict(key='kanto_dp_'+key,labels=labels.split(),subject=subject,replies=replies))

add('moon_marcos','MtMoon_1F_Text_MarcosPostBattle',
    'Marcos warns children against wandering in the dark cave.','''
N~Fair warning. The cave has been very stingy with streetlights.|
N~Visibility and navigation are legitimate concerns regardless of age.|
N~We came prepared. Still worth watching our footing.|
N~I appreciate the concern, even wrapped in that scolding tone.|
N~A little caution is reasonable when the way back is not obvious.|
N~The cave's unofficial chaperone has issued a stern review.|
N~Darkness is quite good at making familiar distances feel strange.|
N~Age is less relevant than light, supplies, and a route plan.|
N~A dark path asks people of every size to tread carefully.|
N~He could offer directions along with the disapproval.|
N~I wonder whether he has had to help someone lost here before.
''')
add('moon_josh','MtMoon_1F_Text_JoshPostBattle',
    'Josh admits entering the cave to impress girls.','''
M~A dark cave is an ambitious place to rely on being noticed.|
N~His chosen setting makes visual self-presentation unusually difficult.|
N~Hope he packed for the cave, not just the entrance.|
F~That is a rather honest explanation for an awkward plan.|
N~An outing is easier when you also enjoy the place yourself.|
M~A romantic campaign with poor lighting and an exceptionally bat-heavy venue.|
M~A long way to come to be barely visible.|
N~Requirements and environment seem poorly matched.|
N~He followed a bright idea into a very dark room.|
M~Confidence helps. So does choosing a place where people can see the outfit.|
N~I wonder whether anyone he hoped to meet actually came this way.
''')
add('moon_miriam','MtMoon_1F_Text_MiriamPostBattle',
    'Miriam fears getting lost and asks how to leave the large cave.','''
N~The mountain has more indoors than she ordered. Understandable concern.|
N~She needs reliable directions rather than reassurance without a route.|
N~Stay on a known path. Do not wander farther while unsure.|
N~It is frightening when every passage looks like a possible mistake.|
N~A calm pause and a clear route back would help.|
N~The expedition has revised its objective from discovery to finding the door.|
N~A large place can make a small uncertainty grow quickly.|
N~Stop, establish a known position, then choose the exit route.|
N~The next useful landmark may be the one that leads out.|
N~She is sensible to ask before pretending she knows the way.|
N~I wonder which entrance she came through.
''')
add('moon_jovan','MtMoon_1F_Text_JovanPostBattle',
    'Jovan wonders where to find stronger Pokemon.','''
N~The next strong partner may need some help becoming strong first.|
N~Habitat, training, and team needs all matter more than an undefined strength ranking.|
N~Look after the team he has before blaming it for the loss.|
N~I hope he is curious about new partners, not simply tired of the old ones.|
N~A better plan can help an existing team more than a hurried replacement.|
N~The casting search expands before the rehearsal schedule receives a review.|
N~Strength is easier to ask for than to define usefully.|
N~Specify the missing capability before looking for a new component.|
N~A stronger branch still needs someone to tend the roots.|
N~He might begin by noticing what his current partners already do well.|
N~I wonder what he most needs the team to handle differently.
''')
add('moon_iris','MtMoon_1F_Text_IrisPostBattle',
    'Iris says rumors of rare fossils brought her to Mt. Moon.','''
S~A treasure hunt with very old treasure. Good reason to bring patience.|
S~A fossil-bearing site can reward careful examination of ordinary-looking rock.|
N~Worth searching carefully. Fragile finds need steady hands.|
S~I understand coming a long way for a chance to find something extraordinary.|
N~A good search needs time and enough supplies to leave comfortably afterward.|
S~The mountain's oldest residents are attracting a new generation of visitors.|
S~A little of the vanished world waiting in the walls.|
S~A geological search! I would like to compare the layers.|
S~The stone may have kept a shape the world no longer walks in.|
S~A specific interest makes the cave feel like more than a shortcut.|
S~I wonder what first made her interested in fossils.
''')
add('moon_kent','MtMoon_1F_Text_KentPostBattle',
    'Kent insists he saw Team Rocket in the cave.','''
N~That makes the cave's shadows feel a little less ordinary.|
N~A direct claimed sighting is more useful than a vague rumor, though details still matter.|
N~Stay alert. Do not assume the next person down here is harmless.|
N~He sounds certain enough that I would take the warning seriously.|
N~We should keep the team ready and know our way back.|
N~The underground excursion has acquired a rather unwelcome supporting cast.|
N~Dark places do not need people deliberately making them worse.|
N~Potential hostile presence. Reassess the route and supplies.|
N~Some shadows have people inside them who mean harm.|
N~A warning worth hearing, even from someone still a little shaken.|
N~I wonder which way they were heading when he saw them.
''')
add('moon_robby','MtMoon_1F_Text_RobbyPostBattle',
    'Robby praises Zubat as a dependable partner despite its toughness to catch.','''
S~A difficult introduction can still become very good company.|
S~The effort of catching a Pokemon and its value as a partner are separate questions.|
N~Earn its trust after the catch. That is the important part.|
S~It is nice to hear someone talk about Zubat with affection instead of annoyance.|
S~A partner who knows the cave could be reassuring down here.|
S~The frequently unwelcome cave resident receives a deserved favorable review.|
S~Even a creature that startles everyone can be someone's dependable friend.|
S~A cave-adapted partner has useful capabilities. Worth understanding them.|
S~Something at home in the dark can make the dark less lonely.|
S~He seems to value the bond beyond the difficult first meeting.|
S~I wonder what Zubat did that made him trust it so much.
''')
add('moon_excavator','MtMoon_1F_Text_BrockHelpsExcavateFossils',
    'The excavator says Brock sometimes helps dig for fossils under Mt. Moon.','''
S~Brock has a second kind of rock appointment. A useful pair of interests.|
S~Field excavation benefits from practical knowledge of stone as well as careful technique.|
S~Good of him to lend a hand with the actual work.|
S~It is nice to hear what someone does outside the role everyone knows.|
S~Helping with a slow job says something good about a person.|
S~The Gym Leader's off-duty chapter includes a rather patient supporting role.|
S~Someone who knows stones is helping them tell a much older story.|
S~Relevant specialist volunteering on site. Excellent collaboration.|
S~A strong pair of hands making room for fragile old shapes.|
S~A reputation feels more rounded when you hear the ordinary details.|
S~I wonder which find Brock was most excited to help uncover.
''')
add('moon_fossil_agreement','MtMoon_B2F_Text_WellEachTakeAFossil',
    'After losing, Miguel agrees that we may each choose one fossil.','''
S~A fossil each. Much better than trying to fit all of prehistory in one pocket.|
N~The agreement establishes a clear shared allocation before either item is taken.|
N~Fair arrangement. Take one and leave the other.|
S~I am glad the argument found a calm ending.|
S~There is enough for both people to leave with something meaningful.|
S~The excavation dispute concludes with a mercifully simple division of the cast.|
S~An old world has enough room for two people's curiosity.|
N~Two resources, two claimants, explicit allocation. Straightforward.|
S~A little restraint can keep a discovery from turning bitter.|
S~He has made the choice fair without making it complicated.|
S~I wonder which one he hopes we leave for him.
''')
add('moon_fossil_selected','MtMoon_B2F_Text_ThenThisFossilIsMine',
    'After our fossil selection, Miguel takes the remaining fossil.','''
S~Two explorers, two fossils, and no prehistoric tug-of-war. Good finish.|
S~The agreed allocation is now complete; each person has one fossil.|
S~Deal kept. We can move on without taking more than our share.|
S~It is nice that both people get to be pleased with the discovery.|
S~A shared find can leave two good stories instead of one argument.|
S~The remaining ancient role has found its equally enthusiastic custodian.|
S~The old stones are leaving by two separate little journeys.|
N~Selection complete, remainder assigned. No ambiguity left.|
S~Two shapes from the past have begun different roads into the present.|
S~Fairness looks very ordinary when it is actually practiced.|
S~I wonder whether he will take his fossil somewhere to be examined too.
''')
add('moon_lab_lead','MtMoon_B2F_Text_LabOnCinnabarRegeneratesFossils',
    'Miguel tells us the Cinnabar laboratory studies fossil regeneration.','''
U~Our old rock has a possible next appointment on an island. Quite a journey for a fossil.|
S~A specialized laboratory is the appropriate place to investigate its potential.|
N~Useful lead. Keep the fossil safe until we can get there.|
S~The thought of that old shape moving again is difficult to imagine.|
N~A remarkable possibility deserves patience and careful handling.|
S~The prehistoric discovery has acquired a promising next chapter and a distant address.|
S~A little trace of the old world may yet have somewhere new to go.|
U~Regeneration research! The lab should have better answers than our guesses.|
S~Something that rested in stone may be carried toward another beginning.|
N~A clear recommendation makes a strange find easier to take seriously.|
S~I wonder how Miguel first heard about that laboratory.
''')
add('moon_blacklist','MtMoon_B2F_Text_Grunt1PostBattle',
    'The defeated grunt threatens to put us on Team Rocket\'s blacklist.','''
N~A list of people they dislike. We seem to have arrived with suitable qualifications.|
N~The threat indicates ongoing hostility rather than a harmless complaint.|
N~Stay alert. His threat does not make letting him hurt people acceptable.|
N~I do not like being threatened in a place with so few exits.|
N~Best keep moving together and stay aware of the route out.|
M~A disreputable organization has expressed disappointment in our compatibility.|
N~An unpleasant little honor, with potential practical consequences.|
N~Hostility recorded. No reason to remain within easy reach.|
N~A name on a cruel person's list is still our own name.|
N~We do not need his approval. We do need to be careful.|
N~I wonder how much of that threat he can actually act on.
''')
add('moon_associates','MtMoon_B2F_Text_Grunt2PostBattle',
    'The grunt threatens retaliation from his associates.','''
N~He has outsourced the next threat to people who are not even in the conversation.|
N~The possibility of accomplices warrants attention even if the statement is bluster.|
N~Keep together. Watch for his friends rather than arguing with him.|
N~That makes the passages ahead feel less comfortable.|
N~We should not let him draw us into standing here longer.|
N~The defeated speaker announces that the sequel has a larger cast.|
N~An unpleasant promise of more unpleasant company.|
N~Potential group threat. Reassess before continuing farther.|
N~The cave can hold more than one sharp voice.|
N~He is trying to borrow strength from people elsewhere. We can still be cautious.|
N~I wonder whether his associates know what happened yet.
''')
add('moon_fossil_demand','MtMoon_B2F_Text_Grunt3PostBattle',
    'The defeated grunt still demands that we surrender any fossil we find.','''
N~He lost the battle and kept the unreasonable shopping request.|
N~The demand does not establish any legitimate claim to a discovery.|
A~No. He does not get to steal what someone else finds.|
N~That is not an offer. We should keep our distance.|
A~A threat does not turn somebody else's work into his property.|
N~The extortion script survives a performance that should have discouraged it.|
N~An entitlement so stubborn it has outlasted its own argument.|
N~Unauthorized resource claim. No transfer warranted.|
N~A hand held out for taking is not the same as a hand offered in help.|
A~He can stop ordering us about. The fossil is not his.|
N~I wonder how many people he has frightened with the same demand.
''')
add('moon_ancient_residents','MtMoon_B2F_Text_Grunt4PostBattle',
    'A grunt notes that Pokemon lived here before humans arrived.','''
N~True. A useful thought to remember before barging in and taking everything.|
N~The observation places the current habitat in a much longer ecological history.|
N~Then show some respect for the residents who are still here.|
S~It makes the cave feel less empty, knowing how long it has been a home.|
N~We are visitors, whatever brought us underground.|
N~An unexpectedly thoughtful line from a very unthoughtful expedition.|
S~The stone remembers company older than our footsteps.|
N~A long-established habitat deserves more care than a convenient resource site.|
S~We are late arrivals in a house with very old rooms.|
N~A good fact. I wish the group acted like it mattered.|
S~I wonder what traces of those earlier lives remain around us.
''')
add('rock_lenny','RockTunnel_1F_Text_LennyPostBattle',
    'Lenny warns that occasional Onix in the tunnel can be dangerous.','''
N~A very large surprise for something that appears only occasionally.|
N~Low frequency does not imply low risk when the encounter itself is powerful.|
N~Watch the passage. Give an Onix room if one appears.|
N~That is a useful warning to have before the stone starts moving.|
N~A calm route plan should include room for an unexpected strong opponent.|
N~The cave may introduce a guest star with substantially greater dimensions.|
N~A rare encounter can still leave a very common bruise.|
N~High-consequence hazard, low observed frequency. Still plan for it.|
N~A stone wall can sometimes decide to become a neighbor.|
N~Worth remembering while the tunnel feels quiet.|
N~I wonder where he last saw one.
''')
add('rock_oliver','RockTunnel_1F_Text_OliverPostBattle',
    'Oliver is taking Rock Tunnel because a sleeping Pokemon blocks Route12.','''
N~One nap has made a remarkable number of other people do extra walking.|
N~A blocked route has shifted traffic onto a longer underground alternative.|
N~A detour is better than trying to force past a large sleeping partner.|
N~That must have been frustrating when he had a simpler day planned.|
N~I hope he packed enough for the longer way round.|
N~An unconscious traveler has rewritten several conscious travelers' itineraries.|
M~A single sleeper has become an unusually effective regional planning department.|
N~Access blocked. The alternative route has different supply and visibility needs.|
N~One still body can send many moving feet through the mountain.|
N~A route change is easier to accept when you know before leaving town.|
N~I wonder how many people down here are making the same detour.
''')
add('rock_lucas','RockTunnel_1F_Text_LucasPostBattle',
    'Lucas praises our ability and says we are fit to hike.','''
S~We have passed the very official mountain-walking audition.|
S~He seems to connect our preparation in battle with competence on the trail.|
N~Good of him. Still need to mind the route.|
S~A bit of encouragement feels nice in such a dark place.|
N~The next stretch still deserves a steady pace and a rested team.|
M~The mountain's informal admissions committee has approved our application.|
S~A kind word leaves the tunnel feeling a little less severe.|
N~Positive assessment noted. Keep the safety checks anyway.|
S~A voice along the path has decided we belong on it.|
S~A straightforward compliment without an extra challenge attached.|
S~I wonder how long he has been hiking this route.
''')
add('rock_ashton','RockTunnel_1F_Text_AshtonPostBattle',
    'Ashton plans to catch a Zubat while continuing through the tunnel.','''
S~A new cave companion could make the rest of the dark less lonely.|
N~Zubat is adapted to the environment, though forming a partnership takes more than catching it.|
N~Give it a good home if he does. It is more than a tunnel souvenir.|
S~It is nice to leave a loss still curious about the next meeting.|
N~A new partner deserves a plan for care as well as a spare ball.|
S~The journey may acquire a local expert with wings.|
S~The cave's familiar shadow might become someone's familiar friend.|
N~Local candidate identified. Check whether its capabilities fit his team.|
S~Something comfortable in the dark can travel out beside him.|
N~A good choice if he likes the actual Pokemon, not just the convenience.|
S~I wonder what caught his attention about Zubat.
''')
add('rock_leah','RockTunnel_1F_Text_LeahPostBattle',
    'Leah reports seeing Machop in Rock Tunnel.','''
S~A little local strongperson. Good to know who else shares the tunnel.|
N~A direct sighting provides a useful lead for anyone studying local species.|
N~Worth watching for. Give it space if we meet it.|
S~One sighting can make a familiar tunnel feel more alive.|
N~A new meeting is worth approaching calmly.|
S~The cave has introduced another possible member of its resident cast.|
S~A little life going on with its own business somewhere in the rock.|
S~Field observation recorded. I would ask where in the tunnel.|
S~The mountain has more neighbors than the echoes reveal.|
S~A useful detail, plainly offered.|
S~I wonder what Machop was doing when she saw it.
''')
add('rock_dana','RockTunnel_1F_Text_DanaPostBattle',
    'Dana admits underestimating us because we looked cute and harmless.','''
M~A soft-looking exterior has survived the performance review with a few surprises.|
N~Her first impression was an unreliable estimate of battle capability.|
N~Look at what someone does before deciding what they can do.|
F~Cute and capable do not have to cancel each other out.|
S~A gentle appearance can belong to somebody who works very hard.|
M~The packaging has been accused of concealing an unexpectedly strong contents list.|
M~Harmless-looking is a useful disguise when it comes naturally.|
N~Visual assessment failed. Update the model with actual results.|
S~A small flower can grow through a surprisingly stubborn stone.|
M~Cute was accurate. The assumption attached to it needed work.|
S~I wonder which part of the battle changed her mind most quickly.
''')
add('rock_ariana','RockTunnel_1F_Text_ArianaPostBattle',
    'Ariana feels hot and sweaty after the battle.','''
N~A cave workout with absolutely no complimentary breeze.|
N~The exertion and enclosed environment make a recovery break sensible.|
N~Take a breather. No reason to push on overheated.|
N~A cool quiet moment would be welcome right now.|
N~A drink and a little rest belong before another hard stretch.|
N~The underground venue has failed to provide adequate ventilation for the performance.|
N~The glamour of adventure continues to include very ordinary sweat.|
N~Heat buildup noted. Reduce load and allow time to cool.|
N~The still air has made the effort linger around her.|
N~A practical pause would look better than trying to pretend she is fresh.|
N~I wonder how far she has left before reaching daylight.
''')
add('rock_sofia','RockTunnel_B1F_Text_SofiaPostBattle',
    'Sofia wants to leave the tunnel and go home.','''
N~An excellent destination when the cave has become entirely too much cave.|
N~Her wish to leave should inform the next route choice.|
N~Head out while she has the strength. No shame in stopping.|
N~I understand. Sometimes the familiar room at home feels very far away.|
N~A safe return matters more than making the outing as long as planned.|
N~The expedition has changed its preferred genre to homecoming.|
S~Wanting something ordinary can become very clear in a strange place.|
N~Objective revised: nearest safe exit, then home.|
S~A familiar door can call through a great deal of stone.|
N~She does not need a more impressive reason to end the day.|
N~I wonder whether she knows the quickest way back.
''')
add('rock_dudley','RockTunnel_B1F_Text_DudleyPostBattle',
    'Dudley favors raw power because he dislikes thinking about tactics.','''
N~A big hammer still needs someone to notice where the nail is.|
N~Force without judgment can be inefficient and dangerous against an unfavorable matchup.|
N~His partners still need him to pay attention.|
N~That sounds like asking the Pokemon to do all the difficult work.|
N~A little thought can save the team a lot of unnecessary strain.|
N~The strategy department has resigned and forwarded all inquiries to muscle.|
N~An uncomplicated plan can become complicated very quickly when it fails.|
N~More output does not fix an unsuitable approach.|
N~A heavy stone can still be pushed toward the wrong place.|
N~Strong partners deserve a trainer who uses their effort thoughtfully.|
N~I wonder how often that approach leaves him without a second option.
''')
add('rock_cooper','RockTunnel_B1F_Text_CooperPostBattle',
    'Cooper asks to have our Pokedex after we finish it.','''
M~That is a very ambitious borrowing request with a suspiciously permanent verb.|
N~The record represents sustained personal work. Completion does not make it unneeded.|
N~He can ask to look. Giving it away is a different question.|
F~I would find it difficult to hand over something full of so many memories.|
N~Sharing what we learned does not require surrendering the whole record.|
M~The spectator proposes acquiring the entire research project after the difficult part.|
N~A book can become rather more than the sum of its pages.|
N~Access to the data and ownership of the record are separate requirements.|
N~A long road has left itself inside those entries.|
N~He could ask about particular discoveries instead of claiming the finished collection.|
S~I wonder what he most hopes to learn from it.
''')
add('rock_steve','RockTunnel_B1F_Text_StevePostBattle',
    'Steve explains Pokemon cosplay and says Clefairy is a popular choice.','''
S~A way to become temporarily pink and moon-shaped. Strong recreational potential.|
S~Costume-making can combine close observation with substantial craft skill.|
N~Fine hobby. Make sure the costume is safe to walk in down here.|
S~It must take care to make something recognizable from a few small details.|
S~People finding a harmless way to share what they love sounds good.|
S~An explanation from someone delightfully willing to become the supporting creature.|
S~A soft disguise can be a way to be more openly yourself.|
S~Materials, silhouette, mobility. An interesting fabrication problem.|
S~Someone borrowing a little shape from the things that make them happy.|
S~Clefairy has an unmistakable outline. Good design choice for a costume.|
S~I wonder whether he makes his own outfits.
''')
add('rock_allen','RockTunnel_B1F_Text_AllenPostBattle',
    'Allen says mountains are good places to encounter Rock-type Pokemon.','''
N~The rocks are not always scenery. A useful adjustment to my assumptions.|
N~The habitat offers resources and conditions suited to many Rock types.|
N~Watch what moves before leaning on an unfamiliar stone.|
S~It changes the way you look at a tunnel when some of it may look back.|
N~A good reminder to notice the residents while navigating.|
M~The setting and the supporting cast share a suspiciously similar costume.|
S~The mountain keeps some of its life very close to its own shape.|
N~Material and habitat correlate. Still worth checking each specimen.|
S~Stone can wear more than one kind of stillness.|
N~An obvious-sounding fact that becomes useful in a dark passage.|
S~I wonder which Rock type he most enjoys finding here.
''')
add('rock_martha','RockTunnel_B1F_Text_MarthaPostBattle',
    'Martha prefers tiny Pokemon because large ones frighten her.','''
N~A smaller friend can feel less intimidating. Tiny still comes with its own opinions.|
N~Size influences perceived safety, though behavior is the better guide.|
N~Keep a comfortable distance. Small partners deserve respect too.|
S~It is understandable to begin with something that makes you feel at ease.|
N~Comfort can grow slowly once you know a particular Pokemon.|
N~A preference for a more manageable silhouette, expressed with admirable honesty.|
S~A small companion can make the larger world less daunting.|
N~Scale affects the experience. Temperament remains a separate specification.|
S~Some friendships begin where a frightened hand can reach comfortably.|
N~She does not need to force herself close to something that scares her.|
S~I wonder whether one particular big Pokemon gave her that impression.
''')
add('rock_eric','RockTunnel_B1F_Text_EricPostBattle',
    'Eric plans to train his Pokemon to beat ours in the future.','''
S~The rematch has been scheduled in his imagination. Plenty of time to prepare.|
N~A clear target can support training if it does not become the only measure of progress.|
N~Train them well. We can meet again without making it personal.|
N~A little rivalry can be motivating when everyone still enjoys it.|
N~I hope the plan includes good care as well as harder practice.|
S~The defeated rival commissions a future sequel with a revised outcome.|
N~A loss can become a direction without becoming a grudge.|
N~Goal identified. Next step is a specific training plan, not just more force.|
N~The next attempt has already begun taking shape in his mind.|
N~Confidence is useful when the work underneath it is kind.|
S~I wonder which part of his team he wants to improve first.
''')
add('rock_winston','RockTunnel_B1F_Text_WinstonPostBattle',
    'Winston decides to return home to draw rather than continue battling.','''
S~A pencil has won the afternoon. A perfectly respectable result.|
S~He recognizes a preferred activity and is returning to it.|
S~Fair enough. Nobody has to make battling their whole life.|
S~I like hearing someone choose the thing they actually want to do.|
S~A quiet creative evening sounds like a good way to end the trip.|
S~The artist steps out of an unsuitable genre and returns to his chosen work.|
S~A page can be a gentler place to spend the rest of a day.|
N~Correct tool, preferred task. Good reassignment.|
S~The road has left a few shapes for his hands to remember.|
S~Knowing what suits you is its own kind of confidence.|
S~I wonder what he wants to draw after being in the tunnel.
''')
add('mansion_ted','PokemonMansion_1F_Text_TedPostBattle',
    'Ted denies knowing about the key we seek.','''
N~No key clue from him. The search remains a key-shaped problem.|
N~He provides no usable information about the key's location.|
N~No answer here. Keep looking carefully.|
N~It is difficult to tell whether he truly does not know or wants the conversation over.|
N~We can move on without pressing someone who has nothing to add.|
N~The inquiry has reached an emphatic blank page.|
N~A dark house does not make every evasive answer a secret.|
N~No lead obtained. Avoid treating a denial as a verified location.|
N~The empty space where an answer might have been can stay empty for now.|
N~A clear refusal to help is at least easier to leave behind.|
N~I wonder what brought him into the mansion.
''')
add('mansion_johnson','PokemonMansion_1F_Text_JohnsonPostBattle',
    'Johnson feels frightened exploring alone and decides he should leave soon.','''
N~The house has successfully out-spooked its visitor. Time to head for daylight.|
N~Recognizing discomfort is a reasonable basis for ending solitary exploration.|
N~Good call. Leave while the route out is still clear.|
N~I would not enjoy being alone in here either.|
N~A safe return is a fine ending to an exploratory day.|
N~The solo expedition has revised its ambition from mystery to the front door.|
S~A good haunted-house instinct: notice the feeling and consider leaving.|
N~Risk and comfort both say stop. That is sufficient.|
N~Some rooms make the outside feel wonderfully ordinary.|
N~He is allowed to prefer company or daylight. Sensible, really.|
N~I wonder how long he has been trying to talk himself into staying.
''')
add('mansion_arnie','PokemonMansion_1F_Text_ArniePostBattle',
    'Arnie explains that the mansion switches alternate which doors are open.','''
N~The house rearranges its invitations. We should remember which door we just closed.|
N~The switches change the accessible route rather than simply opening every barrier.|
N~Watch the route back before pressing another switch.|
N~That explains why the way through keeps feeling different.|
N~A little note of the layout could save a long walk in circles.|
N~The old residence changes the scenery every time someone touches the controls.|
N~A house that cannot decide which rooms it wants you to reach.|
S~Alternating state! Now the door behavior makes much more sense.|
N~One open way may mean another has quietly shut.|
N~Useful explanation. The building is not exactly generous with signs.|
N~I wonder why anyone wanted a home laid out this way.
''')
add('mansion_simon','PokemonMansion_1F_Text_SimonPostBattle',
    'Simon wonders where his partner has gone.','''
N~This is a complicated house to misplace your company in.|
N~Regrouping is sensible when the building changes access through switches.|
N~Find the partner before exploring farther alone.|
N~I hope they agreed on somewhere to meet if they got separated.|
N~A calm search of the last known route is better than both wandering farther.|
N~The supporting explorer has disappeared from a setting with too many entrances.|
N~An absent familiar voice makes this place rather less charming.|
N~Need a rendezvous point. Random searching can double the problem.|
N~A house full of rooms can still feel short of the one person you expected.|
N~He seems more occupied with that than the battle now. Fair enough.|
N~I wonder when they last saw each other.
''')
add('mansion_braydon','PokemonMansion_1F_Text_BraydonPostBattle',
    'Braydon suggests jumping from a particular opening when we are stuck.','''
N~An unusual direction. I would like to inspect the landing before following it.|
N~A suggested drop requires checking the destination and actual route conditions first.|
N~Look before jumping. A stranger's confidence will not soften a bad landing.|
N~That is rather more adventurous than pointing toward a staircase.|
N~A route that sounds quick still needs to be safe for the whole group.|
N~The architectural advice has taken an abruptly vertical turn.|
N~A hole in the floor deserves better research than enthusiasm.|
N~Verify the landing and route. Do not treat a shortcut claim as a safety rating.|
N~The way down should be seen before the feet stop touching this floor.|
N~Practical advice would include exactly where we are meant to land.|
N~I wonder whether he has used that route himself.
''')
add('mansion_lewis','PokemonMansion_B1F_Text_LewisPostBattle',
    'Lewis points out objects left by the mansion\'s former residents.','''
N~An old house leaves a lot of little traces when the people stop coming back.|
N~Abandoned objects can reveal former use, though not every object is safe or ownerless.|
N~Check before picking things up. We do not know what was left here.|
N~It feels strange to see pieces of somebody's daily life still lying around.|
N~A careful look is better than treating every room as a supply shelf.|
N~The departed residents have left a scattered and rather incomplete inventory of their lives.|
N~A house can keep ordinary things long after ordinary days stop happening there.|
N~Inspect unknown material before handling it. Especially in an old research building.|
N~Small belongings remain where the hands that knew them no longer reach.|
N~Left behind and free to take are not always the same thing.|
N~I wonder which items have stayed exactly where the residents put them.
''')
add('mansion_ivan','PokemonMansion_B1F_Text_IvanPostBattle',
    'Ivan likes the mansion\'s atmosphere for studying.','''
N~He has found quiet. It comes with considerably more creaking than I would choose.|
N~A secluded space can aid concentration, though the building presents practical risks.|
N~His choice. Make sure he knows a safe way out.|
S~I understand liking a place others find unsettling, if it lets your thoughts settle.|
N~A comfortable chair and safe light would improve the study arrangement.|
S~The ominous residence has unexpectedly received a favorable academic review.|
S~A strange quiet can be a very good place to think. I see his point.|
N~Low distraction, uncertain structural condition. Mixed evaluation.|
S~An empty house gives his thoughts room to make their own noise.|
N~He knows the atmosphere he likes. I hope he also checked the floorboards.|
S~I wonder what he studies that feels suited to a place like this.
''')
add('tower_memorial','PokemonTower_1F_Text_ErectedInMemoryOfDeadMons',
    'A visitor explains that Pokemon Tower commemorates Pokemon that have died.','''
N~A place to remember the companions who cannot walk beside us now.|
S~A shared memorial gives individual losses a lasting place in the community.|
N~Keep quiet and give the visitors room. This place matters to them.|
D~It is a tender reason for a building to exist.|
S~A place where people do not have to explain why they still miss someone.|
S~The lives beyond the journey are given space instead of being written out.|
S~A room for names that are no longer called home in the evening.|
N~A useful place for remembering, without anything to solve or improve.|
S~Stone keeping a little place open for those who are gone.|
N~We should move through respectfully. These are people's real memories.|
S~I wonder how many visitors return on the same day each year.
''')
add('tower_blessing','PokemonTower_1F_Text_ComeToPayRespectsSon PokemonTower_1F_Text_ComeToPayRespectsGirl',
    'A mourner warmly blesses our visit to pay respects.','''
S~A kind welcome in a quiet place. We can try to deserve it.|
S~The greeting recognizes respect rather than asking for a performance of grief.|
S~Good of them. A quiet visit is enough.|
S~There is room to be gentle here without knowing exactly what to say.|
S~A little shared kindness matters in a place like this.|
S~The welcome asks only that we enter with care.|
S~An old voice making the solemn room less lonely.|
N~A clear invitation to behave respectfully. No complicated procedure needed.|
S~A blessing placed softly beside the door.|
S~They made space for a stranger without prying into the reason for the visit.|
S~I wonder whether they offer those words to everyone who comes through.
''')
add('tower_clefairy_mourner','PokemonTower_1F_Text_CameToPrayForDepartedClefairy',
    'A visitor weeps while praying for a departed Clefairy.','''
D~They loved Clefairy very much. We can give them quiet company or space.|
D~There is no timetable they need to meet for feeling less grief.|
D~Let them have the moment. They do not need to explain it to us.|
D~I wish there were a small thing to say that could make the missing easier.|
D~They deserve to remember their companion without being hurried.|
D~A little name is carrying a whole life of shared days.|
D~Grief can be very large around something once held in your arms.|
D~Nothing here needs a fix from us. Just a little consideration.|
D~An old warmth has left a space that still feels warm at the edges.|
D~We should not make their tears feel like a public display.|
D~I wonder what small habit of Clefairy's they remember most.
''')
add('tower_growlithe_mourner','PokemonTower_1F_Text_GrowlitheWhyDidYouDie',
    'A mourner painfully asks why their Growlithe died.','''
D~That is a question with a great deal of missing someone inside it.|
D~We should not pretend to have an explanation for a loss we know nothing about.|
D~Stay gentle. They are hurting.|
D~Sometimes the question is simply the shape the sadness takes.|
D~A familiar presence leaves so much of the day changed when it is gone.|
D~The words are asking for something no clever answer can supply.|
D~An empty place beside someone can make the whole room feel different.|
D~No assumption about what happened would help. Let them speak if they choose.|
D~A voice still calling toward the place its companion used to answer from.|
D~They do not need us to find the right-looking response. They need respect.|
D~I hope someone who knew Growlithe can sit with them when they want company.
''')
add('tower_spirit_warning','PokemonTower_1F_Text_SenseSpiritsUpToMischief',
    'A channeler senses troublesome spirits on the upper floors.','''
N~The upper floors have an unusually unsettling neighborhood report.|
N~The channeler is reporting an interpretation of a disturbance, not an identified cause.|
N~Take the warning seriously. Keep the team close upstairs.|
N~The quiet below makes that feel more ominous somehow.|
N~We should prepare rather than treating the Tower like a dare.|
N~A solemn setting offers an unwelcome promise of activity above.|
S~The room grows stranger without growing louder. An effective warning.|
N~Unknown disturbance at higher levels. Gather information before pushing on.|
N~Something unsettled may be moving where the air should be still.|
N~Her tone makes clear this is more than an amusing story to her.|
N~I wonder what she noticed that first told her something was wrong.
''')
add('tower_rival','PokemonTower_2F_Text_RivalPostBattle',
    'The rival boasts of catching Cubone, speculates about Marowak, and dismisses our progress.','''
N~He has packed a lot of certainty into some very uncertain guesses.|
N~His failure to find Marowak does not establish their absence. The Pokedex question is fairer.|
N~He can mind his own progress. This is not the place to show off over a loss.|
N~The boasting feels especially jarring in a room meant for remembering.|
N~I hope his new Cubone gets more patience than the conversation did.|
N~A rival delivers a travel update with several unnecessary barbs and a weak biological conclusion.|
N~A room full of loss deserves a little more quiet than that.|
N~Insufficient evidence for the species claim. Plenty of evidence for overconfidence.|
N~His words keep hurrying past the things this place asks people to notice.|
N~He could ask about our work without making it a comparison.|
N~I wonder whether he understands the stories behind the Pokemon here.
''')
add('tower_scope_hint','PokemonTower_2F_Text_SilphScopeCouldUnmaskGhosts',
    'A channeler suggests that a Silph Scope could identify the unknown ghosts.','''
N~A clearer look would be very welcome before we start guessing at floating strangers.|
N~An instrument may provide identification where unaided observation has failed.|
N~Useful lead. Better information beats rushing at something we cannot identify.|
N~Not knowing what we are seeing makes the place much more frightening.|
N~A careful way to understand the problem sounds better than a harder battle.|
N~The mystery may require a better lens rather than a louder declaration.|
S~Some things need to be seen properly before anyone can help.|
S~A tool suited to the actual uncertainty. Good lead.|
S~A different eye may show what the shadows have kept unnamed.|
N~She admits the limit of what she knows. That makes the recommendation more useful.|
N~I wonder whether anyone here has used one before.
''')
add('tower_hope','PokemonTower_3F_Text_HopePostBattle',
    'Hope says the Silph Scope identifies the ghosts.','''
N~An unknown face becomes a little less frightening once you can actually see it.|
N~Identification changes the information available for the encounter.|
N~Good. Know what is there before deciding how to handle it.|
N~A name can make the dark feel less crowded with possibilities.|
N~A useful answer to a very unsettling problem.|
N~The mysterious cast may at last be introduced properly.|
S~Being strange does not mean being impossible to know.|
S~Observed uncertainty has a specific instrument solution. Excellent.|
S~A small lens finding an outline inside the mist.|
N~That is the sort of clear explanation this place badly needs.|
N~I wonder what the ghosts look like through it.
''')
add('tower_carly','PokemonTower_3F_Text_CarlyPostBattle',
    'Carly apologizes and says she was possessed.','''
N~She sounds like she has only just come back into her own conversation.|
N~Her account suggests impaired control. Checking her condition matters more than blame.|
N~Make sure she is all right. The battle can wait.|
D~That must feel frightening to realize afterward.|
N~She needs a calm moment, not a demand for a better apology.|
N~The unwilling performer has returned and is trying to account for a missing scene.|
N~An apology can wait until the room feels like her own again.|
N~Check orientation and immediate safety before asking for a report.|
N~A voice finding its way back into the person it belongs to.|
N~She sounds sincere and shaken. We can be kind.|
N~I wonder whether she remembers anything of what happened.
''')
add('tower_patricia','PokemonTower_3F_Text_PatriciaPostBattle',
    'Patricia suspects the channelers upstairs have also been possessed.','''
N~A warning about more people who may need help, rather than more people to blame.|
N~She infers a wider pattern from her experience. We should remain alert without assuming every case.|
N~Keep ready upstairs. Those people may not be in control.|
N~It is frightening to think someone can be there and not quite themselves.|
N~We should treat anyone we meet carefully, even if they act strangely.|
N~The trouble may extend beyond one unwilling participant.|
N~The higher floors have become a more unsettling kind of unknown.|
N~Possible repeated condition. Check each case instead of treating it as confirmed.|
N~The unease seems to have climbed ahead of us.|
N~She is trying to warn us, even while still making sense of her own experience.|
N~I wonder how far upward she had gone before things changed.
''')
add('tower_paula','PokemonTower_4F_Text_PaulaPostBattle',
    'Paula thinks the possession experience must have been a dream.','''
N~A strange waking moment. I hope the room feels steadier to her soon.|
N~She is uncertain about what happened. There is no need to force a conclusion immediately.|
N~Give her a moment to get her bearings.|
N~A dream that leaves you in a different-feeling room would shake me too.|
N~Rest and a quiet voice seem more useful than another challenge.|
N~A bewildered witness has found the gentlest explanation she can currently manage.|
N~Waking does not always make the strange feeling leave at once.|
N~Incomplete recall. Let her orient before collecting more information.|
N~The room has returned, but perhaps not all at the same time.|
N~We can accept that she is unsure without making her feel foolish.|
N~I wonder whether anything familiar nearby would help her settle.
''')
add('tower_laurel','PokemonTower_4F_Text_LaurelPostBattle',
    'Laurel admits the channelers cannot identify the ghosts.','''
N~Not knowing is a useful thing to admit before the guesses start growing teeth.|
N~Acknowledging the limit of identification is more reliable than inventing certainty.|
N~Then use the right tool or get help. No shame in that.|
N~It must be unsettling to find the familiar work suddenly beyond you.|
N~A careful next step matters more than pretending to have an answer.|
N~The supposed experts have reached the edge of the available evidence.|
N~An honest uncertainty is better company than a confident fiction.|
N~Capability limit identified. Need a different observation method.|
N~Some shapes remain hidden from the eyes that first seek them.|
N~I appreciate that she tells us the problem plainly.|
N~I wonder what they have already tried.
''')
add('tower_jody','PokemonTower_4F_Text_JodyPostBattle',
    'Jody quietly prays for the departed Pokemon to rest in peace.','''
S~A small gentle wish, exactly suited to this place.|
S~A respectful moment need not provide an explanation to have value.|
S~Let her finish. No need for us to add anything.|
S~That sounds like the voice this room was meant to hold.|
S~I am glad there is room for kindness even after all the fear.|
S~A brief line that asks for nothing except peace for someone else.|
S~Some words are best left with a little silence around them.|
N~No practical task required. We can simply be respectful.|
S~A little stillness offered to the ones no longer walking.|
S~Quiet sincerity needs no decoration.|
S~I wonder whether she comes here for someone particular.
''')
add('tower_rest_offer','PokemonTower_5F_Text_RestHereInPurifiedSpace',
    'A channeler offers a protected resting place within the Tower.','''
S~A safe little island in a very unsettling building. Welcome offer.|
S~A defined place to recover can make continued exploration more manageable.|
S~Take the rest. The team has earned it.|
S~I can feel how much I wanted someone to say it was safe to stop.|
S~A quiet recovery before another difficult floor sounds sensible.|
S~The ominous setting makes one generous exception for tired travelers.|
S~A small circle where the dark has agreed to wait outside.|
N~Protected rest point identified. Use it before pushing the team farther.|
S~A little clearing inside a house full of shadows.|
S~She made the offer feel welcoming instead of embarrassing.|
S~I wonder how many frightened visitors have been relieved to find her here.
''')
add('tower_tammy','PokemonTower_5F_Text_TammyPostBattle',
    'Tammy says she had been under possession.','''
N~She has a name for what happened. I hope she has somewhere safe to sit too.|
N~The reported loss of control deserves care rather than an assumption of intent.|
N~Check she is steady before leaving her alone.|
N~It is unsettling to imagine missing pieces of your own actions.|
N~A quiet pause could help her feel more like herself again.|
N~A reluctant participant returns with a very troubling explanation.|
N~It is a relief to hear her own voice again, however brief.|
N~Recovery first, explanation second. She seems shaken.|
N~The room has given its occupant back her place within it.|
N~We need not make her prove how frightening it was.|
N~I wonder whether she can reach the protected resting space nearby.
''')
add('tower_ruth','PokemonTower_5F_Text_RuthPostBattle',
    'Ruth explains that she was possessed.','''
N~A short explanation for an experience that sounds anything but small.|
N~Her account changes how we should interpret the earlier behavior.|
N~Then she needs a safe moment, not another opponent.|
N~I hope the simple words mean she is beginning to understand it.|
N~It is worth making sure she feels all right before we move on.|
N~The unwilling actor offers a concise report from a very unwelcome role.|
N~Sometimes a person has very few words left after something strange.|
N~Confirm immediate safety. The full report can wait.|
N~A familiar voice has a little room to stand in again.|
N~That is enough explanation for us to respond gently.|
N~I wonder whether someone she knows is nearby.
''')
add('tower_karina','PokemonTower_5F_Text_KarinaPostBattle',
    'Karina says she has regained her senses.','''
S~Welcome back to your own afternoon. I hope the next part is much quieter.|
S~She recognizes a return to normal awareness. A reassuring sign.|
S~Good. Let her get steady before asking anything else.|
S~There is such relief in a simple sentence like that.|
S~A little rest still seems worthwhile after what happened.|
S~The person has returned to the center of her own scene.|
S~A room can feel new again when it finally belongs to your senses.|
N~Awareness restored. Still allow time to recover from the disruption.|
S~The light has found its way back behind her eyes.|
S~I am glad she can say that for herself.|
S~I wonder what was the first familiar thing she noticed.
''')
add('tower_janae','PokemonTower_5F_Text_JanaePostBattle',
    'Janae is shaken that spirits overcame her mountain training.','''
N~Preparation can matter and still not cover every strange thing. That is not her failure.|
N~Training for one set of conditions does not guarantee resistance to an unfamiliar threat.|
N~She trained. Something still went wrong. Get help rather than blame her.|
D~It must be frightening when something you trusted to protect you does not.|
N~She can recover without having to defend whether she tried hard enough.|
N~An old discipline has met a danger outside its established script.|
N~A broken expectation can hurt after the immediate fear has gone.|
N~The test exceeded the training conditions. That calls for a revised approach.|
N~Even a well-tended wall cannot keep out every kind of weather.|
N~Her effort was real even if it did not prevent this.|
N~I wonder whether she has someone experienced to talk it through with.
''')
add('tower_angelica','PokemonTower_6F_Text_AngelicaPostBattle',
    'Angelica feels weak after the encounter.','''
N~That sounds like a proper reason to sit down, not a minor detail.|
N~She reports weakness. Rest and appropriate help are more useful than further exertion.|
N~Get her somewhere safe to rest. No more battling.|
N~She sounds unsteady. I would not want her left alone up here.|
N~The protected space below might give her somewhere calmer to recover.|
N~The encounter's aftermath deserves more attention than its battle result.|
N~A person can look composed and still feel very far from well.|
N~Stop the load. Check her condition before resuming anything.|
N~The strength has gone quiet in her voice. Let her rest.|
N~She is telling us she does not feel well. We should listen plainly.|
N~I wonder who nearby can help her downstairs.
''')
add('tower_emilia','PokemonTower_6F_Text_EmiliaPostBattle',
    'Emilia realizes a malevolent spirit caused the experience, rather than her hair falling out.','''
U~A terrible moment has ended with the hair still present. One very specific relief.|
N~She is revising her interpretation of a frightening sensation. The immediate relief is clear.|
N~Glad she is all right. Give her time to settle.|
N~I would be rattled by not knowing what had happened to my own body.|
S~A small reassuring fact can matter when everything else felt strange.|
U~The alarming personal crisis has acquired a supernatural culprit and a better hair outcome.|
M~A very unusual victory for the continued existence of one's hairstyle.|
N~Initial diagnosis revised. Check the actual condition rather than the frightening impression.|
S~A familiar little part of herself remains exactly where she left it.|
S~I understand checking the hair first after a scare like that.|
N~I wonder what she felt that made her think that was happening.
''')
add('tower_jennifer','PokemonTower_6F_Text_JenniferPostBattle',
    'Jennifer is confused about what is happening in the Tower.','''
N~A fair question. This building has supplied far more mysteries than explanations.|
N~She lacks a clear account of the event. Start with what she remembers.|
N~Make sure she is safe before giving her the long version.|
N~That confused feeling would frighten me more than a clear warning.|
N~A calm explanation and a place to rest seem useful.|
N~A bewildered participant asks for the script after the scene has already happened.|
N~The room should feel familiar before the story is demanded of her.|
N~Missing context. Provide simple facts, not a barrage of theories.|
N~She is standing in the space between an experience and its meaning.|
N~We should not make her feel foolish for asking.|
N~I wonder how much of the encounter she can recall.
''')
add('tower_grunt1','PokemonTower_7F_Text_Grunt1PostBattle',
    'The retreating grunt threatens to remember our interference.','''
N~He can remember us. I would prefer he remember why he had to leave.|
N~A lingering threat does not change the need to stop his current behavior.|
N~Let him leave. Stay alert until he is gone.|
N~I dislike hearing that in a place where people came for peace.|
N~We can keep moving without feeding the threat another conversation.|
N~A villain promises a sequel on his way out of a scene he has already lost.|
N~An unpleasant memory may be a useful thing for him to keep.|
N~Threat recorded. Do not prolong exposure for the sake of an argument.|
N~A sharp voice is finally moving toward the stairs.|
N~The important part is that he is leaving the people here alone.|
N~I wonder whether the others heard that he was driven back.
''')
add('tower_grunt2','PokemonTower_7F_Text_Grunt2PostBattle',
    'The grunt dismisses Pokemon as money-making tools and tells us not to interfere.','''
A~The Pokemon have more to offer the world than padding his pockets.|
N~He is reducing living partners to revenue while dismissing the harm that causes.|
A~No. Their lives are not his business inventory.|
D~It sounds especially cruel in a place remembering what those lives meant.|
A~A companion does not stop deserving care when it cannot earn somebody money.|
N~A remarkably naked statement of a thoroughly ugly philosophy.|
A~A purse is a poor replacement for any part of a heart.|
N~The intended use is the problem. Efficiency would not improve it.|
N~He hears coins where everyone else remembers voices.|
A~He wants privacy for cruelty. That is no reason to give it to him.|
N~I wonder whether he has ever really paid attention to a Pokemon outside a price tag.
''')
add('tower_grunt3','PokemonTower_7F_Text_Grunt3PostBattle',
    'The last grunt threatens retaliation as he retreats.','''
N~He seems to be getting away with leaving. We should let that part continue.|
N~The threat accompanies withdrawal. We should remain cautious without pursuing an argument.|
N~Keep walking out. That is enough from him.|
N~I will feel better once the Tower is quiet again.|
N~The people here need peace more than another shouted exchange.|
N~The final retreating voice insists the ending is temporary. We need not applaud.|
N~The stairs are doing useful work carrying that threat away.|
N~Immediate threat reducing. Maintain attention until the exit is clear.|
N~A harsh echo fades one step at a time.|
N~He can keep his last word if it gets him out of the room.|
N~I wonder whether the visitors below can hear that the fighting has stopped.
''')
add('hideout_disrespect','RocketHideout_B1F_Text_Grunt1PostBattle',
    'A defeated grunt accuses us of disrespecting Team Rocket.','''
N~Respect is not something they can confiscate from passing trainers.|
N~Criticism of harmful conduct does not become invalid because the organization dislikes it.|
N~They can start by giving people a reason to respect them.|
N~He seems more upset by disobedience than by anything the group has done.|
N~A little decency would do more than demanding a better opinion.|
N~The villainous organization has requested a more favorable review from its unwilling audience.|
N~An unpleasant name does not become respectable by being shouted.|
N~Reputation problem identified. Their behavior remains the cause.|
N~A shadow cannot demand that everyone call it daylight.|
N~He wants admiration where basic courtesy would already be generous.|
N~I wonder whether anyone ever tells him what the group looks like from outside.
''')
add('hideout_brat_threat','RocketHideout_B1F_Text_Grunt2PostBattle',
    'The grunt threatens us for interfering in the hideout.','''
N~Another threat. The underground customer service is consistently terrible.|
N~He remains hostile after the result. Distance is preferable to further argument.|
N~Keep close. We are not letting him catch someone off guard.|
N~I would rather keep moving than wait for him to think of something worse.|
N~A clear route onward matters more than answering him.|
N~A stock threat, delivered with entirely unnecessary conviction.|
N~The insults are small. The caution they ask for is not.|
N~Hostile signal continues. Do not treat the battle result as total safety.|
N~The passage has one more sharp voice than it needs.|
N~We can leave him without giving him another opportunity.|
N~I wonder how many others are waiting beyond the next corner.
''')
add('hideout_scope_denial','RocketHideout_B1F_Text_Grunt3PostBattle',
    'A grunt refuses to tell us where the Silph Scope is.','''
N~No helpful directions from that corner of the basement.|
N~He provides no usable location information. The refusal does not resolve the search.|
N~No Scope location. We can stop asking him and look for another lead.|
N~He clearly does not want to help us. We can stop asking.|
N~We should use what we can actually verify rather than chase the tone.|
N~The investigation receives a grudging blank instead of a useful clue.|
N~Some closed mouths are merely closed mouths, however suspicious the room.|
N~No data obtained. Continue from established clues.|
N~A missing answer is not a direction to follow.|
N~He seems to enjoy making the conversation harder. No need to stay in it.|
N~I wonder who here actually knows where the device was taken.
''')
add('hideout_elevator_boss','RocketHideout_B1F_Text_Grunt4PostBattle',
    'The grunt tells us the elevator leads to his boss.','''
N~Directions at last. A rare basement luxury.|
N~The elevator is a concrete lead toward the person directing the operation.|
N~Useful. Check the team before going farther.|
N~He sounds reluctant, but at least that is something we can follow.|
N~A clear lead is a good moment to pause and prepare.|
N~The reluctant informant has finally supplied an address rather than an insult.|
N~A route through this place is beginning to take a less shapeless form.|
N~Destination access method identified. Still need to verify operation.|
N~The way down has acquired a name at its end.|
N~A practical answer after all the posturing. Appreciated.|
N~I wonder how closely the elevator is guarded.
''')
add('hideout_open_door','RocketHideout_B1F_Text_Grunt5PostBattle',
    'The grunt notices the disturbance has opened a door.','''
N~That is a very unusual door policy. Apparently the noise did the paperwork.|
N~The disturbance coincided with the door opening; the exact mechanism is unclear.|
N~New way through. Check it before rushing in.|
N~A changed room is worth noticing, even while everyone is upset.|
N~We should look at the opening together instead of splitting up.|
M~The villainous headquarters has allowed the commotion to edit its floor plan.|
N~A closed place has accidentally changed its mind.|
N~Unexpected state change. Inspect the doorway before drawing conclusions.|
N~Something shut has stopped being shut. A small useful fact.|
N~He sounds more surprised by the door than the defeat.|
N~I wonder whether that was supposed to happen at all.
''')
add('hideout_four_floors','RocketHideout_B2F_Text_GruntPostBattle',
    'The grunt boasts that the hideout has four underground floors before its boss.','''
N~Four floors of this. Somebody should have put that on the entrance sign.|
N~Knowing the building's depth helps estimate the remaining distance, though not the safe route.|
N~We can take it one floor at a time. Keep the team ready.|
N~It is better to know how far the place goes, even if I dislike the answer.|
N~A long underground route needs a sensible use of supplies.|
N~The villain supplies a floor count in place of a convincing deterrent.|
N~An ambitious amount of basement for so much bad company.|
N~Four levels noted. Need a route map, not just an inventory of floors.|
N~The building keeps lowering its ceiling over the next part of the road.|
N~He has made the place sound exhausting rather than impressive.|
N~I wonder how anyone working here learns the quickest way through.
''')
add('hideout_scope_stolen','RocketHideout_B3F_Text_Grunt1PostBattle',
    'The grunt admits that his boss stole the Silph Scope and it is somewhere in the hideout.','''
N~That was a remarkably casual confession with a useful location attached.|
N~He has linked the stolen device to the boss and this building. A more specific lead.|
N~So it is stolen and nearby. Keep looking.|
N~The casual way he says it makes the theft feel even uglier.|
N~Getting it back would be a useful thing to put right here.|
N~The witness supplies a confession and then misplaces the final address.|
N~A stolen thing is still somebody's missing thing, however casually they name it.|
N~Provenance established as theft; search area narrowed to this structure.|
N~A useful little truth has slipped out of a careless voice.|
N~He talks as if taking someone else's work is ordinary. It should not be.|
N~I wonder whether he realizes how much he just told us.
''')
add('hideout_key_required','RocketHideout_B3F_Text_Grunt2PostBattle',
    'The grunt says the elevator cannot run without the Lift Key.','''
N~The elevator has a very specific idea of who belongs in it. We need the key.|
N~A physical access credential is required before the elevator can operate.|
N~Find the key. Do not waste time arguing with the controls.|
N~At least we know what is missing now.|
N~A clear requirement is better than trying the same closed route again.|
N~The journey downward has paused for a small but decisive prop.|
N~A large machine can be made helpless by a little missing shape.|
N~Authorization device required. That explains the failed operation.|
N~The way through has narrowed to a small piece of metal.|
N~A taunt can still contain useful instructions.|
N~I wonder who has been trusted to carry the key.
''')
add('hideout_giovanni','RocketHideout_B4F_Text_GiovanniPostBattle',
    'Giovanni recognizes our care for Pokemon, dismisses our understanding, and retreats.','''
N~He noticed we care and still thinks that makes us the confused ones. Strange judgment.|
N~His acknowledgment of our care does not excuse the operation he leads.|
N~He is stepping aside. Stay ready until he is gone.|
N~It is unsettling to hear a sincere observation inside such a dismissive farewell.|
N~We can care about the partners without needing his approval of the reason.|
N~The departing antagonist offers one accurate compliment and an expansive claim to mystery.|
N~Being difficult to understand is not proof of being worth understanding on his terms.|
N~He supplied no justification for the harm. The compliment does not fill that gap.|
N~A soft truth has passed through a voice still holding something sharp.|
N~He speaks as if distance from him is a lack in us. I disagree.|
N~I wonder whether he has ever listened seriously to the people his plans hurt.
''')
add('hideout_against_rocket','RocketHideout_B4F_Text_Grunt2PostBattle',
    'A grunt asks whether we have something against Team Rocket.','''
N~A few things, yes. The basement has been generous with examples.|
N~The question overlooks the group's conduct as a clear source of opposition.|
N~The theft and threats are a good starting point.|
N~He sounds surprised that someone might object to what they are doing.|
N~People do not need a personal grudge to want others treated decently.|
M~An organization with this much misconduct requests a detailed explanation for disapproval.|
N~An oddly innocent question from a room with very little innocence in it.|
N~The evidence is already available throughout the facility.|
N~A cruel path should expect a few feet to stand across it.|
N~He could begin by considering how they treat visitors.|
N~I wonder what he thinks a reasonable objection would look like.
''')
add('hideout_failed_boss','RocketHideout_B4F_Text_Grunt3PostBattle',
    'The defeated grunt apologizes to his absent boss.','''
N~He is more worried about the boss's opinion than the person he threatened.|
N~His first concern appears to be accountability upward rather than the consequences of the operation.|
N~Hope fear of the boss does not make him take it out on the team.|
N~He sounds frightened of a person who is not even standing here.|
N~A workplace that leaves people that afraid has something badly wrong with it.|
N~The defeated underling addresses an absent authority as though the whole room were watching.|
N~An empty chair can still frighten someone who knows who owns it.|
N~Hierarchy pressure seems high. That does not justify the harm, but it explains the panic.|
N~A distant voice is apparently loud enough in his head already.|
N~Loyalty built from fear never looks comfortable on anyone.|
N~I wonder what the boss has taught him to expect after failure.
''')
add('hideout_dropped_key','RocketHideout_B4F_Text_Grunt1PostBattle',
    'The grunt realizes he has dropped the Lift Key.','''
M~A security announcement delivered directly to the person searching for the key. Helpful.|
N~His statement identifies the dropped object, but does not mean we have picked it up yet.|
N~There is the key. Check where it fell.|
N~He probably wishes he had noticed silently.|
N~A useful opening, but we should still collect it carefully.|
M~The crucial prop makes its entrance with a disastrously informative line from its keeper.|
M~A secret kept right up until the moment someone narrates its location.|
N~Access token displaced. Recovery remains a separate action.|
N~A small lost thing has changed who may open the next way.|
N~He has made an accident considerably more public than necessary.|
N~I wonder how long it would have taken us to notice without the announcement.
''')
add('victory_naomi','VictoryRoad_1F_Text_NaomiPostBattle',
    'Naomi is especially disappointed to lose to a younger trainer.','''
N~The birthday gap did not do any of the battling. The team did.|
N~Age alone is a poor predictor of skill or preparation.|
N~Young does not mean unprepared. She has seen the work now.|
N~It hurts more when a loss challenges the picture you had of yourself.|
N~A difficult match can teach something without deciding anyone's worth.|
N~The result has offended an age hierarchy the battle never agreed to follow.|
N~The calendar is an unreliable shield against disappointment.|
N~Capability estimate based on age has failed. Update it with the actual evidence.|
N~A younger branch can still reach somewhere the old one did not.|
N~She could give the team credit without making it a contest of birthdays.|
N~I wonder what part of the battle surprised her most.
''')
add('victory_rolando','VictoryRoad_1F_Text_RolandoPostBattle',
    'Rolando grudgingly acknowledges that we battled better.','''
S~A compliment with a little gravel still attached. We can take it gently.|
S~He accepts the result even though the disappointment remains audible.|
S~Fair of him to say it. The team earned that.|
S~It can take effort to give someone credit while still feeling hurt.|
S~A little honesty is a good beginning for the next attempt.|
S~The defeated opponent offers an accurate review through firmly clenched pride.|
S~Grudging can still be genuine. I will count it.|
N~Result acknowledged. Useful starting condition for a proper review.|
S~A little truth can pass through a difficult moment.|
S~Not graceful, exactly, but more generous than an excuse.|
S~I wonder what he will change after thinking the battle over.
''')
add('victory_dawson','VictoryRoad_2F_Text_DawsonPostBattle',
    'Dawson claims superior Pokemon knowledge despite losing.','''
N~There is room for a quiz champion and a battle winner in the same cave.|
N~Factual knowledge and applying decisions under pressure are distinct skills.|
N~Maybe he knows plenty. Still needs to use it well.|
N~It is understandable to reach for something you still feel confident about.|
N~Knowing things can help the next battle if he is willing to review this one.|
M~The result is appealed to an entirely different department.|
N~A full head can still have trouble choosing what matters in the moment.|
N~Stored information is not the same as an effective operating plan.|
N~A map is useful, but someone still has to walk the ground.|
N~He can keep his knowledge without turning it into another contest immediately.|
N~I wonder which fact he most enjoys surprising people with.
''')
add('victory_daisuke','VictoryRoad_2F_Text_DaisukePostBattle',
    'Daisuke recommends moving boulders when the route seems blocked.','''
N~The mountain has included movable furniture. We should consider the arrangement carefully.|
N~Boulder placement affects access. Plan the movement rather than pushing at random.|
N~Check where it needs to go before putting the team's backs into it.|
N~It is reassuring that the dead end may have a practical answer.|
N~A little thought saves a lot of unnecessary heavy work.|
N~The scenery may need a physical rewrite before the next scene becomes available.|
N~A large obstacle becomes less mysterious when you know it can be moved.|
N~Spatial planning problem. Trace the destination before committing to a push.|
N~Stone can be persuaded, if the direction is chosen well.|
N~Useful advice. More useful still with a good look at the room.|
N~I wonder which boulder catches most people out.
''')
add('victory_rival_passed','VictoryRoad_2F_Text_NelsonPostBattle',
    'Nelson mentions that our rival already passed through Victory Road.','''
N~The rival-shaped rumor has arrived ahead of the rival-shaped person. Again.|
N~It confirms his recent presence, not his current condition or exact location.|
N~Good for him. We still move at the team's pace.|
N~Hearing that can make the road feel like a race even when it need not be.|
N~No reason to hurry the partners just because someone else got here first.|
N~The recurring rival has left a brief advance notice in the local dialogue.|
N~Someone else's footsteps do not shorten or lengthen ours.|
N~Prior transit recorded. No requirement to change our schedule.|
N~Another set of tracks ahead, without an obligation to chase them.|
N~Useful to know. We can leave the comparison there.|
N~I wonder what impression he made on the people he met here.
''')
add('victory_vincent','VictoryRoad_2F_Text_VincentPostBattle',
    'Vincent acknowledges that we earned our place on Victory Road.','''
S~A little recognition after a very long climb. Welcome words.|
S~He recognizes the sustained qualification required to reach this point.|
S~We earned it together. The team deserves that acknowledgment.|
S~It is good to hear we belong here when the path feels daunting.|
S~A long effort can feel real in a different way when someone notices it.|
S~The gatekeeping critic has granted a favorable review of the whole journey.|
S~A small sentence with a great many roads behind it.|
N~Prerequisites met, performance observed. Acceptance justified.|
S~The stone beneath us is also a place we have worked to reach.|
S~Recognition without an extra insult attached. Appreciated.|
S~I wonder whether he remembers how it felt to arrive here himself.
''')
add('victory_gregory','VictoryRoad_2F_Text_GregoryPostBattle',
    'Gregory says many trainers end their challenge here and return home.','''
N~A hard road is still allowed to have an exit that leads home.|
N~Stopping can reflect sound judgment as well as exhaustion or discouragement.|
N~Nobody owes the cave their last ounce of strength.|
N~I hope the people who turn back are kind to themselves about it.|
N~A safe return leaves the choice to try again another day.|
N~Not every journey needs its final scene at the same summit.|
N~Home is a destination, not automatically a verdict.|
N~Know the stop conditions. Continuing is not always the better outcome.|
N~A path can turn back without becoming meaningless.|
N~I dislike making retreat sound like the whole measure of a person.|
N~I wonder how many come back later with a different plan.
''')
add('victory_george','VictoryRoad_3F_Text_GeorgePostBattle',
    'George recognizes us as the trainer who defeated Team Rocket\'s Giovanni.','''
N~That story has made it all the way into the mountain. Hope it kept the useful details.|
N~He recognizes a prior result, though reputation may simplify what actually happened.|
N~The team did the work. We had people worth helping.|
F~It is strange to hear a difficult day become how someone identifies us.|
N~I am glad the people helped are part of what the story remembers.|
N~A familiar incident has become the advance notice to our next appearance.|
N~A person can arrive somewhere after the story about them has already settled in.|
N~Prior encounter linked correctly. Do not let the recognition distract from the current route.|
N~An old clash has left an echo even in this far room of stone.|
N~I hope he remembers the care behind it, not just the win.|
N~I wonder who told him about that battle.
''')
add('victory_alexa','VictoryRoad_3F_Text_AlexaPostBattle',
    'Alexa says difficult battles help trainers grow stronger.','''
N~A challenge helps when it teaches something, rather than merely leaving everyone flattened.|
N~Appropriate difficulty and recovery can turn experience into improvement.|
N~Learn from it. Rest after it. Both matter.|
N~A hard attempt can reveal something you could not see before.|
N~Strength grows better when the team has time to recover between efforts.|
N~A demanding scene can improve the cast, provided the rehearsal does not become punishment.|
N~Difficulty is a teacher with rather uneven bedside manners.|
N~Stress without learning is just stress. Review the result.|
N~A strong wind can help a branch grow, until it is simply too much wind.|
N~A useful thought when it comes with judgment about what the team can handle.|
N~I wonder what this match taught her about her own partners.
''')
add('victory_caroline','VictoryRoad_3F_Text_CarolinePostBattle',
    'Caroline says the battle showed her the limits of her current ability.','''
N~A clearer picture can sting and still help draw the next plan.|
N~A challenging comparison provides information without setting a permanent limit.|
N~She knows where to work now. That is useful.|
N~I hope she sees what she did well alongside what needs practice.|
N~An honest review can become something kinder than simply calling the day a failure.|
N~A difficult performance has supplied an unusually candid self-review.|
N~A present boundary is not necessarily the edge of the whole future.|
N~Baseline measured. Now identify one change worth testing.|
N~Knowing where you stand can help you choose the next step.|
N~She is allowed to be disappointed without making the result her whole identity.|
N~I wonder which part of the battle was most revealing to her.
''')
add('victory_colby','VictoryRoad_3F_Text_ColbyPostBattle',
    'Colby warns that everyone here aims for the League and we should remain prepared.','''
N~A cave full of people with the same very ambitious appointment. Stay sharp.|
N~Shared high-level goals make strong preparation likely, though each opponent still differs.|
N~Keep the team ready. No reason to underestimate the next person.|
N~It makes the whole place feel full of quiet determination.|
N~A rest when we need one is part of staying prepared.|
N~Every traveler here believes they belong in the final act. An interesting room.|
N~A common destination does not make the company predictable.|
N~High expected challenge. Review condition and resources regularly.|
N~Many different roads are narrowing toward the same door.|
N~A clear warning without trying to frighten us off. Useful.|
N~I wonder how differently everyone imagined this place before arriving.
''')
add('victory_ray','VictoryRoad_3F_Text_RayPostBattle',
    'Ray accepts the pair\'s loss and says greatness remains out of reach.','''
N~Greatness is a slippery target when one battle gets to move it around.|
N~A single result does not define the upper limit of their partnership.|
N~They lost. They can train again without calling the whole goal impossible.|
N~I hope the disappointment does not make them forget what they have already built together.|
N~A shared plan can change without becoming a failed partnership.|
N~The grand pursuit pauses for a sobering review from the field.|
N~An elusive thing need not be chased with quite so much self-punishment.|
N~Vague ultimate objective. Specific improvements would be easier to measure.|
N~The summit can remain far away without taking the path from under you.|
N~They can value the work even before the title they want fits.|
N~I wonder what each partner means when they say greatness.
''')
add('victory_tyra','VictoryRoad_3F_Text_TyraPostBattle',
    'Tyra recognizes many different forms of strength after the double battle.','''
S~A good discovery. Power has more than one outfit and several surprising shoes.|
S~A diverse set of capabilities can produce strength through different combinations.|
S~Good lesson. Learn what works instead of chasing one perfect shape.|
S~I like hearing a difficult match make someone's view of the world wider.|
S~Different partners bring different useful things to the same team.|
S~The critic has discovered that the leading role can be played in many forms.|
S~An ordinary-looking creature may have an extraordinary answer to the right question.|
S~Multiple valid designs! Much more interesting than a single optimal-looking machine.|
S~A strong root, a flexible branch, a seed that survives. Many answers.|
S~A useful eye for variety will serve her better than one narrow ideal.|
S~I wonder which unexpected combination taught her the most.
''')
add('silph_reception','SilphCo_1F_Text_WelcomePresidentInBoardroom',
    'The receptionist directs visitors to the president\'s eleventh-floor boardroom.','''
N~Eleven floors of company before you reach the person running it. Ambitious building.|
N~A precise floor and room are useful directions in a structure this large.|
N~Good. We know the destination before taking the stairs.|
S~A calm welcome makes a large unfamiliar building easier to enter.|
N~Worth knowing how far up we are going before planning the walk.|
N~The corporate summit has been assigned a suitably lofty location.|
N~A very tall house for a collection of working days.|
N~Destination specified. Now establish the actual route.|
N~The next conversation waits well above the first door.|
S~Clear directions are a kind of good manners.|
N~I wonder how often visitors end up on the wrong floor.
''')
add('silph_worker3_worry','SilphCo_3F_Text_WhatAmIToDo',
    'A frightened employee does not know what to do during the takeover.','''
N~An ordinary workday has become something nobody trained them for.|
N~They need a safe immediate plan rather than an expectation to resolve the takeover.|
N~Stay out of danger. Their job does not require facing criminals.|
D~That helpless feeling must make every minute seem longer.|
N~A safe place to wait and someone reliable to help would matter now.|
N~An office worker has been abruptly cast in a danger they never auditioned for.|
N~A familiar room can become frightening without changing its furniture.|
N~Unexpected emergency. Prioritize the person, not the workplace task.|
N~The day's usual instructions have stopped being useful.|
N~Nobody should have to invent courage just to survive a work shift.|
N~I wonder whether they can reach any of their coworkers safely.
''')
add('silph_worker3_thanks','SilphCo_3F_Text_YouAndYourMonsSavedUs',
    'The employee gratefully credits us and our Pokemon after the takeover ends.','''
S~They remembered the whole team in the thank-you. I am glad.|
S~Their acknowledgment includes the Pokemon who carried the practical effort.|
S~Good to hear they are safe. The partners earned that thanks.|
S~The relief makes the words feel very plain and very real.|
S~A safer ordinary day is a good outcome to have helped with.|
S~The rescued worker gives the ensemble its deserved place in the credits.|
S~A little gratitude where a helpless question used to be.|
N~Immediate danger resolved. The human result matters more than the battle tally.|
S~The room has enough quiet again for a warm voice.|
S~They looked at the Pokemon as helpers, too. A thoughtful detail.|
S~I wonder what the first ordinary thing they want to do is.
''')
add('silph_hiding','SilphCo_4F_Text_CantYouSeeImHiding',
    'An employee asks us not to expose their hiding place.','''
N~Right. Less conversation, more not pointing at the hiding person.|
N~Their priority is avoiding detection. We should not draw attention to the location.|
N~Keep our voices down. They are trying to stay safe.|
N~I am sorry we startled them. We should step back quietly.|
N~A safe corner should stay a safe corner until help can reach them.|
N~The unwilling participant has requested a substantially smaller speaking role.|
N~A person does not need to look brave to deserve safety.|
N~Minimize noise and exposure. Clear requirement.|
N~A small shadow is doing the work of shelter. Leave it intact.|
N~We should not make hiding feel like another thing to be embarrassed about.|
N~I wonder how long they have been waiting here.
''')
add('silph_hiding_after','SilphCo_4F_Text_TeamRocketIsGone',
    'The hidden employee is surprised to learn Team Rocket has left.','''
S~Good news can take a moment to reach someone who has been trying not to be found.|
S~They had incomplete information while sheltering. Confirmation should be calm and clear.|
S~Yes. Let them take a moment before coming out.|
S~I hope the relief reaches them as soon as the words do.|
S~A little reassurance may help them believe the room is safe again.|
S~The quiet survivor has finally received the scene change they were waiting for.|
S~The world outside a hiding place can feel difficult to trust at first.|
N~Threat status changed. Provide a simple verified update.|
S~The shadow may no longer need to hold them so tightly.|
S~No need to rush them into acting relieved immediately.|
S~I wonder whose familiar voice they will want to hear first.
''')
add('silph_intruder_rumor','SilphCo_5F_Text_RocketsInUproarAboutIntruder',
    'An employee recognizes us as the intruder upsetting Team Rocket.','''
N~We have apparently become the building's least popular unscheduled visitor.|
N~Our movements are affecting the occupying group. That may also increase their alertness.|
N~Keep the worker safe. Drawing Rocket attention has consequences.|
N~It is strange to hear people calling us an intruder in a building they took over.|
N~We should keep the disruption away from anyone trying to shelter.|
N~The criminals object to an uninvited visitor with admirable lack of self-awareness.|
N~An intruder, according to the people who invaded the place. Neatly absurd.|
N~Hostile alert level may be rising. Adjust the route carefully.|
N~The noise of our arrival has traveled ahead through the floors.|
N~The label says more about who thinks they own the place.|
N~I wonder how far the report has spread through the building.
''')
add('silph_hero5','SilphCo_5F_Text_YoureOurHeroThankYou',
    'The employee celebrates Rocket\'s departure and calls us a hero.','''
S~A good ending is the one where people can stop being afraid at work.|
S~The practical outcome is restored safety for the staff. Their relief is unmistakable.|
S~Glad they are safe. The team helped make that happen.|
F~Hero is a big word. Their relief makes it easier to accept kindly.|
S~I am happy the next workday can be ordinary again.|
S~The title is grand; the reward is a room no longer waiting for danger.|
S~A familiar place has been given back to the people who spend their days in it.|
N~Occupancy restored to staff. Successful result beyond the combat.|
S~The building can let out a breath it has held too long.|
S~We can thank them without pretending we did everything alone.|
S~I wonder whether they have been able to tell their family they are safe.
''')
add('silph_president_worry','SilphCo_5F_Text_RocketBossLookingForStrongMons',
    'A worker fears for the president after hearing Rocket\'s boss wants strong Pokemon.','''
N~That is a worrying ambition to hear from somebody already taking over the building.|
N~Their concern connects a stated goal with the president's exposed position.|
N~Find out who is safe. The boss's plans should not leave staff guessing like this.|
N~Not knowing whether someone upstairs is all right must be awful.|
N~A clear message between floors would help people frightened for each other.|
N~The worker has heard enough of the villain's objective to fear its next scene.|
N~A distant office can become a very worrying place when the phone goes quiet.|
N~Need verified staff status, particularly on the upper floors.|
N~Concern has climbed ahead of us toward a closed room.|
N~They are thinking of the person, not just their job title.|
N~I wonder when anyone last heard from the president directly.
''')
add('silph_takeover6','SilphCo_6F_Text_RocketsTookOverBuilding',
    'An employee reports the building\'s takeover in alarm.','''
N~A workplace should not need a battle plan between the front door and the desk.|
N~The report establishes an immediate threat to ordinary staff. Their safety comes first.|
N~Stay away from the grunts if possible. No employee needs to face them alone.|
D~It must feel unreal to have this happen somewhere you know so well.|
N~I hope there is somewhere they can wait safely with coworkers.|
N~The ordinary workday has been forcibly replaced by somebody else's ugly production.|
N~A familiar building can become strange in a terribly short time.|
N~Emergency conditions. Normal work priorities should stop.|
N~The desks are familiar; the voices in the corridors are wrong.|
N~Their alarm is reasonable. We should not treat it as mere background noise.|
N~I wonder whether anyone managed to leave before the doors were blocked.
''')
add('silph_back_to_work','SilphCo_6F_Text_BetterGetBackToWork',
    'After the takeover ends, the employee returns to ordinary duties.','''
S~Back to work sounds wonderfully boring after everything that happened.|
N~A return to routine can mark the restoration of a safer environment.|
S~Good. Hope they get a proper break too.|
S~There is something comforting about an ordinary next task.|
N~The work can wait long enough for everyone to catch their breath.|
S~The grand crisis gives way to the modest, valuable business of a normal day.|
S~An ordinary sentence made unexpectedly precious by the day around it.|
N~Operations resuming. Check the people before the productivity.|
S~The room is remembering what it used to be for.|
N~I hope nobody expects them to act as if nothing frightening happened.|
S~I wonder which familiar task feels easiest to begin again.
''')
add('silph_help6','SilphCo_6F_Text_HelpMePlease',
    'A frightened worker directly asks us for help.','''
N~A simple request. We should hear the fear before anything else.|
N~They need immediate safety information, not a demand to remain composed.|
N~Stay close to cover. We will not make them confront anyone.|
D~They sound so frightened. I would want to answer quietly.|
N~A clear safe next step would help more than a grand reassurance.|
N~No dramatic speech needed. Just a person asking not to be left in danger.|
N~A small plea is enough reason to take the situation seriously.|
N~Identify the immediate threat and the nearest safe place.|
N~Fear has made the sentence very small. The need is not small.|
N~We should not ask them to earn the help by appearing brave.|
N~I wonder whether they have anyone beside them who can stay calm.
''')
add('silph_engaged','SilphCo_6F_Text_WeGotEngaged',
    'After the danger, the worker happily announces an engagement.','''
U~That is quite a change in the office news! I hope the next celebration is quieter.|
S~A personal commitment has emerged alongside the return of safety.|
S~Good for them. Hope they make the choice kindly together.|
S~It is lovely to hear some happy news in this room at last.|
S~A good reason for a celebration after a very difficult day.|
S~The workplace drama has acquired an unexpected romantic epilogue.|
S~A small bright announcement in a building that needed one.|
S~Unexpected positive development! No technical explanation required.|
S~Two people have found a little future inside a difficult day.|
S~I hope the joy belongs to both of them equally.|
S~I wonder whether they had been hoping to say that for a while.
''')
add('silph_coward_comment','SilphCo_6F_Text_ThatManIsSuchACoward',
    'A worker insults the frightened man beside her as a coward.','''
N~People can be scared of criminals without failing a personality test.|
N~Fear in a dangerous situation is not evidence of poor character.|
N~He is frightened. Help him instead of scoring him.|
D~That would make feeling afraid even lonelier.|
N~A kind word would be more useful than calling him names.|
N~The unwilling audience has begun reviewing each other's survival performances.|
N~Nobody should have to look impressive while trying to stay safe.|
N~The alarm response is functioning. That is not a fault.|
N~A shaking hand is still a hand worth holding steady.|
N~A little compassion would suit this moment much better than contempt.|
N~I wonder whether he can hear everything she is saying.
''')
add('silph_helpless_comment','SilphCo_6F_Text_NeedsMeToLookAfterHim',
    'The newly engaged worker says her partner is helpless and needs her care.','''
N~Care sounds better when it leaves the other person a little dignity.|
N~Support can be valuable without defining the recipient as permanently incapable.|
N~Help him if he wants it. Do not turn a frightened day into his whole identity.|
N~I hope he gets to feel valued, not merely managed.|
N~Looking after someone works best when they still have a say.|
N~A romantic announcement has acquired an unnecessarily one-sided character description.|
N~A partnership should leave both people room to stand upright.|
N~Mutual support is more robust than one person claiming full control.|
N~Shelter should not become a room with the latch on the outside.|
N~She can be proud of helping without making him sound smaller.|
N~I wonder what he likes about the way they look after each other.
''')
add('silph_world_goal','SilphCo_6F_Text_RocketsTryingToConquerWorld',
    'A worker fears that Rocket wants world domination through Pokemon.','''
N~A very large ambition from people already being awful in one building.|
N~The worker describes a feared broader objective. The immediate threat is serious enough.|
N~Start by stopping what they are doing here. Staff need safety now.|
N~That thought would make an already frightening day feel enormous.|
N~One safe room and one safe person at a time still matter.|
N~The villains' ambitions have expanded well beyond their already intolerable local conduct.|
N~A huge threat can make it difficult to see the useful small thing in reach.|
N~Scope uncertain. Immediate containment remains a practical priority.|
N~A shadow can look endless when it falls across your own door.|
N~The fear is real even if the whole plan is not known to the worker.|
N~I wonder what they overheard that made them think the ambition was that large.
''')
add('silph_departure_credit6','SilphCo_6F_Text_RocketsRanAwayBecauseOfYou',
    'The worker credits us for driving Rocket away.','''
S~They can finally talk about Rocket in the past tense. Good change.|
S~The immediate danger has ended, and they connect that outcome with our intervention.|
S~Glad they are safe. The team did a lot of the hard work.|
S~You can hear the relief under the excitement.|
S~A normal day is a very good thing to help give back.|
S~The former emergency becomes a story the survivor can tell from safety.|
S~A frightening presence has become an absent one. That is enough for now.|
N~Hostiles withdrew. Staff can begin recovering the space.|
S~The room is no longer waiting for the next harsh footstep.|
S~A generous thank-you. We can make sure the partners hear it too.|
S~I wonder who they are most excited to tell that it is over.
''')
add('silph_products_targeted','SilphCo_6F_Text_TargetedSilphForOurMonProducts',
    'A worker thinks Rocket targeted Silph for its Pokemon-related products.','''
N~Making useful things should not mean criminals get to choose your workday.|
N~Valuable technology is a plausible motive, though the worker is inferring it.|
N~The products can be replaced. The people need protecting first.|
N~It is awful when something you helped make becomes a reason to feel unsafe.|
N~I hope the company remembers the people behind those products after this.|
N~Innovation has drawn an audience with unusually destructive purchasing methods.|
N~A clever thing can attract people who care very little for its maker.|
N~Threat model includes technology theft. Protect the staff along with the research.|
N~Useful work has cast a shadow its makers did not ask for.|
N~It is a sensible suspicion. The blame still belongs with the attackers.|
N~I wonder which projects the staff were most worried about losing.
''')
add('silph_job_offer','SilphCo_6F_Text_ComeWorkForSilphWhenYoureOlder',
    'A grateful employee suggests we work for Silph in the future.','''
M~An unusual recruitment process. Most interviews involve fewer occupied floors.|
S~They see useful qualities beyond our immediate intervention. A warm compliment.|
S~Kind offer. We have time to decide what work suits us.|
F~It is flattering to hear someone imagine a place for you in their future.|
S~A job worth choosing should leave room for a good ordinary life too.|
M~The rescue concludes with a very informal invitation to join the staff list.|
S~Someone has looked at a difficult day and found a possible future in it.|
S~Interesting offer. I would have questions about the actual work and tools.|
S~A new door has been mentioned, without asking us to walk through it today.|
S~A friendly possibility is nicer than a demand for a promise.|
S~I wonder which role the employee imagines us enjoying.
''')
add('silph_lapras','SilphCo_7F_Text_ExplainLapras',
    'After a successful Lapras handoff and naming flow, the employee explains Lapras\'s intelligence and swimming.','''
S~A clever new companion, trusted to us with a very hopeful goodbye.|
S~The handoff completed before this explanation. We now need to learn the individual's habits.|
S~Welcome aboard, Lapras. A partner first, transport second.|
S~I hope the change from the lab feels like a kinder, wider place to be.|
S~We should give the new arrival time to settle before expecting anything.|
S~A sheltered life opens into a journey, with a rather touching vote of confidence.|
S~A larger world can be a gift when there is someone patient beside you.|
S~An intelligent swimming partner! Lots to learn from, with no need to rush.|
S~A life kept indoors is being trusted with a road made of water.|
S~The employee sounds concerned about Lapras's future, not just the thank-you.|
S~I wonder what Lapras will notice first outside the building.
''')
add('silph_boardroom_worry','SilphCo_7F_Text_RocketBossWentToBoardroom',
    'On a later visit, the Lapras employee worries that Rocket\'s boss reached the president.','''
N~A useful direction, with a very worried person at the end of it.|
N~The boardroom is a specific lead. The president's current safety remains unknown to the worker.|
N~Head there prepared. The staff need a clear answer about who is safe.|
N~It is hard to hear how helpless the distance between floors makes them feel.|
N~We can keep the worker out of danger while following the lead.|
N~A familiar office has become the worrying destination of the whole building's attention.|
N~Concern travels upward more quickly than reliable news.|
N~Destination confirmed by report. Check the team before proceeding.|
N~A closed room above has gathered a great deal of fear around it.|
N~They want to know someone is all right, not hear another grand plan.|
N~I wonder when they last received an update from upstairs.
''')
add('silph_masterball_target','SilphCo_7F_Text_RocketsAfterMasterBall',
    'A researcher says Rocket came for the Master Ball.','''
N~A ball that catches anything would be a terrible thing to put in those hands.|
N~A guaranteed capture device would be a powerful target for an exploitative organization.|
N~Keep it away from Rocket. The partners they would use it on deserve better.|
N~That makes the takeover feel very deliberate.|
N~A useful invention can become frightening when the wrong people decide how to use it.|
N~The criminal plot has selected a prop with exceptionally ugly implications.|
N~A tool without a failure condition still needs a person with limits.|
N~Capability alone is not safety. Access control matters enormously here.|
N~A closed ball can be a much larger cage in the wrong hand.|
N~The device is impressive. Their reason for wanting it is the disturbing part.|
N~I wonder who on the project realized it was being targeted first.
''')
add('silph_project_canceled','SilphCo_7F_Text_CanceledMasterBallProject',
    'After Rocket leaves, the researcher says the Master Ball project was canceled.','''
N~A brilliant idea has left everyone with a very difficult decision about it.|
N~Canceling further development may reflect the consequences of its misuse risk.|
N~Better to stop than hand more power to people who will hurt partners with it.|
N~It must be hard to set aside something you worked on for so long.|
N~People matter more than finishing a project simply because it began.|
N~The invention's extraordinary promise has acquired consequences the proposal could not ignore.|
N~Sometimes the gentlest ending for a dangerous possibility is to leave it unfinished.|
N~A capability can be technically successful and still fail a broader design review.|
N~An unopened future can be a deliberate choice rather than a loss.|
N~I hope the people who made it are given time to find work they feel good about.|
N~I wonder how the team feels about the decision now the immediate danger is over.
''')
add('silph_takeover_fear7','SilphCo_7F_Text_BadIfTeamRocketTookOver',
    'A worker fears what Rocket control would mean for Silph and its Pokemon.','''
N~They are worried about the people and Pokemon inside the company, not just the name on the door.|
N~Institutional control would affect staff and living research subjects alike.|
N~They are right to worry. Keep them away from the grunts.|
N~It is awful having to imagine your familiar workplace under someone cruel.|
N~The Pokemon kept here need safe people looking after them.|
N~A corporate takeover becomes a very personal danger when the assets are alive.|
N~A name on a building can conceal many small lives depending on the people inside.|
N~Protect the living participants first. Equipment can wait.|
N~The door sign is less important than who is allowed to hold the keys.|
N~A reasonable fear from someone who knows what is at stake in the rooms.|
N~I wonder whether the Pokemon have somewhere protected away from the occupied halls.
''')
add('silph_surprised7','SilphCo_7F_Text_WowYouChasedOffTeamRocket',
    'The worker marvels that we drove Team Rocket out.','''
S~Not alone. There were quite a few determined Pokemon involved.|
S~The surprise is understandable, though the team deserves explicit credit.|
S~The partners did the hard part beside us. Glad the worker is safe.|
F~It feels strange to hear the whole day folded into one astonished sentence.|
S~A good outcome belongs to everyone who helped make it possible.|
S~The final summary has accidentally reduced an ensemble to a solo performance.|
S~A remarkable day is easier to tell than it was to stand inside.|
N~Successful outcome, shared effort. Include the full team in the record.|
S~Many little strengths carried the same difficult hour.|
S~We can accept the kindness while making room for the partners in it.|
S~I wonder what part of the news first reached this floor.
''')
add('silph_danger7','SilphCo_7F_Text_ReallyDangerousHere',
    'A frightened worker warns us away and cannot believe we can help.','''
N~They are trying to warn us even while they need help themselves.|
N~Fear and an uncertain assessment of our ability explain the reaction.|
N~Get them somewhere safer. No need to convince them with a speech.|
D~They sound worried for us as well as themselves.|
N~A practical safe step will mean more than a promise that everything will be fine.|
N~The intended rescue meets a frightened person reluctant to see another person put at risk.|
N~Concern can sound like refusal when it has nowhere safer to go.|
N~Demonstrate a safe route rather than arguing about capability.|
N~A scared voice is still trying to put a hand between us and the danger.|
N~It is a kind instinct, however hopeless they feel.|
N~I wonder whether they have watched anyone else get hurt trying to intervene.
''')
add('silph_thanks7','SilphCo_7F_Text_ThankYouSoMuch',
    'The previously frightened worker thanks us after the takeover ends.','''
S~A quieter voice, with much less fear inside it. That is good to hear.|
S~The danger has ended, and the gratitude follows a very real change in conditions.|
S~Glad they can breathe again. The team did well.|
S~A few plain words can hold an enormous amount of relief.|
S~I hope they have someone to spend a calmer evening with.|
S~The rescue finally becomes something the person can believe happened.|
S~A room returned to the people who were frightened inside it.|
N~A meaningful success condition: the staff feel safe enough to say this.|
S~The voice has found a little warmth under the fear.|
S~A sincere thank-you does not need more explanation than that.|
S~I wonder when they last felt comfortable enough to smile.
''')
add('silph_finished_fear','SilphCo_8F_Text_WonderIfSilphIsFinished',
    'An employee fears the takeover means the end of Silph.','''
N~It is hard to imagine an ordinary next week while the building feels like this.|
N~They are projecting an uncertain crisis into a permanent outcome. The uncertainty is understandable.|
N~Start with keeping people safe. The company's future can be sorted afterward.|
D~A familiar life can feel very fragile when the place it depends on is threatened.|
N~They deserve a clear answer from someone responsible when the danger is over.|
N~An entire working future has begun to look like a story ending mid-page.|
N~A job can hold far more of a life than the tasks written under its title.|
N~Current failure does not establish permanent collapse. First contain the immediate damage.|
N~A building can feel like the edge of someone's whole world.|
N~I hope the staff are included when people start deciding what comes next.|
N~I wonder how long they have worked here.
''')
add('silph_thanks8','SilphCo_8F_Text_ThanksForSavingUs',
    'The employee thanks us after fears for Silph\'s future give way to safety.','''
S~The end of the company has become a much nicer sentence. Good.|
S~The immediate crisis has passed, leaving room for recovery rather than speculation about collapse.|
S~They are safe. That comes before any name on the building.|
S~It is lovely to hear the fear loosen its hold.|
S~A future that includes ordinary work again must feel very welcome.|
S~The threatened ending has become a beginning of the next working day.|
S~A small thank-you from someone who briefly could not see what came next.|
N~Emergency resolved. Recovery can proceed on a much steadier basis.|
S~A little future has returned to the room.|
S~I hope the relief lasts long enough for everyone to recover properly.|
S~I wonder what they are most glad to have back.
''')
add('silph_tools_fear','SilphCo_8F_Text_ToRocketBossMonsAreTools',
    'A worker fears Giovanni\'s cruelty and his view of Pokemon as tools.','''
A~A living partner should never have to earn the right to be treated like it matters.|
N~Treating Pokemon solely as instruments removes necessary concern for their welfare.|
A~Keep him away from them. They deserve care, not a use assigned by him.|
D~It is frightening to hear someone talk about living things without warmth.|
A~Useful or not, every partner still needs a safe place and decent treatment.|
N~A tyrant's efficiency is merely cruelty with a neatly labeled objective.|
A~A creature is not a thing just because someone finds it convenient to think so.|
N~Living partners are not interchangeable components. The premise is wrong.|
N~A hand that only grasps has forgotten what holding safely means.|
A~I understand why the staff are afraid of the kind of place he would make this.|
N~I wonder whether any of the Pokemon here have already been put in his custody.
''')
add('silph_rest_encouragement','SilphCo_9F_Text_DontGiveUp',
    'After offering a restorative rest, the helper encourages us to continue.','''
S~A rest first, a brave word afterward. That is the right order.|
S~Encouragement is more useful when paired with practical recovery.|
S~Good help. Now check the team before going back out.|
S~It is easier to keep going when somebody has noticed you were tired.|
S~A little care can make the next part feel manageable again.|
S~The encouraging line arrives after the kind action that gives it weight.|
S~A small safe pause holding the rest of the journey together.|
N~Recovery completed before renewed effort. Excellent support sequence.|
S~A little shelter can put the road back beneath your feet.|
S~The encouragement feels earned by the care that came before it.|
S~I wonder how many frightened people this helper has already steadied.
''')
add('silph_thanks9','SilphCo_9F_Text_ThankYouSoMuch',
    'After Rocket leaves, the helper thanks us.','''
S~They offered us a rest when it mattered. I am glad the safety came back their way too.|
S~The support was reciprocal: they helped us continue, and the intervention improved their situation.|
S~They helped the team first. Good to have been useful in return.|
S~It is lovely when a kind person gets to feel relieved too.|
S~They made room for our rest. Now they deserve their own quiet evening.|
S~The supporting character receives a safer ending for the whole scene.|
S~A little care has traveled in both directions.|
N~Shared effort produced the outcome. Their practical contribution mattered.|
S~A warm place offered has become a warm place returned.|
S~We should remember that we were helped along the way.|
S~I wonder what they need after spending the day looking after others.
''')
add('silph_crying','SilphCo_10F_Text_WaaaImScared',
    'An employee openly cries in fear during the takeover.','''
D~They are frightened. Nobody needs to be witty about that.|
D~An acute fear response deserves calm support and a safer setting.|
N~Get them away from the danger. Let them cry if they need to.|
D~I wish the room could feel gentler for them right now.|
N~A calm voice and a safe place would help more than telling them to stop.|
D~No audience commentary required. Just somebody having a terrible day.|
D~There is nothing undignified about being unable to hide fear.|
N~Reduce the threat and the noise. Emotional control is not the first priority.|
D~A frightened voice needs room to tremble without being punished for it.|
N~We can protect their dignity without pretending not to hear the distress.|
N~I wonder whether someone they trust is still on this floor.
''')
add('silph_crying_secret','SilphCo_10F_Text_KeepMeCryingASecret',
    'Afterward, the employee asks us not to tell others they cried.','''
S~Their secret is safe. Being scared did not make them smaller.|
S~Privacy is a reasonable request after a vulnerable moment.|
S~We will not make their fear into gossip.|
S~I understand wanting to keep that moment for yourself afterward.|
S~They should not have to worry about being teased on top of everything else.|
S~A private scene will remain private. Not every story belongs in the retelling.|
S~Some memories deserve a closed little drawer.|
N~Confidentiality request received. No reason to redistribute the information.|
S~The shaky part of the day can rest without an audience.|
S~Of course. Kindness includes knowing which details to leave alone.|
S~I hope the people here would be gentle if they knew anyway.
''')
add('silph_masterball_received','SilphCo_11F_Text_ThatsOurSecretPrototype',
    'After giving the Master Ball, the president explains its guaranteed capture and asks for discretion.','''
U~An extraordinary gift with a very quiet introduction. We should think carefully before using it.|
N~The prototype has exceptional capability, and the request for discretion is explicit.|
N~Keep it safe. A powerful tool still needs a careful choice.|
N~It feels like a lot of trust placed in one small object.|
N~A generous reward does not mean we need to decide how to use it immediately.|
N~The confidential prototype enters our care with a rather weighty final line.|
N~Something can be tiny enough for a pocket and still carry a large responsibility.|
U~Guaranteed capture is a remarkable claim. Secure storage first, questions later.|
N~A small closed shape holding a very consequential possibility.|
N~We can be grateful and still take time to understand the choice it gives us.|
N~I wonder how the people who developed it feel about seeing it leave the lab.
''')
add('silph_president_no_room','SilphCo_11F_Text_YouHaveNoRoomForThis',
    'The president cannot give his reward because our bag is full.','''
N~An entire rescue, concluded by a pocket refusing one more object. Very practical anticlimax.|
N~The intended reward did not transfer. Lack of space is the stated obstacle.|
N~Sort the bag. No reason to make this harder for anyone.|
F~It is awkward to be unprepared after such heartfelt thanks.|
N~A little tidying will let us accept the generosity properly.|
N~The grand gratitude has encountered the remarkably democratic limits of luggage.|
N~A full bag is unimpressed by wealth, titles, and dramatic timing.|
N~Capacity failure at handoff. No reward should be assumed received.|
N~The small place we carry has held up a much larger moment.|
N~We can fix our own inconvenience without making him feel responsible.|
N~I wonder how much of the bag we have been carrying out of habit.
''')
add('silph_secretary_thanks','SilphCo_11F_Text_ThanksForRescuingUs',
    'The secretary thanks us on behalf of the president and all staff.','''
S~It is good that the thanks includes everyone, not just the biggest office.|
S~Her wording recognizes the takeover as a threat across the whole workforce.|
S~Glad the staff are safe. Every floor mattered.|
S~A simple collective thank-you makes the whole building feel more human.|
S~I hope everyone gets a quiet chance to recover, from the front desk upward.|
S~The final acknowledgment gives the supporting cast its proper share of the ending.|
S~A tall building is still mostly made of ordinary people's days.|
N~Staff-wide safety restored. That is the outcome worth recording.|
S~Many familiar rooms can begin to feel like their own again.|
S~She remembered the people beyond the room. A thoughtful way to speak.|
S~I wonder how the staff will mark their first peaceful day back.
''')
add('silph_connor','SilphCo_2F_Text_ConnorPostBattle',
    'Connor admits working for both Silph and Team Rocket.','''
N~Two employers, one remarkably ugly conflict of interest.|
N~His divided allegiance directly compromises the people relying on him at Silph.|
A~He helped endanger his own coworkers. A second job is no excuse.|
N~That would make the people around him feel betrayed.|
N~The coworkers trusted him with an ordinary working day.|
N~The double role is less impressive than the damage it leaves behind.|
N~An extra name on the pay slip does not divide the responsibility.|
N~Conflicting access and incentives. A serious failure of trust.|
N~He has brought a cruel voice through a familiar door.|
A~Being trusted by people should mean more than another opportunity.|
N~I wonder how many coworkers knew him before this happened.
''')
add('silph_jerry','SilphCo_2F_Text_JerryPostBattle',
    'Jerry challenges us to navigate Silph\'s complicated interior.','''
N~An office that requires maze skills has taken workplace confusion too literally.|
N~A complex layout increases the value of a deliberate route record.|
N~We can map it. No need to wander into every fight.|
N~I would like a simple sign pointing to a simple staircase.|
N~A confusing route is a good reason to pace the team carefully.|
N~The architectural challenge has received a rather smug introduction.|
N~An unreasonable amount of building between a person and the room they need.|
N~Track state and position. Teleporters make casual intuition unreliable.|
N~A corridor can hide its direction even when it is brightly lit.|
N~The layout is impressive in precisely the way that makes visitors tired.|
N~I wonder whether the regular staff still take wrong turns.
''')
add('silph_teleport_tiles','SilphCo_2F_Text_Grunt1PostBattle',
    'The grunt identifies the diamond tiles as Silph teleporters.','''
N~A diamond-shaped shortcut with a rather uncertain destination. Step thoughtfully.|
S~The tiles are transport devices, explaining the apparent discontinuities in the layout.|
N~Remember where each one takes us. Useful does not mean simple.|
N~It is unsettling when the next room is not physically beside the last one.|
N~A little route note would save a lot of backtracking.|
N~The floor has been given a supporting role in relocating the entire cast.|
S~A small bright shape that makes distance briefly change its mind.|
U~Built-in transporters! Fascinating, though the labeling needs work.|
N~The room has little doors lying flat on the ground.|
N~A clear explanation makes the floor much less mysterious.|
N~I wonder whether each tile always leads to the same place.
''')
add('silph_association','SilphCo_2F_Text_Grunt2PostBattle',
    'The grunt claims Silph will become associated with Team Rocket.','''
A~That is a very polite word for threatening the people who work here.|
N~A coerced takeover is not a voluntary association between equal parties.|
A~The staff did not agree to this. He can stop dressing it up.|
N~That sounds worse for how casually he says it.|
A~A company is full of people who deserve a say in what happens to them.|
N~The villainous proposal has borrowed the dullest possible business vocabulary.|
N~An ugly act does not become mild when given an office-friendly name.|
N~Consent is missing from this proposed integration. That matters.|
N~A hand around a door handle can still be forcing its way inside.|
A~He wants the name to sound respectable while the behavior stays cruel.|
N~I wonder whether he has listened to a single employee's answer.
''')
add('silph_card_hint3','SilphCo_3F_Text_GruntPostBattle',
    'The grunt tells us the Card Key opens Silph\'s doors.','''
N~A very small answer to a building full of closed questions.|
N~The Card Key is the relevant credential for the locked doors.|
N~Find the key. Keep track of which route it opens.|
N~At least the obstacle has a clear practical answer.|
N~A useful lead before the team spends more energy searching blindly.|
N~The reluctant informant introduces a crucial piece of office stationery.|
N~A flat little thing deciding how large the building is allowed to be.|
N~Access token identified. That explains the electronic locks.|
N~One card can turn walls back into doorways.|
N~A plain explanation is welcome, whatever his reason for giving it.|
N~I wonder who was supposed to keep the key secure.
''')
add('silph_jose','SilphCo_3F_Text_JosePostBattle',
    'Jose says Rocket promised to let him study Pokemon if he helped them.','''
N~An interesting subject does not make the people offering access trustworthy.|
N~A research opportunity does not justify aiding coercion or ignoring welfare.|
A~He chose a chance to study over the safety of the people beside him.|
N~I wish he had thought about what kind of studying those people would permit.|
N~Curiosity needs care beside it, especially when the subject is alive.|
N~The tempting offer has rather conspicuously omitted the moral cost of admission.|
N~Knowledge gathered by cruelty is not made gentler by calling it curiosity.|
N~Access is useful only within a sound method. Their method is already causing harm.|
N~A door to understanding should not open by closing a cage.|
A~Being offered something desirable does not erase what they asked him to do.|
N~I wonder whether he ever asked what would happen to the Pokemon afterward.
''')
add('silph_boss_interest4','SilphCo_4F_Text_Grunt1PostBattle',
    'The grunt boasts that his boss has long wanted Silph.','''
N~Wanting a place does not make its people something you get to take.|
N~Prior ambition does not establish any legitimate claim to the company.|
A~His boss wanted it. The staff wanted a safe workday. Their claim matters.|
N~He sounds pleased about something the people here find terrifying.|
A~An employer's dream is not more important than everyone else's safety.|
N~An old desire is presented as though it were a deed of ownership.|
N~Greed does not become history worth honoring just by lasting a long time.|
N~Desired asset and authorized access are different states.|
N~A long shadow still has no right to the room it falls across.|
A~They have made wanting something sound like permission. It is not.|
N~I wonder how much the staff knew of that interest before today.
''')
add('silph_rodney','SilphCo_4F_Text_RodneyPostBattle',
    'Rodney explains the electronic locks and their Card Key requirement.','''
N~The doors are not being stubborn. They are being very specifically electronic.|
N~The locks require the matching credential rather than physical force.|
N~Find the Card Key. Do not waste the team's strength on the doors.|
N~A clear explanation makes the maze feel a little less personal.|
N~Knowing what we need saves a lot of unnecessary effort.|
N~The building's refusal to admit us has a technical rather than dramatic cause.|
N~The quietest barrier can still be a firm one.|
S~Electronic authentication. Now the door behavior is less mysterious.|
N~A little card can carry permission farther than a loud voice.|
N~Useful detail, directly stated. Appreciated.|
N~I wonder how the employees manage when someone misplaces a card.
''')
add('silph_report_boss4','SilphCo_4F_Text_Grunt2PostBattle',
    'The grunt plans to report to the boss on the eleventh floor.','''
N~A threat that accidentally includes an address. We should remember the useful part.|
N~He identifies the boss's location while describing his intended report.|
N~Eleventh floor. Keep ready; the warning may get there first.|
N~It is unsettling knowing somebody could be waiting for us now.|
N~A clear destination is useful, but not a reason to hurry the team.|
M~The messenger supplies his destination with admirable generosity to the opposition.|
N~A hostile voice has still managed to point the way.|
N~Destination intel obtained. Expect possible increased alertness upstairs.|
N~His hurried words have drawn a little line toward the top of the building.|
N~He could have kept the floor number to himself. Fortunately, he did not.|
N~I wonder whether the boss has already heard from the other floors.
''')
add('silph_warning5','SilphCo_5F_Text_Grunt1PostBattle',
    'The grunt calls it unwise to oppose Team Rocket.','''
N~Letting them carry on has its own fairly obvious disadvantages.|
N~The statement offers intimidation rather than an argument about the conduct being opposed.|
N~The people here need help. His warning does not change that.|
N~He wants caution to mean doing nothing at all.|
N~We can be careful and still refuse to leave people in danger.|
N~The villain advises the audience that the whole plot would be easier without resistance.|
N~A sensible concern for safety is being used to sell surrender.|
N~Risk is real. So is the cost of leaving the problem untouched.|
N~A dark road is still sometimes the road someone needs you to walk.|
N~He has mistaken refusing to be frightened away for refusing to think.|
N~I wonder whether that line has stopped many people before.
''')
add('silph_beau','SilphCo_5F_Text_BeauPostBattle',
    'Beau describes work on a ball intended to catch any Pokemon.','''
U~That is a very large promise to put inside a very small sphere.|
S~A universal capture claim would represent exceptional technical capability and serious ethical choices.|
N~Hope the people making it think hard about who gets to use it.|
N~It is impressive and unsettling in the same breath.|
N~A useful invention still needs people willing to ask who it could hurt.|
N~The ultimate prop promises to remove the uncertainty from every encounter. A weighty claim.|
N~A tool that never fails can make a careless intention much more dangerous.|
U~Extraordinary design target. The failure modes extend beyond the mechanism itself.|
N~A little closed room that could decide the next part of a life.|
N~The work is impressive. I would like to hear the limits they set around it.|
N~I wonder which question the researchers found hardest to answer.
''')
add('silph_dalton','SilphCo_5F_Text_DaltonPostBattle',
    'Dalton taunts us that the boss is still many floors above.','''
N~A tall building is not an argument. It is mostly stairs.|
N~The remaining distance is practical information, even delivered as discouragement.|
N~We will take the floors as they come. Watch the team's condition.|
N~I would rather know how far it is than have to guess.|
N~A long way is manageable with sensible pauses and supplies.|
N~The obstacle's spokesman has reduced the threat to an elevation report.|
N~The next floor is still only one floor away.|
N~Remaining workload substantial. Pace resources rather than reacting to the taunt.|
N~A high room is reached by small ordinary steps.|
N~He has told us the scale of the problem. We do not have to borrow the attitude.|
N~I wonder whether he ever takes the stairs himself.
''')
add('silph_koffing_evolution','SilphCo_5F_Text_Grunt2PostBattle',
    'The grunt abruptly changes the subject to Koffing evolving into Weezing.','''
U~An unexpected educational detour. The conversation has grown a second head.|
N~The fact is relevant to Pokemon development, though oddly disconnected from his situation.|
N~Useful fact. Does not excuse the work he is doing here.|
N~It is a strange moment to start sharing something ordinary.|
N~Knowing a partner's development is worthwhile in a much kinder setting than this.|
M~The hostile encounter briefly becomes an unsolicited natural-history lesson.|
M~A conversation trying to escape itself through a cloud of Pokemon trivia.|
N~Correct topic, peculiar timing. No change to the immediate problem.|
N~A small normal fact has wandered into a very abnormal day.|
N~He sounds almost like an ordinary enthusiast for a moment.|
N~I wonder what made that particular thought interrupt everything else.
''')
add('silph_brothers6','SilphCo_6F_Text_Grunt1PostBattle',
    'The grunt promises that his brothers will avenge him.','''
N~He has a surprisingly extensive family plan for losing battles.|
N~The threat implies further coordinated hostility, whether the relationship is literal or organizational.|
N~Keep alert. He is not the only hostile person here.|
N~That makes it difficult to feel the encounter is really finished.|
N~We should keep together and avoid giving them an easy opening.|
N~The defeated speaker refers the sequel to a larger ensemble.|
N~An unpleasant promise with several possible footsteps attached.|
N~Potential reinforcement threat. Do not assume the route is clear.|
N~One voice gone quiet may still have called another one closer.|
N~He can stop trying to make his embarrassment everyone else's problem.|
N~I wonder whether his brothers are as eager for the fight as he says.
''')
add('silph_taylor','SilphCo_6F_Text_TaylorPostBattle',
    'Taylor gives an odd geographic answer about Silph\'s Tiksi branch.','''
U~That branch sounds like quite a commute from this office.|
N~He offers a specific location claim, but it does not explain his choices here.|
N~A branch office is not the pressing issue. The people here need safety.|
N~That is a strange bit of ordinary company knowledge to hear now.|
N~The company has people far away who may have no idea what is happening here.|
N~The defeated employee diverts us into a distant corporate footnote.|
N~A faraway place can feel unreal while the danger is in the next corridor.|
N~Location detail noted, though its immediate usefulness is limited.|
N~The building holds names of places beyond the windows we can see.|
N~He has found a very distant subject to avoid the nearby problem.|
N~I wonder whether anyone from this office has actually worked there.
''')
add('silph_justice6','SilphCo_6F_Text_Grunt2PostBattle',
    'The grunt says standing for justice betrays the bad guys.','''
M~That is a remarkably honest job description. Terrible argument, excellent labeling.|
N~Opposing harmful conduct is not a betrayal of any legitimate obligation to him.|
N~Fine. The bad guys can manage their disappointment.|
N~He says it as if we had ever agreed to help them.|
N~The people being hurt deserve more consideration than the people complaining about being stopped.|
M~The villain has correctly identified his side and completely misunderstood our duties to it.|
M~A very clear moral map, kindly supplied by the person standing on the wrong side.|
N~No contractual dependency on the bad guys detected. Proceed.|
N~A shadow is offended that someone brought a light.|
M~It is considerate of him to make the disagreement that easy to understand.|
N~I wonder whether he hears how strange that complaint sounds aloud.
''')
add('silph_scurry7','SilphCo_7F_Text_Grunt3PostBattle',
    'The grunt taunts our difficulty navigating toward the boss.','''
N~Scurrying? I prefer exploratory walking with an occasionally wrong turn.|
N~Random movement is inefficient. His taunt still points toward using a deliberate route.|
N~Map the path. Do not let him hurry us into a mistake.|
N~The layout is confusing enough without someone enjoying the confusion.|
N~A calm plan saves more energy than trying to look certain.|
N~The maze's heckler is less useful than a single well-placed arrow.|
N~Being lost is unpleasant without a commentator.|
N~Track the route and teleporter destinations. Better than reacting to the insult.|
N~The way through is still there, however much he laughs at the searching.|
N~He can keep the commentary. We need clear directions.|
N~I wonder whether he knows the route or merely knows how to mock visitors.
''')
add('silph_joshua','SilphCo_7F_Text_JoshuaPostBattle',
    'Joshua acknowledges our skill while expressing surprise at our age.','''
S~The team has supplied enough evidence to get past his first impression.|
N~The observed performance is a better estimate than age-based expectation.|
N~We trained for it. Age did not choose the moves.|
S~It is nice to hear the skill recognized, even with the surprised little qualifier.|
N~Young trainers still put real time and care into their teams.|
N~The critic revises his forecast after consulting the actual performance.|
N~A calendar has lost another argument with a determined person.|
N~Model updated with evidence. Good, though the original shortcut was weak.|
S~A small traveler can carry a long stretch of careful work.|
N~He could have simply said skilled. The rest was his assumption.|
N~I wonder how often he has underestimated someone that way.
''')
add('silph_brothers7','SilphCo_7F_Text_Grunt1PostBattle',
    'The grunt dismisses losing and promises retaliation from his brothers.','''
N~If it does not matter, he has chosen an unusually threatening way to relax about it.|
N~The dismissal conflicts with the promised retaliation. Continued hostility is the relevant fact.|
N~Watch for the others. We are not finished just because he is.|
N~I would rather not stand here while he imagines a second attack.|
N~Keep the group together and the route in mind.|
N~A supposedly insignificant defeat receives an ambitiously staffed revenge sequel.|
N~Indifference is wearing a remarkably angry face.|
N~Local win does not remove network risk. Keep checking the next corridor.|
N~One stopped voice is pointing toward several more.|
N~He is trying to make the threat do what his battle could not.|
N~I wonder whether the others know they have been volunteered for this.
''')
add('silph_boss_anger7','SilphCo_7F_Text_Grunt2PostBattle',
    'The grunt urges us to leave before his boss becomes angry.','''
N~The boss's mood is not a good regional safety system.|
N~The warning implies danger without offering any justification for the operation.|
N~People here are already in danger. We are not leaving them because he is annoyed.|
N~It is unsettling how often the staff and grunts talk about that man's anger.|
N~A boss who makes everyone afraid is part of the problem.|
N~The local threat delegates its dramatic authority to someone supposedly more irritable upstairs.|
N~An angry man is not a reason to accept an ugly situation forever.|
N~Known hostile authority. Prepare carefully rather than treating the mood as a rule.|
N~A distant temper should not decide how much safety everyone else gets.|
N~He thinks fear of the boss will explain everything. It explains quite enough.|
N~I wonder whether he is more afraid for us or for himself.
''')
add('silph_rival7','SilphCo_7F_Text_RivalPostBattle',
    'The rival boasts that Pokedex study will help him defeat the League, then departs.','''
N~Useful research, enormous confidence, and somehow still room for a parting jab.|
S~Using the Pokedex to study capabilities and evolution is genuinely sensible preparation.|
N~He can chase the League. We still have people in this building to help.|
N~I wish he had noticed the frightened staff as clearly as his own next goal.|
N~Learning is good. The current situation deserves some attention too.|
M~The rival's future triumph receives an advance review written by the rival himself.|
N~A busy ambition can make a person strangely inattentive to the room around them.|
N~Research-informed planning is useful. Self-assigned genius rating is less measurable.|
N~His eyes keep traveling toward a far door while nearby ones remain in trouble.|
N~The practical part is worth hearing beneath the grand presentation.|
N~I wonder whether anyone here will remember him as anything besides in a hurry.
''')
add('silph_backup8','SilphCo_8F_Text_Grunt1PostBattle',
    'The grunt threatens to call for backup unless we retreat.','''
N~He has found the part of the plan labeled ask someone else.|
N~Potential reinforcement is a practical risk even when used as intimidation.|
N~Keep ready. Do not stand around waiting for him to prove it.|
N~That makes the quiet corridor feel less empty.|
N~We should avoid leaving anyone exposed while the alert spreads.|
N~The defeated opponent attempts to enlarge the cast by telephone.|
N~A threat is not less unpleasant for arriving with company.|
N~Escalation possible. Reassess route and remaining resources.|
N~One call can put more sharp footsteps into the hallway.|
N~He wants the warning to make the decision for us. We can still think carefully.|
N~I wonder how close the nearest backup is.
''')
add('silph_parker','SilphCo_8F_Text_ParkerPostBattle',
    'Parker asks what we think of Silph\'s maze-like interior.','''
N~A strong case for putting the stairs somewhere less philosophical.|
N~The layout is technically interesting but creates substantial navigation overhead.|
N~Bad place to be lost during an emergency. That is my review.|
N~I would like it more if fewer people were frightened inside it.|
N~A useful building should make getting help easier, not harder.|
N~An architectural critic requests a review from a captive research sample.|
N~A bright labyrinth still feels like a labyrinth when you need the door.|
N~Fascinating mechanism, poor wayfinding. Both can be true.|
N~Many doors, not enough clear directions between them.|
N~It has presence. It could use a kinder relationship with its visitors.|
N~I wonder whether he helped design it or simply enjoys watching people navigate it.
''')
add('silph_other_brothers8','SilphCo_8F_Text_Grunt2PostBattle',
    'The grunt leaves further fighting to his brothers.','''
N~The next encounter has been assigned to somebody else's calendar.|
N~His withdrawal does not imply that the broader threat has ended.|
N~Fine. Watch the route for the next one.|
N~I wish he sounded more interested in stopping than passing the danger along.|
N~The team still needs a steady pace through the remaining floors.|
N~The recurring villain role is handed down to the next available performer.|
N~An unpleasant shift change, without any improvement in the job.|
N~Local unit disengaging. Network still active.|
N~A rough voice leaves the door open for another rough one.|
N~He seems comfortable making other people finish the fight.|
N~I wonder how much choice his brothers get in that arrangement.
''')
add('silph_age_regret9','SilphCo_9F_Text_Grunt1PostBattle',
    'The grunt imagines how his life might differ if he began training at our age.','''
N~A different start might have helped. A different next choice is still available.|
N~The counterfactual is uncertain. His present conduct remains something he can change.|
N~He can start making better choices now. The past is not an instruction.|
N~That sounds almost like regret, before the sentence disappears.|
N~It is not too late to care for Pokemon without using them to frighten people.|
N~A villain briefly glimpses an unwritten earlier chapter and forgets to finish the line.|
N~A missed beginning need not make every later door false.|
N~Initial conditions matter, but they do not fix every future action.|
N~An old path cannot be walked again. The next step is still under his own feet.|
N~I hope he lets that thought change something rather than simply excuse it.|
N~I wonder what he wanted to be before ending up here.
''')
add('silph_ed','SilphCo_9F_Text_EdPostBattle',
    'Ed acknowledges that exploiting type weaknesses is effective.','''
N~The matchup has delivered its lesson in very direct language.|
N~Type relationships are a substantial tactical variable, as the result demonstrates.|
N~Know the opponent. Raw strength is not the whole plan.|
N~A clear lesson is something useful to take from a difficult match.|
N~Good planning can save the team from unnecessary strain.|
N~The defeated critic confirms the technique that just complicated his afternoon.|
N~A small weakness can matter more than an imposing outline.|
N~Correctly matched tool, improved result. Basic and effective.|
N~A strong door can still have a small latch.|
N~He has noticed something specific instead of reaching for an excuse.|
N~I wonder what he will change in his own team's coverage.
''')
add('silph_avenge9','SilphCo_9F_Text_Grunt2PostBattle',
    'The grunt promises revenge from his brothers.','''
N~Another family reunion I would rather miss.|
N~He is invoking further hostility rather than accepting the encounter as finished.|
N~Stay alert. No reason to give his friends an easy chance.|
N~I wish the next corridor could simply be a corridor.|
N~Keep the team close and the way back clear.|
N~The revenge department appears to employ a great many relatives.|
N~A tired threat, still capable of making the room less comfortable.|
N~Potential linked threat remains. Check the next area carefully.|
N~An angry voice points toward footsteps we cannot hear yet.|
N~He is trying to make losing sound like an appointment we cannot cancel.|
N~I wonder whether any of his brothers want a quieter life than this.
''')
add('silph_boardroom10','SilphCo_10F_Text_GruntPostBattle',
    'The grunt tells us the boardroom is one floor above.','''
N~One floor left to the right office. The directions are finally getting shorter.|
N~A precise nearby destination helps narrow the remaining route.|
N~Check the team, then go up prepared.|
N~It is a little reassuring to know the search is not endless.|
N~A short pause here could help before a difficult next room.|
N~The reluctant guide places the next scene exactly one level overhead.|
N~The journey's height has become a manageable number.|
N~Destination one level up. Final readiness check is worthwhile.|
N~The next ceiling is nearly the last one between us and an answer.|
N~Useful directions, despite the tone they arrived in.|
N~I wonder whether the people upstairs know help is this close.
''')
add('silph_travis','SilphCo_10F_Text_TravisPostBattle',
    'Travis urges us to leave after beating him.','''
N~This was never a sightseeing tour of his personal defeat. There are people to help.|
N~He frames the visit as personal competition, ignoring the broader emergency.|
N~We are not here just for him. Keep moving toward the staff who need help.|
N~He sounds eager to make the whole situation smaller than it is.|
N~Leaving now would not make the frightened people here safe.|
N~A supporting antagonist attempts to declare himself the conclusion of the entire plot.|
N~His embarrassment is not the only thing happening in this building.|
N~Local obstacle cleared. Main objective remains unresolved.|
N~One closed conversation does not mean the way ahead has ended.|
N~He can finish his part without deciding ours is over.|
N~I wonder whether he ever considers the people outside his own room.
''')
add('silph_giovanni','SilphCo_11F_Text_GiovanniPostBattle',
    'Giovanni retreats, condemns our interference, and claims all Pokemon exist for Team Rocket.','''
A~The Pokemon were not consulted about that ridiculous claim. They have lives beyond him.|
N~He asserts ownership without any legitimate basis and promises continued hostility.|
A~They do not exist for him. Keep ready until he is out of here.|
N~I am glad he is leaving. The way he talks about living things is chilling.|
A~No plan of his matters more than the care those partners deserve.|
N~The retreating tyrant attempts to leave an entire world under his name in the final sentence.|
A~A man can claim the sun too. It does not make the light his property.|
N~The premise is false. A stronger declaration cannot repair it.|
N~A closed hand imagines everything was made to fit inside it.|
A~He has confused having power with being entitled to everyone else's lives.|
N~I wonder whether he can imagine a Pokemon choosing something he did not order.
''')
add('silph_boss_question11','SilphCo_11F_Text_Grunt2PostBattle',
    'The grunt asks whether we want to see his boss.','''
N~After this many floors, the direction of our interest seems fairly well established.|
N~He recognizes the objective at last, though he has supplied no new detail.|
N~Yes. The staff need this finished. No more stalling.|
N~I would like the frightening part of this building to end.|
N~The people here deserve an ordinary safe room again.|
N~The final gatekeeper asks the question answered by the whole preceding staircase.|
N~A very late opportunity for a remarkably obvious introduction.|
N~Objective confirmed. Next step should be a clear route, not another query.|
N~The name at the end of the corridor has been spoken enough.|
N~He seems to have run out of more elaborate objections.|
N~I wonder whether he expected anyone to come this far.
''')
add('silph_tough_boss11','SilphCo_11F_Text_Grunt1PostBattle',
    'The grunt warns that his boss favors tough Pokemon.','''
N~A tough team still needs a decent person deciding what to ask of it.|
N~Preference for strong Pokemon does not identify their exact capabilities or welfare.|
N~We will be ready. His partners are not the ones choosing the cruelty.|
N~I worry more about what he asks them to endure than how intimidating they look.|
N~The stronger partner still deserves ordinary care.|
N~The ominous introduction confuses physical power with any reason for trust.|
N~A strong creature can still be trapped in a small-minded person's plan.|
N~High expected capability. Prepare without assuming a particular composition.|
N~Even a hard shell can carry something that needs gentleness.|
N~A preference for tough partners tells us very little about being a good trainer.|
N~I wonder what he values in them when they are not winning for him.
''')
