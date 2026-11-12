"""Source-reviewed Kanto interior conversations and route post-battle replies.

All entries bind final NPC speech, never battle intros/defeat text or receipts.
Shared native trade and nickname printers need separate runtime review and are
intentionally not represented as unique successful fossil/trade conversations.
"""
ROWS = []
EMOTIONS = dict(N='neutral', S='soft_smile', A='annoyed', F='flustered',
                D='sad', U='surprised', M='smug', L='laughing')

def add(key, labels, subject, lines):
    replies = []
    for line in lines.strip().split('|'):
        line = line.strip()
        if len(line) > 1 and line[1] == '~' and line[0] in EMOTIONS:
            line = EMOTIONS[line[0]] + line[1:]
        replies.append(line)
    assert len(replies) == 11, (key, len(replies))
    ROWS.append(dict(key='kanto_ir_' + key, labels=labels.split(),
                     subject=subject, replies=replies))

add('tea_received', 'CeladonCity_Condominiums_1F_Text_NothingBeatsThirstLikeTea',
    'After successfully giving Tea, the woman praises hot tea for thirst.', '''
S~She has strong opinions about tea. Luckily, they come with actual tea.|
S~A generous recommendation, backed by a sample. Excellent procedure.|
S~She noticed we were passing through and gave us something useful.|
S~There is something reassuring about how certain she is of a simple pleasure.|
S~Good tea and a warm welcome. That is a respectable house specialty.|
S~Her argument has a fragrant supporting exhibit. I find it persuasive.|
S~The world briefly became a little warmer. Tea does that sometimes.|
S~No elaborate sales pitch. She just handed us the solution.|
S~A small hot cup can make quite a large invitation.|
S~She knows her favorite and shares it without making a performance of it.|
S~I like that she welcomed a traveler with something she enjoys herself.
''')
add('tea_company', 'CeladonCity_Condominiums_1F_Text_MyDearMonsKeepMeCompany',
    'The tea woman enjoys her Pokemon company; Meowth brings home money.', '''
L~Meowth contributes to the household budget? I owe several plush toys an awkward conversation.|
S~Companionship and an income. Meowth has a remarkably broad role here.|
S~They keep her company. The money sounds like a pleasant extra.|
S~She sounds proud of them in a very familiar, everyday way.|
L~That Meowth pays its way. Mine would probably invoice me for lunch.|
M~A devoted household, with one unusually enterprising member.|
S~A quiet room full of company. That sounds like a decent life.|
U~Meowth brings money home? Better accounting than some businesses.|
S~Perhaps Meowth considers coins a perfectly ordinary affection.|
S~She says dear Pokemon first and money second. Good priorities.|
S~I wonder where Meowth goes on those little earning expeditions.
''')
add('tea_daisy', 'CeladonCity_Condominiums_1F_Text_DaisyComesToBuyTea',
    'The woman asks about Pallet and mentions Daisy buys tea in Celadon.', '''
S~Daisy has a tea route! That is a very civilized kind of adventure.|
S~A daily habit explains why the shop and Daisy are familiar to her.|
S~Nice to hear a familiar name so far from Pallet.|
S~She remembered Daisy through something small. Those details stay with people.|
S~A favorite tea is a good reason to make a regular trip.|
S~A little thread from Pallet turns up here, smelling faintly of tea.|
S~People leave traces in ordinary places. Sometimes the trace is a shopping list.|
S~Daisy found a dependable supplier. An underrated accomplishment.|
S~The teacup seems to know more people than I do.|
S~She remembers what Daisy enjoys. That is a sweet sort of familiarity.|
S~Celadon must feel less anonymous when somebody remembers your usual purchase.
''')
add('store_welcome', 'CeladonCity_DepartmentStore_1F_Text_WelcomeToDeptStore',
    'The department store receptionist directs us to its layout board.', '''
S~A whole building of shopping, with instructions. They anticipated my wandering.|
N~The directory should save us several unnecessary journeys between floors.|
N~Check the board before we haul the team up five flights.|
S~That was a clear welcome. I appreciate knowing where to start.|
S~A directory first, shopping second. My feet support this arrangement.|
M~The grand expedition begins by reading the board immediately to our right.|
N~A map of temptation. At least the floors are labeled.|
S~Good signage! The least glamorous part of a building doing important work.|
N~So many floors, and only one pair of feet apiece.|
S~She points people toward what they need. That is good service.|
S~I wonder which floor gets the most lost visitors.
''')
add('super_repel', 'CeladonCity_DepartmentStore_2F_Text_SuperRepelMorePowerfulRepel',
    'A shopper studies Super Repel and compares it with ordinary Repel.', '''
M~The name does seem fairly confident about being better.|
N~Comparing the labels is sensible. Similar packaging can hide useful differences.|
N~Worth checking before paying extra for the word Super.|
N~They are taking their time with the choice. That seems reasonable.|
N~Buy the version that suits the walk, rather than the loudest name.|
M~A product named Super has narrowly survived its first critical review.|
N~The promise of fewer interruptions has an understandable appeal.|
N~A comparison shopper! Finally, somebody reads the specifications.|
N~Some journeys call for a little more distance between strangers.|
S~They are reading instead of buying by the color of the bottle. Sensible.|
N~Everyone prepares differently for the same patch of tall grass.
''')
add('revive_outings', 'CeladonCity_DepartmentStore_2F_Text_BuyReviveForLongOutings',
    'A shopper recommends carrying Revives for long outings.', '''
N~Long outing supplies: shoes, water, and a way to rescue the plan.|
N~A contingency item becomes more useful as the distance to a Center grows.|
N~Good advice. A long road is a poor place to discover an empty pocket.|
N~They sound like they have had a journey go wrong before.|
S~A little preparation keeps a difficult outing from becoming a miserable one.|
N~One prefers an uneventful journey, but packs for a less considerate author.|
N~An unexciting purchase can be the best one by the end of the day.|
N~Spare capacity for a bad day. I approve of that design principle.|
N~A way back onto your feet is worth carrying.|
N~Practical advice, delivered without inspecting our entire bag. Appreciated.|
N~That sounds like advice somebody learned a long walk from town.
''')
add('lance_capes', 'CeladonCity_DepartmentStore_2F_Text_LanceComesToBuyCapes',
    'The clerk wonders why Lance repeatedly buys identical capes.', '''
L~Emergency cape. Spare cape. Cape for when the emergency cape gets dramatic.|
M~Repeated purchases suggest wear, preference, or an exceptionally narrow wardrobe.|
M~Find something that works. Buy a spare. I understand him.|
S~Having one reliable look must make mornings easier.|
L~Even capes need laundry days. Probably very inconvenient laundry days.|
M~A man cannot let his signature silhouette be defeated by a washing line.|
M~Perhaps every cape is different in ways only he can bear to explain.|
N~Rotation reduces wear! Though cape storage must be a peculiar engineering problem.|
S~A cupboard full of the same shadow. Oddly comforting.|
M~Consistency is a style choice. So is having absolutely no backup look.|
S~The staff remember his capes before anything else. That is quite an impression.
''')
add('original_trainer', 'CeladonCity_DepartmentStore_3F_Text_OTStandsForOriginalTrainer',
    'A shopper explains original trainer registration and ID numbers.', '''
N~A Pokemon can have a long history before it meets us. A little label remembers the start.|
S~The registration preserves provenance even when the Pokemon changes companions.|
N~Useful to know where a partner came from. Useful to treat it well now, too.|
S~A name in the record is a small piece of somebody else's journey.|
N~Records help, especially when a Pokemon has traveled through several hands.|
N~Every arrival has a first chapter, even when we enter much later.|
S~A beginning that does not vanish when the next part starts. I like that.|
N~An ID makes the record traceable. Clear labeling earns its keep again.|
N~Names can travel without their owners. These ones follow Pokemon.|
N~A useful detail to check when meeting a traded partner.|
S~I wonder how many different towns a traded Pokemon remembers.
''')
add('haunter_trade_plan', 'CeladonCity_DepartmentStore_3F_Text_BuddyTradingKangaskhanForHaunter',
    'A shopper is excited to trade Haunter for a friend\'s Kangaskhan.', '''
S~Both friends found a Pokemon they want. That is a promising exchange.|
S~A trade between friends offers the reassuring possibility of future updates.|
N~As long as both know what they are agreeing to, sounds fair.|
S~The excitement makes the whole shop feel a little less impersonal.|
S~They sound pleased with the arrangement. Good to settle that before trading.|
S~Two collections take an interesting turn, with a handshake in the middle.|
S~A friend is a comforting person to trust with a familiar Pokemon.|
S~A mutually useful swap. Those are remarkably satisfying when they work out.|
S~Two companions finding different doors to walk through.|
S~Knowing what your friend wants makes a good trade much easier.|
S~I would be curious to hear how both Pokemon settle into the change.
''')
add('haunter_surprise', 'CeladonCity_DepartmentStore_3F_Text_HaunterEvolvedOnTrade',
    'The Haunter collector is surprised that the traded Haunter evolved.', '''
U~They ordered a Haunter and received a surprise with a much larger grin.|
N~The trade triggered evolution. Their collection plan omitted an important variable.|
N~Still their new partner. Just came with an unexpected change.|
U~They sounded so certain a moment ago. That must be a lot to take in.|
S~Give the new arrival a chance before deciding the trade went wrong.|
U~The collector's carefully arranged expectation has acquired teeth.|
M~A ghost found a way to surprise the person specifically collecting ghosts.|
U~Unexpected behavior! Useful discovery, unfortunate timing for the collection.|
S~Even a familiar ghost has another shape tucked away.|
N~They loved the look they expected. I wonder how this new look will grow on them.|
U~That reaction tells me nobody warned them what trading could do.
''')
add('trade_id', 'CeladonCity_DepartmentStore_3F_Text_CanIdentifyTradeMonsByID',
    'A shopper explains using ID numbers to identify traded Pokemon.', '''
N~A tiny number doing a great deal of remembering.|
N~Consistent identifiers prevent confusion when names or ownership change.|
N~Worth checking the record before mixing up two partners.|
N~It is good that something can keep their histories distinct.|
N~Careful records matter when several similar Pokemon arrive together.|
N~A modest string of digits keeps an elaborate case of mistaken identity at bay.|
N~A number cannot tell the whole story, but it can keep two stories apart.|
S~Labels that survive a handoff! Someone thought about the awkward cases.|
N~A small mark can follow a very long journey.|
N~Especially useful when everyone has named their Pokemon something fashionable.|
N~The number is one way to trace where a new partner began.
''')
add('doll_present', 'CeladonCity_DepartmentStore_4F_Text_GettingPokeDollAsPresent',
    'A shopper chooses a popular Poke Doll as a present for his girlfriend.', '''
S~A doll is a good start. Knowing which one she likes would be an even better start.|
N~Popularity is information about many people. Her preferences would be better data.|
N~Ask what she likes. Saves a second trip.|
S~He wants to choose well. I hope he remembers something she has actually mentioned.|
S~A present lands better when there is a little of the person in the choice.|
M~The popular choice has volunteered as a substitute for romantic research.|
S~A small, soft offering. There are worse ways to be unsure.|
N~A tiny bit of user research could make this a much stronger selection.|
S~Perhaps she has already pointed at the answer in a shop window.|
S~Popular is fine. Her favorite color would make it feel meant for her.|
S~I wonder whether she collects them or whether this will be her first.
''')
add('doll_escape', 'CeladonCity_DepartmentStore_4F_Text_CanRunAwayWithPokeDoll',
    'A shopper explains distracting wild Pokemon with a Poke Doll to escape.', '''
U~The doll has a dangerous second career. I thought it only sat on shelves.|
N~A distraction can create enough time to withdraw without another attack.|
N~An escape option is useful. No need to win every encounter.|
N~Leaving safely sounds better than pressing a battle the team cannot manage.|
N~One more sensible thing to carry when the route is unfamiliar.|
M~A plush decoy. The gift department has concealed a tactical division.|
N~A soft toy buying a hard exit. Unexpectedly practical.|
U~Simple distraction, immediate retreat. Elegant, if rough on the doll.|
N~A little false friend left behind so the real ones can leave.|
M~Cute and useful. A surprisingly strong argument for shelf space.|
N~I would never have guessed that use from looking at the display.
''')
add('stat_enhancers', 'CeladonCity_DepartmentStore_5F_Text_ExplainStatEnhancers',
    'A customer explains the different stat enhancers sold on this floor.', '''
N~That is a lot of bottles to keep straight. My shopping list needs a shopping list.|
N~Different supplements target different attributes. The labels deserve careful attention.|
N~Know what the team needs before buying the expensive bottle.|
N~They have clearly spent time understanding the differences.|
N~The right purchase matters more than coming away with a heavy bag.|
M~An entire shelf of improvements, each with its own rather confident name.|
N~So many tiny bottles promising to make a difference. Choose carefully.|
S~Specific effects, clear categories. I could spend far too long comparing these.|
N~A little bottle is still a choice about what you want to grow.|
N~Good that they explained the differences. Those labels are not exactly intuitive.|
N~The fifth floor attracts some very deliberate planners.
''')
add('protein_iron', 'CeladonCity_DepartmentStore_5F_Text_HereForStatEnhancers',
    'A shopper describes Protein for Attack and Iron for Defense.', '''
M~Protein and Iron. The shopping basket sounds tougher than I do.|
N~Attack and defense call for different purchases. Specific goals simplify the choice.|
N~Hit harder or hold up longer. Depends what the team is missing.|
N~They seem to have a reason for coming to this particular shelf.|
M~A label saying Protein still does not make it a meal.|
N~Two very different approaches to surviving the same difficult afternoon.|
N~Strength and endurance in neighboring bottles. A tidy little rivalry.|
N~Useful distinction. More force and more resistance solve different problems.|
N~One bottle for striking, another for weathering the strike.|
N~They know what they came for. Dangerous shopping skill in a store this large.|
N~I wonder whether they buy for one partner or plan for a whole team.
''')
add('light_screen', 'CeladonCity_DepartmentStore_Roof_Text_ExplainTM16',
    'After receiving water and giving TM16, the girl explains Light Screen.', '''
S~We brought water; she brought protection from special attacks. Strong picnic arrangement.|
S~She knows exactly what her gift does. A thoughtful exchange.|
S~Light Screen could keep the team standing through a rough special attack.|
S~Her thank-you was generous. I like that she explained it, too.|
S~A bottle of water turned into something that can help the whole team.|
S~An unexpectedly practical flourish to a very ordinary kindness.|
S~Clear water, a barrier of light. She has a consistent aesthetic.|
S~A defensive option from a rooftop errand. Productive detour!|
S~We eased her thirst; she gave us a little shelter.|
S~She was prepared to thank somebody properly. That is rather sweet.|
S~That small exchange gave us more than I expected when we walked upstairs.
''')
add('safeguard', 'CeladonCity_DepartmentStore_Roof_Text_ExplainTM20',
    'After receiving Soda Pop and giving TM20, the girl explains Safeguard.', '''
L~Soda for Safeguard. Fizzy drinks have become a strategic resource.|
S~Preventing status problems can preserve several turns of a difficult battle.|
S~Useful cover against tricks that stop a partner from acting.|
S~She made sure we knew why the gift could help.|
S~A grateful explanation beats just handing over a mysterious disc.|
M~A fizzy interlude concludes with an unusually sensible defensive recommendation.|
S~A little protection against unpleasant surprises. Good rooftop luck.|
S~Prevention! Fixing a problem before it appears is deeply satisfying.|
S~A sweet drink purchased a small ward against trouble.|
S~She traded us something useful rather than something she merely wanted gone.|
S~Who expects a lesson in status protection beside a vending machine?
''')
add('reflect', 'CeladonCity_DepartmentStore_Roof_Text_ExplainTM33',
    'After receiving Lemonade and giving TM33, the girl explains Reflect.', '''
S~Lemonade in, defensive wall out. This roof has excellent exchange rates.|
S~Reflect reduces the threat of physical attacks. A useful addition to our options.|
S~A little more room to take a hit and keep going. Worth remembering.|
S~She sounded happy to share something that matters to her team.|
S~A refreshing drink and a helpful thank-you. Both sides did well.|
S~Lemonade has purchased us a rather more durable kind of refreshment.|
S~There is an odd gentleness to a gift that softens a blow.|
S~Physical protection from a small disc! Nice payoff for a drink run.|
S~She answered a small kindness with a little wall of light.|
S~A good gift comes with enough explanation to actually use it.|
S~The rooftop crowd knows more about battle support than I expected.
''')
add('drink_no_room', 'CeladonCity_DepartmentStore_Roof_Text_DontHaveSpaceForThis',
    'The girl cannot give her reward because the bag has no room.', '''
N~We found room for generosity but forgot a pocket for the reply.|
N~The reward could not fit. We should avoid assuming the exchange completed normally.|
N~Bag is full. Sort it before trying to carry anything else.|
N~She did try to give us something. It is awkward when the bag gets in the way.|
N~A little sorting would have helped before making the exchange.|
N~A charming transaction has encountered the immovable force of packed luggage.|
N~A full bag can make even a thank-you complicated.|
N~Capacity limit. Predictable in theory, annoying at exactly this moment.|
N~The gift has reached a door that opens onto a wall of belongings.|
N~Our bag has chosen an unfortunate moment to reject accessories.|
N~That is a different ending than the cheerful exchange she had in mind.
''')
add('drink_declined_repeat', 'CeladonCity_DepartmentStore_Roof_Text_ImNotThirstyAfterAll',
    'The girl declines a drink whose corresponding reward was already claimed.', '''
M~The thirst has withdrawn its application. Fair enough.|
N~She declined. There is no reason to press the offer.|
N~Keep the drink for later. She said no.|
S~At least she let us know before we handed it over.|
S~Another time, perhaps. A drink keeps better than an awkward insistence.|
M~A sudden revision in the rooftop thirst forecast.|
N~Even a simple offer can reach its natural ending.|
N~Request canceled. Conveniently, the drink is still usable.|
N~Thirst comes and goes. The bottle can wait.|
S~She changed her answer politely. That is enough explanation.|
N~Interesting how quickly that request disappeared once we offered something.
''')
add('thirsty_no_drink', 'CeladonCity_DepartmentStore_Roof_Text_ImThirstyIWantDrink',
    'The girl says she wants a drink when we are carrying none.', '''
N~She has identified the problem. The vending machines seem to have anticipated it.|
N~A straightforward request, with a likely source of drinks nearby.|
N~If we buy one, do it because we choose to.|
N~She is being very direct about what she needs.|
S~A rooftop in the sun is a sensible place to want a cold drink.|
M~The roof presents a thirst problem alongside several coin-operated answers.|
N~A very small emergency, stated with complete conviction.|
N~Demand and supply are standing impressively close together.|
N~The machines hum, and someone nearby wishes for a drink.|
N~She has made her priorities unusually easy to understand.|
N~I wonder how long she has been standing beside those machines.
''')
add('immature_sister', 'CeladonCity_DepartmentStore_Roof_Text_MySisterIsImmature',
    'A trainer complains that his trainer sister is immature.', '''
M~Siblings can apparently detect immaturity from several floors away.|
N~Being a trainer does not make someone mature in every other respect.|
N~Sounds like siblings. A badge will not settle that argument.|
N~She may be different around him than around her Pokemon.|
M~A family outing can test patience more thoroughly than a battle.|
M~A brother files his official rooftop grievance. The sister has not been called to testify.|
N~Family has a way of remembering your least dignified moments.|
N~Training skills and sibling diplomacy clearly need separate practice.|
N~He knows exactly which little things she does to annoy him.|
M~He says that with the exhaustion only a sibling can earn.|
N~We have heard his side. I suspect she could offer a lively response.
''')
add('hotel_full', 'CeladonCity_Hotel_Text_ThisHotelIsForPeople',
    'The hotel clerk explains this is a human hotel and all rooms are full.', '''
N~A bed for people! Tragically, all the people arrived before us.|
N~Different accommodation, same capacity problem. There are no vacancies.|
N~Full up. We will need another place to rest.|
N~An easy mistake from outside. At least they explained kindly.|
N~A room would have been nice. We can still find somewhere to sit.|
M~Human lodging exists, but has declined to demonstrate its comforts today.|
N~A building full of occupied beds. Somehow that makes my feet more tired.|
N~Correct service, zero available capacity. That answers both questions.|
N~Every room already holds someone else's little evening.|
N~The clerk has probably had to explain that distinction quite often.|
N~Busy hotel. Celadon seems to attract visitors from everywhere.
''')
add('vacation_woman', 'CeladonCity_Hotel_Text_OnVacationWithBrotherAndBoyfriend',
    'A woman enjoys Celadon on vacation with her brother and boyfriend.', '''
S~She brought two favorite people to a pretty city. Ambitious travel planning.|
S~A mixed group can enjoy the same city for quite different reasons.|
S~She is having a good time. That is what the trip is for.|
S~It is nice to hear somebody enjoying the city without being in a hurry.|
S~A holiday with family and someone you love sounds worth planning.|
S~Celadon has acquired a party with three perspectives on the itinerary.|
S~She sounds happily oblivious to any complications. A useful holiday skill.|
S~Three people, one itinerary. Hope somebody built in flexible time.|
S~A pretty city becomes a different place with familiar company.|
S~She looks pleased with her arrangements. I respect that confidence.|
S~I wonder which place she wants to show them first.
''')
add('vacation_boyfriend', 'CeladonCity_Hotel_Text_WhyDidSheBringBrother',
    'The boyfriend wonders why his girlfriend brought her brother on vacation.', '''
M~He packed for a date and discovered a family excursion.|
N~Their expectations for the trip appear to differ substantially.|
N~He should ask her. Quietly resenting the brother will not help.|
F~That sounds like a conversation they should have between themselves.|
M~A surprise extra guest changes a holiday faster than bad weather.|
M~The romantic itinerary has encountered an unscheduled sibling.|
M~He is mourning a trip that apparently existed only in his own planning.|
N~This is why the passenger list belongs near the top of the plan.|
N~Three travelers, and one imagined table for two.|
M~They really should have compared their ideas of a romantic getaway.|
N~Same reservation, very different expectations. That could be a long holiday.
''')
add('vacation_brother', 'CeladonCity_Hotel_Text_SisBroughtMeOnVacation',
    'The brother is delighted his sister brought him on vacation.', '''
S~At least one person has no complaints about the guest list!|
S~For him, the arrangement is an uncomplicated success.|
S~Kid got a holiday with his sister. Hard to fault that excitement.|
S~He sounds so glad she thought to include him.|
S~Being invited along can mean a lot when you are the younger one.|
L~Our third traveler awards the trip an entirely unqualified review.|
S~A little joy, completely untroubled by romantic scheduling.|
S~One satisfied passenger! That is useful feedback for the organizer.|
S~His holiday has begun exactly where the others' argument might.|
S~He is having the time he was promised. That is quite sweet.|
S~I like how differently all three people describe the same vacation.
''')
add('restaurant_break', 'CeladonCity_Restaurant_Text_TakingBreakRightNow',
    'The restaurant worker says staff are taking a break.', '''
S~The people who serve lunch also need lunch. A sound arrangement.|
N~Scheduled rest is part of operating a restaurant sustainably.|
N~They are on break. We can come back.|
S~They sounded polite about it. No reason to make their rest awkward.|
S~Good. The kitchen deserves time to breathe between orders.|
N~Even the grand business of feeding strangers requires an intermission.|
S~For once, a closed service means somebody gets to sit down.|
N~Maintenance includes the people doing the work. Easy to forget.|
S~The room can be quiet while the hands that feed it rest.|
S~A short explanation and a proper boundary. Nicely handled.|
N~It must feel different in here when the lunch rush finally stops.
''')
add('restaurant_drugstore', 'CeladonCity_Restaurant_Text_OftenGoToDrugstore',
    'A diner says weak Pokemon lead to frequent drugstore visits.', '''
N~The drugstore knows them by now. I hope the team gets some quiet afternoons too.|
N~Frequent recovery needs may suggest adjusting the training plan as well as buying supplies.|
N~If every trip ends at the drugstore, ease up on the team.|
N~That sounds tiring for both the trainer and the Pokemon.|
N~Supplies help, but a gentler pace could save them a lot of trouble.|
N~The local shop prospers while this trainer's itinerary limps along.|
N~A routine built around getting hurt could use a small revision.|
N~Repeated repairs usually mean it is time to check how something is being used.|
N~Perhaps the route needs to get shorter before the shopping list does.|
N~They sound resigned to it. A change of plan might suit everyone better.|
N~I wonder whether they have tried a route better suited to their team.
''')
add('restaurant_basement', 'CeladonCity_Restaurant_Text_PsstBasementUnderGameCorner',
    'A diner whispers a rumor about a basement beneath the Game Corner.', '''
N~A basement rumor delivered at whisper volume. That always makes the stairs sound worse.|
N~A useful lead, though a rumor still needs confirmation.|
N~Worth remembering. Do not walk into an unknown basement unprepared.|
N~They lowered their voice before saying it. That makes me a little uneasy.|
N~A place can look cheerful upstairs and still have trouble underneath.|
M~The local gossip has developed an underground branch.|
N~A bright room overhead does not tell us much about what lies below it.|
N~Could be ordinary storage. Could be something worth checking carefully.|
N~The city has another layer people only discuss in whispers.|
N~That was a very deliberate whisper for a very public dining room.|
N~I wonder how the rumor started, and who has actually been down there.
''')
add('slots_regret', 'CeladonCity_Restaurant_Text_ThoughtIdWinItBack',
    'After giving away his Coin Case, the ruined gambler admits chasing losses.', '''
D~That sounds like a very expensive tomorrow that never arrived.|
N~Expecting the next attempt to erase previous losses can sustain a damaging cycle.|
N~Good that he stopped. Losing more would not fix what is gone.|
D~He says it so quietly now. It must hurt to understand it afterward.|
D~I am glad he is stepping away. He deserves a steadier evening.|
D~A cruel promise: one more try, and the whole story will turn around.|
D~He kept paying for an ending the machines did not owe him.|
N~Past losses cannot improve the next result. A brutal lesson to buy.|
D~A small box of coins can become a very deep hole.|
D~That is a hard thing to admit to a stranger. No jokes at his expense.|
D~His explanation tells us much more than the room's gossip about him did.
''')
add('x_attack', 'CinnabarIsland_Mart_Text_DontTheyHaveXAttack',
    'A shopper looks for X Attack to raise Attack during battle.', '''
N~They came for one very specific kind of extra oomph.|
N~They want a temporary battle enhancement, rather than a permanent training change.|
N~Worth checking stock before building a whole plan around it.|
N~Knowing the exact item must make the rest of the shelf easier to ignore.|
N~A short shopping list can still be frustrating when the one item is missing.|
M~The offensive strategy has paused for a disagreement with the inventory.|
N~One absent bottle, one interrupted plan for violence.|
N~Specific requirements meet uncertain stock. Classic supply problem.|
N~An empty space on a shelf can stop quite a confident plan.|
N~They know what they want. The shop has yet to cooperate.|
N~I wonder how often visiting trainers ask for that particular item.
''')
add('extra_items', 'CinnabarIsland_Mart_Text_ExtraItemsNeverHurt',
    'A Cinnabar shopper recommends carrying spare items for surprises.', '''
M~Extra items do hurt when the bag strap finally gives up. Still, sensible thought.|
N~Reserves reduce uncertainty, provided we can carry them comfortably.|
N~Keep the essentials spare. We still have to carry the bag.|
N~It is comforting to have a little room for things going differently.|
S~A few sensible extras can save a very inconvenient return trip.|
N~An optimistic excursion deserves a pessimistically stocked pocket.|
N~Spare supplies are quiet until the exact moment they become wonderful.|
S~Redundancy! A spare can turn a failure into a brief inconvenience.|
N~The unplanned part of a journey rarely sends a shopping list.|
N~A useful reserve, within reason. A packed bag has opinions too.|
N~Island shops must hear plenty of stories about forgotten supplies.
''')
add('locked_gym', 'CinnabarIsland_PokemonCenter_1F_Text_CinnabarGymLocked',
    'A visitor speculates that the locked Gym key may be in the burned mansion.', '''
N~A missing key in a burned mansion. That is an unusually complicated opening time.|
N~The mansion is a lead, though the visitor is speculating about the key.|
N~A burned building deserves caution, even if it might hold what we need.|
N~They came to challenge the Gym and found a very different problem.|
N~We should prepare before searching an old damaged place.|
M~The Gym entrance has outsourced its challenge to a rather ominous address.|
N~A locked door points toward a burned house. This island has difficult errands.|
N~A key search in a damaged building. Better watch where we step.|
N~The old house is keeping more than its own doors shut.|
N~They are careful to say could. We should remember that part.|
N~The connection between the old resident and the Gym might be worth asking about.
''')
add('evolution_wait', 'CinnabarIsland_PokemonCenter_1F_Text_EvolutionCanWaitForNewMoves',
    'A visitor advises that delaying evolution can allow learning moves first.', '''
S~Growing up can wait until the homework is done. Pokemon get that option!|
N~Evolution timing can affect which techniques become available. A useful planning detail.|
N~No need to rush a change when the team has a reason to wait.|
S~I like hearing that waiting can be a real choice.|
N~A little patience now can give a partner more to work with later.|
N~A delayed transformation can still be progress. An excellent complication.|
S~Something can keep learning without becoming something else yet.|
S~Sequence matters! Learn the useful thing, then consider the next stage.|
S~There are more ways to grow than changing shape.|
N~Timing can be part of the plan. Faster is not automatically better.|
N~I wonder which Pokemon taught that trainer to pay attention to the timing.
''')
add('lab_studies', 'CinnabarIsland_PokemonLab_Entrance_Text_StudyMonsExtensively',
    'The laboratory researcher describes daily study and rare Pokemon visitors.', '''
S~People bring rare Pokemon right to work? That would improve any Monday.|
S~A steady stream of unusual specimens could make comparative research very productive.|
N~Hope the visitors are handled carefully. Rare still means living.|
S~It must be exciting to arrive without knowing what someone will bring that day.|
S~That sounds like work that rewards patience as much as excitement.|
S~Their ordinary working day includes somebody else's extraordinary discovery.|
S~A room where strange arrivals are expected. Rather welcoming, in its own way.|
S~New observations every day! I would need so many notebooks.|
S~People carry their mysteries here and ask for names.|
N~An interesting place to work, especially if the team shares what it learns.|
S~I would love to hear which recent visitor surprised them most.
''')
add('lab_eevee', 'CinnabarIsland_PokemonLab_ResearchRoom_Text_EeveeCanEvolveIntroThreeMons',
    'A lab scientist describes three possible Eevee evolutions.', '''
U~One small Pokemon, three very different futures. That is a busy decision.|
N~Eevee is unusually responsive to different evolutionary conditions.|
N~Worth thinking about the partner and the team before choosing a direction.|
S~Three possibilities can be exciting and a little daunting.|
S~There is time to get to know Eevee before making a big decision.|
S~A single beginning offers a remarkably generous selection of next chapters.|
S~A creature with several possible silhouettes. I understand the fascination.|
S~One starting point, multiple outcomes. No wonder researchers find Eevee interesting.|
S~Several futures curled inside the same small body.|
S~It is easy to imagine each version. Harder to choose just one.|
S~I wonder which possibility the researcher finds most interesting.
''')
add('lab_fossil_found', 'CinnabarIsland_PokemonLab_Lounge_Text_FoundFossilInMtMoon',
    'A visitor believes a Mt. Moon fossil belonged to a rare prehistoric Pokemon.', '''
U~A piece of mountain that used to be somebody. That is quite a find.|
S~The identification is tentative, but a well-preserved fossil could offer valuable evidence.|
N~Handle it carefully. One careless bump could ruin a remarkable find.|
S~Their excitement is quiet, but you can hear how much the discovery matters.|
S~Good that they brought it somewhere people can examine it properly.|
S~Mt. Moon has surrendered a very old character from a very incomplete story.|
S~Something ancient survived long enough for someone to be delighted by it.|
U~A natural record preserved inside the rock! I would be staring too.|
S~The mountain kept a shape the living world forgot.|
S~Calling it remarkable before being certain what it is feels rather honest.|
S~I wonder what first caught their eye among all the ordinary stone.
''')
add('fossil_wait', 'CinnabarIsland_PokemonLab_ExperimentRoom_Text_TakesTimeGoForWalk',
    'The fossil scientist asks us to wait while resurrection is in progress.', '''
U~Bringing back ancient life takes a little while. Apparently we should stretch our legs.|
S~An extraordinary process still needs time. We should let the researcher work.|
N~No point hovering. We can come back when the work is ready.|
N~Waiting feels strange when the thing you are waiting for is so enormous.|
S~A short walk is better than crowding somebody doing delicate work.|
U~The ancient world is being restored; meanwhile, we have been assigned a stroll.|
S~Something absent for so long can keep us waiting a little longer.|
N~Important work in progress. Resist the urge to ask every ten seconds.|
S~A very old silence is taking its time becoming a heartbeat.|
N~The doctor is brisk, but at least the instruction is clear.|
N~I wonder how the lab sounds when the machine begins its work.
''')
add('fossil_return', 'CinnabarIsland_PokemonLab_ExperimentRoom_Text_YouComeAgain',
    'The fossil scientist invites another visit after a refusal or completed fossil work.', '''
S~The invitation survived the very abrupt delivery. We can come back.|
N~That leaves the conversation open without requiring another decision now.|
N~We are done here for now. He knows where to find us: eventually, back here.|
S~A short goodbye. I think he means it kindly.|
S~We can leave him to his research and return when we have a reason.|
M~A farewell stripped to its essential instruction: make another entrance someday.|
S~A door left open in very few words.|
N~Brief, reusable, difficult to misinterpret. Efficient farewell.|
S~He sends us away without quite closing the door.|
N~He does not waste syllables on goodbyes, does he?|
N~He seems more comfortable with another visit than a long conversation.
''')
add('warden_teeth_local', 'FuchsiaCity_House1_Text_WardenIsOldHasFalseTeeth',
    'A local describes the active Safari Warden and mentions his false teeth.', '''
M~Apparently the Warden has more energy than his original teeth had staying power.|
N~Dental replacements tell us little about someone's ability to manage a reserve.|
N~He is still active. That is the part that matters for his work.|
N~An oddly personal detail to offer a visitor.|
S~Staying busy doing something you care about sounds good at any age.|
M~A professional biography with a sudden detour into dentistry.|
N~He has outlasted his teeth. There is a certain stubborn dignity in that.|
N~Replacement parts, continued operation. Nothing wrong with that.|
S~An old keeper, still making his rounds. Teeth are a separate matter.|
N~She could have stopped at active. Town gossip rarely knows where to stop.|
N~People here certainly know the Warden's everyday details.
''')
add('bill_grandfather', 'FuchsiaCity_House1_Text_BillIsMyGrandson',
    'Bill\'s grandfather recalls that Bill collected things as a child.', '''
S~The impressive grown-up was once a kid bringing more things home. That tracks.|
S~A childhood interest persisted and became much more organized over time.|
S~Sounds like his family saw the beginnings long before anyone else did.|
S~His grandfather sounds pleased that we know him.|
S~I like hearing the small beginning behind somebody's big reputation.|
S~A famous name briefly becomes somebody's grandson with an overfull collection.|
S~It is nice when a person's old strangeness becomes something their family treasures.|
S~Early collecting habits scaled up impressively. I sympathize with the storage problem.|
S~A child kept things. Years later, people kept his name in mind.|
S~There is pride in the way he says grandson. Very little disguise on it.|
S~I wonder what Bill collected before Pokemon took over his attention.
''')
add('bill_data', 'FuchsiaCity_House1_Text_BillFilesHisOwnMonData',
    'A child admires Bill recording his Pokemon data on his own PC.', '''
S~Collecting the facts as well as the Pokemon. That is a second collection hiding inside the first.|
S~Personal records can preserve observations that broad references overlook.|
N~Keeping track makes it easier to care for what you have.|
S~The boy sounds impressed by the care behind the collection.|
N~A record is only useful if somebody takes the time to maintain it.|
S~Bill seems unwilling to let an interesting detail escape without being filed.|
S~An orderly place for all the little things someone else might forget.|
S~A personal database! Now I want to know how he organizes the entries.|
N~A machine full of carefully kept little traces of living things.|
S~The child noticed the work, not just the impressive collection. Good eye.|
S~I wonder whether Bill showed him how the system works.
''')
add('good_rod', 'FuchsiaCity_House2_Text_GoodRodCanCatchBetterMons',
    'After giving the Good Rod, the fishing guru\'s brother explains its broader catches.', '''
S~A better rod and a speech about poetry. Fishing comes with a surprisingly full service.|
S~Different equipment changes the range of Pokemon we might encounter.|
S~Better tool, more options. Still need patience.|
S~He shared something he loves instead of just telling us to try it.|
S~That was generous. We can make good use of it without matching his enthusiasm immediately.|
M~He has equipped a new disciple and delivered the opening verse.|
S~He finds poetry in waiting beside water. I can respect that.|
S~A practical upgrade, personally endorsed by somebody gloriously biased.|
S~A line can reach a little farther into the unknown now.|
S~He calls it a way of life and actually gives people a way to begin.|
S~I wonder what catch made him love fishing this much.
''')
add('fishing_refused', 'FuchsiaCity_House2_Text_OhThatsDisappointing',
    'The fishing enthusiast is disappointed that we do not share his interest.', '''
N~We have gently punctured a very fish-shaped dream.|
N~Shared enthusiasm would please him, but it cannot be assumed.|
N~He asked. We answered. No need to pretend.|
F~It is hard to disappoint someone who was so ready to be excited.|
N~He will find another person eager to talk rods and water.|
M~The proposed fishing fellowship has met a polite administrative obstacle.|
N~Not every visitor is a future fishing companion. A small, survivable tragedy.|
N~Enthusiasm is not universal. An unfortunate constraint on recruiting hobbyists.|
N~The water can keep its invitation for another person.|
N~He took that personally, but at least he accepted the answer.|
N~I wonder how many conversations here begin and end with fishing.
''')
add('fish_biting', 'FuchsiaCity_House2_Text_HowAreTheFishBiting',
    'The fishing enthusiast greets us by name and asks about our catches.', '''
S~He remembers us! We have become part of the fishing report.|
S~He is following up on an interest he helped us explore.|
S~Nice that he remembers who he gave the rod to.|
S~A familiar greeting makes coming back feel easier.|
S~That sounds like a real invitation to stay and compare stories.|
S~We return as acquaintances, expected to bring news from the water.|
S~His world has room for one more person and their small fishing failures.|
S~A follow-up question after handing over equipment. Good support!|
S~The river has become a reason for him to remember our name.|
S~He made the greeting personal. That is how a hobby becomes company.|
S~I suspect he enjoys hearing about a catch almost as much as making one.
''')
add('safari_souvenirs', 'FuchsiaCity_Mart_Text_DontTheyHaveSafariZonePennants',
    'A shopper wants Safari Zone pennants, lanterns, or calendars.', '''
M~They have assembled a complete souvenir wish list and found none of it.|
N~There seems to be unmet demand for merchandise beyond practical trainer supplies.|
M~A calendar seems harmless. Better than trying to take a whole fence sign home.|
S~They want a little reminder of the place. I understand that.|
S~A local keepsake would make a nice gift for somebody who could not come.|
M~The reserve has inspired a merchandising vision this shop cannot fulfill.|
S~They want to carry the memory home in paper rather than a ball.|
U~Clear demand, three product ideas, zero stock. Someone is missing a market!|
S~A paper lantern can hold a place in someone's memory surprisingly well.|
S~They even offered alternatives. That is a committed souvenir shopper.|
S~I wonder which scene they would want on the calendar.
''')
add('x_speed', 'FuchsiaCity_Mart_Text_DidYouTryXSpeed',
    'A shopper recommends X Speed for raising Speed in battle.', '''
M~A whole bottle of hurry. Useful, provided we know when to open it.|
N~A temporary Speed increase can change which combatant acts first.|
N~Useful if getting the first move changes the fight.|
N~They sound pleased to have found something that worked for them.|
N~Good to know what the bottle does before a hurried battle decision.|
M~The shop offers haste in conveniently portable form.|
N~Speed, briefly borrowed from a bottle. A peculiar little advantage.|
N~Changing action order can change the whole plan. Small item, big timing effect.|
N~A moment can matter more than a great deal of force.|
N~A clear recommendation. Refreshing after the shelves of vague promises.|
N~I wonder which battle made them start recommending it to strangers.
''')
add('balanced_team', 'FuchsiaCity_PokemonCenter_1F_Text_CantBecomeGoodTrainerWithOneMon',
    'A trainer warns against relying on one strong Pokemon while admitting balanced training is hard.', '''
N~One hero cannot carry the whole picnic forever. Especially if the picnic fights back.|
N~Distributing training reduces dependence on a single partner, though it takes more time.|
N~One exhausted partner is a weak backup plan. Share the work.|
N~I appreciate that they admitted the difficult part instead of making it sound easy.|
N~Everybody needs a turn and a rest. Keeping that balance takes attention.|
N~An ensemble demands more rehearsal than a solo act, and survives more surprises.|
N~Depending on one strong partner puts a quiet weight on that partner.|
N~A system with one point of failure needs better backup. Training is the costly part.|
N~Let more than one set of shoulders learn the weight.|
N~Sound advice, made better by admitting the effort it asks for.|
N~I wonder whether they learned this after their strongest partner had a bad day.
''')
add('league_path', 'FuchsiaCity_PokemonCenter_1F_Text_PokemonLeagueWestOfViridian',
    'A visitor describes the League headquarters reached west of Viridian.', '''
N~A narrow trail to the people overseeing all those trainers. Busy little path.|
N~Useful geographic information. The League's headquarters lie west of Viridian.|
N~Worth knowing where it is before we need to make the trip.|
N~A place that important begins with an ordinary trail. That feels strange.|
N~That sounds like a journey to plan carefully, with supplies and time.|
N~A modest turning in Viridian leads toward an institution with a very large reach.|
N~A narrow path can carry a remarkable amount of ambition.|
N~Regional headquarters at the end of a trail. Memorable navigation advice.|
N~A small way west, then a great many expectations.|
N~A useful direction from someone who assumes visitors may be aiming high.|
N~I wonder how many travelers pass Viridian without noticing that trail.
''')
add('safari_pokedex', 'FuchsiaCity_PokemonCenter_1F_Text_VisitSafariZoneForPokedex',
    'A visitor recommends the Safari Zone to Pokedex collectors for rare Pokemon.', '''
S~A place full of new faces. Some may be better at leaving than introducing themselves.|
S~A reserve with varied species could fill important gaps in a field record.|
N~Prepare before going in. Rare sightings do not guarantee easy catches.|
S~Even seeing something unfamiliar would make the trip interesting.|
S~A good lead for the Pokedex. Bring patience along with the fee.|
S~The local reserve offers an unusually lively appendix to our travels.|
S~A place to meet creatures the roads have not introduced us to yet.|
S~A concentrated observation opportunity! Worth keeping careful notes.|
S~Some names wait behind the reserve's gates rather than along the road.|
N~A recommendation tailored to what we might be trying to do. Helpful.|
S~I wonder which zone gives visitors their most surprising first encounter.
''')
add('warden_nickname', 'FuchsiaCity_SafariZone_Office_Text_NicknamedWardenSlowpoke',
    'An employee says staff call the Warden Slowpoke because of his vacant expression.', '''
N~I wonder whether the Warden approved this very detailed performance review.|
N~An expression is a poor measure of what someone is thinking.|
N~A blank look does not mean an empty head.|
N~I hope he finds the nickname as funny as they do.|
N~Being familiar with somebody is not always the same as being kind to them.|
M~The office has established a nickname on the strength of one facial expression.|
N~Some of us look vacant while doing perfectly adequate worrying.|
N~External display does not always show internal activity. Machines taught me that.|
N~Quiet faces can conceal very busy weather.|
N~A nickname works better when the person wearing it gets a say.|
N~I wonder what the Warden calls the people in this office.
''')
add('warden_knowledge', 'FuchsiaCity_SafariZone_Office_Text_WardenIsVeryKnowledgeable',
    'An employee praises the Warden\'s Pokemon knowledge and fossil collection.', '''
S~A head full of Pokemon facts and a shelf full of ancient ones. Good combination.|
S~His collection may reflect decades of sustained interest and careful study.|
S~Experience and actual knowledge. Good qualities for the person running the place.|
S~It is nice to hear someone recognize what he knows.|
S~He must have plenty of stories behind those fossils.|
S~The office nickname conceals a rather distinguished natural historian.|
S~He keeps company with living creatures and traces of the vanished ones.|
S~Fossils and field experience! I would have several questions ready.|
S~Someone tending the living has kept room for the long absent.|
S~That tells us much more about him than his expression does.|
S~I wonder whether his rare fossils came from his own journeys.
''')
add('warden_speech', 'FuchsiaCity_SafariZone_Office_Text_CouldntUnderstandWarden',
    'An employee could not understand the Warden when he visited the office.', '''
N~That sounds frustrating for him too. Words get heavy when they will not come out right.|
N~Difficulty producing clear speech does not imply difficulty understanding the situation.|
N~Give him time. He is still trying to tell them something.|
D~It is awful when people stop listening because the words are difficult.|
N~They could try writing things down together instead of guessing at him.|
N~A failed conversation has become gossip. I would rather hear whether anyone helped.|
N~Being misunderstood in your own workplace sounds quietly miserable.|
N~If one way of communicating fails, try another. Paper is not complicated equipment.|
N~A message can be trapped at the very edge of being heard.|
N~I hope they offered patience before giving the problem a name.|
N~I wonder what he was trying so hard to tell them.
''')
add('warden_prize', 'FuchsiaCity_SafariZone_Office_Text_PrizeInSafariZone',
    'An employee describes a prize for reaching the Safari Zone\'s farthest corner.', '''
U~A prize for getting thoroughly lost in the correct direction. Tempting.|
N~We should study the layout before committing limited time to the farthest section.|
N~Plan the route. Getting there means little if we waste the whole visit wandering.|
S~A little goal might make exploring feel less aimless.|
N~We can explore at a steady pace and see how far we get.|
M~The Warden has placed convenience at a deliberately inconvenient distance.|
S~A useful prize waiting in the farthest quiet corner. A good lure.|
S~A navigation challenge with a practical reward! I am listening.|
S~The far corner has a reason for us to find it.|
N~They have made the promotion sound mysterious enough to work.|
S~I wonder how many visitors find the prize by accident.
''')
add('copycat_mimic', 'SaffronCity_CopycatsHouse_2F_Text_MimickingFavoriteHobbyMale SaffronCity_CopycatsHouse_2F_Text_MimickingFavoriteHobbyFemale',
    'Copycat imitates our side of the conversation and calls mimicry her favorite hobby.', '''
U~For a moment, there were twice as many of us and neither knew what to say.|
N~Accurate imitation requires careful observation. The conversational confusion is substantial.|
N~Clever trick. Still unsettling when somebody borrows your voice without warning.|
F~Hearing your own hesitation from someone else is rather embarrassing.|
M~She managed both sides of that exchange without needing much help.|
M~An ambitious performance in which our role was taken from us mid-sentence.|
M~I am relieved she has not discovered how little I say. Easy material to steal.|
U~Fast turnaround on voice replication! Social consequences still under development.|
N~An echo that lives in a house and enjoys itself.|
M~She notices people closely. A little warning would improve the presentation.|
U~I wonder how many tiny habits she picked up before we even spoke.
''')
# Trainer rows bind post-battle follow-up text only. Native trainer dispatcher
# reachability must be checked separately from the existence of these labels.
add('r13_sebastian', 'Route13_Text_SebastianPostBattle',
    'Sebastian notices his birds are happy despite losing.', '''
S~The birds enjoyed themselves. Their scoreboard may be entirely different from ours.|
S~Their behavior matters more than assuming defeat made them unhappy.|
S~Good. They worked hard and still had a decent time.|
S~He noticed how they felt before worrying about the result.|
S~A happy team after a loss is a good thing to bring home.|
S~The trainer lost the match; the birds appear to have enjoyed the outing.|
S~They have refused to make a tragedy of the afternoon. Sensible birds.|
S~Actual feedback from the team beats guessing from a win-loss record.|
S~Feathers do not have to droop just because the battle ended badly.|
S~He is reading his Pokemon instead of just the result. Good instinct.|
S~I like that he stopped to look at them and noticed their mood.
''')
add('r13_susie', 'Route13_Text_SusiePostBattle',
    'Susie promises to train hard and become a good trainer.', '''
S~She has already turned the loss into tomorrow's plan. Quick work.|
S~Deliberate practice will help more than effort without direction.|
S~Good resolve. Rest the team before putting it to work again.|
S~She sounds determined without trying to pretend the loss did not happen.|
S~A good trainer keeps learning and looks after the partners doing the work.|
S~A declaration delivered to the nearest available witness. I believe her.|
S~A little stubbornness can keep a bad afternoon from becoming an ending.|
S~That is energy she can use. A clear training goal would give it direction.|
S~She has planted the next attempt right inside this defeat.|
S~She wants us to remember this. There is some real fire behind it.|
S~I would be curious to see what changes when she tries again.
''')
add('r13_valerie', 'Route13_Text_ValeriePostBattle',
    'Valerie recognizes that our badges came from Gym Leaders.', '''
M~The badges have been successfully identified as badges. Investigation complete.|
S~She recognizes what the badges represent, even if the explanation is familiar.|
N~We earned them with the team. They are more than something shiny to wear.|
S~She sounds delighted to have worked it out herself.|
S~They carry a lot of effort for such small things.|
M~Our credentials have passed a very enthusiastic visual inspection.|
S~A tiny metal object can make a long struggle look deceptively neat.|
M~Correct origin identified. I award her an imaginary badge for badge analysis.|
S~Little marks of places where we stayed and tried.|
S~Her excitement is sweet. A badge does make a good conversation starter.|
S~I wonder which Gym Leader she would most like to challenge.
''')
add('r13_gwen', 'Route13_Text_GwenPostBattle',
    'Gwen says Pokemon need battle experience to become tougher.', '''
N~Practice helps. So does knowing when everybody has had enough practice.|
N~Experience can improve performance when the challenge is appropriate and recovery is adequate.|
N~Train them. Do not grind them down. There is a difference.|
N~Learning through battles makes sense when the partners are ready for them.|
N~Hard work needs proper rest on either side of it.|
N~A reasonable principle, provided toughness is not measured by how much hurt one ignores.|
N~Growing stronger should leave a creature with more than just new bruises.|
N~Repeated testing helps if you learn from the results and allow repairs.|
N~A living thing can harden without being treated like stone.|
N~Good training takes judgment, not just more battles on the schedule.|
N~I wonder how she decides her Pokemon have had a good day's practice.
''')
add('r13_alma', 'Route13_Text_AlmaPostBattle',
    'Alma says the Carbos she found increased her Pokemon\'s Speed.', '''
S~A cave trip made her Pokemon quicker. My cave trips mostly make my socks wetter.|
N~She put the find to use and observed a change in Speed.|
N~Useful find. Good that it suited something her team needed.|
S~She sounds pleased that exploring helped her partner.|
S~Always satisfying when a lucky discovery becomes something practical.|
M~The expedition yielded a measurable improvement rather than merely an impressive story.|
S~A small bottle from a dark place changed the pace of her journey.|
S~Exploration, useful material, observable result. Excellent little chain of events.|
S~The cave held a little hurry in reserve.|
S~She knows where it came from and what it did. A well-remembered find.|
S~I wonder whether finding it made her more eager to explore other caves.
''')
add('r13_perry', 'Route13_Text_PerryPostBattle',
    'Perry is tired after losing and decides to fly home.', '''
S~He has chosen the skyward route to a quiet evening. Good exit.|
N~Ending the outing while tired is a reasonable decision.|
N~Heading home beats pushing an exhausted team another mile.|
S~It sounds like he knows when to call it a day.|
S~Home and a proper rest seem like a good next plan.|
S~A defeat followed by a practical and admirably swift departure.|
S~Some afternoons are best folded away before they get any longer.|
N~Return route selected. Now make sure the bird is rested enough for the trip.|
S~There is a particular comfort in seeing home from above.|
S~A graceful exit does not have to pretend the day went well.|
S~I wonder whether flying home is his favorite part of an outing.
''')
add('r13_lola', 'Route13_Text_LolaPostBattle',
    'Lola wonders whether male or female Pokemon are stronger.', '''
N~I would start by asking the actual Pokemon, rather than appointing a winning half.|
N~A broad comparison conceals species, training, individual traits, and match conditions.|
N~Judge the partner in front of you. That question is too broad.|
N~It seems unfair to decide what someone can do before meeting them.|
N~Training and care tell us much more about this team than that guess does.|
N~A sweeping debate has arrived to distract us from one quite specific loss.|
N~An entire category of Pokemon need not answer for this afternoon.|
N~Too many uncontrolled variables. Also, several potential bites.|
N~Living things rarely fit neatly into the boxes we make for them.|
N~That is a very large conclusion to try to draw from one battle.|
N~I would rather hear what surprised her about the particular opponents she faced.
''')
add('r13_sheila', 'Route13_Text_SheilaPostBattle',
    'Sheila admits choosing her team for looks and knowing little about Pokemon.', '''
S~Looks got her interested. Now she has a whole team of reasons to learn more.|
N~Visual preference can begin an interest; understanding their needs should follow.|
N~Fine place to start. Learn what those partners can actually do.|
S~Admitting what she does not know takes a little courage.|
S~Liking them is a beginning. Caring well for them is the next part.|
S~The cast was chosen for appearance. Now comes the rewarding work of knowing them.|
S~Beauty opened the door. I hope curiosity gets a room too.|
N~She has identified the knowledge gap. That is a workable starting point.|
S~A pretty surface can invite you toward a much stranger interior.|
S~Style caught her eye. Personality might be what makes her stay.|
S~I wonder which one first made her stop and look.
''')
add('r13_jared', 'Route13_Text_JaredPostBattle',
    'Jared angrily tells us to leave after losing.', '''
N~That sounds like our invitation to be somewhere else.|
N~He has made his preference for ending the conversation sufficiently clear.|
N~We are leaving. No need to give him another excuse.|
N~I would rather let the conversation stop there.|
N~A little distance seems good for everybody now.|
N~A brief review of our presence, with no invitation for revisions.|
N~An economical farewell. Rather lacking in charm.|
N~Signal received, aggressively. Exit seems straightforward.|
N~Some doors close themselves quite loudly.|
N~He could have managed that with fewer sharp edges. We can go.|
N~That is not a conversation likely to improve by staying.
''')
add('r13_robert', 'Route13_Text_RobertPostBattle',
    'Robert wishes he could fly like Pidgey and Pidgeotto.', '''
S~The birds make it look unfairly easy. My arms have received the complaint.|
S~Watching flight can make its mechanical difficulty feel almost insulting.|
S~A fair wish on a road this long.|
S~I understand wanting that feeling, even for a little while.|
S~A cool breeze and no tired feet. There is plenty to like in that idea.|
S~An old human ambition, renewed by two birds doing it without ceremony.|
S~To leave the ground without asking anything to carry you. Yes, I understand.|
S~Wings solve a very tempting transport problem. Shame about the weight requirements.|
S~The sky looks nearer when something small can reach it.|
S~He admires them for something beyond winning battles. I like that.|
S~I wonder whether he watches them fly even when they are just playing.
''')
add('r14_carter', 'Route14_Text_CarterPostBattle',
    'Carter warns that HM moves cannot be forgotten easily.', '''
N~A useful move can be a stubborn houseguest. Good to know before inviting it in.|
N~The difficulty of removing an HM move makes the initial choice consequential.|
N~Think before teaching it. Useful does not mean easy to replace.|
N~That is the sort of detail I would rather hear before choosing.|
N~A long-term choice deserves a little time, even when the move helps immediately.|
N~A lesson with unusually persistent attendance. Read the commitment before enrolling.|
N~Some knowledge lingers past the moment we wanted it. This kind quite literally.|
N~A hard-to-reverse configuration change. Plan the slot first.|
N~A useful thing can still take root where you did not mean it to stay.|
N~Important advice, though he could have led with it before the battle.|
N~I wonder how many trainers learn that rule only after trying to change a move.
''')
add('r14_mitch', 'Route14_Text_MitchPostBattle',
    'Mitch thinks his birds need a better selection of moves.', '''
S~He has found something to work on besides being cross with the birds. Good.|
S~Reviewing move selection is a more specific response than simply demanding more strength.|
S~Give them better options. That is something he can actually help with.|
S~He sounds disappointed, but he is looking for a way forward.|
S~A thoughtful change may help more than another exhausting practice session.|
S~The post-match review has produced an actionable note for once.|
S~The wings are fine. Perhaps the plan needs a different shape.|
S~Check the available tools before blaming the operator. Sensible revision.|
S~A bird can have more than one answer to trouble.|
N~He is thinking about what to change. Hopefully he gives the birds some credit too.|
S~I wonder which part of the battle made the missing option clear.
''')
add('r14_beck', 'Route14_Text_BeckPostBattle',
    'Beck recommends moves matching the Pokemon\'s type for added power.', '''
S~A move that feels at home gets a little extra bite. Useful.|
N~Type affinity can improve a move's power. An important factor in selecting attacks.|
N~Work with the partner's strengths. Good starting point.|
N~That is a clear bit of advice to take from the battle.|
N~It helps to know which tools a partner already handles especially well.|
N~Sometimes the natural choice has a measurable advantage behind its elegance.|
S~A small reward for doing what comes naturally.|
N~Compatibility affects output. Always worth checking before optimizing the rest.|
N~Some actions sit more comfortably in a creature's bones.|
N~A useful rule, and simple enough to remember under pressure.|
N~I wonder who first explained that trick to him.
''')
add('r14_marlon', 'Route14_Text_MarlonPostBattle',
    'Marlon says he only wants to raise bird Pokemon.', '''
S~He found his people. His people happen to have feathers.|
S~A narrow focus can produce deep knowledge of a particular group.|
N~His choice. Best learn their weaknesses as well as the things he loves.|
S~It is nice to hear someone so certain about what makes them happy.|
S~A team you enjoy caring for is a good reason to keep learning.|
S~An exclusive devotion, declared with absolutely no room for a non-winged understudy.|
S~The world has many creatures. He knows which ones call him outside.|
N~Specialization has benefits. A contingency plan still belongs in the kit.|
S~Some people look up and find their whole answer there.|
S~There is a difference between chasing a trend and knowing your own taste.|
S~I wonder which bird made him decide this was his kind of team.
''')
add('r14_donald', 'Route14_Text_DonaldPostBattle',
    'Donald names Articuno, Zapdos, and Moltres as the three winged mirages.', '''
U~Three legendary birds. The sky has a very impressive guest list.|
N~He can name the three legendary birds, though that does not establish their whereabouts.|
N~Names are a start. Legends still deserve a careful approach.|
S~The names make them feel a little more real than a vague story.|
N~Interesting tale. We can keep listening without running after every rumor.|
S~The winged mirages have acquired names, which only sharpens the mystery.|
S~Three names that sound like weather people learned to whisper about.|
U~Three distinct legendary birds! I would love to compare reliable observations.|
S~Ice, lightning, flame. The sky keeps a varied household.|
S~That is a much better explanation than just saying winged mirages.|
S~I wonder how far those stories have traveled from their first witnesses.
''')
add('r14_benny', 'Route14_Text_BennyPostBattle',
    'Benny says winning and losing are insignificant beneath the huge sky.', '''
M~The sky has declined to keep score. Honestly, very considerate of it.|
N~A wider frame can make a single result feel less consequential.|
N~Fair enough. Still thank the team for the work.|
S~Looking up can make a bad moment feel less crowded.|
S~A little perspective after a hard match is no bad thing.|
M~An immense celestial backdrop has been summoned for the post-match commentary.|
S~The sky remains entirely unimpressed by both our records. Comforting.|
N~Scale does change how a problem feels. Does not change the need to patch up afterward.|
S~Above us, something vast is getting on with the afternoon.|
N~A graceful thought, provided he remembers other people cared about the battle.|
S~I wonder whether he felt that way before losing too.
''')
add('r14_lukas', 'Route14_Text_LukasPostBattle',
    'Lukas impatiently asks why we are still talking to him.', '''
N~He has enough whats for three conversations and wants none of them.|
N~The repeated question suggests irritation rather than a request for detail.|
N~Nothing else we need here. We can move on.|
N~I do not think another answer would make this less awkward.|
N~Best leave him a little room to cool down.|
M~His vocabulary has narrowed while his volume remains ambitious.|
N~A conversation stumbling over the same stone three times. We can leave.|
N~Repeated warning signal. No extra troubleshooting needed.|
N~The air around him has become rather prickly.|
N~He is not in a listening mood. We do not need to stay.|
N~He seems more upset that we remained than curious about what we want.
''')
add('r14_isaac', 'Route14_Text_IsaacPostBattle',
    'Isaac complains that raising Pokemon is a drag.', '''
N~The Pokemon may also have notes about their working conditions.|
N~Enjoying battle does not necessarily mean enjoying the sustained care training requires.|
N~They depend on him. Boredom is no excuse to neglect them.|
N~I hope he finds something about them that makes the effort feel worthwhile.|
N~Caring for a team takes work. They still need him to show up.|
N~He enjoys the premise and objects to the responsibilities in the fine print.|
N~Living creatures are inconveniently unable to become hobbies only when we feel like it.|
N~Ongoing maintenance is part of ownership. He cannot skip the whole section.|
N~A companion is still there when the novelty goes quiet.|
N~That is a rough thing to say while the team is standing nearby.|
N~I wonder what made him want Pokemon before the daily work set in.
''')
add('r14_gerald', 'Route14_Text_GeraldPostBattle',
    'Gerald praises our strong Pokemon and declares might makes right.', '''
N~Strong Pokemon, yes. A complete philosophy of justice, probably no.|
N~Strength establishes capability. It does not establish whether a choice is justified.|
N~Power tells you what you can do. Still have to choose well.|
N~I am glad he respects the team. The rest makes me uneasy.|
N~Being strong gives you more ways to help, too.|
N~A compliment has wandered into a rather alarming political doctrine.|
N~The biggest creature in a room does not automatically have the best idea.|
N~Force solves some problems and creates plenty. It is not a universal tool.|
N~A heavy hand can still point the wrong way.|
N~He can admire the team without making every argument a contest of muscle.|
N~I wonder how that rule sounds to him when someone stronger disagrees.
''')
add('r14_malik', 'Route14_Text_MalikPostBattle',
    'Malik threatens that he could beat us in a personal fight.', '''
N~He has proposed changing the entire sport until the result suits him. We can decline.|
N~That threat is unrelated to the Pokemon battle and does not warrant engagement.|
A~Stay close. We are leaving him right here.|
N~That stopped sounding like a game. I would rather go.|
A~No reason to let his embarrassment become somebody else's injury.|
N~The defeated competitor has requested a new contest with markedly worse manners.|
N~His pride would like to borrow our bruises. It can remain disappointed.|
N~Unacceptable rule change. Best end the interaction.|
N~Some people try to make their hurt into someone else's. Keep walking.|
A~Losing did not grant him permission to threaten us.|
N~He seems much more interested in recovering his pride than having a conversation.
''')
add('r14_kiri', 'Route14_Text_KiriPostBattle',
    'Kiri worries that the double-battle loss was her fault.', '''
S~Two people shared that battle. One person does not have to carry all the sad bits.|
N~A team result has several causes. Assigning all responsibility to herself is premature.|
S~She tried. That matters more than finding someone to blame.|
D~I know how quickly a loss can start sounding like proof against yourself.|
S~She needs a kind word before she needs a detailed battle review.|
S~A shared defeat need not end with one partner appointed its sole author.|
S~The mind can make a single loss unreasonably personal. I know the trick.|
N~One result is not enough to isolate a cause. Especially with two trainers involved.|
S~Two shadows crossed the field. One need not hold all the darkness afterward.|
S~She is looking for blame when her partner might simply want another try together.|
S~I hope she looks at Jan before deciding what Jan thinks.
''')
add('r14_jan', 'Route14_Text_JanPostBattle',
    'Jan comforts Kiri and proposes trying harder together next time.', '''
S~She kept the important part of the team standing: the part between them.|
S~Reassuring a partner preserves the cooperation they will need for improvement.|
S~Good response. Nobody learns much while being blamed for everything.|
S~She noticed Kiri needed her more than the result needed explaining.|
S~A next time together is a good thing to offer someone who feels awful.|
S~The match ended badly; the partnership received a rather better ending.|
S~A loss can leave room for an unexpectedly good friend to speak.|
S~Team morale repaired before the next round of practice. Excellent priorities.|
S~She is keeping a small light on for the next attempt.|
S~A generous response, with no audience needed to make it count.|
S~That tells us more about their partnership than the battle did.
''')
add('r17_raul', 'Route17_Text_RaulPostBattle',
    'Raul recommends collecting and selling things found on Cycling Road.', '''
M~Roadside treasure hunting. Mind the part where a bicycle tries to become the treasure.|
N~Recovering discarded useful items can be worthwhile if the road remains safe.|
N~Watch the traffic before watching the ground.|
N~It must take a patient eye to notice things while everyone else rushes past.|
N~Useful finds are nice. Stepping into a rider's path would spoil the profit.|
M~Cycling Road supports an unexpected salvage economy.|
N~A living made from what hurried people fail to notice.|
N~Recover, inspect, reuse. Sensible, provided the item is not someone's missing possession.|
N~The road sheds little things as people travel through it.|
N~A sharp eye can find value. It should also recognize something recently lost.|
N~I wonder what the strangest useful thing he has found here was.
''')
add('r17_isaiah', 'Route17_Text_IsaiahPostBattle',
    'Isaiah threatens to belly-bump us away after losing.', '''
N~An unusual threat. Still a threat, even with that much wobble in the wording.|
N~Physical intimidation is not an appropriate extension of a lost battle.|
A~No. Keep your hands and everything else to yourself.|
N~That is enough of this conversation for me.|
N~He can be disappointed without trying to knock people over.|
M~An undignified tactic has been announced with considerable confidence.|
N~I prefer my personal space without an incoming stomach.|
N~Collision testing is neither requested nor necessary. Let's move on.|
N~His pride seems to be looking for somewhere to land. We can step away.|
A~He has confused taking up space with being entitled to ours.|
N~That sounds like an excellent reason to give him a wide berth.
''')
add('r17_virgil', 'Route17_Text_VirgilPostBattle',
    'Virgil enthusiastically describes racing downhill.', '''
S~Downhill does half the pedaling and all the tempting. Keep a hand on the brakes.|
N~Gravity supplies acceleration; steering and braking remain the rider's responsibilities.|
N~Enjoy the slope. Leave yourself enough room to stop.|
S~He sounds happiest when he is moving. I understand the appeal.|
S~A breeze after a hard climb must feel earned.|
S~A whole hill conspires to make his favorite pastime more dramatic.|
S~The road lends you speed and expects you to return it carefully.|
S~Free acceleration! With a very important braking system attached.|
S~For a moment, the hill does the work and the wind takes the credit.|
S~There is a particular joy in a road that finally tilts your way.|
S~I wonder whether he has a favorite stretch of the descent.
''')
add('r17_billy', 'Route17_Text_BillyPostBattle',
    'Billy asks whether we are looking for adventure.', '''
M~Adventure keeps finding us before we finish looking for a bench.|
N~That depends on what sort of adventure he has in mind. Details matter.|
N~Depends. A good road is enough without someone manufacturing trouble.|
S~I like a little uncertainty, when there is still time to get home safely.|
S~An interesting route and decent company already count for quite a lot.|
M~A broad invitation from a man beside a very long slope. Clarification advised.|
N~Adventure is a lovely word until it starts explaining the bruises.|
S~Possibly! I would like to see the plan before committing the equipment.|
S~Sometimes the next bend offers enough strangeness for one afternoon.|
M~He has the opening line. I am waiting for the actual proposal.|
S~I wonder what he considers an adventure on a road he knows so well.
''')
add('r17_nikolas', 'Route17_Text_NikolasPostBattle',
    'Nikolas says he caught Voltorb in the abandoned Power Plant.', '''
U~An abandoned Power Plant still had somebody at work. Round somebody.|
N~An old electrical facility is a plausible habitat for Voltorb.|
N~Useful lead. Abandoned does not mean safe to wander through.|
N~That must have been an unsettling place to hear something moving.|
N~I hope he was careful around whatever equipment remained inside.|
S~The building retired from one purpose and acquired a rather lively tenant.|
S~A little life in a place people left behind. With a dangerous temper, perhaps.|
U~An electrical Pokemon in a Power Plant! The old equipment may still matter to it.|
N~Some buildings keep a pulse after their workers leave.|
N~A memorable place to meet a partner. Also a place to watch your step.|
S~I wonder what first gave away that the round thing was a Pokemon.
''')
add('r17_zeek', 'Route17_Text_ZeekPostBattle',
    'Zeek wonders whether some Pokemon need elemental stones to evolve.', '''
S~Some Pokemon apparently want a very specific rock before making a big decision.|
N~Evolutionary triggers vary. Stones are relevant to some species, not a universal solution.|
N~Check the species before buying a pocket full of expensive rocks.|
N~It is worth asking before assuming every partner changes the same way.|
N~A little research can save a lot of confused waiting.|
M~The next stage of life may have a mineral requirement. Biology remains delightfully inconvenient.|
S~A stone can look very ordinary until it belongs beside the right creature.|
S~An external trigger! The compatibility details would be worth checking.|
S~Some futures open only when the right small thing is brought near.|
N~A useful possibility to investigate before deciding a Pokemon has stopped progressing.|
N~I wonder which partner made him start considering stones.
''')
add('r17_jamal', 'Route17_Text_JamalPostBattle',
    'Jamal jokes that the battle must have made him lose weight.', '''
M~An intense battle can feel like a whole afternoon of exercise in one minute.|
N~A change in effort or sweating is not a reliable measure of lasting weight change.|
N~He worked hard. A rest matters more than guessing at the scale.|
N~He sounds exhausted enough that a quiet moment would help.|
N~Catch your breath first. The battle does not need a second scorecard.|
M~The match has received an unexpected review from the fitness department.|
N~An afternoon can leave you feeling lighter without the numbers agreeing.|
N~One dramatic trial is a poor measurement. Hydration would be more immediately useful.|
N~He seems to have left a considerable amount of energy on the field.|
N~He could simply be pleased he put in the effort.|
N~I wonder whether that was his plan for the afternoon or just his consolation.
''')
add('r17_corey', 'Route17_Text_CoreyPostBattle',
    'Corey urges us to be ready to fight for our beliefs.', '''
N~I believe in choosing the right fight. That one saves a lot of running.|
N~Conviction deserves examination as well as commitment. Certainty alone is not evidence.|
N~Stand by what matters. Think before swinging at everything else.|
N~Holding your ground can matter. So can listening long enough to understand someone.|
N~There are ways to show you mean something without getting everybody hurt.|
N~A stirring declaration, though I would like to inspect the beliefs before endorsing the battle.|
N~A belief should survive a question before it demands a fight.|
N~Worth checking whether the plan serves the principle or just the adrenaline.|
N~Roots hold firm without striking at every passing foot.|
N~A strong conviction looks better with a little judgment attached.|
N~I wonder which belief he had in mind when he said that.
''')
add('r17_jaxon', 'Route17_Text_JaxonPostBattle',
    'Jaxon warns that the slope makes steering difficult.', '''
N~The hill has opinions about where the bicycle goes. Keep yours louder.|
N~Downhill speed can make small steering errors much more consequential.|
N~Slow down before the bend. Correcting late is how people get hurt.|
N~I appreciate a warning from someone who has already tried the road.|
N~Better to take the descent steadily than turn it into a very fast mistake.|
N~Gravity has taken an interest in the handlebars. An unwelcome collaborator.|
N~The road can carry you faster than your confidence deserves.|
N~Steering gets harder at speed. Good reason to test the brakes before the slope.|
N~A downward road asks for more attention than effort.|
N~That is useful advice, especially from someone staying here to practice.|
N~I wonder which bend catches visiting cyclists off guard most often.
''')
add('r17_william', 'Route17_Text_WilliamPostBattle',
    'William decides he needs sleep after the battle.', '''
S~He has identified a problem best solved horizontally.|
N~Fatigue is a good reason to stop, particularly before further cycling.|
N~Get somewhere safe before sleeping. Tired riding is a bad idea.|
S~A quiet rest sounds like the kindest end to this afternoon.|
S~Food and a proper place to lie down could improve things considerably.|
S~The day's ambitions have been revised to a single, sensible objective.|
S~A nap is a perfectly respectable answer to a long road.|
N~Low battery detected. Best recharge before using the steering system.|
S~The afternoon has finally become heavier than his eyelids.|
S~Good that he can admit it. Looking energetic is a tiring obligation.|
S~I wonder how far he still has to get home.
''')
add('r19_richard', 'Route19_Text_RichardPostBattle',
    'Richard thanks us for the battle and feels ready to swim.', '''
S~Apparently we were the warm-up. My warm-ups usually involve less being attacked.|
N~He seems to regard the battle as preparation for his swim.|
N~He sounds ready. Still needs to pay attention to the sea.|
S~It is nice to finish a battle with a simple thank-you.|
S~A cheerful start to his swim. I hope he has enough energy left for the return.|
S~A courteous opponent departs toward a rather larger pool of challenges.|
S~He has managed to keep the day light. Good for him.|
N~Warm-up complete. The actual swimming still deserves its own precautions.|
S~He is carrying the good mood straight into the water.|
S~A little gratitude makes the whole encounter feel better.|
S~I wonder whether he comes here for a swim every day.
''')
add('r19_reece', 'Route19_Text_ReecePostBattle',
    'Reece warns us that Tentacool stings are painful.', '''
N~Pretty floating things have filed a formal objection to being bumped into.|
N~A useful warning. Tentacool should be given space rather than treated as harmless drift.|
N~Watch the water. Give them room.|
N~That sounds like knowledge he would rather not have learned personally.|
N~A warning like that is worth passing on before somebody gets hurt.|
N~The sea's delicate decorations apparently come equipped with an emphatic boundary.|
N~Something translucent can still make its presence very clear.|
N~Hazard identified. Better to steer clear than test the warning.|
N~The gentlest-looking thing in the water may still insist on distance.|
N~He offered that warning without making fun of anyone. Helpful.|
N~I wonder how easy they are to spot when the water is choppy.
''')
add('r19_matthew', 'Route19_Text_MatthewPostBattle',
    'Matthew boasts that he can outswim even marine Pokemon.', '''
M~That is a bold challenge to make while most of the competitors live here.|
N~The claim depends considerably on which marine Pokemon and over what distance.|
N~Confidence is fine. Save enough energy to get back.|
N~He sounds proud. I hope he knows the water as well as he knows his own pace.|
N~Winning a race matters less than having enough left for the shore.|
M~A visiting mammal has challenged the entire resident swimming profession.|
M~The sea has an extensive roster of possible rebuttals.|
N~I would want species, distance, current, and a reliable stopwatch before accepting that.|
N~The creatures that sleep here may have a few advantages.|
M~A wonderfully confident statement with a lot of water around it.|
N~I wonder whether a Pokemon has ever actually accepted his challenge.
''')
add('r19_douglas', 'Route19_Text_DouglasPostBattle',
    'Douglas points out islands visible across the sea.', '''
S~Land on the horizon! Always nice when the sea includes a place to stop being sea.|
N~Visible land gives us a useful reference point, though distance over water can deceive.|
N~Good landmark. Do not assume it is as close as it looks.|
S~A little shape in the distance can make all this water feel less endless.|
N~Worth keeping in sight while we watch our strength and the return route.|
S~The horizon has finally supplied something with edges.|
S~Faraway land looks peaceful when you cannot yet hear it.|
N~Useful navigation reference. We should still account for the current.|
S~The water has left a few small places for feet.|
S~I like how a distant island can redirect an entire conversation.|
S~I wonder what he can make out from here that we cannot yet see.
''')
add('r19_david', 'Route19_Text_DavidPostBattle',
    'David guesses that fishing is how to find sea Pokemon.', '''
M~The sea is full of Pokemon and he is still negotiating introductions.|
N~Fishing is one method, though his statement sounds more tentative than comprehensive.|
N~A rod is worth trying. Watch what is around you, too.|
N~It is all right to be figuring things out as you go.|
N~A suitable rod and some patience would give him a way to start.|
M~Surrounded by an ocean, he has reached a cautiously nautical conclusion.|
N~Sometimes an enormous habitat still leaves you wondering where to begin.|
N~A testable idea. Better than standing here and wondering indefinitely.|
N~A line is one small question you can lower into a large mystery.|
N~He sounds uncertain rather than boastful. I appreciate that.|
N~I wonder whether he has tried fishing here yet or is planning his first attempt.
''')
add('r19_tony', 'Route19_Text_TonyPostBattle',
    'Tony watches the sea to take his mind off something bad that happened.', '''
S~The sea can do the talking for a while. He does not owe us the story.|
N~A change of focus may offer relief. We need not ask for details he did not offer.|
S~Let him have the view. We can give him some space.|
D~Sometimes it helps to look at something that keeps moving without asking you to.|
S~A quiet place and a little time can be enough company for now.|
S~He has chosen an audience that will not interrupt or demand an explanation.|
S~An immense thing going on with its day can be oddly good company.|
N~No problem to solve for him unless he asks. We can leave him his quiet.|
S~The water can hold a gaze without asking what brought it there.|
S~He told us the boundary of the story. We should respect it.|
S~I hope the shoreline gives him the pause he came here looking for.
''')
add('r19_anya', 'Route19_Text_AnyaPostBattle',
    'Anya is tired of the long journey toward Seafoam and wants to return to Fuchsia.', '''
N~Turning back is also a destination. A much more familiar one.|
N~Recognizing fatigue before reaching the limit is a useful judgment.|
N~Then turn back while there is energy left. The islands can wait.|
N~She sounds homesick for shore more than curious about the islands now.|
S~There is nothing wrong with choosing a shorter day than you planned.|
N~The expedition has discovered that its finest destination may be the starting point.|
N~Wanting home is good information when there is a lot of water left.|
N~Revise the route before the energy budget reaches zero. Sensible.|
S~A familiar shore can call louder than an unknown island.|
N~An ambitious plan can change once you find out how it actually feels.|
N~I wonder whether she has someone heading back with her.
''')
add('r19_alice', 'Route19_Text_AlicePostBattle',
    'Alice explains that swimming to Seafoam was her boyfriend\'s idea.', '''
N~His idea, their very long swim. I hope they both agreed on the return journey.|
N~A shared outing still needs both people's limits considered.|
N~His plan does not get to overrule her need for a rest.|
N~The way she says it makes me wonder whether she wanted this trip herself.|
N~A trip together works better when both people can say they have had enough.|
N~The author of this itinerary appears to have recruited a second set of tired arms.|
N~A romantic proposal can become considerably less romantic several miles offshore.|
N~Shared project, separate energy reserves. Someone should have checked both.|
N~One person's faraway wish can become another person's long way home.|
N~I would like to know whether he asked what she wanted to do.|
N~I wonder how differently they imagined this swim when they were still on land.
''')
add('r19_axle', 'Route19_Text_AxlePostBattle',
    'Axle reports leg cramps while struggling in the water.', '''
U~That is not a joke-shaped problem. He needs something solid to hold onto.|
N~Cramping in the water is urgent. Help him reach flotation or nearby shore safely.|
U~Get him support. Keep his head above water.|
U~He sounds frightened. We should take that seriously right now.|
U~He needs help getting out of the water before anything else.|
U~The bravado ends here. A struggling swimmer needs help, promptly.|
U~The sea is no place to hide that you are in trouble.|
U~That needs immediate support, not another battle or a clever reply.|
U~Something that floats needs to reach him before the words run out.|
U~He is struggling. Somebody needs to help him toward safety.|
U~He is having trouble staying up. We cannot treat that like ordinary post-battle chatter.
''')
add('r19_connie', 'Route19_Text_ConniePostBattle',
    'Connie imagines riding Lapras to stay dry while crossing the sea.', '''
S~A sea journey with a seat. She has identified the important luxury.|
N~Lapras's size makes the idea plausible, though waves would still be a factor.|
S~A steady ride sounds better than exhausting yourself out here.|
S~I understand wanting to enjoy the water without being entirely inside it.|
S~A comfortable crossing and a dry change of clothes would make a lovely day.|
S~She envisions nautical travel with a rather excellent seating arrangement.|
S~The sea is beautiful from a place where it cannot immediately fill your shoes.|
S~Buoyancy, room for a passenger, fewer wet belongings. Strong requirements list.|
S~A gentle back between you and all that restless water.|
S~Practical comfort is an underrated part of a good adventure.|
S~I wonder whether she has ever met a Lapras close enough to see its size.
''')
add('r19_lia', 'Route19_Text_LiaPostBattle',
    'Lia asks about a younger brother and hopes we teach him useful things.', '''
S~She takes the big-sister job seriously. It apparently comes with a lesson plan.|
S~Older siblings can provide a very influential model, deliberately or otherwise.|
N~Teaching matters. Listening to the younger one matters too.|
S~She sounds proud of having someone to look out for.|
S~Sharing what you know is a good way to make a journey less frightening for somebody new.|
S~An elder sister recruits the wider world into her informal educational program.|
S~Small people remember what the larger familiar people bother to show them.|
S~Passing on useful skills saves someone else from repeating every mistake.|
S~A path is easier when someone points out the loose stones first.|
S~She wants him prepared, rather than merely impressed. That is kind.|
S~I wonder which little lesson her brother still talks about most.
''')
add('r19_luc', 'Route19_Text_LucPostBattle',
    'Luc admires his big sister for being both strong and kind.', '''
S~Strong and nice. That is a very good pair of things to be famous for.|
S~He admires her conduct as well as her ability. An encouraging distinction.|
S~Sounds like she has earned that trust.|
S~He says it with no hesitation. That is a lovely thing to hear.|
S~A younger sibling feeling safe and proud beside you is quite an achievement.|
S~A concise and entirely devoted review from the person closest to the subject.|
S~A small admirer who has chosen good things to admire.|
S~Strength plus kindness. Finally, a specification with both essential features.|
S~He has found someone whose shadow feels like shelter.|
S~He notices that she is kind. Children are very good at knowing when it matters.|
S~I wonder whether she knows he talks about her that way.
''')
add('r20_roger', 'Route20_Text_RogerPostBattle',
    'Roger realizes his exhausted birds cannot fly him back.', '''
N~The return ticket needs a rest. A rather important detail when it has wings.|
N~Transport depends on the birds' remaining stamina. Their fatigue changes his options.|
N~Rest them. Do not force a tired bird to carry you.|
N~He sounds stranded. I hope there is somewhere safe for them all to recover.|
N~A sheltered rest and time for the team would be the sensible next step.|
N~The homeward journey has discovered that its transport also participated in the battle.|
N~A way home can become a creature that needs you to wait.|
N~The transport system shares the team's energy budget. Important planning lesson.|
N~The wings that brought him here have earned a quiet place to fold.|
N~He should have kept the return trip in mind. Now the birds need care.|
N~I wonder whether he has a safe place to stop while they recover.
''')

