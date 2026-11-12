"""Additional Kanto NPC replies in the established eleven-voice order."""
ROWS=[]
EMOTIONS=dict(N='neutral',S='soft_smile',A='annoyed',F='flustered',D='sad',
              U='surprised',M='smug',L='laughing')
def add(key,labels,subject,lines):
    replies=[]
    for line in lines.strip().split('|'):
        line=line.strip()
        if len(line)>1 and line[1]=='~' and line[0] in EMOTIONS:
            line=EMOTIONS[line[0]]+line[1:]
        replies.append(line)
    assert len(replies)==11,(key,len(replies))
    ROWS.append(dict(key=key,labels=labels.split(),subject=subject,replies=replies))

add('pewter_hobbyists_and_brock','PewterCity_Text_BrockOnlySeriousTrainerHere',
    'A local dismisses Bug Catchers as hobbyists while praising Brock as a serious trainer.','''
M~I would like to hear him explain that distinction to a very determined Beedrill.|
N~An interest can begin as a hobby and still involve considerable knowledge and care.|
N~Taking good care of a Wurmple counts. Brock being capable does not make everyone else pointless.|
N~I dislike the idea that enjoying something makes your effort less real.|
N~I hope the Bug Catchers here know somebody appreciates what they do.|
M~He has appointed himself critic of the local training scene. The review seems rather narrow.|
N~I would rather be sincerely interested in something than perform seriousness for somebody like that.|
N~I have learned useful things from people who were supposedly just messing about.|
N~There is room for more than one way to care about Pokemon.|
N~He could praise Brock without dressing everybody else down first.|
N~I would like to hear the hobbyists describe their own work.
''')

add('pewter_gym_guide_arrival','PewterCity_Text_GoTakeOnBrock',
    'Having led us to the gym, the guide urges us to challenge Brock.','''
M~He has delivered us to the challenge. I hope there is equally enthusiastic guidance toward lunch afterward.|
N~We know where the Gym is. We can still decide when the team is ready.|
N~Being shown the door does not mean we have to walk through it immediately.|
S~He sounds excited for us. I hope the nerves leave some room to enjoy the first step.|
N~We should check that everybody is comfortable before accepting the invitation.|
M~Our entrance has been arranged. I would still like a moment with the script.|
N~I prefer encouragement that leaves room to take a breath first.|
N~We have reached the right building. Preparation remains our responsibility.|
N~We can be grateful for the help and choose our own pace.|
S~I hope he enjoys hearing how it went when we come back out.|
N~I would remember this spot. First arrivals can look ordinary once they become familiar.
''')

add('pewter_museum_guide_arrival','PewterCity_Text_ThisIsTheMuseum',
    'The guide has led us to the museum and says the admission fee is worthwhile.','''
S~A personal escort to some fossils. I had expected the ancient things to be harder to arrange a meeting with.|
S~I would like to see the collection. We can ask what the admission helps the museum look after.|
S~He wanted us to see something he likes. That is a pleasant reason to show a visitor around.|
S~I like an introduction that ends with time to look for ourselves.|
S~I hope we have enough time to enjoy the visit instead of hurrying past the interesting parts.|
S~The guide has made a very committed recommendation. I am ready to meet his chosen supporting cast of fossils.|
S~I like knowing somebody wanted us to find this place.|
S~I would enjoy seeing how the exhibits are preserved. I will keep my hands safely to myself.|
S~Sharing a place you love is a kind way to welcome someone.|
S~I appreciate being told about the fee before arriving at the desk with empty pockets.|
S~I would like to see which exhibit made him so eager to bring people here.
''')

add('pewter_fossil_enthusiasm','PewterCity_Text_WerentThoseFossilsAmazing',
    'A museum enthusiast asks whether we found the Mt. Moon fossils amazing.','''
S~They are excellent at making a little afternoon feel rather short and recent.|
S~A fossil can preserve evidence of a life nobody living has ever seen. Yes, that is remarkable.|
S~It is worth stopping to think about what those shapes used to belong to.|
S~I like imagining the quiet before anyone put a name beneath the glass.|
S~I am glad people have kept them somewhere we can learn from them.|
S~They have remained compelling for an exceptionally long time without improving their presentation.|
S~I like that something so old can still make a person sound this excited.|
S~I have questions about the preservation process. Several pages of questions, unfortunately.|
S~A small piece of a long-gone life can still change how somebody sees the world.|
S~I like seeing a display someone has cared enough to make clear and beautiful.|
S~I would try to capture the scale. Tiny details deserve room in the picture too.
''')

