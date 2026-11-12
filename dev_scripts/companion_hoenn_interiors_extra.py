"""Further reviewed Hoenn interior conversations; eleven independently written voices."""
ROWS = []
EMOTIONS = dict(N='neutral', S='soft_smile', A='annoyed', F='flustered', D='sad',
                U='surprised', M='smug', L='laughing')

def add(key, labels, subject, lines):
    replies = [line.strip() for line in lines.strip().split('|')]
    replies = [EMOTIONS.get(line[0], line[0]) + line[1:] for line in replies]
    assert len(replies) == 11, (key, len(replies))
    ROWS.append(dict(key='hix_' + key, labels=labels.split(), subject=subject, replies=replies))

add('museum_aqua_good', 'SlateportCity_OceanicMuseum_1F_Text_AquaExistForGoodOfAll',
    'A Team Aqua grunt claims that the organization exists for everyone benefit.', '''
N~Everyone is a very large group to speak for without asking.|
N~A stated intention does not establish a beneficial result.|
N~Then they should stop making trouble for the people here.|
N~I don't think saying it confidently answers the doubts.|
N~People generally notice when help keeps making their day worse.|
N~A sweeping claim delivered without any troublesome supporting evidence.|
N~How convenient that everyone apparently appointed him their spokesman.|
N~I'd judge the work by what it actually does for this town.|
N~A kind word can be placed over an unkind purpose.|
N~He assumes we are included in his definition of good.|
N~I'd ask which local people he has actually helped.
''')
add('museum_boss_missing', 'SlateportCity_OceanicMuseum_1F_Text_OurBossIsntHere',
    'A Team Aqua grunt complains that their ordered gathering lacks its leader.', '''
S~They assembled all the parts except the person with the instructions.|
N~A group relying on one coordinator becomes inefficient when that person is absent.|
N~Not our job to organize them. Let them wait.|
N~They don't seem to know what to do without being told.|
N~A meeting without the person who called it is a familiar nuisance.|
M~The assembled villains are missing their principal source of direction.|
N~A leaderless collection of matching outfits. Very educational.|
N~You'd think they would agree on a time and a backup plan.|
N~An instruction can bring people together without giving them purpose.|
N~The uniforms create a stronger impression of organization than the meeting does.|
N~I'd rather hear the museum guide than help them find their boss.
''')
add('museum_theft_value', 'SlateportCity_OceanicMuseum_1F_Text_WouldStuffHereMakeMeRich',
    'An Aqua grunt wonders whether stealing museum exhibits would make them rich.', '''
A~They came to a museum and only noticed the imaginary price tags.|
N~Public research value is not equivalent to resale value.|
N~Leave the exhibits where people can learn from them.|
N~It is a sad way to look at something meant to be shared.|
A~There are people working hard to keep this place open.|
N~An exhibition reviewed by someone with a catastrophically narrow interest.|
N~He appears to have mistaken public education for a shopping opportunity.|
N~Those instruments belong to the work they support. Keep them here.|
N~Taking a thing can rob others of more than the thing itself.|
A~He didn't even pretend to be interested in why it matters.|
N~I'd rather point that plan out to a member of staff.
''')
add('museum_nefarious_learning', 'SlateportCity_OceanicMuseum_1F_Text_CanLearnForNefariousDeeds',
    'An Aqua grunt plans to use museum knowledge for wrongdoing.', '''
A~The information is free, and somehow they still found a way to misuse it.|
N~Education supplies capability. It does not determine how someone applies it.|
N~Learning something doesn't give you the right to hurt people with it.|
N~That makes his interest in the displays feel unpleasant.|
N~A useful skill can still end up in very inconsiderate hands.|
N~The museum has acquired an admirer with an unfortunate proposed application.|
N~At least he has spared us the effort of doubting his intentions.|
N~Knowing how something works should make you more careful with it.|
N~A clear window can be used to choose where to throw a stone.|
N~He says that as though we are going to appreciate the ambition.|
N~I'd remember his face if he starts asking about restricted equipment.
''')
add('museum_rustboro_blame', 'SlateportCity_OceanicMuseum_1F_Text_RustboroBungled',
    'An Aqua grunt blames fellow members Rustboro failures for the current assignment.', '''
N~Their team spirit seems to consist mostly of pointing at another team member.|
N~Blame has arrived more quickly than an analysis of what went wrong.|
N~Their bad planning isn't our concern. Their actions are.|
N~I doubt the people he's blaming are enjoying the story either.|
N~A group goes sour quickly when nobody owns their part.|
M~An organization rich in villains and poor in favorable references.|
N~A charming workplace. All the menace, none of the mutual respect.|
N~Even their complaints tell us they haven't coordinated very well.|
N~People can stand together and still leave each other alone.|
N~He wants us to know he is better than the absent members.|
N~I'd listen to what he reveals rather than joining in the blame.
''')
add('museum_grunt_fee', 'SlateportCity_OceanicMuseum_1F_Text_DidntHaveMoney',
    'An Aqua grunt admits being delayed because they could not afford the museum fee.', '''
S~The museum's smallest obstacle has defeated a very official-looking criminal budget.|
N~The entrance fee appears to have been omitted from their preparations.|
N~The attendant shouldn't have to argue just to collect the fee.|
F~I feel for the person who had to handle that conversation.|
N~If you're going somewhere, bring enough for the entrance. Basic planning.|
M~A grand operation, stalled at the ticket counter.|
N~The revolution has forgotten its spending money.|
N~A tiny predictable cost should not become a staff member's problem.|
N~A large purpose can trip over a very small threshold.|
N~He seems more annoyed by the delay than embarrassed by his preparation.|
N~I'd like to hear the attendant's version of that exchange.
''')
add('museum_thief_gift_done', 'SlateportCity_OceanicMuseum_1F_Text_HopeINeverSeeYouAgain',
    'After giving Thief, the familiar Aqua grunt hurriedly wishes never to meet the player again.', '''
S~A gift and a request to disappear from his life. Very mixed manners.|
N~He is eager to end the encounter now that the exchange is complete.|
N~Good. Let him leave without making more trouble.|
F~I don't think that laugh was quite as relaxed as he intended.|
N~At least he has found a way to finish this without another fight.|
M~A farewell attempting to sound triumphant while backing rapidly toward the door.|
S~Our company has inspired both generosity and a desperate exit.|
N~His nerves are clearer than his attempt at confidence.|
N~He leaves a small gift where he would rather leave no memory.|
N~He wants to keep a little dignity on the way out. Fine.|
S~That will be a very different story when he tells his friends.
''')
add('museum_thief_no_room', 'SlateportCity_OceanicMuseum_1F_Text_YouHaveToTakeThis',
    'With no bag space for Thief, the frightened grunt insists the player accept before he can leave.', '''
F~His escape plan depends on our packing skills. That's unfortunate for both of us.|
N~The transfer failed for lack of space. Nothing has changed hands yet.|
N~He can wait while we sort the bag. No need for panic.|
F~He looks trapped by the favor he is trying to give us.|
N~A gift needs somewhere to go. We can't solve that by insisting.|
M~A daring getaway defeated by an overfull bag.|
N~An unusually literal case of baggage delaying a farewell.|
N~We need to clear space before this particular exchange can finish.|
N~He cannot put down his fear until we can put away the item.|
N~He's trying very hard to hurry a problem that needs a quiet moment.|
N~I'd give him room while we decide what can leave the bag.
''')
add('museum_battle_learning', 'SlateportCity_OceanicMuseum_1F_Text_LearnAboutSeaForBattling',
    'A museum patron wants to apply knowledge of the sea to Pokemon battles.', '''
S~Homework that comes with fish and eventually helps win a battle!|
S~Understanding a habitat may reveal useful context for the Pokemon found there.|
N~Good. Learn what you're working with before testing it in a fight.|
N~I like that they're looking for more than a list of moves.|
N~Knowing where a partner lives can help you understand what it needs.|
S~A challenger has found a training ground with exceptionally informative walls.|
N~A museum as battle preparation. Quietly more alarming than shouting.|
N~Useful ideas often turn up outside the place where you plan to use them.|
N~A creature carries traces of its home into every encounter.|
N~They are taking their interest far enough to study it.|
S~I'd ask which display changed the way they think about battling.
''')
add('museum_stern_admiration', 'SlateportCity_OceanicMuseum_1F_Text_SternIsRoleModel',
    'A sea enthusiast admires Captain Stern as their foremost role model.', '''
S~They love the sea so much the sentence went a little wobbly.|
S~Stern gives that enthusiasm a person and a body of work to follow.|
S~Good choice to admire someone who does the hard work too.|
S~It's sweet to hear somebody so openly delighted by their interest.|
S~The sea makes them happy, and Stern gives them something to aim for.|
S~An admirer in danger of becoming entirely liquid with enthusiasm.|
S~A passionate endorsement delivered with minimal structural stability.|
N~I'd ask which of Stern's projects first caught their attention.|
S~The sea has given them wonder, and someone to look up to.|
S~No embarrassment about caring this much. I find that refreshing.|
S~I'd ask whether they have had a chance to meet him yet.
''')
add('museum_unknown_depths', 'SlateportCity_OceanicMuseum_1F_Text_MustBePokemonWeDontKnow',
    'A patron imagines unknown Pokemon in the immense unexplored sea.', '''
U~There could be a Pokemon down there that has never seen a person either.|
S~The ocean's scale makes incomplete knowledge entirely unsurprising.|
N~Good reason to explore carefully. Unknown doesn't mean harmless.|
N~It is strange to think how much life can go unseen beneath us.|
N~Whole kinds of ordinary days might be happening where we can't look.|
S~An enormous unwritten cast beneath a surface we mistake for the whole scene.|
N~The depths retain excellent privacy. I can understand the appeal.|
N~Better equipment could let researchers investigate without guessing so much.|
N~Dark water need not be empty water.|
N~There is room for wonder without pretending we already know what waits.|
U~I'd like to hear what the explorers saw that they couldn't identify.
''')
add('museum_sea_hug', 'SlateportCity_OceanicMuseum_1F_Text_WantSeaPokemon',
    'A patron wants a sea Pokemon because it seems pleasantly cool to hug.', '''
S~A cool hug sounds lovely. We should check whether the Pokemon agrees.|
N~Sea Pokemon vary substantially in texture, temperature, and comfort with handling.|
N~Meet the Pokemon first. Some are less cuddly than the idea.|
S~I understand wanting that sort of gentle company.|
S~A lovely plan, provided the chosen partner doesn't have sharp edges.|
S~An affectionate casting decision that still needs the candidate's approval.|
N~A cooling embrace. Species selection seems crucial.|
N~I'd learn how to handle that species before trying a hug.|
S~A creature of the sea may still enjoy being close on its own terms.|
S~The fondness is sweet. A little knowledge would make it sweeter.|
S~I'd ask which sea Pokemon they've actually spent time with.
''')
add('museum_fee_short', 'SlateportCity_OceanicMuseum_1F_Text_NotEnoughMoney',
    'The museum attendant cannot admit the player because they cannot afford the fee.', '''
F~We have arrived with curiosity and slightly insufficient coins.|
N~The admission requirement is clear. We can return once it is met.|
N~No argument needed. We'll come back prepared.|
F~I always feel as if everyone can hear the coins I don't have.|
N~Let's check the purse before making another trip to the counter.|
N~Our cultural outing has encountered a modest financial obstacle.|
N~The budget has delivered a concise critique of our plans.|
N~We can set aside the entrance fee before buying other things.|
N~A closed visit today need not be a closed door forever.|
N~The attendant kept it polite. Let's do the same.|
N~I'd find out the opening hours so the return trip is easy.
''')
add('museum_mistaken_group', 'SlateportCity_OceanicMuseum_1F_Text_CatchUpWithYourGroup',
    'The attendant mistakes the player for part of the earlier group and waives the fee.', '''
F~We have been admitted by a very unfortunate assumption about our company.|
N~She inferred an affiliation that we have not actually claimed.|
N~We're here to find Stern. Let's stick to that.|
F~I don't especially want people thinking we came with them.|
N~A helpful gesture, attached to the wrong explanation.|
N~An accidental disguise supplied entirely by the ticket counter.|
N~We have acquired an affiliation without the inconvenience of joining.|
N~The assumption explains her decision, even though the premise is wrong.|
N~A mistaken resemblance can open an unexpected door.|
N~She sees a late visitor, not what we actually came to do.|
N~I'd be careful not to turn her mistake into more trouble for her.
''')
add('slateport_balanced_team', 'SlateportCity_PokemonCenter_1F_Text_RaiseDifferentTypesOfPokemon',
    'A Trainer recommends developing varied Pokemon rather than relying on one strong partner.', '''
N~One star Pokemon shouldn't have to carry the whole sky.|
N~A varied team can cover weaknesses that raw strength alone cannot remove.|
N~Have a second plan and a partner ready to carry it out.|
N~It's kinder when one Pokemon doesn't have to handle everything.|
N~Spread the work around. Everybody needs a chance to learn.|
N~An ensemble gives the adventure more than one solution to a difficult scene.|
N~A single excellent answer eventually meets the wrong question.|
N~Different capabilities give us options when a familiar approach fails.|
N~Several kinds of strength can share one road.|
N~A team needs room for each member to contribute.|
N~I'd ask what encounter first taught that Trainer this lesson.
''')
add('slateport_trade_item', 'SlateportCity_PokemonCenter_1F_Text_TradedMonWithFriend',
    'A Trainer especially enjoys a friend traded Pokemon arriving with a held item.', '''
S~A new Pokemon arrives carrying a little extra hello from a friend.|
S~The held item adds practical value and evidence of an extra thoughtful choice.|
S~Nice touch. Someone remembered to send it with something useful.|
S~Small surprises can make a happy meeting even warmer.|
S~It's like sending someone home with a little packed lunch.|
S~The introduction comes with a thoughtful footnote from its previous companion.|
S~A gift carrying a gift. Efficiently pleasant.|
S~I'd check what the item does before changing it. They may have chosen carefully.|
S~A small object can carry another person's attention with it.|
S~They enjoyed the thought behind it as much as the thing itself.|
S~I'd ask about the friend who made that exchange special.
''')
add('slateport_tent_assumption', 'SlateportCity_House_Text_MustBeGoingToBattleTent',
    'A resident assumes any visiting Trainer must be going to the Battle Tent.', '''
S~We apparently look like people with very specific plans.|
N~It is a plausible destination, though being a Trainer does not establish our itinerary.|
N~Could be. Plenty else worth visiting in this town too.|
F~I might just have wanted to look around quietly.|
S~A port city surely has room for an errand and a good lunch as well.|
N~The local attraction has become the only approved explanation for our presence.|
S~An itinerary supplied by a stranger. Saves thinking, I suppose.|
N~We can ask what the Tent offers before deciding whether to visit.|
N~A person may arrive with a purpose that isn't visible.|
N~They are proud of the attraction, even if the guess is narrow.|
N~I'd ask what they enjoy watching there themselves.
''')
add('slateport_hasty_stats', 'SlateportCity_House_Text_NatureToDoWithStatGains',
    'A Trainer connects a hasty Pokemon nature to its unusually high Speed.', '''
S~Its personality may be doing a little of the running too.|
N~That observation is a useful lead. Controlled comparisons would strengthen it.|
N~Worth understanding your partner's strengths before planning training.|
N~It's interesting when a habit and an ability seem to line up.|
N~They noticed a difference by paying attention to their own team.|
N~An everyday observation has opened the door to a serious question.|
N~Hasty in temperament, swift in practice. An unusually consistent individual.|
N~We should compare similar Pokemon before assuming nature is the only cause.|
N~The way a creature meets the day may leave a trace in its strength.|
N~I like that they're curious instead of treating every difference as a flaw.|
N~I'd ask what else they have noticed when raising them side by side.
''')
add('fanclub_red_scarf', 'SlateportCity_PokemonFanClub_Text_ExplainRedScarf',
    'After awarding a Red Scarf, the chairman explains that it emphasizes Pokemon coolness.', '''
S~The scarf says cool while also being a perfectly sensible neck blanket.|
N~An accessory can emphasize the contest quality it was designed to support.|
S~It suits a purpose. Make sure the partner is comfortable wearing it.|
S~A small detail can make a confident pose easier to notice.|
S~A bright little finishing touch after all that raising.|
S~Our distinguished contestant has acquired an appropriately dramatic accent.|
S~A formal certificate of coolness, issued in wearable form.|
N~Now we know which contest category to pair it with.|
S~A warm color can frame a very composed presence.|
S~Red draws attention. Let the Pokemon's own confidence do the rest.|
S~I'd like to see how the Pokemon carries itself wearing that.
''')
add('fanclub_blue_scarf', 'SlateportCity_PokemonFanClub_Text_ExplainBlueScarf',
    'After awarding a Blue Scarf, the chairman explains that it enhances beauty.', '''
S~A little blue frame around an already lovely Pokemon.|
N~The scarf is intended to accentuate beauty rather than change the underlying work.|
S~Good reward. It should complement the partner, not get in its way.|
S~Blue can make the little changes in the light easier to notice.|
S~They've put care into raising it. This gives that care a nice finish.|
S~The contestant receives a finishing flourish in the color of a clear day.|
S~Beauty has been provided with a pleasantly restrained accessory.|
N~A small item with a clear specialized use. Easy to remember.|
S~A soft color can draw the eye without demanding it.|
S~Let it sit comfortably. A lovely accessory shouldn't compete with its wearer.|
S~I'd enjoy seeing the difference in how it looks when it moves.
''')
add('fanclub_pink_scarf', 'SlateportCity_PokemonFanClub_Text_ExplainPinkScarf',
    'After awarding a Pink Scarf, the chairman explains that it emphasizes cuteness.', '''
S~The Pokemon was cute already, and now the scarf is enthusiastically agreeing.|
N~It supports a specific contest quality. The intended use is clear.|
S~Cute is fine. Just keep it comfortable and out of the way.|
S~A little pink detail can make a familiar face look unexpectedly sweet.|
S~A cheerful reward for the work that brought us here.|
S~Our contender has received official assistance in being adorable.|
S~A strategic deployment of pink. The opposition has been warned.|
N~We can keep it with the items meant for that contest category.|
S~A small bright thing can invite a gentler sort of attention.|
S~Pink works best when it feels like part of the Pokemon's own charm.|
S~I'd watch for the little expression it makes when everyone notices.
''')
add('fanclub_green_scarf', 'SlateportCity_PokemonFanClub_Text_ExplainGreenScarf',
    'After awarding a Green Scarf, the chairman explains that it enhances smartness.', '''
S~A smart scarf! I hope it doesn't start judging my decisions.|
N~The accessory supports smartness in contests. It is not a substitute for preparation.|
N~Useful for that category. Keep the plan as sharp as the outfit.|
S~It's a quiet color for drawing attention to something clever.|
S~The right finishing touch can show the work off nicely.|
S~An intellectual flourish, delivered in fabric rather than footnotes.|
S~At last, a scarf with a promising academic record.|
N~A clear visual cue helps us remember which quality it supports.|
N~Green suits the thought of something carefully growing.|
S~A smart look should feel deliberate. This gives us a place to start.|
S~I'd ask what clever performance the chairman remembers best.
''')
add('fanclub_yellow_scarf', 'SlateportCity_PokemonFanClub_Text_ExplainYellowScarf',
    'After awarding a Yellow Scarf, the chairman explains that it emphasizes toughness.', '''
U~Toughness in a scarf! I have clearly underestimated laundry.|
N~Its contest function is specific. Yellow marks it as the toughness accessory.|
N~Good. Let the Pokemon do the hard part; the scarf can help present it.|
S~A bright detail can make a steady stance look even surer.|
S~There's a cheerful reward for a very sturdy partner.|
S~The rugged contender gains a surprisingly sunny finishing touch.|
S~Toughness, with a color that refuses to brood. An interesting choice.|
N~We should match it to the appropriate contest rather than its color alone.|
N~Strength does not always need to dress in dark colors.|
S~Bright yellow can make confidence look open instead of threatening.|
S~I'd like to see the Pokemon show that toughness in its own way.
''')
add('fanclub_more_condition', 'SlateportCity_PokemonFanClub_Text_GiveMonMorePokeblocks',
    'The chairman finds contest condition moderate and recommends additional Pokeblocks.', '''
N~He has advice, though he wraps it in a rather large frown.|
N~He is assessing contest condition, which is narrower than overall welfare.|
N~We can improve condition without treating the partner like a failed project.|
N~That is a rather stern way to say there is room to grow.|
N~We should check which flavors suit it before making more treats.|
N~The critic has requested revisions and suggested an edible method.|
N~A lukewarm review accompanied by practical snack advice. Could be worse.|
N~Let's identify the quality we're trying to improve before choosing Pokeblocks.|
N~A measure can point to work ahead without defining the whole creature.|
N~He could offer the useful suggestion without making it sound like a scolding.|
N~I'd ask what change he would look for at our next visit.
''')
add('fanclub_no_space', 'SlateportCity_PokemonFanClub_Text_NoSpaceForReward',
    'The Pokemon qualifies for a scarf reward, but the full bag prevents receiving it.', '''
F~Our Pokemon passed the assessment. Our packing failed its own little exam.|
N~The condition qualifies; storage capacity is the only obstacle identified.|
N~Make some space. No need to redo the training.|
F~I'd rather not have our partner think the delay is its fault.|
N~A good result still needs somewhere to put the reward.|
M~A promising award ceremony interrupted by a bag's unreasonable completeness.|
N~Merit has encountered luggage. Luggage appears to be winning.|
N~Let's organize the bag before returning for that specialized item.|
N~The praise has arrived even if the object must wait.|
N~We can enjoy the compliment while fixing the practical problem.|
S~I'd thank him for recognizing the work, then sort our things.
''')
add('fanclub_all_scarves', 'SlateportCity_PokemonFanClub_Text_NothingElseToGiveYou',
    'After all scarf rewards are awarded, the chairman says he has nothing further to give.', '''
S~We have exhausted the scarf supply. An unexpectedly fashionable achievement.|
S~His available rewards are exhausted. The work he praised remains accomplished.|
S~We've had plenty from him. A thank-you is enough now.|
S~It's nice to visit without needing the visit to end in a gift.|
S~We can still show him how the team is doing.|
S~The critic has run out of accessories before running out of admiration.|
S~A finite stock of fabric has met a persistent visitor.|
N~We should keep track of what each scarf helps with. The set is useful.|
S~A completed collection can leave room for an ordinary conversation.|
S~That's quite a range of looks to work with now.|
S~I'd ask which part of our Pokemon's growth he enjoyed seeing most.
''')
add('fanclub_contest_interest', 'SlateportCity_PokemonFanClub_Text_LikeToSeeEnteredContestPokemon',
    'The chairman hopes to see Pokemon raised by a Trainer who has entered a contest.', '''
S~He wants to meet a contestant almost as much as he wants to talk about one.|
N~He is particularly interested in how contest participation affects training.|
N~We can show him when we have something relevant to share.|
S~His curiosity sounds a little more personal than a list of results.|
S~People who raise Pokemon enjoy comparing the little things they learn.|
S~The chairman is waiting for a story with a qualified leading Pokemon.|
S~An enthusiast hoping for a visitor who shares his particular obsession.|
N~I'd ask which changes he expects to notice in a contest-trained partner.|
N~Care takes different shapes around different shared pursuits.|
S~He wants to see the Pokemon behind the performance. That's good.|
S~I'd listen to the questions he asks when he finally meets one.
''')
add('fanclub_chairman_intro', 'SlateportCity_PokemonFanClub_Text_MeetChairman',
    'The chairman boasts about his position and explains the club informal Pokemon showcases.', '''
S~He is very important, and fortunately still has room to admire everyone else's Pokemon.|
N~The club provides a local exchange when distant contest venues are inconvenient.|
N~A place to meet and compare training is useful. The boasting is optional.|
F~That introduction had quite a lot of chairman in it.|
S~He can be proud of his team and still enjoy what other people bring.|
M~A grand introduction to the modest pleasure of showing friends your Pokemon.|
N~The chairmanship appears to come with excellent self-esteem.|
N~They have found a practical local substitute for traveling to every contest.|
S~A shared room can hold many kinds of fondness.|
S~He makes himself sound grand, but the gathering itself sounds welcoming.|
S~I'd ask to meet his Pokemon after hearing such an introduction.
''')
add('fanclub_fainting', 'SlateportCity_PokemonFanClub_Text_PokemonDontLikeFainting',
    'A club member warns that repeated fainting damages Pokemon trust.', '''
D~Our partners remember the hard parts, even after the battle is over.|
N~Repeated adverse experiences can weaken trust. Prevention matters more than repair.|
N~Pull a struggling partner back before making it take more hits.|
D~I wouldn't want one to expect that every outing ends badly.|
N~Getting them healed doesn't erase the need to change the routine.|
N~A battle record leaves things out that the participant still remembers.|
N~Repeated collapse is a poor foundation for any working relationship.|
N~We should adjust our plan before the same failure happens again.|
D~A creature can learn to fear the hand that keeps sending it forward.|
N~They need to see us respond when something is hurting them.|
N~I'd watch for fatigue before a number tells us it's already too much.
''')
add('fanclub_protein', 'SlateportCity_PokemonFanClub_Text_MonEnjoyedProtein',
    'A member noticed their Pokemon seeming happy when given Protein.', '''
S~A pleased Pokemon is very persuasive feedback, even without a review card.|
N~A positive reaction is worth observing, though it may not reveal the exact cause.|
S~Good that they're paying attention to how their partner responds.|
S~It's nice when you can tell something you offered was welcome.|
S~I love the small happy reactions that make you want to remember a favorite.|
S~The recipient has supplied a favorable review without writing a word.|
S~A supplement with an unexpectedly enthusiastic audience.|
N~We should remember that useful items still have appropriate limits.|
S~A small moment of pleasure is worth noticing.|
S~They sound delighted by having made their Pokemon happy.|
S~I'd ask what it did that made the happiness so clear.
''')
add('fanclub_love_before', 'SlateportCity_PokemonFanClub_Text_ShowMePokemonThatLoveYou',
    'The Soothe Bell woman invites a return visit when Pokemon affection has grown.', '''
S~She wants to see the friendship when it's ready, not hurry it into posing.|
N~She is asking for an established relationship rather than a promise of one.|
N~Give the partner good days. We can visit again later.|
S~I like that she finds other people's closeness worth celebrating.|
S~The quiet daily care is what will give us something to show her.|
S~An invitation to return with a relationship, rather than a trophy.|
S~A patient audience for something that refuses to grow on command.|
N~We'll learn more by watching the partner than chasing a quick result.|
S~Affection arrives through small things repeated kindly.|
S~She makes warmth sound like something visible, and sometimes it is.|
S~I'd ask what little signs she usually notices first.
''')
add('fanclub_love_after', 'SlateportCity_PokemonFanClub_Text_TreatPokemonWithLove',
    'The Soothe Bell woman reiterates that Pokemon respond to affection and care.', '''
S~They notice how we feel about them. Even on the days with no big adventure.|
N~Care is communicated through behavior as well as intention.|
N~Treat them well consistently. That's the whole job underneath the battles.|
S~Being gentle can be something they recognize before we say anything.|
S~A meal, a rest, and someone who notices what they need. It adds up.|
S~The advice is simple enough that it cannot hide behind cleverness.|
S~A reciprocal arrangement with a fairly reasonable starting requirement.|
N~Knowing an individual partner helps us make that care specific.|
S~Warmth offered steadily can become something another creature trusts.|
S~It's less about looking kind than making the partner feel it.|
S~I'd keep watching how our Pokemon responds to everyday company.
''')

