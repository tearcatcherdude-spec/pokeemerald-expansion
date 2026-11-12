"""Reviewed League and Battle Frontier human conversation endings."""
ROWS = []
EMOTIONS = dict(N='neutral', S='soft_smile', A='annoyed', F='flustered', D='sad', U='surprised', M='smug', L='laughing')

def add(key, labels, subject, lines):
    replies = [x.strip() for x in lines.strip().split('|')]
    replies = [EMOTIONS[x[0]] + x[1:] for x in replies]
    assert len(replies) == 11, (key, len(replies))
    ROWS.append(dict(key='hpg_'+key, labels=labels.split(), subject=subject, replies=replies))

add('fortree_trade_complete', 'FortreeCity_House1_Text_MonYouTakeCare', 'The Fortree trader welcomes the new partner and bids the traded Pokemon farewell.', '''
S~That was a proper little goodbye. Even a happy swap deserves one.|
S~He welcomed one partner while acknowledging the other. A considerate transition.|
S~Good. He remembered to say goodbye, too.|
S~His excitement softened when he spoke to the one leaving. I noticed that.|
S~A warm welcome and a kind goodbye. Both sides of the trade needed those.|
S~He found room for enthusiasm and manners in the same breath. Excellent work.|
S~One new arrival, one small farewell. Neither was treated like spare luggage.|
S~The exchange is complete. Now both trainers get to learn somebody new.|
S~A welcome can face two directions. His nearly did.|
S~I liked that he addressed both Pokemon. Nobody disappeared into the transaction.|
S~I'd ask him later how they're getting along. That welcome sounded promising.
''')
add('sidney_after', 'EverGrandeCity_SidneysRoom_Text_PostBattleSpeech', 'Sidney accepts defeat and enthusiastically sends the player onward.', '''
S~He lost and still wants us to enjoy ourselves. That's a remarkably sturdy good mood.|
S~His assessment survived a result he disliked. I respect that intellectual flexibility.|
S~A clean loss, a straight answer. Onward.|
S~He didn't make his disappointment our burden. That's kind.|
S~No bitter aftertaste from that battle. He sends us off well.|
L~He introduced himself as the loser and somehow kept command of the room.|
S~Defeat seems to have injured neither his humor nor his hair.|
S~He's already thinking about our next challenge. We should do the same.|
S~He knows when a closed door should become an open one.|
S~He wears defeat comfortably. That takes more confidence than boasting.|
S~I'd enjoy hearing him describe a match he won. This was already lively.
''')
add('phoebe_after', 'EverGrandeCity_PhoebesRoom_Text_PostBattleSpeech', 'Phoebe recognizes the bond behind the player team and accepts her mistake.', '''
S~She spotted what mattered, even if it took a battle to get a good look.|
N~She revised her explanation after observing us. That's a useful habit in an expert.|
S~She gives the whole team credit. Fair assessment.|
S~Being understood after all that effort feels good. Even by an opponent.|
S~She noticed how everyone worked together. That's worth more than a simple compliment.|
S~A gracious correction from someone perfectly capable of making defeat sound mysterious.|
S~She sees the bond now. Apparently it required a fairly forceful introduction.|
S~She found the thing her first assessment missed. Better than defending a bad assumption.|
S~Some ties become visible only when pulled tight. She recognized ours.|
S~She looked past the result and noticed the relationship. I appreciate her eye.|
S~I'd ask what tipped her off. Those little moments between partners interest me.
''')
add('glacia_after', 'EverGrandeCity_GlaciasRoom_Text_PostBattleSpeech', 'Glacia sends the victor onward to test the strength of the League.', '''
N~She makes the next room sound like a very serious second opinion.|
N~Her conclusion is deliberately provisional. The remaining battles will supply more evidence.|
N~She says there's more ahead. Let's prepare before we walk in.|
N~She still sounds composed. I think that makes the warning land harder.|
N~A victory here doesn't refill anyone's strength. Let's check how the team feels.|
N~She concedes the room without conceding the entire League. Quite precise.|
N~The welcome grows colder as the compliments grow warmer. Efficient arrangement.|
N~Another stage of the challenge remains. We have a moment to assess our resources.|
N~Her warning points onward. It would be foolish to mistake it for empty pride.|
N~She hasn't lost her poise. That lends the next opponent a little extra weight.|
N~I'd like to hear her assessment after we've seen the rest. For now, onward.
''')
add('drake_after', 'EverGrandeCity_DrakesRoom_Text_PostBattleSpeech', 'Drake credits a virtuous heart and sends the victor toward the Champion.', '''
S~That's a big compliment from a man with very big dragons. I'll hold it carefully.|
N~He considers a trainer's conduct part of a Pokemon's education. A substantial responsibility.|
N~Strong partners learn from what we do. He's right to remind us.|
S~He spoke about kindness at the end of such a hard battle. I liked that.|
N~They learn our habits along with our commands. We ought to give them good ones.|
S~After all those dragons, the final lesson is decency. I find that rather satisfying.|
S~A good heart survives the room full of teeth. Encouraging news.|
N~He's judging how we guide the team, not merely which moves we selected.|
S~Strength takes the shape of the hands guiding it. His warning is gentle, but serious.|
S~He gives character the same attention as ability. That's a compliment worth keeping.|
S~I'd remember that advice even outside this League. Our partners notice the small things.
''')
add('best_friends', 'BattleFrontier_OutsideWest_Text_BestOutOfAllMyFriends', 'A trainer discovers being strongest among friends does not assure Frontier success.', '''
S~Being the biggest fish at home doesn't stop this pond from having very large fish.|
N~A stronger comparison group changes the ranking, not the value of earlier progress.|
N~New opponents, new lessons. He isn't useless.|
N~It must feel lonely when the thing everyone knows you for suddenly isn't enough.|
S~He's found people who can teach him something. Once the sting wears off, that's useful.|
S~His title survived the journey. Its jurisdiction turned out to be rather small.|
N~The local champion has discovered a much larger locality. Painful, but educational.|
S~Now he has better benchmarks. He can find the specific things holding him back.|
S~A familiar hill can hide a mountain. It doesn't make the climb up the hill worthless.|
N~He's comparing himself so harshly that he's erased the friends he used to impress.|
S~I'd ask what surprised him most in those matches. There's probably a starting point there.
''')
add('seasick', 'BattleFrontier_OutsideWest_Text_GotSeasickOnWayHere', 'An eager visitor is still too seasick to begin battling.', '''
D~The boat won the first match. Let's give him some room to recover.|
N~His enthusiasm arrived before his equilibrium did. A quiet rest seems sensible.|
N~Battles can wait. He needs a steady place to sit.|
D~I won't keep him talking. He looks like every extra word costs effort.|
N~Fresh air, a quiet seat, and no grand challenge for a little while.|
D~His opening opponent was apparently the sea. A notoriously poor sport.|
N~The island is holding still. His stomach has yet to accept the evidence.|
N~He shouldn't have to start a challenge just because he planned to arrive ready.|
S~Even firm ground takes a while to feel trustworthy again.|
N~I think the kindest greeting right now is a little more personal space.|
D~I'll ask about the voyage later. Right now he needs fewer questions.
''')
add('exclusive', 'BattleFrontier_OutsideWest_Text_OnlyToughTrainersBroughtHere', 'A visitor describes the Frontier invitation system and its limited reputation.', '''
U~A whole island that some trainers haven't heard of. Scott keeps a very peculiar guest list.|
N~Selective invitations would explain why knowledge of this place spreads unevenly.|
N~Getting here proves an invitation. What happens next still needs earning.|
N~I wonder how many good trainers simply haven't been noticed yet.|
N~Being invited is exciting. I wouldn't let it make us rude to people outside the list.|
N~An exclusive gathering announcing its exclusivity. The invitation is doing double duty.|
N~A secret known by this many boastful people must require constant maintenance.|
N~Scott's scouting network must cover a lot of ground. Finding people is real work.|
N~Recognition is a gate with somebody else's hand on the latch.|
N~He seems almost as proud of knowing about the place as of being invited.|
N~I'd be curious how each visitor first heard about it. Probably quite a few Scott stories.
''')
add('rental_reassurance', 'BattleFrontier_OutsideWest_Text_BigGuySaidIllLendYouMons', 'One visitor reassures another that the Factory provides rental Pokemon.', '''
S~They came without Pokemon and brought enough nervousness for an entire team.|
N~The rental arrangement resolves their practical concern. Their confidence is catching up slowly.|
N~They should confirm the rules at the desk. Better than reassuring each other indefinitely.|
S~He sounds frightened too, but he's trying to help his friend stay brave.|
S~Asking the staff would settle it. Neither friend has to pretend to know everything.|
S~A reassuring promise delivered with several audible cracks in its foundation.|
S~Two uncertain people have pooled their uncertainty. Somehow it looks a little warmer.|
N~They have the right lead. Next step is confirming how the rental selection works.|
S~Borrowed partners, borrowed courage. Both can be treated carefully.|
S~The scary man's helpful offer seems to be struggling against his first impression.|
S~I'd go ask with them. A clear answer could save a lot of nervous whispering.
''')
add('rental_raising', 'BattleFrontier_OutsideWest_Text_WhosRaisingThoseRentalMons', 'A visitor wonders who raises the Factory rental Pokemon.', '''
N~Somebody must do the work before the impressive entrance. I'd like to meet that somebody.|
N~A rotating rental roster implies substantial husbandry and training behind the facility.|
N~Good question. Strong Pokemon don't prepare themselves for strangers overnight.|
N~I wonder if they have favorite people among the staff.|
S~Feeding that many trained partners must be a serious daily operation. Respect to the crew.|
N~At last, someone has noticed that the impressive attraction requires actual people to run it.|
S~The mysterious unseen worker. Usually found doing all the work.|
U~I'd love to see the preparation routine. A rental system depends on much more than a counter.|
N~Someone knows each one well before a visitor learns its name.|
N~The finished experience hides a lot of care. I'm glad he thought to ask.|
S~That's the person I'd want to interview. They probably know a hundred excellent details.
''')
add('seviper_fear', 'BattleFrontier_OutsideWest_Text_ScaredOfPikeBecauseSeviper', 'A visitor wants to challenge everything despite fear of Seviper and the Pike building.', '''
S~That's a lot of giant snake to walk toward when you're already afraid of snakes.|
N~The architecture is an unusually intense introduction to the subject of her fear.|
N~She can take her time. The building isn't going anywhere.|
S~She admitted she was scared and still wants to try. That counts for something.|
N~Coming this far doesn't mean she owes anybody a panic. A pause is allowed.|
N~The architect certainly committed to the theme. Perhaps a little too successfully for her.|
S~An enormous snake-shaped invitation. Subtlety was presumably unavailable.|
N~She could look at the entrance first and decide afterward. Smaller steps still move forward.|
S~Courage can shudder. I've never understood why people expect it to stand perfectly still.|
N~She wants to go in, but she's allowed to choose the pace of her own entrance.|
S~I'd walk with her if she wanted company. No need to turn it into a spectacle.
''')
add('rps_win', 'BattleFrontier_OutsideWest_Text_WonIllTakePikeChallenge', 'Winning rock-paper-scissors persuades a visitor to attempt the Pike.', '''
L~One tiny victory has opened the gates of the giant snake. A busy pair of scissors.|
N~An unrelated game has supplied confidence. It hasn't supplied a prediction of the challenge.|
S~She's decided. Now she still needs to prepare.|
S~That little win seems to have made starting feel easier.|
S~A cheerful start helps. I'd still check the team before heading in.|
S~The grand campaign begins with a small, decisive hand gesture.|
S~Fate has apparently submitted its opinion through rock-paper-scissors.|
S~Confidence acquired. Practical preparation remains a separate task.|
N~A small omen, freely chosen. The next door will offer its own answer.|
S~She looks much happier now that she's given herself permission to begin.|
S~I'd ask how the challenge went afterward. This is an entertaining beginning.
''')
add('rps_loss', 'BattleFrontier_OutsideWest_Text_LostIllPutOffPikeChallenge', 'Losing rock-paper-scissors persuades a visitor to postpone the Pike.', '''
N~The scissors have canceled an entire day's plans. That's a lot of authority for two fingers.|
N~That result doesn't establish her future luck, though postponing is still her choice.|
N~She can try tomorrow. I'd put more weight on whether her team is ready.|
N~Maybe she wanted a reason to wait. The game gave her one.|
N~If she feels unsettled, a break might help more than another prediction.|
N~An administrative decision issued by a hand game. I question the department's qualifications.|
N~Tomorrow has been asked to provide better luck. A demanding appointment.|
N~A different result wouldn't change the Pike's rules. Preparation gives her something firmer.|
N~An omen can become an excuse very quietly. She still gets to choose.|
N~She seems to need certainty before starting. I don't think this game can really offer it.|
N~I'd ask what worries her about the Pike itself. That might be easier to talk through.
''')
add('fishing', 'BattleFrontier_OutsideWest_Text_ChooseFishingOverBattling', 'A visitor prefers fishing and is disappointed the Frontier offers no catches.', '''
D~An island full of challenges and not one is the patient little fishing kind.|
N~His preferred activity isn't supported here. Competitive density doesn't equal variety.|
N~Fair preference. Not every trip needs a battle.|
N~He came somewhere exciting and couldn't find the quiet thing he enjoys.|
N~I'd help him find a better fishing stop after the visit. Everyone needs their own good day.|
N~Hundreds of formidable opponents, yet no one has arranged an appointment with a fish.|
D~The sea surrounds him in a particularly unhelpful manner.|
N~A place can be excellent at its purpose and still miss someone's favorite pastime.|
N~He can hear the water everywhere. That must make the disappointment rather pointed.|
N~He sounds more surprised by his own preference than he needs to be.|
N~I'd ask about his favorite fishing spot. He probably has much better stories from there.
''')
add('dome_gentleman', 'BattleFrontier_OutsideWest_Text_YoureOffToChallengeDome', 'A gentleman wishes the player luck and hopes to meet as opponents.', '''
S~He wants us both to do well enough to become each other's problem. That's lovely.|
S~A mutually successful path would eventually create a direct competition. He welcomes both parts.|
S~Good manners. I'd be glad to meet him across the field.|
S~He made being an opponent sound like a friendly appointment.|
S~A little goodwill before a hard challenge. There's room for both.|
S~A courteous invitation to a future disagreement conducted entirely through Pokemon.|
S~A promising acquaintance. Potentially dangerous, but very polite.|
S~He's picturing both of us progressing. That's an encouraging way to frame the bracket.|
S~Two wishes for success can share a path until the path narrows.|
S~That was a graceful way to make a rival feel welcome.|
S~I'd remember him if we met again. That greeting gives a match a little history.
''')
add('symbol_determined', 'BattleFrontier_OutsideWest_Text_KeepBattlingUntilIGetSymbol', 'A trainer intends to keep battling until earning a Symbol today.', '''
N~That's a determined plan. I wonder if the Symbol knows it's on a deadline.|
N~Persistence helps, but fatigue can reduce the value of repeated attempts.|
N~Keep the goal. Take breaks before mistakes become habits.|
N~I like the determination. The phrase no matter what makes me a little uneasy.|
N~A whole day of battling still needs meals and water somewhere in it.|
N~An admirable refusal to surrender. I would reserve the right to surrender briefly to lunch.|
N~The Symbol has acquired a pursuer. Hopefully one who remembers to sit down.|
N~A specific goal is useful. Reviewing each attempt would make the effort more useful still.|
N~Resolve burns well. It also needs tending if it's meant to last.|
N~He sounds as though stopping would feel like failure. A break doesn't have to mean that.|
N~I'd ask what he's learned between attempts. That tells me more than the number of battles.
''')
add('dome_entrance', 'BattleFrontier_OutsideWest_Text_WontLetGentlemenBeatMe', 'An older trainer vows to beat the gentlemen but cannot locate the Dome entrance.', '''
L~His rivals are in serious danger as soon as he defeats the problem of the door.|
N~His competitive plan currently depends on resolving a modest navigation problem.|
S~First, the entrance. Then the gentlemen.|
S~He sounded so fierce until he asked where to go. It was rather endearing.|
S~Let's point him toward the entrance before the rivalry gets cold.|
L~A formidable declaration, brought to a temporary halt by architecture.|
S~The first opponent is the building. It appears to be defending competently.|
S~Clearer entrance signs might prevent a surprising amount of wasted competitive energy.|
S~Ambition is pointing straight ahead. His feet require slightly better directions.|
S~I like his confidence. I'd quietly help with the part he hasn't mastered yet.|
S~He'll have a much better story once he's actually found the way in.
''')
add('new_development', 'BattleFrontier_OutsideWest_Text_NothingHereNotLongAgo', 'A visitor marvels at the new Frontier and wants to bring their mother.', '''
S~His first thought after seeing all this was bringing his mother. That's my favorite detail.|
N~Rapid development is impressive. I'd be curious what the site looked like before construction.|
S~He wants to share the surprise. Good reason for another trip.|
S~Some places make you wish a particular person were beside you. He knows who.|
S~A visit with his mother sounds like a good next plan. Plenty here to talk about afterward.|
S~An entire Frontier, and he immediately begins arranging a family outing. Sensible priorities.|
S~A spectacular island has been promoted to somewhere Mother ought to see.|
U~I'd love to compare the construction plans with what stood here before. That's a huge change.|
S~He remembers the empty space. Bringing her will let him tell the story of its filling.|
S~He wants to share the experience instead of simply saying he got here first.|
S~I'd ask whether she enjoys battles too. Either way, he'd have plenty to show her.
''')
add('attention_arrival', 'BattleFrontier_OutsideWest_Text_FinallyArrivedAtFrontier', 'An arriving trainer expects their looks and ability to attract attention.', '''
S~They've brought two kinds of confidence. Let's see how both handle the Frontier breeze.|
N~Ability can be tested here. The amount of attention is a less controllable variable.|
N~They're here. Now comes the part that earns the attention.|
N~It's brave to arrive expecting to be noticed. I'd rather settle in quietly first.|
S~A bright arrival. They'll still need a good routine once the excitement wears off.|
S~They've announced an entrance without requiring anyone to announce it for them. Efficient.|
N~The confidence has arrived ahead of the evidence. It looks quite comfortable.|
S~Enthusiasm is useful starting energy. I'm curious what their team can actually do.|
N~Being seen and being known are different wishes. They seem to want both.|
S~Presentation and skill can work together. Neither guarantees what the crowd will do.|
S~I'd ask which challenge they're most eager to try. That's where the interesting details begin.
''')
add('eating_square', 'BattleFrontier_OutsideWest_Text_SquareFilledWithToughPeople', 'A visitor surveys the formidable crowd while eating.', '''
S~They've assessed the whole square without pausing the snack. Excellent jaw coordination.|
N~A plausible observation, though the invitation system already selects a strong sample.|
N~Eat first. Size up the competition afterward.|
S~They sound comfortable here. Even all these tough trainers haven't spoiled the snack.|
S~A sensible spectator has brought provisions. I'd ask what they're having.|
S~An intimidating crowd receives its verdict between two unhurried bites.|
S~The square is full of danger. The snack remains the immediate priority.|
N~They're taking in the environment before jumping into a challenge. That seems useful.|
S~A formidable gathering becomes a little less solemn with someone quietly munching through it.|
S~They seem impressed without feeling obliged to compete with everyone in sight.|
S~I'd like to know who caught their attention first. They've had time to look around.
''')
add('eating_pike', 'BattleFrontier_OutsideWest_Text_MetOlderGirlAtPike', 'A snacking trainer recalls being defeated by a girl annoyed at their eating.', '''
U~That was a frightening lesson. The snack seems to have declined to learn it.|
N~The defeat changed his account of the opponent, but apparently not his eating schedule.|
N~He lost. He can still choose a better moment for the snack next time.|
N~Being frightened didn't make him stop eating. I can't tell whether that's brave or distracted.|
N~I respect a good snack. I also respect putting it down when somebody needs your attention.|
N~His terrible experience is interrupted by the exact habit that helped make it terrible.|
S~Fear has passed through him. The appetite appears structurally untouched.|
N~I'd separate what he learned about her team from what he learned about her patience.|
N~He remembers the eyes very clearly. Perhaps the rest of the lesson is still arriving.|
N~She wanted his attention. He seems to have given her only the part between bites.|
N~I'd ask about the battle itself once he finishes chewing. That part is still missing.
''')
add('fan_eye_contact', 'BattleFrontier_OutsideWest_Text_LastTimeOurEyesMet', 'A fan insists shared eye contact with the Dome Ace meant sparks flew.', '''
S~Their eyes met, and now the poor moment has to support an entire argument.|
N~Eye contact is observable. The proposed significance is considerably less certain.|
N~They can enjoy the memory without making it a competition.|
F~A glance can feel important. I'd be embarrassed to argue over whose it was.|
S~That memory clearly makes them happy. No need to turn it into a contest at the seats.|
N~A brief glance has been asked to provide sworn evidence of mutual devotion.|
S~Sparks, allegedly. No damage to the seating has been reported.|
N~From a crowded arena, it's hard to establish exactly where somebody was looking.|
N~A small bright moment can grow strange thorns when someone starts defending it.|
N~They want the experience to feel personal. The argument is making it less pleasant.|
S~I'd ask what they enjoyed about the match itself. There must have been more than one glance.
''')
add('fan_loud_cheering', 'BattleFrontier_OutsideWest_Text_DomeAceLookedBecauseOfMyCheering', 'A rival fan claims the Ace looked toward their especially loud cheering.', '''
L~They've promoted volume into proof of affection. My ears request a second opinion.|
N~A loud sound can attract attention. That alone doesn't establish personal preference.|
N~He heard the cheering. That's plenty. No need to shout down the neighbor.|
N~I feel a bit sorry for whoever sat between them.|
N~Cheering should make the day better for the people around you, too.|
N~The argument now measures devotion in volume. A difficult system for everyone nearby.|
N~The loudest person claims victory. A familiar and exhausting method.|
N~They may well have attracted his attention. That doesn't tell us what he thought.|
N~A voice can fill a room and still fail to make its owner feel seen.|
N~They've turned a shared happy moment into a dispute over who owns it.|
N~I'd rather hear why they admire him than hear the cheering reenacted at this distance.
''')
add('fan_exclusive', 'BattleFrontier_OutsideWest_Text_DomeAceIsMine', 'A longtime fan dismisses others and claims exclusive devotion to the Dome Ace.', '''
N~I don't think cheering comes with a deed of ownership. Someone should mention that gently.|
N~Longer admiration doesn't confer exclusive access to the person being admired.|
N~They can support him without treating other fans as trespassers.|
N~It would be hard to enjoy a match with somebody deciding whether I belonged there.|
N~There should be room for another person to discover something you love.|
N~A fan club of precisely one, currently objecting to an alarming membership increase.|
N~The idol has been claimed as private property. I doubt he signed the paperwork.|
N~New fans could make the cheering stronger. They're treating a possible benefit as a threat.|
N~Affection becomes a rather narrow room when only one person is allowed inside.|
N~Calling everyone else insincere won't make their own admiration look warmer.|
N~I'd like to hear how they became a fan, if we can get past the gatekeeping first.
''')
add('fans_were_trainers', 'BattleFrontier_OutsideWest_Text_FansOverThereUsedToBeTrainers', 'An observer explains that defeated accomplished trainers became devoted fans.', '''
U~He beat them so thoroughly they changed which side of the arena they wanted to stand on.|
N~The defeat appears to have transformed their interest rather than extinguished it.|
N~They know enough to recognize what beat them. Credit where it's due.|
S~They found something to love inside a hard loss. I like that part.|
S~At least the loss didn't drive them away from Pokemon altogether. They're still excited.|
U~That must have been a spectacular defeat. It apparently recruited the entire opposition.|
S~A crushing loss with an unusually successful fan-club enrollment afterward.|
N~Experienced trainers can notice impressive choices a casual audience might miss.|
S~They left the battle carrying admiration instead of only a bruise to their pride.|
N~Their expertise makes the admiration interesting. Their squabbling makes it harder to hear.|
S~I'd love their separate accounts of that match. They probably remember different turning points.
''')
add('long_tail_rumor', 'BattleFrontier_OutsideWest_Text_MonWithLongTailInFrontier', 'A visitor delays challenges to seek a rumored long-tailed Pokemon.', '''
S~One unusually long tail has defeated the whole challenge schedule. It must be very persuasive.|
N~A report of tail length doesn't establish temperament or appearance. Still, curiosity is reasonable.|
N~Look carefully. Cute is a guess, not permission to grab it.|
S~I understand putting a crowded challenge aside for a chance to see something small and unusual.|
S~A quiet search could be a good break. I'd keep a respectful distance if we find it.|
S~The Frontier prepared seven grand attractions and has been upstaged by a rumored tail.|
S~An unseen creature has already acquired an admirer. A powerful debut.|
N~We could ask where it was seen before wandering around the entire island.|
S~A rumor has tugged them away from the crowd. Long tails are apparently useful for that.|
S~They've imagined the cuteness already. The real Pokemon deserves a chance to surprise them.|
S~I'd ask the person who saw it where they were standing. Specific details would help.
''')
add('tower_impression', 'BattleFrontier_OutsideEast_Text_BattleTowerFeelsSpecial', 'A visitor is impressed by the size and distinct presence of the Tower.', '''
U~It does seem determined to be visible from every possible direction.|
N~Its vertical scale gives it a different visual presence from the surrounding facilities.|
N~Big building. Still one battle at a time once we're inside.|
N~I think I'd feel very small walking toward it alone.|
N~It makes an impressive landmark. At least getting lost near it would be difficult.|
N~The Tower has declined any invitation to blend into the neighborhood.|
S~A building with no apparent fear of being called conspicuous.|
U~I'd love to know how they planned the structure for that height and all those visitors.|
N~It asks the eye to keep climbing. The feet may have other opinions.|
N~It looks like the centerpiece, even among all these places competing for attention.|
U~I'd want to see how it looks from the far side of the grounds, too.
''')
add('ambition_mimi', 'BattleFrontier_OutsideEast_Text_ConquerLeagueAndFrontier', 'A visitor wants to conquer the League and Frontier before asking Mimi for friendship.', '''
S~That's an enormous errand before saying hello to the neighbor. We could probably shorten it.|
N~Those achievements aren't a necessary prerequisite for asking someone to be friends.|
S~He can ask her now. A no wouldn't erase anything he's earned.|
F~I understand finding excuses to wait. His are much more ambitious than mine.|
S~Maybe start with a greeting. Friendship usually needs conversation more than trophies.|
S~He has placed an extraordinary amount of competitive bureaucracy between himself and hello.|
S~Two mighty institutions stand between him and the girl next door. Neither knows this.|
S~That's a very elaborate dependency chain. I'd try the smallest step first.|
S~He wants enough glory to make a simple question feel safe. It may never work that way.|
S~Mimi might prefer getting to know him before hearing the complete victory list.|
S~I'd ask what they already have in common. There may be an easier opening right next door.
''')
add('pyramid_outside', 'BattleFrontier_OutsideEast_Text_PyramidTooHarsh', 'A frustrated trainer jokes about climbing the outside of the Pyramid.', '''
N~The outside route seems to have fewer trainers and significantly worse handrails.|
N~External climbing wouldn't solve the actual challenge and introduces rather different hazards.|
N~Bad plan. Rest, rethink, use the entrance.|
N~He sounds worn down enough to make an absurd shortcut feel tempting.|
N~Maybe he needs a proper break before another attempt. Frustration isn't good climbing equipment.|
N~An ingenious attempt to avoid the problem by acquiring a much taller problem.|
N~The walls have been mistaken for an alternate admissions policy.|
N~We should review where his attempts fail. Moving the problem outside won't fix the strategy.|
N~A hard path can make every nearby wall look like a door. Usually it isn't.|
N~He wants a way around feeling stuck. I think he needs a fresh plan inside.|
N~I'd ask which part keeps stopping him. The answer might be more useful than a ladder.
''')
add('dark_pyramid', 'BattleFrontier_OutsideEast_Text_ThriveInDarkness', 'A Hex Maniac enthusiastically welcomes the Pyramid darkness and desperation.', '''
N~She says total desperation the way other people say complimentary breakfast.|
N~Her preferred environment differs markedly from the average visitor's comfort requirements.|
N~She likes the dark. I still want a way to see where we're stepping.|
N~Darkness can be peaceful. I'm less sure about the desperation part.|
N~I'd pack carefully before accepting that invitation. Enthusiasm won't find a misplaced supply.|
S~A wonderfully candid advertisement. Absolutely no effort to soften the word desperation.|
S~I appreciate the darkness. I usually prefer to schedule desperation separately.|
N~Low visibility changes how you navigate. I'd plan for it rather than trust the mood.|
S~Darkness has its comforts. She and I may disagree about which ones.|
N~She's found a challenge that suits her whole presentation. That's an impressive match.|
N~I'd be curious what she notices down there that visitors miss while worrying.
''')
add('ultimate_no_sleep', 'BattleFrontier_OutsideEast_Text_PutTogetherUltimateTeam', 'A trainer claims a sleepless week produced an unbeatable Arena team.', '''
N~The team might be ultimate. The trainer sounds one blink away from meeting the floor.|
N~Sleep loss is unlikely to improve the decisions needed to use that team effectively.|
N~A week's preparation deserves a rested trainer. Go sleep.|
N~I can't tell how much of that confidence is excitement and how much is exhaustion.|
N~I'd feed him something simple and point him toward a bed before the Arena.|
N~He has perfected every component except the person currently issuing the commands.|
N~The ultimate team has a very tired weak link standing in front of us.|
N~Testing a design while exhausted makes the results harder to trust. Rest first, then assess it.|
N~He's poured the entire week into a future victory. He should keep some strength for arriving there.|
N~He's proud of the work. Resting would protect that effort rather than diminish it.|
N~I'd rather hear his team plan after he's slept. He might even spot an improvement himself.
''')
add('zigg_treats', 'BattleFrontier_OutsideEast_Text_BelieveInYouBuddy', 'A trainer promises Zigzagoon favorite treats if it wins.', '''
S~Zigg has a personal cheering section and a very specific reason to win.|
N~The promised reward is clearly tailored to the individual. He knows his partner's preferences.|
S~Good to hear him backing his little partner. Keep that up after losses, too.|
S~He sounds so fond when he says the name. Zigg must hear that.|
S~Favorite treats are serious business. I'd ask Zigg which ones top the list.|
S~A heartfelt address, followed by a highly practical incentive package.|
S~The stakes are high. Possibly crunchy. We haven't established the menu.|
S~He's made the reward concrete. Now the battle still needs a sensible plan.|
S~A small creature has someone's whole faith placed gently beside it.|
S~That nickname makes the encouragement feel like theirs alone.|
S~I'd love to hear how Zigg earned its name. He sounds ready to tell us.
''')
add('busybody', 'BattleFrontier_OutsideEast_Text_PeopleCallMeBusybody', 'A compulsive intervenor worries about merely observing at the Palace.', '''
S~He fixed our hat, found some trash, and scheduled dinner before finishing one thought.|
N~A format that removes direct commands may be especially uncomfortable for him.|
N~He'll have to let his Pokemon act. That's the Palace rule.|
N~He notices every small thing. Letting go must take a lot of effort.|
S~Remembering dinner is useful. Correcting everybody else's evening may be less welcome.|
S~A man attempting to supervise the entire island has encountered a no-supervision challenge.|
N~Even the litter has received instructions. The Palace should be educational.|
N~He could practice observing without correcting. Start with something smaller than a battle.|
N~Still hands can be harder work than busy ones. He's about to discover how much.|
N~Helpful attention can feel intrusive when nobody asked for the help.|
S~I'd ask what he notices when he gives himself a minute without acting on it.
''')
add('older_glory', 'BattleFrontier_OutsideEast_Text_OnceBeatGymLeader', 'An older trainer considers returning to competition after a past Gym victory.', '''
S~A victory doesn't expire just because the trainer has acquired more birthdays.|
N~His past success is relevant experience, though a return would test his current preparation.|
S~Give it a try if he wants. No need to apologize for being older.|
S~That old win still makes him brighten. A new attempt might mean a lot.|
S~He can return at his own pace. There's no need to recreate his younger self exactly.|
S~He has a perfectly good achievement and is considering another. An excellent use of history.|
S~The retired glory appears to be considering part-time employment.|
S~I'd start by seeing what his team can do now. Experience gives him a useful foundation.|
S~An old fire has stirred. It needn't burn exactly as it once did.|
S~I dislike that he feels obliged to explain his appearance before his achievement.|
S~I'd ask about that Gym match. People remember remarkable little details after years.
''')
add('fast_cyclist', 'BattleFrontier_OutsideEast_Text_FastOnBikeAndBattles', 'A cyclist boasts of speed both riding and winning battles.', '''
S~Fast wheels, fast wins. I wonder if he takes his victory lap before anyone notices.|
N~Quick wins suggest decisive matchups. Speed alone doesn't explain the underlying choices.|
N~Quick is useful. Knowing when to slow down is useful, too.|
N~I might need him to describe one of those matches more slowly.|
S~A quick match leaves more time for a proper meal afterward. Sensible scheduling.|
S~He appears committed to giving both opponents and scenery very little time with him.|
N~A man in a hurry, even while boasting about being in a hurry.|
N~I'd like to know which decisions let him finish so efficiently.|
N~Speed makes a clean promise. A difficult opponent may ask him to amend it.|
S~He's made quickness his signature. It's a memorable introduction.|
S~I'd ask for one specific match story before he speeds off again.
''')
add('daughter_skill', 'BattleFrontier_OutsideEast_Text_BetterThanDaddyAtPokemon', 'A girl confidently says she is better at Pokemon than her father.', '''
S~She has measured the family rankings and sees no need for a committee.|
N~She sounds confident in that comparison. I'd be interested in how they practice together.|
S~Good for her. He seems proud enough to survive it.|
S~She says it so simply. No grand speech required.|
S~A child getting better than her parent can be a happy milestone for both.|
S~A concise family assessment. Father has apparently lost the deciding vote.|
S~The household hierarchy has been updated. Daddy seems likely to receive a notice.|
S~Teaching someone who eventually surpasses you is a successful result.|
S~Growing past someone's reach needn't mean leaving their affection behind.|
S~She's comfortable taking credit for her skill. I'm glad she can.|
S~I'd ask whether they battle each other often. It sounds like an entertaining household.
''')
add('father_cheers', 'BattleFrontier_OutsideEast_Text_GoRackUpSomeWinsForDaddy', 'A father cheers his daughter and compares her skill to her mother.', '''
S~He's cheering for the next generation and complimenting the previous one at the same time.|
S~He sees a family resemblance in ability. His enthusiasm seems quite genuine.|
S~He knows she's good. He's not pretending otherwise to protect his pride.|
S~It must feel good to know he believes in her that openly.|
S~That's a proud dad. I bet he'll remember every match more loudly than she does.|
S~A family with one very enthusiastic supporter and apparently two formidable competitors.|
S~He sounds thoroughly outmatched at home and delighted about it.|
S~Recognition from somebody who knows her well can help steady the nerves.|
S~His pride has room for both of them. A warm sort of inheritance.|
S~He makes the resemblance to her mother sound like the highest possible compliment.|
S~I'd ask whether her mother came along. This sounds like a whole family of stories.
''')
add('scott_never_battles', 'BattleFrontier_OutsideEast_Text_DidScottBringYouHere', 'A visitor observes that Scott spots talent but has never been seen battling.', '''
N~Scott has found all these trainers without once demonstrating how he handles a tackle.|
N~Recognizing expertise and performing it are related but distinct abilities.|
N~He recruited the talent. That doesn't tell us what he can do in a battle.|
N~I hadn't realized how little we know about that part of him.|
N~Some people are better at bringing a team together than taking the field themselves.|
N~He has assembled a remarkable guest list while leaving his own entry strangely blank.|
N~A man surrounded by battle records who has supplied none of his own. Neat trick.|
N~Scouting skill is evident. His competitive skill remains untested evidence.|
N~He's very good at opening doors for others. His own door remains shut.|
N~He directs attention toward everyone else's ability. People are starting to notice the gap.|
N~I'd ask him if he enjoys battling. A simpler question than guessing at a secret history.
''')
add('arena_spectator', 'BattleFrontier_OutsideEast_Text_HeardPrettyGirlAtBattleArena', 'A visitor complains the Arena crowd differs from the attractive girl he expected.', '''
N~He traveled all this way and forgot the battle part of Battle Arena.|
N~His expectation concerned one person's appearance rather than the purpose of the facility.|
N~People are there to battle. They don't owe him a pleasing view.|
N~Those martial artists didn't do anything wrong by being there.|
N~He might enjoy the trip more if he gave the actual matches a chance.|
N~A man disappointed that a martial contest contains martial artists. An ambitious complaint.|
N~The Arena has failed to organize itself around one stranger's taste. Tragic, apparently.|
N~He should check the event before planning a trip around a rumor.|
N~He brought a narrow expectation. The crowd has politely refused to fit inside it.|
A~He could have kept the insults to himself. Nobody here was hired to decorate his visit.|
N~I'd rather talk to the people who came for the battles. They probably have better observations.
''')
add('palace_old_man', 'BattleFrontier_OutsideEast_Text_SometimesImportantOldManInThere', 'A child describes a kind older Palace visitor with impressive Pokemon.', '''
S~Awesome Pokemon and a nice person. That's a much better combination than awesome and unbearable.|
N~The child separates his imposing presence from his actual manner. A useful distinction.|
S~Strong doesn't have to mean unfriendly. Good that the kid has seen that.|
S~He noticed the kindness after the impressive entrance. I like that.|
S~A powerful team is easier to admire when its trainer treats people well.|
S~An important-looking gentleman who hasn't let the appearance become an obligation to be unpleasant.|
S~The formidable old man turns out to be nice. A welcome breach of expectation.|
N~I'd be curious how he works with those Pokemon under the Palace rules.|
S~Some people carry authority lightly enough that a child can approach it.|
S~He made an impression without frightening the child. That's a good kind of presence.|
S~I'd ask what made him seem nice. Children often remember exactly the thing adults overlook.
''')
add('invented_legend', 'BattleFrontier_OutsideEast_Text_LegendOfBattlePyramid', 'A visitor improvises a Pyramid legend and admits it has no established meaning.', '''
L~A freshly baked ancient legend. Still warm, and nobody knows what's inside.|
N~He disclosed the invention immediately. At least the provenance is unusually transparent.|
N~Fair enough. As long as he doesn't pass it off as history.|
S~He sounded so solemn. Then he admitted it, and I nearly laughed.|
S~He invented it on the spot and told us so. Harmless fun with honest labeling.|
L~I admire the immediate confession. Most invented legends insist on several centuries of dignity first.|
S~An ancient tradition born moments ago and already unsure of its purpose.|
S~He's testing an idea aloud. It clearly still needs a few design decisions.|
S~A new tale has no roots yet. He seems content to let it wander.|
S~The delivery was grand enough to make the admission much funnier.|
L~I'd ask him again tomorrow. He may have invented an entirely different meaning by then.
''')
add('first_crushing_loss', 'BattleFrontier_OutsideEast_Text_GotWipedOut', 'A previously unbeaten trainer reels from a crushing loss and an insult to his talent.', '''
D~Losing for the first time is hard enough without somebody stamping an insult on top.|
N~One defeat disproves invincibility. It doesn't establish an absence of talent.|
N~He lost a battle. Whoever called him talentless was adding noise.|
D~He sounds hurt underneath all that anger. I wouldn't make him explain it twice.|
N~Let him cool off before picking apart the match. Right now everything feels personal.|
N~The result was clear enough without an unsolicited verdict on his entire future.|
N~An undefeated record has broken. The person attached to it is still intact.|
N~He can examine the decisions later. First he needs to separate the result from the insult.|
N~One fallen certainty can sound like the whole world falling. It isn't.|
D~He had never practiced being the person who loses. That part takes learning, too.|
N~I'd ask about one turning point once he's ready. A whole career is too much to judge at once.
''')
add('tower_warning', 'BattleFrontier_OutsideEast_Text_ToughTrainerInBattleTower', 'An observer warns that a nearby trainer suffered a difficult Tower defeat.', '''
N~The warning is useful. Pointing at the poor fellow adds a little too much demonstration.|
N~His account establishes a difficult opponent exists, though not how often we would meet them.|
N~We'll prepare. He should give his friend a minute to recover.|
D~It's hard enough losing without becoming the example everyone points at.|
N~A warning can help us without making the other trainer feel smaller.|
N~A cautionary tale is standing right there, apparently without being asked to participate.|
N~The Tower is dangerous. So is becoming the local public-service announcement.|
N~Knowing a tough opponent exists is useful. Learning how they battled would help more.|
N~Someone else's wound is being used as a signpost. A gentler warning would do.|
N~He may mean well, but his friend's embarrassment probably doesn't need an audience.|
N~I'd listen to the trainer's own account if he wanted to share it.
''')
add('plush_points', 'BattleFrontier_OutsideEast_Text_EnoughBattlePointsForDoll', 'A visitor has earned enough points for another giant plush doll.', '''
S~All that fierce battling has produced a very large, very soft objective. Excellent.|
S~A tangible personal goal can sustain effort better than an abstract ranking.|
S~Earned enough for something they want. Good for them.|
S~They sound genuinely excited. I'd like to see which one they choose.|
S~A giant plush seems like a comfortable reward after so many hard battles.|
S~The campaign concludes in upholstery. I thoroughly approve of this ambition.|
S~A formidable trainer is about to acquire another extremely huggable dependent.|
S~They planned for a specific reward and reached the point total. Satisfying work.|
S~A hard-earned softness. There are worse things to carry home.|
U~Another giant one? I need to know how they've arranged the first ones.|
S~I'd ask about the collection. That word another is doing interesting work.
''')
add('posterity', 'BattleFrontier_OutsideEast_Text_LikeToHaveNameRecordedHere', 'A trainer wants a lasting place in the Ranking Hall.', '''
S~A name on a wall is a fine goal. First it needs a few very busy battles underneath it.|
N~The record would document a specific performance. Longevity depends on what later challengers do.|
N~He's found the goal. Now he needs the work that gets him there.|
N~Wanting to be remembered feels bigger than simply wanting to win.|
S~It could be something lovely to show people later. He'll have to earn the entry first.|
N~Posterity has a reception desk here. Apparently it requests excellent battle results.|
S~Immortality, with competitive admission requirements.|
N~He could pick a facility and measure his progress toward its listed records.|
N~A name can stay on a wall while its owner keeps changing. I wonder which part he wants preserved.|
N~He already imagines how the name will look. I wonder which achievement he wants beside it.|
S~I'd ask why being remembered matters to him. There's usually a good story behind that wish.
''')
add('couple_confidence', 'BattleFrontier_OutsideEast_Text_CanDoAnythingWithYou', 'One partner expresses absolute confidence from being beside the other.', '''
S~That's sweet. I'd still bring a plan for the things affection can't tackle directly.|
N~A trusted partner can improve confidence. Unlimited ability is a more poetic claim.|
S~Good to have someone you trust. Stay ready to help them, too.|
F~They said it so easily. I think I'd need a moment before answering.|
S~Being on the same side matters. I like hearing them say it out loud.|
S~A magnificent promise. I trust neither has been asked to move the Tower by hand.|
S~Together they can do anything. Presumably including accepting reasonable exceptions.|
S~Trust makes cooperation easier. The details of the plan will still matter.|
S~Some hands make the next step feel possible before anything else has changed.|
S~It sounds less like showing off and more like telling one person they matter.|
S~I'd be curious how they first became partners. They seem very comfortable together.
''')
add('couple_multi', 'BattleFrontier_OutsideEast_Text_PowerOfOurLoveWillOvercome', 'An enthusiastic partner expects their love to conquer the Multi Battle challenge.', '''
S~Love has entered the tournament and is making very bold predictions about the bracket.|
N~Mutual trust should help their coordination. Opponents will still require specific responses.|
N~They'd better talk tactics as enthusiastically as they talk about each other.|
F~They really don't mind everyone hearing. I'm a little impressed.|
S~They sound happy. I'd also check that both of them know the plan.|
L~A romantic declaration with collateral damage promised to every team in the building.|
S~Affection has become a competitive hazard. Nearby dominoes should seek shelter.|
S~The shared enthusiasm is excellent. They'll need to account for their partners' moves together.|
S~They see a straight path because they're looking toward the same thing. The arena may bend it.|
S~They're enjoying being a pair. A difficult match will test how well they listen, too.|
S~I'd ask afterward whether the teamwork matched the prediction. They're making it memorable.
''')
add('scott_objective', 'BattleFrontier_OutsideEast_Text_FrontierNotExclusivelyForToughTrainers', 'A visitor speculates that the variety of invited talents reflects a larger purpose.', '''
N~There are plenty of unusual talents here. Scott's guest list is more interesting than a win chart.|
N~The varied invitations are observable. His proposed larger objective remains speculation.|
N~Maybe Scott has a bigger plan. We can ask before inventing one.|
N~I like that there might be room here for more than the loudest battlers.|
S~A gathering works better with people who bring different things to it.|
N~A mysterious objective is possible. So is a man who simply enjoys assembling interesting people.|
N~The suspicion has a promising shape and no confirmed contents yet.|
N~Different specialties make the whole place more capable. That part needs no secret explanation.|
N~A place can serve more than one purpose. We haven't been handed its hidden one.|
S~I'm glad someone noticed the people whose talents don't fit a battle score.|
N~I'd ask what special abilities they've actually seen. That gives us something firmer to explore.
''')
add('wiggling_tree', 'BattleFrontier_OutsideEast_Text_OddTreeHereSeemsToWiggle', 'An older visitor asks whether an unusual tree is really moving.', '''
U~If the tree is wiggling, I don't think her eyes are the part causing trouble.|
N~Independent observation could distinguish actual movement from a visual impression.|
N~We can look. Give the odd tree some space until we're sure.|
N~She asks so gently. I'd like to help her check.|
N~No reason to dismiss her just because she's tired. Let's see what she noticed.|
N~A tree behaving suspiciously is a perfectly respectable reason to request a second witness.|
S~I dislike vegetation that makes eye contact with my doubts.|
N~We should observe it for a moment before deciding whether the movement is real.|
N~Some things seem rooted only because we haven't stood quietly enough beside them.|
N~She noticed something odd and asked for another opinion. Sensible, really.|
N~I'd ask when she first saw it move. Then we can watch the same spot.
''')
add('tree_gone', 'BattleFrontier_OutsideEast_Text_OnceAnOddTreePastHere', 'After the unusual tree is gone, the visitor asks whether her memory is accurate.', '''
N~Now the tree's gone and she's doubting a different part of herself. Poor thing.|
N~A changed location doesn't invalidate a previous observation. Memory and present evidence differ.|
N~She remembers something real. We can reassure her about that.|
D~I'd tell her she didn't imagine it. That seems important.|
S~A simple answer could put her mind at ease. No need to make a mystery out of it.|
N~The tree has departed and left its former observer to defend the evidence alone.|
N~An absence with unusually poor manners. It could at least have left a note.|
N~We can confirm that the place changed rather than making her question her memory.|
N~An empty patch can make a clear memory feel very small. It shouldn't have to.|
N~She deserves a straightforward answer instead of a joke about getting older.|
N~I'd tell her what we know. There's no reason to leave her wondering whether she imagined it.
''')
add('sticky_sighting', 'BattleFrontier_OutsideEast_Text_StickyMonWithLongTail', 'A camper describes a sticky long-tailed Pokemon hiding beneath a boulder.', '''
U~A sticky stranger under a rock was staring back. That's a very good reason to blink first.|
N~We have a location and several physical observations. More useful than the earlier rumor alone.|
N~Look from a distance. Don't reach under a boulder after something startled.|
N~It might have been as surprised to see him as he was to see it.|
N~If it's hiding, I'd give it room. Curiosity doesn't require pulling it out.|
N~The rumored tail now comes with a boulder and a rather pointed stare. Details are accumulating.|
S~The hidden observer has been observed. Neither party appears pleased by the arrangement.|
N~I'd check the surroundings before approaching. That boulder may conceal more than the Pokemon.|
N~It chose shelter and still kept an eye on the world. A familiar compromise.|
N~He sounds startled, which is fair. An unexpected stare can make a small encounter feel enormous.|
U~I'd ask which boulder and how far away he stood. Quiet observation seems the best next step.
''')
add('judge_good', 'BattleFrontier_Lounge1_Text_StatRelativelyGood', 'The expert calls the assessed stat relatively good.', '''
S~A good quality in that stat. Small praise still deserves a little smile.|
N~That assessment applies to the particular stat he identified. It isn't an overall verdict.|
N~Useful to know. One trait doesn't decide the whole partner.|
S~He found something good there. I'd keep the rest of the Pokemon in mind, too.|
S~A useful strength to work with. No need to turn it into a demand for perfection.|
N~A modest compliment, delivered with the gravity of a royal proclamation.|
S~Relatively good. The elder has opened the smallest drawer in his praise cabinet.|
N~That's one useful detail for planning. It doesn't replace checking the rest of the team.|
S~One good thread in a larger weave. The whole creature is still there.|
N~It's a measured compliment. We don't have to make it smaller by comparing endlessly.|
N~I'd ask how that strength shows itself in practice. Numbers become interesting when they matter.
''')
add('judge_impressive', 'BattleFrontier_Lounge1_Text_StatImpressive', 'The expert calls the assessed stat quite impressive.', '''
S~That stat got a proper nod from the expert. Nicely done, little partner.|
N~He rates that particular attribute highly. A useful distinction from his overall assessment.|
S~A real strength. Let's use it well.|
S~I like that he sounds pleased to find something impressive.|
S~That's something to feel good about without making every other quality a competition.|
S~The expert has moved beyond polite approval. His eyebrows may even have participated.|
S~Impressive enough to earn an entire sentence of approval. A generous day.|
S~Now we know a strong part of the design. The plan can account for it.|
S~A bright quality noticed by an old eye. It was there before he named it.|
S~Specific praise feels better than a vague compliment. This gives us something clear.|
S~I'd be interested to see when that quality makes a difference in a close match.
''')
add('judge_outstanding', 'BattleFrontier_Lounge1_Text_StatOutstanding', 'The expert calls the assessed stat outstanding.', '''
U~That stat has earned the big compliment. I think it can stand a little taller now.|
S~An excellent assessment of the identified attribute. It doesn't imply every attribute matches it.|
S~Strong trait. Good information to have.|
S~He sounds certain. I think our partner deserves a quiet bit of praise, too.|
S~That's a lovely strength. It still belongs to a whole Pokemon we care about.|
S~Outstanding, pronounced with all the ceremony the word seems to require.|
S~One stat has distinguished itself from the crowd. Quietly smug behavior is now understandable.|
S~That's a significant strength to factor into training and battle choices.|
S~Something exceptional has been seen clearly. Naming it doesn't create it, but it can help.|
S~It's good to have the compliment aimed at something specific instead of just a ranking.|
S~I'd ask what surprised him about it. An expert's small observations can be fascinating.
''')
add('judge_flawless', 'BattleFrontier_Lounge1_Text_StatFlawless', 'The expert calls the assessed stat flawless, without implying all stats are perfect.', '''
U~A perfect mark for that stat! Even the stern little grading pencil seems pleased.|
S~That attribute meets his highest standard. We should keep its scope precisely in mind.|
S~Can't improve that particular mark. Plenty else still matters.|
S~That's such emphatic praise. I'd probably be smiling at our partner for a while.|
S~A perfect mark is lovely. Being cared for never depended on earning one.|
U~The expert has reached the ceiling of his vocabulary. A memorable occasion.|
S~One flawless stat. The universe has allowed a small exception to its usual untidiness.|
S~That's the upper limit for this assessment. Now we can plan around that confirmed strength.|
S~A small perfection in a living, changing creature. No need to ask the rest to imitate it.|
S~An excellent quality, clearly recognized. We can celebrate it without demanding eleven more.|
S~I'd remember the look on the trainer's face when he said that. Good news lands visibly.
''')
add('judge_cancel', 'BattleFrontier_Lounge1_Text_NoTimeForMyAdvice', 'The breeder scolds the player for declining his assessment.', '''
N~I can respect seventy years of experience and still have somewhere else to be.|
N~His expertise deserves consideration. It doesn't make every declined consultation disrespectful.|
N~We said no to advice, not to his entire life.|
F~I didn't mean to upset him. I just wasn't ready to show a Pokemon.|
N~A useful offer is still an offer. There's no need to season it with guilt.|
N~A consultation politely declined has somehow become a referendum on respect for one's elders.|
N~The advice has been canceled. The lecture has proved less cooperative.|
N~We can return when an assessment would actually help us make a decision.|
N~An open hand feels different once it closes around your sleeve.|
N~I wish he'd let the invitation stay welcoming. We might have come back more readily.|
N~I'd rather ask when we're curious than pretend to listen just to avoid a scolding.
''')
add('judge_careful', 'BattleFrontier_Lounge1_Text_SaidMyMonIsOutstanding', 'A trainer is pleased that careful raising received the expert praise.', '''
S~That compliment has found someone who will be smiling about it all day.|
S~The assessment reassures her, though it doesn't measure every aspect of her care.|
S~She's proud of her partner and the work. Fair enough.|
S~She sounds relieved as well as pleased. The effort mattered to her.|
S~Being attentive every day rarely comes with applause. Nice that she got a moment of it.|
S~A short expert opinion has supplied a very long-lasting grin. Efficient generosity.|
S~The quiet daily work has received one loud little reward.|
S~It's encouraging to have a strength recognized after putting real care into a partner.|
S~She held something carefully, and someone noticed its brightness.|
S~I like that her pride goes straight back to the Pokemon.|
S~I'd ask what routines they enjoy together. Care is often hidden in ordinary details.
''')
add('judge_natural', 'BattleFrontier_Lounge1_Text_DidntDoAnythingSpecialRaisingIt', 'A trainer is surprised by an outstanding rating despite no special raising method.', '''
S~Sometimes a little partner arrives with surprises already packed inside.|
N~Innate variation can explain a strong assessment without an unusual training method.|
S~Doesn't need a secret method to be worth celebrating.|
S~He looks almost apologetic about the good news. He can just be happy.|
S~Ordinary care can still be good care. Nothing special doesn't mean nothing kind.|
S~Excellent news has arrived without the expected heroic backstory. How refreshing.|
S~An outstanding Pokemon has neglected to require an elaborate origin story.|
N~The result may reflect qualities he didn't create. Recognizing them is still useful.|
S~Not every lovely thing announces the work of becoming lovely. Some simply arrive.|
S~He doesn't have to invent an impressive routine to deserve enjoying his partner.|
S~I'd ask what surprised him most about the assessment. He seems ready to reconsider a few assumptions.
''')
add('mentor_news', 'BattleFrontier_Lounge2_Text_NewsGatheringPower', 'A student admires the Frontier Maniac ability to gather news.', '''
S~His mentor gathers news. He gathers opportunities to tell us how impressive that is.|
N~Collecting timely information is a real skill. I'd also ask how the sources are checked.|
N~Useful talent. Accurate matters as much as fast.|
S~He's very proud of his teacher. It's nice when admiration is that uncomplicated.|
S~Keeping up with this whole island must take a fair amount of conversation.|
S~The mentor has acquired an enthusiastic publicity department of one.|
S~Every rumor enters. Presumably some facts emerge. I'd ask about the sorting process.|
N~An information network needs dependable contacts. I'm curious how he maintains them.|
N~News travels from mouth to mouth. Its shape can change on the way.|
S~He praises the skill instead of claiming it as his own. That's rather sweet.|
S~I'd ask which discovery impressed him most. That would make a good introduction.
''')
add('mentor_observation', 'BattleFrontier_Lounge2_Text_AmazingPowersOfObservation', 'A student admires the mentor powers of observation.', '''
S~He watches his mentor watching things. That's a surprisingly busy little arrangement.|
N~Careful observation is teachable. I wonder what his mentor asks him to notice first.|
N~Seeing details helps. Checking what they mean comes next.|
S~I like teachers who help people notice what was already beside them.|
S~Noticing a small problem early can save everyone a large headache later.|
S~A keen observer, now observed by an extremely approving observer.|
S~The noticing has become recursive. We may be watching its third generation.|
N~I'd ask for a specific example. The method interests me more than the praise.|
S~Some eyes make an ordinary room seem crowded with things we missed.|
S~He's impressed enough to look more closely himself. That may be the real lesson.|
S~I'd compare what each of them noticed in the same match. That could be fascinating.
''')
add('mentor_persuasion', 'BattleFrontier_Lounge2_Text_AmazingPowerOfPersuasion', 'A student praises the mentor persuasive ability.', '''
S~He's convinced me that he's convinced. The mentor's work is traveling well.|
N~Persuasion can communicate good evidence or conceal weak evidence. The distinction matters.|
N~A convincing voice still needs a sound point.|
N~I hope he feels free to disagree with the person he admires.|
N~Getting people to listen is useful. Leaving them room to decide matters, too.|
S~The mentor's greatest proof of persuasion appears to be standing directly in front of us.|
N~A very persuasive man has obtained a very persuaded audience.|
N~I'd like to know how he explains things. A clear method can be learned.|
N~Some voices open a path. Others quietly remove all the forks.|
N~Admiration is warm. I'd still want to hear the idea before agreeing with it.|
N~I'd ask for an example of an opinion the mentor changed. The details would tell us more.
''')
add('room_scary', 'BattleFrontier_Lounge2_Text_ThisPlaceIsScaringMe', 'A visitor is unnerved by the intense Frontier Maniac room.', '''
S~A room full of matching enthusiasm can be more unsettling than an actual ghost.|
N~The concentrated admiration may feel socially disorienting to someone outside the group.|
N~They can step outside. No need to stay uncomfortable.|
N~I understand. Sometimes a room feels as though everyone learned a rule except you.|
N~Let's give them a little space. They don't need another person asking what's wrong.|
N~The atmosphere appears to have become slightly more organized than comfort allows.|
S~No hauntings confirmed. The enthusiasm alone seems to be managing.|
N~A quiet break outside might make the room less overwhelming when they return.|
N~A room can be crowded with certainty. It's difficult to breathe between all of it.|
N~Being the only uncertain person in a very certain group is uncomfortable.|
N~I'd ask whether they want company outside. We don't need to make a scene.
''')
add('gambler_busy', 'BattleFrontier_Lounge3_Text_CantYouSeeWereBusyHere', 'The gamblers brusquely dismiss the player before considering a wager.', '''
N~He could have said busy without wrapping it in quite so many elbows.|
N~Their activity doesn't excuse the discourteous response. We can leave them to it.|
N~Fine. Plenty of better company elsewhere.|
N~I wasn't trying to interrupt anything important. We can go.|
N~No need to stand around waiting for someone determined to be unpleasant.|
N~A spectacularly unwelcoming welcome from a room that could have simply said later.|
N~The atmosphere has declined our company. I accept on behalf of both sides.|
N~We don't have a reason to keep interrupting. Let's use the time elsewhere.|
N~A closed door without the courtesy of an actual door.|
N~He made the room smaller with one greeting. I wouldn't fight for a place in it.|
N~I'll save my questions for somebody who feels like answering them.
''')
add('gambler_return', 'BattleFrontier_Lounge3_Text_ThinkOfMeForAnotherChallenge', 'After paying a successful wager, the gambler invites another challenge.', '''
N~He's paid up and would love another appointment with our points. Naturally.|
N~The previous payout is settled. It doesn't change the risk of the next wager.|
N~One settled deal. We don't owe him another.|
N~He sounds friendly again now that everything went well. I'd remember both moods.|
N~We can enjoy getting the points back without immediately putting them at risk again.|
N~A business relationship that survives success is now eagerly requesting a sequel.|
N~The points returned home. Their former host is already sending invitations.|
N~Any new arrangement needs a fresh decision. The previous result shouldn't make it automatic.|
N~A returned handful can make the next open hand seem safer than it is.|
N~He's pleasant when he's pleased. That doesn't tell us how the next bet will go.|
N~I'd rather choose our next challenge first, then decide whether this arrangement belongs in it.
''')
add('gambler_loss', 'BattleFrontier_Lounge3_Text_NiceTryCantReturnPoints', 'After a failed wager, the gambler says the staked points cannot be returned.', '''
D~The points are gone, and his consolation has arrived with completely empty pockets.|
N~The loss is now realized. Another wager isn't required to justify the previous stake.|
N~Lost points. Stop and think before risking more.|
D~His softer voice doesn't make the missing points feel much better.|
N~We don't need to chase the loss today. Let's do something that doesn't require another stake.|
N~He offers motivation with admirable generosity, given that it costs him none of the missing points.|
N~The consolation is free. Everything useful has remained elsewhere.|
N~We should assess the arrangement on its actual cost before repeating it.|
N~An empty hand can itch to reach out again. It doesn't have to.|
N~Calling the loss motivation puts a flattering ribbon around an unpleasant result.|
N~I'd rather review what happened than hear another promise about next time.
''')
add('gambler_decline', 'BattleFrontier_Lounge3_Text_NotInterested', 'The gambler calls the player afraid after a declined wager.', '''
N~My points don't have to jump off a cliff to prove they aren't afraid of heights.|
N~Declining a wager may reflect preference or judgment. Fear isn't the only explanation.|
N~We said no. He can live with it.|
N~That makes me less inclined to change my mind, honestly.|
N~A good offer shouldn't need an insult to push someone into it.|
N~He has mistaken an attempt to preserve our points for a personal character flaw.|
N~The offer has grown teeth now that we stopped feeding it.|
N~Pressure after a refusal is useful information about the person making the offer.|
N~A choice stops feeling free when refusal becomes an accusation.|
A~He's trying to make sensible caution look embarrassing. That doesn't improve his proposal.|
N~I'd rather spend time with someone who can hear no without inventing a story about it.
''')
add('gambler_observer', 'BattleFrontier_Lounge3_Text_ShouldBeTakingChallenges', 'An observer disapproves of trainers gambling instead of taking challenges.', '''
N~An island full of actual battles, and they've built a small argument about other people's battles.|
N~They prefer wagering to direct competition. That may explain the activity without endorsing it.|
N~Their choice. Just don't let them rope unwilling people in.|
N~Maybe being a spectator feels easier than being judged themselves.|
N~I'd rather use my own effort to earn points, too. Less waiting on somebody else.|
N~They have found a way to make other people do the battling while they supply the tension.|
N~A battle facility has developed a secondary industry in standing around.|
N~The challenges offer direct feedback. Watching a wager doesn't teach quite the same things.|
N~Some people prefer to place their hopes in another person's hands.|
N~I understand his frustration. I'd also leave room for people to enjoy different parts of a visit.|
N~I'd ask the gamblers what they like about it. The answer might be more revealing than the game.
''')
add('gambler_wrong_trainer', 'BattleFrontier_Lounge3_Text_BackedWrongTrainer', 'A repeated losing bettor considers returning to ordinary battles.', '''
S~His own Pokemon might enjoy being promoted from audience to actual participants again.|
N~Repeatedly unsuccessful predictions are a reasonable basis for reconsidering the method.|
N~Sounds sensible. Put effort into a result he can influence.|
S~He sounds tired of waiting for someone else to win for him.|
S~Battling himself could give him something useful even when he loses: practice.|
S~He has discovered that choosing the winner is harder than simply announcing one.|
S~The fortune-telling department is considering a practical career change.|
N~Direct participation would give him more information about his own decisions.|
S~His attention is beginning to return to the path beneath his own feet.|
S~He seems ready to choose a different way to spend the afternoon. Good.|
S~I'd ask which challenge he used to enjoy. That could be a nicer place to restart.
''')
add('gambler_confident', 'BattleFrontier_Lounge3_Text_KnowWinnerWhenISeeOne', 'A bettor confidently claims to recognize winners on sight.', '''
S~I wonder if the winners know they've been identified. It might save them some suspense.|
N~That claim would be interesting to compare against a recorded prediction history.|
N~Everyone can spot the winner after the result. Before it is the hard part.|
N~She sounds very sure. I wouldn't borrow that certainty without knowing why.|
N~A confident smile doesn't make a stake any less costly if she's wrong.|
N~A bold claim, conveniently unaccompanied by the results ledger.|
N~The smile is certain. The future has declined to comment.|
N~I'd ask what evidence she uses. A repeatable method is more useful than confidence.|
N~Eyes can find what they expect very easily. The next match may be less obliging.|
S~She certainly knows how to make the prediction feel reassuring. That's its own skill.|
N~I'd ask her before a match and check afterward. Memory is kinder to winners than to misses.
''')
add('gambler_pressure', 'BattleFrontier_Lounge3_Text_TrainerGoodButRattled', 'An observer says a skilled trainer struggles with pressure at the Dome.', '''
N~Knowing the right move and remembering it while everyone's staring are different little beasts.|
N~Performance under pressure is a separate skill from understanding the strategy.|
N~Then he needs practice with pressure. Calling him doomed won't help.|
N~I understand getting rattled when people expect you to do well.|
N~He might do better with a calm supporter than another person measuring every wobble.|
N~A sound assessment could become useful advice if delivered with considerably more kindness.|
N~Talent has encountered nerves. They have a well-established disagreement.|
N~He could rehearse decisions under smaller amounts of pressure and build up gradually.|
N~A steady hand is sometimes learned one shaking attempt at a time.|
N~Everybody watching him seems to have an opinion. That may be part of the difficulty.|
N~I'd ask the trainer what helps him settle. The spectator can't answer that for him.
''')
add('restaurant', 'BattleFrontier_Lounge4_Text_IfIOpenedRestaurantHere', 'A cook sees a restaurant opportunity among the Frontier visitors.', '''
S~A crowd of hungry battlers. That's a business plan with several rumbling endorsements.|
N~Visitor volume suggests demand. Costs and daily demand variation still need checking.|
N~People need to eat. He should work out the numbers before opening.|
S~I'd like somewhere quiet to sit after a challenge. Maybe he could make that.|
S~I'd ask what he'd serve first. Feeding a rushed crowd takes a menu that works hard.|
S~Seven facilities have produced an eighth challenge: finding lunch. He's noticed the vacancy.|
S~A profitable ambition. The island's stomachs are probably willing to negotiate.|
N~He needs a supply plan as well as customers. An island adds complications.|
S~A place built around striving could use somewhere that simply welcomes hunger.|
S~The room itself might matter as much as the menu. People will want a breather.|
S~I'd ask who he imagines sitting at the first table. That usually makes a plan more vivid.
''')
add('strategy_rest', 'BattleFrontier_Lounge4_Text_NeedBreatherAfterBattles', 'A resting trainer continues planning strategies despite exhaustion.', '''
N~His feet are resting. The rest of him has started another tournament.|
N~Mental fatigue can persist even when physical activity stops. A genuine pause may help.|
N~Take the breather properly. The next combination can wait.|
N~Sometimes thoughts keep moving because going quiet feels harder.|
N~I'd give him a drink and a few minutes without asking about the next match.|
N~He has granted his body a recess while keeping his mind under full interrogation.|
N~A rest with all the restful parts carefully removed.|
N~Writing the idea down might let him stop rehearsing it for a while.|
N~A mind can pace the room long after its owner has sat down.|
N~He sounds proud of never stopping. I wonder whether it's still helping him.|
N~I'd ask about something besides battling for once. He might enjoy remembering the island exists.
''')
add('tv_interviews', 'BattleFrontier_Lounge4_Text_WonderIfInterviewsAiring', 'A viewer hopes to see interviews with strong trainers on television.', '''
S~The battles show what they do. I'd like to hear what they thought they were doing.|
S~Interviews can reveal reasoning unavailable from observing the battle alone.|
N~Could be useful. Depends whether they ask about the actual decisions.|
S~I'd be curious what they're like once nobody needs to look fearless.|
S~I like hearing the ordinary routines behind somebody's big achievement.|
S~A chance for the formidable trainers to reveal whether they can also survive a question.|
S~After the battle comes the difficult task of explaining yourself in public.|
S~I'd want them to explain one choice that didn't work. That's often the useful part.|
S~A voice after the spectacle can bring a distant person a little closer.|
S~Interviews show how people carry attention. That can be as revealing as the answers.|
U~I'd love to know which questions the interviewer chooses. Follow-ups make all the difference.
''')
add('nature_egg', 'BattleFrontier_Lounge5_Text_NatureGirlEgg', 'The girl refuses to read an Egg because it is asleep.', '''
S~The Egg has declined the interview by being extremely busy becoming a Pokemon.|
N~An unhatched Pokemon doesn't provide her the same basis for a reading. Sensible boundary.|
N~Fair enough. Let the little Egg be.|
S~I like that she thinks of it as sleeping. She sounds very certain about being considerate.|
S~No need to wake a guest who hasn't even arrived yet.|
S~The smallest guest has secured an exemption from all conversation. Enviable.|
S~The Egg is unavailable for comment. A dignified response.|
N~She knows a case her method doesn't cover. That's useful to acknowledge.|
S~Some closed things deserve time before questions.|
S~She may be blunt, but she isn't going to pretend to hear something just to impress us.|
S~We can ask again after it hatches. Then there will be a new little personality to meet.
''')
add('nature_decline', 'BattleFrontier_Lounge5_Text_NatureGirlNoneShown', 'The girl pouts after the player declines to show a Pokemon.', '''
N~We've been charged one small pout for keeping our Pokemon to ourselves.|
N~Disappointment doesn't create an obligation to participate in her reading.|
N~She can be disappointed. We can still say no.|
F~I feel a little bad. I still wasn't ready to show anyone.|
N~A no doesn't have to spoil the whole visit. She'll find another thing to do.|
N~A devastating review from a customer who was never actually our customer.|
N~The consultation has ended in a highly compact protest.|
N~No Pokemon was selected, so there's no reading to assess. We can return another time.|
N~A small disappointment can make a loud little shadow. It passes.|
N~She wants to show what she can do. I understand the pout without needing to give in.|
N~I'd give her a moment rather than turn it into an argument.
''')
add('nature_gentleman', 'BattleFrontier_Lounge5_Text_LadyClaimsSheUnderstandsPokemon', 'A gentleman is charmed by a girl who claims to understand Pokemon.', '''
S~He finds it charming. I'd like to hear the Pokemon's review before we settle the question.|
N~He reports her claim, rather than independently demonstrating its accuracy. A useful distinction.|
N~Interesting claim. Let's listen before deciding what to make of it.|
S~He sounds pleased just watching her enjoy herself.|
S~If she pays close attention to them, that part alone is worthwhile.|
S~A charming claim with a conveniently difficult interview process for its other witnesses.|
S~The gentleman is convinced of the charm. The translation remains under review.|
N~I'd compare the reading with observable behavior. That gives us a place to start.|
N~Understanding another creature begins with noticing it. Whatever else she does, that matters.|
S~He isn't mocking her. That's a gentler response than she might get elsewhere.|
S~I'd ask what he's seen her notice. A specific example would be interesting.
''')
add('nature_profound', 'BattleFrontier_Lounge5_Text_GirlSayingSomethingProfound', 'A Black Belt suspects the girl Pokemon readings are profound.', '''
S~He's searching for deep meaning. The girl may just be having a very direct conversation.|
N~A feeling of profundity isn't evidence of accuracy, though it can prompt closer attention.|
N~Maybe ask her what she means. No need to guess forever.|
N~I know that feeling when something simple seems bigger than I can explain.|
N~A good question might get him farther than looking impressed from across the room.|
S~He has discovered mystery and is treating it with admirable seriousness.|
S~The depth remains unmeasured. He has wisely declined to announce a number.|
N~He could ask for clarification. That's often the quickest route through a mysterious idea.|
S~A small voice can make a large silence around it. He seems to be listening to that.|
N~He wants to understand, which is a warmer response than simply dismissing her.|
N~I'd ask which part stayed with him. That might be more revealing than the word profound.
''')
add('nature_red_house', 'BattleFrontier_Lounge5_Text_GirlPlaysAtRedHouseALot', 'A boy says the girl often plays at the red house.', '''
S~A grand mystery has acquired a very ordinary detail: she has a favorite place to play.|
N~A specific repeated observation. That helps place her daily routine.|
N~Good to know. Still her choice where she goes.|
S~I like hearing about the ordinary part of her day.|
S~Even somebody with an unusual talent needs somewhere familiar to spend time.|
S~A useful reminder that the mysterious young oracle also has afternoons to fill.|
S~The intriguing child has been discovered committing ordinary childhood.|
N~He knows where she spends time. That doesn't tell us everything about why she likes it.|
S~A favorite house can anchor a very strange little day.|
S~He's noticed her routine without making a grand claim about it. Refreshing.|
S~I'd ask whether they play together. He seems glad to share the detail.
''')
add('frontier_trade_complete', 'BattleFrontier_Lounge6_Text_PromiseIllBeGoodToIt', 'The Frontier trader promises care after exchanging Meowth for Skitty.', '''
S~Two new partners, and she remembers to wish both of them well.|
S~The exchange is complete. Her promise concerns the ongoing care that follows it.|
S~Good promise. Now both trainers need to keep it.|
S~She sounds delighted and a little protective at the same time.|
S~A new home starts with getting to know what the little one actually likes.|
S~The exchange ends with mutual responsibilities. A much better conclusion than merely calling it a bargain.|
S~A small creature has arrived to enthusiastic reviews and a promise of kindness.|
S~Now comes the learning: habits, preferences, and how each partner communicates.|
S~A parting wish reaches after the one leaving. A welcome waits for the one staying.|
S~She's delighted without forgetting the partner she handed over. I appreciate that.|
S~I'd ask her later how Skitty settled in. That first welcome sounds warm.
''')
add('frontier_trade_decline', 'BattleFrontier_Lounge6_Text_WellThatsFineToo', 'The trader graciously accepts a declined exchange and invites another visit.', '''
S~A declined trade, and we're still welcome. Nice when a conversation keeps its manners.|
S~She separates the proposed exchange from the social visit. A considerate response.|
S~No argument. Good way to handle it.|
S~I'm glad she didn't make saying no feel unkind.|
S~We can enjoy visiting without having to make an exchange.|
S~A gracious refusal of any need to be offended. Admirably economical.|
S~The trade has vanished. The hospitality remains.|
S~We can reconsider later without being pushed into a decision now.|
S~A door stays open after a hand is drawn back.|
S~She left room for us to visit as people instead of only potential traders.|
S~I'd happily come back just to ask how her partner is doing.
''')
add('frontier_trade_wrong', 'BattleFrontier_Lounge6_Text_DontTradeForAnythingButMon', 'The trader declines a Pokemon of the wrong requested species.', '''
N~She's looking for one particular little face. Our offer hasn't changed the shopping list.|
N~The proposed Pokemon doesn't meet the species requirement. The exchange hasn't occurred.|
N~Wrong species. At least she's clear about it.|
N~She apologized first. That makes a small refusal easier to hear.|
N~Wanting a specific partner isn't a criticism of the one we showed her.|
N~A precise request has received a precise correction. No diplomatic incident required.|
N~The specification survives contact with an alternative. A firm little boundary.|
N~We need the requested species if we want to proceed. The condition hasn't changed.|
N~One creature cannot stand in for another merely because we offered it.|
N~She knows what she wants and says it politely. That's fair.|
N~I'd ask why that species caught her interest. There might be a nice story behind it.
''')
add('frontier_trade_skitty', 'BattleFrontier_Lounge6_Text_SkittySoMuchCuterThanImagined', 'After the trade, the delighted trader says Skitty exceeds her expectations.', '''
S~The real Skitty has defeated the imaginary Skitty in a decisive cuteness contest.|
S~Direct experience exceeded her expectation. A rather pleasant revision.|
S~She's happy with the partner. Good to see.|
S~She still sounds surprised by how much she likes the little one.|
S~That welcome seems to have lasted past the first excitement. Lovely.|
S~An excellent result for Skitty, whose mere presence has outperformed advance publicity.|
S~Reality has briefly been kinder than imagination. Skitty should receive appropriate credit.|
S~She had a clear wish and is pleased by the actual partner, not just the idea.|
S~Sometimes the thing we waited for arrives with more life than our wanting could invent.|
S~She's delighted by the individual in front of her. That matters more than the original picture.|
S~I'd ask what Skitty does that she finds funniest. She looks ready to tell us.
''')
add('tutor_cancel', 'BattleFrontier_Lounge7_Text_YouDontWantTo', 'A move tutor accepts cancellation and invites the player back.', '''
S~We can come back when the team is ready. Her confidence will clearly keep until then.|
N~No lesson was completed. The option remains available for a later decision.|
N~Fine. Better to choose a move carefully than spend points in a hurry.|
S~She sounded disappointed, but she still invited us back.|
S~A lesson can wait until we know which partner actually needs it.|
S~She has preserved both the invitation and her unshaken opinion of her own skill.|
S~The demonstration has been postponed. The confidence is already fully assembled.|
N~We can compare the move choices before committing our points.|
S~Knowledge can wait without becoming less useful.|
S~She wants to impress us, but she left the choice with us.|
N~I'd come back with a specific question. That would make the visit more useful.
''')
add('tutor_paid', 'BattleFrontier_Lounge7_Text_IllTakeBattlePoints', 'The tutor finishes a successful lesson and takes the agreed Battle Points.', '''
S~New skill learned, agreed fee paid. Her victory speech comes included.|
N~The lesson succeeded and the quoted cost is now collected. A completed transaction.|
S~Learned the move. Paid the price. Let's practice using it well.|
S~She's so pleased to prove herself. Our partner did some learning, too.|
S~Worth giving the new move a little thought before trying it in a serious match.|
S~Service rendered, fee collected, modesty still notably absent. A complete experience.|
S~The lesson is complete. Her self-esteem required no additional instruction.|
S~Now the team has another option. I'd work out where it fits with the existing moves.|
S~An old skill has found a new pair of hands. Or paws.|
S~She earned the payment. I think she enjoyed the recognition almost as much.|
S~I'd ask our partner how that new move feels. The teacher has certainly given her review.
''')
add('tutor_friends', 'BattleFrontier_Lounge7_Text_ThinkLadiesDontGetAlong', 'An observer suspects the bickering tutors remain together because they are friends.', '''
S~They've found someone willing to stay nearby through an impressive amount of complaining.|
N~Their continued company supports his interpretation, though it doesn't settle every disagreement.|
S~Could be fond of each other and still argue. Happens.|
S~They seem to know exactly which things will make the other react.|
S~Some people fuss at each other the way other people offer another cup of tea.|
S~A friendship conducted almost entirely through objections. The longevity is persuasive.|
S~They have apparently agreed to remain together and disagree about everything else.|
N~A long working partnership can include friction. I'd look at how they actually treat each other.|
S~Some roots twist around one another. Pulling apart would be the stranger shape.|
S~He notices the choice to stay together underneath the noisy performance.|
S~I'd like to hear how they met. They might even interrupt each other with matching corrections.
''')
add('tutor_age', 'BattleFrontier_Lounge7_Text_LadiesWereStrongAndBeautiful', 'An old admirer praises the tutors increasing skill but laments aging.', '''
S~Their moves keep improving. Time seems to have handed them at least one decent gift.|
N~He reports their skill has advanced with experience. That deserves attention in its own right.|
N~Still strong, still teaching. Nothing cruel about that part.|
N~I wish he could say all the kind things without making the years sound like an apology.|
S~They've kept learning and sharing it. That's a good way to carry a long life.|
N~He praises everything the years have added, then files a complaint against the years.|
N~Time has improved the moves and offended the admirer. The ladies seem busy regardless.|
S~Decades of refinement would explain the polish. Experience keeps producing useful work.|
S~A long life changes the vessel. What it holds can grow richer.|
N~He remembers their beauty so strongly that he's overlooking the people standing here now.|
S~I'd ask the tutors what they're proudest of learning lately. They're the better people to answer.
''')
add('all_but_pokemon', 'BattleFrontier_Lounge8_Text_WhatATrainerNeeds', 'A boastful visitor lists every trainer virtue but does not know what Pokemon are.', '''
U~He's packed every possible quality and somehow left out the Pokemon. That's a special kind of light travel.|
N~His checklist omits the defining participant in the activity. A substantial conceptual gap.|
N~He might want to start with the basic question before challenging anything.|
S~I thought he was joking. I'm still not completely sure.|
S~That's like planning a whole meal and asking what food is. We should begin again.|
L~A magnificent inventory of qualifications, missing only the central premise of the entire profession.|
S~Perfectly prepared, apart from a small disagreement with the meaning of prepared.|
N~The requirements list needs one major revision before any practical testing.|
S~He has gathered every key except the one belonging to the door.|
U~His confidence survived not knowing the central detail. That's almost a talent by itself.|
U~I'd ask one careful follow-up. I really need to know whether he's serious.
''')
add('seven_brains', 'BattleFrontier_Lounge8_Text_KnowAboutFrontierBrains', 'A visitor explains Scott title for the seven facility leaders.', '''
S~Seven Brains running seven buildings. I wonder who gets called when they disagree.|
N~The title identifies the seven facility leaders. Useful terminology for the local hierarchy.|
N~Seven specialists. Each place has someone responsible for its challenge.|
N~That makes the big buildings feel a little more personal. Somebody shaped each one.|
N~Seven very different challenges must need seven very different kinds of attention.|
S~A grand collective title. Considerably more memorable than facility management.|
S~An island with seven Brains and apparently no shortage of opinions.|
N~I'd like to know how much each leader helped design their facility's rules.|
N~Seven houses, seven minds. Each will leave a different shape on the people entering.|
S~Scott understands a memorable title. People will remember that one after hearing it once.|
N~I'd ask which leader they've met. The official title tells us less than an actual encounter.
''')
add('talent_preference', 'BattleFrontier_Lounge8_Text_ToldMeIHaveTalentForBattling', 'A boy distinguishes his battle talent from his stronger interest in Contests.', '''
S~Being good at one thing doesn't mean it gets to confiscate the thing you love.|
N~Aptitude and interest are separate variables. Practice can still improve the preferred activity.|
S~He can like Contests. Talent isn't an order.|
S~I'd rather hear what he loves about Contests than tell him to give them up.|
S~He doesn't have to turn his easiest skill into his whole life. Enjoyment is worth something.|
S~A talent has arrived and attempted to appoint itself his future. He may decline the position.|
S~A gift doesn't get to issue instructions simply because it arrived early.|
S~He can build Contest skills deliberately. Starting behind doesn't make the project pointless.|
S~The easy path isn't always the one that calls your name.|
S~I like that he knows the difference. Other people may need reminding more than he does.|
S~I'd ask which part of Contests he enjoys most. That's where I'd start talking about practice.
''')
add('ranking_welcome', 'BattleFrontier_RankingHall_Text_ExplainRankingHall', 'The attendant introduces the hall honoring Frontier records.', '''
S~A room full of names that earned a little extra space in people's memories.|
N~The hall records exceptional results across facilities. A useful comparative archive.|
N~Those names earned their place. Ours would need to do the same.|
N~I'd read slowly. Each name probably means a great deal to someone.|
S~A lot of ordinary practice must sit behind every extraordinary number.|
S~Immortality has been reduced to a conveniently readable list. Efficient institution.|
S~A hall of people who have defeated the reasonable stopping point.|
N~I'd compare the categories before deciding which record to pursue.|
N~The wall keeps the name. The person keeps the cost of reaching it.|
N~Recognition matters. I like that the achievement stays beside the name.|
S~I'd want to hear one story from each person, though that might take a very long visit.
''')
add('ranking_no_attempt', 'BattleFrontier_RankingHall_Text_MyNamesNotUpThere', 'A boy realizes he cannot appear in the records before attempting a challenge.', '''
S~He checked just in case the wall had done the battling for him. Sensible to confirm.|
N~He has correctly identified the missing prerequisite. Participation precedes a result.|
S~At least he's honest. First attempt comes before the record.|
S~Maybe seeing the empty place will make starting feel a little more real.|
S~Everyone on that list had a first attempt. He can have one, too.|
S~An unexplained omission has received an exceptionally straightforward explanation.|
S~The records office has declined to invent his career. Harsh but fair.|
N~Now he can choose a challenge and establish a starting result.|
S~An unwritten name isn't a rejected one. Sometimes the story hasn't begun.|
S~He's able to laugh at the gap between wanting it and having tried. That's healthy.|
S~I'd ask which challenge he wants to attempt first. That's the interesting next question.
''')
add('ranking_yes', 'BattleFrontier_RankingHall_Text_WowThatsSuper', 'The boy admires the player listed record and feels motivated to improve.', '''
S~Our name gave him a little push forward. That's a nice thing for a name to do.|
S~An example has become a concrete source of motivation. A constructive comparison.|
S~Good. Let it encourage him to try.|
S~He sounds happy for us without making himself smaller.|
S~A shared achievement can give someone else a place to start.|
S~An accolade has escaped the wall and become useful to another person. Excellent.|
S~The record has successfully reproduced ambition. The hall should be pleased.|
S~He has a benchmark now. Smaller goals can build toward it.|
S~A name on a wall has opened a door in someone else's day.|
S~His congratulations felt warm. I like that he made room for his own hopes, too.|
S~I'd ask him to tell us when he sets his first record. I'd like to hear about it.
''')
add('ranking_no', 'BattleFrontier_RankingHall_Text_WorkHarderIfYouSawFriendsName', 'The boy suggests a friend name in the records could encourage harder effort.', '''
S~A familiar name might make the big wall feel a little closer to home.|
N~Peer examples can motivate effort, though people respond differently to comparison.|
N~Friendly competition can help. It shouldn't become resentment.|
N~I'd mostly be happy to see someone I knew. The harder work could come later.|
S~A friend's success is worth celebrating before making it our next assignment.|
N~He proposes borrowing ambition from a familiar name. A plausible arrangement.|
S~Friendship, now available as a gentle competitive nuisance.|
N~A specific example can make a target seem reachable. The next step still needs planning.|
S~A familiar name can turn a distant achievement into a path someone we know has walked.|
N~I'd want the friend to feel celebrated, rather than immediately treated as the next rival.|
S~I'd ask how they earned it. Knowing their route could be more useful than copying the goal.
''')
add('souvenir_grandparents', 'BattleFrontier_Mart_Text_ChaperonGrandson', 'Grandparents accompanying their grandson decide to shop for souvenirs.', '''
S~They came as chaperons and have discovered the side quest of bringing something home.|
S~A supporting visit can still include interests of their own. Sensible use of the trip.|
S~Good. They should enjoy the visit, too.|
S~I like that this has become a little outing for all of them.|
S~A small souvenir can make the journey feel like theirs as well as his.|
S~The official chaperoning mission has expanded to include a modest shopping operation.|
S~Responsible supervision, with optional commemorative purchases.|
S~I'd choose something easy to carry for the return journey.|
S~They followed his adventure and found a small piece of their own.|
S~They deserve something they actually like, rather than just a token of being good grandparents.|
S~I'd ask what they enjoyed most so far. The answer might surprise their grandson.
''')
add('protein_gift', 'BattleFrontier_Mart_Text_ProteinMakeNiceGift', 'A grandparent mistakes the Pokemon supplement Protein for an appetizing gift.', '''
S~It sounds tasty to her. I think we should check the label before anyone sets out a plate.|
N~That's a Pokemon supplement rather than an ordinary snack. The label deserves a closer look.|
N~Ask the clerk what it is before buying it as food.|
S~She wants to choose something nice. A little explanation would help more than laughing.|
S~I admire the gift instinct. I'd redirect the menu before anybody samples it.|
S~A generous purchase is approaching a small but important category error.|
S~The gift may be useful. The proposed tasting notes are less well supported.|
N~Packaging should make the intended use clearer. This confusion is quite understandable.|
S~A kind thought has taken a wrong turn at an unfamiliar word. Easy enough to guide back.|
S~She wants the gift to feel like a treat. We can help her find something that fits.|
S~I'd ask the clerk to explain it kindly. She's choosing with care, just missing a detail.
''')
add('item_restrictions', 'BattleFrontier_Mart_Text_FacilitiesDontAllowItems', 'A shopper notes item restrictions make Frontier battles more difficult.', '''
N~The bag can't rescue every problem here. It may have to enjoy being luggage for once.|
N~Restricting in-battle items shifts more weight onto preparation and move selection.|
N~Know the rules before packing a plan around items.|
N~I'd miss having one more way to help when a partner struggles.|
N~Then preparing well beforehand matters even more. Shopping isn't the whole plan.|
N~The emergency supplies have been politely informed that they are not on the team sheet.|
N~An impressive bag is about to discover the indignity of being irrelevant.|
N~We'll need plans that work within each facility's restrictions.|
N~A familiar safety net has been folded away. Best to notice before stepping out.|
N~The same team can need a different approach when one familiar option disappears.|
N~I'd ask which restriction surprised them most. That could save us an avoidable mistake.
''')
add('one_skitty', 'BattleFrontier_PokemonCenter_1F_Text_GoingThroughEveryChallenge', 'A trainer plans to take every challenge with a cherished Skitty.', '''
S~One Skitty, an entire Frontier, and enough confidence to fill the rest of the team slots.|
N~A highly focused ambition. Facility rules and matchups may complicate the implementation.|
N~Bold plan. She'll still need to respect each facility's entry rules.|
S~She calls the little one her baby. There's so much affection in that.|
S~I like the faith in her partner. I'd keep the challenges at a pace they both enjoy.|
S~A tiny partner has been assigned a very large itinerary.|
S~The Frontier has seven grand facilities. Skitty has one enthusiastic advocate.|
N~I'd start by checking which challenge formats allow the team she intends to use.|
S~One small companion can make a huge place feel like a shared adventure.|
S~She isn't shopping for a more impressive-looking partner. She's proud of the one beside her.|
S~I'd ask which challenge they're excited about first. That pair clearly has plans.
''')
add('unknown_school_mon', 'BattleFrontier_PokemonCenter_1F_Text_NeverSeenPokemon', 'A student encounters a Pokemon absent from their school lessons and wonders about its habitat.', '''
U~School has run out of Pokemon before the world has. That's a rather exciting discovery.|
S~A curriculum is necessarily incomplete. Direct observation has supplied a new question.|
N~Good question. Ask the trainer where they met it.|
S~I like that not knowing made them curious instead of embarrassed.|
S~There's always something new beyond the lessons. A polite question could tell them plenty.|
S~The world has failed to stop expanding at the end of the textbook. Excellent news.|
S~An educational omission with a face. Much more interesting than a missing paragraph.|
U~They could note its features, ask the trainer, and compare the information afterward.|
S~A lesson ended. The creature beyond it did not.|
S~They're comfortable admitting they haven't seen it before. That makes learning much easier.|
U~I'd ask what detail caught their eye first. A good observation begins there.
''')
add('arena_team_select', 'BattleFrontier_PokemonCenter_1F_Text_NextStopBattleArena', 'A trainer chooses suitable partners from storage before visiting the Arena.', '''
S~An enthusiastic destination, followed by a sensible pause to choose who actually comes.|
N~Selecting for the facility's specific rules should improve the relevance of the team.|
N~Good. Prepare before walking into the challenge.|
S~I like hearing someone sound excited and still take time to think.|
S~Picking the right partners is kinder than expecting everyone to handle every situation.|
S~The grand declaration has been followed by the practical work. A rare and pleasing sequence.|
S~Ambition remembered to stop at the planning desk. Promising behavior.|
N~Order matters in the Arena. I'd check the whole sequence, not only the first partner.|
N~A choice made quietly here will shape what happens in the bright room ahead.|
N~Being ready can look quite ordinary from the outside. This is part of it.|
S~I'd ask why they chose each partner. The reasoning would tell us a lot about their plan.
''')
add('ferry_no_ticket', 'BattleFrontier_OutsideWest_Text_MustHaveTicketToBoard', 'The ferry attendant refuses boarding because the player has no ticket.', '''
N~A whole ferry is being held back by one missing little rectangle. Rules do love rectangles.|
N~The required ticket is absent, so boarding cannot proceed. A clear administrative barrier.|
N~Need the ticket. Arguing won't put one in the bag.|
N~At least the attendant explained it kindly.|
N~We should check where the ticket belongs before making another trip to the dock.|
N~The ship may float, but the paperwork has declined to budge.|
N~The sea is open. The boarding policy is not.|
N~We have a specific missing requirement. That's easier to solve than an unclear refusal.|
N~A short crossing can wait behind a very small missing thing.|
N~They're apologetic without making the rule confusing. I appreciate the clear answer.|
N~I'd ask where to sort out the ticket. Better than guessing around the harbor.
''')
add('ferry_cancel', 'BattleFrontier_OutsideWest_Text_SailWithUsAnotherTime', 'The attendant warmly accepts a canceled ferry trip.', '''
S~The boat is staying without us, and nobody has made it awkward. A fine cancellation.|
S~The journey was declined without consequence. The service remains available later.|
S~We can sail another time. No hurry.|
S~I'm glad changing our mind didn't become a whole conversation.|
S~A trip is more pleasant when we actually feel ready to take it.|
S~A cordial end to an expedition that never quite became an expedition.|
S~The sea has been postponed. It seems likely to remain available.|
N~We can finish what we're doing here before deciding on a destination.|
S~A departure can wait. The shore isn't going to resent us for staying.|
S~That was an easy, gracious goodbye. Good service includes letting people leave the counter.|
S~I'd rather sail with a clear plan for where we're going. We can take a little time.
''')
add('tower_farewell', 'BattleFrontier_BattleTowerLobby_Text_LookForwardToAnotherChallenge', 'The Tower attendant ends the visit by inviting another challenge, regardless of result.', '''
S~The Tower will still be here when we feel like trying again. Rather hard to misplace it.|
N~That invitation follows multiple outcomes. It doesn't itself specify a win or loss.|
N~A clear stopping point. We'll decide when to return.|
S~It's nice to be welcomed back without another judgment attached.|
S~Time to regroup and see what everyone needs before another attempt.|
S~A courteous farewell from a building with an inexhaustible supply of opponents.|
S~The Tower remains optimistic about our future availability.|
N~We can review the visit before choosing another challenge.|
S~An open invitation can stay open while we rest.|
S~I appreciate a goodbye that leaves the next visit up to us.|
S~I'd return with a fresh plan and see what changes.
''')
add('dome_farewell', 'BattleFrontier_BattleDomeLobby_Text_HopeToSeeYouAgain', 'The Dome guide closes the visit without specifying the tournament result.', '''
S~The Dome has said goodbye without asking for one more round of applause.|
N~A general farewell. The tournament outcome must be established by other information.|
N~Visit finished. Good time to take stock.|
S~I like leaving on a quiet, kind note after all the competition.|
S~We can get something to eat before considering another tournament.|
S~A pleasant closing line that wisely makes no promises about our next opponent.|
S~The bracket has released us back into ordinary conversation.|
N~We have time to reconsider team choices before another visit.|
S~A crowded contest can end with a very small goodbye.|
S~The invitation is warm without being pushy. That helps.|
S~I'd be curious what the tournament looks like on a different day.
''')
add('factory_farewell', 'BattleFrontier_BattleFactoryLobby_Text_LookForwardToNextVisit', 'The Factory attendant ends the rental challenge visit.', '''
S~Next visit, a new set of unfamiliar faces to get to know. That's quite a greeting policy.|
N~A later visit may offer a different rental selection. Adaptation remains central here.|
N~We're finished for now. Review what worked before going back.|
S~I wonder which rental partners we'll remember longest.|
S~Learning somebody else's habits quickly takes attention. A break sounds good now.|
S~The Factory parts politely with its temporary workforce of visiting strategists.|
S~The next visit is waiting. Presumably beside several unpredictable teammates.|
N~I'd note which combinations worked while the details are fresh.|
S~A borrowed partnership can leave a surprisingly lasting impression.|
S~A neat end to a visit built around quick introductions.|
S~I'd ask the staff how often the rental lineup changes.
''')
add('palace_farewell', 'BattleFrontier_BattlePalaceLobby_Text_ReturnWhenFortified', 'The Palace guide asks the visitor to return when trainer and Pokemon are fortified.', '''
S~A little stronger, a little steadier, and perhaps a little less tempted to shout advice.|
N~The Palace asks us to prepare both the team and our expectations of direct control.|
N~We'll return when we're ready. Both parts of the partnership.|
S~I like that the farewell includes us as well as our Pokemon.|
S~A good rest belongs in that preparation. Strength isn't only earned by pushing.|
S~A polite invitation to improve one's inner resources before disturbing theirs again.|
S~The Palace recommends fortification. I support the version involving a quiet chair.|
N~We can consider how the moves suit each partner before another attempt.|
S~Some strength is built by learning when to loosen your grip.|
S~The farewell sounds serious without shutting the door on us.|
N~I'd return after noticing more about how our partners choose to act.
''')
add('arena_farewell', 'BattleFrontier_BattleArenaLobby_Text_AwaitAnotherChallenge2', 'The Arena attendant invites a later challenge after the visit concludes.', '''
S~Three-turn decisions can be tiring. I'm glad the goodbye isn't also being judged.|
N~The visit has reached its endpoint. The invitation doesn't distinguish the preceding result.|
N~Enough for now. We can prepare the next team order later.|
S~I'm happy to have a moment where nobody has to act quickly.|
S~A breather first. Then we can talk through what the Arena taught us.|
S~A gracious farewell from an institution that gives indecision very little room to stretch.|
S~The judges have no jurisdiction over our leisurely walk outside. Reassuring.|
N~We can revise the sequence before entering another challenge.|
S~The short battles are over. We can let the next few moments take their time.|
S~They keep the invitation courteous, whatever kind of visit we had.|
N~I'd like to compare our expectations with what actually mattered there.
''')
add('pike_farewell', 'BattleFrontier_BattlePikeLobby_Text_LookForwardToSeeingYou', 'The Pike guide closes the visit and invites a return without promising luck.', '''
S~The snake has politely let us go. I won't ask it to predict our next visit.|
N~The farewell is an invitation, not evidence that a future route will be fortunate.|
N~We're done for now. No need to test one more door immediately.|
S~I'm glad there's no choice hidden inside the goodbye.|
S~We can sort ourselves out before another trip through those rooms.|
S~A courteous conclusion from a place whose hospitality varies considerably by doorway.|
S~The Pike wishes to see us again. Its rooms have submitted no separate statement.|
N~I'd review which preparations helped across the different room outcomes.|
S~An uncertain path has a certain exit, at least for this moment.|
S~The calm goodbye feels welcome after so many unpredictable possibilities.|
N~I'd ask other visitors which surprises caught them out. There may be something useful to learn.
''')
add('pyramid_farewell', 'BattleFrontier_BattlePyramidLobby_Text_LookForwardToNextChallenge', 'The Pyramid guide ends the expedition visit and invites another.', '''
S~Back to ground-level plans for a little while. My feet approve.|
N~The expedition is concluded. A future attempt can be planned from the available results.|
N~A good point to stop and check the whole team.|
S~It's nice to have a simple way out after all those uncertain passages.|
S~I'd settle somewhere comfortable before planning another climb.|
S~The guide is already looking forward to an expedition our legs have not yet agreed to.|
S~Another invitation to upward mobility. We may consider remaining horizontal first.|
N~We can review navigation and supplies before taking the next challenge.|
S~The climb has ended. There is no need to keep climbing inside our heads.|
S~A warm welcome back makes even a difficult trip easier to leave behind.|
N~I'd ask which part of the expedition stays clearest in everyone's memory.
''')
add('pyramid_fortune_end', 'BattleFrontier_BattlePyramidLobby_Text_BelieveMyFortunesOrNot', 'The fortune teller ends by allowing disbelief and saying the future can change.', '''
S~A fortune that leaves us room to disagree. I like having some elbow room in the future.|
S~She explicitly allows uncertainty and change. More responsible than presenting inevitability.|
N~We'll use the warning without surrendering our judgment.|
S~The safe-passage wish matters more to me than sounding certain.|
S~Advice should leave room for what we choose next. Hers does.|
S~An oracle willing to release the audience from compulsory belief. Excellent manners.|
S~The future has been allowed to revise its appointment. Civilized arrangement.|
N~Treat the warning as preparation information, then respond to what actually happens.|
S~A glimpse needn't become a chain. She understands that.|
S~She doesn't need us to agree in order to wish us well. I appreciate that.|
S~I'd remember the caution and keep observing. Those can work together.
''')
add('arena_defensive_loss', 'BattleFrontier_BattleArenaLobby_Text_BadIdeaToNotAttack', 'A trainer learns that using only defensive moves hurt the Arena judgment.', '''
N~A very sturdy defense has discovered the judges wanted an actual attack somewhere.|
N~The Arena evaluates aggression as one criterion. Pure defense can therefore score poorly.|
N~He identified the problem. Change the plan for these rules.|
N~It must be frustrating when surviving still isn't enough.|
N~A safe-looking choice can cost you under different rules. Good lesson to carry forward.|
N~An excellent fortress has lost an argument about whether it did anything.|
N~The defense held. The judges remained unimpressed.|
N~The strategy needs to account for the scoring system as well as damage prevention.|
N~A shelter can keep you safe without taking you anywhere.|
N~He's willing to question his own choice. That gives him something useful after the loss.|
N~I'd ask which defensive move he'd replace first. That's a practical starting point.
''')
add('arena_hits_win', 'BattleFrontier_BattleArenaLobby_Text_LandingHitsWorked', 'A trainer credits consistent successful attacks for a judging victory.', '''
S~A plan built around actually landing the hits has received a favorable review.|
N~Successful moves support the Skill criterion. His result is consistent with that rule.|
S~Reliable hits did the job. Useful lesson.|
S~He sounds pleased to understand why it worked.|
S~Something dependable paid off. That's a satisfying kind of win.|
S~The humble successful attack has triumphed over more elaborate forms of wishful thinking.|
S~Hitting the opponent. An unfashionably direct method, vindicated.|
N~Consistency mattered under the judging rules. I'd keep that in mind when choosing moves.|
S~Small certainties can add up to a deciding weight.|
S~He gives credit to a repeatable choice instead of calling it magic.|
N~I'd ask what he changed from his previous attempt. That could explain the improvement.
''')
add('arena_draw', 'BattleFrontier_BattleArenaLobby_Text_MatchWasDeclaredDraw', 'A trainer describes a timed Arena match ending in a draw with similar HP.', '''
N~They both reached the finish with almost the same amount of stubbornness left.|
N~Similar remaining HP alone doesn't explain every scoring factor, but he remembers a close contest.|
N~Close match. Worth looking at what could have broken the tie.|
N~A draw must feel strange after trying so hard to separate the result.|
N~Neither side quite pulled away. There's probably a useful detail to learn from it.|
N~Two opponents spent the match arguing and arrived at an inconveniently balanced conclusion.|
N~A very thorough disagreement that failed to select a winner.|
N~I'd review the other judging factors as well as the remaining HP.|
N~Two paths met at the same edge and neither crossed it.|
N~He isn't inventing a grand excuse. Just describing how close it felt.|
N~I'd ask which turn he would change if he could replay one.
''')
add('arena_order', 'BattleFrontier_BattleArenaLobby_Text_OrderOfMonsImportant', 'A trainer recommends arranging Arena partners to handle weaknesses in sequence.', '''
N~The next partner needs to know how to clean up the kind of trouble the first one attracts.|
N~Sequential coverage matters when switching is unavailable. His advice addresses that constraint.|
N~Build for the whole line, not three separate strong choices.|
N~I like thinking about how one partner can make things easier for the next.|
N~Planning the order now can spare someone a very uncomfortable entrance later.|
N~A queue with consequences. The second arrival should have a useful answer to the first disaster.|
N~Even standing in line has become a tactical responsibility.|
N~We can map likely weaknesses across the order before selecting the final team.|
N~Who comes next matters most when the first door closes behind you.|
N~He's thinking about the relationship between choices. That tends to get overlooked.|
N~I'd ask for an example from his own team. Concrete matchups make the advice clearer.
''')
add('dome_reserve_regret', 'BattleFrontier_BattleDomeLobby_Text_NeedToCheckOpponentCarefully', 'A trainer regrets leaving the needed partner in reserve and advises checking opponents.', '''
N~The perfect answer was nearby, having a very unhelpful afternoon off.|
N~Preselection information can improve the matchup. Hindsight may still overstate certainty of victory.|
N~Check the opponent before choosing. He learned that the expensive way.|
D~It hurts when the choice you regret was made before the battle even started.|
N~A minute spent looking carefully can save a lot of wishing afterward.|
N~The reserve partner has become an undefeated champion in the tournament of what might have happened.|
N~The absent solution is enjoying a very flattering reputation.|
N~We should compare the available information before committing our selections.|
N~A closed choice can grow very bright in memory. It still can't be reopened today.|
N~He has useful advice. I wouldn't assume the alternative was a guaranteed win, though.|
N~I'd ask which opposing partner changed his mind. That detail matters.
''')
add('dome_first_round', 'BattleFrontier_BattleDomeLobby_Text_TrashedInFirstRound', 'A trainer was eliminated early after drawing a tournament favorite.', '''
D~A first round can still contain somebody's final-boss-sized problem.|
N~Early elimination doesn't imply a weak opponent. The draw affects the route considerably.|
N~Tough draw. Still worth learning how they beat him.|
D~He sounds as though he stopped believing he had a chance before it began.|
N~A hard opponent first doesn't make the whole effort worthless. Let the sting settle.|
N~The tournament placed the intimidating part at the front for his convenience. Unkind arrangement.|
N~A short visit with a very concentrated amount of defeat.|
N~I'd separate the unfavorable matchup from decisions he can improve next time.|
N~A difficult beginning can make the path seem shorter than the work behind it.|
N~He expected the favorite to win. I wonder whether that changed how he approached it.|
N~I'd ask whether there was a moment that felt closer than he'd expected.
''')
add('dome_reputation', 'BattleFrontier_BattleDomeLobby_Text_WinnersGainReputation', 'A visitor explains repeated Dome victories attract stronger challengers.', '''
N~Win enough and your reward is more people determined to ruin the winning part.|
N~Reputation creates a feedback loop that attracts stronger opposition. Sustaining success gets harder.|
N~A title draws challengers. Keeping it takes work.|
N~Being known sounds exciting until everyone arrives expecting something from you.|
N~I'd rather build a routine that lasts than spend every day trying to look unstoppable.|
N~Fame has arranged its usual prize: a growing queue of people eager to contradict it.|
N~The reward for winning is an increasingly inconvenient guest list.|
N~A strategy needs to adapt as the opponents get stronger and learn what to expect.|
N~A bright name calls distant eyes toward it. Some arrive carrying a challenge.|
N~Keeping a reputation can ask more of a person than earning the first bit of attention.|
N~I'd ask a frequent winner what changed once other trainers started recognizing them.
''')
add('factory_hints', 'BattleFrontier_BattleFactoryLobby_Text_CantFigureOutStaffHints', 'An adult admits difficulty interpreting the Factory hints.', '''
S~Being grown-up doesn't automatically install the hint decoder. Mine certainly didn't arrive.|
N~Age doesn't guarantee familiarity with specialized clues. He needs a clearer interpretive method.|
N~Ask what the hint means. Being an adult doesn't forbid questions.|
S~I'm glad he admitted it. I'd probably be wondering the same thing quietly.|
N~I'd rather ask twice than pretend I understood and waste a whole attempt.|
N~Adulthood has failed to supply an honorary degree in cryptic receptionist remarks.|
S~A full-grown man has discovered a perfectly ordinary gap in the instructions.|
N~He could compare a hint with the opponent afterward and build a useful reference.|
N~A clue is only helpful when someone can find the handle.|
S~He shouldn't have to apologize for needing the explanation to be clearer.|
N~I'd ask which hint confused him. We might work it out more easily together.
''')
add('factory_knowledge', 'BattleFrontier_BattleFactoryLobby_Text_NeedKnowledgeOfMonsMoves', 'A trainer warns that rental teams still require extensive battle knowledge.', '''
N~Borrowing the Pokemon doesn't come with borrowing somebody else's understanding of them.|
N~Removing the raising requirement leaves team assessment and move knowledge fully relevant.|
N~A ready team still needs a trainer who knows what it's doing.|
N~Meeting a partner for the first time before a challenge sounds difficult in its own way.|
N~Somebody else did the raising. We still have to pay attention to the Pokemon in front of us.|
N~The rental agreement includes the Pokemon, regrettably without a transferable lifetime of expertise.|
N~The team is provided. Competence remains a bring-your-own requirement.|
N~We should inspect the moves and team interactions before deciding how to battle.|
N~A borrowed tool still asks the hand to learn its weight.|
N~He's warning against an easy assumption. Better to hear it here than discover it mid-match.|
N~I'd ask what unfamiliar move caught him out. Specific mistakes can teach a lot.
''')
add('factory_opponent_checks', 'BattleFrontier_BattleFactoryLobby_Text_NeedToCheckOpponentsMons', 'An unsuccessful trainer advises studying opposing Pokemon during rental battles.', '''
N~An opponent can be a future teammate. That's a good reason to pay attention before the handshake.|
N~Observed battle behavior provides information for the later swap decision.|
N~Watch what they actually do before deciding they're worth a swap.|
N~It must be odd choosing someone who was trying to beat you a moment ago.|
N~A familiar species can still carry surprises. Better to learn before making the exchange.|
N~The opposing team is conducting an extremely aggressive job interview.|
N~Today's enemy may become tomorrow's coworker. Take useful notes.|
N~We can track revealed moves and how they complement the existing team.|
N~A hard encounter may leave something useful besides the memory of being hit.|
N~He's looking for better information rather than just another lucky choice. That helps.|
N~I'd ask which detail he wishes he'd noticed earlier. That's usually the useful clue.
''')
add('factory_bad_swap', 'BattleFrontier_BattleFactoryLobby_Text_SwappedForWeakMon', 'A trainer regrets choosing a rental partner based on species rather than its actual strengths.', '''
D~The species looked like the answer. The actual battle filed a rather firm objection.|
N~Species reputation alone doesn't describe the individual moveset or fit within the team.|
N~Check the actual partner, not just the name.|
D~He sounds disappointed in the choice. I'd avoid making the Pokemon the whole blame.|
N~Sometimes a good partner is a bad fit for the plan. That distinction matters.|
N~A promising label has failed to perform the work of a careful inspection.|
N~The name was reassuring. Reality proved less interested in the name.|
N~He needs to compare the role and known moves, not only the species.|
N~An imagined strength can hide the creature actually standing there.|
N~Calling it weak may be easier than explaining why it didn't suit the team.|
N~I'd ask what the swap was supposed to solve and what happened instead.
''')
add('palace_docile', 'BattleFrontier_BattlePalaceLobby_Text_MonDocileButTransforms', 'A trainer is surprised by a docile partner fierce behavior in the Palace.', '''
U~The quiet one apparently had a very forceful opinion saved up for battle.|
N~Behavior changes with context. A docile everyday manner doesn't exclude competitive aggression.|
N~Gentle at home doesn't mean helpless in a fight.|
N~Maybe this is a side they hadn't needed to show before.|
S~I like learning that a familiar partner still has surprises. I'd pay attention rather than panic.|
N~The supposedly mild partner has submitted a dramatic correction to its public description.|
S~Quiet creatures are under no obligation to remain convenient little mysteries.|
N~The Palace reveals choices the trainer usually makes on the Pokemon's behalf. Useful information.|
S~A still pond can hold a very determined current.|
N~They're meeting a less familiar part of someone they thought they knew completely.|
U~I'd ask what it did that looked so different. That sounds worth describing carefully.
''')
add('palace_match_nature', 'BattleFrontier_BattlePalaceLobby_Text_NatureAndMovesKeyHere', 'A trainer advises matching a partner moves to its nature for the Palace.', '''
N~A fine move won't help much if the little expert carrying it refuses to use it.|
N~The rule set makes individual move preferences strategically important. Fit matters.|
N~Build for how the partner acts here. Wishing won't change the rules.|
N~I like that the answer starts with understanding the Pokemon instead of blaming it.|
N~It's easier to work together when you know what someone is comfortable doing.|
N~A brilliant plan must first survive consultation with the creature expected to execute it.|
N~The Pokemon has preferences. The strategy has been asked to accommodate this inconvenience.|
N~We should compare move categories with the nature's behavior before entering.|
N~A path fits better when it follows the shape of the feet walking it.|
N~Sometimes improving the match means changing the plan instead of pushing the partner harder.|
N~I'd ask what adjustment made the biggest difference for their team.
''')
add('palace_lax_guess', 'BattleFrontier_BattlePalaceLobby_Text_WhatNatureFavorsChippingAway', 'A visitor doubts the correct guess that a Lax nature favors indirect interference.', '''
N~He found a possibility and talked himself away from it before anyone could answer.|
N~The nature's name alone isn't a reliable guide to its behavior under Palace rules.|
N~Check the rule instead of arguing with the label.|
N~I know that feeling of distrusting the answer that came to mind first.|
N~A question is easier to settle when you ask someone who knows the system.|
N~An idea has been proposed, cross-examined, and dismissed by a committee of one.|
N~His guess has failed its interview before the evidence arrived.|
N~We can test the preference or consult the relevant data rather than infer it from a name.|
N~A name can point the imagination down entirely the wrong little corridor.|
N~He seems worried the answer sounds silly. That isn't the same as it being wrong.|
N~I'd ask the guide. A direct answer could rescue him from quite a long internal debate.
''')
add('palace_lady', 'BattleFrontier_BattlePalaceLobby_Text_LadyCanTellWhatMonsThink', 'A visitor abandons a battle discussion to praise the girl who reads Pokemon thoughts.', '''
N~He took the scenic route from battle tactics to admitting he likes seeing her visit.|
N~His attraction doesn't establish whether her readings are accurate. Two separate questions.|
N~He can like her. He could also listen to what she's actually saying.|
F~I think he realized halfway through how much he'd said out loud.|
N~He remembers her looks very clearly. I'd ask whether he remembers any of her advice.|
S~A tactical lecture has wandered off and become a rather obvious personal confession.|
N~A formidable offense has encountered a complete failure of subtlety.|
N~I'd rather hear whether her observations helped him understand his team.|
N~He sees the visitor brightly and her words only dimly. Perhaps that can change.|
N~Complimenting her appearance is easy. Taking her thoughts seriously would tell me more.|
N~I'd ask him one question about what she said. He might discover he was listening after all.
''')
add('pike_no_battles', 'BattleFrontier_BattlePikeLobby_Text_NeverHadToBattleTrainer', 'A visitor reports ten completed Pike challenges without a trainer battle.', '''
U~Ten trips and no trainer battles? The trainers must keep choosing a different corridor.|
N~An unusual reported sequence. It doesn't guarantee the same outcome for the next visitor.|
N~Lucky route history. I wouldn't plan around repeating it.|
U~I wonder whether that made the rooms feel calmer or stranger each time.|
N~Good for them. I'd still bring a team ready for the battle they haven't met yet.|
N~A remarkable campaign of successfully failing to meet one's opponents.|
S~The battle facility has provided a prolonged absence of battles. Impressive specialization.|
N~Past routes don't remove the need to prepare for other possible rooms.|
N~An empty path ten times can still have someone waiting on the eleventh.|
U~That's a memorable streak. I hope they're enjoying it without expecting the place to owe them more.|
N~I'd ask what they encountered instead. No trainers doesn't mean nothing happened.
''')
add('pike_near_goal', 'BattleFrontier_BattlePikeLobby_Text_OneRoomAwayFromGoal', 'A trainer lost one room from the Pike goal and warns about status conditions.', '''
D~One room short is a particularly pointy place to lose.|
N~Status conditions can accumulate into a decisive constraint. Proximity to the goal doesn't remove them.|
N~Hard loss. Take the warning seriously before our next entry.|
D~I think the almost part is hurting more than the loss itself.|
N~A near finish can leave you replaying every small choice. Rest before doing that endlessly.|
N~The finish was close enough to be irritatingly specific. A cruel feature of almost.|
N~The last room has become much larger in memory than any room deserves.|
N~We should account for condition protection when choosing partners and held items.|
D~A threshold can be visible and still remain out of reach. That hurts.|
N~He has turned the frustration into one useful warning. That part is generous.|
N~I'd ask which condition caused the turning point once he's ready to talk about it.
''')
add('pike_abilities', 'BattleFrontier_BattlePikeLobby_Text_ThinkAbilitiesUsefulHere', 'A visitor suggests Pokemon abilities may be especially useful in the Pike.', '''
S~The little things a Pokemon does without being asked might become very big advantages here.|
N~Passive abilities can affect hazard resilience and encounters. A sound avenue to examine.|
N~Yes. Choose for more than attacks.|
N~I like noticing the strengths that don't need a shouted command.|
N~A partner may help the whole trip simply by being the kind of Pokemon it is.|
N~A sensible reminder that the team contains more useful features than the move list.|
S~The quiet advantages would like a moment of recognition.|
N~We should review each ability against the possible room effects.|
N~Some gifts work quietly enough that people forget to thank them.|
N~It's good advice for anyone focused only on what looks impressive in a battle.|
N~I'd compare notes with someone who used an ability to avoid a difficult room effect.
''')
add('pyramid_lost_items', 'BattleFrontier_BattlePyramidLobby_Text_LostLotOfItems', 'A distraught explorer lost accumulated Battle Bag items after a failed expedition.', '''
D~That wasn't only a loss. It was a whole collection of useful little hopes falling out at once.|
N~The Battle Bag loss rule makes accumulated supplies vulnerable when an expedition fails.|
N~Rough. Let him be upset before offering another plan.|
D~I don't think he wants advice yet. I think he wants someone to understand how much was there.|
N~I'd find somewhere quiet for him to sit. Counting everything again won't make this easier right now.|
D~An inventory has become a lament, with every missing item apparently joining the chorus.|
D~The expedition took the supplies and left him with a very thorough explanation of grief.|
N~Once he's ready, we can look at what led to the failure and how to protect the next run.|
D~A bag holds more than things once you've struggled to gather them.|
D~He lost the work those items represented as well as the items themselves.|
D~I'd let him tell us what happened at his own pace. The shouting sounds like real frustration.
''')
add('pyramid_running', 'BattleFrontier_BattlePyramidLobby_Text_TrainersNoticeRunning', 'A visitor advises quiet movement to avoid attracting Pyramid trainers.', '''
N~The Pyramid notices an enthusiastic pair of feet. Mine will attempt to become boring.|
N~Running changes how trainers detect the explorer. Movement speed becomes a tactical choice.|
N~Slow down if we're trying to avoid a battle. Simple enough.|
N~Quiet steps feel sensible in a place where we can't see far ahead.|
N~No need to hurry into a fight we meant to avoid.|
N~A useful case in which making a dramatic entrance is explicitly the wrong approach.|
N~The floor has no interest in our athletic ambitions. Walk politely.|
N~We can trade speed for lower attention when preserving resources matters.|
N~A quiet foot can leave a larger distance between us and trouble.|
N~Small habits can announce us before we've decided whether we want company.|
N~I'd ask how close they got before being noticed. That could help us judge the spacing.
''')
add('exchange_goodbye', 'BattleFrontier_ExchangeServiceCorner_Text_ThankYouVisitWithPoints', 'The exchange clerk closes shopping and welcomes a later visit with saved points.', '''
S~A whole counter of lovely things, and we are allowed to leave without adopting them all.|
N~The shopping session has ended. This farewell doesn't specify whether a purchase occurred.|
N~Done shopping. We can decide what to save for next.|
S~I like having time to think instead of choosing just because the list is open.|
N~I'd save for something we'll actually use, or something that genuinely makes us happy.|
S~The clerk releases us from the menu and sends us back into the economy of effort.|
S~The prizes remain. Our impulse to own every cushion may hopefully subside.|
N~We can compare the point costs with our priorities before returning.|
S~Wanting something can wait without spoiling it.|
S~A polite goodbye gives us room to decide what belongs in our life.|
N~I'd ask everyone which prize they remember afterward. The favorites usually become clear.
''')
add('exchange_decor_full', 'BattleFrontier_ExchangeServiceCorner_Text_PCIsFull', 'A decoration exchange fails because decoration storage is full.', '''
N~The new decoration has reached the border of an already very decorated life.|
N~Storage capacity prevented the exchange. The decoration wasn't delivered.|
N~No room. Sort what we have before trying again.|
N~It's a little disappointing to choose something and find nowhere for it.|
N~We should make space deliberately instead of clearing something we still like in a hurry.|
N~The collection has become so successful that it now objects to further collecting.|
N~The dolls have apparently occupied all available territory.|
N~We need a free decoration slot before this transaction can succeed.|
N~A crowded shelf is also a record of earlier wishes. Choose carefully what moves.|
N~I would look through the collection before deciding another piece has to fit.|
N~I'd like to see what's already there. We may rediscover something worth displaying.
''')
add('exchange_bag_full', 'BattleFrontier_ExchangeServiceCorner_Text_DontHaveSpaceToHoldIt', 'An item exchange fails because the player cannot carry it.', '''
N~We've earned the choice but failed the carrying portion of the examination.|
N~The item was not received because carrying capacity prevented delivery.|
N~Make room first. The points aren't a substitute for space.|
N~At least we found out here instead of dropping something outside.|
N~Time to sort the bag before asking for more things to put in it.|
N~A promising purchase has encountered the implacable physics of a full bag.|
N~The bag has exercised its right to refuse further responsibility.|
N~We can reorganize and return. No need to force the transaction now.|
N~Even a useful thing needs somewhere to arrive.|
N~I'd rather make space thoughtfully than discard the first thing we touch.|
N~We should check what we've been carrying around without using. There may be an easy fix.
''')
add('exchange_protective_doll', 'BattleFrontier_ExchangeServiceCorner_Text_GoGetYourOwnDoll', 'A man defensively tells the player to obtain their own plush doll.', '''
N~I admired the doll. I hadn't realized it needed a personal security detail.|
N~Looking at an object doesn't establish an intention to take it. His reaction is disproportionate.|
N~We're looking. The doll is safe.|
F~I didn't mean to make him uncomfortable. I just thought it was nice.|
N~He can enjoy his doll. There's no need to bark at somebody for noticing it.|
N~An innocent glance has triggered a full defense of the plush estate.|
N~The doll has acquired an unusually aggressive legal representative.|
N~If he dislikes attention, pointing it out to everyone may be counterproductive.|
N~A soft thing is being guarded with rather sharp words.|
N~He doesn't have to justify loving a plush. I wish he knew that before going on the attack.|
N~I'd leave him to enjoy it. No reason to turn a passing glance into a feud.
''')
add('exchange_items_power', 'BattleFrontier_ExchangeServiceCorner_Text_ItemsWillGetMonTougher', 'A sailor expects the exchange items to strengthen his Pokemon.', '''
S~He has found the shopping list of his dreams. The actual training may still want a word.|
N~Suitable items can help, but their value depends on the partner and intended use.|
N~Useful gear helps. It won't replace a sound plan.|
N~I hope he keeps seeing his partner underneath all the improvements he's imagining.|
N~I'd choose what suits the Pokemon, rather than whatever sounds most powerful on the shelf.|
N~A confident forecast issued before the items have even left the counter.|
N~The merchandise has been assigned responsibility for an entire future victory.|
N~He should match each item's effect to a specific need in the team.|
N~A useful gift fits the creature receiving it. The wish alone isn't enough.|
N~He sounds eager to help his Pokemon. A more specific choice would serve that wish better.|
N~I'd ask which item he wants first and what problem he expects it to solve.
''')
add('exchange_mother', 'BattleFrontier_ExchangeServiceCorner_Text_GetYouAnythingYouWant', 'A mother promises to overcome anything to obtain the prize her child wants.', '''
S~That's a devoted promise. I wonder which plush has persuaded her to take on the island.|
N~Her affection is clear. A specific goal and manageable effort would make the promise more practical.|
N~She wants to make the kid happy. She can still set a limit.|
S~It's sweet hearing somebody feel that supported. I hope she enjoys the visit herself, too.|
N~A gift is lovely. She doesn't have to wear herself out proving how much she cares.|
S~An innocent prize counter has received a declaration of unlimited maternal determination.|
S~Somewhere on the shelf, a doll has no idea what it's started.|
N~She could set a point target and work toward it without turning the visit into an ordeal.|
S~Love can make a small wish feel worth a very long journey.|
N~I'd like the child to know her company is a gift before the prize ever arrives.|
S~I'd ask which prize caught their eye. She's certainly ready to hear the answer.
''')
add('exchange_every_doll', 'BattleFrontier_ExchangeServiceCorner_Text_WishIHadAllDolls', 'A shopper wants every size of doll and cushion on display.', '''
S~Big dolls, little dolls, cushions. His wish list has discovered categories and refuses to stop.|
N~The desire concerns the entire assortment. Prioritizing one choice may be more manageable.|
N~Pick a favorite first. A room still needs somewhere to walk.|
S~I understand wanting several soft things. All of them sounds difficult to carry home.|
S~I'd start with the one that makes him smile most when he looks back at the shelf.|
S~A collector surveying an empire he intends to acquire one extremely soft province at a time.|
S~The ambition is vast. The proposed population is entirely plush.|
N~He should measure the available space before assigning every doll a future address.|
S~A wish can grow until it fills the room before a single thing has arrived.|
U~The big and little pieces could look wonderful together. We'd still need an arrangement.|
S~I'd ask whether he already has a collection. That level of enthusiasm suggests a story.
''')
add('exchange_streak_points', 'BattleFrontier_ExchangeServiceCorner_Text_MoreBattlePointsForRecord', 'A visitor explains that longer facility records increase Battle Point awards.', '''
S~The longer the streak, the more the prize shelf starts looking reachable.|
N~Rewards increase with extended records. The expected effort still varies by facility and skill.|
N~Useful to know. Chasing more points still needs a sensible stopping point.|
N~I'd rather build up steadily than make every match feel like a shopping deadline.|
N~A bigger award is nice. Resting before mistakes pile up is nice, too.|
N~Success has acquired a loyalty program. Predictably, it requires more success.|
S~The winning streak receives encouragement to become even more of itself.|
N~We can account for the reward structure when choosing a facility goal.|
N~A growing reward can make a tired person forget how far they've walked.|
N~I like knowing the system before setting a goal. It makes the choices less hazy.|
N~I'd ask which facility they found most rewarding for the time they actually enjoyed spending.
''')
add('gambler_tower_single', 'BattleFrontier_Lounge3_Text_GetToBattleTowerSingle', 'The gambler urges the player toward Tower Singles because the wager depends on it.', '''
N~His future has apparently climbed into our Tower appointment without asking for a seat.|
N~The instruction identifies Tower Singles. His urgency doesn't change the challenge requirements.|
N~Tower Singles. We heard him. The pressure isn't helping.|
N~Both our futures sounds like an awful lot to put on one visit.|
N~I'd rather prepare calmly than carry his panic through the Tower door.|
N~A wager has become an extravagant prediction about the fate of two entire lives.|
N~The Tower is tall enough without him adding emotional floors.|
N~We'll need a Singles plan. His shouting contributes no useful part of one.|
N~He has tied his hopes to our climb. We still have to choose each step.|
N~That urgency is his feeling. We don't need to wear it as our own.|
N~I'd confirm the event, then step outside for a quieter moment before starting.
''')
add('gambler_tower_double', 'BattleFrontier_Lounge3_Text_GetToBattleTowerDouble', 'The gambler demands success in the Tower Double challenge.', '''
N~Two Pokemon at once, plus one very demanding voice we'd best leave in this room.|
N~Tower Doubles requires coordination. Anxiety about the wager supplies no tactical advantage.|
N~Doubles, then. We should check how the partners work together.|
N~I'd like a little quiet before making a decision with two partners depending on it.|
N~His points are invested. Our attention still belongs with the team.|
N~He has volunteered us for a rescue mission in the doubles division. How generous of him.|
N~Two active partners are enough company. His panic needn't become the third.|
N~We should review paired moves and avoid interfering with our own partner.|
N~Two paths must move together. A stranger's urgency won't align them.|
N~He makes the wager sound personal. The practical work is still ours to do.|
N~I'd rather talk through our pairings than listen to another warning about blowing it.
''')
add('gambler_tower_multi', 'BattleFrontier_Lounge3_Text_GetToBattleTowerMulti', 'The gambler sends the player to the Tower Multi challenge with exaggerated urgency.', '''
N~We're finding a battle partner while he auditions to be an entire crowd of pressure.|
N~Multi Battles add another trainer's decisions. His demand can't control that variability.|
N~Need a good partner. Not a louder gambler.|
N~I hope the person beside us feels easier to talk to than he does.|
N~A calm conversation with our partner will help more than his dramatic instructions.|
N~He has invested in teamwork and expressed it by speaking as though nobody else has a choice.|
N~A team event, burdened with a spectator who has mistaken himself for management.|
N~We should understand our partner's team before attempting a coordinated challenge.|
N~Trust grows between the people doing the work. His wager stands outside that circle.|
N~He wants a result from people whose cooperation he isn't helping.|
N~I'd ask the battle partner about their plan first. We need a conversation that goes both ways.
''')
add('gambler_dome_single', 'BattleFrontier_Lounge3_Text_GetToBattleDomeSingle', 'The gambler insists the player win the Dome Singles tournament for the bet.', '''
N~The tournament bracket apparently contains our opponents and his entire peace of mind.|
N~Dome Singles involves selection against known opponents. That deserves more attention than his urgency.|
N~We'll inspect the opponents. Rushing the selection won't help.|
N~It's harder to think when somebody keeps announcing how much depends on you.|
N~A breath before choosing is worth more than a hurried promise.|
N~He has turned a tournament entry into a personal emergency without consulting the tournament.|
N~The bracket has enough branches without his worries growing extras.|
N~We need to select the right pair from the information available at the Dome.|
N~A chart can show the route. It cannot promise who reaches the end.|
N~He's trying to make certainty out of insistence. The match won't work that way.|
N~I'd focus on the first matchup rather than try to carry the whole tournament at once.
''')
add('gambler_dome_double', 'BattleFrontier_Lounge3_Text_GetToBattleDomeDouble', 'The gambler pressures the player to enter the Dome Double tournament.', '''
N~A doubles tournament and double the urgency, somehow from the same single man.|
N~The requested event is Dome Doubles. Pair compatibility and opponent information remain essential.|
N~Prepare the pair. His impatience can stay here.|
N~I'd like the two partners to feel settled before everybody starts expecting a grand result.|
N~We should choose carefully instead of treating his worry like a countdown.|
N~He is remarkably eager for us to perform a strategy he has contributed nothing toward.|
N~An entire tournament has been reduced to please fix my bet. Concise, if unpleasant.|
N~The pair needs to function against the selected opponents, not merely look strong together.|
N~Two companions will carry the work. His hope adds weight without adding strength.|
N~He keeps saying chance as though it becomes safer when spoken loudly.|
N~I'd check the matchup information before agreeing with any of his predictions.
''')
add('gambler_factory_single', 'BattleFrontier_Lounge3_Text_GetToBattleFactorySingle', 'The gambler urgently assigns the Factory Singles rental challenge.', '''
N~He trusts us with his future before we've even met the Pokemon supposed to help carry it.|
N~The rental roster is not yet known. A guarantee would be particularly unjustified here.|
N~We need to see the rentals before making a plan.|
N~New partners and somebody else's expectations. That's quite an introduction.|
N~We'll take time to understand the rentals. They deserve more attention than his deadline.|
N~An urgent demand for mastery of a team we haven't been introduced to. Delightfully reasonable.|
N~The unknown team has already been assigned responsibility for two futures. Busy day.|
N~Inspect the rental moves first, then build a Singles strategy around the actual options.|
N~Borrowed company still needs a moment to become familiar.|
N~He wants instant confidence. The unfamiliar partners need careful attention instead.|
N~I'd ask the staff about the selection process and give each option a proper look.
''')
add('gambler_factory_double', 'BattleFrontier_Lounge3_Text_GetToBattleFactoryDouble', 'The gambler sends the player toward the Factory Double rental event.', '''
N~We have to find two borrowed partners who agree on a plan. He has helpfully provided shouting.|
N~Rental Doubles requires assessing interactions within an unfamiliar roster. Haste is unhelpful.|
N~Two rentals need to work together. We'll choose carefully.|
N~I want enough time to notice which partners seem comfortable beside each other.|
N~A patient introduction can save a messy battle. The wager won't change that.|
N~He wants a triumph assembled from unfamiliar parts, preferably before we've read the instructions.|
N~The borrowed team has been handed an urgent problem by a man lending nothing but pressure.|
N~We need compatible moves and roles from the rentals actually offered.|
N~Two strangers may find a rhythm. They cannot be hurried into knowing one another.|
N~He sees a destination. I'm thinking about the partners who have to get us there.|
N~I'd compare how the rental options help each other before selecting the strongest-looking individuals.
''')
add('gambler_palace_single', 'BattleFrontier_Lounge3_Text_GetToBattlePalaceSingle', 'The gambler demands Palace Singles success despite the Pokemon acting independently.', '''
N~He wants us to control our future at the building where we don't give the battle commands.|
N~The Palace limits direct control. His certainty is especially misplaced under that format.|
N~Prepare the partner. We can't shout the decisions into place there.|
N~It might be a relief to leave his voice outside and watch our Pokemon for a while.|
N~Our partner needs a suitable set of moves, not somebody else's panic.|
N~He has selected a remarkably awkward venue for demanding complete control of the outcome.|
N~A command to guarantee victory in the no-command building. Beautifully inconsistent.|
N~We should match the moves to the nature before entering the Single Battle Hall.|
N~Some outcomes require a loosened hand. He seems determined to close his.|
N~He might learn something by watching a challenge he can't manage through demands.|
N~I'd focus on understanding the Pokemon's choices. That's more useful than pretending we can promise them.
''')
add('gambler_palace_double', 'BattleFrontier_Lounge3_Text_GetToBattlePalaceDouble', 'The gambler urgently requests the Palace Double challenge.', '''
N~Two independent minds will be battling. He seems disappointed not to be appointed a third.|
N~Palace Doubles combines autonomous choices. Preparation can help without guaranteeing coordination.|
N~Pick a compatible pair. Then let the Palace rules do their work.|
N~I'd rather trust the partners than let his worry drown out everything I know about them.|
N~Both Pokemon deserve a plan that suits them before the challenge starts.|
N~He has enormous confidence in our ability to command an event that discourages commands.|
N~Two Pokemon may exercise their judgment. He has apparently opted out of exercising his.|
N~We need to consider both natures and the interaction of their available moves.|
N~Two wills share a room. The wager doesn't get to become either one.|
N~His insistence leaves no room for uncertainty. The actual rules leave plenty.|
N~I'd watch how each partner behaves and keep the gambler's expectations outside the hall.
''')
add('gambler_arena', 'BattleFrontier_Lounge3_Text_GetToBattleArena', 'The gambler pressures the player to succeed in the Arena Set KO challenge.', '''
N~Three turns per battle, and he's already used several imaginary turns on worrying at us.|
N~The Arena has specific scoring constraints. Emotional urgency offers no substitute for meeting them.|
N~Order the team properly. Ignore the extra pressure.|
N~A short battle can still feel very long with that speech hanging over it.|
N~I'd rather check the team than promise him anything while he's worked up.|
N~He has converted the Set KO Tourney into an urgent referendum on our shared destiny.|
N~The referee evaluates battles. Fortunately, this speech is outside the judging area.|
N~Prepare sequential coverage and moves that function within the three-turn rules.|
N~A short measure of time can hold plenty of consequence without his adding more.|
N~He wants us hurried and certain. Careful and prepared seems more useful.|
N~I'd talk through the opening partner before stepping into a format with so little recovery time.
''')
add('gambler_pike', 'BattleFrontier_Lounge3_Text_GetToBattlePike', 'The gambler urgently sends the player into the chance-heavy Pike challenge.', '''
N~He's asking us to hurry over and make luck behave. I'll add that to its suggestion box.|
N~The Pike includes variable encounters. We can prepare for them, not promise their sequence.|
N~We can handle preparation. We can't sign a guarantee on luck.|
N~I wish he'd stop treating an uncertain route like a broken promise waiting to happen.|
N~We'll prepare for the possibilities and take the rooms as they come.|
N~A man who chose a wager is now expressing outrage at the general concept of uncertainty.|
N~Luck has been ordered to report for duty. No response yet.|
N~Choose for resilience across possible room effects. That's the part we can influence.|
N~A door conceals what it conceals. His hopes don't change its contents.|
N~He makes the chance sound like our personal responsibility. It isn't that simple.|
N~I'd review the possible hazards instead of letting his deadline choose our pace.
''')
add('gambler_pyramid', 'BattleFrontier_Lounge3_Text_GetToBattlePyramid', 'The gambler sends the player into a Pyramid expedition with exaggerated stakes.', '''
N~A dark maze, limited supplies, and now his entire future in the luggage. Travel light, he says.|
N~A Pyramid expedition requires resource management. His urgency may conflict with cautious exploration.|
N~Plan the supplies. Move carefully. He can wait.|
N~I'd prefer fewer expectations to carry into a place where we can't see far ahead.|
N~A quiet meal and a clear plan would help more than this farewell.|
N~He has contributed to the expedition by increasing the weight of the invisible baggage.|
N~The Pyramid has gained one additional hazard, mercifully unable to follow us inside.|
N~We need to manage the Battle Bag and pace the climb according to conditions.|
N~He calls us toward the summit. The next visible step still matters more.|
N~His wishes are loud. The actual warning signs may be quiet, so I'd listen for those.|
N~I'd prepare for the expedition itself rather than picture his reaction at the end.
''')
add('scott_equal_battles', 'BattleFrontier_ScottsHouse_Text_WhyIGoSeekingTrainers', 'Scott explains that he seeks trainers because battle brings different people into equal competition.', '''
S~He likes meeting all sorts of people, then finding them one shared way to say hello.|
N~Common rules provide a shared framework. People still arrive with different resources and experience.|
N~A fair contest is worth building. Keep the rules fair for the people using it.|
S~I like hearing that everyone's ordinary life doesn't decide whether they belong in a match.|
S~Different people need somewhere they can meet without carrying every outside label in first.|
S~An ambitious ideal, and a much better reason for traveling than merely collecting impressive acquaintances.|
N~People are complicated. A clear set of rules offers them somewhere slightly less complicated to argue.|
N~The equal framework is useful. Making the facilities accessible and consistent keeps it meaningful.|
S~Different roads can meet on a small, level patch of ground. That is worth tending.|
N~I like the welcome in his idea. I'd want that spirit to survive when the visitor isn't famous.|
S~I'd ask which meeting stayed with him longest. All that traveling must have changed the idea, too.
''')
