"""Reviewed Kanto background inspections and fixed object outcomes."""
ROWS=[]
E=dict(N='neutral',S='soft_smile',A='annoyed',F='flustered',D='sad',U='surprised',M='smug',L='laughing')
def add(key,labels,subject,lines):
    replies=[]
    for s in lines.strip().split('|'):
        s=s.strip()
        if len(s)>1 and s[1]=='~'and s[0]in E:s=E[s[0]]+s[1:]
        replies.append(s)
    assert len(replies)==11,(key,len(replies))
    ROWS.append(dict(key='kanto_bg_inspect_'+key,labels=labels.split(),subject=subject,replies=replies))
add('everything_sign','CeladonCity_Condominiums_Roof_Text_IKnowEverything',
    "A rooftop sign makes the extravagant claim that its owner knows everything.",'''
L~Everything? I have several questions about socks that could make this a very long afternoon.|
N~A confident assertion with a rather impossible burden of proof attached.|
N~A sign can say anything. We can judge the advice separately.|
S~I would be more comfortable asking questions if the sign left room for not knowing.|
L~An expert in everything should be useful when dinner refuses to behave.|
M~The shortest autobiography ever written, and possibly the least reliable.|
S~An admirably compact way to leave no room for growth.|
N~Knowing the limits of your knowledge is a much more useful skill.|
N~A very full cup has announced that it contains the entire sea.|
M~A modest sign would apparently have been too large a sacrifice.|
S~I wonder which question its owner most enjoys being challenged with.
''')
add('tm_pamphlet','CeladonCity_Condominiums_RoofRoom_Text_PamphletOnTMs',
    "A Silph pamphlet describes TMs and repeatedly usable HMs.",'''
S~A little reading material for people who like their new techniques to come with instructions.|
N~The pamphlet describes its catalogue and usage rules. We should still check the item we actually have.|
N~Useful to read the instructions before relying on a tool.|
S~I like when something unfamiliar comes with a quiet explanation instead of a test.|
N~A quick look at the instructions can save a very avoidable disappointment later.|
S~The manufacturer has supplied a brief practical preface to a shelf of possibilities.|
S~A small pamphlet is preferable to learning every limitation through regret.|
S~Clear instructions make useful equipment much easier to put to work properly.|
N~A few printed words can steady the hand that carries an unfamiliar thing.|
S~The useful part is knowing what something does before choosing it.|
S~I wonder which question made the writer realize that explanation needed to be included.
''')
add('sports_game','CeladonCity_DepartmentStore_3F_Text_SportsGame',
    "A sports game on display seems like something Dad would enjoy.",'''
S~A shop display has turned into a very specific gift idea. That is dangerous for the budget.|
S~Recognizing someone else's tastes is a thoughtful starting point for choosing a gift.|
S~Nice to spot something with another person in mind.|
S~It is sweet when a small familiar detail makes somebody come to mind.|
S~A good gift begins with remembering what the other person enjoys.|
S~The browsing expedition has unexpectedly acquired a warmly personal subplot.|
S~A shelf can briefly make an absent person feel close.|
S~We could check what kind of sports game it is before deciding it would suit him.|
S~A little box has tugged on a thread that runs back home.|
S~Thinking of the person matters more than simply choosing the most expensive thing.|
S~I wonder what ordinary evening together makes that game feel like his kind of thing.
''')
add('fighting_game','CeladonCity_DepartmentStore_3F_Text_FightingGame',
    "A fighting game on display looks challenging.",'''
S~Another kind of battling, apparently designed for people whose fingers also need an adventure.|
N~An intimidating appearance does not tell us how approachable the game actually is.|
N~We can look without having to prove anything to a display.|
S~Learning something difficult can be fun when there is room to be clumsy first.|
S~A challenge is easier to enjoy when it is allowed to start as play.|
S~The shelf has offered an alternative venue for being dramatically outmatched.|
S~A small box has managed to look rather more confrontational than necessary.|
S~I would like to see how well it teaches the basics before judging the difficulty.|
S~A make-believe contest can still ask a real little leap of courage.|
S~Looking difficult is one thing. Making people want to try is the more interesting trick.|
S~I wonder whether the players who love it most began by losing rather spectacularly.
''')
add('red_green','CeladonCity_DepartmentStore_3F_Text_RedGreenBothArePokemon',
    "The display offers Red and Green Pokemon games side by side.",'''
S~Two colourful invitations to spend far too long deciding which colourful invitation to take.|
N~The two editions invite comparison. Their packaging alone would not establish every difference.|
N~We can read what each offers before choosing.|
S~I like how two small boxes can suggest different beginnings to the same kind of afternoon.|
S~It is a good excuse to compare interests with a friend before buying anything.|
S~The same premise has dressed for two separate opening nights.|
S~A choice becomes strangely large when both little boxes look inviting.|
S~I would compare the actual contents rather than choose solely by the colour.|
S~Two doors can invite the same curiosity in slightly different coats.|
S~A paired display knows exactly how to make browsing last longer.|
S~I wonder which small difference people end up caring about most after they start playing.
''')
add('broken_slot','CeladonCity_GameCorner_Text_OutOfOrder',
    "A Game Corner machine is marked out of order.",'''
S~A machine whose current game is not taking anybody's money. Quite a restful design.|
N~The sign clearly states that the machine is unavailable. No attempt to operate it is warranted.|
N~Leave the broken machine alone. Plenty else to do.|
N~A clear little notice saves an awkward disappointment.|
N~We can spend the time somewhere that does not need a repair first.|
S~The attraction has wisely cancelled its performance rather than improvise a malfunction.|
S~An inactive machine can be remarkably good company in a loud room.|
N~A useful failure notice. Testing it ourselves would not make it more fixed.|
N~This little corner of chance has gone quiet for the day.|
N~It is better to say clearly that something is broken than let people discover it at their expense.|
S~I wonder what the room sounds like when all the machines finally stop for the night.
''')
add('lunch_slot','CeladonCity_GameCorner_Text_OutToLunch',
    "A Game Corner seat is reserved while its user is out to lunch.",'''
S~A gaming session has left a note explaining that lunch briefly won the argument.|
N~The sign communicates a temporary absence rather than an abandoned place.|
N~Reserved. Leave it for the person coming back.|
S~I hope the break feels like a proper pause instead of an anxious dash back.|
S~At least somebody has remembered that an afternoon needs lunch in it.|
S~The player has announced an intermission and retained the seat for the next act.|
S~A small note has been asked to sit patiently in somebody else's place.|
N~The message makes the intended use clear without us needing to guess.|
S~An empty chair is holding a little promise of return.|
N~A reservation deserves the same courtesy whether its owner is watching or eating.|
S~I wonder whether the person notices the room differently after stepping outside for a while.
''')
add('keys_slot','CeladonCity_GameCorner_Text_SomeonesKeys',
    "Keys left by a Game Corner machine indicate that its user plans to return.",'''
N~The keys have been promoted to a tiny and rather important seat-saving assistant.|
N~Personal belongings indicate somebody intends to return. They are not an invitation to investigate.|
N~Leave the keys where their owner expects them.|
N~I would hate to come back and find the one thing I needed to get home had moved.|
N~We can respect the place without touching the owner's belongings.|
N~The absent player has left a surprisingly consequential stand-in.|
N~A small object is doing the important work of being exactly where it was left.|
N~Changing their position would add an unnecessary problem for somebody else.|
N~A little ring of metal is keeping a person's next doorway within reach.|
N~There is no need to make a stranger's afternoon harder just because they stepped away.|
N~I wonder whether they remembered where they left those the moment they reached the door.
''')
add('poster_switch','CeladonCity_GameCorner_Text_SwitchBehindPosterPushIt',
    "A hidden switch is discovered behind the Game Corner poster and activated.",'''
U~The poster was doing considerably more work than looking decorative.|
S~The concealed switch confirms that the display was also hiding an access mechanism.|
N~A secret entrance in a public room. Stay alert.|
N~The familiar-looking wall feels different now that we know something was hidden there.|
N~We should think about where the passage leads before hurrying into it.|
S~An innocent piece of scenery has disclosed its second profession.|
N~A very thin layer of normality was covering something less ordinary.|
S~A concealed control is easier to understand now that we can see what it operates.|
N~A flat bright picture has acquired a dark little depth.|
N~The deliberate concealment is more interesting than the poster's sales pitch.|
N~I wonder how many people looked straight at that wall without noticing what it was protecting.
''')
add('photo_ready','CeladonCity_GameCorner_Text_PrintIsReadyCheckTrainerCard',
    "The Pokemon printer completes a print on the player's Trainer Card.",'''
S~Our card has acquired a little more company without getting any harder to carry.|
S~The printer reports completion. We can check the resulting image directly on the card.|
S~Done. Have a look before putting the card away.|
S~A small familiar image can make an ordinary card feel much more personal.|
S~A nice little keepsake does not have to be elaborate.|
S~The travelling cast has received its official pocket-sized promotional portrait.|
S~A whole companion reduced to a little image, without losing the reason we like seeing it.|
S~A compact print on an existing card is a neat practical format.|
S~A small likeness has found a place among the ordinary things we carry.|
S~A personal detail makes the card feel more like its owner's.|
S~I like pictures that stay close through ordinary days instead of only appearing for an occasion.
''')
add('photo_money','CeladonCity_GameCorner_Text_DontHaveEnoughMoney',
    "The Pokemon printer cannot be used because the player lacks the fee.",'''
N~The little photo opportunity has reached the practical end of our pockets.|
N~The payment condition is unmet, so the print has not been produced.|
N~No print today. We can leave it for later.|
N~A disappointing little pause, but the picture does not have to happen right now.|
N~Keep the money for what we need before chasing a keepsake.|
N~The promotional portrait has been delayed by a very small production budget.|
N~A missing fee is allowed to remain a reason to do something else.|
N~The printer needs the payment before its process can begin.|
N~A wanted little image can wait without losing the life it would have shown.|
N~No need to make a small extra feel like an urgent omission.|
N~We still have the real company beside us, even without a new picture on the card.
''')
add('magazine_shelf','LavenderTown_VolunteerPokemonHouse_Text_PokemonMagazinesLineShelf',
    "Pokemon magazines line a shelf at the volunteer Pokemon house.",'''
S~A whole shelf of reading for people whose favourite subject is already wandering around the room.|
S~A collection of specialist magazines can preserve a wider range of interests than one reference book.|
S~A good way to spend a quiet few minutes here.|
S~I like a room with things to read while familiar lives carry on nearby.|
S~A comfortable place needs small pleasures as well as the practical care.|
S~The residents have acquired an admirably enthusiastic periodical section.|
S~A shelf of old magazines can make waiting feel like somewhere to be.|
S~Different issues could show how information and interests changed over time.|
S~Small printed worlds have gathered beside the living ones.|
S~The shelf makes the room feel used rather than merely furnished.|
S~I wonder which issue people keep picking up even after they have read it before.
''')
add('copycat_secrets','SaffronCity_CopycatsHouse_2F_Text_MySecrets',
    "A personal note lists Copycat's mimicry, doll collecting, and fondness for Clefairy.",'''
S~A very small set of secrets, most of which the dolls were already cheerfully giving away.|
N~The note offers a selected self-description. It does not claim to explain the whole person.|
N~We have read enough. No need to rummage for anything more personal.|
S~It is sweet to see the ordinary favourite things behind all that confident imitation.|
S~A few things someone enjoys can make an unfamiliar room feel like theirs.|
S~The self-authored character sketch is brief, clear, and rather well supported by the scenery.|
S~The alleged secrets have left a remarkably visible trail of soft evidence.|
S~The interests are specific enough to remember without needing to turn them into a theory.|
S~A little list has given the room's scattered things a familiar centre.|
S~Her own choices say more than someone else deciding she is merely a clever trick.|
S~I wonder which of those favourites she would spend longest talking about if we asked her.
''')
add('bucket_game','SaffronCity_CopycatsHouse_2F_Text_MarioWearingABucket',
    "A game on display features Mario wearing a bucket on his head.",'''
L~The hero has apparently solved a hat shortage in the most resourceful possible way.|
S~An unusual silhouette is certainly an effective way to make a game memorable.|
S~A ridiculous little detail can be a perfectly good reason to enjoy something.|
S~I like that somebody kept a game with such a specific silly image.|
L~The bucket was probably not expecting a career in heroic headwear.|
S~The leading man has made a bold and highly practical costume choice.|
S~Dignity has stepped out while the bucket handles the scene.|
S~Improvised equipment is entertaining when it works in a world built for it.|
S~A very ordinary object has wandered into a much less ordinary story.|
M~An accessory with unmistakable confidence and absolutely no restraint.|
S~I wonder how long it takes before the strange little design starts feeling entirely normal.
''')
add('captain_book','SSAnne_CaptainsOffice_Text_HowToConquerSeasickness',
    "The captain is reading a book about conquering seasickness.",'''
N~Even the captain has a problem the captain's hat cannot fix on its own.|
S~Seeking information about a difficulty is sensible, regardless of professional experience.|
N~No shame in looking for help with something that keeps troubling him.|
N~It must be tiring to struggle with the very place people expect him to feel most at home.|
N~An ordinary bit of help can matter more than trying to look unbothered.|
S~The seasoned captain's reading list has revealed a thoroughly human complication.|
N~Expertise does not come with a guarantee of comfort. An inconvenient omission.|
S~A reference book is a practical response to a recurring problem.|
N~A person can know the sea well and still find its movement unkind.|
N~Being accomplished should not mean having to hide every difficulty.|
N~I wonder whether he feels more relieved by useful advice or simply knowing other sailors struggle too.
''')
add('captain_trash','SSAnne_CaptainsOffice_Text_YuckShouldntHaveLooked',
    "Looking into the captain's bin proves unpleasant.",'''
A~My curiosity has filed an immediate apology to my nose.|
N~An avoidable investigation has produced an entirely unsurprising reason to stop investigating.|
N~Enough looking. Step back and leave the bin alone.|
F~Some discoveries really do work better as things we never found out.|
N~Fresh air seems like a much better next activity.|
N~The investigation has received a decisive and deeply unappealing closing argument.|
A~A private little abyss has answered the question nobody needed to ask.|
N~Observation complete. No further sampling is remotely necessary.|
N~Some lids are kind enough to hide precisely what they ought to.|
A~A valuable lesson in resisting the impulse to look at absolutely everything.|
N~I would be content to remember the room through any other detail.
''')
add('island_gems','ThreeIsland_House1_Text_RareRocksGemsDisplayed',
    "A Three Island house displays rare rocks and gems.",'''
S~Somebody has brought home a very sparkly selection of things the ground was keeping.|
S~A mineral collection can reward close observation of differences in colour and structure.|
S~Look carefully without touching. Those pieces matter to their owner.|
S~I like seeing a room arranged around something a person simply enjoys noticing.|
S~A collection gives ordinary days a reason to keep looking closely at the world.|
S~The house has lent part of itself to a small exhibition of the earth's better flourishes.|
S~A handful of quiet stones can make a surprisingly personal room.|
S~The shapes and surfaces would be interesting to compare under the same light.|
S~Small old pieces of the world have been gathered into one person's care.|
S~The display makes each piece feel chosen rather than merely expensive.|
S~I wonder whether the owner remembers where each one was found.
''')
add('pippi_letter','VermilionCity_House3_Text_DearPippiLetter',
    "A letter hopes for a reunion, worries about Rocket trouble in Saffron, and reports safety in Vermilion.",'''
N~A small hello from far away has made room for worry and a little reassurance.|
N~The letter distinguishes a report about Saffron from the writer's impression of safety in Vermilion.|
N~People keeping each other informed matters when a place is in trouble.|
N~The hope of seeing someone soon feels especially tender beside the worry.|
N~An ordinary message can mean a lot when someone is wondering whether a friend is safe.|
N~A brief personal letter has carried the wider trouble directly into an otherwise quiet room.|
N~Distance makes even a plain assurance of safety feel worth writing down.|
N~We should remember this is the writer's report, not a guarantee about every place mentioned.|
N~A few words are trying to make the space between two people feel less uncertain.|
N~The personal greeting makes the news feel much closer than a public notice would.|
N~I wonder how many times the recipient reads the part about seeing each other again.
''')
add('club_listening','VermilionCity_PokemonFanClub_Text_ListenPolitelyToOtherTrainers',
    "A Fan Club notice asks members to listen politely to other trainers.",'''
S~A club full of favourite stories needs a few people remembering to leave room for the next one.|
S~Reciprocal attention makes a shared-interest conversation more informative and enjoyable.|
N~Let other people finish. Simple enough.|
S~It is easier to share something you love when someone actually lets you say it.|
S~A good gathering has room for more than the person with the loudest story.|
S~The house rules have sensibly protected the audience from becoming a permanent occupation.|
S~Listening is a useful contribution for people with no story prepared.|
S~Taking turns keeps one enthusiastic participant from occupying the whole conversation.|
S~A room grows warmer when every small voice has somewhere to land.|
S~Good manners make enthusiasm much easier to enjoy.|
S~I wonder what lovely little story gets missed whenever the loudest admirer keeps talking.
''')
add('club_bragging','VermilionCity_PokemonFanClub_Text_SomeoneBragsBragBack',
    "A Fan Club notice recommends answering another person's bragging with some of one's own.",'''
L~The club has installed a competitive boasting system. I hope the chairs are sturdy.|
N~That may keep a conversation energetic, though it could also become a competition for attention.|
N~A little pride is fine. Do not drown out the other person.|
N~I would rather people enjoy sharing than worry about having a better story.|
S~A friendly bit of showing off can be fun if everyone still feels welcome.|
M~An official invitation to escalate the anecdote. The club knows its audience.|
S~Mutually assured exaggeration has apparently become a social policy.|
N~It works best if both people are enjoying the exchange, not defending their place in it.|
N~Two bright stories need not burn each other out to fill the room.|
S~A little playful rivalry is charming when nobody mistakes it for a ranking of people.|
S~I wonder how quickly two ordinary favourite-Pokemon stories turn into something magnificent here.
''')
add('report_trade_evolution','SilphCo_5F_Text_SomeMonsEvolveWhenTraded',
    "A Silph report records that some Pokemon evolve through trading.",'''
S~An exchange can contain a rather bigger surprise than the two trainers first bargained for.|
S~The report identifies trading as an evolutionary condition for some species, not all of them.|
N~Worth understanding before agreeing to a trade.|
S~It must feel extraordinary to watch a familiar companion change during that handover.|
N~A thoughtful exchange should make room for what happens to the Pokemon afterward.|
S~The research report has found a way for a handover to become a transformation scene.|
S~A change of company can apparently arrive with a change of shape.|
S~Interesting trigger. Comparing affected species could tell researchers more about the process.|
S~A threshold between two hands can also become a threshold between forms.|
N~It is important information for somebody choosing whether to trade a companion.|
S~I wonder how surprised the first trainers to see that happen must have been.
''')
add('report_moves','SilphCo_5F_Text_Over350TechniquesConfirmed',
    "A Silph report lists more than three hundred and fifty confirmed Pokemon techniques.",'''
U~That is a very large list of things a Pokemon might do while we are still deciding what to expect.|
S~A confirmed catalogue represents substantial observation; its size is not a reason to stop revising it.|
N~Plenty to learn. Start with what our own team needs.|
N~A number that large makes me grateful nobody expects us to learn it all this afternoon.|
S~The world has enough variety to keep a curious person busy for a long time.|
S~The repertoire has grown beyond any sensible one-evening performance.|
S~A reassuring amount of the world remains too busy to fit neatly in my head.|
S~Organizing that many observations into something usable is a significant job in itself.|
S~A long list can still be only the edge of what living things know how to do.|
S~The impressive part is all the patient confirmation behind the number.|
S~I wonder which discovery made the researchers realize the catalogue was much bigger than they expected.
''')
add('report_porygon','SilphCo_5F_Text_PorygonFirstVRMon',
    "A research report credits Pokemon Lab with creating Porygon, a virtual-reality Pokemon.",'''
U~Somebody's research became a whole Pokemon. That is considerably more exciting than finishing a report.|
S~A created Pokemon raises fascinating questions beyond the technical achievement of making it.|
N~Creating a life means taking responsibility for what happens to it.|
N~I would like to know what the people who made it noticed when it first responded.|
N~An extraordinary beginning still needs ordinary care afterward.|
S~The laboratory has crossed the impressive distance between describing a character and introducing a life.|
S~A manufactured beginning does not make the being that follows less worth knowing.|
U~That is an astonishing piece of engineering. I would have a notebook full of questions.|
N~A life can begin in an unfamiliar place and still belong fully to itself.|
S~I would rather meet Porygon than only admire the people taking credit for it.|
S~I wonder which small moment first made the researchers see a companion instead of a project.
''')
add('record_blank','SixIsland_WaterPath_House1_Text_BlankChartOfSomeSort',
    "An empty chart has spaces intended for recording measurements.",'''
S~A chart patiently waiting for somebody to introduce a suitably impressive bug.|
S~A prepared record sheet turns future observations into something that can be compared consistently.|
N~Blank for now. No need to fill it with guesses.|
S~I like seeing the little space people leave for things they have not found yet.|
S~An empty page can make a hobby feel like it has somewhere to grow.|
S~The record has built its stage and is awaiting the first extraordinary contestant.|
S~An absence of numbers is occasionally the most honest set of numbers available.|
S~A consistent format is a good start. Measurements still need a clear method.|
S~A few empty boxes have made room for an unknown future.|
S~It is nice to see enthusiasm given a tidy place to keep track of itself.|
S~I wonder what the first entry will look like beside the last one somebody eventually adds.
''')
add('record_heracross','SixIsland_WaterPath_House1_Text_BiggestHeracrossIsXSize',
    "A chart records the largest Heracross measured so far.",'''
S~A bug has earned itself a place on the wall without having to climb the wall.|
S~The wording correctly limits the record to what has been observed so far. That distinction matters.|
S~A useful record. It does not need to make every smaller Heracross feel like a disappointment.|
S~I like imagining the excited little moment when somebody wrote that measurement down.|
S~A hobby can give an otherwise ordinary day something specific to remember.|
S~The reigning champion has been preserved in the surprisingly modest form of a measurement.|
S~A number on a chart is a very small monument to a rather particular enthusiasm.|
S~Keeping the record makes later comparisons possible instead of relying on an excited memory.|
S~One encountered life has left a careful little mark among the numbers.|
S~A record is charming when it stays a shared delight rather than a judgment of everything else.|
S~I wonder what the room sounded like when that record was first broken.
''')
add('box_breeze','SevenIsland_House_Room1_Text_SlightBreezeAroundBox',
    "A slight breeze can be felt around a box in the Seven Island house.",'''
N~An ordinary box has developed a rather interesting relationship with the air.|
N~The airflow is observable. Its source is not established by noticing it alone.|
N~Notice it without pulling the house apart. We are guests.|
N~A tiny unexpected detail can make an otherwise familiar room feel different.|
N~We can mention it to the person who lives here rather than start moving their things.|
S~The unassuming prop has supplied a very quiet suggestion of something beyond it.|
N~An excellent small mystery to avoid solving with somebody else's furniture.|
N~Airflow could indicate a gap. That does not authorize an improvised inspection of the wall.|
N~A little breath of elsewhere has found the edge of the room.|
N~Curiosity can remain polite even when it notices something tempting.|
S~I wonder whether the owner stopped noticing that breeze long ago.
''')
add('warehouse_second_password','FiveIsland_Meadow_Text_EnteredPasswordAnotherNeeded',
    "One warehouse password is entered, but a second is still required.",'''
N~Half a secret is apparently not enough to persuade the whole door.|
N~The first credential has been supplied, but the second required condition remains unmet.|
N~Still locked. We need the other password.|
N~It is a little frustrating to be closer without being through.|
N~We can keep the known part without trying to force the missing one.|
N~The entrance has accepted the opening line and declined to begin the scene without the second.|
N~A door has found an impressively literal way to demand more information.|
N~Two-part access checks need both parts. Repeating the first will not add the second.|
N~One small tooth of the key has found its place; the rest is still absent.|
N~A partial success is useful information, even when it is not yet a welcome.|
N~I wonder how much confidence the guards place in people never learning the two pieces together.
''')
add('warehouse_open','FiveIsland_Meadow_Text_WarehouseDoorAlreadyOpen',
    "The warehouse door is already open.",'''
N~The warehouse has run out of door-related objections. We should still watch what is past it.|
N~The entrance state is clear. An open door does not establish the safety of the interior.|
N~Open. Stay alert when we enter.|
N~A barrier being gone can make the next part feel more real.|
N~Worth checking our readiness before turning an opening into a rushed entrance.|
N~The obstacle has retired from its role, leaving the rest of the scene unresolved.|
N~An open threshold is not necessarily a friendly one.|
N~Access and safety are separate questions. We have answered only the first.|
N~A shut place has given up its boundary, not all its secrets.|
N~We can appreciate progress without behaving as though the whole problem is finished.|
N~I would pay as much attention to what lies beyond as we did to what kept us outside.
''')
add('dotted_open','SixIsland_RuinValley_Text_DoorIsOpen',
    "The ancient door in Ruin Valley is open.",'''
S~The old doorway has finally stopped answering every question with a wall.|
N~The opening provides access, but it does not by itself explain the structure beyond.|
N~Take a careful look before moving farther in.|
S~A place feels different once its entrance is no longer only something to stare at.|
N~A slow first step is sensible in an unfamiliar ruin.|
S~The setting has finally granted the visitor more than a view of its exterior.|
S~A threshold has changed its mind after a very long silence.|
N~We can learn more by observing the entrance than by rushing through it.|
S~The dark little space beyond has become somewhere we can approach.|
S~It is satisfying to see an obstacle become an invitation.|
S~I wonder which detail inside will make the most sense of what we saw on the door.
''')
add('dotted_decline','SixIsland_RuinValley_Text_LeftDoorAlone',
    "The player decides not to investigate the strange door further.",'''
N~The door can keep its quiet mystery for a little longer. We have other footsteps available.|
N~Deferring an inspection is reasonable when we are not ready to interpret what we find.|
N~Leave it for now. Curiosity does not set the schedule.|
S~I like knowing we can be interested without having to press farther immediately.|
N~There is time to return with a clearer head and a better plan.|
N~The suspense has been left intact by the perfectly legitimate decision to walk away.|
S~An unanswered question can survive being given the afternoon off.|
N~A pause avoids making an irreversible guess just to satisfy the urge to act.|
S~Some thresholds are kind enough to wait where we found them.|
N~Walking away can be a deliberate choice rather than a failure of nerve.|
S~I wonder what we will notice differently if we come back after thinking about it.
''')
add('cardkey_open','Text_CardKeyOpenedDoor',
    "The Card Key successfully opens a Silph security door.",'''
S~A little card has settled an argument that the whole door was winning.|
N~The key has satisfied the access control and the door has opened.|
N~Through this one. Keep an eye on the next room.|
S~It is a small relief when the thing you found fits the problem in front of you.|
N~A useful tool is a good reason to remember where we put it.|
S~The imposing barrier has accepted a rather understated credential.|
S~A very small rectangle has out-argued a very large panel of metal.|
S~The access system has responded as expected. Useful to confirm.|
S~A little carried thing has made a wall remember it was a doorway.|
S~A clean solution has its own quiet satisfaction.|
S~I wonder how ordinary that little success feels to the people who used to work here every day.
''')
add('cardkey_missing','Text_ItNeedsCardKey',
    "A Silph security door remains locked without a Card Key.",'''
N~The door has a very particular opinion about which flat little object counts as a greeting.|
N~The required credential is absent. Force is not a substitute for identifying the access method.|
N~We need the key. Keep looking carefully.|
N~It helps to know what the barrier actually needs instead of guessing at it.|
N~We can work out the next step without making this one into a wrestling match.|
N~The gatekeeper has no lines beyond its inflexible request for proper identification.|
N~A locked door has made its demands admirably specific.|
N~Look for the intended credential rather than testing the strength of the mechanism.|
N~A thin piece of absence is keeping a thick door closed.|
N~At least the problem is clearer than simply being told we cannot go through.|
N~I wonder who last carried the key that should fit this part of the building.
''')
add('card_door_open','Text_TheDoorIsOpen',
    "The inspected security door is already open.",'''
S~One less door trying to become a separate chapter of our afternoon.|
N~The access barrier is already resolved. We can focus on the route beyond it.|
N~Clear passage. Keep moving carefully.|
S~It is nice when checking something confirms there is no new problem waiting.|
N~A clear route is useful, especially when the team needs a simple way back.|
S~The scenery has courteously declined to supply another obstacle.|
S~An ordinary open door can be surprisingly reassuring after enough locked ones.|
N~Worth noting the route while it is unobstructed.|
S~A space has remained open long enough to feel like a little kindness.|
N~There is no need to make an easy part harder just because we expected trouble.|
S~I wonder how different the building will feel when open doors are ordinary again.
''')
add('machine_adjustment','OneIsland_PokemonCenter_1F_Text_MachineUnderAdjustment',
    "The Network Machine display reports that adjustment work is still in progress.",'''
N~The machine has announced that it is having a work-in-progress sort of day.|
N~The display reports an incomplete adjustment state. It does not claim normal operation.|
N~Leave the work to the person handling it. No reason to hurry the equipment.|
N~I appreciate a plain message that admits the job is not done yet.|
N~A careful finish is worth more than pretending something is ready.|
N~The impressive apparatus has issued a modest request for more time backstage.|
N~A machine has found an honest way to say not yet.|
N~A visible status helps people understand what is happening without interfering with the work.|
N~The lights have not quite settled into their finished pattern.|
N~Work in progress is a respectable state to acknowledge instead of hiding it.|
N~I wonder which small adjustment will make the operator finally step back looking satisfied.
''')
add('machine_first_link','OneIsland_PokemonCenter_1F_Text_MachineLinkedWithKanto',
    "The Network Machine display reports its first established connection.",'''
S~A very plain status message with a considerable amount of work hiding behind it.|
S~The display now confirms a connection rather than merely describing an adjustment in progress.|
S~Good. The work has a clear result to show.|
S~I like the little relief in seeing something complicated finally say it is working.|
S~Somebody has earned the chance to stop watching the equipment anxiously for a moment.|
S~The grand technical effort has chosen a remarkably restrained announcement of success.|
S~A difficult little triumph has arrived wearing an ordinary status line.|
S~A confirmed state is useful. It gives the operator something definite to test from.|
S~A patient effort has found one clear answer among its lights.|
S~It is satisfying when a result does not need a complicated explanation to be noticed.|
S~I wonder how many earlier attempts the operator remembers while looking at that same message.
''')
add('machine_second_link','OneIsland_PokemonCenter_1F_Text_MachineLinkedWithKantoAndHoenn',
    "The Network Machine display reports an additional established connection.",'''
S~Another successful line on the display. Complicated work can look wonderfully small once it succeeds.|
S~The status indicates that an additional part of the planned connection is now established.|
S~More progress, properly confirmed. Good work by the people doing it.|
S~It feels good to see a long effort become something the display can state so calmly.|
S~I hope the people behind that result give themselves time to enjoy finishing it.|
S~The technical epic has concluded another chapter in the least dramatic typeface available.|
S~A second quiet confirmation can carry a surprising amount of relief.|
S~An additional working connection means another clear result to verify, not just a hopeful plan.|
S~A careful labour has gathered another little light into its finished shape.|
S~The modest display makes the achievement feel rather sincere.|
S~I wonder which person first noticed the confirmation and called the others over to see.
''')
add('dojo_sides','SaffronCity_Dojo_Text_EnemiesOnEverySide',
    "A Dojo slogan warns of enemies on every side.",'''
N~A very energetic way to make standing in the middle of a room feel complicated.|
N~As a training slogan, it encourages awareness. Taken literally all the time, it would be exhausting.|
N~Stay aware. No need to turn every stranger into an enemy.|
N~I would rather leave the room more attentive than more afraid of people.|
N~A useful lesson should leave some room for a peaceful meal afterward.|
N~The training hall has declined to give the protagonist a single convenient direction to face.|
N~An excellent slogan for ensuring the shoulders never get a day off.|
N~Awareness is useful when it helps distinguish actual threats from ordinary surroundings.|
N~A person can watch the path without teaching every shadow to wear a hostile face.|
N~Alertness looks better when it leaves room for good judgment.|
N~I wonder whether the instructor explains the difference between readiness and suspicion.
''')
add('dojo_return','SaffronCity_Dojo_Text_GoesAroundComesAround',
    "A Dojo slogan says that what goes around comes around.",'''
S~A slogan with enough room for consequences, kindness, and the occasional badly aimed kick.|
N~Actions often affect future interactions, though the phrase is not a guarantee of perfect fairness.|
N~Treat people decently even when nobody promises a reward for it.|
S~I like the idea of giving the next person something kind to carry onward.|
S~A small good turn can travel farther than the person who began it notices.|
S~The hall has supplied a compact theory of consequences with a nicely circular structure.|
N~A comforting thought, provided we do not mistake every misfortune for something deserved.|
N~Feedback matters. So does remembering that real situations are more complicated than a slogan.|
S~What we set loose in the day may find another doorway than the one we expect.|
N~A good reminder to think beyond the instant of getting what we want.|
S~I wonder which experience made that phrase worth putting where students would see it every day.
''')
