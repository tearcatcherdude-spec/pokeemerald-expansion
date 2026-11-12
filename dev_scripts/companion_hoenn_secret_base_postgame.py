"""Verified Secret Base trainer refusals and post-Champion repeat endings."""
ROWS = []
EMOTIONS = dict(N='neutral', S='soft_smile', A='annoyed', F='flustered', D='sad', U='surprised', M='smug', L='laughing')

def add(key, labels, subject, lines):
    replies = [x.strip() for x in lines.strip().split('|')]
    replies = [EMOTIONS[x[0]] + x[1:] for x in replies]
    assert len(replies) == 11, (key, len(replies))
    ROWS.append(dict(key='hsb_'+key, labels=labels.split(), subject=subject, replies=replies))

add('decline0', 'SecretBase_Text_Trainer0DeclineBattle', 'The base owner accepts that the player cannot battle now.', '''
S~No battle today, and the ceiling has stayed up. A very successful refusal.|
S~The owner accepts the present limitation without requiring an explanation.|
S~Not now is enough. Good that they leave it there.|
S~I like not having to turn a small no into a whole account of my day.|
S~We can still enjoy visiting without making it another task for the team.|
S~A proposed battle has quietly returned to being a perfectly ordinary visit.|
S~The challenge has withdrawn without attempting to haunt the rest of the afternoon.|
N~We can decide on a challenge later when the team is ready.|
S~A welcoming room can keep its warmth after an invitation is declined.|
S~They seem disappointed, but they haven't made us responsible for fixing that.|
S~I'd be happy to ask about the base itself instead, if the owner feels like talking.
''')
add('post0', 'SecretBase_Text_Trainer0PostBattle', 'The owner asks for an opinion of the base and invites a visit tomorrow.', '''
S~They've moved from battling to the very serious question of whether we like the room.|
N~The invitation is for another visit. This message doesn't establish a particular battle result.|
S~A friendly return invitation. We can look around properly now.|
S~I'd find one small detail I genuinely liked rather than give a vague compliment.|
S~It feels nice to be wanted back for more than a single match.|
S~The combat report has been replaced by a request for an interior review. A pleasant change.|
S~Tomorrow has received an invitation. It remains entitled to arrive at its own pace.|
N~I'd ask which part of the arrangement took the most effort.|
S~A little hidden room can become familiar through the promise of another hello.|
U~I'd like to know which piece the owner most wanted visitors to notice.|
S~I'd ask how the base has changed since the first day they moved in.
''')
add('decline1', 'SecretBase_Text_Trainer1DeclineBattle', 'The owner interprets refusing a battle as not wanting the desirable base location.', '''
N~We declined a battle, not an entire opinion about the floor plan. Two separate little forms.|
N~Interest in the location doesn't necessarily imply willingness to battle for it now.|
N~A no to battling isn't a claim about wanting the spot.|
N~I'd rather say what I meant than let the conversation quietly choose it for me.|
N~We can admire a place without turning somebody's home into a prize.|
N~A practical refusal has accidentally been entered into the property-interest questionnaire.|
N~The room and the battle have become tangled. No need to let them stay that way.|
N~We should distinguish appreciating the location from agreeing to the proposed contest.|
N~A place can be worth seeing without needing to become ours.|
N~They seem proud of the spot. We don't have to covet it to recognize that.|
N~I'd ask what made them wait for this location, rather than argue about taking it.
''')
add('post1', 'SecretBase_Text_Trainer1PostBattle', 'The owner promises the spot only if they move out one day.', '''
N~A future home with a very flexible moving date. I wouldn't start carrying boxes yet.|
N~The statement is conditional on the owner's eventual move. No transfer has occurred.|
N~They still live here. Don't treat the promise as a vacant room.|
N~I'd rather they enjoy their place than feel we are waiting outside for it to empty.|
N~A friendly promise doesn't mean either of us needs to plan a move today.|
N~A generous offer whose timetable has been carefully delegated to some unspecified future day.|
S~The lease is imaginary and the vacancy date has declined to introduce itself.|
N~We should leave the arrangement conditional rather than assume any current ownership change.|
N~A possible doorway in the future isn't a room we occupy now.|
N~I'd appreciate the gesture without making their home feel like borrowed space.|
N~I'd ask where they'd like to go if they ever did decide to move.
''')
add('decline2', 'SecretBase_Text_Trainer2DeclineBattle', 'The sociable base owner invites the player to ask for a battle when ready.', '''
S~The battle can wait for our shout. I may send a polite indoor voice instead.|
S~The owner leaves initiation with us. A future attempt remains optional.|
S~Good. We can ask when we're ready.|
S~I like having time to look around without feeling the invitation is counting down.|
S~No need to hurry the team just because someone else is eager.|
S~A refreshingly clear arrangement: the host is available, and our readiness gets a vote.|
S~The challenge has settled into a chair instead of following us around the room.|
N~We can inspect the team's condition before taking up the offer.|
S~A door left open doesn't need to pull anyone through it.|
S~The invitation stays friendly because it isn't trying to become an obligation.|
S~I'd ask about a favorite decoration while we decide what we want to do.
''')
add('post2', 'SecretBase_Text_Trainer2PostBattle', 'The owner wants furniture and decorations that make the base enjoyable for visitors.', '''
S~A secret base with guest comfort in the budget. That's a very nice kind of secret.|
S~The owner connects personal choices with other people's experience of the room. Considerate design.|
S~Make it somewhere people can settle. Doesn't have to be expensive.|
S~I'd like a small quiet place where a shy visitor doesn't feel stuck in the middle.|
S~A comfortable seat and room for the partners could do more than an impressive display.|
S~A battle host has remembered the excellent possibility of entertaining people without battling them.|
S~An interior scheme containing the radical idea that guests have feet and need places to put them.|
U~I'd ask what visitors actually do in the space before choosing the next pieces.|
S~A little room changes when someone makes space for another person's ease.|
U~I'd help choose one welcoming focal point instead of filling every spare tile.|
S~I'd ask a returning visitor which detail made them feel most at home.
''')
add('decline3', 'SecretBase_Text_Trainer3DeclineBattle', 'The owner wonders whether finding the hidden base has left the player tired.', '''
S~They've considered that the journey might have used up our spare battling legs. Thoughtful host.|
N~Fatigue is proposed as a possibility, not established by this question.|
S~Could be tired. Either way, we don't need a battle now.|
S~I like that the first guess is considerate instead of accusing us of being afraid.|
S~A host who notices the trip can be part of the effort has the right idea.|
S~The invitation has been replaced by the sensible suspicion that visitors also possess limited stamina.|
S~At last, someone acknowledging that a hidden address creates an errand.|
N~We can check the team's condition rather than simply accept or reject the guess.|
S~Being found can be a welcome without becoming another demand.|
S~They've made room for the visitor's day instead of only thinking about their own plans.|
S~I'd ask how most people find the place. There may be several rather different arrival stories.
''')
add('post3', 'SecretBase_Text_Trainer3PostBattle', 'The owner asks about the player base and expresses interest in visiting.', '''
S~A hidden-house visit has become a possible exchange of hidden-house directions. Very neighborly.|
S~The owner proposes reciprocity without claiming a visit has already been arranged.|
S~Nice offer. We can share directions if we want company.|
F~I'd want a little time to make the place feel ready for someone else to see.|
S~A visit can be nicer when both people get a turn being the host.|
S~The secret-base community has discovered the complicated diplomatic business of returning a visit.|
S~Two hidden addresses attempting to establish ordinary neighborly relations.|
N~We should agree on the invitation and actual location before treating it as a plan.|
S~One small doorway can make another one feel less far away.|
S~I'd enjoy seeing what the owner notices in our choices after showing us their own.|
S~I'd ask what kind of detail they most enjoy discovering in someone else's base.
''')
add('decline4', 'SecretBase_Text_Trainer4DeclineBattle', 'The owner accepts that people are not always in the mood to battle.', '''
S~An excellent discovery: even an enthusiastic trainer can have a not-today pocket.|
S~The owner recognizes that interest varies with circumstances. A reasonable response.|
S~Exactly. No need to turn a quiet day into a test.|
S~I like hearing someone say that as though it is ordinary. Because it is.|
S~Being fond of battling doesn't mean every visit has to become one.|
S~A host has successfully distinguished an enduring interest from an endless obligation to demonstrate it.|
S~The mood has been allowed to exist without submitting a written defense.|
N~We can choose a better time rather than force a less prepared attempt.|
S~An open hand can remain open while the person beside it rests.|
S~That response makes me more comfortable accepting an invitation on another day.|
S~I'd be happy simply talking about what they've been enjoying lately.
''')
add('post4', 'SecretBase_Text_Trainer4PostBattle', 'The owner encourages mutual improvement after the battle.', '''
S~Both of us can get stronger. I like a conclusion with room for everybody's next try.|
S~The response frames the encounter as shared development rather than a final ranking.|
S~Good attitude. Take one useful lesson each and keep going.|
S~It's nice when a battle ends without somebody needing the other person to feel small.|
S~I'd rather leave with an idea to practice than only a number to defend.|
S~A competitive meeting has produced a cooperative conclusion. An excellent use of opponents.|
S~Two trainers have survived a comparison without becoming permanent categories.|
N~We can identify a specific improvement instead of treating stronger as an undefined demand.|
S~Two paths can sharpen each other without needing to become the same path.|
S~I like the shared direction in that encouragement. It feels generous.|
N~I'd ask what they noticed changing during the match. That could give both sides something to work on.
''')
add('decline5', 'SecretBase_Text_Trainer5DeclineBattle', 'The base owner quietly accepts that a battle cannot happen now.', '''
S~The battle has been put away without making the whole visit feel canceled.|
S~The present refusal is accepted. The message doesn't establish any loss of future access.|
S~No fight now. We can still be courteous guests.|
N~The small pause sounds disappointed, but not angry. I appreciate that.|
S~A kind no can leave the rest of the afternoon perfectly usable.|
S~An invitation has been declined with no attempt to turn the answer into a grand insult.|
S~The challenge has receded peacefully into the furniture.|
N~We can decide later whether this is a suitable time for a match.|
S~A quiet answer can leave the room just as warm as before it.|
S~I'd rather acknowledge the disappointment than pretend the offer never mattered.|
S~I'd ask what the owner most likes about this particular place.
''')
add('post5', 'SecretBase_Text_Trainer5PostBattle', 'The owner invites the player to visit again when passing through the area.', '''
S~A little place has become somewhere we might stop instead of merely somewhere we found once.|
S~The invitation is conditional on a future journey through the area. No appointment is implied.|
S~Good reason to remember the turn next time we're nearby.|
S~I like the easy kind of invitation that doesn't make distance feel like neglect.|
S~A friendly stop can give a long trip a different shape.|
S~A home has quietly promoted itself to a welcome landmark on future journeys.|
S~The hidden address has acquired a repeat visitor policy. Quite civilized.|
N~We should remember the actual location if we want to take up the offer later.|
S~A familiar greeting can wait along a road without asking the road to bend toward it.|
S~The wording feels relaxed. It leaves us welcome without keeping count.|
S~I'd ask whether the base changes much between visits. There may always be something new to notice.
''')
add('decline6', 'SecretBase_Text_Trainer6DeclineBattle', 'The private battle researcher accepts postponing the match.', '''
S~The research has been postponed. I hope the notebook has a box for visitor-not-in-the-mood.|
N~No trial occurred, so there is no battle evidence to interpret from this visit.|
S~Another time. Better than a reluctant test match.|
S~I'm glad being curious about the lab doesn't make us responsible for supplying an experiment.|
N~A good host leaves room for somebody to be a guest instead of a useful opponent.|
S~The secret laboratory has accepted the regrettable temporary shortage of willing test subjects.|
S~Science will have to endure a moment without making us its immediate problem.|
N~The owner can use the time to refine the question they want a future battle to test.|
N~A paused experiment needn't become an unwelcome room.|
S~They accepted the answer neatly. That makes me more curious about talking again.|
N~I'd ask what they most want to learn from their next match.
''')
add('post6', 'SecretBase_Text_Trainer6PostBattle', 'The battle researcher thanks the player and invites another visit tomorrow.', '''
S~A thank-you from the secret lab. I hope our contribution is filed under helpful visitor rather than unusual specimen.|
S~The completed match offers observations. A repeat visit could test a revised idea.|
S~Good. Learn something from the match before asking for another.|
S~I like that the thanks comes before the next invitation.|
N~A useful practice partner should be appreciated as a person, too.|
S~The experiment concludes with gratitude and a politely requested sequel. Sound academic manners.|
S~Our participation has earned a thank-you and possible future employment as a difficult question.|
N~The owner can review the match and choose one change to investigate next time.|
S~A shared effort can leave something worth returning to, without making tomorrow a debt.|
N~I'd hope the next visit includes a little of what they've discovered since this one.|
N~I'd ask which result surprised them most before leaving.
''')
add('decline7', 'SecretBase_Text_Trainer7DeclineBattle', 'The decoration-loving owner openly expresses disappointment after a battle refusal.', '''
N~A little disappointment is allowed. It doesn't mean we have to buy it a battle.|
N~The feeling is stated without a further demand. We can acknowledge it and keep our choice.|
N~They're disappointed. Our answer can still stay no.|
D~I feel the little sting in that pause, but I don't think a guilty yes would help.|
N~I'd be kind without treating their mood as something we're obliged to repair.|
N~The invitation has met an ordinary disappointment, mercifully without becoming a contract dispute.|
N~A feeling has been announced. It has not thereby become an instruction.|
N~A later match can be considered on its own merits, not as compensation.|
N~A small cloud can cross a friendly room without becoming its whole sky.|
N~I'd let the honest feeling exist instead of hurrying to make it look happier.|
N~I'd ask about the room only if the owner still felt like sharing it.
''')
add('post7', 'SecretBase_Text_Trainer7PostBattle', 'The owner treats the match as fun and turns toward shopping afterward.', '''
S~Battle finished, next adventure: a very dangerous encounter with a cushion display.|
S~The owner can move between interests without making the battle define the entire day.|
S~Enjoyed the match and ready to move on. Sensible.|
S~I like that the afternoon can contain a serious effort and something light afterward.|
S~A little ordinary pleasure can be a good way to leave a hard match behind.|
S~The competitive appointment has concluded. Decorative acquisition is now accepting visitors.|
S~The Pokemon can rest while the furniture experiences the pressure.|
N~I'd suggest a clear idea of what the room needs before browsing everything at once.|
S~A day can keep more than one kind of enjoyment without making them compete.|
U~I'd ask what they feel is missing from the room before choosing another piece.|
S~I'd love to hear which object they come home pleased to have found.
''')
add('decline8', 'SecretBase_Text_Trainer8DeclineBattle', 'The owner leaves the battle offer open for another time.', '''
S~A standing battle invitation. I hope it has comfortable shoes.|
S~The statement leaves a later challenge possible, rather than establishing a current obligation.|
S~Good. We'll ask if the time is right.|
S~I like being welcome without having to decide immediately.|
N~We can enjoy the visit and keep the team's readiness separate from the host's enthusiasm.|
S~The challenge has adopted a flexible schedule, an excellent improvement in hospitality.|
S~A battle offer willing to sit quietly until needed. Unusually considerate offer.|
N~We can review our plans before deciding whether another match fits.|
S~An invitation can remain present without standing in the doorway.|
S~That kind of patience makes a return visit feel easier.|
S~I'd ask what other parts of the base the owner enjoys showing visitors.
''')
add('post8', 'SecretBase_Text_Trainer8PostBattle', 'The owner promises to remain competitive at collecting decorations and invites another visit.', '''
S~The battle has ended, but the cushions have apparently entered a much longer tournament.|
N~Decoration collecting is the owner's next competitive focus. No collection result is established here.|
N~A room should still be useful, not just a score against someone else.|
N~I hope they keep choosing things they like, even when nobody is comparing collections.|
N~A favorite object can be worth more than the one bought only to beat a rival.|
S~One contest has ended and another has immediately recruited the household furnishings.|
S~The shelves have been informed that victory remains compulsory. Poor shelves.|
N~We could ask which piece serves the room best instead of ranking sheer quantity.|
N~A collected thing deserves a place beyond proving somebody else has less.|
N~I'd want the base to show the owner's taste rather than the opponent they imagined while shopping.|
S~I'd ask which decoration they'd keep if the competition vanished tomorrow.
''')
add('decline9', 'SecretBase_Text_Trainer9DeclineBattle', 'The style-conscious owner offers to demonstrate battle style another time.', '''
S~The demonstration has a flexible curtain time. I appreciate that in a person's living room.|
N~The owner offers a future demonstration. We haven't seen a new battle from this refusal.|
N~Another time can work. No need to perform for us now.|
S~I like being allowed to look at the room without immediately joining the next event.|
N~A style is easier to appreciate when the person leaves room for the visitor's mood.|
S~A postponed display, with the owner's enthusiasm apparently sufficient to preserve it indefinitely.|
S~The style remains available by appointment. Merciful arrangement.|
N~We can decide whether a future match suits the team rather than answer under pressure.|
S~Something worth showing can wait until another person is ready to look.|
S~I'd enjoy asking about the choices themselves before judging the whole impression.|
N~I'd ask what the owner most wants an opponent to notice about their approach.
''')
add('post9', 'SecretBase_Text_Trainer9PostBattle', 'The owner asks about their battle style and intends to keep refining it.', '''
S~They've asked for a review and already booked more polishing time. A productive little mirror.|
S~Continued refinement suggests the owner treats style as something developed through feedback.|
N~Give a useful observation. Flattery won't improve the next match.|
N~I'd find one thing that felt distinctly theirs and say why it stayed with me.|
N~A specific kind comment can help more than calling the whole thing perfect.|
S~A performance has concluded with an unusually practical request for an opinion that might improve it.|
S~The style has survived being tested and is reporting for further maintenance.|
N~We can distinguish what worked from what simply looked impressive.|
N~A chosen way of moving can become clearer each time it meets another person's answer.|
U~I'd ask which part they most want to develop, then respond to that rather than redesign everything.|
N~I'd describe one turning point clearly. It gives the owner something concrete to think about.
''')
