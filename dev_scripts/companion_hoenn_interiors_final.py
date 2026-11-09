"""Additional Hoenn interior endings, authored in canonical eleven-voice order.

Only final conversational branches are bound. Shared item/decor receipts may
follow gifts; bag/storage failures remain distinct unknown or authored endings.
"""
ROWS = []
EMOTIONS = dict(N='neutral', S='soft_smile', A='annoyed', F='flustered', D='sad', U='surprised', M='smug', L='laughing')
def add(key, labels, subject, lines):
    replies = [x.strip() for x in lines.strip().split('|')]
    replies = [EMOTIONS[x[0]] + x[1:] for x in replies]
    assert len(replies)==11, (key,len(replies))
    ROWS.append(dict(key='hif_'+key, labels=labels.split(), subject=subject, replies=replies))

add('flats_workers', 'RustboroCity_Flat2_1F_Text_DevonWorkersLiveHere', 'The building houses Devon employees.', '''
S~Their commute appears to be pleasingly short.|
N~The employer is part of both the working day and the neighborhood.|
N~Good to have somewhere close to rest after work.|
N~I wonder what everyone talks about when the workday ends.|
N~Hopefully they get to leave the job at the office door.|
N~A building full of people with one very reliable conversation starter.|
N~An office reunion every time someone takes out the rubbish.|
N~They probably compare ideas in the hallway without planning to.|
N~A workplace can cast its shape across the nearby homes.|
N~Sharing an employer doesn't mean they all live the same life.|
N~I'd ask what makes the building feel like a neighborhood.
''')
add('flats_tiny_devon', 'RustboroCity_Flat2_2F_Text_DevonWasTinyInOldDays', 'An elder remembers Devon as a tiny company.', '''
U~The enormous company used to be a tiny company with enormous plans.|
N~Remembering its early scale gives the present buildings useful context.|
N~Somebody remembers the work before it looked impressive.|
S~It must feel strange to watch a familiar little place grow so large.|
N~I wonder what the first employees thought would happen.|
S~The grand institution began with a much smaller cast list.|
N~Every enormous thing was once easier to fit in a room.|
N~I'd ask which change made the growth feel real.|
N~A small beginning can remain vivid beside a vast result.|
N~He has a version of the company the brochures can't quite give us.|
S~I'd like to hear what the building looked like back then.
''')
add('flats_child_work', 'RustboroCity_Flat2_2F_Text_GoingToWorkAtDevonToo', 'A child hopes to follow their father into Devon employment.', '''
S~Dad's workplace has become somewhere important on the map of growing up.|
N~A familiar example can strongly shape a child's imagined future.|
S~Good ambition. There's time to discover what kind of work suits him.|
S~He sounds proud of his father before he even mentions himself.|
S~I would ask which part of his dad's work he likes hearing about.|
S~A young character has already chosen the setting of his adult chapter.|
S~The family business is rather larger than the family.|
N~He could start by learning what different people do there.|
S~A future can first look like someone coming home at dusk.|
S~Following a parent can be sweet, as long as other choices stay open.|
S~I'd ask what he'd love to make there one day.
''')
add('flats_premier_gift', 'RustboroCity_Flat2_2F_Text_MyDaddyMadeThisYouCanHaveIt', 'The child shares a Premier Ball made by their father; unsuccessful bag transfers invalidate this offer.', '''
S~He has shared a little piece of being proud of his dad.|
S~The object matters to him partly because he knows who made it.|
S~That's generous. Treat a gift from the kid with care.|
S~I like that he wants somebody to use something his father made.|
S~It's a kind offer, even if it began as something he couldn't use.|
S~A small gift arrives with a warmly personal maker's signature.|
S~A souvenir of someone else's perfectly understandable parental pride.|
N~I'd ask what his father worked on when making it.|
S~An ordinary thing can hold a very particular fondness.|
S~He made the gift feel personal by telling us where it came from.|
S~I'd make sure he knows we appreciate the thought.
''')
add('flats_stone_president', 'RustboroCity_Flat2_3F_Text_PresidentCollectsRareStones', 'An employee mentions the president rare-stone collection.', '''
S~A man named Stone collecting stones feels unusually well organized.|
N~A material can be professionally useful and personally fascinating.|
N~Everybody needs something they enjoy beyond running a company.|
N~I wonder which stone he remembers finding himself.|
S~A hobby gives somebody a reason to notice a little thing carefully.|
S~The president's name has received unusually enthusiastic thematic support.|
S~Rocks make pleasantly undemanding company after a day of meetings.|
N~I'd ask whether he chooses for appearance, rarity, or composition.|
N~A quiet collection can hold a person's wandering attention.|
N~The interesting part is usually why a particular piece was kept.|
S~I'd enjoy hearing the story of the least impressive-looking one.
''')
add('flats_stone_son', 'RustboroCity_Flat2_3F_Text_PresidentsSonAlsoCollectsRareStones', 'A resident thinks the president son also collects rare stones.', '''
S~The family has found something solid to agree about.|
N~A shared interest can develop through early exposure without remaining identical.|
S~A good thing to share, if they both enjoy it.|
S~I wonder whether they ever bring finds back to show each other.|
S~Some family traditions fit into the palm of a hand.|
S~The younger Stone appears to have retained the family theme.|
S~An inherited interest with very durable souvenirs.|
N~I'd ask whether their collections focus on the same kinds of material.|
S~The same road can leave different stones in two pockets.|
S~Sharing a hobby still leaves room for individual taste.|
S~I'd ask who first took the younger collector out looking.
''')
add('devon_security_shock', 'RustboroCity_DevonCorp_1F_Text_HowCouldWeGetRobbed', 'The stair guard angrily questions how Devon was robbed.', '''
N~Shock is understandable. Calling the whole situation stupid won't recover the parcel.|
N~A failed security process needs examination rather than disbelief.|
N~Work out how it happened. Anger alone won't stop a repeat.|
N~He sounds shaken enough to put it all into one sharp sentence.|
N~I'd rather hear whether the person carrying it is all right.|
N~The institution has discovered its impressive name does not repel thieves.|
N~Disbelief remains an ineffective lock.|
N~They should review the actual route and access points.|
N~A place that felt secure has acquired a crack in its certainty.|
N~He can be upset without turning it into blame for the victim.|
N~I'd ask what they know for certain before guessing at fault.
''')
add('devon_victim_blame', 'RustboroCity_DevonCorp_1F_Text_StaffGotRobbed', 'The greeter blames a staff member for being robbed of a parcel.', '''
A~The thief did the stealing. That seems like the important detail.|
N~Being targeted does not establish negligence by the victim.|
A~Blame the robber. Check on your coworker.|
D~I'd hate to come back shaken and hear people say that about me.|
N~Someone had a bad enough day before the office started judging them.|
N~The account has curiously assigned the villain's work to the victim.|
A~An unpleasantly efficient way to make a frightened colleague feel worse.|
N~They need facts about the failure, not a convenient person to insult.|
D~A stolen parcel should not cost somebody their dignity as well.|
A~That is a poor way to speak about someone who needed help.|
N~I'd ask whether anyone has actually listened to the staff member's account.
''')
add('devon_greeter', 'RustboroCity_DevonCorp_1F_Text_WelcomeToDevonCorp', 'The greeter welcomes visitors to Devon and describes its products.', '''
S~A company that makes useful things is happy to tell us about every one of them.|
N~Their products span several applications rather than one narrow field.|
N~A clear welcome. We can ask where we need to go.|
S~It's nice to have someone make the large building feel less daunting.|
N~I'd ask which everyday item people use without knowing it came from here.|
S~The welcome contains a brisk tour of the company's ambitions.|
N~A pleasant introduction with a brochure quietly folded inside.|
N~I'd like to know how they decide which problems are worth solving next.|
N~A building can send small useful things into many different lives.|
N~They want us to know the work has a purpose beyond the walls.|
S~I'd ask what the greeter is most proud to see people using.
''')
add('devon_guard_welcome', 'RustboroCity_DevonCorp_1F_Text_YoureAlwaysWelcomeHere', 'After the goods return, the guard warmly welcomes the player.', '''
S~The door has changed its opinion of us quite dramatically.|
S~Our earlier actions have established trust with the staff.|
S~Good to know. Let's respect the welcome.|
S~A familiar face being glad to see us makes the building feel warmer.|
S~It's a nice thing to hear after a difficult errand.|
S~The former obstacle has become a particularly agreeable host.|
S~Authorization has acquired a smile. An improvement.|
N~We should still ask before entering an active work area.|
S~A closed place can become somewhere that remembers us kindly.|
S~A thank-you sometimes takes the form of being comfortable when you return.|
S~I'd take a moment to say hello instead of simply rushing past.
''')
add('devon_feature_hard', 'RustboroCity_DevonCorp_2F_Text_DevelopNewPokenavFeature', 'A researcher is struggling to develop a new PokeNav feature.', '''
N~The idea sounds smaller when you say feature than when you try making it work.|
N~Integrating a new function often creates constraints beyond the function itself.|
N~Better to test it properly than hurry out something unreliable.|
N~I know the feeling of something clear in your head refusing to come out right.|
N~A difficult day doesn't mean the whole idea is bad.|
N~The promised improvement has reached the obstinate middle of its development.|
N~A new feature has discovered several innovative ways to be unfinished.|
N~I'd ask which test keeps failing. That would give us something useful to discuss.|
N~A small light can need a great deal of work before it stays lit.|
N~They may need a patient listener more than another bright suggestion.|
N~I'd ask what they tried most recently and what it taught them.
''')
add('devon_new_project', 'RustboroCity_DevonCorp_2F_Text_WhatToWorkOnNext', 'An engineer appreciates Devon freedom to pursue new inspirations.', '''
S~Finishing one invention has apparently opened twelve doors in his head.|
S~Support for exploratory work can make uncertain but valuable projects possible.|
S~Good situation. Pick a useful problem and give it proper attention.|
S~It's nice hearing someone happy about the possibilities in their work.|
S~Room to try things is worth appreciating. So is time to finish them.|
S~The engineer stands before the blank page with an unusually supportive publisher.|
S~A blank project list producing excitement instead of dread. Remarkable.|
U~I'd ask which everyday frustration he's most tempted to tackle.|
S~A place can offer shelter to thoughts that aren't useful yet.|
N~Freedom is nicest when the people doing the work actually feel it.|
S~I'd love to hear the strange idea he hasn't decided to say aloud yet.
''')
add('devon_nav_try', 'RustboroCity_DevonCorp_2F_Text_WowThatsAPokenav', 'A researcher recognizes the PokeNav and recommends learning its features by trying it.', '''
S~He almost gave us the entire explanation, then trusted us to poke the useful buttons.|
N~Direct exploration can teach an interface when its functions are discoverable.|
N~Try it somewhere calm before relying on it in a hurry.|
S~I appreciate being allowed to learn at a quieter pace.|
N~I'd start with the feature we actually need for the next trip.|
S~The lecture has graciously transformed into a practical demonstration by the visitor.|
S~A description spared. The device may yet describe itself.|
S~A tool should help people discover its functions without a long speech.|
N~Curiosity can learn the shape of a useful thing through ordinary use.|
S~He notices our experience matters more than his complete explanation.|
N~I'd come back with one question after trying it rather than guess at everything.
''')
add('devon_fossil_working', 'RustboroCity_DevonCorp_2F_Text_DevelopDeviceToResurrectFossils', 'The fossil scientist reports a working regenerator; this label alone does not mean a fossil was submitted.', '''
U~A machine that can turn a very old trace into a living introduction!|
U~Reconstructing a living Pokemon from a fossil is an extraordinary technical claim.|
N~Impressive work. Be careful with whatever comes back.|
N~The idea of meeting something from so long ago feels enormous.|
N~A living creature will need more than a successful machine waiting for it.|
U~The distant past has been offered a door into the present.|
U~Prehistory has apparently become available by appointment.|
U~I'd want to understand how they confirm the result is healthy and stable.|
N~Something once held by stone may breathe again.|
N~That is a tremendous responsibility as well as an achievement.|
U~I'd ask what the first living result did when it looked around.
''')
add('devon_fossil_decline', 'RustboroCity_DevonCorp_2F_Text_OhIsThatSo', 'The player declines fossil regeneration and the researcher affirms Devon expertise.', '''
N~He's still proud of the machine, even when we aren't using it today.|
N~Our refusal does not evaluate the technology's actual capability.|
N~We can wait until we're ready to make that decision.|
N~It is a big choice. I'm glad nobody forced a quick answer.|
N~Bringing a creature into our care deserves a little thought first.|
N~The inventor accepts a declined demonstration while preserving the sales pitch.|
N~His confidence has survived our lack of participation.|
N~We can ask more questions about the process before committing a fossil.|
N~An old remnant can remain quiet while we decide what follows.|
N~We don't owe curiosity a decision before we're comfortable.|
N~I'd ask what the process requires after the Pokemon is revived.
''')
add('school_trade_now', 'RustboroCity_PokemonSchool_Text_TradingRightNow', 'A student is trading Pokemon with a friend.', '''
S~An actual lesson happening right in the middle of being excited.|
N~They are learning an exchange process through a real transaction with a peer.|
N~Let them finish. They need to pay attention.|
S~They seem pleased to share something with each other.|
S~A friend makes learning a new thing less intimidating.|
S~The practical portion of the curriculum has acquired a personal audience.|
S~A school activity with unusually interesting passengers.|
N~They should check the exchange details before confirming.|
S~Two little journeys are about to change who walks beside them.|
S~Knowing the other Trainer makes it easier to ask about the Pokemon's habits.|
S~I'd ask what made them choose this particular trade afterward.
''')
add('school_seedot', 'RustboroCity_PokemonSchool_Text_AlwaysWantedSeedot', 'A student is excited to receive a long-wanted Seedot.', '''
S~A long-standing wish is about to arrive wearing an acorn hat.|
S~A particular interest can make the first chance to care for a Pokemon memorable.|
S~Good. Now comes learning how to look after it.|
S~I like the feeling in finally. It carries a lot of waiting.|
S~I'd ask what they have learned about keeping Seedot comfortable.|
S~A much-anticipated character is finally due to make an entrance.|
S~An exceptionally small dream with a very satisfactory shape.|
N~Enthusiasm is a good start. Preparation will help the first days go well.|
S~A wish can be small enough to sit quietly beside you.|
S~They already have a place for that Pokemon in their imagination.|
S~I'd love to hear why Seedot became the one they hoped for.
''')
add('school_confusion', 'RustboroCity_PokemonSchool_Text_ConfusedPokemonAttacksItself', 'A student explains involuntary self-injury under battle confusion and recovery after leaving battle.', '''
D~That's awful for the Pokemon. It isn't choosing to hurt itself.|
N~Confusion changes control of an action rather than reflecting a deliberate intention.|
N~Pull a confused partner out if it needs help. Don't blame it.|
D~It must be frightening to have your own movement stop making sense.|
N~We should give it a calmer moment, not another shouted demand.|
N~A cruel complication in which the actor loses command of its own actions.|
N~One more reason not to mistake every action for a choice.|
N~Switching out can remove the problem. Keep that option ready.|
D~A body can become unfamiliar for a moment. Kindness should remain familiar.|
N~The partner needs us to notice the condition before judging the result.|
N~I'd watch closely for those signs instead of waiting for it to happen twice.
''')
add('school_quickclaw_gift', 'RustboroCity_PokemonSchool_Text_StudentsWhoDontStudyGetQuickClaw', 'The teacher gives a Quick Claw while jokingly warning inattentive students; bag-full failure invalidates the gift offer.', '''
F~That lesson came with a claw and a surprisingly pointed attendance policy.|
N~She intends its use as a practical assessment of what a student understands.|
N~We can learn the item without endorsing the threat in that introduction.|
F~I think I would sit very straight in this classroom.|
N~A demonstration will teach more than making students nervous.|
N~The teacher has selected an unusually tactile metaphor for poor study habits.|
N~An educational accessory with a rather alarming disciplinary reputation.|
N~I'd ask what decisions she expects the holder to make differently.|
N~A lesson should leave understanding, not just an anxious silence.|
N~The useful gift doesn't need the intimidating flourish to matter.|
N~I'd ask a student how the teacher actually explains its use.
''')
add('school_scott_cut', 'RustboroCity_PokemonSchool_Text_ScottMetAlreadyCut', 'Scott introduces his Trainer scouting and recommends obtaining Cut in Rustboro.', '''
N~He is looking for battle experts, and we're still collecting useful lessons.|
N~He has offered a concrete local lead alongside his introduction.|
N~Cut is useful. We can follow up without trying to impress him.|
F~Being noticed by someone looking for experts makes a classroom feel different.|
N~I'd rather learn the next useful thing than hurry to look accomplished.|
N~The talent scout interrupts the first chapter with a sensible errand.|
N~Potential expertise has been assigned some preliminary tree work.|
N~We should ask the local resident for the HM and learn its limits.|
N~A larger future can begin with one small obstacle understood.|
N~He sees a Trainer to assess; we still get to choose our own pace.|
N~I'd ask what he notices in the decisions of a good beginner.
''')
add('school_scott_badge', 'RustboroCity_PokemonSchool_Text_ScottMetAlreadyStoneBadge RustboroCity_PokemonSchool_Text_ScottStoneBadge', 'Scott recognizes the Stone Badge but says it cannot show how the player actually battles.', '''
S~The badge tells him we did it. It doesn't tell him how many nervous faces I made.|
N~An outcome records success without revealing the process that produced it.|
N~Fair point. A Trainer's choices matter more than the shine in the case.|
N~It's nice that he wants to see more than the finished result.|
N~A badge doesn't show the practice, the mistakes, or how the team was treated.|
N~The review acknowledges the award while requesting access to the actual performance.|
N~A certificate has declined to become a full biography. Sensible.|
N~Watching a battle would reveal far more about planning and adaptation.|
N~A mark can remember a moment without holding its whole shape.|
N~He treats the badge as a beginning to the conversation rather than its answer.|
N~I'd ask which parts of a battle he watches most carefully.
''')
add('school_scott_potential', 'RustboroCity_PokemonSchool_Text_StudentTalentLevelUnknown', 'Scott sees student potential but does not yet know their talent levels.', '''
S~A classroom full of people who haven't become their future selves yet.|
N~He is distinguishing possible growth from currently observed ability.|
N~Give them time and proper teaching before judging the result.|
S~I like that not knowing still leaves room for hope.|
N~People learn better when they aren't treated as finished products.|
S~A cast of unwritten futures, mercifully spared a final review.|
N~Potential: the respectable scientific term for wait and see.|
N~The teaching environment matters as much as the first signs of aptitude.|
N~A seed does not need to resemble a tree to be worth tending.|
N~I'd want every student to get room to try, not only the obvious standouts.|
S~I'd ask what the quietest student is excited to learn.
''')