add('lily_fan_new', 'LilycoveCity_PokemonTrainerFanClub_Text_HeardAboutYouImYourFan',
    'A fan has heard the player achievements and hopes future battles will persuade the other fans.', '''
F~We have arrived as somebody's favorite argument. I wasn't prepared for that.|
N~They know the results, though they still want to see the method for themselves.|
N~We'll battle for our team, not just to settle a room's argument.|
F~That's a lot of excitement to receive from someone we've just met.|
S~It's kind to cheer. I just don't want our partner carrying everyone else's expectations.|
S~Our reputation has entered a lively debate and acquired counsel for the defense.|
N~We have been recruited into an argument without attending the first meeting.|
N~They can watch and form their own view. We still need to make careful decisions.|
N~A distant story has met the ordinary person walking inside it.|
S~They sound sincere, even if they are already planning what our success will prove.|
S~I'd like to hear which battle first made them pay attention.
''')
add('lily_fan_rumor', 'LilycoveCity_PokemonTrainerFanClub_Text_HearingAboutToughNewTrainer',
    'A fan unknowingly asks the player about rumors of their own Gym victories.', '''
S~The mysterious new Trainer has apparently walked right into the inquiry.|
N~The description is consistent with us. Recognition has not yet followed.|
S~We could save him a bit of guessing.|
F~I'm not quite sure how to introduce ourselves after that.|
S~News travels oddly. Sometimes the story gets here before the face.|
M~A delightful scene in which the subject is consulted about the legend.|
S~Fame has misplaced our description. An excellent loophole.|
N~We can tell him what actually happened rather than add to the rumor.|
N~A name can move farther and faster than the one carrying it.|
S~He is asking honestly. No need to embarrass him for not recognizing us.|
S~I'd love to hear which version of our journey has reached this room.
''')
add('lily_fan_brawly', 'LilycoveCity_PokemonTrainerFanClub_Text_MyFavoriteTrainerIsBrawly',
    'A fan confidently names Brawly as her favorite Trainer.', '''
S~She has selected a favorite and arrived ready to defend the selection.|
N~A preference need not be a claim that every other Trainer is inferior.|
S~Fair choice. She doesn't owe the room a different favorite.|
S~I like hearing someone say what they enjoy without apologizing.|
S~Every good gathering needs room for different tastes.|
S~Brawly has an advocate whose position is admirably unambiguous.|
S~A settled opinion. The meeting may proceed without further suspense.|
N~I'd ask what part of his battling she finds most effective.|
S~Admiration can settle around one familiar name.|
S~She knows her own taste. That's enough to begin a good conversation.|
S~I'd ask whether she has seen him battle in person.
''')
add('lily_fan_brawly_loyal', 'LilycoveCity_PokemonTrainerFanClub_Text_ICantHelpLikingBrawly',
    'A fan remains attached to Brawly despite the player popularity.', '''
S~A new popular Trainer hasn't moved the chair Brawly already had in her heart.|
N~New evidence of our ability need not change her personal preference.|
N~She can like Brawly. It isn't something we need to win.|
S~There is no need to feel guilty for keeping a favorite.|
S~You can appreciate someone new without replacing an old fondness.|
S~An established favorite survives the arrival of a fashionable new contender.|
S~She has resisted the room's latest approved enthusiasm. Admirable.|
N~Popularity shifts quickly. Her reasons may be more durable.|
S~Some names keep their place when the room changes around them.|
S~Her hesitation sounds like she expects us to take offense. We needn't.|
S~I'd rather hear what Brawly means to her than ask her to switch sides.
''')
add('lily_fan_brawly_alone', 'LilycoveCity_PokemonTrainerFanClub_Text_NobodyUnderstandsBrawly',
    'As Brawly sole remaining supporter, a fan insists she will continue cheering.', '''
S~One person's cheering can still be heard. Especially if she means it this much.|
N~A minority preference remains a valid preference.|
N~She doesn't have to surrender an opinion because the room disagrees.|
S~It takes a little courage to enjoy something alone in a crowded room.|
S~I'd rather make room for her than turn every conversation into a contest.|
S~The last loyal champion of an unfashionable cause refuses to yield her seat.|
S~A room full of agreement sounds dreary anyway.|
N~They could compare what they admire instead of trying to erase a preference.|
N~Being outnumbered is not the same as being mistaken about what you love.|
S~She wants to be understood as much as she wants to defend Brawly.|
S~I'd listen to the reasons nobody else seems willing to hear.
''')
add('lily_fan_brawly_slip', 'LilycoveCity_PokemonTrainerFanClub_Text_BrawlyNoImYourFan',
    'A player fan accidentally sighs Brawly name and quickly reasserts support for the player.', '''
S~Her cheering took a brief scenic trip through Dewford.|
N~An involuntary association is not particularly strong evidence about loyalty.|
S~She can cheer for two people. Saves the trouble of hiding it.|
F~I think she is more embarrassed than she needs to be.|
S~Having a second favorite isn't an offense against the first.|
M~A former leading man has wandered into the wrong declaration of devotion.|
S~An entirely convincing recovery, if we all politely forget the first word.|
N~No need for a complicated explanation. People can admire several Trainers.|
S~A little fondness slipped through before she could arrange it neatly.|
S~I wouldn't make her perform loyalty just because her thoughts wandered.|
S~I'd laugh gently and let the conversation move on.
''')
add('lily_fan_pull', 'LilycoveCity_PokemonTrainerFanClub_Text_ImPullingForYou',
    'A fan warmly encourages the player to keep going.', '''
S~A quick little cheer can fit in your pocket for later.|
S~Simple encouragement can be helpful without predicting an outcome.|
S~Appreciated. We'll give the next challenge proper effort.|
S~That was easy to hear in a room that can get rather loud.|
S~Nice to have someone wish us well without adding instructions.|
S~A brief, thoroughly favorable review of our continued existence in the contest.|
S~Encouragement with no lengthy speech attached. A rare pleasure.|
S~A friendly reminder that people are interested in how we do.|
S~A kind voice can travel with you after you leave the room.|
S~Her smile did as much as the words.|
S~I'd make sure she knows we heard and appreciated it.
''')
add('lily_fan_norman_less', 'LilycoveCity_PokemonTrainerFanClub_Text_LongWayToGoComparedToNorman',
    'A fan judges the player lacking in comparison to Norman strength and showmanship.', '''
N~It is difficult to stand in your own shoes while somebody keeps measuring your father's.|
N~He has named several distinct qualities, then collapsed them into one judgment.|
N~We're building our own skills. We don't need to borrow Norman's manner.|
N~A comparison can make it harder to hear what you've actually done well.|
N~Different people do good work differently. There is room for that here too.|
N~A reviewer determined to judge the new volume by the previous author's cover.|
N~A family resemblance has become an unsolicited performance requirement.|
N~Useful feedback would identify a decision we could improve, not an entire person.|
N~A shadow can be long without deciding where your own feet go.|
N~He has preferences. They don't need to become our whole measure of ourselves.|
N~I'd ask for a particular battle example if he wants the criticism taken seriously.
''')
add('lily_fan_norman_more', 'LilycoveCity_PokemonTrainerFanClub_Text_YouveSurpassedYourFather',
    'A fan enthusiastically declares the player superior to Norman in every regard.', '''
F~Every regard? I don't think we've even had a father-and-child folding contest.|
N~That is a much broader conclusion than a battle comparison can support.|
S~Kind praise. We can accept it without turning family into a scoreboard.|
F~Being compared so completely makes even the compliment feel heavy.|
S~There can be pride in both of you without deciding who is everything best.|
M~An emphatic review that has abolished all categories and uncertainty.|
N~An exhaustive judgment from a remarkably limited sample. Impressive confidence.|
N~I'd rather examine what we improved than claim superiority in every field.|
N~Growing beyond someone need not make their own growth smaller.|
S~He means to celebrate us. We can keep that part.|
S~I'd ask which improvement caught his attention most clearly.
''')
add('lily_fan_norman_different', 'LilycoveCity_PokemonTrainerFanClub_Text_YouAndNormanAreDifferent',
    'A fan notices similarities with Norman but urges the player to discover their own difference.', '''
N~We can resemble someone without becoming their second edition.|
N~Shared traits do not erase individual differences in decision and experience.|
N~We have our own team and our own road. That is a start.|
S~It's a relief when the difference is allowed to stay ours to find.|
N~You learn your own way by doing things, not by staring at a comparison.|
S~At last, the family sequel is allowed a different authorial voice.|
N~A mysterious distinction. Unhelpful, but at least he admits the mystery.|
N~We can notice our choices without forcing them to differ just for the sake of it.|
N~Two branches may share a trunk and still turn toward different light.|
S~Recognition can feel kinder when it leaves room for individuality.|
N~I'd remember the observation without making it another assignment.
''')
add('lily_fan_norman_persist', 'LilycoveCity_PokemonTrainerFanClub_Text_YourFatherNeverGaveUpSoKeepOnBattling',
    'A fan invokes Norman persistence to encourage the player after setbacks.', '''
S~That's a useful thing to inherit: a reason to try again.|
N~A loss can inform the next attempt if we review it carefully.|
N~Rest, learn, come back better prepared. That's how to keep going.|
S~It helps to hear that the person you admire had difficult days too.|
N~Trying again should include looking after the team between attempts.|
S~A family story offers support instead of another impossible comparison.|
N~Persistence is helpful when accompanied by the ability to change tactics.|
N~We should carry the determination and update the plan.|
S~A path can pause without ending.|
S~He is offering an example we can use, not merely someone to match.|
N~I'd ask what Norman changed when he faced his own hard battles.
''')
add('lily_fan_club_purpose', 'LilycoveCity_PokemonTrainerFanClub_Text_WeDiscussStrongestTrainers',
    'A fan explains the club debates strong Trainers and might support the player if famous.', '''
S~A whole room devoted to discussing battles. The chairs must hear some strong opinions.|
N~They compare reputations, though their access to actual battle evidence may vary.|
N~We can visit without needing to win the room over.|
F~I might listen for a while before trying to speak over everyone.|
S~A gathering is nicer when being interested matters more than being right.|
M~The tribunal is in session, and future membership in our audience is conditional.|
N~A committee for determining greatness. I predict excellent disagreement.|
N~I'd ask what criteria they use before taking the rankings too seriously.|
N~Stories gather around strong names, and people gather around the stories.|
N~Fame brings attention. It doesn't automatically bring understanding.|
S~I'd enjoy hearing which moments made each person choose a favorite.
''')
add('lily_fan_handshake', 'LilycoveCity_PokemonTrainerFanClub_Text_OhWoweeItsPlayer',
    'A delighted young fan recognizes the player and requests a handshake.', '''
F~Our hand has become a local attraction. Please let it behave normally.|
S~Recognition can make an ordinary gesture very meaningful to someone.|
S~A handshake's easy enough. Be kind to the kid.|
F~I think I would be nearly as nervous as she is.|
S~It's a small bit of our time and a very big moment for her.|
S~The heroic hand is summoned for ceremonial duty.|
F~An unexpectedly intense examination of ordinary fingers.|
S~A gentle greeting can keep the excitement comfortable for both of them.|
S~A person from a story has become someone within reach.|
S~I would meet her enthusiasm warmly without making her feel foolish.|
S~I'd ask her name as well. This meeting belongs to both people.
''')
add('lily_fan_perfect_record', 'LilycoveCity_PokemonTrainerFanClub_Text_AlwaysCheerForYou',
    'The sole remaining young fan promises support but says she never wants to see the player lose.', '''
N~She is cheering so hard she forgot even good Trainers have bad days.|
N~Confidence should leave room for ordinary variance and the possibility of loss.|
N~We'll try our best. Nobody can promise a perfect record.|
F~I'd hate for her to think a loss means she believed in the wrong person.|
N~Kind support leaves someone room to have a difficult day.|
N~An admirer has given us an impossible contract in very affectionate handwriting.|
N~Endless victories. A modest request, apparently.|
N~What matters is how we make decisions and learn, even when a battle goes badly.|
N~A steady light is still there when a cloud crosses it.|
N~She means well. I would gently loosen that expectation.|
N~I'd tell her what trying again can look like, not just winning.
''')
add('lily_fan_cool_consensus', 'LilycoveCity_PokemonTrainerFanClub_Text_EveryoneThinksTrainerIsCool',
    'A girl seeks agreement that her favored Trainer is cool.', '''
S~She likes the Trainer and would like the room to like liking them too.|
N~A preference does not become more valid merely through unanimous agreement.|
S~She can enjoy her favorite even if others choose differently.|
S~It can feel lonely when you're the only one excited about something.|
S~Different favorites give everybody more to talk about.|
S~A favorable review has been opened for signatures.|
N~Consensus is being requested at enthusiastic volume.|
N~I'd ask what she finds cool instead of asking the room for a vote.|
S~Fondness does not need a chorus to be real.|
S~She wants a shared little moment of excitement. That's understandable.|
S~I'd give her space to tell the story that made her a fan.
''')
add('lily_fan_cool_solo', 'LilycoveCity_PokemonTrainerFanClub_Text_TrainerIsReallyCoolItsJustMe',
    'A girl continues supporting her favorite despite being alone in that preference.', '''
S~A one-person cheering section still counts. It may even get the best seat.|
N~She distinguishes her preference from the majority view without abandoning it.|
S~Good for her. She knows what she likes.|
S~I like the little bit of courage in saying that out loud.|
S~Her favorite doesn't need to become a group decision.|
S~An independent reviewer, undeterred by a catastrophically small readership.|
S~A perfectly respectable solitary enthusiasm.|
N~She may enjoy it more without needing to change everybody else's mind.|
S~One voice can keep company with a distant name.|
S~She's finding a way to stay fond without turning it into an argument.|
S~I'd ask about her favorite moment and let her enjoy remembering it.
''')
add('lily_fan_ideal', 'LilycoveCity_PokemonTrainerFanClub_Text_WishThereWasTrainerLikeThat',
    'A girl dreams of a favorite Trainer who is cool, strong, and kind.', '''
S~She has a list, and I'm very glad nice made it onto the list.|
S~She values conduct as well as battle ability. A sensible combination.|
N~Strong and decent is a better goal than strong alone.|
S~The kind part is what would make me feel comfortable meeting them.|
S~Someone can impress a crowd and still remember the person beside them.|
S~A character brief with an encouraging moral requirement.|
S~A hero expected to possess basic kindness. Refreshing standards.|
N~Kindness is easiest to judge in the small decisions people make.|
S~Strength can hold a door instead of merely breaking one.|
S~She wants admiration to feel safe. That's a good instinct.|
S~I'd ask who has already shown her one of those qualities.
''')
add('lily_fan_child_goal', 'LilycoveCity_PokemonTrainerFanClub_Text_WantToBeStrongLikeYou',
    'An excited boy wants to grow into a Trainer as strong as the player.', '''
S~He's looking at us and seeing a possible future for himself. That's quite a thing.|
S~An attainable example can turn an abstract ambition into a concrete goal.|
N~Start by treating your partner well and learning the basics. Strength follows work.|
F~I don't think I'd know what to say to being somebody's example.|
S~I'd tell him about the practice, so he knows it isn't something you are born with.|
S~Our adventure has unexpectedly become the opening sentence of someone else's.|
S~He has selected a challenging hobby. The optimism is impressive.|
N~I'd show him one useful habit he can start practicing now.|
S~A small person has found a larger shape to grow toward.|
S~He should know there is room to become strong in his own way.|
S~I'd ask what Pokemon he wants beside him when he begins.
''')
add('lily_fan_child_solo', 'LilycoveCity_PokemonTrainerFanClub_Text_OnlyOneWhoCheersForYou',
    'A boy promises to keep cheering for the player even if nobody else does.', '''
S~One steady cheer is worth remembering when the room gets quiet.|
S~His support is framed around belief rather than agreement with the crowd.|
S~Appreciated. He doesn't have to argue with everyone on our behalf.|
S~A small kind statement can make you feel less alone than a whole crowd.|
S~I'd thank him without making him feel responsible for how we do.|
S~A loyal supporter offers an audience even after the fashionable applause ends.|
S~A single voice with admirable persistence.|
N~We can appreciate the kindness without relying on him to keep morale afloat.|
S~A little lamp need not ask the others to stay lit.|
S~He wants us to know his care isn't borrowed from the room.|
S~I'd make sure he knows being here is already enough.
''')
add('lily_fan_other_unbeaten', 'LilycoveCity_PokemonTrainerFanClub_Text_NeverGoingToStopBeingTrainersFan',
    'A lone supporter promises loyalty to another Trainer based partly on an unbeaten reputation.', '''
N~I'd like his loyalty to survive the first time that Trainer has a bad day.|
N~An unbeaten reputation is not a guarantee of future results.|
N~Cheering is fine. Leave the Trainer room to lose and learn.|
N~That sounds like a fragile reason to promise forever.|
N~People deserve a bit of support when the easy victories stop too.|
N~A vow of eternal devotion has been fastened to a temporary statistic.|
N~Never loses. A rumor with an ambitious shelf life.|
N~I'd ask what else he admires besides the reported results.|
N~A name can stay dear after a story of perfection ends.|
N~The affection seems real. The condition underneath it could use some kindness.|
N~I'd like to hear about a battle he actually watched.
''')

