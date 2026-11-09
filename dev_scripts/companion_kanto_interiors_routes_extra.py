"""Append-only continuation of source-reviewed Kanto interior/route replies."""
ROWS = []
EMOTIONS = dict(N='neutral', S='soft_smile', A='annoyed', F='flustered',
                D='sad', U='surprised', M='smug', L='laughing')

def add(key, labels, subject, lines):
    replies = []
    for line in lines.strip().split('|'):
        line = line.strip()
        if len(line)>1 and line[1]=='~' and line[0] in EMOTIONS:
            line = EMOTIONS[line[0]] + line[1:]
        replies.append(line)
    assert len(replies)==11, (key,len(replies))
    ROWS.append(dict(key='kanto_irx_'+key,labels=labels.split(),subject=subject,replies=replies))

add('r11_hugo','Route11_Text_HugoPostBattle',
    'Hugo declares that life is about Pokemon and playing games.','''
S~A cheerful philosophy with room for a lunch break, I hope.|
N~Play can be valuable without accounting for the whole of life.|
N~Enjoy it. Remember the partners doing the work.|
S~He sounds happy to have something he loves this much.|
S~A day with play in it is usually better than one without.|
M~A complete philosophy, delivered roadside without tuition fees.|
S~A little play makes being alive less severe.|
S~Enthusiasm successfully detected. Supporting evidence: all of him.|
S~He has found something that makes the days move brightly.|
S~An uncomplicated joy. Those are rarer than they look.|
S~I wonder which game he would introduce a newcomer to first.
''')
add('r11_jasper','Route11_Text_JasperPostBattle',
    'Jasper insists a Pokemon trainer cannot be a coward.','''
N~Being scared and doing the sensible thing can happen together.|
N~Fear can provide useful information. Ignoring it is not inherently brave.|
N~Caution keeps partners safe. Call it what you want.|
N~A frightened person can still try. I wish he had said that.|
N~Knowing when to stop is a skill worth keeping.|
N~He has offered a bold slogan where a little nuance might survive longer.|
N~Fear does not revoke your right to belong out here.|
N~Warning systems are useful. I do not remove them to look confident.|
N~Even brave creatures know how to step away from a fire.|
N~He could encourage people without shaming the ones who are nervous.|
N~I wonder whether he gives himself permission to be afraid.
''')
add('r11_eddie','Route11_Text_EddiePostBattle Route24_Text_EthanPostBattle Route24_Text_ReliPostBattle Route24_Text_TimmyPostBattle Route24_Text_AliPostBattle Route24_Text_CalePostBattle',
    'These defeated trainers say they did their best and have no regrets.','''
S~A loss with a clean landing. They know they showed up properly.|
S~Satisfaction with sincere effort need not depend on victory.|
S~Fair enough. They put the work in and can stand by it.|
S~I like that they can say that without pretending they won.|
S~An honest effort is something worthwhile to take home.|
S~The result is settled, and they have declined to turn it into a personal tragedy.|
S~A quiet dignity. No elaborate excuse needed.|
S~Good effort acknowledged, result accepted. Useful place to begin improving.|
S~They can leave the field without leaving something bitter behind.|
S~There is confidence in accepting a loss without dressing it up.|
S~That tells me they value how they battled as well as the outcome.
''')
add('r11_braxton','Route11_Text_BraxtonPostBattle',
    'Braxton urges us to spread the word about conserving energy.','''
S~A message worth passing on. Preferably without shouting ourselves tired.|
N~Small conservation habits become more effective when many people adopt them.|
N~Use what you need. No point wasting the rest.|
S~He wants the thought to go farther than this conversation.|
N~Saving a little each day is easier than finding more when it runs out.|
S~An energetic appeal for using less energy. I appreciate the dedication.|
S~Leaving something unused can be its own useful act.|
S~Less waste, same useful work. My favorite kind of improvement.|
S~A little left over means a little more for later.|
N~A practical cause, if people turn the slogan into a habit.|
N~I wonder what small change he would recommend first.
''')
add('r11_dillon','Route11_Text_DillonPostBattle',
    'Dillon asks to be left alone after the battle.','''
N~He would like the conversation to stop. We can manage that.|
N~The request is clear enough. Further questions would be unwelcome.|
N~Give him space. We are finished here.|
N~I would rather leave him to settle down.|
N~He needs a quiet moment more than another visitor.|
N~A farewell with all the decorative flourishes removed.|
N~Solitude requested, with very little ambiguity.|
N~No follow-up needed. Message received.|
N~A little distance may soften the air around him.|
N~Roughly phrased, but the boundary is clear.|
N~He seems ready to be alone with the result.
''')
add('r11_dirk','Route11_Text_DirkPostBattle',
    'Dirk dismisses our victory as luck.','''
M~Luck must have been doing a remarkable amount of training lately.|
N~Random factors exist, but do not account for every decision in that battle.|
N~He can call it luck. The team still did the work.|
N~It stings a little when effort gets brushed aside that quickly.|
N~We know what the team put into that. No need to argue.|
M~A verdict designed to preserve the speaker's spotless self-review.|
M~How convenient that luck can accept all the blame without answering back.|
N~If he skips the review, he skips a chance to improve.|
N~A small excuse can cast a surprisingly comfortable shadow.|
N~We do not need his approval to recognize the team's effort.|
N~I wonder what he would notice if he watched the battle again.
''')
add('r11_darian','Route11_Text_DarianPostBattle',
    'Darian blames another loss on his usual bad luck.','''
N~His luck has become the designated villain of every afternoon.|
N~A recurring result deserves examination beyond a recurring explanation.|
N~Look at the battle. There may be something he can actually change.|
N~He sounds used to expecting things to go wrong. That must feel heavy.|
N~One small adjustment could help more than another sigh at fate.|
N~A familiar antagonist saves him the trouble of revising the plot.|
N~Bad luck can become an easy name for disappointment that keeps returning.|
N~Repeated failure suggests checking the setup, not just cursing the test.|
N~A cloud follows more easily when you keep looking only for rain.|
N~I hope he gives himself a useful explanation instead of a permanent label.|
N~I wonder whether anyone has helped him review what actually happened.
''')
add('r11_yasu','Route11_Text_YasuPostBattle',
    'Yasu wonders about the strength of a large Pokemon descending from the mountains.','''
U~A mountain visitor with a very noticeable silhouette. Interesting lead.|
N~Size suggests some possibilities, but is not enough to assess battle ability.|
N~A large unfamiliar Pokemon deserves room before it deserves a challenge.|
N~He sounds curious rather than certain. I like that distinction.|
N~Whatever it is, meeting it calmly seems wiser than testing its strength first.|
S~A passing mountain resident has become the subject of roadside speculation.|
N~Something large coming down from the hills sounds worth noticing carefully.|
N~We need more observations before making a useful identification.|
S~The mountain occasionally sends someone down to visit.|
N~A memorable sight does not tell us everything about the creature.|
S~I wonder when he saw it and what it was doing.
''')
add('r11_bernie','Route11_Text_BerniePostBattle',
    'Bernie ends his break and returns to work.','''
S~Battle break over. The ordinary world has called him back.|
N~He appears to be fitting training around another responsibility.|
N~Fair enough. We should let him get on.|
S~It is nice to see a little of the rest of someone's day.|
S~A short break can make getting back to work easier.|
S~Our dramatic encounter has concluded before the end of his shift.|
N~The day resumes its less heroic duties. As days tend to do.|
N~Break completed, main task resumed. Efficient afternoon.|
N~An adventure can fit between two ordinary pieces of work.|
S~He knows when the break is over. A useful skill.|
S~I wonder whether his coworkers hear about these roadside battles.
''')
add('r11_dave','Route11_Text_DavePostBattle',
    'Dave decides he needs to catch stronger Pokemon.','''
N~Before replacing the team, maybe ask what the team needed.|
N~A new Pokemon may help, but training and tactics also influence the result.|
N~Do not blame the partners before checking your own choices.|
N~I hope the Pokemon with him still feel wanted.|
N~An existing partner may need a better plan more than a replacement.|
N~The casting department has received the blame before the director was consulted.|
N~A loss is a poor moment to decide the whole team is disposable.|
N~Check the current setup before buying a completely new solution.|
N~The companions already beside him deserve more than a disappointed glance.|
N~Stronger is not much of a plan unless he knows what is missing.|
N~I wonder whether he has noticed what his present team does well.
''')
add('r12_ned','Route12_Text_NedPostBattle',
    'Ned has snagged his fishing line.','''
N~He caught the scenery. A very uncooperative species.|
N~A snag calls for care; pulling harder may simply break the line.|
N~Easy with it. No need to hurt your hands over a hook.|
N~That is a frustrating interruption to a quiet pastime.|
N~A little patience now might save the line and the rest of his afternoon.|
M~The fishing expedition has made a firm connection with an immovable supporting character.|
N~The bottom has accepted his offering and declined to return it.|
N~Tension problem. More force is not automatically the next step.|
N~Something under the water has decided to keep the thread.|
N~At least he noticed before winding himself into a bigger problem.|
N~I wonder how often this stretch catches hooks instead of fish.
''')
add('r12_chip','Route12_Text_ChipPostBattle',
    'Chip thinks a better fishing rod would broaden his catches.','''
N~The rod may be due for promotion. His patience already has experience.|
N~Equipment can limit the range of possible catches. His idea is reasonable.|
N~Worth checking what the current rod can actually catch.|
N~It is discouraging to keep trying without knowing whether the tool is enough.|
N~The right upgrade could make his next outing more rewarding.|
N~A modest equipment grievance, backed by several disappointing introductions.|
N~Sometimes waiting longer is less useful than changing what you brought.|
S~Correct tool for the task! Always worth checking before blaming your technique.|
N~A different rod may ask a different question of the water.|
N~An upgrade makes sense when it solves a problem he has actually noticed.|
N~I wonder which Pokemon he has been hoping to catch.
''')
add('r12_justin','Route12_Text_JustinPostBattle',
    'Justin thinks using a Moon Stone to evolve his Pokemon would have guaranteed victory.','''
N~A Moon Stone might change the Pokemon. It cannot promise the whole afternoon.|
N~Evolution could alter the matchup, but the alternative outcome is not certain.|
N~Maybe. Still need a plan after the change.|
N~It is tempting to imagine one choice would have fixed everything.|
N~He can consider the stone without making it responsible for every future win.|
N~A hypothetical victory has been assigned to a rock that was not consulted.|
N~The battle he imagines afterward has a suspiciously cooperative opponent.|
N~A changed component requires a new test. It is not proof of success.|
N~One stone can open a door without choosing everything beyond it.|
N~It might help. Guaranteed is doing a lot of work in that thought.|
N~I wonder whether he wanted that evolution before losing.
''')
add('r12_luca','Route12_Text_LucaPostBattle',
    'Luca recommends Electric attacks against sea Pokemon.','''
N~Useful battle advice. Terrible instruction for somebody repairing a seaside kettle.|
N~Electric attacks can be effective against Water types; individual typing still matters.|
N~Check the opponent before trusting a broad rule.|
N~A simple idea can be useful when there is a lot to remember.|
N~Good to learn the matchup before reaching for a move in a hurry.|
N~A familiar physical fact has been recruited into tactical commentary.|
N~The sea already has enough surprises without us forgetting the obvious ones.|
N~Compatibility matters. Also, please distinguish battle tactics from electrical work.|
N~Water carries more than reflections when lightning comes near.|
N~A useful starting rule, as long as he leaves room for exceptions.|
N~I wonder which sea Pokemon gave him the clearest demonstration.
''')
add('r12_hank','Route12_Text_HankPostBattle',
    'Hank accepts our battle skill but boasts that he is still the better angler.','''
S~He has saved one crown and graciously lent us the other.|
N~Different activities reward different practice. One result does not rank every skill.|
S~Fair enough. He knows what he is good at.|
S~It is nice that losing did not make him forget what he enjoys.|
S~We do not all need to be best at the same thing.|
M~A diplomatic settlement: the field is ours, the fishing platform remains his.|
S~A loss leaves plenty of room for another kind of pride.|
N~Separate skill sets, separate rankings. Reasonable enough.|
S~He has another quiet place where he knows his own hands.|
S~A little boast, but he gave the team credit first.|
S~I would be curious to watch him fish after hearing that confidence.
''')
add('r12_elliot','Route12_Text_ElliotPostBattle',
    'Elliot says losing no longer bothers him.','''
S~He has made peace with the scoreboard. Saves a lot of grumbling.|
N~Accepting a result can make it easier to examine without defensiveness.|
S~Good. Plenty left to enjoy after one loss.|
S~I hope that means he can enjoy the battle more easily now.|
S~A calmer ending is good for the whole team.|
S~The defeat has been admitted without being given the whole room.|
S~Some disappointments get smaller once you stop feeding them.|
N~Less frustration leaves more room to learn from the result.|
S~The water keeps moving, and he seems ready to move with it.|
S~There is a relaxed confidence in not needing every result to flatter you.|
S~I wonder what changed his mind about losing.
''')
add('r12_andrew','Route12_Text_AndrewPostBattle',
    'Andrew complains that the Magikarp he catches are weak.','''
N~They are doing their best at being Magikarp. A demanding profession.|
N~A Pokemon's current battle performance does not exhaust its possible value.|
N~If he keeps catching them, he could at least treat them with respect.|
N~It sounds unkind when the Pokemon did nothing but be caught.|
N~A little patience can matter more than calling a partner useless.|
N~The angler's abundant supporting cast has received a rather ungrateful review.|
N~Poor fish. Being common apparently earns them extra criticism.|
N~Repeatedly getting the same result suggests reviewing the method, not insulting the output.|
N~A small fish still has a whole life behind its small splash.|
N~He could want a different catch without putting these ones down.|
N~I wonder whether he knows anything about them beyond their battle strength.
''')
add('r12_jes','Route12_Text_JesPostBattle',
    'Jes dramatically asks Gia to forgive his role in their defeat.','''
N~That is a lot of apology for one battle. I hope he remembers to breathe.|
N~Taking responsibility is useful; assuming the entire result was his fault may not be.|
N~Apologize once, then work out what actually went wrong.|
F~He seems more frightened of disappointing Gia than of losing.|
N~A calmer conversation would probably help them both more.|
N~A roadside tragedy in which the stakes may need a slightly smaller orchestra.|
N~The apology has arrived before the practical review. By quite a distance.|
N~Emotional alarm is high. Troubleshooting would work better at a lower volume.|
N~He is trying to mend something before knowing where it broke.|
N~He cares what she thinks. I hope he can hear his own thoughts too.|
N~I wonder whether they usually talk this way after a loss.
''')
add('r12_gia','Route12_Text_GiaPostBattle',
    'Gia blames Jes for spoiling their double battle.','''
N~A team of two should not become a blame delivery service.|
N~Assigning fault before reviewing their joint choices is unlikely to improve coordination.|
N~They both battled. They both need a fair say afterward.|
D~That sounds harsh when he is already apologizing.|
N~A kind word would do more for the next attempt than another sharp one.|
N~The partnership's post-match review has become regrettably one-sided.|
N~Disappointment does not need a person to stand in front of it and take the hit.|
N~Blame is not the same as a useful diagnosis.|
N~A shared defeat should not leave only one person standing in the cold.|
N~She can be upset without making him the whole problem.|
N~I wonder what he would say if he felt able to answer honestly.
''')
add('r15_kindra','Route15_Text_KindraPostBattle',
    'Kindra explains that only the original trainer can change a traded Pokemon\'s nickname.','''
N~A name can travel farther than the person who chose it.|
N~The nickname retains a link to the original trainer through that restriction.|
N~Best know that before agreeing to a trade.|
N~A familiar name may matter to the Pokemon even when its home changes.|
N~Worth considering the name as part of the partner you are welcoming.|
N~A former trainer's creative decision has acquired remarkable permanence.|
N~A little piece of the old life arrives with the new companion.|
N~Persistent naming rights. Important constraint to know in advance.|
N~Someone's first word for you can follow a long journey.|
N~A nickname carries taste and history. Sometimes more of one than the other.|
N~I wonder what memorable traded name made her bring that up.
''')
add('r15_becky','Route15_Text_BeckyPostBattle',
    'Becky says the Bikers\' appearance frightens her.','''
N~Looking mean is not proof. Acting mean would be a more convincing clue.|
N~Appearance alone is an unreliable predictor of how someone will behave.|
N~Keep space if you feel unsafe. Judge what people actually do.|
N~I understand being nervous, though looks do not tell the whole story.|
N~She deserves to feel safe without deciding every stranger is dangerous.|
N~A costume has received a moral review before the wearer has spoken.|
N~Dark clothes attract a surprising amount of fictional wrongdoing.|
N~Visual warning signs can be misleading. Actual behavior is better evidence.|
N~A sharp outline does not always hide a sharp intention.|
N~Some people cultivate a rough look. That still leaves the person to meet.|
N~I wonder whether someone frightened her or she has only seen them from afar.
''')
add('r15_edwin','Route15_Text_EdwinPostBattle',
    'Edwin doubts he is suited to battling after losing.','''
S~One loss is a very small audition for a whole life.|
N~A single result cannot establish whether he could improve with suitable practice.|
S~He can decide later. No need to write himself off while it still stings.|
D~I know how quickly one bad attempt can sound like a final answer.|
S~There are other ways to enjoy Pokemon if battles do not make him happy.|
S~A disappointing scene need not decide the casting of the whole story.|
S~Perhaps he needs a different approach. Perhaps a different joy. Neither is failure.|
N~One test is not a complete assessment of capability.|
S~A path can be difficult without being closed to you.|
S~He is allowed to keep trying, and allowed to prefer something else.|
S~I wonder whether he enjoyed any part of the battle before judging himself.
''')
add('r15_chester','Route15_Text_ChesterPostBattle',
    'Chester explains that Ground attacks such as Earthquake and Fissure do not affect birds.','''
N~Hard to shake the ground under someone who is not standing on it.|
N~Flying immunity is an important matchup consideration for Ground attacks.|
N~Check what the opponent can ignore before choosing a move.|
N~Useful advice, though he did not need to make knowing it sound mandatory.|
N~A reminder can help even when somebody thinks the rule is obvious.|
M~The lesson is useful; the little preface announcing its obviousness less so.|
N~The earth may complain all it likes. A flying bird need not answer.|
N~A powerful tool is useless against the wrong target. Always check compatibility.|
N~The ground cannot catch every creature that passes above it.|
N~He could share that without making someone feel foolish for learning it now.|
N~I wonder how many trainers he has seen try the wrong move here.
''')
add('r15_grace','Route15_Text_GracePostBattle',
    'Grace says she forgives our victory and is old enough to cope.','''
S~She has granted us absolution for following the battle rules. Very generous.|
N~She seems to be reassuring herself that she can manage disappointment.|
S~She held up fine. A loss is allowed to sting a little.|
S~Trying to sound grown-up after something hurts is very familiar.|
S~She can be proud of trying without pretending she felt nothing.|
S~A dignified pardon, issued while its author steadies herself.|
S~Growing up need not mean becoming impossible to upset.|
N~Handling a setback is a skill. This looks like practice.|
S~A small voice can stand a little taller after being shaken.|
S~She is giving herself a way to leave with her head up.|
S~I wonder whether saying it aloud helped her believe it.
''')
add('r15_olivia','Route15_Text_OliviaPostBattle',
    'Olivia treasures her Pokemon greeting her when she gets home.','''
S~A welcoming committee with tails. Extremely strong argument for going home.|
S~A familiar greeting can make returning home reliably comforting.|
S~Good to have somebody glad you made it back.|
S~I can hear the warmth in how she talks about that moment.|
S~That sounds like the best part of an ordinary evening.|
S~No grand ceremony can quite compete with being expected by someone delighted.|
S~A little proof that your absence was noticed kindly.|
S~Reliable positive feedback at the door. Hard to improve that design.|
S~A house feels different when something inside is listening for you.|
S~Being welcomed without needing to impress anyone is a lovely luxury.|
S~I wonder which one always gets to the door first.
''')
add('r15_ernest','Route15_Text_ErnestPostBattle',
    'Ernest glorifies outlaw life and cheers for Team Rocket.','''
N~Life is short. Making everyone else's day worse is a strange way to spend it.|
N~Excitement does not justify harming others. The slogan offers no actual defense.|
A~People get hurt by that crowd. Nothing cool about it.|
N~He sounds excited by the image and uninterested in who suffers for it.|
N~There are better ways to feel alive than frightening people.|
N~A glamorous outlaw fantasy has omitted every person left to clean up afterward.|
N~Cruelty in an interesting jacket is still cruelty.|
N~If the plan requires ignoring the damage, the plan is bad.|
N~A short life is no reason to leave sharp pieces in other people's paths.|
A~A rough image does not make hurting people stylish.|
N~I wonder whether he has ever listened to someone Team Rocket actually frightened.
''')
add('r15_alex','Route15_Text_AlexPostBattle',
    'Alex dismisses his earlier demand for money as a joke.','''
N~An odd joke if only the person asking for money knows it is funny.|
N~Calling a demand a joke afterward does not remove its effect at the time.|
N~Then pick a joke that does not sound like a threat.|
N~It did not feel especially lighthearted from this side.|
N~A joke works better when the other person can relax enough to laugh.|
N~The threatening opening has received a hasty comic rewrite.|
N~A convenient punchline, arriving just after the consequence.|
N~Intent should be clearer before someone else has to assess the risk.|
N~Some words leave a bruise even after someone calls them light.|
N~He could acknowledge how it sounded instead of blaming us for hearing it.|
N~I wonder whether he says that every time someone objects.
''')
add('r15_celia','Route15_Text_CeliaPostBattle',
    'Celia says she frequently trades Pokemon with friends.','''
S~Her Pokemon have a very well-connected social circle.|
S~Regular trades between friends could expose everyone to a wider range of partners.|
N~Good to know the people you are trusting with a partner.|
S~It must be nice to keep hearing how the Pokemon are doing afterward.|
S~Friends can make the change feel a little less uncertain.|
S~A lively exchange network, with friendship doing the paperwork.|
S~A new home does not have to mean every familiar door closes.|
S~A trusted exchange network! Much less guesswork than dealing with strangers.|
S~The roads between friends carry more than the friends themselves.|
S~Knowing one another's tastes probably makes the choices easier.|
S~I wonder whether their Pokemon recognize one another when the friends meet up.
''')
add('r15_yazmin','Route15_Text_YazminPostBattle',
    'Yazmin decides to practice against weaker opponents.','''
N~A gentler challenge can help. Just do not mistake easy wins for the whole lesson.|
N~Appropriate difficulty can support practice, provided the goal is skill rather than reassurance.|
N~Train at a workable level. Do not bully somebody smaller.|
N~It is reasonable to want a challenge she can understand better.|
N~A steady next step can help more than repeating an overwhelming fight.|
N~A smaller stage may help her rehearse, if applause is not the only objective.|
N~There is a difference between finding your pace and finding someone to crush.|
N~Reduce difficulty, isolate the skill, then increase it again. Good if done deliberately.|
N~A shallow place can teach you to stand before you try the deep water.|
N~Useful practice should build confidence without borrowing it from someone else's humiliation.|
N~I wonder what specific part of her battling she wants to improve.
''')
add('r15_mya','Route15_Text_MyaPostBattle',
    'Mya plans to add to the siblings\' training schedule after losing.','''
N~The training menu has expanded. I hope rest is still one of the courses.|
N~More practice can help if it addresses what actually happened in this match.|
N~Ask her partner how much they can handle before adding more.|
N~She is eager to improve. I hope they agree on what the new plan looks like.|
N~A sensible menu includes recovery as well as hard work.|
N~The schedule has grown in response to criticism from reality.|
N~More is an easy answer. Better takes a little more thought.|
N~Add the exercise that fixes the problem, not simply more of everything.|
N~A growing plan still needs room for people to breathe inside it.|
N~Enthusiasm is good. Making a plan together would be better.|
N~I wonder whether Ron helped choose anything on that menu.
''')
add('r15_ron','Route15_Text_RonPostBattle',
    'Ron wishes his sister were nicer after she increases their training.','''
N~The revised training menu has received a complaint from the dining room.|
N~His reaction suggests the new schedule needs more discussion between them.|
N~He should get a say in the training he has to do.|
N~He sounds worn down more than excited about improving.|
N~They might enjoy practicing more if they planned it together.|
N~The supporting sibling would like a word with the author of the schedule.|
N~A family team still needs room for both people's wishes.|
N~Poor agreement at the planning stage becomes poor morale during the work.|
N~A shared road feels longer when only one person chooses the pace.|
N~A little kindness would probably get further than another added drill.|
N~I wonder whether she hears how unhappy he sounds.
''')
add('r16_lao','Route16_Text_LaoPostBattle',
    'Lao defensively says the group likes spending time here.','''
N~A simple answer wearing a rather spiky coat.|
N~Enjoying the location is an adequate reason to be here. The hostility adds little.|
N~He can stay. We can pass. Easy arrangement.|
N~I do not mind where he spends his afternoon.|
N~There is room to enjoy the place without making visitors feel unwelcome.|
N~The local leisure committee has issued a defensive statement.|
N~Standing somewhere need not become a declaration of war.|
N~Compatible requirements: they stay here, we continue down the road.|
N~A familiar patch of ground can matter a great deal to someone.|
N~He sounds ready for an argument nobody needs to start.|
N~I wonder what they like most about this particular spot.
''')
add('r16_koji','Route16_Text_KojiPostBattle',
    'Koji angrily denies needing our bicycle after losing.','''
N~The bicycle has survived a very moody appraisal.|
N~The change of attitude appears more related to the result than the bicycle.|
N~Good. Our bike stays right here with us.|
N~That sounds like a conversation best left finished.|
N~No argument needed. We can keep moving.|
M~The coveted object has abruptly lost all appeal in the official account.|
N~A remarkably convenient change of taste.|
N~Ownership dispute canceled. Excellent outcome for the bicycle.|
N~The road remains open, and the bike remains ours.|
M~He has decided it was never desirable. A familiar recovery strategy.|
N~I wonder how long this new lack of interest will last.
''')
add('r16_luke','Route16_Text_LukePostBattle',
    'Luke angrily says he hates losing and tells us to leave.','''
N~He has had enough of the result and quite enough of us. Time to go.|
N~Disappointment is understandable. The hostile delivery is still unnecessary.|
N~Leave him space. Nothing to gain by staying.|
N~I would rather go before he finds something else to be angry about.|
N~A quiet break would help him more than another exchange.|
N~A frank critical assessment of losing, followed by an eviction notice.|
N~An unpleasant feeling has become an unpleasant conversation. We can stop one of those.|
N~Overheated system. Best give it room to cool down.|
N~Let the sharp feeling spend itself without standing in its way.|
N~He could be more gracious. We can still be sensible about leaving.|
N~I wonder whether his team gets a kinder response once the visitors leave.
''')
add('r16_hideo','Route16_Text_HideoPostBattle',
    'Hideo insists the group will stay and suggests the coastal detour between Fuchsia and Vermilion.','''
N~A stubborn declaration with travel advice attached. Unexpectedly useful.|
N~The coastal route is useful information, though it may be a considerable detour.|
N~We can use the road without asking them to move away.|
N~He seems determined to argue. I appreciate the directions more than the tone.|
N~A detour is an option, but we should know how much farther it takes us.|
M~An entrenched resident briefly moonlights as a coastal travel adviser.|
N~A prickly conversation has left one practical thing on the table.|
N~Alternative route supplied. Need to compare distance and conditions before choosing.|
N~Even a difficult voice can point toward a useful road.|
N~He gave us a direction while insisting he does not care. Interesting combination.|
N~I wonder whether he has taken that coastal route himself.
''')
add('r16_camron','Route16_Text_CamronPostBattle',
    'Camron wants ferocious Pokemon to injure his enemies.','''
N~That is a lot of ugly intention to put on a Pokemon's shoulders.|
N~He is describing deliberate harm, not ordinary competitive training.|
A~Pokemon are partners. They are not his excuse to hurt people.|
N~I do not want to stay close to someone talking like that.|
A~He is asking living creatures to carry his grudges for him.|
N~A menacing image has become a frankly unpleasant plan.|
N~Cruelty does not improve when somebody else does the biting for you.|
N~That goal is the problem. Better equipment would only make it worse.|
N~A creature should not be made into the sharp edge of someone's spite.|
A~He can keep that fantasy. We should keep our distance.|
N~I wonder how his Pokemon are treated when they do not seem fierce enough.
''')
add('r16_ruben','Route16_Text_RubenPostBattle',
    'Ruben brags about using his Pokemon to frighten and bite people.','''
A~His idea of fun keeps arriving at somebody else's expense.|
N~He is deliberately encouraging harmful behavior toward passersby.|
A~Keep the team close. We are not giving him another opportunity.|
N~That sounds frightening for anyone who simply wants to use the road.|
A~Scaring people and getting them bitten is a rotten use of a partner's trust.|
N~The boast contains no redeeming twist. Just a bully enjoying an audience.|
A~An ugly little hobby. I am comfortable leaving him disappointed in our reaction.|
N~The dangerous part is that he considers this a successful outcome.|
N~Some people leave teeth in the memory of an ordinary walk.|
A~If the joke needs an unwilling victim, the joke is doing poorly.|
N~I wonder how many travelers have changed routes because of him.
''')
add('r16_jed','Route16_Text_JedPostBattle',
    'Jed asks Lea to pay less attention to him during battles.','''
M~A flattering distraction is still a distraction when the other team is attacking.|
N~Divided attention can interfere with coordination, even when the reason is affectionate.|
N~Fair request. Watch the battle while you are in it.|
F~That must be an awkward thing to say while somebody is smiling at you.|
S~They might have more fun if both can stay involved in the actual match.|
M~The romantic subplot has been asked to stop blocking the main action.|
M~Admiration has developed a minor tactical disadvantage.|
N~Attention allocation problem. He has identified it fairly clearly.|
N~Even a fond gaze can face the wrong direction for a moment.|
S~He asked directly rather than making her guess. Good start.|
N~I wonder whether she realizes how much of the match she missed.
''')
add('r16_lea','Route16_Text_LeaPostBattle',
    'Lea apologizes for being distracted by her admiration for Jed.','''
S~She heard the complaint. The admiration remains fully operational.|
N~She acknowledges the distraction without appearing particularly discouraged.|
N~Save the staring for after the match. Everybody wins.|
F~She seems happy enough to admit exactly what happened.|
S~A little focus during battle leaves plenty of time to enjoy each other's company later.|
M~The romantic subplot apologizes while firmly retaining its leading man.|
S~An embarrassingly happy explanation. There are worse problems to have.|
N~Cause confirmed. Now they need an actual adjustment, not just a cheerful diagnosis.|
S~Her thoughts keep wandering toward a very familiar face.|
M~She is not even pretending to have a more dignified excuse. Fair enough.|
S~I wonder whether Jed is trying not to look pleased.
''')
add('r18_wilton','Route18_Text_WiltonPostBattle',
    'Wilton wishes he owned a bicycle.','''
N~A road full of bicycles is a very persistent advertisement.|
N~The nearby cycling route makes that wish especially understandable.|
N~Would make some of these long stretches easier.|
S~Watching everyone ride past must make the walk feel longer.|
S~A good bike can turn an errand into something you look forward to.|
N~The scenery has supplied a repeated demonstration of the thing he lacks.|
N~Envy with wheels. At least it has a practical use.|
S~Human-powered transport is satisfying when the road cooperates.|
S~Two small circles can make the world feel less far away.|
S~He knows exactly which purchase would improve his afternoons.|
S~I wonder where he would ride first if he got one.
''')
add('r18_ramiro','Route18_Text_RamiroPostBattle',
    'Ramiro enjoys collecting sea Pokemon on weekends because the coast is nearby.','''
S~A local sea and a weekend plan. Nicely organized happiness.|
S~A nearby habitat makes repeated observation and practice much easier.|
S~Good to make use of a place he knows well.|
S~It is nice to have something familiar to look forward to.|
S~A regular day outside can do a lot for a long working week.|
S~The weekend has a reliable coastal appointment.|
S~An ordinary shoreline becomes a private little reason to anticipate Saturday.|
S~Convenient access makes a hobby much easier to keep doing.|
S~The sea is close enough to become part of his week.|
S~He has built a pleasant routine around what is already nearby.|
S~I wonder whether the same shore still surprises him after so many visits.
''')
add('r18_jacob','Route18_Text_JacobPostBattle',
    'Jacob calls this his favorite Pokemon-catching area.','''
S~He has a favorite patch of the map. Those are good to collect too.|
S~Repeated visits could give him detailed knowledge of the local encounters.|
S~Knowing a place well can be worth more than rushing somewhere new.|
S~A favorite place makes an ordinary outing feel easier to begin.|
S~Nice to find somewhere that keeps giving you reasons to come back.|
S~A familiar stretch of ground has earned a standing recommendation.|
S~He has found somewhere that does not wear out when repeated.|
S~Local expertise! He probably notices changes a visitor would miss.|
S~A place can become yours without belonging to you.|
S~A clear favorite, with no need to make it sound fashionable.|
S~I wonder what keeps drawing him back to this particular area.
''')
add('r20_barry','Route20_Text_BarryPostBattle',
    'Barry wishes he could ride a Pokemon rather than swim.','''
N~He has spotted the difference between a sea trip and an arm workout.|
N~Swimming and riding make very different demands on the traveler.|
N~Tired? Stop somewhere safe before it becomes trouble.|
N~I can understand envying a comfortable ride from down in the water.|
N~A rest would help more than comparing how tired everyone looks.|
M~Our transport has received an envious review from a floating critic.|
N~The view is probably lovelier when you are not swallowing it.|
N~A good transport method reduces the work. Someone still has to do it.|
N~The sea feels bigger when your own arms have to measure it.|
N~He is noticing comfort at exactly the point he could use some.|
N~I wonder how much farther he intended to swim today.
''')
add('r20_shirley','Route20_Text_ShirleyPostBattle',
    'Shirley tells us a huge cavern lies beneath the island.','''
U~An island with a whole downstairs. The sea keeps surprisingly large secrets.|
N~The visible island may be only a small part of the geological structure.|
N~Good to know. A cavern near the sea deserves careful footing.|
N~It is strange to stand above so much empty space.|
N~Exploring somewhere like that takes preparation, not just curiosity.|
S~A modest island turns out to have a considerably larger interior life.|
S~A dark room beneath all this brightness. Rather appealing.|
U~A huge underground space! I wonder how water moves through it.|
S~The land has kept a hollow thought beneath the waves.|
N~That changes how I imagine the little bit we can see.|
S~I wonder how much of the cavern she has actually explored.
''')
add('r20_tiffany','Route20_Text_TiffanyPostBattle',
    'Tiffany invites us to float with her.','''
S~For once, an invitation that does not involve going anywhere at all.|
S~A quiet pause can be appealing, provided the water and current are safe.|
N~Only if the conditions are safe. The sea can move you without asking.|
S~That sounds peaceful. A little quiet company without much conversation.|
S~A gentle break could be nice when everyone knows their limits.|
S~An admirably minimalist outing: remain here, and let the water do the staging.|
S~Being quietly beside someone can be enough of a plan.|
N~Low-effort recreation, variable drift. Keep an eye on the shore.|
S~A little while held up by something larger than yourself.|
S~A relaxed invitation. She makes stopping feel like a proper activity.|
S~I wonder whether she has a favorite spot where the water stays calm.
''')
add('r20_irene','Route20_Text_IrenePostBattle',
    'Irene says Seafoam was once one island.','''
U~The islands used to be one? Even the map has old family stories.|
N~Coastal erosion and geological change can transform a landmass over time.|
N~The sea has been working on this place longer than any of us.|
S~It is difficult to imagine the gap between them filled with land.|
N~A reminder that familiar places have histories far older than ours.|
S~The landscape has undergone an extensive revision since its first edition.|
S~Two pieces of land remembering a shape nobody living saw.|
S~A changed structure leaves clues. I would look for matching layers of rock.|
S~The water now lives where the island once held hands with itself.|
S~That makes the gap feel like part of the place's story.|
S~I wonder what evidence first showed people they used to be connected.
''')
add('r20_dean','Route20_Text_DeanPostBattle',
    'Dean realizes he trained his own physique while neglecting his Pokemon\'s preparation.','''
M~The muscles attended the workout. The battle team apparently missed the invitation.|
N~His personal fitness does not substitute for preparing the partners doing the battling.|
N~Training the team is his job too. Good that he noticed.|
N~It is useful to see the gap instead of just being angry about losing.|
N~He can keep enjoying his exercise and still make time for the Pokemon.|
M~The leading physique has discovered that the supporting cast needs rehearsal.|
N~An impressive silhouette cannot do everyone else's homework.|
N~Optimized the wrong subsystem. Familiar mistake, honestly.|
N~Strength in one place does not fill every empty place beside it.|
N~At least his conclusion includes something he can change.|
N~I wonder how he will include the team in his next training day.
''')
add('r20_darrin','Route20_Text_DarrinPostBattle',
    'Darrin thinks riding a Pokemon over the sea looks fun.','''
S~It does look like a very good way to keep your shoes in the same condition.|
S~The appeal includes companionship as well as easier transport.|
N~Fun when the partner is ready and the water is manageable.|
S~A shared trip can feel different from simply trying to cross.|
S~It would be a lovely way to enjoy the view without rushing.|
S~A floating traveler has developed an interest in upgrading the journey.|
S~The sea is easier to admire when it is not immediately in your mouth.|
S~Transport that also has a personality. Several advantages, some opinions.|
S~The water could become a road you travel together.|
S~A comfortable ride can be part of the pleasure, not just a shortcut.|
S~I wonder which Pokemon he imagines traveling with.
''')
add('r20_nora','Route20_Text_NoraPostBattle',
    'Nora wonders if pearls would grow larger inside Cloyster.','''
N~That is a question to research before making a very sharp clam uncomfortable.|
N~An interesting hypothesis, but resemblance to a shellfish does not establish pearl biology.|
N~Ask someone who knows. Do not put things inside a Pokemon to find out.|
N~I hope she is only wondering. Cloyster might have a strong opinion.|
N~Curiosity is fine. The Pokemon's comfort comes before an experiment.|
M~A potentially lucrative theory with an exceptionally uncooperative jewelry box.|
N~The beautiful shell may object to becoming a storage service.|
N~First check the biology. A closed shell is not a general-purpose growth chamber.|
N~A living shell keeps its own secrets, not necessarily our valuables.|
N~It is a striking idea. Permission and research would improve it considerably.|
N~I wonder where she heard the idea in the first place.
''')
add('r20_missy','Route20_Text_MissyPostBattle',
    'Missy says Pokemon occupy an abandoned Cinnabar mansion.','''
N~The mansion has new tenants. Probably a difficult place to deliver the mail.|
N~An abandoned human structure can become a habitat, especially with little disturbance.|
N~Then enter carefully. Empty of people does not mean empty.|
N~It is unsettling to picture familiar rooms occupied so differently.|
N~We should prepare before disturbing somewhere Pokemon have made their home.|
N~A deserted residence has received a new cast and a more accurate title.|
S~A house people left behind has found another way to be inhabited.|
N~Unused building, available shelter. Practical from the Pokemon's perspective.|
S~The old walls have learned to keep unfamiliar company.|
N~Calling it abandoned leaves out the ones living there now.|
N~I wonder how much of the old house is still recognizable inside.
''')
add('r20_melissa','Route20_Text_MelissaPostBattle',
    'Melissa recounts that volcanic activity raised Cinnabar from the sea.','''
U~An island built by a volcano. That is an exceptionally dramatic construction crew.|
N~Volcanic activity can build new land. Her account fits Cinnabar's setting.|
N~Worth remembering the ground here has a history of moving.|
S~It is strange to think of the island beginning below all that water.|
N~A beautiful place can have a powerful beginning underneath it.|
S~The island's origin story arrives with fire and an ocean-sized entrance.|
S~Land made from an argument between heat and water. Quiet now, at least.|
U~Natural construction on a huge scale! Rock laid down one eruption at a time.|
S~The sea once made room for something burning to become a home.|
S~It gives the island a very particular sort of presence.|
S~I wonder which parts of the shoreline still show that beginning clearly.
''')
add('r21_jack','Route21_South_Text_JackPostBattle',
    'Jack asks where our Pokemon were caught.','''
S~Every partner comes with directions to a different memory. That could take a while.|
S~Location can help explain the composition of a team, though not every partner was caught.|
N~A fair question. The team has covered a lot of ground.|
S~That is a nice way to ask about the journey behind a battle.|
S~Some of the best travel stories begin with meeting a partner.|
S~The cast list has prompted a request for the story behind its assembly.|
S~A question about the team can turn into a map of where you have been.|
S~Field origins! I would be interested in the encounter conditions too.|
S~Each companion carries a small piece of the place you met.|
S~He noticed the team closely enough to be curious about them.|
S~I like questions that look beyond how well a Pokemon fights.
''')
add('r21_jerome','Route21_South_Text_JeromePostBattle',
    'Jerome is exhausted but still has cycling and running stages ahead.','''
N~He has scheduled three ways to be tired and reached the first milestone.|
N~Fatigue this early makes pacing and recovery especially important for the remaining events.|
N~Stop if you need to. Finishing is not worth collapsing.|
N~That sounds daunting when he already feels spent.|
N~He needs to think about what he has left, not just what is left on the schedule.|
N~The itinerary has several more chapters than the body currently wants to read.|
N~An ambitious list can become rather cruel when the legs disagree.|
N~Energy budget needs revision. There are two major tasks still pending.|
N~The road ahead should be measured against the strength still here.|
N~Commitment is admirable. Listening to exhaustion is sensible too.|
N~I wonder whether he has support waiting between the stages.
''')
add('r21_roland','Route21_South_Text_RolandPostBattle',
    'Roland complains of severe sunburn.','''
N~The sun won that encounter without even asking for a battle. Time for shade.|
N~He should get out of direct sun rather than continuing the exposure.|
N~Find shade and cool down. No more standing out here to prove anything.|
N~That sounds painful. A sheltered place would be much kinder.|
N~Shade and a break come before another long outing.|
N~The beautiful weather has written an unkind review directly onto him.|
N~The sea reflects light with very little concern for human skin.|
N~Exposure limit exceeded. Immediate change of location seems wise.|
N~Even a bright day can leave something that aches afterward.|
N~A little preparation would have helped. Right now, he needs shelter.|
N~I wonder how long he has been out here without getting ashore.
''')
add('r21_claude','Route21_South_Text_ClaudePostBattle',
    'Claude has caught nothing and jokingly questions whether this is really the sea.','''
M~A disappointing afternoon has put the entire ocean's credentials under review.|
N~An absence of catches is not evidence that the habitat itself is artificial.|
N~Bad day fishing. The sea is still the sea.|
N~He must be frustrated if the water itself has become the suspect.|
N~A break or a different spot might help more than arguing with the shoreline.|
M~The angler formally accuses a large body of water of professional misconduct.|
M~The sea has offered no comment on these allegations.|
N~Check the method and the location before replacing the geographic explanation.|
N~A vast silence can feel personal when you have waited all afternoon.|
N~It is a good complaint, even if the ocean is unlikely to apologize.|
N~I wonder whether the other anglers here are having better luck.
''')
add('r21_nolan','Route21_South_Text_NolanPostBattle',
    'Nolan interrupts the conversation because something bites his line.','''
U~Our conversation has been outbid by a fish. Fair enough!|
S~His attention belongs on the line now. The timing appears promising.|
S~Let him focus. This is what he came for.|
S~That sudden excitement is lovely. We can leave him to it.|
S~A patient afternoon just became interesting. Good luck to him.|
S~A new character has entered from below the water and seized the scene.|
S~The quiet has finally answered him.|
S~Signal detected! Now is not the time for extra distractions.|
S~A small tug can change the shape of the whole afternoon.|
S~He forgot everything else at once. That is real enthusiasm.|
S~I wonder what is on the other end this time.
''')
add('r21_lil','Route21_North_Text_LilPostBattle',
    'Lil is tired and asks her brother to go home.','''
N~That sounds like a complete sentence and a reasonable request.|
N~Her fatigue should factor into any decision about continuing their outing.|
N~She wants to stop. He needs to listen.|
N~She should not have to keep asking for a rest.|
N~Going home is a sensible plan when the trip has stopped feeling manageable.|
N~The joint expedition has received a clear request to revise its ending.|
N~A shared outing does not require matching levels of exhaustion.|
N~One participant has reached the limit. The plan needs to account for that.|
N~A tired voice should not need to become a shout to be heard.|
N~Her comfort belongs in the plan as much as his goal does.|
N~I wonder how long she has been asking to turn back.
''')
add('r21_ian','Route21_North_Text_IanPostBattle',
    'Ian pressures his tired sister to continue exercising to lose weight.','''
A~His sister is a person, not a project he gets to keep pushing.|
N~A weight goal does not justify disregarding fatigue or personal choice.|
A~She asked to go home. Listen to her.|
N~That is an unkind answer to someone who just said she is tired.|
A~She needs a brother who listens, not another person counting her effort.|
N~He has confused encouragement with refusing to hear the other participant.|
A~Her body is not a group assignment with him in charge.|
N~Feedback from the person doing the work should change the plan.|
N~A goal that drowns out the person is no longer helping them.|
A~That tone would spoil any outing. Her request deserves respect.|
N~I wonder whether he has asked what she actually wants from this trip.
''')
add('r21_ronald','Route21_North_Text_RonaldPostBattle',
    'Ronald complains that none of his catches are good Pokemon.','''
N~A disappointing catch is still a creature, not a failed delivery.|
N~Good is vague. He may need to define what he is actually looking for.|
N~Want a different catch if you like. Treat these ones properly.|
N~I hope he does not say that where his own partners can hear.|
N~A little curiosity might make an ordinary catch more interesting.|
N~The sea has supplied candidates and received only blanket rejection.|
N~Common things spend a lot of their lives being underestimated.|
N~Unclear requirements make every result disappointing. He needs a better specification.|
N~A living thing has more to offer than the first use someone imagines.|
N~He could say what he wants without putting everything else down.|
N~I wonder what would make a catch count as good in his eyes.
''')
add('r21_wade','Route21_North_Text_WadePostBattle',
    'Wade complains that every catch seems to be Magikarp.','''
M~The Magikarp have formed a welcoming committee and refuse to delegate.|
N~Repeated similar catches may reflect the equipment, location, or encounter distribution.|
N~Try changing the rod or the spot before blaming the fish.|
N~I can see why the surprise has worn off a little.|
N~A different approach could give him something new to look forward to.|
M~The supporting cast appears to have negotiated exclusive fishing rights.|
S~Even a persistent little fish eventually becomes a familiar face.|
N~Consistent output suggests a consistent constraint. Check the setup.|
N~The water has learned one answer and keeps repeating it.|
N~A very recognizable problem. Perhaps it is time for a change of scenery.|
N~I wonder whether he has compared notes with the other anglers.
''')
add('r21_spencer','Route21_North_Text_SpencerPostBattle',
    'Spencer enjoys both the sea and the mountains.','''
S~Excellent. Two completely different ways to get sand or gravel in your shoes.|
S~Different habitats can reward different kinds of attention. No need to choose only one.|
S~Both are worth seeing. Both deserve preparation.|
S~I like that he does not feel obliged to pick a favorite.|
S~A change of place can make coming back to the first one sweeter.|
S~A man of expansive scenery and admirably little geographic loyalty.|
S~Water and stone are both good at making a person pleasantly small.|
S~Varied terrain, varied problems to solve. I see the appeal.|
S~The horizon can rise or lie flat and still call you outside.|
S~It is good to leave room for more than one kind of beautiful place.|
S~I wonder what he notices first when he goes from one to the other.
''')
add('r22_early_rival','Route22_Text_EarlyRivalPostBattle',
    'Our early rival anticipates the League\'s tough trainers and urges us onward.','''
N~He has given us both a warning and a shove toward it. Efficient rivalry.|
N~He knows the League requires preparation, even if he delivers the point competitively.|
N~We will move when the team is ready. He can set his own pace.|
N~He seems eager enough to hide being uncertain behind a challenge.|
N~Preparing properly is still progress, even when someone calls it dawdling.|
M~A rival's encouragement arrives dressed as an accusation of standing still.|
N~He is thinking ahead. A little patience would make it less abrasive.|
N~Known challenge, incomplete plan. Rushing does not fill the missing steps.|
N~Another person's hurry need not become the rhythm of our feet.|
N~He can be ambitious without choosing our timetable for us.|
N~I wonder what he is planning to change before he reaches the League.
''')
add('r22_late_rival','Route22_Text_LateRivalPostBattle',
    'Our later rival calls the battle a warm-up, criticizes our preparation, and leaves for the League.','''
M~He has departed at full confidence. Apparently that weighs less than modesty.|
N~His assessment is competitive commentary, not an objective review of our readiness.|
N~Let him go. We know what the team still needs.|
N~It is difficult to hear useful advice through quite that much boasting.|
N~We can review the battle ourselves without carrying his tone along.|
M~A brisk farewell from a man determined to win the last word as well.|
M~He has an impressive ability to make every result sound like his warm-up.|
N~Extract any useful information, discard the noise, prepare the team.|
N~Some people leave a little gust of rivalry after the road is empty.|
M~He makes confidence look effortless. Courtesy remains a work in progress.|
N~I wonder whether he says that to steady himself as much as to unsettle us.
''')
add('r24_shane','Route24_Text_ShanePostBattle',
    'Shane admits hiding because the people on the bridge frightened him.','''
S~Finding somewhere quiet was his answer. That is allowed.|
N~Avoidance can be a reasonable immediate response to feeling unsafe.|
N~No shame in stepping away from people who frighten you.|
S~I understand wanting a little space where nobody is looking for you.|
N~I hope he has somewhere comfortable to go when he is ready to leave.|
S~A small refuge from an audience he never asked for.|
S~Some people call it hiding. Sometimes it is just finding room to breathe.|
N~He identified a situation he could not manage and created distance. Sensible first step.|
S~A quiet patch of ground can be a kind of shelter.|
N~He trusted us enough to admit it. We should treat that gently.|
N~I wonder what happened on the bridge to make him this uneasy.
''')
add('r25_joey','Route25_Text_JoeyPostBattle',
    'Joey recommends varied Pokemon types to cover each other\'s weaknesses.','''
S~Nobody has to be good at everything if the team can share the job.|
N~A varied team can reduce exposure to any one unfavorable matchup.|
N~Have someone ready when your strongest partner needs help.|
S~I like a team where needing help is already part of the plan.|
N~Different strengths make the whole group easier to look after.|
S~An ensemble earns its place when the leading star meets a difficult scene.|
S~Even the strongest thing is allowed to need someone beside it.|
N~Complementary capabilities reduce a system's weak points.|
S~Different roots can hold the same patch of earth together.|
N~A good team makes room for more than one way to be useful.|
N~I wonder which weakness first made him rethink his team.
''')
add('r25_dan','Route25_Text_DanPostBattle',
    'Dan recalls seeing international trainers aboard the S.S. Anne.','''
U~A whole ship of different journeys briefly traveling together.|
S~That would offer a useful glimpse of training practices from other regions.|
S~Good place to learn how other people handle a team.|
S~Meeting so many visitors must make the world feel much larger.|
S~I imagine there were plenty of interesting stories over dinner.|
S~A vessel temporarily carrying several continents' worth of ambition.|
S~A ship is a strange little town that eventually scatters.|
S~So many approaches in one place! Plenty to compare.|
S~The sea brought faraway voices close enough to hear.|
S~Travelers make a place feel lively before they even unpack.|
S~I wonder which meeting he remembers most clearly.
''')
add('r25_flint','Route25_Text_FlintPostBattle',
    'Flint looks forward to his girlfriend comforting him after a loss.','''
S~A bad result is easier when a good person waits afterward.|
S~Supportive company can help put a setback in perspective.|
S~Good to have someone in your corner after the match.|
S~He sounds certain she will be kind. That is a comforting certainty.|
S~A familiar face can make the trip home feel much better.|
S~The battle's unhappy ending has a gentler scene waiting offstage.|
S~Someone to sit beside can be better than an explanation.|
S~A reliable support system. Those matter outside battles too.|
S~He knows where the day will become warmer again.|
S~It is sweet that comfort is the first thing he expects.|
S~I wonder whether they share their good days as readily.
''')
add('r25_kelsey','Route25_Text_KelseyPostBattle',
    'Kelsey wishes her boyfriend battled as well as we do.','''
N~I hope he is allowed a few good qualities outside the scoreboard.|
N~Battle performance is only one attribute of a person or relationship.|
N~He does not need to win every match to be worth her time.|
F~That would hurt a little if he heard it.|
N~Perhaps she could help him practice instead of comparing him to strangers.|
N~A boyfriend has been given an unfavorable review in absentia.|
N~An ordinary loss should not become a relationship ranking.|
N~If skill is the problem, practice is more useful than comparison.|
N~A person is larger than the one thing they did less well.|
N~Admiring us need not cost him a little dignity.|
N~I wonder what she likes about him when nobody is battling.
''')
add('r25_chad','Route25_Text_ChadPostBattle',
    'Chad recommends switching out a confused Pokemon.','''
N~Sometimes the best battle plan is letting someone else take this one.|
N~Switching can remove confusion and avoid its immediate risk.|
N~Pull them back before confusion turns into an injury.|
N~A simple way to give a struggling partner a little relief.|
N~No shame in asking the next teammate to help.|
N~A tactical exit can be a better line than a heroic mistake.|
N~Being confused is bad enough without being made to push through it.|
N~Change the active partner, remove the problem. Neat solution.|
N~A little distance can let a tangled moment pass.|
N~Practical advice with the partner's comfort built in.|
N~I wonder which battle taught him to switch promptly.
''')
add('r25_haley','Route25_Text_HaleyPostBattle',
    'Haley asks us for a Clefairy after hearing we came through Mt. Moon.','''
U~That is quite a souvenir request! Most people start with a pebble.|
N~Passing through a habitat does not establish that we caught a particular species.|
N~A Pokemon is not something we owe her for taking a route.|
F~She asks very directly. I would not quite know how to answer.|
N~Wanting one is understandable. It still matters where it will belong.|
M~Our travel history has generated an unexpectedly ambitious gift request.|
N~The moonlit souvenir has opinions and needs of its own.|
N~First check whether we even have one. There are several missing steps.|
N~A companion is not a little piece of the mountain to give away.|
N~A bold ask from someone we have only just met.|
S~I wonder what she likes most about Clefairy.
''')
add('r25_franklin','Route25_Text_FranklinPostBattle',
    'Franklin complains about being bitten by Zubat in the cave.','''
N~The cave left him a very unwelcome keepsake.|
N~An injury deserves attention rather than being treated as part of the scenery.|
N~Have that checked. No point ignoring a bite.|
N~That sounds painful. I hope he finds somewhere to rest.|
N~A little care now is better than letting a bad encounter spoil the whole day.|
N~His underground excursion has received a pointed review from a resident.|
N~Caves are considerably less romantic when the darkness bites.|
N~Inspect the injury before resuming the expedition.|
N~The dark left a sharp little mark on the journey.|
N~I hope he is doing more for it than complaining.|
N~I wonder whether he startled it in the dark.
''')
add('r25_nob','Route25_Text_NobPostBattle',
    'Nob admires the Pokemaniac\'s collection of many rare species.','''
S~That is a reputation backed by some very unusual company.|
S~A varied rare collection could reflect substantial travel and study.|
N~Impressive if those rare partners are cared for properly.|
S~He sounds intrigued by the person as much as the collection.|
S~There must be a lot of work behind keeping so many different needs straight.|
S~An eccentric title supported by a thoroughly committed cast.|
S~A collection can be a strange, living map of someone's curiosity.|
S~Rare species with different requirements. Serious organizational work.|
S~Some people gather small windows into places they have visited.|
S~A distinctive interest becomes much more interesting when it is sincere.|
S~I wonder which species surprised him most.
''')
add('r25_wayne','Route25_Text_WaynePostBattle',
    'Wayne points out a shortcut to Cerulean on the trail below.','''
S~Directions and fewer footsteps. An excellent parting gift.|
N~A local shortcut could reduce the return journey considerably.|
S~Useful. Check the trail before assuming it is the easy way.|
S~I appreciate someone making the next bit of the journey simpler.|
S~A shorter walk can leave more time for a proper rest in town.|
S~The road offers a merciful edit to our return itinerary.|
S~A little less distance between tired feet and familiar streets.|
S~Route optimization from local knowledge. Very useful.|
S~Sometimes a path seems kinder once somebody names where it goes.|
S~Clear directions, no fuss. A good way to finish a meeting.|
S~I wonder how many travelers walk past without noticing it.
''')
add('r3_colton','Route3_Text_ColtonPostBattle',
    'Colton notes that Pokemon beyond the forest differ from forest species.','''
S~New ground, new neighbors. The forest was only the first guest list.|
N~Habitat differences are a good reason to expect different species.|
N~Keep watching. One place does not show you everything.|
S~That makes the next stretch feel a little more interesting.|
S~A change of scenery can give the team a whole new set of introductions.|
S~The familiar woodland cast is not the entire production.|
S~The world gets stranger the farther you walk from your first answer.|
S~New environment, new observations. Worth adjusting expectations.|
S~The trees end, but the creatures do not.|
S~A useful reminder to look up from what we already recognize.|
S~I wonder which new Pokemon made him notice the difference.
''')
add('r3_pc_capacity','Route3_Text_BenPostBattle',
    'Ben describes Pokemon Center PC storage and thirty-Pokemon boxes.','''
N~Thirty Pokemon make a very busy attendance sheet.|
N~Clear capacity limits make it easier to organize a growing collection.|
N~Keep the records straight. Every partner needs a place.|
N~It is useful to know how the boxes are arranged before they fill up.|
N~Organization saves a lot of searching later.|
N~A practical aside from the department of increasingly crowded collections.|
N~A small label can become important when many familiar faces gather.|
S~Known capacity, distinct boxes. Sensible storage planning.|
N~Names need somewhere orderly to wait in the records.|
N~A little organization is kinder to the future version of yourself.|
N~I wonder how he chooses which Pokemon to group together.
''')
add('r3_janice','Route3_Text_JanicePostBattle',
    'Janice warns that staring at trainers invites battles.','''
N~Eye contact has more paperwork out here than I expected.|
N~She is describing a local convention rather than a universal meaning of looking.|
N~Looking around is not a crime. Still worth knowing what people expect.|
F~That makes an already awkward moment considerably more complicated.|
N~A clear challenge would be easier on everybody than guessing from a glance.|
M~A roadside glance apparently comes with contractual obligations.|
N~An unfortunate rule for anyone whose thoughts drift while their eyes stay open.|
N~Ambiguous input, dramatic response. Poor interface.|
N~A gaze can wander farther than the intention behind it.|
N~She could ask whether someone wants a battle before deciding for them.|
N~I wonder how many accidental challenges begin with someone simply being lost.
''')
add('r3_greg','Route3_Text_GregPostBattle',
    'Greg advises changing boxes when a PC box is full.','''
N~A full box is a sign to use another box. Pleasantly solvable problem.|
N~Using another available box preserves the organization without exceeding capacity.|
N~Check space before it becomes urgent.|
N~A simple reminder can still save an awkward moment later.|
N~Good to keep track of where the next arrival can go.|
N~A storage crisis resolved by the existence of additional storage.|
N~Some problems are mercifully shaped exactly like their answers.|
S~Capacity reached? Select another container. Excellent straightforward system.|
N~Even a careful collection needs an empty corner left somewhere.|
N~Useful advice for a person who keeps postponing the sorting.|
N~I wonder how often he has had to reorganize his own collection.
''')
add('r3_sally','Route3_Text_SallyPostBattle',
    'Sally explains that avoiding trainers\' sight can avoid battles.','''
N~The grass has become a very informal appointments system.|
N~Avoiding a trainer's line of sight can change whether an encounter begins.|
N~Useful when the team needs a quiet route through.|
S~It is good to know you can choose a little space.|
N~Sometimes getting everyone to town comfortably is the best plan.|
M~The great tactical art of declining the audience before it notices you.|
S~A quiet path is still a legitimate path.|
N~Observe the sight lines, choose the route. Straightforward navigation.|
S~A small turn can leave an entire conversation asleep.|
N~A practical option when you are dressed for a walk rather than a challenge.|
N~I wonder whether she learned that by trying to get home unnoticed.
''')
add('r3_calvin','Route3_Text_CalvinPostBattle',
    'Calvin insists on wearing shorts even in winter.','''
M~His knees have signed a very demanding loyalty agreement.|
N~A consistent preference need not suit every temperature equally well.|
N~His choice. Bring a warmer option when the weather turns.|
N~I admire the certainty, though my legs disagree with the policy.|
N~A favorite outfit is good. Being comfortable in the cold is also good.|
M~A constitutional commitment to exposed shins, upheld through all seasons.|
M~Winter has submitted an objection and been ignored.|
N~A fixed configuration in a variable environment. Bold maintenance choice.|
N~The season changes. His knees remain unconvinced.|
M~Signature style is one thing. Freezing for consistency seems excessive.|
S~I wonder how long he has defended that rule.
''')
add('r3_james','Route3_Text_JamesPostBattle',
    'James says trained Pokemon are stronger than wild ones.','''
N~Practice helps, though the wild ones have been practicing their own things.|
N~Training can improve battle performance. Wild Pokemon still vary considerably.|
N~Never underestimate an opponent just because it is wild.|
N~Having a trainer can help, when the trainer pays attention.|
N~Care and steady practice can make a difference. It is still work.|
N~A broad claim that may meet a very specific exception in the next patch of grass.|
N~The wild has its own lessons, even if nobody awards badges for them.|
N~Structured training is an advantage, not a guarantee.|
N~A creature raised by the road may know things a sheltered one does not.|
N~Training matters. So does respecting what is already in front of you.|
N~I wonder what he has noticed changing in his own team.
''')
add('r3_robin','Route3_Text_RobinPostBattle',
    'Robin points out Route4 at the foot of Mt. Moon.','''
S~Another road, one mountain closer. Our shoes are making progress.|
N~A useful landmark for keeping track of the next section.|
N~Good. We know where the route leads.|
S~A clear direction makes the mountain feel less distant.|
N~Worth checking supplies before the next part of the walk.|
S~A concise preview of the next setting on our itinerary.|
S~The mountain has stopped being background and started becoming a destination.|
N~Map and local description agree. Reassuring.|
S~The road is beginning to gather itself toward the mountain.|
N~Simple directions are particularly welcome after a battle.|
S~I wonder what the mountain looks like when we are right beneath it.
''')
add('r4_crissy','Route4_Text_CrissyPostBattle',
    'Crissy thinks she has collected all the mushrooms in this spot.','''
N~A thorough search. The mushrooms may appreciate a chance to catch up.|
N~If the patch is depleted, moving on allows it time to recover.|
N~Leave the place some time. No point picking it bare again.|
N~She sounds pleased with the search, though there may be nothing left to find.|
N~A good harvest is also a reason to let the patch rest.|
M~The local mushroom chapter has reached a rather comprehensive conclusion.|
N~A little empty patch where yesterday had hidden several small surprises.|
N~Supply exhausted. Continued searching has diminishing returns.|
N~The ground needs time to grow its little umbrellas again.|
N~Knowing when to stop collecting is part of being good at it.|
N~I wonder whether she knows which spots grow back first.
''')
add('r6_whispers','Route6_Text_RickyPostBattle Route6_Text_NancyPostBattle',
    'Ricky or Nancy turns back to their private whispered conversation.','''
N~Their conversation has returned to its previously scheduled whispering.|
N~They appear to prefer speaking privately. We need not infer the subject.|
N~Private conversation. Leave them to it.|
F~I would rather not stand close enough to overhear.|
N~No need to interrupt them again. We can move on.|
M~Our guest appearance has ended; the confidential subplot resumes.|
N~The words are not for us. That is enough to know.|
N~Low-volume communication. Respecting the intended audience seems wise.|
N~A little pocket of words closed around two people.|
N~They have made it clear who is included in the conversation.|
N~I wonder nothing aloud. That seems the polite option here.
''')
add('r6_keigo','Route6_Text_KeigoPostBattle',
    'Keigo decides to return to Viridian Forest because he likes bugs.','''
S~He knows where his favorite neighbors live. Good reason to visit.|
S~Returning to a familiar habitat can deepen an existing interest.|
S~Go where you enjoy being. Plenty left to learn there.|
S~It is nice to hear someone choose a place because it makes them happy.|
S~A familiar outing can be every bit as worthwhile as a new one.|
S~The forest retains a devoted returning audience.|
S~A person can go back without going backward.|
S~Same place, more experience, new things to notice. Excellent.|
S~The trees still have little lives waiting under their leaves.|
S~A clear favorite makes planning a good afternoon simple.|
S~I wonder which bug he most hopes to find again.
''')
add('r6_jeff','Route6_Text_JeffPostBattle',
    'Jeff thinks bringing more Pokemon would help him feel safer.','''
N~A bigger support group can help. It still needs a sensible plan.|
N~More partners provide options, though their condition and preparation matter too.|
N~Backup helps. Make sure everyone is ready to be there.|
N~It is understandable to want a little more company on the road.|
N~A team that shares the work can make the journey easier for everybody.|
N~The expedition proposes enlarging its cast before the next challenge.|
S~Being less alone can change how a road feels.|
N~Redundancy helps, provided the backups are actually prepared.|
N~A few more footsteps beside yours can steady the path.|
N~Numbers help most when each partner has a useful place in the plan.|
N~I wonder what made him feel least secure during that battle.
''')
add('r6_isabelle','Route6_Text_IsabellePostBattle',
    'Isabelle asks for the secret to becoming stronger.','''
S~The secret is disappointingly full of practice and paying attention.|
N~Progress usually comes from several ordinary habits rather than one hidden trick.|
N~Know your team. Practice. Rest. Adjust when something fails.|
S~Asking what she can learn is already a good beginning.|
S~Care, patience, and a plan you can keep doing. Not glamorous, but useful.|
S~The grand secret appears to be several small unglamorous chapters in succession.|
S~There may be no secret door. Just a path people kept walking.|
N~Observe, test, revise. Repeat more patiently than seems exciting.|
S~Small things done faithfully can become a large change.|
N~She might learn more from one specific question than one enormous secret.|
S~I would ask which part of getting stronger she finds hardest.
''')
add('r6_elijah','Route6_Text_ElijahPostBattle',
    'Elijah asks whether his Pokemon are weak or he is a bad trainer.','''
N~That question has two gloomy doors and has forgotten the window marked learning.|
N~The choice is falsely limited. Matchups, decisions, experience, and chance all contribute.|
N~Neither label helps. Look at what happened and change one thing.|
D~A loss can make the questions about yourself much crueler than they need to be.|
N~He and the team can improve without deciding somebody is the problem.|
N~A harsh little questionnaire with no useful answer offered.|
N~He could ask what went wrong instead of who is wrong.|
N~Bad diagnostic categories. We need observations before conclusions.|
N~One difficult moment need not become a name you carry.|
N~He is allowed to be disappointed without insulting himself or his partners.|
N~I wonder whether anyone has helped him find a specific next step.
''')
add('r8_aidan','Route8_Text_AidanPostBattle',
    'Aidan says he performs better at school than in Pokemon battles.','''
S~Good. A bad battle has not erased the rest of his report card.|
N~Skills do not transfer uniformly between very different activities.|
S~Everybody has strengths. He can practice this one separately.|
S~It helps to remember something you do well after a hard moment.|
S~A loss does not get to judge every other part of your day.|
S~The roadside result has been appealed to a more favorable academic record.|
S~A different room can reveal a different kind of competence.|
N~Different task, different skill set. Entirely plausible.|
S~He has another place where the answers come more easily.|
S~A little pride can survive without pretending the loss went well.|
S~I wonder which school subject makes him feel most confident.
''')
add('r8_stan','Route8_Text_StanPostBattle',
    'Stan accepts that his plans did not work today.','''
N~A compact review. Tomorrow can have a revised plan.|
N~A failed attempt is useful if he examines which part failed.|
N~Some days go that way. Rest, then take another look.|
S~He is disappointed without making it sound like the end of everything.|
N~A little time can make the next change easier to see.|
N~The day's production has received a brief but honest review.|
N~A bad day can remain one day if you let it.|
N~Result acknowledged. Next step is finding the cause.|
N~The plan can be folded up and opened differently tomorrow.|
N~There is dignity in accepting that something simply did not work.|
N~I wonder what he would try differently next time.
''')
add('r8_glenn','Route8_Text_GlennPostBattle',
    'Glenn struggles to finish planning what comes after leading with Grimer.','''
N~He has step one. The rest of the staircase is still under construction.|
N~A battle plan needs contingencies beyond the opening choice.|
N~Good start. Need a plan for what the other side does too.|
N~It is hard to think clearly when you are still replaying the loss.|
N~A short break might help him sort the next step.|
M~The opening line is ready; the rest of the script has become ellipses.|
N~The thought has found a comfortable place to stop halfway.|
N~Initial state specified. Transition logic currently missing.|
N~A path that begins firmly can still disappear after the first bend.|
N~He is trying to work it out. That is better than a convenient excuse.|
N~I wonder what kept interrupting his plan during the battle.
''')
add('r8_paige','Route8_Text_PaigePostBattle',
    'Paige dislikes the appearance of evolved Pokemon and thinks they should not evolve.','''
N~Growing up should not require winning somebody else's cuteness contest.|
N~Aesthetic preference does not determine what change is right for a Pokemon.|
N~Let the partner matter more than the look she prefers.|
N~It would hurt to hear affection had a deadline.|
N~The same companion still deserves care when its appearance changes.|
N~The critic would like biology to submit all revisions for visual approval.|
N~A creature is allowed to become something inconvenient to someone's taste.|
N~Appearance is one variable. Function and the partner's needs also count.|
N~A living thing need not stay small to keep its place beside you.|
N~Preferring a design is fine. Making affection conditional is another matter.|
N~I wonder whether she has met an evolved Pokemon closely enough to know its personality.
''')
add('r8_leslie','Route8_Text_LesliePostBattle',
    'Leslie wanted fresh air but is frustrated by the closed Saffron gates.','''
N~The fresh air arrived. The freedom to go anywhere did not.|
N~A closed transit route can turn a simple outing into a logistical problem.|
N~Frustrating. Check the alternatives before taking a long detour.|
N~It is disappointing when a small plan becomes difficult for no reason you can change.|
N~A quiet break here might salvage part of the outing.|
N~The modest quest for fresh air has encountered municipal resistance.|
N~A blocked gate can make a wide world feel oddly cramped.|
N~Access restriction. The route plan needs a current alternative.|
N~Even open sky can feel smaller beside a closed way through.|
N~She asked very little of the day. No wonder she is annoyed.|
N~I wonder how many other travelers have been stopped there today.
''')
add('r8_andrea','Route8_Text_AndreaPostBattle',
    'Andrea says she finds common Pidgey and Rattata cute too.','''
S~The everyday neighbors deserve a fan club too.|
S~Being common does not make a species less worthy of interest.|
S~Nothing wrong with liking the partners everyone walks past.|
S~I like that she notices the familiar ones kindly.|
S~There is plenty to enjoy without finding the rarest thing on the route.|
S~A defense of the supporting cast that appears on every road.|
S~Ordinary little creatures still have their own quiet charm.|
S~Availability and appeal are entirely separate properties.|
S~A common visitor can still be a small delight.|
S~Popular taste forgets how lovely familiar things can be.|
S~I wonder what little habit of theirs she likes best.
''')
add('r8_megan','Route8_Text_MeganPostBattle',
    'Megan understands the gatekeeper has a job but finds his refusal unkind.','''
N~Knowing why a gate is shut does not make your feet less tired.|
N~A role can explain behavior without making the resulting inconvenience pleasant.|
N~She can understand the job and still dislike being stuck.|
N~That is a fair feeling. Explanations do not always make disappointment smaller.|
N~A gentler explanation at the gate might help, even if the answer stays no.|
N~A reasonable grievance with a surprisingly balanced acknowledgment attached.|
N~Both things can be true: a job to do, and an unpleasant afternoon.|
N~A restriction can be valid and the experience badly handled.|
N~A closed door still feels closed after you learn who holds the key.|
N~She has left room for his side while explaining her own.|
N~I wonder whether he told the waiting travelers anything useful.
''')
add('r8_rich','Route8_Text_RichPostBattle',
    'Rich compares his inability to stop playing games to eating peanuts.','''
M~Peanuts have a similar habit of turning one more into an empty bowl.|
N~Enjoyable repeated rewards can make stopping harder than intended.|
N~Set a limit before starting. Easier than negotiating with one more.|
N~It sounds fun until you realize the whole afternoon disappeared.|
M~A small bowl is the cook's answer to that particular problem.|
M~The humble peanut has been summoned as an expert witness for poor restraint.|
N~A tiny pleasure can become an oddly determined little loop.|
N~A stopping condition helps before the loop becomes the whole program.|
N~One more can be a small door into a very long room.|
N~A little enjoyment keeps better when you can choose to stop.|
N~I wonder whether he notices when playing stops feeling like a choice.
''')
add('r8_julia','Route8_Text_JuliaPostBattle',
    'Julia asks whether a journal report about Clefairy evolving with a Moon Stone is true.','''
S~A moon-named stone for a moon-named friend. Suspiciously tidy, but worth checking.|
S~She has a specific claim and an identified source. Good starting point for verification.|
N~Worth confirming before using a rare stone.|
S~I like that reading made her curious instead of merely certain.|
N~A reliable answer would help her decide without wasting anything.|
S~A printed claim has escaped the page and become a proper question.|
S~The journal has left her with a little lunar mystery.|
S~Source named, hypothesis clear. Now find a reliable confirmation.|
S~Some stones carry a stranger invitation than their shape suggests.|
S~She remembers where she read it. A useful habit.|
S~I wonder whether she knows someone with a Clefairy who could tell her more.
''')
add('r8_eli','Route8_Text_EliPostBattle',
    'Eli recalls catching his Pokemon together with Anne.','''
S~The team began with company. That is a nice memory to carry.|
S~A shared encounter can give both trainers a lasting point of connection.|
S~Good to have someone there for the beginning.|
S~He remembers who was beside him as well as what he caught.|
S~A day outside becomes more memorable when you share the surprise.|
S~The team's origin story has a recurring guest star.|
S~A small meeting can tie several lives to the same afternoon.|
S~Shared field experience! Useful backup and a better story afterward.|
S~Some beginnings are remembered in more than one pair of eyes.|
S~He sounds proud that they did it together.|
S~I wonder whether they remember the same little details of that day.
''')
add('r8_anne','Route8_Text_AnnePostBattle',
    'Anne says she and Eli are raising Pokemon together.','''
S~Catching together was the opening. The daily work is the longer adventure.|
S~Shared training can provide mutual feedback if responsibilities remain clear.|
S~Good. Make sure both get a say in how it is done.|
S~It is nice that the companionship continued after the exciting first day.|
S~Taking turns with the everyday work can make it much easier to keep doing.|
S~The partnership has continued beyond the charming first chapter.|
S~Affection has found itself a routine. That can be a very good thing.|
S~Ongoing collaboration beats a one-time burst of enthusiasm.|
S~A shared beginning has grown into shared ordinary days.|
S~Doing the work together says more than a matching story.|
S~I wonder what each of them brings to the way they train.
''')
add('r8_ricardo','Route8_Text_RicardoPostBattle',
    'Ricardo complains about grass tangled in his bicycle spokes.','''
N~The lawn has attempted to join the bicycle. Poorly.|
N~Debris in the spokes should be cleared before it impedes the wheel further.|
N~Stop and clear it. Do not reach in while the wheel moves.|
N~An annoying little problem can make the whole ride feel wrong.|
N~Better a short stop now than a damaged bike later.|
M~A modest encounter between nature and machinery has produced an unwanted collaboration.|
N~The grass has found an unusually loud way to travel.|
N~Foreign material in a moving assembly. Fix that before riding.|
N~The roadside has caught a little hold of his journey.|
N~A good reason to check the bike before the next long stretch.|
N~I wonder where he rode that let it wrap around so thoroughly.
''')
add('r8_jaren','Route8_Text_JarenPostBattle',
    'Jaren warns us not to feel special because we beat him.','''
N~We can be pleased without commissioning a statue.|
N~One result does not establish general superiority. Nor does it need to.|
N~The team earned the win. That is enough for today.|
N~It is possible to be happy without trying to make someone else smaller.|
N~We can give the team credit and let the rest go.|
M~The celebration committee has received a preventative complaint.|
N~He is defending against a boast we have not actually made.|
N~A modest result is still a result. No extra claims required.|
N~A small bright moment need not become a crown.|
N~He could let us enjoy the match without inventing an attitude for us.|
N~I wonder whether he expects every winner to gloat.
''')
add('r9_alicia','Route9_Text_AliciaPostBattle',
    'Alicia warns that Rock Tunnel is dark and recommends Flash.','''
N~A tunnel that supplies its own darkness. We should supply the opposite.|
N~Visibility is a practical preparation issue, not merely an inconvenience.|
N~Get ready before entering. Do not stumble in hoping it improves.|
N~I am glad someone told us before the light disappeared behind us.|
N~A little preparation saves a much more frightening trip.|
N~The next location comes with a clear lighting requirement. Useful warning.|
N~Darkness is prettier when you are not trying to find the floor in it.|
N~Check illumination before starting the underground section. Basic but important.|
N~A little light can make a very large dark place less demanding.|
N~That is the kind of local advice worth stopping to hear.|
N~I wonder which parts of the tunnel are hardest to navigate.
''')
add('r9_chris','Route9_Text_ChrisPostBattle',
    'Chris curtly tells us to keep walking.','''
N~Our departure has enthusiastic local support.|
N~He is not inviting further conversation. We can continue along the route.|
N~We are moving. No argument needed.|
N~That seems like a good place to end the exchange.|
N~Best let the afternoon get quieter for both sides.|
N~A travel recommendation reduced to its sternest possible form.|
N~An economical exit line. I can respect the brevity more than the tone.|
N~Forward movement requested. Conveniently, that was already the plan.|
N~The road has become more welcoming than the conversation.|
N~He could ask more politely. We can still take the hint.|
N~I wonder whether losing usually leaves him this short of words.
''')
add('r9_drew','Route9_Text_DrewPostBattle',
    'Drew asks whether we are also heading toward Rock Tunnel.','''
S~A fellow traveler! The mountain has been attracting a little crowd.|
N~Comparing destinations may provide useful information about the route ahead.|
N~Worth comparing notes before entering a dark tunnel.|
S~A shared destination makes a stranger feel a little less unfamiliar.|
N~We should both make sure the team is ready before the next stretch.|
S~The road has supplied a traveler with a matching next chapter.|
S~It is comforting to know somebody else is looking toward the same dark entrance.|
S~Same destination, potentially useful preparation notes. Good question.|
S~Two journeys can briefly point toward the same opening in the rock.|
S~A natural question to ask someone walking the same road.|
S~I wonder whether he has been through before.
''')
add('r9_caitlin','Route9_Text_CaitlinPostBattle',
    'Caitlin praises our talent and wishes us luck.','''
S~A kind send-off. That travels better than another complaint.|
S~A gracious acknowledgment of the team's performance.|
S~Good of her. The team worked for that.|
S~It is nice to leave someone feeling encouraged instead of awkward.|
S~A little kindness can improve a long stretch of road.|
S~The encounter closes with a generous review and no hidden sting.|
S~A small good word, offered without demanding anything back.|
S~Useful positive feedback. Far nicer than a vague excuse.|
S~She has left a little warmth on the road behind us.|
S~Losing gracefully looks good on her.|
S~I wonder whether she knows how welcome that encouragement is.
''')
add('r9_jeremy','Route9_Text_JeremyPostBattle',
    'Jeremy acknowledges our nerve in challenging him.','''
S~We have apparently passed the test of not running away immediately.|
N~He seems to value the willingness to face a difficult opponent.|
N~We stood our ground. No need to make more of it.|
S~He sounds less intimidating now that he is giving us credit.|
N~Courage counts more when it comes with knowing your limits.|
M~The imposing opponent has awarded us a favorable review for appearing at all.|
N~Being nervous does not make showing up any less real.|
N~Challenge accepted, outcome recorded. Courage was one input, not the whole plan.|
S~Sometimes steadiness is simply deciding not to take the first step backward.|
N~A compliment with a little swagger still attached.|
N~I wonder whether he was testing our confidence as much as our team.
''')
add('r9_brice','Route9_Text_BricePostBattle',
    'Brice laughs and says children should be tough.','''
N~Tough is useful. So are dry socks and knowing when to sit down.|
N~Resilience develops best with support and manageable challenges.|
N~Kids deserve backup, not just a demand to toughen up.|
N~I hope he means helping them feel capable rather than hiding when they hurt.|
N~Strength grows better with care than with being told to stop complaining.|
N~A hearty endorsement that could use a little more instruction attached.|
N~Small people need room to be soft as well as strong.|
N~Build capability gradually. Excess load is not an educational method.|
N~A sapling becomes strong without being asked to bear a roof.|
N~Encouragement lands better when it leaves room for being a child.|
N~I wonder how he helps a nervous beginner find confidence.
''')
add('r9_brent','Route9_Text_BrentPostBattle',
    'Brent considers catching Pokemon beyond bugs to make his team stronger.','''
S~He can try new neighbors without evicting the bugs from his heart.|
N~A wider type selection may cover weaknesses while preserving his existing interests.|
N~Add options. No need to stop valuing the team he has.|
S~Trying something different does not have to make the old favorite less special.|
N~A new partner should have a place beside the others, not arrive as an insult to them.|
S~The specialist considers expanding the cast without abandoning the original production.|
S~An interest can grow a new branch without losing its roots.|
N~Broader coverage could help. Check what role the addition should fill.|
S~A garden can welcome another kind of visitor.|
S~He is allowed to broaden his taste without apologizing for loving bugs.|
S~I wonder which other kind of Pokemon first caught his attention.
''')
add('r9_alan','Route9_Text_AlanPostBattle',
    'Alan says hearty people like him always laugh.','''
M~A very cheerful rule. His lungs seem committed to enforcing it.|
N~Humor can express resilience, though it need not be everyone's response.|
S~If laughing helps him shake off the loss, fair enough.|
N~I like the good mood. I would not want to have to perform it all the time.|
S~A laugh can make a tiring day easier to share.|
M~The local school of heartiness apparently requires a substantial vocal exercise.|
M~A confident claim from a man doing his own sound effects.|
N~Positive recovery strategy. Optional volume control would be useful.|
S~He carries his good weather where everyone can hear it.|
S~A big personality can be quite welcoming when it leaves room for others.|
S~I wonder whether anyone nearby can recognize his laugh before seeing him.
''')
add('r9_conner','Route9_Text_ConnerPostBattle',
    'Conner gets defensive about whether we like Bug Pokemon.','''
N~The bugs do not need us to have matching favorites to deserve respect.|
N~Preference and respectful treatment are separate matters.|
N~Nobody needs to insult what he likes. Nobody needs to like it all the same.|
N~He sounds ready to defend something that matters to him.|
N~There is room for different favorites without turning it into a fight.|
N~An imagined critical review has upset the entire insect appreciation society.|
N~Being used to mockery can make even a neutral room sound hostile.|
N~Disagreement about preference need not become a compatibility failure.|
N~A small creature can occupy a large place in someone's affections.|
N~He can love bugs without asking every passerby to prove the same thing.|
N~I wonder whether people have made fun of his team before.
''')
add('r10_mark','Route10_Text_MarkPostBattle',
    'Mark boasts about more rare Pokemon waiting at home.','''
M~The reserve collection has entered the argument from a considerable distance.|
N~An unseen collection does not change the evidence of this particular battle.|
N~Good for him. The partners here still deserve his attention.|
N~It sounds like he wants us to know there is more to him than this loss.|
N~I hope he is proud of the Pokemon beside him too.|
M~The defeated cast would like us to know the absent cast is exceptionally impressive.|
N~A distant collection is a comfortable place to store an undefeated reputation.|
N~Interesting claim, unavailable for inspection. Not relevant to the current result.|
N~The rare companions at home do not erase the familiar ones here.|
N~He does not have to inventory his whole life to earn respect.|
N~I wonder which partner he chooses when rarity is not the deciding factor.
''')
add('r10_clark','Route10_Text_ClarkPostBattle',
    'Clark sneezes repeatedly after the battle.','''
N~The conversation has been interrupted by his entire nose. Bless him.|
N~Repeated sneezing makes a pause more useful than further questions.|
N~Give him a moment. And a little room.|
N~Poor thing. It is hard to talk when your own face keeps interrupting.|
N~A tissue and a quiet pause would help more than another question.|
N~An involuntary series of emphatic remarks from the nasal department.|
N~A very small catastrophe, happening several times in a row.|
N~Speech channel temporarily unavailable. Wait for the sneezing to stop.|
N~The mountain air has apparently started an argument with him.|
N~We should let him recover before trying to continue.|
N~I wonder whether something growing here sets him off.
''')
add('r10_herman','Route10_Text_HermanPostBattle',
    'Herman says he dislikes anyone better than himself.','''
N~That is a very efficient way to run out of pleasant acquaintances.|
N~Comparative ability is a poor basis for deciding whether to like someone.|
N~His problem to work on. We are not shrinking the team for him.|
N~It must make learning from people rather lonely.|
N~Someone doing well does not have to take anything away from him.|
N~A social policy guaranteed to make improvement awkward for everyone.|
N~An exhausting rule to carry through a world full of other people.|
N~Rejecting better examples removes a useful source of information.|
N~Someone else's height need not make the ground beneath you lower.|
N~He has mistaken admiration for a threat. That will get tiring.|
N~I wonder whether he has anyone he lets himself look up to.
''')
add('r10_heidi','Route10_Text_HeidiPostBattle',
    'Heidi is surprised to see Pokemaniacs in the mountains.','''
N~Interesting Pokemon live here. That seems like a fairly strong explanation.|
N~A mountain habitat would plausibly attract people interested in unusual species.|
N~Public mountain. Plenty of room for different sorts of travelers.|
N~They may simply enjoy being here as much as she does.|
N~A shared interest can bring together people who do not look much alike.|
N~The mountains have failed to enforce her imagined guest list.|
N~Strange clothes do not make a person incompatible with fresh air.|
N~Specialists go where the interesting observations are. Perfectly logical.|
N~The mountain does not inspect a visitor's taste before letting them climb.|
N~An unusual look is not a reason somebody should stay indoors.|
N~I wonder whether she has actually spoken to any of them.
''')
add('r10_trent','Route10_Text_TrentPostBattle',
    'Trent describes feeling full of mountain air.','''
M~An unusual lunch choice. At least the mountain serves generous portions.|
N~That is an expressive description, though not a precise physiological one.|
N~Take a breather. Preferably without trying to swallow the whole mountain.|
N~I think he means the air feels different up here.|
M~Air is a very light meal. I would still suggest something solid later.|
M~The mountain has catered the occasion with an apparently overgenerous atmosphere.|
M~A man briefly overfilled by the outdoors. It happens.|
N~I would need a more specific symptom before diagnosing excessive scenery.|
N~Perhaps the mountain feels larger on the inside of a breath.|
N~A memorable way to describe a day outside, certainly.|
N~I wonder whether he always feels that way after climbing.
''')
add('r10_carol','Route10_Text_CarolPostBattle',
    'Carol wishes the mountain had a pink Pokemon with a floral pattern.','''
S~A very specific request for the local wildlife department.|
N~Her preferred color and pattern need not match the species adapted to this habitat.|
N~The mountain's residents do not choose their looks for visitors.|
S~It is a sweet image, even if this is not where she will find it.|
N~She can have a favorite look without calling the others wrong.|
M~The mountain has received a detailed commission for a softer visual theme.|
S~An oddly delicate wish among all this heavy stone.|
N~Clear design brief. The habitat has not agreed to manufacture it.|
S~A little imagined garden walking around on its own feet.|
S~Pink with flowers is a whole aesthetic. She has considered this.|
S~I wonder whether she has seen one somewhere or imagined it entirely.
''')
add('deleter_success','FuchsiaCity_House3_Text_MonHasForgottenMoveCompletely',
    'The Move Deleter confirms the selected move was successfully forgotten.','''
N~A very tidy disappearance. Now there is room for a different answer.|
N~The requested move was removed. The available options have changed accordingly.|
N~Done. Remember the team now has one less option until we teach another.|
N~That is a strange kind of relief, making room by letting something go.|
N~Good to have the choice settled before the next battle.|
N~An old line has been removed from the repertoire at our express request.|
N~Some endings are useful precisely because they leave an empty place.|
N~Configuration updated. Worth checking the remaining moves before heading out.|
N~A small silence where a familiar action used to live.|
N~A deliberate change looks better than endlessly carrying a choice that no longer suits.|
N~I wonder what new role the partner will take on now.
''')
add('deleter_one_move','FuchsiaCity_House3_Text_MonOnlyKnowsOneMove',
    'The Move Deleter refuses to remove a Pokemon\'s only move.','''
N~He draws the line at leaving a partner with absolutely no lines. Sensible.|
N~Preserving at least one move prevents removing the Pokemon's entire usable repertoire.|
N~Keep one option. That is a reasonable limit.|
N~I am glad he stops rather than simply doing whatever we ask.|
N~Better to learn another choice before losing the only one.|
N~The editor declines to publish a completely blank battle plan.|
N~An empty space is less helpful when it is the whole page.|
N~Minimum functional configuration protected. Excellent safeguard.|
N~A door should remain when the other ways are being closed.|
N~A professional who knows when to refuse is worth trusting.|
N~That limit makes the service feel much more considered.
''')
add('deleter_egg','FuchsiaCity_House3_Text_NoEggShouldKnowMoves',
    'The Move Deleter cannot remove moves from an Egg.','''
M~The Egg has not begun its lessons, so canceling them is difficult.|
N~The requested operation does not apply to an Egg. A straightforward restriction.|
N~Wait until it hatches before planning a move change.|
N~We may be getting rather ahead of the little one.|
N~There will be time for decisions after it arrives.|
M~An unborn performer cannot yet submit revisions to the repertoire.|
S~A small life has been granted a little peace from administration.|
N~Wrong input type. Better that the service catches it.|
S~Let it keep its quiet beginning a little longer.|
N~A fair answer. The Egg has other priorities just now.|
S~I wonder what its first real move will look like.
''')
add('deleter_cancel','FuchsiaCity_House3_Text_ComeAgainToForgetOtherMoves',
    'The Move Deleter ends the visit without deleting a move and invites another visit.','''
N~No change today. The forgetting appointment can wait.|
N~Canceling leaves the existing moves intact. We can reconsider later.|
N~No need to change something before we are sure.|
S~It is nice to be able to leave without making a decision.|
N~A little more thought now can save regret later.|
N~The proposed edit has been set aside, with the original preserved.|
S~Some things can remain exactly where they are for another day.|
N~Operation canceled cleanly. Good, predictable behavior.|
S~The familiar answer can stay until a different one is ready.|
N~He accepted the hesitation without making it awkward.|
N~I wonder how often trainers come back after thinking it through.
''')
add('warden_strength','FuchsiaCity_WardensHouse_Text_ExplainStrength',
    'After his teeth are returned and HM04 given, the Warden explains Strength and asks about the Safari Secret House.','''
S~He can talk again, and the team can learn to move boulders. A productive reunion with teeth.|
S~The final explanation confirms a useful reward after resolving his communication trouble.|
S~Good to hear him clearly. The boulder-moving lesson is useful too.|
S~He sounds much more at ease now that people can understand him.|
S~We helped with something that had really embarrassed him. I am glad.|
S~A dental rescue concludes with a lesson in moving considerably larger obstacles.|
S~His voice has returned, and with it several useful directions.|
S~Communication restored, new capability explained. Successful troubleshooting!|
S~A small lost thing returned, a large stone no longer quite so fixed.|
S~He is comfortable enough to chat again. That is the nicest part.|
S~I wonder how long he has wanted to ask visitors about that Secret House.
''')
add('saffron_letter','SaffronCity_House_Text_DontLookAtMyLetter',
    'A resident catches us reading a private letter and objects.','''
F~That letter was not addressed to our eyeballs. We should step back.|
N~Private correspondence requires permission. The objection is entirely reasonable.|
N~That is their private letter. Leave it alone.|
F~I would be upset too. We should give them some space.|
N~No need to know the rest. A private letter belongs to its reader.|
N~An accidental audience has been firmly dismissed from a personal scene.|
F~A page can feel like a room someone walked into without knocking.|
N~Access boundary clearly identified. Best respect it immediately.|
N~Some words are meant to travel to only one pair of hands.|
F~That was personal. Looking away promptly is the decent response.|
N~We learned enough to know we should not be reading it.
''')
add('saffron_copycat_gift','SaffronCity_House_Text_GettingCopycatPokeDoll',
    'A resident plans to give Copycat a Poke Doll.','''
S~A gift that matches something she actually likes. Good reconnaissance.|
S~The choice appears informed by the recipient's known interests.|
S~A thoughtful choice. No need to make it complicated.|
S~It is sweet when somebody remembers a small favorite.|
S~A little present can say you paid attention.|
S~The admirer has chosen a prop with unusually good evidence behind it.|
S~A soft little offering to someone with an odd little reputation.|
S~Requirements gathered before selecting the gift. Strong method.|
S~A small doll can carry a surprisingly clear message.|
S~Knowing her taste makes it feel personal rather than merely expensive.|
S~I wonder which doll they chose for her collection.
''')
add('saffron_ppup','SaffronCity_House_Text_ExplainPPUp',
    'A resident explains a gifted PP Up and considers using it on a low-PP powerful move.','''
N~A few extra uses of the right move can matter more than a much louder gift.|
N~A powerful move with limited uses is a reasonable candidate for a PP increase.|
N~Put it where the extra use actually helps.|
N~They have taken time to think about the gift instead of using it at once.|
N~A useful present deserves a choice that fits the team.|
N~A modest improvement to how often the dramatic line can be delivered.|
N~A little more staying power can change a difficult afternoon.|
N~Improve the bottleneck rather than a capacity you already have enough of.|
N~One more answer left when the long fight asks again.|
N~Thoughtful use makes a useful gift feel even better.|
N~I wonder which move they are considering.
''')
add('saffron_mrpsychic','SaffronCity_MrPsychicsHouse_Text_ExplainTM29',
    'After giving TM29, Mr. Psychic explains Psychic while assuming we already know.','''
M~He gave us the explanation and still credited us with having it already. Efficient flattery.|
N~The explanation is useful regardless of his assumption about our prior knowledge.|
N~A useful move. Glad he explained it even if he thinks we know everything.|
F~I would probably nod even if I had no idea. He sounds so certain.|
S~A clear explanation is part of a good gift, psychic or otherwise.|
M~The lesson arrives with a flattering claim that the audience is ahead of it.|
M~Knowing what people know must make conversation unusually repetitive.|
N~Documentation supplied despite presumed knowledge. Excellent support practice.|
N~He leaves very little space between a thought and his answer to it.|
S~A generous gift, delivered with a very distinctive manner.|
S~I wonder whether anyone ever surprises him by asking a question.
''')
add('saffron_mrpsychic_full','SaffronCity_MrPsychicsHouse_Text_YouveNoRoom',
    'Mr. Psychic cannot give the TM because the bag is full.','''
M~He saw the gift coming but apparently left bag management to us.|
N~The intended gift did not fit. Nothing has been successfully received.|
N~Make room first. He cannot solve that part for us.|
F~An awkward end to such a confident entrance.|
N~We can sort the bag and return without making this complicated.|
M~The psychic forecast has encountered a solid wall of luggage.|
M~The future is mysterious. The full bag is rather less so.|
N~Capacity check failed. Clear space before repeating the transaction.|
N~A thought can arrive where a physical object still cannot.|
N~A fair question, delivered with impressively little patience.|
N~I wonder how often his visitors arrive this unprepared for a gift.
''')
add('saffron_maxrepel','SaffronCity_Mart_Text_MaxRepelMoreEffectiveThanSuper',
    'A shopper explains that Max Repel lasts longer than Super Repel.','''
N~More walking between bottle checks. A useful kind of maximum.|
N~Duration is the relevant comparison here, rather than assuming every effect is stronger.|
N~Longer-lasting supplies help on a long route. Check the cost too.|
N~A clear comparison makes the choice less confusing.|
N~Match it to the walk instead of buying the grandest name automatically.|
M~The product hierarchy has reached Maximum and now has a duration to justify it.|
N~A little longer without interruptions can feel like a luxury.|
N~Longer operating time. Now compare the price per use.|
N~Some journeys need a longer quiet stretch between meetings.|
N~Useful distinction. The names alone make everything sound endlessly bigger.|
N~I wonder which long route made them compare the two.
''')
add('saffron_revive_cost','SaffronCity_Mart_Text_ReviveIsCostly',
    'A shopper weighs Revive\'s high price against helping a fainted Pokemon.','''
N~The useful shelf has found the expensive shelf. They do meet often.|
N~The cost is substantial, but so is the value of restoring a fainted partner.|
N~Keep a reserve if we can afford it. A long walk can turn costly fast.|
N~It is a difficult choice when a useful thing strains the budget.|
N~Plan for what the team needs before spending on extras.|
N~A price tag with an unusually persuasive argument printed beside it.|
N~Some purchases feel too dear until the moment you need them.|
N~Compare cost against the consequence of having none. Practical decision.|
N~A small reserve can hold the way out of a bad moment.|
N~A sensible concern. Useful does not make the money unlimited.|
N~I wonder how they decide what to carry on a long outing.
''')
add('saffron_growth','SaffronCity_PokemonCenter_1F_Text_GrowthRatesDifferBySpecies',
    'A visitor explains that Pokemon species grow at different rates.','''
S~The team does not have to use one shared calendar for getting stronger.|
N~Different growth curves make direct comparisons between species misleading.|
N~Train the partner in front of you. Do not punish it for someone else's pace.|
S~That is reassuring. Slow progress can still be real progress.|
N~A good routine has room for each partner's needs.|
S~The cast has declined to reach every milestone on the same page.|
S~Not every living thing keeps the same clock.|
N~Different inputs, different response curves. Adjust the plan accordingly.|
S~Some seeds take a little longer beneath the same sun.|
N~Useful advice before a trainer decides the quieter progress is failure.|
S~I wonder which partner made them notice the difference first.
''')
add('saffron_silph_fame','SaffronCity_PokemonCenter_1F_Text_SilphCoVictimOfFame',
    'A visitor believes Silph\'s fame attracted Team Rocket.','''
N~Being known for useful things should not come with uninvited criminals.|
N~A prominent company may attract opportunists. Responsibility still lies with the attackers.|
N~Rocket chose to hurt people. The company being well known is no excuse.|
N~It is frightening to think familiar workplaces can become targets.|
N~I hope the people working there can get somewhere safe.|
N~Success drew the wrong audience. That does not make the victims responsible for it.|
N~A bright name can attract something unpleasant from the dark.|
N~Visibility can expose valuable resources. Protect the people, not just the inventory.|
N~Something useful became a beacon to the wrong eyes.|
N~Fame explains attention. It does not justify what Rocket did with it.|
N~I wonder whether the visitor knows someone trapped inside.
''')
add('saffron_elitefour_wish','SaffronCity_PokemonCenter_1F_Text_GreatIfEliteFourCameBeatRockets',
    'A frightened visitor wishes the Elite Four would drive Team Rocket away.','''
N~It makes sense to wish the strongest people would show up when home feels unsafe.|
N~They are looking for capable help in a situation they cannot resolve alone.|
N~People need help now. They should not have to handle Rocket themselves.|
D~They sound tired of waiting to feel safe again.|
N~A city full of worried people deserves someone who takes the danger seriously.|
N~A hopeful rescue scene, imagined by someone tired of being in the audience.|
N~A wish for powerful strangers is sometimes a very ordinary wish for peace.|
N~Expert help would be welcome. The waiting is the hard part for everyone here.|
N~A frightened town listens for footsteps stronger than the ones threatening it.|
N~They want the people with influence to use it. Understandable.|
N~I wonder how long they have been hoping someone would come.
''')
add('saffron_safe_again','SaffronCity_PokemonCenter_1F_Text_TeamRocketTookOff',
    'The visitor celebrates being able to go outside safely after Team Rocket leaves.','''
S~A normal walk outside has become excellent news. I am glad they get it back.|
S~Restored safety changes ordinary daily movement in a very tangible way.|
S~Good. People should be able to use their own streets.|
S~You can hear the relief before anything else.|
S~A simple errand feels different when you no longer dread the road.|
S~The city's grand victory is also a thousand small journeys made ordinary again.|
S~The familiar street has stopped holding its breath.|
S~Basic access restored. The most important repairs can look very ordinary.|
S~Doors can open without quite so much listening first.|
S~Being able to go out without fear is worth celebrating plainly.|
S~I wonder which familiar place they wanted to visit first.
''')
add('copycat_parent_friends','SaffronCity_CopycatsHouse_1F_Text_DaughterIsSelfCentered',
    'Copycat\'s parent calls her self-centered and worries she has few friends.','''
N~Few friends is a circumstance, not a complete description of a person.|
N~Social isolation can have several causes. One parental judgment is incomplete evidence.|
N~Talk with her. Counting friends will not tell you what she needs.|
D~It hurts to be described that way in your own home.|
N~A little understanding might help more than another label.|
N~An entire personality has been summarized before the subject gets a line.|
N~Having few friends is not, by itself, a moral failure. Fortunately for me.|
N~We should inspect the situation before assigning a single cause.|
N~A quiet doorway does not tell you everything about the room beyond it.|
N~She might need somebody curious about her instead of disappointed in her.|
N~I wonder how she would describe the same problem.
''')
add('copycat_parent_mimic','SaffronCity_CopycatsHouse_1F_Text_DaughterLikesToMimicPeople',
    'A parent explains the origin of Copycat\'s nickname and finds her mimicry vexing.','''
N~A memorable talent can also be a lot to live beside at breakfast.|
N~Imitation may demonstrate close observation while still annoying its subjects.|
N~A talent needs boundaries when other people are involved.|
N~Being copied can feel strange, even when no harm was intended.|
N~They might get farther by explaining when it bothers them.|
N~A household has acquired a resident impersonator with no scheduled performances.|
N~The gift of noticing people can be irritatingly accurate.|
N~Clear boundaries would help more than repeatedly being surprised by the same behavior.|
N~An echo is charming until it lives across the dinner table.|
N~She has a real eye for people. Timing may still need work.|
N~I wonder whether anyone has asked what she enjoys about doing it.
''')