add('game_coins_bought', 'MauvilleCity_GameCorner_Text_ThankYouHereAreYourCoins', 'The coin purchase has completed successfully.', '''
N~Our money has become smaller money with a much more specialized address.|
N~The purchase completed. The coins are now available in the case.|
N~Set aside what we're willing to spend before starting.|
N~I would rather decide a stopping point while everything is still quiet.|
N~Let's keep enough ordinary money for the rest of the trip.|
N~The admission tokens have been acquired; the evening need not become an epic.|
N~Our funds have changed costume. Their finite quantity remains.|
N~We should check the balance and keep a simple limit in mind.|
N~A small handful can still represent a great deal of work.|
N~A budget is easier to keep before the room gets exciting.|
N~I'd remember what we came to enjoy rather than chase every machine.
''')
add('game_case_needed', 'MauvilleCity_GameCorner_Text_NeedCoinCaseForCoins', 'The clerk cannot sell coins because the player lacks a Coin Case.', '''
F~We arrived at the coin shop without anywhere to put the shop's particular coins.|
N~The missing case prevents the transaction before any money changes hands.|
N~Need the proper container first. Clear enough.|
N~At least the problem is something small we can sort out.|
N~Better to know before handing over the money.|
N~The preliminary errand has acquired a preliminary errand of its own.|
N~Special currency, special pocket. Administrative elegance.|
N~We can locate the case before returning to buy anything.|
N~Even a small pastime has its particular threshold.|
N~The clerk gave us a useful reason rather than simply refusing.|
N~I'd ask where visitors usually get a case in town.
''')
add('game_money_short', 'MauvilleCity_GameCorner_Text_DontHaveEnoughMoney', 'The requested coin purchase fails because the player lacks money.', '''
N~The purse has voted to keep this visit short.|
N~The requested amount exceeds our available funds. No purchase occurred.|
N~Leave it for now. We have other things to pay for.|
N~There is no need to feel embarrassed or keep trying the same answer.|
N~Food and travel should come before more game coins.|
N~Our financial narrator has closed this particular subplot.|
N~A remarkably clear spending limit has presented itself.|
N~We can choose a smaller plan instead of trying to force this one.|
N~An empty hand can also be an instruction to pause.|
N~The room's excitement doesn't get to decide what we can afford.|
N~I'd find something else in town to enjoy today.
''')
add('game_buy_canceled', 'MauvilleCity_GameCorner_Text_DontNeedCoinsThen', 'The player cancels buying coins and the clerk wishes them well.', '''
S~A polite goodbye, and all our ordinary coins stayed ordinary.|
N~The transaction was canceled without changing our funds.|
S~We're done here for now. Good time to move on.|
S~I'm glad deciding not to buy something can be this simple.|
N~Sometimes keeping the money for another day is the pleasant choice.|
S~The proposed purchase exits quietly, leaving no financial cliffhanger.|
S~A successful encounter with the word no. Refreshing.|
N~We can come back with a clearer plan if we want to play later.|
S~A hand can close around what it chooses to keep.|
S~The welcome didn't vanish when the purchase did.|
S~I'd say thanks and see what else this afternoon offers.
''')
add('game_case_full', 'MauvilleCity_GameCorner_Text_CoinCaseIsFull', 'The coin purchase cannot complete because the Coin Case is full.', '''
U~We have reached the official edge of how many tiny round things fit.|
N~Capacity, rather than funds, is the limiting condition. No additional purchase occurred.|
N~Enough coins already. We don't need to buy more.|
N~That seems like a useful point to stop at the counter.|
N~A full case is a good reminder to use what we have thoughtfully.|
N~The treasury has declared itself physically complete.|
N~Abundance has met the zipper. A decisive opponent.|
N~Check the actual balance before making another purchase request.|
N~A container can know when enough has arrived.|
N~There is no need to treat every limit as something to work around.|
N~I'd decide what we actually want from this visit before using any.
''')
add('game_prizes_canceled', 'MauvilleCity_GameCorner_Text_OhIsThatSo', 'The player exits the prize-selection session without a new selection.', '''
N~The prize can stay on its shelf while we decide what matters to us.|
N~The selection session has ended. This farewell does not establish a purchase.|
N~No rush. Keep the coins until we know what we want.|
N~I prefer leaving undecided to choosing because somebody is waiting.|
N~A prize is nicer when you have a real place or use for it.|
N~The display remains an assortment of possibilities rather than an obligation.|
N~The dolls will endure another evening of remaining merchandise.|
N~We can compare the options away from the counter.|
N~A wanted thing need not become ours today.|
N~Walking away is part of choosing, too.|
N~I'd look at the whole visit before deciding what souvenir belongs to it.
''')
add('game_coin_basics', 'MauvilleCity_GameCorner_Text_CoinsAreNeededToPlay', 'A patron explains that the games require coins.', '''
N~The games have their own little money ecosystem.|
N~The local currency separates play spending from ordinary purchases.|
N~We know the requirement. We can decide if we want to take part.|
N~It helps when someone explains the small thing everybody else assumes you know.|
N~I'll keep our meal money separate from whatever we choose to spend here.|
N~Every institution has a ritual; this one's is converting perfectly usable money.|
N~A room with a currency and remarkably few essential goods.|
N~We should learn the costs before turning the first coin into a game.|
N~A threshold can be made of small metal circles.|
N~A simple explanation can make an unfamiliar room feel less awkward.|
N~I'd ask which game they actually enjoy, apart from the prizes.
''')
add('game_roulette_luck', 'MauvilleCity_GameCorner_Text_RouletteOnlyLuck', 'A patron describes roulette outcomes as luck rather than reliable skill.', '''
N~The wheel has declined to become predictable just because somebody asked nicely.|
N~A streak does not supply control over a chance-based outcome.|
N~Then don't count on it paying for anything important.|
N~I wouldn't want the next spin to decide how I feel about the whole day.|
N~A little entertainment is easier to enjoy when dinner doesn't depend on it.|
N~The wheel is an indifferent critic with no obligation to admire persistence.|
N~Chance is notorious for not accepting complaints.|
N~We can set a limit without needing to predict a winning pattern.|
N~A turning circle is not a promise to return what it takes.|
N~It's useful that he says so plainly amid all the excitement.|
N~I'd ask whether he still enjoys the game when nothing comes back.
''')
add('game_jackpot_want', 'MauvilleCity_GameCorner_Text_CantWinJackpot', 'The doll owner wants another prize but cannot win the jackpot.', '''
N~That prize has become very good at making the next attempt sound tempting.|
N~Wanting the reward does not improve the probability of obtaining it.|
N~Don't let a shelf decide how long the day lasts.|
D~It sounds as if the waiting has stopped being much fun.|
N~I'd take a break before deciding whether one more try is really worthwhile.|
N~A coveted object has appointed itself the author of an increasingly long afternoon.|
N~The jackpot continues its distinguished career as something not happening.|
N~Compare the time and coins already spent with what the prize actually means.|
N~A small longing can stretch a room until it has no visible end.|
N~It is all right to like the prize and still choose to leave it.|
N~I'd ask what drew her to that particular doll in the first place.
''')
add('game_doll_no_room', 'MauvilleCity_GameCorner_Text_YouWantItButNotNow', 'The offered spare starter doll cannot be accepted because decoration storage is full.', '''
F~The doll has been offered a home that is temporarily all furniture and no room.|
N~The transfer failed for lack of decoration capacity. It remains with her.|
N~We can return once there's space. No need to cram it in.|
N~I'm glad she leaves the offer open without sounding hurt.|
N~A nice gift deserves somewhere better than the edge of a pile.|
N~The prospective new resident has encountered a housing shortage.|
N~Our decor has developed a remarkably firm admissions policy.|
N~We should organize storage before trying the gift again.|
N~A welcome can remain warm while a place is being made.|
N~She understood that the practical problem wasn't a rejection.|
S~I'd thank her for keeping it safe in the meantime.
''')
add('game_doll_declined', 'MauvilleCity_GameCorner_Text_DontBeNegative', 'The girl presses the spare doll offer after the player declines; this branch gives no doll.', '''
F~She is still offering, but our answer hasn't quietly turned into yes.|
N~Her insistence does not complete a transfer. The doll remains unreceived.|
N~We said no. That doesn't need to become a negotiation.|
F~It is difficult when a kind offer doesn't leave room to refuse.|
N~Not wanting another doll doesn't mean we dislike her generosity.|
N~The rejected gift has returned for an unscheduled second audition.|
N~An offer determined to outlive its answer.|
N~She can keep the spare for someone who actually wants it.|
N~A freely given thing needs a freely opened hand.|
N~Calling a refusal negative is an unfair little push.|
N~I'd thank her warmly while keeping the answer clear.
''')
add('game_case_neighbor', 'MauvilleCity_GameCorner_Text_NeedCoinCaseGoNextDoor', 'A patron points the player to the neighboring woman for a Coin Case.', '''
S~A missing piece of equipment with an address conveniently attached.|
N~He has supplied a nearby lead rather than only naming the problem.|
N~Next door. We can ask without wandering town.|
N~It's kind of him to notice a beginner might need directions.|
N~We should ask the woman what she wants before assuming it's free.|
N~The obstacle has been reduced to a very short side quest.|
N~At last, advice whose destination is within ordinary walking patience.|
N~Useful local knowledge saves a lot of unnecessary searching.|
N~Someone nearby may hold the small thing that opens the next door.|
N~He gives us enough information to approach her politely.|
N~I'd ask whether he knows how she came to have a spare.
''')
add('game_local_favorite', 'MauvilleCity_GameCorner_Text_MauvilleSomethingForEveryone', 'A patron calls the Game Corner his favorite part of Mauville.', '''
S~He has found his particular corner of Mauville, very literally.|
N~Different local amenities serve different preferences. This is his.|
N~Fine place to enjoy himself, if he knows when to stop.|
S~It's nice to hear where someone feels pleased to spend an ordinary afternoon.|
N~I'd make sure the rest of his day still gets a turn too.|
S~The town receives a glowing review from one carefully chosen seat.|
S~A city judged by a single favorite room. Honest methodology, at least.|
N~I'd ask what he enjoys about the place beyond the possibility of winning.|
N~A person can find belonging in an unlikely small routine.|
N~His favorite doesn't have to become everyone's favorite for the town to work.|
S~I'd ask what else he would show a first-time visitor.
''')
add('game_roulette_rates', 'MauvilleCity_GameCorner_Text_RouletteTablesDifferentRates', 'An old man advises checking different roulette table costs against available coins.', '''
N~The tables look similar, but the little numbers have different appetites.|
N~The rate determines how quickly a fixed coin supply can be spent.|
N~Check the cost first. Easy rule to remember.|
N~I would rather understand the choice before sitting down.|
N~A little arithmetic keeps the evening from surprising the purse.|
N~The furniture is identical; the financial consequences are not.|
N~An excellent reminder to read the expensive little details.|
N~We should compare cost per play rather than just the appearance of the table.|
N~The same circle can take a different toll.|
N~Knowing the price makes the choice properly ours.|
N~I'd ask which rate he prefers and how he limits the visit.
''')
add('game_cook_time', 'MauvilleCity_GameCorner_Text_EasyToLoseTrackOfTime', 'A cook realizes the games have distracted him from returning to work.', '''
F~The clock has kept doing its job while he forgot about his.|
N~Attention-heavy activities can distort a person's sense of elapsed time.|
N~He knows he needs to go. Best stand up now.|
N~Thinking about leaving can take longer than leaving if you keep postponing it.|
N~As one cook to another: go before somebody has to cover the whole kitchen.|
N~The working day has returned to interrupt an absorbing subplot.|
N~The phrase one more minute has apparently developed several sequels.|
N~A reminder set before playing would make the next visit easier to manage.|
N~A turning game can make the rest of the day feel still. It isn't.|
N~He has noticed the problem. I hope he follows the thought through to the door.|
N~I'd offer a quick goodbye instead of another reason to stay talking.
''')
add('game_three_coins', 'MauvilleCity_GameCorner_Text_UpTo3CoinsCanBeUsed', 'A patron explains the maximum three-coin slot wager.', '''
N~Three is the ceiling, not an instruction to use the whole ceiling.|
N~A permitted maximum does not establish an optimal personal choice.|
N~We can spend less. The machine won't be offended.|
N~It's useful to know the limit before the room makes everything feel hurried.|
N~I'd decide the total for the visit before choosing the amount for one turn.|
N~The game permits a flourish; our budget may prefer restraint.|
N~A small maximum repeated often remains a potentially large total.|
N~Track the cumulative spending, not only the cost of one play.|
N~Many small circles can make a very long chain.|
N~The option should serve what we want, not choose for us.|
N~I'd ask which part of the game changes with the number used.
''')
add('game_reel_seven', 'MauvilleCity_GameCorner_Text_DifficultToStopOn7', 'A patron describes the difficult seven stop and Reel Time bonus.', '''
N~That seven has a very tiny doorway and very good evasive manners.|
N~A difficult timing condition does not become reliable through wishing.|
N~Try it for fun. Don't make a plan that needs the bonus.|
N~I can imagine feeling the missed moment long after it passes.|
N~A near miss is still a miss. Best remember that before trying all afternoon.|
N~The elusive mark has been assigned a suspenseful supporting role.|
N~A symbol with an impressively successful avoidance strategy.|
N~We should understand the timing without treating a close attempt as a guarantee.|
N~Almost can keep a person waiting far longer than never.|
N~I'd enjoy a good attempt without making the next one a debt to it.|
N~I'd ask whether he remembers his good stops more clearly than the misses.
''')
add('game_bonus_info', 'MauvilleCity_GameCorner_Text_HeresSomeSlotsInfo', 'A patron explains lightning bolts, Reel Time chances, and a rare large bonus sequence.', '''
U~That's a very long ladder of maybes before the big pile of coins.|
N~The maximum reward requires a specific sequence. Its size says little about its likelihood.|
N~Rare bonus means don't count on it. Keep the visit sensible.|
N~All those possibilities could make waiting for the best one feel endless.|
N~I would enjoy an ordinary bit of play rather than make the rare result the whole point.|
N~A spectacular ending is described in enough detail to tempt an unwary audience.|
N~An elaborate chain of conditions wearing the cheerful face of a prize.|
N~The sequence is useful to understand, but we should keep probability separate from possibility.|
N~A far light can be real without being a promise to reach it.|
N~She includes how difficult it is. That part deserves equal attention.|
N~I'd ask what a normal visit looks like instead of only the most exciting one.
''')

