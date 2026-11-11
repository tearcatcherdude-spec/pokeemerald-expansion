"""Additional terminal human speech found by the postgame source audit."""
ROWS = []
EMOTIONS = dict(N='neutral', S='soft_smile', A='annoyed', F='flustered', D='sad', U='surprised', M='smug', L='laughing')

def add(key, labels, subject, lines):
    replies = [x.strip() for x in lines.strip().split('|')]
    replies = [EMOTIONS[x[0]] + x[1:] for x in replies]
    assert len(replies) == 11, (key, len(replies))
    ROWS.append(dict(key='hpa_'+key, labels=labels.split(), subject=subject, replies=replies))

add('dome_winner', 'BattleFrontier_BattleDomeLobby_Text_LastWinnerWasTough', 'A spectator praises the last tournament winner and recommends examining the results.', '''
S~The winner has left a very impressed person behind. That's one extra kind of record.|
N~The result display gives us more evidence than the praise alone. Worth examining.|
N~Look at the matches. Could be something useful to learn.|
S~I like hearing someone sound pleased for a trainer they watched.|
S~I'd ask which moment made the winner stand out. Strong is a start, not the whole story.|
S~A convincing performance has recruited a local advertising department without paying a single point.|
S~The trophy isn't the only thing still discussing the winner.|
N~We can compare the reported strength with the actual selections and results.|
S~A brief encounter can keep moving through the people who saw it.|
S~Someone else's achievement can make a whole room feel a little more excited.|
S~I'd ask what they noticed before reading the monitor. Two accounts might show different details.
''')
add('frontier_long_dream', 'BattleFrontier_OutsideWest_Text_LongDreamedAboutBattleFrontier', 'An outdoor visitor says the Frontier fulfills a long-held wish for such a place.', '''
S~A long wish has finally found an address. I hope he takes a good slow look around.|
S~The place matches an idea he carried before arriving. I'd be curious what he imagined.|
S~He's here now. Good reason to enjoy the day.|
S~Somewhere imagined for years must feel strange when you can finally walk through it.|
S~I'd let him savor the arrival before asking which challenge comes first.|
S~Reality has completed construction on a place that already existed in his head. A splendid occasion.|
S~A daydream has become large enough to charge admission. Impressive growth.|
N~I'd ask which part meets the old idea and which part surprised him.|
S~A waiting wish changes shape when it finally becomes ground beneath your feet.|
S~I like that he knows how much being here matters to him.|
S~I'd ask what first made him wish for a place like this. That sounds like a good story.
''')
add('tower_eligibility_end', 'BattleFrontier_BattleTowerLobby_Text_NotEnoughValidMonsEnd', 'After explaining an ineligible team, the Tower attendant invites the player to return ready.', '''
N~A little rearranging before the Tower gets its turn at rearranging our confidence.|
N~Entry wasn't approved. This final invitation doesn't identify which eligibility condition failed.|
N~Check the stated requirements, adjust the team, then return.|
N~At least we can sort it out before anybody has to battle.|
N~Better to learn the entry problem at the counter than after getting everyone excited.|
N~The invitation remains open, pending a small but compulsory consultation with the rules.|
N~The Tower has declined the lineup, not our entire existence. Helpful distinction.|
N~We should review species, levels, and held items against the selected format.|
N~A closed gate sometimes needs an adjustment rather than more force.|
N~The clear invitation helps. It makes the correction feel ordinary instead of humiliating.|
N~I'd check each requirement in order instead of guessing which partner caused it.
''')
add('dome_eligibility_end', 'BattleFrontier_BattleDomeLobby_Text_NotEnoughValidMonsEnd', 'The Dome attendant ends an eligibility refusal with an invitation to return prepared.', '''
N~The tournament has asked us to finish the entrance homework before joining the bracket.|
N~The team wasn't admitted. We need the earlier explanation to know the specific cause.|
N~Sort the entry conditions. Then try the desk again.|
N~A quiet correction now is easier than a problem in front of the whole tournament.|
N~I'd take a moment to check the team instead of hurrying to submit it again.|
N~A competitive grand entrance has been temporarily reassigned to practical preparation.|
N~The bracket can wait while we become less administratively surprising.|
N~We can compare the selection with the event requirements one condition at a time.|
N~A pause before the contest can still belong to the work of entering it well.|
N~Being turned back doesn't need to become a personal embarrassment. It's a fixable condition.|
N~I'd ask for clarification if any part of the rule remains unclear before returning.
''')
add('palace_eligibility_end', 'BattleFrontier_BattlePalaceLobby_Text_NotEnoughValidMonsEnd', 'The Palace guide asks the player to return after meeting entry requirements.', '''
N~Before we practice letting go of control, we have to take control of the entry checklist.|
N~The refusal concerns eligibility, not how well the team would perform in the Palace.|
N~Meet the requirements first. The actual challenge can wait.|
N~I'm glad there's time to correct it without a crowd watching.|
N~We should sort the practical details before asking our partners to enter.|
N~The Palace's philosophical test has been delayed by an entirely practical prerequisite.|
N~Our heartfelt intentions appear to require an eligible lineup as well.|
N~We need to distinguish the entry rules from the nature-and-move planning afterward.|
N~An open heart still has to arrive at the proper door.|
N~The guide leaves room to return without making the problem sound like a moral failing.|
N~I'd review what was explained rather than assume this is about the partners' personalities.
''')
add('arena_eligibility_end', 'BattleFrontier_BattleArenaLobby_Text_NotEnoughValidMonsEnd', 'The Arena guide invites the player to return after correcting team eligibility.', '''
N~The three-turn challenge has politely granted us unlimited time to fix the entrance part.|
N~No Arena entry occurred. The specific eligibility problem was described before this farewell.|
N~Fix the lineup before worrying about the order of battle.|
N~It's better to have the pause here than feel rushed once the match starts.|
N~A careful check now gives the partners a calmer start later.|
N~The first judgment concerns whether we brought the correct paperwork in Pokemon form.|
N~The Arena has found a way to ask for preparation without starting the timer.|
N~Check the entry conditions, then review how the valid partners cover one another in sequence.|
N~A moment spent putting things in order can change the path ahead.|
N~I'd treat the refusal as information instead of a verdict on the team.|
N~I'd make sure the correction solves the actual rule rather than simply swapping someone at random.
''')
add('pike_eligibility_end', 'BattleFrontier_BattlePikeLobby_Text_NotEnoughValidMonsEnd', 'The Pike guide ends an entry refusal by asking the player to return ready.', '''
N~Luck hasn't even had a chance to be awkward yet. This part belongs to the checklist.|
N~The current barrier is eligibility. It isn't evidence of unfavorable luck in the challenge.|
N~Check the rules. This is preparation, not fortune.|
N~I like having a problem we can actually check before facing the uncertain rooms.|
N~Let's sort the team carefully. No need to turn an entry condition into a bad omen.|
N~The giant snake has requested a compliant lineup before offering its less predictable hospitality.|
N~Chance has been excused from responsibility for this particular inconvenience.|
N~We should verify the stated conditions rather than retry the unchanged team.|
N~A strange doorway may still have a perfectly ordinary lock.|
N~I'd rather fix the concrete problem than let the atmosphere make it feel mysterious.|
N~I'd go through the earlier explanation once more if any part of it was unclear.
''')
add('pyramid_eligibility_end', 'BattleFrontier_BattlePyramidLobby_Text_NotEnoughValidMonsEnd', 'The Pyramid guide asks for another conversation once the team meets entry requirements.', '''
N~Before the expedition comes the expedition to find the right lineup. Shorter, fortunately.|
N~The proposed team failed an entry condition. No Pyramid exploration has begun.|
N~Correct the requirements before packing a whole climb around this team.|
N~I'd rather know we're ready here than discover a problem somewhere dark.|
N~Taking time at the desk can spare a lot of difficulty afterward.|
N~The great expedition has encountered its first obstacle, located conveniently beside the receptionist.|
N~The summit remains distant. The entry checklist is pleasantly within reach.|
N~We can review the stated species, level, and held-item conditions before resubmitting.|
N~A far path begins with a few nearby things put right.|
N~The invitation is still open. There's no need to rush the correction out of embarrassment.|
N~I'd ask one direct question if the requirement is unclear. Better now than another failed attempt.
''')
add('arena_cancel', 'BattleFrontier_BattleArenaLobby_Text_AwaitAnotherChallenge', 'The Arena attendant courteously ends an entry cancellation.', '''
S~We can leave before the first turn without the referee awarding our hesitation to anyone.|
N~The challenge wasn't entered. The invitation remains available for a later decision.|
S~Canceled cleanly. We'll enter when we're ready.|
S~I'm glad changing our mind doesn't need a defense.|
S~No reason to begin tired or uncertain just because we're standing at the desk.|
S~A courteous postponement of combat, without requiring a compelling speech about our reasons.|
S~The Arena has accepted our decision to remain temporarily unjudged.|
N~We can compare the format with our team's readiness before returning.|
S~A door left for later hasn't become an unfriendly door.|
S~A good welcome leaves room for a quiet exit.|
S~I'd take a look around before deciding whether this is the challenge we want next.
''')
add('pyramid_cancel', 'BattleFrontier_BattlePyramidLobby_Text_AwaitFutureChallenge', 'The Pyramid guide ends an entry cancellation and awaits a future challenge.', '''
S~The Pyramid will wait. It seems unusually qualified for standing in one place patiently.|
N~Entry was canceled before the expedition began. A later attempt remains possible.|
S~Better to start a climb deliberately. We can return.|
S~I feel better knowing we can stop at the threshold without making it dramatic.|
S~A long expedition deserves a rested team and a clear yes.|
S~The ancient-looking monument has graciously adjusted its extremely flexible schedule.|
S~The climb has been postponed. Gravity remains reliably available.|
N~We can use the time to review the Battle Bag rules and team choice.|
S~A summit can wait beyond today without moving any farther away.|
S~There's something reassuring about an invitation that doesn't hurry us toward the dark.|
N~I'd ask what we want from the expedition before committing the time to it.
''')
add('tower_link_mismatch', 'BattleFrontier_BattleTowerLobby_Text_ChooseDifferentMonsMatchLvlMode', 'The Link Multi registration fails because the players selections do not meet shared conditions.', '''
N~Two people have arrived at the same desk with plans that haven't quite shaken hands.|
N~Registration didn't succeed. Matching level modes and nonoverlapping species need verification.|
N~Compare both selections before registering again.|
N~This is easier to settle by talking together than guessing what the other person picked.|
N~I'd sort it out calmly. A mismatched choice isn't a reason to blame a friend.|
N~The partnership has discovered a small disagreement between the two versions of the plan.|
N~The teams have met. The requirements would like them to try the introduction again.|
N~We should coordinate the mode and species choices explicitly before another attempt.|
N~Two roads must agree where they join. A little conversation can move the crossing.|
N~It's a coordination problem. Making someone feel foolish won't solve it faster.|
N~I'd ask both players to say their choices aloud. The mismatch should become clear quickly.
''')
add('partner_initial_search', 'BattleFrontier_BattleTowerMultiPartnerRoom_Text_PleaseFindPartner', 'On entering the Salon, the attendant asks the player to choose a trainer partner.', '''
S~A room full of possible teammates. Somewhere in there is a very interesting first conversation.|
N~The next selection concerns another trainer and their Pokemon, not merely our own lineup.|
N~Look at the teams and ask how they work. Choose carefully.|
N~I'd want a partner I can talk to without feeling silly for asking a question.|
S~Sharing a challenge starts with hearing what the other person brings to it.|
S~A partner search with an unusually direct requirement that we actually speak to someone.|
S~The room contains several prospective relationships and a disturbing amount of eye contact.|
N~We can compare moves and combined roles before accepting an offer.|
S~A shared road begins by looking up and choosing who might walk it beside us.|
N~I'd notice how each person talks about their Pokemon as well as the list of moves.|
S~I'd start with one genuine question. The answer can tell us more than a grand introduction.
''')
add('pike_resume', 'BattleFrontier_BattlePikeThreePathRoom_Text_PleaseEnjoyChallenge', 'After a properly suspended Pike challenge resumes, the attendant sends the player onward.', '''
S~Back to the doors. I hope our decision-making has finished its own little rest, too.|
N~The suspended challenge has resumed. We should recheck the team before relying on memory.|
N~We're continuing. Take stock before choosing the next path.|
N~I'd like a moment to remember where everyone's condition stood.|
N~A fresh look at the team is worthwhile after any pause.|
S~The unfinished adventure has recovered its place in the schedule. Back to our uncertain corridors.|
S~The doors have waited without becoming less secretive. Consistent of them.|
N~We should review the current room and resources rather than assume the previous plan still fits.|
S~A paused path can be picked up gently instead of rushed back into.|
N~Returning doesn't mean we have to pretend we remember every detail immediately.|
N~I'd look around carefully before taking the first step. Familiar rooms can still hold uncertainty.
''')
add('tower_disqualified', 'BattleFrontier_BattleTowerLobby_Text_DidntSaveBeforeQuitting', 'The Tower attendant disqualifies an improperly interrupted challenge.', '''
D~The streak has ended at the desk instead of on the field. That's a frustrating finish.|
N~The prior challenge is disqualified. A fresh attempt must use the proper suspension procedure.|
N~Learn the stopping rule before another run. No point repeating this.|
D~I wish the work hadn't ended this way. We can still keep what we learned.|
N~Let's ask how to pause correctly before committing to another long round.|
N~A battle record has been defeated by an unfinished departure. An irritating opponent.|
N~The Tower is strict about exits as well as victories.|
N~We should confirm the valid interruption steps rather than rely on an assumption.|
D~Effort can leave a mark even when the official tally no longer carries it.|
N~The rule is clear now. I'd focus on preventing another loss like this.|
D~I'd give everyone a little time before deciding whether to start again immediately.
''')
add('dome_disqualified', 'BattleFrontier_BattleDomeLobby_Text_DidntSaveBeforeQuitting', 'The Dome guide invalidates the challenge after an improper interruption.', '''
D~The bracket has crossed us out without asking an opponent to do it. Rather unceremonious.|
N~The tournament attempt was invalidated by the interruption, rather than a battle result.|
N~The attempt is over. Check the proper pause method before trying again.|
D~It's hard when the match you remember and the official result don't line up.|
N~I'd settle down before restarting. Frustration doesn't make the next selection clearer.|
N~Our tournament has received a procedural ending entirely lacking in dramatic satisfaction.|
N~An anticlimax with a receptionist. Efficient and unpleasant.|
N~We need to understand how the challenge preserves its progress when interrupted.|
D~A line through the record doesn't reach every memory of the work.|
N~I'd rather learn the process once than let embarrassment push us into another hurried attempt.|
N~I'd ask the guide to explain the exact stopping point we're meant to use.
''')
add('factory_disqualified', 'BattleFrontier_BattleFactoryLobby_Text_DidntSaveBeforeQuitting', 'The Factory attendant disqualifies an improperly stopped rental challenge.', '''
D~All those introductions, and the challenge has ended before a proper goodbye.|
N~The rental challenge was invalidated by the interruption. Its earlier progress doesn't continue.|
N~Fresh attempt next time. Learn the approved stopping process first.|
D~I'd probably remember the borrowed partners even though the record won't keep going.|
N~The lost progress hurts. We don't need to rush into choosing another team while upset.|
N~A temporary team has been given an unexpectedly permanent end to its appointment.|
N~The Factory has rejected the paperwork after the Pokemon did the difficult part.|
N~We can preserve our observations even though this particular run is no longer valid.|
D~A short partnership can leave something behind when the official path closes.|
N~I'd keep the useful lessons separate from the frustration with the procedure.|
N~I'd ask where the proper suspension step belongs before choosing another rental roster.
''')
add('palace_disqualified', 'BattleFrontier_BattlePalaceLobby_Text_FailedToSaveBeforeEndingChallenge', 'The Palace guide disqualifies a challenge after an improper interruption.', '''
D~The Palace asked us to let the Pokemon decide things. Unfortunately, the exit had its own rules.|
N~The challenge's validity depends on proper suspension as well as its battle conditions.|
N~It's disqualified. Next time, check how to stop before starting.|
D~That sigh makes the result feel very final. I'd take a moment before answering.|
N~We can recover from an awkward ending without turning the next visit into a punishment.|
N~A test of the heart has encountered a very firm administrative footnote.|
N~The bonds may be intact. The official streak has proved less resilient.|
N~We should verify the interruption procedure separately from the Palace's battle rules.|
D~A broken tally doesn't sever the living ties beside us.|
N~The guide sounds disappointed too. That doesn't make the correction less clear.|
N~I'd make sure we understand the process before letting the frustration choose another immediate run.
''')
add('arena_disqualified', 'BattleFrontier_BattleArenaLobby_Text_DidntSaveBeforeShuttingDown', 'The Arena guide disqualifies the interrupted challenge and allows a fresh start.', '''
D~No referee needed for this ending. I would have preferred losing to somebody with a Pokemon.|
N~The challenge has been invalidated, but the guide explicitly permits a new attempt.|
N~Fresh start is available. First, learn the proper way to pause.|
D~I like hearing that we can begin again, even though it doesn't erase the disappointment.|
N~A fresh attempt can wait until we're calm and ready for it.|
N~A strict procedural defeat, accompanied by a kindly offered new application form.|
N~The Arena has judged the departure and left the rematch available.|
N~We can retain the team-order lessons while correcting the interruption process.|
S~An ended path isn't the same as a barred doorway.|
N~The invitation softens the news. It still deserves a careful explanation before another entry.|
N~I'd ask exactly how to suspend the challenge so the next attempt doesn't end this way.
''')
add('pike_disqualified', 'BattleFrontier_BattlePikeLobby_Text_FailedToSaveBeforeQuitting', 'The Pike guide invalidates a challenge because it was not properly suspended.', '''
D~Luck didn't choose this door. The interruption rule did. Somehow that's more annoying.|
N~This result comes from an invalid interruption, not the random room sequence.|
N~No point blaming luck. Learn the pause procedure and start fresh.|
D~I understand wanting to call it unfair when the work disappears so abruptly.|
N~Let's find the correct way to stop before taking another chance on the rooms.|
N~In a building devoted to uncertainty, the departure rule has remained remarkably certain.|
N~The unpredictable challenge has enforced one completely predictable condition.|
N~We should separate the procedural failure from the choices made during the run.|
D~Chance isn't holding this thread. We can learn where our hands should have been.|
N~A clear cause is useful even when the result feels bad.|
N~I'd ask which attendant handles a proper pause before entering again.
''')
add('pyramid_disqualified', 'BattleFrontier_BattlePyramidLobby_Text_DidntSaveBeforeQuittingTakeBag', 'The Pyramid guide invalidates the interrupted expedition and returns the ordinary bag.', '''
D~The climb is over, and our own bag has come back with rather unwelcome news.|
N~The expedition is disqualified and the held bag returned. No successful ascent is implied.|
N~Bag returned. Run ended. Check the stopping rules before another climb.|
D~Getting familiar things back is comforting, even when the reason is disappointing.|
N~I'd take stock quietly before deciding what to do next. We've had enough surprises for a moment.|
N~The expedition concludes with the return of our belongings and an exceptionally firm correction.|
N~The luggage is home. The official progress has remained elsewhere.|
N~We need the approved suspension process before attempting another extended expedition.|
D~Returning to ordinary things can steady you after an unfinished path.|
N~It's useful that the guide states what happened to the bag as well as the challenge.|
N~I'd check everything and ask how to preserve the next expedition properly when stopping.
''')
