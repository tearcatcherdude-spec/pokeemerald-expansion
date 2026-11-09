"""Kanto interior continuation; exact terminal speech, with no runtime inference."""
ROWS=[]
EMOTIONS=dict(N='neutral',S='soft_smile',A='annoyed',F='flustered',D='sad',U='surprised',M='smug',L='laughing')
def add(key,labels,subject,lines):
    replies=[]
    for line in lines.strip().split('|'):
        line=line.strip()
        if len(line)>1 and line[1]=='~' and line[0] in EMOTIONS:
            line=EMOTIONS[line[0]]+line[1:]
        replies.append(line)
    assert len(replies)==11,(key,len(replies))
    ROWS.append(dict(key='kanto_if_'+key,labels=labels.split(),subject=subject,replies=replies))

add('coin_exchange_info','CeladonCity_GameCorner_Text_CanExchangeCoinsNextDoor',
    'The Game Corner clerk directs coin holders to the prize room next door.','''
N~Coins here, prizes next door. The building has divided temptation into departments.|
N~The exchange counter is separate from the games. Useful to know before wandering.|
N~Check what a prize costs before spending anything.|
N~A clear direction is helpful in a place this busy.|
N~Worth knowing what the coins are for before buying them.|
M~The first act sells the coins; the neighboring stage displays the rewards.|
N~The little metal circles have their own destination.|
N~Separate service counters. Follow the signs before queuing.|
N~One door offers chances, the next gives those chances a price.|
N~They have made browsing the prizes a separate little trip.|
N~I wonder how often visitors check the prize list first.
''')
add('coins_declined','CeladonCity_GameCorner_Text_ComePlaySometime',
    'The coin clerk politely closes the conversation when we decline to buy coins.','''
N~We can leave with exactly the same number of coins and fewer decisions.|
N~Declining the purchase ended the transaction without complication.|
N~Good. No need to buy just because we asked.|
S~They accepted the answer without making it uncomfortable.|
N~We can save the money for something we actually planned to get.|
N~A commercial invitation survives our polite refusal.|
N~A small no, allowed to remain small. Appreciated.|
N~Purchase canceled. No unnecessary steps afterward.|
N~The door remains open without pulling us through it.|
N~A courteous response to a customer deciding against something.|
N~I wonder how many people come in just to look around.
''')
add('coins_no_case','CeladonCity_GameCorner_Text_SorryDontHaveCoinCase CeladonCity_GameCorner_Text_DontHaveCoinCase',
    'The attempted coin transaction cannot proceed without a Coin Case.','''
N~The coins require their own luggage. Ordinary pockets have apparently not qualified.|
N~A missing Coin Case prevents the transfer. No coins were received through this branch.|
N~No case, no coins. We can move on.|
N~At least they explained what was missing instead of leaving us guessing.|
N~Another thing to settle before deciding whether to play.|
N~The proposed transaction has failed its container inspection.|
N~Small pieces of metal have surprisingly specific housing requirements.|
N~Required container missing. Clear, recoverable error.|
N~The little things need their own place to gather.|
N~A useful limit to learn before handing over money.|
N~I wonder where visitors usually get their first Coin Case.
''')
add('coins_case_full','CeladonCity_GameCorner_Text_CoinCaseIsFull',
    'The coin clerk cannot sell coins because the Coin Case is full.','''
N~The case is full. A rare moment when the container firmly ends the shopping.|
N~The purchase exceeded available capacity and did not proceed.|
N~We already have enough to fill the case. Stop there.|
N~That makes the decision rather simple for now.|
N~No reason to spend more while the existing coins have nowhere else to go.|
N~The final authority on the purchase turns out to be a very small box.|
N~A useful refusal from an inanimate accomplice.|
N~Capacity reached. Adding more is not currently an option.|
N~Even a little box can say quite a firm no.|
N~The case has reached its limit. We can respect ours too.|
N~I wonder how long it took to fill that much space.
''')
add('coins_too_costly','CeladonCity_GameCorner_Text_CantAffordCoins',
    'The coin clerk refuses the purchase because we cannot afford it.','''
N~The money has voted against this particular plan.|
N~The purchase did not occur because the funds were insufficient.|
N~Leave it. We have other things to spend money on.|
N~An awkward answer, but a clear ending.|
N~Better to keep what we have for the team's needs.|
N~The budget has exercised its veto over the evening's entertainment.|
N~A closed purse can be an unexpectedly sensible adviser.|
N~Insufficient funds. Changing priorities is easier than changing arithmetic.|
N~A little less money can make the next choice clearer.|
N~No need to turn a declined purchase into a personal challenge.|
N~I wonder how often people spend more here than they meant to.
''')
add('coins_bought','CeladonCity_GameCorner_Text_HereAreYourCoins',
    'The clerk confirms the paid coin purchase has completed.','''
N~Coins acquired. A budget is still a useful companion to bring along.|
N~That was a paid exchange, not a gift. The coins are now available.|
N~Bought what we asked for. Keep track of what we spend from here.|
N~The transaction is settled. We can take a moment before doing anything else.|
N~A planned limit is easier to keep when we remember it at the start.|
N~Our money has changed costume and become local currency.|
N~Different little circles, same reason to be careful with them.|
N~Exchange complete. Useful to record the actual cost, not just the coin count.|
N~The numbers have moved from one place to another.|
N~A clear handoff. The important part is remembering what those coins cost.|
N~I wonder which purchase option most visitors choose.
''')
add('rocket_rumor','CeladonCity_GameCorner_Text_RumoredTeamRocketRunsThisPlace',
    'A player whispers a rumor that Team Rocket operates the Game Corner.','''
N~That rumor makes the cheerful lights feel considerably less cheerful.|
N~A serious claim, though still presented as a rumor. We should distinguish evidence from gossip.|
N~Keep alert. A rumor is not proof, but it is worth hearing.|
N~The way they lowered their voice makes the room feel different.|
N~We can be careful without making a scene.|
N~The bright establishment has acquired a rather darker alleged proprietor.|
N~A whisper can change the color of an entire room.|
N~Unverified ownership claim. Useful lead, not a final conclusion.|
N~Something unpleasant may be keeping time beneath all this noise.|
N~People whisper differently when they worry the subject might hear.|
N~I wonder what made them believe the connection.
''')
add('different_odds','CeladonCity_GameCorner_Text_ThinkMachinesHaveDifferentOdds',
    'A player suspects the slot machines have different odds.','''
N~A theory made of many little hopeful pulls, I suspect.|
N~Distinguishing different odds from random variation would require considerable evidence.|
N~Do not spend more just to prove a hunch.|
N~It must be tempting to think one seat has a better answer.|
N~A feeling is not a good reason to keep spending.|
N~The room has produced a hypothesis that is expensive to investigate badly.|
N~Chance is very good at wearing the face of a pattern.|
N~I would need records, not a streak and a suspicious glance.|
N~People find signs in spinning things when they want an answer.|
N~A different machine can still make the same promise without keeping it.|
N~I wonder whether she has tracked results or simply noticed a few runs.
''')
add('wins_come_go','CeladonCity_GameCorner_Text_WinsComeAndGo',
    'A player says wins are intermittent and nothing is guaranteed.','''
N~The machine has no appointment for the next happy outcome.|
N~An uncertain result remains uncertain after either a win or a loss.|
N~Good to remember before chasing a result.|
N~That sounds like something learned over several uneven afternoons.|
N~Knowing when to leave matters more than waiting for certainty.|
N~A remarkably honest review of an establishment full of promises.|
N~Nothing certain, except how quietly the time disappears.|
N~Unreliable output. Do not build an essential plan around it.|
N~A turning reel is not a promise moving toward you.|
N~A useful reminder, especially after a lucky moment.|
N~I wonder whether he finds it easy to follow his own advice.
''')
add('only_luck','CeladonCity_GameCorner_Text_WinOrLoseItsOnlyLuck',
    'A player attributes slot outcomes to luck.','''
N~The reels are not impressed by our heroic posture. Probably for the best.|
N~Chance does not become more favorable because the player feels more determined.|
N~Then do not treat losing like a challenge to push harder.|
N~It is worth remembering this is not a judgment of anyone's ability.|
N~A quiet limit matters more than trying to outwork the machine.|
N~The grand drama has no obliging author behind the next spin.|
N~The machine does not know whether you deserve a nicer afternoon.|
N~More confidence does not change a random process.|
N~Some doors open by chance, not because you knock more bravely.|
N~Good to separate the result from how clever or worthy someone feels.|
N~I wonder whether that makes the game easier for her to leave.
''')
add('hooked','CeladonCity_GameCorner_Text_SoEasyToGetHooked',
    'An older player worries about how easily games become compulsive.','''
N~A little fun can grow elbows and take over the whole afternoon.|
N~Repeated rewards can make stopping difficult even when enjoyment is fading.|
N~If it stops feeling like a choice, step away.|
N~He sounds less amused than the room around him.|
N~A break outside might make the next choice feel clearer.|
N~The warning comes from inside the spectacle, which gives it a certain weight.|
N~A bright room can hold you more tightly than a dark one.|
N~A stopping rule set in advance is more reliable than willpower mid-loop.|
N~Some invitations keep taking little pieces of your evening.|
N~He is noticing the feeling. I hope he gives himself permission to leave.|
N~I wonder whether he meant that as advice or an admission.
''')
add('coin_overflow_players','CeladonCity_GameCorner_Text_DontNeedMyCoins CeladonCity_GameCorner_Text_YouHaveLotsOfCoins CeladonCity_GameCorner_Text_YouveGotPlentyCoins',
    'A player declines to give more coins because our existing Coin Case is too full.','''
N~They inspected our supply and decided the tiny metal population was large enough.|
N~The intended transfer did not occur because existing holdings were already near capacity.|
N~We have plenty already. No need to ask for more.|
N~A reasonable answer. Their coins can stay where they are.|
N~We can be grateful for the thought without needing another handful.|
N~The patronage application has been rejected on the grounds of visible abundance.|
N~An unusually practical limit to roadside generosity.|
N~No remaining capacity. Avoid promising a transfer the container cannot accept.|
N~A full little case has settled the question for everyone.|
N~They have a point. More is not automatically better.|
N~I wonder whether many visitors already have that much when they ask.
''')
add('coin_target','CeladonCity_GameCorner_Text_NeedMoreCoinsForMonIWant',
    'A player says he still lacks enough coins for the Pokemon he wants.','''
N~A living prize can make one more try sound far too persuasive.|
N~A desired reward can encourage repeated spending beyond the original plan.|
N~Wanting the Pokemon does not make every extra spin worth it.|
N~He sounds close enough to hope and far enough to be frustrated.|
N~I hope he keeps enough aside for caring for the partner afterward.|
N~The promised arrival waits beyond a counter that keeps asking for another coin.|
N~It is unsettling to hear a companion described as a reason not to stop.|
N~Compare total cost with the goal. Sunk effort is not a discount.|
N~A wanted companion should not become a hole in the day.|
N~The prize is doing a lot of work to keep him in that seat.|
N~I wonder how long he has been saving toward that particular Pokemon.
''')
add('reels_advice','CeladonCity_GameCorner_Text_WatchReelsClosely',
    'A player claims close attention to the reels is the trick to winning.','''
N~My eyes can stare very hard. The reels have yet to be intimidated.|
N~Attention alone does not establish control over the outcome.|
N~A claimed trick is still a claim. Keep the spending limit.|
N~I would rather not turn this into a test of how intensely I can look.|
N~No trick is worth spending the team's supply money to verify.|
M~The oracle recommends a stern gaze at the spinning symbols.|
N~A machine can invite concentration without rewarding it.|
N~Need evidence that the input changes the result before optimizing the stare.|
N~Looking closely and seeing a path are not always the same thing.|
N~Confidence in advice does not tell us whether it works.|
N~I wonder what made him settle on that explanation.
''')
add('prizeroom_porygon','CeladonCity_GameCorner_PrizeRoom_Text_FancyThatPorygon',
    'A visitor wants Porygon but finds winning enough coins difficult.','''
S~Porygon has certainly caught their eye. The path to it sounds frustrating.|
N~The desired Pokemon is clear; the uncertain acquisition cost is the difficulty.|
N~Wanting one does not mean spending without a limit.|
N~It is hard when something fascinating is tied to an unreliable game.|
N~I hope they think about the partner's care as well as getting it.|
N~An unusual creature holds the spotlight while the coin counter delays the entrance.|
S~A strange little being behind an unusually ordinary barrier: enough money.|
U~Porygon is fascinating. The slots are a much less interesting engineering proposition.|
S~An unlikely creature can make a person linger a long time.|
N~A distinctive choice. I hope admiration does not become an endless bill.|
S~I wonder what first made Porygon stand out to them.
''')
add('prizeroom_winner','CeladonCity_GameCorner_PrizeRoom_Text_RakedItInToday',
    'A winner celebrates today\'s winnings and wishes every day were as lucky.','''
N~A lucky day can stay a lucky day without becoming tomorrow's business plan.|
N~One favorable session does not predict repeated returns.|
N~Good day to leave with what he has.|
S~He sounds delighted. I hope the memory can be enough without repeating it immediately.|
N~Enjoy the good result without spending it all trying to make it happen again.|
M~Today's applause has inspired ambitious plans for a permanent residency.|
N~A bright afternoon is not a promise the next one signed.|
N~Do not extrapolate from one unusually favorable test run.|
N~Good fortune is a visitor, not a tenant you can charge rent.|
N~The first half sounds happy. The second half is where expectations get expensive.|
N~I wonder whether he has decided what to do with the winnings.
''')
add('programmer','CeladonCity_Condominiums_3F_Text_ImTheProgrammer',
    'A developer introduces himself as the programmer.','''
S~A short introduction from somebody who probably spends all day fixing long problems.|
S~A demanding profession. The brief introduction may conceal a great many late nights.|
N~Sounds like careful work. Hope he gets breaks.|
N~He seems comfortable letting the job speak for itself.|
S~Every workplace has someone quietly keeping things running.|
S~The programmer enters, establishes his role, and wastes no dialogue.|
M~A wonderfully economical biography. I could learn from it.|
S~Excellent! I have questions about how he solves difficult bugs. Several questions.|
N~A person who teaches small rules to do large amounts of work.|
N~Clear introduction. He has probably spent his patience on less clear problems.|
S~I wonder what part of the work he enjoys most.
''')
add('graphic_artist','CeladonCity_Condominiums_3F_Text_ImTheGraphicArtist',
    'The graphic artist jokingly claims to have drawn us.','''
U~I hope he remembered my good side. It keeps moving around.|
M~An unusually personal way to introduce a visual arts specialty.|
N~Bold claim. At least he seems pleased with the work.|
F~I would be rather nervous about someone studying me that closely.|
S~He sounds proud of making something people recognize.|
M~An artist stakes a claim on our likeness with magnificent confidence.|
M~I would ask for a more rested version of me, given the opportunity.|
U~That is quite an introduction. I wonder how he handles the tiny details.|
N~An artist sees outlines the rest of us merely live inside.|
M~I trust he has given the hair the attention it deserves.|
S~I would be curious to see the sketches behind that claim.
''')
add('story_writer','CeladonCity_Condominiums_3F_Text_IWroteTheStory',
    'The writer introduces his role and enthusiastically praises Erika, Misty, and Sabrina.','''
M~He began with his job and ended with a very well-attended favorites list.|
N~His professional introduction has become a personal account of the characters he likes.|
N~He knows what he likes. Quite a lot of it, apparently.|
F~His enthusiasm runs ahead of the introduction. It is rather endearing.|
S~It is nice when somebody still enjoys the people they write about.|
M~A fellow writer whose discerning favorites list is rapidly becoming the entire cast.|
M~A brief biography with several enthusiastic footnotes.|
S~Personal investment in the work! A little unfocused, but unmistakable.|
N~He keeps finding one more name worth speaking warmly.|
M~Several favorites is perfectly acceptable. The rushed defense makes it funnier.|
S~I wonder what he most enjoys about writing them.
''')
add('designer_encouragement','CeladonCity_Condominiums_3F_Text_ImGameDesignerShowMeFinishedPokedex',
    'The designer encourages us to finish the Pokedex and return.','''
S~He has volunteered to be our very patient finishing-line audience.|
S~A long collection project benefits from encouragement that acknowledges the difficulty.|
N~We can keep at it at our own pace. The work is real.|
S~It helps when somebody recognizes the effort before it is finished.|
S~One encounter at a time is a more manageable plan than staring at the total.|
S~A future celebration has been penciled in, with considerable work between here and there.|
S~An unfinished thing is allowed to keep becoming.|
N~Large task, clear completion condition. Break it into smaller outings.|
S~A long book of names fills one meeting at a time.|
S~He wants us to come back with good news. A nice invitation.|
S~I wonder how many completed Pokedexes he has been shown.
''')
add('designer_complete','CeladonCity_Condominiums_3F_Text_CompletedPokedexCongratulations',
    'The designer congratulates us on completing the Kanto Pokedex before the diploma display.','''
U~Every one of those meetings adds up to this! That is a lot of hello.|
S~A completed regional record represents a substantial body of travel and observation.|
S~The team helped make that happen. They deserve the credit too.|
S~It is lovely to have the long effort recognized so plainly.|
S~That took patience. A proper celebration seems deserved.|
S~The sprawling collection finally receives its satisfying final full stop.|
S~A long trail of small discoveries has reached a whole shape.|
U~Complete! All those separate observations finally closing the checklist.|
S~So many little lives, each leaving a name in the same book.|
S~An achievement that carries much more work than the neat certificate can show.|
S~I wonder which encounter comes back to mind first at a moment like this.
''')
add('slots_profit_house','CeladonCity_House1_Text_SlotsReelInTheDough',
    'A resident boasts about profits from the slot machines.','''
N~Somebody is very happy about where the missing coins end up.|
N~The operator's revenue and the player's outcome are quite different perspectives.|
N~That money came from people on the other side of the machines.|
N~His delight makes the room feel rather cold.|
N~I keep thinking of the people who leave with less than they meant to spend.|
N~A candid review from the profitable side of the counter.|
N~A cheerful voice can make an unpleasant truth sound even worse.|
N~Reliable income for the operator does not imply reliable returns for customers.|
N~The spinning things always seem to know which house they belong to.|
N~That laugh tells us more about the business than the bright signs do.|
N~I wonder how many players hear this side of the story.
''')
add('pokemon_prize_shipments','CeladonCity_House1_Text_ShippedMonsAsSlotPrizes',
    'A worker reports shipping two thousand Pokemon as slot prizes.','''
U~Two thousand living creatures, reported like boxes of spare buttons. That feels awful.|
N~The scale is alarming, especially when the animals are discussed only as merchandise.|
A~Those are Pokemon. Not inventory to boast about moving.|
D~There is no warmth at all in how he says it.|
A~That many partners need care, not a cheerful shipping tally.|
N~An enormous number delivered with the emotional weight of an office invoice.|
D~A crowd of lives reduced to one tidy line in a report.|
N~At that scale, welfare cannot be an afterthought. His language gives me no reassurance.|
D~Thousands of small journeys, and nobody here names a single traveler.|
A~He sounds proud of the volume. I wish he sounded concerned about the Pokemon.|
N~I wonder where they came from and who is looking after them.
''')
add('poster_denial','CeladonCity_House1_Text_DontTouchGameCornerPoster',
    'A resident suspiciously denies that the Game Corner poster hides a switch.','''
M~A secret switch? We had not asked. Fascinating choice of detail.|
N~The unsolicited denial supplies a suspiciously specific lead.|
N~He has given us a reason to remember that poster.|
N~That sounded rehearsed in exactly the wrong way.|
N~An ordinary warning usually needs fewer details about the thing it denies.|
M~A magnificent failure of discretion. The secret has received directions to its own entrance.|
M~Nothing suspicious, delivered with several suspicious extras.|
N~Information leak through over-specific denial. Very poor security design.|
N~A hidden thing sometimes points at itself through the person guarding it.|
M~He has made the poster the most interesting object in the building.|
N~I wonder how many people were curious before he mentioned it.
''')
add('flute_hearing','CeladonCity_PokemonCenter_1F_Text_PokeFluteAwakensSleepingMons',
    'A visitor says the Poke Flute wakes Pokemon through a sound only they hear.','''
U~A concert with an audience we cannot quite join. Clever instrument.|
N~A sound beyond ordinary human hearing could explain a selective response.|
N~Useful to know. Wake a partner gently when there is time.|
S~An instrument that reaches a different kind of listener. That fascinates me.|
N~A practical way to help a sleeping partner when the team needs it.|
S~A melody reserved for an audience with rather different ears.|
S~A song can be present without being ours to hear.|
U~Selective acoustic response! I have several questions about the mechanism.|
S~Some notes enter rooms our ears never find.|
S~An unusual instrument with a very specific purpose.|
S~I wonder what its sound is like from a Pokemon's side.
''')
add('cycling_uphill_tired','CeladonCity_PokemonCenter_1F_Text_RodeHereFromFuchsia',
    'A cyclist is exhausted after riding uphill from Fuchsia.','''
N~The hill spent the entire journey arguing with their legs. They earned a sit.|
N~An uphill route explains the increased effort over the same distance.|
N~Rest before riding again. No prize for falling off tired.|
N~They sound relieved to have reached somewhere they can stop.|
S~A drink and a good seat must feel wonderful after that climb.|
N~The scenic route has delivered its bill in muscle fatigue.|
N~A road can feel much longer when it refuses to lie flat.|
N~Elevation gain is real work. Recovery belongs in the itinerary.|
S~The hill is behind them now. That is its own comfort.|
N~They made it. No need to make the recovery look glamorous.|
N~I wonder whether the view made any part of the climb feel easier.
''')
add('cycling_wish','CeladonCity_PokemonCenter_1F_Text_GoToCyclingRoadIfIHadBike',
    'A visitor wishes for a bike so they could visit Cycling Road.','''
S~A bicycle and a ready-made first outing. Half the dream is planned.|
N~A required piece of equipment is the current barrier to their preferred route.|
S~Good to have a place you want to go when the chance comes.|
S~I like how clearly they can imagine the day they want.|
S~A simple ride can be a very good thing to look forward to.|
S~The itinerary waits patiently for its missing pair of wheels.|
S~A small wish with a long road tucked inside it.|
N~Specific goal, specific prerequisite. A very workable plan.|
S~The road is already calling before there are wheels to answer.|
S~Knowing what you would actually do with a purchase is a good sign.|
S~I wonder whether they would start from the easy end or tackle the climb.
''')
add('restaurant_gossip','CeladonCity_Restaurant_Text_ManLostItAllAtSlots',
    'A diner gossips about another customer losing all his money at slots.','''
N~That sounds like somebody's bad day being served as table talk.|
N~The information may be accurate, but discussing him this way adds no help.|
N~He can probably hear. Let him eat without an audience.|
D~It feels unkind to hear his trouble discussed over a meal.|
N~A little privacy would be a better thing to offer than gossip.|
N~A stranger's misfortune has become the dining room's incidental entertainment.|
N~An ordinary meal is not improved by making somebody else's regret the centerpiece.|
N~Observation without compassion is not automatically useful information.|
N~Some sad stories travel too easily between nearby tables.|
N~People deserve a little dignity when their day has gone badly.|
N~I would rather hear from the man himself if he chooses to talk.
''')
add('safari_rules','FuchsiaCity_SafariZone_Entrance_Text_ExplainSafariZone',
    'The attendant explains the four zones, limited time, Safari Balls, and bait or rock tradeoffs.','''
N~Four zones, a time limit, and thirty chances. My wandering needs a little supervision.|
N~The limited resources and different habitats make planning important.|
N~Know the limits. Do not take frustration out on the Pokemon.|
N~There is a lot to remember. I would rather move gently and pay attention.|
N~A calm visit sounds better than turning every encounter into a scramble.|
N~An elaborate set of rules for an afternoon that still depends on wild creatures cooperating.|
N~A place full of life should be more than a race against a counter.|
N~Resource limits noted. Map the zones before spending the whole allowance wandering.|
N~Four places, many shy lives, and a clock that does not stop to watch them.|
N~Clear rules help. A little restraint is still our own responsibility.|
N~I wonder which zone most visitors overlook in their rush.
''')
add('safari_regular','FuchsiaCity_SafariZone_Entrance_Text_SorryYoureARegularHere',
    'The attendant apologizes for offering an introduction to someone already familiar with the Safari Zone.','''
S~We have graduated from explanation to familiar face. Very official.|
S~They adjusted the conversation once they understood we knew the rules.|
N~No harm done. A refresher is better than assuming everyone knows.|
S~A little awkwardness, kindly corrected.|
S~It is nice when a place starts feeling familiar enough for that mistake.|
M~Our credentials as repeat visitors have been accepted without an examination.|
S~A small recognition at the edge of a large reserve.|
N~Experience level clarified. Good to avoid redundant instructions.|
S~A doorway feels different when someone thinks you know the way.|
S~They corrected themselves politely. Easily forgiven.|
S~I wonder how many regular visitors they come to recognize.
''')
add('gate_thirst','Route5_SouthEntrance_Text_ThirstyOnGuardDuty Route6_NorthEntrance_Text_ThirstyOnGuardDuty Route7_EastEntrance_Text_ThirstyOnGuardDuty Route8_WestEntrance_Text_ThirstyOnGuardDuty',
    'A thirsty Saffron gate guard says the road is closed.','''
N~A closed road and an open thirst complaint. We have learned both priorities.|
N~The guard is refusing passage while mentioning a personal discomfort.|
N~Road is closed. No need to argue at the gate.|
N~It is frustrating to get so close and still have to stop.|
N~Standing guard all day must be tiring. Being turned back is tiring too.|
N~The city's entry policy has acquired an oddly beverage-shaped footnote.|
N~A small dry throat beside a much larger closed door.|
N~Access denied. The reason and the complaint seem poorly connected.|
N~The road ends for now in a person wishing for a drink.|
N~He sounds uncomfortable, but the directions are still no more helpful.|
N~I wonder what explanation the waiting travelers have been given.
''')
add('gate_tea_shared','Route5_SouthEntrance_Text_ThanksIllShareTeaWithGuards Route6_NorthEntrance_Text_ThanksIllShareTeaWithGuards Route7_EastEntrance_Text_ThanksIllShareTeaWithGuards Route8_WestEntrance_Text_ThanksIllShareTeaWithGuards',
    'After accepting Tea, the guard allows entry to Saffron and promises to share it with the other guards.','''
S~The tea has achieved impressive diplomatic reach. And he is sharing it.|
N~The guard accepted the tea, opened passage, and intends to distribute it to colleagues.|
S~We can pass now. Glad the other guards get a share.|
S~That sounded like genuine relief. The welcome feels warmer now.|
S~A gift passed along can improve more than one person's shift.|
M~A teacup has accomplished what a travel itinerary could not.|
S~One warm drink has found several people on long quiet shifts.|
S~A remarkably small intervention with a large route-planning effect.|
S~The closed way has opened with a little warmth between strangers.|
S~He remembered the others before the conversation even ended. Nice.|
S~I wonder whether the guards often share small comforts through the day.
''')
add('gate_greeting','Route5_SouthEntrance_Text_HiHowsItGoing Route6_NorthEntrance_Text_HiHowsItGoing Route7_EastEntrance_Text_HiHowsItGoing Route8_WestEntrance_Text_HiHowsItGoing',
    'Once access is allowed, the Saffron guard greets us casually.','''
S~A much friendlier checkpoint. My feet appreciate the shorter conversation.|
S~The interaction has become an ordinary greeting instead of an access dispute.|
S~All clear. Nice to hear a normal hello.|
S~It is easier to feel welcome when the first words are friendly.|
S~A simple greeting makes a familiar route feel a little more human.|
S~The former obstacle now contributes a pleasant line to the passing scene.|
S~The same doorway, a much gentler voice around it.|
N~Routine access restored. Friendly acknowledgment is a welcome extra.|
S~A familiar face at the gate, without the closed road between us.|
S~Casual suits him better than refusing people entry.|
S~I wonder how his shift has been going since the tea arrived.
''')
add('superrod_received','Route12_FishingHouse_Text_IfYouCatchBigMagikarpShowMe',
    'After giving the Super Rod, the enthusiast asks to see especially large Magikarp.','''
S~A splendid rod, with one very fish-shaped request attached.|
S~He has given us equipment and a specific observation he hopes we will bring back.|
S~Generous gift. Showing him an interesting catch seems fair.|
S~He sounds eager to share the excitement, not just hear a thank-you.|
S~A good gift can open the door to more conversations later.|
M~The new fishing partnership includes a standing invitation for outsized guest stars.|
S~He has a particular joy, and there is something charming about its size requirement.|
S~Useful equipment plus a measurable field challenge. Nicely defined.|
S~The river has been asked to send its largest little surprise.|
S~He knows exactly what would make his afternoon. Refreshingly specific.|
S~I wonder what his first enormous Magikarp looked like.
''')
add('superrod_refused','Route12_FishingHouse_Text_OhThatsDisappointing',
    'The younger fishing brother is disappointed when we decline his fishing interest.','''
N~Another future fishing companion has failed the enthusiasm interview.|
N~He hoped for shared interest, but the question allowed an honest negative answer.|
N~We do not have to like it to be polite.|
F~Disappointing someone that enthusiastic always feels more difficult than it should.|
N~He can still enjoy the water without recruiting every visitor.|
M~The proposed angling alliance has dissolved before its first expedition.|
N~A small disappointment can remain small if nobody insists on fixing it.|
N~Interest mismatch. No need to force compatibility.|
N~The river will still be there for the people who want its company.|
N~An honest answer is better than promising to enjoy a hobby for his sake.|
N~I wonder how long it takes before he asks the next visitor.
''')
add('superrod_return','Route12_FishingHouse_Text_TryFishingBringMeMagikarp',
    'The fishing enthusiast recommends trying different waters and repeats his request for giant Magikarp.','''
S~New water, new surprises. He still has one preferred surprise.|
S~Different habitats can change the available catches. His request remains quite specific.|
N~Try the rod where it makes sense. No need to rush a record.|
S~I like that he has more advice ready when we return.|
N~A little exploring can be worthwhile even without a record fish.|
M~The field assignment expands geographically while remaining firmly Magikarp-shaped.|
S~A familiar greeting, followed by the world's least concealed obsession.|
S~Sampling different habitats should give more varied results. Good advice.|
S~Each body of water keeps a different answer beneath its surface.|
S~He is persistent, but at least his directions are useful.|
S~I wonder which nearby water has produced his favorite catches.
''')
add('magikarp_record','Route12_FishingHouse_Text_LookForwardToGreaterRecords',
    'After rewarding a record Magikarp, the enthusiast invites us to break the record again.','''
S~He is delighted, and already imagining an even more alarming fish.|
S~The new record has been recognized and rewarded; further observations are optional.|
S~Good catch. No need to turn every outing into another record attempt.|
S~It is lovely when something we found makes another person that happy.|
S~We can enjoy this result before planning the next one.|
M~A record falls, the applause rises, and the sequel is immediately commissioned.|
S~The quiet water keeps producing reasons for his very loud joy.|
S~Benchmark updated. Future improvements should be measured against the new value.|
S~A little mark on the wall has moved farther than he expected.|
S~He knows how to make a shared hobby feel like an event.|
S~I wonder whether he tells everyone about the new record.
''')
add('magikarp_tie','Route12_FishingHouse_Text_HuhXSizeSameSizeAsLast',
    'The presented Magikarp ties the previous size record.','''
M~A perfect tie. The fish have agreed on a standard edition.|
N~The measurement equals the existing record rather than exceeding it.|
N~Still a good-sized catch. The record can wait.|
S~Matching something impressive is not a disappointing thing in itself.|
N~No need to make the fish larger to make the trip worthwhile.|
M~The reigning champion has acquired an identically proportioned rival.|
S~Two small lives have happened to arrive at the same little number.|
N~No improvement, but useful confirmation that the measurement is repeatable.|
S~A familiar mark has found a second visitor.|
N~A tie can still be interesting, even without a new prize.|
S~I wonder whether the two fish look as similar as their measurements.
''')
add('magikarp_smaller','Route12_FishingHouse_Text_HmmXSizeDoesntMeasureUp',
    'The presented Magikarp is smaller than the recorded best.','''
N~A smaller fish is still a complete fish. The ruler is not its whole biography.|
N~The measurement does not exceed the existing record. That is all the comparison establishes.|
N~No record today. The partner is not at fault for its size.|
N~I hope the catch still feels worthwhile to the person who brought it.|
N~A quiet outing can be good without producing the biggest thing.|
N~The understudy has failed to exceed the star's dimensions. A very narrow review.|
N~Not every living thing needs to become a superlative.|
N~Below benchmark. That does not make the specimen useless.|
N~A small body can carry a whole life quite comfortably.|
N~A fair measurement, but not the only reason to value the catch.|
N~I wonder what else distinguishes this one besides its length.
''')
add('magikarp_wrong_species','Route12_FishingHouse_Text_DoesntLookLikeMagikarp',
    'The enthusiast rejects a submitted Pokemon because it is not Magikarp.','''
M~An ambitious attempt to introduce a new category. The judge remains unmoved.|
N~The comparison is restricted to Magikarp. This submission does not qualify.|
N~Wrong Pokemon for the question. No need to bother it further.|
F~An easy mistake in the selection, perhaps. We can leave it there.|
N~He asked for one particular species. That is fair enough.|
M~The guest has arrived at an exceptionally exclusive fish show.|
N~A different creature has briefly been asked to fit a very specific silhouette.|
N~Input validation catches another mismatch. Good that he checks.|
N~The little contest has a narrow doorway.|
N~At least he declined without putting the Pokemon down.|
N~I wonder whether he gets hopeful every time someone opens a Poke Ball.
''')
add('fishing_gift_no_room','Route12_FishingHouse_Text_NoRoomForGift FuchsiaCity_House2_Text_YouHaveNoRoomForGift VermilionCity_House1_Text_NoRoomForNiceGift',
    'A fishing enthusiast cannot provide an intended gift because the bag is full.','''
N~The generosity is ready. The bag is considerably less ready.|
N~The gift transfer failed for lack of space; its contents should not be assumed received.|
N~Make room before asking him to try again.|
F~A kind offer, stopped by an awkwardly full bag.|
N~A little sorting would make the next visit easier.|
N~The benefactor's plans have collided with our portable collection of everything.|
N~A full bag can make a generous moment unexpectedly sad.|
N~Capacity failure. Resolve the container problem before repeating the transfer.|
N~Something offered cannot enter a place with no room left.|
N~The gift is still his to keep until we are prepared for it.|
N~I wonder which unnecessary thing has been taking up that last bit of space.
''')
add('fly_retreat','Route16_House_Text_ExplainHM02',
    'The woman in the secluded retreat explains Fly after giving it or on return visits.','''
S~A quiet retreat and a way to leave by sky. She has excellent taste in exits.|
S~Fly offers a useful travel option. Her explanation applies on later visits as well.|
S~A generous lesson. We can respect her quiet place in return.|
S~She wants a little privacy, and still made time to help us.|
S~We can put the move to good use without making her home a busy stop.|
S~The reclusive host has given us an unusually convenient departure route.|
S~A private place, and a gift that makes the wider world less far away.|
S~A transport upgrade from someone who has chosen to avoid the traffic. Elegant.|
S~A little hidden room has opened a way into the sky.|
S~Discreet and generous is a very good combination.|
S~I wonder whether flying is how she comes and goes from here.
''')
add('fly_no_room','Route16_House_Text_DontHaveAnyRoomForThis',
    'The retreat\'s resident cannot give HM02 because the bag is full.','''
N~A secret retreat discovered, a useful gift blocked by socks and supplies. Typical bag politics.|
N~The HM transfer did not happen. We need room before receiving it.|
N~Sort the bag, then ask again. No need to crowd her.|
F~We have made a quiet visit rather awkward.|
N~A little preparation would have made accepting the kindness easier.|
N~The promised convenience has encountered the least convenient part of our luggage.|
N~A small disc, a completely occupied bag. A disproportionate obstacle.|
N~Tiny object, insufficient capacity. Clear the buffer first.|
N~The way into the sky is waiting outside a very full pocket.|
N~A tidy bag would have been a better introduction.|
N~I wonder how rarely someone comes this far and cannot carry the gift home.
''')
add('gate_name_rater','Route11_EastEntrance_1F_Text_ManInLavenderRatesNames',
    'A traveler recommends Lavender\'s Name Rater for help with Pokemon nicknames.','''
S~Professional help for the moment you run out of names before running out of Pokemon.|
N~An outside opinion can help with naming, though the trainer's own preference still matters.|
N~Useful lead. A name should still suit the partner living with it.|
S~I find names difficult. It is reassuring that someone enjoys helping with them.|
S~A little thought now can make the name pleasant to use every day.|
M~Lavender employs a critic for the smallest creative decisions with the longest afterlife.|
M~An official assessor of the noises we make when calling friends. Peculiar profession.|
N~A naming service! I would ask what criteria he uses.|
N~Names are small things that can become very hard to set down.|
S~A second opinion can be helpful when you have stared at the same ideas too long.|
S~I wonder what the most memorable name he has heard was.
''')
add('gate_lavender_route','Route11_EastEntrance_1F_Text_RockTunnelToReachLavender',
    'A traveler gives directions to Lavender through Rock Tunnel from Cerulean.','''
N~Directions with a mountain in the middle. We should prepare for that part.|
N~The route connects through Cerulean and Rock Tunnel. A useful sequence of landmarks.|
N~Check supplies and light before taking the tunnel.|
N~Clear directions help, even when the route itself sounds daunting.|
N~A good place to pause and plan the next stretch.|
N~The itinerary offers an underground chapter before the destination.|
N~A dark way through can still be the right way forward.|
N~Route established. Terrain requirements still need checking.|
N~The road to a quiet town bends through a very dark place.|
N~Helpful directions are better when they name the difficult section plainly.|
N~I wonder how often they guide travelers who expected a simpler route.
''')
add('itemfinder','Route11_EastEntrance_2F_Text_ExplainItemfinder',
    'After the Pokedex reward, the aide explains the Itemfinder\'s directional limits.','''
S~It points toward the treasure but leaves us the dignity of poking around in the dirt.|
S~The aide clearly distinguishes directional detection from precise localization.|
N~Useful lead. Still need eyes and patience to finish the job.|
N~I appreciate being told the limit before expecting it to do everything.|
S~A practical tool with practical instructions. Good gift.|
M~The machine supplies suspense; the ground still requires a personal investigation.|
S~A device for finding what the hurried world has overlooked.|
S~Excellent documentation! State the capability and the limit together.|
S~A little needle toward something quietly waiting nearby.|
N~Knowing what a tool cannot do prevents a lot of disappointment.|
S~I wonder what the aide first found while learning to use it.
''')
add('lookout_recommendation','Route12_NorthEntrance_1F_Text_LookoutSpotUpstairs',
    'A traveler recommends the magnificent view from the upstairs lookout.','''
S~A small climb with a scenery reward. My kind of optional challenge.|
S~Elevation can reveal the layout of a place that is hard to see from the road.|
S~Worth a look while we have a quiet moment.|
S~A place to stop and look sounds lovely after all the walking.|
S~A view can be a perfectly good reason to take a short break.|
S~The upstairs room has received a glowing review without charging admission.|
S~Sometimes the best part of a road is a place to stop facing forward.|
S~A higher vantage point! Useful for orientation as well as enjoyment.|
S~A few stairs can make the world feel wider.|
S~A good recommendation does not always need a shop attached.|
S~I wonder what part of the view they like most.
''')
add('return_tm','Route12_NorthEntrance_2F_Text_ExplainTM27',
    'A bereaved girl explains Return after passing on her departed Pokemon\'s TM.','''
S~That gift has a memory inside it. We should treat it gently.|
S~Her explanation links the move to the relationship she remembers with her Pokemon.|
S~A gift like that deserves respect. It mattered to someone she loved.|
D~She is sharing something that belonged to a life she misses.|
S~We can honor the kindness by caring well for the partners still with us.|
D~A small inheritance from a bond that did not end neatly with goodbye.|
S~Something used in love has found another place to be useful.|
N~The practical explanation carries more weight knowing why she no longer needs it.|
S~A little trace of an old affection, passed into another pair of hands.|
D~She gave us more than a useful disc. We should remember that.|
S~I wonder what her partner was like when she talks about that trust.
''')
add('return_no_room','Route12_NorthEntrance_2F_Text_DontHaveRoomForThis',
    'The bereaved girl cannot give the TM because our bag is full.','''
N~That is a tender offer to have stopped by a badly organized bag.|
N~The intended transfer did not occur. The significance of her offer deserves care.|
N~Make room. Do not rush her while we sort it.|
F~I wish we had been ready to accept something that means so much.|
N~A little sorting is all we need. Her generosity can wait without pressure.|
N~An unexpectedly clumsy obstacle in a delicate conversation.|
N~A full pocket can be an awfully small thing to interrupt something important.|
N~Capacity problem. Fix it quietly rather than making her repeat the whole story.|
N~The offered memory is waiting outside a crowded place.|
N~We should make room with more care than this moment first received.|
N~I hope the interruption does not make her feel the gift was unwanted.
''')
add('aide_passed','Route15_WestEntrance_1F_Text_OaksAideCameByHere',
    'The gate worker recognizes our Pokedex project and says Oak\'s aide passed through.','''
S~Our homework has developed a reputation ahead of us.|
S~The aide's recent visit is a useful lead connected to our research task.|
N~Worth checking nearby. The worker remembered why we might need them.|
S~It feels strange and nice to be recognized for something we are working on.|
S~A small message passed along can save a lot of searching.|
S~The research expedition has acquired a modest roadside information network.|
S~Someone remembered our work even before meeting us properly.|
N~Relevant lead, supplied at the right point on the route. Helpful.|
S~The path has kept a little message for us.|
S~Attentive service. They connected the visitor with the work instead of just pointing vaguely.|
S~I wonder how far ahead the aide is.
''')
add('exp_share','Route15_WestEntrance_2F_Text_ExplainExpShare',
    'After rewarding Pokedex progress, the aide explains Exp. Share.','''
S~A way for a quieter teammate to learn while the others take the lead. Lovely.|
S~The held item allows experience sharing without requiring direct participation.|
S~Useful for bringing someone along without throwing them in unready.|
S~I like the idea that being there can help a partner learn.|
S~A careful way to include a newer teammate in a longer journey.|
S~The supporting cast gains something without being thrust into every difficult scene.|
S~A place beside the others can become its own small lesson.|
S~Shared progress without full load. Useful for a developing partner.|
S~Someone can grow quietly in the company of stronger footsteps.|
N~A useful reward, especially when the team's progress is uneven.|
S~I wonder which partner would benefit most from carrying it now.
''')
add('cycling_no_pedestrians','Route16_NorthEntrance_1F_Text_NoPedestriansOnCyclingRoad Route18_EastEntrance_1F_Text_NeedBicycleForCyclingRoad',
    'The gate guard refuses foot traffic on Cycling Road.','''
N~The road has a dress code, and it is two wheels.|
N~The route is restricted to cyclists. Walking through is not an available option.|
N~Fast bikes and walkers are a poor mix on a narrow slope. Fair rule.|
N~It is disappointing to stop, but the warning is clear.|
N~Better to know at the gate than feel stranded halfway down.|
N~The scenic corridor insists on a very particular mode of entrance.|
N~A road can be public and still a poor place for feet.|
N~Access requirement is explicit: bring a bicycle.|
N~Some paths are meant for a different rhythm of travel.|
N~A practical rule, even when it changes our plans.|
N~I wonder how many people arrive expecting to walk the whole way.
''')
add('cycling_downhill','Route16_NorthEntrance_1F_Text_CyclingRoadIsDownhillCourse',
    'A gate traveler praises the downhill coastal Cycling Road.','''
S~Sea air and gravity helping. A very persuasive combination.|
N~The slope makes this direction easier, though it increases the need for braking control.|
N~Enjoy the ride. Keep enough room to stop.|
S~That sounds like a lovely stretch when the wind is gentle.|
S~A pleasant descent is a good reward for reaching this end of the road.|
S~The coast supplies the scenery while the hill supplies the pace.|
S~For once, the ground is willing to do some of the work.|
S~Potential energy put to enjoyable use! Check the brakes first.|
S~A road sloping toward sea air feels like a small invitation.|
S~A good ride is easier to enjoy when you know what the road will do.|
S~I wonder what time of day the water looks best from the road.
''')
add('cycling_new_boyfriend','Route16_NorthEntrance_2F_Text_OnBikeRideWithGirlfriend',
    'A cyclist enjoys a relaxed outing on his new bike with his girlfriend.','''
S~A new bike and good company. That is a very complete afternoon.|
S~A relaxed shared outing is a sensible way to get familiar with new equipment.|
S~Good plan. Keep a pace they both enjoy.|
S~It sounds nice to spend time together without making a competition of it.|
S~A simple day out can be the one you remember warmly.|
S~A pleasant itinerary with an unusually good balance of company and scenery.|
S~New wheels, familiar company, no urgent destination. A decent arrangement.|
S~A gentle test ride with a companion. Good way to notice any problems early.|
S~Two people making a small ordinary journey feel worth keeping.|
S~Relaxed is doing the important work in that plan.|
S~I wonder whether they picked the route together.
''')
add('cycling_new_girlfriend','Route16_NorthEntrance_2F_Text_RidingTogetherOnNewBikes',
    'The girlfriend looks forward to riding together on their new bicycles.','''
S~Two new bicycles. They have skipped straight to a coordinated expedition.|
S~Matching activity, separate bicycles. Each rider can still choose a comfortable pace.|
S~Hope they leave room to enjoy the ride instead of racing it.|
S~She sounds happy about the together part most of all.|
S~A good shared outing leaves time to stop when something catches your eye.|
S~The new wheels have found a very pleasant first chapter.|
S~An ordinary road becomes a little more theirs by riding it together.|
S~Two fresh machines on a first outing! Check the fittings before the descent.|
S~A road can hold two separate tracks moving comfortably beside each other.|
S~A little coordination can be charming when nobody has to match perfectly.|
S~I wonder what made them choose new bikes at the same time.
''')
add('amulet_coin','Route16_NorthEntrance_2F_Text_ExplainAmuletCoin',
    'After the Pokedex reward, the aide explains that a held Amulet Coin raises prize money when its Pokemon participates.','''
S~A lucky coin with very specific attendance requirements. Read the fine print.|
N~The holder must participate in a winning battle for the increased reward to apply.|
N~Useful. Keep the holder safe rather than chasing extra cash.|
N~It is good that the aide explained the condition clearly.|
N~A little more income can help with supplies when we use it thoughtfully.|
M~The lucky charm insists on appearing in the scene before collecting its fee.|
N~A coin that apparently prefers to watch the battle itself.|
N~Conditional effect. Participation requirement matters as much as the reward.|
N~A little metal circle that wants to travel into the work.|
N~Useful accessories deserve instructions. This one certainly has them.|
N~I wonder which partner would be most comfortable carrying it.
''')
add('cycling_uphill_gate','Route18_EastEntrance_1F_Text_CyclingRoadAllUphillFromHere',
    'A traveler warns that Cycling Road is uphill from the southern entrance.','''
N~We have found the end where gravity stops being our friend.|
N~Entering from this side changes the same road into a much more demanding climb.|
N~Take it steady. No shame in stopping before the legs give out.|
N~That is a useful warning before the work begins.|
N~A drink and a sensible pace belong in that plan.|
N~The scenic ride has turned the page to its considerably less merciful edition.|
N~The same road, with all its kindness facing the other direction.|
N~Elevation gain ahead. Revise the time and energy estimates.|
N~The road is about to ask more from each turn of the wheels.|
N~A clear warning is kinder than letting someone discover the slope halfway up.|
N~I wonder how many cyclists decide to change plans after hearing that.
''')
add('safari_entry_declined','FuchsiaCity_SafariZone_Entrance_Text_OkayPleaseComeAgain',
    'The Safari attendant accepts our decision not to enter.','''
N~No safari today. The Pokemon can enjoy a visitor-free afternoon from us.|
N~We declined the paid visit. No entry has been purchased.|
N~Fine. We can come back when we are ready.|
S~It is nice to leave the choice open without being hurried.|
N~A better-prepared visit will be more enjoyable anyway.|
N~The proposed expedition has been postponed before its first muddy footstep.|
S~A closed plan, with the door still politely open.|
N~Cancellation handled cleanly. Good service.|
N~The reserve can wait for a different afternoon.|
S~A pleasant answer to someone deciding against the purchase.|
N~I wonder what season the regular visitors enjoy most.
''')
add('safari_no_money','FuchsiaCity_SafariZone_Entrance_Text_OopsNotEnoughMoney',
    'The Safari attendant refuses entry because we lack the admission fee.','''
N~The safari has met a more ordinary obstacle than wild Pokemon: the budget.|
N~Insufficient funds prevented entry. No successful admission occurred.|
N~Keep the money we have. We can return later.|
N~An awkward stop, but there is no need to dwell on it.|
N~The team's supplies come before an extra outing.|
N~The expedition has been defeated by arithmetic at the front desk.|
N~A wide reserve, a narrow purse. Another day, perhaps.|
N~Fee requirement not met. No change of route into the reserve.|
N~Some doors wait for coins rather than courage.|
N~We can accept the answer without making the attendant's day harder.|
N~I wonder how many visitors forget to set the entrance fee aside.
''')
add('safari_early_exit','FuchsiaCity_SafariZone_Entrance_Text_PleaseReturnSafariBalls',
    'The attendant ends our Safari visit early and asks for remaining Safari Balls.','''
N~Adventure concluded early. Return the special equipment and keep the interesting memories.|
N~The remaining Safari Balls belong to the visit and are being collected on exit.|
N~We chose to leave. Hand back the equipment and let the team rest.|
S~There is nothing wrong with ending a visit when you have had enough.|
N~A shorter outing can still be a good one.|
N~The expedition takes a voluntary bow before the final bell.|
S~An early ending does not erase what was pleasant before it.|
N~Equipment return closes the session. Sensible process.|
N~The gate can be the right destination before the clock says so.|
N~A calm exit is better than forcing the day to fill its whole allowance.|
S~I wonder which part of the visit will stay with us most.
''')
add('safari_finished','FuchsiaCity_SafariZone_Entrance_Text_CatchFairShareComeAgain',
    'The attendant closes a completed Safari visit and invites us back.','''
S~The day has collected enough little surprises for one visit.|
N~The session ended after its available time or Safari Balls were exhausted.|
N~Done for now. Good time to check how everyone is doing.|
S~A friendly ending makes leaving feel less abrupt.|
N~A quiet rest sounds good after all that searching.|
S~The curtain falls on a collection of encounters the schedule could not have predicted.|
S~Some meetings stay with you even after the gate closes.|
N~Session resources exhausted. Review what happened before planning another.|
S~The reserve keeps its remaining mysteries for another day.|
S~An invitation back is a pleasant finish, whatever the catch count.|
S~I wonder what the attendants enjoy hearing from returning visitors.
''')
add('mom_oak','PalletTown_PlayersHouse_1F_Text_AllBoysLeaveOakLookingForYou PalletTown_PlayersHouse_1F_Text_AllGirlsLeaveOakLookingForYou',
    'Mom recognizes our choice to set out and says Professor Oak was looking for us.','''
S~She is letting the journey be ours, while still remembering the next-door message.|
S~Her response respects the decision while passing along a practical detail.|
S~Good to know someone is keeping an eye out without holding us back.|
S~Leaving feels different when the person at home understands.|
S~A familiar voice and one useful reminder before we go.|
S~A departure receives parental approval and a modest errand attached.|
S~Home can open its door outward without becoming less home.|
N~Decision acknowledged, relevant message delivered. Efficient family briefing.|
S~The first road begins in a room where somebody knows your name.|
S~She makes room for independence without making it feel lonely.|
S~I wonder how much she guessed before we said anything.
''')
add('mom_rest_finished','PalletTown_PlayersHouse_1F_Text_LookingGreatTakeCare',
    'After resting at home, Mom says we and our Pokemon look well and sends us off.','''
S~Home has inspected the team and approved us for more wandering.|
S~A familiar rest has left both trainer and partners visibly better.|
S~Good. Head out rested instead of proving how tired we can get.|
S~A simple take care can carry more warmth than a long speech.|
S~Nothing fancy. Just a good rest and someone glad to see us well.|
S~The homeward interlude closes with a kindly renewed blessing.|
S~A familiar room has given back a little of what the road took.|
N~Recovery confirmed. Better starting condition for the next outing.|
S~Home has a way of returning your own footsteps to you.|
S~She notices the Pokemon too. That makes the welcome feel complete.|
S~I wonder whether she watches until we are out of sight.
''')
add('viridian_names','ViridianCity_House_Text_NicknamingIsFun',
    'A parent weighs clever nicknames against simple memorable ones.','''
M~A clever name is excellent until you have to shout all seven syllables across a field.|
N~Memorability and originality can conflict. The intended use should guide the choice.|
N~Pick something the partner can recognize and you can call clearly.|
S~A simple name can become special through who answers to it.|
S~The name you enjoy saying every day is often the right one.|
M~As a collector of elaborate words, I reluctantly concede the practical argument.|
S~A small familiar word can hold a surprising amount of affection.|
N~Good naming includes retrieval speed. Especially during a hurried moment.|
S~A plain word changes when somebody beloved starts answering it.|
S~Clever is optional. A name that feels right lasts longer.|
S~I wonder which name took them the longest to choose.
''')
add('viridian_daddy','ViridianCity_House_Text_MyDaddyLovesMonsToo',
    'A child proudly says their father also loves Pokemon.','''
S~That is a lovely thing to be proud of your dad for.|
S~Shared affection can make learning about Pokemon a family activity.|
S~Good. Children notice how the grown-ups treat their partners.|
S~They sound glad to have that interest in common.|
S~A home is warmer when kindness is something a child can point out.|
S~A concise character reference from a deeply invested family member.|
S~A little pride in somebody else's gentleness. Rather lovely.|
S~Good example identified and enthusiastically reported.|
S~The small person has noticed which things make the large one kind.|
S~That is a sweet introduction to someone who is right here.|
S~I wonder what they most enjoy doing with the Pokemon together.
''')
add('viridian_parcel','ViridianCity_Mart_Text_SayHiToOakForMe',
    'After handing over Oak\'s Parcel, the clerk thanks us and asks us to greet Oak.','''
S~One delivery, with a friendly hello tucked under the wrapping.|
S~The handoff is complete and the clerk has supplied a personal message for the recipient.|
N~Straightforward errand. Keep the parcel safe on the way back.|
S~It is nice when an errand carries a little familiarity between people.|
S~A simple favor can make the next visit to town feel more friendly.|
S~The courier's assignment includes a small conversational attachment.|
S~An ordinary package carrying a little connection between two places.|
N~Parcel received, destination known, extra greeting recorded.|
S~A small journey keeps familiar people in one another's day.|
S~The clerk trusts us with the delivery. We should be careful with it.|
S~I wonder how often Oak orders something from this shop.
''')
add('viridian_antidotes','ViridianCity_Mart_Text_ShopDoesGoodBusinessInAntidotes',
    'A customer remarks that the Viridian shop sells many Antidotes.','''
N~That is a very practical review of the local wildlife.|
N~Strong demand may reflect the hazards of nearby routes. Useful preparation information.|
N~Worth carrying some before heading toward the forest.|
N~An oddly worrying way to hear a shop is doing well.|
N~Better to buy the useful thing before the team needs it.|
N~The local economy offers a concise warning about what lives outside town.|
N~A successful shop can be an indirect portrait of an unpleasant afternoon.|
N~Sales patterns can reveal local risks. Noted.|
N~The shelves remember what the grass has been doing to travelers.|
N~A useful rumor to hear while we can still choose supplies.|
N~I wonder how many visitors arrive without knowing they need one.
''')
add('viridian_potions','ViridianCity_Mart_Text_GotToBuySomePotions',
    'A customer prepares Potions for unexpected injuries.','''
N~A small bottle of being glad you planned ahead.|
N~Accessible recovery supplies help manage uncertainty on the road.|
N~Good habit. Buy what the team needs before leaving town.|
N~It is reassuring to have an answer ready for a bad moment.|
N~A sensible reserve makes the whole outing less fragile.|
N~The most useful supporting character may be a bottle bought before the plot starts.|
N~An ordinary purchase with a potentially very welcome future.|
N~A spare recovery option is basic redundancy. Good planning.|
N~A little help carried quietly until the right moment arrives.|
N~Practical preparation rarely looks exciting in the shop.|
N~I wonder what they learned to pack after their first long walk.
''')
add('viridian_pc_welcome','ViridianCity_PokemonCenter_1F_Text_FeelFreeToUsePC',
    'A visitor appreciates being invited to use the Pokemon Center PC.','''
S~A public corner that actually feels welcoming. Nice work by the receptionist.|
S~Clear permission helps newcomers use a shared resource confidently.|
S~Good to be told what is available instead of having to guess.|
S~A small welcome can make an unfamiliar room feel much easier.|
S~Helpful staff can turn a building into a place you are comfortable returning to.|
S~The receptionist has made an ordinary amenity feel like hospitality.|
S~A little permission can lift a surprising amount of hesitation.|
S~Accessible tool, clear instructions, welcoming introduction. Excellent.|
S~A useful place has left a small light on for strangers.|
S~They remember the kindness as much as the service. That says something.|
S~I wonder how many first-time visitors she has helped settle in.
''')
add('viridian_centers_free','ViridianCity_PokemonCenter_1F_Text_PokeCenterInEveryTown',
    'A traveler explains that towns ahead have free Pokemon Center healing.','''
S~A road with places to recover along it. That makes the distance feel kinder.|
S~Reliable access to free care can substantially reduce the burden of travel.|
S~Use the help. No reason to keep the team hurting.|
S~It is reassuring to know there will be another welcoming place ahead.|
S~Care should not be the thing we hesitate to ask for.|
S~A network of merciful pauses stitched through the journey.|
S~The world has left some doors open without asking what is in your purse.|
S~Distributed recovery facilities. An excellent piece of regional infrastructure.|
S~A lighted room waits somewhere beyond each long stretch.|
S~A useful reassurance, especially for a traveler counting coins carefully.|
S~I wonder how much easier the road feels once people learn that.
''')
add('viridian_healing','ViridianCity_PokemonCenter_1F_Text_PokeCentersHealMons',
    'A visitor explains that Pokemon Centers restore hurt, tired, or fainted Pokemon.','''
S~A place that welcomes the entire list of ways a day can go badly.|
S~The service addresses fatigue and injury as well as fainting.|
N~Bring the team in before things get worse. That is why the help is here.|
S~I like that tired is enough of a reason to come.|
S~A proper recovery is worth making time for.|
S~The journey's troubles meet a reassuringly capable counter.|
S~A place where needing help is an ordinary arrival.|
N~Recovery capability noted. Use it rather than carrying damage into the next test.|
S~A room where the day's sharp edges can be put down.|
N~Clear explanation. Nobody should feel they need to wait until a partner faints.|
S~I wonder how many worried trainers feel better as soon as they reach the door.
''')
add('school_notes','ViridianCity_School_Text_TryingToMemorizeNotes',
    'A student is trying hard to memorize their notes.','''
N~That is the sound of a head trying to become a filing cabinet.|
N~Retrieving ideas in small pieces may be easier than repeatedly rereading everything.|
N~Take breaks. A tired head does not learn by being scolded.|
S~I know that feeling when the page seems larger every time you look at it.|
N~A little rest can make the next pass less frustrating.|
N~The notebook's contents are staging a difficult relocation into memory.|
N~Paper remembers things with an unfair lack of effort.|
N~Test one idea at a time. Otherwise it is hard to know what stuck.|
N~Words settle better when given a quiet little space between them.|
N~They sound determined. I hope someone has shown them a manageable method.|
N~I wonder which part keeps slipping away when they close the notebook.
''')
add('school_blackboard_advice','ViridianCity_School_Text_ReadBlackboardCarefully',
    'The teacher advises reading the blackboard carefully.','''
N~The important words are already written down. A merciful sort of lecture.|
N~Careful reading matters when similar conditions require different responses.|
N~Worth knowing the basics before a partner needs help.|
N~I appreciate having time to read rather than being asked to remember it instantly.|
N~A little attention here can save panic on the road.|
N~The lesson has wisely taken a form that does not vanish once spoken.|
N~An ordinary board holding several ways to make a bad moment less bad.|
N~Read the labels before the emergency. Excellent general rule.|
N~Small chalk marks can carry someone safely through a difficult day.|
N~Good advice. Careful is the useful part.|
N~I wonder which lesson the teacher wishes travelers remembered best.
''')
add('school_private_notes','ViridianCity_School_Text_HeyDontLookAtMyNotes',
    'A student objects to us looking at their personal notes.','''
F~The notebook has an owner. We have discovered this by annoying her.|
N~Personal study notes are not automatically public reference material.|
N~Her notes. Ask before looking.|
F~I would be embarrassed too if someone read over my shoulder.|
N~A little permission would have made this a different conversation.|
N~The unauthorized reader has been removed from the study group.|
F~An open page is not necessarily an open invitation.|
N~Private document. Access denied, clearly enough.|
N~Words can need a little room around them, just like people.|
N~She is allowed a corner of the work that belongs to her.|
N~We should let her study without making the day more awkward.
''')
add('pewter_sit','PewterCity_House1_Text_NidoranSit',
    'A resident tries to teach Nidoran to sit.','''
S~A small lesson, with a very important little audience.|
N~Consistent, patient cues are more useful than simply repeating them louder.|
N~Give Nidoran time to understand what is being asked.|
S~The quiet everyday practice is rather nice to see.|
S~A little patience makes learning easier for both of them.|
S~The household's smallest performer is rehearsing a very concise routine.|
S~A modest request, potentially a very grand achievement.|
N~Clear cue, patient repetition, then acknowledge the right response.|
S~A little creature is learning one of the household's shared words.|
S~Training can look this ordinary and still matter.|
S~I wonder what Nidoran already knows how to do.
''')
add('pewter_trade_difficulty','PewterCity_House1_Text_TradeMonsAreFinicky',
    'The family describes the challenges of training a traded Pokemon and wishes for badges.','''
N~A new partner brings its own opinions. Apparently several strong ones.|
N~A traded Pokemon's training requirements can differ from what a novice expects.|
N~Learning to handle a partner takes work. Keep treating it well while learning.|
N~A new home must be an adjustment for Nidoran too.|
N~Patience matters while they learn each other's habits.|
N~The household has discovered that a new cast member does not arrive fully rehearsed.|
N~Being unfamiliar is difficult on both sides of a greeting.|
N~The family needs experience, not simply a stronger command signal.|
N~Two lives learning how to share a room can take time.|
N~I hope they see a partner adjusting, not just a problem to manage.|
N~I wonder whether the original trainer explained Nidoran's habits.
''')
add('pewter_move_learning','PewterCity_House2_Text_MonsLearnTechniquesAsTheyGrow',
    'A resident distinguishes naturally learned moves from those taught by people.','''
N~Some lessons arrive with growing up. Others require somebody with a lesson plan.|
N~A Pokemon's available techniques can reflect both development and instruction.|
N~Pay attention to what the partner learns and what it still needs help with.|
S~It is interesting how many different ways there are to learn.|
N~Knowing which kind of lesson is needed saves a lot of waiting.|
S~The repertoire grows through experience, with occasional outside editing.|
S~Not every new thing has to be discovered alone.|
S~Built-in learning and external instruction. Useful distinction.|
S~Some doors open with time; others need someone to show the handle.|
N~Good advice for anyone assuming every useful move will simply appear.|
S~I wonder which lesson first made them notice the difference.
''')
add('pewter_status_catch','PewterCity_House2_Text_MonsEasierCatchIfStatused',
    'A resident explains that status conditions aid capture but never guarantee it.','''
N~A better chance is still a chance. The Pokemon has not signed the paperwork.|
N~Status can influence capture probability without making the outcome certain.|
N~Know the risk to the Pokemon. Do not keep hurting it out of frustration.|
N~I appreciate the reminder that a creature is not a guaranteed result.|
N~A calm, careful attempt is better than treating a failed throw as an insult.|
N~The lesson ends with a sensible warning against a guaranteed happy ending.|
N~An advantage is not an entitlement. Worth remembering.|
N~Probability improved, certainty unchanged. Important distinction.|
N~A living creature is not obliged to become the answer you hoped for.|
N~That final caution is as useful as the technique itself.|
N~I wonder how many beginners expect the first useful trick to work every time.
''')
add('pewter_fish_regret','PewterCity_Mart_Text_BoughtWeirdFishFromShadyGuy',
    'A customer regrets paying a shady seller for a weak fish Pokemon.','''
N~Be annoyed with the salesman. The fish did not write the sales pitch.|
N~The misleading transaction and the Pokemon's worth are separate questions.|
N~The seller made the promises. Treat the partner properly.|
D~I hope the fish does not become the target of that disappointment.|
N~A bad purchase story can still become a good partnership with time.|
N~The persuasive merchant has departed, leaving the innocent supporting fish with the review.|
N~A creature should not have to answer for the person who sold it.|
N~Bad sales information does not make the received partner defective.|
N~A small life has arrived wrapped in somebody else's dishonest words.|
N~The poor fish was the only participant who did not choose the deal.|
N~I wonder whether the new trainer has given it a real chance yet.
''')
add('pewter_patience','PewterCity_Mart_Text_GoodThingsIfRaiseMonsDiligently',
    'A customer encourages patient care for apparently weak Pokemon.','''
S~A little faith gives a small partner room to surprise everybody.|
S~Sustained care can reveal capabilities that an early impression misses.|
S~Give the team time. Nobody begins at their best.|
S~It is lovely advice to hear beside all the bottles for quick improvements.|
S~Daily care may be quiet work, but it adds up.|
S~The unassuming cast member is being allowed a proper character arc.|
S~An ordinary creature can become extraordinary company before anybody notices its strength.|
S~Long-term investment beats judging the first test result alone.|
S~Some things need a season before the first visible sign.|
S~Being patient with a partner is a good look on anyone.|
S~I wonder which Pokemon taught them that lesson.
''')
add('pewter_phone','PewterCity_PokemonCenter_1F_Text_TeamRocketMtMoonImOnPhone',
    'A caller reacts to news of Team Rocket at Mt. Moon and snaps at our interruption.','''
N~Bad news, bad timing, and apparently we supplied the interruption.|
N~The caller is occupied with worrying news. We should not assume we heard the full account.|
N~Give them space. We can remember the warning about Mt. Moon.|
N~They sound alarmed. I would rather let them finish the call.|
N~It is no time to press for a conversation they did not choose.|
N~A tense call has acquired an unwelcome live audience. We can remove that part.|
N~Worry makes an ordinary interruption feel much sharper.|
N~Partial report received. Better to seek reliable details later.|
N~A small receiver has made the room feel less safe.|
N~The tone was rough, but the news clearly upset them.|
N~I wonder who is calling from near the mountain.
''')
add('pewter_jiggly_sleep','PewterCity_PokemonCenter_1F_Text_WhenJiggylypuffSingsMonsGetDrowsy',
    'A visitor grows sleepy while explaining Jigglypuff\'s song.','''
S~The explanation has become its own demonstration. Very convincing.|
S~The listener's drowsiness appears to support the reported effect of the song.|
N~At least this is a safe place to get sleepy.|
S~An audience drifting off does not always mean the singer did badly.|
S~A comfortable chair would be useful right about now.|
S~The review concludes with the critic unconscious. A decisive endorsement.|
S~A soft song quietly winning an argument with wakefulness.|
N~Observed effect matches the warning. Very efficient teaching.|
S~A room full of small breaths slowing into the same rhythm.|
S~That is a lovely sound to underestimate at your peril.|
S~I wonder whether anyone ever makes it to the end of the song awake.
''')
add('pewter_clefairy_trade','PewterCity_PokemonCenter_1F_Text_TradingMyClefairyForPikachu',
    'A child plans to trade Clefairy for a wanted Pikachu.','''
S~A new partner is exciting. I hope Clefairy is headed somewhere kind too.|
N~A successful exchange should account for the needs of both Pokemon.|
N~Be sure both trainers understand the deal and can care for the new partner.|
N~I hope they have thought about saying goodbye as well as saying hello.|
S~A good new home matters on both sides of the trade.|
N~The desired arrival deserves a thoughtful farewell for the departing companion.|
N~A change can be welcome and still have a tender edge.|
N~Two transfers, two sets of care requirements. Check both.|
N~One little friendship changes shape as another begins.|
N~Wanting a particular look is only the start of choosing a partner.|
S~I wonder what made Pikachu the one they wanted.
''')
add('pewter_pikachu_trade','PewterCity_PokemonCenter_1F_Text_TradingPikachuWithKid',
    'Another trainer explains trading one of two Pikachu with the child.','''
S~Both trainers want a change. That is a promising place to start.|
N~The exchange offers each trainer something different from their current collection.|
N~Make sure the new trainer knows how to look after Pikachu.|
N~Having two does not make the one leaving any less individual.|
N~A little advice about Pikachu's habits would be a good parting gift.|
S~A familiar companion finds a new role in somebody else's story.|
N~Two similar creatures can still leave very different spaces behind.|
N~Useful swap, provided the handoff includes more than the Poke Ball.|
N~An ordinary exchange carries a small life across a large change.|
N~I hope the choice considers the particular Pikachu, not just the duplicate slot.|
S~I wonder which habits the new trainer will discover first.
''')
add('museum_decline','PewterCity_Museum_1F_Text_ComeAgain',
    'The museum attendant accepts our decision not to buy admission.','''
N~The ancient bones can wait. They are unusually experienced at it.|
N~We declined admission and can return when the visit suits our plans.|
N~No rush. Better visit when we have time to look properly.|
S~It is nice to leave an interesting place for a day when you can enjoy it.|
N~A museum is worth more than a hurried dash between errands.|
S~The prehistoric cast remains available for a later audience.|
S~Some old things will not mind another quiet afternoon.|
N~No transaction, no complication. Straightforward.|
S~The past is not going anywhere before we come back.|
N~A polite ending leaves the future visit feeling welcome.|
S~I wonder which exhibit would catch our eye first next time.
''')
add('museum_entry','PewterCity_Museum_1F_Text_Right50YThankYou PewterCity_Museum_1F_Text_PleaseEnjoyYourself',
    'The museum attendant welcomes us after admission or invites us to enjoy an existing visit.','''
S~Permission to stare at remarkable old things. Happily accepted.|
S~A chance to inspect evidence of lives and events far beyond ordinary experience.|
S~Good place to slow down and look carefully.|
S~A quiet visit sounds lovely after the road.|
S~A little time indoors with something interesting is a good use of an afternoon.|
S~The audience is admitted; the ancient cast has been ready for some time.|
S~A room where being old and strange is considered an accomplishment.|
S~Time to examine the exhibits. I have questions about the displays.|
S~A quiet doorway into things that lasted longer than their own days.|
S~A welcoming introduction matters even in a room full of objects.|
S~I wonder which exhibit visitors linger beside longest.
''')
add('museum_no_money','PewterCity_Museum_1F_Text_DontHaveEnoughMoney',
    'The museum attendant cannot admit us because we lack the fee.','''
N~Even the past has a ticket counter. Another day, perhaps.|
N~The fee could not be paid, so the admission did not proceed.|
N~Keep the supplies budget. We can return later.|
N~An awkward answer, but no reason to be embarrassed.|
N~An interesting visit will still be here when we can spare the money.|
N~Our historical ambitions have met a very present-day accounting issue.|
N~The ancient world waits beyond a rather ordinary small sum.|
N~Budget constraint. Delay the optional visit.|
N~The door can wait without making the world behind it smaller.|
N~A declined ticket is a practical detail, not a judgment.|
N~I wonder whether the outdoor part has anything worth seeing meanwhile.
''')
add('amber_genetics','PewterCity_Museum_1F_Text_AmberContainsGeneticMatter',
    'The museum worker describes ancient Pokemon genetic material in amber and resurrection research.','''
U~A little tree sap kept an ancient instruction book. Trees are excellent accidental librarians.|
U~Preserved genetic material could be scientifically valuable. The reported research is remarkable.|
N~Worth serious study. Ancient life deserves careful handling if it returns.|
U~It is strange to think something so old might carry enough of a life to begin again.|
N~An extraordinary idea needs patient, careful people working on it.|
U~A golden fragment holds the possibility of a very old character returning to the page.|
S~A small hard thing holding a soft possibility for longer than we can imagine.|
U~Information preserved across that much time! The reconstruction problem is astonishing.|
S~A tree's old wound may have kept a way back for something lost.|
S~It makes that small piece of amber feel much larger.|
U~I wonder what first convinced researchers the material could still be useful.
''')
add('amber_sap','PewterCity_Museum_1F_Text_AmberIsFossilizedSap',
    'The worker explains that amber began as tree sap that hardened over time.','''
S~A tree made something sticky, and time turned it into museum material. Nice teamwork.|
S~A familiar biological material can become a durable record through fossilization.|
N~Good reminder that remarkable things can begin very ordinarily.|
S~I like knowing the simple beginning behind that golden color.|
S~Something once messy became worth keeping carefully.|
S~A modest woodland substance has enjoyed a spectacularly long career change.|
S~Time has a peculiar talent for making old messes beautiful.|
S~Natural material changing properties across a very long process. Fascinating.|
S~The tree let go of a little golden time.|
S~Knowing what it began as makes the finished thing more interesting.|
S~I wonder how many visitors guessed its origin before hearing that.
''')
add('museum_long_life','PewterCity_Museum_1F_Text_ShouldBeGratefulForLongLife',
    'An older visitor is grateful to have lived long enough to see dragon bones.','''
S~An old visitor meeting a much older surprise. That is lovely.|
S~An unfamiliar discovery can remain meaningful at any age.|
S~Good to still find something that makes the day feel new.|
S~There is so much wonder in that one small sentence.|
S~I hope there are more unexpected good days waiting for them.|
S~A long life has saved room for one astonishing late chapter.|
S~Growing old without exhausting your capacity to be amazed. A fine ambition.|
S~Decades of experience, still delighted by new evidence. Excellent outlook.|
S~An old pair of eyes finding one more reason to stay curious.|
S~Wonder suits people at every age.|
S~I wonder what they imagined dragons looked like before seeing the bones.
''')
add('amber_followup','PewterCity_Museum_1F_Text_GetOldAmberChecked',
    'The researcher asks us to get the Old Amber examined after entrusting it to us.','''
N~The secret is portable now. We should carry it carefully.|
N~The next step is examination by an appropriate laboratory, rather than assuming the hypothesis.|
N~Get it checked. Keep it safe until then.|
N~He sounds hopeful enough that the request feels very important to him.|
N~A careful delivery matters when someone trusts us with something irreplaceable.|
N~The scientific mystery has left the museum in a travel-sized form.|
N~A little old thing carrying a very new hope.|
N~Independent examination is the right next test. We can handle the transport.|
S~Someone's quiet hope has been placed in our hands.|
N~He is trusting us to take the idea seriously. We should.|
S~I wonder what he hopes the lab will find first.
''')
add('museum_fossils','PewterCity_Museum_1F_Text_WeHaveTwoFossilsOnExhibit',
    'A museum visitor notes the two rare prehistoric Pokemon fossil exhibits.','''
S~Two very old introductions. They have been waiting a while for visitors.|
S~A small collection can still preserve significant evidence of past species.|
N~Worth looking properly. Fragile history does not get a replacement.|
S~It is strange to stand near the shape of a life that old.|
S~Only two displays, but plenty to spend time thinking about.|
S~An ancient double bill, with an exceptionally long interval since the first appearance.|
S~Two silences that still have quite a lot to say.|
S~Two specimens, countless questions. A promising ratio.|
S~The room keeps a little of a vanished world upright.|
S~A small exhibit can be more memorable than a crowded one.|
S~I wonder which fossil people recognize first.
''')
add('moonstone_doubt','PewterCity_Museum_1F_Text_WhatsSpecialAboutMoonStone',
    'A visitor doubts that the ordinary-looking Moon Stone is special.','''
M~A rock is excellent at keeping its qualifications to itself.|
N~Appearance alone is insufficient to determine a material's properties.|
N~Ordinary-looking things can still matter. Worth reading the label.|
S~I understand the surprise. The name promises more than the shape reveals.|
N~A quiet appearance does not make something less useful.|
M~The exhibit has been challenged to look more impressive on demand.|
S~Some strange things have the manners to look completely ordinary.|
N~External casing tells you less than you think. Test the properties.|
S~A secret can be small enough to fit in an unremarkable stone.|
N~The display might need a better explanation, rather than a shinier rock.|
N~I wonder what they expected it to look like.
''')
add('moonlanding_tv','PewterCity_Museum_1F_Text_BoughtColorTVForMoonLanding',
    'An older visitor recalls buying a color TV to watch the 1969 Moon landing news.','''
S~A new television for a very new view of the world. Memorable shopping trip.|
S~A major event can anchor a very precise personal memory.|
S~Some days make people remember exactly where they were.|
S~I like hearing how a huge event fits inside an ordinary living room.|
S~They kept the excitement all these years. That is lovely.|
S~An immense human milestone remembered partly through the furniture bought to witness it.|
S~A room lit by something far beyond the room. A good memory.|
U~A whole new viewing setup for one extraordinary event. I understand completely.|
S~A distant footprint left a small bright mark in someone's home.|
S~The purchase is part of the memory now, not just the picture.|
S~I wonder who gathered around the screen with them.
''')
add('space_exhibit','PewterCity_Museum_1F_Text_RunningSpaceExhibitThisMonth',
    'A museum staffer points out this month\'s space exhibit.','''
S~Old bones downstairs, very large questions upstairs. Good museum range.|
S~A rotating exhibit gives familiar visitors a reason to return.|
N~Worth taking the time if we are already here.|
S~I like when a familiar building still has something new to show.|
S~A quiet way to spend an afternoon without going very far.|
S~The program has expanded from ancient lives to a rather larger setting.|
S~A room that makes the sky feel a little less empty.|
S~Space hardware! I would like a close look at the mechanisms.|
S~A little building keeping room for an enormous outside.|
S~A changing exhibit keeps the place from feeling frozen in time.|
S~I wonder what they chose as the centerpiece.
''')
add('pikachu_wish','PewterCity_Museum_1F_Text_AskedDaddyToCatchPikachu',
    'A child excitedly wants their father to catch a Pikachu.','''
S~One very specific wish, delivered at full small-person enthusiasm.|
N~The interest is clear; the responsibilities of caring for a Pokemon still need discussion.|
N~Hope the grown-up explains the care as well as the catching.|
S~It is sweet how much happiness they can fit into saying one name.|
N~A new companion needs a ready home, not just an excited welcome.|
S~The requested addition to the family has an enthusiastic advance review.|
S~A small person imagines an equally small new friend.|
N~Clear request. Now someone needs to check the care requirements.|
S~A little wish with ears and a bright yellow shape.|
S~They know exactly what they like. The practical details come next.|
S~I wonder whether they have ever met a Pikachu close up.
''')
add('pikachu_parent','PewterCity_Museum_1F_Text_PikachuSoonIPromise',
    'The father promises his child a Pikachu soon.','''
N~That promise may be more difficult than the very short sentence suggests.|
N~A specific promise creates an expectation that practical preparation should support.|
N~Make sure the home is ready before bringing one back.|
N~He sounds fond, and perhaps a little overwhelmed by the repeated request.|
N~A promise about a living companion deserves more care than a surprise toy.|
N~The parental contract has been renewed under energetic negotiation.|
N~A little promise can become very large in a child's memory.|
N~Commitment recorded. Supplies and care plan should follow.|
N~Soon can stretch a long way for someone small.|
N~I hope he means the promise, rather than simply ending the conversation.|
N~I wonder whether he has started finding out where Pikachu live.
''')
add('bike_clerk_end','CeruleanCity_BikeShop_Text_ThankYouComeAgain',
    'The bicycle clerk ends a visit; this same goodbye follows refusal, cancellation, or voucher exchange.','''
N~A polite finish, whether we came to browse or had the right paperwork.|
N~This goodbye alone does not establish which transaction, if any, took place.|
N~We are done here for now. Check what we actually have before heading out.|
S~A friendly goodbye makes it easy to come back with questions.|
N~Good to finish the conversation before planning the next trip.|
N~The shop closes this scene with a versatile line of retail courtesy.|
N~An ordinary farewell, wisely vague about the contents of our pockets.|
N~Interaction complete. Verify the resulting equipment before choosing the route.|
N~The door opens back onto whatever road we are ready for.|
S~A courteous ending does not need to make a sales pitch.|
N~I wonder how many people return just to ask another bike question.
''')
add('bike_followup','CeruleanCity_BikeShop_Text_HowDoYouLikeNewBicycle',
    'The bicycle clerk asks about our bike and recommends roads and caves for riding.','''
S~He sold the wheels and kept some enthusiasm for the journeys afterward.|
S~A follow-up about actual use is welcome after the equipment handoff.|
N~Good bike. Still need to watch the ground in a cave.|
S~It is nice when somebody remembers that the purchase was the beginning.|
S~A helpful suggestion can turn a useful thing into a favorite part of the day.|
S~The bicycle's next chapter receives a cheerful endorsement from its former custodian.|
S~A little machine opens more of the road to ordinary afternoons.|
S~A use recommendation! Cave riding still deserves careful visibility checks.|
S~Two wheels can change how far away a place feels.|
S~He seems to care whether it is a good fit after it leaves the shop.|
S~I wonder which route he recommends to someone testing a new bike.
''')
add('city_bike_basket','CeruleanCity_BikeShop_Text_CityBikeGoodEnoughForMe',
    'A shopper prefers a practical city bicycle with a shopping basket.','''
S~A basket is a strong argument. Hills cannot carry your groceries home for you.|
N~The preferred design matches the actual use case rather than maximum performance.|
S~Buy the tool for the job you do. Sensible.|
S~I like someone knowing what they need without apologizing for it.|
S~A shopping basket is excellent bicycle technology in my opinion.|
S~An unfashionably persuasive defense of arriving home with the purchases intact.|
S~A small useful thing often makes a daily life better than a grand impressive one.|
S~Requirements first, equipment second. Exactly the right order.|
S~A quiet machine for carrying the ordinary things that keep a home going.|
S~Practical can be a style of its own when it suits the person.|
S~I wonder what route they take for their regular shopping.
''')
add('bike_price','CeruleanCity_BikeShop_Text_BikesCoolButExpensive',
    'A youngster admires the bicycles but balks at their cost.','''
N~The bicycle is shiny. The price has a much sharper edge.|
N~Admiration does not make an item affordable. A sensible distinction.|
N~Good to look before spending. No need to buy beyond your means.|
N~It is difficult when something appealing feels so far out of reach.|
N~A planned purchase is nicer than a long regret over the cost.|
N~The display has made an excellent impression; the price tag has staged a rebuttal.|
N~A beautiful thing can remain something you simply look at.|
N~Desirable specification, unacceptable cost. Common engineering problem.|
N~The little gap between wanting and having can look very wide in a shop.|
N~They have an eye for the design and a reasonable concern about the bill.|
N~I wonder whether they are saving for one or just enjoying the display.
''')
add('bike_approval','CeruleanCity_BikeShop_Text_WowYourBikeIsCool',
    'The youngster admires the bike we now own.','''
S~Our wheels have received a very enthusiastic outside review.|
S~They noticed the new equipment immediately. It clearly made an impression.|
S~Nice compliment. The useful part is how it rides.|
F~A little unexpected admiration can make you feel rather visible.|
S~It is fun when someone shares your pleasure in a new thing.|
S~The bicycle makes its public debut to encouraging critical notices.|
S~A small bright moment of shared appreciation.|
S~Positive user-adjacent feedback! I still want to check the mechanism.|
S~Two circles have acquired a surprising amount of attention.|
S~A sincere compliment with no little sting attached. Lovely.|
S~I wonder which detail of the bike first caught their eye.
''')
add('cerulean_burglary','CeruleanCity_House2_Text_RocketsStoleTMForDig',
    'A resident describes Team Rocket damaging his home and stealing an expensive Dig TM.','''
A~A home should not become somebody else's shortcut to stealing things.|
N~The damage and the stolen purchase are separate harms he has to deal with.|
A~They broke into his home. He deserves help getting it put right.|
D~Hearing him explain what he had planned for it makes the loss feel personal.|
N~The repair work and the lost money are a lot to leave one household with.|
N~A criminal escapade leaves an ordinary person counting damage in the room he lives in.|
D~A familiar place should not become evidence of someone else's cruelty.|
N~Broken property, stolen tool, disrupted plans. That is real damage.|
N~They put a hole through more than a wall.|
A~He had a plan for something he paid for. They took both the thing and his peace.|
N~I wonder who is helping them make the house secure again.
''')
add('cerulean_diglett_plan','CeruleanCity_House2_Text_TeachDiglettDigWithoutTM',
    'After losing the Dig TM, the resident makes a new plan to teach Diglett.','''
S~A bad day has not managed to steal his entire next plan. Good.|
S~He has found an alternative approach suited to another Pokemon.|
S~He should not have had to adapt. Glad he has something to work toward.|
S~It is nice to hear a little resolve returning to the room.|
S~A practical new plan can make a damaged day feel less stuck.|
S~The stolen prop will not be allowed to cancel the whole production.|
S~A small beginning growing around an ugly interruption.|
S~A different tool may solve the same problem. Good adaptation.|
S~The next path can begin beside the place someone broke.|
S~He is choosing what comes next without pretending the theft was fine.|
S~I wonder whether working with Diglett will become something he really enjoys.
''')
add('cerulean_dig_joke','CeruleanCity_House2_Text_TeamRocketTryingToDigIntoNoGood',
    'The other resident bitterly jokes about Team Rocket digging into trouble.','''
N~A very literal crime has left room for a very pointed joke.|
N~Wordplay can express frustration without making the damage less serious.|
N~The joke is fair. So is being angry about the house.|
N~Sometimes a little humor is the only part of a bad situation you can choose.|
N~I hope the practical repairs are getting as much attention as the anger.|
M~An apt line, delivered from a home that supplied far too much research material.|
N~A dry remark from somebody with plenty of reason not to feel amused.|
N~Unfortunate practical demonstration. The criticism is accurate enough.|
N~A sharp little word left beside a much larger hurt.|
N~At least the joke points toward the people responsible.|
N~I wonder whether they have been able to sleep comfortably since it happened.
''')
add('trade_wife','CeruleanCity_House3_Text_PleaseTradeWithMyHusband',
    'A woman encourages us to discuss trading Pokemon with her husband.','''
S~He has a very effective personal introductions department.|
N~A trade could benefit both collections if their requirements align.|
N~We can hear the offer without owing anyone a trade.|
S~It is nice that she wants to help him meet someone with the same interest.|
N~A good exchange still needs to suit both people and both Pokemon.|
S~The enthusiast's spouse has taken charge of recruiting a potential audience.|
S~A little household matchmaking, but for Pokemon collections.|
N~An invitation to compare needs. Sensible first step.|
S~A shared interest can make a stranger feel closer to the table.|
N~She sounds keen, though the actual choice stays with the people trading.|
S~I wonder whether he has been waiting for a particular partner.
''')
add('cerulean_repel','CeruleanCity_Mart_Text_RepelWorksOnWeakMons',
    'A customer explains that Repel effectiveness depends on the leading Pokemon.','''
N~The bottle and the front of the team have to agree on the plan.|
N~Lead strength influences the encounters Repel can suppress. Useful preparation detail.|
N~Check the lead before relying on the bottle.|
N~A small detail that would be easy to miss until the grass interrupted.|
N~Good to learn the condition while we still have time to organize the team.|
N~The repellent's performance apparently includes a casting requirement.|
N~Even a promise of quiet has its qualifications.|
N~Effect depends on configuration. Always check the settings first.|
N~The one walking first changes which meetings the road allows.|
N~Clear advice. The label alone might leave that part out.|
N~I wonder how many trainers discover the connection by accident.
''')
add('rare_candy','CeruleanCity_Mart_Text_DoYouKnowAboutRareCandy',
    'A shopper describes Rare Candy as unavailable in shops and capable of rapid growth.','''
U~A sweet with an unusually ambitious side effect. Not ordinary pocket candy.|
N~They describe a rare growth aid, though their wording makes the knowledge secondhand.|
N~Treat it as a useful item, not a substitute for knowing the partner.|
N~It sounds remarkable. I would want to understand it before using one.|
M~Definitely label that carefully before anybody mistakes it for dessert.|
N~A confection whose promised results greatly exceed an ordinary sugar rush.|
N~A small wrapped thing with a much less small consequence.|
U~Rapid change from a tiny item. I would like to know the mechanism.|
N~Some sweets carry more than sweetness into a day.|
N~The word rare seems to be doing real work if the shop cannot sell it.|
N~I wonder who first told them what it does.
''')
add('bill_rumors','CeruleanCity_PokemonCenter_1F_Text_BillDoesWhateverForRareMons',
    'A visitor repeats vague rumors that Bill goes to great lengths for rare Pokemon.','''
N~That is a lot of rumor with not much actual event attached.|
N~Vague secondhand claims provide little basis for judging his conduct.|
N~Ask what he actually did before repeating that.|
N~I would rather hear from him than decide who he is from whispers.|
N~Being enthusiastic does not make every rumor about you fair.|
N~An impressive cloud of insinuation, with the details conspicuously absent.|
N~A person can disappear under other people's unfinished sentences.|
N~Need specifics and a reliable source before drawing conclusions.|
N~A name travels faster when nobody asks what is carrying it.|
N~That sounds designed to invite assumptions without having to defend them.|
N~I wonder whether the speaker has ever actually met Bill.
''')
add('bill_defense','CeruleanCity_PokemonCenter_1F_Text_EveryoneCallsBillPokemaniac',
    'Another visitor thinks criticism of Bill\'s Pokemon enthusiasm is jealousy.','''
N~A collection can be impressive without making every critic jealous. Still, let him enjoy it.|
N~Jealousy is one possible explanation, not something we can establish from the nickname.|
N~Judge how he treats the Pokemon. The nickname tells us little.|
S~It is kind that someone wants to give him a fair hearing.|
N~A sincere interest deserves more than being reduced to gossip.|
N~The defense has an energetic advocate, though its evidence remains mostly enthusiasm.|
S~People are allowed a little oddness around the things they love.|
N~Both the rumor and its explanation need better data.|
S~A strange name can conceal an ordinary person caring very deeply.|
N~Good to push back on mockery without pretending we know everyone's motives.|
S~I wonder what the speaker likes most about Bill's collection.
''')
add('bill_collection_local','CeruleanCity_PokemonCenter_1F_Text_BillCollectsRareMons',
    'A local admires Bill\'s large collection, including rare Pokemon.','''
S~His reputation has a very busy household behind it.|
S~Maintaining a varied collection involves a substantial amount of knowledge and care.|
N~A lot of partners means a lot of responsibility.|
S~They sound impressed in a simple, unguarded way.|
N~The daily care behind that collection must be considerable.|
S~A brief review of a collection too extensive for a brief visit.|
S~A person's curiosity can fill a surprisingly large part of a town's conversation.|
S~Variety is interesting. I would want to know how he organizes the care.|
S~Many little lives gathered under one very curious roof.|
S~Admiration without a nasty rumor attached. A refreshing change.|
S~I wonder which of his partners the local knows best.
''')
add('cerulean_trade_advice','CeruleanCity_PokemonCenter_1F_Text_TryTradingUpstairs',
    'A visitor recommends trading with friends for varied Pokemon and faster growth.','''
S~Friends can introduce us to Pokemon our own road has not met yet.|
N~Trading can broaden a collection and alter training considerations.|
N~Talk through the trade. Make sure the new partner fits the team.|
S~Knowing the person on the other side would make the change feel easier.|
N~A trade is worth considering for the partnership, not just quick progress.|
S~The upstairs invitation promises a wider cast through friendly negotiation.|
S~The world can grow larger through someone else's familiar companion.|
N~Useful option. Different partners bring different requirements as well as benefits.|
S~A friend can open a road that does not appear on the map.|
N~A good exchange gives both sides something they actually want.|
S~I wonder what unusual partner someone upstairs has brought today.
''')
add('oldrod_given','VermilionCity_House1_Text_FishingIsAWayOfLife',
    'After giving the Old Rod, the Fishing Guru encourages fishing in seas and rivers.','''
S~He has given us the starter equipment for a very patient kind of adventure.|
S~Trying multiple habitats is sensible advice for a new angler.|
S~Generous gift. No need to rush the first catch.|
S~He seems glad to have somebody new to share it with.|
S~A quiet hour beside the water could be a good use of this.|
S~A new pupil is sent forth with a rod and a warmly oversized philosophy.|
S~A little tool for meeting the things beneath a quiet surface.|
S~Basic equipment, broad field opportunities. Good beginning.|
S~The still water has become somewhere we can ask a small question.|
S~He gives the welcome as enthusiastically as the equipment.|
S~I wonder where he would recommend casting for the very first time.
''')
add('oldrod_declined','VermilionCity_House1_Text_OhThatsSoDisappointing',
    'The Fishing Guru is disappointed when we say fishing does not interest us.','''
N~He had a whole fishing friendship ready to unfold. Perhaps another visitor.|
N~An honest answer can disappoint without being unkind.|
N~We do not need to pretend. He can keep enjoying it.|
F~It is difficult to say no when the question comes with that much hope.|
N~A different hobby can still make a perfectly good afternoon.|
N~The proposed fellowship has found a small incompatibility at its founding meeting.|
N~Not every shoreline needs to become everyone's favorite place.|
N~Interest not shared. No benefit in forcing the next step.|
N~The river still has plenty of other people to call toward it.|
N~A polite refusal is better than a borrowed enthusiasm that disappears tomorrow.|
N~I wonder what he talks about with visitors who do not fish.
''')
add('oldrod_greeting','VermilionCity_House1_Text_HowAreTheFishBiting',
    'The Fishing Guru remembers us and asks about our fishing.','''
S~We have a regular fishing correspondent now. Updates may contain splashing.|
S~He is interested in how we used the equipment he shared.|
S~Good of him to remember. Makes a return visit easy.|
S~A familiar greeting can make the little house feel welcoming at once.|
S~A hobby is nicer when somebody wants to hear the ordinary stories too.|
S~The mentor requests the next dispatch from the waterfront.|
S~An ordinary question that makes it clear he kept a place for us in mind.|
S~Follow-up support! He seems genuinely invested in the outcome.|
S~The water has given us another small reason to visit someone.|
S~He has turned a one-time gift into an ongoing acquaintance.|
S~I wonder whether he has a good catch story ready to share in return.
''')
add('vermilion_trade_no','VermilionCity_House2_Text_ThatsTooBad',
    'The local trader accepts our decision not to trade.','''
N~A proposed swap has ended without any swapping. Everyone keeps their original companions.|
N~The refusal leaves the trade uncompleted and the existing arrangement intact.|
N~No deal today. We are allowed to decide that.|
N~A little disappointment, but nobody needs to force it.|
N~Better to wait for an exchange both sides actually want.|
N~The negotiation concludes before the cast changes hands.|
N~A small no can save a much more difficult regret.|
N~Requirements did not align. Cancel cleanly and move on.|
N~Some roads meet without anyone needing to change directions.|
N~They accepted the answer. That matters.|
N~I wonder whether they have been hoping to make this trade for long.
''')
add('vermilion_wrong_trade','VermilionCity_House2_Text_ThisIsNoMon',
    'The trader rejects the selected Pokemon because it is not the requested species.','''
N~A different introduction from the one they had arranged. Fair enough to decline.|
N~The selected species did not meet the specified trade condition.|
N~Wrong partner for this offer. We can leave it there.|
F~An awkward selection, but not a serious problem.|
N~Both sides should get what they actually agreed to.|
N~The casting call has a specific role, and this visitor belongs to another story.|
N~A mismatch, not a flaw in the Pokemon. An important little difference.|
N~Validation caught the wrong input. No transfer should follow.|
N~A companion is not made less worthy by arriving at the wrong door.|
N~The request was specific. The refusal can stay simple.|
N~I wonder how often a visitor selects the wrong one by accident.
''')
add('vermilion_trade_done','VermilionCity_House2_Text_ThankYou',
    'The local trader thanks us after completing the in-game trade.','''
S~A new hello and a grateful goodbye in the same little moment.|
S~The trade completed before the thanks. Both trainers now have new care responsibilities.|
S~Deal done. Get to know the new partner properly.|
S~I hope both Pokemon find the next part of their lives comfortable.|
S~A little familiar advice can help a new partner settle in.|
S~The exchange concludes with a modest line for a fairly large change.|
S~A new name in the group, an old companion beginning somewhere else.|
N~Transfer confirmed. Time to check the new partner's needs and habits.|
S~Two small journeys have crossed and continued in different hands.|
S~A sincere thank-you makes the handoff feel considered.|
S~I wonder which habit we will notice about our new companion first.
''')
add('vermilion_trade_followup','VermilionCity_House2_Text_HowIsMyOldMon',
    'The trader asks after the Pokemon given to us and reports that ours is doing well.','''
S~They remembered the friend who left, not just the one who arrived. I like that.|
S~A follow-up on both Pokemon gives the exchange a reassuring continuity.|
S~Good to hear the partner is doing well. Good that they asked about ours too.|
S~It is lovely when a new home does not erase the old person's care.|
S~A short visit can reassure both sides after a big change.|
S~The former cast members receive a warm update from their next chapters.|
S~Affection does not always stop at the edge of an exchange.|
S~Post-transfer check-in. Excellent practical and personal follow-through.|
S~A thread between two homes remains pleasantly unbroken.|
S~They sound interested rather than possessive. That is a good balance.|
S~I wonder what new little habit their new partner has shown them.
''')
add('pidgey_post','VermilionCity_House3_Text_PidgeyFlyLetterToSaffron',
    'A resident sends a letter north to Saffron with Pidgey.','''
S~A little bird carrying a piece of somebody's day across town lines.|
S~A familiar route and a trained messenger can make a dependable communication system.|
N~Hope the route is safe for Pidgey. Important cargo still needs a safe trip.|
S~A letter feels more personal when you can picture the bird carrying it.|
S~It is nice to keep in touch in a way someone has taken time over.|
S~The correspondence has acquired an exceptionally feathered courier.|
S~A small warm body carrying words that cannot fly by themselves.|
S~Light payload, capable carrier, clear destination. Practical arrangement.|
S~A little folded voice traveling under a pair of wings.|
S~An ordinary errand with rather lovely details.|
S~I wonder whether Pidgey recognizes the person at the other end.
''')
add('mail_exchange','VermilionCity_House3_Text_SendMyPidgeyToUnionRoom',
    'The resident wants to exchange Mail with many people through the Union Room.','''
S~Pidgey is helping them meet more pen pals than their own feet can manage.|
S~A wider correspondence network can introduce a useful variety of perspectives.|
N~A nice interest. Keep the messages and the messenger safe.|
S~I like that the goal is hearing from different people.|
S~A small note can make a stranger's day unexpectedly friendly.|
S~The postal project has ambitions beyond its original neighborhood.|
S~A collection of words from people who might otherwise remain far away.|
N~More contacts means more organization. I hope they label the replies.|
S~Many little voices, folded into the same welcoming place.|
S~Mail makes a personal exchange feel like something you can keep.|
S~I wonder what they like asking someone in a first letter.
''')
add('rocket_cruelty','VermilionCity_Mart_Text_TeamRocketAreWickedPeople',
    'A shopper condemns Team Rocket for trafficking and abandoning Pokemon deemed useless.','''
A~A Pokemon's worth is not whatever a criminal can sell it for.|
N~They describe exploitation followed by neglect. Both place the Pokemon's welfare at risk.|
A~Using partners and throwing them away is rotten. No excuse.|
D~I hate thinking of a Pokemon waiting for someone who simply decided it was not useful.|
A~A living companion deserves care even when it cannot do what someone hoped.|
N~A business model with cruelty in every stage of the transaction.|
A~Calling a creature useless says far more about the speaker.|
N~A plan that treats living beings as disposable parts is a bad plan at its foundation.|
D~Something abandoned still has a life after the person stops looking.|
A~Popularity is a dreadful measure of whether a creature deserves a home.|
N~I wonder who helps the Pokemon left behind by them.
''')
add('trainer_influence','VermilionCity_Mart_Text_MonsGoodOrBadDependingOnTrainer',
    'A shopper thinks a Pokemon\'s behavior depends on its trainer.','''
N~The person holding the treats does have a lot of influence. Still, Pokemon have their own minds.|
N~Training strongly influences behavior without making a Pokemon merely an extension of its trainer.|
N~Trainers are responsible for what they teach and allow.|
N~I hope people remember that a badly treated Pokemon can need help too.|
N~A kind routine can make a real difference to how a partner feels around people.|
N~The director bears responsibility, though the cast is more than a set of puppets.|
N~A creature can learn fear from someone and still deserve a gentler life.|
N~Input matters, but a living partner is not a predictable machine.|
N~The hands beside a creature can teach it whether the world is safe.|
N~A good reminder for people blaming the Pokemon while ignoring the trainer.|
N~I wonder what experience made the shopper think about that.
''')
add('vermilion_individual_stats','VermilionCity_PokemonCenter_1F_Text_TrainerMonsStrongerThanWild',
    'A visitor explains differences between same-level Pokemon and the effects of training.','''
N~A level is one number, not the entire Pokemon's introduction.|
N~Equal levels do not imply equal attributes. Training history and individual traits matter.|
N~Look at the actual partner. Do not let one number do all the thinking.|
N~It is reassuring that the little differences between partners still count.|
N~Careful training means paying attention to those differences.|
N~The single-number biography has been found wanting. Entirely fair.|
N~Two lives can reach the same milestone by very different roads.|
N~One summary value cannot describe a whole system. Check the actual properties.|
N~The same mark on a ruler can meet two very different shapes.|
N~A good reminder against judging a team at a glance.|
N~I wonder which pair of Pokemon first made that difference obvious.
''')
add('vermilion_poison','VermilionCity_PokemonCenter_1F_Text_PoisonedMonFaintedWhileWalking',
    'A worried trainer reports that poison caused their Pokemon to faint on the road.','''
D~That must have been a frightening walk. Good that they reached help.|
N~A lingering condition can worsen outside battle. The Center is the appropriate next stop.|
N~They are here now. Get the partner treated before going anywhere else.|
D~I can hear how much it shook them to have it happen between battles.|
N~Rest and proper care first. Supplies for next time can come afterward.|
N~The danger followed them past the end of the battle. An unpleasant lesson.|
D~An ordinary path can become a very long one when someone beside you is hurting.|
N~Persistent damage caught them between encounters. Recovery and prevention both matter.|
D~A small worsening can make each step toward help feel farther.|
N~I hope somebody reassures them while the Pokemon is being treated.|
N~I wonder how far they had to come before reaching the Center.
''')
add('no_universal_strength','VermilionCity_PokemonCenter_1F_Text_AllMonWeakToSpecificTypes',
    'A visitor says type weaknesses prevent any Pokemon from being universally strong.','''
N~Even the biggest champion has a bad matchup waiting somewhere.|
N~Power is conditional. Type relationships can outweigh a simple level advantage.|
N~Have backup. Strong does not mean safe from everything.|
N~It is comforting that a single imposing opponent is not the whole story.|
N~A thoughtful team matters more than one impressive partner carrying everyone.|
N~The invincible lead has been politely informed that the script contains exceptions.|
N~Nothing has to be flawless to be worth trusting.|
N~Every design has tradeoffs. Build the team around covering them.|
N~Even an old wall has a place where the ivy gets through.|
N~A useful correction to the idea that bigger numbers solve every problem.|
N~I wonder which matchup most surprised the visitor.
''')
add('seeker_received','VermilionCity_PokemonCenter_1F_Text_UseDeviceForRematches',
    'After giving the VS Seeker, the trainer explains rematch detection and battery charging.','''
S~A little device for asking old opponents whether they fancy another round. Civilized.|
S~The rematch aid requires charge and detects interested trainers rather than forcing a battle.|
N~Useful. Still check the team before asking for another match.|
S~I like that both sides get to want the rematch.|
S~Seeing a familiar trainer again can be a nice reason to revisit a road.|
S~A practical instrument for arranging a sequel with a consenting cast.|
S~An old encounter does not have to stay finished forever.|
S~Clear purpose, limited battery. Charge before scheduling a field test.|
S~A small call sent out to people whose paths have crossed ours.|
N~Good instructions. The charging detail matters before the next outing.|
S~I wonder which familiar trainer we would most like to meet again.
''')
add('seeker_repeat','VermilionCity_PokemonCenter_1F_Text_ExplainVSSeeker',
    'On a return visit, the trainer explains using the VS Seeker on roads after charging it.','''
S~Beep-beep-beep is a wonderfully precise part of that explanation.|
N~The instructions specify location, charge, and the other trainer's interest. Useful conditions.|
N~Charge it, use it on the road, check who is ready. Clear enough.|
S~A friendly offer to explain again makes asking less embarrassing.|
N~A little preparation keeps a planned rematch from becoming a wasted trip.|
M~The technical manual has been condensed into several encouraging beeps.|
S~An invitation carried in a tiny electronic chirp.|
S~Operation instructions with sound effects! Surprisingly memorable.|
S~A small signal asks whether an old meeting has another shape left in it.|
N~They make it sound simple without forgetting the requirements.|
S~I wonder whether they have a favorite person to challenge again.
''')
add('fan_pikachu','VermilionCity_PokemonFanClub_Text_AdmirePikachusTail',
    'A devoted fan asks us to admire his Pikachu\'s tail.','''
S~An unusually specific appreciation assignment. The tail is doing fine work.|
S~Affection often sharpens attention to small physical details.|
S~Good tail. Happy trainer. No harm in a little admiration.|
S~It is sweet to see someone so pleased by a familiar little detail.|
S~A partner you know well can keep giving you small reasons to smile.|
M~The fan club presents a featured tail with entirely unrestrained enthusiasm.|
S~A small bright shape with a surprisingly large audience.|
S~Distinctive form, expressive movement. I see the appeal.|
S~A little zigzag carrying a great deal of affection.|
S~A striking silhouette does deserve appreciation.|
S~I wonder whether Pikachu knows how often that tail gets introduced.
''')
add('fan_pikachu_rivalry','VermilionCity_PokemonFanClub_Text_PikachuTwiceAsCute',
    'After hearing about the other fan, Pikachu\'s owner claims twice the cuteness.','''
M~Twice as cute! I would like to inspect the official cuteness ruler.|
N~The comparison lacks a defined scale and appears strongly influenced by affection.|
N~Both Pokemon can be liked. No tournament needed.|
N~I would rather not make anyone feel their partner has to lose this.|
S~Everybody can go home believing their own companion is special.|
M~The cuteness arms race has entered its first mathematically unsupported escalation.|
M~A bold use of arithmetic in the service of complete bias.|
N~No measurement method supplied. I am marking this as an enthusiastic opinion.|
S~Affection has looked at a ruler and decided to cheat.|
M~A little rivalry is amusing until someone expects us to judge.|
S~I wonder how often these two restart this exact debate.
''')
add('fan_seel','VermilionCity_PokemonFanClub_Text_AdoreMySeel',
    'A fan lovingly describes Seel\'s squeal when hugged.','''
S~That is a very warm review for a Pokemon shaped for cold water.|
S~She notices a familiar response that has become meaningful between them.|
S~Good to see a partner loved for more than battles.|
S~She remembers the exact little sound. That is lovely.|
S~The everyday affectionate moments are worth talking about too.|
S~A detailed testimonial from the hug department.|
S~A small familiar noise can become a whole reason to smile.|
S~Recognizable positive interaction, fondly reported. Excellent outcome.|
S~A little sound that means the room feels safe.|
S~She enjoys the partner, not just the idea of owning one.|
S~I wonder whether Seel recognizes the tone she uses to talk about it.
''')
add('fan_seel_rivalry','VermilionCity_PokemonFanClub_Text_SeelFarMoreAttractive',
    'Seel\'s owner retaliates by claiming double the attractiveness.','''
M~The cuteness calculations have become a diplomatic incident.|
N~An equally unsupported counterestimate. Neither claim requires us to choose a winner.|
N~They can both be proud without making it a fight.|
F~I would quietly admire both and avoid being appointed judge.|
S~Perhaps the Pokemon could get along while the people compare imaginary scores.|
M~The rival nation of Seel has issued a proportionally inflated response.|
M~Love has once again discovered suspiciously convenient mathematics.|
N~Independent measurement has been replaced by escalating confidence.|
S~Two hearts have invented a contest nobody needed.|
M~The devotion is charming. The arithmetic is a complete accessory.|
S~I wonder whether they enjoy the argument more than they admit.
''')
add('fan_voucher','VermilionCity_PokemonFanClub_Text_ExplainBikeVoucher',
    'After his long story, the chairman gives a Bike Voucher and explains redemption in Cerulean.','''
U~A long horse story has turned into a bicycle. Unexpectedly practical ending!|
S~The voucher has a specific redemption point, and he clearly has no personal need for it.|
S~Generous reward for listening. Take it to the right shop.|
S~He noticed he kept us and tried to thank us properly.|
S~A useful gift from somebody genuinely happy to share his enthusiasm.|
M~Our patient audience has earned a wheeled exit from future lengthy performances.|
S~A rambling affection has left us with a very practical kindness.|
S~A clear handoff with redemption instructions. Excellent finish.|
S~One person's overflowing story has opened a longer road for someone else.|
S~He remembered the listener at the end. That saves the whole speech for me.|
S~I wonder how many people have left this club planning their first ride.
''')
add('fan_story_declined','VermilionCity_PokemonFanClub_Text_ComeBackToHearStory',
    'The chairman accepts our decision not to hear his Pokemon story.','''
N~The story has been stored for later, at very full length I imagine.|
N~He accepted the refusal and left the invitation available.|
N~Good. We can choose when we have time to listen.|
S~A kind ending. Being enthusiastic does not have to mean insisting.|
N~Another day may leave more room for a proper conversation.|
M~The monologue returns to its dressing room, still impeccably prepared.|
N~Some long stories improve when both people have chosen the afternoon for them.|
N~Presentation deferred. Useful to establish audience availability first.|
S~A story can wait quietly until someone has room to hear it.|
S~He did not make us feel rude for having another plan.|
S~I wonder whether he has the opening memorized by now.
''')
add('fan_story_return','VermilionCity_PokemonFanClub_Text_DidntComeToSeeAboutMonsAgain',
    'The chairman greets us again but realizes we did not return for another Pokemon story.','''
N~He had the next story warmed up before the greeting finished.|
S~He remembers the earlier audience and hopes to repeat the conversation.|
N~Nice to be remembered. We still get to choose how long to stay.|
F~I would feel a little bad saying no, even after hearing him once.|
S~A familiar welcome is pleasant, even if today's visit is short.|
M~A returning audience member has narrowly escaped being booked for the sequel.|
S~His enthusiasm seems to have survived the interval completely unharmed.|
N~Repeat presentation offered, not currently requested. Clear enough.|
S~A familiar voice finding its favorite path almost immediately.|
S~He sounds disappointed, but he remembers us kindly.|
S~I wonder whether he has acquired any new stories since the last one.
''')
add('fan_no_room','VermilionCity_PokemonFanClub_Text_MakeRoomForThis',
    'The chairman cannot give his Bike Voucher because the bag is full.','''
N~We found room for the long story and somehow no room for the tiny voucher.|
N~The intended reward did not transfer. Space must be cleared first.|
N~Sort the bag. His gift can wait a moment.|
F~It is awkward to be unprepared after he tried to thank us.|
N~A little tidying will make accepting the kindness much simpler.|
N~A grand monologue has been followed by a minor luggage crisis.|
N~The smallest paper can be too much for a crowded pocket.|
N~Capacity problem at the final handoff. Easy fix with a little sorting.|
N~A road-opening gift has stopped at a very small closed door.|
N~No reason to make the generous part of this feel hurried.|
N~I wonder which pocket has room for a more sensible arrangement.
''')
add('fan_chairman_vocal','VermilionCity_PokemonFanClub_Text_ChairmanVeryVocalAboutPokemon',
    'A club member remarks on the chairman\'s very vocal enthusiasm.','''
M~The building has probably learned every Rapidash story by vibration.|
S~His interest is clearly expressed often enough to be a defining social trait.|
N~No doubt about what he cares about. Hope he lets others speak too.|
F~A quiet visitor might have trouble finding a place to begin.|
S~Enthusiasm can make a room welcoming when it leaves room for another voice.|
M~A chairman whose volume faithfully reflects the size of his affection.|
M~Silence is not among his particular hobbies.|
N~Strong output signal. Need to check how well the input works.|
S~Some people fill a room by caring about something very loudly.|
N~A club needs listeners as well as somebody certain to keep talking.|
S~I wonder which story the regular members hear most often.
''')
add('fan_daisy_affection','VermilionCity_PokemonFanClub_Text_ChairmanReallyAdoresHisMons',
    'A member affirms the chairman\'s love for Pokemon but thinks Pokemon like Daisy most.','''
S~Loving Pokemon and being their favorite are two related, very different contests.|
S~The speaker distinguishes affection expressed toward Pokemon from the trust they return.|
S~The partners get their own opinion. Good to remember.|
S~Daisy must make them feel comfortable without needing to announce it.|
S~Quiet care often tells a Pokemon more than a grand speech.|
S~The chairman has the loudest declaration; Daisy appears to have the more persuasive audience.|
S~Gentleness can be recognized without ever advertising itself.|
N~Reported response is useful feedback. Enthusiasm alone is not the whole method.|
S~Some people become a safe place without trying to be the center of it.|
S~Daisy's reputation seems to come from the Pokemon themselves. A good source.|
S~I wonder what little things Daisy does that make them settle so easily.
''')
add('lavender_cubone_loss','LavenderTown_House1_Text_RocketsKilledCubonesMother LavenderTown_PokemonCenter_1F_Text_CubonesMotherKilledByRockets',
    'A local recounts that Cubone\'s mother was killed trying to escape Team Rocket.','''
D~That poor little one. There is no clever thing to say that makes that smaller.|
D~The loss is devastating. Cubone needs safety and patient care rather than more demands.|
D~Make sure Cubone is safe now. What happened to its mother was cruel.|
D~It is hard to hear. I hope the little one has somebody gentle nearby.|
D~A quiet, safe home is the least Cubone deserves after that.|
D~No adventure makes this acceptable collateral. It is a family torn apart.|
D~Grief is already heavy enough without a small creature carrying it alone.|
D~There is nothing to improve about that account except making sure the danger stops.|
D~A little life has lost the shelter it knew first.|
D~The people looking after Cubone now need all the patience they can give.|
D~I am glad someone is telling what happened instead of letting it disappear.
''')
add('lavender_spirit_soothed','LavenderTown_House1_Text_GhostOfPokemonTowerIsGone',
    'A local believes the Tower\'s ghost has been soothed and is gone.','''
S~I am glad the story can end with some peace instead of another fight.|
S~The local interprets the disappearance as a restless spirit finding relief.|
S~Good. There has been enough pain tied to that place.|
S~A gentler ending feels important here.|
S~I hope the people who were frightened can begin to feel comfortable again.|
S~A troubled presence has been given a quieter final line.|
S~Some stories are kindest when they finally become still.|
N~The disturbance has ended. That matters to everyone still living nearby.|
S~The old hurt may no longer be walking the halls.|
S~I like that they say soothed rather than simply driven off.|
S~I wonder whether the Tower feels different to its visitors now.
''')
add('name_rater_changed','LavenderTown_House2_Text_FromNowOnShallBeKnownAsName',
    'The Name Rater confirms a changed nickname and enthusiastically praises the result.','''
S~A new name, delivered with enough confidence to carry the whole Pokemon.|
N~The selected nickname has been applied. The quality judgment remains enthusiastically subjective.|
N~Done. Make sure it is a name we actually want to keep calling.|
F~He sounds so pleased with it that I would find it difficult to disagree.|
S~A name can feel more familiar each time you use it kindly.|
M~The editor has approved the revised title with customary restraint: none whatsoever.|
S~A little word finding a new place to live.|
N~Label updated. Now test whether it remains easy to say in a hurry.|
S~The same companion steps into a different little sound.|
S~A good name should feel like it belongs when the excitement settles.|
S~I wonder how the partner will react when it hears the new name.
''')
add('name_rater_same','LavenderTown_House2_Text_FromNowOnShallBeKnownAsSameName',
    'The Name Rater praises an unchanged nickname as somehow vastly improved.','''
M~Same name, upgraded approval. Invisible improvements are remarkably convenient.|
M~No observable lexical change. The confidence level, however, has increased dramatically.|
M~Name stayed the same. Glad he is satisfied with the work.|
F~I think he simply wants everyone to leave feeling pleased.|
S~If we already liked the name, keeping it is a perfectly good result.|
M~A masterful revision in which the editor changes only the review.|
M~Nothing happened, but with considerable professional assurance.|
N~No modification detected. Claimed performance increase remains unverified.|
S~The old word has been welcomed back wearing an invisible ribbon.|
M~A complete rebrand of the exact same thing. Confident presentation.|
S~I wonder how often he gives that speech with a perfectly straight face.
''')
add('name_rater_trade','LavenderTown_House2_Text_TrulyImpeccableName',
    'The Name Rater refuses to alter a traded Pokemon\'s nickname while calling it impeccable.','''
N~A compliment that also closes the naming desk. Nicely disguised refusal.|
N~The existing trainer history prevents renaming through this service.|
N~Keep the name it arrived with. That is the rule here.|
S~At least he says it in a way that makes the partner sound special.|
N~A familiar name may be a comforting part of the change of home.|
M~The critic has found perfection precisely where he lacks editorial authority.|
S~A little thread from the old home remains in place.|
N~Permission limit encountered. No change applied.|
S~An old name stays beside a new pair of footsteps.|
N~A tactful way to explain a limit without criticizing somebody else's choice.|
S~I wonder what story the original trainer had behind that name.
''')
add('name_rater_egg','LavenderTown_House2_Text_ThatIsMerelyAnEgg',
    'The Name Rater refuses to rate an Egg.','''
M~The Egg has declined to submit a working title. Fair enough.|
N~The service does not apply to an unhatched Egg.|
N~Let it hatch before worrying about a nickname review.|
S~There will be plenty of time to find the right name later.|
S~For now, warm and safe is a much more important description.|
M~The title cannot be reviewed before the main character has entered.|
S~A quiet beginning, temporarily protected from criticism.|
N~Unsupported input. Good that the rater checks first.|
S~A name can wait outside the shell until someone is ready to answer.|
N~Perhaps merely is a little unfair. The Egg has quite a lot ahead of it.|
S~I wonder what name will come to mind when it finally hatches.
''')
add('name_rater_cancel','LavenderTown_House2_Text_ISeeComeVisitAgain',
    'The Name Rater accepts cancellation without changing a nickname.','''
N~The old name has survived another appointment with the critic.|
N~No change was applied. The current nickname remains intact.|
N~No rush. A name can wait until we are sure.|
S~It is good to be able to hesitate without making the visit awkward.|
N~Keeping a name you like is already a valid choice.|
N~The editorial meeting concludes with the manuscript happily unaltered.|
S~Some familiar words do not need to become different today.|
N~Cancellation preserved the existing setting. Predictable and useful.|
S~The little sound that already belongs can stay where it is.|
N~A polite ending leaves room to think without pressure.|
N~I wonder how many visitors discover they liked the old name all along.
''')
add('lavender_battle_items','LavenderTown_Mart_Text_SearchingForStatRaiseItems',
    'A shopper searches for temporary battle stat items and asks where to buy them.','''
N~A clear shopping list, unfortunately delivered to the wrong shelf.|
N~They distinguish temporary battle effects from lasting training changes. Useful specificity.|
N~Worth asking the clerk before walking the whole town.|
N~It is frustrating to know exactly what you need and not where to find it.|
N~A little local advice could save them a long unnecessary trip.|
N~The supplies are specified; the acquisition chapter remains unwritten.|
N~A modest shopping problem can consume a surprisingly large afternoon.|
N~Good requirements, missing supplier. A familiar logistical snag.|
N~The right little bottle is somewhere beyond this particular counter.|
N~They have done the homework on what they want. Directions are the missing piece.|
N~I wonder which battle they are preparing those items for.
''')
add('lavender_revives','LavenderTown_Mart_Text_DidYouBuyRevives',
    'A shopper reminds us to buy Revives for fainted Pokemon.','''
N~A practical reminder delivered before the road gets the chance to be unpleasant.|
N~A reserve can prevent one fainted partner from ending the entire outing.|
N~Good to carry some if the route is long.|
N~It is comforting to have a way to help after a difficult match.|
N~We should plan the supplies around the team, not just the destination.|
N~A small purchase recommended by the department of avoiding a miserable walk home.|
N~Some things are most welcome precisely when you wish you did not need them.|
N~Recovery supplies are a sensible backup. Check the count before leaving.|
N~A small way to help a tired companion return to its feet.|
N~The advice is useful without inspecting how badly our last battle went.|
N~I wonder whether they learned to carry one after a rough trip.
''')
add('lavender_doubles','LavenderTown_Mart_Text_TrainerDuosCanChallengeYou',
    'A shopper explains that paired trainers require two Pokemon in a double battle.','''
N~Two opponents means twice as many people trying to look confidently at us.|
N~A double battle changes coordination and targeting, not simply the number of participants.|
N~Have two ready. Do not leave the second partner as an afterthought.|
N~It sounds harder to follow when everyone acts at once.|
N~Good reason to prepare the whole team rather than one favorite.|
N~The encounter may expand into an ensemble with very little warning.|
N~A second companion should be more than a person filling an empty chair.|
N~Two active units create interaction effects. Plan their moves together.|
N~A pair of footsteps needs a shared direction.|
N~A useful warning for someone expecting every challenge to look the same.|
N~I wonder whether the shopper has a favorite pair to send out together.
''')
add('lavender_rocket_greed','LavenderTown_PokemonCenter_1F_Text_RocketsDoAnythingForMoney',
    'A local condemns Team Rocket\'s willingness to commit any crime for money.','''
A~Money is a poor excuse for making the world less safe for everyone else.|
N~The accusation reflects a pattern of exploitation, not a harmless preference for profit.|
A~People and Pokemon get hurt. That is what their greed costs.|
D~They sound angry in a way that comes from being frightened for too long.|
A~There are lines nobody should cross just because somebody pays.|
N~An enterprise whose only consistent principle appears to be the cash at the end.|
A~A purse is a very small thing to build a whole conscience around.|
N~A goal that ignores every constraint can produce immense damage.|
N~They keep taking things money cannot return afterward.|
A~The people left coping with the harm do not get a share of the profit.|
N~I wonder what this town has seen that the rest of the region has not heard yet.
''')
add('cubone_skull_market','LavenderTown_PokemonCenter_1F_Text_PeoplePayForCuboneSkulls',
    'A visitor remarks that Cubone skulls command high prices.','''
A~That belongs to a living creature's story, not somebody's shopping list.|
N~Demand can encourage harm when buyers ignore where an object came from.|
A~A price tag does not make taking one acceptable.|
D~That is an awful thing to hear here, knowing what happened.|
A~A Pokemon's safety should matter more than what someone will pay.|
N~A cold little market fact with a much warmer cost hidden inside it.|
A~Some things become uglier the moment someone assigns them a price.|
N~An incentive for cruelty is still cruelty, even when described as demand.|
D~A keepsake of loss should not become another reason to cause it.|
A~Calling it valuable leaves out the creature it matters to most.|
N~I wonder whether the buyers ever ask the question they most need answered.
''')
add('fuji_newcomer','LavenderTown_PokemonCenter_1F_Text_HearMrFujiNotFromAroundHere',
    'A newcomer hears Mr. Fuji also originally came from elsewhere.','''
S~Two people from elsewhere can both become part of the same little town.|
S~A shared experience of arriving may offer the newcomer a point of connection.|
N~Being new does not mean you cannot belong.|
S~It is comforting to find someone who has made a home after arriving from away.|
S~A place becomes home through what people do there, not just where they began.|
S~The newcomer has found a possible guide to the art of becoming local.|
S~A town is partly made of people who once stood at its edge.|
N~Local knowledge can be acquired. Origins do not prevent useful belonging.|
S~Roots can grow in soil they did not start in.|
S~That could be a nice first conversation between them.|
S~I wonder what brought the newcomer here.
''')
add('fuji_missing','LavenderTown_VolunteerPokemonHouse_Text_WhereDidMrFujiGo',
    'A volunteer notices that Mr. Fuji is unexpectedly absent.','''
N~A familiar room feels different when its usual person is missing.|
N~His absence is unusual enough for someone here to notice immediately.|
N~Worth checking on him before assuming he is simply busy.|
N~Their uncertainty makes the quiet in here feel heavier.|
N~I hope somebody knows where he planned to go.|
N~An ordinary absence has become the room's most pressing unanswered line.|
N~People leave a particular shape in the spaces they care for.|
N~Unexpected absence. Start by checking his last known plan.|
N~The room is listening for familiar footsteps.|
N~It is good that the people here notice when someone does not return.|
N~I wonder when they last saw him.
''')
add('fuji_prayer','LavenderTown_VolunteerPokemonHouse_Text_MrFujiWasPrayingForCubonesMother',
    'A volunteer says Mr. Fuji had been praying alone for Cubone\'s mother.','''
D~He made time for someone who could no longer ask for it. That matters.|
S~His action shows sustained concern beyond what could be fixed practically.|
S~He did not forget her just because the danger had passed.|
D~It is a gentle thing to do in a place with so much grief.|
S~Remembering someone quietly is still a form of care.|
S~A private act with no audience to reward it. That tells us something.|
S~Some kindness is simply refusing to let a life vanish without being mourned.|
N~Not every worthwhile act solves a problem. Some acknowledge what happened.|
D~He kept a little space open for a life that was gone.|
S~There is care in choosing to remember without needing anyone to watch.|
S~I wonder whether Cubone knew someone was thinking of its mother.
''')
add('fuji_orphans','LavenderTown_VolunteerPokemonHouse_Text_MrFujiLooksAfterOrphanedMons',
    'A volunteer explains that Fuji welcomes abandoned and orphaned Pokemon into his home.','''
S~A house that keeps saying there is room for one more. That is a wonderful use of a house.|
S~Stable care can provide a crucial refuge after abandonment or loss.|
S~He is doing work that matters. Day after ordinary day.|
S~It is lovely that the welcome lasts beyond the first rescue.|
S~A safe place needs someone willing to do the daily work. He does.|
S~The remarkable thing is not the rescue scene but the home maintained afterward.|
S~A room full of small lives that no longer have to be unwanted.|
S~Practical, ongoing support. The unglamorous part is often the most important.|
S~A door that opens kindly can change the rest of a life.|
S~He makes room in his own everyday life. That says more than a grand promise.|
S~I wonder which resident took the longest to feel at home.
''')
add('pokemon_hug','LavenderTown_VolunteerPokemonHouse_Text_MonsNiceToHug',
    'A child delights in the warmth of hugging a Pokemon.','''
S~A tiny report from the department of excellent cuddles.|
S~Warmth and familiar contact can make a safe interaction especially comforting.|
S~Good to see them comfortable together.|
S~A simple happy moment. I am glad this house has those too.|
S~Warm company can make an ordinary room feel like the best place to be.|
S~A glowing review delivered with no need for elaborate adjectives.|
S~Something soft and alive making the world less severe for a moment.|
S~Positive interaction, no complicated apparatus required. Excellent.|
S~A little warmth shared without needing words.|
S~Comfort looks rather lovely on both of them.|
S~I wonder whether this is part of their everyday routine here.
''')
add('fuji_flute','LavenderTown_VolunteerPokemonHouse_Text_ExplainPokeFlute',
    'After giving the Poke Flute, Mr. Fuji explains that it wakes sleeping Pokemon.','''
S~A gentle-sounding answer to a very large sleeping obstacle. Useful gift.|
S~He describes a clear effect and a practical situation in which to use it.|
N~Useful. Give the waking Pokemon room instead of crowding it.|
S~I would like to hear what kind of breath brings it to life.|
S~A kind gift with a real purpose for the road ahead.|
S~The old caretaker sends us onward with an instrument suited to a new beginning.|
S~A small sound can open a road that force would only make angry.|
S~A specific acoustic tool for a specific problem. Elegant.|
S~A sleeping path may only need the right little song.|
S~He chose something helpful without making the gift about himself.|
S~I wonder how he first came to have the flute.
''')
add('fuji_flute_return','LavenderTown_VolunteerPokemonHouse_Text_HasPokeFluteHelpedYou',
    'Mr. Fuji asks whether his Poke Flute has been useful.','''
S~He remembered the gift and the person carrying it. That feels good.|
S~A simple follow-up on how the item worked in practice.|
S~Good of him to ask. He wanted it to help, not just leave his shelf.|
S~It is a gentle question, with room for a real answer.|
S~A gift means more when the giver stays interested in the journey afterward.|
S~The quiet benefactor asks for news from the instrument's next chapter.|
S~An old kindness checking whether it found a useful place to rest.|
N~Field feedback requested. He seems genuinely interested in the result.|
S~A little thread from this house travels beside us still.|
S~There is no pressure to praise him. Just a kind question.|
S~I wonder whether he enjoys hearing where the flute has traveled.
''')
add('fuji_no_room','LavenderTown_VolunteerPokemonHouse_Text_MustMakeRoomForThis',
    'Mr. Fuji cannot give the Poke Flute because the bag is full.','''
N~A small bag problem at the end of a much kinder conversation. We can fix that.|
N~The intended transfer did not complete. Space must be made before receiving the flute.|
N~Sort the bag. There is no need to hurry him.|
F~I wish we had been ready for his kindness.|
N~A little tidying is a modest thing to do before accepting a useful gift.|
N~The heartfelt handoff has encountered an entirely practical obstruction.|
N~A crowded pocket should not make a generous offer feel unwelcome.|
N~Capacity check failed. Resolve it and return calmly.|
N~A small place needs clearing for something meant to make a larger way open.|
N~We can handle the inconvenience without making him repeat himself.|
N~I wonder which unnecessary thing we can finally put away.
''')

