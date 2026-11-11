"""Final registered Kanto actor speech found by the remaining-label audit."""
ROWS=[]
EMOTIONS=dict(N='neutral',S='soft_smile',A='annoyed',F='flustered',D='sad',U='surprised',M='smug',L='laughing')
def add(key,labels,subject,lines):
    replies=[]
    for line in lines.strip().split('|'):
        line=line.strip()
        if len(line)>1 and line[1]=='~' and line[0] in EMOTIONS:line=EMOTIONS[line[0]]+line[1:]
        replies.append(line)
    assert len(replies)==11,(key,len(replies))
    ROWS.append(dict(key='kanto_audit_'+key,labels=labels.split(),subject=subject,replies=replies))

add('forest_anthony','ViridianForest_Text_AnthonyPostBattle',
    "Anthony regrets losing some of his allowance in the battle.",'''
N~That was snack money before it became battle money. I can see why he looks glum.|
N~A limited allowance makes even a modest loss feel significant.|
N~He should keep enough for what he needs before risking another match.|
N~It sounds worse when you have to wait for the next allowance.|
N~A little budgeting could leave him with lunch even after a rough battle.|
N~The adventure has encountered its first stern financial review.|
N~A small loss can cast an impressively large shadow over a child's afternoon.|
N~Worth keeping essential supplies separate from money he can afford to lose.|
N~The pocket feels lighter long before the disappointment does.|
N~No need to make him feel small about an amount that matters to him.|
N~He will probably remember this battle every time he passes a shop today.
''')
add('forest_balls','ViridianForest_Text_RanOutOfPokeBalls',
    "A forest visitor ran out of Poke Balls while catching Pokemon.",'''
S~The enthusiasm lasted longer than the supplies. A very familiar sort of expedition.|
N~A reserve is useful, though more supplies still need to fit a sensible budget.|
N~Check the bag before heading farther into the forest.|
S~Finding another Pokemon just after running out must feel particularly unfair.|
N~A supply check is less exciting than a catch, but earns its place in the morning.|
S~The hunt has reached an intermission sponsored by an empty pocket.|
S~Ambition is remarkably good at forgetting to count its equipment.|
S~A short checklist would prevent a very predictable interruption next time.|
N~An empty pouch has a way of making every rustle more interesting.|
S~He has converted an inconvenient afternoon into advice for strangers.|
S~I wonder which encounter made him realize he had used the last one.
''')
add('forest_charlie','ViridianForest_Text_CharliePostBattle',
    "Charlie enjoys how quickly Bug Pokemon evolve.",'''
S~A bug team does not make you wait long for the next surprise.|
S~Rapid development makes changes easy to observe over a relatively short period.|
S~He likes watching them grow. Good reason to keep paying attention.|
S~It is lovely when caring for a team brings changes you can actually notice.|
S~You could look away for a snack and come back to a different little face.|
S~His favourite cast is admirably efficient about entering its next act.|
S~A small creature can be very dramatic about changing its shape.|
S~That quick turnaround gives him plenty of chances to compare each stage.|
S~Tiny lives can carry a surprising number of transformations.|
S~He sounds delighted by the team he already has. That is appealing.|
S~I wonder which evolution first made him fall in love with Bug Pokemon.
''')
add('forest_doug','ViridianForest_Text_DougPostBattle',
    "Doug reacts to losing by planning to catch stronger Pokemon.",'''
N~A stronger bug might help, but the plan still needs somebody thinking at the other end.|
N~Changing the team is one option. Reviewing the decisions would provide useful evidence first.|
N~His current team deserves a chance to improve, too.|
N~I hope the Pokemon do not mistake his frustration for how he feels about them.|
N~Replacing ingredients does not fix a pan nobody is watching.|
N~The dissatisfied director has immediately proposed replacing the cast.|
N~A new Pokemon is a rather unfair place to put all his hopes of never losing.|
N~Find the actual weak point before replacing parts at random.|
N~Stronger companions will still need a patient hand guiding them.|
N~An upgrade is not much use if he brings the same careless attitude along.|
N~I would like to know what he thinks stronger means after that match.
''')
add('forest_rick','ViridianForest_Text_RickPostBattle',
    "Rick asks for quiet so the forest bugs are not frightened away.",'''
S~Right. Tiny bug audience, tiny bug volume. I can work with that.|
S~Reducing sudden noise should make observing nearby Pokemon easier.|
N~Keep it quiet. We are in their space.|
S~I like the forest better when we can hear the small sounds underneath us.|
S~A quiet pause seems fair after all that battling.|
S~The resident audience has requested a less thunderous performance.|
S~Silence is a very reasonable thing to bring into the woods.|
N~Let's stop moving for a moment and see what comes back out.|
S~The small hidden things need room to decide we are harmless.|
S~An excellent reminder that being present does not require being conspicuous.|
S~We might notice far more if we wait instead of announce ourselves.
''')
add('forest_sammy','ViridianForest_Text_SammyPostBattle',
    "Sammy is looking for things he dropped and asks for help finding them.",'''
S~The forest floor has temporarily become his very inconvenient storage system.|
N~Retracing his route would narrow the search more effectively than searching everywhere at once.|
N~Watch our footing. We can look without trampling the smaller clues.|
S~Losing something in all these leaves must feel discouraging.|
N~Start where he last remembers having it, then work back slowly.|
S~The treasure hunt has the useful complication that the treasure already has an owner.|
N~Leaves are extremely committed to concealing other people's belongings.|
S~Divide the ground into small patches so we do not keep checking the same place.|
N~The woods keep what falls until somebody notices the absence.|
N~Finding it should come before lecturing him about secure pockets.|
S~I wonder whether the colour would stand out better from another angle.
''')
add('forest_friends','ViridianForest_Text_FriendsItchingToBattle',
    "A visitor says the friends who came to catch bugs are eager to battle.",'''
S~A bug-catching outing has turned into a whole committee of challenges.|
S~A shared interest has given the group several ways to enjoy the forest together.|
N~Good to know what the group is here for. Keep the team ready.|
S~It sounds like the sort of trip they will talk about together afterward.|
S~Catching, battling, then comparing stories. Quite a full afternoon.|
S~The woodland excursion has developed a distinctly competitive second half.|
S~A group of eager bug enthusiasts is a surprisingly lively thing to encounter.|
S~Friends can make testing a new team feel like part of the outing.|
S~The forest has become the meeting place for several small ambitions.|
S~I like a group that arrives excited about the place instead of bored by it.|
S~I wonder whether they all came for the same kind of Bug Pokemon.
''')
add('route3_tired','Route3_Text_TunnelFromCeruleanTiring',
    "A traveller needs a rest after the tunnel journey from Cerulean.",'''
N~That tunnel seems to have taken the spring right out of his walking.|
N~Fatigue after a long passage is a useful signal to pause before continuing.|
N~Rest here. No prize for stumbling through the next stretch exhausted.|
N~He sounds tired enough that a quiet place to sit would mean a lot.|
N~A drink and a proper stop are worth making time for.|
N~The journey has earned an intermission without needing a dramatic incident.|
N~An ordinary rock can become excellent furniture after a long walk.|
N~We should account for the return journey when planning our own energy.|
N~Even a familiar road grows long under tired feet.|
N~There is no need to make resting look more dignified than it is.|
N~I wonder how long he has been telling himself the next stop is close enough.
''')
add('route4_brock','Route4_Text_PeopleLikeAndRespectBrock',
    "A young admirer recognizes the Boulder Badge and wants to become a respected Gym Leader like Brock.",'''
S~Being tough got his attention. Being liked and respected seems to have kept it.|
S~His ambition includes the social responsibilities of leadership, not only strength.|
S~A good example can give a kid something solid to aim for.|
S~I like that he notices how people feel around Brock.|
S~Being someone a town can rely on is a worthwhile part of the dream.|
S~The badge has prompted an aspiring leader to describe his ideal character.|
S~It is pleasant when admiration reaches beyond who can win a fight.|
S~A leader has to keep more than a strong team working well.|
S~Some ambitions begin with noticing the kindness around someone else's strength.|
S~Respect has made a stronger impression on him than a title alone could.|
S~I wonder which little thing Brock did that made him seem worth following.
''')
add('route4_geodude','Route4_Text_TrippedOverGeodude',
    "A traveller has tripped over a Geodude.",'''
U~A rock that can object to being tripped over adds a whole new difficulty to walking.|
N~Camouflage can make a Pokemon difficult to distinguish from the terrain.|
N~Check the injury, then watch the ground before stepping again.|
N~I hope both the traveller and the startled Geodude are all right.|
N~A short pause to check the ankle beats limping all afternoon.|
N~The scenery has objected to being treated as ordinary scenery.|
N~The ground is already difficult enough without having opinions.|
N~Uneven footing is a good reason to slow down and actually scan the path.|
N~Sometimes the stone underfoot is having its own inconvenient day.|
N~A painful reminder that not every obstacle is trying to be an obstacle.|
N~I wonder how many people have mistaken that same Geodude for part of the path.
''')
add('six_balls','Route4_PokemonCenter_1F_Text_CanHaveSixMonsWithYou',
    "A trainer checks the six Poke Balls on their belt.",'''
S~A belt check is the quiet little cousin of a heroic departure.|
N~Checking the team before travelling is a sensible habit.|
N~Know who is with you before heading back onto the road.|
S~There is something reassuring about making sure everyone is accounted for.|
S~A quick check saves reaching for something that is not there later.|
S~The adventurer is completing the essential business of counting the cast.|
S~Small routines do a lot of work keeping a journey from coming apart.|
S~An equipment check is useful precisely because it is so easy to skip.|
S~Six small circles can carry a very busy day.|
S~Practical checks are hardly glamorous, but I appreciate someone doing them.|
S~It makes me wonder what sort of team those six Balls belong to.
''')
add('storage_advice','Route4_PokemonCenter_1F_Text_ShouldStoreMonsUsingPC',
    "A trainer recommends PC storage when there is no room for more Pokemon.",'''
N~A good reminder to make room before enthusiasm brings home another companion.|
N~Planning team capacity ahead avoids an unnecessary interruption while travelling.|
N~Sort the team where there is time to think.|
S~It can be hard to decide who comes along when everyone matters.|
N~A little preparation at the Center makes the next leg simpler.|
N~The expanding cast requires a more deliberate travelling arrangement.|
N~Even a fond collection eventually demands practical decisions.|
N~Choose the team for the trip rather than wait for the capacity problem to choose for us.|
N~Not every companion needs to take every road at the same time.|
N~A useful piece of advice, offered without turning it into a lecture.|
S~I wonder how often travellers only notice the full team at the next encounter.
''')
add('tower_stairs','TrainerTower_Lobby_Text_StairsTougherThanAnyBattle',
    "A Tower visitor is exhausted by the stairs rather than the battles.",'''
L~The stairs have an undefeated record and refuse to shake hands afterward.|
S~Repeated climbing can be substantial exertion even without a single battle.|
N~Catch a breath. The stairs are not going anywhere.|
S~I feel a little less embarrassed about wanting to pause now.|
S~The climb has definitely earned him somewhere comfortable to sit.|
S~A formidable opponent with neither dialogue nor a weakness chart.|
S~Architecture can be extraordinarily rude to a pair of tired legs.|
S~A practical reminder that access routes are part of a building's real difficulty.|
N~The tower asks a price from the body before it asks the team anything.|
S~No shame in losing an argument with several flights of stairs.|
S~I wonder how many challengers arrive ready for everything except the climb.
''')
add('tower_nerves','TrainerTower_Lobby_Text_WonderWhatKindsOfTrainers',
    "A challenger is nervous about the unknown trainers waiting in the Tower.",'''
S~The mystery opponents are currently undefeated at making this person's stomach wobble.|
N~Uncertainty can feel more demanding than a known challenge of the same difficulty.|
N~One battle at a time. No need to fight every possibility in advance.|
S~Wanting to know how good you are can feel frightening right before the answer.|
N~A steady breath and a supply check give the nerves something useful to do.|
S~The unseen cast has created considerable suspense without making an entrance.|
N~Imagination is remarkably energetic when asked to invent possible defeats.|
N~They can prepare the team without needing to predict every opponent.|
S~The closed door has become larger in thought than it is in the wall.|
S~I appreciate someone admitting the nerves instead of trying to look untouchable.|
S~I wonder what sort of challenger they hope to be when the first match begins.
''')
add('daycare_very_well','gDaycareText_GetAlongVeryWell',
    "The Day-Care man reports that the two deposited Pokemon seem to get along very well.",'''
S~Good news from the small social department. They seem happy with the company.|
S~A favourable compatibility report, though it is still a brief observation rather than a whole relationship.|
S~Good that they are settling in together.|
S~That is a comforting thing to hear while they are away from us.|
S~Pleasant company makes a temporary stay feel easier.|
S~The boarding house has delivered an unusually glowing review of its roommates.|
S~A peaceful little arrangement is worth appreciating.|
S~Nice to hear the pairing seems to be working without trouble.|
S~Two familiar presences have found a comfortable rhythm beside each other.|
S~Getting along well is lovely news without needing to embellish it.|
S~I wonder what the man noticed that made him sound so certain.
''')
add('daycare_along','gDaycareText_GetAlong',
    "The Day-Care man reports that the two Pokemon seem to get along.",'''
S~A perfectly respectable roommate report. No tiny arguments noted.|
S~The report suggests reasonable compatibility without claiming anything more specific.|
S~They are doing all right together. Good to know.|
S~A simple bit of reassurance can make leaving them here feel easier.|
S~Sounds like their stay has some comfortable company in it.|
S~A modest review, refreshingly free of invented romantic complications.|
S~Ordinary peace rarely gets enough credit.|
S~A working arrangement does not need dramatic results to count as good news.|
S~Sometimes the kindest report is that two lives fit quietly beside each other.|
S~Comfortable company is worthwhile even without a spectacular friendship story.|
S~I wonder whether they have found something they like doing together.
''')
add('daycare_low','gDaycareText_DontLikeOther',
    "The Day-Care man says the two Pokemon do not seem to like each other much.",'''
N~Not every pair becomes best friends. We do not need to issue matching friendship badges.|
N~This is a compatibility assessment, not evidence by itself of conflict or poor care.|
N~No need to force them to be close. Keep an eye on how they are doing.|
N~It is all right if familiar company takes a while, or never becomes their favourite.|
N~Sharing a place does not oblige anyone to adore the other guest.|
N~The proposed duo has declined to supply an instant friendship subplot.|
N~A lack of fondness need not become a scandal.|
N~We can consider a different pairing instead of insisting the current one should work.|
N~Two lives can share a patch of shade without growing toward each other.|
N~There is no prize for making a reluctant pair look charming.|
N~I would pay attention to their comfort rather than imagine a whole quarrel from one report.
''')
add('daycare_other','gDaycareText_PlayOther',
    "The Day-Care man says the Pokemon prefer playing with other Pokemon instead of each other.",'''
S~They have declined the arranged playdate and selected their own tiny social calendar.|
N~The report describes incompatible pairing preferences. It does not establish that either Pokemon is unhappy.|
N~They can choose different company. That is fine.|
S~Being comfortable with others is still company, even if it is not this particular pair.|
S~No need to make two guests sit together just because they arrived together.|
S~The cast have requested separate scenes and a wider circle of acquaintances.|
S~A polite refusal to become the friendship someone else had planned.|
N~A different pairing may work better than trying to force this one.|
S~They have found other little paths through the same garden.|
S~Choosing their own companions seems fair to me.|
S~I wonder which Pokemon each of them actually enjoys spending time with.
''')
add('oak_grass','PokedexRating_Text_LessThan10',
    "Oak recommends searching more patches of grass to begin filling the Pokedex.",'''
S~The grand scientific plan currently begins with looking carefully in the grass. I can do that.|
S~Sampling more locations should reveal species a narrow search would miss.|
N~Start nearby and pay attention. No need to rush the whole region.|
S~A big task can feel less frightening when the next step is that small.|
S~We can make a day of exploring without expecting to finish everything at once.|
S~The professor has supplied a humble but promising opening chapter.|
S~A great undertaking can begin with being slightly more attentive to weeds.|
S~Let's compare different patches rather than repeatedly searching the same corner.|
S~The grass has been living its own busy story beside our feet.|
S~It is practical advice. No grand pose required to begin.|
S~I wonder what we have already walked past without noticing.
''')
add('oak_flash','PokedexRating_Text_LessThan20',
    "Oak praises early progress and recommends collecting Flash from his aide.",'''
S~Encouragement and a reminder to collect something useful. A nicely practical compliment.|
S~The advice connects research progress with equipment that supports further exploration.|
N~Worth checking with his aide before heading somewhere dark.|
S~It feels good that he notices the beginning instead of only the distance left.|
S~A useful errand to fit into the next stretch of travel.|
S~The professor has paired his favourable review with a rather illuminating recommendation.|
S~A small beginning has earned more than a distracted nod.|
S~Better equipment can make careful exploration much easier.|
S~A little knowledge has opened the possibility of carrying more light.|
S~He remembers the practical help instead of leaving us with praise alone.|
S~I like hearing him sound pleased before the collection is anywhere near finished.
''')
add('oak_volume','PokedexRating_Text_LessThan30',
    "Oak recommends adding a greater variety of species to the Pokedex.",'''
N~The book wants more different neighbours, rather than a long queue of the same little face.|
S~Increasing species variety addresses the particular gap he has identified.|
N~Try a different habitat instead of repeating the same route.|
N~It helps to have a clearer aim than simply doing more.|
S~A change of scenery could make the next bit of work enjoyable, too.|
S~The editor requests a broader cast rather than additional appearances by old favourites.|
S~Variety is a kinder assignment than endless repetition.|
S~Let's look for habitats we have not sampled much yet.|
N~The map has more voices than the ones nearest the road.|
N~A fuller collection should show the place's variety, not just our habits.|
S~I wonder which kind of habitat has been missing from our travels.
''')
add('oak_itemfinder','PokedexRating_Text_LessThan40',
    "Oak recognizes the effort and reminds the player to collect an Itemfinder from his aide.",'''
S~He has noticed our hard work and knows a device that may notice the things we miss.|
S~An Itemfinder would add another means of observing otherwise overlooked surroundings.|
N~Useful reminder. We should speak to the aide when we are nearby.|
S~It means something that he notices the effort behind the pages.|
S~A practical tool makes a good follow-up to kind words.|
S~A favourable review comes with a recommendation for finding the less obvious props.|
S~Apparently curiosity may now receive technical assistance.|
S~A detector could help us examine places our eyes have already dismissed.|
S~The overlooked things may soon become a little harder to overlook.|
S~He makes progress feel worth noticing without pretending the work is finished.|
S~I wonder how many useful little details are lying just outside our attention.
''')
add('oak_coin','PokedexRating_Text_LessThan50',
    "Oak praises the collection and recommends getting the Amulet Coin from his aide.",'''
S~A little praise and a reminder about an amulet. Our errands are getting surprisingly shiny.|
S~He offers a practical reward alongside the assessment rather than only a ranking.|
N~We can check with the aide. No need to turn the whole trip toward money.|
S~His approval feels warmer when he remembers something that might help the journey.|
S~A bit of financial breathing room can make practical travel choices easier.|
S~The professor's encouraging review includes a potentially lucrative footnote.|
S~Research apparently has the occasional less threadbare fringe benefit.|
N~Worth collecting the useful tool before making assumptions about what it will solve.|
S~An ordinary errand has acquired a small promise of good fortune.|
S~He seems genuinely pleased to help the next part go more smoothly.|
S~I like that the reminder is specific enough to act on.
''')
add('oak_fifty','PokedexRating_Text_LessThan60',
    "Oak celebrates passing fifty species and recommends collecting Exp Share from an aide.",'''
U~Fifty species! That is a lot of different ways for the grass to surprise us.|
S~A substantial sample, and the suggested aid could support development across the team.|
S~Solid progress. We should check with his aide when it suits the route.|
S~Fifty feels much more real when somebody says it aloud like that.|
S~That is a milestone worth a proper sit-down and something nice to eat.|
S~The research has reached fifty entries and earned an enthusiastic editorial note.|
S~A number has become large enough to sound like the days we spent earning it.|
S~A useful tool and a measurable milestone. A satisfying report.|
S~Fifty little records carry a great many roads behind them.|
S~The work shows, even if each day only added a little.|
S~I wonder which of those encounters we will remember most clearly years from now.
''')
add('oak_respectable','PokedexRating_Text_LessThan70',
    "Oak calls the growing Pokedex quite respectable.",'''
S~Respectable! Our wandering has officially become a respectable activity.|
S~The assessment recognizes sustained progress rather than a single unusual find.|
S~Good work, steadily done. Worth being pleased with.|
S~A calm bit of praise can stay with me longer than a big fuss.|
S~It is good to stop and appreciate what all those days have added up to.|
S~The collection has received the professor's considered seal of approval.|
S~Respectable is a pleasantly solid word for a heap of small discoveries.|
S~A growing record shows what consistent attention can accomplish.|
S~A little work repeated has made a shape large enough for someone else to see.|
S~He sounds satisfied with the care that has gone into it.|
S~I wonder whether he remembers how his own first collection began.
''')
add('oak_fishing','PokedexRating_Text_LessThan80',
    "Oak recommends fishing to discover more Pokemon.",'''
S~The next research method involves standing by water and trying to look patient.|
S~Fishing samples a habitat that walking through grass cannot adequately represent.|
N~Check the rod and find safe footing before casting.|
S~A quieter kind of searching might make a nice change.|
S~Time beside the water can be enjoyable even before anything bites.|
S~The professor has prescribed a slower-paced chapter with an unpredictable supporting cast.|
S~A perfectly respectable reason to stare into water for a while.|
S~Different water and different locations could produce useful comparisons.|
S~The surface is only the lid on another crowded little world.|
S~It is a good reminder that our usual route does not show us everything.|
S~I wonder what lives beneath places we have only looked across.
''')
add('oak_collector','PokedexRating_Text_LessThan90',
    "Oak guesses that the player enjoys collecting things.",'''
S~The large collection may have given our collecting habit away. Subtle detective work, Professor.|
S~Repeated choices can reveal a preference, though curiosity may matter as much as collecting.|
S~We have certainly put the work in.|
S~It is a little funny to be recognized through all the things we stopped to notice.|
S~There is pleasure in seeing the small efforts gathered together.|
S~The evidence has led the professor to a charmingly obvious character assessment.|
S~A fond accusation, supported by quite a substantial pile of evidence.|
S~Collecting gets especially interesting when the entries start revealing patterns.|
S~Gather enough little wonders and people begin to recognize the habit.|
S~He makes the observation sound affectionate rather than possessive.|
S~I wonder whether he recognizes a younger version of himself in that habit.
''')
add('oak_difficulty','PokedexRating_Text_LessThan100',
    "Oak admires the difficult work behind the Pokedex collection.",'''
S~He can see the long walks hiding between the neat little entries.|
S~The record represents substantial effort that the finished list does not directly display.|
S~It took work. Nice to have that recognized.|
S~I like that he notices it was not always easy.|
S~A good result has a lot of ordinary tiring days tucked behind it.|
S~The reviewer has remembered that the polished volume required an expedition.|
S~Some praise feels better because it includes the difficult part.|
S~A tidy record hides plenty of failed approaches and useful revisions.|
S~The finished pages have not forgotten the miles, even when they look quiet.|
S~He appreciates the effort without demanding we make it look effortless.|
S~I wonder which part of the journey he imagines when he says that.
''')
add('oak_hundred','PokedexRating_Text_LessThan110',
    "Oak enthusiastically celebrates reaching one hundred species.",'''
U~One hundred! That number has enough legs to march right out of the notebook.|
S~A hundred species is a substantial body of observation, gathered encounter by encounter.|
S~A hundred. We earned a moment to enjoy that.|
F~It is hard not to smile when he sounds that pleased.|
S~That deserves something better than eating while walking to the next task.|
S~The hundredth entry has secured a wonderfully enthusiastic review.|
S~A large round number has arrived carrying a surprisingly warm feeling.|
S~A hundred entries give us plenty of interesting details to compare.|
S~A hundred small doors opened, each onto a life that was already there.|
S~He sounds delighted enough for the celebration to feel shared.|
S~I wonder how different the first entry looks to us after all these others.
''')
add('oak_evolved','PokedexRating_Text_LessThan120',
    "Oak admires the inclusion of evolved Pokemon in the collection.",'''
S~The book has room for the little faces and the faces they grew into.|
S~Recording multiple developmental stages adds important information beyond species variety alone.|
S~Good to see growth getting its share of the attention.|
S~There is something lovely about recognizing a familiar Pokemon in a changed shape.|
S~Time and care can leave their own kind of record in those pages.|
S~The professor appreciates that the story includes more than the opening appearance.|
S~Change is easier to understand when somebody bothered to notice both sides of it.|
S~Comparing stages can show which traits persist and which change dramatically.|
S~A growing creature carries its earlier shape somewhere inside the new one.|
S~I like that the collection notices development instead of only novelty.|
S~I wonder which transformation surprised us most when we first saw it.
''')
add('oak_trading','PokedexRating_Text_LessThan130',
    "Oak recommends trading with friends to expand the Pokedex.",'''
S~Apparently the next missing entry might begin with saying hello to somebody.|
S~Trading can connect records and opportunities that separate journeys would not provide.|
N~Make any trade carefully. Both sides should understand what they are agreeing to.|
S~It is nice when a big task gives people a reason to meet.|
S~Friends can help each other without turning every meeting into an errand.|
S~The solo research project has been advised to invite a few collaborators.|
S~A collection can become more interesting when it acquires other people's stories.|
S~Comparing what we have found could reveal useful gaps before arranging a trade.|
S~Two roads can lend each other something neither found alone.|
N~A fair exchange should feel good to everyone when the conversation ends.|
S~I wonder which entries carry the clearest memory of the person we traded with.
''')
add('oak_professional','PokedexRating_Text_LessThan140',
    "Oak says the player has become a true professional at collecting Pokemon.",'''
F~A real pro! I should probably stop looking surprised every time the grass moves, then.|
S~Expertise often begins to show in consistent choices rather than impressive terminology.|
S~High praise from someone who knows the work.|
F~It feels strange and good when somebody says you have become capable.|
S~All those ordinary days have turned into skills we do not have to think about as much.|
S~The apprenticeship has received an unexpectedly distinguished review.|
S~Competence can arrive quietly before a compliment points it out.|
S~Practice has made some once-difficult tasks feel almost automatic.|
S~A path walked often has begun to recognize our feet.|
S~It is lovely to hear expertise recognized without making it sound unreachable.|
S~I wonder which part of this now feels natural that once seemed impossible.
''')
add('oak_professor','PokedexRating_Text_LessThan150',
    "Oak extravagantly declares the player a Pokemon Professor.",'''
U~A professor? Do we need a desk, or can the title travel in a backpack?|
F~That is very generous praise. There remains quite a difference between a thorough collection and every research skill.|
S~He is proud of the work. We can accept that without claiming to know everything.|
F~I think he means it kindly enough that we can just let ourselves be pleased.|
S~A title that grand deserves a comfortable seat before we try it on.|
S~The professor has reviewed the work and offered to hand over the reviewer's chair.|
S~A magnificently oversized compliment can still have a sincere heart.|
S~I like the praise, though I would still have a notebook full of questions.|
S~Knowing much has not made the remaining unknowns any smaller.|
S~He is being wonderfully extravagant with his approval.|
S~I wonder whether he enjoys saying that as much as we enjoy hearing it.
''')
add('oak_complete','PokedexRating_Text_Complete',
    "Oak congratulates the player on completing the regional Pokedex.",'''
U~All those encounters have finally filled the whole list. That is a very big little book.|
S~A completed regional record is an extraordinary result, even as questions about its subjects remain.|
S~We finished it. Take the moment before finding another task.|
S~I am glad he sounds as happy about the end as he was about the beginning.|
S~This deserves a celebration we actually sit down to enjoy.|
S~The final entry has earned its closing applause without ending our curiosity.|
S~A finished list can hold a surprising amount of unfinished wonder.|
S~That is a complete set of observations to start asking more detailed questions from.|
S~The last empty space has become a memory of something alive.|
S~A long project deserves more than a quick checkmark when it is done.|
S~I would like to remember the faces around us at this particular moment.
''')
add('oak_national_future','PokedexRating_Text_LookForwardToFilledNationalDex',
    "Oak looks forward to the growing National Pokedex.",'''
S~A bigger book means the next rustling patch can still have something new to introduce.|
S~Expanding the scope adds substantial work, but also makes comparisons across regions possible.|
N~One new entry at a time. No need to turn the whole thing into a race.|
S~His expectation sounds more like interest than impatience. I like that.|
N~A long project needs ordinary rest built into it.|
S~The professor has expressed interest in the sequel before the current expedition is over.|
S~A larger horizon can be inviting without becoming an order to hurry.|
S~There are new habitats and patterns to compare beyond the familiar record.|
S~The edges of the known world have moved, and the questions have followed.|
S~It is nice to have someone looking forward to what we will notice next.|
S~I wonder which unfamiliar place will give us the next surprising entry.
''')
add('oak_dream','PokedexRating_Text_ThankYouMadeDreamReality',
    "Oak sincerely thanks the player for realizing his lifelong Pokedex dream.",'''
S~Oh. This was not just a very large list to him. We helped something precious become real.|
S~Years of research and hope can make an achievement deeply personal to the researcher.|
S~He meant every word. We did something that matters to him.|
S~I would rather let that thank-you sit quietly for a moment.|
S~It is lovely when a long effort gives someone that much joy.|
S~The grand project has ended in something wonderfully simple: a sincere thank-you.|
S~A dream looks different when it finally has somewhere to stand.|
S~All those separate encounters have added up to a result he once could only imagine.|
S~Someone's long-held hope has found a place in the daylight.|
S~He has dropped every formal word and just let the happiness show.|
S~That is the kind of expression a person remembers without needing a picture.
''')
add('tutor_edge_no','Text_DoubleEdgeDeclined',
    "The Double-Edge tutor leaves the offer available after a refusal.",'''
S~A technique we can return for. The road has left us a bookmark.|
N~Keeping the offer open lets us choose based on the team's actual needs.|
N~We can decide later. No reason to rush the choice.|
S~I like an invitation that survives a quiet no.|
N~Time to think is useful before choosing a move.|
S~A postponed lesson, with the door still courteously open.|
S~The absence of pressure makes returning rather more appealing.|
N~We can compare the move with our current options first.|
S~An offered path can remain a path without becoming an obligation.|
S~A refusal received with grace is always a good look.|
S~I wonder how many travellers eventually come back for that lesson.
''')
add('tutor_edge_done','Text_DoubleEdgeTaught',
    "The Double-Edge tutor encourages the player to keep striving toward the League.",'''
S~That encouragement has enough momentum to jog ahead and wait for us at the next corner.|
N~Determination helps, but a League attempt also needs a prepared team.|
N~Keep going carefully. Drive does not replace preparation.|
S~It is nice to hear someone sound certain we can keep improving.|
N~A bit of encouragement travels well between proper rest stops.|
S~The mentor has supplied a stirring send-off toward greater opposition.|
S~Ambition is easier to carry when somebody has said a kind word over it.|
N~We can turn that energy toward a specific improvement in the team.|
S~A warm push at the back need not become a shove toward danger.|
S~His confidence in a traveller is an unexpectedly generous parting gift.|
S~I wonder whether he remembers the advice that kept him going.
''')
add('tutor_wave_no','Text_ThunderWaveDeclined',
    "The Thunder Wave tutor is disappointed that the convenient move is declined.",'''
S~Convenient is a good recommendation, but it is not the same as compulsory.|
N~A useful technique can still be unsuitable for a particular team.|
N~We heard the offer. The choice is still ours.|
N~He can like the move without needing us to agree today.|
N~Not every useful thing belongs in the plan at once.|
N~The pitch has reached its final appeal to convenience.|
N~A little disappointment need not turn our answer into a negotiation.|
N~There are trade-offs even when a technique is handy.|
N~An unused possibility need not disappear from the world.|
N~He should let the recommendation stand without chasing the refusal.|
N~I wonder which situation first made the move feel indispensable to him.
''')
add('tutor_wave_done','Text_ThunderWaveTaught',
    "The tutor explains Thunder Wave paralysis and notes that some Pokemon are immune.",'''
N~A useful trick still has somebody out there who does not find it impressive.|
S~The exception matters. A strategy based on paralysis needs an alternative.|
N~Know what it will not work on before relying on it.|
N~I appreciate hearing the limits along with the advantages.|
N~A fallback plan belongs beside every favourite trick.|
S~A rare sales pitch improved by admitting where the product fails.|
S~Certainty has been politely interrupted by the existence of exceptions.|
S~Good information. We should plan for immunity as well as success.|
N~A net is useful partly because you know what can pass through it.|
N~Practical advice is better when it includes the awkward details.|
S~I wonder how often opponents expect that move and prepare around it.
''')
add('tutor_slide_no','Text_RockSlideDeclined',
    "The Rock Slide tutor teases the player for declining the move.",'''
N~Not choosing falling rocks is not automatically a failure of courage.|
N~A declined technique does not provide evidence about the trainer's fear.|
N~He can keep the teasing. We can keep our answer.|
N~I do not like a choice being turned into a dare.|
N~There are perfectly sensible reasons to pass on a move.|
N~The instructor has mistaken a recruitment pitch for a bravery test.|
N~A small taunt is a poor argument for taking a lesson.|
N~We should decide by team fit rather than react to a provocation.|
N~A falling stone does not need us to prove anything beneath it.|
N~That little jab adds nothing useful to the offer.|
N~I wonder whether he knows how to hear no without teasing someone.
''')
add('tutor_slide_done','Text_RockSlideTaught',
    "The Rock Slide tutor reflects that using it inside the tunnel could be frightening.",'''
U~Falling rocks inside a tunnel is a sentence that makes the ceiling feel closer.|
N~A confined space deserves particular caution around falling debris.|
N~Keep that sort of force away from an unstable tunnel.|
N~I would rather not find out how the ceiling feels about it.|
N~A lesson about rockfalls is a good time to think about the people nearby.|
N~An impressive technique with a distinctly alarming choice of venue.|
N~The tunnel is already providing enough stone overhead for my taste.|
N~The surroundings matter as much as the move's intended target.|
N~The mountain has no need of help shedding pieces onto us.|
N~A thrill loses its appeal quickly when everyone has to stand beneath it.|
N~I would check the space and the people around us before imagining any demonstration.
''')
add('tutor_punch_no','Text_MegaPunchDeclined',
    "The Mega Punch tutor insists the player will return after appreciating the move.",'''
N~He has predicted our return with the confidence of someone who has not asked our plans.|
N~He values the technique highly; that does not make our future choice certain.|
N~He can wait. We are not obliged to prove his prediction.|
N~I would find the invitation easier to like without the certainty about us.|
N~A good offer can stand without insisting everyone must eventually accept it.|
N~The instructor has written himself a triumphant return scene without consulting the visitor.|
N~A confident prediction is still only a prediction, however loudly it stands.|
N~We can assess the move without adopting his rivalry or his expectations.|
N~An open door needs no prophecy about who will cross it.|
N~He could let the technique speak for itself and make a better impression.|
N~I wonder whether anyone has ever simply walked away without looking back.
''')
add('tutor_punch_done','Text_MegaPunchTaught',
    "The Mega Punch tutor declares camaraderie and insults the nearby Mega Kick trainer.",'''
L~We have joined the punching club and immediately received its gossip bulletin.|
N~His enthusiasm for one technique does not establish that the alternative is foolish.|
N~We need not take sides in their argument.|
N~I like the welcome more than the insult attached to it.|
N~Enjoying one specialty does not require spoiling somebody else's.|
S~Membership apparently includes a complimentary feud with the neighbouring school.|
N~Two grown enthusiasts have found a remarkably small hill to quarrel on.|
S~Punching and kicking solve different problems. The rivalry adds no useful data.|
N~One man's devotion has grown an unnecessary little thorn.|
N~The warm welcome would look better without someone else's dignity under its shoe.|
S~I wonder how long they have been making exactly these speeches about each other.
''')
add('tutor_kick_no','Text_MegaKickDeclined',
    "The Mega Kick tutor predicts the player will come crawling back.",'''
N~A return invitation has somehow put mud on its own welcome mat.|
N~The condescension contributes nothing to evaluating the move.|
A~We said no. He can manage without the insult.|
N~I would rather return because I wanted to learn, not because he wanted to gloat.|
N~Teaching works better when the learner is not being talked down to.|
N~The proposed reunion is rather more humiliating in his version than I care for.|
N~An invitation that imagines us crawling can remain unanswered.|
N~The useful question is whether the move fits our team, not his pride.|
N~There is no need to kneel before a door simply because it remains open.|
A~What an unappealing way to advertise another conversation with himself.|
N~I wonder whether he mistakes making people defensive for being persuasive.
''')
add('tutor_kick_done','Text_MegaKickTaught',
    "The Mega Kick tutor declares a bond through kicking and disparages the punching tutor.",'''
L~Soul mates in kicking is a very specific place to find belonging.|
N~Shared enthusiasm is pleasant. The dismissal of punching is not a technical comparison.|
N~We learned a technique, not an obligation to join his feud.|
F~That is a lot of closeness to announce before we have even left.|
N~A shared specialty can be enjoyable without making the neighbours into enemies.|
S~The kicking fraternity has welcomed us and immediately disclosed its ancient grievance.|
S~An impressively narrow basis for declaring a meeting of souls.|
N~Both techniques deserve judging on their uses rather than their instructors' pride.|
N~A bond made through movement need not require standing against someone else.|
N~The enthusiasm is charming until it drags the other tutor into it.|
S~I wonder whether those two would miss having each other to complain about.
''')
add('tutor_counter_no','Text_CounterDeclined',
    "The Counter tutor invites the player to return if interested later.",'''
S~A no has been accepted without launching a counterattack. Nicely done.|
S~A standing offer allows a later decision when the team's needs may differ.|
N~We can return if we need it. Nothing to settle now.|
S~It is easier to think clearly when the offer does not push back.|
S~A useful lesson will still be useful after we have had time to consider it.|
S~A courteous exit leaves the next meeting entirely possible.|
S~I appreciate an invitation that does not follow us down the road.|
N~We can evaluate the technique against our current options in peace.|
S~Some offers are kind enough to remain still while we move on.|
S~That is a graceful way to leave a future conversation open.|
S~I wonder how the move became this person's favourite thing to teach.
''')
add('tutor_counter_done','Text_CounterTaught',
    "The Counter tutor asks whether the player has been using the move.",'''
S~The teacher wants to know what happened after the lesson. That is a nice detail.|
S~Following up on practical use can reveal whether instruction transferred into actual decisions.|
N~Useful to think about when it helped and when it did not.|
N~I hope the question leaves room for an honest answer either way.|
S~A skill becomes more familiar when there is time to try it and talk it over.|
S~The instructor has requested news from the technique's subsequent adventures.|
S~A lesson has acquired an afterlife interesting enough to ask about.|
S~Feedback from real battles would be more useful than guessing how it went.|
N~A taught thing changes when somebody carries it out into the world.|
S~Remembering a former pupil makes a better impression than reciting the same pitch.|
S~I wonder which part of using it the tutor most wants to hear about.
''')
add('tutor_body_no','Text_BodySlamDeclined',
    "The Body Slam tutor sends the player off with an exuberant boing.",'''
L~A cheerful refusal accepted with a sound effect. That is a refreshingly bouncy goodbye.|
S~The enthusiasm has survived a declined lesson with no apparent difficulty.|
S~Friendly enough. We can leave without an argument.|
S~I did not expect the goodbye to make me smile like that.|
S~A light parting can improve an otherwise ordinary stop.|
S~The lesson has been declined; the instructor's spring remains fully wound.|
S~A conversation can end pleasantly without anyone getting what they offered.|
S~That much energy seems to be part of the tutor's standard equipment.|
S~Some people leave a little bounce in the air after speaking.|
S~An unembarrassed bit of silliness is rather appealing.|
S~I wonder whether anyone manages to hear that goodbye without smiling.
''')
add('tutor_body_done','Text_BodySlamTaught',
    "The Body Slam tutor celebrates with an emphatic bouncing sound.",'''
L~That is either celebration or a person briefly becoming a spring.|
S~A memorable sound makes for a remarkably concise closing remark.|
S~He seems pleased. Hard to miss that.|
F~I think that was a happy goodbye. It was certainly an energetic one.|
S~A cheerful little finish to the visit.|
S~The closing statement has dispensed with words and retained all its enthusiasm.|
S~An entire mood expressed with a very elastic syllable.|
L~A spring-loaded farewell would apparently be entirely on brand here.|
S~The air has been left slightly rounder by that sound.|
S~I respect committing that completely to a ridiculous little flourish.|
S~That is the sort of sound a visitor remembers longer than the formal explanation.
''')
add('tutor_metronome_no','Text_MetronomeDeclined',
    "The Metronome tutor insists the move is fun after the player declines.",'''
S~Fun is an excellent recommendation. It is still allowed to be somebody else's fun.|
N~Enjoyment varies between trainers. His preference does not settle our choice.|
N~We can pass without arguing about whether he enjoys it.|
N~It can be fun and still not feel right for us today.|
S~A favourite activity is tempting, but it does not have to be shared by everyone.|
S~The enthusiastic review has remained enthusiastic in the face of a poor booking.|
S~At least he has not mistaken fun for a solemn duty.|
N~A move's unpredictability may be enjoyable without fitting our current plan.|
S~A playful possibility can wait without losing its sparkle.|
N~The pitch works better when it leaves space for different tastes.|
S~I wonder what unexpected move made him laugh the hardest.
''')
add('tutor_metronome_done','Text_MetronomeTaught',
    "The tutor describes Metronome producing moves the Pokemon does not normally know.",'''
U~An unexpected move hiding inside a little ticking gesture. The surprise has a very small door.|
S~The unpredictability is central to the technique; a specific outcome should not be assumed.|
N~A surprise can go either way. Keep that in mind.|
S~I can see why he likes the moment before finding out what happens.|
N~A little improvisation is fun when the consequences are manageable.|
S~A performer that refuses to disclose its next line until the cue arrives.|
S~Uncertainty has acquired a charmingly regular little sound.|
S~We cannot build a plan around one guaranteed result from that.|
N~A small gesture opens a box without promising what lives inside.|
S~It is an appealing idea precisely because it is so difficult to predict.|
S~I wonder how differently each trainer remembers the same unpredictable move.
''')
add('tutor_seismic_no','Text_SeismicTossDeclined',
    "The Seismic Toss tutor confidently expects the player to return.",'''
N~Another teacher with a very confident forecast about our future footsteps.|
N~Interest may change later, but there is no reason to treat that as inevitable.|
N~He can keep the offer. We can keep moving.|
N~I prefer an invitation to a prediction made on my behalf.|
N~We can decide when there is a good reason, rather than a point to prove.|
N~The instructor has pencilled in our return without asking for availability.|
N~The future remains free to disappoint his appointment book.|
N~The move should earn a place through usefulness, not insistence.|
N~A door can stay open without calling every departing traveller back.|
N~A little less certainty about strangers would improve the welcome.|
N~I wonder whether he has ever asked what a visitor actually needs.
''')
add('tutor_seismic_done','Text_SeismicTossTaught',
    "The Seismic Toss tutor encourages persistence with a toss-in-the-towel pun.",'''
L~He has managed to toss a pun into the encouragement. No towel required.|
S~A little wordplay can make an otherwise ordinary reminder more memorable.|
S~Keep trying, sensibly. Fair advice beneath the joke.|
S~That was a gentle way to tell someone not to give up.|
S~A small joke can make encouragement easier to take along.|
S~The tutor has closed with a pun and an entirely serviceable moral.|
S~A harmless joke is a respectable place to hide a kind thought.|
S~A memorable phrase can help the useful advice survive the walk away.|
S~A light word can still keep a little resolve from sinking.|
S~I like encouragement that does not need to look terribly important.|
S~I wonder how long he has been waiting for somebody new to hear that one.
''')
add('tutor_soft_no','Text_SoftboiledDeclined',
    "The Softboiled tutor hopes to chat again after the lesson is declined.",'''
S~The offer was declined and the person still wants to see us. That feels nice.|
S~The conversation has value to the tutor beyond whether the technique is accepted.|
S~A friendly goodbye. No debt attached to it.|
S~I like that a future chat does not have to be another lesson.|
S~It is lovely when a visit can be enough on its own.|
S~The invitation has quietly changed from instruction to company.|
S~A little warmth survives the absence of a useful transaction.|
S~That is a good way to keep a conversation open without applying pressure.|
S~A familiar face can be welcome without arriving with a request.|
S~There is something charming about wanting another conversation rather than another chance to persuade.|
S~I wonder what we would talk about if we stopped simply to say hello.
''')
add('tutor_soft_done','Text_SoftboiledTaught',
    "The Softboiled tutor offers a simple wish of good luck.",'''
S~A small good-luck wish can fit into almost any pocket.|
S~A brief expression of goodwill makes a perfectly complete farewell.|
S~Kind of the tutor. We can carry that onward.|
S~I like a goodbye that leaves the day feeling a little gentler.|
S~A little kindness is welcome even when there is nothing more to arrange.|
S~A concise farewell with no unnecessary flourish obscuring the warmth.|
S~The simplest good wishes often avoid saying too much.|
S~Practical instruction and a friendly send-off make a good combination.|
S~A kind word has been set lightly beside the road.|
S~Good manners need not be elaborate to leave a lovely impression.|
S~I wonder whether the tutor knows how much a small wish can improve a day.
''')
add('tutor_sub_no','Text_SubstituteDeclined',
    "The Substitute tutor wistfully says the move seems fun.",'''
S~A little disappointed, but still fond of the idea. That is all right.|
N~The appeal is personal, and declining it does not invalidate the tutor's enjoyment.|
N~We can leave the idea with someone who clearly likes it.|
S~I can hear the little wish behind the offer.|
S~Not everything enjoyable has to become part of our own plans.|
S~The rejected proposal retains its enthusiastic author. A survivable review.|
S~A small disappointment need not become a dramatic rejection of the person.|
N~We can appreciate the concept without deciding to use it.|
S~A playful thought can remain bright even when nobody picks it up today.|
N~Different ideas of fun can coexist quite comfortably.|
S~I wonder what the tutor imagines first when thinking about that move.
''')
add('tutor_sub_done','Text_SubstituteTaught',
    "The Substitute tutor daydreams about sheltering in a Kangaskhan pouch.",'''
L~A Kangaskhan pouch does sound cosy. I suspect the actual resident has priority, though.|
S~The thought is understandable, but the pouch serves a biological purpose rather than guest accommodation.|
N~Comfortable thought. Leave the pouch to the youngster.|
F~I understand wanting somewhere warm to hide for a little while.|
S~That is a very portable idea of a comfortable afternoon.|
S~The daydream has requested a rather exclusive form of lodging.|
S~A harmless wish for shelter, with a substantial practical size problem.|
S~Warmth and protection: an excellent design, already occupied.|
S~Some dreams are simply about being small enough to be carried safely.|
S~It is an unexpectedly tender fantasy behind a very practical lesson.|
S~I wonder whether seeing a youngster tucked in there first gave the tutor that idea.
''')
add('tutor_swords_no','Text_SwordsDanceDeclined',
    "The Swords Dance tutor accepts the player's refusal without fuss.",'''
S~A no that gets to be a complete answer. Always refreshing.|
S~The tutor has accepted a different choice without demanding justification.|
S~That settles it. We can move on comfortably.|
S~It is nice when refusing something does not make the air change.|
S~An easy response leaves everyone free to enjoy the rest of the day.|
S~A modest exit, with no theatrical wounded pride to tidy away.|
S~A conversation need not acquire a bruise every time somebody says no.|
S~We can keep considering our options without a debate following us.|
S~An unchosen path has been left peacefully where it was.|
S~Quiet acceptance is a better look than trying to win every exchange.|
S~I like how little work the tutor makes us do to leave politely.
''')
add('tutor_swords_done','Text_SwordsDanceTaught',
    "The Swords Dance tutor wishes strength could keep increasing forever.",'''
N~Forever is a lot of practice. I hope there are water breaks somewhere in it.|
N~Improvement has limits and trade-offs; indefinite growth is an aspiration rather than a guarantee.|
N~Stronger is useful. Knowing when to stop matters, too.|
N~I wonder whether constant improvement would ever let someone feel satisfied.|
N~Strength needs time to recover as well as time to grow.|
S~An ambitious wish for a sequel with no final volume.|
N~Endless progress sounds suspiciously like never being allowed a day off.|
N~A clear goal gives improvement more direction than simply demanding more.|
N~Even growing things pause when the season asks them to.|
N~Wanting to grow is appealing. Never feeling enough sounds exhausting.|
S~I wonder what becoming stronger would let the tutor actually do differently.
''')
add('tutor_explosion_no','Text_ExplosionDeclined',
    "The Explosion tutor agrees that the technique is terrifying after it is declined.",'''
S~A rare instructor willing to agree that the alarming thing is, in fact, alarming.|
N~Recognizing a technique's severe trade-offs is a valid reason to decline it.|
N~A sensible caution. We can leave it there.|
N~It is a relief not to have the fear turned into a challenge.|
N~Some ideas are easier to appreciate from a comfortable distance.|
S~The frightening pitch has received a mutually agreed curtain call.|
S~Agreement has saved us a very unnecessary argument with a bad idea.|
N~A dramatic option is not automatically a useful one for our plan.|
N~We are allowed to leave some kinds of thunder sleeping.|
N~I appreciate the tutor finally hearing the practical objection.|
N~I wonder whether anyone has ever looked more relieved by a declined lesson.
''')
add('tutor_explosion_done','Text_ExplosionTaught',
    "The Explosion tutor finds the idea of using the move on a volcano thrilling.",'''
U~An explosion on a volcano feels like adding an exclamation mark to another exclamation mark.|
N~A volatile setting is a reason for caution, not evidence that a risky demonstration is appropriate.|
N~A thrill is no reason to put people nearby at risk.|
N~I would prefer the volcano to remain scenery rather than join the demonstration.|
N~The setting already supplies enough heat and uncertainty for one visit.|
N~The spectacle has become so ambitious that I would like to leave the audience.|
N~The mountain is already doing an excellent job of seeming ominous.|
N~We should account for the environment before considering a powerful move.|
N~Sleeping fire needs no visitor enthusiastically knocking on its door.|
N~That is a rather large risk to dress up as an exciting anecdote.|
N~I would rather remember the view than a demonstration nobody needed.
''')
add('mimic_no','Text_MimicDeclined',
    "Copycat asks whether the player dislikes Mimic after the offer is declined.",'''
N~We can like an idea without signing up for every version of it.|
N~Declining a lesson does not necessarily indicate dislike of the technique.|
N~No need to turn the choice into a judgment about her favourite move.|
N~I hope she does not hear the answer as a rejection of her.|
N~Enjoying something and choosing it today are different questions.|
N~The rejected offer has been mistaken for an unfavourable review of the whole concept.|
N~A single no has been asked to explain a suspicious amount.|
N~We may simply prefer the team's existing moves. There are several possibilities.|
N~A reflection need not copy every choice to remain friendly.|
N~She can keep her enthusiasm without making us justify different tastes.|
S~I wonder whether she enjoys the move or making people react to it more.
''')
add('mimic_done','Text_MimicTaughtFemale Text_MimicTaughtMale',
    "Copycat gleefully mimics the player's own thanks and conversation.",'''
L~We have met a conversational echo that is thoroughly enjoying itself.|
S~Her imitation depends on timing and observation as much as repeating the words.|
S~She got the reaction she wanted. Hard to miss how pleased she is.|
F~Hearing your own greeting come back must feel a little strange.|
L~Even the thank-you has come back for a second helping.|
S~The visitor has unexpectedly become the source material for the performance.|
S~A mirror has developed opinions and found the whole situation hilarious.|
S~Good mimicry takes careful observation of details people usually ignore.|
S~A borrowed voice has returned wearing a mischievous smile.|
S~She clearly enjoys catching the little details that make someone recognizable.|
S~I wonder which gesture gave her the quickest way to imitate us.
''')
add('cape_decline','Text_YouRejectIt',
    "The Cape Brink tutor protests a rejected lesson and says she will persist.",'''
N~A dramatic protest does not make our answer less of an answer.|
N~Her commitment to teaching does not override the learner's choice.|
N~She can keep the offer. She needs to respect the refusal.|
N~That is a lot of feeling to place on someone deciding about a lesson.|
N~A willing pupil is worth waiting for rather than wearing down.|
N~The mentor has responded to a declined role with an alarmingly forceful appeal.|
N~Determination is less charming when aimed at someone else's boundaries.|
N~She may care deeply about passing it on, but consent still matters.|
N~An old wish should not become a hand gripping someone else's sleeve.|
N~A graceful pause would do more for her cause than another protest.|
N~I wonder whether the fear of losing the knowledge makes every refusal feel final to her.
''')
add('cape_all','Text_PassedOnEverythingIKnow',
    "The Cape Brink tutor feels at peace after passing on all her knowledge.",'''
S~Her knowledge has found somewhere new to live. I can see why she sounds relieved.|
S~Teaching preserves a skill beyond one person's ability to continue practising it.|
S~She finished something that mattered to her. Let her have the moment.|
S~It sounds as though she has been waiting to take that breath for a long time.|
S~There is comfort in knowing something precious will not end with you.|
S~The lifelong work has found its next chapter in somebody else's hands.|
S~An ending can be gentler when something important keeps going.|
S~Passing on the method is a substantial achievement in its own right.|
S~The old flame has caught another wick, and the room has not grown darker.|
S~Her relief feels far more personal than a simple lesson completed.|
S~I wonder who first trusted her with the knowledge she has now passed onward.
''')
add('cape_use','Text_MakeBestUseOfMove',
    "The Cape Brink tutor urges careful use of the technique she entrusted to the player.",'''
N~She has handed over something important and wants it treated as more than a novelty.|
N~A learned technique becomes valuable through informed application rather than possession alone.|
N~Use it thoughtfully. Power needs judgment beside it.|
N~I can hear how much she wants the teaching to mean something beyond this visit.|
N~Something entrusted to us deserves a bit of care in how we use it.|
N~The mentor has requested a worthy future for her life's work.|
N~A powerful gift can carry a quieter request for responsibility.|
N~Understanding when to use it matters as much as knowing how.|
N~What has been passed onward still asks for a careful hand.|
N~She is asking us to respect the work, not merely admire the result.|
S~I wonder what use of the technique would make her feel proudest.
''')
add('cape_mistaken','Text_JustMistaken',
    "The Cape Brink tutor realizes the presented Pokemon is not the one she had hoped to teach.",'''
N~A hopeful guess has come back down to earth rather quietly.|
N~She has corrected her initial assessment rather than insisting it must be right.|
N~Wrong fit for the lesson. That does not make the Pokemon lesser.|
N~The change in her voice sounds like a disappointment she knows is her own.|
N~Not being right for one lesson is no criticism of the learner.|
N~The anticipated apprentice has turned out to be a mistaken identification.|
N~A small retreat from certainty is sometimes the most honest part of a conversation.|
N~A specialized technique can have narrow requirements without judging overall ability.|
N~A door that does not open for this visitor need not be a cruel one.|
N~At least she takes back the assumption instead of blaming the Pokemon.|
N~I wonder what small detail first made her think she had found the right pupil.
''')
add('cape_rejuvenated','Text_FeelRejuvenated',
    "The Cape Brink tutor says teaching relieved her and made her feel young again.",'''
S~The lesson seems to have taken a weight off her shoulders rather than years off the calendar.|
S~Relief and renewed purpose can change how energetic a person feels.|
S~Good to see her feeling lighter after all that worry.|
S~She sounds as though she can finally enjoy having finished something.|
S~A burden set down leaves room for a very different kind of day.|
S~The veteran teacher has discovered that finishing her work need not mean finishing herself.|
S~A good ending has unexpectedly offered her some room to begin again.|
S~Passing knowledge onward can be energizing instead of merely exhausting.|
S~Something long held has left her hands and returned as lightness.|
S~The relief has made a warmer impression than any grand declaration could.|
S~I wonder what she might feel like doing now that the worry is quieter.
''')
add('cape_taught','Text_TaughtMove',
    "The Cape Brink tutor is moved that she lived to pass on the technique.",'''
S~That lesson has been waiting inside a very long hope. No wonder she needs a breath.|
S~A long-held uncertainty has been resolved through the successful transfer of a skill.|
S~It meant a lot to her. Give her time to catch her breath.|
S~I do not think this is a moment that needs us to fill the silence.|
S~Some accomplishments deserve a seat and a quiet minute before anything else.|
S~The triumph is not the spectacle of the move, but that she got to teach it at all.|
S~A feared ending has been interrupted by something continuing.|
S~The important result here is that the knowledge no longer rests with only one person.|
S~A long-kept ember has finally found another place to burn.|
S~Her relief makes the whole visit feel much more intimate than a routine lesson.|
S~I wonder how many years she has imagined this particular moment.
''')
add('daycare_one_well','DayCare_Text_YourMonIsDoingFine',
    "The Day-Care man reassures the player that the deposited Pokemon is doing fine.",'''
S~A small status report can be a very welcome thing when somebody else is watching your friend.|
S~A routine reassurance, with no claim about growth or any specific change.|
S~Good to hear they are doing all right.|
S~Sometimes that is exactly the little bit of news you came back hoping for.|
S~It is comforting to hear about the ordinary well-being, not only the results.|
S~The caretaker has supplied the peaceful update every anxious visitor appreciates.|
S~Nothing dramatic happening can be the nicest news available.|
S~A simple check-in confirms the stay is proceeding normally.|
S~A familiar life is carrying on gently while we are elsewhere.|
S~A warm update makes the service feel a little more personal.|
S~I wonder what the Pokemon has been enjoying while we have been away.
''')
add('daycare_capacity','DayCare_Text_YouHaveNoRoomForIt',
    "The Day-Care man cannot hand over the Egg until there is room in the party.",'''
N~A small passenger still needs a proper place before we take it along.|
N~Party capacity must be resolved before the Egg can be transferred safely.|
N~Make room first. The Egg can wait here.|
N~There is no need to hurry the handover just because we came to collect it.|
N~A bit of preparation makes carrying something delicate less awkward.|
N~The new arrival is awaiting a suitable place in the travelling arrangement.|
N~A practical delay, not a rejection of the little thing waiting.|
N~We should sort the team before trying the collection again.|
N~Something small can still ask for space that is truly its own.|
N~It is better to leave with room prepared than juggle the problem on the doorstep.|
S~I wonder how different the next leg of the journey will feel with an Egg along.
''')
add('daycare_egg_decline','DayCare_Text_IllKeepIt',
    "The Day-Care man agrees to keep the Egg after the player declines it.",'''
N~He has accepted the choice and kept the little passenger somewhere cared for.|
N~The refusal has a clear resolution: the Day-Care man retains the Egg.|
N~The choice is settled. No need to keep pressing it.|
N~I am glad the conversation ends without making the refusal cruel.|
N~Taking responsibility is a choice that should be made willingly.|
N~The prospective new chapter has been left in its caretaker's hands.|
N~An unaccepted beginning still belongs somewhere in the world.|
N~A clear decision avoids leaving everyone uncertain about the handover.|
N~Not every small life that crosses our road must travel under our roof.|
N~A considerate response gives the decision a clean and respectful ending.|
N~I wonder whether he often ends up caring for Eggs travellers choose not to take.
''')
add('daycare_introduction','DayCare_Text_ImDaycareManSpeakToMyWife',
    "The Day-Care man introduces his work and directs service requests to his wife.",'''
S~He has supplied the important introduction and pointed us toward the actual arrangements.|
N~A clear division of responsibilities makes it easier to know whom to ask.|
N~His wife handles the arrangements. We know where to go.|
S~It is nice to hear someone talk about the Pokemon as precious.|
S~Care is easier to trust when the people doing it seem to value the guests.|
S~The proprietor has introduced the household and correctly identified the booking desk.|
S~A little practical information wrapped in a warm description of the work.|
S~Clear handoffs are useful even in a service run by only two people.|
S~A resting place begins to feel welcoming when its keeper speaks gently of its guests.|
S~He sounds proud of helping without making himself the centre of the introduction.|
S~I wonder how many travellers' Pokemon they have come to know over the years.
''')
add('daycare_egg_care','DayCare_Text_TakeGoodCareOfIt',
    "The Day-Care man asks the player to care well for the Egg being handed over.",'''
S~A small bundle comes with a very ordinary and very important request.|
N~Care during transport matters even before we know which Pokemon will emerge.|
N~Keep it secure and travel thoughtfully.|
S~It is a gentle little handover for something whose whole beginning is still ahead.|
S~We can make room in the day for being careful rather than simply rushing onward.|
S~An unknown new character has arrived with a caretaker's brief blessing.|
S~The quiet part before an introduction can feel surprisingly full.|
N~We should plan for a fragile passenger, not treat it like spare equipment.|
S~A small closed world has been entrusted to our footsteps.|
S~The request is simple enough that it deserves to be taken seriously.|
S~I wonder which ordinary moment the Egg will choose to make memorable.
''')
add('daycare_no_money','DayCare_Text_NotEnoughMoney Route5_PokemonDayCare_Text_DontHaveEnoughMoney',
    "The Day-Care service cannot complete the withdrawal because the player lacks the fee.",'''
N~The reunion has met a very unromantic number on the bill.|
N~The stated service fee remains unmet, so the withdrawal has not completed.|
N~We need the fee before collecting the Pokemon. No point arguing here.|
N~It is a disappointing thing to find out when you came back to see them.|
N~We should keep the collection cost in mind before spending elsewhere.|
N~The heartfelt reunion has been postponed by the accounts department.|
N~An ordinary bill can be a surprisingly effective plot obstacle.|
N~We can plan the required money before trying the transaction again.|
N~A practical debt stands in the space between arrival and reunion.|
N~Better to understand the cost now than pretend the exchange happened.|
N~I wonder how often travellers forget the fee while planning to come back.
''')
add('daycare_farewell','DayCare_Text_ComeAgain DayCare_Text_FineThenComeAgain Route5_PokemonDayCare_Text_ComeAgain Route5_PokemonDayCare_Text_ComeAnytimeYouLike',
    "The Day-Care keeper closes the visit and leaves the service available for another time.",'''
S~A simple goodbye, with the next visit left comfortably possible.|
N~The conversation has ended without implying any particular service was completed.|
N~We can leave it there and decide later.|
S~It is nice when a routine visit can end without any fuss.|
S~There will be another chance if the service suits our plans.|
S~The curtain falls on a perfectly ordinary visit, with no sequel demanded.|
S~An uneventful ending can be a very pleasant thing.|
N~We have time to consider the team before making another arrangement.|
S~A door remains available without following us down the path.|
S~A polite farewell asks very little and leaves a good impression.|
S~I wonder what other travellers will be stopping in after us today.
''')
add('daycare_husband','DayCare_Text_HusbandWasLookingForYou',
    "The Day-Care lady tells the player that her husband was looking for them.",'''
S~A small change of errand. The person we came to see knows who wants to see us.|
N~The message gives us a specific person to check with rather than a vague hint.|
N~We should ask him what he needs.|
S~It sounds as though there is something waiting to be said, not something to guess at.|
N~Best speak to him before heading off on the next stretch.|
S~The household has supplied a tidy handoff to the next conversation.|
N~A useful message, refreshingly free of elaborate mystery.|
N~We can get the actual information directly from him.|
N~An ordinary doorstep has become the beginning of a different conversation.|
S~It is considerate of her to remember and pass that along.|
S~I wonder whether he has been watching the road for us to return.
''')
add('daycare_full_party','DayCare_Text_YourPartyIsFull Route5_PokemonDayCare_Text_YouveGotNoRoomForIt',
    "The Day-Care keeper asks for party space before a deposited Pokemon can be returned.",'''
N~We have arrived for a reunion with every travelling place already occupied.|
N~The withdrawal requires a free party slot before it can complete.|
N~Make room, then collect the Pokemon.|
N~A short practical delay is better than an awkward handover.|
N~We can sort the team calmly and come straight back.|
N~The returning cast member needs somewhere to stand before joining the scene.|
N~Even a happy reunion has its logistical details.|
N~A quick team adjustment resolves the capacity issue.|
N~The familiar companion is waiting for an actual place, not merely a wish.|
N~Preparation would have made the visit smoother, but the fix is straightforward.|
N~I wonder whether the Pokemon has already noticed us coming back to the door.
''')
add('daycare_last_battler','DayCare_Text_WhatWillYouBattleWith Route5_PokemonDayCare_Text_WhatWillYouBattleWith',
    "The Day-Care keeper refuses a deposit that would leave the player without a Pokemon able to battle.",'''
N~Leaving every capable partner behind would make the next challenge rather one-sided.|
N~The remaining team needs at least one Pokemon able to handle a battle.|
N~Keep a capable partner with us. Sensible boundary.|
N~It is a practical kindness to catch that before we leave.|
N~A care arrangement should not leave the rest of the journey unprepared.|
N~The proposed boarding arrangement has accidentally removed the expedition's entire defence.|
N~Some helpful plans need someone to point out the obvious missing piece.|
N~Check the remaining team, not only the Pokemon we want to leave.|
N~A road asks for company that can still help us meet what comes.|
N~A well-timed refusal can be more useful than an unquestioning yes.|
N~I am glad someone checked what our team would look like after the choice.
''')
add('daycare_one_only','DayCare_Text_YouHaveJustOneMon Route5_PokemonDayCare_Text_OnlyHaveOneMonWithYou',
    "The Day-Care keeper will not accept the player's only Pokemon.",'''
N~The only travel buddy cannot stay here while we go off being an entire expedition alone.|
N~Retaining a travelling partner is a basic requirement before making a deposit.|
N~We need someone with us on the road. Come back with another partner first.|
N~It would feel strange to leave with nobody beside us.|
N~We should prepare the rest of the team before arranging a stay.|
N~The guest list has attempted to absorb the entire travelling cast.|
N~A very small headcount can create a very obvious practical problem.|
N~The service can wait until our travelling team has another eligible member.|
N~An empty road is not what this care arrangement is meant to give us.|
N~The rule is easy to understand once you picture the walk away.|
N~I wonder how many first-time visitors only realize that at this exact moment.
''')
add('daycare_wait','Route5_PokemonDayCare_Text_ComeSeeMeInAWhile',
    "The Route 5 keeper completes a deposit and asks the player to return after some time.",'''
S~A little stay has begun. We can let the caretaker actually have some time to do the job.|
N~The deposit is followed by a clear invitation to return after a suitable interval.|
N~They are in his care now. We can check back later.|
S~Walking away can feel odd even when the arrangement is a good one.|
S~We can plan a return without hovering on the doorstep.|
S~A temporary farewell, with the next meeting built gently into it.|
S~A small absence can be ordinary without feeling entirely ordinary.|
N~Let the arrangement run for a while before evaluating the result.|
S~One set of footsteps rests here while the road keeps ours for a little longer.|
S~A clear return invitation makes the parting feel less abrupt.|
S~I wonder what new little habits the Pokemon will have picked up when we return.
''')
