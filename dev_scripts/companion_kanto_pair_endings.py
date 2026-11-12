"""Terminal paired-trainer eligibility replies and the departing Game Corner grunt."""
ROWS=[]
EMOTIONS=dict(N='neutral',S='soft_smile',A='annoyed',F='flustered',D='sad',U='surprised',M='smug',L='laughing')
def add(key,labels,subject,lines):
    replies=[]
    for line in lines.strip().split('|'):
        line=line.strip()
        if len(line)>1 and line[1]=='~' and line[0] in EMOTIONS:line=EMOTIONS[line[0]]+line[1:]
        replies.append(line)
    assert len(replies)==11,(key,len(replies))
    ROWS.append(dict(key='kanto_pair_end_'+key,labels=labels.split(),subject=subject,replies=replies))

add('r8_eli','Route8_Text_EliNotEnoughMons',
    'Eli explains that battling the pair requires two Pokemon.','''
S~Two opponents, two partners. The invitation has a headcount.|
N~He has stated the format clearly. A second eligible Pokemon is required.|
N~We can return with the right team if we want the battle.|
N~At least he explains the condition without making it personal.|
S~A little preparation, then we can decide whether to accept.|
S~The double act has a sensible minimum cast requirement.|
N~A postponed battle is not much of a tragedy.|
N~We need the right setup before testing a two-Pokemon strategy.|
N~The road remains open even when a challenge waits.|
N~A straightforward condition. No need to make an occasion of it.|
S~I wonder how differently those two plan when they battle together.
''')
add('r8_anne','Route8_Text_AnneNotEnoughMons',
    'Anne enthusiastically invites a battle but asks for two Pokemon first.','''
S~That welcome came with an exclamation mark and a small attendance rule.|
S~Her enthusiasm remains intact despite postponing the challenge.|
N~She can keep the invitation. We will choose when we are ready.|
S~She sounds pleased by the idea of a battle before it has even begun.|
S~Nice to have an invitation we can prepare for instead of rush into.|
S~An eager hostess whose only request is a complete guest list.|
S~That is quite a bright welcome for a battle we cannot start yet.|
S~We could use the time to consider how our two choices would work together.|
S~A cheerful challenge can wait at the roadside without turning sour.|
S~Her excitement makes the requirement sound like a future plan.|
S~I like seeing someone enjoy the prospect of meeting a new team.
''')
add('r12_gia','Route12_Text_GiaNotEnoughMons',
    'Gia refuses to battle without Jes and asks for another Pokemon.','''
S~Gia has decided her battle buddy is an essential piece of equipment.|
N~Her condition concerns the partnership rather than simply the number of opponents.|
N~She wants Jes beside her. We can respect that and come back prepared.|
S~She does not sound interested in proving she can do everything alone.|
S~A familiar partner can make a challenge something to look forward to.|
S~Gia has declined a solo engagement in favour of the established double act.|
N~There are worse things than being very clear about wanting company.|
S~Their coordination is part of what we would be challenging.|
S~She has chosen whose footsteps she wants beside hers.|
S~That is a very emphatic preference for sharing the spotlight.|
S~I wonder what Jes does in battle that makes her feel so certain.
''')
add('r12_jes','Route12_Text_JesNotEnoughMons',
    'Jes says he and Gia belong together and will only accept a paired battle.','''
S~Forever is a big promise. For now it apparently includes matching battle plans.|
N~Their personal commitment and preferred battle format seem closely connected.|
N~They have set the terms. No reason to press for a different fight.|
F~He says the together part with more feeling than the battle part.|
S~It is sweet when everyday plans make room for somebody important.|
S~The declaration of eternal devotion includes a practical clause about team size.|
S~A grand promise, followed by unusually clear scheduling information.|
N~A paired strategy needs a paired opponent. That part is simple enough.|
S~Forever is made of smaller choices, including who stands beside you today.|
S~He is not trying particularly hard to sound casual about Gia.|
S~I suspect he would enjoy introducing them as a pair even without the battle.
''')
add('r14_pair','Route14_Text_KiriNotEnoughMons Route14_Text_JanNotEnoughMons',
    'Kiri and Jan require two Pokemon before their paired battle can begin.','''
N~We have reached a challenge that needs another partner before it can get started.|
N~Both trainers require the same two-Pokemon format. The constraint is clear.|
N~No battle today unless we change the team. Simple enough.|
N~They are ready as a pair. We can decide whether to prepare for that.|
N~A little planning now will make the eventual match less awkward.|
N~The engagement is postponed until our side can fill both places.|
N~Nothing wrong with leaving an invitation unanswered for a while.|
N~We can think about combinations before returning with two eligible Pokemon.|
N~A road can offer something we choose to leave for later.|
N~Clear terms make a much better invitation than pressure does.|
S~I wonder whether they have practised together for a long time.
''')
add('r15_mya','Route15_Text_MyaNotEnoughMons',
    'Mya offers a challenge with a two-Pokemon requirement.','''
S~She is taking challengers, provided they arrive with both halves of a team.|
N~The invitation specifies a paired battle rather than an ordinary single match.|
N~We can choose our team before accepting her challenge.|
N~A brief explanation leaves us room to decide for ourselves.|
S~A challenge is easier to enjoy when everyone arrives prepared.|
S~Mya has issued a standing invitation with a modest admission condition.|
N~Her confidence can wait while we sort out the practical part.|
N~Two choices mean thinking about how they support each other.|
N~An unopened challenge can stay where we found it.|
N~I appreciate a requirement stated without a little speech about our worth.|
S~It would be interesting to see what she expects from a visiting pair.
''')
add('r15_ron','Route15_Text_RonNotEnoughMons',
    'Ron wants to battle alongside his sister and asks for two Pokemon.','''
S~A sibling team has all those years of arguing about whose turn it is to practise with.|
S~Familiarity may help coordination, though it does not replace planning.|
N~He wants his sister in the match. We need to prepare for both of them.|
S~I like that he introduces the partnership through who she is to him.|
S~A shared challenge gives them something new to talk about afterward.|
S~The family double act is accepting suitable opposition.|
S~Siblings do sometimes find a pleasant use for knowing each other too well.|
S~They may recognize each other's next move before a stranger would.|
S~A familiar voice can make a difficult moment feel less lonely.|
S~He sounds pleased to have something they do together.|
S~I wonder which of them first suggested becoming a battle pair.
''')
add('r16_jed','Route16_Text_JedNotEnoughMons',
    'Jed unfairly treats having one Pokemon as evidence of lacking love.','''
A~One Pokemon can get a whole lot of love. That is not how counting works.|
N~Party size is not a valid measure of affection. His inference is unsupported.|
A~He can ask for a double battle without insulting us.|
N~Having fewer companions does not mean caring less about the one beside you.|
N~The amount of care matters more than how many bowls are on the table.|
N~An eligibility check has taken an unwarranted turn into character criticism.|
N~A remarkably grand accusation to hang on a small headcount.|
N~That is the wrong measurement for the claim he is making.|
N~A single warm light does not make a house loveless.|
A~What an unnecessary little jab to dress up as a question.|
N~He knows how many Pokemon we brought, not how we treat them.
''')
add('r16_lea','Route16_Text_LeaNotEnoughMons',
    'Lea assumes a trainer with one Pokemon must feel lonely.','''
N~One friend is still a friend. Loneliness does not obey neat arithmetic.|
N~Companionship depends on the relationship, not simply the number present.|
N~She cannot tell whether we are lonely from the team count.|
N~Quiet company can feel very full to the people sharing it.|
N~A small table can still be a happy one.|
N~She has inferred the mood of the whole journey from a single number.|
N~Solitude and loneliness are not even reliably on speaking terms.|
N~A required team size tells us nothing useful about emotional satisfaction.|
N~A path with two sets of footsteps can hold plenty of company.|
N~Concern lands better when it leaves space for someone's actual answer.|
N~I would rather ask how the journey feels than decide from appearances.
''')
add('r19_lia','Route19_Text_LiaNotEnoughMons',
    'Lia wants her little brother beside her in a paired battle.','''
S~The big sister has reserved a place on her team for her little brother.|
S~She has identified the partnership as part of the experience she wants.|
S~She wants to include him. We can return with a suitable team.|
S~It is nice to hear an older sibling make room so plainly.|
S~A shared battle can become a good story for them both.|
S~The elder sibling has made the smaller role an essential one.|
S~He is not an extra she can be persuaded to leave behind.|
S~Their plan depends on working as a pair. We should prepare accordingly.|
S~A small hand has been given a steady place beside a larger one.|
S~She makes being his sister sound like something she enjoys.|
S~I wonder whether he likes the battle or being included best.
''')
add('r19_luc','Route19_Text_LucNotEnoughMons',
    'Luc will battle only if his big sister can participate.','''
S~Luc has picked his teammate and is sticking firmly to the choice.|
S~He values the shared activity enough to decline a different format.|
N~His sister is part of the deal. No reason to argue.|
S~Her being there may be what makes the challenge feel fun.|
S~A familiar person beside you can make a big difference to trying something.|
S~The younger member has vetoed any proposed solo appearance.|
S~A clear little boundary, stated without much ceremony.|
N~We need a second eligible Pokemon before their team can face ours.|
S~He knows which company makes the open water feel smaller.|
S~He is wonderfully definite about the person he wants beside him.|
S~I like seeing the little brother get a say in their plans.
''')
add('r21_lil','Route21_North_Text_LilNotEnoughMons',
    'Lil cannot be bothered with a solo battle and requests two Pokemon.','''
L~A very honest minimum level of effort has been posted at the entrance.|
N~She has a preference for paired battles and little interest in concealing it.|
N~Fair enough. We are free to keep walking, too.|
N~At least she does not pretend to be excited by a match she does not want.|
N~Some invitations come with very little garnish.|
S~The performer has declined the solo booking on grounds of insufficient enthusiasm.|
N~Bluntness has saved everyone a longer conversation.|
N~She wants the team format. We can prepare for it or pass.|
N~Her interest has a threshold, and we have found it.|
M~An impressively unpolished way to state a perfectly reasonable preference.|
S~I wonder what makes battling with her partner worth the bother.
''')
add('r21_ian','Route21_North_Text_IanNotEnoughMons',
    'Ian politely asks for two Pokemon to enable their preferred two-on-two battle.','''
S~He has the two-on-two plan ready. Our side needs a little more assembling.|
N~The requested format is explicit and the necessary preparation straightforward.|
N~A clear request. We can return when we want that kind of match.|
N~He leaves the choice with us instead of trying to make the delay awkward.|
S~It is pleasant when a challenge comes with polite instructions.|
S~A courteous invitation to complete the opposing half of the arrangement.|
N~A little civility survives even the desire to defeat strangers.|
N~We can choose a pair that actually works together before accepting.|
N~A waiting challenge need not tug at every traveller passing it.|
S~Good manners make even a refusal easier to receive.|
S~I wonder whether his calm approach carries into their teamwork.
''')
add('kindle_kia','OneIsland_KindleRoad_Text_KiaNotEnoughMons',
    'Kia explains the minimum of two Pokemon for challenging her pair.','''
N~Kia has supplied the rule before we get tangled up in trying the battle.|
N~Two eligible Pokemon are the practical prerequisite for this paired challenge.|
N~We know what to bring if we return.|
N~A direct explanation can be kinder than a long apologetic one.|
N~Best to prepare the team before making a promise to battle.|
N~The invitation remains open once the necessary partners arrive.|
N~A simple condition, with no need to turn it into a judgment.|
N~We should consider the pair as a unit when choosing our side.|
N~Not every encounter needs to become a contest immediately.|
N~She keeps the requirement clear without making us feel examined.|
S~I wonder how many travellers stop here hoping for a quick single battle.
''')
add('kindle_mik','OneIsland_KindleRoad_Text_MikNotEnoughMons',
    'Mik invites a challenge against both trainers after the player brings two Pokemon.','''
S~Mik is advertising the complete two-person package. No half-orders today.|
S~He emphasizes facing both trainers, so the team requirement follows naturally.|
N~If we want their challenge, we can come back ready for both.|
N~He sounds as though he will be happy to see us return.|
S~A future battle gives the next walk along this road something extra to offer.|
S~A return engagement has been proposed before the first could begin.|
S~An invitation can stay pleasant even when the answer is later.|
N~We have time to think through a coordinated opening rather than improvise one.|
S~The path has left a little unfinished business, if we want it.|
S~There is a friendly difference between come back prepared and go away.|
S~I wonder what their favourite part of battling together is.
''')
add('bond_pair','ThreeIsland_BondBridge_Text_JoyNotEnoughMons ThreeIsland_BondBridge_Text_MegNotEnoughMons',
    'Joy and Meg both want to battle together and require two opposing Pokemon.','''
S~They agree very firmly on the together part. We need another partner for our side.|
S~Both trainers independently state the same preference. Their chosen format is unambiguous.|
N~They want a paired battle. We can prepare for one or move along.|
S~It is sweet that either one you ask mentions the other.|
S~A shared hobby is better when neither person feels left out.|
S~The double act has issued two entirely consistent statements about its availability.|
S~They have found a pleasant use for being inseparable.|
N~Two eligible Pokemon first; then we can test how well the teams coordinate.|
S~Each keeps a place beside herself for the other's name.|
S~Their matching answers make it clear this is something both of them chose.|
S~I wonder whether they settled on their tactics as easily as their partnership.
''')
add('victory_pair','VictoryRoad_3F_Text_RayNotEnoughMons VictoryRoad_3F_Text_TyraNotEnoughMons',
    'Ray and Tyra require two Pokemon for a joint challenge on Victory Road.','''
N~Even this far up the road, some challenges need a different team arrangement.|
N~Their paired format has the same eligibility requirement as other double battles.|
N~No need to force a fight with the wrong setup.|
N~Their ambition can wait while we decide how we want to meet it.|
N~A demanding road is a good place to keep preparation sensible.|
N~The aspiring pair have requested a full opposing cast for their climb.|
N~The road contains enough difficulty without inventing an obligation to accept all of it.|
N~Two strong choices also need a plan for supporting each other.|
N~A summit can hold more than one person's ambition.|
N~They know the challenge they want. We get to know our own limits, too.|
S~I wonder how much of their climb they have made side by side.
''')
add('outcast_ava','SixIsland_OutcastIsland_Text_AvaNotEnoughMons',
    'Ava requires two Pokemon to challenge the sibling pair.','''
S~Ava has counted both sides and spotted the missing half of the arrangement.|
N~She correctly identifies the minimum needed for the proposed paired battle.|
N~We can return when our team fits the challenge.|
N~A simple requirement gives us a clear choice about coming back.|
N~Best to settle the setup before anyone gets excited about the match.|
S~The island encounter requires a slightly larger visiting delegation.|
N~A little practical interruption rarely ruins a whole afternoon.|
N~Preparing a pair could be interesting if we decide to take her up on it.|
N~An invitation can remain on the shore until another day.|
N~She makes the condition sound ordinary, which it is.|
S~I wonder how often visitors reach this little island with a battle in mind.
''')
add('outcast_geb','SixIsland_OutcastIsland_Text_GebNotEnoughMons',
    'Geb eagerly asks for a battle with his sister before noticing the party requirement.','''
S~His invitation ran out ahead of his headcount. An understandable burst of excitement.|
S~He corrects the plan as soon as he notices the practical limitation.|
N~He is eager. Still needs the right setup before we start.|
S~That little pause sounds like excitement bumping into disappointment.|
S~We can leave him with a friendly maybe for a better-prepared visit.|
S~The enthusiastic opening has met a brief administrative complication.|
S~A very small cloud across an otherwise wholehearted invitation.|
N~A second eligible Pokemon would solve the problem more usefully than an improvised exception.|
S~His hope has paused at the edge of a simple number.|
S~He seems genuinely pleased at the prospect of showing us their teamwork.|
S~I wonder whether his sister hears that same eager invitation every time someone arrives.
''')
add('water_miu_refusal','SixIsland_WaterPath_Text_MiuNotEnoughMons',
    'Miu says she and her twin Mia want to battle as a pair.','''
S~The twins have decided this is very much a bring-your-other-half sort of battle.|
S~She explains their preferred partnership rather than criticizing the visiting team.|
N~They want to fight together. We can respect that choice.|
S~Being twins does not make them one person, but sharing this can still be special.|
S~It sounds like something they enjoy more when they do it together.|
S~The sisters are offering a joint appearance, with both names on the bill.|
S~A shared beginning need not mean sharing everything. This part they have chosen.|
N~Their paired tactics will need an opposing pair before we can test them.|
S~Two familiar voices have found something they want to say together.|
S~I like that she states what they want instead of assuming we should know.|
S~I wonder whether their battle styles are as similar as people might expect.
''')
add('water_mia_refusal','SixIsland_WaterPath_Text_MiaNotEnoughMons',
    'Mia assumes having only one Pokemon must make the player lonely.','''
S~One Pokemon can still fill a day with a surprising amount of company.|
N~The number of companions cannot tell her whether a relationship feels fulfilling.|
N~A small team is no proof of loneliness.|
N~Some people feel comfortable with one trusted companion. That is enough to respect.|
S~Two at a table can have plenty to talk about.|
N~The arithmetic is accurate; the emotional conclusion has wandered off without support.|
N~Being outnumbered by a pair does not make someone emotionally incomplete.|
N~Team size is a battle requirement, not a useful loneliness gauge.|
S~A single companion can make a very long road feel inhabited.|
N~Her experience of company may differ from ours. Neither needs to erase the other.|
N~I would rather hear how someone feels than decide by counting their companions.
''')
add('entrance_pair_refusal','SevenIsland_SevaultCanyon_Entrance_Text_EveNotEnoughMons SevenIsland_SevaultCanyon_Entrance_Text_JonNotEnoughMons',
    'Eve and Jon want to battle together and request a two-on-two match.','''
S~Their battle plans have a very firm together-shaped centre.|
S~Both express the same preference: participation as a pair rather than as individuals.|
N~They want the shared match. We need another eligible Pokemon before accepting.|
F~They sound happier about being together than impatient to win.|
S~It is nice to make a plan that both people clearly want.|
S~The romance has stipulated its preferred competitive format.|
S~A polite refusal can be surprisingly affectionate when two people agree on it.|
N~Their partnership is part of the challenge, so we should plan for coordinated moves.|
S~Each invitation leaves room for the same familiar person.|
S~They have managed to turn a practical requirement into a little declaration.|
S~I suspect the two of them enjoy planning these matches almost as much as having them.
''')
add('canyon_pair_refusal','SevenIsland_SevaultCanyon_Text_LexNotEnoughMons SevenIsland_SevaultCanyon_Text_NyaNotEnoughMons',
    'Lex and Nya courteously request a two-on-two battle together.','''
S~The lesson needs both teacher and student present, plus a suitably paired problem.|
N~A shared battle would allow them to observe coordination directly rather than describe it.|
N~A polite request. We can come back with a team that fits.|
S~Nya seems to want the chance to learn with someone familiar beside her.|
N~There is no need for her to apologize for explaining the format.|
S~The tutor and apprentice have requested a practical demonstration with a full cast.|
N~Asking clearly is quite enough. The little apology can rest.|
S~A two-on-two match gives the lesson a whole extra layer of decisions.|
N~Learning beside someone does not mean disappearing into their shadow.|
S~Their courtesy makes it easy to leave the possibility open.|
S~I wonder how much of their coordination is instruction and how much is already instinct.
''')
add('gamecorner_grunt','CeladonCity_GameCorner_Text_GruntPostBattle',
    'The defeated Game Corner guard fears the Rocket hideout will be found and leaves to warn his boss.','''
L~The man guarding a poster has helpfully announced there is a hideout to discover.|
N~His warning confirms a concealed Rocket location. The guarded poster warrants closer inspection.|
N~He is warning his boss. Stay alert and check what he was guarding.|
N~That panic tells us the poster mattered more than he wanted us to know.|
N~We should be careful now that he has gone to alert the others.|
M~An impressively informative exit speech from a supposedly secret organization's guard.|
N~A retreat that leaves the secret standing awkwardly in the room.|
S~A guarded poster and a suddenly worried guard. That is a fairly useful connection.|
N~The secret has acquired a voice and immediately asked for its superior.|
M~He has made concealing the place considerably harder with one farewell.|
N~We should notice what he protected before following where he went.
''')