add('lily_fan_wicked', 'LilycoveCity_PokemonTrainerFanClub_Text_TrainerIsWickedlyCool',
    'A boy admires a favored Trainer and dreams of a handshake.', '''
S~A handshake has become the grand prize in his private adventure.|
S~A brief personal meeting can carry unusual significance for an admirer.|
S~I get it. Meeting someone you respect can stay with you.|
S~He probably has imagined what he would say more than once.|
S~I'd tell him to say hello simply. Famous people still understand ordinary greetings.|
S~A hero's appearance is eagerly awaited by one very prepared hand.|
S~An autograph-free ambition. Relatively merciful for the hero.|
N~He might enjoy learning how that Trainer practices as much as meeting them.|
S~A distant figure has become someone he hopes to reach.|
S~The admiration is cheerful enough to make an ordinary gesture feel grand.|
S~I'd ask what first made him pick that Trainer as his hero.
''')
add('lily_fan_decent_second', 'LilycoveCity_PokemonTrainerFanClub_Text_ThinkTrainerIsNumberOne',
    'A fan politely prefers another Trainer while acknowledging the player ability.', '''
S~A ranking with manners! I didn't know this room issued those.|
S~He has expressed a preference without treating it as an objective verdict.|
S~Fair enough. We don't need every vote.|
S~I appreciate being allowed to hear that without making it awkward.|
S~Different tastes, and nobody has to leave hungry for an argument.|
S~A measured review has slipped into the club. Extraordinary restraint.|
S~An opinion aware that it is an opinion. Practically revolutionary.|
N~I'd be interested in which choices made that Trainer his favorite.|
S~There is room for more than one strong name in a room.|
S~He leaves our dignity intact while keeping his own preference. Nice.|
S~That sounds like the beginning of a conversation rather than a contest.
''')
add('lily_fan_confirmed', 'LilycoveCity_PokemonTrainerFanClub_Text_YoureAmazingAfterAll',
    'A fan celebrates the player success as confirmation of their original judgment.', '''
S~He is happy for us and a little happy for his own excellent guessing.|
N~The result supports his prediction, though success always seems clearer afterward.|
S~Good to have him cheering. We still did the work ourselves.|
F~I'd rather he saw the effort than thought he could tell everything at first glance.|
S~It's nice that he stuck around long enough to see the progress.|
M~Our success has kindly validated the critic's reputation as well.|
S~A favorable result with a complimentary serving of self-congratulation.|
N~We can acknowledge the support while remembering what actually changed.|
S~Someone has watched a possibility become something real.|
S~He wants us to know he believed early. I can understand that pride.|
S~I'd ask what he noticed at the start that stayed with him.
''')
add('lily_fan_corner', 'LilycoveCity_PokemonTrainerFanClub_Text_ImInYourCorner',
    'A sole supporter tells the player not to worry about other people opinions.', '''
S~A corner with one good friend can feel much bigger than a room.|
S~He is trying to reduce the weight of social comparison before a challenge.|
S~Good advice. Focus on our partner and the next decision.|
S~I like being told we don't have to become louder to deserve support.|
S~A calm word before a hard task can help more than a grand speech.|
S~A loyal supporter offers shelter from the room's endless reviews.|
S~One person granting permission to ignore several others. Practical.|
N~We can set the opinions aside and use what our own preparation tells us.|
S~A steady place to stand can be made from a few kind words.|
S~He's supporting the person, not trying to manage the performance.|
S~I'd thank him for making it easier to breathe in here.
''')
add('lily_fan_other_needs', 'LilycoveCity_PokemonTrainerFanClub_Text_YoureMaybeStrongerThanTrainer',
    'A loyal fan recognizes the player strength but keeps supporting an isolated favorite.', '''
S~He can praise us without leaving somebody else with an empty cheering section.|
S~He separates ability from his decision to offer continued support.|
S~That's decent. Loyalty doesn't need to pick every winner.|
S~I like that he thought about how the other person would feel.|
S~Sometimes you stay because somebody could use a familiar voice.|
S~A supporter declines to let the scoreboard write the entire relationship.|
S~A little loyalty that has survived contact with evidence. Promising.|
N~He can keep cheering without needing to deny what he sees.|
S~A hand need not abandon one shore to acknowledge another.|
S~That is a warmer reason to stay than simply refusing to be wrong.|
S~I'd ask what kept him attached to that Trainer in the first place.
''')
add('lily_fan_changed', 'LilycoveCity_PokemonTrainerFanClub_Text_YouChangedMyMind',
    'A fan admits the player changed her opinion and asks how they became strong.', '''
S~She changed her mind and made room for a question. That's a good turn.|
S~Updating a judgment in response to evidence is healthy reasoning.|
S~Good of her to say it. We can tell her about the practice.|
S~I appreciate when someone can let a first impression go.|
N~I'd start with the everyday work. That's the part someone can use.|
S~A critic has accepted revisions and requested the author's notes.|
S~An admitted change of mind. The room may need a moment to recover.|
N~We can explain a few actual training choices rather than invent a secret.|
S~A fixed thought has opened a little door.|
S~She is curious now, which makes the compliment feel more substantial.|
S~I'd ask what she saw that made her look again.
''')
add('lily_fan_attractive_pressure', 'LilycoveCity_PokemonTrainerFanClub_Text_YouBattleAttractivelyInToughSituation',
    'A lone fan particularly enjoys the player composure in difficult battles.', '''
N~The difficult bit may look exciting from the chair, but our team still feels it.|
N~Effective decisions under pressure can be impressive without making danger desirable.|
N~We'll aim to handle trouble well, not create more for an audience.|
F~I would rather they notice the calm than wish for another hard situation.|
N~A battle can be good to watch and still leave everyone needing a rest.|
N~The audience admires suspense. The participants would also appreciate a safe ending.|
N~Admirable poise, inconvenient circumstances. I favor separating the two.|
N~Preparation helps make hard decisions look smoother than they feel.|
N~Grace under strain is still strain.|
N~It's a real compliment, provided it leaves us room to prefer an easier day.|
N~I'd ask which decision she thought made the difference.
''')
add('lily_fan_standout_other', 'LilycoveCity_PokemonTrainerFanClub_Text_TrainerIsStandout',
    'A fan declares another rising Trainer far stronger than the player.', '''
N~She has a favorite and a very tall measuring stick for everybody else.|
N~A broad ranking needs comparable evidence, not merely a striking reputation.|
N~Fine. We have our own training to focus on.|
N~I wouldn't want every visit to become another comparison.|
N~Admiring one person doesn't require putting the next person down.|
N~A dazzling review has been paired with a gratuitous dismissal of the visitor.|
N~Our unsolicited ranking has arrived. I shall file it somewhere quiet.|
N~If there is a useful technique to learn from that Trainer, that interests me more.|
N~Someone else's brightness does not extinguish the path under our feet.|
N~She could simply say what she likes without making us the contrast.|
N~I'd ask what she has actually seen them do.
''')
add('lily_fan_other_praise', 'LilycoveCity_PokemonTrainerFanClub_Text_NoOneCanKnockYouButTrainerStronger',
    'A nonfan praises the player strength and care while continuing to favor another Trainer.', '''
S~She found nice things to say about us without changing her favorite. That's allowed.|
S~She recognizes multiple qualities even while retaining a different overall preference.|
S~Fair enough. Good treatment of Pokemon is worth noticing too.|
S~I liked hearing care mentioned alongside strength.|
S~You can enjoy two kinds of good without putting them in the same order.|
S~A generous review that retains the critic's original subscription.|
S~A compliment with an attached ranking. At least the compliment is specific.|
N~We can learn from another strong Trainer without competing for her approval.|
S~Two kinds of admiration can share a sentence.|
S~She doesn't have to belong to our fan club to see something good in us.|
S~I'd ask what she admires about each Trainer rather than demand a winner.
''')
add('lily_fan_potential', 'LilycoveCity_PokemonTrainerFanClub_Text_HaventRealizedPotential',
    'An elder sees strength but judges that the player has unrealized potential.', '''
N~Potential is a very large room with surprisingly few directions on the walls.|
N~The judgment would be more useful with a specific area for improvement.|
N~There's always more to learn. Give us something concrete to work on.|
N~Encouragement can feel rather heavy when it sounds like disappointment.|
N~I'd rather know the next useful step than the size of an imagined future.|
N~A reviewer praises the draft while declining to identify the missing chapter.|
N~An unfinished destiny. Apparently those are diagnosed by looking at eyes.|
N~I'd ask which decisions suggest room to improve and how to practice them.|
N~An unopened bud still needs ordinary rain, not merely prediction.|
N~She means we can grow. I would keep that part and ask for details.|
N~I'd ask what she thinks we haven't tried yet.
''')
add('lily_fan_impressed', 'LilycoveCity_PokemonTrainerFanClub_Text_YouImpressive',
    'An elder fan gives the player brief, direct praise.', '''
S~Two words, and somehow they arrived wearing a whole medal.|
S~A concise positive assessment. The approval is unmistakable.|
S~Thanks. Sometimes that's all that needs saying.|
S~I appreciate praise that leaves a little quiet around it.|
S~A short compliment can feel more generous than a long speech.|
S~A complete favorable review with no unnecessary preface.|
S~Excellent editorial restraint. The sentiment survives intact.|
S~A clear response is helpful. We don't have to decode it.|
S~A small sentence can hold a warm weight.|
S~She let the compliment stand on its own. Elegant.|
S~I'd smile and make sure she knows it was heard.
''')
add('lily_fan_hidden_worth', 'LilycoveCity_PokemonTrainerFanClub_Text_OnlyIRecognizeYourTrueWorth',
    'The player sole elder fan claims exclusive insight into their hidden worth.', '''
N~I'm glad she sees something good. I don't think it needs to be a secret club of one.|
N~Her support is welcome; exclusivity is not evidence of greater accuracy.|
N~We can appreciate her without deciding nobody else understands us.|
F~It feels strange when a compliment tries to put a wall around you.|
N~Kindness doesn't need to tell us all the other people are wrong.|
N~A flattering review has reserved all interpretation rights for its author.|
N~Our true worth has apparently appointed a sole distributor.|
N~I'd ask what specific strength she noticed rather than accept a mysterious verdict.|
N~Being seen by one person need not make the rest of the world blind.|
N~The affection can stay. The claim to understand us best needs room to breathe.|
N~I'd welcome the conversation without making it our only source of support.
''')
add('lily_fan_true_strength', 'LilycoveCity_PokemonTrainerFanClub_Text_YourePowerfulButNotTrueStrength',
    'An elder questions the player true strength before admitting she cannot define it herself.', '''
S~She climbed onto a very serious sentence and discovered the ladder was missing.|
N~A distinction without a definition is difficult to evaluate meaningfully.|
N~If she figures out what she means, we can talk about it.|
F~At least she told us when she ran out of an answer.|
S~I like the honesty more than the speech she almost gave.|
M~A grand philosophical reveal has encountered a blank final page.|
S~A devastating critique, narrowly defeated by its own missing content.|
N~We can ask useful questions about strength without pretending to have a complete theory.|
N~A word can sound deep before anyone looks inside it.|
S~She let the confident pose fall away. That's better than bluffing.|
N~I'd ask for an example and see whether we can work it out together.
''')
add('lily_fan_we_win', 'LilycoveCity_PokemonTrainerFanClub_Text_YoureOneWeWantToWin',
    'A fan enthusiastically names the player as the Trainer they want to succeed.', '''
S~A cheer addressed straight to us. No guessing who they're talking about now.|
S~They are expressing support, not predicting a guaranteed result.|
S~Appreciated. We'll put in the work.|
S~Being wanted here feels different from being judged here.|
S~It's nice to hear good wishes without a comparison attached.|
S~The audience has selected its favorite ending for our next appearance.|
S~A plainly stated preference. How mercifully easy to understand.|
S~We can carry the encouragement into preparation rather than rush because of it.|
S~A warm voice has joined the road ahead of us.|
S~They sound happy simply to have someone to cheer for.|
S~I'd make a point of saying thanks before we leave.
''')
add('lily_fan_others_best', 'LilycoveCity_PokemonTrainerFanClub_Text_OthersDontKnowYoureTheBest',
    'The player sole male fan urges them to prove the rest of the club wrong.', '''
N~I'd rather make our partner proud than win an argument we didn't start.|
N~His support is encouraging, but the room's disagreement is not our obligation to resolve.|
N~We'll fight our own battles. No need to add his argument to them.|
N~It feels heavy when believing in you becomes another thing to prove.|
N~A good wish is easier to carry than somebody else's grudge.|
N~Our next battle has been volunteered as evidence in a private dispute.|
N~An unsolicited feud. I was hoping for a quieter membership benefit.|
N~We can focus on controllable choices instead of everyone else's conclusions.|
N~The loudest challenge in the room may not be one we need to answer.|
N~I'd thank him for caring and quietly decline the pressure.|
N~I'd ask what he enjoys about our battles when there is no argument to settle.
''')
add('lily_fan_unheard_other', 'LilycoveCity_PokemonTrainerFanClub_Text_TrainerIsBestNoOneWantsToListen',
    'A lone supporter complains that nobody listens to his praise of another Trainer.', '''
N~Maybe everyone could take turns before this room runs out of hearing.|
N~Repeating a conclusion is different from sharing the observations behind it.|
N~He can keep his favorite. He can't make the whole room agree.|
N~Not being heard can sting, even when the argument is small.|
N~A conversation works better when everybody gets a little space.|
N~A passionate review has found itself without a willing readership.|
N~A shortage of listeners in a room overflowing with speakers. Predictable.|
N~I'd ask him to describe one battle instead of repeat the ranking.|
N~A voice can be lonely even in company.|
N~He may want someone to enjoy the story more than someone to surrender.|
N~I'd listen once, provided he is willing to listen in return.
''')
add('lily_fan_other_power', 'LilycoveCity_PokemonTrainerFanClub_Text_TrainersPowerIsOutOfTheOrdinary',
    'A fan says another Trainer is the extraordinary competitor everyone is discussing.', '''
N~Extraordinary strength sounds useful to learn from, even when it isn't ours.|
N~A reputation is a lead for inquiry, not a substitute for watching decisions.|
N~Strong opponents give us something to prepare for.|
N~I would like to hear the actual battle instead of only the impressive summary.|
N~Admiring someone's skill can give you ideas without making your own work smaller.|
N~A formidable character has arrived in the story through enthusiastic hearsay.|
N~A notably strong Trainer. The adjective budget has clearly been approved.|
N~I'd ask which tactic made the difference and whether it could be countered.|
N~Some names cast a long ripple before the person arrives.|
N~He needn't feel reluctant to praise somebody else while we're here.|
N~I'd ask who first told him and whether they watched the battle themselves.
''')
add('lily_center_theft_heard', 'LilycoveCity_PokemonCenter_1F_Text_HeardAboutRottenScoundrels',
    'A local has heard reports of Pokemon theft and stolen meteorites.', '''
N~That's a nasty pair of things to hear about while you're trying to enjoy town.|
N~The reports involve distinct thefts, possibly linked. Details would help.|
N~Keep partners close and report anything specific.|
D~Rumors like that can make an ordinary outing feel less safe.|
N~People shouldn't have to wonder if their partner is safe in a busy town.|
N~The trouble has traveled here in the form of an unpleasant story.|
N~A very specialized collection of crimes. None of them charming.|
N~I'd separate what he actually saw from what someone told him.|
N~A stolen companion leaves a different kind of emptiness from a stolen stone.|
N~The unease is real even if the details are still secondhand.|
N~I'd ask where he heard it so useful information can reach the right people.
''')
add('lily_center_theft_gone', 'LilycoveCity_PokemonCenter_1F_Text_HaventSeenRottenScoundrels',
    'After the hideout events, a local has not seen the thieves recently.', '''
S~It's good when the news is that the trouble hasn't come back.|
N~A period without sightings is encouraging, though not proof of permanent absence.|
N~Good. People deserve a quieter time here.|
S~I imagine it feels better to walk around without looking for them.|
S~Ordinary business can settle back into the space the worry took up.|
S~The unwelcome cast has stopped appearing in the local daily story.|
S~A pleasantly uneventful report. One of my favorite kinds.|
N~A calmer town is a good result. We can still stay observant.|
S~Sometimes relief arrives as another unremarkable afternoon.|
S~He noticed their absence. That tells you how much their presence mattered.|
N~I'd ask what has started feeling normal again around town.
''')
add('lily_center_world', 'LilycoveCity_PokemonCenter_1F_Text_HowManyKindsOfPokemon',
    'A boy wonders about worldwide Pokemon diversity and wants to trade across the seas.', '''
U~Somebody far away might think our most ordinary Pokemon is an amazing visitor.|
S~Geographic differences give both travel and trading genuine research value.|
S~Plenty out there to meet. Start by learning the ones beside you.|
S~I like imagining someone elsewhere asking the very same question.|
S~A trade can come with stories about a place we've never eaten breakfast in.|
S~An enormous cast, and a young reader eager for the next introduction.|
S~The world remains inconveniently larger than our list. Interesting, though.|
N~I'd compare records with visiting Trainers before trying to count the whole world.|
S~A distant shore can hold a familiar friendship in an unfamiliar shape.|
S~He wants to meet people as well as collect new entries. Lovely.|
S~I'd ask which place he would choose for his first crossing.
''')