add('bard_decline_song', 'MauvilleCity_PokemonCenter_1F_Text_BardFeelingTheBlues1', 'The bard is disappointed that the player declined to hear his song.', '''
F~The song hasn't started, and we've already reached the sad verse.|
N~His disappointment doesn't mean our refusal was inappropriate.|
N~He can offer. We can decline without needing a reason.|
F~I understand feeling shy about sharing something, but an audience needs a choice.|
N~Maybe another listener will have more time for it.|
N~The performance has been canceled; the lament has regrettably continued.|
N~A musical refusal has produced an unrequested emotional encore.|
N~He could ask a little later instead of treating this as a final verdict.|
N~A closed ear today is not a judgment on every note.|
N~I would be kind without pretending we promised to stay.|
N~I'd wish him a good afternoon and let the moment pass.
''')
add('bard_decline_lyrics', 'MauvilleCity_PokemonCenter_1F_Text_BardFeelingTheBlues2', 'The bard is disappointed when the player declines or cancels writing lyrics.', '''
F~Enjoying a song and having spare lyrics in your head are rather different talents.|
N~Declining to write doesn't establish a negative assessment of his music.|
N~We aren't obliged to fix the song just because we heard it.|
N~Sometimes I can listen carefully and still not know what words belong there.|
N~Creative help is better when somebody actually wants to give it.|
N~The audience has been invited to become staff and politely refused.|
N~The lyrics remain his problem. A surprisingly healthy arrangement.|
N~He can keep experimenting without making a stranger responsible for the result.|
N~A word arrives more freely when it isn't pulled by the wrist.|
N~Listening was already a bit of our time. It doesn't owe the next bit.|
N~I'd thank him for singing without inventing a contribution we don't have.
''')
add('bard_new_song', 'MauvilleCity_PokemonCenter_1F_Text_IllSingThisSongForAWhile', 'The bard accepts the approved new lyrics and will keep performing the song.', '''
S~Our words have acquired legs in the form of someone else's singing.|
S~The revised lyrics are confirmed and saved as his continuing version.|
S~Good. We helped him make something he'll actually use.|
S~It's a lovely feeling when somebody gives your words a voice.|
S~A little shared work can keep making somebody happy after you leave.|
S~The collaboration has reached publication by repeated public performance.|
S~Our contribution has been sentenced to a hopefully pleasant life in song.|
S~Hearing the trial version before approving it was useful.|
S~A few words can travel on breath farther than their author.|
S~He wants to stay with the version we made together. That's a warm compliment.|
S~I'd enjoy hearing what it sounds like after he's lived with it a while.
''')
add('bard_share_song', 'MauvilleCity_PokemonCenter_1F_Text_WishICouldPlaySongForOthers', 'After the song has been changed, the bard wishes more people could hear it.', '''
S~He likes the song enough to want the room around it to grow.|
S~A satisfying result often creates an impulse to share the work.|
S~A good audience can start with one person who listens.|
S~I understand wanting a song to find the person who might need it.|
S~Something enjoyed is often something you want to pass along.|
S~The performer has become the strongest advocate for a wider engagement.|
S~A song searching for a larger room. At least it can pack lightly.|
N~He could start by asking people nearby whether they want to listen.|
S~A small voice can wish for a wider piece of air.|
S~I'd keep the invitation welcoming rather than make listening feel compulsory.|
S~I'd ask where he most enjoys singing when people are around.
''')
add('hipster_already', 'MauvilleCity_PokemonCenter_1F_Text_IAlreadyTaughtYou', 'The hipster has already taught the player and wants to share the word with others.', '''
S~Our lesson is over. The fashionable word has other appointments.|
N~He has no additional lesson for us in his present state.|
N~Fair enough. Other people can have a turn.|
S~I like that he wants to spread the conversation beyond one visitor.|
N~A little novelty is easier to enjoy when nobody keeps serving the same helping.|
S~The linguistic evangelist moves on to a promising new audience.|
N~We have received our ration of being current.|
N~We can use what we learned instead of waiting for another announcement.|
N~A little saying travels by finding another willing ear.|
N~I wonder whether the next person will use it quite differently.|
S~I'd listen for the word turning up somewhere unexpected later.
''')
add('hipster_no_new', 'MauvilleCity_PokemonCenter_1F_Text_IveGotNothingNewToTeach', 'The hipster finds the player already knows his available trendy sayings.', '''
S~We have accidentally become too up-to-date for the update desk.|
N~His available vocabulary contains no new entry for us.|
S~Then we're set. No need to force another lesson.|
S~It's pleasant when someone can just admit they've nothing to add.|
N~Knowing enough for today is a perfectly comfortable place to stop.|
M~The student has overtaken the fashionable syllabus.|
S~Our cultural currency remains valid for at least this conversation.|
N~A useful system recognizes an empty update rather than pretending there is one.|
S~A small cup can be full without needing to overflow.|
S~He doesn't turn the lack of a new saying into a competition.|
N~I'd ask what he finds interesting beyond the latest phrase.
''')
add('hipster_word_meaning', 'MauvilleCity_PokemonCenter_1F_Text_HaveYouHeardOfWord', 'The hipster teaches a phrase but tells the player to ask their parents what it means.', '''
F~He delivered the word and outsourced the explanation to our family.|
N~Knowing a term's sound is not the same as understanding its meaning.|
N~I would rather know what I'm saying before repeating it.|
F~That is an awkward amount of mystery to place inside a small word.|
N~A useful lesson should include what the new thing is actually for.|
N~The language instructor has abruptly transferred the final chapter to another author.|
N~A definition conspicuously absent from the lesson. How fashionable.|
N~I'd ask someone who can explain the context clearly.|
N~A word can leave a mouth before it finds a meaning. Better to wait.|
N~Being current isn't worth accidentally saying something you don't understand.|
N~I'd ask where he heard it used, then work out whether it belongs in our speech.
''')
add('trader_refusal', 'MauvilleCity_PokemonCenter_1F_Text_TraderFeelingTheBlues', 'The decoration trader is disappointed that the player declines his initial offer.', '''
N~We declined the furniture, not his entire existence. An important distinction.|
N~A rejected proposal isn't a rejection of the person offering it.|
N~No trade today. He can put the guilt away.|
F~I wish he didn't make a simple answer sound like we hurt him.|
N~Maybe another visitor will want exactly what he's brought.|
N~The opening offer has been declined; the emotional negotiation persists.|
N~An unexpectedly melancholy introduction to used furniture.|
N~An exchange works best when both people have a clear use for it.|
N~A door can remain friendly even when it doesn't open to barter.|
N~His disappointment is real, but it doesn't become our obligation.|
N~I'd keep the farewell kind and the answer steady.
''')
add('trader_done_before', 'MauvilleCity_PokemonCenter_1F_Text_WeveAlreadyTraded', 'The decoration trader reminds the player that their allowed trade is already complete.', '''
S~He remembers our furniture transaction better than I remember my own pockets.|
N~The existing trade record prevents another exchange in this state.|
N~Already done. We can leave him to it.|
N~It's nice that he recognizes the earlier meeting.|
S~One fair exchange is a perfectly good result for a visit.|
N~The completed bargain declines to be cast as a recurring scene.|
N~The furniture has moved on. We should perhaps do the same.|
N~We can work with the decoration we received instead of trying to repeat the process.|
N~Some meetings leave a single object behind and are complete.|
N~He is setting a clear limit without turning it into a dispute.|
N~I'd ask how the decoration we gave him is working out.
''')
add('trader_no_selection', 'MauvilleCity_PokemonCenter_1F_Text_YouDontWantAnything', 'The player cancels selecting a decoration, and the trader feels unwanted.', '''
N~His collection didn't fit our plans. That isn't a verdict on the man carrying it.|
N~No preferred item was selected. That does not imply a personal judgment.|
N~We're allowed to look and leave. No need for this.|
F~I might like him better if choosing nothing felt safer.|
N~A room only has so much space, and tastes differ.|
N~The catalog has failed to produce a sale and taken it rather personally.|
N~A rejected desk is apparently a rejected soul now.|
N~We should choose for an actual use, not to avoid disappointing the seller.|
N~A thing can be lovely without belonging in our home.|
N~I would reassure him briefly without pretending to want something.|
N~I'd thank him for showing the collection and let that be enough.
''')
add('trader_no_own_decor', 'MauvilleCity_PokemonCenter_1F_Text_YouDontHaveAnyDecor', 'The trade cannot proceed because the player owns no decorations to exchange.', '''
F~We have arrived at the swap with an extremely minimalist contribution.|
N~An exchange requires an item from both parties. We have none eligible to offer.|
N~Nothing to trade. We'll come back when that changes.|
N~I suppose a bare room leaves a lot of room for future plans.|
N~No sense promising something we don't have.|
N~The barter scene is missing half its essential props.|
N~Our impeccable lack of clutter has become temporarily inconvenient.|
N~We need to obtain a decoration before this service can apply.|
N~An empty shelf is a beginning, not a failure.|
N~It's an understandable mistake for a first visit.|
N~I'd ask where beginners usually find something worth exchanging.
''')
add('trader_keep_own', 'MauvilleCity_PokemonCenter_1F_Text_YouDontWantToTrade', 'The player cancels offering their own decoration, and the trader is disappointed.', '''
N~Wanting his decoration didn't mean we had to stop liking our own.|
N~The player declined the proposed outgoing item. No exchange was completed.|
N~Keep what matters to us. A trade has to be worth both sides.|
N~Sometimes you don't notice an attachment until someone asks you to give it away.|
N~We can appreciate the offer and still want to keep our familiar things.|
N~A coveted acquisition has failed to defeat an existing attachment.|
N~The furniture has successfully appealed against relocation.|
N~It's useful to compare the real cost before confirming a change.|
N~A familiar object can hold a place no new thing quite fills.|
N~He can be disappointed without turning our preference into a personal slight.|
N~I'd ask ourselves which decoration we'd genuinely be comfortable parting with.
''')
add('trader_no_room', 'MauvilleCity_PokemonCenter_1F_Text_YouveNoRoomForThis', 'The decoration trade fails because its category storage is full.', '''
N~Our collection has shut the door before the new decoration could introduce itself.|
N~The relevant category is at capacity. The exchange did not complete.|
N~Sort the storage first. No reason to lose track of what we have.|
N~I would rather make a deliberate place than hurry something out of the way.|
N~A roomful of things should still leave room to use them.|
N~The proposed new resident has been declined by the housing office.|
N~Abundance has once again become an administrative problem.|
N~We should check category capacity, not just the total number of objects.|
N~A collection can ask us to pause and look at what is already there.|
N~Wanting one more thing is a good time to reassess the whole arrangement.|
N~I'd choose what to keep before coming back to bargain.
''')
add('trader_success', 'MauvilleCity_PokemonCenter_1F_Text_SendDecorToYourPC', 'The decoration exchange has completed and the trader sends the new decoration to storage.', '''
S~Two decorations get new homes, and two people get a little change of scenery.|
S~The completed exchange updates both collections as agreed.|
S~Done. Let's remember what we traded away.|
S~I wonder how the familiar room will feel with that one detail changed.|
S~It's nice when two people can each make use of the other's spare thing.|
S~The cast has traded props, and both sets can begin their redesign.|
S~A successful rearrangement without carrying furniture down the street. Civilized.|
N~We can inspect the received decoration and plan where it fits.|
S~A once-familiar thing will begin a different little history elsewhere.|
S~The best exchange feels chosen on both sides.|
S~I'd enjoy seeing how the decoration changes the room once it's placed.
''')
add('storyteller_decline', 'MauvilleCity_PokemonCenter_1F_Text_StorytellerFeelingTheBlues', 'The storyteller is disappointed that the player declines or cancels hearing a tale.', '''
N~A story can wait until the ears have time to sit down properly.|
N~Choosing not to listen now is not a judgment on the tale's quality.|
N~We can leave. An audience isn't something he's owed.|
F~I'd rather hear a story when I can actually give it my attention.|
N~Good company lets a person have somewhere else to be.|
N~The narrator has found a listener with an inconveniently independent schedule.|
N~The legend will have to survive another hour without our assistance.|
N~He could offer a shorter version instead of treating the refusal as a disaster.|
N~An untold story can remain safe for another day.|
N~A disappointed host can still accept a kind farewell.|
N~I'd ask when he is usually here if we want to return.
''')
add('storyteller_not_legend', 'MauvilleCity_PokemonCenter_1F_Text_NotWorthyOfLegend', 'The storyteller judges the player supplied accomplishment insufficiently legendary.', '''
N~Our day was still ours, even if it doesn't fit his enormous story hat.|
N~His threshold for legend is a preference, not a measure of our experience's value.|
N~We don't need to turn the trip into a performance for him.|
N~Small stories matter to the people who were there too.|
N~An ordinary good day doesn't have to become an epic to be worth having.|
N~The editor requests a larger explosion of significance. I respectfully disagree.|
N~A perfectly adequate life has failed the dramatization requirements.|
N~I'd ask what qualifies before trying to satisfy a vague target.|
N~A quiet moment can remain dear without becoming a monument.|
N~He can want a grand tale. We can still value the one we brought.|
N~I'd rather hear why the event mattered than how impressive the count sounds.
''')
add('storyteller_our_record', 'MauvilleCity_PokemonCenter_1F_Text_YouDidStatXTimes', 'The storyteller enthusiastically turns a buffered player activity count into a new legend.', '''
U~An ordinary habit has put on a cape while we weren't watching.|
N~The count is real; the interpretation as a legend is his embellishment.|
S~Glad he's enjoying the story. We still know what the days actually felt like.|
F~It's odd hearing a little routine described as something enormous.|
S~There must be a lot of ordinary effort tucked inside that number.|
S~Our daily life has acquired a narrator with a generous scale of importance.|
S~A statistic has escaped its ledger and become folklore.|
N~I'd keep the measurement separate from the more colorful conclusion.|
N~Many small moments can gather into a shape we never noticed forming.|
S~His delight is real, even if the grand title is a bit much.|
S~I'd tell him one detail the number doesn't capture.
''')
add('storyteller_more_legends', 'MauvilleCity_PokemonCenter_1F_Text_CouldThereBeOtherLegends', 'After telling a recorded tale, the storyteller wonders about other undiscovered Trainer stories.', '''
S~Somewhere, another Trainer is doing something ordinary that he could make enormous.|
N~A limited collection should invite further observation rather than a claim of completeness.|
N~Plenty of people out there. Ask them what they've done.|
S~There are probably quiet stories nobody has thought to ask about.|
N~I'd listen to people who don't expect their day to sound impressive.|
S~An anthology has discovered the excellent problem of having more possible chapters.|
N~The world contains a regrettable surplus of untapped anecdotes.|
N~He could gather accounts from different towns instead of only comparing large totals.|
N~A road can hold stories that have never needed an audience.|
S~His curiosity might be kinder if it leaves room for modest lives too.|
S~I'd ask whose story surprised him most when he first heard it.
''')
add('giddy_decline', 'MauvilleCity_PokemonCenter_1F_Text_GiddyFeelingTheBlues', 'Giddy is disappointed that the player declines his opening story invitation.', '''
N~His story wanted a listener, but our afternoon hasn't signed the agreement.|
N~Declining the invitation is a normal limit, not evidence of unkindness.|
N~Not today. We can say it gently and still mean it.|
F~I don't like disappointing people, but sometimes I need a quieter moment.|
N~A friendly offer needs room for a friendly no.|
N~The forthcoming anecdote has encountered a scheduling conflict.|
N~We have spared ourselves an unknown quantity of scintillation.|
N~He could ask whether another time would suit us better.|
N~A story can wait beside its teller without being abandoned.|
N~I'd keep the farewell warm without pretending we can stay.|
N~I'd leave him free to find someone who actually has time to listen.
''')
add('giddy_goodbye', 'MauvilleCity_PokemonCenter_1F_Text_WeShouldChatAgain', 'Giddy finishes his variable anecdotes and warmly invites another conversation.', '''
S~He found the end of his thoughts! I was beginning to wonder where it lived.|
S~The exchange has reached a clear closing without requiring agreement on every detail.|
S~A friendly goodbye. Good place to leave it.|
S~I like that he enjoyed simply having someone listen.|
S~A chat can be a good part of the day without needing to solve anything.|
S~The wandering monologue has discovered a cheerful exit.|
S~The final sentence has arrived. I welcome it warmly.|
N~We can appreciate the conversation and still make room for the rest of our plans.|
S~A few shared words can leave a small warmth after the voices stop.|
S~His invitation sounds sincere, even if his sense of a short chat is adventurous.|
S~I'd wave goodbye and remember which thought made us smile.
''')

