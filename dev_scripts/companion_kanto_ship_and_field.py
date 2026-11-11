"""S.S. Anne and remaining mainland Kanto field-interior NPC terminals."""
ROWS=[]
EMOTIONS=dict(N='neutral',S='soft_smile',A='annoyed',F='flustered',D='sad',U='surprised',M='smug',L='laughing')
def add(key,labels,subject,lines):
    replies=[]
    for line in lines.strip().split('|'):
        line=line.strip()
        if len(line)>1 and line[1]=='~' and line[0] in EMOTIONS:line=EMOTIONS[line[0]]+line[1:]
        replies.append(line)
    assert len(replies)==11,(key,len(replies))
    ROWS.append(dict(key='kanto_sf_'+key,labels=labels.split(),subject=subject,replies=replies))

add('ship_waiter','SSAnne_1F_Corridor_Text_LeStrongSilentType',
    'The waiter interprets our silence as the strong silent personality type.','''
M~Sometimes silence means confidence. Sometimes it means still reading the menu.|
N~He inferred a personality from a very limited response. Efficient, but not reliable.|
N~Quiet does not always need an explanation.|
F~I would be relieved and embarrassed to have my hesitation handled that neatly.|
S~He is trying to keep the welcome comfortable. Good service instinct.|
M~The waiter supplies a character description when the guest declines to provide dialogue.|
M~An excellent strategy: remain quiet until someone assigns you an impressive motive.|
N~Missing input has been given a very flattering default value.|
S~A little silence has been offered a comfortable chair in the conversation.|
S~He managed the awkward pause kindly. That is a real skill.|
S~I wonder how many different kinds of quiet guest he has met.
''')
add('ship_restless','SSAnne_1F_Corridor_Text_PassengersAreRestless',
    'A crew member warns that bored passengers may challenge us.','''
N~Cabin fever has apparently developed a battle schedule.|
N~A confined, lengthy trip can leave passengers looking for stimulation.|
N~Keep the team ready. We can choose a quiet room when they need rest.|
N~I would prefer boredom to announce itself without quite so much eye contact.|
N~A relaxed cruise for one person may be an unexpected match for another.|
M~The leisure program has begun recruiting guests directly from the corridor.|
N~A long voyage gives an idle competitive streak far too much room.|
N~Unscheduled challenges likely. Manage resources before exploring every cabin.|
N~The sea keeps people close enough for their restlessness to meet.|
N~A useful warning before the next passenger decides we are entertainment.|
N~I wonder what activities the crew planned before the battles took over.
''')
add('ship_agent','SSAnne_1F_Room1_Text_ImAGlobalPoliceAgent',
    'A hushed passenger identifies himself as an agent pursuing Team Rocket.','''
N~An undercover introduction with a very short period of remaining under cover.|
N~He claims an investigative role and a specific target. Discretion would be appropriate.|
N~Keep his business quiet. No need to make him easier to spot.|
N~I would feel awkward being told a secret before knowing where to stand.|
N~I hope the investigation keeps the ordinary passengers safe too.|
M~The secret agent announces his secret occupation to the nearest available stranger.|
N~A whisper is not a lock, but we need not make it less private.|
N~Sensitive information volunteered. Avoid redistributing it casually.|
N~A quiet pursuit is moving among the holiday voices.|
N~He sounds serious. We can respond with a little care instead of curiosity alone.|
N~I wonder what led the trail onto this ship.
''')
add('ship_tyler','SSAnne_1F_Room2_Text_TylerPostBattle',
    'Tyler eagerly asks to become friends so we can trade and spend time together.','''
S~A battle has become an enthusiastic application for friendship. Nice turn.|
S~A shared activity can provide a natural start to a new acquaintance.|
S~He can ask. No need to rush the whole friendship in one breath.|
F~That is very direct. I would probably smile before finding an answer.|
S~It is lovely when someone leaves a match wanting more company.|
S~The former opponent proposes a much friendlier sequel.|
S~An awkwardly sincere invitation. Those can be good ones.|
S~Shared interest identified. Start with a manageable conversation.|
S~A little meeting has found somewhere new to grow.|
S~He makes the welcome clear without pretending to be sophisticated about it.|
S~I wonder which Pokemon he would most like to tell a new friend about.
''')
add('ship_ann','SSAnne_1F_Room2_Text_AnnPostBattle',
    'Ann is upset that her Pokemon were hurt and demands Pokemon Center healing.','''
N~A battle should end with care for the partners, even when the complaint comes loudly.|
N~Her concern is legitimate, though responsibility for recovery should not be reduced to an accusation.|
N~Make sure her team gets help. No need to argue over the result.|
D~She sounds more worried about them than about losing.|
N~Getting the partners comfortable matters more than defending anyone's pride.|
N~The match receives an impassioned review from the person watching her team hurt.|
N~A familiar partner looking tired can make every word come out sharply.|
N~Post-battle recovery is the immediate practical requirement.|
N~The fight is finished; the care still has something left to do.|
N~Her fear could use a calm answer rather than another sharp one.|
N~I wonder whether she knows the nearby cabin offers a place to rest.
''')
add('ship_family_cruise','SSAnne_1F_Room2_Text_CruisingAroundWorld',
    'A parent describes traveling around the world with their children.','''
S~A whole family collecting new horizons. That could fill several dinner conversations.|
S~Shared travel can provide children with a broad range of direct experiences.|
S~Hope they are taking the journey at a pace everyone enjoys.|
S~It must be lovely to have those memories belong to all of you.|
S~A familiar family meal can make even a distant port feel less strange.|
S~A family story with an exceptionally expansive choice of settings.|
S~A moving little home, with unfamiliar shores outside it.|
N~A large itinerary needs room for different ages and energy levels.|
S~The world keeps changing beyond the window while the familiar voices stay.|
S~A good trip gives everyone a little say in what they notice.|
S~I wonder which place the children keep talking about.
''')
add('ship_elegance','SSAnne_1F_Room3_Text_CruiseIsElegantAndCozy',
    'A passenger enjoys the cruise\'s elegance and comfort.','''
S~Fancy and comfortable at once. A rare treaty between stiff collars and pillows.|
S~The setting combines novelty with a controlled, familiar base of accommodation.|
S~Good to enjoy a journey without having to prove it was uncomfortable.|
S~A place can feel special and still let you relax. I like that.|
S~A comfortable room makes the unfamiliar parts of travel easier to enjoy.|
S~The grand adventure has agreed to provide a soft chair between scenes.|
S~A journey with enough gentleness left in it to feel like rest.|
S~Good comfort design is easy to miss when it works.|
S~A little warm room moving across a very large cool world.|
S~Elegance works best when the people inside it can actually breathe.|
S~I wonder which small part of the ship makes it feel cozy to them.
''')
add('ship_wigglytuff_companion','SSAnne_1F_Room3_Text_AlwaysTravelWithWigglytuff',
    'A traveler always brings Wigglytuff along.','''
S~A reliable travel companion and an excellent round silhouette in every port.|
S~A familiar partner provides continuity across unfamiliar settings.|
S~Good to have someone who knows you when the place is new.|
S~That sounds less like a habit and more like not wanting to leave a friend behind.|
S~Shared little routines can make any stop feel more like home.|
S~The recurring companion receives a permanent place in every new setting.|
S~A familiar presence can make a strange room feel less borrowed.|
S~Reliable companion, well-practiced routine. Strong travel setup.|
S~Home can sometimes be the one traveling beside you.|
S~The partnership is part of how the traveler sees the world. Lovely.|
S~I wonder which part of the voyage Wigglytuff enjoys most.
''')
add('ship_pie_order','SSAnne_1F_Room4_Text_WaiterCherryPiePlease SSAnne_1F_Room4_Text_WaitressCherryPiePlease',
    'A passenger mistakes us for staff and orders cherry pie.','''
M~I also support cherry pie, but my support does not include knowing where the kitchen keeps it.|
N~They have mistaken our role. A brief correction should resolve the request.|
N~Wrong person. Point them toward the actual staff.|
F~I would have to remember I am allowed to explain the mistake.|
M~A good order, delivered to the wrong apron. I sympathize with the craving.|
M~An unexpected casting call for the role of pastry courier.|
M~A stranger has looked at us and seen the possibility of dessert.|
N~Request routed to the wrong service provider. Redirect.|
S~A small wish for sweetness has wandered into our path.|
M~Perhaps we look competent. Perhaps they simply did not look closely.|
S~I wonder whether the cherry pie is as good as the confidence of that order.
''')
add('ship_arthur','SSAnne_1F_Room5_Text_ArthurPostBattle',
    'Arthur angrily demands privacy after the battle.','''
N~The cabin has become a very clear request for fewer visitors.|
N~His wish to end the interaction is unambiguous, despite the harsh delivery.|
N~Leave the room. No reason to give him another excuse.|
N~I would rather let him have his quiet now.|
N~A little space can end the uncomfortable part of this quickly.|
N~The private performance has concluded with an emphatic evacuation notice.|
N~A room with a door is useful for precisely this kind of mood.|
N~Session closed. Best not to keep sending input.|
N~The next useful step is simply outside the cabin.|
N~He could be more courteous. We can still respect the privacy.|
N~I wonder whether he really wanted company at all before the match.
''')
add('ship_rest_done','SSAnne_1F_Room6_Text_GladEveryoneIsRefreshed',
    'After resting in the cabin, our host is pleased we and the team look refreshed.','''
S~A little land-like comfort in the middle of the moving water. Much appreciated.|
S~The rest helped the whole traveling group, and the host noticed.|
S~Good help. We should head out only when everyone is ready.|
S~It is lovely to be welcomed as tired people rather than another challenge.|
S~A proper rest is one of the kindest gifts a traveler can get.|
S~The journey resumes after a mercifully gentle interlude.|
S~A strange ship briefly felt like somewhere familiar enough to sleep.|
N~Recovery complete. Helpful condition check before resuming.|
S~A quiet room has put a little steadiness back into the day.|
S~The host's kindness includes the Pokemon. That makes it feel complete.|
S~I wonder how many guests have been relieved to find this cabin.
''')
add('ship_rest_no','SSAnne_1F_Room6_Text_SorryYouLookLikeMyBrother SSAnne_1F_Room6_Text_SorryYouLookLikeMySister',
    'When we decline rest, the host explains that we remind them of a younger sibling.','''
S~We accidentally borrowed a familiar face and received the family kindness attached to it.|
S~A resemblance prompted a caring offer. There is no harm in declining it.|
S~Kind of them. We can thank them without needing the rest right now.|
F~That is a sweet explanation for fussing over a stranger.|
S~A small family habit has made the ship kinder to someone new.|
S~A passing resemblance has opened the door to a very sincere welcome.|
S~A familiar absence can make a stranger unexpectedly easy to care about.|
N~Offer declined, reason explained, no pressure added. Good interaction.|
S~A remembered face has left a little warmth in this room.|
S~They make the explanation personal without demanding anything back.|
S~I wonder when they last saw the sibling they are thinking of.
''')
add('ship_thomas','SSAnne_1F_Room7_Text_ThomasPostBattle',
    'Thomas says we should be kind to friends.','''
S~A good rule, though losing a battle is not always a failure of friendship.|
N~Kindness matters. It should be distinguished from avoiding every competitive loss.|
N~Agreed. A fair match still needs decent treatment afterward.|
S~A friendship should have room for both trying your best and caring how it felt.|
S~A little care after a difficult game can keep the game worth sharing.|
N~A sound moral with a somewhat broad application to the scoreboard.|
S~Being kind is usually quieter than winning the argument about kindness.|
N~Cooperation and competition can share a room if the boundaries are clear.|
S~A friend should still feel like a friend when the result goes wrong.|
N~A good reminder, provided it works in both directions.|
S~I wonder what kindness looks like to him after a match.
''')
add('ship_luxury_parties','SSAnne_2F_Corridor_Text_ThisShipIsLuxuryLiner',
    'A crew member describes the liner\'s international trainer parties at its ports.','''
S~A moving party venue with an ocean-sized hallway between stops.|
S~Regular port events bring together travelers from different training communities.|
N~Sounds lively. Hope there is still somewhere quiet for the teams.|
S~It must be exciting to hear new voices at every stop.|
S~The kitchen must have a very ambitious schedule.|
S~A traveling company gathers a new audience each time the setting changes.|
S~A room of strangers that keeps being rebuilt by the next shore.|
N~Repeated events, changing guest lists. Serious logistical work.|
S~The ship carries a little invitation from one piece of land to the next.|
S~A gathering can feel special when it includes people who rarely share a place.|
S~I wonder which port gives the crew their favorite welcome.
''')
add('ship_rival','SSAnne_2F_Corridor_Text_RivalPostBattle',
    'The rival mentions the seasick Cut master and recommends visiting him.','''
N~A useful lead could have traveled without the insult to the poor seasick man.|
N~The practical information is clear: someone aboard can help with Cut. His illness is separate.|
N~We can check on the captain without making fun of him.|
N~It is unkind to turn someone feeling awful into a punchline.|
N~A little help for the sick person should come before asking what he can teach us.|
N~The rival hands us a useful address wrapped in an entirely unnecessary review of the resident.|
N~A capable person is still capable when the sea briefly defeats their stomach.|
N~Function and current condition are distinct. Useful lead, poor presentation.|
N~A rough crossing does not erase the things someone's hands have learned.|
N~He could have passed on the information with a little more grace.|
N~I wonder whether anyone has actually helped the captain feel better.
''')
add('ship_sleeping_discovery','SSAnne_2F_Room1_Text_SleepingMonLookedLikeThis',
    'A well-traveled passenger excitedly shows the unusually sleeping Pokemon they saw.','''
S~A lifetime of travel, and a nap still managed to surprise them. Excellent Pokemon.|
S~An unusual observed behavior can remain memorable even to an experienced traveler.|
N~Good to keep noticing things instead of deciding you have seen everything.|
S~I like that much experience has not used up their surprise.|
S~An ordinary-looking rest can be a very extraordinary thing to someone new.|
S~The worldly traveler has discovered a spectacularly uneventful new act: sleeping.|
S~A large stillness can apparently leave quite an impression.|
S~Behavioral observation worth recording. The illustration helps.|
S~The world still has something unfamiliar curled up inside it.|
S~A good traveler remembers what stood out, not just where they went.|
S~I wonder how long they watched before deciding the nap was remarkable.
''')
add('ship_brooks','SSAnne_2F_Room2_Text_BrooksPostBattle',
    'Brooks insists he would have beaten us fifteen years ago.','''
M~A formidable opponent, safely located fifteen years away from this match.|
N~A hypothetical past performance cannot change the observed current result.|
N~Maybe. The battle we actually had is the one we can learn from.|
N~It can be hard when a familiar skill no longer feels the same.|
N~Past pride does not have to become present disappointment with the whole self.|
M~The critic submits a glowing review of an unavailable earlier edition.|
N~The past makes a very cooperative place to store an undefeated self.|
N~Historical benchmark cannot be rerun. Work with the present configuration.|
N~An old path is not less real because the feet walk differently now.|
N~He can remember being capable without dismissing what the team did today.|
N~I wonder what his favorite battle from those years was.
''')
add('ship_dale','SSAnne_2F_Room2_Text_DalePostBattle',
    'Dale says the ship\'s party is probably already over.','''
N~We may have arrived just in time for the traditional leftover conversation.|
N~He believes the event has ended. We should not assume the current schedule from the invitation alone.|
N~Then enjoy the rest of the ship. No point racing a finished party.|
N~It is a little sad to realize an event has already happened without you.|
M~There may still be something good in the kitchen, though I would ask politely.|
N~The promised social scene has left only its final echo in the corridor.|
N~A room can feel very different after the last excited voice leaves it.|
N~Event window apparently closed. Choose the next available activity.|
N~The ship has begun folding away one part of the day.|
N~A finished party still leaves the people and their stories aboard.|
N~I wonder what the crew most enjoys once the formal event is done.
''')
add('ship_water_transport','SSAnne_2F_Room3_Text_SeenMonsFerryPeople',
    'A traveler recalls Pokemon carrying people across water.','''
S~A living ferry with the option to have a personal opinion about the route.|
S~Some Pokemon have the size and swimming ability to support human travel.|
N~A strong swimmer still needs a sensible load and safe conditions.|
S~Sharing the water with a trusted partner sounds peaceful.|
N~A comfortable crossing should be comfortable for the Pokemon too.|
S~The sea supplies a road, the companion supplies a rather more personal vessel.|
S~A journey that depends on knowing the creature beneath you.|
S~Buoyancy and load-bearing capability, plus an actual partnership. Interesting combination.|
S~A warm back can make the water feel less like a boundary.|
N~Travel looks different when the transport needs care as well as a destination.|
S~I wonder which Pokemon the traveler saw carrying someone.
''')
add('ship_cut_commitment','SSAnne_2F_Room3_Text_SomeTreesCanBeCutDown',
    'The passenger explains Cut\'s use and warns that an HM move is hard to forget.','''
N~A tree-clearing lesson with a long-term place in the lesson book. Choose thoughtfully.|
N~The field utility and the removal restriction are both important parts of the choice.|
N~Know who will learn it before committing. Useful advice.|
N~I appreciate hearing the difficult part before the decision.|
N~A useful move deserves a place that fits the partner's wider needs.|
N~The convenient new skill comes with a surprisingly persistent contract.|
N~A small cleared path can leave a lasting mark on the one who clears it.|
N~Hard-to-reverse configuration change. Plan the slot first.|
N~A way through the trees may take root in the partner's own habits.|
N~Clear guidance includes the condition people might otherwise miss.|
N~I wonder how the passenger learned that caution.
''')
add('ship_lamar','SSAnne_2F_Room4_Text_LamarPostBattle',
    'Lamar says he prefers Pokemon that are both strong and rare.','''
N~A very exclusive preference. I hope ordinary kindness still gets through the door.|
N~Rarity and battle capability are distinct attributes, neither a substitute for good care.|
N~His choice. Common partners can still be worth trusting.|
N~I hope he sees the individual once the rare first impression wears off.|
N~Every partner needs care on the days it is not impressive.|
N~A carefully curated cast, selected for both performance and limited availability.|
N~A creature is not made less interesting because someone else has met one.|
N~Scarcity is not a direct measure of capability. Worth separating the requirements.|
N~A small common life can still have an uncommon place beside someone.|
N~Taste is personal. Treating it as a ranking of worth gets ugly quickly.|
N~I wonder which partner he values for reasons that do not fit those two words.
''')
add('ship_dawn','SSAnne_2F_Room4_Text_DawnPostBattle',
    'Dawn admires and envies our strong Pokemon.','''
S~The team has collected an admirer. A well-earned compliment after the work.|
S~Visible strength reflects care and training as well as individual capabilities.|
N~They put in the effort. Glad someone noticed.|
F~It is lovely to hear the partners praised so warmly.|
S~A good bond takes more than simply wishing for the strongest arrival.|
S~An enthusiastic review of the cast, with a little longing in the final line.|
S~A creature doing well can make the care behind it briefly visible.|
N~Positive result worth tracing back to the preparation, not just the appearance.|
S~The partners carry a little of the road that taught them.|
S~Admiration is nicer when it remembers they are companions, not accessories.|
S~I wonder which partner's performance caught her attention first.
''')
add('ship_safari_parent','SSAnne_2F_Room5_Text_HaveYouGoneToSafariZone',
    'A passenger recommends Fuchsia\'s Safari Zone for its rare Pokemon.','''
S~A ship carries travel tips as efficiently as it carries luggage.|
S~A reserve with varied habitats is a useful destination for species observation.|
N~Worth hearing. Prepare before paying for the visit.|
S~A place that left them excited enough to tell strangers sounds interesting.|
N~A good outing needs time, supplies, and room to enjoy it calmly.|
S~The passenger's review points toward a rather lively shore excursion.|
S~Some places remain pleasantly crowded in the mind after you leave.|
S~Varied species in a concentrated area. Good field-study opportunity.|
S~A distant patch of land has followed the traveler aboard as a story.|
S~A personal recommendation feels different from a poster at the dock.|
S~I wonder which encounter made them recommend it so readily.
''')
add('ship_safari_child','SSAnne_2F_Room5_Text_WeThinkSafariZoneIsAwesome',
    'The child remembers a happy Safari Zone visit with their father and wants to return.','''
S~The best review is sometimes simply wanting to go back with the same person.|
S~A shared positive experience has become a clear family memory.|
S~Good to hear the day was enjoyable for both of them.|
S~I like that the favorite part includes their dad being there.|
S~A good outing can keep making a family happy long afterward.|
S~A young critic awards the excursion an enthusiastic request for a sequel.|
S~A little remembered afternoon has become somewhere to wish toward.|
S~High repeat-visit interest. Strong user satisfaction report.|
S~A place and a familiar hand have become one warm memory.|
S~The enthusiasm is entirely convincing without any fancy description.|
S~I wonder which part of the day they retell to their dad most often.
''')
add('ship_captain_ill_report','SSAnne_2F_Room6_Text_CaptainIsAwfullySick',
    'A passenger reports that the captain looks pale and feels very ill.','''
N~Being in charge of a ship does not give the stomach command of the sea.|
N~His condition deserves care regardless of his experience or role.|
N~Someone should check on him rather than just passing the news around.|
N~It sounds miserable to feel that unwell somewhere you are expected to lead.|
N~A little practical help would be kinder than another story about the pallor.|
N~The captain's authority has encountered an uncooperative bodily department.|
N~A capable person can still need somebody to bring a little comfort.|
N~Human maintenance issue, not a failure of command. Get appropriate help.|
N~The sea has found a place where rank means very little.|
N~I hope the staff are giving him privacy as well as help.|
N~I wonder whether he has been able to rest at all.
''')
add('ship_seasick_common','SSAnne_2F_Room6_Text_ManyPeopleGetSeasick',
    'A passenger remarks that seasickness affects many people.','''
N~The sea is very generous with that particular unwanted souvenir.|
N~Motion sickness is a familiar travel response, not a measure of courage or experience.|
N~No shame in feeling ill. Find a safe place to recover.|
N~It is reassuring to know the problem is not just you.|
N~People deserve a little patience when the trip stops feeling pleasant.|
N~An extremely successful voyage activity that nobody purchased a ticket to enjoy.|
N~The body sometimes reviews travel less favorably than the itinerary does.|
N~Movement input and human response can be poorly matched. Not a moral issue.|
N~A moving floor can make even familiar balance feel far away.|
N~A kind reminder when someone is embarrassed about feeling unwell.|
N~I wonder what advice the experienced crew gives first-time passengers.
''')
add('ship_captain_reputation','SSAnne_3F_Corridor_Text_CaptainTeachesCutToMons',
    'A crew member praises the captain\'s swordsmanship and ability to teach Cut.','''
S~A captain with a very precise second skill. The crew sounds proud of him.|
S~A practiced human technique being taught to Pokemon is an interesting form of instruction.|
N~Useful skill. Hope he teaches it with the same care it takes to use.|
S~It is nice to hear the crew admire something their captain works at.|
S~A good teacher leaves someone else able to do the useful thing too.|
S~The captain's legend includes an unexpectedly educational flourish.|
S~A sharp tool becomes less frightening when the hand behind it is patient.|
S~Transferable technique across different bodies. I would like to see the teaching method.|
S~A practiced motion finding another pair of hands, or paws.|
S~Expertise is more impressive when somebody can explain it kindly.|
S~I wonder how the captain first began teaching Pokemon.
''')
add('ship_phillip','SSAnne_B1F_Room1_Text_PhillipPostBattle',
    'Phillip describes jellyfish Pokemon drifting past the ship at sea.','''
S~A slow little parade beside a very large boat. Lovely sight.|
S~A ship provides repeated opportunities to observe marine species in open water.|
N~Fine to watch. Give them room if we go into the water.|
S~It sounds peaceful to see them go by without needing to do anything.|
S~An ordinary workday can still offer a good little view.|
S~The voyage includes a drifting supporting cast unconcerned with the passenger schedule.|
S~Small pale shapes making the great water feel inhabited.|
S~Passive observation from a stable platform. Good way to notice patterns.|
S~The sea sends little translucent thoughts past the hull.|
S~A detail worth noticing between all the grand ports and formal parties.|
S~I wonder whether the crew recognizes a change in the water by what drifts past.
''')
add('ship_barny','SSAnne_B1F_Room1_Text_BarnyPostBattle',
    'Barny says he had planned to make us his assistant.','''
M~An employment offer we narrowly escaped before reading the duties.|
N~He had a role in mind for us without first establishing our interest.|
N~Ask before recruiting someone. We already have plans.|
F~That is a surprising amount of expectation from one short meeting.|
N~A favor is easier to agree to when somebody actually explains it first.|
M~A casting decision announced after the prospective performer has already declined by winning.|
N~A stranger's plan for your day is remarkably easy to acquire.|
N~Unrequested assignment. Requirements and consent both missing.|
N~His imagined road has tried to borrow our feet.|
N~He seems certain he was offering an honor. A little discussion would help.|
N~I wonder what he thought the assistant would be doing.
''')
add('ship_huey','SSAnne_B1F_Room2_Text_HueyPostBattle',
    'Huey says the sailors caught all their Pokemon while at sea.','''
S~The team is a living collection of places the ship has passed.|
S~The crew's encounters reflect sustained access to marine habitats.|
N~Hope the catches became well-cared-for partners, not just onboard trophies.|
S~It must be strange to remember a meeting by the stretch of ocean around it.|
S~A crew and its Pokemon probably learn a lot of shared routines aboard.|
S~The ship's route has supplied the entire supporting cast.|
S~A horizon can keep returning as a familiar companion beside you.|
S~Consistent sampling environment explains the team composition.|
S~The sea has sent a few of its lives traveling above it.|
S~A team can tell you something about the life its trainer actually leads.|
S~I wonder which one has been with the crew longest.
''')
add('ship_dylan','SSAnne_B1F_Room3_Text_DylanPostBattle',
    'Dylan recommends a fishing rod for Pokemon living in deep water.','''
N~A long line is a much better plan than trying to reach down very confidently.|
N~A rod provides access to encounters unavailable from an ordinary shoreline search.|
N~Bring the right tool. Do not lean over the rail chasing a glimpse.|
N~There is something strange about so much life hidden beneath an empty-looking surface.|
N~A sensible tool makes the attempt safer and less tiring.|
N~The deep-water cast requires a more specialized invitation.|
N~A line reaches where looking harder cannot.|
N~Tool extends the accessible environment. Basic but useful.|
N~A little thread asks a question too deep for the eye.|
N~Practical advice from somebody who spends time around the water.|
N~I wonder which deep-water catch he most enjoys finding.
''')
add('ship_leonard','SSAnne_B1F_Room4_Text_LeonardPostBattle',
    'Leonard cheerfully asks whether we want to become a sailor.','''
S~An inviting laugh, followed by an entire career possibility. Busy conversation.|
N~A warm invitation is pleasant; the work itself would deserve a fuller explanation.|
N~Could be good work. Learn what the ordinary days involve before signing on.|
F~It is nice to be asked, though I would have so many questions.|
S~A life with shared meals and changing shores has its appeal.|
M~The unofficial recruitment office operates through laughter and a remarkably broad opening question.|
S~A road made of water is still a road someone can choose.|
N~Interesting possibility. Need a role description, training plan, and equipment list.|
S~A familiar port can become the beginning rather than the end of the day.|
S~He makes the life sound welcoming without a polished pitch.|
S~I wonder what made him decide to go to sea.
''')
add('ship_duncan','SSAnne_B1F_Room4_Text_DuncanPostBattle',
    'Duncan asks if we visited Vermilion\'s Fishing Guru.','''
S~The local fishing network apparently extends all the way below deck.|
S~A local expert is a useful connection for someone beginning to fish.|
N~Worth visiting if we need advice or a rod.|
S~It is nice when a familiar name turns up in an unexpected place.|
S~A recommendation from a sailor carries a little practical weight.|
S~The waterfront community supplies a recurring supporting character.|
S~A hobby can tie a surprising number of rooms together.|
N~Relevant specialist referral. Sensible.|
S~A name from the shore has followed us across the gangway.|
S~He sounds as if nearly every visitor should make the introduction.|
S~I wonder whether the sailors compare catches with the Guru when they are in port.
''')
add('ship_machoke','SSAnne_B1F_Room5_Text_MachokeHasStrengthToMoveRocks',
    'The sailor proudly describes Machoke\'s ability to move heavy rocks.','''
S~A powerful buddy, introduced with a very large amount of pride.|
N~Strength can serve practical work as well as battling. Appropriate loads still matter.|
N~Strong partner. Give Machoke rest between the heavy jobs.|
S~I like that he says buddy before describing what Machoke can do.|
N~A helpful partner deserves appreciation even when no heavy lifting is needed.|
S~The sailor's trusted companion receives an impressively concrete testimonial.|
S~A familiar pair of hands making an impossible-looking task ordinary.|
N~High load capability. Good technique still belongs in the plan.|
S~A great deal of force can still belong to a gentle companion.|
S~He sounds fond, rather than merely pleased to have strong help.|
S~I wonder what Machoke likes doing when the work is finished.
''')
add('ship_cut_given','SSAnne_CaptainsOffice_Text_ExplainCut',
    'After his recovery and HM01 gift, the captain explains clearing small trees with Cut.','''
S~A little help for his bad afternoon became a way through our next obstacle.|
S~The final explanation follows the successful HM handoff and identifies its field use.|
S~Useful gift. Good that he feels better too.|
S~It is nice when a small kind act ends with both people helped.|
S~He turned his gratitude into something genuinely useful on the road.|
S~The seasick master's scene ends with a practical lesson rather than a demonstration.|
S~A little care has opened a path, quite literally.|
S~Capability acquired with a clear first test location. Good instruction.|
S~A difficult crossing has left a new way through the trees.|
S~He made the gift easy to understand, even while still recovering.|
S~I wonder how many travelers remember the captain when they use that move.
''')
add('ship_captain_farewell','SSAnne_CaptainsOffice_Text_SSAnneWillSetSailSoon',
    'Now feeling better, the captain says the S.S. Anne will leave soon and bids farewell.','''
S~His stomach has finally authorized the sailing schedule. Good news for the whole ship.|
S~His improved condition allows the voyage to continue. The farewell is explicit.|
N~Good to hear he is well. We should be ready to disembark.|
S~A kind goodbye makes the ship feel a little less temporary.|
S~I hope the next stretch of sea treats him more gently.|
S~The captain returns to his proper role and closes the visit with a formal farewell.|
S~A borrowed room, a short acquaintance, and a door about to become a gangway again.|
N~Departure approaching. Finish essential business before leaving the ship.|
S~A little floating world is preparing to carry its own road away.|
S~He remembers to leave the goodbye warm after a miserable day.|
S~I wonder what port he is most looking forward to next.
''')
add('ship_captain_full','SSAnne_CaptainsOffice_Text_YouHaveNoRoomForThis',
    'The captain cannot give HM01 because our bag is full.','''
N~A kindness returned has met the one thing aboard less flexible than our bag: nothing.|
N~The HM transfer did not complete. No successful gift should be inferred.|
N~Make room first. Let the captain recover while we sort it.|
F~I wish we had been ready to accept his thanks.|
N~A little preparation will make the next handoff easier.|
N~The grateful captain's generous flourish has collided with luggage capacity.|
N~A tiny disc, an entirely full pocket, an unnecessarily awkward ending.|
N~Capacity issue. Clear space rather than repeating the failed handoff.|
N~A little place needs to open before the gift can open a larger one.|
N~No need to rush him through another explanation while he still feels ill.|
N~I wonder what in the bag has outlived its usefulness.
''')
add('ship_departure_deck','SSAnne_Deck_Text_ShipDepartingSoon',
    'A crew member says the party has ended and the ship will depart soon.','''
N~The party is folding up, and the whole building is about to leave. Strong closing signal.|
N~The available visit window is ending. It is sensible to review unfinished business.|
N~Keep the team together. We do not want anyone left behind.|
N~There is a particular little sadness when a place prepares to carry on without you.|
N~We should make our last stops without making the crew chase us.|
S~The temporary venue is about to take its entire stage elsewhere.|
S~A familiar room can be gone from shore by evening. Ships are strange.|
N~Departure window near. Check the group and belongings before disembarking.|
S~The small world beside the dock is remembering it belongs to the sea.|
N~A clear notice is kinder than a surprise gangway closing.|
S~I wonder what the deck looks like once the guests have all gone ashore.
''')
add('ship_scrubbing','SSAnne_Deck_Text_ScrubbingDecksHardWork',
    'A sailor is tired from scrubbing the deck.','''
N~That shining deck did not become shiny by admiring the sea. Somebody worked.|
N~The comfort of passengers depends on sustained physical maintenance.|
N~Hard work. Give the sailor room to finish safely.|
S~It makes you notice the ordinary care behind such a polished ship.|
N~I hope the crew gets a proper rest after the guests stop tracking things in.|
N~The elegant setting briefly reveals the labor behind its impeccable appearance.|
N~A bright surface can hide a great deal of someone else's tiredness.|
N~Maintenance is real work, especially on a surface everyone keeps using.|
N~The ship's ordinary shine has a pair of aching arms behind it.|
N~Clean floors are part of good design, and cleaning them should not be invisible.|
N~I wonder how long one full pass of the deck takes.
''')
add('ship_deck_ill','SSAnne_Deck_Text_FeelSeasick',
    'An ill passenger comes on deck for air.','''
N~A little breeze is much better company than another clever comment right now.|
N~They have moved to a place that may feel more tolerable. Give them room.|
N~Make sure they stay somewhere steady and safe while they feel ill.|
N~That sounds miserable. I would keep the conversation short.|
N~A quiet moment and someone checking they are steady would be kind.|
N~The luxurious voyage has briefly narrowed to the question of not feeling awful.|
N~The sea can be beautiful and terrible company for a stomach.|
N~Reduce demands. A moving deck still needs careful footing.|
N~The body has asked for a little more sky around it.|
N~No teasing. Feeling unwell in public is difficult enough.|
N~I wonder whether a crew member nearby knows they need help.
''')
add('ship_edmond','SSAnne_Deck_Text_EdmondPostBattle',
    'Edmond wonders how many Pokemon species exist in the world.','''
U~Every new shore seems capable of adding another name. That is an excellent kind of big question.|
S~The total depends on observation and classification that may still be incomplete.|
N~Enough to keep us learning. No reason to rush past the ones beside us.|
S~I like a question that makes the horizon feel full instead of empty.|
S~A wide world means there is always another good reason to stay curious.|
S~The cast list appears larger than any one traveler's program.|
S~A number that keeps a little space around the unknown.|
S~An open research question! Complete observations are harder than confident estimates.|
S~The world may know more names for itself than we have learned to hear.|
S~A better question than deciding the familiar ones are all there is.|
S~I wonder which new meeting most changed his estimate.
''')
add('ship_trevor','SSAnne_Deck_Text_TrevorPostBattle',
    'Trevor doubts his father\'s claim that only one hundred Pokemon kinds exist.','''
S~A child has looked at the horizon and suspected the list needs more pages.|
S~Questioning a fixed total in light of broader experience is reasonable.|
N~Worth checking. Even a parent can have an outdated answer.|
S~It is nice that he can respect his father and still be curious beyond the answer.|
S~Learning together could make a good next conversation between them.|
S~The inherited encyclopedia has received a polite request for a revised edition.|
S~The world often turns out to be larger than the first number someone gave us.|
S~A claim ready for verification. Good instinct.|
S~A small doubt can make the map grow in a useful direction.|
S~He is making room for what he has not seen yet. Lovely habit.|
S~I wonder which Pokemon first made him think the count was too small.
''')
add('kitchen_busy','SSAnne_Kitchen_Text_BusyOutOfTheWay',
    'A busy cook asks us to get out of the working kitchen.','''
N~The galley is not a spectator sport while people are carrying hot things. Time to move.|
N~An active workspace needs clear routes for staff and equipment.|
N~Out of the way. Hot food and a moving ship are enough trouble already.|
N~I would rather not become one more thing someone has to step around.|
N~Fair request. A busy kitchen needs its floor more than its visitors need a look.|
N~The accidental audience has been removed from a performance involving knives and heat.|
N~A room can be interesting and still be a poor place to stand.|
N~Keep the access path clear. Functional space outranks curiosity here.|
N~The room is moving with work; we should not be its stubborn still point.|
N~A sharp tone is understandable when the floor is crowded and the trays are hot.|
N~I wonder how much room the crew has when every station is busy.
''')
add('kitchen_berry','SSAnne_Kitchen_Text_SawOddBerryInTrash',
    'A cook wonders about an odd Berry seen in the rubbish.','''
N~An interesting find, though rubbish is not my preferred tasting menu.|
N~Identification should precede handling or use, especially with discarded food.|
N~Look carefully. Do not eat an unknown thing from a bin.|
N~A small mystery can still catch someone's attention in the middle of work.|
N~It could be worth identifying, but it stays away from the food preparation.|
N~The culinary setting has produced an unexpected little mystery in its least glamorous corner.|
N~A bright little thing in a place people stop looking.|
N~Unknown material. Identify it without contaminating the work area.|
N~Something discarded has kept a little of its strangeness.|
N~An odd color can be interesting without being an invitation to touch.|
N~I wonder whether anyone in the kitchen recognizes it.
''')
add('kitchen_dizzy','SSAnne_Kitchen_Text_SoBusyImDizzy',
    'An overwhelmed cook asks us to clear space.','''
N~Too much work, not enough floor. We can solve the part currently shaped like us.|
N~The worker is overloaded and explicitly needs a clear area.|
N~Move aside. They need room and a break, not another question.|
N~They sound stretched thin. I would not want to add to it.|
N~A hot busy kitchen is no place to push through dizziness. I hope someone helps them.|
N~The production is running too fast for the person expected to keep pace.|
N~A small request for room can contain a large amount of exhaustion.|
N~Overload warning received. Reduce obstruction immediately.|
N~The room has more movement than one pair of hands can follow.|
N~They should not have to apologize for needing space to work safely.|
N~I wonder whether the crew has someone free to take over for a moment.
''')
add('kitchen_potatoes','SSAnne_Kitchen_Text_PeelSpudsEveryDay',
    'A cook sings through the routine of peeling potatoes daily.','''
S~A potato song! The vegetables have acquired a very reliable touring musician.|
S~A familiar rhythm can help a repetitive task feel more manageable.|
N~Steady work. Hope they get to do something different now and then.|
S~A little song can make a repetitive job feel less solitary.|
S~Potatoes carry a kitchen a long way. Somebody has to do the quiet preparation.|
S~The galley's longest-running production appears to be a solo with potatoes.|
S~An ordinary task keeping time with a private little tune.|
N~Repetitive work, reliable process. Comfortable tools matter here.|
S~Small skins falling away while the day keeps its familiar rhythm.|
S~They found a little personality inside the uniform routine.|
S~I wonder whether the song changes with the menu.
''')
add('kitchen_snorlax','SSAnne_Kitchen_Text_HearAboutSnorlaxItsAGlutton',
    'A cook describes Snorlax\'s enormous appetite and sleep.','''
U~A Pokemon that treats eating and sleeping like competitive events. Formidable schedule.|
N~A large appetite implies substantial care and supply requirements.|
N~Anyone raising one should plan the meals before the first empty cupboard.|
S~It sounds like a creature very sure about which parts of the day it values.|
U~That is a partner you budget for with a separate shopping list.|
M~A lifestyle enthusiast whose principal disciplines are lunch and recovery.|
S~An impressive commitment to two of life's quieter pleasures.|
N~High resource demand. Better calculate food needs before committing.|
S~A large quiet body with a very busy appetite.|
N~A distinctive routine, though a partner is more than the joke people make about it.|
S~I wonder whether the cook has ever had to prepare a meal for one.
''')
add('kitchen_onions','SSAnne_Kitchen_Text_OnlyGetToPeelOnions',
    'An unhappy cook is stuck peeling onions and sniffling.','''
N~The onions have successfully made the assignment personal. Poor cook.|
N~The irritation and repetitive task make the complaint quite understandable.|
N~Hope they rotate the job. Nobody needs that station forever.|
N~It is hard to tell how much is the onions and how much is the unhappy task.|
N~A sharp knife, good ventilation, and a turn away from that station would help.|
N~The galley has assigned a daily tragedy with a predictably tearful audience of one.|
N~A very ordinary vegetable doing unreasonably effective emotional staging.|
N~Poor work rotation creates avoidable discomfort. Fix the process.|
N~A small bitter cloud keeps rising from the day's work.|
N~Someone deserves a chance at a different task, not a joke about the tears.|
N~I wonder whether another cook can take a turn at that pile.
''')
add('chef_salmon','SSAnne_Kitchen_Text_SalmonDuSalad',
    'The chef announces a salmon dish and worries guests will complain about more fish.','''
M~A sea voyage with fish again. The ocean has a very persistent suggestion box.|
N~Availability and menu variety can pull the kitchen in different directions.|
N~A good meal is worth more than a new name every night.|
N~It is difficult when you care about the work and already expect a complaint.|
S~Different preparation can give a familiar ingredient a fresh day. I would try the salad.|
M~The chef presents a perfectly sensible dish to an audience already rehearsing its objections.|
N~A lovely meal can still lose an argument with somebody's idea of novelty.|
N~Supply constraints versus customer preference. A classic design problem.|
S~The sea has followed the passengers into the dining room again.|
N~Presentation matters, but so does the fact that somebody made a proper meal.|
S~I wonder which dish the regular guests actually look forward to.
''')
add('chef_eels','SSAnne_Kitchen_Text_EelsAuBarbecue',
    'The chef serves barbecued eel and jokingly fears a passenger mutiny.','''
M~A barbecue with extremely dramatic anticipated customer feedback.|
N~The chef appears worried about reception rather than the dish's preparation.|
N~They can dislike a meal without declaring war on the kitchen.|
F~I hope the guests are kinder than the chef expects.|
S~Eel can be lovely with a good glaze. I would let the dish speak before planning the mutiny.|
M~The menu announces dinner and prepares for a naval uprising in the same breath.|
M~A surprisingly high-stakes relationship between a plate and an opinion.|
N~Negative feedback is possible. Structural rebellion seems an ambitious forecast.|
N~The cook has imagined sharp voices rising before the smoke has cleared.|
N~A little openness from the diners would make the room much nicer.|
S~I wonder whether the chef has served it here before.
''')
add('chef_beef','SSAnne_Kitchen_Text_PrimeBeefsteak',
    'The chef announces beefsteak but worries about having enough portions.','''
N~A grand main course with a small counting problem behind the curtain.|
N~The supply concern is concrete. Serving estimates should be checked before the rush.|
N~Count the portions now. Better than finding out at the last table.|
N~It is stressful when a beautiful plan depends on one missing number.|
N~Plan the portions and a second dish early. Hungry guests are easier to manage before they wait.|
N~The impressive entrance has reached the logistical question of whether every actor gets a plate.|
N~Luxury becomes arithmetic very quickly in a kitchen.|
N~Inventory check before service. This is exactly why the numbers matter.|
N~A feast still begins with counting the people who need to eat.|
N~The generous appearance needs a practical plan underneath it.|
N~I wonder how the kitchen handles a sudden change in the guest count.
''')
add('diglett_tunnel','DiglettsCave_SouthEntrance_Text_DiglettDugThisTunnel',
    'A surprised traveler says Diglett excavated the long tunnel toward Viridian.','''
U~Tiny diggers, enormous hallway. Never judge an engineer by how far it sticks out of the floor.|
S~Small repeated actions can produce a substantial structure over time.|
N~Impressive work. We are visitors in somebody else's tunnel.|
S~It is lovely to imagine all that quiet work beneath the ordinary road.|
N~A useful route deserves care from the people passing through it.|
S~The smallest excavation crew has delivered a surprisingly large public work.|
S~A hidden little life has made a way through the world.|
U~An animal-built transit route! I would love to understand how they coordinate it.|
S~Small hands in the dark have joined two distant pieces of daylight.|
S~Useful and unassuming. A strong combination.|
S~I wonder how travelers first realized where the tunnel came out.
''')
add('safari_sara','SafariZone_Center_Text_WhereDidErikGo',
    'Sara wonders where her boyfriend Erik went inside the Safari Zone.','''
N~A reserve with several zones is an ambitious place to lose your walking partner.|
N~A shared meeting point would be more reliable than both people searching at random.|
N~Stay somewhere he can find her. Two wandering searches make this harder.|
N~It is unsettling when the familiar person is suddenly not beside you.|
N~A little rest here might be better than rushing into another zone.|
N~The romantic outing has encountered a practical flaw in its cast management.|
N~A large pleasant place can become less pleasant when someone is missing from it.|
N~Rendezvous location needed. Pick a fixed point.|
N~One familiar voice has become difficult to find among all the leaves.|
N~I hope they agreed where to meet before separating.|
N~I wonder which zone they last visited together.
''')
add('safari_gift_catches','SafariZone_Center_Text_CatchingMonsAsGifts',
    'A visitor is catching Pokemon to give as presents.','''
N~A living present needs a prepared home, not just a pleased expression at the wrapping.|
N~The recipient's willingness and ability to provide care should be established in advance.|
N~Make sure the people receiving them actually want the responsibility.|
N~A surprise can be lovely, but a companion should not arrive somewhere unready.|
N~The best gift includes time, supplies, and a home that has said yes.|
N~A charming proposed entrance needs considerably more planning than a ribbon.|
N~A life should not be handed over simply because the moment would look sweet.|
N~Check the receiving environment before transferring the living system.|
N~A small heartbeat needs a welcome longer than one surprised afternoon.|
N~A good intention should make room for what the recipient and Pokemon need.|
N~I wonder whether these are requested partners or unexpected gifts.
''')
add('safari_tired_effort','SafariZone_East_Text_HowManyDidYouCatch',
    'A tired visitor asks about our catches after a demanding safari.','''
N~The catching report has arrived with a request from the legs to sit down.|
N~They are comparing outcomes after a high-effort outing. Recovery still matters.|
N~Rest first. The catch count can wait a minute.|
S~It is nice to compare the little stories instead of just walking past each other.|
N~A bench is part of a good outing, not evidence the outing went wrong.|
N~The field expedition submits its preliminary report from a position of exhaustion.|
N~A little shared tiredness can be its own introduction.|
N~High activity load detected. Good reason to use the rest house.|
N~The day has put more miles into the feet than the map seemed to promise.|
N~A break may make the stories easier to enjoy telling.|
S~I wonder which encounter took the most patience.
''')
add('safari_chansey','SafariZone_East_Text_CaughtChanseyAllWorthwhile',
    'A delighted visitor says catching Chansey made the outing worthwhile.','''
S~One meeting has given the whole day a very happy ending.|
S~A desired encounter can make sustained effort feel rewarding.|
N~Good catch. Now comes getting to know the partner.|
S~Their excitement is lovely. I hope Chansey finds a kind home.|
S~A happy new arrival still needs a gentle first evening.|
S~The long search has finally introduced its much-anticipated central character.|
S~A little round life has become a very large bright spot in the day.|
S~Goal reached. Now transition from acquisition to care.|
S~The familiar world has made room for one more warm presence.|
S~It is nice to hear delight without a complaint about what came before it.|
S~I wonder how long they had hoped to meet a Chansey.
''')
add('safari_fun_tired','SafariZone_East_Text_TiredFromAllTheFun',
    'A visitor is pleasantly exhausted from enjoying the Safari Zone.','''
S~The good kind of tired has still ordered a bench. Sensible.|
S~Enjoyment and physical fatigue can coexist quite comfortably.|
N~Take the rest. Good fun still uses energy.|
S~I like hearing someone say the day was worth the tired feet.|
S~A quiet sit makes a pleasant outing last a little more gently.|
S~A glowing review delivered at the end of the reviewer's remaining stamina.|
S~A day can be full without needing one more thing added to it.|
N~Positive user experience, low remaining battery. Time to recharge.|
S~The day has filled their pockets with memories and their legs with distance.|
S~A cheerful break is part of enjoying yourself properly.|
S~I wonder which part of the visit made them laugh most.
''')
add('safari_item_limits','SafariZone_East_Text_KeepAnyItemFoundOnSafari',
    'A visitor explains that found items may be kept but collecting everything would use the time limit.','''
N~The ground has gifts, but the clock refuses to carry all of them for us.|
N~The limited visit creates a tradeoff between searching every location and other goals.|
N~Choose what matters. No need to chase every glint in the grass.|
N~It is reassuring to know the visit does not have to become a perfect checklist.|
N~A few useful finds and a pleasant day are enough.|
N~The expedition is invited to choose an ending before the inventory becomes the entire plot.|
N~Not finding everything leaves a perfectly respectable amount of afternoon.|
N~Finite resources, competing objectives. Prioritize before wandering.|
N~A pocket can be filled while the day quietly slips past it.|
N~A useful reminder that more collected does not always mean more enjoyed.|
N~I wonder which things visitors most regret spending all their time searching for.
''')
add('safari_deep_prize','SafariZone_East_Text_PrizeInDeepestPartOfSafariZone',
    'A visitor recommends reaching the deepest section for a prize.','''
S~A little motivation at the far end of a great deal of walking.|
N~A destination goal should be balanced against the remaining visit allowance.|
N~Check the route and time before chasing it.|
S~A place at the edge of the map can make exploring feel purposeful.|
N~We can aim for it without turning the outing into a panicked sprint.|
S~The furthest setting promises a practical closing reward.|
S~A secret waiting far enough away to make the road part of its charm.|
N~Clear destination. Now establish the shortest sensible path.|
S~The reserve has left a little invitation in its quietest corner.|
N~A tempting recommendation, especially from someone who sounds certain.|
S~I wonder whether they have already found it themselves.
''')
add('safari_eevee_comparison','SafariZone_East_Text_MyEeveeEvolvedIntoFlareon',
    'A visitor wonders why their Eevee became Flareon while a friend\'s became Vaporeon.','''
S~Same little beginning, very different endings to the story about the next stage.|
N~Different evolutionary conditions can produce different outcomes in Eevee.|
N~Compare what happened before the change. That is where the clue is.|
S~It is interesting to see the difference through two friends' experiences.|
N~Knowing how each changed would make caring for the next stage easier.|
S~Two apparently matching introductions have revealed remarkably different second acts.|
S~A familiar shape can hold more than one possible future.|
N~Same starting species, different conditions. Good reason to compare the inputs.|
S~Fire and water were both waiting behind the same small face.|
S~A shared interest gives them something fascinating to compare now.|
S~I wonder whether they had expected the evolutions before they happened.
''')
add('safari_surf','SafariZone_SecretHouse_Text_ExplainSurf',
    'After the exploration prize is given, the attendant explains Surf and its reusable HM.','''
S~All that walking has earned a way to travel over an entirely different surface.|
S~The prize provides a reusable field capability that broadens accessible routes.|
N~Useful. Make sure the partner and conditions are ready for a crossing.|
S~A hidden little house has made the world feel wider.|
N~A water journey still needs planning, even with a helpful move.|
S~The walking challenge concludes by opening a more aquatic next chapter.|
S~A door at the end of the land has offered a road beyond it.|
S~Reusable capability upgrade! Excellent payoff for careful navigation.|
S~The water may stop being only the edge of where we can go.|
S~A practical prize with instructions that make the visit feel complete.|
S~I wonder where the first water crossing with that move will take us.
''')
add('safari_prize_full','SafariZone_SecretHouse_Text_DontHaveRoomForPrize',
    'The Secret House attendant cannot give the prize because the bag is full.','''
N~We reached the secret house and forgot to leave a room in the bag for the secret prize.|
N~The reward transfer did not complete. Reaching the destination alone did not provide the item.|
N~Clear some space before another attempt to accept it.|
F~That is an awkward end to such a long walk.|
N~A little sorting is better than rushing the handoff and losing track.|
N~The grand exploration challenge concludes at a rather small luggage obstruction.|
N~The furthest corner had a reward; the nearest pocket had no room.|
N~Capacity failure after successful navigation. Separate issues.|
N~A long road has ended at a very small closed place.|
N~We should make room properly before the attendant tries again.|
N~I wonder how often they see a triumphant visitor suddenly sorting the whole bag.
''')
add('safari_koga_patrol','SafariZone_West_Text_KogaPatrolsSafariEverySoOften',
    'A visitor credits Koga\'s patrols for making the large Safari Zone feel safe.','''
S~A reassuring bit of work behind everybody else's relaxing day.|
S~Regular oversight can make a large public habitat more manageable and safer to visit.|
S~Good to know someone is watching for trouble, not just waiting at the gate.|
S~A place feels kinder when someone takes responsibility for the people inside it.|
N~The quiet practical work helps everyone enjoy the outing.|
S~The peaceful setting has a diligent guardian outside the main spotlight.|
S~A safe afternoon often has someone else's attention holding it together.|
N~Active monitoring across a large area. Useful maintenance of public safety.|
S~A wide place feels less empty when someone knows its paths well.|
S~That is a good reason to respect him beyond the Gym title.|
S~I wonder which parts of the grounds he checks most often.
''')
add('safari_rocks','SafariZone_West_Text_RocksMakeMonRunButEasierCatch',
    'A visitor describes the capture tradeoff of throwing rocks at Pokemon.','''
N~A strategy with a very unhappy Pokemon at the other end. I would rather be patient.|
N~The stated tradeoff concerns capture and flight probabilities; welfare still deserves consideration.|
N~Do not let a frustrating catch become an excuse to hurt something.|
N~I would find it hard to enjoy a meeting that begins by frightening the other creature.|
N~A calm approach feels better than making the encounter harsher.|
N~A very clinical description of a method with an unpleasant recipient.|
N~An easier capture is not the only thing worth considering.|
N~The numbers do not include every cost. That matters when the subject is alive.|
N~A stone can make a small life feel very far from welcome.|
N~There are choices beyond whatever makes the counter look better.|
N~I wonder whether the Pokemon remember which visitors were gentle.
''')
add('safari_bait','SafariZone_West_Text_BaitMakesMonStickAround',
    'A visitor explains that bait can keep Pokemon occupied nearby.','''
S~Snacks are a fairly understandable reason to delay an exit. I sympathize.|
N~A food distraction may change behavior, though it does not guarantee a successful catch.|
N~Give them room while they eat. No reason to turn a quiet moment rough.|
S~It sounds gentler than frightening them into staying.|
N~Use what the reserve supplies. Unknown food is not automatically good for every Pokemon.|
M~The buffet briefly outbids the appeal of leaving. A familiar plot.|
S~A small meal making an uncertain visitor linger.|
N~Behavior influenced by an available resource. The remaining tradeoffs still matter.|
S~A little sweetness can hold a creature near without a shout.|
N~A calmer approach still needs patience when it does not give the result we hoped for.|
S~I wonder which residents are most interested in the bait.
''')
add('safari_unwanted_catches','SafariZone_West_Text_HikedLotsDidntSeeMonIWanted',
    'A visitor is disappointed after much walking without finding the desired Pokemon.','''
N~The feet did the work. The particular Pokemon declined the appointment.|
N~A long search does not guarantee a rare encounter. The disappointment is understandable.|
N~Rest now. No need to make a hard day longer out of frustration.|
N~It is disappointing when the day you imagined does not arrive with you.|
N~There may still have been something worth enjoying along the way.|
N~The expedition's desired guest star has remained regrettably offstage.|
N~A wanted meeting can make all the other small discoveries difficult to see.|
N~Effort and outcome are not perfectly correlated. Review conditions before repeating the search.|
N~The path has offered many leaves, but not the one little shape they hoped for.|
N~A missed goal does not have to turn the whole outing into a mistake.|
N~I wonder what they most wanted to see and where they looked for it.
''')
add('underground_shop','UndergroundPath_EastEntrance_Text_DoYouGoToCeladonDeptStore',
    'A traveler recommends Celadon\'s department store and asks whether we visit often.','''
S~A whole conversation can begin with a shared suspicion that one shop has everything.|
N~A broad inventory makes the store useful for several different preparation needs.|
N~Good selection. Still worth knowing what we need before entering.|
S~It is nice when a familiar place becomes a small point of connection.|
N~A list helps in a building full of good reasons to spend more than planned.|
S~The traveler offers a glowing review of a destination with several floors of temptation.|
N~A store can become an oddly reliable landmark in people's lives.|
S~A centralized supplier saves a lot of separate trips. Useful.|
N~A tall building full of little things someone might need.|
S~A good shop gives different people different reasons to remember it.|
S~I wonder which floor they head for first.
''')
add('underground_lost_items','UndergroundPath_SouthEntrance_Text_PeopleLoseThingsInTheDarkness',
    'A traveler says people lose belongings in the dark Underground Path.','''
N~Darkness is a terrible pocket-checking assistant. We should do the job ourselves.|
N~Low visibility makes noticing dropped objects harder for owners and later passersby.|
N~Secure the bag before going in. Lost things may belong to someone still looking.|
N~It is easy for a small mistake to feel much larger in the dark.|
N~A quick check now could save a long walk back later.|
N~The tunnel quietly acquires a collection nobody intended to donate.|
N~An ordinary little object can become surprisingly difficult to find without light.|
N~Improve retention before the low-visibility section. Simple preventive maintenance.|
N~The dark keeps small things without asking to own them.|
N~Useful warning. Closures and pockets deserve a moment of attention.|
N~I wonder how often someone comes back to search for the same dropped thing.
''')
add('underground_sleepy_rumor','UndergroundPath_WestEntrance_Text_SleepyMonNearCeladon',
    'A traveler heard that another sleepy Pokemon appeared near Celadon.','''
N~The region's very large naps appear to be expanding their itinerary.|
N~The speaker presents a secondhand sighting, not a verified current obstruction.|
N~Worth remembering before choosing a route. Confirm it when we get closer.|
N~An unexpected sleeper can change a very ordinary walk.|
N~A little local news can save us a tiring detour later.|
M~Another member of the immovable sleeping cast has reportedly taken a position near town.|
N~A peaceful activity with an unusually inconvenient sense of location.|
N~Potential route constraint. Mark as unconfirmed until observed.|
N~A quiet shape may have become the loudest fact on the road.|
N~At least they say heard. Rumor and firsthand directions are different things.|
N~I wonder who saw it and how long it has been there.
''')
add('dojo_offer','SaffronCity_Dojo_Text_ChoosePrizedFightingMon',
    'After losing, the karate master offers a choice of Fighting Pokemon instead of the dojo emblem.','''
S~A gracious offer after a tough match. We have not chosen a new partner yet.|
N~He proposes an alternative reward and leaves the selection to us. The transfer is still pending.|
N~Fair offer. Think about the partner, not just which prize looks stronger.|
F~He sounds worried about the emblem and proud of the Pokemon at the same time.|
N~A new companion deserves a choice made with time and care.|
S~The defeated master preserves the symbol and offers something considerably more alive.|
N~A living reward deserves more thought than a trophy shelf does.|
N~Choice offered, no handoff yet. Review the options before committing.|
S~An old emblem stays on the wall while a new road may open for a companion.|
N~A gracious ending should still leave room to consider what the Pokemon needs.|
S~I wonder how he chose the two partners he is offering.
''')
add('dojo_training_invitation','SaffronCity_Dojo_Text_StayAndTrainWithUs',
    'After the gift was chosen, the master invites us to remain and train.','''
S~The former opponent has become a possible teacher. A good sort of rematch.|
S~The invitation keeps the relationship open beyond the completed reward.|
S~Good offer. A steady place to practice can matter.|
S~It is nice to be welcome after the exciting part is over.|
S~A shared routine can teach more than a single big challenge.|
S~The challenger is invited into the continuing life of the dojo.|
S~A room that tests you can also become a room that makes space for you.|
S~Ongoing practice opportunity with experienced feedback. Useful.|
S~The doorway has changed from a challenge into an invitation.|
S~He seems to respect the work enough to want to share more of it.|
S~I wonder which exercise he would begin a visitor with.
''')
add('dojo_mike','SaffronCity_Dojo_Text_MikePostBattle',
    'Mike says he is much weaker than the dojo\'s master.','''
N~The master has received a very enthusiastic introduction from the defeated opening act.|
N~A stronger instructor is plausible, though the comparison does not specify the next matchup.|
N~We will prepare. No need for him to talk himself down.|
N~I hope admiration for the master leaves him room to value his own progress.|
N~A teacher can be excellent without making every student sound insignificant.|
M~The supporting fighter redirects the review toward a supposedly more formidable lead.|
N~A small fry is still allowed a perfectly respectable afternoon.|
N~Expected difficulty increased. His self-rating remains unnecessarily harsh.|
N~A shorter shadow can still belong to someone growing.|
N~He can praise his master without making himself disappear from the comparison.|
N~I wonder what his master thinks he already does well.
''')
add('dojo_hideki','SaffronCity_Dojo_Text_HidekiPostBattle',
    'Hideki warns us that the professional master will beat us.','''
N~A confident forecast from someone whose own forecast just had a difficult afternoon.|
N~Professional experience is relevant, but it does not guarantee the result.|
N~We can be ready without deciding the match before it starts.|
N~That makes me nervous, though I would rather know the challenge is serious.|
N~Preparation is more useful than either boasting or worrying about a promised loss.|
N~The next opponent receives a promotional introduction with an exceptionally decisive ending.|
N~A prediction is not a memory. The battle still has to happen.|
N~High capability expected. Outcome remains untested.|
N~A strong door can be approached carefully without already calling it closed.|
N~A little respect is useful. A scripted defeat is less so.|
N~I wonder which part of the master's technique he finds most difficult to answer.
''')
add('dojo_aaron','SaffronCity_Dojo_Text_AaronPostBattle',
    'Aaron admits the dojo fighters fear psychic power.','''
N~An impressive collection of fists has found one subject it would rather discuss quietly.|
N~He identifies a shared concern that may reflect the limitations of their specialization.|
N~Every style has a problem worth preparing for. Good to admit it.|
N~It is reassuring, in a way, to hear a confident person acknowledge fear.|
N~They could learn from the weakness without treating fear itself as a disgrace.|
N~The bravest-sounding chorus finally reaches a subject that lowers the volume.|
M~A very particular shadow at the edge of all that confidence.|
N~Known weakness identified. Now build a response instead of ignoring it.|
N~A strong hand can still hesitate before something it cannot touch.|
N~A good reminder that looking formidable is not the same as feeling invulnerable.|
N~I wonder whether anyone here has tried training with a Psychic-type partner.
''')
add('dojo_hitoshi','SaffronCity_Dojo_Text_HitoshiPostBattle',
    'Hitoshi proudly says top fighters from around the land train at the dojo.','''
S~A small room can have a very wide reputation behind the door.|
S~A strong training community can support learning through varied experienced partners.|
N~Good place to learn if people respect each other while doing it.|
S~It must feel special to share a room with people you used to hear stories about.|
N~The ordinary practice is what makes the reputation worth keeping.|
S~The modest venue claims a distinguished recurring cast.|
S~A familiar floor worn down by many different determined feet.|
S~Access to varied expert feedback is a real advantage.|
S~Many paths have brought their strongest steps into the same room.|
N~An impressive reputation should come with a welcoming place for people still learning.|
S~I wonder which visiting fighter left the biggest impression on him.
''')
add('league_advice','IndigoPlateau_PokemonCenter_1F_Text_GymGuyAdvice',
    'The League guide explains the consecutive Elite Four challenge and restarting after a loss.','''
N~A long challenge with no little chapter break for trying the last page again. Prepare carefully.|
N~The consecutive format changes resource planning and the consequence of a failed attempt.|
N~Check the whole team. This is not a job for one tired partner.|
N~It is daunting, but knowing the rules makes it feel less like stepping into nothing.|
N~Supplies, rest, and a calm moment before the door. The basics still matter here.|
N~The final program is announced, including the unforgiving policy on repeat performances.|
N~A hard ending can still become another attempt, once everyone is ready.|
N~Sequential challenge with reset on failure. Budget for the whole chain.|
N~A row of doors, each asking whether there is enough strength for the next.|
N~His excitement should not hurry us past checking what we need.|
N~I wonder how many challengers come back to thank him after finally succeeding.
''')
add('league_guard_welcome','IndigoPlateau_PokemonCenter_1F_Text_FaceEliteFourGoodLuck',
    'The guard explains that each Elite Four victory opens the next door and wishes us luck.','''
S~One door at a time. That is a manageable shape for a very big challenge.|
N~The progression rule is explicit. Each result controls access to the next opponent.|
N~Good. Take each match seriously and keep track of the team's condition.|
N~A kind good luck feels welcome before a door like that.|
N~A big goal still needs attention to the partners in the current room.|
S~The final corridor promises one clear next scene after another.|
N~A distant challenge becomes a little less abstract when it is simply the next door.|
N~Clear state transitions. Preparation still determines whether we can use them.|
S~The path will open in pieces as we are ready to meet them.|
S~A simple explanation, delivered without trying to intimidate us.|
S~I wonder what the guard notices in people just before they enter.
''')
add('league_closed','IndigoPlateau_PokemonCenter_1F_Text_LoreleiIsAbsentClosedForTimeBeing',
    'The guard apologizes that the League is temporarily closed while Lorelei is away.','''
N~A very long road to a temporarily closed door. At least the answer is clear.|
N~The complete challenge requires the absent member, so entry is suspended.|
N~Nothing to force here. Rest the team and find out when to return.|
N~That would be hard news after coming all this way.|
N~We can use the pause for recovery rather than make the disappointment harder.|
N~The great performance has been postponed for a missing principal.|
N~Even an imposing door can hide a very ordinary scheduling problem.|
N~Required participant unavailable. The system cannot proceed.|
N~A path can pause without having forgotten where it goes.|
N~The guard could have chosen a kinder phrase than wasted time, though.|
N~I wonder how many other challengers arrived before hearing the news.
''')
add('lorelei_after','PokemonLeague_LoreleisRoom_Text_PostBattle',
    'Lorelei acknowledges underestimating us and sends us onward with a warning.','''
N~A first door opened, with a reminder that the building has several more opinions.|
N~She revises her assessment while correctly distinguishing one victory from the entire challenge.|
N~Good result. Check the team before going farther.|
N~The praise is quiet, but I am glad she gave it.|
N~A strong beginning still needs a steady next step.|
S~The first critic revises the review and sends us toward the rest of the program.|
N~A little recognition, kept cool enough not to become a distraction.|
N~Initial test passed. Remaining workload is still significant.|
N~One room behind us, more waiting beyond its door.|
N~She can admit a mistaken first impression without turning it into an excuse.|
N~I wonder which decision changed her view of the team.
''')
add('bruno_after','PokemonLeague_BrunosRoom_Text_PostBattle',
    'Bruno accepts that his part is finished and directs us to the next challenge.','''
N~A very tidy ending from someone who does not need to narrate his disappointment.|
S~He accepts the result and keeps the challenge's progression clear.|
N~Fair match. Onward when the team is ready.|
N~There is a calm dignity in knowing when your part is finished.|
N~A moment to gather ourselves before the next room would be wise.|
S~The formidable performer exits the argument with admirable economy.|
S~A strong presence can also know how to leave a silence.|
N~Stage complete. Check resources before the next test.|
N~The door opens without another hard word attached to it.|
S~A clean acknowledgment is often more impressive than a speech.|
N~I wonder what he will think about from that match after we leave.
''')
add('agatha_after','PokemonLeague_AgathasRoom_Text_PostBattle',
    'Agatha recognizes what Oak sees in us and curtly sends us onward.','''
M~A compliment delivered with the door already held open for our departure.|
S~She connects the observed performance with Oak's earlier confidence in us.|
N~We earned the win. No need to ask her for a softer voice.|
F~That is warm by a very particular person's standards, I think.|
N~A brisk send-off still leaves us with the useful recognition.|
M~The severe critic offers a favorable verdict and immediately closes the interview.|
M~An economical compliment. I appreciate the lack of forced conversation afterward.|
N~Assessment updated. No additional input requested.|
S~A little approval has passed through a very old thorn hedge.|
N~She says it plainly enough. We can accept the praise without polishing it.|
N~I wonder what exactly reminded her of Oak's expectations.
''')
add('lance_after','PokemonLeague_LancesRoom_Text_PostBattle',
    'Lance congratulates our victory over him but reveals the rival is already Champion and remains to be faced.','''
U~One more door! That is a very dramatic footnote to almost being finished.|
N~Defeating the Elite Four has qualified us for the reigning Champion rather than completed the title.|
N~Check the team. The next match still needs everyone ready.|
U~I would need a moment to let that change in expectation settle.|
N~A long effort deserves a calm final preparation, not a hurried last push.|
U~The apparent ending opens a final scene, with an extremely familiar name on the door.|
N~The last step has acquired one more step. A difficult little surprise.|
N~Additional final requirement identified. Reassess remaining resources now.|
N~The road has kept one familiar shadow beyond its furthest visible bend.|
N~The team has come a long way. We can give the last preparation the time it needs.|
N~I wonder how differently the rival felt standing here just before us.
''')