add('museum_lily_request', 'LilycoveCity_LilycoveMuseum_2F_Text_PleaseObtainPaintingsForExhibit',
    'The curator asks the player to secure artists permission to exhibit lively modern Pokemon paintings.', '''
S~A new job for our eyes: notice lovely paintings and ask before borrowing them.|
N~He explicitly asks for the artist's permission. That distinction matters.|
N~We can look while traveling. No promises about what we'll find.|
S~I like the idea of helping a painting find people who will enjoy it.|
S~A shared wall can give someone's careful work a whole new audience.|
S~A curatorial quest with the vital requirement that the author actually agrees.|
S~An adventure involving art and permission. Mercifully more civilized than theft.|
N~We should find out how the museum wants artists to submit work.|
S~A lively creature can leave another kind of life on a wall.|
S~He values new work enough to make room for it beside the established collection.|
S~I'd ask what makes a painting feel alive to him.
''')
add('museum_lily_empty', 'LilycoveCity_LilycoveMuseum_2F_Text_WishToFillExhibit',
    'With no paintings contributed, the curator hopes to fill the hall with modern Pokemon art.', '''
N~Empty walls are apparently a very large collection of possibilities.|
N~He has a clear direction for the collection, even before it has works.|
N~A good space. Now it needs people willing to put work into it.|
S~I can almost see the room he is imagining.|
S~A room feels different when someone has plans for welcoming things into it.|
S~The gallery exists first in its curator's stubbornly vivid imagination.|
S~A blank room with standards. I can respect that.|
N~He should make the submission process clear to potential artists.|
N~An empty frame can wait without being finished.|
S~Modern work needs somebody willing to believe it belongs in a museum.|
S~I'd ask whose paintings he has been looking at recently.
''')
add('museum_lily_added', 'LilycoveCity_LilycoveMuseum_2F_Text_ThanksAddedNewPainting',
    'The curator thanks the player for a new painting depicting their Pokemon.', '''
S~Our partner has become somebody's reason to stop and look at a wall.|
S~A particular Pokemon's image is now part of a public collection.|
S~Good to see our partner recognized in a different way.|
S~A little piece of our journey can stay here after we leave.|
S~People will enjoy meeting it through the painting, even when we're far away.|
S~Our traveling companion has acquired a permanent supporting role in a gallery.|
S~A portrait that won't need feeding while we are away. Convenient.|
S~The artist's work and our partner's presence are doing something useful together.|
S~A moment has found a place where strangers can return to it.|
S~I'd want the Pokemon to see the attention its portrait receives.|
S~I'd watch which detail makes visitors lean a little closer.
''')
add('museum_lily_gift_wait', 'LilycoveCity_LilycoveMuseum_2F_Text_KeepThisForYou',
    'With no decoration space, the curator keeps the Glass Ornament reward for another visit.', '''
S~He'll keep the thank-you safe while we find a place to put it.|
N~The reward remains uncollected. The completed collection is unaffected.|
S~No rush. We can return when there's room.|
S~I'm glad he didn't make the delay feel like a problem.|
S~A thoughtful gift can wait for a proper place.|
S~The award ceremony has arranged a perfectly gracious postponement.|
S~A fragile object spared the company of our present clutter. Wise.|
N~We should organize our decoration storage before the next visit.|
S~A kindness can be held for us without being taken away.|
S~He kept the gratitude warm while sorting out the practical detail.|
S~I'd thank him for holding it and make a note to return.
''')
add('museum_lily_return', 'LilycoveCity_LilycoveMuseum_2F_Text_HonorToHaveYouVisit',
    'After the completed collection reward, the curator welcomes the player to enjoy the museum.', '''
S~A visit where we can simply look around. No painting errands attached.|
S~The invitation now centers on enjoying the collection rather than expanding it.|
S~Good. We've earned a quiet look at the work.|
S~I like being welcome without needing to accomplish something first.|
S~Let's take the time to enjoy what everyone helped bring together.|
S~The contributor is invited to become a visitor again. A lovely courtesy.|
S~An official request to relax. I intend to honor it.|
S~We can see how the finished collection works as a whole now.|
S~A familiar room has kept a place for an unhurried return.|
S~He's made us feel like guests rather than useful hands.|
S~I'd spend a little longer with the painting we rushed past before.
''')
add('museum_lily_new_pretty', 'LilycoveCity_LilycoveMuseum_2F_Text_NewPaintingsSurprisedMe',
    'A returning visitor admires the new portraits and wishes her Pokemon could be painted as beautifully.', '''
S~She came back to familiar walls and found a new wish hanging on them.|
S~A changed collection gives returning visitors a reason to look again.|
S~Good art makes people think about the partners they know.|
S~I wonder which little expression she would want the painter to catch.|
S~Her own Pokemon is probably already lovely to her. She wants others to see it.|
S~A gallery visit has produced a prospective commission. Excellent work by the paintings.|
S~The portraits have inspired envy of a fairly harmless variety.|
N~I'd ask what detail made the Pokemon in the paintings feel so vivid.|
S~A painted stranger can remind us of someone waiting at home.|
S~She wants her fondness translated into something other people can see.|
S~I'd ask her to describe the Pokemon she'd put in the portrait.
''')
add('museum_lily_modern', 'LilycoveCity_LilycoveMuseum_2F_Text_NewPaintingsRatherAmusing',
    'An older visitor is pleasantly interested in the topical modern Pokemon paintings.', '''
S~He gave the new paintings a proper look before deciding what to think.|
S~New subject matter can engage an audience familiar with older work.|
S~Good to see him open to something different.|
S~The little surprise in his voice is nice.|
S~It's good when trying something unfamiliar turns out pleasantly.|
S~A traditional visitor has encountered a new style and survived with enjoyment intact.|
S~An unfamiliar painting has escaped immediate condemnation. Progress.|
N~I'd ask what feels different from the work he usually enjoys.|
S~A familiar eye can still find a fresh doorway.|
S~He doesn't have to abandon old favorites to enjoy these.|
S~I'd ask which painting held him there longest.
''')
add('museum_lily_our_partner', 'LilycoveCity_LilycoveMuseum_2F_Text_ThesePaintingsOfYourPokemon',
    'A visitor is delighted to learn that the displayed paintings depict the player Pokemon.', '''
S~The gallery has accidentally been hosting a very polite family album.|
S~The subject's identity gives the work an additional connection for this visitor.|
S~Proud of the team. They deserve the attention.|
F~It feels strange to stand beside something that makes a familiar face so grand.|
S~I'd be happy knowing people enjoy a partner we've raised with care.|
S~The painted protagonist's traveling household has arrived to inspect the reviews.|
S~An impressive family resemblance, preserved in pigment.|
S~It is satisfying to see everyday work become something people can appreciate.|
S~Something dear to us has found a welcome in another person's eyes.|
S~It's a lovely kind of recognition when affection and skill meet.|
S~I'd tell him one small thing about the Pokemon the portrait doesn't show.
''')
add('pepper_meal_choices', 'RustboroCity_Flat1_2F_Text_ComingUpWithMealsIsHard',
    'Walda mother is worn down by choosing what meals to make every day.', '''
N~Cooking happens once. Deciding what to cook somehow happens for the rest of your life.|
N~A repeated planning task can be exhausting even when each individual choice is small.|
N~The family could help make the choices, not just wait to be served.|
N~It sounds like she wants somebody to notice the thinking behind the meal.|
N~I'd make a short list of meals everyone likes, then let them take turns choosing.|
N~The daily menu is a serial work whose readers expect an endless supply of endings.|
N~An eternal question with hungry critics. A grim occupation.|
N~A simple rotating plan could remove some decisions without repeating every day.|
N~The work begins long before anyone sees something on a plate.|
N~She is carrying the invisible part as well as the shopping and cooking.|
N~I'd ask what the rest of the household could take off her hands.
''')
add('pepper_no_phrase', 'RustboroCity_Flat1_2F_Text_OhIsThatRight',
    'The player declines to suggest a funny phrase, and Walda father remains open to future ideas.', '''
S~He'll keep a little space ready for a joke we haven't thought of yet.|
N~He accepts that we don't currently have a useful suggestion.|
S~No harm in admitting we don't have an answer.|
F~Thinking of something funny gets harder when someone waits for it.|
S~We can bring an idea back if one arrives over lunch.|
S~The household comedy department has kindly extended its submission window.|
S~A joke may arrive once it has stopped being mandatory.|
N~A few ordinary observations of what makes Walda smile might help him more.|
S~A little laughter can be invited without being caught.|
S~He lets us leave the question open instead of forcing an answer.|
S~I'd remember what she reacts to if we spend more time in the room.
''')
add('pepper_canceled_phrase', 'RustboroCity_Flat1_2F_Text_OhYouDontKnowAny',
    'After the phrase entry is canceled, Walda father returns to his previous saying.', '''
F~The old joke has been called back for another performance. Brave little joke.|
N~He retains a familiar approach when no new suggestion is supplied.|
N~He can keep trying, but he shouldn't turn smiling into a test.|
N~Walda doesn't have to laugh every time to enjoy him being nearby.|
S~Sometimes children enjoy the familiar thing more than the clever new thing.|
S~The previous material has survived another round of proposed revisions.|
N~An established joke has received an alarming renewal.|
N~He could watch for other things she enjoys rather than repeat one phrase indefinitely.|
N~A quiet child may have a rich day behind a still face.|
N~I would give both father and daughter a little room to be unpolished.|
N~I'd ask when she seems most relaxed, not only when she laughs.
''')
add('pepper_our_joke_fails', 'RustboroCity_Flat1_2F_Text_ShesNotSmilingAtAll',
    'The player suggested phrase fails to make Walda laugh.', '''
F~Our joke has encountered an audience with exceptionally firm standards.|
N~One unsuccessful stimulus tells us little about a child's overall temperament.|
N~Didn't land. No need to put that on Walda.|
F~I think I would blush more than the joke deserved.|
S~A laugh isn't something you can insist on serving at a particular time.|
M~The youngest critic in Rustboro has declined to issue a favorable review.|
N~My material has found its natural audience: silence.|
N~We can try something different, or simply let her be comfortable.|
N~A serious face may be listening more closely than we know.|
N~I wouldn't label her serious just because one suggestion missed.|
S~I'd smile, let the moment go, and notice what interests her next.
''')
add('pepper_dad_joke_fails', 'RustboroCity_Flat1_2F_Text_ShesNotSmilingAtAll2',
    'After the player cancels a first phrase, Walda father own attempt fails to make her smile.', '''
F~Dad supplied the joke himself. Walda supplied an extremely honest pause.|
N~He tried his own idea and observed no smile. That is not a verdict on either of them.|
N~He tried. Now let the kid have a quiet moment.|
N~Sometimes trying so hard makes everyone a little nervous.|
S~He might get a better laugh when he forgets he is trying to get one.|
S~The author has performed his own material before an unpersuaded household critic.|
N~A brave joke, laid gently to rest by a child.|
N~Watching what she already enjoys could guide his next attempt.|
N~Affection does not always return in the shape we request.|
N~He wants to connect with her. The connection can be quieter than laughter.|
S~I'd ask whether she likes faces, sounds, or a favorite little game.
''')
add('pepper_wallpaper', 'RustboroCity_Flat1_2F_Text_ThankYouIllGiveYouWallpaper',
    'Walda laughs at the player phrase, and her researcher father unlocks Friends box wallpapers as thanks.', '''
S~A baby laughed, a dad lit up, and the boxes got redecorated. Excellent chain reaction.|
S~An emotional success inspired him to share a practical piece of his own work.|
S~Glad it helped. He looks happier than any reward could explain.|
S~I think his delight would have been enough of a thank-you.|
S~A little laugh can make a tired parent's whole day.|
S~The comedy has succeeded so thoroughly that it has received a design commission.|
S~A laugh with unexpectedly durable consequences for interior decoration.|
S~He's sharing a skill he knows well in return for help with something unfamiliar.|
S~One small sound has warmed an entire room.|
S~The wallpapers are lovely, but his face is the best part.|
S~I'd remember that first pleased look between him and Walda.
''')
add('devon_stone_caution', 'RustboroCity_DevonCorp_3F_Text_MrStoneGoWithCautionAndCare',
    'After gifts, navigation advice, and a rest, Mr Stone sends the player off cautiously.', '''
S~A sensible farewell after a rather full collection of favors and surprises.|
N~Preparation is useful only if we still make careful decisions while traveling.|
N~Good advice. Let's check the route before we head out.|
S~I like that he ends by caring how we get there.|
N~A fresh start is easier after a proper rest.|
S~The grand meeting concludes with a surprisingly practical blessing.|
N~Caution and care. Two companions unlikely to shout for attention.|
N~We have the information now. Time to use it deliberately.|
N~An open road still asks us to notice where we place our feet.|
S~It makes the farewell feel personal after all the business.|
N~I'd make sure we know the next stop before leaving the building.
''')
add('devon_stone_letter_wait', 'RustboroCity_DevonCorp_3F_Text_CountingOnYou',
    'Mr Stone reminds the player he is relying on their letter delivery.', '''
N~The letter is small, but somebody is waiting for what is inside.|
N~He is reminding us of an outstanding commitment rather than offering a new one.|
N~Let's get the letter where it needs to go.|
N~A short reminder can make an unfinished errand feel suddenly present.|
N~We should keep it somewhere it won't get lost among the supplies.|
N~Our quiet parcel has retained its place in the plot.|
N~The responsibility has not become lighter through being portable.|
N~Let's check our route to Steven instead of leaving this as a vague intention.|
N~Something meant for another person is resting in our hands awhile.|
N~He trusts us. A useful reason to follow through.|
N~I'd remember the person at the other end as well as the person who asked.
''')
add('devon_exp_share', 'RustboroCity_DevonCorp_3F_Text_ExplainExpShare',
    'After receiving Exp Share, Mr Stone explains training a partner without direct participation.', '''
U~A partner can learn without being sent into every dangerous lesson. Very handy.|
S~It distributes battle experience to a holder that did not participate directly.|
N~Good way to help a weaker partner catch up without overexposing it.|
S~I like having a gentler way for someone to join the learning.|
S~Everybody starts somewhere. This makes the early part a little easier.|
S~A junior member may benefit from the adventure without entering every scene.|
S~A way to learn while someone else handles the alarming part. Tempting.|
N~We should check which partner would benefit most before choosing a holder.|
N~Growth can happen beside the struggle as well as inside it.|
S~It gives a less experienced partner room to become ready.|
N~I'd pay attention to how quickly the holder catches up with the team.
''')
add('devon_stone_trends', 'RustboroCity_DevonCorp_3F_Text_NotFamiliarWithTrends',
    'Mr Stone admits work has isolated him from youth trends and wonders if all young people want the League.', '''
S~All young people is quite a big survey to conduct from one office chair.|
N~His sample is biased toward the Trainers who have reason to visit him.|
N~Plenty of people want different things. Best ask a few of them.|
N~He sounds curious, though the question is very large.|
S~Some want to travel, some want to cook, some haven't picked yet. That's normal.|
N~A powerful man discovers the peril of knowing only the characters who enter his office.|
S~Work has eaten the part of his schedule labeled the rest of society.|
N~He could begin by talking to the young people already working in the building.|
N~A generation is many doors, each opening onto a different wish.|
N~I'd answer for ourselves and leave room for everyone else to differ.|
S~I'd ask what he wanted when he was that age.
''')
add('devon_stern_direction', 'RustboroCity_DevonCorp_3F_Text_VisitCaptSternShipyard',
    'A Devon employee directs the player toward Captain Stern at Slateport shipyard.', '''
N~A name and a place. Much better directions than somewhere near the boats.|
N~A specific contact should reduce the uncertainty of delivering the parcel.|
N~Shipyard, then Stern. Clear enough to follow.|
N~I like having somebody definite to ask for.|
N~We can sort the delivery before looking for lunch in town.|
N~The errand now possesses both a destination and a named recipient.|
N~Useful directions. A mercifully underrated form of conversation.|
N~We should ask the shipyard staff if he isn't there when we arrive.|
N~A journey becomes easier when its next door has a name.|
N~That gives us a polite way to introduce ourselves when we arrive.|
N~I'd note where the shipyard is before wandering the harbor.
''')
add('devon_ball_popularity', 'RustboroCity_DevonCorp_3F_Text_RepeatAndTimerHugelyPopular',
    'An employee reports that Devon Repeat and Timer Balls are popular with Trainers.', '''
S~The new inventions have escaped the laboratory and found some busy pockets.|
S~Adoption suggests the specialized uses solve problems Trainers recognize.|
S~Useful gear gets talked about. Sounds like they did good work.|
S~The researchers must be pleased to hear people are using them.|
S~It's nice when the hard work becomes part of somebody else's easier day.|
S~The prototypes have reached the enviable stage of being recommended by strangers.|
S~A commercial success with actual practical content. Encouraging.|
N~I'd ask which situations Trainers find them most helpful in.|
S~An idea has traveled farther than the desk where it began.|
S~Popularity is nicest when people can tell you why they keep choosing it.|
S~I'd enjoy hearing the first unexpected story of how someone used one.
''')
add('mauville_mail_wish', 'MauvilleCity_House2_Text_BuyHarborMailAtSlateport',
    'A woman wishes a bicycle would make shopping in Slateport for Harbor Mail easier.', '''
S~That's a lot of travel planning for a very specific piece of paper.|
N~The transport cost is larger than the item itself. A common access problem.|
N~A bike would shorten the trip. We know where to ask about one.|
S~Some little things become important enough to plan a whole outing around.|
S~I'd combine the trip with other errands and a good meal.|
S~A simple shopping wish has acquired the scope of a travel itinerary.|
N~Stationery has demanded a surprisingly ambitious commute.|
N~A bicycle is useful beyond this one errand too.|
S~A small wish can point someone toward a farther road.|
N~She knows exactly what she wants, even if getting there is awkward.|
N~I'd ask whether she's looking for a particular design.
''')
add('mauville_mail_decline', 'MauvilleCity_House2_Text_ThatsDisappointing',
    'The woman accepts the player refusal to exchange Harbor Mail and explains the Coin Case use.', '''
N~We kept the mail. She kept her case. The world remains reasonably tidy.|
N~The proposed exchange was declined. No ownership has changed.|
N~Fair answer. We can reconsider later if we want.|
N~She sounds disappointed without making the whole room awkward.|
N~A useful offer doesn't have to suit what we need today.|
N~The barter scene ends with both parties retaining their original props.|
N~An exchange has peacefully failed to occur.|
N~We should decide whether the Coin Case is useful before agreeing to trade.|
N~A small refusal leaves both paths where they were.|
N~She gave the reason it might be useful and left the choice with us.|
N~I'd remember the offer if we decide to visit the Game Corner.
''')
add('mauville_case_after', 'MauvilleCity_House2_Text_UseCoinCaseAtGameCorner',
    'After the mail trade, the woman explains where the acquired Coin Case is used.', '''
N~Our mail has become a container for coins. Trading produces unusual family trees.|
N~The exchange is complete, and she has specified the item's intended venue.|
N~Good to know. We can decide whether to visit.|
N~She sounds pleased enough with her half of the trade.|
S~Two people found a use for something the other didn't need.|
N~A piece of stationery has financed an accessory for a different pastime.|
N~Our pockets have acquired a pocket with a very narrow specialty.|
N~We can keep it organized with the equipment for that outing.|
N~A small object has carried two different wishes past each other.|
S~A clear explanation makes the trade feel properly finished.|
N~I'd make sure she has the mail she wanted before we leave.
''')
add('mauville_weird_man', 'MauvilleCity_PokemonCenter_1F_Text_ManOverThereSaysWeirdThings',
    'A visitor finds the unusual old man funny and memorable.', '''
S~Being memorable is easy when your sentences keep taking unexpected exits.|
N~Unexpected statements can be memorable without being particularly informative.|
S~If he's harmless and she's amused, sounds fine.|
S~Sometimes the person you remember is simply the one who surprised you.|
S~A peculiar conversation can brighten an ordinary wait.|
S~The gentleman has acquired a favorable review for unconventional dialogue.|
S~An odd man being appreciated for being odd. Excellent news for some of us.|
N~I'd hear what he actually says before deciding what kind of strange it is.|
S~A familiar room can make room for an unfamiliar voice.|
N~I'd rather let him be interesting than turn him into the room's joke.|
S~I'd ask what he said that stayed with her.
''')
add('mauville_records_update', 'MauvilleCity_PokemonCenter_1F_Text_MyDataUpdatedFromRecordCorner',
    'A visitor Dewford trend data now matches a friend after record mixing.', '''
S~Their pockets have agreed on what Dewford is talking about. Very sociable pockets.|
N~The exchange synchronized a particular piece of local trend information.|
N~Useful to know what changed instead of just assuming nothing did.|
N~It's funny that news from one town can arrive through a friend's visit.|
S~A small piece of somebody else's outing found its way home with them.|
S~A fashionable phrase has migrated through an unusually technical grapevine.|
N~The local trend has become a portable condition. Fascinatingly inconvenient.|
N~A specific changed value tells us more than a vague report that it worked.|
N~A little piece of another place can cross through a shared moment.|
S~They sound delighted to have a detail in common with their friend.|
N~I'd ask what the trend was before and how the new one caught on.
''')
add('mauville_records_curious', 'MauvilleCity_PokemonCenter_1F_Text_RecordCornerSoundsFun',
    'A boy plans to investigate the newly opened Record Corner despite not yet knowing how it works.', '''
S~He has enough curiosity to go upstairs and acquire the missing explanation.|
S~Direct observation is a sensible next step when the service is nearby.|
S~Go ask. Easier than standing down here guessing.|
S~I like being interested enough to try a small unfamiliar thing.|
S~An easy little outing can start with simply asking what is happening.|
S~An invitation discovered, with an admirably short interval before investigation.|
S~A mystery located one staircase away. Manageable scale.|
N~He can ask what it does before agreeing to use it.|
S~A new door in a familiar place can be worth opening.|
S~A little enthusiasm makes asking questions feel less awkward.|
S~I'd ask him what he learned when he comes back down.
''')
add('mauville_rocksmash_first', 'MauvilleCity_House1_Text_ExplainRockSmash',
    'After giving Rock Smash, its enthusiastic owner explains removing boulders from paths.', '''
U~An obstacle can become several much smaller obstacles. Very decisive.|
N~The move provides a field application beyond its battle effect.|
N~Useful when a boulder blocks the route. Check the surroundings first.|
N~He is wonderfully excited about a problem becoming rubble.|
N~We should keep clear of where the broken pieces will fall.|
S~The local obstacle-removal enthusiast has reached his favorite part of the speech.|
N~A remarkably forceful solution to an inconvenient piece of geology.|
N~We should choose a safe angle and make sure nobody is on the other side.|
N~A hard boundary can become a passage, with enough care and force.|
N~He gives that explanation as though the rocks personally offended him.|
N~I'd ask which blocked paths nearby are safe to open.
''')