add('paci_return_frustration', 'PacifidlogTown_House2_Text_ExplainReturnFrustration', 'The Fan Club chairman brother explains how affection affects Return and Frustration after a TM gift.', '''
N~A move can show how things are going between partners. That's worth listening to.|
N~The two moves depend on opposite ends of the friendship measure.|
N~I'd rather build trust than build a plan around a partner resenting us.|
N~A feeling becoming power doesn't make the unhappy feeling something to seek.|
N~Keep the relationship healthy. The battle plan should work around that.|
N~A relationship becomes a mechanic, without ceasing to be a relationship.|
N~An effective grievance is still a grievance.|
N~We should choose moves that fit a well-treated partner rather than manipulate distress.|
N~Power can come from a feeling without telling us that feeling is good to cultivate.|
N~The explanation is useful. The partner's comfort matters beyond the number.|
N~I'd watch how our Pokemon feels about us outside battle too.
''')
add('paci_tm_wait', 'PacifidlogTown_House2_Text_GetGoodTMInXDays', 'The weekly TM recipient is told how many days remain before another suitable TM is available.', '''
N~His supply schedule is slower than our ability to ask again.|
N~A timed interval gates the next gift. The stated wait is the relevant constraint.|
N~We'll come back later. No point standing over him.|
S~It's nice to have a reason to stop by again after some time has passed.|
N~We have plenty else to do while he waits for the next supply.|
N~The next installment has a release date rather than a second copy today.|
N~The calendar has declined an encore.|
N~We can note the wait without repeatedly checking the same visit.|
N~Some things arrive with days, not persistence.|
N~He's offering a future kindness, not promising an endless handful now.|
N~I'd plan another visit around the trip rather than make the wait the whole purpose.
''')
add('paci_moderate_friendship', 'PacifidlogTown_House2_Text_PutInSomeMoreEffort', 'The chairman brother judges the player Pokemon bond moderate and asks for more effort.', '''
N~We don't need a grand trick. We need to keep showing up kindly.|
N~The assessment suggests an ordinary middle range, not hostility.|
N~Spend good time together. No need to panic over a middling report.|
N~There is room to get closer without making the present sound terrible.|
N~A dependable meal and a gentle routine are useful effort.|
N~The reviewer requests development rather than a dramatic rescue.|
N~Neither disaster nor triumph. A suspiciously normal result.|
N~We can learn which parts of the routine our partner actually enjoys.|
N~A bond can be growing before it looks remarkable.|
N~I'd take the useful suggestion without turning affection into an exam.|
N~I'd notice the small signs of comfort before looking for a bigger verdict.
''')
add('paci_azurill_happy', 'PacifidlogTown_House2_Text_VeryFriendlyWithTrainer', 'An Azurill interaction ends with an observation that it is friendly with its Trainer.', '''
S~That little Azurill has a familiar person it is very glad about.|
S~Its behavior suggests comfort and a strong association with its Trainer.|
S~Good. A small partner should feel safe beside its person.|
S~You can hear a little warmth even in a short meeting.|
S~I like seeing the result of ordinary care in a place like this.|
S~A small cast member provides the most convincing reference for its companion.|
S~A content little creature. An adequately persuasive argument for kindness.|
N~It's useful to notice these small signals, not only obvious distress.|
S~A little body can carry a great deal of trust.|
S~Comfort often shows in how little someone feels they need to guard.|
S~I'd watch how it turns toward the person it knows.
''')
add('paci_azurill_unhappy', 'PacifidlogTown_House2_Text_DoesntLikeTrainerVeryMuch', 'An Azurill interaction ends with an observation of low affection for its Trainer.', '''
D~That little one doesn't seem comfortable with the person who should be helping.|
N~The observed behavior suggests a weak bond. It warrants attention rather than ridicule.|
N~Its Trainer needs to notice that and change something.|
D~I'd give it space instead of asking it to be friendly for us.|
N~The next useful thing is a gentler routine, not blaming the Azurill.|
N~A small character has supplied an unfavorable review without being given words.|
N~Unhappiness is not improved by calling the unhappy one difficult.|
N~We don't know the whole history, but the signal deserves a response.|
D~A small guarded creature can make a room feel suddenly less warm.|
N~I would watch what makes it tense before deciding what it needs.|
N~I'd rather ask how to help than turn the reaction into a spectacle.
''')
add('paci_dex_wish', 'PacifidlogTown_House3_Text_IsThatAPokedex', 'A resident admires the player Pokedex and the varied Pokemon encounters behind it.', '''
S~The little book looks exciting because of all the meetings tucked inside it.|
S~A record can make experiences visible to someone who has not traveled the same route.|
S~They can start with what's nearby. A journey doesn't need to begin far away.|
S~I like that they're imagining the meetings, not just the filled pages.|
S~There are stories behind the entries we probably forget to tell.|
S~An ordinary carried object has become a window onto someone else's adventure.|
N~The catalog has inspired understandable dissatisfaction with staying home.|
N~I'd show a local entry first and explain what we observed.|
S~A small page can point toward a very wide world.|
N~We can share the interesting parts without making their own life sound smaller.|
S~I'd ask which Pokemon they most want to meet for themselves.
''')
add('paci_trade_decline', 'PacifidlogTown_House3_Text_NotDesperateOrAnything', 'The birthday Pokemon owner awkwardly insists he is not desperate after the player declines a trade.', '''
S~That was an impressively casual sentence carrying a rather heavy disappointment.|
N~He is trying to preserve his composure after a rejected proposal.|
N~Let him keep his dignity. No trade is fine.|
F~I know the voice people use when they hope nobody noticed the sting.|
N~We can be kind without reopening the bargain out of guilt.|
M~A wounded salesman has attempted to disguise himself as an uninterested bystander.|
S~Absolutely unconcerned, as announced at extraordinary length.|
N~A trade needs two willing people. His eagerness doesn't change that.|
N~A wish can retreat behind a deliberately careless voice.|
S~I'd let the recovery stand rather than tease him about it.|
N~I'd ask about the birthday catch if he still wants to chat.
''')
add('paci_trade_wrong', 'PacifidlogTown_House3_Text_WontAcceptAnyLessThanRealMon', 'The trader refuses the wrong species for the Bagon request.', '''
F~Our perfectly real Pokemon is simply real in the wrong category.|
N~The selected species does not meet the exchange condition.|
N~Wrong species. We can stop here or return with the requested one.|
N~I would rather not make our partner stand there feeling unwanted.|
N~He has a specific wish. This one isn't it.|
N~The candidate is genuine, but has arrived for a different role.|
N~An authentic Pokemon has failed an authentic species check.|
N~We should verify the request before choosing another partner.|
N~A refusal to exchange does not diminish the creature beside us.|
N~He could be clear without sounding as if we offered a forgery.|
N~I'd double-check what he wants before attempting the trade again.
''')
add('paci_trade_success', 'PacifidlogTown_House3_Text_ItsSubtlyDifferentThankYou', 'The trade completes and the recipient compares the new Pokemon with his previous one.', '''
S~He's already noticing the new partner instead of treating the trade like a finished errand.|
N~Comparing familiar traits can help him begin observing the unfamiliar Pokemon.|
S~Good. Now he needs to learn what this partner actually needs.|
S~The little differences are where you start knowing someone.|
S~A new home begins with paying attention, one small habit at a time.|
S~The new character has earned a closer reading than a glance at the species name.|
N~Subtly different may become considerably different once it has opinions about dinner.|
N~He should compare care requirements rather than assume the resemblance is enough.|
S~A familiar outline can hold a very different presence.|
S~He's curious. That's a better beginning than expecting an exact replacement.|
S~I'd ask what he notices once the partner has settled in.
''')
add('paci_trade_after', 'PacifidlogTown_House3_Text_ReallyWantedToGetBagon', 'After trading, the recipient explains he especially wanted a Bagon raised by another Trainer.', '''
S~He wanted a Bagon with a journey already tucked into its little history.|
N~He values the previous Trainer's involvement as well as the species itself.|
N~Then he should respect the work someone already put into that partner.|
S~It's nice to know the earlier part of its life matters to him.|
N~I'd ask about its habits before assuming a new home should mean a new routine.|
S~A character with an existing first chapter was exactly what he hoped to meet.|
S~He wanted a history, not merely a specimen. Reasonable distinction.|
N~Information from the previous Trainer can make the transition easier.|
S~A borrowed beginning can become a carefully continued story.|
S~That is a thoughtful preference if it comes with thoughtful care.|
S~I'd tell him one familiar thing the Bagon might miss.
''')
add('paci_sky_rest', 'PacifidlogTown_House4_Text_PeopleSawHighFlyingPokemon', 'A woman wonders where the high-flying Pokemon rumored over Hoenn rests.', '''
N~Even a very grand sky Pokemon probably appreciates somewhere to put its feet.|
N~Reported sustained flight raises useful questions about resting behavior.|
N~Interesting sighting. I'd want a location before going looking.|
S~I like that she wonders whether it gets tired.|
N~A creature can be impressive and still need a peaceful place to rest.|
S~The legend acquires an unexpectedly domestic question: where does it sleep?|
N~A powerful being with possible accommodation needs. Humanizing, somehow.|
N~I'd compare sighting times instead of assuming it never lands.|
N~Something high above us may still know the comfort of a sheltered place.|
S~She sees a living creature behind the astonishing report.|
N~I'd ask who saw it most clearly and whether they watched it descend.
''')
add('paci_sky_child', 'PacifidlogTown_House4_Text_SkyPokemon', 'A child excitedly repeats the idea of a sky Pokemon.', '''
U~Two words, and the whole ceiling feels too low for the excitement.|
S~A striking possibility can hold a child's attention without much explanation.|
S~She's excited. Let her enjoy wondering.|
S~I like hearing a little voice make the world feel enormous.|
S~That is the sort of thought that makes you forget your snack for a moment.|
S~An entire epic premise, announced twice for emphasis.|
S~Concise and enthusiastic. An unusually efficient legend.|
N~I'd ask what she thinks it looks like before offering our own guess.|
S~A small voice can reach up toward a very wide thing.|
S~She has found a thought she simply likes saying.|
S~I'd ask where she looks when she hopes to see it.
''')
add('paci_ancestors', 'PacifidlogTown_PokemonCenter_1F_Text_AncestorsLivedOnBoats', 'An elder recounts Pacifidlog ancestors spending entire lives aboard boats while searching for something.', '''
N~An entire life on a boat makes finding land sound like a major change of furniture.|
N~The account preserves a lifestyle clearly, but leaves the search target unspecified.|
N~That takes endurance. I wonder what kept them going.|
N~Born and growing old with the water always just beneath you.|
N~They must have known the work of making a small space into home.|
N~A generational voyage whose destination has fallen out of the surviving account.|
N~A lifetime at sea. I would have several strongly worded concerns.|
N~I'd compare family accounts to see whether any preserve the missing purpose.|
N~A home can move for years while the same question travels inside it.|
N~The search mattered enough to shape how whole families lived.|
N~I'd ask which parts of that boat life still show in the town today.
''')
add('paci_corsola', 'PacifidlogTown_PokemonCenter_1F_Text_OnColonyOfCorsola', 'A resident presents the claim that Pacifidlog rests on a Corsola colony.', '''
U~Our downstairs neighbors might be an entire colony with very important structural duties.|
N~That claim would make the settlement's ecology particularly important to understand.|
N~If it's true, they need to look after what's supporting them.|
N~It makes every ordinary step feel a little more connected to something living.|
N~A whole town should be careful about what it sends into the water below.|
U~The foundation may have a much larger cast than the population records suggest.|
N~A living foundation. I would like the maintenance agreement explained.|
N~I'd want to know how the platforms are supported without harming the colony.|
N~A home may rest on many small lives that go unseen.|
N~It's a lovely story, and one that deserves practical care if it is true.|
N~I'd ask whether anyone can show us where the Corsola gather.
''')
add('paci_card_copper', 'PacifidlogTown_PokemonCenter_1F_Text_WhatColorTrainerCard', 'A girl proudly says her Trainer Card is copper and asks about the player card.', '''
S~She sounds proud enough of copper to make it look shiny from here.|
S~The card color provides a compact symbol of recorded accomplishments.|
S~Good for her. Ask what she did to earn it.|
F~I would rather hear the story than compare which color is ahead.|
S~A little mark can stand for a lot of work somebody remembers.|
S~The credentials have become a pleasantly portable conversation starter.|
S~A social introduction conducted through metallic stationery.|
N~I'd ask which achievement changed it most recently.|
S~A small color can hold a long stretch of effort.|
S~She wants to share pride. We can receive that without making it a ranking.|
S~I'd ask which part of earning it she enjoyed most.
''')
add('verd_league_skill', 'VerdanturfTown_House_Text_TrainersGatherAtPokemonLeague', 'A resident describes the exceptionally skilled Trainers gathering at the distant League.', '''
N~A faraway room full of people who've also done a lot of walking and practicing.|
N~A selective challenge attracts competitors with substantial experience.|
N~Then we prepare seriously before going.|
N~It sounds distant in more than just miles.|
N~Strong Trainers still need ordinary good habits to keep their teams well.|
N~A formidable cast assembled at the far end of a very long introduction.|
N~An intimidating concentration of people with excellent battle plans.|
N~We can work toward the specific skills needed instead of fearing a vague reputation.|
N~A distant gate grows less mysterious one learned lesson at a time.|
N~Their skill can be something to learn from, not only something to fear.|
N~I'd ask whether the speaker has seen a League battle firsthand.
''')
add('verd_faith', 'VerdanturfTown_PokemonCenter_1F_Text_FaithInYourPokemon', 'A resident argues that successful Trainers need faith in their Pokemon.', '''
N~Trusting a partner also means noticing when it needs help, not just cheering louder.|
N~Trust is useful when grounded in knowledge of the partner's actual abilities.|
N~Believe in them, and make decisions that protect that trust.|
N~I like confidence that leaves room for a partner to be tired.|
N~Faith should come with the daily care that makes it reasonable.|
N~A stirring principle, improved considerably by the practical work underneath it.|
N~Belief is welcome. It should not be used as a substitute for a healing item.|
N~Knowing the partner well makes trust more than optimistic guessing.|
N~To believe in a creature is also to believe what its distress tells us.|
N~They deserve support before the final battle as much as during it.|
N~I'd ask what the speaker does when a trusted plan still goes wrong.
''')
add('verd_tent_reason', 'VerdanturfTown_PokemonCenter_1F_Text_VisitForBattleTent', 'A resident assumes visitors come for the Battle Tent, then considers a personal visit.', '''
S~The town's biggest attraction has competition from simply wanting to see somebody.|
N~Public attractions and personal connections both explain travel.|
S~Could be either. People are a good reason to come somewhere.|
S~Sometimes one familiar person makes a whole town feel worth the trip.|
S~A visit and a shared meal can be the entire plan.|
S~The tourist brochure makes a gracious concession to the existence of relationships.|
S~An itinerary featuring a person instead of a building. Sensible.|
N~It's useful to ask rather than settle on the first assumption.|
S~A place can become important because someone waits there.|
S~I like that they leave room for the quieter reason in the end.|
S~I'd ask who they would travel to another town to see.
''')
add('verd_aunt_worry', 'VerdanturfTown_WandasHouse_Text_IfAnythingHappenedToWally', 'Wally aunt fears being unable to face his parents if he is hurt.', '''
D~She is carrying worry for Wally and the weight of someone else's trust.|
N~Responsibility to family can intensify uncertainty when a young person travels alone.|
N~She needs reliable news about him, not another frightening guess.|
D~It is hard to let someone grow when you promised to keep them safe.|
N~I'd help her get a clear message rather than tell her simply not to worry.|
N~His adventure has left a second story of anxious waiting at home.|
D~An absent child can fill a room with very loud possibilities.|
N~A regular way to check in could help without taking his independence away.|
D~Love can hold fear in both hands and still wish to let go.|
N~She wants to do right by him and by his parents. That's a difficult balance.|
N~I'd ask when she last heard directly from Wally.
''')
add('verd_uncle_absent', 'VerdanturfTown_WandasHouse_Text_WallySlippedOff', 'Wally uncle learns that he has left on his own.', '''
N~Wally has made a decision, and the news is only now catching up with home.|
N~The lack of advance notice is a separate concern from his ability to travel.|
N~Find out where he went before assuming the worst.|
D~That first moment of realizing someone isn't where you expected is awful.|
N~A short message would spare the people at home a lot of guessing.|
N~The young adventurer has left the supporting cast without its next scene.|
N~Independence has neglected to file its departure notice.|
N~We should gather a recent location and a way to contact him.|
N~An empty place can suddenly feel like a question.|
N~He can be capable and still owe his family a little notice.|
N~I'd ask who saw him most recently and what he said about his plans.
''')
add('verd_aunt_evergrande', 'VerdanturfTown_WandasHouse_Text_WallyWasInEverGrande', 'After Victory Road, Wally aunt marvels that his parents would be astonished by his journey.', '''
S~That is going to be a very interesting family conversation when the news arrives.|
S~His demonstrated range has exceeded the family's earlier expectations.|
S~They should hear it from Wally if possible. He earned the telling.|
S~I imagine their surprise making room for a great deal of pride.|
S~Someone should make sure the news reaches them before the rumors do.|
S~The family's quiet child has returned in the account as a seasoned traveler.|
S~An expedition large enough to disturb several relatives' expectations.|
N~I'd help get a clear message to his parents, with the useful details.|
S~A long road can change the way home imagines the one who left.|
S~It is lovely when pride catches up with somebody's real growth.|
S~I'd enjoy hearing which part Wally chooses to tell them first.
''')
add('fortree_wingull_depart', 'FortreeCity_House4_Text_GoBirdPokemon', 'The boy sends Wingull out on its mail errand.', '''
S~The little courier is off, with considerably less packing than we need.|
N~A trained messenger can connect two places without a human escort.|
N~Hope the route is clear. Give it room to leave.|
S~There's something sweet about watching a familiar bird start a familiar task.|
S~Somebody at the other end may be looking forward to that arrival.|
S~A brief instruction launches a journey whose other chapter waits elsewhere.|
S~A remarkably concise dispatch. The bird appears to know the paperwork.|
N~I'd like to know how they taught the route reliably.|
S~A small pair of wings carries a thread between homes.|
S~The boy trusts it to know where it belongs and how to return.|
S~I'd ask who is waiting at the far end of the errand.
''')
add('fortree_wingull_return_gift', 'FortreeCity_House4_Text_WelcomeWingullTakeMentalHerb', 'The returned Wingull carries a Mental Herb that its non-Trainer owner offers; failed receipt invalidates the offer.', '''
S~Wingull brought home a little extra, and the boy found someone who might use it.|
N~He distinguishes what he owns from what he has a practical use for.|
S~Kind offer. Make sure the bird gets its welcome too.|
S~I like that his first reaction was being glad Wingull came back.|
S~A returning friend and an unexpected useful thing. A good afternoon.|
S~The courier has added an unscheduled botanical subplot to the delivery.|
S~A small bird has returned with an inexplicably excellent gratuity.|
N~I'd check the herb's use before assigning it to a partner.|
S~A journey can bring back something no one thought to ask for.|
S~He shares the find without trying to make it more important than the homecoming.|
S~I'd ask whether Wingull often returns carrying surprises.
''')

