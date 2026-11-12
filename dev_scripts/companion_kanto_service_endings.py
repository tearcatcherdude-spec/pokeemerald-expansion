"""Fixed shared service endings reached by registered Kanto actor scripts."""
ROWS=[]
EMOTIONS=dict(N='neutral',S='soft_smile',A='annoyed',F='flustered',D='sad',U='surprised',M='smug',L='laughing')
def add(key,labels,subject,lines):
    replies=[]
    for line in lines.strip().split('|'):
        line=line.strip()
        if len(line)>1 and line[1]=='~' and line[0] in EMOTIONS:line=EMOTIONS[line[0]]+line[1:]
        replies.append(line)
    assert len(replies)==11,(key,len(replies))
    ROWS.append(dict(key='kanto_service_end_'+key,labels=labels.split(),subject=subject,replies=replies))
add('profile_later','Text_TellMoreNextTime',
    "A club member looks forward to hearing more about the player on another visit.",'''
S~We have left a little room in the conversation for the next hello.|
S~An open-ended invitation encourages a future visit without requiring immediate disclosure.|
S~We can share more another time, if we want.|
S~It is nice to have a conversation that does not demand the whole story at once.|
S~Knowing someone can happen over several ordinary visits.|
S~The interviewer has sensibly saved a few pages for the next instalment.|
S~A little left unsaid can be comfortable rather than ominous.|
S~More time gives people a chance to share details they actually want to share.|
S~A person can unfold slowly without being a riddle to solve.|
S~Interest feels warmer when it gives someone room to answer later.|
S~I wonder what small part of the journey we will want to talk about next time.
''')
add('profile_cancel','Text_DecidedNotTo',
    "A club member calls the player fickle for cancelling a profile entry.",'''
N~Changing your mind is a normal feature of having a mind. No repair required.|
N~Cancelling a choice does not establish an unreliable personality.|
N~We can stop. No explanation owed for a profile we do not want to give.|
N~That little comment makes the conversation feel less welcoming than it needed to.|
N~A person should get to decide how much of themselves to put on display.|
N~The editor has mistaken a withdrawn submission for a character flaw.|
N~An unused form is a small thing to hang a personal judgment on.|
N~A cancel option ought to remain an acceptable outcome.|
N~A door opened briefly can still be closed without apology.|
N~A graceful response would have left a much better chance of another visit.|
N~I wonder whether that remark ever makes anyone more eager to talk.
''')
add('profile_unchanged','Text_LikeProfileWayItIs',
    "A club member accepts the choice to leave the current profile unchanged.",'''
S~The little introduction is staying as it is today. No compulsory renovation.|
S~Retaining an existing profile is a valid choice when the owner is satisfied with it.|
S~Our choice. Good that it is accepted.|
S~It is comfortable when something does not need changing just because we were asked.|
S~Sometimes the familiar version still says what we want it to say.|
S~The current edition has survived review without demands for revision.|
S~A small unchanged thing can be an entirely deliberate decision.|
S~Keeping a working choice is often more useful than changing it for the sake of activity.|
S~A name on a doorway need not be repainted every time someone visits.|
S~Agreement without pressure makes the whole exchange feel easy.|
S~I wonder which part still feels most like us when we read it back.
''')
add('profile_pressure','Text_DontBeLikeThat',
    "A club member pushes for a profile after the player declines to share one.",'''
N~A little introduction should not need to be pulled out like a stubborn tooth.|
N~Interest in another person does not create an entitlement to their information.|
N~We can decline. They need to let the answer stand.|
N~I would feel more like talking if the quiet answer were allowed first.|
N~Friendliness works better when it leaves people room to choose.|
N~The enthusiastic interviewer has misplaced the part where the subject agrees.|
N~A conversation grows awkward when a polite boundary becomes something to coax away.|
N~An optional profile should remain optional after the first refusal.|
N~A closed little window is not an invitation to keep tapping the glass.|
N~That appeal would land better if it did not make privacy sound unfriendly.|
N~I wonder whether they realize how much easier a relaxed invitation would be to accept.
''')
add('profile_received','Text_ProfileSaysSomethingAboutYou',
    "A club member feels better acquainted with the player after receiving a profile.",'''
S~A few chosen words have given the conversation a little more shape.|
N~A profile offers a selected introduction, not a complete account of the person.|
S~A friendly start. Real familiarity will take more time.|
S~It is nice when a small thing shared is received warmly.|
S~A simple introduction can make the next conversation feel easier.|
S~The brief character sketch has won an unusually affectionate review.|
S~A little self-portrait can open a conversation without finishing the person inside it.|
S~The useful part is having something new to talk about, not pretending the profile explains everything.|
S~A few words can light the first step without showing the whole path.|
S~Warm interest is lovely, provided it leaves room for us to be more than the introduction.|
S~I wonder what they will actually remember after the words have become familiar.
''')
add('profile_familiar','Text_HeardThatBefore',
    "A club member says the profile reminds them of something a distant cousin used to say.",'''
S~Our words have accidentally waved hello to somebody's faraway cousin.|
S~A familiar phrase can trigger a personal association without the speakers knowing one another.|
N~A coincidence, perhaps. No need to invent more than the memory they mentioned.|
S~It is tender how an ordinary phrase can bring someone back into the room for a moment.|
S~Familiar words can make a distant person feel a little nearer.|
S~An unexpected echo has introduced an absent relative to the conversation.|
S~Memory is very good at finding a side door through an ordinary sentence.|
S~Recognizing a phrase does not tell us whether it came from the same source.|
S~A few words have tugged gently on an old thread.|
S~That is a warmer response than simply deciding the phrase is unoriginal.|
S~I wonder what the cousin was like that made those words stay with them.
''')
add('badge_pass','Text_OnlyPassWithBadgeOhGoAhead Text_OhThatsBadgeGoRightAhead',
    "A League checkpoint guard recognizes the required Badge and allows passage.",'''
S~The Badge has introduced us more efficiently than a very long explanation would have.|
N~The guard has verified the required credential and granted passage.|
N~Cleared. Keep the team ready for what comes next.|
S~A little recognition makes the road ahead feel more real.|
N~A checkpoint passed is a good moment to make sure we are still prepared.|
S~The gatekeeper has approved the next scene on documentary evidence.|
S~A small piece of proof has made the path a little wider.|
N~The access requirement is satisfied. Preparation still matters beyond the gate.|
S~The road has asked a question and accepted the answer we earned.|
S~It is satisfying to see earlier work recognized so plainly.|
S~I wonder how many journeys those guards have watched finally reach this point.
''')
add('badge_missing','Text_OnlyPassWithBadgeDontHaveYet',
    "A League guard refuses passage because the required Badge has not been earned.",'''
N~The next stretch of road has a very specific piece of unfinished business attached.|
N~The required credential is missing, so the checkpoint does not permit passage.|
N~We need the Badge first. No point pushing past the guard.|
N~A closed way can still tell us clearly what the next step is.|
N~We can plan the missing challenge before trying this route again.|
N~The journey has encountered a chapter that cannot yet be skipped.|
N~A firm boundary is easier to work with when its reason is plain.|
N~The condition is concrete. We can prepare for the challenge that satisfies it.|
N~The road is waiting on proof from somewhere behind us.|
N~A clear requirement is better than being made to guess why we are refused.|
N~I wonder how often travellers arrive here already knowing which Badge they still need.
''')
add('badge_rule','Text_CantLetYouPass',
    "The first League checkpoint guard firmly enforces the missing-Badge restriction.",'''
N~The guard has used the smallest possible signpost toward not this way yet.|
N~The refusal enforces the checkpoint requirement rather than offering a discretionary exception.|
N~We need to meet the condition. Arguing will not help.|
N~A firm answer can feel abrupt even when the reason is straightforward.|
N~Better to put the effort toward the missing challenge than this conversation.|
N~The gatekeeper has declined to negotiate an exceptionally firm admission policy.|
N~A uniform does sometimes contain somebody whose entire afternoon is saying not yet.|
N~We should resolve the requirement instead of repeating the same request.|
N~A gate remains a gate even when the traveller feels ready to be beyond it.|
N~At least there is no pretence that a little flattery would change the answer.|
N~I wonder whether the guard gets to hear the stories when those same travellers return qualified.
''')
add('everstone','Route10_PokemonCenter_1F_Text_ExplainEverstone',
    "Oak's aide explains that an Everstone can prevent a Pokemon from evolving.",'''
S~An aid for saying not yet to a very dramatic growth spurt.|
S~Evolution is not the only valid development plan; the Everstone provides a means of delaying it.|
N~Useful option. We can decide what suits the Pokemon and the team.|
S~I like knowing that change does not always have to happen at the first opportunity.|
N~A thoughtful choice is better than assuming every available change must be taken.|
S~The next act may be postponed without cancelling the character's future.|
S~Remaining familiar can be a deliberate choice rather than a failure to grow.|
S~A reversible way to control the timing gives a trainer more planning options.|
S~A stone can hold a little door closed until the right season.|
S~It is nice to hear an option explained without making one choice sound compulsory.|
S~I wonder what makes each trainer decide that this is the right form for now.
''')
add('island_battle_decline','SevenIsland_House_Room1_Text_OhYouWontBattle',
    "The old woman accepts a declined visiting-trainer battle and invites the player to return.",'''
N~A disappointed little pause, then the invitation is left where we can find it later.|
N~The refusal is accepted without forcing the optional battle to continue.|
S~We can leave peacefully. She has kept the offer open.|
N~I can hear that she hoped we would stay, but she lets us choose.|
S~A quiet refusal can still leave room for a friendly future visit.|
S~The prospective performance has been postponed with unusually wistful grace.|
S~Disappointment and good manners have managed to share the same small silence.|
N~There is time to reconsider a challenge without committing to it now.|
S~A waiting room can hold an invitation without becoming a trap.|
S~She makes the next meeting possible by not spoiling this goodbye.|
S~I wonder what she enjoys most about watching a new challenger take part.
''')
add('minigame_adapter','Text_AdapterNotConnectedMinigame_Frlg',
    "The minigame attendant reports that the required Wireless Adapter is not connected.",'''
N~The game has reached the less playful part where a missing connection gets the final say.|
N~The required adapter connection is absent, so this activity cannot begin.|
N~No game right now. We can choose something else.|
N~A small practical obstacle can still be disappointing when you came ready to play.|
N~No need to spend the whole visit standing at an unavailable activity.|
N~The proposed entertainment has been postponed by its least entertaining prerequisite.|
N~An empty connection has displayed an impressive ability to end a conversation.|
N~The missing hardware requirement needs resolving before another attempt.|
N~The doorway is here, but the little bridge it needs is absent.|
N~It is better to receive a clear explanation than a cheerful invitation that goes nowhere.|
N~I wonder how often the attendant has to deliver that exact disappointing news.
''')
add('dodrio_info','Text_DodrioBerryPickingInfo_Frlg',
    "The attendant explains directing Dodrio's three heads to catch falling Berries.",'''
L~Three heads and one falling Berry sounds like a family argument with unusually good reflexes.|
S~The activity combines directional timing with coordinating three possible catching positions.|
N~Watch the falling Berries before committing to a direction.|
S~It sounds busy in a cheerful sort of way.|
S~A Berry-catching contest is an excellent use of that many eager beaks.|
S~A three-headed ensemble performing under the demanding direction of gravity.|
S~The instructions have somehow made falling fruit sound competitive.|
S~Observe the timing first. Good coordination should beat frantic button presses.|
S~Three little attentions must share one falling moment.|
S~An entertainingly specific activity for an entertainingly specific Pokemon.|
S~I wonder whether each head has a different idea of who caught the most.
''')
add('minigame_directions','Text_TalkToManToPlay_Frlg',
    "A minigame helper directs interested players to the man beside her.",'''
S~A tiny set of directions with the destination already standing beside it. Convenient.|
N~The helper has identified the correct person to handle participation.|
N~We know whom to ask if we want to play.|
S~It is less awkward to approach when someone has told you that is the right person.|
N~We can hear the arrangements before deciding whether the game suits us.|
S~The welcoming voice has correctly identified the person who handles the booking.|
S~A little guidance saves a surprising amount of hovering uncertainly.|
N~Clear responsibility is helpful even when the whole operation fits in one room.|
S~The next conversation is close enough to point to.|
S~A useful answer that does not make an ordinary question feel foolish.|
S~I wonder whether she gets to watch the matches once the players have signed up.
''')
add('jump_info','Text_PokemonJumpInfo_Frlg',
    "The attendant explains jumping a Vine Whip rope with eligible small Pokemon.",'''
S~A rope-skipping game with a rope that has rather more opinions than usual.|
S~The activity requires timing repeated jumps to a moving obstacle.|
N~Learn the rhythm before trying to go faster.|
S~It sounds like the sort of game where everyone laughs after nearly missing a turn.|
S~A simple game can keep a whole group happily occupied for a long time.|
S~The vine has secured a starring role in a remarkably energetic ensemble piece.|
S~A little repeated leap can become a very absorbing business.|
S~A consistent cue should help more than reacting late to every pass.|
S~Small feet are being invited to borrow the air for a moment.|
S~I like a game whose main attraction is doing a simple thing together.|
S~I wonder how different it looks when the whole group gets the timing right.
''')
add('grunt_leaves','CeruleanCity_Text_BetterGetMovingBye',
    "The Rocket departs after returning the stolen TM.",'''
N~A very quick goodbye from somebody with excellent reasons not to linger.|
N~The departure follows the restitution branch, not a new claim of innocence.|
N~He can go. Returning one stolen thing does not excuse the rest.|
N~I am glad the conversation ends without making the residents endure more of him.|
N~Now the people who live here can have the space back.|
N~The criminal has wisely selected an abbreviated exit speech.|
N~An unusually welcome lack of lingering sentiment at a farewell.|
N~We can focus on what still needs putting right after he leaves.|
N~A bad presence has finally chosen to become an absence.|
N~His best contribution to the atmosphere is the decision to depart.|
N~I wonder how different this little yard will feel without him standing in it.
''')
add('tower_encouragement','TrainerTower_Lobby_Text_GiveItYourBest',
    "The Tower receptionist encourages the player to do their best.",'''
S~A good send-off does not need to promise that every battle will go our way.|
S~An effort-focused encouragement avoids making the result the only meaningful part.|
N~Prepare well, then give it a fair try.|
S~I like a little encouragement that does not make losing sound shameful.|
N~Our best will go farther after a proper rest and a supply check.|
S~A modest opening benediction before the demanding part begins.|
S~A small kind word is useful luggage for an uncertain challenge.|
N~We can focus on decisions within our control rather than guarantee the outcome.|
S~A doorway has offered warmth without pretending to know what lies past it.|
S~It is a pleasant way to welcome someone who may already be nervous.|
S~I wonder how many challengers remember that greeting once the first battle starts.
''')
add('tower_thanks','TrainerTower_Lobby_Text_ThanksForCompeting',
    "The Tower receptionist thanks the returning player for competing.",'''
S~A little recognition for taking part, after all the noise and stairs.|
S~The acknowledgement values participation without adding a claim about the particular result.|
S~A decent closing word after a challenge.|
S~It is nice to be welcomed back as a person instead of only a score.|
S~Now would be a good time to let the team settle and catch our own breath.|
S~The venue has remembered to thank the cast after the performance is over.|
S~An ordinary thank-you can make the end feel less abrupt.|
S~A clear closing interaction helps the whole visit feel complete.|
S~The building has given the day back to us with a kind little nod.|
S~Good hospitality includes the moment people leave, too.|
S~I wonder which part of the challenge each traveller talks about first after walking out.
''')
add('tower_time','TrainerTower_Roof_Text_IdLikeToSeeBetterTime',
    "The Tower owner asks the player to return with a better completion time.",'''
N~The view is lovely, but he has kept one eye firmly on the clock.|
N~He is setting a future time-improvement goal, not describing the entire value of this attempt.|
N~We can decide whether we want another timed run.|
N~I would like a moment to enjoy getting here before thinking about getting here faster.|
N~A quicker attempt still needs a rested team and a sensible plan.|
N~The critic has admired the setting and requested a brisker second performance.|
N~The summit has turned out to contain somebody recommending a faster climb.|
N~We could review the delays before assuming more speed requires less care.|
N~A clock can measure a journey without containing all of it.|
N~His preference is clear. Our enjoyment does not have to use the same measure.|
N~I wonder which parts of a run are actually worth hurrying through and which are worth keeping.
''')
add('rocket_recruit','Route24_Text_YoudBecomeTopRocketLeader',
    "The defeated bridge Rocket continues trying to recruit the player by flattering their ability.",'''
N~He has lost the battle and doubled the flattery. The job description is still terrible.|
N~Recognizing ability does not make the proposed organization or its conduct acceptable.|
A~No. Being capable does not oblige us to help people hurt others.|
N~I dislike praise being used as a handle to pull someone toward something ugly.|
N~An opportunity is not automatically good just because somebody calls us suited to it.|
N~The recruiter has revised the title while leaving the moral problem untouched.|
N~A flattering mirror can still be hung over a very bad doorway.|
N~The relevant issue is what the role asks us to do, not how impressive its title sounds.|
N~A crown offered by cruel hands is not made kinder by fitting well.|
A~He has confused being impressed with us for having a right to recruit us.|
N~I wonder how many people hear the compliment first and only notice the cost afterward.
''')
add('rocket_nugget_room','Route24_Text_YouDontHaveAnyRoom',
    "The bridge challenge's prize giver cannot hand over the Nugget because the Bag is full.",'''
N~We have reached the prize and discovered the Bag has its own final challenge.|
N~The item handover is blocked by capacity; receiving the prize has not completed.|
N~Make room before trying to collect it.|
N~A frustrating little delay after making it through the challenge.|
N~A short sorting stop is easier than arguing with an overfull Bag.|
N~The awards ceremony has been postponed by the winner's luggage arrangements.|
N~An allegedly small prize can become large when there is nowhere left to put it.|
N~We can resolve the capacity issue before resuming the conversation.|
N~The reward waits outside a very crowded little door.|
N~The practical obstacle is clear, even if the rest of this fellow feels less straightforward.|
N~I wonder which thing we packed convinced us there would still be room for prizes.
''')
add('bill_bag','Route25_SeaCottage_Text_YouveGotTooMuchStuff',
    "Bill cannot give the player his offered item because the Bag is full.",'''
N~Bill has offered something and our luggage has answered on our behalf.|
N~The offered item cannot be transferred until the capacity issue is resolved.|
N~We need space before he can hand it over.|
N~I hope we can make the practical delay feel less awkward than it sounds.|
N~A little clearing out will let the kind gesture actually happen.|
N~The grateful host has been defeated by the visiting expedition's packing habits.|
N~An overfull bag is an oddly effective way to interrupt generosity.|
N~We can sort what we are carrying before returning to the offer.|
N~A small kindness is waiting for a place to land.|
N~No need to make him keep holding it while we pretend there is room.|
N~I wonder whether he is quietly glad of another minute to return to his research.
''')
add('minigame_goodbye','CableClub_Text_ComeAgain_Frlg',
    "The minigame or Cable Club attendant politely closes a cancelled or ended visit.",'''
N~A straightforward goodbye. The visit can end without pretending a game happened.|
N~The closing line alone does not establish whether any activity was completed.|
N~We can leave it there and choose another plan.|
S~It is nice to have a simple ending after a conversation full of arrangements.|
S~Another visit remains possible if it suits the day.|
N~The reception desk has closed the scene without adding a review of our performance.|
S~An ordinary farewell is enough to release a complicated little conversation.|
N~We can decide what to try next without assuming this visit produced a result.|
N~The door stays where it is while the afternoon continues elsewhere.|
S~A polite goodbye costs little and makes leaving less awkward.|
S~I wonder how different the room feels when a whole group arrives ready to play.
''')