add('slateport_ferry_unavailable', 'SlateportCity_Harbor_Text_FerryServiceUnavailable',
    'The harbor attendant explains that the ferry service is not yet operating.', '''
N~A harbor full of water, and the particular ride we wanted is still missing.|
N~The service is unavailable. A different route is needed for now.|
N~We'll check the other travel options. No point waiting here all day.|
N~At least we know before settling in for a long wait.|
N~We can use the stop to sort supplies while planning another way.|
N~Our sea voyage has been postponed before acquiring a first chapter.|
N~The timetable currently consists of not yet. Clear, if inconvenient.|
N~I'd ask when they expect service to begin, if they know.|
N~A shore can promise a journey before it can offer one.|
N~The attendant looks sorry enough. We needn't make it more difficult.|
N~I'd find out where they post updates about the service.
''')
add('slateport_ferry_decline', 'SlateportCity_Harbor_Text_SailAnotherTime',
    'After the destination choice is canceled, the attendant welcomes a future sailing.', '''
S~The ship can keep its appointment with the sea. We'll pick ours later.|
N~No destination was committed to. Our travel plan remains open.|
N~We'll sail when we're ready. Plenty to finish on land.|
S~I like being able to change plans without a fuss.|
N~Better to settle the route before everybody has boarded.|
S~The voyage remains available for a later edition of the itinerary.|
S~A gracious cancellation. Almost as pleasant as not scheduling anything.|
N~We can compare destinations before coming back to choose.|
N~A departure can wait without becoming a lost possibility.|
S~The welcome stayed warm after the answer became no.|
N~I'd remember the boarding point for when we do want to go.
''')
add('slateport_sub_dream', 'SlateportCity_Harbor_Text_LoveToGoDeepUnderwaterSomeday',
    'A harbor visitor dreams of exploring the seafloor.', '''
U~The bottom of the sea is a very ambitious place to put someday.|
S~A useful ambition would begin with learning the equipment and conditions.|
N~Good dream. Prepare properly before chasing it.|
S~I wonder what they imagine the light looks like down there.|
S~Some places make you curious enough to learn a whole new way to travel.|
S~A future expedition has begun as a quiet wish beside the harbor.|
N~A holiday without ordinary weather. Several other complications, though.|
N~I'd ask what training local divers recommend to a beginner.|
N~A hidden landscape waits below a familiar surface.|
S~I like that they are interested in experiencing the place itself.|
S~I'd ask what first made them want to see the seafloor.
''')
add('slateport_weather_warning', 'SlateportCity_Harbor_Text_AbnormalWeather',
    'A harbor worker recommends consulting the Weather Institute about widespread abnormal weather.', '''
N~The sea is difficult enough without the weather inventing new rules.|
N~A primary source at the institute would be more informative than a secondhand report.|
N~Check the forecast before traveling. Strange weather is worth taking seriously.|
N~It sounds unsettling when even the people watching the weather are surprised.|
N~Good information can keep a whole crew from making a bad departure.|
N~The ominous rumor comes with a sensible address for further inquiry.|
N~Abnormal weather. An uncomfortably broad category of inconvenience.|
N~I'd ask which areas are affected and what measurements changed.|
N~The air leaves warnings that people must learn to read.|
N~He knows where his own knowledge stops and points us toward someone who knows more.|
N~I'd ask the institute what travelers should do differently right now.
''')
add('slateport_sub_space', 'SlateportCity_Harbor_Text_SubTooSmallForMe',
    'A would-be expedition member cannot fit in the submarine alongside Captain Stern.', '''
F~A submarine with room for the dream, but not quite enough room for the dreamer.|
N~Occupied volume is a hard constraint in a small pressure vessel.|
N~No squeezing past the safe capacity. Better to wait for another way.|
D~It must be disappointing to be that close to going.|
N~Nobody should spend an expedition unable to move comfortably.|
N~An enthusiastic participant has encountered the least negotiable critic: the floor plan.|
N~An adventure prevented by arithmetic and shoulders. Cruel but sensible.|
N~Future designs should account for the people who actually need to use them.|
N~A narrow doorway can stand between a person and a wide wish.|
N~He can be disappointed without pretending the space problem will disappear.|
N~I'd ask whether there is another part of the expedition he can join.
''')
add('slateport_stern_same_thugs', 'SlateportCity_Harbor_Text_SameThugsTriedToRobAtMuseum',
    'Stern recognizes Team Aqua as the thieves from the museum.', '''
N~The same trouble has changed buildings without improving its manners.|
N~Recognition connects the present threat with an earlier attempted theft.|
N~Then we know to take them seriously and protect the people here.|
N~It must be upsetting to recognize a danger before knowing how to stop it.|
N~They have already made his work difficult once. That's enough.|
N~A returning villain has neglected to bring a new profession.|
N~Familiar faces, persistently poor conduct.|
N~We can use what we learned from the earlier incident without assuming an identical plan.|
N~An old disturbance has found another door into the day.|
N~Recognition can be useful even when it brings no relief.|
N~I'd ask what he saw them do this time.
''')
add('slateport_stern_sub_stolen', 'SlateportCity_Harbor_Text_CaptSternWhyStealMySubmarine',
    'After the submarine theft, Stern fears Aqua may be targeting a sleeping seafloor Pokemon.', '''
N~They took his ship and left him trying to guess how much worse it could become.|
N~Their choice of vehicle suggests an underwater target. His concern deserves investigation.|
N~He shouldn't chase them unprepared. We need a plan and proper equipment.|
D~He sounds shaken by the thought that his own work might help them.|
N~A stolen tool can endanger people far beyond its owner.|
N~The theft has opened a darker question than how to recover the vessel.|
N~An alarming theory, regrettably supported by the choice of transport.|
N~We should establish what the submarine can reach and what support is available.|
N~Something made to discover can be turned toward disturbing what sleeps.|
N~His fear is reasonable. It doesn't mean he is to blame for their decision.|
N~I'd ask who can help track where a vessel like that could go.
''')
add('slateport_stern_not_fault', 'SlateportCity_Harbor_Text_TeamAquaLeftNeedDive',
    'Stern absolves the player of blame for Aqua escaping and suggests finding Dive expertise in Mossdeep.', '''
N~He's right. We didn't build their bad decisions, and we can't outrun a submarine on foot.|
N~The constraint is practical, not a personal failure. Dive expertise is a concrete lead.|
N~Take the lead to Mossdeep. Leave the blame where it belongs.|
S~I'm glad he said that plainly before giving us another thing to do.|
N~A hard setback is easier to face when somebody refuses to make it your fault.|
N~The captain replaces an impossible chase with a possible next step.|
N~A sensible assessment of our lack of submarine-catching legs.|
N~We need the right capability before attempting the next part.|
N~The path forward can begin after the weight of blame is put down.|
N~He offers help without turning the help into another accusation.|
N~I'd follow up with divers who know the waters near Mossdeep.
''')
add('slateport_stern_dive_lead', 'SlateportCity_Harbor_Text_NeedDiveToCatchSub',
    'Stern directs the player to Mossdeep divers to learn how to follow the stolen submarine.', '''
N~We need a way down, not a faster way to wave at the water.|
N~The proposed pursuit requires a capability we should secure before attempting it.|
N~Mossdeep is the lead. We'll ask people who know the depth.|
N~A definite next step makes the whole problem feel less impossible.|
N~We should learn how to come back up as well as how to go down.|
N~The chase pauses for the acquisition of a very necessary skill.|
N~At last, a plan acknowledging the inconvenient volume of water involved.|
N~Local divers can explain hazards as well as the move itself.|
N~An unseen path still needs a safe way home.|
N~He's sharing the useful part instead of pretending the task will be simple.|
N~I'd ask the divers what they know about that particular stretch of sea.
''')
add('slateport_ferry_soon', 'SlateportCity_Harbor_Text_WontBeLongBeforeWeFinishFerry',
    'Stern credits Briney arrival with bringing the ferry near completion.', '''
S~Briney's experience has turned not yet into nearly. That's a useful kind of magic.|
S~The additional expertise has improved the project's progress.|
S~Good. More people will have a reliable way to travel soon.|
S~He sounds pleased to have someone he trusts helping.|
S~A good pair of hands can change the mood of a whole job.|
S~The long-awaited voyage is approaching the end of its construction chapter.|
S~Nearly finished. A phrase with considerably more hope than the earlier version.|
S~I'd ask which remaining checks they need before passengers can board.|
S~A careful craft can bring distant homes a little closer.|
S~He made sure Briney's contribution didn't disappear behind the finished product.|
S~I'd like to hear how the two of them first started working together.
''')
add('slateport_ferry_finished', 'SlateportCity_Harbor_Text_FinishedMakingFerry',
    'Stern celebrates the completed S.S. Tidal, credits Briney, and invites the player aboard.', '''
S~The ferry is real now! All those plans have finally become a very large ride.|
S~A completed vessel turns their collaboration into a useful public service.|
S~Well done to the crew. Worth taking a trip when we're ready.|
S~I like that he wants us to enjoy the thing they made.|
S~A launch deserves a celebration, and so do the people who did the work.|
S~The project's finale includes an invitation to become part of the next story.|
S~A boat with a name, a purpose, and apparently sufficient room. Excellent.|
U~I'd love to see what they learned from Briney reflected in the finished design.|
S~Something built on land is ready to belong to the water.|
S~Giving Briney credit makes the invitation feel warmer.|
S~I'd want to hear what the crew felt as the first passengers boarded.
''')
add('slateport_scanner_no', 'SlateportCity_Harbor_Text_IfYouWantToTradeLetMeKnow',
    'Stern accepts a declined Scanner exchange while leaving his offer open.', '''
N~He can't use our answer yet, but he can leave us room to change it.|
N~The exchange is optional, and the equipment remains with us.|
N~No trade for now. He knows where he stands.|
N~I'm glad disappointment didn't become an argument.|
N~We can decide what is useful without being rushed by someone else's need.|
N~The bargain remains open, with its final page mercifully unsigned.|
N~A device of no use to us has acquired a surprisingly complicated farewell.|
N~We should compare the offered items before choosing.|
N~A wish can remain open without becoming a demand.|
N~He pressed a little, then respected the answer. That matters.|
N~I'd remember what he offered if we come back to reconsider.
''')
add('slateport_scanner_yes', 'SlateportCity_Harbor_Text_ThisWillHelpResearch',
    'The Scanner exchange is complete and Stern thanks the player for helping research.', '''
S~The Scanner has finally reached the person with a sea-sized use for it.|
S~The transfer is complete. Specialized equipment can now support the intended research.|
S~Good. He'll put it to proper use.|
S~He sounds relieved to have the missing piece in hand.|
S~Something we carried around is going to make somebody's work easier.|
S~The wandering instrument has reached the chapter where its purpose begins.|
S~A technical object reunited with someone qualified to be excited about it.|
S~I'd ask what new observations the Scanner will let them make.|
S~A small tool can open a larger hidden place to understanding.|
S~His thanks feel tied to the work it will help, which I like.|
S~I'd come back later to hear what they discovered with it.
''')
add('name_rater_return', 'SlateportCity_NameRatersHouse_Text_DoVisitAgain',
    'The Name Rater politely ends a canceled or declined naming session.', '''
S~Our Pokemon's name has survived the consultation unruffled.|
N~No naming change was committed to during this visit.|
N~We're fine with it for now. Good to leave the choice open.|
S~I'm glad declining didn't need a speech.|
S~A familiar name doesn't have to change just because someone offers.|
S~The editorial consultation concludes without revisions.|
S~A perfectly satisfactory result: no unnecessary alterations.|
N~We can come back when we have a deliberate change in mind.|
N~A name can rest where it has already found a home.|
S~He let the decision stay ours. A good way to end the visit.|
S~I'd say thanks and keep the introduction we already know.
''')
add('name_rater_egg', 'SlateportCity_NameRatersHouse_Text_ThatIsMerelyAnEgg',
    'The Name Rater refuses to assess a Pokemon Egg nickname.', '''
F~The Egg has not yet submitted a name for critical consideration.|
N~There is no hatched Pokemon's nickname for him to assess yet.|
N~Let it hatch first. No hurry on the naming.|
S~It might be easier to find a name once we meet the one inside.|
S~We can wait until there's a face to go with the idea.|
S~The candidate has arrived before the character introduction.|
N~The critic has rejected our most quietly mysterious applicant.|
N~We need a hatched partner before this service applies.|
S~A little life can begin before its name does.|
S~There is time to choose something that feels right later.|
S~I'd rather meet the Pokemon than decide everything from the shell.
''')
add('name_rater_traded', 'SlateportCity_NameRatersHouse_Text_MagnificentName',
    'The Name Rater declines to change another Trainer Pokemon name and praises the existing one.', '''
S~Somebody else chose that name with a little thought we weren't here to see.|
N~He preserves a name assigned by the previous Trainer.|
N~Keep the name it arrived with. We can learn the partner behind it.|
S~A familiar name may be one comfortable thing on a new journey.|
S~It comes with a bit of its old home attached.|
S~The previous author retains the title, with an enthusiastic endorsement from the editor.|
S~An impeccable name. Conveniently beyond the critic's jurisdiction.|
N~Continuity can help us remember the Pokemon's history beyond our own team.|
S~An old voice can remain folded inside the sound we use now.|
N~A name carries a relationship as well as a style choice.|
S~I'd ask the previous Trainer how they came to choose it if we get the chance.
''')
add('name_rater_changed', 'SlateportCity_NameRatersHouse_Text_MonShallBeKnownAsName',
    'After the player chooses a different nickname, the Name Rater declares the new name superior.', '''
S~A new name! Our Pokemon may need a moment to update its who-is-being-called list.|
N~The nickname has changed. We should use it consistently so the partner recognizes it.|
S~If it fits, good. Let's say it kindly.|
S~A name feels different once you speak it to the Pokemon itself.|
S~I'd try it gently and see how the partner responds.|
S~The revised title has been published with extravagant editorial approval.|
S~A new name, declared superior by the man responsible for approving new names.|
N~A useful change should be something we actually want to keep calling it.|
S~A familiar companion can meet us through a different sound.|
S~The best test is how naturally it feels when we say it together.|
S~I'd remember the first time it turns toward that new name.
''')
add('name_rater_unchanged', 'SlateportCity_NameRatersHouse_Text_NameNoDifferentYetSuperior',
    'The unchanged nickname is nevertheless declared superior by the Name Rater.', '''
L~The name has improved so much it has become exactly the same name. Remarkable.|
N~The output is unchanged. His evaluation has altered without a change in the subject.|
S~Same name. Saved us learning a new one.|
F~I suppose being certain about the old choice can feel like a new choice.|
S~The familiar name is still a perfectly good thing to enjoy.|
M~A masterful revision whose restraint includes making no revision whatsoever.|
S~An invisible improvement. The most convenient kind to maintain.|
N~There is no functional change, but we have confirmed our preference.|
S~Sometimes returning to a name makes it feel chosen again.|
S~He gave the old name a fresh bit of confidence. I can live with that.|
S~I'd laugh with him and see whether our Pokemon noticed any difference.
''')
add('deleter_farewell', 'LilycoveCity_MoveDeletersHouse_Text_ComeAgain',
    'The Move Deleter ends a canceled or declined session and invites another visit.', '''
N~The moves are staying where they are today. Their tiny eviction notices are canceled.|
N~No deletion occurred. The current move set remains available.|
N~Better to wait if we aren't sure.|
S~It's a relief that asking doesn't commit us to forgetting anything.|
N~We can think it over without holding up the room.|
N~The editor puts down the eraser until a clear decision arrives.|
N~Forgetting has been postponed. An oddly memorable outcome.|
N~We should choose what replaces a move before removing it.|
N~A skill can stay with us until letting it go has a purpose.|
N~A calm ending makes it easier to return when the choice is clearer.|
N~I'd revisit the team's needs before making another appointment.
''')
add('deleter_one_move', 'LilycoveCity_MoveDeletersHouse_Text_MonOnlyKnowsOneMove',
    'The Move Deleter refuses to remove a Pokemon only known move.', '''
N~Taking its only move would leave a rather awkward hole in the instructions.|
N~The last remaining move is protected so the Pokemon retains an action.|
N~Keep it. Our partner needs something it can do.|
N~I'm glad that limit is there before anyone tries to remove everything.|
N~We should give it another option before taking this one away.|
N~The editor has declined to erase the book's only sentence.|
N~An empty move list seems like a particularly bleak syllabus.|
N~The minimum capability needs to stay intact. Sensible safeguard.|
N~Even letting go needs somewhere left to stand.|
N~A change should leave the partner with more room, not none.|
N~I'd look at what it can learn next before returning.
''')
add('deleter_egg', 'LilycoveCity_MoveDeletersHouse_Text_EggCantForgetMoves',
    'The Move Deleter refuses to perform the service on an Egg.', '''
F~We have asked the Egg to forget something before it has introduced itself.|
N~The service cannot operate on an unhatched Pokemon.|
N~Leave the Egg be. We can talk about moves after it hatches.|
N~There is plenty of time to meet the one inside before changing anything.|
S~Let the little one arrive before we start rearranging its day.|
N~A premature revision request has reached a still-sealed manuscript.|
N~The Egg has wisely arrived without an editable curriculum.|
N~We need a hatched Pokemon for this selection to make sense.|
N~A beginning should be allowed to begin first.|
N~I'd rather learn who is inside than plan what it should leave behind.|
N~We can return after we've had time to know the Pokemon.
''')
add('deleter_surf_needed', 'LilycoveCity_MoveDeletersHouse_Text_CantForgetSurf',
    'The last available Surf user cannot have Surf removed.', '''
N~Our way across the water is requesting continued employment. Sensible move.|
N~Surf is retained because this is our last available user. It preserves travel access.|
N~Keep it until another partner can get us across safely.|
N~I would rather not discover the missing ride while standing on an island.|
N~Some useful things need to stay until another arrangement is ready.|
N~The plot has declined an edit that would strand its entire cast.|
N~A vital transport service has successfully resisted deletion.|
N~Redundancy first, removal second. A practical order of operations.|
N~The path home should not be the thing we choose to forget.|
N~A safety limit is welcome when a small menu choice can have a large effect.|
N~I'd check who else can learn it before trying to change this partner.
''')
add('deleter_success', 'LilycoveCity_MoveDeletersHouse_Text_MonHasForgottenMove',
    'The selected Pokemon has successfully forgotten the selected move.', '''
N~One move has left the list. I hope we have something useful ready for that room.|
N~The deletion is complete. The available move set has genuinely changed.|
N~Done. Let's make sure the remaining moves cover what we need.|
N~It is a strange thing to hear a forgetting announced so neatly.|
N~There's room for something new now. We should choose it with care.|
N~A deliberate edit has been made; the next lesson can take its place.|
N~A very successful absence. Unusual work to congratulate someone on.|
N~We should review the result rather than assume one removed move solves the whole plan.|
N~An empty space can be a choice rather than a loss.|
N~The change is settled. Now the partner needs a clear direction for what comes next.|
N~I'd check how the new arrangement feels before making another change.
''')