add('soot_sea_researcher', 'SootopolisCity_House5_Text_BrotherUsedToStudySea', 'A girl mentions her brother past marine research.', '''
S~Her brother studied a subject bigger than the view from the window.|
N~Past work can remain part of how a family knows someone.|
N~Sounds like someone worth asking about these waters.|
N~I wonder which part of the sea he used to come home talking about.|
S~A family remembers the ordinary person behind somebody's research.|
N~A whole professional chapter, introduced by a much shorter family sentence.|
N~The sea offers enough material to keep a sibling talking for years.|
N~I'd ask what he investigated before assuming every sea question was his specialty.|
N~A former pursuit can leave its tide in a person's life.|
N~She says it with the familiarity of a story she has heard many times.|
N~I'd ask what discovery she remembers him being excited about.
''')
add('soot_pyre_link', 'SootopolisCity_House5_Text_SootopolisMtPyreConnection', 'A former researcher describes studying a connection between Sootopolis and Mt Pyre.', '''
N~Two places that seem separate may have a longer conversation underneath them.|
S~A proposed connection calls for comparing evidence from both sites.|
N~Worth hearing what they actually found.|
N~I like discovering that a familiar place has another history beneath it.|
N~I'd ask what brought the research group to that question.|
N~Two distant settings may turn out to share a much older chapter.|
N~A suggestive connection. I trust the evidence is less vague than the introduction.|
N~I'd want to know which observations support the link and which remain uncertain.|
N~Water and mountain can keep different parts of one old memory.|
N~He sounds interested in the work even after leaving the lab.|
N~I'd ask whether there is a record we can look at together.
''')
add('soot_doll_decline', 'SootopolisCity_House6_Text_DontWantThisDoll', 'The visitor declines the Wailmer Doll and its owner expresses surprise.', '''
F~Declining a very large Wailmer is still a perfectly ordinary kind of no.|
N~The offer was declined. No decoration has been received.|
N~We can say no kindly. We don't need to fill the room to prove gratitude.|
N~I hope she knows we enjoyed visiting even without taking something home.|
N~A warm welcome is already a good thing to give someone.|
N~The prospective guest has declined to adopt the plush supporting cast.|
N~The doll has survived another proposed relocation.|
N~A gift needs a willing recipient, not just available storage.|
N~A kind visit can leave no object behind and still matter.|
N~I'd reassure her about the visit without changing an answer we meant.|
N~I'd ask about the dolls she has kept, if she still feels like talking.
''')
add('soot_doll_keep_safe', 'SootopolisCity_House6_Text_TakeGoodCareOfIt', 'The Wailmer Doll gift succeeds after this request; later storage failures replace it.', '''
S~A large soft new friend is joining the furniture. I think it will be good at sitting.|
S~The transferred decoration comes with a simple request to preserve it well.|
S~We'll give it a proper place. Kind of her to share it.|
S~She sounds attached enough to want it comfortable in its new home.|
S~A clean, dry spot and no crushing it under the supplies. Simple care.|
S~The plush newcomer arrives bearing a modest condition of continued kindness.|
S~A Wailmer with refreshingly manageable feeding requirements.|
N~We should place it where it won't get caught on rough edges.|
S~A small kindness can leave in the shape of a large soft creature.|
S~It will look best where it feels deliberately welcomed, not squeezed into a gap.|
S~I'd tell her where we plan to put it when we visit again.
''')
add('soot_doll_full', 'SootopolisCity_House6_Text_IllHoldItForYou', 'The Wailmer Doll gift cannot fit, so its owner agrees to keep it for later.', '''
N~The Wailmer is patiently waiting for our room to become less crowded.|
N~The decoration remains with her because storage prevented the transfer.|
N~We'll make room before coming back. No need to rush her.|
S~It's kind of her to make the delay feel easy.|
N~A soft gift should get a better welcome than being jammed into the last corner.|
S~The adoption has been courteously postponed pending adequate accommodation.|
N~The large doll has identified an entirely predictable spatial problem.|
N~We should organize the decoration category before another attempt.|
S~Something offered kindly can wait without turning cold.|
S~She understood that lack of room wasn't lack of appreciation.|
S~I'd thank her for keeping it while we sort things out.
''')
add('soot_dolls_love', 'SootopolisCity_House6_Text_LovePlushDolls', 'After the gift, the collector simply shares her fondness for plush dolls.', '''
S~A perfectly reasonable fondness for small faces that never argue about bedtime.|
S~A collection can offer comfort as well as visual variety.|
S~She enjoys them. That's enough reason to keep a few.|
S~I like a room with something soft to rest your eyes on.|
S~Some little things make coming home feel nicer.|
S~An entirely unembarrassed declaration of allegiance to the plush arts.|
S~Quiet companions with no interest in small talk. Understandable taste.|
N~I'd ask how she keeps the older fabric in good condition.|
S~A soft shape can hold a comforting familiarity.|
S~You can tell she enjoys choosing them, not just accumulating them.|
S~I'd ask which doll has been with her the longest.
''')
add('soot_cave_barrier', 'SootopolisCity_House7_Text_CaveMadeToKeepSomething', 'A resident wonders whether Sootopolis cave entrance was intended to keep something inside.', '''
N~That's a very different question from where the exit is.|
N~The form of a passage does not by itself establish the intention behind it.|
N~Worth being cautious. Speculation isn't proof something is trapped there.|
N~A familiar doorway feels different once somebody asks that.|
N~I'd want to know before treating the place like an ordinary shortcut.|
N~The entrance has acquired the disquieting possibility of being a lock.|
N~A cave with a possible containment function. Comforting local conversation.|
N~I'd compare the structure with actual evidence of deliberate construction.|
N~A boundary can face inward as easily as outward.|
N~She leaves room for being mistaken. That's useful with a thought this unsettling.|
N~I'd ask what feature first made her wonder about it.
''')
add('soot_size_no_seedot', 'SootopolisCity_LotadAndSeedotHouse_Text_DontHaveBigSeedot', 'The Seedot enthusiast responds to a canceled showing by inviting a future large Seedot.', '''
N~His enormous Seedot appointment will have to wait for an enormous Seedot.|
N~No specimen was shown. No size comparison has been established.|
N~We can return if we find the right partner.|
N~He sounds disappointed, but the invitation is still friendly.|
N~A very particular hobby comes with very particular visitors to wait for.|
N~The grand exhibition has been postponed through lack of its principal attraction.|
N~The search for a disproportionately impressive acorn continues.|
N~We should verify the species before another attempt.|
N~A wish can remain waiting without becoming an obligation.|
N~He knows what he wants to see. We don't need to bring something just to fill the silence.|
N~I'd ask what makes a Seedot unusually large in his experience.
''')
add('soot_size_no_lotad', 'SootopolisCity_LotadAndSeedotHouse_Text_DontHaveBigLotad', 'The Lotad enthusiast responds to a canceled showing by inviting a future large Lotad.', '''
N~The big Lotad fan is waiting for a big Lotad. At least the instructions fit together.|
N~The canceled selection leaves the size question unanswered.|
N~We haven't shown one. We can leave it at that.|
N~There is something gentle about being invited back for a small shared enthusiasm.|
N~I would ask about the pond before volunteering to find him a giant.|
N~The hall awaits its broad-leafed guest of honor.|
N~A very specialized disappointment. Manageable, fortunately.|
N~A later visit is an option, not a reason to rush out and catch something.|
N~A little house can hold a very wide expectation.|
N~His enthusiasm doesn't need to become a task for every visitor.|
N~I'd ask about the largest Lotad he has actually seen.
''')
add('soot_wrong_seedot', 'SootopolisCity_LotadAndSeedotHouse_Text_ThatsNotSeedot', 'The selected Pokemon is not Seedot and cannot enter that size comparison.', '''
F~Our candidate has many excellent qualities and one very decisive lack of Seedot.|
N~An incorrect species cannot be used for the requested comparison.|
N~Wrong species. Simple mistake.|
N~I wouldn't want our partner to think it needs to be somebody else.|
N~He asked for an acorn-shaped guest. We brought a different introduction.|
N~The exhibitor admires the arrival while rejecting the category.|
N~A flawless example of not being a Seedot.|
N~Check the selection before asking the measurement question again.|
N~A creature is not diminished by being the wrong answer to one question.|
N~His interest is narrow. That doesn't have to make the meeting unpleasant.|
N~I'd laugh softly, correct the choice, and keep the partner comfortable.
''')
add('soot_wrong_lotad', 'SootopolisCity_LotadAndSeedotHouse_Text_ThatsNotLotad', 'The selected Pokemon is not Lotad and cannot enter that size comparison.', '''
F~Definitely a Pokemon. Unfortunately not the particular leafy one on the invitation.|
N~The comparison cannot proceed with the wrong species.|
N~Our mistake. We can choose again or move on.|
N~A mismatched introduction is a small problem, not an embarrassing disaster.|
N~Nobody should expect the wrong guest to become the right one on demand.|
N~The candidate has failed only the test of possessing the requested name.|
N~A fine creature, tragically short of the required Lotadness.|
N~We should check the species before worrying about the size.|
N~What it is remains more important than what someone hoped to see.|
N~He can be excited about Lotad without dismissing the one we brought.|
N~I'd make the correction without keeping our partner on display.
''')
add('soot_seedot_small', 'SootopolisCity_LotadAndSeedotHouse_Text_SeenBiggerSeedot', 'The displayed Seedot does not exceed the enthusiast previous size observation.', '''
N~Our Seedot is still exactly Seedot-sized for itself. A perfectly respectable measurement.|
N~This specimen did not exceed the existing comparison. That is a narrow result.|
N~Fine. Our partner doesn't need to win a size argument.|
N~I like it as it is. Being larger isn't a kind of happiness.|
N~A small partner still deserves a proper welcome.|
N~The record remains intact, and the protagonist remains entirely worthy of a snack.|
N~Our acorn has declined to become monumental. Reasonable.|
N~A comparison should not turn into a reason to overtrain or overfeed it.|
N~A small tree begins without apologizing for its size.|
N~I would keep his disappointment from becoming our partner's problem.|
N~I'd ask about its habits instead of staying fixed on the measurement.
''')
add('soot_lotad_small', 'SootopolisCity_LotadAndSeedotHouse_Text_SeenBiggerLotad', 'The displayed Lotad does not exceed the enthusiast previous size observation.', '''
N~Not the largest leaf in the pond. Still a very good leaf with a Pokemon underneath.|
N~The existing size reference remains larger. Nothing else about the Pokemon was assessed.|
N~Size isn't the only thing worth knowing about our partner.|
N~I'd rather notice how comfortable it is than whether it breaks a record.|
N~It doesn't need to grow for the sake of somebody else's family argument.|
N~The championship is postponed; the ordinary charm remains undefeated.|
N~A perfectly adequate amount of Lotad.|
N~We can accept the result without trying to force a different size.|
N~A small floating leaf still holds its own place on the water.|
N~I'd give the partner some attention after being reduced to a comparison.|
N~I'd ask what makes this particular Lotad distinctive beyond the numbers.
''')
add('soot_seedot_big', 'SootopolisCity_LotadAndSeedotHouse_Text_GoshMightBeBiggerThanLotad', 'A large Seedot excites its admirer and earns an Elixir when the bag permits.', '''
U~Our Seedot has accidentally joined a very intense family debate.|
N~He observed an unusually large specimen; the cross-species claim remains his comparison.|
S~Glad he enjoyed meeting it. The partner still deserves a calm goodbye.|
F~I don't think Seedot expected to receive quite so much attention today.|
S~A happy visitor and a generous thank-you. That's a pleasant meeting.|
M~The acorn contender has entered the household championship to thunderous approval.|
S~A small species has produced a large disruption in sibling relations.|
N~We should keep the actual observation separate from declaring either species always larger.|
N~One ordinary creature has become somebody's extraordinary afternoon.|
S~His joy is infectious, even if the rivalry is rather silly.|
S~I'd remember the way his voice changed when he saw it.
''')
add('soot_lotad_big', 'SootopolisCity_LotadAndSeedotHouse_Text_WowMightBeBiggerThanSeedot', 'A large Lotad excites its admirer and earns an Elixir when the bag permits.', '''
U~A great big Lotad has become a great big point in a brotherly argument.|
N~He has a new large observation. It does not settle the size of every individual.|
S~Good to make someone happy. Let's not crowd the partner.|
S~It's sweet to see him this delighted by a Pokemon he loves.|
S~He made the meeting feel like a little celebration.|
S~The broad-leafed champion has arrived before an exceedingly receptive audience.|
S~A leaf has tipped the balance of domestic power.|
N~I'd keep track of the measurement rather than only the triumphant comparison.|
N~A familiar kind of creature can still bring an unexpected wonder.|
S~I like enthusiasm most when it leaves the Pokemon room to be comfortable.|
S~I'd ask what he noticed first: the leaf, the body, or his brother's likely reaction.
''')
add('soot_seedot_bag_full', 'SootopolisCity_LotadAndSeedotHouse_Text_BagCrammedFull1', 'The Seedot admirer cannot deliver the Elixir reward because the bag is full.', '''
N~The Seedot made an impression. The reward has failed to make an entrance.|
N~The size observation stands, but the item transfer failed.|
N~We'll make room if we want the reward. No harm done to the showing.|
N~It's nice that the good part of the meeting doesn't depend on the item.|
N~One more reason to organize the bag before accepting thanks.|
N~The award ceremony has encountered a spectacularly overqualified collection of luggage.|
N~An Elixir has been defeated by the quantity of everything else.|
N~Clear capacity before repeating the transfer attempt.|
N~A moment can remain generous even while an object must wait.|
N~The compliment arrived safely. We can sort the practical part next.|
N~I'd thank him for the thought while checking what can be stored elsewhere.
''')
add('soot_lotad_bag_full', 'SootopolisCity_LotadAndSeedotHouse_Text_BagCrammedFull2', 'The Lotad admirer cannot deliver the Elixir reward because the bag is full.', '''
N~A giant Lotad fit into the conversation more easily than one Elixir fit into the bag.|
N~The failed transfer does not undo his observation of the Pokemon's size.|
N~Sort the bag. The reward hasn't been received yet.|
N~I would rather take a calm moment than spill everything across the floor.|
N~A useful thank-you still needs somewhere safe to go.|
N~The generous finale has paused for an inventory intermission.|
N~The pocket has displayed a stronger defense than expected.|
N~We need an open item slot before this exchange can finish.|
N~A full hand cannot receive, even when the intention is warm.|
N~His excitement can survive a short delay while we make room.|
N~I'd leave the partner comfortable while we deal with the luggage.
''')
add('soot_center_strength', 'SootopolisCity_PokemonCenter_1F_Text_WallaceToughestInHoenn', 'A resident compares Wallace, his mentor Juan, and the Elite Four reputations.', '''
U~That is a very tall stack of people said to be stronger than somebody else.|
N~Training lineage and reputation do not by themselves determine an exact ranking.|
N~Enough strong people to learn from. One challenge at a time.|
N~The next room always sounds larger when someone describes the one beyond it.|
N~I'd rather ask how they prepare than keep climbing the rumor ladder.|
N~A hierarchy of formidable names, balanced carefully on the word rumored.|
N~The intimidating comparison has developed an additional intimidating comparison.|
N~We can study actual strategies without needing to settle every ranking.|
N~A long shadow can be made from several stories told together.|
N~They sound fascinated as much as afraid. That's a useful way to stay curious.|
N~I'd ask which of those Trainers they have personally watched battle.
''')

