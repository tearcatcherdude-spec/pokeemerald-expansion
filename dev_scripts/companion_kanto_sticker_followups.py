"""Receipt-safe sticker tiers and remaining conditional actor endings."""
ROWS=[]
EMOTIONS=dict(N='neutral',S='soft_smile',A='annoyed',F='flustered',D='sad',U='surprised',M='smug',L='laughing')
def add(key,labels,subject,lines):
    replies=[]
    for line in lines.strip().split('|'):
        line=line.strip()
        if len(line)>1 and line[1]=='~' and line[0] in EMOTIONS:line=EMOTIONS[line[0]]+line[1:]
        replies.append(line)
    assert len(replies)==11,(key,len(replies))
    ROWS.append(dict(key='kanto_tier_end_'+key,labels=labels.split(),subject=subject,replies=replies))
add('daycare_second','DayCare_Text_WellRaiseYourMon',
    "The Day-Care lady confirms a deposit; this is final when both Day-Care places are occupied.",'''
S~A little stay has been arranged, and somebody else is taking a turn at the daily looking-after.|
N~The statement confirms the care arrangement without claiming a particular amount of growth.|
N~They are in her care now. We can return and check how things are going.|
S~It helps to hear the arrangement said plainly before we walk away.|
S~A temporary stay can be part of caring well, too.|
S~A supporting member of the journey is taking a short residence away from the road.|
S~A brief goodbye need not be a dramatic one to feel like something.|
N~We can plan the next visit without assuming a result before enough time has passed.|
S~One small life rests beneath another roof for a while.|
S~A clear handover makes the parting feel a little less uncertain.|
S~I wonder what familiar detail will be the first thing we notice when we come back.
''')
add('snorlax_asleep','Route12_Text_MonSprawledOutInSlumber Route16_Text_MonSprawledOutInSlumber',
    "A sleeping Snorlax lies comfortably across the route.",'''
L~A roadblock has achieved perfect comfort without consulting any of the road's users.|
N~The Pokemon appears deeply asleep. The blocked path is inconvenient, but there is no immediate emergency.|
N~No pushing it around. We need a sensible way to deal with the blocked route.|
S~It looks very comfortable in a place that is making everyone else's day less comfortable.|
N~A sleeping traveller should not be treated like a piece of luggage to drag aside.|
S~The road has acquired an immovable lead actor with no intention of waking for the cue.|
S~An impressively peaceful source of logistical difficulty.|
N~We should work around the actual obstacle instead of trying force first.|
S~The path has become somebody's entire afternoon bed.|
N~Comfortable is an excellent choice of mood and a less excellent choice of location.|
S~I wonder how long the path had been quiet before Snorlax decided it belonged to a nap.
''')
add('snorlax_leaves','Text_SnorlaxReturnedToMountains',
    "Snorlax calms down, yawns, and returns to the mountains after the encounter.",'''
S~A huge yawn has put a very gentle full stop on a rather large interruption.|
S~The immediate disturbance has ended, and Snorlax has left the route on its own.|
S~Good. The path is clear and the Pokemon has moved on.|
S~I am glad the last thing we see is it calm enough to yawn.|
S~Everyone can get back to their day without another argument over the road.|
S~The formidable obstacle has delivered a sleepy exit rather than a final threat.|
S~A surprisingly soft ending for something that occupied so much space.|
S~A clear route and a settled Pokemon are both useful outcomes.|
S~The mountain has called its wandering sleeper back.|
S~An enormous presence can leave a very peaceful absence behind it.|
S~I wonder whether the next chosen sleeping spot will inconvenience fewer travellers.
''')
add('hof_first_tier','FourIsland_House2_Text_WowHoFLowest',
    "The sticker collector recognizes Hall of Fame achievement and offers the first award tier.",'''
S~An enormous accomplishment has been met with a very small decorative celebration. I like the mismatch.|
S~The sticker records recognition of the Hall of Fame achievement without adding to the achievement itself.|
S~We earned the record. A little acknowledgment is welcome.|
S~It is nice when somebody hears the story and is simply pleased for us.|
S~A small keepsake can hold the memory of a much bigger day.|
S~The grand triumph has found an endearingly modest commemorative edition.|
S~A tiny bright square can be a perfectly respectable monument.|
S~A visible marker makes the milestone easy to recognize later.|
S~A large memory has been given a small place to rest.|
S~I like recognition that is allowed to be cheerful rather than solemn.|
S~I wonder which part of earning that record comes to mind when we look at the sticker.
''')
add('hof_repeated','FourIsland_House2_Text_WowHoFLow',
    "The collector admires repeated Hall of Fame entries and offers a higher award tier.",'''
S~Coming back and doing it again is a different sort of impressive from one wonderful afternoon.|
S~Repeated success suggests consistency across attempts, not only one favourable result.|
S~A strong record. The team has done a lot of work.|
S~Returning to a hard challenge can take a quieter kind of courage.|
S~There are a lot of preparations and recoveries hiding behind those entries.|
S~The successful run has acquired enough sequels to impress the reviewer.|
S~Familiar ground can still ask for real effort every time.|
S~Consistency usually means several small processes are working reliably together.|
S~The road has learned our footsteps through the number of times they returned.|
S~It is good to see repeated effort recognized instead of treated as automatic.|
S~I wonder which return visit felt most different from the first.
''')
add('hof_high','FourIsland_House2_Text_WowHoFHigh',
    "The collector is astonished by the large Hall of Fame record and says the player owns the League.",'''
L~We apparently own the League now. I hope ownership does not include sweeping all those corridors.|
S~His wording is enthusiastic exaggeration, but the record does reflect substantial repeated achievement.|
S~An impressive history. We can enjoy the praise without believing the exaggeration.|
F~He sounds so surprised that I almost want to check the record again.|
S~That much effort deserves more than pretending it was easy.|
S~The reviewer has promoted the visiting champion to proprietor of the entire venue.|
S~A fine achievement has received an entertainingly oversized hat.|
S~The underlying consistency is more interesting than the colourful description.|
S~A familiar road can become deep with the weight of remembered journeys.|
S~A little extravagant praise is charming when everyone knows it is affection talking.|
S~I wonder how many different teams and decisions are folded into that record.
''')
add('hof_highest','FourIsland_House2_Text_WowHoFHighest',
    "The collector can scarcely believe the Hall of Fame total and offers his highest tier.",'''
U~We have reached the number that makes the sticker man briefly forget how numbers work.|
S~The total has exceeded the scale his ordinary praise was prepared to describe.|
S~A lot of hard-won victories. We do not need another one today to make them count.|
S~I like that he still sounds capable of being surprised.|
S~After that much returning, a quiet day would also be well earned.|
S~The awards committee has reached the end of its adjective budget.|
S~A little astonishment has made the familiar record feel strange again.|
S~A long run of success represents many preparations, not simply a large final number.|
S~The small room has been asked to hold a very long stretch of road.|
S~His delight makes the last tier feel like a celebration rather than a formality.|
S~I wonder what advice we would give the version of us making that first attempt.
''')
add('eggs_discovery','FourIsland_House2_Text_WowEggsLowest',
    "The sticker collector is surprised to learn about Pokemon Eggs.",'''
L~We came to brag and accidentally became a very small educational programme.|
S~His surprise is a reminder that an ordinary fact to one traveller may be new to someone else.|
S~He learned something. No need to make him feel foolish for not knowing.|
S~I like seeing someone delighted by a thing that had become familiar to us.|
S~A fresh discovery can make an old subject feel interesting again.|
S~The intended boast has become an introductory lecture with a decorative honorarium.|
S~The world has managed to be larger than he expected without leaving the room.|
S~A new observation is a perfectly good reason to revise what he thought he knew.|
S~Something ordinary has opened a new little window for him.|
S~His lack of embarrassment makes the surprise rather charming.|
S~I wonder what question he will think to ask after we have gone.
''')
add('eggs_many','FourIsland_House2_Text_WowEggsLow',
    "The collector admires the number of Eggs hatched and assumes the player enjoys it.",'''
S~A lot of tiny introductions have added up to a very convincing reputation.|
N~The record establishes repeated hatching, though the motive need not be exactly what he assumes.|
S~That took patience. Worth recognizing it.|
S~Each one was its own little beginning, even if the total sounds like one big task.|
S~A lot of careful ordinary days sit behind a number like that.|
S~The collector has reviewed the quantity and inferred a favourite genre.|
S~A heap of separate beginnings can look oddly tidy from a distance.|
S~Repeated care is less flashy than the final number but much more important to the process.|
S~Many closed little worlds have opened along the same stretch of road.|
S~It is nice that he sees enthusiasm in the work instead of only a statistic.|
S~I wonder which hatching we remember most vividly out of all those quiet waits.
''')
add('eggs_machine','FourIsland_House2_Text_WowEggsHigh',
    "The collector calls the prolific hatcher an Egg-hatching machine.",'''
L~An Egg-hatching machine still needs snacks, sleep, and somewhere to put its shoes.|
S~A colourful description of persistence, though the work still depends on individual care.|
S~A strong record. We are still allowed a break.|
S~The number is impressive, but I like thinking of the separate little lives behind it.|
S~No machine here. Just a lot of patient days and new mouths to welcome.|
S~The enthusiastic reviewer has promoted the traveller to an entire specialist industry.|
S~A human being has once again been mistaken for the sum of their busiest habit.|
S~A repeated process can become efficient without making its results interchangeable.|
S~Each new beginning remains singular, however many have come before it.|
S~I would keep the compliment and quietly put the mechanical nickname aside.|
S~I wonder whether the most memorable hatch was one we expected or one that startled us.
''')
add('eggs_highest','FourIsland_House2_Text_WowEggsHighest',
    "The collector is overwhelmed by the highest Egg-hatching tier and asks what motivates it.",'''
S~The total is so big that he has started asking about the person behind the Egg collection.|
S~Motivation is a more interesting question than assuming a large record explains itself.|
S~That much care takes commitment. No need to make the number larger right now.|
S~I think the honest answer could be much smaller and warmer than the grand total.|
S~A love of beginnings can turn into a remarkable amount of daily work.|
S~At last, the interviewer has moved from the impressive statistic to the character question.|
S~A very large habit can grow around a surprisingly small fondness.|
S~It would be interesting to know which parts of the process kept it rewarding.|
S~A hundred little dawns may all be loved for different reasons.|
S~He sounds sincerely curious now, beneath the magnificent overstatement.|
S~I wonder what story we would choose instead of answering with another number.
''')
add('link_success','FourIsland_House2_Text_WowLinkWinsLowest',
    "The collector recognizes success in battles against other trainers.",'''
S~A few good matches have travelled all the way into this man's sticker collection.|
S~Competition with other trainers tests decisions against someone else's changing plans.|
S~A good record. Respect the people who helped make those matches worth having.|
S~Winning feels nicer when the other person still wants to say hello afterward.|
S~A friendly match can give both trainers something useful to take home.|
S~The competitive record has received a modest but enthusiastic local review.|
S~A victory is more pleasant when it leaves a conversation still possible.|
S~Another person's decisions make a match more revealing than practising the same sequence.|
S~Two roads have crossed often enough to leave a few bright marks.|
S~Being a good opponent makes the achievement easier to celebrate.|
S~I wonder which match taught us something we could not have learned alone.
''')
add('link_repeated','FourIsland_House2_Text_WowLinkWinsLow',
    "The collector admires repeated victories against friends.",'''
S~Winning often is impressive. Having friends who still enjoy the matches is a very good extra part.|
S~Repeated competition can be valuable when both trainers have opportunities to adapt.|
N~Keep the matches fair and the friendships worth coming back to.|
S~I hope there is room for laughing together after the difficult matches, too.|
S~The best repeat opponents are people we actually like spending time with.|
S~The successful rivalry has apparently secured a recurring cast.|
S~A familiar opponent can teach entirely new lessons on an ordinary rematch.|
S~Shared practice works best when both people can learn rather than one only collect wins.|
S~A friendly road can cross itself many times without wearing thin.|
S~A good winner makes it easy for someone to be glad the two of them played.|
S~I wonder how many of those victories came after finally understanding an old friend's favourite tactic.
''')
add('link_friends','FourIsland_House2_Text_WowLinkWinsHigh',
    "The collector jokingly wonders whether so many victories have cost the player friendships.",'''
N~A win should not come with a compulsory friendship deduction. Good manners help.|
N~The result alone does not determine whether people enjoy competing together. Conduct matters.|
N~Win decently. A friend is worth more than another mark in the record.|
N~It would be sad if being good at something made sharing it feel unpleasant.|
N~A thoughtful winner leaves room for the other person to enjoy the afternoon, too.|
N~The reviewer has identified the social cost the scorekeeper conveniently omits.|
N~A victory can become very lonely if it insists on being the whole conversation.|
N~We can keep the challenge interesting without treating friends as sources of points.|
N~A bright record is a poor lantern if everybody else has stopped walking beside it.|
N~A little graciousness can keep an impressive streak from becoming a tedious personality.|
N~I wonder whether the friends remember those matches as fondly as the winner does.
''')
add('link_highest','FourIsland_House2_Text_WowLinkWinsHighest',
    "The collector extravagantly praises the highest victory tier as the stuff of nightmares.",'''
L~Nightmare is a very dramatic title to receive from a man holding a sticker sheet.|
S~His astonishment is understandable, though the theatrical wording exceeds the information in the record.|
S~A formidable record. We can still make a match pleasant for the person across from us.|
F~I would rather people be excited to see us than actually frightened to try.|
S~A long winning record is worth enjoying without making it the whole meal.|
M~A fearsome legend has been officially endorsed by a tiny decorative awards office.|
S~A grand dark title attached to a remarkably cheerful form of stationery.|
S~Such consistency is interesting; I would rather examine the decisions than cultivate the reputation.|
N~Strength is kinder when it does not need somebody else's unease to feel real.|
S~I would accept the extravagant praise and continue being pleasant company.|
S~I wonder which match the collector would find most surprising if he could hear the actual story.
''')