add('pewter_gardener_acknowledged','PewterCity_Text_ThatsRightItsHardWork',
    'After we say we understand what he is doing, the gardener emphasizes the effort.','''
S~He sounds pleased we noticed the work. I hope his garden gives him a peaceful afternoon back.|
N~Routine work can disappear from people's notice until it stops being done.|
S~It is good to acknowledge somebody keeping an ordinary place in order.|
N~I wonder whether he likes the quiet part after he has finished.|
S~I hope somebody brings him a drink when he needs a break.|
M~He has accepted our recognition and added a strongly worded footnote about the labor involved.|
S~Sometimes being seen trying is the thing you wanted from a conversation.|
N~I appreciate maintenance. People tend to notice it most enthusiastically after something fails.|
S~A cared-for place usually has somebody's effort behind it.|
S~I hope he knows the garden is appreciated when nobody happens to mention it.|
N~I would like to see the place before and after a season of his work.
''')

add('cerulean_encyclopedia_interest','CeruleanCity_Text_PokemonEncyclopediaAmusing',
    'A resident finds our work on a Pokemon encyclopedia amusing.','''
M~An encyclopedia. A respectable name for a very long walk interrupted by wildlife.|
S~I like recording what we learn. It becomes much more useful when somebody else can understand the notes.|
S~It is a big project. We can be proud of learning one thing properly at a time.|
S~I wonder which entry will end up reminding us most clearly of an ordinary day on the road.|
S~I hope the record includes the little things that help people care for their partners.|
M~Our extensive wandering has acquired an academically impressive description.|
N~I would like to leave some room in the notes for things we do not understand yet.|
S~I support useful documentation. This is me attempting to learn from several personal disasters.|
S~Paying attention can become something other people get to share.|
S~I would enjoy making the pages clear enough that the interesting parts are easy to find.|
S~I would like the pictures to show something the written entry cannot quite explain.
''')

add('cerulean_trainer_life','CeruleanCity_Text_TrainerLifeIsToughIsntIt',
    'A fellow trainer remarks on the work involved in collecting and battling.','''
S~He has noticed the part between the heroic poses. It contains a surprising number of chores.|
N~It is demanding work when you take the care as seriously as the results.|
N~We do not have to pretend every day is easy to prove we want to be here.|
N~Some days the journey feels longer than the map suggested. I like that he understands.|
S~I hope he has somebody reminding him to eat and rest when the day gets away from him.|
M~Adventure has an extraordinary amount of uncredited preparation.|
N~It helps when somebody says the hard part out loud without turning it into a competition.|
N~Things going smoothly usually means somebody did the dull preparations properly.|
N~We can love the life and still need a little care ourselves.|
N~I appreciate a conversation that allows us to admit we have sore feet.|
S~I would like to hear which parts still make the effort worthwhile for him.
''')

add('cerulean_red_bike_display','CeruleanCity_Text_WantBrightRedBicycle',
    'A girl wants a bright red bicycle but plans to keep it indoors so it stays clean.','''
M~An indoor bicycle. At least the hills should be manageable.|
S~She can enjoy how it looks. I suspect riding it might give her another reason to like it.|
N~It is hers to enjoy. I hope keeping it perfect does not turn into worrying about it constantly.|
S~I understand liking an object before knowing everything you want to do with it.|
S~I hope she gets some happy days with it, whether they happen indoors or out.|
M~A vehicle cast exclusively as a decorative presence. Bold use of the equipment.|
N~I would want to take it somewhere once the fear of the first scratch wore off.|
U~The moving parts would like a word about their future employment.|
N~Something can be beautiful and still have a life outside the room.|
S~I understand the color choice. I would personally allow the tires a little adventure.|
S~I would like a picture from its first outing, if she ever chooses one.
''')

add('cerulean_slowbro_trainer','CeruleanCity_Text_HardToControlMonsObedience',
    'After Slowbro ignores commands, its trainer says obedience depends on the trainer\'s abilities.','''
M~Slowbro has reviewed the instructions and returned them without comment.|
N~Understanding the partner may help more than issuing the next command more firmly.|
N~He is frustrated. I hope that does not become a reason to stop listening to Slowbro.|
N~They do not seem to be hearing the same rhythm yet.|
N~I would give them a quiet moment together instead of adding another person shouting advice.|
M~The director has discovered that having a line ready does not guarantee a performance.|
N~I hope Slowbro gets a chance to communicate something besides apparent refusal.|
N~He has noticed a problem. Repeating the same approach is unlikely to explain it.|
N~A relationship needs room for something other than instructions.|
N~I hope they find a way to work together without making every attempt a public argument.|
N~I would listen to what he has already tried before deciding what the difficulty is.
''')