add('moss_base_brother', 'MossdeepCity_House4_Text_BrotherLikesToFindBases', 'A woman describes her brother enthusiasm for finding Secret Bases.', '''
S~Her brother treats every suspicious tree as a possible invitation.|
N~Searching for hidden places is a different interest from making one.|
N~Finding a base doesn't mean skipping a polite hello.|
S~I wonder what tiny clue makes him most certain someone lives there.|
N~I'd pack a snack if his searches take all afternoon.|
S~An amateur detective specializing in unusually decorated holes.|
S~A hobby whose success somewhat undermines its subject's name.|
N~I'd ask how he distinguishes a base entrance from an ordinary feature.|
N~A hidden place can draw someone gently away from the obvious path.|
N~Discovering something is nicest when its owner still gets a choice about visitors.|
S~I'd ask which base he remembers finding first.
''')
add('moss_base_battles', 'MossdeepCity_House4_Text_BrotherLikesToVisitBasesAndBattle', 'After League completion, the brother enjoys visiting bases for Pokemon battles.', '''
N~The hidden clubhouse has become a very personal place to arrange a battle.|
N~A visit now provides both social contact and a challenge.|
N~Ask the owner first. Their home isn't automatically an arena.|
N~I hope they find a place for the fragile things before starting.|
N~A battle is nicer when everybody has agreed and the room is ready.|
S~The secret setting has acquired a regular action sequence.|
N~Indoor combat beside treasured dolls. A confidence I do not share.|
N~I'd check the available space before letting the teams loose.|
N~A place of welcome should remain one after the challenge.|
N~The visiting part matters as much as the victory.|
N~I'd ask how they make the rules comfortable for both Trainers.
''')
add('moss_base_recognized', 'MossdeepCity_House4_Text_YouMadeSecretBaseNearX', 'The base enthusiast recognizes the area of the player Secret Base.', '''
U~Our secret has developed an address and apparently a local audience.|
N~He has associated the nearby location with our activity.|
N~He found it. We should establish when visitors are welcome.|
F~I suddenly wish I had tidied a little more carefully.|
S~A guest is fine, but some notice before arriving would be kind.|
M~The hidden retreat has failed a determined child's inspection.|
N~Secrecy has been reviewed and found wanting.|
N~I'd ask what clue gave the location away. Useful information.|
N~A hidden doorway can still be known to a careful pair of eyes.|
S~He is pleased to connect the place with a person he has met.|
S~I'd ask what he noticed first when he found it.
''')
add('moss_duo', 'MossdeepCity_PokemonCenter_1F_Text_GymLeaderDuoFormidable', 'A visitor admires the Mossdeep Gym duo coordinated attacks.', '''
N~Two opponents agreeing on a plan sounds much more worrying than two opponents merely standing there.|
N~Coordination can create effects that neither participant achieves alone.|
N~Prepare for how they work together, not only each one separately.|
N~It must be striking to see the timing come together.|
N~A good pair notices what the other is about to need.|
N~The formidable duo has earned a review consisting partly of delighted noises.|
N~A pair with functioning teamwork. A serious complication.|
N~I'd study the interaction between their moves before choosing counters.|
N~Two separate paths can make one stronger pattern.|
N~Their shared rhythm matters as much as individual confidence.|
N~I'd ask which combination made the visitor react that way.
''')
add('steven_dive', 'MossdeepCity_StevensHouse_Text_ExplainDive', 'After giving Dive, Steven explains deep-water entry and limits on resurfacing.', '''
N~Down is useful, but remembering where up works seems especially useful.|
N~Entry and surfacing conditions are not identical. Plan both before descending.|
N~Know the way back up before exploring. That's the first rule.|
N~The dark patches look different once you know they are doors.|
N~We should prepare for the whole trip, not just the exciting first plunge.|
N~A new passage opens beneath the scenery, with important restrictions on the exit.|
N~The seafloor is available. So is the possibility of poor planning.|
N~I'd keep track of surfaces we can safely return through.|
N~A hidden path still needs a remembered way home.|
N~He made sure the warning came with the invitation to explore.|
N~I'd ask what experienced divers check before entering an unfamiliar patch.
''')
add('steven_cavern', 'MossdeepCity_StevensHouse_Text_UnderwateCavernBetweenMossdeepSootopolis', 'Steven mentions the underwater cavern discovered by Stern between Mossdeep and Sootopolis.', '''
N~A place between two familiar towns that was hiding underneath the usual directions.|
S~The discovery gives us a specific location to investigate rather than a general rumor.|
N~We should learn the route before heading down there.|
N~It is strange how close something can be while nobody sees it.|
N~I'd ask what Stern found and what supplies the trip required.|
N~The map has acquired a deeper chapter between two existing headings.|
N~A local cavern, inconveniently separated from us by an ocean's worth of overhead.|
N~Knowing where it is doesn't yet tell us whether the entrance is safe.|
N~The water keeps another landscape folded beneath this one.|
N~I'd like to know whether the people studying it have concerns visitors should hear.|
N~I'd ask Steven which parts of the report are confirmed.
''')
add('steven_letter', 'MossdeepCity_StevensHouse_Text_LetterFromSteven', 'Steven letter explains his extended training journey and entrusts a Beldum to the player.', '''
S~He left room in his own journey for trusting us with someone he cares about.|
N~The letter records a deliberate choice of a new caretaker, not an abandoned possession.|
N~That's real trust. We should think carefully about taking responsibility.|
N~A quiet room feels different with somebody's goodbye waiting on the desk.|
N~I'd want to know the Beldum has a good routine ready if we accept.|
N~A departure letter becomes an introduction to a life continuing in other company.|
N~Soul-searching with an unusually substantial favor left in its wake.|
N~We can honor the request by preparing for the Pokemon's actual needs.|
N~A closed door behind one traveler can open beside another.|
N~His fondness is clear. The choice deserves more than a quick look at the Ball.|
N~I'd remember to tell him how Beldum is doing when our paths cross again.
''')
add('space_beach_unsafe', 'MossdeepCity_SpaceCenter_1F_Text_CantStrollOnBeachWithMagma', 'The Sun Stone giver says Magma presence makes his beach walks unsafe.', '''
D~They've even spoiled the simple business of going for a walk.|
N~A security threat affects ordinary movement beyond the targeted facility.|
N~Stay where it's safe for now. A beach walk can wait.|
D~It is a small loss inside the large trouble, but it still matters.|
N~People deserve to enjoy their neighborhood without planning around criminals.|
N~The villainy has interrupted a chapter that should have needed no conflict at all.|
N~A quiet stroll. Apparently too much to ask of an occupied island.|
N~We should make sure the routes people use every day are secure too.|
D~A familiar shore can feel far away when fear stands in the path.|
N~He isn't asking for anything extravagant, just his normal day back.|
N~I'd ask where he feels safe waiting while this is dealt with.
''')
add('space_meteors', 'MossdeepCity_SpaceCenter_1F_Text_HoennFamousForMeteorShowers', 'The Sun Stone giver mentions Hoenn long-standing meteor showers.', '''
S~Hoenn has apparently been receiving little sparkly visitors for quite a while.|
S~A long record of sightings could reveal useful seasonal patterns.|
N~Worth seeing from somewhere safe and quiet.|
S~I like imagining people watching the same sky long before we arrived.|
S~A night outside with something warm to drink would suit that nicely.|
S~The sky has maintained a very old habit of giving people stories.|
S~A celestial event with the courtesy to occur above most conversation.|
N~I'd ask where local observers get the clearest view.|
S~A brief light can join many generations in the same upward glance.|
S~Something spectacular can still belong to ordinary people looking up together.|
S~I'd ask which meteor shower he remembers most vividly.
''')
add('space_launch_precision', 'MossdeepCity_SpaceCenter_1F_Text_RocketLaunchDemandsPerfection', 'A scientist explains that small faults can compromise launches but the dream motivates continued work.', '''
N~A rocket is a very large argument for checking the tiny parts.|
N~A critical subsystem failure can invalidate the performance of the whole vehicle.|
N~Then every check deserves the time it takes.|
N~It must be tiring to care that much about every small thing.|
N~The people doing the checking need rest too. Tired eyes miss details.|
N~A magnificent dream rests on a multitude of deliberately unromantic inspections.|
N~The exciting achievement depends on an exhausting quantity of being correct.|
N~Perfection is an ambition; repeated testing and redundancy are how you approach reliability.|
N~A great upward light begins with many patient hands on the ground.|
N~Their care is part of the achievement, even when nobody sees the checks.|
N~I'd ask what they learned from the last fault they caught before launch.
''')
add('space_threat_minor', 'MossdeepCity_SpaceCenter_1F_Text_MagmaHaveSightsOnSpaceCenter', 'A scientist is determined to continue the launch despite Magma targeting the center.', '''
N~Determination is good. Calling thieves minor doesn't make their hands smaller.|
N~Maintaining the schedule should not override a credible security risk.|
N~Secure the people and fuel first. The launch can wait if it has to.|
N~I understand not wanting to let them take the day away.|
N~The people here matter more than keeping the plan on time.|
N~The heroic refusal to be delayed should leave room for a sensible safety check.|
N~A minor incident involving criminals and rocket fuel. An interesting definition.|
N~They need to evaluate the threat as a real system hazard.|
N~A dream should not require pretending the danger is small.|
N~His resolve is admirable. The staff still deserve a plan that protects them.|
N~I'd ask who is coordinating security while the launch team works.
''')
add('space_steven_watch', 'MossdeepCity_SpaceCenter_1F_Text_StevenMagmaCantBeAllowedToTakeFuel', 'Steven is watching for Team Magma planned fuel theft and suggests the player inspect the town meanwhile.', '''
N~Someone dependable is watching the fuel. That makes the room feel a little steadier.|
N~He separates what is known about the threat from the still-unknown motive.|
N~Good. We'll stay alert and keep out of the staff's way.|
N~It helps that he sounds serious without making everyone panic.|
N~People nearby may need information as much as another worried face.|
N~A capable ally keeps guard while the wider setting waits to be understood.|
N~Competence and uncertainty in the same sentence. Reassuringly honest.|
N~We can learn the town's layout while he monitors the immediate target.|
N~A calm person can hold a little space against a gathering disturbance.|
N~He's giving us room to act without pretending we already know the whole plan.|
N~I'd ask who to tell if we notice anything unusual around town.
''')
add('space_good_weather', 'MossdeepCity_SpaceCenter_2F_Text_MossdeepIdealForRockets', 'A scientist explains that Mossdeep sunshine and stable winds favor rocket launches.', '''
S~Even a rocket appreciates the sky behaving itself before it leaves.|
S~Predictable weather reduces one important source of launch uncertainty.|
N~Good reason to build here. Still check the conditions every time.|
N~I like learning why a place suits the work people chose for it.|
N~Some jobs begin with finding the right day, not just the right tools.|
N~The spectacular launch has a surprisingly mundane ally in reliable weather.|
N~A location selected partly for its lack of atmospheric drama. Sensible.|
N~A good site removes problems before the design has to solve them.|
N~A steady wind can help carry an ambitious wish beyond it.|
N~The place is part of what makes their work possible.|
N~I'd ask what weather change makes them postpone a launch.
''')
add('space_fuel_motive', 'MossdeepCity_SpaceCenter_2F_Text_WhyWouldMagmaStealRocketFuel', 'A scientist is puzzled by Magma motive for stealing rocket fuel.', '''
N~Not knowing their reason doesn't make a missing tank sound any better.|
N~The target is clear even though the intended application remains uncertain.|
N~Stop the theft first. Work out the motive without handing them the fuel.|
N~It must be unnerving when someone wants something dangerous and won't explain why.|
N~They shouldn't have to guess what harm their own supplies might be used for.|
N~The villains have supplied a destination for the theft but omitted its final act.|
N~Rocket fuel and criminal intent. An adequate reason for concern without further detail.|
N~We can assess the immediate storage risk while investigating the rest.|
N~A hidden purpose can still cast a very visible threat.|
N~The uncertainty makes clear information especially important.|
N~I'd ask what quantities they threatened to take and who heard the warning.
''')
add('space_astronaut_try', 'MossdeepCity_SpaceCenter_2F_Text_WouldveLikedToBeAstronaut', 'An elder rejects his own thought that age makes astronaut ambition too late and resolves to try.', '''
S~He caught his own dream trying to slip out the door and invited it back.|
N~The next useful question is what requirements he can realistically work toward.|
S~Good. Find out what's needed before deciding for himself that it's impossible.|
S~I liked hearing the hesitation change into a little courage.|
S~There is something lovely about giving an old wish a fresh morning.|
S~A regret revises itself into the opening line of a new attempt.|
S~An ambition has successfully appealed against premature retirement.|
N~He can ask about training and see which concrete steps remain available.|
S~An old seed may still answer when someone brings it water.|
S~Trying doesn't have to mean pretending it will be easy.|
S~I'd ask what part he wants to learn first.
''')
add('space_astronaut_threat', 'MossdeepCity_SpaceCenter_2F_Text_MagmaCantGetAwayWithThis', 'The aspiring astronaut fears fuel theft will end his spaceflight hopes.', '''
N~They aren't only taking fuel. They're trying to carry off somebody's next chance.|
N~The threatened resource supports a program that people have committed hopes to.|
N~He deserves a safe chance to try. Keep the fuel secured.|
D~He had just given himself permission to want this.|
N~It's cruel to make people fight for the ordinary chance to pursue a dream.|
N~A personal ambition becomes collateral in someone else's grand plan.|
N~The thieves have found a very efficient way to become universally disliked.|
N~Security protects the future use of the fuel, not merely the tank itself.|
N~An imagined journey can be wounded before it begins.|
N~His anger makes sense. Someone is treating what matters to him as expendable.|
N~I'd like to hear his plans again once the danger has passed.
''')
add('space_everyone', 'MossdeepCity_SpaceCenter_2F_Text_WishOrdinaryPeopleCouldGoIntoSpace', 'A visitor hopes space travel will eventually be available to ordinary people.', '''
U~An ordinary afternoon that includes leaving the planet would be quite an upgrade.|
N~Wider access would require substantial advances in reliability, cost, and support.|
N~Good dream. Make it safe before making it common.|
S~It is nice to imagine a distant place becoming something you could really visit.|
S~People would still ask what to pack and whether there will be food.|
S~The extraordinary voyage hopes to become a chapter available to an ordinary life.|
N~A larger selection of travel anxiety. Progress is generous.|
U~Making complicated systems usable by more people is an exciting challenge.|
S~A far light can become a place instead of only a point to wish upon.|
N~It would be lovely if wonder weren't reserved for the unusually fortunate.|
S~I'd ask what they would want to see first from up there.
''')
add('space_magma_space', 'MossdeepCity_SpaceCenter_2F_Text_DoesMagmaWantToGoToSpace', 'A visitor guesses Magma may want the fuel for space travel.', '''
N~I'd rather the first clue to someone's travel plans weren't theft.|
N~The fuel could suggest several uses. Spaceflight is only one hypothesis.|
N~Whatever they want, taking the center's fuel isn't acceptable.|
N~It's a natural guess in this room, but I wouldn't be comfortable assuming it.|
N~Wanting a journey doesn't make everyone else's work yours to take.|
N~The missing motive is briefly filled by the nearest available genre.|
N~A criminal space program. Somehow not the most reassuring interpretation.|
N~We should look for evidence of compatible equipment before accepting that theory.|
N~A thing's usual purpose does not tell us every use someone might force on it.|
N~They are trying to make the danger understandable. That doesn't mean the guess is right.|
N~I'd ask what the staff know rather than build the whole story from the fuel.
''')

