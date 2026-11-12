"""Sevii 4-7 physical NPC terminals; placement reviewed in registered Kanto maps."""
ROWS=[]
EMOTIONS=dict(N='neutral',S='soft_smile',A='annoyed',F='flustered',D='sad',U='surprised',M='smug',L='laughing')
def add(key,labels,subject,lines):
    replies=[]
    for line in lines.strip().split('|'):
        line=line.strip()
        if len(line)>1 and line[1]=='~' and line[0]in EMOTIONS:line=EMOTIONS[line[0]]+line[1:]
        replies.append(line)
    assert len(replies)==11,(key,len(replies))
    ROWS.append(dict(key='sevii47_'+key,labels=labels.split(),subject=subject,replies=replies))

add('four_lorelei_home','FourIsland_Text_LoreleiHasReturned',
    'An older local wonders whether Lorelei returned because city life was stressful.','''
N~A return home can have more than one reason. We should let Lorelei supply hers.|
N~The resident is speculating about motivation, not reporting Lorelei's explanation.|
N~She can come home without giving the whole island a reason.|
S~A familiar place can be welcome even when nothing went wrong elsewhere.|
N~It is kind to be glad someone is back without diagnosing the trip.|
N~The returning local has acquired a speculative city-life subplot.|
S~A door can remain yours even after you have learned to live somewhere else.|
N~Observed return, unknown cause. Keep those separate.|
S~A familiar shore need not ask why the footsteps came back.|
N~People love explaining a woman's choices before asking her.|
S~I wonder what Lorelei most likes seeing when she comes home.
''')
add('four_old_lapras','FourIsland_Text_LoreleiMetLaprasAsChild',
    'A local believes Lorelei\'s Lapras is the same partner she met in Icefall Cave as a child.','''
S~One little meeting might have lasted all the way into that formidable team. Lovely thought.|
N~The account is partly tentative, but a longstanding partnership would be meaningful.|
S~A partner that stays beside you for years is worth more than a reputation.|
S~I like imagining the familiar creature beneath the impressive adult story.|
S~Years of ordinary care can become something people remember from a distance.|
S~The celebrated trainer's long story may still carry its earliest companion.|
S~A life can grow much larger around the same small beginning.|
N~Long-term partnership suggests sustained practical knowledge of each other.|
S~A cold cave may have given two lives a long warm thread between them.|
S~They say imagine and believe. A lovely story can keep its uncertainty honestly.|
S~I wonder what little habit Lorelei recognizes in Lapras after all these years.
''')
add('four_rival_egg','FourIsland_Text_RivalAlreadyGotEggBeSmellingYa',
    'The rival boasts of receiving an Egg, mocks our progress, and hints at a familiar island resident.','''
N~He arrived with news and wrapped every useful part in a little elbow jab.|
N~The Egg and familiar-person sighting are information; the claims about our knowledge are assumptions.|
N~Let him set his own pace. We can learn without his commentary.|
N~It is tiring to have every friendly place turned into another comparison.|
N~I hope the Egg gets more patience than he gives people asking questions.|
M~The rival's travel bulletin remains professionally committed to its insulting house style.|
N~A person can hurry away and still leave a rather crowded conversation behind.|
N~Extract the actual leads. Ignore the unsupported assessment.|
N~His feet keep rushing while the small useful facts fall out behind him.|
N~A little curiosity would look better on him than pretending everyone follows his itinerary.|
N~I wonder what he is most looking forward to when the Egg hatches.
''')
add('four_dolls','FourIsland_Text_LoreleiHasLotsOfStuffedDolls',
    'A girl shares Lorelei\'s growing stuffed-doll collection as a secret.','''
S~A tough public reputation can still go home to a very soft collection. Good.|
N~A private interest need not resemble the role someone is known for.|
S~Nothing wrong with it. Maybe leave her private room out of the gossip.|
S~It makes her seem warmly familiar instead of less impressive.|
S~A few little comforting things are a perfectly good reason to browse a shop.|
S~The formidable trainer has a much softer recurring cast at home.|
S~One can command great power and still appreciate a small plush face.|
S~A growing collection! I would be interested in how she arranges it.|
S~A cold-looking reputation keeps a warm little room behind it.|
S~Her taste is allowed to be sweet without becoming a scandal.|
S~I wonder which doll has been there longest.
''')
add('four_slushie','FourIsland_Text_MadeSlushieUsingIcefallCaveIce',
    'A child enjoys a slushie made with ice collected in Icefall Cave.','''
N~A cave-sourced dessert. I would prefer knowing the ice was clean before celebrating the crunch.|
N~Cold material is not automatically safe to consume. Source cleanliness still matters.|
N~Enjoy the treat if the ice is safe. A cave is not a kitchen freezer.|
S~They sound delighted by having made something from a familiar local place.|
N~A slushie is lovely; I would still use clean drinking-water ice for it.|
S~The frozen cavern has unexpectedly joined the refreshment department.|
N~A small cold pleasure with a rather adventurous ingredient history.|
N~Temperature controlled by nature, cleanliness not verified by that fact.|
S~A little of the island's hidden winter carried into the sun.|
N~It looks refreshing. I hope the preparation was thoughtful too.|
S~I wonder what flavor makes it the child's favorite.
''')
add('four_boing_weight','FourIsland_House1_Text_YoureAwfullyHeavy',
    'A resident reacts to the weight during the house\'s playful bouncing routine.','''
N~A rather blunt review from the bounce department. We can enjoy the joke without keeping the label.|
N~The physical interaction produced a reaction, not a meaningful judgment of the person.|
N~Enough commentary. Make sure the bouncing is safe.|
F~That is an awkward thing to hear while already not quite standing normally.|
N~A playful moment should not need someone to feel bad afterward.|
N~The performance has acquired an unsolicited critique of its principal's mass.|
N~A little more grace would weigh considerably less on the room.|
N~Unexpected load commentary. I would rather check the mechanism.|
N~A small joke can land harder than the person making it expects.|
N~Play is nicer when the teasing leaves everyone comfortable.|
N~I wonder whether the resident realizes how that remark sounds to a visitor.
''')
add('icefall_after','FourIsland_IcefallCave_Back_Text_ThankYouThisIsAwful',
    'After the poachers leave, Lorelei thanks us and is shaken by crime reaching her birthplace.','''
N~The cave is safer, but learning this happened at home is a different kind of hurt.|
N~Resolving the immediate threat does not erase her concern about what she missed.|
N~She helped protect the Pokemon. Start with that, then follow the warehouse lead.|
D~A familiar place can feel suddenly fragile when you learn what was happening inside it.|
N~The partners still need care, and she deserves time to take in what happened.|
N~The triumphant scene has a quieter ending for someone who knows the setting as home.|
N~A place can be rescued and still need a long time to feel untouched again.|
N~Immediate incident contained. Broader trafficking problem still needs attention.|
N~An old safe shore has shown her a shadow she did not know was there.|
N~She is allowed to be upset without turning the whole absence into her fault.|
N~I wonder whom on the island she will want to speak with first.
''')
add('lorelei_responsibility','FourIsland_LoreleisHouse_Text_IfAnythingWereToHappenToIsland',
    'Lorelei worries that working at the League means failing to protect her home.','''
N~One person cannot stand on every shore at once, even with a very capable Lapras.|
N~Responsibility can be shared through trusted people and reliable information. Constant presence is not the only method.|
N~She cares. She still cannot do everybody's job from one place.|
N~It is hard when two parts of your life both feel like the place you should be.|
N~A plan with the people here would help more than carrying every possible worry alone.|
N~The great trainer has reached a problem no solitary heroic pose can cover.|
N~Home can ask a very large thing without ever speaking aloud.|
N~Distributed responsibility is more reliable than one exhausted expert.|
N~A heart can keep two shores without growing another body to stand on them.|
N~Caring about home should not require giving up every life beyond it.|
N~I wonder who here she trusts to contact her when something is wrong.
''')
add('lorelei_return','FourIsland_LoreleisHouse_Text_IllReturnToLeagueInShortWhile',
    'After the island problems are resolved, Lorelei thanks us and plans to return to the League.','''
S~The island has room to be home again instead of a place she must keep guarding.|
S~The change in conditions lets her reconsider where her immediate presence is needed.|
S~Good. She can go back knowing the people here have help.|
S~I like hearing the guilt become a practical next step.|
S~A calmer goodbye will feel very different from leaving while worried.|
S~The local chapter closes well enough for its returning character to resume another role.|
S~A familiar shore can remain hers after the boat leaves it behind.|
N~Immediate obligations resolved. Returning to the other role is reasonable.|
S~The road away no longer needs to feel like turning away.|
S~She has made the decision herself, with the new facts in hand. Good.|
S~I wonder what small thing she will take from home for the journey back.
''')
add('lorelei_here_now','FourIsland_LoreleisHouse_Text_WillDoWhatICanHereAndNow',
    'On later visits, Lorelei commits to doing what she can despite uncertainty about the future.','''
S~A useful plan, with fewer impossible promises than the worrying version.|
S~She has separated actionable responsibility from uncertainty she cannot eliminate.|
S~Good. Do the work in reach and keep people informed.|
S~There is a quieter steadiness in that than in trying to solve every possible tomorrow.|
N~A plan you can actually carry is kinder than an endless one.|
S~The character has traded an impossible total role for a clear present scene.|
S~A small real act can be sturdier than a magnificent imaginary guarantee.|
N~Operate on known conditions, revise as information arrives. Sensible.|
S~The next step is small enough to rest a foot on.|
S~She sounds like she has left herself room to breathe as well as care.|
S~I wonder what ordinary task helps her feel useful here today.
''')
add('four_lorelei_teacher','FourIsland_Mart_Text_LoreleiGrewUpOnThisIsland',
    'An older resident proudly recalls teaching Lorelei about Pokemon as a child.','''
S~A small early lesson grew into a very impressive grown-up. Lovely reason to be proud.|
S~Early encouragement can leave a lasting contribution that later achievements make visible.|
S~Good to remember the people who helped before anyone was famous.|
S~They sound pleased by the child they still recognize beneath the title.|
S~A little patient teaching can reach farther than the teacher ever expects.|
S~The celebrated trainer's biography pauses to credit a modest earlier supporting role.|
S~Someone kept a little door open before the whole road existed.|
S~Foundational instruction matters. It is good to hear it remembered.|
S~An old voice still carries the shape of her very first questions.|
S~That kind of pride feels warm rather than possessive.|
S~I wonder which early lesson they remember her asking about most.
''')
add('four_cold_cave','FourIsland_Mart_Text_IcefallCaveIsFrigid',
    'A local warns that Pokemon make Icefall Cave cold despite the warm region.','''
N~A hidden winter in a warm island. Pack for the cave, not the palm trees.|
N~Local conditions can differ greatly from the regional climate. Preparation should match the destination.|
N~Bring a warm layer and watch the footing. Sun outside proves nothing underground.|
N~That is useful to hear before the familiar warmth disappears behind us.|
N~A little proper preparation makes a cold visit much kinder to the team.|
N~The island's scenic program includes an abrupt seasonal costume change.|
S~A pocket of winter kept alive beneath the warm ordinary day.|
N~Microclimate warning noted. Adjust clothing and route assumptions.|
S~The island has kept a small cold room inside its summer.|
N~A very practical warning for visitors dressed only for the ferry ride.|
N~I wonder how quickly the temperature changes near the entrance.
''')
add('four_ice_visitors','FourIsland_PokemonCenter_1F_Text_RareIceMonsInCave',
    'A local says visitors seek a rare Ice Pokemon in the cave.','''
S~A quiet cave has a very particular attraction hidden inside it.|
N~A sought-after resident can draw visitors, making respectful behavior important.|
N~Rare does not mean available for everyone to crowd. Give the Pokemon space.|
N~I hope the visitors remember it is a home before it is a sight to see.|
N~A patient visit is better than turning a rare encounter into a rush.|
S~The island's elusive resident has become an attraction without volunteering for publicity.|
N~A rare life deserves more than being the thing a trip must produce.|
N~High visitor interest means the habitat needs care, not just access.|
S~Something suited to the cold has made the warm island's stories a little stranger.|
N~A beautiful sight is easier to enjoy when everyone leaves it some room.|
S~I wonder what first brought news of that Pokemon beyond the island.
''')
add('four_eggs_local','FourIsland_PokemonCenter_1F_Text_DayCarePeopleFoundEggBefore',
    'A resident remembers the local Day Care finding Pokemon Eggs.','''
S~A small local story with a whole new life waiting inside it.|
N~The Day Care staff are the better source for details about what they found.|
N~Worth asking them directly. Keep the Egg safe while learning.|
S~It is nice to imagine an ordinary morning changed by such a quiet discovery.|
N~A little life needs care before it needs a complete explanation.|
S~The local routine has occasionally acquired an unexpected new beginning.|
S~Something small and silent making a familiar place feel new.|
N~Relevant specialist identified. Seek the firsthand account.|
S~A shell has left a little question in the island's ordinary day.|
N~They admit what they do not know and point us toward someone who might. Helpful.|
S~I wonder what the Day Care people noticed first about the Egg.
''')
add('five_meadow_building','FiveIsland_Text_WeirdBuildingInMeadow',
    'A child cannot play in the meadow after a strange building was put there.','''
N~A child's familiar play space has become someone else's locked project. That is a real loss.|
N~Land-use changes affect daily life beyond the people commissioning the construction.|
N~They should not have taken away the safe place without caring who used it.|
N~It is sad when a place you know stops having room for you.|
N~I hope the children have somewhere else safe to spend the afternoon.|
N~The new scenery has displaced the people who actually enjoyed the old setting.|
N~An empty-looking field is not empty to the lives that meet there.|
N~A new structure can remove an existing function. The missing play space matters.|
N~A little open patch of the day has been walled away.|
N~Someone thought about the building and apparently forgot the neighbors.|
N~I wonder what the child and friends used to play there.
''')
add('five_fishing_change','FiveIsland_Text_BeenGettingBusierAroundHere',
    'A fisher notices more activity around the island and poorer catches.','''
N~The shore has become busier while the fishing has become quieter. Worth noticing.|
N~The changes may be related, but the conversation alone does not establish a cause.|
N~A local who knows the water is worth listening to.|
N~Small changes can feel large when they touch the thing you do every day.|
N~I hope the new activity has not made the familiar fishing places less safe.|
N~The island's increasing bustle receives a distinctly unfavorable waterfront review.|
N~A familiar quiet can vanish before anyone agrees it was being taken.|
N~Two observed trends. We would need records before linking them confidently.|
N~The shore is hearing more voices and offering fewer little tugs on the line.|
N~A place getting busier is not automatically good news for everyone living there.|
N~I wonder when the fisher first noticed the catches changing.
''')
add('five_dinner_promise','FiveIsland_House1_Text_HusbandWentOffFishing',
    'A woman doubts her husband will catch enough fish for the dinner he promised.','''
M~An ambitious menu written by a man who has not yet consulted the fish.|
N~An uncertain catch should not be the only contingency for a planned meal.|
N~Have a backup. Confidence does not fill a plate.|
S~It sounds like a familiar little family debate rather than a new worry.|
M~Keep a simple second meal ready. The fish have not signed the dinner agreement.|
M~The chef's principal ingredient is currently a heroic claim made at the door.|
M~An evening that may yet become a very quiet argument with an empty bucket.|
N~Unreliable supply dependency. Backup ingredients would be sensible.|
N~The promised meal is still somewhere beneath a large amount of water.|
M~It is good to appreciate enthusiasm without shopping entirely on its behalf.|
S~I wonder whether his successful catches earn a retelling for weeks afterward.
''')
add('five_family_meadow','FiveIsland_House2_Text_MeadowBelongedToFamily',
    'The family owner regrets not building on the meadow before thugs occupied it.','''
N~A meadow should not have needed a mansion on it to keep bullies from taking over.|
N~The criminal occupation is the problem. Leaving land undeveloped did not authorize it.|
N~The thugs chose to cause trouble. He did not owe the field a wall first.|
N~It is hard when a place tied to your family becomes somewhere you dread.|
N~A familiar patch of land can mean more than what is built on it.|
N~The owner imagines a different setting as though the villains' behavior were his design failure.|
N~An open thing is not an invitation for somebody cruel to claim it.|
N~Do not blame absence of a structure for someone else's unauthorized use.|
N~A field can hold generations of footsteps without needing stone walls.|
N~The regret is understandable. The responsibility belongs with the people causing harm.|
N~I wonder which family memory first comes to him when he looks toward the meadow.
''')
add('five_chef_job','FiveIsland_PokemonCenter_1F_Text_OnMyWayToPrepareMeal',
    'A chef heads to prepare a meal for a wealthy client.','''
S~A very important dinner is still built out of somebody showing up with practical skills.|
N~A demanding client makes preparation and clear requirements especially valuable.|
N~Good work deserves decent treatment, whatever the guest's title is.|
S~I hope the person eating notices the care, not just the expensive setting.|
N~A meal for a particular person is easier when they explain what they actually enjoy.|
S~The grand household's next scene depends on a professional arriving from an ordinary journey.|
N~An elaborate table can hide how much of the day belongs to the people preparing it.|
N~Client-specific delivery. Check the requirements before the heat goes on.|
S~A little warmth is being carried toward a very polished room.|
N~High society still needs someone to make sure dinner is ready.|
S~I wonder which dish the chef is most pleased to put on that table.
''')
add('five_pokedex_fan','FiveIsland_PokemonCenter_1F_Text_YoureOnQuestToCatchEveryMon',
    'A visitor admires our species-collecting quest and asks to hear about strong catches.','''
S~A big project has found another person ready to enjoy its little discoveries.|
S~The interest focuses on strength, while the full record should include less obvious species too.|
N~We can share the story without making strength the only interesting part.|
S~It is nice when somebody sounds curious instead of turning the work into a test.|
N~Every new partner deserves care, even if the impressive ones make easier stories.|
S~The extensive field project has acquired a reader with very particular favorite chapters.|
S~A long road becomes something a stranger is pleased to hear about.|
N~Interested audience found. Useful to share the observations, not just the record size.|
S~A book of names is becoming a little bridge between people.|
S~The enthusiasm is generous. I hope the quieter finds get mentioned too.|
S~I wonder what makes a Pokemon especially impressive to this visitor.
''')
add('tectonix_grave','FiveIsland_MemorialPillar_Text_ThisIsWhereIBuriedMyOnix',
    'A mourner tells us that his Onix, Tectonix, is buried here.','''
D~A very large companion has left a very quiet space beside him.|
S~He gives us a name and a place to understand the loss. We should handle both respectfully.|
D~Let him have the moment. Tectonix clearly mattered.|
D~Saying the name makes the grave feel like someone, not just somewhere.|
S~He is still looking after a place that means love to him.|
D~A long shared story has become a few small words offered to a stranger.|
S~Stone remembering a creature that was more than stone to him.|
N~No problem to solve. A quiet acknowledgment is enough.|
D~A heavy familiar life has become an empty place in the day's footsteps.|
S~He trusted us with the name. That deserves gentleness.|
S~I wonder which ordinary little thing he misses most about Tectonix.
''')
add('tectonix_kindness','FiveIsland_MemorialPillar_Text_BeGoodToYourMonsToo',
    'After the lemonade offering and successful reward, the mourner asks us to care for our own Pokemon.','''
S~We can do that. A small promise worth carrying into every ordinary day.|
S~His request connects the memory of his partner with care for the living ones beside us.|
S~We will. They matter beyond what they can do in a match.|
D~It is a gentle thing to ask when you know what missing one feels like.|
S~Daily care is a good way to honor the kindness he shared.|
S~The farewell asks for no grand monument, only a better next day for another companion.|
S~A little grief has become a very clear kind of tenderness.|
N~A practical principle worth keeping after the reward itself is put away.|
S~The old affection has found a small way to keep moving among the living.|
S~A sincere request, with no need for a speech in return.|
S~I hope he knows the little offering was meant kindly without needing any reward.
''')
add('tectonix_reward_full','FiveIsland_MemorialPillar_Text_DontHaveRoomForIt',
    'The mourner offers to hold the reward because our bag is full.','''
S~The bag can be sorted later. The kindness we came to offer did not need a prize.|
N~The intended reward did not transfer, and he is explicitly preserving it for another visit.|
N~No rush. His thanks is already clear.|
S~It is kind that he makes the awkward part feel so small.|
S~We can make room without hurrying him through a tender moment.|
N~The practical handoff pauses while the more important exchange has already happened.|
S~A little generosity can wait without becoming less generous.|
N~Deferred transfer, no completed receipt. Keep the outcome distinct.|
S~The small offered thing can rest beside the memory a little longer.|
S~He has been thoughtful about a problem that belongs to our bag.|
S~I wonder whether he would enjoy a quiet visit even without another gift involved.
''')
add('tectonix_scrubbing','FiveIsland_MemorialPillar_Text_ScrubScrubTectonix',
    'On later visits, the mourner quietly tends Tectonix\'s memorial.','''
D~A familiar little task keeping the name close. We need not interrupt it.|
S~The repeated care gives the memorial an ongoing place in his routine.|
S~Let him work quietly. It is his way of remembering.|
D~There is so much affection in doing the same small careful thing again.|
S~A little company could be kind if he wants it. Silence is fine too.|
S~The story continues through an ordinary act rather than another long declaration.|
S~Love sometimes keeps the shape of a chore after the reason first begins to ache.|
N~Ongoing maintenance can have a personal purpose beyond the physical result.|
D~Hands keeping a place clean where the heart still leaves a little warmth.|
S~The routine belongs to him. We should let it be dignified.|
S~I wonder which days he most likes having someone quietly nearby.
''')
add('selphy_request','FiveIsland_ResortGorgeous_House_Text_WishToSeeMonPlease',
    'Selphy imperiously asks to see a particular Pokemon at once.','''
N~A very specific wish has arrived with no consideration for how far the road might be.|
N~Her preference does not establish an obligation for us to satisfy it immediately.|
N~We can decide whether to help. Her impatience is not our deadline.|
F~It is difficult to answer someone who speaks as though the yes has already happened.|
N~A living partner is not an ornament to rush across the islands for someone else's boredom.|
N~The hostess has mistaken the visiting audience for a fully staffed casting agency.|
N~A wish is allowed to remain a wish when the requested world is not hers to command.|
N~Unrequested task with aggressive priority. Acceptance remains optional.|
N~A small name has become a large demand inside a polished room.|
N~She could make the invitation much more appealing by remembering a visitor's time matters.|
N~I wonder what she likes about that Pokemon besides wanting it right now.
''')
add('selphy_butler_reward','FiveIsland_ResortGorgeous_House_Text_ButlerPleaseAcceptThisAsHerThanks',
    'After we show the requested Pokemon, the butler gives Selphy\'s reward; generic success receipts preserve his thanks.','''
S~The butler has supplied the graceful part of the thank-you. I appreciate the effort.|
N~The reward follows the fulfilled request, with his courteous speech preceding the successful transfer.|
N~A proper thank-you, at least. The partner has done enough showing for now.|
S~He makes a rather awkward exchange feel gentler.|
S~A courteous person can improve a whole room's manners by a little.|
S~The supporting attendant delivers the line the hostess might usefully have learned herself.|
S~A small island of courtesy in an unusually demanding room.|
N~Task verified and reward transferred. Clear, polite handoff.|
S~A gentler voice has found its way between the commands.|
S~His presentation makes the gift feel welcome instead of something thrown at a departing guest.|
S~I wonder how often he quietly makes visitors feel better about this household.
''')
add('selphy_bag_failure','FiveIsland_ResortGorgeous_House_Text_OhHowDisappointing',
    'When the reward cannot fit, Selphy ends the exchange with disappointment instead of providing it.','''
N~The empty space in the bag has somehow become another thing disappointing her.|
N~The preceding capacity failure prevented the reward. Her final reaction is not a success confirmation.|
N~No gift received. We do not need to apologize for failing to improve her afternoon further.|
N~It is a cold ending to a favor someone else made time for.|
N~A little practical patience would suit the moment better than the sigh.|
N~The fulfilled request ends with the hostess reviewing our luggage as inadequate.|
N~An elegant room can still offer a very ungenerous little goodbye.|
N~Capacity failure remains unresolved. The disappointed tone does not change the state.|
N~A small closed pocket has become the newest cloud over her very comfortable room.|
N~She could notice the effort already made instead of only the final inconvenience.|
N~I wonder whether the butler gets to finish a kinder goodbye once we leave.
''')
add('selphy_goodluck','FiveIsland_ResortGorgeous_House_Text_SelphyWishYouBestOfLuck',
    'After a request is marked fulfilled, Selphy briefly wishes us luck.','''
N~A short good-luck wish. The room has finally run out of assignments for us.|
N~A courteous close, though this line alone does not establish whether the earlier reward fitted.|
N~Thanks. We can head out and choose our own next stop.|
S~A simpler goodbye is easier to accept than another immediate wish.|
N~It is good to leave the favor finished instead of making the visit endless.|
N~The hostess permits the completed scene a brief, civil final line.|
N~A little open air will be a pleasant next chapter.|
N~Interaction closed. No further task requested at this moment.|
N~The doorway has become a place to leave without another pull at the sleeve.|
N~A restrained farewell suits her better than the demands did.|
N~I wonder what she does when nobody arrives to solve the next bout of boredom.
''')
add('butler_selphy_praise','FiveIsland_ResortGorgeous_House_Text_LadySelphySmileHasBrillianceOfSun',
    'The butler extravagantly praises Selphy\'s smile and begs us to please her.','''
N~A sunny smile is lovely. It still should not require the whole island's scheduling department.|
N~His devotion does not make satisfying her every wish an obligation for visitors.|
N~She can find some of her own joy. The butler sounds overworked already.|
N~That is a lot of someone else's happiness to be asked to carry.|
N~I hope his day has something in it besides managing her mood.|
N~The house's official poet has issued a solar comparison and an urgent service request.|
N~A very bright description can cast a rather long shadow over the person saying it.|
N~Single-user satisfaction has become the entire operating objective. Risky design.|
N~A room should have more than one person allowed to be a source of warmth.|
N~Admiration is fine. Making every visitor responsible for the smile feels unfair.|
N~I wonder what the butler enjoys when he is not making somebody else's day go well.
''')
add('egg_assessment','FiveIsland_WaterLabyrinth_Text_HmmISeeIsee',
    'After inspecting our lead Pokemon, the traveler ends the assessment without offering the Egg.','''
N~A thoughtful hmm, with no explanation attached. We need not turn it into a verdict on the team.|
N~He has completed the inspection but supplied no detailed conclusion. No Egg was transferred here.|
N~Keep caring for the partner. His brief reaction is not the whole measure of the bond.|
N~I would be tempted to worry about what the pause meant. Best not invent an answer.|
N~The everyday care matters more than one stranger's quiet assessment.|
N~The examiner has closed his notebook without sharing the review.|
N~A little silence can invite more self-doubt than it has actually earned.|
N~No specific diagnostic feedback provided. Do not infer more than the observation supports.|
N~A small unreadable moment beside a much longer companionship.|
N~We do not need to perform affection on command to know what the partner needs.|
N~I wonder what he noticed that he chose not to explain.
''')
add('egg_no_space','FiveIsland_WaterLabyrinth_Text_DontHaveSpaceInYourParty',
    'The traveler postpones the Egg gift because the party is full.','''
N~A new little beginning needs a place beside the others before it arrives.|
N~The gift could not enter the party. The Egg remains with the giver for now.|
N~Make a proper space before accepting responsibility for it.|
N~It is good that there is time to prepare instead of hurrying the handoff.|
N~A little planning gives the Egg a calmer welcome.|
N~The prospective new character is waiting for a real place in the traveling cast.|
S~Something quiet can wait while a little room is made safely.|
N~Party capacity reached. The proposed addition is deferred.|
S~A shell holding tomorrow is allowed to wait for an open place today.|
N~An honest limit is better than pretending we can carry every new responsibility at once.|
S~I wonder where we will be when the Egg finally decides it is time.
''')
add('egg_after','FiveIsland_WaterLabyrinth_Text_GladIMetSomeoneLikeYou',
    'After giving the Egg, the traveler is glad he met someone he trusts to care for it.','''
S~A little life has changed hands through a very warm bit of trust.|
S~His explanation confirms the Egg's travel history and the confidence behind the handoff.|
S~We will look after it. Trust like that deserves ordinary steady care.|
S~It is lovely to be remembered for the way we treat a partner.|
S~A safe welcome matters more than making an exciting story of receiving it.|
S~The traveling Egg finds its next chapter through a quiet vote of confidence.|
S~A small silent thing carrying somebody else's hope into the journey.|
N~Responsibility transferred. Time to provide consistent care rather than test the trust.|
S~A life still hidden has already met more kindness than it can see.|
S~He chose carefully. I hope the future gives him a happy update.|
S~I wonder what he first thought when he received that Egg on his own travels.
''')
add('egg_daisy_memory','FiveIsland_WaterLabyrinth_Text_CuteMonRemindsMeOfDaisy',
    'Seeing our Togepi or Togetic reminds the traveler of Daisy gently grooming Pokemon.','''
S~A gentle person can leave a memory clear enough for a small Pokemon to bring back.|
S~He remembers a specific act of care rather than a title or reputation.|
S~Good thing to be remembered for. Daisy treated the partners kindly.|
S~It is lovely that the little grooming moment stayed with him across the journey.|
S~Ordinary patient care is worth noticing. It is where a lot of trust begins.|
S~The traveler's remembered portrait is built around a quiet action rather than a grand entrance.|
S~A kind hand can remain the sharpest detail in a faraway day.|
S~Observable careful handling made a lasting impression. Reliable evidence of care.|
S~A small familiar creature has opened a warm old window in his memory.|
S~He remembers how she made the Pokemon feel. That says more than a polished introduction.|
S~I wonder which little detail of the grooming he can still picture.
''')
add('warehouse_disbelief','FiveIsland_RocketWarehouse_Text_Grunt2PostBattle',
    'A grunt refuses to believe Team Rocket disbanded.','''
N~News seems to reach this warehouse rather selectively.|
N~His disbelief is not evidence against the report. It may reflect isolation or refusal to accept it.|
N~A group being gone does not stop a few people from causing trouble under its name.|
N~It is unsettling when someone sounds so certain while the wider world has changed.|
N~The Pokemon here need help regardless of what he believes about the organization.|
N~The obsolete company name attempts to remain in business through sheer incredulity.|
N~A name can outlast the thing it used to describe, especially when someone needs it to.|
N~State information may be outdated. Current harmful behavior remains observable.|
N~An old shadow is pretending the sun never moved.|
N~He could check the news instead of insulting the messenger.|
N~I wonder when they last heard directly from the people they claim to serve.
''')
add('warehouse_buying','FiveIsland_RocketWarehouse_Text_Grunt1PostBattle',
    'The grunt offers money to buy our Pokemon.','''
A~The partners are not the part of the journey we came to sell.|
N~A price does not establish consent or an appropriate future for a living companion.|
A~No deal. They are our partners, not stock for his warehouse.|
N~It is horrible hearing a familiar companion spoken about like merchandise.|
A~A good home is not something replaced by a bigger number.|
N~The defeated trafficker attempts to turn the visiting cast into inventory.|
A~Some bonds are not improved by introducing a cash register.|
N~The proposed transaction ignores the essential welfare requirements. Reject it.|
N~A little life should not become a figure passed between greedy hands.|
A~A generous-sounding price cannot make his purpose kind.|
N~I wonder whether he can imagine valuing a Pokemon without planning to sell it.
''')
add('warehouse_adults','FiveIsland_RocketWarehouse_Text_Grunt3PostBattle',
    'The grunt dismisses our opposition as a child interfering in adult business.','''
N~Being older does not turn a cruel plan into a grown-up responsibility.|
N~Age does not justify conduct that harms others or invalidate a sound objection.|
A~Their business hurts Pokemon. A child can see that clearly enough.|
N~It is an unkind way to avoid answering what we are actually objecting to.|
N~A responsible adult would care about the harm, not just who noticed it.|
N~The villain invokes seniority when the moral argument fails to make an appearance.|
N~A tall shadow is still only a shadow.|
N~Credential irrelevant to the observed failure. Address the actual problem.|
N~A small voice can point at a large wrong thing.|
A~He has mistaken being older for being entitled to go unchallenged.|
N~I wonder how often that line has kept someone from asking the next useful question.
''')
add('warehouse_rest_route','FiveIsland_RocketWarehouse_Text_MadeItSoYouCanComeBackThrough',
    'The first admin opens a return route, suggests rest, and warns that the next admin is stronger.','''
N~A useful way back and a warning from an unexpected source. We should use both.|
N~The route modification permits recovery without losing access to the next challenge.|
N~Take the opening. Resting the team is smarter than proving we can keep limping forward.|
N~It is surprising, and welcome, to have someone make the way less punishing.|
N~A proper rest will help more than treating the warning as an invitation to hurry.|
N~The former obstacle becomes a grudging stagehand and opens a path between scenes.|
N~An unkind place has made one unexpectedly considerate adjustment.|
N~Recovery loop established. Use it before the higher expected load.|
N~A hard road has briefly left a softer way back.|
N~The practical help matters more than the grand phrasing about the next opponent.|
N~I wonder what made this admin choose to help us continue.
''')
add('warehouse_admin_departure','FiveIsland_RocketWarehouse_Text_Admin2PostBattle',
    'The final admin abandons the warehouse while vowing to find Giovanni and revive Team Rocket.','''
N~The immediate room gets safer even if the departing speech has unpleasant plans in it.|
N~The withdrawal ends this occupation, not necessarily the speaker's future hostility.|
N~Let them leave. Check the trapped partners and keep the threat in mind.|
N~I am relieved they are going, even if the last words make it difficult to relax.|
N~The Pokemon still here deserve attention before another argument with an exiting voice.|
N~The defeated antagonist departs while attempting to commission an entire future series.|
N~A closed operation is a real good outcome, however loudly someone threatens to reopen it.|
N~Immediate site cleared. Future threat uncertain; present recovery can proceed.|
N~The room is getting quieter while the shadow tries to promise a return.|
N~We can accept the useful part of the ending without believing the grand vows.|
N~I wonder what news of this departure will reach the other islands first.
''')
add('warehouse_sapphire','FiveIsland_RocketWarehouse_Text_GideonPostBattle',
    'Gideon dismisses the Sapphire as worthless without a buyer and tells us to take it.','''
N~The stone did not change. Only his chance to profit from keeping it did.|
N~He is assigning value solely by sale potential, which ignores its practical purpose.|
N~Get the gem back to Celio safely. Gideon can keep the bitter opinion.|
N~It is strange hearing something important reduced to whether he can sell it.|
N~Someone else's hard work needs it more than his wallet does.|
N~The defeated opportunist writes the most revealing review of his own priorities.|
N~A thing can be worth saving even when nobody offers coins for it.|
N~Market value and functional value are clearly different here.|
N~A little blue stone holds a road he cannot see through the price tag.|
N~His loss of interest is useful. His definition of worthless is very small.|
N~I wonder whether he ever wanted to understand the gem, rather than simply own it briefly.
''')
add('warehouse_gideon_leave','FiveIsland_RocketWarehouse_Text_GetLostLeaveMeBe',
    'Afterward, Gideon angrily asks to be left alone.','''
N~The conversation has reached the part where leaving improves every reply.|
N~He has explicitly ended the interaction. Further questioning is unlikely to help.|
N~Fine. We have better things to do than listen to him stew.|
N~I would rather go than make the room harsher for another minute.|
N~A little distance is a good next step.|
N~The defeated researcher issues a hostile closure notice.|
N~An unpleasant person can still be granted an ordinary end to the conversation.|
N~No further information offered. Stop the exchange.|
N~The sharp voice can keep its little room to itself.|
N~We do not need a warmer farewell to know it is time to leave.|
N~I wonder whether quiet will give him anything useful to think about.
''')
add('warehouse_redhair','FiveIsland_RocketWarehouse_Text_GiovannisKidHasRedHair',
    'On a later visit, Gideon briefly mistakes us for Giovanni\'s child and mentions red hair.','''
U~That is a startling family theory to throw at a returning visitor.|
N~He rejects his own identification, leaving only a reported detail about another person.|
N~Wrong person. He can leave us out of that family business.|
N~It is awkward being fitted into somebody else's troubling idea before you speak.|
N~A passing resemblance is not a reason to hand someone a whole story.|
N~An abandoned family subplot appears long enough to deliver one strangely specific detail.|
N~An unfamiliar name can briefly become a room full of things you never agreed to enter.|
N~Identity hypothesis rejected by the speaker. No need to preserve it as a fact about us.|
N~A red thread has been mentioned, but not tied to the person standing here.|
N~He has made a private detail sound like an accusation. Unpleasant.|
N~I wonder what made that thought occur to him just now.
''')
add('lostcave_lawson','FiveIsland_LostCave_Room1_Text_LawsonPostBattle',
    'Lawson keeps returning to the same cave spot and suspects the boulder count is a clue.','''
N~The cave has a very strict return policy. Counting the rocks sounds worth trying.|
S~Repeated returns suggest a rule in the route structure. The boulder pattern is a testable lead.|
N~Track the turns and count. Better than repeating the same frustrated walk.|
N~It must be unnerving when a path seems to refuse to become somewhere new.|
N~A calm note of the layout can help when the scenery keeps repeating.|
N~The maze has trapped the explorer in an unusually literal recurring scene.|
S~A pattern may be hiding inside what first looked like an empty room.|
S~A loop with possible encoded guidance. Time for a careful controlled test.|
N~The stone keeps returning the same face until someone notices its small difference.|
N~A useful observation. Frustration had not stopped him seeing the clue.|
N~I wonder which turns he has already tried from this room.
''')
add('lostcave_laura','FiveIsland_LostCave_Room4_Text_LauraPostBattle',
    'Laura reports that a woman went deeper into Lost Cave.','''
N~A useful sighting in a place particularly good at making ahead difficult to define.|
N~The observation suggests another person is in the deeper passages. Her condition is unknown.|
N~Keep an eye out. A confusing cave is a bad place to end up tired and alone.|
N~I hope she knows the way back better than the walls suggest.|
N~A calm check on someone farther in could be worthwhile.|
N~The maze's cast may include one more person beyond the next uncertain doorway.|
N~Someone else's footsteps have left a little worry in the dark.|
N~Presence reported, location approximate. Follow the route carefully.|
N~Another small life has passed between these silent walls.|
N~A clear sighting is more helpful than a dramatic guess about what happened.|
N~I wonder how long ago Laura saw her go by.
''')
add('pillar_milo','FiveIsland_MemorialPillar_Text_MiloPostBattle',
    'Milo mentions flying onward to Four Island.','''
S~A clear next destination, with the sea kept pleasantly beneath the route.|
N~Aerial travel is an available route between these locations under the appropriate conditions.|
N~Useful option if the flying partner is ready for the trip.|
S~It is nice hearing a complicated bit of geography become a simple way onward.|
N~A safe crossing still means checking the partner's condition first.|
S~The itinerary offers a skyward transition to the next setting.|
S~A far shore is sometimes closer from above.|
N~Alternative transport route noted. Verify readiness before departure.|
S~The water can lie quietly between two places the wings already know.|
N~Helpful directions, especially when the ground route is not obvious.|
S~I wonder which island Milo most likes arriving at from the air.
''')
add('pillar_chaz','FiveIsland_MemorialPillar_Text_ChazPostBattle',
    'Chaz points out a somber man nearby.','''
N~Then we should approach gently, if we approach at all. A sad person is not an attraction.|
N~The description concerns an apparent mood, not the cause of it. We should avoid assumptions.|
N~Give him room. He may have a good reason to want quiet.|
N~I would not want my expression made into somebody else's sightseeing tip.|
N~A little consideration is more useful than curiosity about the sadness.|
N~The local observer points toward a scene that may not need an audience.|
N~A quiet sorrow can be noticed without being investigated.|
N~Observation does not grant access to the person's private history.|
N~A lowered voice is enough of a reason to lower our own.|
N~Somebody looking sad does not owe strangers an explanation.|
N~I wonder whether Chaz knows him well enough to offer company kindly.
''')
add('pillar_harold','FiveIsland_MemorialPillar_Text_HaroldPostBattle',
    'Harold delights in his birds\' playful begging.','''
S~A very persuasive little feathered lobbying group. They know their audience.|
S~Familiar play behaviors can become a rewarding part of the partnership.|
S~Good to enjoy the small things between battles.|
S~It is lovely how much happiness fits inside a tiny familiar habit.|
M~Birds can negotiate very effectively when they think a snack is available.|
S~The devoted audience appears delighted with an entirely improvised avian performance.|
S~A little silliness keeping a strong bond pleasantly ordinary.|
S~Positive interaction that both sides recognize. Excellent feedback.|
S~Small bright movements making a familiar afternoon warmer.|
S~The partner's personality is what he remembers first. Nice.|
S~I wonder whether each bird has a different way of asking him.
''')
add('resort_daisy','FiveIsland_ResortGorgeous_Text_DaisyPostBattle',
    'Daisy realizes her paint tubes have spilled everywhere.','''
N~The painting supplies have attempted an unscheduled still life. Better gather them.|
N~A scattered kit can be damaged or lost quickly outdoors. Recovery first.|
N~Pick them up before someone slips or a tube rolls away.|
F~That sinking little moment when the things you need are suddenly everywhere.|
N~A cloth and a little patience are better than stepping through the mess.|
N~The art department has distributed its materials across the entire set.|
N~A small colorful catastrophe. Fortunately, an ordinary one to put right.|
N~Contain the spill, retrieve the small parts, then inspect the damage.|
N~The colors have gone wandering before reaching the page.|
N~An organized bag can save a lot of this particular kind of drama.|
N~I wonder whether any of the tubes opened when they fell.
''')
add('resort_celina','FiveIsland_ResortGorgeous_Text_CelinaPostBattle',
    'Celina immediately resumes directing Gillian\'s pose for her art.','''
S~The battle has ended; the important head angle is back on the schedule.|
S~A small pose adjustment can change the composition considerably.|
N~Fair enough. Make sure Gillian is comfortable holding it.|
S~It is interesting watching someone recognize the exact little look they wanted.|
N~A patient model deserves a break as much as the artist needs the right angle.|
S~The artist returns to directing the more cooperative scene.|
S~A small tilt can make a familiar face feel suddenly different.|
N~Fine adjustment requested. Check the model's comfort before a long hold.|
S~One face turns slightly, and the light finds another place to rest.|
S~She has a precise eye. Kind direction makes that eye easier to work with.|
S~I wonder what changed in the expression when the head moved.
''')
add('resort_rayna','FiveIsland_ResortGorgeous_Text_RaynaPostBattle',
    'Rayna finds the changing sky and sea difficult to capture in art.','''
S~The scenery keeps changing its mind faster than the paint can dry. Unfairly talented scenery.|
S~Changing light and moving surfaces make a single fixed representation challenging.|
N~Pick the moment worth keeping. Cannot hold the whole sea still.|
S~I understand wanting to catch a feeling just before it becomes another one.|
S~A little of the change can be part of what makes the finished thing alive.|
S~The two grandest models in the room refuse to hold a pose.|
S~A restless subject may ask for a little restlessness in the picture.|
N~Dynamic input, fixed output. Choose which properties to preserve.|
S~The light keeps crossing a threshold no hand can quite follow.|
S~An honest little impression can be more striking than pretending nothing moved.|
S~I know that feeling. Sometimes one clear moment says more than trying to keep every wave.
''')
add('resort_jacki','FiveIsland_ResortGorgeous_Text_JackiPostBattle',
    'Jacki enjoys relaxed battles in the gentle sea breeze.','''
S~A match with a nice breeze has fewer complaints from the hair department.|
S~Comfortable conditions can make a familiar activity feel pleasantly different.|
N~Good to enjoy it without turning every result into a crisis.|
S~A battle can be a happy shared moment instead of a grand judgment.|
S~A calm pace and a lovely place make the outing easier on everyone.|
S~The competitive scene has chosen a rather agreeable natural venue.|
S~A little challenge, a little wind, no need to make the afternoon cruel.|
S~Suitable conditions, positive experience. A good recreational setup.|
S~The air has left room for the game to stay light.|
S~Enjoying the setting is part of choosing the outing well.|
S~I wonder whether Jacki comes here at the same time to catch this breeze.
''')
add('resort_gillian','FiveIsland_ResortGorgeous_Text_GillianPostBattle',
    'Gillian imagines the relative pleasures of a pool and a sunroom.','''
M~A difficult choice between two exceptionally comfortable ways to stay in one place.|
N~They offer different conditions. The preference depends on how the room would actually be used.|
N~Either is fine if she enjoys it. The view is already doing plenty of work.|
S~A little room for quiet daylight sounds lovely to me.|
S~A sunroom with a comfortable seat would make a good place for a slow meal.|
M~The leisure itinerary has expanded into a property-development proposal.|
S~A room full of light is a quiet sort of luxury.|
N~Glazing, ventilation, shade. Sublime still needs a practical design.|
S~Somebody is imagining a little place to sit inside the weather.|
S~The sunroom has atmosphere. The pool has a much more demanding maintenance list.|
S~I wonder which view she would want the windows to frame.
''')
add('resort_destin','FiveIsland_ResortGorgeous_Text_DestinPostBattle',
    'Destin enjoys running with the wind and imagines flying.','''
S~The wind is a very encouraging running partner, provided it is on the correct side.|
S~A following wind can make movement feel unusually effortless.|
N~Enjoy the pace. Keep enough energy to return.|
S~That small feeling of lightness sounds worth the run.|
N~A happy bit of exercise still deserves water and a break afterward.|
S~The runner briefly finds the world willing to provide its own uplifting soundtrack.|
S~A few quick steps can make the body feel less heavy with itself.|
N~External assistance to motion, excellent subjective result.|
S~The feet stay on the earth while the thought runs a little higher.|
S~It is nice hearing someone enjoy the motion instead of simply measuring it.|
S~I wonder whether Destin has a favorite stretch where the wind always seems right.
''')
add('resort_toby','FiveIsland_ResortGorgeous_Text_TobyPostBattle',
    'Toby dismisses taking the battle seriously as nonsensical.','''
N~He can keep it light without deciding everyone else's effort was silly.|
N~Different levels of personal investment can coexist without invalidating the activity.|
N~The team tried. Nothing nonsensical about doing a job properly.|
N~It hurts a little when someone makes caring sound embarrassing.|
N~A game can be relaxed and still deserve attention to the partners involved.|
N~The disappointed critic dismisses the entire genre to avoid reviewing the scene.|
N~Irony is a very convenient place to retreat when sincerity loses a match.|
N~If the objective was leisure, assess enjoyment rather than mocking effort.|
N~A light afternoon does not require everyone to put their heart away.|
N~A little composure would look better than pretending the match never mattered.|
N~I wonder whether he felt the same way before the outcome was known.
''')
add('labyrinth_alize','FiveIsland_WaterLabyrinth_Text_AlizePostBattle',
    'Alize thinks our care for Pokemon could suit breeding.','''
S~A kind compliment about the quiet work, rather than just the scoreboard.|
S~Attention to individual needs is relevant to responsible breeding and care.|
N~Good care comes first. A title can wait.|
S~It is lovely when someone notices how a partner is treated.|
N~That work takes patience every ordinary day, not just enthusiasm for Eggs.|
S~The observer has found a possible future role in the care already visible.|
S~A gentle habit can be more revealing than an impressive introduction.|
N~Useful skills identified. Any next responsibility still needs preparation.|
S~A little trust noticed from the outside is a warm sort of compliment.|
S~She praises something that lasts beyond one good match. I like that.|
S~I wonder which small interaction made her think so.
''')