add('cerulean_slowbro_blocked_path','CeruleanCity_Text_IfSlowbroWasntThereCouldCutTree',
    'A resident explains that Slowbro blocks access to a tree but another way around exists.','''
M~A Pokemon, a tree, and a possible detour. Navigation has assembled a small committee.|
N~If another route is available, we can check it before making either Slowbro or the tree the problem.|
N~We can go around without treating a resting Pokemon like an obstacle that owes us an apology.|
S~A slightly longer walk sounds nicer than beginning an argument with the scenery.|
S~I am happy to take the detour if everyone gets to stay comfortable.|
M~The shortest route has two very quiet objections standing on it.|
N~I like that he mentioned a way around before we started inventing dramatic solutions.|
N~I would check the alternative first. A route can be inconvenient without needing reconstruction.|
S~Passing through should not always mean making everything else move.|
N~A few more steps are cheaper than a thoroughly unnecessary scene.|
N~I would like to know where the other route begins. That is the useful part for us now.
''')

add('cerulean_tree_detour','CeruleanCity_Text_YouCanCutDownSmallTrees',
    'A resident explains Cut but also points out a way around the small tree.','''
M~We can cut it, or we can walk around. I appreciate the tree receiving a place on the options list.|
N~A technique being available does not mean it is the best answer to every small inconvenience.|
N~If the way around is easy, I would try that before making work for the team.|
S~I would like to see what is along the other path anyway.|
S~We can take a few extra steps. It might give everybody a pleasant little break.|
M~The dramatic application of a technique has been challenged by an ordinary detour.|
N~I like knowing we have another choice before doing something we cannot take back.|
N~I would compare the effort involved before treating every tree as an engineering assignment.|
S~We can find our way through a place without always changing its shape.|
N~I am quite willing to sacrifice the perfectly straight route to a nicer walk.|
S~The route around might show us something the shortcut would have hidden.
''')

add('cerulean_robbery_police','CeruleanCity_Text_PeopleHereWereRobbed',
    'A police officer describes a Rocket burglary and the difficulty of dealing with the gang.','''
N~The people inside have already had a terrible day. I hope the attention stays on helping them recover.|
N~We should separate what the officer knows from what still needs investigating. The victims deserve a careful account.|
N~They need their home to feel safe again. That matters beyond catching the person responsible.|
D~It is hard to imagine a familiar room after someone has made it feel like that.|
N~I hope somebody has asked what the residents need right now.|
N~A burglary leaves more behind than a scene for other people to examine.|
D~I hope the people living here have somewhere they can sit without having to answer questions for a while.|
N~There will be damage to put right. I would like the practical help to arrive as promptly as the speculation.|
N~A person's home should belong to them again after the investigation, not to everyone else's curiosity.|
N~I hope they are given privacy as well as sympathy.|
N~I would ask permission before documenting anything here. It is still somebody's home.
''')

add('cerulean_cave_requirements','CeruleanCity_Text_ThisIsCeruleanCave',
    'The cave guard explains that exceptionally strong Pokemon require a highly accomplished trainer.','''
N~The cave has a rather demanding admissions policy. I would prefer to arrive qualified rather than test how literal the warning is.|
N~A place with unusually strong Pokemon deserves preparation, even from someone with an impressive record.|
N~We should go when our team is ready, not simply when a guard stops objecting.|
N~I would like to know the way back as carefully as the way in.|
N~Nobody should have to carry us into a dangerous place just because we are eager to see it.|
N~The entrance has given us unusually clear notice that the next scene may be difficult.|
N~I do not think the warning becomes less serious because we are curious.|
N~I would prepare supplies and a route before presenting our qualifications to the cave itself.|
N~Being allowed somewhere is not quite the same thing as being ready to care for one another there.|
N~I would rather leave an impressive cave for another day than make the team pay for our impatience.|
N~There will be plenty to notice when we are prepared enough to look without panicking.
''')