add('mart_rust_shroomish', 'RustboroCity_Mart_Text_BuyingHealsInCaseOfShroomish', 'A shopper prepares paralysis and poison cures for Shroomish encounters in Petalburg Woods.', '''
N~That shopper has imagined the mushroom-shaped problem before meeting it.|
S~Preparing for known status effects is more useful than buying without a scenario.|
N~Good preparation. Keep the cures where they're easy to reach.|
N~It helps to know what worries you before entering the woods.|
N~A small bit of shopping can save a very uncomfortable walk back.|
N~The forest excursion has received a properly researched packing list.|
N~A mushroom has influenced the shopping before appearing in person. Efficient.|
N~We should match supplies to the conditions likely along our route.|
N~The woods can be gentle-looking and still ask for care.|
N~They're preparing for their partner's comfort, which is worth noticing.|
N~I'd ask whether they learned this from a previous trip.
''')
add('mart_rust_potions', 'RustboroCity_Mart_Text_ShouldBuySuperPotionsInstead', 'A shopper upgrades healing supplies after their Pokemon evolves and gains HP.', '''
S~The Pokemon grew, and the shopping list is trying to keep up.|
N~A fixed healing amount becomes less adequate as maximum HP increases.|
N~Check the team's current needs instead of packing for the team we used to have.|
N~It's nice when growing stronger also means someone notices you need different care.|
N~A bigger partner may need a bigger helping of recovery.|
N~Character development has produced a practical amendment to the inventory.|
N~Evolution has submitted an expense request.|
N~Compare recovery per use against what the partner actually needs now.|
N~Care should change as the one receiving it changes.|
N~They are adjusting a familiar habit instead of assuming it will always fit.|
N~I'd ask what else surprised them after the evolution.
''')
add('mart_rust_escape', 'RustboroCity_Mart_Text_GettingEscapeRopeJustInCase', 'A shopper buys Escape Rope as a way out of caves.', '''
N~A way back to the door is an excellent thing to pack before getting lost.|
N~An exit option reduces the consequences of uncertain navigation.|
N~Good. Know how to leave before pushing farther in.|
N~I would feel a little calmer knowing the entrance isn't our only plan.|
N~Being prepared to stop is part of being prepared to explore.|
N~The intrepid explorer has wisely purchased an ending before the adventure begins.|
N~A retreat made portable. One of civilization's finer ideas.|
N~Keep it accessible rather than beneath the rest of the equipment.|
N~An unknown passage feels kinder when a way home remains possible.|
N~A backup isn't pessimism. It gives curiosity room to be sensible.|
N~I'd ask whether they have a particular cave in mind.
''')
add('mart_slate_specialties', 'SlateportCity_Mart_Text_SomeItemsOnlyAtMart', 'A shopper distinguishes the market interesting goods from items exclusive to the Mart.', '''
N~Two shopping places, each convinced the other one doesn't have quite everything.|
N~Different inventories serve different purchasing needs.|
N~Check both lists before walking all over town.|
N~I like learning the little reasons people choose one familiar shop over another.|
S~A market for surprises, a Mart for the particular thing you came for.|
N~The town supports both wandering curiosity and a very specific shopping list.|
N~A productive rivalry between organized shelves and interesting stalls.|
N~We can plan which stops are necessary instead of buying a substitute in a hurry.|
N~An ordinary errand can show the different ways a town lives.|
N~It's nice when the shopper can appreciate both without dismissing either.|
N~I'd ask which item usually brings them back here.
''')
add('mart_slate_greatball', 'SlateportCity_Mart_Text_GreatBallIsBetter', 'A shopper hopes a Great Ball will help catch an elusive Pokemon.', '''
N~A better Ball helps, but the elusive Pokemon may still have its own plans.|
N~Improved capture performance changes the odds rather than guaranteeing an outcome.|
N~Useful gear. Still prepare the encounter properly.|
N~I hope the next meeting feels less frustrating for both of them.|
N~A good tool shouldn't make us forget patience with the Pokemon.|
N~The next attempt receives an equipment upgrade, not a rewritten ending.|
N~An improved container has been assigned an ambitious expectation.|
N~I'd consider the target's condition and the Ball together.|
N~An encounter remains a meeting even when we arrive with better tools.|
N~I'd be careful that wanting a catch doesn't turn the whole outing sour.|
N~I'd ask what keeps making that Pokemon so difficult to meet.
''')
add('mart_mauville_temp', 'MauvilleCity_Mart_Text_ItemsToTemporarilyElevateStats', 'A shopper describes temporary battle stat items such as X Attack and X Defend.', '''
N~A useful boost that doesn't move into the Pokemon permanently.|
N~These items affect the current battle state rather than lasting growth.|
N~Know how long the benefit lasts before planning around it.|
N~It's easy to miss the temporary part when the promise sounds exciting.|
N~A short-term helping hand still needs a good moment to use it.|
N~A brief flourish added to the performance, not a new line in the biography.|
N~Temporary excellence. A manageable subscription.|
N~Timing matters because using an item also takes an opportunity to act.|
N~A passing strength can be useful without becoming who someone is.|
N~I would keep the exact effect clear instead of just trusting the bright label.|
N~I'd ask which one they actually found useful in a difficult battle.
''')
add('mart_mauville_decisions', 'MauvilleCity_Mart_Text_DecisionsDetermineBattle', 'A shopper considers choosing a move versus using an item as an important Trainer responsibility.', '''
N~Our partners do the hard movement. We still have to do the careful thinking.|
N~Action selection can matter as much as the nominal strength of the available options.|
N~Make the call that helps the team, not the one that looks boldest.|
N~It is a lot of trust to have someone wait for your next decision.|
N~Sometimes giving a partner a little help is better than asking for one more attack.|
N~The person outside the direct struggle remains responsible for its direction.|
N~An excellent reminder that enthusiasm is not itself a battle plan.|
N~We should compare immediate benefit with the risk of delaying another action.|
N~A quiet choice can turn the path of a loud moment.|
N~That responsibility should make us attentive rather than eager to blame a partner.|
N~I'd ask what choice they remember wishing they'd made differently.
''')
add('mart_verd_special', 'VerdanturfTown_Mart_Text_XSpecialIsCrucial', 'A shopper strongly recommends temporary X Special boosts.', '''
N~Crucial for every match sounds like the shop shelf wrote part of that sentence.|
N~A special-attack boost is useful only when the move set and situation can exploit it.|
N~Good tool in the right battle. Not a substitute for choosing well.|
N~I would want to know whether our partner's moves actually need that help.|
N~An enthusiastic recommendation still deserves a look at the ingredients of the plan.|
N~A useful accessory has been promoted to universal savior. Bold marketing.|
N~Every battle is a suspiciously large number of battles.|
N~Check the relevant stat and the opportunity cost before using it.|
N~A thing can help without being the answer to every door.|
N~The certainty is louder than the explanation. I'd ask for a specific example.|
N~I'd hear about the battle where it worked best for them.
''')
add('mart_verd_guide', 'VerdanturfTown_Mart_Text_NoStrategyGuidesForBattleTent', 'A shopper cannot find a winning Battle Tent guide and expects to rely on personal judgment.', '''
S~The shelf has declined to do the thinking part for us.|
N~A guide could inform preparation, but no fixed text can choose every response.|
N~Learn the rules, then pay attention to the actual battle.|
N~It's daunting when the answer isn't waiting neatly on a page.|
N~Useful advice helps most when you still understand why you're following it.|
N~The aspiring victor discovers the adventure contains an unpurchasable component.|
N~The guaranteed-winning manual remains conspicuously out of stock.|
N~We can observe a few matches and work out what decisions matter.|
N~An unwritten path can still be walked one clear step at a time.|
N~Not having a script doesn't mean having to go in uninformed.|
N~I'd ask somebody who competed what surprised them most.
''')
add('mart_verd_nest', 'VerdanturfTown_Mart_Text_NestBallOnWeakenedPokemon', 'A shopper recommends Nest Balls and points out their local availability.', '''
N~A special Ball with a special purpose. We should be clear what that purpose is.|
N~Nest Balls depend on the target's level; low HP and low level are different conditions.|
N~Check how it works before expecting a catch.|
N~A small distinction in the explanation can change what someone expects.|
N~I'd ask a second question rather than buy a whole bag on a vague promise.|
N~The specialist tool deserves a more precise introduction than the sales pitch offers.|
N~A charming name is not a full set of instructions.|
N~We should compare the effect with the Pokemon we're actually trying to catch.|
N~A name can suggest a refuge while the mechanism follows its own rules.|
N~Local advice is useful when we know exactly what it means.|
N~I'd ask which Pokemon the shopper has successfully used it with.
''')
add('mart_fall_skitty', 'FallarborTown_Mart_Text_DecidingSkittyEvolve', 'A Trainer weighs evolving Skitty with a Moon Stone against its changed appearance.', '''
N~A familiar little face matters. I'd also like to know how Skitty feels about changing it.|
N~Evolution changes several traits; strength and appearance are not the only considerations.|
N~No rush. Make the choice with the partner in mind.|
N~I'd find it difficult to separate loving a familiar face from fearing a change.|
N~A stronger partner should still be a happy partner. Take some time.|
N~A character's future is being debated between affection for the present and possibility ahead.|
N~A permanent transformation deserves more than a hurried aisle decision.|
N~I'd learn what changes in capability before using the stone.|
N~A new shape need not erase who has been dear to us.|
N~Attachment isn't silly. It just needs room for the Pokemon's own future too.|
N~I'd spend a little time with Skitty away from the counter before deciding.
''')
add('mart_fall_nugget', 'FallarborTown_Mart_Text_SellNuggetIFound', 'A shopper decides to sell a found Nugget because it has little practical use.', '''
S~A lucky shiny rock is about to become several useful ordinary things.|
N~An object with high exchange value can still have little direct utility to its finder.|
N~If he doesn't want to keep it, useful supplies are a fair trade.|
N~I would remember where I found it, even after selling it.|
S~A small lucky find can pay for a very practical shopping trip.|
S~The treasure concludes its narrative by financing more mundane necessities.|
N~Gold has the peculiar talent of becoming almost anything else.|
N~I'd check the offered price before selling. No need to hurry a good find.|
N~A thing can leave our hand while its lucky moment stays.|
N~Having no use for it doesn't mean it needs to remain clutter.|
S~I'd ask how it caught their eye in the first place.
''')
add('mart_lava_speed', 'LavaridgeTown_Mart_Text_XSpeedFirstStrike', 'A shopper explains using X Speed to act earlier in battle.', '''
N~Getting there first is helpful, provided we know what we want to do when we arrive.|
N~Higher Speed can alter action order, though other priority conditions still matter.|
N~Useful advantage. Don't forget the turn spent setting it up.|
N~Being quicker feels reassuring when the next moment matters.|
N~A head start is useful when the rest of the plan is ready.|
N~The cast member receives assistance arriving before the opposing line.|
N~Punctuality weaponized. Intriguing product category.|
N~We should compare the speed difference before using it automatically.|
N~The first step matters because of where it lets the next step land.|
N~I'd rather be clear than hurried, even with a faster partner.|
N~I'd ask when that shopper found the extra speed most useful.
''')
add('mart_lava_treat', 'LavaridgeTown_Mart_Text_LocalSpecialtyOnMtChimney', 'A shopper recommends Mt Chimney local specialty as a Pokemon treat.', '''
S~A mountain trip with a snack recommendation attached. Excellent geography.|
N~A local specialty can have both a regional identity and a practical use.|
S~Worth a look if we're going that way. Don't drag the team uphill just for a rumor.|
S~I like bringing something back that reminds you where the day took you.|
S~Now I want to know what makes the mountain version different.|
S~The summit has added a culinary incentive to its existing dramatic scenery.|
S~A snack whose travel requirements are more ambitious than mine.|
N~I'd ask where the vendor is and whether supplies depend on the time.|
S~A small taste can carry a whole place back down the mountain.|
S~A recommendation for making our partner happy is a nice kind of souvenir advice.|
S~I'd ask what the Pokemon does that makes its delight so obvious.
''')
add('mart_fort_superrepel', 'FortreeCity_Mart_Text_SuperRepelBetter', 'A shopper prefers Super Repel longer duration over ordinary Repel.', '''
N~Fewer spray stops means fewer times I have to remember where the bottle went.|
N~Longer duration changes convenience as well as total trip consumption.|
N~Good for a planned stretch of travel. Keep watching where we walk.|
N~A quieter walk can be pleasant when we just need to reach somewhere.|
N~I'd compare how much route one bottle covers before stocking up.|
N~The journey receives fewer interruptions, including interruptions to renew the interruption preventer.|
N~A longer interval between chores. Persuasive.|
N~We should compare duration per cost, not simply the size of the label.|
N~A clear passage is useful when we know why we are passing through.|
N~Convenience can be worth paying for on a tiring day.|
N~I'd ask which route made them start preferring this one.
''')
add('mart_fort_spares', 'FortreeCity_Mart_Text_StockUpOnItems', 'A shopper prefers carrying extra supplies for unforeseen problems.', '''
N~A spare is useful. Twelve spares may require a second person to carry the first eleven.|
N~A reserve should be sized around plausible risks and transport capacity.|
N~Prepare for trouble without making the pack the trouble.|
N~I understand feeling calmer when the bag has an answer ready.|
N~I'd cover the essentials first, then leave room for what the road brings.|
N~The expedition is prepared for contingencies, and perhaps for some of their relatives.|
N~Reassurance has weight. The shoulders should be consulted.|
N~A simple checklist can prevent both shortages and needless duplicates.|
N~A bag can carry preparation without carrying every imagined fear.|
N~Feeling safe is important. So is being able to move comfortably.|
N~I'd ask which spare they were happiest to have on their last trip.
''')
add('mart_fort_candy', 'FortreeCity_Mart_Text_RareCandyMakesMonGrow', 'A boy explains that Rare Candy immediately raises a Pokemon by one level.', '''
U~An entire level inside one little sweet. Lunch has some catching up to do.|
N~It provides immediate level advancement rather than a normal meal's role.|
N~Useful item. Still need practice with whatever comes from the growth.|
N~I'd give the partner a moment to understand what feels different afterward.|
N~A remarkable sweet is still no replacement for regular food and care.|
S~Character development, delivered in unexpectedly compact confectionery.|
N~A sugary abbreviation of a longer process. Conveniently rare.|
N~We should consider who benefits most before using a limited item.|
N~A quick step forward still leaves a journey to make sense of it.|
N~I'd want the partner comfortable with its new strength, not merely stronger on paper.|
N~I'd ask whether the boy has watched a Pokemon try one himself.
''')
add('mart_moss_revive', 'MossdeepCity_Mart_Text_ReviveIsFantastic', 'A shopper praises Revive but warns that it does not replenish move PP.', '''
N~Getting back up and being ready for everything are two different sorts of better.|
N~Restoring consciousness and HP does not replenish move usage capacity.|
N~Check the whole partner's condition before sending it back in.|
N~I wouldn't want being able to stand mistaken for being ready to continue.|
N~A recovery item can help without replacing a proper rest.|
N~The fallen character returns, but the script's remaining lines are still finite.|
N~Revival has limits. A reassuringly honest product review.|
N~We should review remaining moves as well as the restored HP.|
N~Returning to the path does not erase how far someone has already walked.|
N~They need us to notice the exhaustion that one item doesn't solve.|
N~I'd check whether a Center visit is the better next step.
''')
add('mart_moss_maxrepel', 'MossdeepCity_Mart_Text_MaxRepelLastsLongest', 'A shopper values Max Repel longest duration.', '''
N~The longest quiet spell in a bottle. Helpful when we have somewhere definite to be.|
N~Maximum duration may reduce the number of applications a long route requires.|
N~Useful. It still doesn't replace looking where we step.|
N~An uninterrupted stretch can be nice when everybody is tired.|
N~We can choose it for a long trip instead of using the biggest thing for every short walk.|
N~The traveler's pause in encounters receives an extended edition.|
N~A larger allowance of peace before the next practical task.|
N~I'd compare the route length with the actual duration needed.|
N~A quiet passage can be chosen without disliking what lives beside it.|
N~The convenience should fit our plans rather than decide them.|
N~I'd ask which journey made the longer duration worth it for them.
''')
add('mart_moss_balls', 'MossdeepCity_Mart_Text_NetAndDiveBallsRare', 'A sailor describes local Net and Dive Balls and their different capture specialties.', '''
S~Two kinds of Ball, two very different ideas of who belongs in the customer list.|
N~Net Balls key on types; Dive Balls key on the underwater encounter setting.|
N~Choose for the actual encounter. Similar colors don't mean similar uses.|
N~It's nice to know why something is made in the town where we're standing.|
N~A specialist tool earns its space when the trip actually calls for it.|
N~The local industry has produced a pair of impressively specific invitations.|
N~The sea has generated several product categories. Predictable economic behavior.|
N~We should keep the two conditions distinct when packing.|
N~The same water can hold different reasons for choosing a thing.|
N~Knowing the purpose makes the shelf less overwhelming.|
N~I'd ask the sailor which one he uses on his own trips.
''')
add('mart_soot_ppup', 'SootopolisCity_Mart_Text_PPUpIsGreat', 'A shopper explains that PP Up raises a move use capacity.', '''
N~A favorite move gets a little more room before it needs a rest.|
N~It increases a move's capacity rather than simply refilling the current amount.|
N~Use it on something the partner will actually keep using.|
N~It's useful to know the difference between more room and a refill.|
N~A little more endurance can help, but we should still notice when the team needs a break.|
N~The reliable line receives permission for a few additional repetitions.|
N~An enlarged allowance of one particular activity. Sensible specialization.|
N~We should choose the move deliberately before using a limited item.|
N~A well-known path can be given a little more distance.|
N~The best choice is the one that fits the partner, not simply our newest move.|
N~I'd ask which move the shopper thought worth improving.
''')
add('mart_soot_scared', 'SootopolisCity_Mart_Text_TooScaryOutside', 'During the crisis, a shopper fears leaving shelter despite wanting to understand events.', '''
D~Wanting an answer doesn't mean you have to walk into danger to get it.|
N~The desire for information can be met without unnecessary exposure.|
N~Stay inside. We can seek reliable news without sending him out.|
D~Not knowing makes every sound outside feel larger.|
N~He needs a calm update and somewhere safe to wait.|
N~The extraordinary event has trapped an ordinary person between curiosity and fear.|
N~A perfectly reasonable objection to conducting firsthand fieldwork today.|
N~Clear information inside the shelter would reduce both confusion and risky trips.|
D~A window can feel too small for the fear beyond it.|
N~His hesitation is sensible. Nobody needs to shame him into bravery.|
N~I'd ask whether the shop has received a recent message from someone trustworthy.
''')
add('mart_soot_awaken', 'SootopolisCity_Mart_Text_DidSomethingAwaken', 'A shopper speculates that the abnormal weather signals something awakening.', '''
N~That is a much larger explanation than forgetting to bring an umbrella.|
N~The weather is observable; its proposed cause still needs evidence.|
N~Something is wrong. We don't need a complete theory to take shelter.|
N~A half-spoken question can make the room feel very quiet.|
N~I would rather give him what we know than add another alarming guess.|
N~The weather has prompted a question old stories are unusually ready to answer.|
N~An ominous hypothesis has entered the shop without buying anything.|
N~We should separate direct reports from interpretations while the situation develops.|
N~A disturbance can feel older than the sky it darkens.|
N~He is trying to give the fear a shape. That doesn't establish the answer.|
N~I'd ask what he saw change before deciding what caused it.
''')
add('mart_soot_fullrestore', 'SootopolisCity_Mart_Text_FullRestoreItemOfDreams', 'A shopper enthusiastically praises Full Restore combined HP and status recovery.', '''
U~A bottle with more than one helpful answer inside. That's efficient kindness.|
N~Combined recovery can resolve HP loss and status in a single use.|
N~Useful when both problems need solving. Keep one ready for a hard stretch.|
N~It sounds reassuring to have a broad answer when something goes wrong.|
N~A good emergency supply still leaves room for a proper rest afterward.|
S~The comprehensive remedy has acquired an understandably enthusiastic reviewer.|
N~Several problems, one bottle. A rare economy of effort.|
N~We should save the combined effect for situations that actually benefit from it.|
N~A helpful thing can make a frightened moment feel a little more manageable.|
N~The dream is useful recovery, not an excuse to keep pushing forever.|
N~I'd ask what situation made the shopper appreciate it so much.
''')

