"""Verified static Tower partner refusal responses, independently authored by ending."""
ROWS = []
EMOTIONS = dict(N='neutral', S='soft_smile', A='annoyed', F='flustered', D='sad', U='surprised', M='smug', L='laughing')

def add(key, labels, subject, lines):
    replies = [x.strip() for x in lines.strip().split('|')]
    replies = [EMOTIONS[x[0]] + x[1:] for x in replies]
    assert len(replies) == 11, (key, len(replies))
    ROWS.append(dict(key='hpt_'+key, labels=labels.split(), subject=subject, replies=replies))

add('apprentice1', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_Apprentice1Reject', 'A rejected former apprentice bursts into tears.', '''
D~Oh dear. That's a very small no making a very large puddle.|
N~The refusal has clearly hurt. We can clarify without changing our choice.|
N~Let them settle. No need to make an audience of this.|
D~I feel bad. I still don't think a guilty yes would help either of us.|
D~A quiet word would be kinder than leaving them crying in the crowd.|
D~The disappointment has arrived at full volume before an explanation could catch it.|
D~A public room is an unfortunate place for private feelings to overflow.|
N~We can explain that this team choice isn't a verdict on their entire progress.|
D~A small refusal has touched something deeper than the question we answered.|
N~I'd offer some privacy instead of pretending not to notice.|
D~I'd stay nearby for a moment, if they wanted company while settling down.
''')
add('apprentice2', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_Apprentice2Reject', 'A former apprentice asks why the player declined the hoped-for partnership.', '''
N~They had the team-up planned a little farther ahead than we did.|
N~Their expectation wasn't shared. A clear explanation may help reset it.|
N~They can ask why. We can answer without promising another team.|
D~They sound so disappointed to hear it from us specifically.|
N~I'd explain the choice kindly rather than make them guess at a fault.|
N~A cheerful imagined partnership has encountered the less cooperative actual answer.|
N~The plan existed quite firmly on one side of the conversation.|
N~We should distinguish team fit from their worth as a trainer.|
D~An expected door closed. The person outside deserves a gentle word.|
N~They thought knowing us made the answer certain. That's hard to unlearn.|
N~I'd give a specific reason if we have one. Vague reassurance can confuse things.
''')
add('apprentice3', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_Apprentice3Reject', 'A former apprentice quietly admits hoping to join the player tag team.', '''
D~They saved a hopeful little place for us in the plan. I wish no didn't sound so sharp.|
N~The disappointment is restrained, but plainly expressed. It deserves acknowledgment.|
N~A quiet refusal still needs a kind answer.|
D~They didn't argue. Somehow that makes me want to choose my words more carefully.|
N~I'd thank them for wanting to join us without offering a promise I can't keep.|
D~An entire hoped-for afternoon has been folded into that small sentence.|
D~No grand protest. Just a hope setting down its bag.|
N~We can explain the current pairing decision without making it permanent rejection.|
D~Some hopes leave very quietly. It's still possible to hear the door.|
N~I'd rather acknowledge the disappointment than rush to make it disappear.|
D~I'd ask whether they'd like to talk about another challenge they plan to try.
''')
add('apprentice4', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_Apprentice4Reject', 'The former apprentice interprets declining a team as proof of being inadequate.', '''
D~Oh, no. One empty team slot is not a measuring cup for a whole person.|
N~That conclusion goes beyond the decision. A declined pairing doesn't establish inadequacy.|
N~Not the right pair today doesn't mean not good enough.|
D~It sounds as though they were waiting for someone to confirm a fear.|
N~I'd be very clear that this wasn't a judgment on all their work.|
N~They have turned a team-selection answer into an unfair examination of their entire worth.|
D~A doubt arrived early and is now pretending it predicted everything.|
N~A concrete explanation would be better than leaving that assumption unchallenged.|
D~An old worry can wear a new event like borrowed proof.|
N~I don't want our choice becoming a sentence they keep repeating about themselves.|
N~I'd mention something specific they've done well, without bargaining over the team choice.
''')
add('apprentice5', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_Apprentice5Reject', 'The refused apprentice attacks the player judgment of character.', '''
N~The character assessment seems to have changed the instant we said no. Curious timing.|
N~A rejected proposal doesn't demonstrate defective judgment of character.|
N~Insulting us won't make the partnership a better fit.|
N~I think that was hurt speaking faster than they meant it to.|
N~I'd let the temper settle before trying to explain anything.|
N~A single refusal has apparently invalidated our entire ability to understand people.|
N~The verdict arrived suspiciously close to the disappointment.|
N~We can keep the explanation factual instead of answering the insult.|
N~A bruised hope has found a sharp edge. Best not to press against it.|
N~It's possible to feel rejected without making somebody else the villain.|
N~I'd return to the actual team choice once they're ready to discuss that.
''')
add('apprentice6', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_Apprentice6Reject', 'The apprentice complains about taking time from a busy schedule for the refused team.', '''
N~Their calendar has filed a complaint. It still can't choose our partner for us.|
N~Time invested before agreement doesn't create an obligation to accept the proposal.|
N~They chose to come. That doesn't settle our choice.|
N~I understand being disappointed after setting time aside. I don't like being blamed for it.|
N~We can respect their time without spending ours on a team we didn't choose.|
N~An appointment made entirely on their own behalf has somehow generated an invoice for us.|
N~The schedule is busy and has become rather argumentative.|
N~Next time, confirming plans first would prevent this mismatch.|
N~An empty space in a calendar isn't a promise from another person.|
N~Their effort matters. Treating it as a debt we owe won't help.|
N~I'd ask whether there was an actual arrangement we missed before accepting the accusation.
''')
add('apprentice7', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_Apprentice7Reject', 'A refused apprentice calls the player mean and cites a recommendation.', '''
N~The recommendation didn't come with a mandatory-team stamp. At least, I didn't see one.|
N~An endorsement can support consideration. It can't guarantee compatibility or consent.|
N~A recommendation isn't an order to team up.|
D~They seem to have trusted that recommendation to make this feel safe.|
N~I'd acknowledge the good word without letting it make the decision for us.|
N~The recommendation has been presented as though it were an admission ticket with assigned seating.|
N~A reference has been mistaken for a binding contract.|
N~We still need to evaluate the actual team combination ourselves.|
N~Another person's good opinion can open a door, not hold someone inside it.|
N~Being recommended is encouraging. It doesn't make a refusal deliberately unkind.|
N~I'd ask what the recommendation said. It may still be useful information for a future choice.
''')
add('apprentice8', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_Apprentice8Reject', 'The apprentice expresses personal disappointment after hoping to join the player.', '''
D~They sound as though they kept that hope warm all the way here.|
N~The response expresses disappointment without demanding we reverse the decision.|
N~They took it calmly. Let's answer with the same respect.|
D~Hearing our name in the answer makes the disappointment feel very close.|
N~A sincere thank-you for the offer seems better than hurried reassurance.|
D~A quiet answer can carry rather more weight than a loud complaint.|
D~The hope was ordinary and quite genuine. An inconvenient thing to disappoint.|
N~We can leave future possibilities open without promising a specific team.|
D~A familiar name makes the space between two choices feel smaller.|
N~I'd like them to know the invitation mattered, even though we didn't accept.|
D~I'd check in later about how their own challenge went, if they wanted to tell us.
''')
add('apprentice9', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_Apprentice9Reject', 'The apprentice asks for pity but then admires the refusal as cool.', '''
U~That was a fast trip from heartbreak to admiration. I nearly needed directions.|
N~They seem to interpret detachment as impressive even while seeking sympathy.|
N~Don't let a cool image decide who gets treated kindly.|
F~I'm not sure which response they want from us now.|
N~I'd rather be straightforward than play the cold person they seem to admire.|
U~The complaint has unexpectedly become a compliment before reaching its final punctuation.|
N~Their disappointment appears to have developed an inconvenient admiration for itself.|
N~A clear explanation may be less confusing than acting out either role.|
N~Some people reach for warmth and then praise the frost that meets them.|
N~I wish they didn't feel they had to admire being hurt to make it look acceptable.|
N~I'd ask whether they're actually all right, away from the performance of being impressed.
''')
add('apprentice10', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_Apprentice10Reject', 'The apprentice calls the player calculating after the partnership is declined.', '''
N~Thinking about a team has apparently been upgraded to scheming. That's a large promotion.|
N~Deliberate selection is appropriate here. Calculation isn't necessarily callousness.|
N~We should think about the pairing. That's part of the challenge.|
N~I don't want making a careful choice to sound like we don't care about them.|
N~A clear reason could help separate thoughtfulness from the insult they heard in no.|
N~Our tactical decision has received a rather grand accusation of sinister arithmetic.|
N~The numbers have been blamed for a feeling they didn't create alone.|
N~The choice should account for actual team interactions. That's reasonable planning.|
N~Care can count carefully. It isn't always a spontaneous yes.|
N~They may want the choice to be purely personal. That isn't how a team decision works.|
N~I'd explain one practical consideration instead of arguing over the label.
''')
add('apprentice11', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_Apprentice11Reject', 'The refused apprentice jokes about wrecking the Tower and immediately retracts it.', '''
U~The whole Tower briefly appeared on the disappointment list. Glad it has been released unharmed.|
N~They immediately identify the destructive remark as a joke. No actual damage is indicated.|
N~Good that they walked the joke back. Keep the building out of it.|
F~I was worried for a second. Then I realized they were trying to make the disappointment funny.|
N~A joke can ease the sting. I'd still prefer one that doesn't make everyone look at the walls.|
L~A catastrophic building review, revoked before the maintenance crew could be consulted.|
S~The architecture has survived an imaginary incident. A narrow escape.|
N~The Tower isn't part of the disagreement. Sensible to correct the exaggeration.|
S~A storm was announced and then politely canceled before the roof noticed.|
N~I think they wanted a laugh rather than a scene. The quick correction helped.|
S~I'd give the joke a small smile and leave the actual disappointment room to exist.
''')
add('apprentice12', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_Apprentice12Reject', 'The apprentice delivers a rhyming complaint about the cold refusal.', '''
S~The disappointment came with a rhyme. At least it brought its own little blanket.|
N~The wordplay softens the complaint without changing the refused proposal.|
N~A neat rhyme. Still the same decision.|
S~I almost smiled before remembering they really were disappointed.|
S~Sometimes making a small joke is how people keep an awkward moment manageable.|
S~A tidy little verse has been recruited to escort hurt feelings through a public room.|
S~The temperature complaint has arrived with matching endings. Thoughtful packaging.|
N~We can appreciate the humor without pretending we accepted the team.|
S~A small rhyme can give a difficult feeling something to lean on.|
S~They found a way to sound disappointed without turning cruel. I appreciate that.|
S~I'd ask whether they always think of rhymes that quickly. It was an unexpectedly deft response.
''')
add('apprentice13', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_Apprentice13Reject', 'The apprentice turns the refusal into a rhyme about frowning.', '''
S~They've made the frown rhyme. I suppose that gives the sadness a tidy little hat.|
N~The response communicates disappointment through playful language rather than an accusation.|
N~They can be disappointed. We can still be kind about the choice.|
D~A funny line doesn't mean it didn't hurt. I'd remember that.|
S~I'd answer warmly without trying to buy the smile back with a promise.|
S~A brief rhymed protest, mercifully without a demand for a complete revised ending.|
S~A frown has acquired structure. It may feel slightly less untidy now.|
N~We should keep the response clear rather than let the wordplay obscure our decision.|
S~Even a small frown sometimes wants to arrive holding a little dignity.|
S~They've left room to smile at the wording while taking the feeling seriously.|
S~I'd like to hear them tell a happier story another time. The delivery has charm.
''')
add('apprentice14', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_Apprentice14Reject', 'The apprentice thinks the pair would work well despite the player refusal.', '''
N~They still see a good team where we haven't chosen one. Two views can fit in the room.|
N~Their positive assessment doesn't require us to reach the same selection decision.|
N~Maybe we would. We still get to choose a different partner.|
D~They sound hopeful even after the answer. I wouldn't leave it vague.|
N~I'd explain what we're looking for rather than argue that their idea was bad.|
N~A promising partnership can remain merely possible. Not every good idea becomes today's plan.|
N~The alternate future appears pleasant. Unfortunately, it isn't the one we've selected.|
N~A particular team goal may call for another combination without making theirs weak.|
N~Two branches can both be healthy. We still walk along only one at a time.|
N~They made a positive case without insulting the choice. That's fair.|
N~I'd ask what they thought would work especially well. It may be useful to understand.
''')
add('apprentice15', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_Apprentice15Reject', 'The apprentice pleads against rejection because they already feel self-conscious.', '''
D~They've brought a worried little heart to a room full of people choosing partners. Hard place.|
N~Their existing self-consciousness amplifies the refusal. It doesn't require an insincere acceptance.|
N~Be gentle. Don't make a promise we won't keep.|
D~I understand wanting one answer to make the whole room feel less frightening.|
N~I'd offer a quiet explanation, away from anyone who might turn it into a spectacle.|
D~A team choice has landed on a feeling that was already sore. Tread carefully.|
D~The refusal arrived at an occupied bruise. That deserves care.|
N~We can explain the specific pairing issue rather than leave them imagining a broader judgment.|
D~A crowded room can make one small no echo far too long.|
D~I'd want them to feel seen without feeling examined. There's a difference.|
N~I'd check whether they'd prefer space or a quiet conversation. Neither needs an audience.
''')
add('apprentice16', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_Apprentice16Reject', 'The apprentice questions whether the player refusal is a joke.', '''
N~They've checked for a hidden punch line. The answer unfortunately arrived without one.|
N~Their expectation makes the refusal seem implausible. Clarifying our intent should help.|
N~It's a real choice. Best to say that clearly.|
F~I don't want them waiting for a joke to end when we meant the answer.|
N~A kind, plain explanation beats leaving somebody unsure whether they're being teased.|
N~They are searching the refusal for comic intent. It would be unkind to prolong the search.|
N~The conversation has misplaced the boundary between surprise and a joke.|
N~We should confirm the decision without making the surprise itself something to ridicule.|
N~An unexpected answer can sound unreal before it begins to hurt.|
N~I'd make sure they know we aren't playing with them. That matters more than sounding clever.|
N~I'd explain calmly and give them time to absorb it rather than rush to the next person.
''')
add('lass', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_LassReject', 'The refused Lass predicts the player will regret declining her.', '''
N~That no has apparently booked us an appointment with future regret. We'll check the calendar later.|
N~The prediction expresses displeasure. It isn't evidence about the best pairing.|
N~A warning won't make us choose her.|
N~I wish disappointment didn't have to become a little threat.|
N~We can let her be upset without arguing about an imagined future.|
N~She has sent our decision forward in time for disciplinary review.|
N~Future regret has been volunteered without being consulted.|
N~We should keep evaluating the actual team options.|
N~A closed choice doesn't need a shadow laid across every later one.|
N~She wants us to feel uncertain now. That doesn't improve the offer.|
N~I'd leave it politely rather than compete over who will be right later.
''')
add('youngster', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_YoungsterReject', 'The Youngster imagines an unstoppable tag team after the player declines.', '''
S~An unstoppable team has been stopped at the agreeing-to-be-a-team part. Awkward weakness.|
N~The imagined strength hasn't been tested. His enthusiasm is clearer than the prediction.|
N~Could have been good. Unstoppable is a bigger claim.|
S~He's excited about what his partners could do with ours. I understand the disappointment.|
S~I like the confidence in his Pokemon, even if the forecast runs ahead of the evidence.|
S~A magnificent unbeaten partnership, preserved forever by never actually being formed.|
S~The hypothetical team retains a flawless record. Very convenient.|
N~Potential cooperation still needs compatible moves and actual coordination.|
S~An unwalked path can look beautifully smooth from a distance.|
S~He's picturing us succeeding together. That's a nicer refusal response than an insult.|
N~I'd ask what combination made him so excited. There may be a useful idea there.
''')
add('hiker', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_HikerReject', 'The Hiker quietly says he wanted the player beside him in battle.', '''
D~That sounded less like missing a tactic and more like missing the company.|
N~He states his preference plainly without challenging our choice. Considerate.|
S~A decent offer. Decent way to hear a no, too.|
D~I like that he said beside him. It feels different from just needing a useful team.|
S~I'd thank him for the offer. He made it easy to stay friendly.|
S~A gracious little disappointment, leaving both the invitation and our dignity intact.|
S~No prophecy of regret. Just an honest wish that didn't become a plan.|
N~We can appreciate the partnership idea without committing this time.|
S~Some invitations offer a place at someone's side rather than a role to fill.|
S~He didn't make his disappointment into something we had to fix.|
S~I'd be glad to hear how his next challenge goes. He seems easy to talk to.
''')
add('beauty', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_BeautyReject', 'The Beauty laments losing the chance to form the best team together.', '''
S~She already had a little space cleared for the best-team trophy. I admire the preparation.|
N~The proposed superlative is speculative. The disappointment is understandable.|
N~Confidence is fine. We still need the right pair for this attempt.|
D~She seems to have pictured the whole match before we answered.|
S~I'd rather thank her than argue about how good the team might have been.|
S~An imagined triumph has met its first administrative setback: the team doesn't exist.|
S~The best team has remained safely beyond all testing.|
N~We can recognize the possible strengths while choosing another combination.|
N~A shining possibility can be real without becoming the path we take.|
N~She sounds disappointed, but she hasn't made it personal.|
N~I'd ask what made her think we fit so well. It's worth hearing the idea clearly.
''')
add('fisherman', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_FishermanReject', 'The Fisherman believes the teams matched perfectly despite the refusal.', '''
N~A perfect match still needs both people to agree on the fitting.|
N~His compatibility assessment may overlook priorities we haven't explained.|
N~Perfect from one side isn't a settled partnership.|
N~I wonder which part he thought fit so neatly. Maybe we saw different things.|
N~I'd explain our goal instead of insisting his team was wrong.|
N~The pieces apparently matched perfectly, apart from the opinion of one of the pieces.|
N~An excellent fit has encountered the inconvenience of consent.|
N~We should compare the actual team roles before treating the fit as established.|
N~Two shapes may touch neatly without belonging in the same place today.|
N~He sees a match. We may be choosing for something he doesn't know about.|
N~I'd ask what he noticed. A specific explanation could be useful next time.
''')
add('lady', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_LadyReject', 'The Lady confidently predicts regret after being declined.', '''
N~She's certain we'll miss her. That's quite a large goodbye for someone still standing here.|
N~Her certainty concerns an unobserved future. It doesn't resolve the current selection.|
N~We'll own the choice. She doesn't need to choose our feelings afterward.|
N~I don't like having a future feeling assigned to me before I've left.|
N~We can be polite without accepting the guilt that came with the offer.|
N~A formal notice of forthcoming regret. I wonder whether it requires a signature.|
N~The predicted remorse has been delivered with excellent posture.|
N~Our decision should stay grounded in the intended team, not social pressure.|
N~A farewell can leave a thorn where an invitation used to be.|
N~She may be disappointed. Making us feel smaller isn't a gracious way to show it.|
N~I'd let the conversation end instead of trying to prove we won't regret anything.
''')
add('cycling_f', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_CyclingTriathleteFReject', 'The cycling triathlete believes the refused pair would certainly have been tough.', '''
S~She had us racing straight toward victory. We hadn't quite agreed on the starting line.|
N~Combined toughness is plausible, though no performance has established certainty.|
N~Maybe a strong pair. We still have other needs to consider.|
N~She sounds more disappointed in the lost possibility than angry with us.|
S~It's nice that she imagined working together so confidently.|
N~A promising team has been awarded a hypothetical excellent result without entering.|
S~The imagined partnership has impressive speed and no actual footsteps yet.|
N~A tough pair still needs the right coverage for the opponents.|
N~A shared destination can be appealing even when our routes separate.|
N~She isn't questioning her own partners just because we chose differently. Good.|
N~I'd ask which two roles she imagined working together. That's the interesting part.
''')
add('bug_catcher', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_BugCatcherReject', 'The Bug Catcher praises his Pokemon and hopes the refusal does not cause regret.', '''
S~He stands by his little team. The warning has a softer edge than he probably intended.|
N~He remains confident in his partners. That confidence doesn't establish our best option.|
N~His Pokemon can be good without being our choice today.|
S~I like hearing him defend them. I hope he doesn't think we were insulting them.|
N~I'd make clear the refusal wasn't a judgment against the partners he raised.|
S~A proud defense of the team, followed by a cautiously worded invitation to future remorse.|
S~His Pokemon have retained their advocate. Sensible little creatures.|
N~Team fit and individual quality are different questions. We can say so.|
N~A small creature can carry a large share of someone's pride. Handle the answer gently.|
N~He cares how we see his partners. That seems to be the real sore point.|
S~I'd ask what he's proudest of them doing. He sounds ready to tell us.
''')
add('school_m', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_SchoolKidMReject', 'The School Kid hoped to learn beside the player and is disappointed by the refusal.', '''
D~He came looking for a teammate and a lesson. That's two hopes in one little offer.|
N~He values the learning opportunity, not merely the chance of a stronger result.|
S~Good reason to want a partner. A no today doesn't end the learning.|
D~I understand wanting to stand beside someone instead of asking from across the room.|
S~We could share one useful observation without pretending we'd accepted the whole team-up.|
S~An aspiring student has chosen a much more useful goal than simply borrowing a win.|
S~He wanted knowledge that could leave the building with him. Sensible ambition.|
N~A brief explanation of our selection might still give him something practical to learn.|
S~The hand he offered was carrying a question as well as a team.|
S~I'd take that wish seriously. It's braver than pretending he already knows everything.|
S~I'd ask what he wants to learn most. Perhaps a short answer could still help.
''')
add('rich_boy', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_RichBoyReject', 'The Rich Boy reacts with disbelief that the player would refuse him in particular.', '''
N~He seems surprised our no recognized neither his outfit nor his very important sense of himself.|
N~His perceived status isn't sufficient evidence of compatibility. The reaction suggests otherwise to him.|
N~Yes, him. Everyone can hear no.|
N~That reaction makes the room feel less friendly than it needs to.|
N~I'd rather team up with someone who can accept an ordinary disagreement.|
N~An astonishing discovery: the partnership form contains no automatic exception for this particular gentleman.|
N~He has met a decision that failed to recognize his special exemption.|
N~The relevant question remains what his team contributes to the plan.|
N~A polished name can still stop at an ordinary closed door.|
A~The disbelief is more revealing than the threat of regret.|
N~I'd end it politely and speak to someone who sees this as a mutual choice.
''')
add('black_belt', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_BlackBeltReject', 'The Black Belt respectfully hopes for a future opportunity to team up.', '''
S~A no today has stayed a no today. He hasn't stretched it into a whole unhappy future.|
S~He preserves the possibility of another meeting without demanding a commitment.|
S~Respectful answer. I'd remember that.|
S~He made it easy not to feel guilty about choosing.|
S~A good invitation can survive a refusal when nobody tries to turn it into a debt.|
S~A graceful retreat with the next door left conveniently unblocked.|
S~No wounded proclamation. Just another possible day.|
S~Future team needs may differ. Keeping the offer open is practical.|
S~Some roads part without needing to become unfriendly.|
S~He seems comfortable enough in himself to leave the choice with us.|
S~I'd be glad to speak again. That response tells me something useful about working with him.
''')
add('tuber_f', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_TuberFReject', 'The Tuber imagines how strong the refused partnership could have been.', '''
S~She's kept the imaginary team's muscles. At least they don't need carrying to the next room.|
N~She's describing potential strength, rather than a demonstrated outcome.|
N~Could have been strong. That's still different from the team we need.|
N~She sounds sad about missing the chance to find out.|
S~I like her excitement about what the partners might do together.|
S~The unrealized team has received an excellent review from its most enthusiastic supporter.|
S~The hypothetical muscles are flourishing. Very little equipment required.|
N~I'd want to know how the combined moves would actually work.|
N~A possibility can feel almost solid before the answer arrives.|
N~It's a disappointed wish, not a reason we have to reverse ourselves.|
S~I'd ask which partner she was most excited to see beside ours.
''')
add('hex_maniac', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_HexManiacReject', 'The Hex Maniac quietly says she longed to join the player.', '''
D~That is a very small sentence for such a long-sounding hope.|
N~The reply conveys strong interest with little detail. We shouldn't invent more behind it.|
N~She wanted the partnership. We can acknowledge that plainly.|
D~The way she said longed makes the silence afterward feel bigger.|
N~I'd thank her sincerely. There's no need to dress the refusal up as a joke.|
D~An entire declaration reduced to one quiet line. Effective, and rather difficult to answer.|
D~A longing has stepped briefly into view and now has nowhere obvious to sit.|
N~A clear, respectful response is better than vague hints about another chance.|
D~Some wishes arrive already sounding like echoes.|
N~She doesn't need us to treat the intensity as something strange or funny.|
N~I'd listen if she wanted to say more, without assuming she owes us an explanation.
''')
add('breeder_m', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_PkmnBreederMReject', 'The Breeder says he was looking forward to the declined partnership.', '''
D~He had a good afternoon pictured already. I wish the real one could have matched it.|
N~An anticipated collaboration didn't occur. His disappointment remains courteous.|
S~He handled the answer well. Thank him for the offer.|
D~It sounds like he enjoyed imagining the company as much as the battle.|
S~I'd be glad to hear about his partners even if we're not entering together.|
S~A cheerful expectation has met an ordinary disappointment without becoming anyone's indictment.|
S~He has set down the plan without throwing it at us. Appreciated.|
N~We can respect the preparation he put into the offer while choosing otherwise.|
D~An expected meeting can leave an empty place before it ever happens.|
S~He made room for the disappointment without making it ours to repair.|
S~I'd ask what he's trying next. A different partner may still make this a good visit.
''')
add('running_f', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_RunningTriathleteFReject', 'The running triathlete thinks the declined team could have ranked at the top.', '''
S~She had us near the top already. We'll have to admire the view from separate plans.|
N~The predicted ranking is hypothetical. It expresses confidence in the possible combination.|
N~Strong idea. Not every strong idea becomes today's team.|
N~I think she's disappointed we won't get to test the thought together.|
S~A hopeful forecast can stay a nice compliment without becoming a promise.|
S~The partnership has been nominated for first place before completing enrollment.|
S~An excellent hypothetical ranking. The competition has yet to be informed.|
N~We should still judge combinations by the challenge we're actually entering.|
N~Two people can imagine the same summit and choose different paths upward.|
N~She hasn't turned the missed chance into an insult. That keeps it pleasant.|
N~I'd ask what advantage she saw in the pair. It's worth understanding the reasoning.
''')
add('running_m', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_RunningTriathleteMReject', 'The running triathlete expresses a sincere wish to battle as the player partner.', '''
D~He wanted to be on our side of the field. That's a nice offer even when the answer is no.|
N~His interest appears personal and direct, without a claim of guaranteed success.|
S~A sincere offer. We can decline it sincerely, too.|
D~I like that he said he wanted to battle beside us, rather than needed us to win.|
S~I'd thank him for wanting to share the effort. That deserves a real answer.|
S~An invitation to do the work together, rather than outsource the difficult part.|
S~A straightforward wish. Refreshingly free of predictions about our future misery.|
N~He may be a useful future partner when the team requirements align.|
S~Wanting company in a hard place is an honest sort of invitation.|
S~He made the proposal feel mutual. I appreciate that.|
S~I'd be interested to hear how he likes to coordinate with a new partner.
''')
add('battle_girl', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_BattleGirlReject', 'The Battle Girl imagined an ultimate partnership before the player refusal.', '''
S~The ultimate team has discovered that ultimate still needs two signatures.|
N~She sees substantial potential, though the proposed combination remains untested.|
N~Good confidence. We still need more than a title for the pair.|
N~She sounds genuinely excited by the idea she had. I'd acknowledge that.|
S~I'd rather hear the plan than argue about whether ultimate is too big a word.|
S~A splendid team name has arrived before the actual team. A common administrative difficulty.|
S~The ultimate partnership is experiencing a modest staffing problem.|
N~I'd ask which moves or roles she expected to complement each other.|
N~A bright possibility can be worth noticing even when we walk elsewhere.|
N~She isn't making her disappointment ugly. That matters.|
S~I'd ask what made the combination feel so promising to her.
''')
add('cycling_m', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_CyclingTriathleteMReject', 'The cyclist regrets losing what he imagines would be the toughest tag team.', '''
S~He had the toughest team on the island ready in his head. Very efficient assembly.|
N~The superlative describes confidence rather than a result from actual competition.|
N~Potential isn't a guarantee. We can choose a different fit.|
N~He'd probably spent a while imagining that first match.|
S~It's nice to be offered that much belief. We don't have to accept to appreciate it.|
S~A theoretical champion has been forced into retirement before its competitive debut.|
S~Undefeated, untested, and unfortunately unformed. A remarkably clean record.|
N~We should compare coverage instead of selecting the most enthusiastic forecast.|
N~An untraveled route has no difficult bends yet. Imagination smooths them well.|
N~His good opinion can be a compliment without becoming our assignment.|
N~I'd ask which opponents he thought we would handle best together.
''')
add('tuber_m', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_TuberMReject', 'The Tuber defends his Pokemon strength while accepting the declined pairing.', '''
S~His partners still get his vote, even if they didn't get our team slot. That's good.|
N~A refusal doesn't contradict his assessment that his Pokemon are strong. Different questions.|
N~They can be tough. We can still want another combination.|
N~I don't want him thinking we turned away because we disliked his partners.|
S~I'd tell him the team choice wasn't meant to take away his pride in them.|
S~The partnership was declined; the Pokemon's favorable local reviews remain intact.|
S~His little team's reputation has survived one incomplete application.|
N~We can explain the role we're seeking rather than make a broad judgment.|
N~Strength doesn't have to vanish because it wasn't chosen today.|
N~He sounds disappointed without attacking us. I'd meet that calmly.|
S~I'd ask what his partners have done that made him proudest.
''')
add('guitarist', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_GuitaristReject', 'The Guitarist boasts about his Pokemon and predicts regret after being declined.', '''
N~His Pokemon rock hard. His handling of no has a few sharper edges.|
N~The emphatic boast doesn't establish whether the team suits our chosen approach.|
N~Loud confidence isn't the same as the right matchup.|
N~I like hearing pride in his partners. I like the threat much less.|
N~We can leave the boast where it is without answering in the same tone.|
N~A rejected offer has come with a complimentary warning about the foolishness of our taste.|
N~The volume has increased. The evidence remains at its previous setting.|
N~We still need compatible moves, regardless of how strongly the team is advertised.|
N~A proud sound can become harsh when it meets an answer it dislikes.|
N~He may love his team. He doesn't have to make our different choice a personal offense.|
N~I'd rather hear a specific battle story than another prediction about being sorry.
''')
add('gentleman', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_GentlemanReject', 'The Gentleman politely hopes for another chance after the refused partnership.', '''
S~A very tidy goodbye. He even left the next invitation folded neatly beside it.|
S~He accepts the present answer while preserving a future possibility. Considerate.|
S~Good manners. Easy person to speak with again.|
S~I feel relieved when somebody lets a no remain simple.|
S~He's disappointed and still courteous. Both can fit in the same response.|
S~A refusal has been received without a duel, a prophecy, or a lecture. Exemplary.|
S~The conversation has retained its dignity on both sides. A rare luxury.|
N~A future challenge may suit the combination better. No promise is needed now.|
S~A road can part gently enough that another meeting still feels possible.|
S~He didn't use politeness to hide a demand. That's what makes it feel warm.|
S~I'd be happy to hear from him again. The response gives a good impression of teamwork.
''')
add('pokefan_m', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_PokefanMReject', 'The Pokefan interprets refusal as failure to appreciate his top-grade Pokemon.', '''
N~We declined a team slot, and apparently also failed an appreciation exam we hadn't enrolled in.|
N~Recognizing quality doesn't compel a particular pairing. He has conflated the two.|
N~We can appreciate his partners and choose somebody else.|
N~I wish he knew liking a Pokemon didn't have to mean saying yes to everything.|
N~His pride is clear. It doesn't need defending against an insult we didn't make.|
N~A practical selection has been reviewed as though it were a grave failure of taste.|
N~The team has excellent grades. The owner has invented a separate grade for our opinion.|
N~Quality and suitability are related, but not identical. The distinction matters here.|
N~A fine thing doesn't become less fine when it isn't the one carried onward.|
N~He seems to hear rejection of himself through our answer about the team.|
N~I'd explain what we're looking for instead of debating whether his Pokemon deserve praise.
''')
add('expert_m', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_ExpertMReject', 'The Expert pointedly hopes the player refusal is the correct decision.', '''
N~That hope arrived with one eyebrow raised and a small chair reserved for our mistakes.|
N~The decision can be reasonable without becoming provably optimal in advance.|
N~We'll take responsibility for the choice. That's enough.|
N~It sounds like a kind wish until you listen to the pause.|
N~I'd rather make a careful decision than try to satisfy the tone of that remark.|
N~A courteous sentence carrying a rather heavy parcel of implied doubt.|
N~The blessing has a pointed corner. Mind your fingers.|
N~We can review the actual reasoning without treating his disappointment as evidence against it.|
N~A quiet doubt has been laid across the path. We needn't carry it with us.|
N~He wants us to feel the weight of refusing his expertise. I noticed.|
N~I'd answer plainly and move on. We don't need a courtroom for a partner choice.
''')
add('expert_f', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_ExpertFReject', 'The Expert graciously suggests teaming up on a later meeting.', '''
S~Another day is allowed to be another day. I like a calendar without guilt tucked into it.|
S~She leaves future cooperation possible without treating it as guaranteed.|
S~A sensible response. Today's choice doesn't settle every future one.|
S~She made it easy to imagine talking again.|
S~A warm invitation keeps better when it isn't tied into a promise.|
S~A dignified postponement of a possibility, with no attempt to invoice us for disappointment.|
S~The future has been left open rather than aggressively reserved.|
N~Different opponents could make the same partnership more useful later.|
S~An unused path can remain welcoming without asking us to turn back.|
S~She seems confident enough not to make the refusal about her value.|
S~I'd remember her when the next challenge calls for a different sort of team.
''')
add('dragon_tamer', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_DragonTamerReject', 'The Dragon Tamer insists few available partners are tougher than him.', '''
N~He's placed himself very high on the toughness shelf. We may still need a different tool.|
N~Individual strength doesn't fully describe compatibility with our team.|
N~Tough isn't the only requirement for a partner.|
N~I wonder whether he's used to being chosen for strength before anyone asks him anything else.|
N~I'd rather have the right fit than turn the search into a contest of boasts.|
N~A robust personal ranking, apparently prepared without the inconvenience of consulting the other applicants.|
N~The supply of tough partners is allegedly low. The supply of confidence seems adequate.|
N~We need complementary roles, not simply the strongest individual claim.|
N~A strong hand can still hold the wrong end of a shared task.|
N~He wants recognition. We can acknowledge strength without surrendering the choice.|
N~I'd ask how he works with a partner whose plan differs from his own.
''')
add('bird_keeper', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_BirdKeeperReject', 'The Bird Keeper insists his team is strong and calls the refusal a letdown.', '''
N~His confidence is still perched safely. The disappointment has landed beside it.|
N~His team can be capable even when we select a different combination.|
N~Strong team. Different choice. No contradiction there.|
N~He sounds as though he hoped the decision would be easier.|
S~I'd thank him without trying to argue him out of being disappointed.|
N~A capable team has encountered the unfortunate fact that capability doesn't fill every slot.|
N~The strength remains. The proposed partnership has failed to materialize.|
N~We can explain the specific role we need rather than dispute the team's merits.|
N~Something can stand tall and still feel the weight of not being chosen.|
N~I'd separate our selection from any judgment on the partners he cares about.|
S~I'd ask which challenge he plans to enter next. The day isn't over for his team.
''')
add('ninja_boy', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_NinjaBoyReject', 'The Ninja Boy warns the player will regret lacking his tough Pokemon.', '''
N~His partners sound tough. His farewell seems determined to do a little battling of its own.|
N~The claim concerns a future counterfactual we cannot verify from this exchange.|
N~He can trust his team without threatening our decision.|
N~I wish he could hear that a different choice isn't an insult.|
N~I'd leave the warning alone. No need to make disappointment into an argument.|
N~An offer declined has become an ominous preview of all the victories we allegedly won't have.|
N~His Pokemon have acquired a very assertive advertising department.|
N~Our planned pair still needs to be judged by its actual coverage.|
N~A missed possibility can grow teeth in the person still holding it.|
N~He wants the last word to make us doubt ourselves. It doesn't have to work.|
N~I'd rather hear what those Pokemon have actually done than a prediction about our regrets.
''')
add('parasol_lady', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_ParasolLadyReject', 'The Parasol Lady is disappointed because she believes her Pokemon are tremendously strong.', '''
N~She's brought a tremendously strong opinion of the team along with the team itself.|
N~The refusal doesn't disprove her partners' strength. It selects a different fit.|
N~They can be strong and still not match this plan.|
N~She sounds hurt on their behalf as much as her own.|
N~I'd reassure her that we weren't dismissing the care she's put into them.|
N~A formidable team has received an answer that doesn't measure quite what she thinks it measures.|
N~The assessment is enthusiastic. The disappointment is also fully equipped.|
N~We should explain the practical combination we're seeking.|
N~Pride can mistake an unchosen path for a judgment on every step behind it.|
N~She doesn't have to defend their worth just because we chose someone else.|
N~I'd ask what works best about her pair. A specific answer would help us understand.
''')
add('bug_maniac', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_BugManiacReject', 'The Bug Maniac claims the refused team would not have lost.', '''
N~An unbeaten team is easiest to maintain when nobody has agreed to form it yet.|
N~The claim of no possible losses is unsupported. Every actual match would introduce constraints.|
N~No team gets a guarantee. Not even his.|
N~He sounds certain because the imagined matches haven't had a chance to go wrong.|
N~I'd rather hear how the partners help each other than be promised a perfect run.|
N~An immaculate record has been awarded to a partnership spared the trouble of existing.|
N~The imaginary defeats have all been canceled. A convenient format.|
N~A strong combination still needs testing against varied opponents.|
N~An untested hope has never met the weather outside its own room.|
N~He may genuinely believe it. That doesn't make the promise something we can rely on.|
N~I'd ask which difficult matchup he had in mind. That would give the claim some shape.
''')
add('sailor', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_SailorReject', 'The Sailor regrets the chance to overwhelm opponents together.', '''
S~He pictured us storming through the place. Our little paperwork disagreement stopped the weather early.|
N~He imagines a decisive combined performance, but no actual outcome was established.|
N~Could have been a strong run. We chose another plan.|
N~His disappointment sounds cheerful around the edges. I appreciate that.|
S~It's nice being invited to share the effort instead of just being asked to carry it.|
S~A magnificent campaign has been postponed by the absence of a mutually agreed army.|
S~The imaginary opposition has been spared a very confident afternoon.|
N~I'd be interested in the team interactions behind that confidence.|
S~Two people can imagine the same strong wind without setting out together.|
S~He sounds disappointed without trying to diminish anyone. That keeps the invitation warm.|
S~I'd ask him what kind of teammate he enjoys working beside.
''')
add('collector', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_CollectorReject', 'The Collector equates declining his team with failure to appreciate his Pokemon.', '''
N~Admiring the collection apparently comes with a team-registration form attached. Unexpected extra.|
N~Appreciation and selection are distinct. The refusal doesn't establish a lack of regard.|
N~His Pokemon aren't being insulted by a different pairing.|
N~I wish I could show that I liked them without being expected to say yes.|
N~I'd explain what the plan needs instead of debating whether we have good taste.|
N~The collection has excellent reviews, but apparently only one acceptable way to express them.|
N~Admiration has acquired a compulsory participation clause. Inconvenient.|
N~We can value the individual partners while seeking another functional combination.|
N~A beautiful thing needn't be taken into our hands to be seen clearly.|
N~He wants his care to be recognized. A forced partnership isn't the only way to do that.|
N~I'd ask about one partner's story. Appreciation can be a conversation rather than a transaction.
''')
add('ranger_m', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_PkmnRangerMReject', 'The Ranger asks the player to choose his Pokemon at the next opportunity.', '''
N~He's penciled himself onto the next list. I'd leave the pencil handy for revisions.|
N~He requests a future selection, but no future arrangement has been agreed.|
N~Maybe next time. Best not to promise before we know the challenge.|
N~He sounds hopeful. I wouldn't want a polite answer mistaken for an appointment.|
N~We can keep him in mind without giving away a decision we haven't reached.|
N~The present application has been resubmitted to the future with admirable efficiency.|
S~Today's no has been filed under pending rather than permanent.|
N~A later team choice should reflect the requirements at that time.|
S~A later door may open differently. It hasn't opened yet.|
N~I'd keep the answer warm and clear. The two don't have to compete.|
N~I'd ask which other challenges he enjoys. It might help us find a genuine shared plan.
''')
add('ranger_f', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_PkmnRangerFReject', 'The Ranger expresses hope of being chosen next time.', '''
S~That's a little hope left by the door, without anybody standing in the way of it.|
S~She expresses a preference without treating it as a commitment from us.|
S~Fair enough. We can keep the possibility in mind.|
S~She made the refusal feel like part of a conversation rather than the end of one.|
S~I'd rather leave a kind possibility than manufacture a promise.|
S~A future invitation offered without trying to repossess today's decision.|
S~The next chance remains politely available and unbooked.|
N~We can reconsider the pairing if another challenge calls for those roles.|
S~An unchosen path can stay green. No need to close it forever.|
S~She seems disappointed and still generous about the choice.|
S~I'd be glad to talk again when we have a different plan to compare.
''')
add('aroma_lady', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_AromaLadyReject', 'The Aroma Lady warmly hopes a later meeting will produce a partnership.', '''
S~A lovely way to leave another day looking friendly instead of awkward.|
S~Her response preserves goodwill without making future cooperation obligatory.|
S~Kind answer. No reason the next meeting has to be uncomfortable.|
S~I like that she imagines meeting again without needing to secure it now.|
S~A welcoming offer doesn't spoil just because it wasn't taken today.|
S~She has left the future open with considerably more grace than most people manage a doorway.|
S~No ominous forecast. Just another possible pleasant afternoon.|
N~We can assess that future team against whatever challenge we choose then.|
S~Some invitations linger like a pleasant scent instead of a hand on the sleeve.|
S~She makes the possibility sound enjoyable, not like a debt.|
S~I'd remember that warmth when looking for company on a later visit.
''')
add('ruin_maniac', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_RuinManiacReject', 'The Ruin Maniac seems uncertain while defending his Pokemon toughness after refusal.', '''
N~His confidence has picked up a small question mark. Our choice doesn't have to answer it.|
N~A refusal doesn't provide enough evidence to revise his assessment of the Pokemon's strength.|
N~They can still be tough. We just chose differently.|
D~I think he's doubting them because of one answer from us. I hope we can clear that up.|
N~I'd be careful not to let a pairing decision become blame directed at his partners.|
N~A sturdy opinion of the team has developed an unnecessary wobble at the end.|
N~The team's toughness has been placed on trial by a completely different question.|
N~We can explain the required role without judging their overall ability.|
N~A single unopened door doesn't say how strong the hands knocking on it are.|
N~He sounds less angry than unsure. That's a different kind of care to take.|
N~I'd ask what made him proud of them before this conversation. That evidence still exists.
''')
add('cool_m', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_CoolTrainerMReject', 'The Cooltrainer imagined the declined pair as the greatest team.', '''
S~Greatest ever is a rather tall place to put a team before we've exchanged plans.|
N~The superlative is an enthusiastic forecast rather than a tested conclusion.|
N~He liked the idea. That doesn't make it our only good option.|
N~He'd already made the partnership into a happy story in his head.|
S~I'd thank him for thinking so well of us, even if we choose another route.|
S~A potential team has been nominated for an award with exceptionally broad eligibility.|
S~The greatest team ever has unfortunately missed its own formation meeting.|
N~I'd ask what concrete combination he thought would make it work.|
N~An imagined summit can be bright enough to hide every step below it.|
N~I like the compliment. I'd still want the actual plan before sharing the conclusion.|
S~I'd ask which match he most wanted to try together. That would make the idea real.
''')
add('cool_f', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_CoolTrainerFReject', 'The Cooltrainer had imagined a strong partnership and accepts its loss.', '''
S~She had a good thought about us together. It's still a kind thought even unused.|
N~She describes the hoped-for combination without claiming the refusal was unreasonable.|
S~A strong possibility. Not a wasted one just because we said no.|
N~She sounds disappointed in a quiet, ordinary way. I'd answer gently.|
S~Sometimes acknowledging the nice idea is enough. We don't have to argue it away.|
S~A promising proposal has been set aside without anyone declaring the world badly designed.|
S~The hypothetical team has departed with surprisingly good manners.|
N~We can retain the useful idea for a different set of requirements.|
S~A path not taken can still have looked welcoming.|
N~She doesn't make the missed opportunity into a personal attack. I appreciate that.|
S~I'd be curious what first made her think our teams would fit.
''')
add('pokemaniac', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_PokemaniacReject', 'The Pokemaniac praises brutal Pokemon and disclaims responsibility for future regret.', '''
N~We haven't regretted anything yet, and he's already completed the disclaimer. Very prompt.|
N~The warning predicts an unobserved outcome while trying to assign responsibility in advance.|
N~Brutal isn't the only trait we need in a teammate.|
N~That makes the invitation sound less comfortable, honestly.|
N~We can own our decision without borrowing his opinion of how it will end.|
N~A partnership declined has somehow required an advance waiver concerning imaginary remorse.|
N~The future has received a legal notice from a very confident stranger.|
N~We need suitable coordination, not just a forceful description of the team.|
N~Some warnings are only disappointment looking for a larger shadow.|
N~I prefer a partner who wants to work with us rather than predict punishment for refusing.|
N~I'd let him finish without signing up for an argument about a future we haven't lived.
''')
add('kindler', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_KindlerReject', 'The Kindler asks for a promise to team up on the next meeting.', '''
N~Today's no has been offered a little disguise called promise-me-next-time. I recognize the ears.|
N~A future commitment shouldn't be made merely to soften the present refusal.|
N~Don't promise a team before knowing what we'll need.|
F~I'd be tempted to say yes just to make this less awkward. That wouldn't be fair.|
N~A warm answer can still say we don't know what next time will bring.|
N~He has requested a binding sequel to an arrangement that never received a first installment.|
N~The future is being used as a cupboard for an answer that didn't fit today.|
N~We can agree to reconsider without guaranteeing the selection.|
N~An unmade promise is kinder than one left to wilt later.|
N~He deserves an honest possibility instead of a reassuring commitment we don't mean.|
N~I'd say we'll look at the team again if we meet. That's the part we can honestly offer.
''')
add('camper', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_CamperReject', 'The Camper asks hopefully to join the player team at a later meeting.', '''
S~He's saved a hopeful little next time without making the whole room gloomy.|
N~The future request remains an invitation. No actual partnership has been arranged.|
S~Maybe another time. Keep the answer honest.|
S~I like that he's still looking forward instead of turning the moment bitter.|
S~I'd be glad to say hello again, whether or not the teams match then.|
S~A small request has packed its own optimism for the next journey.|
S~The disappointment is already scouting another possible day.|
N~We'll still need to compare the available partners when that opportunity comes.|
S~Hope sometimes travels quite lightly after all.|
S~He asks directly without making the wish sound like something we owe.|
S~I'd ask him to tell us how his next challenge goes. He seems eager to share it.
''')
add('picnicker', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_PicnickerReject', 'The Picnicker gently suggests partnering at another time.', '''
S~Another time has been invited to the conversation very politely.|
S~She accepts the decision and leaves cooperation possible without pressure.|
S~Easy answer. We can part on good terms.|
S~She sounds a little sad, but she hasn't made the sadness difficult to stand beside.|
S~That's a kind way to say the invitation mattered.|
S~A cordial future possibility, presented without demanding a date or a signature.|
S~The door remains open and has stopped trying to follow us. Excellent arrangement.|
N~The same pair could be useful under different requirements later.|
S~Some paths can separate without losing the kindness where they met.|
S~I'd remember how comfortable she made an awkward answer.|
S~I'd be happy to talk again. A good teammate should be easy to be honest with.
''')
add('psychic_m', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_PsychicMReject', 'The Psychic hopes the next meeting will be a chance to team up.', '''
S~For someone called a Psychic, he has wisely left next time as a wish rather than a guarantee.|
N~He's stating a preference about a future meeting, not reporting a certain outcome.|
S~A future offer. We'll consider it if we meet.|
S~I like how plain the wish is. No need to make it sound inevitable.|
S~A kind possibility is enough to leave behind.|
S~A refreshingly modest forecast from someone whose title might encourage a much larger claim.|
S~The future remains unpredicted and politely available.|
N~We can assess the partnership when the actual options are known.|
S~A hoped-for crossing is different from a path already laid.|
S~He leaves us room to have our own answer later. That feels respectful.|
S~I'd ask what sort of challenge he'd most like us to try together.
''')
add('psychic_f', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_PsychicFReject', 'The Psychic hopes for another opportunity to forge an alliance.', '''
S~An alliance is a grand name for it. I suppose even a small team deserves good stationery.|
S~She frames cooperation as a shared future possibility, not an entitlement.|
S~Respectful offer. We can leave that possibility open.|
S~Forge an alliance sounds serious. I wonder how carefully she'd plan the first match.|
S~A good alliance should leave both people comfortable saying what they need.|
S~A diplomatic proposal has been preserved for a later summit, without threatening this one.|
S~The negotiations have paused with all bridges still standing.|
N~We can revisit the practical terms when the challenge and teams are clear.|
S~Some ties are offered as possibilities, with neither end pulled tight.|
S~I like that she wants another chance without making today's answer an offense.|
S~I'd ask how she likes to share decisions with a battle partner.
''')
add('school_f', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_SchoolKidFReject', 'The School Kid politely asks to be chosen at the next opportunity.', '''
S~That's a very polite little reservation request. We haven't opened the next booking book yet.|
N~Her request concerns a future choice we haven't reached. A kind but qualified answer fits.|
S~We can consider her next time. No need to promise more.|
D~She sounds eager enough that I'd be careful not to answer vaguely.|
S~I'd rather give her an honest maybe than a cheerful promise we might break.|
S~An application for a future place, submitted with exceptionally good manners.|
S~Hope has raised its hand and is waiting to be called on.|
N~The next pairing still needs to suit the selected challenge.|
S~A small question can carry a rather determined hope.|
S~Her politeness makes me want to answer with equal care.|
S~I'd ask which partner she'd want to bring if the chance came. She may enjoy explaining.
''')
add('breeder_f', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_PkmnBreederFReject', 'The Breeder insists the player must team up with her next time.', '''
N~She has promoted next time from a possibility to a compulsory appointment. Rather sudden.|
N~Her insistence doesn't establish a future agreement. We should keep that distinction clear.|
N~Next time is still a choice. Don't promise it to end the conversation.|
F~That sounds friendly until I try to work out how to say maybe.|
N~A genuine invitation needs room for a different answer later, too.|
N~The declined proposal has returned wearing the uniform of a future obligation.|
N~The next meeting has been booked on our behalf. We seem to have missed the consultation.|
N~We can agree to review the team without guaranteeing selection.|
N~A warm hand can still hold too tightly. Gently loosen the expectation.|
N~I'd like her confidence better with a little more room for our answer.|
N~I'd explain that we'll decide based on the next challenge. Clear expectations help both sides.
''')
add('pokefan_f', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_PokefanFReject', 'The Pokefan is annoyed and insists her beloved Pokemon are the best.', '''
N~Her darlings are still darlings. Our team choice hasn't revoked the certificate.|
N~Affectionate ranking doesn't establish compatibility. Her annoyance comes from conflating them.|
N~We aren't arguing about whether she loves her Pokemon.|
N~I wish she didn't hear the refusal as a cruel word about them.|
N~I'd make clear we weren't asking her to love her partners any less.|
N~A practical pairing decision has accidentally walked into a fiercely defended family compliment.|
N~The darlings have retained first place in the household rankings. As expected.|
N~We're selecting roles for a challenge, not awarding a universal prize.|
N~A loved creature doesn't lose its place because a stranger chose a different path.|
N~She's protective of them. That doesn't mean our choice was an attack.|
N~I'd ask what she enjoys about battling with them, once the annoyance has passed.
''')
add('swimmer_f', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_SwimmerFReject', 'The Swimmer claims the player owes her a partnership at the next meeting.', '''
N~A team-up debt? I don't remember borrowing a partner from the future.|
N~No agreement occurred, so the refusal hasn't created an obligation for a later meeting.|
N~We don't owe a partnership for saying no.|
N~I don't like the thought that being polite now makes next time less free.|
N~We can consider her again without pretending a debt exists.|
N~A declined invitation has somehow generated an invoice payable at our next encounter.|
N~The future has been charged for a service that was never provided.|
N~We should make clear that future selection depends on the actual team requirements.|
N~A wish can be offered. It shouldn't be tied around someone else's wrist.|
N~She might mean it lightly. I'd still leave the boundary clear.|
N~I'd say we'd be glad to talk again, then let the next choice remain undecided.
''')
add('swimming_m', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_SwimmingTriathleteMReject', 'The triathlete expects to be selected at the next meeting.', '''
N~He's already packed an expectation for next time. We haven't picked the destination yet.|
N~His expectation is not a mutual arrangement. A clear answer prevents later confusion.|
N~Next meeting, we'll make the choice then.|
N~I wish he asked instead of assuming we'd agree later.|
N~I'd rather explain now than let a cheerful misunderstanding grow into another disappointment.|
N~A future partnership has been announced with only half the necessary people consulted.|
N~The calendar has been requisitioned by a man with excellent confidence.|
N~We can consider the pairing when we know which challenge we're attempting.|
N~Tomorrow remains open space, not a chair somebody else can reserve for us.|
N~He sounds confident enough to overlook the missing agreement. I wouldn't leave it unspoken.|
N~I'd answer warmly but plainly. A possible team isn't an appointment yet.
''')
add('swimming_f', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_SwimmingTriathleteFReject', 'The triathlete asks hopefully for another chance at partnership.', '''
S~Another chance to ask is a much easier thing to offer than an entire future victory tour.|
N~Reconsidering later doesn't require committing now. Her request leaves room for that distinction.|
S~We can look again another time. That's honest enough.|
S~I like the question in her voice. She hasn't decided the answer for us.|
S~A second conversation could be welcome even if the final choice stays open.|
S~A modest appeal for another hearing, rather than a demand for a guaranteed favorable verdict.|
S~The next conversation has been invited, not commandeered.|
N~A different team goal may produce a different decision later.|
S~Some doors are asked to open again instead of being pulled off their hinges.|
S~She makes room for both hope and our choice. That's a good balance.|
S~I'd be happy to compare plans again. Her response makes that feel comfortable.
''')
add('swimmer_m', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_SwimmerMReject', 'The Swimmer presses for a promise to team up if they meet again.', '''
N~His next-time request has arrived carrying a small net for our answer. I'd mind the knots.|
N~The leading question seeks a future commitment that hasn't been justified by the current selection.|
N~We can meet again without owing him a yes.|
F~I find that sort of question hard to answer without sounding unkind.|
N~A friendly maybe is better than agreeing just to stop the pressure.|
N~An invitation to tomorrow has become surprisingly insistent about controlling the guest list.|
N~The future partnership has been volunteered twice and agreed to zero times.|
N~We should state that the next pairing will depend on the challenge and available teams.|
N~An offered hand should leave enough room for the other one to stay open.|
N~I'd like him to hear the difference between considering the idea and promising it.|
N~I'd keep the answer clear now so neither of us has to untangle it at the next meeting.
''')
