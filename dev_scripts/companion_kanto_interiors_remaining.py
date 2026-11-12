"""Remaining Kanto service and trainer-fan-club terminal conversations."""
ROWS=[]
EMOTIONS=dict(N='neutral',S='soft_smile',A='annoyed',F='flustered',D='sad',U='surprised',M='smug',L='laughing')
def add(key,labels,subject,lines):
    replies=[]
    for line in lines.strip().split('|'):
        line=line.strip()
        if len(line)>1 and line[1]=='~' and line[0] in EMOTIONS:line=EMOTIONS[line[0]]+line[1:]
        replies.append(line)
    assert len(replies)==11,(key,len(replies))
    ROWS.append(dict(key='kanto_im_'+key,labels=labels.split(),subject=subject,replies=replies))

def fan(key,label,subject,lines):
    add(key,'SaffronCity_PokemonTrainerFanClub_Text_'+label,subject,lines)

fan('first_fans','YourePlayerWereYourFansNow',
    'Club members recognize us and announce they are becoming our fans.','''
U~We have a fan club! Do we need to learn how to wave professionally?|
U~They have connected our battles with a public reputation. That is a substantial change.|
N~Nice of them. The team still comes before putting on a show.|
F~That is a lot of attention to walk into all at once.|
S~It is lovely that our work has made somebody happy.|
U~An audience has formed without our ever booking a venue.|
F~I had not prepared a face for being celebrated indoors.|
U~Unexpected public recognition! There should be a briefing for this.|
S~Our footsteps have apparently been arriving in stories before us.|
S~A warm welcome. I hope they remember we can have ordinary days too.|
S~I wonder which battle first got them talking about us.
''')
fan('cheering','AlwaysCheerForYou',
    'An enthusiastic fan promises continued support.','''
S~A little cheering to carry along the next long stretch.|
S~Encouragement can be welcome without changing the work ahead.|
S~Good of her. We will keep looking after the team.|
F~She sounds so certain. It is a little overwhelming and very kind.|
S~A kind voice can make a difficult day feel less solitary.|
S~The cheering section has renewed its season ticket.|
S~A stranger has decided to be warmly invested. Rather nice.|
S~Positive feedback received. No technical adjustment required.|
S~A small voice leaves a bright little echo.|
S~She gives the encouragement generously. That suits her.|
S~I wonder whether she cheers this loudly from the sidelines too.
''')
fan('loyal_belief','IllAlwaysBelieveInYou',
    'Our remaining fan believes in us and wants others to see our serious battling.','''
S~She kept her little flag raised when the crowd wandered off.|
S~Her support has persisted independently of the group's current preference.|
S~One sincere supporter is worth hearing. We still set our own pace.|
S~It means something when encouragement stays after the room gets quiet.|
S~We can appreciate her faith without making every day a performance.|
S~The audience has shrunk; the commitment has not.|
S~A single steady voice can be easier to hear than a crowd.|
N~Support retained through changing conditions. That seems genuine.|
S~One light remaining is still a light.|
S~She wants people to see what she sees. A sweet impulse.|
S~I wonder what part of our battling made that impression on her.
''')
fan('former_fan','WasYourFanNotAnymore',
    'A former fan says we lost our drive and now prefers another trainer.','''
N~The cheering has changed addresses. We can still have a perfectly good afternoon.|
N~Her interpretation of our motivation is not a direct measurement of it.|
N~Her choice. We do not owe her a busier schedule.|
N~That stings, though she is allowed a different favorite.|
N~The team's well-being still matters more than keeping strangers impressed.|
N~The critic has moved to another production and issued a rather personal review.|
N~A quiet season need not explain itself to every former admirer.|
N~Preference changed. Our goals do not need an automatic update.|
N~An echo fading does not mean the road has disappeared.|
N~She can move on without deciding what is happening inside us.|
N~I wonder how much of our journey she actually sees.
''')
fan('loyal_other','EveryonesYourFanButICantBe',
    'A club member respects our strength but remains loyal to another favorite.','''
S~Fair enough! A fan club is not compulsory uniform day.|
S~She distinguishes recognizing ability from choosing a personal favorite.|
S~Her choice. Respect does not require switching sides.|
S~I appreciate how kindly she explained it.|
S~There is room to admire more than one person without changing loyalties.|
S~A graceful refusal to follow the room's newest enthusiasm.|
S~A favorite can remain a favorite without everyone else's permission.|
N~Independent preference maintained. Completely reasonable.|
S~Not every flower needs to turn toward the same light.|
S~She can appreciate us without making a performance of joining in.|
S~I wonder what first made her a fan of that trainer.
''')
fan('battle_cool','TrainersCoolWhenBattling',
    'A member admires the way trainers look during battles.','''
S~The focused look does have something to it. Mine is mostly trying to count.|
N~Skilled coordination can be visually impressive as well as effective.|
N~Best when they are paying attention to the team, not the audience.|
S~There is something striking about seeing somebody fully absorbed in what they know.|
S~I like the quieter moments when a trainer notices what a partner needs.|
S~Concentration supplies its own rather convincing costume.|
N~A composed exterior can conceal an impressive amount of internal panic.|
S~Competence looks good when the decisions actually work.|
S~A person and a creature briefly moving toward the same thought.|
S~Confidence works best when it is supported by real care.|
S~I wonder which small gesture she notices most during a battle.
''')
fan('shorts_autograph','CanYouAutographShorts',
    'The youngster asks us to autograph his shorts.','''
U~The shorts have been offered as official memorabilia. I hope the ink survives laundry.|
M~An unusual writing surface with predictable durability concerns.|
N~Only if everyone is comfortable. A piece of paper works too.|
F~I would be very nervous trying to sign clothing neatly.|
M~That is a souvenir with a complicated washing schedule.|
M~Fame has reached the critical stage of being asked to endorse trousers.|
M~A signature whose public life depends on the laundry.|
N~Fabric needs the right ink. Otherwise this is a very temporary autograph.|
N~A little name asked to live on a very active pair of legs.|
M~He has chosen a canvas that is clearly important to his personal style.|
S~I wonder whether he plans to wear them or display them afterward.
''')
fan('shorts_faith','CountingOnYou',
    'The youngster compares faith in our victories to his lifelong faith in shorts.','''
M~We have joined shorts in his most trusted category. Tremendous company.|
M~The analogy is peculiar, but the commitment appears consistent.|
N~Glad he is cheering. We still get to have a difficult day.|
F~That is a lot of faith, explained in a very unexpected way.|
S~He has found two things that make him happy. Good for him.|
M~Our reputation now stands beside a garment with an unbroken seasonal record.|
M~A wonderfully specific hierarchy of personal loyalties.|
N~Established reference point, unusually ambitious comparison.|
S~He knows what he believes in, right down to the knees.|
M~His brand is consistent. His expectations of our win record are ambitious.|
S~I wonder whether he has any other great convictions beyond these two.
''')
fan('brock_embroidery','BrocksMyHero',
    'The youngster proudly shows that his mother embroidered Brock\'s name on his shorts.','''
S~His mom has contributed official lettering to the fan club uniform.|
S~A family member turned his enthusiasm into a personal keepsake.|
S~Nice of his mother to make something that matters to him.|
S~A small handmade thing can mean much more than merchandise.|
S~That sounds like an affectionate way for her to join his interest.|
M~The hero's name has been immortalized in a highly mobile textile edition.|
S~A little stitchwork preserving a large enthusiasm.|
S~Custom fabrication for a very satisfied user. Excellent.|
S~Someone's patient hands made room for his favorite name.|
S~A homemade detail makes the outfit his own.|
S~I wonder whether she chose the lettering or let him design it.
''')
fan('brock_loyal','BrocksFanToBitterEnd',
    'The youngster swears loyalty to Brock even as the last remaining fan.','''
S~The shorts have been called as witnesses to a very solemn oath.|
S~His preference remains stable despite social pressure to change it.|
S~He can like Brock without needing a crowd behind him.|
S~It is nice that other people changing their minds does not make him feel wrong.|
S~A genuine favorite does not need to win a room vote.|
M~A vow of rock-hard loyalty, countersigned by the shorts.|
S~A small stubborn affection standing pleasantly on its own.|
N~Preference held independently of popularity. Reasonable.|
S~One little flag stays where it was planted.|
S~He has made the loyalty theatrical, but it seems sincere.|
S~I wonder what Brock did that he remembers so strongly.
''')
fan('brock_example','BrocksLastWordOnCool',
    'The youngster sees Brock as the person he wants to become like.','''
S~A hero can be a good starting point. He still gets to become himself.|
N~A role model is most useful when admired qualities are identified specifically.|
N~Learn what is worth learning. No need to copy the whole person.|
S~It is sweet to hear a future imagined with that much certainty.|
S~I hope he admires the care behind the strong-looking part too.|
S~An impressive figure has become a rough draft for somebody's future.|
S~A borrowed example can help you find your own shape.|
N~Useful to ask which traits he wants to practice first.|
S~A small person has found a taller outline to grow toward.|
S~Admiration suits him. A little room for his own taste would suit him too.|
S~I wonder what he would ask Brock if they met.
''')
fan('gentleman_memories','HadPleasureOfWatchingYouBattle',
    'An older fan says our battling recalls his youth and wishes us success.','''
S~We gave him a little of an old afternoon back. That is a lovely compliment.|
S~A present experience has connected with a meaningful earlier memory.|
S~Good to know he enjoyed watching. Sounds like he has stories of his own.|
S~There is a gentle warmth in how he remembers being young.|
S~A shared interest can bridge quite a few years without much effort.|
S~The spectator recognizes a familiar fire in a new generation's scene.|
S~An old memory stirred kindly instead of aching. I am glad.|
S~Experience across generations can make the feedback interesting.|
S~A long-quiet part of someone's life answered a little when we battled.|
S~He gives the praise without trying to make it a claim on us. Lovely.|
S~I would be curious to hear what his own early journeys were like.
''')
fan('gentleman_idol','NeverSeenTrainerOfYourMagnificence',
    'Our remaining older fan praises us extravagantly and asks us to promise to continue.','''
F~Magnificence is a large word to carry when I still misplace my own socks.|
N~His praise is generous, but a promise about future battling remains our choice.|
N~Kind of him. We do not need to promise a stranger our whole road.|
F~It is lovely and a little too much all at once.|
S~We can thank him warmly without turning every future day into an obligation.|
M~A magnificent review, followed by a proposed long-term engagement.|
F~I would prefer to remain slightly less magnificent and considerably less observed.|
N~Positive assessment noted. Avoid committing beyond the team's needs.|
S~A bright opinion can be held gently without becoming a heavy crown.|
N~The praise should feel like a gift, not a contract.|
S~I wonder which moment made such a strong impression on him.
''')
fan('gentleman_unknown','HmmAndYouAre',
    'The older member does not recognize us and asks whether we want to join the fan club.','''
S~For one peaceful moment, we are simply a potential new club member.|
N~He does not recognize us. No special status needs to be inferred.|
N~No problem. We can be visitors without a reputation.|
S~An ordinary introduction feels rather comfortable.|
S~A club should be able to welcome someone without knowing their accomplishments.|
S~The public figure has been recast as an interested member of the public.|
S~Being unknown can be a pleasant little rest.|
N~Identity not established. A simple introduction would resolve it.|
S~A name can arrive quietly before the stories attached to it.|
S~No need to announce ourselves like an important delivery.|
S~I wonder how he welcomes people who are new to the whole hobby.
''')
fan('gentleman_standards','YouveStillAWaysToGo',
    'The older member acknowledges our reputation but says we have not met his standard of greatness.','''
N~His personal greatness committee has deferred the application. We can keep walking.|
N~His standard is subjective and not clearly specified. It need not define our goals.|
N~Fine. The team is not training for his approval.|
N~That can be hard to hear when you did not ask to be evaluated.|
N~We can value the work already done and still keep learning.|
N~The critic has produced a high bar without providing its height.|
N~An impressive-looking gate, built entirely from someone's opinion.|
N~Undefined acceptance criteria. Not a useful target for planning.|
N~Another person's distant horizon need not become ours.|
N~He is allowed a standard. We are allowed our own reasons for traveling.|
N~I wonder whether he ever explains what he thinks is still missing.
''')
fan('club_popularity','YoullBeTalkedAboutIfYouKeepWinning',
    'The older member says repeated victories could make us a subject of fan-club discussion.','''
N~Win enough, become table talk. An unusual prize to put on a training plan.|
N~The club's attention appears contingent on visible performance. That is not the only measure.|
N~We have better reasons to train than being discussed in this room.|
N~I would rather be noticed by the partners who actually know the work.|
N~The team's needs make a steadier guide than a room's changing excitement.|
N~Repeated victories may purchase a speaking role in the club's weekly conversation.|
N~Being worth discussing and being worth something are rather different matters.|
N~External interest is feedback, not a required objective.|
N~The road continues even when nobody tells stories about it.|
N~A reputation can be pleasant. Chasing it sounds tiring.|
N~I wonder how much the club knows about trainers' ordinary days.
''')
fan('child_rolemodel','WantToBeLikeYouOneDay',
    'A child excitedly says she wants to become like us.','''
S~That is a big little compliment. We should try to deserve the kind part.|
S~Admiration makes our conduct, not just our results, potentially influential.|
S~Then show her how to look after a team as well as win.|
F~I would want to say something useful, and probably forget every word.|
S~She can learn from us and still find a journey that fits her.|
S~The audience has begun imagining its own turn on the road.|
S~A little future is looking at us with very wide eyes.|
N~Role-model responsibility detected. Better demonstrate good habits.|
S~A small bright wish has found a person to stand beside it.|
S~A sincere compliment. I hope she keeps room to become herself too.|
S~I wonder what part of our journey she most wants to try.
''')
fan('child_onlyfan','EveryoneButMeStoppedBeingYourFan',
    'The child celebrates being our only remaining fan as if she can have us to herself.','''
N~A smaller fan club does not come with exclusive ownership of the trainer.|
N~Her enthusiasm is affectionate, but exclusivity should not be confused with possession.|
N~We can be kind without agreeing that we belong to her.|
F~That is sweet and a little too close to a promise nobody made.|
N~She can enjoy cheering without needing everyone else to disappear.|
M~The diminished audience has mistaken vacancy for a private booking.|
N~A person is not a collectible made rarer by fewer admirers.|
N~One interested observer does not become the system administrator.|
S~A small heart sometimes holds an idea more tightly than it knows.|
N~A gentle boundary would help more than laughing at her.|
N~I wonder whether she simply means she is glad to get a chance to talk.
''')
fan('child_sabrina','WantToBeLikeSabrina',
    'The child admires Sabrina and wants to be a psychic girl.','''
S~A future with psychic powers is certainly an ambitious first draft.|
N~An admired figure can encourage curiosity even when their abilities are not easily reproduced.|
N~Good to have a hero. There is plenty she can learn without copying every power.|
S~She imagines herself so clearly. It is rather lovely.|
S~I hope she finds someone patient to answer her questions.|
S~The young admirer has selected a striking and mysterious model for the future.|
S~A small person has found room in the world for being unusual.|
N~A clear interest. Reliable information is the next useful step.|
S~An odd gift can look like a door when someone you admire wears it well.|
S~Cute and capable is a perfectly reasonable thing to admire.|
S~I wonder which story about Sabrina first caught her imagination.
''')
fan('child_sabrina_loyal','WontStopBeingSabrinasFan',
    'The child remains Sabrina\'s fan even when everyone else favors us.','''
S~She has kept her favorite without asking the room to vote again.|
S~Her admiration is not dependent on matching the group's current preference.|
S~Her choice. No reason she needs to cheer for us.|
S~It is nice that she still sounds happy being the only one.|
S~A real favorite can be good company even in a room full of other opinions.|
S~The small defender of a personal favorite holds her corner admirably.|
S~She has made a comfortable little place outside the crowd.|
N~Preference stable under social pressure. Perfectly fine.|
S~One little star need not become the whole room's favorite to remain bright.|
S~She is keeping her own taste. A useful skill to have early.|
S~I wonder whether she knows other Sabrina fans outside this club.
''')
fan('child_trainer_dream','CanIBecomeCoolTrainerOneDay',
    'The child wonders if she can become an impressive trainer someday.','''
S~A small start is still a start. Every impressive trainer had one.|
S~Learning, support, and patient practice can develop abilities over time.|
S~She can begin by learning how to care for a partner. Good first step.|
S~I would rather encourage the question than make a grand promise about the answer.|
S~A kind, steady trainer is already something worth aiming for.|
S~An audience member has begun considering an entrance of her own.|
S~The future is not a room she needs permission to imagine.|
S~Start with manageable skills, then add the next challenge.|
S~A path can begin with a little question asked quietly.|
S~She does not have to look impressive before she starts learning.|
S~I wonder what kind of partner she imagines beginning with.
''')
fan('rocker_battle_only','TheWayYouBattleIsCool',
    'The rocker clarifies that he admires our battling rather than us personally.','''
M~A compliment carefully fitted with an emergency exit.|
N~He is distinguishing admiration for performance from personal attachment.|
N~Fine by me. The team did good work.|
F~That was a rather awkward correction to an already surprising compliment.|
N~He can appreciate the skill without needing to know everything about us.|
M~A favorable review followed by an emphatic disclaimer from the critic.|
M~He has made admiration sound suspiciously like denying an accusation.|
N~Specific feedback is useful. The defensive packaging is optional.|
N~A person and the thing they do cast slightly different shadows.|
M~He is allowed a precise compliment. A little more grace would finish it nicely.|
N~I wonder what particular decision impressed him.
''')
fan('rocker_onlyfan','ImOnlyOneLeftOfYourFans',
    'The rocker enjoys being our only fan because it feels less stressful.','''
S~A one-person fan club has very manageable meeting arrangements.|
S~He appears more comfortable without the social pressure of the wider group.|
S~Fair enough. He can enjoy the battles without joining a crowd.|
S~I understand finding the quiet version of something easier.|
S~It is nice that he still sounds relaxed rather than disappointed.|
M~The exclusive audience appreciates the improved legroom.|
S~Fewer voices can leave more room to hear what you actually like.|
N~Reduced crowding improves the experience for this user. Noted.|
S~A little quiet corner of admiration, with no elbows to compete against.|
S~He has found a way to enjoy the situation on his own terms.|
S~I wonder what part of the crowded club felt stressful to him.
''')
fan('rocker_voice','LoveWayTrainerTalks',
    'The rocker admires another trainer\'s way of speaking and wants to meet him.','''
S~Some people make an ordinary sentence sound like an event.|
S~Vocal style can strongly influence a public impression independently of battle skill.|
N~Could be an interesting meeting. A good line is not the whole person.|
S~A voice can stay with you in a very particular way.|
S~I hope the real conversation is as pleasant as he imagines.|
S~An admirer drawn by the dialogue as much as the action. A discerning interest.|
S~A turn of phrase can become a strange little thing to carry around.|
N~Distinctive presentation can make information remarkably memorable.|
S~A voice can leave a shape after the words themselves are gone.|
S~Delivery is part of style. I understand noticing it.|
S~I wonder what phrase he keeps remembering.
''')
fan('rocker_other_only','ImLoneTrainerFan',
    'The rocker stays loyal to another trainer and enjoys being that trainer\'s only fan.','''
S~He has turned an empty fan table into his preferred seat.|
S~He is comfortable retaining a preference that no longer matches the group.|
S~Good. No need to change favorites to fit the room.|
S~It is nice that being outnumbered does not make him feel unwelcome.|
S~He can enjoy the battles without needing a crowd to agree.|
M~The lone critic has declared solitude an essential part of his aesthetic.|
S~An eccentric little pleasure, and apparently quite sufficient.|
N~Independent preference, positive experience. No fault to fix.|
S~A single candle can make a corner feel like someone's own.|
S~Keeping your taste is easier when you can laugh about the empty seats.|
S~I wonder whether he would be delighted or annoyed to meet another fan.
''')
fan('woman_admiration','AdoreWayYouBattle',
    'An enthusiastic woman praises our battling and calls herself our number-one fan.','''
S~The number-one position filled itself before we knew it was vacant.|
S~She is expressing strong appreciation for a particular performance.|
S~Kind of her. The partners deserve their share of the praise.|
F~That much excitement makes me want to hide and smile at the same time.|
S~It is lovely when somebody's enjoyment is so unguarded.|
S~A glowing notice from a critic who has chosen a very prominent seat.|
F~I hope there is no required speech for receiving that much enthusiasm.|
S~Strong positive feedback. We can acknowledge it without promising a perfect record.|
S~A bright voice welcoming the road into this little room.|
S~Her delight is charming. No need to turn it into a contest over who cheers most.|
S~I wonder what moment of the battle she would describe first.
''')
fan('woman_onlyfan','ImYourNumberOneFan',
    'The woman realizes she is our only fan but cheers anyway.','''
S~Number one out of one still comes with a very determined cheer.|
S~She acknowledges the changed crowd while continuing her own support.|
S~Good of her. We can appreciate one voice without chasing the rest.|
S~There is something touching about cheering after noticing nobody else joined in.|
S~A small sincere welcome can mean more than a noisy room.|
S~The diminished audience has elected to give an undiminished performance.|
S~A little embarrassment, bravely made into kindness.|
N~Support continues despite reduced participation. Seems genuine.|
S~A voice can be warm without having another voice beside it.|
S~She lets herself be disappointed and kind in the same breath.|
S~I wonder whether she knows the cheer matters without the crowd.
''')
fan('woman_current_favorite','TrainerHasBeenOnFire',
    'The woman enthusiastically praises another trainer\'s recent battle form.','''
S~Someone has been giving her very exciting matches to talk about.|
S~Her enthusiasm is directed at a recent performance trend, not necessarily a permanent ranking.|
N~Good for that trainer. We do not need to compete for every compliment.|
S~It is nice to hear someone enjoy watching so much.|
S~A good match can give people something pleasant to share for days.|
S~The current favorite receives a vivid, if thankfully figurative, description.|
S~A spark of someone else's good day has traveled into this room.|
N~She likes the current style. Preferences can be that specific.|
S~An unseen battle is still giving off a little heat in the telling.|
S~She knows the kind of performance she enjoys. Fair enough.|
S~I wonder what changed recently that caught her eye.
''')
fan('woman_lonely_other','EveryoneTalksAboutYou',
    'The woman feels isolated because everyone discusses us while she prefers another trainer.','''
N~A room can get very narrow when it discovers one subject and refuses to put it down.|
N~Her isolation concerns the group's conversation, not merely her private preference.|
N~She should be able to talk about her favorite too.|
N~I know what it is like when there is no small opening for your own thought.|
N~A club is nicer when more than one interest gets a turn.|
N~The audience has become unanimous enough to forget it contains separate people.|
N~A room full of voices can still leave someone feeling quite alone.|
N~The conversation needs broader input, not a change to her preference.|
N~There should be room at the table for a different little light.|
N~Being enthusiastic does not mean everybody has to wear the same opinion.|
N~I would rather ask what she likes about her favorite than make her defend it.
''')
fan('beauty_try_training','YouReallyAreAmazing',
    'Watching us inspires the woman to consider becoming a trainer herself.','''
S~The fan club may have accidentally launched a new expedition. Excellent side effect.|
S~Observation has prompted interest in direct participation. A useful transition.|
S~Start with care and the basics. There is room for a new trainer.|
S~It is lovely when admiration turns into wanting to try something yourself.|
S~She can begin small and find out which parts she enjoys.|
S~A spectator has begun considering her own entrance, which is always an interesting moment.|
S~A borrowed spark can become someone's own small fire.|
S~Try a manageable first task. Much easier than planning an entire new identity.|
S~The road has reached into the audience and found another pair of feet.|
S~A genuine interest can look good before it looks impressive.|
S~I wonder what kind of first partner she imagines.
''')
fan('beauty_onlyfan_pressure','ImYourOnlyFan',
    'Our only remaining fan asks us to try harder so she has company in cheering.','''
N~We cannot fix her empty table by making the team perform on demand.|
N~Her loneliness is real, but changing our schedule is not an automatic obligation.|
N~The team does not owe anyone a perfect record to keep them company.|
N~I feel for her, though that is a heavy request to put on a stranger.|
N~A club could help her feel included without asking us to win more.|
N~The lonely audience has submitted a rather demanding revision request.|
N~An empty seat is not something another person has to win a battle to fill.|
N~Wrong proposed fix. Broader club interaction would address the actual problem.|
N~A lonely room should not become a weight on someone else's journey.|
N~She deserves company. We deserve room to travel at our own pace.|
N~I wonder whether anyone here asks her about interests beyond the scoreboard.
''')
fan('beauty_dignity','WhyCantOthersSeeMastersDignity',
    'The woman admires another trainer\'s dignity and wonders why the club does not agree.','''
S~Dignity is a quieter sort of favorite than another impressive win.|
N~She is responding to manner and presence, qualities others may value differently.|
N~She can admire that without convincing the whole room.|
S~It is nice to notice how someone carries themselves, not just what they win.|
N~Different people find different qualities reassuring. Nothing wrong with that.|
S~A devoted critic appeals to the room's tragically unrefined appreciation of bearing.|
S~A quiet presence can matter more to one person than a loud record.|
N~Different evaluation criteria explain much of the disagreement.|
S~Some people notice the stillness around a person first.|
S~Poise is a real part of an impression. It just does not charm everyone equally.|
S~I wonder what moment first made her think of him as dignified.
''')
fan('beauty_loyal_master','BelieveInMasterWithAllMyHeart',
    'The woman remains contentedly loyal to another trainer even as that trainer\'s only fan.','''
S~Her favorite is still her favorite without an echo from the room.|
S~She finds the preference rewarding without requiring social agreement.|
S~That is her choice. No reason to take it away from her.|
S~It is nice that she sounds settled rather than defensive.|
S~A harmless enthusiasm can be good company on an ordinary day.|
S~The loyal admirer declines to let a dwindling audience rewrite her opinion.|
S~A private affection need not become a public petition.|
N~Positive experience despite low popularity. No adjustment needed.|
S~One little flame, quite content with its own corner.|
S~She knows what she likes without borrowing everyone else's taste.|
S~I wonder whether she has ever had the chance to tell him.
''')
fan('dojo_learning','YourBattleStyleIsEducational',
    'A martial artist says our battle style is educational and urges us onward.','''
S~A fan who brought a notebook in spirit. We should try to set a decent example.|
S~He is attending to technique rather than only celebrating the result.|
S~Good. Learning from a battle is worth more than just applauding it.|
S~It is a thoughtful compliment, even delivered quite that loudly.|
S~I hope he finds something useful for his own partners.|
S~A critic who leaves the performance with practical notes. Excellent audience.|
S~Admiration can become something useful in another person's hands.|
S~Observed technique converted into possible improvements. Productive feedback loop.|
S~A path can leave a little guidance for the next pair of feet.|
N~He is interested in what works. That makes the praise feel considered.|
S~I wonder which decision he would like to try himself.
''')
fan('dojo_spectator','WontStopBeingYourFan',
    'The martial artist resists his master\'s demand to stop watching and do more battling.','''
N~A person can practice and still enjoy cheering. There are enough hours for both, usually.|
N~Observation and participation can complement one another rather than compete absolutely.|
N~He should do the training he agreed to. He can still like watching us.|
N~I understand wanting one interest that is simply yours to enjoy.|
N~A balance would help more than making him choose a side.|
N~The devoted spectator has encountered a director demanding he leave the audience.|
N~Enjoyment does not always need to prove it is productive.|
N~Observation needs practical follow-through, but practical work can allow spectatorship.|
N~A voice cheering beside the road need not stop having its own footsteps.|
N~His enthusiasm sounds real. I hope the master leaves room for it.|
N~I wonder how much training time the watching actually takes away.
''')
fan('dojo_only_master','OnlyMasterHasMyRespect',
    'The martial artist says only his dojo master deserves his respect and urges us to become fans.','''
N~That is a very narrow guest list for respect. The invitation is enthusiastic, though.|
N~Respect need not be an exclusive resource restricted to one person.|
N~He can admire his master without dismissing everyone else.|
N~I would rather not have to pass a loyalty test just to talk here.|
N~There are many people worth learning from without replacing his favorite.|
N~The disciple has opened a recruitment desk for a remarkably exclusive philosophy.|
N~A single candle does not need every other candle put out.|
N~One trusted source is not a complete reference library.|
N~A path can have more than one person worth listening to.|
N~Admiration looks better when it leaves room for ordinary courtesy.|
N~I wonder what he most wants us to understand about his master.
''')
fan('dojo_secret_fan','NeverBeFanOfAnyoneButMaster',
    'The martial artist says he sneaks out of the dojo to promote his master.','''
M~An unauthorized field trip in the name of extremely authorized admiration.|
N~The secrecy suggests his method may not match the master's expectations.|
N~If the master asked him to train, sneaking out is not much of a tribute.|
N~He seems sincere, even if he has found an odd way to show it.|
N~He might help his master more by asking what support is actually wanted.|
M~A devoted publicist conducts a covert campaign for a man who may prefer him in class.|
M~Loyalty has acquired an impressively disobedient practical method.|
N~The stated goal and chosen behavior appear poorly aligned.|
N~A shadow slipping away to praise the person it is hiding from.|
N~A public tribute can still ignore the person supposedly receiving it.|
N~I wonder whether the master knows where his most enthusiastic student goes.
''')
add('news_none','CeruleanCity_House4_Text_NothingEntertaining',
    'The news enthusiast complains of boredom when he has no new Wonder News.','''
N~A quiet day has failed his entertainment requirements. Perhaps he could go for a walk.|
N~A lack of received news does not imply that nothing interesting is happening nearby.|
N~Could make a plan instead of waiting for one to arrive.|
N~Too much empty time can feel surprisingly heavy.|
N~A small ordinary outing might help more than waiting for a spectacular story.|
M~The resident critic has found today's entire world insufficiently eventful.|
N~A comfortable room can become rather small when every minute echoes.|
N~No new input. Maybe change the source rather than refreshing the same expectation.|
N~The window remains full of a day that has not introduced itself yet.|
N~He might find more to enjoy by looking beyond whatever arrives as news.|
N~I wonder what kind of story he usually finds interesting.
''')
add('news_share','CeruleanCity_House4_Text_WishCouldShareNewsWithOthers',
    'The enthusiast wishes his current news could be shared with more people.','''
S~A good story has started bumping against the walls of his living room.|
S~He sees information as something that gains value through appropriate sharing.|
N~Good to share it if it is accurate and people want to hear.|
S~It is nice that enjoying it makes him think of someone else enjoying it too.|
S~A little interesting news can brighten an ordinary conversation.|
S~The delighted audience member has volunteered to become a distributor.|
S~A small bright thing asking for another pair of eyes.|
N~Check the source before extending the network. Then share responsibly.|
S~A story can be a little lamp passed from one room to another.|
S~He wants the pleasure to travel farther than his own chair. Sweet.|
S~I wonder whom he most wants to tell first.
''')
add('news_satisfied','CeruleanCity_House4_Text_EnjoyingMyselfWithAllSortsOfNews',
    'After enough news-related rewards, the enthusiast says he is happily occupied.','''
S~His boredom has been thoroughly outnumbered by things to read.|
S~He has enough information to remain occupied for now. A clear stopping point.|
S~Good. We can leave him to enjoy it.|
S~It is nice to see the same room feel more lively to him.|
S~A pleasant afternoon does not always need anything more than a good read.|
S~The formerly restless critic has found a program sufficient to his tastes.|
S~A chair can be a lovely place when the mind has somewhere to go.|
N~Input queue full, user satisfied. No additional material required.|
S~The quiet room now has a few more windows than before.|
S~He sounds content without asking us for the next thing immediately.|
S~I wonder which story he will return to after reading everything once.
''')
add('news_reward_full','CeruleanCity_House4_Text_YourBerryPouchIsFull',
    'The news enthusiast cannot give his Berry reward because the Berry Pouch is full.','''
N~Our news delivery succeeded; the thank-you has nowhere to land.|
N~The intended Berry transfer failed. The speaker explicitly says the gift remains ungiven.|
N~No reward received. Make space if we want to accept it later.|
F~He sounds apologetic about a problem in our own bag.|
N~A little sorting would make the next thank-you simpler.|
N~The news has circulated more successfully than the accompanying fruit.|
N~A crowded pouch interrupting an uncomplicated kindness.|
N~Container capacity failure. Distinct from a successful reward.|
N~A full little place has delayed the offered sweetness.|
N~At least he states plainly that nothing has been handed over.|
N~I wonder whether we have been keeping more Berries than we use.
''')
add('powder_jar_task','CeruleanCity_House1_Text_GoCrushBerriesAtDirectCorner',
    'After giving the Powder Jar, the maker explains Berry crushing and requests powder for medicine.','''
N~He has repeated the directions enough that even my distracted elbow remembers them.|
S~The process links a supplied container, a preparation method, and a defined use for the material.|
N~Clear enough. Check what we need before making the trip.|
N~He sounds very eager to make sure the request is understood.|
N~Preparing an ingredient properly matters when it is going into medicine.|
M~The favor includes an unusually thorough rehearsal of the address.|
N~A simple request made large by repeated directions and considerable hope.|
S~Raw material, processing equipment, useful product. A proper workflow!|
N~A little crushed fruit is meant to become a different kind of help.|
N~He has made the instructions difficult to forget, at least.|
S~I wonder which medicine he most enjoys making from it.
''')
add('powder_no_berries','CeruleanCity_House1_Text_WhyMustYouLieNoBerries',
    'The maker accuses us of lying about interest in Berries because we have none.','''
N~An empty pouch is not proof of an empty interest. That was a sharp leap.|
N~Owning a resource and being interested in it are separate conditions. His inference is unsound.|
N~No need to call someone a liar over a missing Berry.|
F~That is an upsetting answer to a question we thought was about liking something.|
N~He could explain what we need without making an accusation.|
N~The interview has unexpectedly become a prosecution with very poor evidence.|
N~Apparently curiosity now requires a physical sample at the door.|
N~Incorrect validation rule. Interest does not depend on current inventory.|
N~A bare branch does not mean the tree dislikes fruit.|
N~A gentler correction would have made him much easier to talk to.|
N~I wonder whether he realizes how differently his question sounded to us.
''')
add('powder_interest_refused','CeruleanCity_House1_Text_TakeInterestInAllSortsOfThings',
    'The maker lectures us about curiosity after we decline an interest in Berries.','''
N~There are many interesting things. We cannot carry all of them in one afternoon.|
N~Broad curiosity is useful, but it does not require equal enthusiasm for every subject.|
N~We answered honestly. He can leave it there.|
N~Being told to enjoy something rarely makes it easier to begin.|
N~He might make a better invitation by showing why he enjoys it.|
N~A declined hobby has expanded into an unsolicited philosophy of education.|
N~A mind can be open without furnishing a room for every visitor.|
N~Time is limited. Choosing a focus is not a system fault.|
N~Not every seed needs to take root in the same garden.|
N~A little more welcome and a little less scolding might help his cause.|
N~I wonder what first made him interested before he began recruiting others.
''')
add('powder_trade_finished','CeruleanCity_House1_Text_HopeToSeeYouAgain',
    'After a successful powder exchange, the maker accepts our decision to stop trading.','''
S~Exchange finished. The little pharmacy can take a breather from our menu browsing.|
N~This goodbye follows a completed exchange and refusal of further trading.|
N~Done for now. Check the supplies before heading out.|
S~It is nice to finish without being pushed into another decision.|
S~A useful ingredient has become something useful to carry. Good trade.|
S~The transaction ends neatly rather than developing an unnecessary sequel.|
S~A quiet close to a practical little bargain.|
N~Exchange complete, menu closed, no extra operation requested.|
S~Something gathered has changed into another kind of help.|
S~A courteous finish matters after all the detailed choices.|
S~I wonder how much of his day he spends preparing the next batch.
''')
add('powder_menu_exit','CeruleanCity_House1_Text_SeeMeIfYoudLikeToTradePowder',
    'The maker closes the selection menu and invites future powder trading.','''
N~The menu has released us without requiring a purchase. A fine feature.|
N~Closing the menu alone does not establish that an exchange occurred.|
N~No need to choose something before we know what the team needs.|
S~It is good to have room to think outside a long list of options.|
N~We can come back with a clear plan instead of choosing just to finish.|
N~The catalogue closes, leaving the invitation intact.|
N~A page of possibilities can stay a page for today.|
N~Menu exit handled cleanly. Existing holdings should remain as they were.|
N~The little counter will be here when the right need arrives.|
N~A calm invitation beats trying to rush a decision.|
N~I wonder which option regular visitors choose most often.
''')
add('route2_fainted_field','Route2_House_Text_FaintedMonsCanUseFieldMoves',
    'A resident explains that fainted Pokemon can still perform field moves.','''
N~Still able to help does not mean a tired partner no longer needs a rest.|
N~The distinction concerns battle stamina versus some field capabilities.|
N~Useful to know. Get them healed when we can.|
N~I would feel bad asking too much from someone already worn out.|
N~A partner helping on the way to care still deserves that care promptly.|
N~The last reserve of usefulness should not become an excuse to postpone kindness.|
N~A creature is more than the number that says it cannot battle now.|
N~Different functions have different limits. Do not confuse capability with readiness.|
N~A tired companion may still open the way home. Go home afterward.|
N~A practical fact worth handling with a little judgment.|
N~I wonder how often that knowledge has helped a stranded trainer.
''')
add('forest_habitats','Route2_ViridianForest_NorthEntrance_Text_ManyMonsOnlyInForests',
    'A traveler encourages searching different habitats to find different Pokemon.','''
S~A forest is not a cave with extra leaves. New place, new neighbors.|
S~Habitat specialization makes varied exploration important for a complete record.|
N~Look carefully. Do not rush every place like it is the last one.|
S~There is something lovely about having a reason to notice the whole landscape.|
N~Good preparation includes knowing which kind of place we are entering.|
S~The wider cast refuses to assemble in a single convenient clearing.|
S~The world has hidden different little lives in different kinds of quiet.|
S~Broaden the sampling locations. Better data, more surprises.|
S~Each place keeps a few names that belong especially to it.|
N~Persistence is useful when it means patient attention instead of frantic searching.|
S~I wonder which habitat the traveler most enjoys exploring.
''')
add('roadside_cut_trees','Route2_ViridianForest_NorthEntrance_Text_CanCutSkinnyTrees',
    'A traveler says certain thin roadside trees can be cleared with a Pokemon move.','''
N~The tiny tree has become a puzzle with roots.|
N~The speaker suggests a specific field technique, though the claim is secondhand.|
N~Know what we are clearing before swinging at every tree.|
N~It is interesting how one small obstacle can shape an entire route.|
N~A useful skill when the path actually calls for it.|
N~A modest sapling has found a demanding role as the road's gatekeeper.|
N~Even a small tree can make people reconsider their direction.|
N~A capability gate disguised as vegetation. Memorable design.|
N~A narrow trunk can still stand between two parts of a journey.|
N~A specific obstacle is more useful to notice than a vague dead end.|
N~I wonder what is on the other side of the trees they noticed.
''')
add('cancel_evolution','Route2_ViridianForest_NorthEntrance_Text_CanCancelEvolution',
    'A traveler explains choosing to stop evolution and keep raising a Pokemon as it is.','''
S~A growing-up pause button. The Pokemon world keeps finding surprising options.|
N~Delaying evolution offers control over timing while training continues.|
N~A choice worth understanding before the moment arrives.|
S~It is reassuring that change does not always have to happen immediately.|
N~Take the partner and the plan into account before deciding.|
S~The transformation may be deferred without canceling the rest of the story.|
S~Something can remain familiar and still be learning.|
N~Reversible timing decision. Useful option when the sequence matters.|
S~A door can remain closed for a while without becoming a wall.|
N~A thoughtful choice is better than changing just because it is available.|
S~I wonder which partner made them want to wait.
''')
add('forest_maze','Route2_ViridianForest_SouthEntrance_Text_ForestIsMaze',
    'A traveler warns that Viridian Forest is a natural maze.','''
N~The trees did not include a corridor numbering system. We should pay attention.|
N~Similar-looking paths make landmarks and deliberate navigation useful.|
N~Remember the way back. Keep the team together.|
N~A little preparation makes a quiet forest much less intimidating.|
N~We should leave enough time to return without hurrying.|
N~The woodland setting comes with an unusually uncooperative floor plan.|
S~A maze made by things that had no intention of making a maze.|
N~Track turns and landmarks. Repeated scenery is how routes get confused.|
N~The trees can make several paths wear the same face.|
N~A plain warning is welcome before a confusing route.|
N~I wonder which landmark locals use when they want to find the exit.
''')
add('rattata_bite','Route2_ViridianForest_SouthEntrance_Text_RattataHasWickedBite',
    'A traveler warns that small Rattata can bite hard.','''
N~Small teeth remain teeth. My ankles accept the warning.|
N~Body size is not a reliable measure of the harm a bite can cause.|
N~Give it space. Do not assume small means harmless.|
N~A little creature still needs people to respect its boundaries.|
N~Better to learn that from a warning than from a bandage.|
N~The smallest resident declines a supporting role in anyone's complacency.|
N~A modest silhouette, a pointed rebuttal to being underestimated.|
N~Compact design can still deliver significant force. Noted.|
N~A small shadow can hold a sharp edge.|
N~A useful reminder for someone tempted to pick up every cute thing.|
N~I wonder how many travelers are surprised by the same mistake.
''')
add('flash_reward','Route2_EastBuilding_Text_ExplainHM05 Route2_EastBuilding_Text_CanGetThroughRockTunnel',
    'Oak\'s aide explains Flash after the reward or reminds us it helps navigate Rock Tunnel.','''
S~A useful bit of light, earned by meeting enough new neighbors.|
S~Flash addresses the visibility problem of dark routes such as Rock Tunnel.|
N~Good. Prepare the light before entering the dark.|
S~A little less uncertainty under the mountain sounds very welcome.|
N~A practical reward for the next part of the journey.|
S~The field research has paid out in improved lighting for the next setting.|
S~A small answer to a very large amount of dark.|
S~Visibility upgrade acquired. It should make navigation less error-prone.|
S~A light carried beside you changes the shape of a cave.|
N~Useful guidance, especially before someone learns the need halfway inside.|
S~I wonder what part of Rock Tunnel people most often miss without light.
''')
add('amber_no_room','PewterCity_Museum_1F_Text_DontHaveSpaceForThis',
    'The researcher cannot give Old Amber because our bag is full.','''
N~Ancient history has waited this long; our bag can still make it wait another minute.|
N~The specimen was not transferred. Its intended examination remains pending.|
N~Make room. An old specimen deserves better than being jammed between supplies.|
F~A serious favor deserves a more prepared pair of hands than ours just now.|
N~We can sort the bag and return ready to carry it carefully.|
N~A scientific breakthrough has been delayed by luggage management.|
N~The old thing has survived time; it can survive a short wait for a proper place.|
N~Capacity issue. Also, protect the specimen rather than forcing it in.|
N~A piece of old sunlight is waiting outside a crowded pocket.|
N~We should make room properly if we are going to accept that trust.|
N~I wonder how the researcher has kept the amber safe until now.
''')
add('badge_talk_end','CeruleanCity_House1_Text_ComeVisitAnytime',
    'The badge enthusiast closes the explanation menu and invites another visit.','''
S~A little badge lecture, available whenever our curiosity comes back.|
N~The menu has ended. This farewell does not specify which explanations were selected.|
N~Good to know we can ask again instead of remembering it all at once.|
S~I appreciate somebody making questions feel welcome.|
N~A little learning is easier when there is time to return to it.|
S~The lecturer leaves office hours agreeably open.|
S~Some useful rooms are simply places where asking again is allowed.|
N~Reference service remains available. No need to memorize the entire interface.|
S~A patient voice can leave the door to a difficult subject open.|
S~A generous invitation, without another test attached.|
S~I wonder how often visitors return with a question they forgot the first time.
''')