add('dept_welcome', 'LilycoveCity_DepartmentStore_1F_Text_WelcomeToDeptStore', 'The greeter welcomes the player to Lilycove Department Store.', '''
U~A whole tower of things we didn't know we might want until we walked in.|
N~A larger store makes the floor directory an especially useful first stop.|
N~Check the list before we start wandering.|
F~It's a lot of room and a lot of people all at once.|
N~Let's find what we came for before the bags fill themselves.|
S~The grand entrance opens onto several floors of possible subplot.|
N~An impressive building dedicated to making a short errand less likely.|
N~A good layout should help us find a specific item without searching every floor.|
N~A bright doorway can hold more choices than we need today.|
S~A friendly greeting makes an enormous store feel a little easier to enter.|
N~I'd ask which floor has the thing at the top of our list.
''')
add('dept_fun_buying', 'LilycoveCity_DepartmentStore_1F_Text_IBuyAllSortsOfThings', 'A shopper enjoys the store enough to buy many unplanned things.', '''
S~Every shelf has apparently volunteered to come home with her.|
N~The pleasurable browsing experience is influencing purchases beyond the original need.|
N~Have fun. Leave enough money and room for the trip home.|
N~I'd want a quiet moment to decide which things I really liked.|
N~A little planned treat is easier to enjoy than a bagful of surprises at the till.|
S~The store has an unusually successful talent for expanding the supporting cast.|
N~A hobby with an alarming receipt length.|
N~A short list and spending limit would make the choices easier.|
N~A pretty thing can be enjoyed without being carried away.|
N~I like browsing too. The trick is keeping the room's excitement separate from your own taste.|
S~I'd ask which unexpected purchase she was happiest about later.
''')
add('dept_child_furniture', 'LilycoveCity_DepartmentStore_1F_Text_MomBuyingMeFurniture', 'A girl looks forward to her mother buying furniture for her.', '''
S~She is already furnishing the room in her head while her feet are still downstairs.|
S~Choosing a space can help a child feel ownership and comfort at home.|
S~Good day for her. Make sure it fits through the door.|
S~I wonder which corner she's been imagining differently.|
S~A comfortable place for her own things is a lovely gift.|
S~The interior designer has arrived with maternal funding.|
S~A room renovation with a very enthusiastic small client.|
N~Measure the space before falling in love with the biggest piece.|
S~A new little corner can make a familiar room feel newly hers.|
S~I'd let her describe what she wants the room to feel like.|
S~I'd ask which piece she is most excited to choose herself.
''')
add('dept_azumarill_reward', 'LilycoveCity_DepartmentStore_1F_Text_BuyingSomethingForAzumarill', 'A Trainer buys a present for Azumarill after a contest victory.', '''
S~Azumarill won a contest and now gets to win the shopping trip too.|
S~The gift marks a shared achievement, though its value depends on what Azumarill enjoys.|
S~Nice. Pick something the partner likes, not just something that looks grand.|
S~I like that the victory includes a happy ordinary moment afterward.|
S~A favorite treat can say well done more clearly than an expensive guess.|
S~The triumphant performer has earned a modest shopping epilogue.|
S~A champion with a potentially excellent gift budget.|
N~I'd narrow the choices by Azumarill's actual habits.|
S~An achievement can be remembered through a small act of affection.|
S~The reward should make the partner feel celebrated, not displayed.|
S~I'd ask what Azumarill gets most excited about outside contests.
''')
add('dept_use_items', 'LilycoveCity_DepartmentStore_2F_Text_LearnToUseItemsProperly', 'A cook stresses knowing how to use items properly.', '''
N~Owning a very useful thing is only half the very useful arrangement.|
N~Understanding the application conditions is necessary to obtain the intended effect.|
N~Read the instructions before the emergency.|
N~I'd rather ask a basic question here than guess under pressure later.|
N~I agree about learning. Calling it basic doesn't help someone who hasn't been taught.|
N~The equipment list has been accompanied by a curt request for competence.|
N~A sensible lesson in a slightly uninviting wrapper.|
N~Test understanding with a clear example instead of assuming familiarity.|
N~A helpful object needs a hand that knows what it offers.|
N~People learn better when the explanation leaves them room to be beginners.|
N~I'd ask which mistake the cook most often sees people make.
''')
add('dept_husband_gift', 'LilycoveCity_DepartmentStore_2F_Text_GoodGiftForHusband', 'A shopper considers a gift for her husband waiting at home.', '''
S~The best aisle may be the one that reminds her of something he said last week.|
N~A good prediction of his preferences is more useful than the item's general popularity.|
N~Something he will use or genuinely enjoy. Doesn't have to be elaborate.|
S~I like the thought of her picturing his face before choosing.|
S~A favorite small comfort is often better than the most expensive shelf.|
S~An absent character has become the quiet center of the shopping scene.|
S~A present selected for an actual person. A promising departure from gift panic.|
N~I'd start with a need or interest he has mentioned recently.|
S~A familiar wish can guide a hand through an unfamiliar shelf.|
S~Choose something that says she noticed him, not simply that she went shopping.|
S~I'd ask what he has been enjoying doing at home lately.
''')
add('dept_journey_supplies', 'LilycoveCity_DepartmentStore_2F_Text_StockUpOnItems', 'A sailor stocks up before a long journey.', '''
N~A long journey is easier when the useful little things aren't all back at home.|
N~Supply planning should reflect route length, likely hazards, and opportunities to restock.|
N~Good. Check the essentials before adding extras.|
N~Packing makes a journey feel real before you've taken the first step.|
N~I'd plan meals and water alongside the battle supplies.|
N~The adventure is still in its most practical preparatory chapter.|
N~An expedition begins with shopping and optimism. One is easier to measure.|
N~A checklist will catch gaps more reliably than buying whatever looks useful.|
N~A bag can hold a little foresight for the road ahead.|
N~I hope the preparations include a comfortable way to carry everything.|
N~I'd ask where the route next gives them a safe place to stop.
''')
add('dept_carbos', 'LilycoveCity_DepartmentStore_3F_Text_GaveCarbosToSpeedUpMon', 'A shopper observed increased Speed after giving Carbos.', '''
S~A little extra speed, and now the Trainer has to keep up with the explanation.|
N~The reported increase follows a relevant training supplement rather than a temporary battle boost.|
N~Useful if speed suits the partner's role. Keep the rest of the training balanced.|
N~I'd want to see how the partner feels using the change.|
N~A helpful supplement works best alongside an ordinary healthy routine.|
N~The character has acquired faster entrances through a remarkably small purchase.|
N~An accelerated Pokemon and a presumably unchanged walking companion.|
N~We should track the result and remember there are limits to supplementation.|
N~A quick step should still lead somewhere chosen carefully.|
N~Strengthening a trait makes sense when it fits who the partner is.|
N~I'd ask where the Trainer first noticed the added speed.
''')
add('dept_protein_calcium', 'LilycoveCity_DepartmentStore_3F_Text_ItemsBestForTougheningPokemon', 'A shopper recommends Protein and Calcium for distinct attacking stats.', '''
N~Two kinds of strength, and the bottles don't get to swap their jobs.|
N~Attack and special attack support different move categories. The distinction is important.|
N~Match the item to the moves the partner actually uses.|
N~I would rather understand the choice than make someone stronger in the wrong direction.|
N~A supplement is only helpful when it fits the rest of the plan.|
N~The preparation montage has developed a branching nutritional syllabus.|
N~Two bottles, two attack statistics, several opportunities to read the label.|
N~We should check which stat governs the intended moves before buying.|
N~Different strengths can live behind the same familiar face.|
N~The right choice serves the Pokemon's role, not the shopper's impatience.|
N~I'd ask what kind of battle the shopper is preparing for.
''')
add('dept_endurance', 'LilycoveCity_DepartmentStore_3F_Text_WantMoreEndurance', 'A shopper weighs Iron physical Defense against Zinc special Defense.', '''
N~Two ways to be sturdier. The hard part is knowing what is likely to hit you.|
N~The relevant defensive stat depends on the category of incoming moves.|
N~Cover the weakness that actually matters to the partner.|
N~It is nice that they are thinking about enduring a battle, not only hitting harder.|
N~I'd look at the team's needs before choosing which bottle feels more reassuring.|
N~The defender's preparation depends on which sort of trouble the next scene contains.|
N~A choice between two kinds of not being knocked over. Both appealing.|
N~We should compare likely threats rather than raise both numbers without a purpose.|
N~A shelter is strongest where it answers the weather that reaches it.|
N~More endurance should mean more comfort, not permission to ignore distress.|
N~I'd ask which attacks have been giving the partner trouble.
''')
add('dept_attack_defense_tm', 'LilycoveCity_DepartmentStore_4F_Text_AttackOrDefenseTM', 'A shopper struggles to choose between offensive and defensive TM moves.', '''
N~A strong move is helpful. Being able to stay for the next turn is also persuasive.|
N~The value of either option depends on the partner's role and existing coverage.|
N~Choose what the team lacks, not simply whichever sounds more impressive.|
N~A quieter defensive choice can be difficult to recognize as the brave one.|
N~I'd think about the whole team before choosing what one partner should learn.|
N~The author must decide whether the next line delivers a blow or changes the scene.|
N~An attacking answer or an answer to being attacked. Context insists on participating.|
N~We can identify a real failure in the current plan and choose what fixes it.|
N~A held ground can matter as much as a forward step.|
N~The move should make sense for the one learning it, not only the shelf description.|
N~I'd ask which situation made the shopper want a new move.
''')
add('dept_tm_catalog', 'LilycoveCity_DepartmentStore_4F_Text_FiftyDifferentTMs', 'A shopper cites a catalog listing fifty kinds of TM moves.', '''
U~That's a lot of little lessons for something with only four spaces to remember them.|
N~A catalog's count describes the listed collection, not the usefulness of every option.|
N~Plenty of choices. We only need the ones that fit the team.|
N~I think I would want one question answered before looking at all fifty.|
N~A large menu is easier when you know what you came hungry for.|
N~The course catalog is extensive; the student is permitted a much smaller timetable.|
N~A comprehensive selection, with an excellent chance of decision fatigue.|
N~I'd group them by the problems they solve instead of reading the entire list at once.|
N~Many possible paths can wait while we choose the next useful step.|
N~A number can impress without making the choice clearer.|
N~I'd ask which unfamiliar TM the shopper is most curious about.
''')
add('dept_four_moves', 'LilycoveCity_DepartmentStore_4F_Text_PokemonOnlyHaveFourMoves', 'A shopper wants every TM but recognizes Pokemon can only know four moves at once.', '''
N~The collection wants a warehouse. The Pokemon would like us to make four decisions.|
N~Owning all options does not remove the constraint on simultaneous use.|
N~Four useful moves beat a bag full of indecision.|
N~A smaller set can feel reassuring when every choice has a clear place.|
N~You can enjoy collecting without expecting one partner to use the whole collection.|
N~An enormous library meets an uncompromising four-line script.|
N~The inventory may be ambitious. The move list remains concise.|
N~We need complementary functions rather than four versions of the same solution.|
N~A small vessel asks us to choose what truly belongs inside it.|
N~Limits can help the partner's role feel clear instead of unfinished.|
N~I'd ask which four the shopper actually finds hardest to choose between.
''')
add('dept_dolls_self', 'LilycoveCity_DepartmentStore_5F_Text_PlaceFullOfCuteDolls', 'A parent considers buying a doll for herself as well as for her children.', '''
S~Grown-ups are allowed a small soft friend too. No child-shaped permission slip needed.|
S~Enjoyment of a comforting object does not require a particular age.|
S~Get one she likes. Nothing wrong with enjoying her own home.|
S~I like hearing someone remember that their own little wishes count too.|
S~She can choose a treat for herself without taking anything from the children.|
S~The patron of children's collections finally commissions a piece for her own.|
S~Adulthood has many burdens. It need not include a ban on plush creatures.|
N~I'd ask what size and place would make it easy to enjoy at home.|
S~A small soft thing can belong to any tired hand.|
S~I'd encourage her to pick the one she keeps looking back at.|
S~I'd ask which doll she would choose if nobody else had an opinion.
''')
add('dept_mat_choices', 'LilycoveCity_DepartmentStore_5F_Text_SellManyCuteMatsHere', 'A shopper considers buying every cute mat rather than choosing one.', '''
N~A room has only so much floor before the mats start stacking like sandwiches.|
N~Buying every option avoids choosing but creates a storage and placement problem.|
N~Pick the one that fits the room. We can leave some for another day.|
N~I would want to picture how it feels under the familiar furniture.|
N~One well-chosen thing often feels nicer than a pile of almost-right ones.|
N~The decorating decision threatens to become a complete acquisition of the floor department.|
N~An ambitious attempt to solve taste with quantity.|
N~Measure the available area and compare the colors before buying.|
N~A lovely pattern needs space around it to be seen.|
S~I'd choose the mat that ties the room together instead of competing with it.|
N~I'd ask what the rest of the room looks like first.
''')
add('dept_roof_closed', 'LilycoveCity_DepartmentStore_5F_Text_ClosedRooftopForWeather', 'During the crisis, a shopper explains that dangerous weather has closed the rooftop.', '''
N~A roof is a poor place to argue with wild weather. Staying inside sounds wise.|
N~Closing the exposed area is an appropriate response to hazardous conditions.|
N~Keep it closed until it's safe. Shopping can wait.|
N~It's unsettling when an ordinary stairway suddenly leads somewhere you shouldn't go.|
N~I'd rather everyone be indoors than hurry through a sale outside.|
N~The weather has removed a floor from the day's available itinerary.|
N~The open-air shopping experience has become excessively open to the air.|
N~They should keep the barrier clear and explain the closure to visitors.|
N~A familiar height can become a different place under a changed sky.|
N~A plain explanation helps people accept the detour without feeling dismissed.|
N~I'd ask whether the staff have reliable information about reopening.
''')
add('dept_doll_before_partner', 'LilycoveCity_DepartmentStore_5F_Text_GettingDollInsteadOfPokemon', 'A child chooses a doll while waiting until old enough to raise a Pokemon.', '''
S~A little pretend companion can keep a real future companion's place warm.|
S~The doll offers enjoyment without the responsibilities of a living Pokemon.|
S~Good start. There's time to learn before taking care of a partner.|
S~I wonder which Pokemon the doll lets her imagine meeting.|
S~She can enjoy the soft part now and learn the daily care a little at a time.|
S~The future Trainer rehearses companionship with an exceptionally patient understudy.|
S~A beginner's partner with admirably forgiving care requirements.|
N~Learning what a real Pokemon needs will make the eventual meeting easier.|
S~A small wish can sit beside you while you grow toward it.|
S~It's a kind way to let her enjoy the dream at her own pace.|
S~I'd ask what name she wants to give the doll.
''')
add('dept_roof_sale', 'LilycoveCity_DepartmentStoreRooftop_Text_BeenWaitingForClearOutSale', 'A shopper eagerly attends the rare clear-out sale and plans to stock up.', '''
U~The long-awaited sale has arrived, and his bag is about to discover why he was waiting.|
N~Limited availability can create urgency beyond an item's actual usefulness.|
N~Get what he'll use. Rare doesn't automatically mean needed.|
N~I can hear how long he has been looking forward to the visit.|
N~I'd make a list before the excitement starts filling every spare pocket.|
S~The anticipated event finally opens its doors to a devoted audience of one.|
N~The clearance table has successfully produced a sense of destiny.|
N~Check the dimensions and price before making a large decorative commitment.|
N~A rare opening can invite a hurried hand. Pause long enough to choose.|
N~A good find should still fit the life it's going home to.|
S~I'd ask which particular item made the wait worthwhile for him.
''')
add('dept_roof_schedule', 'LilycoveCity_DepartmentStoreRooftop_Text_SetDatesForClearOutSales', 'A shopper cannot find a predictable schedule or television advertisement for clear-out sales.', '''
N~The sale is behaving more like a rare bird than a shop appointment.|
N~An unpredictable schedule makes planning difficult even for interested customers.|
N~Ask the staff. Waiting for a commercial isn't much of a plan.|
N~It is frustrating to keep checking when nobody tells you what to expect.|
N~A notice near the entrance would save people a wasted trip.|
N~The grand commercial event has neglected the small business of announcing itself.|
N~A sale marketed primarily through uncertainty. Bold.|
N~A clear posted date would solve this more reliably than repeated television watching.|
N~An opening is kinder when people know when to look for it.|
N~He shouldn't have to turn an errand into a guessing game.|
N~I'd ask where the department store publishes its notices.
''')
add('dept_roof_thirst', 'LilycoveCity_DepartmentStoreRooftop_Text_BoneDryThirsty', 'A rooftop visitor complains of thirst near the vending machines.', '''
N~His next grand adventure should probably involve a cup of water.|
N~Thirst is a useful signal to act on before continuing a warm outing.|
N~Get a drink and sit down for a moment.|
N~The rooftop can feel warmer than you expect after all those stairs.|
N~Water first. Choosing the perfect flavor can happen after the urgent part.|
N~The towering shopping expedition has reached an unglamorous physiological requirement.|
N~A dramatic condition with a potentially undramatic solution nearby.|
N~He should check the vending machines rather than keep announcing the shortage.|
N~A little water can bring the afternoon back into proportion.|
N~Comfort sometimes asks for something very plain.|
N~I'd point out the machines and give him room to get a drink.
''')
