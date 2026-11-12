"""Reviewed posted advice and safety notices in Kanto and Sevii."""
ROWS=[]
E=dict(N='neutral',S='soft_smile',A='annoyed',F='flustered',D='sad',U='surprised',M='smug',L='laughing')
def add(key,labels,subject,lines):
    replies=[]
    for s in lines.strip().split('|'):
        s=s.strip()
        if len(s)>1 and s[1]=='~'and s[0]in E:s=E[s[0]]+s[1:]
        replies.append(s)
    assert len(replies)==11,(key,len(replies))
    ROWS.append(dict(key='kanto_notice_'+key,labels=labels.split(),subject=subject,replies=replies))
add('guard_spec','CeladonCity_Text_GuardSpecProtectsFromStatus',
    "A Trainer Tips sign recommends Guard Spec and advertises the Department Store.",'''
N~A helpful battle tip has brought a tiny shop advertisement along as its travelling companion.|
N~Preventing a problem can be useful. The purchase still needs to fit our actual plan.|
N~Read the item properly before relying on it.|
N~I like the useful part better than the assumption that reading means we should buy something.|
N~A little preparation can help, provided we do not fill the Bag with every advertised answer.|
S~The educational notice has remembered which merchant paid for its closing line.|
N~A piece of advice can be useful and still have something to sell.|
N~Match the tool to the problem rather than collect tools without a plan.|
N~A shield is most useful when we know which small doors it can close.|
N~Practical advice benefits from a little thought about the sales pitch attached.|
N~I wonder which situation first made someone wish they had packed that item.
''')
add('accuracy_crit','CeladonCity_Text_ExplainXAccuracyDireHit',
    "A posted tip advertises items intended to improve accuracy or critical-hit chances.",'''
S~Two little promises to make a battle less wobbly, both conveniently sold just over there.|
N~Improving a probability and guaranteeing an outcome are different claims. Useful to keep them distinct.|
N~Helpful options. They do not replace paying attention to the fight.|
N~I would rather plan calmly than reach for something because one missed move made us panic.|
N~Choose what helps the team instead of buying every promise on a sign.|
S~The store has offered the traveller two kinds of dramatic improvement in portable form.|
N~Chance has been invited to behave itself, not forced to sign a contract.|
N~We can compare the effect with the situation before deciding it earns a place in the Bag.|
N~A little help can steady the hand without writing the ending.|
N~The distinction between more likely and certain deserves larger lettering.|
S~I wonder how many shoppers remember the useful explanation after the colourful promise.
''')
add('held_items','CeruleanCity_Text_TrainerTipsHeldItems',
    "A Trainer Tips sign explains that Pokemon can carry useful items.",'''
S~A little equipment for the companion instead of another thing for us to drop in the Bag.|
S~A held item can support a particular role when its effect suits the Pokemon's actual needs.|
N~Choose something useful and check who is carrying what.|
S~It is a small way of preparing with the team rather than only for them.|
N~The right thing within reach is often more useful than a lot of things somewhere else.|
S~The supporting cast has been granted its own practical wardrobe of equipment.|
S~A small carried thing can quietly change the shape of a difficult moment.|
S~Matching equipment to the job is more effective than assigning it at random.|
S~A little object can become part of how a companion meets the road.|
N~Useful is a better standard than giving everyone something merely to fill a place.|
S~I wonder which item each trainer first learns to check without needing a reminder.
''')
add('fossil_theft_notice','PewterCity_Text_CallPoliceIfInfoOnThieves',
    "A public notice asks for information about fossil thefts at Mt Moon.",'''
N~Those fossils should be things people learn from, not things everyone has to worry about losing.|
N~A report of theft deserves useful observations rather than speculation presented as evidence.|
N~If we learn something definite, pass it to the people investigating.|
N~It is sad to see something old and remarkable become the subject of an ordinary ugly theft.|
N~Keeping a place's discoveries safe matters beyond the people who first found them.|
N~An ancient history has been interrupted by a depressingly modern sort of greed.|
N~The mountain has survived ages and still needs protection from somebody wanting a quick profit.|
N~Specific facts will help more than turning every unfamiliar visitor into a suspect.|
N~Old things have already endured enough without becoming prizes for careless hands.|
N~Concern should make us attentive without making us reckless.|
N~I wonder what details a hurried traveller might have noticed without realizing they mattered.
''')
add('battle_experience','PewterCity_Text_TrainerTipsEarningEXP',
    "A posted tip describes learning through participation in battle.",'''
S~Even a short turn can leave somebody knowing a little more than before.|
N~Experience is useful when the task gives the Pokemon a reasonable chance to learn safely.|
N~Give the team practice they can handle. Nobody needs to be thrown in unprepared.|
S~It is nice to think the brief attempts count, too.|
N~A small chance to try something can matter without turning every lesson into an ordeal.|
S~The supporting appearance has been granted some of the educational value of the main role.|
S~A little time in the difficult part can still be time that teaches something.|
N~We should judge readiness rather than treat participation itself as a complete plan.|
S~A short step on an unfamiliar path can leave a lasting shape in the memory.|
S~Improvement is easier to enjoy when every small beginning is allowed to matter.|
S~I wonder which tiny first attempt each team member would choose to remember.
''')
add('bag_order','Route13_Text_SelectToSwitchItems',
    "A sign explains how to rearrange items in the Bag.",'''
S~The Bag has a tidying option. I may need a separate sign explaining how to remember to use it.|
S~A consistent arrangement can reduce the time spent searching when an item is needed.|
N~Keep important supplies easy to find. Simple habit, useful later.|
S~A little order can make an awkward moment feel much less hurried.|
N~Put the things we use often where our hands expect them to be.|
S~A practical note for preventing the dramatic search through an overambitious packing list.|
S~A tidy bag is a small mercy for the future tired version of ourselves.|
S~Clear ordering is useful precisely when there is less time to think about it.|
S~An ordinary arrangement can become a quiet kind of reassurance.|
N~Knowing where something is matters nearly as much as remembering to bring it.|
S~I wonder which object always finds its way to the wrong end of the Bag despite our best plans.
''')
add('post_left','Route13_Text_LookToLeftOfThatPost',
    "A sign playfully tells readers to look left of a nearby post.",'''
S~A sign has stopped being a sign and started pointing excitedly like a person with a small secret.|
N~A clear local direction is useful, provided we actually check which post it refers to.|
N~Take a look without stomping through everything around it.|
S~It is a friendly little way to make someone slow down and notice the roadside.|
S~A small nudge of curiosity can turn an ordinary walk into a better afternoon.|
S~The signwriter has supplied stage directions and an unusually enthusiastic cue.|
S~A public notice has briefly become a conspirator.|
N~Specific landmarks make a clue much more useful than vague encouragement.|
S~A familiar post has acquired a little space worth looking toward.|
S~I like the unembarrassed eagerness of somebody wanting a stranger to notice something.|
S~I wonder how many people look exactly where they were told and smile at being guided there.
''')
add('cycling_brake','Route17_Text_PressBToStayInPlace',
    "A Cycling Road sign explains holding position on a slope.",'''
N~Excellent advice for discovering that the hill has its own travel plans.|
N~Controlling movement on a slope is more useful than trying to correct excessive speed afterward.|
N~Know how to stop before taking the slope fast.|
N~I like a route that explains how to pause instead of assuming everyone wants to hurry.|
N~A steady stop is a good chance to check where the next stretch leads.|
N~The downhill adventure has wisely included a note about declining the downhill part.|
N~Gravity is a very persistent travelling companion when nobody tells it to wait.|
N~A reliable brake gives the rider more choice about the pace.|
N~A slope is less demanding when we know how to ask it for a still moment.|
N~Control is much more attractive than hoping to look confident while gathering speed.|
N~I wonder how many riders learn to appreciate that little instruction after the first steep stretch.
''')
add('individual_growth','Route17_Text_SameSpeciesGrowDifferentRates',
    "A tip emphasizes individual differences between Pokemon of the same species and level.",'''
S~Matching names do not make matching little lives. That seems worth putting on a sign.|
S~A broad category cannot capture every difference between individuals. Observation remains important.|
N~Learn the companion in front of us instead of expecting it to match a chart perfectly.|
S~It is comforting to know that being different is part of being ordinary, too.|
S~Two things can share a name and still need a different amount of time and attention.|
S~The cast has declined to be manufactured from a single reusable character sheet.|
S~A tidy label has once again failed to contain an entire living thing.|
S~Adjust the plan to actual results instead of forcing the results to fit the plan.|
S~Two seeds of the same kind need not reach toward the light in exactly the same way.|
N~Comparison is useful until it makes us stop noticing the individual.|
S~I wonder which small difference a caring trainer learns to recognize before anyone else does.
''')
add('safari_remaining','SafariZone_Center_Text_PressStartToCheckTime',
    "A Safari Zone tip explains how to check the remaining allowance.",'''
N~A little reminder to ask the clock how the adventure is actually going.|
N~Checking the remaining allowance supports planning instead of relying on a vague sense of time.|
N~Know what we have left before choosing a longer route.|
N~It feels calmer to check once than keep worrying without knowing.|
N~Leave enough of the visit for getting back comfortably.|
N~The excursion has included a discreet invitation to consult its less romantic accounting.|
N~An honest number is sometimes kinder than an optimistic guess.|
N~A visible limit makes it easier to compare the route with the remaining opportunity.|
N~A little measure can keep the day from slipping away entirely unnoticed.|
N~Planning is more pleasant than being surprised by the end.|
N~I wonder how many visitors only remember that instruction when they wish they had read it earlier.
''')
add('safari_pause','SafariZone_East_Text_TimeDeclinesOnlyWhileYouWalk',
    "A Safari sign explains that the visit's allowance is spent by walking.",'''
S~Thinking has been given a rather generous discount compared with wandering in circles.|
N~The notice makes route choice important. A considered pause can prevent unnecessary travel.|
N~Decide where we are going before spending steps getting there.|
S~I like an invitation to stop and look carefully rather than hurry past everything.|
N~A brief plan can save enough wandering to make the visit more enjoyable.|
S~The expedition has discovered that contemplation is its most economical mode of travel.|
S~A rare institution that appears willing to subsidize standing thoughtfully.|
N~Check the map and make each stretch purposeful instead of repeatedly backtracking.|
S~A still moment can hold more of the place than a hurried lap around it.|
S~There is something pleasant about being allowed to pause without losing the afternoon to haste.|
S~I wonder what visitors notice when they finally stop counting the path and actually look around.
''')
add('safari_house_search','SafariZone_North_Text_SecretHouseStillAhead SafariZone_West_Text_SearchForSecretHouse',
    "Safari Zone notices encourage searching for the Secret House.",'''
L~A secret house with an advertising campaign. I admire the confidence of that secret.|
N~The notices establish an intended destination, but we still need to navigate the actual route.|
N~Keep track of the route as we search. No need to wander blindly.|
S~A little destination can make a large unfamiliar area feel easier to approach.|
N~A search is more pleasant when we leave ourselves a sensible way back.|
S~The hidden location has secured unusually enthusiastic publicity.|
S~A secret can remain elusive while being astonishingly bad at staying unmentioned.|
N~Use the landmarks instead of treating the whole area as equally likely.|
S~A little house has become a question at the far edge of the path.|
S~The promise gives the walk some direction without taking away all the curiosity.|
S~I wonder how many people remember the search more fondly than arriving at the house.
''')
add('safari_grass','SafariZone_North_Text_ZigzagThroughTallGrass',
    "A Safari tip recommends exploring tall grass to find hidden Pokemon.",'''
S~The grass contains more neighbours than it puts on the path's welcome committee.|
N~Searching suitable habitat is more informative than expecting every Pokemon to appear in the open.|
N~Watch our footing and do not rush through the whole patch.|
S~It is nice to remember that the quiet grass can be full of lives we have not seen.|
N~A careful look is better than trampling everything in a hurry to find something.|
S~The notice recommends meeting the supporting cast where they actually live.|
S~An apparently empty patch has refused to be summarized by the first glance.|
N~A varied search path covers more ground than repeatedly checking the same edge.|
S~The green has kept little spaces that our eyes cannot see from the road.|
N~Curiosity should still leave the habitat in decent condition behind it.|
S~I wonder which rustle belongs to the Pokemon and which is simply the grass making its own noise.
''')
add('safari_hm_prize','SafariZone_North_Text_WinFreeHMFindSecretHouse',
    "A notice offers an HM for finding the Safari Secret House.",'''
S~A walk with a useful prize waiting at the end. The house has a very effective invitation.|
N~The reward is conditional on reaching the destination. Reading the notice does not award it.|
N~A useful goal, if we are ready for the route.|
S~I like when a challenge rewards looking around instead of only winning a battle.|
N~The promised gift is worth planning for rather than rushing blindly toward.|
S~The hidden house has added a practical epilogue to its adventure pitch.|
S~A prize can make an old-fashioned walk suddenly acquire much more plot.|
N~We should navigate carefully and verify the actual condition on arrival.|
S~A little destination has hung a promise where the path can see it.|
N~The reward should add to enjoying the visit, not turn it into a frantic obligation.|
S~I wonder whether people arrive more pleased with the prize or with finally finding the way.
''')
add('warden_teeth_notice','SafariZone_West_Text_PleaseFindWardensLostTeeth',
    "A notice requests the Warden's lost Gold Teeth and offers a reward.",'''
S~A very personal rescue mission has been printed in remarkably official lettering.|
N~The notice identifies a specific lost object and an owner to return it to. Useful information.|
N~If we find them, get them back to him. He clearly needs them.|
N~It must have taken a little courage to make that problem so public.|
N~Helping him get through an ordinary day seems a good enough reason to look.|
S~The administrative notice has unexpectedly become an intimate tale of missing dental equipment.|
N~A small public embarrassment may be hiding a very inconvenient private day.|
N~A clear description and contact make a lost-item notice much easier to act on.|
N~A person has put a small vulnerable part of the day into strangers' care.|
N~The reward is less important than not turning his difficulty into a joke at his expense.|
N~I wonder how relieved he will be when somebody walks in with what he thought was lost.
''')
add('great_ball_tip','SaffronCity_Text_GreatBallImprovedCatchRate',
    "A sign recommends Great Balls for difficult wild Pokemon captures.",'''
N~The helpful sign would like us to know there is a fancier answer to a very persistent escape artist.|
N~A better capture chance is useful, though it remains a probability rather than a promise.|
N~Prepare before the encounter. Do not count on any single throw.|
N~It is nice to have options when repeated attempts are becoming frustrating.|
N~We can choose supplies that suit the trip without buying only the most expensive answer.|
S~The shop has offered a more distinguished container for our uncertain hopes.|
N~A little improvement in chance need not become a certainty in the retelling.|
N~Compare the situation and the cost instead of assuming one item is always the right choice.|
N~A better net still leaves the world some say in what stays.|
N~A clear benefit is useful; an advertising promise deserves its own careful look.|
N~I wonder which encounter makes people finally appreciate the difference between possible and likely.
''')
add('full_heal_tip','SaffronCity_Text_FullHealCuresStatus',
    "A posted tip recommends Full Heal for several kinds of status trouble.",'''
S~One bottle trying to solve several different bad afternoons. A useful sort of ambition.|
N~The convenience is covering several status conditions with one item, not replacing every other kind of care.|
N~Useful supply. Still check what the team actually needs.|
N~It is reassuring to have an answer ready before a companion is struggling.|
N~A simpler supply list can help, provided we remember what the item does not cover.|
S~A versatile supporting player, advertised with commendable confidence.|
N~Convenience is valuable when it prevents confusion rather than replacing attention.|
N~A flexible tool can reduce packing complexity, but understanding its limits still matters.|
N~One small preparation can soften several different ways a day turns difficult.|
N~Practical convenience is worth considering alongside the price.|
N~I wonder which item experienced travellers learn to check before they leave town.
''')
add('current_warning','SeafoamIslands_B4F_Text_DangerFastCurrent TwoIsland_Text_DangerFastCurrent',
    "A warning marks water with a dangerous fast current.",'''
N~The water has supplied a moving argument, and somebody was kind enough to add a written one.|
N~A fast current can exceed the control a swimmer or rider expects to have. The warning deserves respect.|
N~Do not test that current for fun. Find the safe route.|
N~I am glad someone thought to warn the next person before the danger became obvious too late.|
N~Getting through safely is worth more than saving a few steps.|
N~The scenery has posted a rather firm objection to becoming our shortcut.|
N~Water does not need to look angry to be stronger than us.|
N~Observe the flow and follow the warning instead of treating ability as immunity.|
N~A bright surface can carry a hard pull beneath it.|
N~Confidence is less useful here than accepting good information.|
N~I wonder how much trouble that plain little sign has prevented without anyone ever knowing.
''')
add('snorlax_detour_notice','VermilionCity_Text_SnorlaxBlockingRoute12',
    "A police notice warns of a possible sleeping-Pokemon blockage and suggests a detour through Rock Tunnel.",'''
N~The police have found a very official way to say that a nap may be controlling the traffic.|
N~The notice offers an alternative route for a possible obstruction, not confirmation of the route's current state.|
N~Check the situation before committing to the longer way. Prepare properly if we take the tunnel.|
N~A detour feels less frustrating when somebody explains why it might be needed.|
N~The suggested route deserves its own supply check, not just a quick change of direction.|
S~A sleeping obstacle has become large enough to acquire a police-authored travel advisory.|
N~An entire journey can be revised by someone else's very committed nap.|
N~A useful alternate route still needs evaluating for our team's readiness.|
N~A small sheet of words is helping the road find a way around a great sleeping shape.|
N~It is considerate to offer another option instead of merely announcing a problem.|
N~I wonder how many travellers changed their whole afternoon after stopping to read that notice.
''')
add('forest_tired_team','ViridianForest_Text_AvoidGrassyAreasWhenWeak',
    "A forest tip recommends avoiding encounter areas when the team is tired.",'''
N~The grass is still full of challenges even when our companions would rather be full of rest.|
N~Reducing avoidable encounters is sensible when the team's current condition is poor.|
N~Get the team rested before looking for another battle.|
N~A quiet way back can be a kindness after a difficult stretch.|
N~Being prepared includes knowing when the next useful stop is a place to recover.|
N~The adventure has recommended an intermission instead of another unnecessary confrontation.|
N~A tired team should not have to argue with every rustling patch on the way home.|
N~Choose a route that fits the team's condition rather than the route that fits our impatience.|
N~The path can ask less of us if we stop asking too much of those beside us.|
N~Good judgment is more attractive than insisting we always have another fight in us.|
N~I wonder which trainer first learned that a careful retreat can be the kindest decision of the day.
''')
add('oak_pc_tip','ViridianForest_Text_ContactOakViaPCToRatePokedex',
    "A posted tip explains that Oak can evaluate the Pokedex through a PC.",'''
S~A progress report without making the notebook walk all the way back to the professor. Handy.|
S~Remote evaluation makes an ongoing research task easier to review between field visits.|
N~We can check the record when we reach a suitable place to stop.|
S~It is nice that somebody remains interested in what we are noticing along the way.|
S~A little outside perspective can help us plan the next part of the trip.|
S~The travelling researcher can submit the current chapter without delivering the author in person.|
S~A small convenience for a task that involves rather a lot of walking.|
S~Regular feedback can help turn a large collection goal into manageable next steps.|
S~A distant familiar voice can still put a little light on the path ahead.|
N~A useful assessment should help the journey, not make every quiet day feel graded.|
S~I wonder which discovery we would be most eager to tell him about instead of merely count.
''')
add('owned_pokemon_tip','ViridianForest_Text_CantCatchOwnedMons',
    "A forest notice explains that another trainer's Pokemon cannot be caught.",'''
N~Meeting a wonderful Pokemon does not make its entire existing life available for us to pack up.|
N~The notice distinguishes a wild encounter from somebody else's established partnership.|
N~Respect the companion and the person it came with.|
N~It would feel awful to have a stranger treat a friend as something to collect.|
N~Admiring someone else's team is not the same as being entitled to it.|
N~An appealing character does not become ours simply because we have decided we like the role.|
N~Wanting something is a poor argument for erasing everyone already attached to it.|
N~A clear boundary saves us from treating every encounter as the same kind of opportunity.|
N~A life already walking beside someone is not an empty place in our own story.|
N~A little admiration can remain perfectly pleasant without becoming possessive.|
N~I would rather hear how a trainer and Pokemon met than imagine taking the place between them.
''')
add('capture_preparation','ViridianForest_Text_WeakenMonsBeforeCapture',
    "A forest tip recommends weakening wild Pokemon before attempting capture.",'''
N~A practical tip, with the important bit being not to let excitement run the whole encounter.|
N~Improving capture conditions can help, though the trainer still needs control over the encounter.|
N~Plan carefully. Do not let a promising encounter become a careless scramble.|
N~I hope people remember there is a living creature in the situation, not only an empty Ball.|
N~A calm approach makes it easier to notice when to stop.|
N~The would-be collector has been advised to prepare the scene rather than improvise every cue.|
N~Enthusiasm is not famous for measuring its own strength accurately.|
N~Choose an approach that offers control rather than relying on a forceful guess.|
N~A new meeting deserves more care than the hurry to make it ours.|
N~Getting what we wanted should not be the only measure of whether we handled the encounter well.|
N~I wonder which small choice experienced trainers learn to make before the excitement takes over.
''')
add('antidote_notice','ViridianForest_Text_UseAntidoteForPoison',
    "A notice recommends packing Antidotes for poisoning.",'''
N~A small practical item is much nicer to remember before the forest makes it relevant.|
N~Matching a remedy to the specific status condition avoids relying on an unsuitable item.|
N~Check our supplies before heading farther in.|
N~It is reassuring to know there is something ready when a companion needs help.|
N~A modest bit of preparation can make a rough stretch much less unpleasant.|
N~An unglamorous supporting item has received a thoroughly deserved piece of publicity.|
N~A small bottle may be the least exciting and most welcome thing in a bag.|
N~A clear label helps when the situation is already distracting.|
N~Some kinds of care begin quietly before anybody is hurting.|
N~Useful preparation need not be impressive to be worth doing.|
N~I wonder which supply every experienced forest traveller checks twice before leaving the shop.
''')
add('safari_resthouse','SafariZone_Center_Text_RestHouse SafariZone_East_Text_RestHouse SafariZone_North_Text_RestHouse SafariZone_West_Text_RestHouse',
    "A Safari Zone sign identifies a rest house.",'''
S~An excellent destination for feet that have developed a persuasive argument against further enthusiasm.|
S~A designated rest point makes the visit easier to pace sensibly.|
N~A good place to pause and check the team.|
S~I like seeing a route make room for being tired.|
S~A proper pause can make the rest of the visit feel new again.|
S~The excursion has thoughtfully provided a setting for its intermission.|
S~A small shelter can become the most attractive exhibit in the park.|
N~We can use the stop to consider the next route instead of wandering without a plan.|
S~A place to be still belongs on a map of a good journey.|
S~Rest looks much better when nobody has to pretend it was not needed.|
S~I wonder how many visitors arrive only wanting a seat and leave ready to look around again.
''')
