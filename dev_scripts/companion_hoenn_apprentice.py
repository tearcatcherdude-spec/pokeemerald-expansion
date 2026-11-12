"""Actual terminal apprentice counseling templates exposed by the native source hook."""
ROWS = []
EMOTIONS = dict(N='neutral', S='soft_smile', A='annoyed', F='flustered', D='sad', U='surprised', M='smug', L='laughing')

def add(key, labels, subject, lines):
    replies = [x.strip() for x in lines.strip().split('|')]
    replies = [EMOTIONS[x[0]] + x[1:] for x in replies]
    assert len(replies) == 11, (key, len(replies))
    ROWS.append(dict(key='hap_'+key, labels=labels.split(), subject=subject, replies=replies))

add('level0', 'gText_ApprenticeLevelModeThanks0', 'The apprentice cries with happiness after the player selects a challenge level.', '''
S~Happy tears over a level choice. We've apparently become a very efficient little fountain switch.|
S~The relief seems genuine. We can acknowledge it without making the reaction embarrassing.|
S~A choice helped. Give them a moment to settle.|
S~I'm glad the tears meant happiness. I was worried I'd misunderstood.|
S~A little patient help can matter much more than the task itself suggests.|
S~Our modest piece of advice has received an unexpectedly enthusiastic weather report.|
S~Joy has escaped containment. At least the cause is kind.|
N~Now they have a starting format. The next step can be small and concrete.|
S~Relief sometimes arrives in water before it finds words.|
S~I'd rather let them be moved than hurry them into looking composed.|
S~I'd ask later how the first attempt felt, once the happy surprise has settled.
''')
add('level1', 'gText_ApprenticeLevelModeThanks1', 'The apprentice accepts the selected level and eagerly asks for future teaching.', '''
S~They've found a starting line and already waved at us from the next lesson.|
S~They accept the recommendation and remain interested in learning. Good momentum.|
S~A clear start. They still need to do the work.|
S~I like how quickly the question turned into wanting to try.|
S~I'd be happy if the advice helps them discover what they enjoy doing.|
S~One answer has successfully created a future appointment with more questions.|
S~The lesson is finished. Curiosity has declined to leave with it.|
N~We can review the choice after they have actual experience with the format.|
S~A small answer can open the next door rather than close the conversation.|
S~They make learning feel sociable instead of shameful. That's lovely.|
S~I'd ask them to bring back one thing they noticed during their attempt.
''')
add('level2', 'gText_ApprenticeLevelModeThanks2', 'The apprentice confirms the selected level and plans to return with further questions.', '''
S~Understood, accepted, next question reserved for later. A wonderfully organized little visit.|
S~They've retained a clear next step and a source for clarification. Practical approach.|
S~Good. Try the format, then ask about anything unclear.|
S~I like not needing to pretend one answer settles every question forever.|
S~A useful lesson gives someone something to do, not just something to repeat.|
S~A crisp acknowledgment, with future confusion sensibly booked into a later conversation.|
S~The question has been answered without acquiring a dramatic afterlife.|
N~Their next observations can help us decide whether the initial choice suited them.|
S~A path is easier to begin when asking again remains allowed.|
S~They sound comfortable enough to admit there may be more they don't know.|
N~I'd ask what they hope to learn from the first round before they go.
''')
add('level3', 'gText_ApprenticeLevelModeThanks3', 'The apprentice doubts their chances but agrees to try the chosen level.', '''
D~They're taking the first step while their doubt keeps trying to tie the shoes together.|
N~Their prediction of failure isn't established. An attempt will provide actual information.|
N~Try it first. They haven't lost the match in advance.|
D~I recognize that habit of apologizing before anyone has been disappointed.|
N~I'd like them to know the time wasn't wasted just because they're uncertain.|
N~A perfectly ordinary lesson has been made to carry an unfair trial of the learner's worth.|
D~The doubt arrived early and is pretending to be an official forecast.|
N~We can set a small first goal that doesn't require immediate victory.|
D~A trembling beginning is still a beginning.|
N~They don't have to earn the right to be helped by sounding confident.|
N~I'd ask them to notice one thing they learned, whatever the first result is.
''')
add('level4', 'gText_ApprenticeLevelModeThanks4', 'The apprentice accepts the level partly because blaming the player choice would soften a loss.', '''
N~We've recommended a level and accidentally been appointed the official cushion for disappointment.|
N~Advice can inform a decision without taking ownership of every future result.|
N~We'll help. They still own how they approach the challenge.|
N~I'm glad it feels less frightening, though I don't want the choice to become a place to hide.|
N~A loss can be handled without needing to hand it to someone else.|
N~Our teaching appointment appears to include a complimentary blame-absorption service.|
N~The responsibility has been quietly placed beside our name tag.|
N~They should understand why the format was selected, not only who selected it.|
N~A borrowed certainty won't hold every difficult feeling for long.|
N~I'd rather help them feel able to choose than simply feel safe because we did it.|
N~I'd explain the reason behind the recommendation before they rely on the name behind it.
''')
add('level5', 'gText_ApprenticeLevelModeThanks5', 'The busy apprentice accepts the level advice and hurries back to work.', '''
S~A battle plan squeezed between shifts. I hope their calendar leaves somewhere for breathing.|
N~They need to fit practice into existing obligations. A realistic schedule will matter.|
N~Work first if it needs them. The challenge can wait.|
N~I hope they get to enjoy the attempt instead of making it one more thing they're late for.|
N~I'd rather they try rested than carve the time out of every meal and break.|
S~The grand training ambition has met the much more punctual demands of employment.|
S~Adventure has been allocated a small gap in the schedule. Brave little gap.|
N~We can keep future advice specific enough to use in limited practice time.|
N~A wish can travel beside an ordinary working day, even if it has to walk slowly.|
N~Their time matters. I'd make the next conversation useful rather than merely long.|
S~I'd ask what part of battling makes the effort of finding time worthwhile.
''')
add('level6', 'gText_ApprenticeLevelModeThanks6', 'The delighted apprentice calls the level advice cool and ends the day visit.', '''
S~We've delivered a cool answer. I wasn't aware the level menu came with a temperature rating.|
S~Their enthusiasm is encouraging, though the recommendation still needs experience behind it.|
S~Enough for today. Let them try what they learned.|
S~They sound happy to have one clear thing to take away.|
S~I like ending a lesson while the learner still feels eager instead of exhausted.|
S~An ordinary choice has received excellent reviews for style. I shall endeavor to remain humble.|
S~The advice has been judged cool. Its practical assessment is scheduled for later.|
N~They have a next step. Another question can wait until the choice has been tested.|
S~A small lesson can leave a brighter mood than it found.|
S~Their delight is infectious. I'd still want the decision to feel useful tomorrow.|
S~I'd ask them next time whether the format matched what they expected.
''')
add('level7', 'gText_ApprenticeLevelModeThanks7', 'The apprentice politely thanks the player for choosing a level and promises effort.', '''
S~A little thanks, a little determination, and a very kind goodbye. Nicely packed.|
S~They distinguish the advice from the effort they must supply. A healthy response.|
S~They'll do their best. That's the part in their hands.|
S~I like the way they wished us well, too.|
S~Help feels better when both people remember the other is a person.|
S~A courteous lesson ending that has remembered to distribute goodwill in both directions.|
S~No grand guarantee. Just effort and decent manners. An excellent combination.|
N~They can test the recommendation and bring back observations later.|
S~A little trust can be carried without becoming a heavy demand.|
S~Their gratitude feels warm without making the relationship awkwardly grand.|
S~I'd be glad to hear how their attempt goes when we next meet.
''')
add('level8', 'gText_ApprenticeLevelModeThanks8', 'The apprentice repeats understanding the level choice and expresses delighted gratitude.', '''
L~They understood it twice. That's a very generous margin of understanding.|
S~The repetition signals excitement. I'd still check their practical interpretation when needed.|
S~They've got the choice. Time to see how it works.|
S~It's lovely hearing someone so pleased about a starting point.|
S~I hope the excitement carries into patient practice, not just a quick rush.|
S~The answer has been understood with enough enthusiasm to require a second confirmation.|
S~Understanding has been achieved and then enthusiastically achieved again.|
N~A short explanation of the choice would help turn delight into usable knowledge.|
S~Relief can repeat itself when one set of words isn't quite enough.|
S~They sound delighted by being helped as much as by the actual answer.|
S~I'd ask what they're most looking forward to trying within that format.
''')
add('level9', 'gText_ApprenticeLevelModeThanks9', 'The apprentice energetically accepts the format and calls the player a mentor.', '''
S~That goodbye had enough momentum to start the first match on its own.|
N~They're eager to act. The mentoring role should still support their own judgment.|
S~Good energy. Put it into a prepared attempt.|
S~I might need a moment to catch up with how quickly the excitement moved.|
N~I'd want them to leave with a sensible plan underneath all that enthusiasm.|
S~A brisk promotion to mentor, awarded before anyone could arrange a suitably dignified ceremony.|
S~The lesson has concluded at considerable speed. Several syllables may still be catching up.|
N~We can review the format's practical requirements before the enthusiasm carries them past those.|
S~Some people greet a new path as though the ground has started moving with them.|
S~Their style is exuberant. I'd leave room for that while keeping the advice clear.|
S~I'd ask for a story from their first attempt when they return.
''')
add('level10', 'gText_ApprenticeLevelModeThanks10', 'The apprentice jokes about selecting the opposite level before agreeing to follow the advice.', '''
S~They sent the advice the wrong way for a second, then kindly brought it back.|
N~The joke is explicitly retracted. The selected recommendation remains the intended plan.|
N~Fine joke. Make sure the actual choice is clear.|
F~I was briefly worried I'd explained it badly. Then I caught up.|
S~A little teasing can make learning feel less stiff, if both people know where the answer landed.|
S~The student has staged a tiny rebellion and concluded it before administration could intervene.|
S~Defiance, swiftly recalled for maintenance. The lesson survives.|
N~We should verify which format they'll actually enter rather than leave the joke ambiguous.|
S~A small sideways step can still return to the path without harm.|
S~They want the conversation to be playful. I can appreciate that without taking the master title seriously.|
S~I'd ask what they think the chosen format will feel like. That puts the idea in their own words.
''')
add('level11', 'gText_ApprenticeLevelModeThanks11', 'The apprentice accepts the level through an enthusiastic rhyming thank-you.', '''
S~They've taken the answer and given it a rhyme. That's more decoration than most menus receive.|
S~The wordplay conveys acceptance. Understanding should still extend beyond the matching sounds.|
S~A cheerful answer. Hope the actual preparation is just as sound.|
S~I like the little rhyme. It makes the whole exchange feel less formal.|
S~If it helps them remember the plan, a bit of play can be useful.|
S~A recommendation has departed wearing an unexpectedly neat set of rhyming cuffs.|
S~The lesson has been absorbed into verse. A tidy containment method.|
N~We can check the reasoning next time rather than only whether they remember our words.|
S~A small rhythm can make a new thought easier to carry.|
S~They've found their own way to respond instead of merely repeating the answer.|
S~I'd ask whether they always think of rhymes so quickly or only when excited.
''')
add('level12', 'gText_ApprenticeLevelModeThanks12', 'The rhyming apprentice accepts the advice and asks not to be forgotten.', '''
S~The advice came back with a rhyme and a little please-remember-me tied to the end.|
N~Their farewell combines trust in the choice with a wish to remain personally recognized.|
S~We can remember them without guaranteeing another appointment.|
D~That last little request feels more important than the rhyme around it.|
S~I'd answer the person, not just the lesson. A kind goodbye can do that.|
S~A cheerful flourish has quietly smuggled a very sincere request into the final lines.|
S~The verse is playful. The wish underneath has less armor.|
N~They can use the format as a starting point rather than assume the recommendation is infallible.|
S~A name wants somewhere to remain after the feet have carried its owner away.|
S~I'd acknowledge the wish directly instead of smiling only at the clever wording.|
S~I'd ask them to tell us how the attempt went if we meet again. That gives the next hello something real.
''')
add('level13', 'gText_ApprenticeLevelModeThanks13', 'The apprentice accepts the level and hopes to keep asking the mentor for help.', '''
S~A starting choice today, another question tomorrow. Learning has sensibly refused to finish all at once.|
N~Ongoing guidance can help, provided it gradually develops independent decisions.|
N~We can help again. They should think through the choice, too.|
S~I like that asking for help doesn't sound embarrassing to them.|
N~A useful mentor explains enough that the next question can become more specific.|
S~An efficient acknowledgment followed by a long-term application for our available wisdom.|
S~The question has departed. Its relatives may visit later.|
N~I'd ask what they learned from this choice before recommending the next one.|
S~A path can be shared for a while without either person carrying the other the whole way.|
N~The trust is encouraging. I'd want them comfortable disagreeing as they learn.|
N~I'd ask what they already suspect about their next question before supplying an answer.
''')
add('level14', 'gText_ApprenticeLevelModeThanks14', 'The flustered apprentice agrees to try the recommended level and hopes to remain composed.', '''
S~They don't need to arrive perfectly unflustered. The first step can bring its own little wobble.|
N~Composure may improve with familiarity. The initial attempt need not be flawless.|
N~Try it carefully. Being nervous doesn't cancel the effort.|
D~I understand wanting to do well without everyone noticing how worried I am.|
N~I'd rather they have one calm plan than demand a brave-looking face from themselves.|
S~A valiant challenge may begin with several undignified little breaths. Entirely acceptable.|
S~Courage has declined to iron every wrinkle before leaving the house.|
N~A simple routine before entry could reduce the number of decisions made while flustered.|
S~A shaking hand can still open the right door.|
N~I'd like them to feel allowed to be nervous without apologizing for taking up space.|
N~I'd ask what helps them settle before a challenge. They may already know one useful thing.
''')
add('level15', 'gText_ApprenticeLevelModeThanks15', 'The formal apprentice verifies the choice and appreciates being accepted despite fears of annoying the player.', '''
S~They checked the answer, thanked us, and apologized for existing a little too loudly. No apology needed.|
S~Clarification is reasonable. Their fear of being annoying doesn't invalidate the question.|
N~Asking once more is fine. Better than leaving uncertain.|
D~I wish they didn't have to wonder whether being welcomed was a favor.|
S~Taking time to understand isn't an inconvenience we need to make them feel guilty about.|
N~A perfectly respectable question has arrived burdened by an unnecessary apology.|
S~The manners are immaculate. The self-criticism is doing far too much work.|
N~We can confirm the recommendation and explain why it fits their stated situation.|
S~A person can ask for a place beside us without apologizing for the space they occupy.|
N~I'd answer the question plainly and leave the self-judgment out of the exchange.|
S~I'd ask them to bring their own observations next time. That makes the learning a conversation.
''')
add('mon0', 'gText_ApprenticeMonThanks0', 'The apprentice happily cries and plans to catch the recommended species.', '''
S~The recommendation has launched a search and another small raincloud of happiness.|
N~They intend to find the recommended species. No capture has happened yet.|
N~Find one patiently. A recommendation isn't a reason to rush a capture.|
S~I hope the new partner gets as warm a welcome as our answer did.|
S~I'd like them to learn about the individual they meet, not only the name we chose.|
S~A future teammate has already received an extremely emotional advance welcome.|
S~The tears are cheerful. The prospective Pokemon has not yet been notified.|
N~They should look for a partner suited to the plan and learn its actual strengths.|
S~A little hope has gone ahead to wait for someone they haven't met.|
N~I'd want the excitement to leave room for the Pokemon's own personality.|
S~I'd ask how they recognized the one they eventually chose.
''')
add('mon1', 'gText_ApprenticeMonThanks1', 'The apprentice accepts the advised Pokemon choice and thanks the player.', '''
S~One choice settled. Now the little partner gets to show there's more to it than a name.|
N~The recommendation concerns this selection, not universal superiority of the species.|
N~A choice for this plan. Still learn the individual partner.|
S~I like the relief in having somewhere definite to begin.|
N~Good advice should help them notice what suits the Pokemon, too.|
S~The decision has been neatly received without requiring a grand declaration of destiny.|
S~The lesson has produced an answer and mercifully little paperwork.|
N~They can compare the actual partner's qualities with the role they intend it to fill.|
S~A chosen name is only the first small part of getting to know a living creature.|
N~I'd keep the word better attached to the decision, not the Pokemon's whole worth.|
N~I'd ask what they like about that choice besides knowing we recommended it.
''')
add('mon2', 'gText_ApprenticeMonThanks2', 'The apprentice sets out to catch a strong example of the recommended species.', '''
S~They've turned our answer into a very purposeful errand. I hope the Pokemon appreciates the introduction.|
N~Finding the species is one step. Assessing an individual's suitability is another.|
N~Strong is useful. Compatible with the team matters, too.|
N~I'd want them to notice more than whether the first one looks impressive.|
S~A new partner deserves a patient first meeting, even when we're excited to begin.|
S~The lesson has issued an expedition order and expects the wildlife to cooperate.|
S~A targeted search. The wilderness may have scheduling opinions.|
N~They should check the partner's actual moves and traits once they've met it.|
N~A search begins with an idea. The meeting may change the shape of it.|
N~I'd be curious what quality makes them decide this is the one.|
S~I'd ask for the story when they return, including whatever surprised them.
''')
add('mon3', 'gText_ApprenticeMonThanks3', 'The apprentice worries a wild Pokemon will ignore them but resolves to try catching it.', '''
D~They haven't met the Pokemon yet and are already apologizing to its imaginary first impression.|
N~The anticipated rejection isn't evidence. The actual encounter can supply information.|
N~Try a careful approach first. Don't decide the result beforehand.|
D~I know that feeling of expecting someone to turn away before you've said hello.|
N~I'd want them to approach patiently, without treating the Pokemon's caution as a personal insult.|
N~An unseen future teammate has been assigned a surprisingly severe opinion of the applicant.|
D~Their doubt has arrived at the encounter before either actual participant.|
N~We can explain a practical approach so the first step feels less vague.|
N~A cautious creature may need space, not a person convinced they are unworthy of notice.|
N~I'd separate a wild Pokemon's reaction from a judgment about the trainer.|
N~I'd ask what part of the meeting worries them most, then address that specifically.
''')
add('mon4', 'gText_ApprenticeMonThanks4', 'The apprentice embraces the species recommendation because player responsibility may soften losses.', '''
N~Our recommendation has become a comfortable little umbrella for any later disappointment.|
N~Choosing a species doesn't make us responsible for every subsequent battle outcome.|
N~Explain the choice. They still need to learn how to use the team.|
N~I want them less frightened, but also able to trust their own understanding.|
N~A new partner shouldn't arrive already carrying someone else's excuse for losing.|
N~The proposed Pokemon has been selected, and the blame appears to have selected us.|
N~A recommendation with an unrequested warranty attached.|
N~They need the reasoning behind the choice so they can adapt it independently.|
N~Borrowed certainty can feel light until the first difficult day leans on it.|
N~I'd rather help them feel capable than merely protected by our name.|
N~I'd ask them to explain how the partner fits the plan in their own words.
''')
add('mon5', 'gText_ApprenticeMonThanks5', 'The busy apprentice plans to find time to catch the recommended Pokemon.', '''
S~Another appointment for a very crowded calendar: meet one future teammate.|
N~They'll need time both for the encounter and for learning about the new partner afterward.|
N~Don't rush the meeting just to fit it between shifts.|
N~I hope this becomes something they enjoy looking forward to, not another deadline.|
N~A new partner needs ordinary attention after the exciting first day, too.|
N~The schedule has been asked to find a space large enough for an entirely new companion.|
S~A busy life is attempting to make room for somebody with paws. Worthwhile rearrangement.|
N~A realistic routine will matter more than finding the species quickly.|
S~Making room in a day can be the beginning of making room in a life.|
N~I'd want the plan to fit their actual time rather than an ideal week that never happens.|
S~I'd ask where the new partner might fit into an ordinary working day.
''')
add('mon6', 'gText_ApprenticeMonThanks6', 'The apprentice enthusiastically calls the species recommendation cool and ends the lesson.', '''
S~A cool answer about a Pokemon. I hope its actual personality is allowed to be wonderfully uncool.|
N~The enthusiasm follows the recommendation. Suitability still needs to be observed in practice.|
N~Good. Learn the partner before deciding the choice solved everything.|
S~It's nice seeing them leave with something they're eager to discover.|
N~I'd want them to notice the Pokemon's comfort, not only the exciting idea of having it.|
S~The species has received an excellent style review from someone who hasn't met the individual yet.|
S~A remarkably fashionable recommendation. The practical test comes later.|
N~They can bring observations from the actual partner to the next conversation.|
S~An imagined companion has become a little clearer, though the real one will bring surprises.|
N~The excitement is lovely. I'd leave room for the individual to differ from the expectation.|
S~I'd ask what they first noticed that wasn't in the recommendation.
''')
add('mon7', 'gText_ApprenticeMonThanks7', 'The apprentice politely commits to finding the chosen species and hopes for later advice.', '''
S~A clear plan and a kind goodbye. The search is leaving on excellent manners.|
N~They intend to find the chosen species. The future encounter remains to happen.|
N~Find one carefully. Then learn what that individual needs.|
S~I like that their enthusiasm still leaves room to wish us well.|
S~A patient search is a good beginning for a partner they'll care for afterward.|
S~The next step has been accepted without turning it into an extravagant promise of greatness.|
S~A tidy plan, with enough courtesy left over for the farewell.|
N~They should check how the new partner's qualities fit the intended role.|
S~A small decision can become a path toward someone not yet known.|
N~I'd rather they return with a real observation than simply repeat that they obeyed the advice.|
S~I'd be interested to hear how the first meeting went when we see them again.
''')
add('mon8', 'gText_ApprenticeMonThanks8', 'The delighted apprentice plans to raise the recommended Pokemon as well as possible.', '''
S~They're already thinking beyond finding one. That's a very good kind of excitement.|
S~The commitment includes sustained raising, rather than merely obtaining the species.|
S~Good. The daily work matters more than the first decision.|
S~I like hearing them imagine what they can give a partner, not just what it can win.|
S~Doing their best will mean learning the small preferences, too.|
S~A recommendation has been answered with a promise of actual effort. Delightfully substantial gratitude.|
S~The enthusiasm has remembered tomorrow exists. Excellent development.|
N~They can build a routine and revise it as the partner's needs become clearer.|
S~A chosen companion grows into the days somebody makes for it.|
S~Their pride is aimed at caring well. That's a lovely place to begin.|
S~I'd ask what part of raising a new partner they're most looking forward to learning.
''')
add('mon9', 'gText_ApprenticeMonThanks9', 'The energetic apprentice plans to catch the recommended Pokemon and hurries away.', '''
N~A lot of enthusiasm has just promised to cram itself and a new partner into one plan. Carefully, please.|
N~The intention to catch one is clear. A patient encounter will be more useful than haste.|
N~Find one. Don't turn the hurry into rough handling.|
N~I hope the new partner gets a gentle hello beneath all that momentum.|
N~I'd like their eagerness to come with enough time to make the Pokemon comfortable.|
S~The search has departed at a speed normally reserved for arriving late.|
N~Enthusiasm is abundant. Available caution has not yet reported in.|
N~They should slow down enough to observe the actual encounter rather than only its goal.|
N~A living creature needs more room than the excited idea of catching one.|
N~I'd want the rough-sounding phrase to remain only a phrase. The meeting should be kind.|
N~I'd ask them to notice the first sign of the Pokemon feeling at ease.
''')
add('mon10', 'gText_ApprenticeMonThanks10', 'The apprentice jokes about choosing the other species before accepting the advice.', '''
S~They briefly sent our answer back with the wrong address, then rescued it.|
N~The joke is retracted. The intended species remains the one recommended.|
N~Make sure the real choice is clear before they leave.|
F~I thought I'd lost them for a moment. Then the smile caught up with the words.|
S~A playful answer is fine, as long as the future partner isn't selected by a misunderstanding.|
S~The advice has survived a tiny theatrical coup and resumed its original position.|
S~A brief rebellion, followed by remarkably prompt reinstatement.|
N~I'd check their reasoning rather than settle for the promise to obey.|
S~A joke can turn away and return without breaking the thread of a conversation.|
N~I enjoy the playfulness more than the master title. They still need their own judgment.|
N~I'd ask why the chosen species seems useful to them now.
''')
add('mon11', 'gText_ApprenticeMonThanks11', 'The apprentice rhymes their acceptance and plans to find the recommended Pokemon immediately.', '''
S~They've given the new teammate a rhyming invitation. I hope it doesn't demand a matching reply.|
N~The decision is accepted. Immediate enthusiasm shouldn't replace a careful search.|
N~A cheerful plan. Still take the time to find the right individual.|
S~I like how the rhyme makes the prospect sound like something they're glad to do.|
N~I'd rather they bring patience as well as a catchy way to remember the choice.|
S~The species has acquired a brief recruitment verse and an eager prospective trainer.|
S~The search has been set to rhyme. Navigation remains a separate skill.|
N~They can remember the recommendation while still evaluating the partner they actually meet.|
S~A little rhythm can carry a hope a surprising distance.|
N~The playful delivery is theirs. The eventual Pokemon should get room for its own personality, too.|
S~I'd ask what the first meeting did to their neatly rhymed expectations.
''')
add('mon12', 'gText_ApprenticeMonThanks12', 'The apprentice rhymes acceptance of the species advice and asks to be remembered.', '''
S~A new Pokemon to find, a rhyme to carry, and one small wish to stay in our memory.|
N~They trust the recommendation, but it should remain contextual rather than an absolute ranking.|
N~They can follow the advice without thinking every other partner is worse.|
D~The cheerful rhyme nearly hides how much they want the next hello to matter.|
S~I'd remember the person more clearly if we hear what they actually discover.|
S~A practical recommendation has departed carrying a surprisingly tender postscript.|
S~The rhyme is traveling light. The wish beneath it weighs rather more.|
N~I'd ask them to observe the new partner rather than only pursue the label best.|
S~A future meeting begins as a hope someone leaves in the current goodbye.|
N~They want to be known, not simply instructed. I'd keep that difference in mind.|
S~I'd ask them to bring back the story of finding their partner when we meet again.
''')
add('mon13', 'gText_ApprenticeMonThanks13', 'The apprentice accepts the recommended species but postpones seeking one until they feel more capable.', '''
S~They've left room to get ready before meeting the new partner. Sensible little pause.|
N~They plan to act later. The wording doesn't specify exactly what improvement they're waiting for.|
N~No rush. Prepare enough to care for the partner properly.|
S~I like that they haven't made beginning immediately the only way to take advice seriously.|
N~A new companion deserves time and readiness, not just a spare space in a plan.|
S~An enthusiastic recommendation has been received without turning into an emergency errand.|
S~The future teammate has been spared a hurried introduction. Promising start.|
N~They can clarify what readiness means and work toward that concrete condition.|
S~A delayed first step can still be a careful one aimed in the right direction.|
N~I'd want the pause to help rather than become an excuse to doubt themselves forever.|
N~I'd ask what they want to feel more comfortable with before beginning the search.
''')
add('mon14', 'gText_ApprenticeMonThanks14', 'The flustered apprentice agrees to do their best with the chosen Pokemon.', '''
S~They've found a partner to aim for. They don't need to find a completely new personality before trying.|
N~Nervousness doesn't prevent learning. A simple routine may make the new partnership easier.|
N~Do the next small task. Confidence can catch up later.|
S~I understand wanting the Pokemon to meet the calm version of you first.|
N~A patient welcome matters more than pretending never to feel flustered.|
S~A valiant attempt needn't wait for all evidence of nervousness to vacate the room.|
S~The nerves are invited along, provided they don't get sole control of the plan.|
N~We can suggest manageable first steps instead of demanding instant mastery.|
S~A small creature may understand a gentle shaking hand perfectly well.|
N~I'd rather they feel able to learn with their partner than judged for being visibly uncertain.|
N~I'd ask which first task feels manageable enough to begin today.
''')
add('mon15', 'gText_ApprenticeMonThanks15', 'The formal apprentice verifies the recommended species and hopes to handle it well.', '''
S~They've asked for certainty and brought a wonderfully formal word for getting along with a new friend.|
N~Confirming the recommendation is reasonable. Handling the individual will still require observation.|
N~A good choice still takes practice. Nobody needs instant aplomb.|
N~I like that they care about whether they can manage the responsibility well.|
N~I'd explain what the partner may need instead of offering an empty guarantee.|
S~A future companion has been considered with enough dignity to warrant the word aplomb.|
S~The manners are polished. The practical learning may remain pleasantly untidy.|
N~We should describe the role and expected challenges so the choice feels informed.|
S~A careful question can be a kinder beginning than an effortless claim of confidence.|
N~I'd want them to know competence can grow after the first introduction.|
N~I'd ask what part of caring for that species they feel least certain about.
''')
add('item0', 'gText_ApprenticeThanksHeldItem0', 'The apprentice is delighted by an item recommendation and thinks they already own it.', '''
S~They might already have it. Their excitement is definitely in stock.|
N~They believe they own the recommended item. That still needs checking before the plan relies on it.|
N~Check they actually have it before setting the team up around it.|
S~The relief sounds enormous for such a small piece of equipment.|
S~It's nice when useful advice begins with something already close at hand.|
S~A possible inventory match has received the sort of reception normally reserved for major triumphs.|
S~The item may be available. The celebration certainly is.|
N~They should verify the item's effect and whether the intended partner can use it well.|
S~An ordinary object can become a small answer to a long uncertainty.|
N~I'd leave room for checking the cupboard after the happy reaction settles.|
S~I'd ask later whether they found it and how it suited the partner.
''')
add('item1', 'gText_ApprenticeThanksHeldItem1', 'The apprentice accepts the suggested held item and thanks the player.', '''
S~One more decision settled. The partner's pockets are acquiring a plan.|
N~The item is recommended, not transferred. Its actual use remains to be arranged.|
N~A clear choice. Make sure the item's effect fits the partner.|
S~I like seeing them leave less uncertain than they arrived.|
N~An item helps when somebody understands what it's for. I'd explain that part, too.|
S~A neat acknowledgment from someone ready to convert advice into practical preparation.|
S~The equipment question has stopped rattling around for a moment.|
N~They should check the held-item rule alongside the item effect.|
N~A little thing carried well can change the shape of a difficult moment.|
N~I'd rather the choice feel understood than simply fashionable.|
N~I'd ask them what they expect the item to help their partner do.
''')
add('item2', 'gText_ApprenticeThanksHeldItem2', 'The apprentice accepts the item advice and plans to find one.', '''
N~The shopping quest has begun. I hope the item is easier to locate than the confidence to ask.|
N~They haven't obtained the item yet. The recommendation creates a future preparation task.|
N~Find it first. Don't count on equipment that isn't there yet.|
N~I hope searching for it feels like progress rather than another test they might fail.|
N~I'd help them check a sensible source instead of sending them off with only the name.|
N~An answer has become an errand, which is often how practical advice makes its entrance.|
N~The plan has an item-shaped gap and a determined applicant.|
N~We should identify the actual source before assuming availability.|
N~A named need can make a search clearer, though not necessarily shorter.|
N~I'd want to know they have the means to obtain it before treating the choice as finished.|
N~I'd ask where they intend to look first. That might be the next useful piece of advice.
''')
add('item3', 'gText_ApprenticeThanksHeldItem3', 'The apprentice doubts they can obtain the suggested item but resolves to try.', '''
N~They've started arguing with the errand before leaving. I hope the actual item is less intimidating.|
N~The difficulty of obtaining it is uncertain. We can clarify the source rather than rely on optimism.|
N~Find out where it comes from. Effort needs a direction.|
D~I hear the doubt arrive and then the little effort to push back against it.|
N~I'd make sure this isn't an unreasonable burden before praising the determination.|
N~A small item has acquired the proportions of an intimidating expedition. Better directions may help.|
N~The imaginary obstacle is currently better documented than the real one.|
N~We should check the acquisition conditions and suggest an attainable plan.|
N~A vague task can grow teeth in a worried imagination. Name the next step.|
N~They don't have to prove themselves by struggling unnecessarily.|
N~I'd ask what makes it seem difficult to obtain and see whether we can answer that.
''')
add('item4', 'gText_ApprenticeThanksHeldItem4', 'The apprentice accepts the item choice while placing emotional responsibility for losses on the adviser.', '''
N~The item has been selected. Apparently our name will be carrying the emergency cushion.|
N~A held-item recommendation doesn't guarantee results or transfer responsibility for every match.|
N~Know why the item fits. Our name won't make it work.|
N~I want the advice to steady them, not become the only reason they can accept a loss.|
N~I'd explain the useful effect and its limits before letting the promise grow larger.|
N~The equipment recommendation has unexpectedly included a warranty against wounded pride.|
N~The item holds an effect. We appear to have been asked to hold the blame.|
N~They need to understand when the effect helps and when it doesn't.|
N~A small object can't carry every fear attached to the hand that chose it.|
N~I'd rather they gain confidence in the reasoning than depend on who supplied it.|
N~I'd ask what situation they think this item is meant to answer.
''')
add('item5', 'gText_ApprenticeThanksHeldItem5', 'The busy apprentice plans to find time to obtain the recommended held item.', '''
N~One more errand for a calendar already full of elbows. Let's make it a useful one.|
N~Their limited time makes a clear acquisition plan particularly valuable.|
N~Find a practical source. Don't waste the little free time they have.|
N~I hope this choice makes the next attempt easier rather than filling the whole week.|
N~I'd look for the simplest reliable way to get it, not the most impressive one.|
N~The schedule has accepted another small commission on behalf of the battle team.|
N~A busy person has received homework with a shopping component.|
N~We should check availability before they spend their spare time searching randomly.|
N~A small task can still feel heavy when there are already many beside it.|
N~Good advice should respect the life it has to fit into.|
N~I'd ask where the search can fit comfortably into an ordinary day.
''')
add('item6', 'gText_ApprenticeThanksHeldItem6', 'The apprentice calls the held-item choice cool and agrees to test it.', '''
S~The equipment has passed the coolness test. Now it gets the slightly more useful battle test.|
S~They're willing to try the recommendation. Results will matter more than the initial enthusiasm.|
N~Try it, notice what changes, then judge the choice.|
S~I like that they're looking forward to finding out rather than just being told.|
N~I'd want them to see whether the partner actually benefits from it.|
S~An equipment proposal has received an excellent review from the department of first impressions.|
S~Cool now. Useful later, with any luck and some actual observation.|
N~They can compare the expected effect with what happens in a relevant match.|
N~A little borrowed excitement can open the way to a useful discovery.|
N~I'd keep the experiment more important than the stylish name attached to it.|
S~I'd ask them to tell us one moment when the item mattered, if it does.
''')
add('item7', 'gText_ApprenticeThanksHeldItem7', 'The apprentice accepts the item advice and says they will order it.', '''
S~Advice has become an order, in the shopping sense. I appreciate the useful distinction.|
N~They plan to acquire it through an order. Delivery and actual use remain future steps.|
N~Check the order details. Then make sure the item reaches the right partner.|
N~I like that they've chosen a definite way to get ready.|
N~A clear little errand can make a big plan feel more manageable.|
S~The lesson has concluded with a procurement decision and excellent manners.|
S~The recommended item has been summoned through respectable administrative channels.|
N~They should verify the exact item and any time needed before relying on it.|
N~A useful thing can begin its journey toward a person through one clear request.|
N~Their confidence is practical here. They know what the next action is.|
N~I'd ask whether the expected arrival fits when they hope to attempt the challenge.
''')
add('item8', 'gText_ApprenticeThanksHeldItem8', 'The apprentice wonders whether the player uses the same item and plans to obtain it.', '''
S~Now they're curious about our pockets, too. The lesson has developed a follow-up investigation.|
N~Our own use wouldn't establish suitability for every partner. The specific role still matters.|
N~What we carry isn't automatically right for their team. Explain the reason.|
N~I think they want to understand whether this is experience talking or just a suggestion.|
N~I'd answer honestly about the idea without making imitation the whole plan.|
N~The recommendation has prompted a polite request to inspect the adviser's practical credentials.|
S~The equipment is interesting. Our equipment has become interesting by association.|
N~They should adapt the principle to their partner instead of copying a setup blindly.|
N~Another person's tool can point toward a method without becoming a pattern to repeat exactly.|
N~I'd like the curiosity to lead to understanding rather than simply matching our choices.|
N~I'd ask how they think their partner might use the effect differently from ours.
''')
add('item9', 'gText_ApprenticeThanksHeldItem9', 'The apprentice energetically commits to finding the recommended item.', '''
S~That errand has been launched with enough enthusiasm to rattle the shop windows.|
N~The plan is to obtain the item, not evidence that it has already been received.|
N~Find the right item. Speed doesn't fix a mistaken purchase.|
N~I hope they leave enough time to ask questions after the exciting first dash.|
N~A careful check at the counter is worth more than arriving there dramatically.|
S~The procurement expedition has departed at a speed unsuitable for reading price labels.|
N~Plenty of momentum. The exact item name should remain attached to it.|
N~They should confirm the item effect and availability before building the plan around it.|
N~A quick start still needs eyes that notice where the path bends.|
N~I'd keep the exuberance and slow down only the part that can create an avoidable mistake.|
N~I'd ask them to explain what they're buying before they hurry off to find it.
''')
add('item10', 'gText_ApprenticeThanksHeldItem10', 'The apprentice jokes about using any item except the recommended one before accepting it.', '''
S~The recommendation briefly became a list of everything not to buy. Glad we sorted that out.|
N~The contrary plan is explicitly a joke. The intended choice remains our recommendation.|
N~Make the real item clear. The joke shouldn't reach the checkout.|
F~I thought I'd need to explain the whole thing again. Then I realized they were teasing.|
S~A playful lesson is nice. I'd still check the partner ends up with the intended effect.|
S~A momentary rebellion against the shopping list has been withdrawn with full ceremonial obedience.|
S~Defiance has completed its brief shift and handed the item choice back.|
N~I'd ask them to state the item's purpose, so the practical point survives the joke.|
S~A small detour in words can still arrive at the intended thing.|
N~I like the humor better when it doesn't turn learning into performing obedience.|
N~I'd ask what other item they actually considered and why, if they had one in mind.
''')
add('item11', 'gText_ApprenticeThanksHeldItem11', 'The apprentice rhymes acceptance of the held-item recommendation.', '''
S~The item has acquired a little rhyme before it's even arrived. Very well dressed advice.|
N~The choice is accepted. Understanding the effect matters beyond remembering the sound.|
N~A neat answer. Know what the item does, too.|
S~I like how the rhyme makes a practical decision feel cheerful.|
N~I'd want them to remember the purpose just as readily as the item name.|
S~The shopping instruction has become a small verse, an unexpectedly elegant destination for equipment advice.|
S~An item recommendation with matching endings. Very orderly baggage.|
N~We can check the reasoning by asking which situation the item addresses.|
N~A little rhythm can hold a name. Experience will teach it the weight.|
N~They've made the answer their own in one way. I'd like the understanding to be theirs, too.|
S~I'd ask which part of the effect they hope to see first.
''')
add('item12', 'gText_ApprenticeThanksHeldItem12', 'The apprentice accepts the item in rhyme and asks the player to remember them.', '''
S~A small piece of equipment has received a rhyme, a goodbye, and a much more personal footnote.|
N~The response trusts our recommendation while seeking continuity in the mentoring relationship.|
N~We can remember them without promising the item will solve everything.|
D~I hear the wish to be remembered more clearly than the clever wording around it.|
S~I'd like the next meeting to include what they learned, not only what we told them.|
S~A practical purchase has been escorted out by a cheerful verse carrying a sincere little request.|
S~The rhyme has pockets. One appears to contain a softer feeling.|
N~They should observe how the item works instead of treating the recommendation as absolute.|
N~A useful thing can wait in the hand while a different wish waits in the goodbye.|
S~I'd answer the request for recognition plainly. It deserves that much.|
S~I'd ask them to tell us how the partner got on with the item when we next meet.
''')
add('item13', 'gText_ApprenticeThanksHeldItem13', 'The apprentice says the Pokemon arm is fine and accepts the held-item suggestion.', '''
N~Good news about the arm. I'd also check the item is useful rather than merely holdable.|
N~Physical ability to carry it doesn't establish the tactical fit. The effect still matters.|
N~A sound arm helps. Make sure the equipment does its own job.|
N~I'm glad they're thinking about whether the partner can manage it comfortably.|
N~I'd want the Pokemon comfortable with the object, not simply instructed to keep it there.|
N~A practical update on the limb has arrived alongside a somewhat less complete equipment assessment.|
S~The arm is available for duty. The item should justify its appointment.|
N~They should consider both the partner's comfort and the intended battle effect.|
N~A hand can carry something well without the burden necessarily belonging there.|
N~It's a curious detail to volunteer. I'd ask what made the arm part of the question.|
N~I'd want to hear whether the partner seems at ease carrying it after the first try.
''')
add('item14', 'gText_ApprenticeThanksHeldItem14', 'The apprentice accepts the item but feels nervous about how cool it seems.', '''
S~The item is apparently intimidating by being too cool. A very stylish new kind of obstacle.|
N~The item's perceived image is separate from its effect and suitability.|
N~Use it for the job. No need to look impressive while holding it.|
F~I understand feeling as though something nice belongs to a more confident version of you.|
N~Useful equipment doesn't require a trainer to perform a different personality.|
S~A practical tool has unexpectedly acquired social ambitions beyond its advertised effect.|
S~The equipment is causing stage fright before the battle has begun. Efficient.|
N~We can focus on what it does to make the choice less abstractly intimidating.|
S~A thing can feel brighter than the hand reaching for it. That doesn't make the hand unworthy.|
N~They don't need to match the item's imagined image to use it well.|
N~I'd ask which part feels nerve-racking, so we can talk about a real concern instead of the whole feeling.
''')
add('item15', 'gText_ApprenticeThanksHeldItem15', 'The apprentice formally confirms the item advice and hopes the Pokemon uses it well.', '''
S~They've checked the choice and remembered the partner has to do something useful with it. Good thought.|
S~The concern is appropriately about effective use, not simply possessing the object.|
N~Good question. An item needs to suit the Pokemon carrying it.|
N~I like that they're thinking about the partner after the decision, not stopping at the shopping list.|
N~I'd explain the effect clearly enough that they can recognize whether it's helping.|
S~A carefully phrased inquiry into the difference between owning equipment and employing it sensibly.|
N~The item is not expected to succeed purely by being present. Reassuring standard.|
N~We should describe both the useful conditions and the limits of the effect.|
N~A small tool becomes useful through the way a living creature meets it.|
N~I'd rather answer that honest uncertainty than hear another grand claim of guaranteed success.|
N~I'd ask them what sign would tell them the item is doing the job they wanted.
''')
add('noitem0', 'gText_ApprenticeThanksNoHeldItem0', 'The apprentice celebrates settling on no held item.', '''
S~Nothing to hold, plenty to celebrate. That's very efficient packing.|
N~The settled plan is to use no item. It doesn't imply items are always inappropriate.|
N~No item for this choice. Keep the rest of the plan sound.|
S~It's lovely seeing relief arrive even when the answer is simply nothing.|
N~A smaller equipment list still needs a thoughtful plan around the partner.|
S~The absence of a purchase has received a remarkably lavish reception.|
S~Nothing has been selected and enthusiastically applauded. Excellent value.|
N~We should make clear why the empty slot suits this specific recommendation.|
S~An empty hand can feel lighter once the uncertainty leaves it.|
S~Their happiness seems to be about having a clear choice. I understand that.|
N~I'd ask what they'll watch for to decide whether the choice works.
''')
add('noitem1', 'gText_ApprenticeThanksNoHeldItem1', 'The apprentice accepts going without an item and thanks the player.', '''
S~A little less to carry, one less question rattling around.|
N~The no-item recommendation is accepted. The reasoning should remain specific to the current plan.|
N~They understand the choice. Now test it carefully.|
S~I like the simple relief in their answer.|
N~Leaving something out can be deliberate preparation, not forgetting.|
S~A brief lesson in making a decision without acquiring another object.|
S~The empty slot has been successfully appointed.|
N~They can compare the expected tradeoff with the actual results later.|
N~Sometimes making room is itself the useful choice.|
N~I'd want them to feel clear about the reason, not merely relieved we answered.|
N~I'd ask them how the rest of the partner's setup supports that decision.
''')
add('noitem2', 'gText_ApprenticeThanksNoHeldItem2', 'The apprentice briefly confirms the no-item choice and says goodbye.', '''
S~That answer traveled light all the way through the goodbye.|
N~A concise acknowledgment. No held item is the selected advice outcome.|
N~Good. Nothing to fetch before the next preparation step.|
N~I like a quiet thank-you that doesn't make the moment bigger than it needs to be.|
N~I'd still make sure the practical reason is clear before they go.|
S~A tidy conclusion, demonstrating that gratitude need not carry several extra paragraphs.|
S~A lesson with no shopping expedition attached. Highly civilized.|
N~We can review the effect of the decision after an actual attempt.|
N~A small answer can leave without dragging a long shadow behind it.|
N~Their brevity feels comfortable rather than dismissive.|
N~I'd ask one quick question about their plan if anything still seems uncertain.
''')
add('noitem3', 'gText_ApprenticeThanksNoHeldItem3', 'The apprentice interprets the choice as advice not to rely on items.', '''
N~We've left one pocket empty, not banished every item from the universe. Important distinction.|
N~That interpretation is too broad. A specific no-item choice isn't a general prohibition on equipment.|
N~Explain the particular choice. Items aren't a moral weakness.|
N~I don't want them turning one answer into another reason to judge themselves.|
N~Using a useful item isn't failing to try hard enough. I'd say that clearly.|
N~A small recommendation has attempted to grow into an unnecessarily severe philosophy.|
N~The empty hand has been mistaken for a universal doctrine.|
N~We should narrow the conclusion to this partner and this plan.|
N~A lighter choice shouldn't become another heavy rule.|
N~I'd want them to learn flexibility instead of a new way to feel guilty.|
N~I'd give an example of when an item could still be a sensible help.
''')
add('noitem4', 'gText_ApprenticeThanksNoHeldItem4', 'The apprentice accepts no item while treating the adviser as a buffer against disappointment.', '''
N~The partner carries nothing. Our advice has somehow picked up the extra baggage.|
N~Responsibility for later decisions doesn't disappear because we recommended an empty item slot.|
N~Their choices still matter after this one. Explain why it fits.|
N~I hope the reassurance helps them act, rather than only gives them somewhere to place a loss.|
N~A mistake can be understood without needing someone else to own it.|
N~An empty-handed Pokemon has acquired a surprisingly well-appointed arrangement for distributing blame.|
N~No item equipped. One adviser equipped for absorbing disappointment.|
N~They should understand the tradeoff so they can revise it when circumstances change.|
N~A borrowed answer can't hold every feeling the next battle brings.|
N~I'd rather build trust in their judgment than become the name attached to every decision.|
N~I'd ask them what they think the empty slot changes and listen before adding more advice.
''')
add('noitem5', 'gText_ApprenticeThanksNoHeldItem5', 'The busy apprentice appreciates that no item means no acquisition errand.', '''
S~At last, advice that gives a little time back instead of adding another errand.|
S~The choice removes an acquisition task. That is a practical benefit within their schedule.|
S~One less thing to find. Use the time to prepare the team.|
S~They sound relieved to have one part of the day become simpler.|
S~A little spared time can mean a proper rest instead of another rushed trip.|
S~A recommendation whose principal convenience is mercifully visible before anyone leaves the room.|
S~Nothing to buy, nowhere extra to be. A luxurious form of simplicity.|
N~The saved time is useful, though the tactical choice should still make sense independently.|
S~A small task removed can make a crowded day breathe again.|
N~I like advice that respects the person's real circumstances.|
S~I'd ask what they'll enjoy doing with the little bit of time they no longer need to spend searching.
''')
add('noitem6', 'gText_ApprenticeThanksNoHeldItem6', 'The apprentice accepts going without an item and closes the day lesson.', '''
S~Today's puzzle is solved without adding anything to the shopping bag. A tidy little victory.|
S~The advice is accepted and the current lesson ends. Future results remain untested.|
N~Enough for today. Let them work with the decision.|
S~I like that one answer can be enough for one meeting.|
N~I'd leave them with a clear next step rather than keep adding instructions.|
S~The lesson has concluded before either participant could invent an unnecessary equipment purchase.|
S~A small decision, allowed to remain small. Refreshing restraint.|
N~We can ask next time what they noticed while using the setup.|
S~An empty place in the plan can still be settled rather than missing.|
N~The easy goodbye feels like somebody leaving with less uncertainty.|
S~I'd look forward to hearing what they discovered for themselves between lessons.
''')
add('noitem7', 'gText_ApprenticeThanksNoHeldItem7', 'The apprentice clearly accepts no held item and politely promises continued effort.', '''
S~They've taken the answer with both hands, despite the answer being nothing to hold.|
S~The stated understanding and continued effort make a constructive ending.|
N~Keep trying thoughtfully. The empty slot isn't the whole plan.|
S~I like how they send kindness back instead of keeping the whole exchange about needing help.|
S~The next useful thing may simply be noticing how the partner gets on.|
S~A courteous resolution with neither a dramatic vow nor a new errand attached.|
S~No equipment, ample good manners. A manageable load.|
N~They can check whether the rest of the setup supports the decision.|
S~Trust can leave room for a person to keep learning in their own steps.|
S~Their confidence sounds quiet and usable. I like that.|
N~I'd ask for one observation from their next attempt rather than only the final score.
''')
add('noitem8', 'gText_ApprenticeThanksNoHeldItem8', 'The enthusiastic apprentice resolves to continue without an item.', '''
S~They've made an empty hand sound like an exciting piece of equipment. Impressive delivery.|
N~They understand the selected setup. It should remain open to later revision if evidence changes.|
N~Try it properly. Nothing says the choice has to last forever.|
S~I like that they sound ready instead of deprived.|
N~Going without something can be a choice, not a punishment to endure.|
S~A vigorous endorsement of the deliberate absence of accessories.|
S~The empty slot has acquired a very enthusiastic defender.|
N~We should evaluate how the actual partner performs under the intended conditions.|
N~An open hand can still be prepared for the work ahead.|
N~I'd like the confidence to leave space for noticing when another approach would help.|
N~I'd ask what they expect to learn from trying the setup this way.
''')
add('noitem9', 'gText_ApprenticeThanksNoHeldItem9', 'The apprentice energetically accepts the no-item setup and departs.', '''
S~Nothing equipped, enthusiasm fully loaded. That's certainly one way to travel light.|
N~The chosen item state is empty. Their energy doesn't change the need for a coherent strategy.|
N~Good effort needs a plan. Keep both pointed at the same goal.|
S~I hope all that excitement feels good to the partner beside them, too.|
N~I'd rather see steady care than have the whole attempt run on adrenaline.|
S~A spirited departure carrying considerably more confidence than equipment.|
S~The inventory is light. The farewell has enough momentum for several people.|
N~They should check the rest of the setup before turning eagerness into an entry.|
N~A quick current still needs banks if it's meant to carry someone safely.|
N~I'd keep the energy and make the practical instructions short enough to travel with it.|
N~I'd ask what their first step will be after leaving here.
''')
add('noitem10', 'gText_ApprenticeThanksNoHeldItem10', 'The apprentice jokes about equipping something before agreeing to the no-item advice.', '''
S~A shopping trip appeared for one sentence and was canceled in the next. Excellent savings.|
N~The proposed contradiction is a joke. The final accepted instruction is to leave the slot empty.|
N~Make sure nothing is the actual choice when the joke is finished.|
F~I nearly followed the joke into a completely different conversation.|
S~A little play is fine. The partner shouldn't end up with confused instructions.|
S~The imaginary errand has been formally recalled before causing any expense.|
S~A brief equipment rebellion has surrendered to an empty pocket.|
N~I'd check the intended setup plainly rather than rely only on the claim of obedience.|
S~Words can take a short detour and still leave the hands where they were meant to be.|
N~I like the humor. I'd rather their agreement rest on understanding than the master title.|
N~I'd ask why no item makes sense here, just to let them state the idea themselves.
''')
add('noitem11', 'gText_ApprenticeThanksNoHeldItem11', 'The apprentice rhymes that the Pokemon will go empty-handed.', '''
S~An empty hand and a full little rhyme. The preparation is becoming unexpectedly decorative.|
N~The phrasing acknowledges the setup. It doesn't imply the partner has lost a previously held item.|
N~No item selected. Keep the rest of the partner's role clear.|
S~I like the way the rhyme makes it sound deliberate instead of lacking something.|
N~A clear plan doesn't need every possible accessory attached to it.|
S~The absence of equipment has been supplied with a small ceremonial verse.|
S~Empty-handed, but not empty of matching word endings. Efficient compromise.|
N~We can ask what advantage or tradeoff they expect from the choice.|
N~A light hand can still carry intention.|
N~They've given the decision a memorable shape. I'd want the reason to stay just as clear.|
S~I'd ask whether the rhyme helps them remember their choices during a nervous moment.
''')
add('noitem12', 'gText_ApprenticeThanksNoHeldItem12', 'The apprentice accepts no held item in rhyme and asks to remain remembered.', '''
S~They've left the item slot empty and tucked a little wish for another hello into the goodbye.|
N~The empty slot is a specific recommendation, not a universal ideal of being unequipped.|
N~A choice for now. They can revise it as they learn.|
D~I hear the same tender part after the rhyme: please let this meeting have mattered.|
S~I'd remember what they tell us about trying it, not just whether they followed the instruction.|
S~A small piece of tactical restraint has received a surprisingly personal farewell.|
S~No item to carry. A wish to be remembered has taken its place.|
N~They should remain willing to compare other setups once they have useful observations.|
N~An empty hand can leave behind a very real thread between people.|
N~I'd answer the personal wish without promising that the advice is perfect.|
S~I'd ask them to bring one new thing they learned when we meet again.
''')
add('noitem13', 'gText_ApprenticeThanksNoHeldItem13', 'The apprentice says going without an item is easier given current circumstances.', '''
S~A useful choice that makes life a little simpler. Those deserve more applause than they get.|
N~The arrangement fits their present circumstances. We shouldn't infer details they haven't supplied.|
N~If it's easier now, good. Reassess when the circumstances change.|
S~I'm glad the answer lightened something instead of adding another burden.|
N~A plan someone can actually carry out is better than an impressive one they can't maintain.|
S~A practical accommodation, free of any grand claim that difficulty itself is a virtue.|
S~The plan has become easier to live with. An underrated improvement.|
N~We can balance the tactical implications with the constraints they actually face.|
S~A lighter path may leave enough strength for the work that truly matters.|
N~I'd respect the little relief in that answer without asking them to justify every circumstance.|
N~I'd ask whether the simpler setup gives them a clearer way to begin.
''')
add('noitem14', 'gText_ApprenticeThanksNoHeldItem14', 'The apprentice nervously accepts a no-item setup and worries about appearing too cool.', '''
S~Even holding nothing has become intimidatingly cool. The empty pocket has quite a reputation.|
N~The perceived image of the setup is separate from whether it suits the plan.|
N~No item isn't a performance. They can just use the setup.|
F~I understand feeling watched even when the thing I'm worrying about is hardly visible.|
N~I'd want them comfortable with the decision instead of trying to look like the right kind of trainer.|
S~An empty item slot has somehow developed enough charisma to unsettle its prospective user.|
S~Nothing is causing a surprising amount of social pressure. Very accomplished nothing.|
N~We can explain the practical reasoning to give the worry something concrete to settle around.|
N~An empty hand needn't become a pose someone has to hold perfectly.|
N~I'd remind them they don't have to make the choice look impressive for it to be useful.|
N~I'd ask whether they're worried about the battle or about how other people will see them.
''')
add('noitem15', 'gText_ApprenticeThanksNoHeldItem15', 'The formal apprentice accepts going without an item and politely closes the lesson.', '''
S~A quiet acceptance, no errand required. The lesson has packed itself away neatly.|
S~The recommendation is acknowledged without additional claims about the outcome.|
S~A clear answer and a courteous goodbye. Good ending.|
S~I like how they leave room for another meeting without trying to secure it now.|
N~I'd make sure the simple decision feels understood before letting the conversation close.|
S~A perfectly dignified conclusion to the practical business of selecting no object whatsoever.|
S~Nothing chosen, manners intact, future meeting politely possible.|
N~We can revisit the setup after they have actual experience to discuss.|
S~A small decision can come to rest without becoming a grand promise.|
S~Their thanks feels considered rather than automatic.|
S~I'd be glad to hear what they noticed when we next cross paths.
''')
add('move0', 'gText_ApprenticeMoveThanks0', 'The apprentice cries happily after receiving a move recommendation.', '''
S~We've chosen a move and accidentally activated the happy-waterworks technique again.|
N~The recommended move is settled. Learning and using it remain future tasks.|
S~Good to see relief. Now let them learn the move calmly.|
S~I hope their partner gets the same gentle patience they wanted from us.|
S~A useful suggestion can feel like someone helping carry the uncertainty.|
S~Our tactical recommendation has received another unexpectedly emotional ovation.|
S~The tears are an enthusiastic review, if a somewhat damp one.|
N~They should understand what role the move serves in the planned set.|
S~A small answer has loosened a much larger knot.|
N~I'd let them enjoy the relief before adding another pile of instructions.|
S~I'd ask what the partner finds easy or difficult when they begin practicing.
''')
add('move1', 'gText_ApprenticeMoveThanks1', 'The apprentice accepts the advised move and hopes to learn more later.', '''
S~A move picked, a lesson learned, and another question already stretching somewhere nearby.|
N~The choice should be understood in relation to the rest of the moveset.|
N~Useful choice for the plan. Not the best move in every situation.|
S~I like hearing them sound comfortable asking for another lesson someday.|
N~I'd want the partner to have time to practice instead of only collecting instructions.|
S~The recommendation has been received without anyone declaring all other techniques obsolete.|
S~The lesson ends. The syllabus appears determined to survive.|
N~They can test the move's intended role and bring back observations.|
N~A new habit begins long before it feels familiar in the body.|
N~I'd keep their own understanding at the center of the next conversation.|
N~I'd ask when they expect to choose this move over the others.
''')
add('move2', 'gText_ApprenticeMoveThanks2', 'The apprentice plans to teach the recommended move immediately.', '''
S~The lesson has become another lesson, this time for somebody with much less interest in our paperwork.|
N~They plan to teach the move. This acknowledgment doesn't establish that learning has occurred.|
N~Take the time to teach it properly. Right away doesn't mean roughly.|
N~I'd like the first practice to feel encouraging rather than urgent.|
N~A new move needs patience from the trainer as well as effort from the partner.|
N~Our advice is being forwarded to its actual working recipient. May the explanation travel clearly.|
S~The next pupil has not yet received the timetable.|
N~They should check compatibility and how the new move fits the existing set.|
N~A word offered here will become a movement somewhere else. That deserves care.|
N~I'd want the partner's experience to matter as much as the trainer's eagerness.|
N~I'd ask them to notice what makes the lesson easier for their Pokemon.
''')
add('move3', 'gText_ApprenticeMoveThanks3', 'The apprentice doubts whether the Pokemon will learn the advised move for them.', '''
D~They've asked a future lesson to prove the Pokemon likes them. That's a heavy textbook.|
N~Learning difficulty wouldn't establish personal rejection. The two issues should remain separate.|
N~A move can take practice. It isn't a test of being liked.|
D~I understand worrying a struggle means somebody doesn't want your help.|
N~I'd encourage patience without making the partner responsible for fixing the trainer's confidence.|
N~A practical lesson is being asked to settle an entire question of personal worth. Unfair workload.|
D~The doubt has arrived early and is trying to teach the class.|
N~They need a clear teaching method and realistic expectations.|
N~A hesitant beginning isn't always a turned back. Sometimes it is only something not yet understood.|
N~I'd want them to notice progress instead of waiting for a dramatic sign of devotion.|
N~I'd ask what the partner already learns comfortably and build from there.
''')
add('move4', 'gText_ApprenticeMoveThanks4', 'The apprentice accepts the move advice partly to soften future losses by crediting the adviser.', '''
N~The move gets the battle job. Our name gets the job of cushioning any bruised pride.|
N~A recommendation is conditional advice, not a guarantee or transfer of responsibility.|
N~They need to know when to use it, not just who picked it.|
N~I'd like the reassurance to help them learn instead of avoid looking at a difficult result.|
N~A loss can teach something even when nobody volunteers to wear all the blame.|
N~Our lesson appears to include an optional service for outsourcing disappointment. I would decline that part.|
N~The move is selected. The emotional warranty remains unapproved.|
N~They should understand both the move's advantages and its limits.|
N~A borrowed answer can guide a hand without taking over every consequence.|
N~I'd rather they gain trust in the reasoning than depend on our reputation.|
N~I'd ask them for one situation where they would choose something else.
''')
add('move5', 'gText_ApprenticeMoveThanks5', 'The busy apprentice plans to make time to teach the recommended move.', '''
N~A training session has joined an already crowded calendar. I hope it gets a proper seat.|
N~Teaching requires usable time, not merely an intention to fit it somewhere.|
N~Plan a calm practice period. Don't squeeze it into exhaustion.|
N~I hope they and their partner both get to enjoy learning it.|
N~A short patient session may help more than a long rushed one.|
N~The schedule has been asked to produce a lesson without admitting that it is already full.|
S~A busy day has acquired a small educational guest.|
N~We can suggest a realistic practice goal rather than demand immediate mastery.|
N~A little room made carefully can hold more learning than a large hour full of hurry.|
N~I'd want the plan to respect the partner's attention as well as the trainer's time.|
N~I'd ask when both of them are usually most settled and ready to focus.
''')
add('move6', 'gText_ApprenticeMoveThanks6', 'The apprentice praises the move recommendation as cool and ends the lesson.', '''
S~A cool answer about a potentially very uncool day for the next opponent.|
N~The approval is enthusiastic. The move's usefulness still depends on its role and context.|
N~Learn what it does. Cool isn't the whole reason to choose it.|
S~I like that the new idea makes them eager to practice.|
N~I'd want that excitement to become patient work with their partner.|
S~A tactical recommendation has been awarded excellent marks for personal style.|
S~The move has impressed someone before being used. Efficient publicity.|
N~They can compare the expected effect with actual practice.|
N~A bright idea is a beginning, not the whole path it lights.|
N~I'd keep the useful part clear enough to survive after the first excitement fades.|
S~I'd ask which part they most want to try with their partner.
''')
add('move7', 'gText_ApprenticeMoveThanks7', 'The apprentice politely agrees to teach the chosen move right away.', '''
S~A clear answer, a practical next step, and a kind goodbye. That lesson travels well.|
S~They acknowledge the recommendation and intend to apply it. No completed teaching is implied.|
N~Good. Give the partner time to understand it.|
S~I like how their eagerness still leaves room to wish us well.|
N~A lesson goes better when the trainer stays as patient as they sound here.|
S~Our suggestion is headed toward actual practice with remarkably little ceremonial delay.|
S~The next instruction has been received, with manners still functioning.|
N~They should check how the move interacts with the rest of the set.|
S~A little guidance can become a shared discovery between trainer and partner.|
N~I'd want the new routine to feel like cooperation rather than merely carrying out our answer.|
S~I'd be glad to hear how the first practice went when we next meet.
''')
add('move8', 'gText_ApprenticeMoveThanks8', 'The apprentice gratefully repeats understanding the recommended move.', '''
S~They've understood it with enough enthusiasm to make the move sound personally welcomed.|
N~Their certainty about receiving the answer should be followed by understanding its application.|
N~They know the name. Make sure they know the purpose.|
S~The delighted little repetition makes me smile.|
N~I'd turn the excitement toward noticing how their partner learns.|
S~A single answer has been greeted as though it brought several good friends along.|
S~Understanding has arrived with a full-sized celebration.|
N~We can ask them to explain when the move would be useful.|
S~A little clarity can make a mind feel less crowded all at once.|
N~I'd rather let them feel pleased than immediately turn the moment into another test.|
N~I'd ask what they expect to see when the move works as intended.
''')
add('move9', 'gText_ApprenticeMoveThanks9', 'The apprentice energetically plans to have the recommended move taught.', '''
N~The move is getting a very loud introduction. I hope the first lesson has a gentler volume setting.|
N~The stated plan is future teaching. The exclamation doesn't establish successful learning.|
N~Careful practice first. Save the explosive confidence for later.|
N~I'd like the partner to have a chance to understand before the trainer races onward.|
N~Learning isn't always as fast as deciding. The partner deserves that little bit of time.|
S~The announcement has accomplished the dramatic impact well ahead of the actual technique.|
N~The enthusiasm has already made a noise. The move still needs to learn its part.|
N~They should confirm compatibility and use a manageable teaching process.|
N~A quick intention needs patient hands before it becomes a new skill.|
N~I'd keep the energy and slow down the part where somebody is trying to learn.|
N~I'd ask how they'll know the Pokemon feels confident using it.
''')
add('move10', 'gText_ApprenticeMoveThanks10', 'The apprentice jokes about choosing a different move before accepting the recommendation.', '''
S~The advice went on a tiny holiday to another move and came straight back.|
N~The contrary choice is retracted as a joke. The intended recommendation remains unchanged.|
N~Make the real move clear before practice begins.|
F~I thought I had explained something badly for one very small second.|
S~A joke can make learning easier, if it doesn't leave the practical choice muddled.|
S~The student has briefly attempted an educational coup, then restored the lesson with admirable speed.|
S~A rebellion lasting less time than the thank-you. Manageable.|
N~I'd ask why the selected move fits, rather than rely on the promise to obey.|
S~A small turn in the conversation doesn't have to change where the hands eventually work.|
N~I like the playfulness more than the title master. They still need their own judgment.|
N~I'd be interested whether they really considered an alternative and what appealed about it.
''')
add('move11', 'gText_ApprenticeMoveThanks11', 'The apprentice rhymes a plan to teach the recommended move.', '''
S~The move has been sent to practice with a little rhyming escort.|
N~A memorable response can help recall, though application still requires understanding.|
N~Good. Teach it patiently, not just quickly.|
S~I like how they make a practical plan sound like something to look forward to.|
N~I'd want the partner to enjoy the learning as much as the trainer enjoys the rhyme.|
S~An ordinary teaching plan has acquired a jaunty rhythm on its way to the door.|
S~The move's education has been scheduled in verse. Elegant bureaucracy.|
N~They should consider how the technique fits the partner's existing options.|
S~A small rhythm can carry a new idea into the next quiet hour of practice.|
N~I'd like the reasoning to be as memorable as the wording.|
S~I'd ask which part of teaching it they expect to find easiest and which part might need time.
''')
add('move12', 'gText_ApprenticeMoveThanks12', 'The apprentice accepts the move in rhyme and asks not to be forgotten.', '''
S~A move to practice, a rhyme to remember, and a quieter request behind both.|
N~The move is accepted as advice. Calling it best shouldn't erase the importance of context.|
N~A useful choice now. Keep learning when another option fits.|
D~I hear the wish for another meeting more than the clever little farewell.|
S~I'd remember what they discover while practicing, not only what we chose for them.|
S~The lesson has ended with a rhymed departure and a rather sincere request for continued acquaintance.|
S~The rhyme is cheerful. The hope underneath is less protected.|
N~They should observe where the move works and where it doesn't.|
S~A name can linger between two meetings like a thread nobody needs to pull tight.|
N~I'd answer the personal part warmly without making the recommendation sound perfect.|
S~I'd ask them to bring a story about the partner's first successful practice next time.
''')
add('move13', 'gText_ApprenticeMoveThanks13', 'The coughing apprentice plans to teach the move after recovering.', '''
N~The move can wait while they get better. A patient technique won't run off without them.|
N~Postponing practice while unwell is sensible. The recommendation doesn't create urgency.|
N~Rest first. Teach it when they can pay attention properly.|
D~I hope they feel allowed to recover without thinking they've let the lesson down.|
N~I'd want a warm drink and a quiet evening to take priority over another training task.|
N~The curriculum has been asked to respect the inconvenient fact of having a body. Quite reasonable.|
S~The move has no appointment important enough to outrank getting well.|
N~They can return to the practical plan once they have the energy to use it.|
N~A paused lesson can keep its place without costing another little piece of strength.|
N~I'd rather they heard permission to rest than another reminder to be productive.|
N~I'd ask how they're managing today before asking anything more about practice.
''')
add('move14', 'gText_ApprenticeMoveThanks14', 'The apprentice nervously agrees to try teaching the recommended move.', '''
S~One new move, several worried thoughts. We'll make room for the lesson without letting worry teach it.|
N~Anxiety about teaching doesn't establish inability. A clear first step can help.|
N~Start small. They don't have to teach it perfectly in one try.|
D~I know how a small task gets larger when you imagine doing it wrong in front of someone.|
N~I'd explain one patient practice step instead of offering a whole list to feel nervous about.|
N~The technique hasn't begun its lesson and already has a formidable audience of imagined mistakes.|
N~The nerves have arrived early and selected the front row.|
N~They need a realistic method and permission to adjust when the partner needs more time.|
S~A careful hand can learn its own steadiness beside the creature it's helping.|
N~I'd want them to notice progress rather than grade every uncertain moment.|
N~I'd ask which part of teaching feels least clear, so we can work on that one thing.
''')
add('move15', 'gText_ApprenticeMoveThanks15', 'The apprentice formally verifies the move and worries whether the Pokemon can learn it.', '''
N~A very proper question. The move still needs to fit the actual little scholar attending the lesson.|
N~Compatibility should be checked rather than assumed from the recommendation alone.|
N~Check it can learn the move. That's a sensible concern.|
N~I like that they're thinking about the partner instead of treating the answer as automatic.|
N~I'd rather answer the practical doubt than ask them to put faith where a check would do.|
N~A formal request for certainty, best answered with a fact rather than a grand mentorly gesture.|
N~The Pokemon has been granted the reasonable right to have actual capabilities.|
N~We should verify the learning conditions and how the move fits the current set.|
N~A good intention still has to meet the shape of the living creature receiving it.|
N~Their skepticism is useful when it points toward a real detail worth checking.|
N~I'd ask what they already know about the partner's available moves before we continue.
''')
add('lead0', 'gText_ApprenticeMonFirstThanks0', 'The apprentice cries happily when the player chooses a lead Pokemon.', '''
S~The lineup has a first place, and the relief has found its usual watery exit.|
N~The opening partner is selected. Its suitability still depends on likely matchups and support.|
N~Lead chosen. Make sure the next partner supports it.|
S~They sound so relieved to stop weighing the choice alone.|
N~I'd want them to understand the order rather than only feel grateful it exists.|
S~A team-order decision has received an emotional reception of quite disproportionate size.|
S~The first position is settled. The tears remain in vigorous motion.|
N~We should explain what the lead is intended to accomplish.|
S~A little order can let a crowded mind breathe.|
N~I'd let the relief settle before asking them to carry another lesson.|
S~I'd ask what they notice about the opening once they try the lineup.
''')
add('lead1', 'gText_ApprenticeMonFirstThanks1', 'The apprentice accepts the suggested lead and thanks the player.', '''
S~One partner moves to the front, and the whole plan suddenly looks less tangled.|
N~A lead assignment is contextual. It isn't a ranking of the partners' value.|
N~Good. First in line doesn't mean the only one that matters.|
S~I like the simple confidence that comes from understanding the next small thing.|
N~The rest of the team still needs a role after the opening.|
S~A useful decision has been accepted without a ceremony promoting one Pokemon above all others.|
S~The queue has acquired leadership. Mercifully little campaigning required.|
N~They can check how the second partner answers the lead's weaknesses.|
N~A first step gains strength from knowing what can follow it.|
N~I'd keep the explanation about teamwork rather than turn the order into a status contest.|
N~I'd ask why they think this partner should open, now that the choice is made.
''')
add('lead2', 'gText_ApprenticeMonFirstThanks2', 'The apprentice briefly confirms which Pokemon should lead.', '''
S~A wonderfully short appointment with the question of who's first.|
N~The intended opening partner is confirmed. The battle result remains unknown.|
N~Lead settled. Check the rest of the sequence before entering.|
S~I like a decision that can be received quietly and carried away clearly.|
N~I'd make sure the partner behind it isn't left without a plan.|
S~The lineup has been rearranged with fewer words than most people use to say they're ready.|
S~A concise adjustment to the front of the queue.|
N~We should ensure the lead's role and the follow-up are understood.|
N~A small beginning can be clear without promising how the whole path ends.|
N~Their brief thanks feels comfortable. Not every lesson needs a speech.|
N~I'd ask them later whether the opening went the way they expected.
''')
add('lead3', 'gText_ApprenticeMonFirstThanks3', 'The apprentice accepts the lead choice and is deeply grateful for repeated attention.', '''
D~They're surprised we keep answering. I wish help didn't feel like something they had to apologize for receiving.|
N~Repeated questions are part of learning. Their gratitude needn't imply they are a burden.|
N~They asked a fair question. We can answer without making it charity.|
D~I know the feeling of being amazed somebody still wants to listen.|
S~I'd like them to leave knowing their question deserved time.|
N~A small tactical answer has touched a much larger uncertainty about being worth speaking to.|
D~The gratitude is carrying an unnecessary apology in every pocket.|
N~We can explain the lead choice and encourage them to form their own next question.|
S~A listening ear can become a steady place without asking anyone to bow before it.|
N~I'd want them to feel included, rather than endlessly indebted.|
S~I'd ask what they think the next partner should do. Their own ideas belong in the conversation.
''')
add('lead4', 'gText_ApprenticeMonFirstThanks4', 'The apprentice accepts the opening choice while leaning on the adviser for future losses.', '''
N~Our advice is first in line to receive the blame if the opening goes badly. Very prompt appointment.|
N~A lead recommendation doesn't determine every matchup or transfer every consequence to the adviser.|
N~Know the opening plan. Our name isn't part of the moveset.|
N~I want them reassured enough to try, not protected from noticing what they could learn.|
N~A difficult result can be understood without finding one person to carry all of it.|
N~The team has selected an opening partner and an external department for emotional liability.|
N~The lead gets the opponent. We appear to get the complaint afterward.|
N~They should understand the expected role and what could require a different order later.|
N~A borrowed decision can be a step toward judgment, not a place to leave it behind.|
N~I'd rather their confidence grew from seeing the reason than trusting our name alone.|
N~I'd ask them how they'd change the opening against a different kind of team.
''')
add('lead5', 'gText_ApprenticeMonFirstThanks5', 'The busy apprentice accepts the lead order and hurries to meet a waiting girlfriend.', '''
S~A lineup fixed in time to remember a completely different appointment. A very busy heart.|
N~The change is quick, but their waiting companion is a separate obligation worth respecting.|
N~Lead sorted. They should go meet the person waiting.|
S~I like that the battle plan doesn't swallow the whole afternoon.|
N~A promise to meet someone deserves attention, too. The team can wait a moment.|
S~Tactical order restored, romantic punctuality still subject to urgent review.|
S~The Pokemon are in line. The social calendar is sprinting to catch up.|
N~A simple team adjustment fits their limited time better than another large assignment.|
S~A life can hold several important directions at once. One is waiting just outside this conversation.|
S~I'd send them off kindly rather than add another question while someone is already waiting.|
S~I'd ask next time whether they managed to arrive before the apology became necessary.
''')
add('lead6', 'gText_ApprenticeMonFirstThanks6', 'The apprentice happily calls the lead selection cool and ends the day lesson.', '''
S~The front of the line has become a fashionable address.|
N~The lead is chosen. Its tactical role matters more than the approval attached to the decision.|
N~A clear opening. Think through the next partner, too.|
S~They sound pleased to have a picture of how the team will begin.|
N~I'd want every partner to feel part of the plan, not just the one with the first turn.|
S~A queue rearrangement has received an unexpectedly enthusiastic style review.|
S~The first position has acquired considerable social prestige.|
N~They can test whether the opening performs the role we intended.|
N~A beginning can feel brighter once it has a familiar face.|
N~I'd leave room to reconsider if the actual matchups teach something different.|
N~I'd ask what they want the lead to accomplish before the rest of the team enters.
''')
add('lead7', 'gText_ApprenticeMonFirstThanks7', 'The apprentice politely commits to moving the recommended partner to the lead.', '''
S~One small rearrangement, accepted with very good manners. The team is nearly better organized than we are.|
S~They intend to apply the lead choice. The acknowledgment doesn't establish a successful battle.|
N~Put the partner first, then check the whole order.|
S~I like that their thanks still includes a thought for how we're doing.|
N~A useful opening should make the rest of the team's job clearer, too.|
S~The recommendation has become a practical instruction without acquiring a heroic prophecy.|
S~An orderly queue and a courteous goodbye. Much of civilization in miniature.|
N~We can explain which role the lead serves and how the follow-up supports it.|
S~A first step feels steadier when someone knows what follows.|
N~I'd rather they feel prepared than merely obedient.|
S~I'd be glad to hear what the opening taught them during the actual challenge.
''')
add('lead8', 'gText_ApprenticeMonFirstThanks8', 'The apprentice is overwhelmed with gratitude that the player chose the lead for them.', '''
S~The choice has made them so happy I think the lineup may need to wait for the smile to catch up.|
N~They value our involvement strongly. The goal should still be developing their own judgment.|
N~Help them understand it. They won't always have us choosing.|
S~It's touching being trusted that much. It's also something to handle carefully.|
N~I'd like the kindness to become confidence they can carry by themselves later.|
N~Our advisory role has acquired a grandeur normally associated with very rare ceremonial offices.|
S~An ordinary team decision has been warmly mistaken for a small miracle.|
N~They should be able to explain why the lead fits, not only who selected it.|
S~A little help can feel immense when someone expected to stand alone.|
N~I'd be careful not to enjoy the admiration more than helping them become capable.|
N~I'd ask them which partner they'd put second and why. Let their own thinking have a turn.
''')
add('lead9', 'gText_ApprenticeMonFirstThanks9', 'The apprentice energetically accepts the advised lead and plans to reorder the team.', '''
S~The lineup is being reordered at tremendous verbal speed. I hope the Pokemon receive a calmer explanation.|
N~The proposed order is accepted. The practical change still needs to match the intended selection.|
N~Check the order after rearranging. Fast fingers can make mistakes.|
N~I'd like everyone to know what's changing before the next match begins.|
N~The first partner deserves a prepared trainer, not just an excited announcement.|
S~A modest administrative change has been launched with the force of a public event.|
S~The queue has moved. Several exclamations are still following behind it.|
N~They should verify the complete sequence rather than only the first position.|
N~A quick beginning gains value from the quiet choices placed behind it.|
N~I'd keep the enthusiasm and add one careful last look.|
N~I'd ask them to tell us the whole order back, so the plan stays clear.
''')
add('lead10', 'gText_ApprenticeMonFirstThanks10', 'The apprentice jokes about leading with any other partner before accepting the advice.', '''
S~The chosen lead briefly visited the back of the imaginary queue. Everyone seems safely returned now.|
N~The contradictory selection is a joke. The final accepted lead is unchanged.|
N~Make sure the real lineup follows the real answer.|
F~I had a very small moment of wondering whether I'd explained the opposite thing.|
S~A laugh is fine, as long as the partner doesn't receive two different opening instructions.|
S~A tiny mutiny in the line has been resolved before anyone could become inconveniently attached to it.|
S~The queue has survived an imaginary coup. Remarkably resilient queue.|
N~I'd ask why that partner leads, rather than settle for a promise of obedience.|
S~A playful detour can return without unsettling the actual step ahead.|
N~I prefer the joke to the master title. Teamwork needs thought, not reverence.|
N~I'd ask whether their pretend alternative would ever make sense against a different opponent.
''')
add('lead11', 'gText_ApprenticeMonFirstThanks11', 'The apprentice rhymes their acceptance of changing the team order.', '''
S~The partners are being lined up with a little rhythm to the paperwork.|
N~The response accepts the sequence change. The role of the lead still deserves understanding.|
N~Reorder carefully. Make the rhyme easier than the mistake.|
S~I like hearing the adjustment feel cheerful instead of like a correction they should resent.|
N~The order should help the whole team, not make one partner feel like the only important one.|
S~The lineup has been rearranged with considerably more rhyme than the task strictly demanded.|
S~A queue set to verse. It may become easier to remember than the route home.|
N~They can check how each position covers the one before it.|
N~A small rhythm can keep separate steps moving toward one purpose.|
N~I'd want the team logic to remain clear underneath the playful wording.|
N~I'd ask what they expect to happen after the opening partner's first job is done.
''')
add('lead12', 'gText_ApprenticeMonFirstThanks12', 'The apprentice cheerfully accepts the lead choice in rhyme and asks to be remembered.', '''
S~The lineup is settled, the rhyme is complete, and the little wish for another hello has stayed.|
N~They accept the opening decision while seeking continued recognition as a person.|
N~A clear choice. Remembering them doesn't mean we choose every future lineup.|
S~I like the relief. I also hear the quieter part when they ask not to be forgotten.|
S~I'd want the next conversation to include what they worked out themselves.|
S~A tactical adjustment has received a cheerful send-off with a tender request tucked in its pocket.|
S~No distress, according to the rhyme. A little hope remains carefully visible.|
N~They should observe how the lead performs and remain willing to revise the order.|
S~A name can wait between two meetings without being held tightly in either hand.|
N~I'd acknowledge the farewell warmly without letting it turn into a debt.|
S~I'd ask them to tell us something surprising about the opening when we next meet.
''')
add('lead13', 'gText_ApprenticeMonFirstThanks13', 'The apprentice plans to set the lead order after supper.', '''
S~Supper first, lineup second. At last, a training plan with an excellent sense of sequence.|
N~The adjustment is deferred until after a meal. Nothing in the decision requires immediate action.|
S~Eat first. A clear head will still know how to reorder the team.|
S~I like that this lesson has room to be part of an ordinary evening.|
S~A sensible plan. I'd rather rearrange a team after eating than let hunger make every choice.|
S~A grand tactical decision has respectfully taken its place behind supper. As it should.|
S~The lineup can wait in line behind the meal. Appropriately educational.|
N~They should check the full order afterward, rather than rely on remembering only the lead name.|
S~An ordinary meal can be a gentle threshold between one day's questions and the next choices.|
S~They aren't treating every instruction as a demand to hurry. Good.|
S~I'd ask about the meal before bringing the whole conversation back to tactics.
''')
add('lead14', 'gText_ApprenticeMonFirstThanks14', 'The apprentice accepts the lead choice while worrying about becoming flustered.', '''
S~The first partner is settled. The trainer's nerves are still choosing where to stand.|
N~A prepared opening can reduce cognitive load, even if it doesn't remove anxiety entirely.|
N~Have the opening clear. They don't need perfect composure.|
D~I know that wish to do well without the worried part of you becoming visible.|
N~A small routine might help them and the partner feel steadier together.|
N~The lineup is organized. The thoughts have not yet accepted the same arrangement.|
S~The nerves have joined the team without completing registration.|
N~They can rehearse the first decision instead of trying to predict the whole match.|
S~A shaking beginning can still be guided by a steady intention.|
N~I'd want them to feel allowed to pause rather than perform confidence for an audience.|
N~I'd ask what they can check before the first turn to make it feel less sudden.
''')
add('lead15', 'gText_ApprenticeMonFirstThanks15', 'The skeptical apprentice verifies the lead choice and promises their best effort.', '''
S~They checked whether we were teasing before taking the advice. Sensible protection for a serious little plan.|
N~Clarifying sincerity is reasonable. The recommendation should have an explainable basis.|
N~It's a real recommendation. Show them why it fits.|
N~I like that they ask instead of quietly leaving uncertain whether we meant it.|
N~Doing their best doesn't require becoming a different person first.|
N~A formal verification that the mentor has not mistaken a practical lesson for an opportunity to be amusing.|
S~Skepticism has checked the invitation and found the advice genuine.|
N~We should explain the lead's role clearly enough that they can evaluate it themselves.|
N~A careful question can keep trust from being built on a misunderstanding.|
N~I'd rather earn their confidence with a clear reason than ask them to suppress the doubt.|
N~I'd ask what part of the choice surprised them most.
''')
add('farewell0', 'gText_ApprenticeWinSpeechThanks0', 'The grateful apprentice accepts a victory saying, cries happily, and hopes to battle the player someday.', '''
S~They've packed a saying, several lessons, and enough happy tears to water the whole road ahead.|
S~The teaching sequence is complete. A future battle remains an intention, not an arranged result.|
S~They did the learning. They should take some credit with them.|
S~I'm glad the goodbye includes something they want to try for themselves.|
N~I'd like them to battle for their own enjoyment, not feel they owe us every result.|
S~A final lesson has become a farewell with an unusually generous supply of emotion.|
S~The pupil is departing. The tear supply seems determined to outlast the curriculum.|
N~Now the useful test is adapting those lessons to unfamiliar opponents.|
S~A little guidance has become something another person can carry beyond us.|
N~I'd let the gratitude stay warm without letting it turn into a lifelong debt.|
S~I'd love to hear what they discover before that hoped-for battle ever happens.
''')
add('farewell1', 'gText_ApprenticeWinSpeechThanks1', 'The apprentice accepts the saying and leaves eager to improve and meet the player in battle.', '''
S~They've found their own road out of the classroom. I hope the new saying travels comfortably.|
S~They intend to apply the instruction broadly. Experience will supply situations our lessons didn't cover.|
S~Good. Go practice, think, and make the choices their own.|
S~I like the change from asking what to do to sounding ready to try.|
S~Doing their best can mean learning from a hard day as well as enjoying a good one.|
S~The final answer has successfully produced a future opponent. An excellent educational complication.|
S~The student has graduated to threatening us politely with a rematch. Progress.|
N~They should keep observing rather than treat the completed lessons as finished knowledge.|
S~A goodbye can be the first step of a new way to meet.|
S~Their confidence sounds earned through trying, not borrowed only from our name.|
S~I'd ask them to remember one surprise from the first battle they approach on their own.
''')
add('farewell2', 'gText_ApprenticeWinSpeechThanks2', 'The apprentice accepts the saying and plans to seek battles widely, perhaps meeting the player again.', '''
S~The lessons have grown legs and a fairly ambitious itinerary.|
S~Seeking varied opponents can test how well the learned principles transfer.|
N~Different opponents will need different thinking. Keep learning on the road.|
S~I like imagining a familiar face arriving later with stories we haven't heard yet.|
N~I'd want the journey to include care and rest, not only a list of people to challenge.|
S~The graduate has selected the wider world as the next classroom. Sensible choice of venue.|
S~An educational departure with a possible future disagreement conducted through Pokemon.|
N~They can compare what works across different teams rather than assume one plan fits all.|
S~A path away from someone can still curve toward another meeting.|
N~I'd hope they meet people worth listening to as well as people worth defeating.|
S~I'd be curious where they choose to go first and what draws them there.
''')
add('farewell3', 'gText_ApprenticeWinSpeechThanks3', 'The apprentice admires the saying but still doubts their worth and fears being forgotten after leaving.', '''
D~They've learned so much and still think they're the small forgettable part of the story.|
N~Their self-dismissal isn't supported by the effort they've already shown.|
N~They earned the progress. Say that plainly before they go.|
D~That fear of being forgotten makes the goodbye feel much quieter than the words around it.|
N~I'd want them to leave knowing they weren't merely being tolerated through the lessons.|
D~A substantial amount of work has been completed by someone still apologizing for appearing in the room.|
D~The lessons are finished. The old doubt has apparently missed the announcement.|
N~We can point to specific decisions they've learned to make rather than offer vague reassurance.|
S~A person can leave a mark without believing they had the weight to make one.|
N~I'd tell them what I remember about their effort instead of demanding they stop feeling uncertain.|
S~I'd ask them to tell us about their next journey if we meet again. Their story has room to grow.
''')
add('farewell4', 'gText_ApprenticeWinSpeechThanks4', 'The apprentice accepts the final saying, apologizes for being pushy, and sets out with the lessons.', '''
S~They've noticed the elbows in their earlier questions. That's a useful extra lesson to pack.|
S~Acknowledging the pressure they placed on us suggests reflection beyond merely following instructions.|
S~Good apology. Now take responsibility for the next choices, too.|
S~I appreciate hearing them recognize how the conversations felt from the other side.|
S~The best thing they can carry forward may be learning to ask without making the answer a burden.|
S~An unusually satisfying graduation: practical knowledge accompanied by an actual revision of one's manners.|
S~The self-awareness has arrived before departure. Excellent timing.|
N~They can apply the principles independently instead of carrying our exact choices unchanged.|
S~A little roughness can soften before someone steps onto a new road.|
S~The apology makes the farewell warmer. It feels like they see us as people, too.|
S~I'd be interested to hear how their own way of asking and deciding changes after this.
''')
add('farewell5', 'gText_ApprenticeWinSpeechThanks5', 'The busy apprentice accepts the saying and resolves to make time for battling beyond the lessons.', '''
S~They can find time for a sentence. I hope the rest of the adventure gets a reasonable appointment, too.|
N~A wish to continue is clear. A sustainable schedule will matter more than an enormous promise.|
N~Make room for the battles without giving away every break.|
S~I like hearing them choose something for themselves in such a busy life.|
N~I'd want the hobby to add something good to the week instead of becoming another shift.|
S~A graduation ceremony briefly delayed by the continuing logistical problem of having a job.|
S~The adventure has received tentative space in the calendar. Guard that little square kindly.|
N~They can begin with manageable practice periods rather than wait for an entirely empty day.|
S~A road can begin in the small piece of time someone finally keeps for themselves.|
N~I'd like their future effort to be a choice they enjoy, not another obligation to us.|
S~I'd ask what kind of battle they most look forward to making time for.
''')
add('farewell6', 'gText_ApprenticeWinSpeechThanks6', 'The apprentice accepts the saying, recognizes growing competence, and plans to challenge other trainers.', '''
S~They've finally heard their own progress speaking. That's an excellent sound to take on the road.|
S~Their assessment now includes personal improvement, rather than only admiration for the adviser.|
S~They're getting better. Good that they can say it themselves.|
S~I like the small question about being decent. It sounds like confidence finding its own voice.|
S~They've done the practice behind that feeling. They can keep a share of the credit.|
S~The most important statement in the farewell is the discovery that they can do some of this themselves.|
S~The pupil has detected competence in the vicinity. Correctly, for once.|
N~New opponents will let them refine that competence rather than simply repeat familiar answers.|
S~A borrowed light has helped someone notice the light they carry.|
S~I'd celebrate that little bit of self-recognition more than the claim of a perfect saying.|
S~I'd ask what they can do now that felt impossible when they first came to the desk.
''')
add('farewell7', 'gText_ApprenticeWinSpeechThanks7', 'The apprentice finds the saying refreshing and formally leaves to battle many others.', '''
S~A refreshed trainer with a whole road waiting. I hope the saying is easier to carry than all that gratitude.|
S~They regard this as a transition to independent experience. The lessons can support rather than constrain it.|
S~They can remember the teaching and still change the plan when needed.|
S~The formal goodbye feels sincere. I'd want to answer it with equal care.|
N~I'd rather they keep what helps than feel obliged to preserve every instruction forever.|
S~A dignified departure, giving one short saying a remarkable amount of ceremonial work to do.|
S~A new beginning has been declared. No actual rebirth paperwork seems necessary.|
N~They can test the guidance against new situations and revise their understanding.|
S~A farewell can clear a little space for the person who steps through it.|
N~Their respect is lovely. I'd want it to leave them free to become different from the teacher.|
S~I'd like to hear which lesson changes most once they've met a wider range of opponents.
''')
add('farewell8', 'gText_ApprenticeWinSpeechThanks8', 'The overwhelmed apprentice thanks the player for everything and leaves to travel and battle.', '''
S~The joy has packed for the whole trip. I hope they leave a little room for giving themselves credit.|
N~Our guidance contributed, but their participation and future effort belong to them.|
N~They don't owe us everything. They did the learning.|
S~It's moving hearing that much gratitude. I wouldn't want it to make them feel smaller.|
N~I'd like them to leave feeling supported, not carrying a debt for every good thing ahead.|
S~An ordinary mentor has been awarded a frankly implausible share of the credit for another person's life.|
S~The gratitude is enormous. The invoice should remain nonexistent.|
N~They should keep using their own observations as they meet unfamiliar teams.|
S~A gift of guidance can help a person stand. It needn't become something tied around the ankles.|
N~I'd answer the warmth while gently returning some of the achievement to its actual owner.|
S~I'd ask what discovery they're eager to make that nobody has told them about yet.
''')
add('farewell9', 'gText_ApprenticeWinSpeechThanks9', 'The apprentice enthusiastically accepts the saying and hopes for a future battle before departing.', '''
S~A fast goodbye, a new line to try, and the promise of a very lively next hello.|
N~The farewell expresses a future challenge without establishing when or whether it will occur.|
S~Good. Go learn from other teams. We can meet again if our paths cross.|
S~I think the energy will still be in this room a moment after they leave.|
N~I'd want the journey to feel good for the partner beside all that excitement.|
S~A thoroughly energetic graduation, concluding before the punctuation could request a rest.|
S~Several syllables may arrive at the exit before their speaker.|
N~They can use varied encounters to test their plan rather than rely on one confident impression.|
S~Some goodbyes sound less like an ending than a door being flung open.|
S~Their style is entirely their own. I'd like their future choices to become just as individual.|
S~I'd ask for one surprising story if we meet after their travels.
''')
add('farewell10', 'gText_ApprenticeWinSpeechThanks10', 'The joking apprentice accepts the final saying, recognizes learning, and leaves hoping to challenge the mentor.', '''
S~One last tiny rebellion, then off to become a possible opponent. The lessons have grown an excellent sense of mischief.|
S~They recognize growing understanding. That matters more than the repeated promise to obey.|
S~Take the learning. Leave the need for a master behind.|
S~I like that the farewell sounds ready to turn admiration into a fair challenge someday.|
N~I'd rather they carry a thoughtful habit than a rule that our answer must always be followed.|
S~The student has graduated from joking rebellion to the entirely legitimate prospect of defeating the teacher.|
S~Obedience is promised. A future battle suggests the healthy possibility of ignoring us competently.|
N~Independent decisions will test whether they understand the principles beneath the choices.|
S~A good lesson can lead someone far enough away to meet us on level ground.|
N~The title master can stay in the joke. Their actual judgment needs room to grow.|
S~I'd ask them to bring their own plan if we ever meet as opponents.
''')
add('farewell11', 'gText_ApprenticeWinSpeechThanks11', 'The rhyming apprentice accepts the saying, thanks the mentor, and cheerfully leaves the nest.', '''
S~They've packed the farewell, rhymed the luggage, and spelled the departure for good measure. Thorough traveler.|
S~The playful delivery accompanies a clear transition to independent practice.|
S~Ready to leave the nest. Keep thinking when the first plan fails.|
S~I like hearing the goodbye sound so much like them.|
S~A good lesson should eventually make room for someone to go and try.|
S~A final tribute with enough rhyme to require its own luggage allowance. Magnificent excess.|
S~The nest has been vacated through a considerable quantity of verse.|
N~They can take the useful ideas while adapting the actual methods to new conditions.|
S~A bird leaves with more than the sound of the voice that called it forward.|
S~The confidence is playful instead of polished. I'd hate to smooth that out of them.|
S~I'd enjoy hearing which story their next rhyme decides to tell.
''')
add('farewell12', 'gText_ApprenticeWinSpeechThanks12', 'The rhyming apprentice has no questions left, offers an affectionate farewell, and hopes to meet in battle.', '''
S~No questions left, one rhyme overflowing, and a goodbye that seems reluctant to stop waving.|
S~The teaching sequence ends, though future experience will certainly generate new questions.|
S~Go try things. Being out of questions today doesn't mean finished learning.|
F~The affectionate little ending caught me off guard. It feels very sincere.|
S~I'd like them to carry the warmth without feeling they have to return it through victories.|
S~A farewell performing several excellent attempts to end before discovering another line it wanted to say.|
S~The goodbye has packed a possible rematch and forgotten how doors work for a moment.|
N~They can develop their own judgments rather than treat the completed questions as a fixed recipe.|
S~A fond thread can remain without keeping either person from walking away.|
S~I'd remember the warmth more than the rhyme. That's what gives the words somewhere to land.|
S~I'd be glad to hear how the world surprised them after this cheerful departure.
''')
add('farewell13', 'gText_ApprenticeWinSpeechThanks13', 'The emotional apprentice accepts the saying, thanks the player, and declares a new rivalry.', '''
S~Tears, a runny nose, and a rival declaration. They have not let dignity delay the important part.|
S~They are shifting from seeking instruction to proposing equal competition. A meaningful change.|
S~A rival now. Good. They should trust some of their own work.|
S~I like that the tears don't stop them saying what they want next.|
N~I'd still wish them a quiet chance to recover before any grand new campaign.|
S~The pupil has completed the course and issued a rival notice without waiting for the tissues to arrive.|
S~The sniffle is temporary. The newly declared competitive relationship may last longer.|
N~A future contest would let them test an independently chosen plan.|
S~A shaking voice can still speak a new place for itself in the world.|
S~They've found a way to stand beside the person they looked up to. That deserves recognition.|
S~I'd ask them what they most want to try now that they're choosing for themselves.
''')
add('farewell14', 'gText_ApprenticeWinSpeechThanks14', 'The nervous apprentice accepts the saying but doubts being able to deliver it before saying goodbye.', '''
S~They can borrow the words without borrowing a louder voice. A quiet victory still counts.|
N~Difficulty saying the phrase doesn't invalidate their progress as a trainer.|
N~They don't have to perform the line perfectly. The battle comes first.|
S~I understand having the words ready and still finding them difficult to let out.|
N~I'd want the goodbye to leave them less pressured, not with one final test of sounding brave.|
N~A useful education should not end by demanding a flawless public performance from its most nervous student.|
S~The saying can survive being whispered. Remarkably durable thing, a sentence.|
N~They can adapt their delivery instead of treating our wording as a compulsory performance.|
S~A small voice needn't become large to carry something true.|
N~I'd rather they feel like themselves than imitate an idea of the perfect confident trainer.|
S~I'd ask them to remember one thing they accomplished despite feeling nervous.
''')
add('farewell15', 'gText_ApprenticeWinSpeechThanks15', 'The skeptical apprentice carefully accepts the saying, thanks the mentor, and chooses independence.', '''
S~They've checked the final answer twice and then chosen their own road. That's a very respectable goodbye.|
S~Their skepticism can become useful independent evaluation rather than simple reluctance.|
S~They can stop asking permission to think. That's a good next step.|
S~I like the quiet certainty in deciding it's time to go, even after all the questions.|
S~No need to apologize for wanting advice that makes sense. I'd want them to keep that habit.|
S~A carefully considered graduation, complete with a formal release of the mentor from further questioning.|
S~The inquiry has concluded. Independent skepticism is now open for business.|
N~They should retain the habit of checking whether a recommendation fits the actual situation.|
S~A doorway opens differently when someone chooses it for themselves.|
S~Their farewell feels earned because they haven't pretended every doubt vanished.|
S~I'd like to hear which choice they first make differently once they're out on their own.
''')