add('vermilion_foundation_builder','VermilionCity_Text_BuildingOnThisLand',
    'A landowner describes plans for a building while his Pokemon levels the ground.','''
M~He owns the plot. The Pokemon appears to own most of the current workload.|
N~A good foundation matters. I hope the Pokemon doing the work gets appropriate breaks and care.|
N~I would like to hear as much about the worker's needs as the owner's plans.|
N~I wonder what he imagines here once the sound of tamping finally stops.|
N~I hope there is a meal and a proper rest planned for the Pokemon as well as a building.|
M~The owner has announced his future masterpiece. The supporting performer is currently doing the groundwork.|
N~I hope he thanks the Pokemon as confidently as he describes owning the land.|
N~I would enjoy hearing about the foundation design. I would also like to see a reasonable work schedule.|
N~Making a place should involve caring for the one helping you make it.|
N~I hope the finished building leaves some evidence of the work the Pokemon put into it.|
N~I would begin the record before the building exists. The worker belongs in the history too.
''')

add('vermilion_machop_work','VermilionCity_Text_MachopStompingLandFlat',
    'Machop is flattening the ground for the future building.','''
S~That is a very determined method of persuading a piece of ground to be flatter.|
N~Machop is doing useful physical work. We should avoid getting in its way or treating it like a demonstration.|
N~I hope it gets regular breaks. Working hard does not mean being ready to work forever.|
N~That steady rhythm must become part of the street after you hear it long enough.|
N~I hope somebody has water ready when it stops.|
S~An impressive performance of a practical task. It deserves more than being called part of the equipment.|
N~I hope it likes some part of the job, rather than only being very good at it.|
N~I would ask how it signals that it needs a break before adding any more work.|
N~A helpful Pokemon is still someone whose comfort matters.|
N~I would like the finished place to remember its first hard worker.|
N~I would ask before taking a picture while it works. A pause might be more welcome than an audience.
''')

add('vermilion_annual_cruise','VermilionCity_Text_SSAnneVisitsOnceAYear',
    'A resident says the luxury S.S. Anne visits Vermilion once each year.','''
S~One visit a year. I hope the ship makes an effort to remember everybody's birthday while it is here.|
N~An annual visit must become part of how people here mark the seasons.|
S~I wonder who waits for it because someone they know might step off.|
S~A ship returning to a familiar harbor has the beginning of a good song in it.|
S~I would like to know what special food appears in town when the passengers arrive.|
S~A yearly entrance with considerable anticipation. The ship has excellent timing for a recurring role.|
S~I like the idea of a familiar arrival that still gives people something to look forward to.|
S~I would love a look at the maintenance work between those glamorous visits.|
S~A place can have a relationship with something that only stays briefly.|
S~I hope the people who work aboard get to enjoy the visit as well as arrange it for everyone else.|
S~I would like pictures of the harbor before and after it arrives.
''')

add('vermilion_oaks_aide_directions','VermilionCity_Text_Route2AideHasPackageForYou',
    'Oak\'s aide directs us to another aide carrying a package near Route 2.','''
M~The aides have organized a small relay of people telling us where the package is.|
N~Route 2 gives us a useful place to look. We should introduce ourselves before assuming every aide is expecting us.|
N~We know where to ask now. There is no need to rush the person making the delivery.|
S~I like knowing somebody remembered to help us find what was meant for us.|
S~I hope the other aide has not spent the whole day looking up the wrong road.|
M~A package with a supporting cast and a short geographical subplot.|
N~I hope we manage to find one another before everyone has to make another trip.|
N~A clear destination would have improved the delivery plan, but this is a useful update.|
S~Somebody is making sure a kind intention reaches the person it was meant for.|
N~I would like the next conversation to include the actual package.|
N~I will remember Route 2. It is the part of the message that will help us find him.
''')

add('lavender_tower_memorials','LavenderTown_Text_TownKnownAsMonGraveSite',
    'A resident explains that memorial services for Pokemon are held in the tower.','''
N~We should take our time and be considerate here. People have come with someone on their minds.|
N~A place for remembrance gives grief somewhere it can be acknowledged without explanation.|
N~We can be quiet without making a show of it. This is somebody else's difficult day.|
D~I hope the people coming here have someone to sit beside them afterward.|
N~I would like to know whether anyone needs help with the little things that are difficult while grieving.|
N~Some places do not need us to supply anything impressive to say.|
D~Remembering can be painful and still be something you want to do.|
N~I will keep my tools and questions quiet unless somebody asks for help.|
N~The love does not end because the life did. It makes sense to have a place for it.|
N~We should let people choose whether they want company or privacy.|
N~I would keep the camera away unless somebody specifically wanted a memory recorded.
''')

