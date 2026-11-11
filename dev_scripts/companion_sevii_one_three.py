"""Sevii 1-3: registered physical NPC roots and reviewed terminal branches.

Map registration and object-script placement are source verified. This is not
proof of a continuous ferry/postgame playthrough on the compiled ROM.
"""
ROWS=[]
EMOTIONS=dict(N='neutral',S='soft_smile',A='annoyed',F='flustered',D='sad',U='surprised',M='smug',L='laughing')
def add(key,labels,subject,lines):
    replies=[]
    for line in lines.strip().split('|'):
        line=line.strip()
        if len(line)>1 and line[1]=='~' and line[0]in EMOTIONS:line=EMOTIONS[line[0]]+line[1:]
        replies.append(line)
    assert len(replies)==11,(key,len(replies))
    ROWS.append(dict(key='sevii13_'+key,labels=labels.split(),subject=subject,replies=replies))

add('celio_praise_local','OneIsland_Text_LuckyToHaveCelioHere',
    'An older islander praises Celio despite not fully understanding his work or Bill\'s reputation.','''
S~He may not know the job title, but he knows the young man who keeps helping the island.|
S~People can recognize reliable service without understanding every technical detail.|
S~Good to hear the quiet work is noticed. Celio seems to have earned trust.|
S~He sounds proud of someone who is not even his own family.|
S~A community remembers who keeps ordinary things working.|
S~The technical briefing is vague; the character reference is exceptionally warm.|
S~A person's work can leave kindness visible even where the mechanism is not.|
S~The best maintenance is invisible until a neighbor says thank you.|
S~A small island keeps its useful people close in conversation.|
S~He cares about the person, not just the impressive new words.|
S~I wonder how long he has watched Celio working here.
''')
add('celio_kanto_praise','OneIsland_Text_HavePCLinkageWithKanto',
    'The islander celebrates Celio\'s new connection with Kanto though the technical side puzzles him.','''
S~The news has passed through a granddaughter and arrived as a very proud review of Celio.|
S~He understands the social value of the improvement even without its engineering details.|
S~Good work can matter to people who never need to know how it was done.|
S~It is lovely to hear the excitement reach more than the person who built it.|
S~A useful change can make a small community feel less far away.|
S~The achievement receives a family-mediated announcement and an enthusiastic endorsement.|
S~A distant shore has become a little less distant in the island's conversation.|
S~Successful deployment, positive community feedback. Excellent result.|
S~A quiet worker has given the island a new thread toward other people.|
S~He has kept the important part: somebody here worked hard and helped.|
S~I wonder what his granddaughter was most excited to try.
''')
add('celio_matchmaking','OneIsland_Text_HavePCLinkageWithHoenn',
    'After another breakthrough, the islander decides Celio would suit his granddaughter as a husband.','''
M~A successful project has unexpectedly reached the grandfather-approved husband shortlist.|
N~Professional competence is admirable, but the two people would still need their own interest.|
N~Celio did good work. Marriage is a separate decision for the people involved.|
F~That is an awfully personal direction for a proud announcement to take.|
S~He means it warmly. I hope he leaves both young people room to decide.|
M~The technical achievement has been repurposed as a romantic recommendation.|
M~One repairs a machine and suddenly acquires an imagined wedding. Dangerous work.|
N~Excellent engineering is not complete compatibility testing.|
S~A proud elder has wandered from useful wires into possible family ties.|
M~A flattering opinion, though he has skipped a few conversations before the wedding.|
S~I wonder whether his granddaughter knows he is making these recommendations.
''')
add('one_warm_climate','OneIsland_Text_IsntWarmClimateHereGreat',
    'A local warmly welcomes sightseeing and praises the island climate.','''
S~The weather has been included in the welcome basket. Very generous island.|
S~A mild climate can shape daily life as much as the scenery visitors notice.|
S~Pleasant place. Still need water and a sensible pace in the sun.|
S~A friendly greeting makes a strange shore feel easier to stand on.|
S~A slow walk and something cool to drink sound like a good beginning here.|
S~The island presents its climate as a principal local attraction. Convincingly.|
S~A warm day, offered as if the speaker had personally arranged it.|
S~Comfortable working conditions for an afternoon of exploring.|
S~The air has a softer edge around this little town.|
S~They sound glad to share the place, not just sell it to us.|
S~I wonder which view they suggest to first-time visitors.
''')
add('one_volcano_routine','OneIsland_House1_Text_GazeUponVolcanoOnSunnyDays',
    'An older islander makes looking at the volcano part of a daily routine.','''
S~A daily appointment with a mountain. Unlikely to arrive late.|
S~Repeated observation can make small changes in familiar scenery especially noticeable.|
S~Good to have something worth stepping outside for.|
S~I like a routine that begins with quietly noticing the day.|
S~A simple pleasant habit can do a lot for an ordinary morning.|
S~The volcano enjoys a loyal returning audience on every clear day.|
S~A familiar great thing can keep being worth a small look.|
S~Regular inspection from a safe distance. Both enjoyable and informative.|
S~One old presence greeting another across the morning air.|
S~A good view does not wear out just because it is familiar.|
S~I wonder what change in the mountain they notice first after cloudy weather.
''')
add('one_last_eruption','OneIsland_House1_Text_LastTimeMtEmberErupted',
    'The other resident tries to remember Mt. Ember\'s last eruption.','''
N~That sounds like a date worth getting right before planning a picnic.|
N~A vague personal memory is not a reliable geological risk assessment.|
N~Check a reliable record. Better than guessing about a volcano.|
N~It is strange to live beside something so powerful and mostly quiet.|
N~A familiar landmark can still deserve practical respect.|
N~The peaceful view has acquired an important historical footnote someone cannot quite retrieve.|
N~An old mountain has kept a longer calendar than the people looking at it.|
N~Need records, not a tentative recollection, before making a safety claim.|
N~The quiet stone may remember more heat than anyone in the room.|
N~The fact that it is familiar does not make the question unimportant.|
N~I wonder where the island keeps its old eruption records.
''')
add('one_staying_home','OneIsland_House2_Text_IWantToStayHereForever',
    'A young resident rejects the assumption that everyone wants a big city and prefers the island.','''
S~The big city has lost one prospective customer to a perfectly good view from home.|
N~A preference for familiar community and setting is as legitimate as an interest in urban life.|
S~Her choice. A good life does not need the biggest address.|
S~It is reassuring to hear someone know where they feel at home.|
S~A place you love is a good reason to stay.|
S~The supposedly inevitable departure has been declined by the person expected to make it.|
S~A quiet place can contain quite enough of a life.|
N~Requirements fit the current environment. No automatic upgrade needed.|
S~Some roots are happy where the sea wind already knows them.|
S~She knows her own taste instead of borrowing what young people are meant to want.|
S~I wonder what ordinary part of island life she would miss most elsewhere.
''')
add('spa_invitation','OneIsland_KindleRoad_EmberSpa_Text_WaterWarmsMeToCore',
    'A relaxed bather praises the hot pool and invites us to warm up in the middle.','''
S~A review delivered mostly in extremely satisfied vowels. Persuasive.|
N~A comfortable soak can be pleasant; the heat still calls for sensible limits.|
N~Enjoy it without staying in until everyone feels faint.|
S~They sound so thoroughly relaxed that the room feels quieter around them.|
S~A warm rest after the road sounds lovely. Leave time to cool down afterward.|
S~The spa's leading critic has temporarily misplaced every adjective except heavenly.|
S~A very small pool holding a great deal of contentment.|
N~Good user satisfaction. Temperature and time still matter.|
S~The warm water has softened the edges of the afternoon.|
S~Relaxation looks good on someone who is not trying to make it impressive.|
S~I wonder whether they come at the same quiet hour every day.
''')
add('spa_chowder','OneIsland_KindleRoad_EmberSpa_Text_EnjoyBowlOfChowder',
    'A bather looks forward to warming up further with chowder afterward.','''
S~Warm outside, warm inside. They have designed a very thorough cozy afternoon.|
S~A pleasant routine can connect a restorative stop with a satisfying meal.|
S~A good meal after a rest. Sensible priorities.|
S~It is sweet to hear someone so pleased with a simple plan.|
S~A proper bowl of chowder is an excellent closing argument for a spa visit.|
S~The experience is scheduled to conclude with a warmly edible final act.|
S~A day can be wonderfully small and still feel complete.|
S~Two complementary heat-delivery systems. One includes potatoes.|
S~A bowl waiting after the water, one quiet warmth after another.|
S~They know exactly which little pleasure comes next. Lovely.|
S~I wonder where on the island they get their favorite bowl.
''')
add('spa_claim','OneIsland_KindleRoad_EmberSpa_Text_HotSpringIsTherapeutic',
    'A bather repeats the claim that hot spring soaking is therapeutic.','''
N~It certainly looks relaxing. I would keep the miracle claims smaller than the pool.|
N~Relaxation is plausible; broad treatment claims would need more specific evidence.|
N~Enjoy the soak. Get proper care for an injury too.|
S~Sometimes simply feeling comfortable for a while is worth the visit.|
N~A pleasant rest should still be gentle on someone who already feels unwell.|
N~The spa receives a favorable review with a carefully secondhand medical endorsement.|
S~The water may be kind without being required to perform miracles.|
N~Specify the claimed effect before deciding what therapeutic means.|
S~Warmth can be a comfort without needing to become a promise.|
N~They say people say. Worth keeping that uncertainty attached.|
S~I wonder whether the quiet company is part of what makes it feel helpful.
''')
add('spa_skin_claim','OneIsland_KindleRoad_EmberSpa_Text_SeeHowSmoothMySkinIs',
    'A bather credits the spring with keeping their skin youthful.','''
S~They are very happy with the mirror report. That is a nice way to leave a bath.|
N~The observation is personal; it does not isolate the spring as the cause.|
N~Glad they feel well. No need to make age a problem to solve.|
F~I would be embarrassed by that close a face inspection, but they seem delighted.|
S~Feeling comfortable in your own skin is a good reason to enjoy a routine.|
M~The spa's most enthusiastic before-and-after display appears to have only an after.|
S~A little vanity can be pleasantly harmless when it makes someone smile.|
N~Anecdotal result, many possible variables. User satisfaction nevertheless high.|
S~The water has returned a face the owner is glad to meet.|
S~A happy glow is real, even when the skincare theory is ambitious.|
S~I wonder how long this has been their favorite part of the routine.
''')
add('spa_bruno_recovery','OneIsland_KindleRoad_EmberSpa_Text_BrunoVisitsSpaOnOccasion',
    'A martial artist says Bruno brings himself and his Pokemon to recover at the spa.','''
S~Even the strongest people have a recovery plan. Good to hear it includes their partners.|
N~Sustained training requires recovery for both trainer and Pokemon. The visit is not a substitute for care.|
S~Good example. Tough does not mean ignoring an injury.|
S~It is reassuring to hear rest treated as part of being capable.|
N~Looking after the partners afterward matters as much as the hard work before.|
S~The formidable fighter's offstage routine includes the unglamorous business of healing.|
S~Strength can look like knowing where to be gentle.|
N~Maintenance interval respected. Much better than running everything until failure.|
S~The strongest footsteps still come here to grow quiet for a while.|
S~He brings the Pokemon into the care routine too. A good detail to remember.|
S~I wonder whether the other visitors treat him like an ordinary regular here.
''')
add('spa_rocksmash','OneIsland_KindleRoad_EmberSpa_Text_ExplainHM06',
    'The spa maker compares the Rock Smash technique with breaking crackers.','''
U~Cracker-like boulders. I recommend keeping the snack bag and the stone pile very separate.|
N~The comparison illustrates the move's effectiveness, not a change in the rock's material.|
N~Useful skill. Keep everyone clear before breaking stone.|
S~He sounds quietly proud of a tool that helped make this peaceful place.|
M~Crackers are a vivid comparison, though I prefer mine less geological.|
S~The pool's maker offers a formidable craft lesson in disarmingly edible terms.|
S~Something forceful helped make somewhere gentle. I like that history.|
S~A practical capability with an actual construction story behind it. An excellent bit of craft.|
S~A hard thing was broken so warm water could hold people softly.|
S~The gift feels personal because he remembers the work it did.|
S~I wonder how long the original pool took him to shape.
''')
add('bill_farewell_task','OneIsland_PokemonCenter_1F_Text_BillCatchYouLater',
    'At the end of the introductions and travel handoffs, Bill sends us off to deliver his greeting.','''
S~An island introduction has become a small delivery adventure. We even have a greeting to carry.|
N~The initial briefing is complete and the practical errand is now clear.|
N~Keep the package safe and remember where it goes. Straightforward task.|
S~It is nice to be trusted with a small personal favor in a new place.|
N~We can take the errand at a sensible pace and enjoy the trip too.|
S~The visit has neatly supplied its next chapter and a line for the eventual arrival.|
S~A friendly message can be a small thing that makes a strange doorstep easier.|
N~Task assigned, destination identified. Check the travel plan before leaving.|
S~A borrowed greeting is riding beside us toward another island.|
S~He leaves the goodbye friendly, even with his attention already back on work.|
S~I wonder how long Bill and the recipient have been exchanging interesting finds.
''')
add('bill_working','OneIsland_PokemonCenter_1F_Text_HmmHowAboutLikeThis',
    'Bill is absorbed in trying an adjustment to the machine.','''
S~He is deep in the part of a problem where every hmm is doing real work.|
S~He appears to be testing a specific adjustment. Best let the observation finish.|
N~Give him room. He knows where his attention needs to be.|
N~I would not want to pull the thought away just as it found something.|
S~A quiet pause is a perfectly good contribution when someone is concentrating.|
S~The problem-solving monologue has reached the promising stage of incomplete sentences.|
S~A small thought turning itself carefully toward a new shape.|
S~That is a proper troubleshooting noise. I recognize it immediately.|
S~The room has become still around one useful little idea.|
N~He is not being rude. His mind is simply very occupied.|
S~I wonder what detail made him try that particular adjustment.
''')
add('bill_more_time','OneIsland_PokemonCenter_1F_Text_GotPCWorkingStrollAWhileMore',
    'Bill reports progress but asks us to explore a little longer while he teaches Celio.','''
S~The repair worked; the lesson is still running. We have been officially assigned a stroll.|
S~Passing on the method matters as much as completing the immediate repair.|
N~Good. Let Celio learn it properly instead of rushing them.|
S~It is kind that Bill is staying to explain rather than simply leaving the fix behind.|
S~A little more time now can save Celio much more trouble later.|
S~The completed repair has developed a useful educational epilogue.|
S~A good helper leaves someone less dependent on the next visit.|
S~Documentation by demonstration! Worth letting them finish.|
S~The new thing works, and another pair of hands is learning its habits.|
S~A pleasant excuse to explore while someone else gets a proper explanation.|
S~I wonder which part Celio most wanted Bill to show him.
''')
add('celio_host_apology','OneIsland_PokemonCenter_1F_Text_SorryForBeingPoorHost',
    'Celio apologizes for taking Bill\'s time and being distracted during our visit.','''
S~A busy host is still a host. We can survive an afternoon without a personal tour.|
S~He is accounting for competing demands, though help between friends need not be a debt.|
S~No problem. Let him finish the work without feeling guilty about us.|
S~He sounds worried about being kind to everybody at once.|
S~We can find our way around. He deserves room to learn without apologizing for it.|
S~The earnest host has tried to add impeccable hospitality to an already full task list.|
S~A good intention can be visible even through distraction.|
N~Multiple active tasks. Remove the unnecessary burden of entertaining us too.|
S~A small room can hold more obligations than one person has hands.|
S~He has been considerate enough. We do not need a performance of welcome.|
S~I wonder how long he has been trying to manage all this on his own.
''')
add('celio_modifying','OneIsland_PokemonCenter_1F_Text_CelioImModifyingMyNetworkMachine',
    'Celio describes ongoing work on his machine and hopes we will try the result first.','''
S~A work in progress with a very eager first-customer invitation attached.|
S~He is planning the improvement and already thinking about a useful field test.|
N~Good to have a goal. Let him finish and check it before trying the result.|
S~It is lovely to hear him imagine someone enjoying the thing he is making.|
S~A useful project feels more personal when you know who it is meant to help.|
S~The inventor's future unveiling already has a place reserved for us.|
S~A quiet hope taking shape among familiar tools.|
S~An actual user involved before release! I approve of that enthusiasm.|
S~A new little possibility is growing inside the work he already knows.|
S~He sounds excited without needing to make a grand promise.|
S~I wonder which part of the change has been most satisfying to work out.
''')
add('celio_gem_needed','OneIsland_PokemonCenter_1F_Text_NeedsSpecialGemstone',
    'Celio explains that his project needs a special gem believed to be on One Island.','''
N~The machine is waiting for a very rare spare part. A difficult shopping list.|
N~A specific material requirement has become the project's current bottleneck.|
N~Useful lead, uncertain location. Search prepared rather than wandering everywhere.|
N~It is frustrating when so much work stops at something you cannot find.|
N~A careful search needs a plan and time, not just determination.|
N~The grand invention has narrowed to one missing prop with no forwarding address.|
N~A small absent thing can occupy an enormous part of a person's thoughts.|
N~Dependency identified, supply route unknown. Now investigate likely locations.|
N~The next way forward has the shape of a little stone.|
N~At least he says what he knows and what he has not found.|
N~I wonder where he has already looked.
''')
add('celio_overloaded_search','OneIsland_PokemonCenter_1F_Text_TryingToFindGem',
    'Celio has stalled by splitting attention between study and searching, yet wants to solve it himself.','''
N~Two difficult jobs have been taking turns borrowing the same tired brain.|
N~Dividing attention can slow both tasks. Independence does not require refusing every useful resource.|
N~Pick one next step. Doing everything alone is not the same as doing it well.|
N~I understand wanting the result to feel like your own work.|
N~A little help would not erase the time he has already put in.|
N~The determined researcher has written himself into two unfinished chapters at once.|
N~A borrowed hand does not take your name off the thing you made.|
N~Context switching is expensive. Separate the tasks and accept useful information.|
N~Two paths pulling on the same pair of feet can leave someone standing still.|
N~He can be proud of the work without making loneliness part of the requirement.|
N~I wonder which small task would give him the clearest sense of progress.
''')
add('celio_rainbow_pass','OneIsland_PokemonCenter_1F_Text_PassLetYouGetToAllIslands',
    'After the Ruby handoff and pass upgrade, Celio explains access to all Sevii islands and asks for help.','''
S~A wider ferry route and a clear request. Our little island map has grown.|
N~The upgraded travel permission is established before this explanation. The search is still ahead.|
N~Check the destinations and supplies before setting out. He needs careful help.|
N~He sounds both hopeful and anxious about asking so much.|
N~We can take the journey one safe stop at a time.|
S~The small errand has expanded into an archipelago-sized next chapter.|
N~A larger map is exciting and a little heavier in the hand.|
N~New access granted. Plan the search rather than treating every island as one task.|
S~More pieces of land have become places we may stand.|
N~He is trusting us with his own pass. That deserves care.|
S~I wonder which new island will give us the most useful lead.
''')
add('celio_completed_work','OneIsland_PokemonCenter_1F_Text_ManagedToLinkWithHoennThankYou',
    'After installing the Sapphire, Celio celebrates his completed machine and thanks us for realizing his dream.','''
S~There it is: the voice of someone whose stubborn little dream finally answered back.|
S~The material search and his technical work have both contributed to the completed result.|
S~He did the work too. Good to see him happy enough to forget the worrying for a moment.|
S~It is lovely hearing the relief arrive right in the middle of the excitement.|
S~We helped him get there, but he deserves to be proud of his own hands.|
S~A long-running private hope has finally found a wonderfully unpolished closing speech.|
S~Something that lived mostly in his head now exists where other people can use it.|
S~Successful operation after a long dependency chain! That feeling never gets old.|
S~A quiet room has become large enough to hold the dream he kept inside it.|
S~The imperfect excited words make the moment feel more personal.|
S~I wonder what he will notice first once the excitement settles into an ordinary working day.
''')
add('celio_after_completion','OneIsland_PokemonCenter_1F_Text_WishYouBestOfLuck',
    'On a later visit, emotional Celio turns the attention back to our Pokemon search and wishes us luck.','''
S~He is not crying, officially. We can respect the official version and the very obvious feeling.|
S~He acknowledges the emotion indirectly and returns encouragement to us.|
S~Good of him. No need to make him explain the tears.|
S~I like that we can let the moment stay tender without naming it too loudly.|
S~He worked hard for this. A little emotion is nothing to apologize for.|
S~The delighted maker attempts a dignified exit from his own happy scene.|
S~A small bright thing is allowed to spill over a little.|
S~He gets to enjoy a successful project. The eyes can file whatever report they want.|
S~The room is warm enough for the careful face to soften.|
S~A little discretion is a good thank-you for that kind of trust.|
S~I wonder how long he imagined saying those words before they finally became true.
''')
add('bill_first_abra','OneIsland_PokemonCenter_1F_Text_BillsFirstMonWasAbra',
    'Celio says Bill loves all Pokemon and first caught Abra.','''
S~A first partner with a talent for being somewhere else. Memorable introduction.|
S~The beginning of an interest can be quite different from the breadth it later develops.|
S~Good to know the famous collector had a first partner too.|
S~It is nice when a big reputation becomes one small early meeting.|
S~A first companion can leave a trace in everything someone learns afterward.|
S~The celebrated enthusiast's expansive biography begins with one elusive character.|
S~A small beginning that grew room for a great many names.|
S~Abra as an initial partner would make for interesting training observations.|
S~One quiet creature opened the first door into a much larger life.|
S~A personal detail makes the reputation feel less like a title.|
S~I wonder what Bill remembers most clearly about meeting that Abra.
''')
add('bill_goldenrod','OneIsland_PokemonCenter_1F_Text_BillsHometownInGoldenrod',
    'Celio contrasts Pallet with Bill\'s bustling hometown of Goldenrod and hopes to visit.','''
S~A quiet town and a bustling one can both send out very curious people.|
S~Different hometown environments can shape experience without defining the whole person.|
S~Hope Celio gets the chance to see it himself someday.|
S~It is lovely hearing a familiar friend's home imagined with such curiosity.|
S~A trip means more when there is someone there whose everyday life you can picture.|
S~The friend's backstory offers a possible setting for a future visit.|
S~Someone else's ordinary streets can become a place you quietly wish toward.|
S~A useful reminder that interesting people do not share one standard origin.|
S~Two kinds of home, both leaving roads that reach this little room.|
S~He sounds interested in the place rather than simply impressed by its size.|
S~I wonder what Bill would show him first if he visited.
''')
add('bill_milk','OneIsland_PokemonCenter_1F_Text_BillCantStomachMilk',
    'Celio shares that Bill cannot tolerate milk and asks about our dislikes.','''
N~The mighty collector has one very ordinary breakfast limitation. Respect the breakfast limitation.|
N~An individual's food tolerance is a practical detail, not something to argue them out of.|
N~Good to remember before offering him a drink.|
S~A tiny personal fact can make someone famous feel pleasantly ordinary.|
N~Useful to know if we ever cook for him. There are plenty of other options.|
M~The grand portrait acquires an unexpectedly domestic footnote.|
N~Even a remarkable person gets to decline an entirely unremarkable beverage.|
N~Dietary requirement recorded. No need to test it.|
S~A little familiar discomfort beneath all the impressive stories.|
N~That is the sort of detail a friend remembers quietly.|
S~I wonder whether Celio asks because he wants to offer us something we actually enjoy.
''')
add('one_pallet_unknown','OneIsland_PokemonCenter_1F_Text_CameFromPalletDontKnowIt',
    'An island child warmly asks our origin but has never heard of Pallet.','''
S~A new shore is a fine place to discover your hometown is not the center of every map.|
N~Local familiarity varies. Not knowing Pallet is entirely unsurprising.|
S~Fair enough. We are new to plenty of places too.|
S~The greeting stays friendly even without a familiar name to share.|
S~A town can be important to us without being known to everyone.|
S~The traveler's important origin receives a cheerfully blank review.|
S~A familiar name briefly becomes a small strange sound in someone else's room.|
N~Knowledge gap identified without any real problem attached.|
S~Home can be far enough away that even its name arrives as a visitor.|
S~A clear, honest answer is nicer than pretending recognition.|
S~I wonder how the child imagines Pallet after hearing only the name.
''')
add('one_hike_advice','OneIsland_PokemonCenter_1F_Text_EnormousVolcanoOnIsland',
    'A hiker recommends visiting the island\'s quiet volcano.','''
N~An enormous volcano and a casual why not. We should bring a less casual supply bag.|
N~A lack of recent eruption does not replace checking present conditions and the route.|
N~Prepare for the hike. Familiar scenery still needs proper footing.|
S~It is tempting to see the thing that shapes the whole island's horizon.|
N~A good outing needs water, time, and enough strength left to return.|
S~The local landmark is offered as a pleasant excursion with a rather dramatic origin.|
N~A sleeping mountain still deserves respectful visitors.|
N~Check access and conditions before treating the suggestion as a complete plan.|
S~A great old heat keeps a quiet outline above the houses.|
N~A confident local recommendation is useful, alongside practical preparation.|
S~I wonder which part of the climb gives the best view back toward town.
''')
add('one_faraway_wish','OneIsland_PokemonCenter_1F_Text_WishICouldTradeWithBoyfriend',
    'A traveler wishes she could trade Pokemon with her distant boyfriend.','''
S~A familiar person can feel very far away when even a small shared thing needs a journey.|
S~The wish concerns sharing an interest across distance, not simply acquiring another Pokemon.|
N~Hope they get a workable way to arrange it. Keep both partners' care in the plan.|
S~It is the together part that sounds most important in the wish.|
S~A little exchange can make distant lives feel more connected.|
S~The faraway relationship has found a very particular activity it wants a bridge for.|
S~Distance has a way of making ordinary gestures feel ambitious.|
N~A real user need, clearly expressed. Someone should listen to that.|
S~Two familiar voices are waiting for an easier way to share a little of their day.|
S~Shared interests can hold a relationship close even when the people are not.|
S~I wonder which Pokemon they have been talking about exchanging.
''')
add('one_faraway_done','OneIsland_PokemonCenter_1F_Text_TradedWithFarAwayBoyfriend',
    'She has now traded with her distant boyfriend and thanks us and Celio.','''
S~An old wish has become a very ordinary happy report. Best kind of progress.|
S~The new service has produced a concrete personal benefit for someone here.|
S~Good. Nice to hear the work helped real people, not just a machine.|
S~I like hearing the same voice with the distance feeling a little less heavy.|
S~A useful project feels different when someone tells you what it meant to their day.|
S~The technical achievement receives its warmest review from a very personal subplot.|
S~A small shared act has made a faraway life feel closer.|
S~Actual field outcome confirmed by a satisfied user. Excellent.|
S~A thread between two people has been pulled a little more gently.|
S~She gives Celio credit too. Thoughtful, and deserved.|
S~I wonder what their first conversation about the traded partners was like.
''')
add('treasure_warm_sea','OneIsland_TreasureBeach_Text_AmaraPostBattle',
    'Amara enjoys the pleasantly warm sea near Treasure Beach.','''
S~The sea has adjusted its temperature for a much friendlier introduction.|
S~Local water conditions can make a familiar activity feel quite different.|
N~Pleasant water still needs sensible swimming limits.|
S~That sounds like a lovely little part of living here.|
S~A gentle swim and a quiet shore could make an excellent afternoon.|
S~The coastal setting receives a glowing review from someone actually in it.|
S~Warm water has a way of making the horizon less severe.|
N~Comfortable conditions noted. Keep the return route in mind.|
S~The island has left a little warmth out beyond its sand.|
S~A simple pleasure, appreciated without needing to make it grand.|
S~I wonder whether the water feels different at dawn and late afternoon.
''')
add('treasure_beachcomber','OneIsland_TreasureBeach_Text_GoodThingsWashUpOnBeach',
    'A child regularly searches the beach for things carried in by the current.','''
S~The sea keeps arriving with pockets full of small surprises.|
S~Currents can deposit varied material from places far beyond the visible shore.|
N~Interesting finds. Be careful with sharp things and belongings someone may have lost.|
S~I like a place that can give a familiar walk something new to notice.|
N~A careful search should leave the beach safe for the next person too.|
S~The tide runs an unpredictable little delivery service.|
S~Small lost things arriving where someone still knows how to be curious.|
S~Natural transport and sorting! The changes between visits must be interesting.|
S~The water leaves little notes from places we have not walked.|
N~An eye for detail makes this kind of ordinary outing rewarding.|
S~I wonder what the most surprising thing they have found here was.
''')
add('two_new_shop','TwoIsland_Text_FellowMovedFromCeladonCity',
    'A resident discusses the brothers who moved from Celadon and opened the small island shop.','''
S~From a city of giant stores to making one little shop of their own. A bold move.|
N~A new local market can involve different needs and constraints from a large city.|
N~Hope the brothers get a fair chance to make it work.|
S~Starting again somewhere small must feel exciting and lonely in different moments.|
N~A useful shop can become part of everyday life if the community welcomes it.|
S~The bustling city's former residents have chosen a considerably more intimate stage.|
S~A large place does not own the people who choose to leave it.|
N~New environment, new demand. They will need to learn the local requirements.|
S~Two familiar people have brought a little of one shore to another.|
N~The question sounds doubtful. I would rather see how they actually settle in.|
S~I wonder what made this island feel worth the move to them.
''')
add('two_brother_work','TwoIsland_Text_ShopkeepersBrotherWorksGameCorner',
    'The younger brother works at the Game Corner to help finance the shop\'s stock.','''
N~A small shop with a whole second workday helping fill its shelves.|
N~The brothers are dividing income generation and shop operation between them.|
N~Hard work. Hope they both get a rest instead of stretching every day thin.|
S~It sounds like they are trying to carry the difficult beginning together.|
N~A new shop takes more ordinary effort than the neat front counter shows.|
N~The little business has a supporting story unfolding at another workplace.|
S~A shelf can hold a surprising amount of somebody's tired evening.|
N~Cash flow problem being addressed through additional labor. Sustainable hours matter.|
N~Two hands at separate tasks are trying to build the same small future.|
N~It is good to know the work behind the display, not just judge the size.|
N~I wonder which bit of merchandise they are saving to add next.
''')
add('two_bruno_candy','TwoIsland_Text_BrunoCameToIslandWhileBack',
    'A resident recalls Bruno leaving disappointed because Rage Candybars were sold out.','''
M~Even an Elite Four member can lose to an empty sweet shelf. A humbling matchup.|
M~A powerful reputation offers little advantage against finite inventory.|
N~Fair disappointment. Still just a customer when the stock is gone.|
S~It is oddly comforting to imagine somebody so imposing wanting a favorite sweet.|
M~That is why the last box should never be promised before someone checks the cupboard.|
M~The formidable visitor's island adventure ended at the confectionery counter.|
S~An impressive person briefly reduced to an ordinary small wish. Rather nice.|
N~Demand exceeded supply. Even exceptional strength cannot fix that immediately.|
S~A great strong traveler had a little empty-handed walk back to the boat.|
M~An unexpectedly human footnote to an intimidating public image.|
S~I wonder whether anyone saved him a bar when the next batch arrived.
''')
add('two_rare_shopping','TwoIsland_Text_BuyRareItemsHere',
    'A local recommends the island shop to discerning trainers seeking rare items.','''
M~Discerning is a fancy word for having a shopping list, ideally.|
N~A specialized selection can be useful, though rarity alone does not establish need.|
N~Check what helps the team. Do not buy just because it is hard to find.|
N~It is nice to hear someone proud of a small local shop.|
N~A useful item is one we can actually put to work.|
M~The modest storefront has acquired an impressively exclusive-sounding endorsement.|
N~Scarce things can become very good at asking for money.|
N~Evaluate the specification, not just the limited supply.|
N~A small shelf can still carry something important for a long road.|
N~Good taste includes knowing which tempting thing to leave on the shelf.|
S~I wonder which item the regular customers are most pleased to find here.
''')
add('two_cape_woman','TwoIsland_Text_OldWomanLivesOutOnCape',
    'A boy finds the cape woman\'s intense scrutiny of Pokemon unnerving.','''
N~A very thorough look can feel like the beginning of an examination you did not study for.|
N~Her close observation may have a purpose, though the boy does not explain it.|
N~No need to judge her from a distant stare. Learn what she actually does.|
N~I understand feeling awkward when someone looks very closely without explaining.|
N~A little clear communication could make the meeting easier for everyone.|
N~A local specialist has acquired the wonderfully vague reputation of looking at things ominously.|
S~An old woman with a keen eye is allowed a little mystery.|
N~Observed behavior, unknown intent. Need more data before classifying the concern.|
S~Some quiet eyes seem to notice a little more than the room expects.|
N~A serious look is not necessarily an unfriendly one.|
S~I wonder what detail she is looking for in the Pokemon.
''')
add('two_jumping','TwoIsland_Text_HaveYouTriedJumpingGame',
    'A bouncing child explains that different Pokemon jump differently in the local game.','''
S~The explanation has arrived with its own sound effects and demonstration. Very complete.|
S~Body structure can influence jump behavior. The child's enthusiasm is difficult to miss.|
N~Good fun if the partners are comfortable joining in.|
S~The little differences seem to be the part they love most.|
S~It is nice when an activity lets different partners have their own way of playing.|
S~A young announcer presents the local athletic program entirely in boings.|
S~Joy has a very springy vocabulary today.|
S~Different motion profiles! I would enjoy comparing the jumps.|
S~A small body discovering how much happiness fits between the ground and the air.|
S~The game has clearly found its most enthusiastic promoter.|
S~I wonder which Pokemon gets the very longest boooooooing.
''')
add('two_game_friend','TwoIsland_PokemonCenter_1F_Text_HaveYouVisitedGameCorner',
    'A visitor says the local Game Corner is meant to be visited with a friend.','''
S~A game that puts bring a friend before bring coins sounds promising.|
S~The activity depends on shared participation rather than a solitary visit.|
N~Fair enough. Choose someone who actually wants to play too.|
S~It is nice when the point is having a good time together.|
S~A simple shared game can make a quiet day much warmer.|
S~The venue politely declines to perform its whole program for an audience of one.|
S~A little room built around the possibility of company.|
N~Multiplayer requirement. Check before making a solo trip.|
S~Some small joys are shaped to leave a place for another person.|
S~A good excuse to invite somebody without making the meeting complicated.|
S~I wonder which game pairs of friends ask for first.
''')
add('two_old_resident','TwoIsland_PokemonCenter_1F_Text_OldLadyLivesOutOnCape',
    'A resident describes the sparsely populated island and its long-established cape resident.','''
S~A small island can keep someone familiar for so long that the beginning goes missing.|
S~A longstanding resident may hold knowledge that newer inhabitants do not share.|
N~Her home is still her home. Visit respectfully if we go out there.|
S~It is strange to imagine being part of a place for longer than anyone nearby remembers.|
S~A quiet life can leave a very steady mark on the people around it.|
S~The island's recurring resident has outlasted the narrator's available backstory.|
S~Some houses feel like they grew into the land rather than being built on it.|
N~Long-term local knowledge could be useful. No need to turn it into a legend.|
S~A quiet figure at the cape, held in everyone's map of home.|
S~They describe her as part of the place without really describing the person.|
S~I wonder how she would tell the story of first coming here.
''')
add('move_mushroom_end','TwoIsland_House_Text_NeedMushroomOrTwoToLearnMove',
    'The Move Maniac closes either a canceled or completed tutoring visit by restating his mushroom requirement.','''
N~The lesson desk accepts mushrooms, and the farewell does not tell us whether a lesson happened.|
N~He asks for mushrooms again. That is his standing arrangement, whether we take a lesson today or return later.|
N~Clear terms. Check the partner's actual moves before planning the next match.|
N~An unusual arrangement, but at least he explains what to bring next time.|
N~A mushroom should stay out of the cooking pot if we mean to use it for a lesson.|
M~The tutor's syllabus and the shopping basket remain unusually intertwined.|
N~Knowledge has a peculiar little price in this house.|
N~Service requirement restated. Verify the actual resulting configuration separately.|
N~A remembered technique may be waiting behind a little forest offering.|
N~A specific request is easier to work with than a mysterious favor.|
N~I wonder how he became equally devoted to moves and mushrooms.
''')
add('three_biker_claim','ThreeIsland_Text_IslandBelongsToUs',
    'A biker declares ownership of Three Island.','''
A~A loud arrival is not a deed to everybody else's home.|
N~An assertion of control does not establish legitimate ownership.|
A~The island belongs to the people living their lives here, not his noise.|
N~That would be frightening to hear outside your own house.|
A~People should not have to negotiate permission to feel safe at home.|
N~A visiting nuisance has promoted himself to ruler without consulting the setting.|
N~A wheel on a road does not make the road yours.|
N~Unauthorized access has become an unauthorized ownership claim.|
N~A stranger's shadow cannot decide where everyone else belongs.|
A~He has mistaken taking up space for having a right to all of it.|
N~I wonder how long the residents have had to listen to that.
''')
add('three_cowards_pack','ThreeIsland_Text_YouCowardsToughInPack',
    'An island defender angrily confronts the bikers\' reliance on intimidating the village as a group.','''
N~A gang does make quite a lot of confidence for people who came to frighten neighbors.|
N~Group intimidation can create a severe imbalance for unprepared residents.|
N~The defender should not have to face the whole group alone.|
N~They sound angry and frightened together. I understand both.|
N~A safe place for the residents matters more than winning a shouted exchange.|
N~The harassed villager has correctly identified the production's reliance on a crowded cast.|
N~Borrowed bravery grows cheaply when someone else is outnumbered.|
N~Numbers are amplifying the threat. Avoid isolating the residents.|
N~Several loud shadows have gathered around a small familiar street.|
N~It takes nerve to say that while they are still standing there.|
N~I wonder whether the other neighbors can hear someone standing up for them.
''')
add('three_bikers_declined','ThreeIsland_Text_ThatsSmart',
    'When we decline the biker confrontation, he smugly tells us not to interfere.','''
N~We can step back without agreeing with a single thing he is doing.|
N~A refusal to engage immediately is not approval of the harassment.|
N~A careful choice is ours to make. His opinion of it means little.|
N~It is difficult to be pressured into a fight by someone already trying to frighten people.|
N~Preparing before intervening is better than making the team pay for his impatience.|
N~The bully mistakes a delayed scene for a victory in the entire story.|
N~Not every retreat belongs to the person who shouted it into being.|
N~No confrontation initiated. Reassess condition and options independently.|
N~A step back can still belong to the path forward.|
N~He wants the last word to sound like control. We need not treat it that way.|
N~I wonder whether the residents have somewhere safe to wait while help is prepared.
''')
add('three_paxton','ThreeIsland_Text_PaxtonPostBattle',
    'After the final biker battle, Paxton insults the island residents and retreats with his gang.','''
N~The insult can leave with the motorbikes. The island has had enough of both.|
N~His dismissal does not diminish the residents' right to safety and respect.|
N~Good. Let them go, and make sure the locals are all right.|
N~I will be glad when the quiet belongs to the village again.|
N~The people here deserve a calm evening without waiting for the next arrival.|
N~The defeated visitor exits with one final review nobody requested.|
N~An unkind voice fading is a perfectly pleasant local attraction.|
N~Hostile group withdrawing. Check the people and the area before assuming all is settled.|
N~The road is slowly getting its own sound back.|
N~He can sneer from a considerable distance. Preferably farther away.|
N~I wonder what the neighbors will say once the engines are gone.
''')
add('three_team_praise','ThreeIsland_Text_YouveGotImpressiveMons',
    'An island defender praises our team, after the Full Restore handoff or on return visits.','''
S~A proud little moment for the partners after a rough job.|
S~The praise recognizes the team directly. This line can also occur on later visits.|
S~They did good work. Glad someone here sees the partners, too.|
S~It is lovely to hear the team welcomed after the noise they helped end.|
S~They deserve a proper rest as well as a kind word.|
S~The grateful village gives the ensemble its own favorable review.|
S~A little affection where there had been a great deal of fear.|
S~Actual performance noticed and appreciated. Good feedback for the whole group.|
S~Many small strengths have left the same street gentler.|
S~A compliment feels better when it includes the ones who worked beside us.|
S~I wonder which partner the defender remembers most clearly.
''')
add('three_full_bag','ThreeIsland_Text_OhYourBagIsFull',
    'The defender cannot give a Full Restore because our bag is full.','''
N~The thank-you is ready. The bag has chosen a very ungrateful moment to be full.|
N~The offered recovery item did not transfer. The failed handoff is explicit.|
N~Make room. The team could use that help.|
F~It is awkward when someone notices we need help and we cannot carry it.|
N~A little sorting would make accepting the practical kindness easier.|
N~The relieved villager's gift has encountered the least dramatic obstacle imaginable.|
N~A crowded pocket interrupting a much kinder moment.|
N~Capacity failure. No Full Restore should be counted as received.|
N~A small helpful thing is waiting outside a full place.|
N~We can handle our own bag without making the offer feel unwelcome.|
N~I wonder what we can put away before asking again.
''')
add('three_lostelle_lead','ThreeIsland_Text_LostelleWentOffTowardsBondBridge',
    'The defender wishes we would stay but tells us Lostelle went toward Bond Bridge.','''
N~A warm invitation and a useful direction. The direction matters first while a child is missing.|
N~The last reported movement narrows the search toward Bond Bridge.|
N~Follow the lead prepared. Finding Lostelle comes before a longer visit.|
N~I hope the familiar place-name helps us reach her quickly.|
N~We should keep the child in mind rather than turn the search into sightseeing.|
N~The grateful invitation pauses for a more urgent story still looking for its missing person.|
N~A small name makes the road ahead feel much more important.|
N~Last-known direction identified. Search deliberately from that point.|
N~One child's footsteps have led away from the village's warm doors.|
N~They remembered where she went. That is more useful than another compliment.|
N~I wonder how long ago someone last saw her crossing the bridge.
''')
add('three_quiet_after','ThreeIsland_Text_WouldntWantToSeeBikersHereAgain',
    'A resident wants a livelier island but rejects the bikers\' harassment as entertainment.','''
N~A place can want more excitement without ordering the threatening motorcycle package.|
N~Welcoming activity is different from accepting disruption and intimidation.|
N~Fair distinction. A quiet town does not owe bullies an audience.|
S~People should get to enjoy their home without having to defend liking it.|
N~A good gathering leaves the people living there glad it happened.|
N~The residents decline the unsolicited show while remaining open to better programming.|
N~A quiet place is not a broken place waiting for a rude stranger to repair it.|
N~User feedback is clear: more pleasant activity, less imposed chaos.|
S~A village can open its windows without giving away its doors.|
N~Lively should include the people who actually have to live with it.|
S~I wonder what kind of event the residents would enjoy making together.
''')
add('three_doduo_goal','ThreeIsland_Text_WhenDodouEvolvesGoingToPlayGame',
    'A child plans to train Doduo in Berry Forest, then play a game on Two Island after it evolves.','''
S~A training plan with a game waiting at the end. Doduo gets quite an itinerary.|
N~A goal can support practice, provided the Pokemon's pace and welfare guide it.|
N~Train safely. The forest is not a place to push a partner too far.|
S~It is nice to hear someone picture a little celebration after the work.|
N~A good day can include rest and play before the whole goal is finished too.|
S~The young trainer has scheduled a developmental milestone and an afterparty.|
S~A future outing can make today's ordinary effort feel connected to something bright.|
N~Clear goal, planned reward. Keep the schedule flexible around the actual partner.|
S~A small road through trees is pointing toward a happy day across the water.|
S~I hope the Pokemon gets a say in which part of the day is fun.|
S~I wonder which game the child wants to try together.
''')
add('three_spoon','ThreeIsland_House2_Text_CantMakeThisSpoonBend',
    'A resident strains unsuccessfully to bend a spoon with his mind.','''
M~The spoon has defended its original shape with remarkable composure.|
N~The failed attempt does not require a moral explanation. The ability was never established.|
N~Put the spoon down before the straining gives him a headache.|
F~It is awkward to be present at a very earnest attempt that does not work.|
M~I would like the spoon returned to dinner duty before anyone gets upset with it.|
M~The utensil has declined the leading role in a psychic breakthrough.|
M~A tiny domestic object calmly refusing an entire dramatic premise.|
N~No observed deformation. The spoon passes its structural test.|
N~The mind can be busy while the little silver thing remains very still.|
M~He is allowed a disappointing experiment without calling himself useless afterward.|
N~I wonder what first convinced him he might be able to do that.
''')
add('three_sabrina_admiration','ThreeIsland_House2_Text_IAdmireSabrina',
    'A resident admires Sabrina\'s Psychic abilities, composure, and appearance.','''
S~A calm person can travel a long way in other people's imaginations.|
N~The impression combines observed reputation with secondhand descriptions.|
N~A good example if the admiration turns into learning something useful.|
S~I understand being drawn to someone who seems so certain of themselves.|
N~It is nice to admire someone without expecting them to know you back.|
S~A distant figure has acquired an enthusiastic island review.|
S~Quiet confidence can make a surprisingly loud impression.|
N~Interesting public reputation. Direct observation would tell us more.|
S~A still presence has left a ripple far from the room where it stood.|
S~Composure is a striking part of style. I understand noticing it.|
S~I wonder which story about her first reached this island.
''')
add('three_fishing_home','ThreeIsland_House3_Text_WantedToLiveSomewhereQuiet',
    'A resident bought a quiet island home and plans an ordinary fishing day.','''
S~A quiet house and a fishing plan. The day seems to match the brochure in their head.|
S~They have chosen an environment that supports the routine they actually enjoy.|
S~Good to know what sort of life suits you.|
S~A simple plan can sound wonderful when it belongs to you.|
S~A quiet home, a day outside, and no hurry. A good arrangement.|
S~The resident's chosen setting is delivering exactly the modest story requested.|
S~An ordinary afternoon can be a surprisingly ambitious thing to build a life around.|
N~Requirements match environment and activity. Successful selection.|
S~A little house has made a place for someone's preferred kind of silence.|
S~They know what they wanted beyond how the house would look.|
S~I wonder what little view from home they like coming back to.
''')
add('three_forest_parent','ThreeIsland_House4_Text_GhostsInBerryForest',
    'A parent warns a child away from going to Berry Forest alone by citing ghosts.','''
N~A safety warning might work better with the real hazards than a ghost doing all the explaining.|
N~Clear reasons and a practical plan are more useful than an unverifiable frightening claim.|
N~The child needs safe boundaries, not just a scary story.|
N~I understand wanting the child safe. I hope there is room for questions too.|
N~Going together would teach more than making the whole forest forbidden and mysterious.|
N~The parental warning has delegated its persuasion to a supernatural supporting cast.|
N~A story can keep someone indoors and still leave them unprepared for the world.|
N~Explain the constraint and offer a safe alternative. Better design than fear alone.|
N~The forest should not need a false shadow to deserve careful feet.|
N~A protective intention needs a truthful explanation underneath it.|
N~I wonder whether they have ever shown the child a safe way to explore.
''')
add('three_child_restriction','ThreeIsland_House4_Text_PapaKeepsLyingToMe',
    'The child feels the father lies to stop them going outside to play.','''
N~Being kept safe is easier to trust when the explanation stays true.|
N~Perceived dishonesty can undermine compliance with genuinely important safety advice.|
N~The child deserves a clear reason and a safe way to play.|
D~It is hard when someone you trust makes the world feel needlessly closed.|
N~A supervised outing could help more than another argument through the window.|
N~The protective story has lost its audience's trust. Time for a better conversation.|
N~A locked door feels colder when the reason behind it keeps changing.|
N~Trust failure. Fix the explanation, not just the restriction.|
N~A small person is trying to see where the true edge of the world is.|
N~Feeling unheard can make even a reasonable rule difficult to accept.|
N~I wonder what the child most wants to do outside with someone they trust.
''')
add('three_not_lostelle','ThreeIsland_House5_Text_ImNotLostelle',
    'Another girl clarifies her identity and suggests Lostelle went Berry-picking in the forest.','''
N~A corrected introduction and a useful clue. We should listen closely.|
N~Her information suggests a likely purpose and destination, though she is not certain.|
N~Good lead. Keep the uncertainty in mind while searching.|
N~It must feel strange to have a worried stranger mistake you for someone missing.|
N~A familiar lunch routine can tell us where to begin looking.|
N~The mistaken identity scene contributes a practical detail to the search.|
N~An ordinary habit can become an important little trail.|
N~Probable destination identified, not confirmed. Verify the route.|
N~A small domestic errand has led a child's footsteps toward the trees.|
N~She is clear about who she is and careful about what she only thinks. Helpful.|
N~I wonder who last saw Lostelle carrying her Berry basket.
''')
add('three_play_lostelle','ThreeIsland_House5_Text_IllGoPlayWithLostelle',
    'After Lostelle is safe, the girl plans to go play with her.','''
S~Back to ordinary plans with friends. That is a very good ending to the search.|
S~A return to routine indicates how much safety matters beyond the immediate rescue.|
S~Good. Let them have a quiet normal day together.|
S~It is lovely that the next thing can be as simple as going to play.|
S~A familiar friend can make a frightening day feel farther away.|
S~The adventure closes by returning the child to a much smaller, happier story.|
S~An ordinary invitation can be the sweetest thing after a scare.|
N~Normal activity resumed. A meaningful recovery outcome.|
S~The little roads between friends are open again.|
S~No grand celebration needed. Just someone looking forward to seeing her.|
S~I wonder what they like playing when the afternoon is quiet.
''')
add('lostelle_lunch','ThreeIsland_House1_Text_YoureAlwaysSoCool',
    'Lostelle admires us and promises to make us lunch someday.','''
S~An invitation to a future lunch is an excellent form of thanks. I accept in principle and appetite.|
S~She is imagining a safe future meeting and offering something from her own routine.|
S~Glad she is home and making ordinary plans again.|
F~That is such a sweet little promise. I would remember it.|
S~A lunch made because someone wanted to thank you is a very good lunch.|
S~The rescued child offers a warm little sequel with an edible conclusion.|
S~A frightened day has become a story she can end with generosity.|
S~Future plan, positive association, practical hospitality. Lovely.|
S~A little hand wants to return some of the kindness it was given.|
S~She has found her own way to say she remembers. That matters.|
S~I wonder what she most likes putting in a lunch for somebody.
''')
add('three_store_comparison','ThreeIsland_Mart_Text_TrueThatCeldadonDeptStoreBigger',
    'A youngster marvels that Celadon\'s store may be many times larger than the island Mart.','''
U~A building with several shops stacked inside it is a lot to picture from this little counter.|
N~Store size reflects different markets, not necessarily better service for every local need.|
N~Big does not mean better for the errand we have today.|
S~It is lovely hearing a familiar place sound enormous in someone else's imagination.|
N~A small shop can still remember what its regular customers actually need.|
S~A distant department store has grown into a surprisingly tall island legend.|
S~The world gets large again when someone describes a building you have not seen.|
N~Different demand, different scale. Both designs can suit their setting.|
S~A whole tall town of shelves is being imagined from one small room.|
N~A big selection is useful. A familiar helpful shopkeeper has value too.|
S~I wonder which part of a department store the youngster would want to see first.
''')
add('three_berry_medicine','ThreeIsland_Mart_Text_PeopleHealWithBerriesFromForest',
    'A shopper describes the island\'s reliance on abundant forest Berries for Pokemon care.','''
N~The forest has become part of the local supply shelf. Best treat the shelf kindly.|
N~Local resources can support care, though availability and appropriate use still need judgment.|
N~Use what suits the partner. Do not assume every Berry solves every problem.|
S~It is interesting how a place shapes the ordinary ways people help their Pokemon.|
N~Gather carefully and leave enough for the creatures living there too.|
N~The village's practical care routine extends from the counter into the trees.|
S~A little of the forest's work returns to the homes around it.|
N~Local supply reduces dependence on imports. Sustainability still matters.|
S~The woods keep a quiet kind of help growing close to the ground.|
N~A useful tradition works best when people understand what they are collecting.|
S~I wonder which Berry most island families keep ready at home.
''')
add('three_mart_safe','ThreeIsland_Mart_Text_BikersWereAboutToTrashMart',
    'A shop visitor is relieved the bikers left before damaging the Mart.','''
S~A shop getting to remain an ordinary shop is worth being glad about.|
N~Prevented damage matters even when it leaves no dramatic evidence afterward.|
S~Good. People need this place for their daily supplies.|
S~It must be a relief to stop waiting for the sound of something breaking.|
S~A small shop can matter to a whole community's ordinary day.|
S~The threatened scene has mercifully failed to become a pile of broken scenery.|
S~Something familiar remained intact. That is a quiet good outcome.|
N~Damage avoided, service preserved. Important practical result.|
S~The shelves are still holding what the neighbors came for.|
S~The relief tells us this was much more than an annoying group outside.|
S~I wonder whether the shopkeeper has had time to tell everyone it is safe to come in.
''')
add('three_connection_news','ThreeIsland_PokemonCenter_1F_Text_PCNetworkCanLinkWithKanto',
    'A local celebrates the new connection with Kanto without knowing how it was achieved.','''
S~A useful change has reached the island as good news instead of another complicated explanation.|
S~A service can produce value for people who never need to understand the mechanism.|
S~Good to hear the quiet work is helping more than one island.|
S~Their excitement makes the place feel a little closer to the wider world.|
S~It is nice when a difficult project becomes something ordinary people can simply enjoy.|
S~The inventor's painstaking story arrives here as one happy short announcement.|
S~A distant place has become a little easier to imagine reaching.|
S~Successful service delivery with no requirement for technical literacy. Good outcome.|
S~A thread between shores has made this room a little brighter.|
S~They do not know every detail, but they know the change matters.|
S~I wonder whom they first wanted to get in touch with after hearing the news.
''')
add('three_tides','ThreeIsland_PokemonCenter_1F_Text_ImpossibleToSurfBetweenIslands',
    'A sailor warns that dangerous currents prevent traveling between these islands by Surf.','''
N~The sea has firmly declined to be the shortcut. We should take the boat.|
N~Strong currents can exceed a swimmer's capability regardless of apparent distance.|
N~Use the ferry. Do not ask a partner to prove itself against a dangerous tide.|
N~I am glad someone said it plainly before the water looked tempting.|
N~A safe crossing is worth waiting for.|
N~The scenic route has a nonnegotiable objection from the ocean itself.|
N~Nearby land can still be very far away through moving water.|
N~Environmental load exceeds the method's safe range. Use appropriate transport.|
N~The water between the islands is doing work the eye cannot easily see.|
N~A clear warning is much better than a brave-looking mistake.|
N~I wonder how sailors first learned the safest passages through these currents.
''')
add('three_crush_berries','ThreeIsland_PokemonCenter_1F_Text_AlwaysBerriesInBerryForest',
    'A local encourages Berry crushing because more Berries grow in Berry Forest.','''
N~Plenty nearby is nice. It still deserves a little more thought than endless means free to waste.|
N~Renewable supply should not be confused with unlimited availability or use without consequence.|
N~Take what is needed. Leave the forest some room to keep being a forest.|
N~An abundant place can make people forget the small lives sharing it.|
N~Good ingredients are still worth using carefully, even when they grow nearby.|
N~The enthusiastic proposal has assumed the supporting forest will provide infinite encores.|
N~A growing thing is generous without having signed a permanent supply contract.|
N~Resource replenishment has a rate. Keep that in the calculation.|
N~Fruit returns, but not because every visitor is owed a full hand.|
N~There is room to enjoy a local abundance without treating it carelessly.|
N~I wonder how the forest looks after the busiest gathering days.
''')
add('three_engine_noises','ThreeIsland_Port_Text_WereKantoRiderFederation',
    'A biker boasts of the Rider Federation but admits making engine noises because his bike is weak.','''
M~An impressive performance from the mouth department, with limited support from the motorcycle.|
M~The sound effect is compensating for a gap between the desired impression and the machine.|
N~Could make less noise and have a better visit. Just a thought.|
F~It is almost endearing until I remember how much the neighbors have had to hear.|
N~The village did not ask to be the audience for that imitation engine.|
M~The great motor spectacle turns out to have a human Foley artist at its center.|
M~A surprisingly honest confession from somebody trying to seem formidable.|
M~Manual audio enhancement. Does not improve actual engine output.|
N~A small machine has borrowed a very large voice.|
M~The presentation is doing heroic amounts of work for the product.|
N~I wonder whether the other riders know he is supplying his own exhaust track.
''')
add('three_money_demand','ThreeIsland_Port_Text_ForkOverMoney',
    'A biker demands spending money from a frightened local woman.','''
A~Her purse is not the welcome committee. He can stop threatening her.|
N~This is an extortion demand, not an ordinary request for assistance.|
A~Leave her alone. She owes him nothing.|
D~It is awful to be made afraid just for standing in your own village.|
A~People should not have to pay a stranger to be left in peace.|
N~The self-appointed entertainer has revealed the much uglier point of the performance.|
A~A hand held out for taking is still a threat when it smiles.|
N~Coercive request identified. Protect the person, not the transaction.|
N~A harsh voice is trying to make a small ordinary day belong to it.|
A~He has made his intentions painfully clear. She deserves help.|
N~I wonder whether any neighbors are close enough to support her safely.
''')
add('three_woman_frightened','ThreeIsland_Port_Text_IllCallThePolice',
    'The frightened woman threatens to call police while the bikers harass the port.','''
N~She is trying to make a boundary heard over all that noise.|
N~Seeking outside help is a reasonable response to intimidation.|
N~Good. She should not have to handle them alone.|
D~Her voice sounds so frightened even while she tries to stand firm.|
N~A safe place to wait with someone she trusts would help.|
N~The harassed resident has appealed to an authority beyond the gang's own volume.|
N~A shaking voice can still be saying exactly the right thing.|
N~Escalate to appropriate help without putting her closer to the threat.|
N~A small voice is trying to draw a line that should already exist.|
N~She deserves to be taken seriously without having to sound fearless.|
N~I wonder whether someone can stay beside her until the port is safe.
''')
add('three_port_relief','ThreeIsland_Port_Text_ThankGoodnessBikersGone',
    'Once the bikers leave, the woman admits how terrified she was.','''
S~The question comes first, then the breath she has probably been holding all day.|
S~Confirmation of safety matters before expecting her fear to settle.|
S~They are gone. Give her room to feel safe again at her own pace.|
D~I am glad she can say how frightened she was without them standing there.|
S~A familiar calm evening would be a good thing for her now.|
S~The noise has left, and the survivor finally has room to describe what it cost.|
S~Silence can be a tremendous relief when it belongs to the place again.|
N~Threat withdrawn. Reassurance should be factual and patient.|
S~The port has its own gentler air back around it.|
S~No teasing her for being scared. The fear was justified.|
S~I wonder what ordinary sound first tells her the village is itself again.
''')
add('three_port_all_well','ThreeIsland_Port_Text_EverythingTurnedOutForBest',
    'After the bikers leave and Lostelle is found, the woman celebrates both resolutions.','''
S~A quiet port and a child safely home. That is an excellent end to a very loud day.|
S~Two separate threats have resolved. Her relief encompasses the whole community.|
S~Good. The neighbors and Lostelle can get back to ordinary life.|
S~It is lovely hearing the missing part of the good news finally arrive.|
S~A safe child and a peaceful village are worth a proper shared meal.|
S~The tangled island story has found the gentle endings its people deserved.|
S~The little place can let its attention return to smaller things.|
N~Both immediate objectives resolved. A welcome basis for recovery.|
S~The road back home has stopped carrying an unanswered question.|
S~A simple happy summary, with a lot of real relief underneath it.|
S~I wonder how quickly the good news traveled from house to house.
''')
add('prospector_plan','ThreeIsland_DunsparceTunnel_Text_ProspectingForGold',
    'The prospector hopes to find gold and buy a house in Kanto.','''
S~A future house is currently hiding somewhere in this rock. I hope his pick finds a sensible route.|
N~The goal is concrete, though prospecting has uncertain returns and substantial effort.|
N~Hope he works safely. A future home is not worth being trapped down here.|
S~It is lovely hearing a very ordinary dream give the hard work a direction.|
N~Food, rest, and safe tools belong in that plan too.|
S~The miner's imagined next setting is a quiet house paid for by this noisy chapter.|
S~A little light in a tunnel can be the thought of a window elsewhere.|
N~Clear objective, uncertain resource yield. Keep the safety margin real.|
S~He is asking the stone for a door into another kind of life.|
S~A home is a good thing to want. I hope the plan leaves room to enjoy getting there.|
S~I wonder what sort of neighborhood he imagines living in.
''')
add('prospector_nugget','ThreeIsland_DunsparceTunnel_Text_ThatsANugget',
    'After giving a Nugget or on later visits, the prospector jokes that gold must stand in for wisdom.','''
S~Gold instead of wisdom. Much heavier in the pocket, occasionally easier to spend.|
S~His success has made him generous, and the joke keeps the gift from feeling grandiose.|
S~Kind of him to share. Hope he keeps enough for the house he wanted.|
S~It is lovely when somebody remembers you knew them before the good news.|
S~A little of his happy day is leaving with someone else.|
M~The philosopher has settled his lack of aphorisms with an unusually tangible alternative.|
S~A warm joke carrying a small bright piece of luck.|
S~Actual useful material, zero lecture. A strong gift format.|
S~The stone has answered, and he has left a little of the answer in another hand.|
S~He makes the generosity easy to accept with a modest little joke.|
S~I wonder whether he has already started looking at houses.
''')
add('prospector_full','ThreeIsland_DunsparceTunnel_Text_WhoopsBagCrammedFull',
    'The prospector postpones the Nugget gift because our bag is full.','''
N~His fortune has arrived. Our carrying capacity has not kept pace.|
N~The intended Nugget transfer failed; he explicitly offers to defer it.|
N~Make some room. No need to rush a generous person.|
F~It is nice that he makes the delay feel so uncomplicated.|
N~A little sorting will let us accept the gift without making a fuss.|
N~The golden conclusion has paused for a distinctly ordinary luggage problem.|
N~A good day is waiting patiently outside a crowded pocket.|
N~Handoff postponed. Capacity can be corrected before retrying.|
N~The small bright thing can wait while a little space is cleared.|
N~He handles the awkwardness kindly. Appreciated.|
N~I wonder what in the bag we have been meaning to put away for days.
''')
add('game_scuffed_floor','TwoIsland_JoyfulGameCorner_Text_PunkScuffedUpMyFloor',
    'After the biker interruption ends, Lostelle\'s worried father notices the damage to his floor.','''
N~A worried day has acquired one more small ugly mark from somebody who did not care.|
N~The material damage adds to a situation already stressful for him.|
N~The biker should not have brought the machine inside. The search still matters more.|
N~Sometimes a small mess is the thing your mind can hold while the bigger worry is too much.|
N~The floor can be fixed. I hope he soon hears something good about his daughter.|
N~The rude visitor exits, leaving a minor piece of damage in a much more anxious scene.|
N~An ordinary scratch can become the only easy complaint in an impossible-feeling hour.|
N~Damage noted. Prioritize the missing child before maintenance.|
N~A hard little scrape beside a much larger worry.|
N~He has had enough intrusion for one afternoon. A little respect would help.|
N~I wonder who can stay here with him while the search continues.
''')
add('game_lostelle_request','TwoIsland_JoyfulGameCorner_Text_PleaseGoToThreeIsland',
    'Lostelle\'s father asks us to search Three Island while he waits in case she returns.','''
N~A worried dad trying to be in two places at once has finally asked for another pair of feet.|
N~Staying at the expected meeting point while someone else searches is a sensible division.|
N~Go prepared and follow the lead. He needs reliable help, not a brave speech.|
D~The way he explains why he cannot leave makes the worry feel very close.|
N~A clear search and a way to return news would help him more than a vague promise.|
N~The father holds the familiar door open while asking us to find the missing part of his day.|
N~Waiting can be the hardest task when it is the one you need to do.|
N~Roles assigned: fixed return point here, active search there. Keep it deliberate.|
N~One person stays where the child expects home to be. Another follows the path outward.|
N~He has given a useful address through a great deal of fear. We should remember it.|
N~I wonder when Lostelle was last seen leaving for the forest.
''')
add('game_no_play','TwoIsland_JoyfulGameCorner_Text_NotRunningAnyGamesToday',
    'The attendant says no games are running today.','''
N~The games can wait. There is a much more important reason the room feels quiet.|
N~The service is currently unavailable. We should respect the closure.|
N~Fair enough. No need to press the attendant.|
N~It does not sound like a day for trying to make the place lively.|
N~A little patience is a reasonable thing to offer here.|
N~The entertainment program has been set aside for a real concern beyond the counter.|
N~A quiet room is allowed to stay quiet when people are worried.|
N~Service paused. Choose another activity without adding pressure.|
N~The bright little room is waiting for better news.|
N~A simple explanation is enough. They do not owe us a cheerful performance.|
N~I wonder whether someone has checked that the staff are managing all right.
''')
add('game_soon','TwoIsland_JoyfulGameCorner_Text_GetGamesGoingSoon',
    'After Lostelle is rescued, the attendant says games will start again soon.','''
S~The room is beginning to remember what it was built for. Good news.|
S~The service is preparing to resume after the immediate family concern is resolved.|
N~Let them get ready. No need to hurry the return to normal.|
S~It is lovely when ordinary fun can be the next thing again.|
S~A happy noisy room will feel different after the worrying quiet.|
S~The little venue prepares to reopen its gentler kind of excitement.|
S~A place can slowly grow cheerful again after the hard news passes.|
N~Service restart pending. Give the staff time to restore the setup.|
S~A small bright sound may soon return to the room.|
S~A calm promise is kinder than pretending everything was instantly fixed.|
S~I wonder which game the returning regulars will ask for first.
''')
add('game_found_scene','TwoIsland_JoyfulGameCorner_Text_LostelleItsOkayDaddy',
    'At the end of the reunion, Lostelle reassures her father and celebrates making friends with us.','''
S~She has found a kind little thing inside a frightening day. I am glad her dad can hear it.|
S~Her reassurance marks a return to safety without requiring her to retell every frightening detail.|
S~Good. She is home, and her father knows she is safe.|
S~That is a lovely ending to all the waiting.|
S~A familiar room and a familiar voice can make the relief feel real at last.|
S~The reunion ends on the child's own gentler account of the story.|
S~A small voice has put some warmth back into a room full of worry.|
N~Safe return confirmed. Let the family have their moment.|
S~The missing footsteps have come back through the door.|
S~She gets to choose the bright part she tells first. That feels right.|
S~I wonder whether her father will remember that exact little sentence for years.
''')
add('game_future_running','TwoIsland_JoyfulGameCorner_Text_IllGetGameCornerRunning',
    'On a later visit, Lostelle\'s father plans to reopen and invites us to return with a friend.','''
S~A room full of games can return to being a room full of games. Excellent recovery plan.|
S~He is returning to ordinary work and explicitly welcoming shared participation.|
N~Good to hear him making plans without fear in every word.|
S~It is nice when a familiar job becomes something happy to look forward to again.|
S~A small ordinary celebration with a friend sounds right for this place.|
S~The worried father resumes the more cheerful role of host.|
S~A little invitation where an urgent plea used to be.|
N~Normal operation planned. Multiplayer requirement clearly stated.|
S~The room has room for play again. A lovely small change.|
S~He is inviting us back as guests instead of people carrying the next worry.|
S~I wonder what reopening will feel like for the first pair of visitors.
''')
add('game_gift_full','TwoIsland_JoyfulGameCorner_Text_NotGoingToFitInBag',
    'Lostelle\'s father cannot give the Moon Stone because our bag is full.','''
N~A kind thank-you has reached a very stubborn pocket. We can fix the pocket.|
N~The Moon Stone handoff failed. The earlier delivery and this reward are separate outcomes.|
N~Make room before asking again. His thanks is already clear.|
F~It is awkward, but he has had bigger things to worry about than our bag.|
N~A little sorting will let the generous moment finish calmly.|
N~The heartfelt reward has paused for the least romantic obstacle: packed luggage.|
N~A small stone waiting patiently outside an overly busy bag.|
N~Reward pending after capacity failure. Do not count it as obtained.|
N~A bit of pale stone needs a small place cleared for it.|
N~We can deal with our own inconvenience without making him repeat his gratitude.|
N~I wonder what we can finally put away after carrying it all this way.
''')
add('game_lostelle_repeat','TwoIsland_JoyfulGameCorner_Text_PleaseShowMeYouBeingCool',
    'Lostelle eagerly asks to see us being impressive again.','''
S~A small enthusiastic fan has requested a sequel. I hope ordinary kindness is exciting enough.|
N~Her admiration need not require recreating the dangerous situation that prompted it.|
S~A safer fun day would be a much better repeat performance.|
F~It is sweet, though I would be nervous trying to match her picture of us.|
S~We can show her something pleasant without making a whole adventure out of it.|
S~The youngest critic requests another show with a very broad creative brief.|
S~A little admiration, still bright enough to make the room warmer.|
N~Need to define impressive without introducing another hazard.|
S~She has kept the kind part of the story ready in her eyes.|
S~Being good company may be a quieter kind of cool worth showing her.|
S~I wonder which small everyday skill she would find most astonishing.
''')
add('kindle_maria','OneIsland_KindleRoad_Text_MariaPostBattle',
    'Maria asks us not to splash her makeup.','''
N~A very clear request from the small fragile artwork currently on her face.|
N~The practical boundary is simple: avoid splashing her.|
N~Easy enough. Give her room in the water.|
F~I would be embarrassed if something I had carefully done was ruined as a joke.|
N~A little consideration costs less than making someone start over.|
M~The face has a carefully managed costume department and a strict water policy.|
N~An ordinary preference is allowed to remain ordinary. No teasing required.|
N~Water-sensitive finish. Maintain a respectful distance.|
N~A small painted thing is asking the sea to be a little gentler.|
S~Makeup takes effort. Respecting the request is hardly difficult.|
N~I wonder how she manages to keep the rest of the look so neat while swimming.
''')
add('kindle_abigail','OneIsland_KindleRoad_Text_AbigailPostBattle',
    'Abigail admires our cap and considers wearing one.','''
S~Our hat has successfully recruited a new member of the shade appreciation club.|
S~A useful piece of clothing can be appealing in both appearance and function.|
N~A cap helps in the sun. Find one that stays put in the wind.|
F~A small compliment can make you notice something you wear without thinking.|
S~A practical bit of shade is a good thing to enjoy wearing.|
S~The costume receives a favorable review and a tentative request for adaptation rights.|
S~A familiar little thing becoming someone else's new idea.|
N~Useful design, visible demonstration. Sensible candidate to try.|
S~A little roof carried wherever your thoughts wander.|
S~A cap can finish a look and save your eyes some squinting. Strong choice.|
S~I wonder which color she would pick for herself.
''')
add('kindle_finn','OneIsland_KindleRoad_Text_FinnPostBattle',
    'Finn admires the immense island sky.','''
S~A sky with very few buildings trying to squeeze into the view. Lovely arrangement.|
S~An open horizon changes the perceived scale of the surroundings.|
S~Good place to stop and look for a moment.|
S~It makes the road feel quiet in a way I like.|
S~A wide view can make an ordinary rest feel like part of the outing.|
S~The island has reserved an exceptionally large backdrop.|
S~A vast empty-looking thing that never quite runs out of detail.|
S~Excellent visibility. No artificial skyline in the way.|
S~There is room above us for a thought to stretch without hitting anything.|
S~A simple view with no need to add an attraction sign.|
S~I wonder how different the clouds look after the weather turns.
''')
add('kindle_garrett','OneIsland_KindleRoad_Text_GarrettPostBattle',
    'Garrett recommends swimming ourselves rather than always riding with Surf.','''
N~Our arms may have a different leisure proposal, but the partner deserves a break too.|
N~Direct swimming can be enjoyable when skills, conditions, and stamina are appropriate.|
N~Only where it is safe. No need to prove anything to a stranger.|
N~I would want calm water and someone who knows the shore.|
N~A little exercise is fine when it fits the person, not just somebody else's idea of the day.|
N~The comfortable traveler is offered an unsolicited alternative with considerably more arm work.|
N~Enjoying the sea does not require every visitor to enjoy it in the same way.|
N~Method should match conditions and capability. No universal best choice.|
N~The water asks different things from a rider and a swimmer.|
N~A suggestion is fine. Making comfort sound like a failing would be less helpful.|
N~I wonder where he recommends a beginner can safely practice.
''')
add('kindle_tommy','OneIsland_KindleRoad_Text_TommyPostBattle',
    'Tommy is disappointed to lose the battle and miss a big catch.','''
N~A very uncooperative afternoon has managed two separate exits.|
N~Two disappointments close together can make each feel larger. Neither fixes the other.|
N~Take a breather. Chasing both results while upset will not help.|
N~It is rough when the thing you hoped would rescue the day goes wrong too.|
N~A quiet break might keep the next attempt from becoming another frustration.|
N~The double-feature tragedy has included both a defeat and a departing fish.|
N~Some days seem determined to leave you holding the empty end of something.|
N~Reset attention before another try. Frustration is poor operating input.|
N~The line and the battle have both gone slack at once.|
N~He deserves a moment to be disappointed without being made fun of.|
N~I wonder which loss he will remember once the afternoon feels less sharp.
''')
add('kindle_sharon','OneIsland_KindleRoad_Text_SharonPostBattle',
    'Sharon warmly praises our battle skill.','''
S~A compliment and a friendly opinion in one little breath. Nice ending.|
S~She responds positively to the performance rather than treating the loss as an insult.|
S~Good of her. The team worked for that result.|
F~That is a very direct, very kind thing to say.|
S~It is lovely to leave someone happy to have met us.|
S~The match closes on a gracious review rather than a demand for a sequel.|
S~A small warm word makes the road feel friendlier afterward.|
S~Positive feedback with a clear basis. Useful and pleasant.|
S~The meeting has left a little warmth beside the water.|
S~She makes liking someone sound refreshingly uncomplicated.|
S~I wonder which bit of our approach she noticed most.
''')
add('kindle_tanya','OneIsland_KindleRoad_Text_TanyaPostBattle',
    'Tanya plans to work harder after losing.','''
N~Tomorrow's plan has more training in it. I hope it leaves a chair for rest.|
N~More effort helps when it is directed toward a specific observed weakness.|
N~Train well, not just longer. The partners need recovery too.|
S~It is good to hear determination survive a disappointing match.|
N~A routine worth keeping should be kind enough to keep doing.|
S~The result is immediately converted into a pledge for the next rehearsal.|
N~Harder is an easy word. A useful plan needs a few more.|
N~Identify the change before increasing the load.|
N~A path grows clearer when the next step has a purpose.|
N~She can be ambitious without making every day a punishment for this one.|
S~I wonder what she would most like the team to handle better.
''')
add('kindle_shea','OneIsland_KindleRoad_Text_SheaPostBattle',
    'Shea blames the loss on exhaustion from running.','''
N~The legs spent the energy before the battle asked for its share. A scheduling problem.|
N~Preexisting fatigue can affect performance, though it is not the only possible factor.|
N~Rest first. No point making the next match a test of exhaustion too.|
N~It is hard to think clearly when the rest of you already wants to stop.|
N~A little recovery would help more than another excuse or another immediate challenge.|
N~The runner's day has booked two demanding scenes against one reserve of energy.|
N~The body occasionally objects to the second half of an ambitious afternoon.|
N~Shared energy budget exceeded. Sequence the tasks more carefully.|
N~A long run has left the battle very little room to stand.|
N~A fair reason to pause, even if the match deserves a fuller review later.|
N~I wonder whether she planned to battle before starting the run.
''')
add('kindle_hugh','OneIsland_KindleRoad_Text_HughPostBattle',
    'Hugh comments on martial artists becoming interested in fashion.','''
S~A strong punch and a pleasing outfit are perfectly capable of sharing a person.|
N~Interest in appearance does not reduce the discipline of another pursuit.|
N~They still have to train. Clothes can be something else they enjoy.|
S~It is nice when people get to be more than the one role expected of them.|
N~Comfortable clothing should still let them do the work safely.|
S~The martial arts program has admitted the costume department without losing the plot.|
S~A severe-looking interest can leave room for a little personal vanity.|
N~Appearance and function are separate design goals that can coexist.|
S~A practiced movement can belong to someone who also likes a particular color.|
S~Of course they can care about style. Strength does not require an empty wardrobe.|
S~I wonder which look he has noticed changing around the dojo.
''')
add('kindle_bryce','OneIsland_KindleRoad_Text_BrycePostBattle',
    'Bryce praises the taste of local volcanic-region water.','''
N~An enthusiastic water review. I would still prefer a known safe source to a random puddle.|
N~Mineral content may influence taste, but location alone does not establish drinking safety.|
N~Use a safe supply. A volcano is not a quality certificate.|
S~A familiar local flavor can become part of what someone loves about a place.|
N~Good water matters. So does knowing where it came from.|
S~The landscape has received a surprisingly culinary review.|
N~Stone can leave a taste in the things that pass through it. Not always an invitation.|
N~Composition and safety are separate checks. Ask the source.|
S~A mountain can leave a little trace in an ordinary glass.|
N~I like the affection for the place. I would keep the recommendation specific.|
S~I wonder whether he notices the difference when he travels elsewhere.
''')
add('kindle_claire','OneIsland_KindleRoad_Text_ClairePostBattle',
    'Claire is hungry again after the battle.','''
N~The afternoon has filed another request with the lunch department.|
N~Exertion can make the need for a meal more noticeable. A practical next stop.|
N~Eat and rest before taking on more. Simple enough.|
N~It is hard to enjoy the scenery once your stomach is making all the decisions.|
S~A proper meal sounds better than pretending a battle snack will carry the whole day.|
N~The next chapter has been decisively assigned to food.|
N~A hunger that has returned is rarely persuaded by a stern look.|
N~Low fuel warning. Do not schedule another test before addressing it.|
N~The body has made the wide world briefly smaller than a bowl.|
N~A sensible reason to pause, without needing a more impressive explanation.|
S~I wonder what the local place serves that she is hoping for.
''')
add('kindle_kia','OneIsland_KindleRoad_Text_KiaPostBattle',
    'Kia is astonished that anyone could beat her big brother.','''
S~A big brother can still be wonderful after meeting somebody better at one battle.|
N~A child's strong admiration need not depend on an unbroken victory record.|
S~He can be someone she trusts without winning every match.|
S~I remember how enormous a familiar person can seem when you are small.|
S~A little reassurance from him would matter more than a rematch right now.|
S~The unbeatable family hero has encountered a plot development the audience did not expect.|
S~A small disappointment can leave room for a more ordinary, steadier kind of admiration.|
N~New evidence challenges the simple ranking. The relationship remains intact.|
S~A tall familiar shadow is still shelter even when another one reaches farther.|
S~She will learn more from how he treats her now than from whether he won.|
S~I wonder what kind thing he will say when he hears how surprised she is.
''')
add('kindle_mik','OneIsland_KindleRoad_Text_MikPostBattle',
    'Mik is surprised that his double-battle partnership with Kia failed.','''
N~A good pair can have a bad match without becoming a bad pair.|
N~Cooperation helps, but cannot guarantee every matchup or decision.|
N~Review the plan together. Do not make Kia carry the blame.|
N~I hope he remembers how much she trusts him while he thinks it through.|
N~A calm little review will help more than treating the loss like something impossible.|
N~The proud double act discovers that chemistry does not prewrite the ending.|
N~A bond can survive the discovery that it is not a shield against everything.|
N~Coordinated units still need a suitable strategy. Check what actually failed.|
N~Two joined paths can still reach a difficult patch of ground.|
N~He can keep valuing their partnership while changing the way they battle.|
N~I wonder which part of their combination he had felt most certain about.
''')
add('bond_nikki','ThreeIsland_BondBridge_Text_NikkiPostBattle',
    'Nikki rudely suggests our Pokemon smell from sweating.','''
N~A long day can smell like a long day without needing a public review.|
N~The remark contributes little beyond an unkind interpretation of ordinary exertion.|
N~The team worked hard. They deserve care, not a sneer.|
N~That would be a hurtful thing to hear after trying your best.|
N~A wash and a rest are normal needs, not moral failures.|
N~The critic has moved from battle analysis to unsolicited commentary on the cast's personal condition.|
N~An unkind little sentence, dressed as an observation.|
N~Identify a practical need without insulting the living participants. Not difficult.|
N~A tired creature should be met with water and kindness before judgment.|
A~There is a way to mention hygiene without making the partner feel disgusting.|
N~I wonder whether she realizes the Pokemon is standing right here hearing her tone.
''')
add('bond_violet','ThreeIsland_BondBridge_Text_VioletPostBattle',
    'Violet points us along the bridge toward Berry Forest.','''
N~The forest is still ahead. A useful direction for a search with no time to become a scenic stroll.|
N~The route continues toward the named destination. A concrete navigation cue.|
N~Keep going carefully. Watch for signs of the child along the way.|
N~It is reassuring to hear we are still on the right path.|
N~A clear direction saves strength for the part that matters.|
N~The bridge's next setting is identified without unnecessary suspense.|
N~A little certainty makes a long path feel less empty.|
N~Destination ahead confirmed. Continue tracking landmarks.|
N~The trees are waiting at the end of this open little road.|
N~Simple helpful information is welcome on a worrying trip.|
N~I wonder how far beyond the bridge the first Berry paths begin.
''')
add('bond_amira','ThreeIsland_BondBridge_Text_AmiraPostBattle',
    'Amira resolves to learn swimming this year.','''
S~A good new skill, preferably learned somewhere kinder than the strongest current.|
N~Qualified instruction and suitable conditions make a useful goal more achievable.|
S~Good plan. Learn safely with someone watching.|
S~It is lovely to hear someone make a promise to try something that has felt difficult.|
N~Start gently. A steady first lesson is better than a frightening big leap.|
S~The next year's personal program has acquired a very practical new act.|
S~A body can learn to trust a place that once felt like a boundary.|
N~Clear skill objective. Break it into supervised steps.|
S~A little courage can begin at the shallow edge.|
S~She does not have to look graceful before she starts learning.|
S~I wonder what finally made this feel like the year to try.
''')
add('bond_alexis','ThreeIsland_BondBridge_Text_AlexisPostBattle',
    'Alexis is confused about whether the battle ended in victory or defeat.','''
N~The match has ended; the result seems to be arriving a few moments behind it.|
N~A simple factual answer is more useful than making fun of the confusion.|
N~We won this one. Give her a moment to settle.|
N~That is a disorienting feeling, losing track of something happening right in front of you.|
N~A quiet break is sensible if she is too tired or distracted to follow the result.|
N~The final scene has concluded before its participant received the program note.|
N~A strange little gap between an event and understanding that it happened.|
N~Outcome unclear to the participant. Confirm it and check whether she needs a rest.|
N~The thought has not quite found its way back to the room.|
N~We can answer plainly and kindly. No need to make it a joke at her expense.|
N~I wonder whether she was distracted by something else on her mind.
''')
add('bond_tisha','ThreeIsland_BondBridge_Text_TishaPostBattle',
    'Tisha cannot leave the water because a Pokemon damaged her swimsuit.','''
N~That is an awkward problem that needs a towel, not an audience.|
N~Her immediate need is privacy and a safe way to get out of the water.|
N~Find something to cover her. Give her room.|
F~I would be mortified. We should look away and help quietly.|
N~A towel or a spare layer would do more than any amount of commentary.|
N~A deeply inconvenient costume failure deserves discreet practical assistance.|
N~An embarrassing moment should not be made into everyone else's entertainment.|
N~Provide cover, preserve privacy, then address any injury.|
N~A small piece of cloth can become a very important kind of shelter.|
N~No staring. Help her get something she can wear safely ashore.|
N~I wonder whether a nearby friend has a towel ready.
''')
add('bond_joy','ThreeIsland_BondBridge_Text_JoyPostBattle',
    'Joy enjoyed the double battle and hopes for another.','''
S~A loss that still leaves someone wanting another happy match. Good sign.|
S~Enjoyment need not depend on the winning outcome. The invitation is friendly.|
S~Good match. Another time when both teams are ready.|
S~I like hearing the first question be whether it was fun.|
S~A shared game worth repeating has done something right.|
S~The delighted participant requests a sequel without demanding a revised ending.|
S~A little competition has left something friendly behind it.|
S~Positive experience recorded across a loss. Strong game design.|
S~Two paths crossed and left a small invitation between them.|
S~She makes the next meeting feel welcome rather than owed.|
S~I wonder which part of the teamwork she enjoyed most.
''')
add('bond_meg','ThreeIsland_BondBridge_Text_MegPostBattle',
    'Meg happily asks Joy whether she enjoyed their shared battle.','''
S~She checked on her partner's fun before checking the scoreboard. I like that.|
S~Her first concern is the shared experience between the two trainers.|
S~Good to ask. A team should know how both people felt about the match.|
S~It is sweet that she turns toward Joy with that much certainty of welcome.|
S~A game feels better when someone actually wants to know if you enjoyed it.|
S~The double act ends by reviewing the important part with each other.|
S~A happy question holding the partnership together.|
S~Direct partner feedback. Simple and useful.|
S~The end of the battle still leaves two people smiling toward the same thing.|
S~She is making room for Joy's answer, not just announcing her own.|
S~I wonder whether they talk this warmly after practice too.
''')
add('ember_digging','MtEmber_Exterior_Text_WellTryDiggingHere',
    'A Rocket grunt discusses digging for a treasure mentioned by the admins.','''
N~A treasure hunt is much less charming when Rocket has already assigned the destination.|
N~They have a specific objective based on an internal report, but its accuracy is unverified.|
N~Watch what they are doing. Their interest here is worth remembering.|
N~It feels unpleasant hearing a familiar kind of excitement from them.|
N~A mountain is not simply a box of things to haul away.|
N~The excavation scene has a regrettably familiar criminal production company.|
N~A hidden thing can attract rather more than innocent curiosity.|
N~Resource target identified. Need to distinguish a rumor from an actual find.|
N~The stone is being asked for something by hands I would not trust with it.|
N~They sound certain somebody else has already told them what to expect.|
N~I wonder what the admins actually knew about this location.
''')
add('ember_get_lost','MtEmber_Exterior_Text_YoureInTheWayGetLost',
    'The other grunt rudely orders us away from the excavation.','''
N~The mountain's self-appointed reception desk has rejected our existence nearby.|
N~His hostility provides no legitimate reason for excluding other visitors.|
N~Keep a safe distance without letting him decide the whole route.|
N~I would rather not stand close while he works himself into another threat.|
N~A quiet step aside can give us time to judge the situation.|
N~The guarded excavation offers a spectacularly unhelpful visitor policy.|
N~A voice sharpened to make a public place feel privately hostile.|
N~Hostile access claim. No explanation of actual authority provided.|
N~The rough words are trying to become a wall.|
N~He could have simply asked for room to work. The threat says more.|
N~I wonder how many ordinary hikers have been turned away like that.
''')
add('ember_grunt1','MtEmber_Exterior_Text_Grunt1PostBattle',
    'On a standalone return interaction, the defeated grunt bitterly asks why we had to win.','''
N~An odd complaint to bring to someone he challenged in the first place.|
N~The outcome follows the battle; it is not a personal obligation we failed to avoid.|
N~The team did its job. He can stop blaming us for trying.|
N~He sounds more disappointed in being stopped than worried about what he was doing.|
N~We do not need to make the partners smaller to protect his pride.|
N~The defeated antagonist files a formal objection to the script containing opposition.|
N~The answer is unkindly simple: someone had to lose that match.|
N~Expected contest had a possible losing state. He appears unhappy to confirm it.|
N~A hard result has left him holding a question with no useful answer.|
N~He is allowed disappointment. The accusation is not necessary.|
N~I wonder what he thought would happen if someone finally pushed back.
''')
add('ember_grunt2','MtEmber_Exterior_Text_Grunt2PostBattle',
    'The defeated grunt absurdly demands that we forget everything overheard.','''
M~A convenient case of amnesia has been requested at the information desk. Denied.|
N~A command to forget does not change the information already learned.|
N~We heard it. His threat does not erase the lead.|
N~It is an oddly desperate request after so much confidence.|
N~Useful information is worth remembering when someone urgently wants it gone.|
M~The failed security officer attempts a vigorous verbal edit to our memory.|
M~A remarkably ambitious request for someone whose last plan did not work.|
N~Data deletion request lacks authorization and any practical mechanism.|
N~A spoken secret cannot be pushed back into an empty mouth.|
N~He would probably have preferred keeping his voice down earlier.|
N~I wonder whether he has realized how much the others let slip.
''')
add('ember_rocket_retreat','MtEmber_Exterior_Text_WellRegroupDontStepInsideThere',
    'After the linked battles, the Rockets retreat while warning us away from the cave entrance.','''
N~They have left a door and an extremely unconvincing reason not to look at it.|
N~Their retreat resolves the immediate confrontation, not the uncertainty about the passage.|
N~Check the team before entering. The threat does not tell us what is inside.|
N~I will be glad when they are gone, even with the warning still hanging there.|
N~A new cave entrance deserves preparation rather than a rush after departing voices.|
N~The exiting villains spend their final lines advertising the forbidden next setting.|
N~Some warnings protect you. This one mostly sounds protective of their own plans.|
N~Access point exposed. Inspect conditions before proceeding.|
N~A rough voice leaves, and the mountain keeps the opening behind it.|
N~We can hear the practical uncertainty without obeying their ownership claim.|
N~I wonder what they managed to disturb while opening the route.
''')
add('ember_logan','MtEmber_Exterior_Text_LoganPostBattle',
    'Logan enthusiastically repeats a global volcano count and describes his excitement.','''
U~That is a lot of mountains with very dramatic interiors. He has chosen a spectacular interest.|
N~The count is a reported estimate, not something established by this conversation.|
N~Good to be interested. Keep a safe distance from the hot parts.|
S~He sounds happy in a way that is entirely his own.|
N~An exciting subject still deserves water, sensible shoes, and good footing.|
S~An enthusiastic geological review delivered with a highly personal temperature report.|
S~A strange warm joy, but a sincere one. Those are allowed.|
U~Volcanic systems are fascinating. I would like reliable records behind the number.|
S~The thought of so much old heat has made his afternoon brighter.|
S~I like a person knowing exactly which kind of scenery makes them enthusiastic.|
S~I wonder which volcano he most wants to visit after this one.
''')
add('ember_beth','MtEmber_Exterior_Text_BethPostBattle',
    'Beth explains how flowing lava can leave a cavern when the outer layer hardens.','''
U~The mountain can make a hallway by letting the inside run away. Clever stone trick.|
S~A hardened exterior can preserve a channel after the flowing material drains away.|
N~Useful to know how the ground formed. Still need to check where it is safe.|
S~It is strange to imagine the empty passage once full of moving heat.|
N~A good explanation makes the scenery worth looking at a little longer.|
S~The cavern's empty room receives an unexpectedly vivid construction history.|
S~A great hot movement remembered by the space it left behind.|
S~Natural tube formation! The remaining shell tells the story of the flow.|
S~The mountain has kept the shape of something that would not stay still.|
S~A simple explanation can make an ordinary-looking rock feel entirely different.|
S~I wonder whether there is a passage nearby where the shape is especially clear.
''')
add('ember_jocelyn','MtEmber_Exterior_Text_JocelynPostBattle',
    'Jocelyn says our battling reminds her of the person who ended their relationship.','''
N~An unfortunate memory for the battle to shake loose. We did not mean to bring that guest.|
N~A resemblance in style can trigger an association without saying anything about us personally.|
N~That sounds rough. No need to press her for the story.|
F~It must feel strange when a little familiar movement catches you before you are ready.|
N~A quiet moment would be kinder than making a joke about the comparison.|
N~An unrelated performance has wandered into a much more personal old chapter.|
N~Memories have a habit of arriving without checking the room first.|
N~Association noted. It does not require recreating the relationship in this conversation.|
N~An old footprint has appeared briefly inside a new one.|
N~She can notice the resemblance without needing to explain the whole history to us.|
N~I wonder whether saying it aloud makes the memory easier to set back down.
''')