add('lavender_rocket_ghost_rumor','LavenderTown_Text_GhostsAppearedInTower',
    'A resident suspects the tower ghosts are Pokemon killed by Rocket.','''
D~That is an awful thing to imagine. I would like us to find out what happened without treating it as entertainment.|
N~It is a serious account. We should be careful about what is known, what is feared, and who needs help.|
A~If Rocket hurt Pokemon here, the people grieving deserve more than a rumor passed around the street.|
D~I wish the story began with someone being kind to the Pokemon before any of this happened.|
D~I hope there is someone helping the Pokemon and the people left hurting.|
N~A frightening story can still concern real grief. It should be handled with care.|
D~I do not want someone else's loss turned into a reason for visitors to be excited.|
A~I would rather work out what can be put right than collect a more dramatic version of the story.|
D~If something here cannot rest, I hope somebody will listen to what it needs.|
D~I hope the people affected get to speak for themselves.|
N~I would ask gently and avoid recording anything somebody does not want to revisit.
''')

add('lavender_ghost_believer_answer','LavenderTown_Text_SoThereAreBelievers',
    'After we affirm belief in ghosts, the girl acknowledges that there are other believers.','''
N~She sounds glad not to be the only person saying it. We can listen without making the conversation a contest.|
N~I am interested in what she experienced. Agreeing to listen is a useful beginning.|
N~She does not have to convince an entire street before somebody treats her kindly.|
N~It can be a relief to hear someone answer without laughing first.|
N~I hope talking about it helps her feel less alone with whatever worried her.|
N~She has found an audience willing to hear the account. We should let it remain her account.|
N~I know the relief of discovering you do not have to explain yourself quite so hard.|
N~I would ask what she noticed before asking for conclusions.|
N~There are ways to make room for someone's experience without demanding that it become a performance.|
N~I hope she feels comfortable enough to say what she means at her own pace.|
N~I would rather hear her actual memory than prompt her into the story I expected.
''')

add('fuchsia_safari_recommendation','FuchsiaCity_Text_DidYouTrySafariGame',
    'A resident recommends the Safari Game for its unusual Pokemon.','''
S~New Pokemon and a place to wander. I hope the excitement leaves enough attention for the way back.|
S~I would enjoy observing species we have not encountered yet. Their habits interest me as much as their rarity.|
N~We should learn the rules before going in, and be considerate of the Pokemon living there.|
S~I would like to see which sounds become familiar before we find the Pokemon making them.|
S~I hope the visit gives us time to notice how the Pokemon are doing, too.|
M~An excursion promising unusual encounters. I shall try not to treat the ordinary ones as disappointing extras.|
S~I would like a quiet moment to look before everybody starts deciding what to catch.|
N~I would check the equipment and rules first. Excitement is a poor substitute for either.|
N~Being rare does not mean a Pokemon owes a visitor a meeting.|
S~I would enjoy seeing something unfamiliar without immediately trying to make it part of our luggage.|
S~I would love to go looking, provided we let the wildlife choose how close to come.
''')

add('fuchsia_ball_is_pokemon','FuchsiaCity_Text_ItemBallInThere',
    'A visitor discovers the apparent item ball in the exhibit is actually a Pokemon.','''
U~The tempting item has developed a private life. We should probably stop planning to pocket it.|
N~It is a useful reminder to identify what we are looking at before deciding what we want from it.|
N~Good thing we stopped to look. The Pokemon deserves better than an argument over who found it first.|
S~It has completely changed the conversation without doing anything at all.|
S~I hope it is comfortable while people keep mistaking it for something to collect.|
M~An excellent reveal from a performer who has remained impressively still.|
N~I would prefer to be recognized as a person before somebody decided I was a prize.|
U~That is a fairly consequential identification error. I am glad the correction arrived early.|
N~Noticing that it is alive should change how we approach it.|
M~I admire a Pokemon that can make an entrance by simply continuing to be where it already was.|
N~I would spend a little longer looking now. The interesting part was there before we understood it.
''')

add('fuchsia_poison_leaders_daughter','FuchsiaCity_Text_MyFatherIsGymLeader',
    'The Gym Leader\'s daughter is training to match her father\'s skill with Poison Pokemon.','''
S~She has a very specific family tradition to live up to. I hope the household labels its lunch containers carefully.|
N~Learning from her father gives her a starting point. Her own methods will be interesting to see.|
N~I hope people notice the work she does, instead of only comparing her with him.|
N~She sounds determined. I wonder what part of his teaching she will eventually make her own.|
S~I hope they get time to enjoy being family as well as being teacher and student.|
S~A successor preparing her own entrance. I would like her to get a little room to surprise the audience.|
N~It can be hard to know where admiration ends and expectations begin. I hope she gets to choose.|
N~I would like to hear how they train safely with those partners. That is part of the skill too.|
N~She can learn from someone she loves without becoming the same person.|
S~I hope she keeps a sense of her own style while learning what she admires in his.|
N~I would like to record her progress before everybody starts treating the outcome as inevitable.
''')

add('fuchsia_safari_two_areas','FuchsiaCity_Text_SafariZoneZooInFront',
    'A resident distinguishes the entrance displays from the Safari Game beyond them.','''
S~A place to look first and a place to explore afterward. I appreciate directions in the order my feet need them.|
N~We should understand the different rules for the displays and the area beyond them.|
N~We can enjoy meeting the Pokemon here without treating them like the ones we might catch farther in.|
S~I would like a slow look around before choosing whether to spend the rest of the day exploring.|
S~I hope both areas have people paying close attention to the Pokemon's comfort.|
M~The introduction and the expedition have helpfully been given separate entrances.|
N~It is nice to know we can simply look around without committing to the whole excursion.|
N~I would ask about the facilities before going beyond the entrance. Useful directions are a good start.|
N~Different ways of sharing a place with Pokemon come with different responsibilities.|
S~I appreciate knowing what sort of visit we are choosing before I have dressed for the wrong one.|
N~I would like to see how people behave around the displays before deciding how to approach the wider area.
''')

add('fuchsia_erik_waiting_sara','FuchsiaCity_Text_WheresSara',
    'Erik is waiting for Sara at the place they agreed to meet.','''
N~The meeting place has been successfully found by half the meeting. I hope the other half arrives soon.|
N~I would check exactly where they agreed to meet before assuming something has gone wrong.|
N~He sounds worried. We should avoid supplying reasons to worry that he has not actually been given.|
N~Waiting makes every approaching footstep seem briefly important.|
S~I hope Sara gets here soon and they can enjoy the visit they planned.|
M~One character has arrived precisely on cue. The scene is waiting patiently for its second line.|
N~I dislike how quickly waiting can turn into guessing what somebody is thinking.|
N~This sounds like a job for confirming the meeting point before devising a complicated search.|
N~We can offer a little calm without pretending to know why she is late.|
S~I hope they both recognize the exact same here when they describe where they meant to meet.|
N~I would ask whether there is another entrance. It is a practical question before a dramatic conclusion.
''')

add('cinnabar_mansion_experiments','CinnabarIsland_Text_ScientistsExperimentInMansion',
    'A resident says scientists experiment in the burned-out Pokemon Mansion.','''
U~A burned-out building is a bold place to continue announcing experiments. I hope the next word is safely.|
N~I would like to know what the work involves and whether the building is fit for it.|
N~People doing research still deserve a safe place to do it.|
N~A place can look abandoned and still contain someone's working day. I hope they are looking after themselves.|
N~I hope the Pokemon there are receiving more care than the building appears to have had.|
N~The setting has already supplied a rather strong warning. I would pay attention to it.|
N~I would like to know what we are walking into before the door closes behind us.|
U~I have worked in questionable rooms. The word burned-out would give me pause.|
N~Knowing a place has been damaged should make us more careful about the lives still inside it.|
N~I would prefer a clearer account of the safety arrangements before admiring the commitment to research.|
N~I would ask permission before approaching anyone's work, and find out which parts are safe to visit.
''')

add('cinnabar_blaine_long_residence','CinnabarIsland_Text_BlaineLivedHereSinceBeforeLab',
    'A resident calls Blaine unusual and says he lived on Cinnabar before the laboratory existed.','''
S~Blaine has been here long enough to have opinions about the island before it acquired laboratory paperwork.|
N~He may remember changes that the newer institutions take for granted. I would enjoy hearing that account.|
N~I would rather meet him than decide what being unusual is supposed to mean.|
N~I wonder which version of the island he thinks of first when he says home.|
S~I hope there are still familiar things he enjoys here after so much has changed.|
S~A long-running local character with an island's worth of backstory. I would let him choose where to begin.|
N~Sometimes people mean unfamiliar to me when they say someone is odd.|
N~I would like to ask what changed when the lab was built. Long-term residents notice practical details.|
N~A person can carry a history of a place that its newest buildings do not show.|
N~He deserves an introduction larger than the local verdict on his personality.|
N~I would like to see any old photographs he wanted to share. His account could give them a different meaning.
''')
