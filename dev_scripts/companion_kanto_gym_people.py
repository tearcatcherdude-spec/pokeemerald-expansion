"""Kanto Gym terminal conversations with eleven independently authored voices."""
ROWS = []
EMOTIONS = dict(N='neutral', S='soft_smile', A='annoyed', F='flustered', D='sad',
                U='surprised', M='smug', L='laughing')

def add(key, labels, subject, lines):
    replies = []
    for line in lines.strip().split('|'):
        line = line.strip()
        if len(line) > 1 and line[1] == '~' and line[0] in EMOTIONS:
            line = EMOTIONS[line[0]] + line[1:]
        replies.append(line)
    assert len(replies) == 11, (key, len(replies))
    ROWS.append(dict(key=key, labels=labels.split(), subject=subject, replies=replies))

add('pewter_brock_cerulean_next','PewterCity_Gym_Text_BrockPostBattle',
    'Brock praises our talent and recommends challenging Cerulean Gym.', '''
S~A compliment and directions. Much easier to carry than another boulder.|
S~A new Gym means a different test. We can take confidence without assuming the same plan will work.|
S~Good win. Check the team before the next road.|
S~He is sending us onward like he expects to hear good things.|
S~We should celebrate with the team before turning this into the next errand.|
S~The formidable first obstacle has become a generous guide to the next chapter.|
S~I appreciate an opponent who gives us something useful besides bruises.|
N~Cerulean is a concrete next objective. Time to check the route and our supplies.|
S~A stone can mark the beginning of a road rather than block it.|
S~He sounds sincerely impressed. You are allowed to enjoy that.|
S~I wonder what he hopes challengers remember about meeting him here.
''')
add('pewter_liam_brock_hotter','PewterCity_Gym_Text_LiamPostBattle',
    'Liam calls us good but insists Brock is even better.', '''
M~We are hot, but Brock is hotter. The Rock Gym has developed a temperature scale.|
N~He recognizes our strength while warning about his leader. Both observations can be useful.|
N~We will take Brock seriously. He does not need to diminish our win to arrange that.|
N~I think that was a compliment trying not to disappoint his favorite person.|
N~We can be proud of this battle and still prepare for the next one.|
M~A favorable review carefully approved by the Brock appreciation committee.|
M~A compliment with a larger compliment standing directly behind it.|
N~Then the next test will need its own plan. This result does not predict all the others.|
N~One stone is not the mountain. We still earned our footing.|
M~I appreciate his loyalty. The comparison is doing a lot of work.|
N~He admires Brock enough to put him into every part of this conversation.
''')
add('pewter_rock_tomb_tm','PewterCity_Gym_Text_ExplainTM39',
    'Brock explains the single-use Rock Tomb TM and its Speed reduction.', '''
U~The rocks hurt and make you slower. I had a similar experience carrying groceries.|
N~Reduced Speed can influence later turns. The single-use TM makes choosing its recipient important.|
N~Check who can learn it before deciding. We cannot take the lesson back afterward.|
N~I like moves that leave the next moment a little easier to handle.|
N~Let us choose a teammate it really suits, rather than use a gift just because it is new.|
M~A lesson in momentum, taught by a rather unaccommodating pile of stones.|
M~A permanent educational decision disguised as a small disc. No pressure.|
N~Damage plus speed control. Its second effect may be more useful than the first.|
N~The falling stone changes the rhythm after the impact.|
N~He explained the limitations clearly. We should give the choice the same care.|
N~It is a useful reminder to watch what a move changes beyond the visible hit.
''')
add('pewter_guide_party_order','PewterCity_Gym_Text_TryDifferentPartyOrders',
    'The guide explains the lead Pokemon and recommends changing party order for opponents.', '''
M~We can change the plan by moving a name up a list. Finally, tactics that respect my knees.|
N~The opening matchup can shape the whole battle. Party order is worth reviewing deliberately.|
N~Put the right partner first. Do not make the lead position somebody's permanent chore.|
N~It is nice to have one useful thing we can decide before the noise starts.|
N~Different teammates deserve chances to begin when the situation suits them.|
N~The cast order can change the opening scene more than a louder entrance.|
M~A rearrangement that accomplishes more than most of my rearranging.|
N~A low-cost adjustment with a potentially large effect. Good advice.|
N~Who takes the first step changes how the others can follow.|
N~A fitting order depends on where we are going. It need not stay the same forever.|
N~I will watch how each teammate handles getting the first turn.
''')
add('pewter_guide_champ_material','PewterCity_Gym_Text_YoureChampMaterial',
    'The guide says the victory proves we are Champion material.', '''
F~Champion material! I hope it is comfortable and does not shrink in the wash.|
S~A promising result. Becoming Champion will involve many more, not merely repeating this one.|
S~Take the encouragement. Keep doing the work.|
F~He sounds very certain. I hope the feeling reaches you without turning into pressure.|
S~We can enjoy this step without asking the team to carry the whole future today.|
S~Our enthusiastic adviser has upgraded the forecast to a possible championship finale.|
S~You do not have to be perfect tomorrow to deserve his happiness today.|
N~The first test is passed. The next ones will supply more information.|
S~A bright possibility does not need to become a demand.|
S~That confidence is a gift. You get to choose how to carry it.|
S~I would remember how it felt to hear that before the title became anything more than a possibility.
''')
add('cerulean_diana_other_trainers','CeruleanCity_Gym_Text_DianaPostBattle',
    'Diana says battling other trainers reveals how good one really is.', '''
M~Other people are an inconvenient but effective test of my excellent imaginary plans.|
N~An unfamiliar opponent can expose weaknesses a familiar routine never tests.|
N~A real battle teaches something. It does not need to decide your entire worth.|
N~It is easier to learn when losing is allowed to mean more than being bad.|
N~Different partners bring different lessons. So do different opponents.|
M~A private rehearsal has encountered the very useful inconvenience of another actor.|
N~Reality is an annoyingly thorough editor.|
N~Test the plan against behavior you did not design yourself. That is where the surprises are.|
N~A mirror shows one side. Another traveler shows a different one.|
N~Feedback helps when it is specific. A single result still leaves plenty unknown.|
S~She seems to have learned something about us and herself from the same match.
''')
add('cerulean_luis_misty_will_win','CeruleanCity_Gym_Text_LuisPostBattle',
    'Luis insists Misty keeps improving and cannot lose to someone like us.', '''
M~Misty is improving. We are apparently expected to remain politely where he last estimated us.|
N~Her progress is a reason to prepare, not evidence that ours must stop.|
N~We can respect her without accepting his opinion of us.|
N~I would rather meet her than keep hearing who we supposedly are.|
N~Let us check our team instead of arguing over his prediction.|
M~The local fan has declared our role in advance. We are free to improvise.|
M~Someone like us. He has known us for an impressively brief time.|
N~Both teams can improve. His forecast leaves out one moving variable.|
N~A person's certainty does not narrow the road under our feet.|
N~Admiring her does not require being rude to everyone else.|
N~I wonder what Misty would think of him dismissing her challengers before she meets them.
''')
add('cerulean_water_pulse_tm','CeruleanCity_Gym_Text_ExplainTM03',
    'Misty gives Water Pulse and suggests an aquatic Pokemon learn it.', '''
S~A water move for a water-loving teammate. Finally, a lesson that comes with its own splash zone.|
N~We should check compatibility rather than choose purely by appearance.|
N~See who can learn it and who benefits. Then choose.|
S~I would like to see a teammate enjoy learning something that suits them.|
N~Let us make sure the recipient actually needs another Water move first.|
M~An aquatic part is available. We should cast it for ability rather than costume alone.|
M~I support teaching it to someone who enjoys being damp more than I do.|
N~The suggested category is a start. The actual movepool is the specification.|
N~Let the lesson find a creature it belongs with.|
N~A thoughtful match is better than giving it to the first blue Pokemon we see.|
S~She sounds pleased to share a move she likes with somebody new.
''')
add('cerulean_guide_water_matchups','CeruleanCity_Gym_Text_GymGuyAdvice',
    'The guide recommends Grass or Electric Pokemon against Misty Water team.', '''
M~Drain them or zap them. His tactical vocabulary has a very practical little sound department.|
N~Grass and Electric attacks offer useful matchups. We still need to consider individual opponents.|
N~Good starting advice. Check our actual team before assuming a type alone will win.|
N~Having a plan makes the pool feel a little less enormous.|
N~The right matchup helps the team avoid taking unnecessary damage.|
M~Our adviser has supplied two possible approaches and one enthusiastic nickname for us.|
M~Champ in the making. I would settle for challenger with dry socks.|
N~Two counter-options. Choose based on the moves and resources we actually have.|
N~There is more than one way through the water.|
N~We can use the advice without making our own team feel like the wrong choice.|
N~I would like to see how Misty responds when someone arrives with that very common plan.
''')
add('cerulean_guide_shared_credit','CeruleanCity_Gym_Text_WeMakePrettyGoodTeam',
    'The guide claims we make a great team after we beat Misty.', '''
M~You, me, and the Pokemon who did all the splashing. A very large team, selectively remembered.|
S~The advice helped. The team still had to carry out the battle.|
S~He can share the celebration. Make sure our Pokemon get the credit.|
S~I like that he feels involved. It is nice to have someone waiting to be happy for us.|
S~A little encouragement can matter. So can thanking the ones who actually battled.|
M~The adviser has awarded himself a supporting credit in our successful production.|
M~I admire his confidence in a partnership conducted entirely from the dry side of the room.|
N~Useful input, successful execution. Different contributions, both easy to acknowledge.|
S~A few kind words can travel alongside a team without entering the battle.|
S~I am happy he is celebrating. Let us widen the thanks to everyone involved.|
S~He was waiting to see how we did. That is a small kindness worth noticing.
''')
add('vermilion_surge_ground_immunity','VermilionCity_Gym_Text_LtSurgePostBattle',
    'Surge warns that Electric attacks do not affect Ground Pokemon.', '''
U~Powerful electricity, stopped by dirt. Nature has a very dry sense of humor.|
N~Immunity matters more than raw power in that matchup. We should remember the type, not the appearance.|
N~A strong move still needs the right target. Good lesson.|
N~It helps to know there is something a frightening attack simply cannot do.|
N~Knowing our team's limits is part of keeping them safe.|
M~The grand electrical spectacle meets a remarkably firm objection from the ground.|
M~I appreciate a weakness that can be explained without making me touch a wire.|
N~Increasing output will not solve an immunity. Change the approach.|
N~The earth has its own answer to a storm.|
N~A confident fighter admitting a clear limit. I respect that.|
N~I wonder how often he has watched challengers learn that the hard way.
''')
add('vermilion_tucker_locked_door','VermilionCity_Gym_Text_TuckerPostBattle',
    'Tucker connects the difficult door with Surge cautious military habits.', '''
M~Caution is one thing. Hiding the entrance behind the rubbish is a very personal interpretation.|
N~He has carried a security habit into the Gym design. It certainly slows visitors.|
N~A cautious leader can still make the exit obvious. I hope he did.|
N~It makes meeting him sound like something we need clearance for.|
N~I hope the staff can get through quickly when somebody needs help.|
M~An audience with the commander requires defeating both his team and his housekeeping.|
M~Cautious enough to make strangers inspect his bins. A remarkable defensive doctrine.|
N~Security should account for usability. I would like to see the emergency procedure.|
N~Some old habits become walls long after the danger changes.|
N~The story explains the locks. It does not make them less irritating.|
N~I wonder which part of this place feels reassuring to him rather than inconvenient.
''')
add('vermilion_baily_switch_hint','VermilionCity_Gym_Text_BailyPostBattle',
    'Baily gives the vague hint that door switches are hidden inside something.', '''
M~Inside something. Our search has narrowed to the entire concept of containers.|
M~Technically information. Only slightly more specific than saying they exist.|
M~He could have saved us a little more time than that.|
N~I think he wants the secret to survive the explanation.|
N~We can look carefully without turning the room upside down.|
M~A witness has revealed that the concealed objects are, indeed, concealed.|
M~A generous serving of almost an answer.|
M~I shall record that under insufficiently specified location data.|
M~The secret has moved from nowhere to somewhere. Progress, of a kind.|
M~A hint so discreet it can barely be distinguished from withholding one.|
N~I will watch where people glance when the switches come up. It may be more useful than that answer.
''')
add('vermilion_dwayne_adjacent_switch','VermilionCity_Gym_Text_DwaynePostBattle',
    'Dwayne says Surge built the double locks and the second switch neighbors the first.', '''
S~The second switch is next door to the first. Finally, a neighbor with useful information.|
N~Adjacent to the first switch. That substantially reduces the search space.|
N~Remember the first location before checking its neighbors.|
N~An actual clue. I can feel the room becoming less confusing.|
N~We should slow down once we find the first one, not rush past the useful detail.|
S~The mystery has acquired a rule instead of merely a personality.|
M~A secret explained by someone apparently willing to explain it. Refreshing.|
S~A local adjacency constraint! Much better than searching randomly.|
N~The second answer waits close to the first. Keep track of where we began.|
N~That is a hint I can use without pretending to understand the leader's entire life.|
N~I would remember which bin started the sequence before looking anywhere else.
''')

add('celadon_erika_attractive_collection','CeladonCity_Gym_Text_ErikaPostBattle',
    'Erika admires our cataloguing but says she would collect only attractive Pokemon.', '''
N~Some of my favorite faces look like a dropped sandwich. They still deserve an entry.|
N~A catalogue is most useful when it includes what the observer would not personally choose.|
N~She can have favorites. The others still matter.|
N~I like the strange ones that take a little longer to understand.|
S~Sometimes a creature becomes beautiful because you know how it greets you.|
N~An excellent personal collection and a complete account are different projects.|
M~Fortunately, attractiveness has never required unanimous approval. I checked.|
N~Research that selects only appealing examples produces a distorted record.|
N~There are flowers that look like weeds until someone kneels close enough.|
N~Her taste is her own. I would rather keep mine curious.|
N~A less obvious subject can become the picture you remember longest.
''')
add('celadon_kay_sour_loss','CeladonCity_Gym_Text_KayPostBattle',
    'Kay hopes Erika defeats us after losing.', '''
M~We have lost the local cheering section. Fortunately, it was already cheering for someone else.|
N~She is disappointed. Her wish tells us little about the battle ahead.|
N~Let us move on. Winning does not require getting her approval.|
N~I hope she feels better after we leave. We do not have to wait for it.|
N~We can be kind without standing here to receive more anger.|
M~The defeated supporting character has handed the revenge subplot to management.|
M~A hostile review from a very recently defeated critic.|
N~That is an emotional response, not additional tactical information.|
N~Her sharp words can stay in this room.|
N~We are allowed to enjoy the win without convincing her to enjoy it with us.|
N~I would rather remember the team working together than the last thing she said.
''')
add('celadon_bridget_grass_matchups','CeladonCity_Gym_Text_BridgetPostBattle',
    'Bridget explains Grass advantages against Water, Rock and Ground.', '''
U~A leaf has a surprisingly ambitious list of things it can defeat.|
N~Three useful matchups. We should still check the opponent's other type and moves.|
N~Good advantages to know. They are a start, not permission to stop thinking.|
N~Something that looks delicate can have a very firm answer.|
N~It helps to know when a teammate will feel at home in the battle.|
M~The greenery has arrived with a rather assertive list of professional references.|
M~I admire a plant that can make a rock regret its choices.|
N~An effective range of targets. Coverage gaps still matter when building the rest of a team.|
N~Roots know how to enter both stone and soil.|
N~A gentle appearance is not the same thing as a weak position.|
N~I like watching an unassuming teammate reveal exactly what it can do.
''')
add('celadon_tina_attention','CeladonCity_Gym_Text_TinaPostBattle',
    'Tina realizes the attention she noticed was directed at Erika.', '''
F~The misunderstanding has left the conversation very carefully through a side door.|
F~We should not turn an awkward realization into a public investigation.|
N~No need to make her feel worse. We can leave it there.|
F~I would like everyone to look somewhere neutral until this feeling passes.|
N~A little kindness will do more than trying to explain every glance.|
F~An imagined subplot has been cancelled in front of its hopeful author.|
F~I am going to study this completely unremarkable patch of floor.|
N~A mistaken observation. No need to make her defend it.|
N~Some small hopes arrive before anyone has invited them.|
N~We can spare her the little laugh she is probably expecting.|
N~Not every awkward moment needs to become a story we keep telling.
''')
add('celadon_tamia_flower_arrangements','CeladonCity_Gym_Text_TamiaPostBattle',
    'Tamia says Grass Pokemon also help the Gym make flower arrangements.', '''
U~The team does battles and centerpieces. I have been dramatically underusing my hobbies.|
S~A shared interest connects their training with something creative outside it.|
S~Good to know the team gets to do more together than fight.|
S~I like imagining the room after practice, when everyone makes something quiet.|
S~Growing things and arranging them together sounds like a pleasant afternoon.|
S~The ensemble handles both combat and the set decoration.|
S~A Gym with a peaceful use for all that enthusiasm. I approve.|
N~I would be interested in how the different Pokemon contribute to the work.|
S~The garden is allowed to be both strong and beautiful.|
U~Finally, someone understands that an arrangement can have a personality.|
S~I would like to see an unfinished one, with the team deciding what belongs where.
''')
add('celadon_lisa_quiet_erika','CeladonCity_Gym_Text_LisaPostBattle',
    'Lisa says Erika is quiet but well known locally.', '''
S~Quiet and famous. An excellent strategy for making everybody else handle the announcements.|
N~Public influence does not require speaking more than everyone around you.|
S~She lets her work establish who she is. Nothing wrong with that.|
S~I like knowing a quiet person does not have to become louder to be taken seriously.|
S~People remember how you make a place feel, too.|
S~A leading role need not be played at maximum volume.|
S~A comforting career possibility for those of us suspicious of introductions.|
N~A reputation is a result of sustained work, not merely the noise around it.|
S~A soft voice can still be the one a room listens for.|
S~She has a presence that does not need to keep asking for attention.|
S~I would rather catch an ordinary moment with her than make her perform being famous.
''')
add('celadon_lori_blind_date_manners','CeladonCity_Gym_Text_LoriPostBattle',
    'Lori wants to improve her manners before a blind date, including if it involves battling.', '''
U~Battle etiquette for a date. I had only prepared how to share the bread basket.|
N~Courtesy under competition is useful. I hope the date is not primarily an examination.|
N~Treat them well whether you win or lose. That is a good place to start.|
F~If the date requires battling, I would like to know before choosing what to wear.|
S~Listening and being kind are easier to remember than an elaborate performance.|
M~The romantic subplot comes with a contingency plan for competitive combat.|
F~I had not considered bringing a battle strategy. My social anxiety is taking notes.|
N~A little preparation helps. Trying to script the entire meeting probably will not.|
N~A stranger may become familiar faster over kindness than victory.|
S~Manners help. So does arriving as someone you can keep being after the first hour.|
S~I hope she gets to enjoy meeting them instead of only checking how she is doing.
''')
add('celadon_mary_better_team_next','CeladonCity_Gym_Text_MaryPostBattle',
    'Mary says she did not bring her best Pokemon and promises a stronger next battle.', '''
M~The best team was unavailable. A very popular explanation among today's defeated teams.|
N~A different team may change the next result. It does not change this one.|
N~We will take the next challenge seriously when she brings it.|
N~I hope the Pokemon beside her do not hear that as being the disappointing ones.|
N~This team did its best today. They deserve care before comparisons.|
M~An unfavorable premiere has prompted a promise to replace the cast.|
M~The invisible better team remains undefeated. Impressive record.|
N~Then the next test will involve different conditions. We should prepare rather than argue.|
N~The creatures who came with her are still the ones waiting for kindness now.|
N~A better team begins with treating the current one as worth her attention.|
N~I would like to see what she learns before the next meeting, not only who she brings.
''')
add('fuchsia_kayden_brawn_brains','FuchsiaCity_Gym_Text_KaydenPostBattle',
    'Kayden praises our combination of strength and thought but is surprised by a young trainer.', '''
M~Brawn and brains. I contribute a third quality: standing somewhere inconvenient.|
S~He noticed the decisions behind the power. The surprise about age is less useful.|
S~You used what the team could do well. That is worth recognizing.|
S~I like being noticed for thinking, even when somebody sounds surprised we can.|
S~A good plan gives the team room to use its strengths.|
S~The reviewer has noticed both the action and the rather important work behind it.|
M~A compliment that almost made it to the end without expressing surprise at our existence.|
N~Force and planning are complementary. Neither excuses ignoring the other.|
N~A strong arm still needs to know what it is reaching for.|
S~Keep the useful praise. The surprised tone can stay with him.|
S~I would like to know which choice made him stop and reconsider us.
''')
add('fuchsia_kirk_koga_teachings','FuchsiaCity_Gym_Text_KirkPostBattle',
    'Kirk will keep training under Koga teachings after losing.', '''
S~He still has a teacher and tomorrow. Losing has not cancelled either.|
N~A consistent method can help, provided he reviews what this battle exposed.|
N~Keep training. Just leave room to change what did not work.|
S~It helps to have somewhere to return with the mistakes you want to understand.|
N~I hope the next lesson includes giving the team a proper rest.|
S~A loyal student has placed the defeat inside a longer course of study.|
N~Devotion is useful when it leaves room for an inconvenient question.|
N~Test the method against the result. Loyalty does not require ignoring data.|
N~A teaching can be a path without becoming a cage.|
S~It is nice to have a practice you still believe in on a bad day.|
N~I wonder what Koga will ask him about this battle when he describes it.
''')
add('fuchsia_nate_lingering_status','FuchsiaCity_Gym_Text_NatePostBattle',
    'Nate likes poison and sleep because their effects outlast the battle.', '''
N~An attack that follows you home. A particularly unwelcome souvenir.|
N~Persistent effects make recovery supplies important beyond the immediate battle.|
N~Check the team afterward. Winning does not automatically make everyone well.|
N~I dislike the part where the fight can be over and someone is still hurting.|
N~We should tend to any lingering condition before continuing.|
N~The antagonist enjoys an effect that ignores the closing curtain.|
M~A memorable impression. Unfortunately, the medical sort.|
N~Post-battle state matters. We should inspect it instead of assuming the reset is complete.|
N~Some harms remain after the noise stops. Notice them.|
N~I prefer a battle that ends when both sides agree it has ended.|
N~I will watch how the team is moving afterward, not only whether we won.
''')
add('fuchsia_phil_wall_gaps','FuchsiaCity_Gym_Text_PhilPostBattle',
    'Phil compliments the win and advises looking closely for gaps in the invisible walls.', '''
M~Look closely at the invisible thing. A hint with an ambitious relationship to eyesight.|
N~The gaps are the useful detail. We can test the route systematically.|
N~Slow down and follow the boundary. Guessing wildly will take longer.|
N~I would like to draw the path as we learn it. It is easy to forget what we cannot see.|
N~Let us avoid sending a teammate into each wall just to find the way.|
M~The scenery is concealed, but the exit apparently has visible intentions.|
M~I will stare at the air with renewed purpose.|
N~Map the obstruction, then identify the breaks. Unseen does not mean unmeasurable.|
N~Even a hidden wall must leave room for a path.|
N~A patient look costs less than another bruised shoulder.|
N~I am watching where people actually walk. That may tell us more than the empty-looking room.
''')
add('fuchsia_edgar_more_to_learn','FuchsiaCity_Gym_Text_EdgarPostBattle',
    'Edgar admits he still has a great deal to learn.', '''
S~A short sentence with a whole useful future inside it.|
S~Recognizing what is unknown is a good beginning, not an embarrassment.|
S~He can start with this battle. One thing to change is enough for today.|
S~It is good when you can say that without having to sound ashamed.|
S~I hope he is as patient with himself as he would be with a new Pokemon.|
S~An honest closing line leaves the next chapter open.|
S~I trust that more than a speech explaining why the result does not count.|
N~Now identify the first question. A vague gap becomes manageable when it is specific.|
S~An open hand can receive more than a clenched one.|
S~He did not turn the admission into an excuse or an insult. I like that.|
N~I would ask what surprised him most. That is often where the next lesson begins.
''')
add('fuchsia_shawn_light_shadow','FuchsiaCity_Gym_Text_ShawnPostBattle',
    'Shawn asks whether we choose light or shadow.', '''
M~I choose whichever contains the exit and preferably a chair.|
N~Those are not independent options. A shadow depends on a light source.|
N~Depends what we need. Shade is useful on a hot day.|
N~A little shade can feel kind. I do not think it needs to become a declaration.|
N~I choose a place where the team can rest comfortably.|
M~A dramatic either-or has encountered the practical appeal of sitting under a tree.|
M~Shadow, if this is about where I have to stand for the rest of the conversation.|
N~Could he specify the task? The correct lighting depends on what we are trying to do.|
S~I prefer the place they meet. Edges reveal things.|
N~Both belong in a good room. One makes the other interesting.|
S~Light shows the face. Shadow gives it shape. I would not want to lose either.
''')

add('cinnabar_blaine_fire_blast','CinnabarIsland_Gym_Text_BlainePostBattle',
    'Blaine recommends teaching Fire Blast to a Fire Pokemon such as Vulpix or Charmeleon.', '''
U~Fire Blast. A name that has not wasted anybody's time wondering what it does.|
N~His examples are sensible. We should still check the recipient's current moves before teaching it.|
N~Choose someone who can use it well. A strong move is not automatically the right replacement.|
N~I would like to admire the demonstration from somewhere with very little dry grass.|
N~Let us decide with the whole team's needs in mind.|
M~The gift arrives with casting suggestions and a distinctly unsubtle stage effect.|
M~I appreciate being told the fire is going to be a blast before meeting it personally.|
N~A high-output option. Compatibility and the rest of the moveset still matter.|
N~A fierce flame asks for a hand that knows how to guide it.|
N~A dramatic move deserves a thoughtful choice of who gets it.|
N~I would want to see how the chosen teammate makes that power its own.
''')
add('cinnabar_erik_combustion_lecture','CinnabarIsland_Gym_Text_ErikPostBattle',
    'Erik begins explaining oxygen and combustion before trailing into blah blah.', '''
M~The fire needed oxygen. The explanation eventually needed an ending.|
M~He had a real explanation before abandoning it to sound effects. I would have listened.|
M~If there is a useful point, he can make it without holding us here all afternoon.|
N~I feel bad when someone stops expecting people to listen halfway through a thought.|
N~A shorter explanation might give the interesting part room to land.|
M~A promising opening paragraph has been swallowed by its own placeholder text.|
M~He reached the scientific term for the moment my attention left the room.|
M~Oxygen was relevant. I was waiting for the rest of the mechanism.|
N~A fire needs air. A thought needs someone willing to finish tending it.|
M~Editing is an act of kindness to the person standing in front of you.|
N~I would ask one specific question. It might help him find the part he actually wants to tell us.
''')
add('cinnabar_quinn_stealing_urge','CinnabarIsland_Gym_Text_QuinnPostBattle',
    'Quinn admits wanting to steal other people Pokemon.', '''
A~Wanting a Pokemon is not a permission slip to take somebody else's partner.|
A~An urge is something he is responsible for managing, not an instruction the rest of us must accept.|
A~Keep the team close. We do not owe him a chance to prove he means it.|
D~I do not like hearing someone talk about another person's companion that way.|
A~A Pokemon is not a prize he gets to take because he wants one.|
A~A troubling confession has arrived with rather too little concern for its intended victims.|
A~I am suddenly more interested in keeping our belongings and partners beside us.|
A~He needs a way to interrupt that behavior before anyone is harmed.|
N~Desire does not undo another creature's home.|
A~There are ordinary ways to meet a Pokemon. Theft does not become charming because he admits it.|
N~I would rather leave than give him more details about our team.
''')
add('cinnabar_avery_complicated_theories','CinnabarIsland_Gym_Text_AveryPostBattle',
    'Avery claims his theories are too complicated for us to understand.', '''
M~An impressive theory. Apparently its greatest defense is refusing to explain it.|
M~An explanation is part of the work. Complexity alone does not establish correctness.|
M~If he will not explain, we are allowed to stop asking.|
N~Not understanding a bad explanation does not make us incapable of learning.|
N~He could start with one small part if he actually wanted to share it.|
M~A grand manuscript has been protected from criticism by withholding every page.|
M~I have never met such carefully guarded evidence of being clever.|
M~Then identify the prerequisite and begin there. Otherwise this is only a claim about us.|
N~A locked box can hold a treasure or nothing. The lock does not tell us which.|
M~A little mystery can be stylish. Condescension is harder to accessorize.|
N~I would rather hear him explain one thing well than tell us how much we cannot know.
''')
add('cinnabar_ramon_thief_pokemon','CinnabarIsland_Gym_Text_RamonPostBattle',
    'Ramon wishes for a thief Pokemon he could use.', '''
A~A Pokemon is not a way to outsource being responsible for stealing.|
N~Training another creature to carry out the act would not remove his responsibility for it.|
A~A partner deserves a better ambition than becoming his excuse.|
N~I hope he finds something kinder to be excited about teaching.|
A~A good teammate is somebody you care for, not somebody you send to take things for you.|
A~He would like an accomplice written as a convenient special ability.|
M~A career plan that becomes worse when he starts recruiting.|
N~The tool does not change the purpose of the task. He is still describing theft.|
N~A creature follows the path we teach. That is a reason to choose the path carefully.|
A~Wanting a partner should begin with what he can offer it, too.|
N~I wonder whether he has ever pictured the person waiting for the stolen Pokemon to come home.
''')
add('cinnabar_derek_fiery_bird','CinnabarIsland_Gym_Text_DerekPostBattle',
    'Derek tells how a fiery bird helped the lost Blaine descend a mountain at night.', '''
U~A bird became the emergency lantern. I hope Blaine sent a very large thank-you.|
N~That is an extraordinary account. I would like to hear which details Blaine remembers directly.|
S~Something helped him find a safe way down. That is the important part.|
S~Seeing a light when you thought you were alone must have stayed with him.|
S~I hope he has given other lost people that same feeling of relief since then.|
S~A life-changing encounter arrived as a light in a scene that had nearly lost its way.|
S~A quiet reason to care about a fierce kind of Pokemon. I like that.|
N~I would ask about the route, the conditions, and what the light revealed.|
S~A flame on the mountain became a path home.|
S~I can see why that story would matter more than any ordinary winning battle.|
S~I would rather hear him remember it than try to turn it into a spectacle for us.
''')
add('cinnabar_dusty_popular_fire','CinnabarIsland_Gym_Text_DustyPostBattle',
    'Dusty names Ponyta and Ninetales as popular Fire Pokemon.', '''
M~Popular and warm. A dangerous combination when everyone wants to hug you.|
N~Both are memorable examples. Their individual needs differ considerably.|
N~Popularity is not a care guide. Learn about the partner before choosing one.|
S~I can understand why people notice them. I would still want to know their quieter habits.|
S~A beautiful Pokemon also needs somebody who likes the everyday work of looking after it.|
M~Two impressive candidates with excellent silhouettes and a rather demanding heating department.|
M~I admire them from the distance recommended for clothing that is not fireproof.|
N~Their appearance is familiar. Housing and handling would require a more detailed plan.|
S~A flame can be admired without being asked to belong to us.|
S~They are striking. I hope people admire the actual creatures, not only the idea of looking impressive beside one.|
S~I would love to see the way their fire moves when they are relaxed.
''')
add('cinnabar_zac_fire_matchups','CinnabarIsland_Gym_Text_ZacPostBattle',
    'Zac explains Water beats Fire while Fire beats Ice.', '''
M~Every dramatic element has somebody else arriving with a very practical objection.|
N~A favorable matchup in one direction does not remove a weakness in another.|
N~Know both sides of the matchup. Nobody gets to be strong against everything.|
N~It helps to think about who needs support rather than only who looks strongest.|
N~A teammate can be brilliant at one job and need help with the next.|
M~The cast of elements has developed an admirably balanced schedule of rivalries.|
M~Even fire has situations where it would rather not be the center of attention.|
N~Matchups are relationships, not a single ranking from best to worst.|
N~What melts one barrier can be quieted by another.|
N~A weakness does not erase a strength. It tells us where a partner might help.|
N~I like seeing how different teammates make room for each other's difficult matchups.
''')
add('saffron_amanda_willpower','SaffronCity_Gym_Text_AmandaPostBattle',
    'Amanda says equal opponents are separated by will and urges focus against Sabrina.', '''
N~Focus helps. I would still like a plan that works even when my eyebrows stop looking determined.|
N~Concentration matters, but equal strength does not make every other variable disappear.|
N~Keep your attention on the battle. You do not need to turn losing into a failure of character.|
N~I hope she means staying present, not being angry at yourself for feeling afraid.|
N~Determination works better when the team is rested and trusts the plan.|
N~A forceful inner monologue still needs an actual next move.|
M~I have been willing myself to win for years. It occasionally requires supplementary practice.|
N~Focus is useful. Preparation and information remain useful even when motivation is high.|
N~A steady flame still needs fuel. Will alone is not everything.|
N~You can want it fiercely and still deserve kindness if it goes badly.|
N~I would watch the decisions that focus makes possible, rather than try to measure the feeling itself.
''')
add('saffron_johan_psychic_fears','SaffronCity_Gym_Text_JohanPostBattle',
    'Johan claims Psychic Pokemon fear only Ghosts and Bugs.', '''
N~Only ghosts and bugs? His list sounds rather more confident than complete.|
N~That advice leaves out the Dark matchup. We should use the current type chart, not his certainty.|
N~Remember Dark moves, too. Do not build a team from one trainer's incomplete list.|
N~A frightening reputation can make people stop checking the details.|
N~There are more options than he mentioned. We can choose what suits our own team.|
M~The declaration has omitted an entire dark corner of the cast.|
M~His explanation seems to have a weakness of its own.|
N~An incomplete specification can still sound authoritative. Verify the matchups.|
N~He has named two shadows and missed the darkness between them.|
N~Confidence is not a substitute for remembering the rest of the list.|
N~I would rather check what our teammates can actually do than let that narrow our choices.
''')
add('saffron_stacy_master_psychic','SaffronCity_Gym_Text_StacyPostBattle',
    'Stacy wants to master Psychic and teach it to her Pokemon.', '''
M~A learning project for the whole team. I hope she does not assign them all the same homework.|
N~Understanding a move and choosing which partner benefits from it are separate tasks.|
N~Keep learning. Make sure the move suits the Pokemon, too.|
N~I like hearing a next step that sounds possible instead of just promising never to lose again.|
N~The team can learn with her, at a pace that leaves room for mistakes.|
S~The lesson continues after the scene ends. A useful kind of unfinished business.|
N~A concrete goal is easier to live with than the instruction to become generally perfect.|
N~One specific technique gives her something measurable to practice.|
N~A thought becomes a path when it names the next step.|
N~I hope she notices what each partner brings to the lesson, too.|
N~I would be interested to see what changes when she tries it again.
''')
add('saffron_tyron_dojo_defeat','SaffronCity_Gym_Text_TyronPostBattle',
    'Tyron says Sabrina decisively defeated the neighboring Karate Master.', '''
N~The neighbor lost very thoroughly. I hope that is not how every conversation between the buildings begins.|
N~That matchup favors her specialty. It is not a complete judgment on his training.|
N~He lost a battle. No need to keep making it a public humiliation.|
N~I wonder whether the neighbors can still speak without somebody bringing up the result.|
N~A strong community needs more than the winner feeling important.|
N~A local rivalry has acquired a narrator who greatly prefers one ending.|
M~A victory with apparently unlimited retelling rights.|
N~The result is useful matchup information. The contempt is not.|
N~Two doors can remain beside each other long after the contest ends.|
N~I would rather know what each place teaches than hear which one is allowed to feel superior.|
N~I wonder what the same afternoon looked like from the other doorway.
''')
add('saffron_tasha_predicted_loss','SaffronCity_Gym_Text_TashaPostBattle',
    'Tasha claims she knew the defeat would happen.', '''
M~She predicted it. I am impressed by how reliably predictions arrive after the event.|
N~A prediction recorded beforehand would be easier to evaluate.|
M~Then she could have warned her team a little more usefully.|
N~Maybe knowing would not make a difficult moment feel any easier.|
N~I hope the team still gets comfort instead of being told it was inevitable.|
M~The defeated prophet has added a retrospective footnote to the script.|
M~An undefeated record of explaining losses after they happen.|
N~That claim does not tell us what she expected or when.|
N~Even an expected rain can leave someone wet.|
M~I would like to see the prediction before accepting the excellent timing.|
N~I wonder whether that is certainty or a way of feeling less caught off guard.
''')
add('saffron_cameron_two_gyms','SaffronCity_Gym_Text_CameronPostBattle',
    'Cameron boasts the Psychic Gym defeated the dojo and removed its Gym status.', '''
N~Two schools became one official Gym and one very long-running brag.|
N~Winning a contest determined the title. It did not erase the dojo's ability to teach.|
N~They can be proud without treating the neighbors as worthless.|
N~I hope the people next door still feel they belong in their own town.|
N~There ought to be room for both groups to care about their Pokemon.|
N~An institutional rivalry has been edited into an unnecessarily triumphant anecdote.|
N~An official title is useful. It is not the only proof that a place matters.|
N~Different training methods can remain valuable after an administrative decision.|
N~A sign was taken down. The lives behind the door remained.|
N~I would rather see what survives in both schools than join a victory lap over the loss.|
N~I want to hear the dojo's version before letting that become the whole history.
''')
add('saffron_preston_telepathy','SaffronCity_Gym_Text_PrestonPostBattle',
    'Preston says he used telepathy to read our mind.', '''
U~Then he knows where I left the thought I was having. Please ask.|
N~A claim about private information needs more than an announcement.|
M~He can keep out of our heads. The conversation works fine out here.|
F~I would prefer he asked before looking, if that is something he can do.|
N~Being able to learn something does not make it kind to take it.|
M~An intrusive narrator announces access to the unpublished draft.|
M~My condolences to him. I have been living in there for years.|
N~I would propose a blinded test before accepting that result.|
N~A mind is still someone's room, even if the door is easy to open.|
N~I would like my private thoughts to remain an invitation, not an open service.|
N~Did he notice what we were thinking, or only what he expected us to think?
''')

add('viridian_yuji_leader_power','ViridianCity_Gym_Text_YujiPostBattle',
    'Yuji warns that keeping up with his leader requires power.', '''
N~We brought power. I would like to bring a little planning along as well.|
N~Power is one requirement. A good matchup may change how much of it we need.|
N~We will prepare. We do not have to rush because he sounds certain.|
N~I would rather hear what makes the leader difficult than another warning about strength.|
N~Let us make sure the team is well enough to use the strength it has.|
N~The penultimate opponent has issued the traditional warning about the main attraction.|
M~I will add power to the list, immediately beneath not panicking.|
N~Then check our resources and matchups. A warning should lead to a practical response.|
N~A heavy door still opens on the right hinge.|
N~We can take him seriously without accepting that only brute force will work.|
N~I wonder what he has seen challengers do wrong against the leader.
''')
add('viridian_atsushi_unworthy','ViridianCity_Gym_Text_AtsushiPostBattle',
    'Atsushi calls himself unworthy after losing.', '''
N~He lost a battle. That is a result, not a certificate about his entire existence.|
N~Worth is not a statistic this contest can measure. The battle can still teach him something.|
N~He needs a correction to the plan, not a reason to hate himself.|
D~I know how quickly a mistake can grow into that word. It still is not the truth.|
N~I hope he speaks to his team more kindly than he is speaking to himself.|
N~One unfavorable scene has been mistaken for the verdict on the whole character.|
N~A cruel narrator lives in that sentence. He need not keep giving it the pen.|
N~Review the failure specifically. A vague judgment cannot be repaired.|
N~A bowed branch is not a worthless tree.|
N~He deserves a next attempt without having to earn the right to matter first.|
N~I would ask what he wants to improve when he is ready to say something gentler.
''')
add('viridian_jason_leader_identity','ViridianCity_Gym_Text_JasonPostBattle',
    'Jason asks whether we know the Gym Leader identity.', '''
M~An identity quiz inside a Gym. Most places settle for a sign.|
N~He has a specific person in mind. We should see who is actually here rather than speculate.|
N~We will find out. Keep your attention on the room.|
N~The way he asked makes the answer feel less ordinary than it should.|
N~I would rather know how the leader treats people than only learn a name.|
M~A mysterious final entrance is being promoted by its own supporting cast.|
M~I dislike a workplace that treats the manager's name as a dramatic reveal.|
N~The room contains a testable answer. We do not need a theory yet.|
N~A hidden name still belongs to a real person. Soon we will meet them.|
N~An introduction should not require this much suspense.|
N~I am watching how people react when they mention him. That may tell us more than the name.
''')
add('viridian_kiyo_karate_team','ViridianCity_Gym_Text_KiyoPostBattle',
    'Kiyo wishes his Pokemon were as good at karate as he is.', '''
M~His Pokemon have been asked to explain a result their trainer has already excused himself from.|
N~Teaching requires adapting the method to the learner, not comparing them unfavorably with oneself.|
N~Then he should help them learn. Blaming the team will not do it.|
N~I hope they know he still values what they can do in their own way.|
N~A good teacher notices the student's needs before admiring his own skill.|
M~The instructor has written an excellent review of himself and a poor one of his entire cast.|
M~A shame his own technique did not include a way to teach it.|
N~A skill is not transferred merely by demonstrating how pleased you are with having it.|
N~Their bodies have their own ways of finding strength. He should learn those, too.|
N~The team deserves more than being the place he puts his disappointment.|
N~I would rather see what he changes in the next practice than hear another comparison.
''')
add('viridian_warren_scolding','ViridianCity_Gym_Text_WarrenPostBattle',
    'Warren worries his leader will scold him for losing.', '''
N~I hope the lesson is about the battle, not about making him afraid to return.|
N~Fear of reporting failure makes accurate learning harder. That is poor leadership.|
N~He should be able to discuss a loss without expecting humiliation.|
D~The way he said that makes this room feel smaller.|
N~I hope his team gets comfort rather than having the fear passed down to them.|
N~An ordinary defeat has become a scene he is afraid to take back to his own director.|
N~That is a miserable thing to be thinking about while your team needs you.|
N~A useful review identifies what to change. Scolding alone does not.|
N~A place of learning should not make the path back feel dangerous.|
N~He sounds worried about more than a lost match. I do not like that.|
N~I wonder what he would say about the battle if he were not afraid of the listener.
''')
add('viridian_takashi_league_dismissal','ViridianCity_Gym_Text_TakashiPostBattle',
    'Takashi mocks our intention to challenge the League.', '''
M~The League has not rejected us. Its unofficial grumbling department has concerns.|
N~His disbelief is not part of the entrance requirements.|
N~We know what we are working toward. He does not need to approve.|
N~A dream can be spoken quietly and still be serious.|
N~We can keep preparing without making the whole journey an answer to him.|
M~An unsuccessful obstacle would like editorial control over the ending.|
M~He has mistaken the right to comment for the power to stop us.|
N~Check the actual requirements. His prediction is not a substitute for them.|
N~A dismissive voice is not a gate.|
N~Ambition is not automatically arrogance just because he dislikes hearing it.|
N~I would rather remember who helped us get there than who said we could not.
''')
add('viridian_cole_careless','ViridianCity_Gym_Text_ColePostBattle',
    'Cole insists his loss was only carelessness.', '''
M~Carelessness is apparently a separate trainer who arrived and lost on his behalf.|
N~If he can identify the careless decision, he has something concrete to improve.|
N~Then learn from it. The result still stands.|
N~I hope he finds the useful part instead of getting stuck defending himself.|
N~The team needs care now, not another explanation of why the loss should not count.|
M~An unfavorable review has been attributed to a temporary lapse in the production.|
M~A popular explanation with very little practical advice attached.|
N~A specific error can be corrected. The label alone is not a correction.|
N~A loose step is still a step that happened. We can choose the next more carefully.|
N~He can keep his pride and still admit we did something well.|
N~I would ask which moment he would change. That answer might actually tell us something.
''')
add('viridian_samuel_league_gate','ViridianCity_Gym_Text_SamuelPostBattle',
    'Samuel says beating the leader is required to reach the League.', '''
N~One more leader between us and the League. A very serious item on the to-do list.|
N~We should confirm the badge requirement and prepare for the actual opponent ahead.|
N~Then we finish this properly. Check the team first.|
N~It feels different hearing the last step described as something in the next room.|
N~Let us take the time the team needs. The goal will still be there after a rest.|
N~The final local gate has a name and a battle waiting behind it.|
N~Almost there is still a place where we are allowed to breathe.|
N~A clear remaining condition. We should not mistake closeness for completion.|
N~The last door deserves the same care as the first.|
N~We have come too far to treat preparation as an inconvenience now.|
N~I want to remember who we are before the next door opens.
''')
add('viridian_giovanni_leaves','ViridianCity_Gym_Text_GiovanniPostBattle',
    'Giovanni promises to disband Rocket, says he will train again, and leaves.', '''
N~I hope he means the part about leaving people alone. They have earned some ordinary, boring days.|
N~He has made a significant promise. What follows will matter more than the declaration.|
N~Let him leave. The people he hurt deserve safety, not another speech.|
N~I keep thinking about everyone who can finally stop watching the door.|
N~I hope the people and Pokemon he harmed get time to recover.|
N~A powerful man has given himself an ending. The people behind him still have lives to rebuild.|
N~I would like his next ambition to involve considerably fewer stolen companions.|
N~A stated shutdown is not the same as every part stopping. We should stay observant.|
N~A shadow moving away leaves things visible that still need tending.|
N~He can choose a new life. The people he hurt should get that freedom, too.|
N~I would rather remember the people who stood up to him than turn his exit into the whole story.
''')
add('saffron_sabrina_everyone_psychic','SaffronCity_Gym_Text_SabrinaPostBattle',
    'Sabrina says everyone has psychic power without realizing it.', '''
U~Then mine has been hiding with the thought I forgot on the way into this room.|
N~An interesting claim. I would like to know how she distinguishes unused power from no measurable power.|
N~Maybe. I would still rather do the work than wait for a hidden talent to solve everything.|
F~I wonder what it feels like before you know how to name it.|
S~I hope people hear a possibility, not another thing they are supposed to prove about themselves.|
M~The audience has unexpectedly been invited to audition for the impossible.|
M~Mine has shown remarkable restraint during every embarrassing conversation of my life.|
N~I would ask what a beginner can actually observe and repeat. That gives the claim somewhere to start.|
S~Some quiet abilities do wait a long time for a name.|
N~It is a lovely possibility. I do not want anyone feeling ordinary as a result to feel defective.|
N~I would ask her about the first moment she realized something unusual was happening.
''')
add('fuchsia_koga_toxic_lesson','FuchsiaCity_Gym_Text_KogaExplainTM06',
    'Koga introduces Toxic as a secret technique passed down for centuries.', '''
U~Four hundred years of practice making somebody have a worse afternoon. An impressive, troubling tradition.|
N~A long history can preserve expertise. We should still understand the technique before using it.|
N~Old does not mean harmless. Learn what it does and how to treat it.|
N~I wonder how a secret feels after being handed to a stranger in a disc.|
N~We should keep remedies ready for effects we choose to bring into a battle.|
M~A centuries-old secret has reached the convenient gift-counter stage of its career.|
M~An ancient legacy of being deeply unpleasant to the opposing team.|
N~I am curious which parts of the method changed over those centuries.|
N~A long-kept secret still asks us what we will do with it now.|
N~A tradition deserves thought, not automatic admiration for its age.|
N~I would like to hear who taught him, and what they wanted him to remember besides winning.
''')
add('fuchsia_koga_worsening_poison','FuchsiaCity_Gym_Text_KogaPostBattle',
    'Koga explains that Toxic poison damage worsens as a battle continues.', '''
N~That is a very unpleasant clock to leave running. We should know where the antidotes are.|
N~Its pressure increases with time. A slow plan needs a way to address that.|
N~Do not ignore a poisoned teammate while waiting for the perfect move.|
N~It makes every extra moment feel expensive. I understand why people find him frightening.|
N~We will look after the team promptly. Nobody should be left hurting because the battle is exciting.|
N~The technique makes delay into an opponent of its own.|
N~A steadily worsening situation. I prefer those in fiction, where I can close the book.|
N~The cost is cumulative. Planning only around the first tick will underestimate it.|
N~A small harm can become a large one when nobody tends it.|
N~I would rather remember the remedy as clearly as the threat.|
N~I will keep watching the team after a battle with that kind of pressure.
''')
add('celadon_erika_giga_drain','CeladonCity_Gym_Text_ExplainTM19',
    'Erika explains Giga Drain heals the user for half the damage inflicted.', '''
U~Hit them and feel better. I have been trying that with pillows and getting much poorer results.|
N~Damage and recovery are linked, so the target and the actual damage both affect the benefit.|
N~Useful staying power. Do not assume it replaces proper healing.|
N~It changes the feeling of an attack when it also gives our teammate a little room to recover.|
N~A helpful move, though the team should still get rest between battles.|
M~The action scene contributes directly to the performer's recovery budget.|
M~An efficient move with a considerably less charming description from the other side.|
N~Recovery scales with output. It will not provide the same return in every matchup.|
N~Taking and restoring meet in one motion. We should use that strength thoughtfully.|
N~I can see why she likes it. It gives a team more than one useful result.|
N~I would watch how much breathing room it actually gives the teammate using it.
''')

add('vermilion_shock_wave_tm','VermilionCity_Gym_Text_ExplainTM34',
    'Surge gives Shock Wave and recommends an Electric Pokemon.', '''
S~A little bottled thunder, with considerably less bottle than I expected.|
N~Check who can learn Shock Wave and whether it improves their present options.|
N~Pick the right teammate before using the TM.|
N~I would like the first demonstration to happen somewhere less full of metal bins.|
N~A useful gift. We should choose who needs it rather than simply who is nearest.|
M~The loud commander has sent us away with a compact version of his favorite noise.|
M~I support keeping the thunder on the team list and out of my pockets.|
N~The recommendation narrows the candidates. Compatibility still needs checking.|
N~A storm can become a lesson when somebody knows how to guide it.|
N~A strong signature move should suit the Pokemon learning it, too.|
S~I like seeing which part of a leader's style they choose to pass on.
''')
add('saffron_calm_mind_tm','SaffronCity_Gym_Text_ExplainTM04',
    'Sabrina explains Calm Mind raises Special Attack and Special Defense.', '''
S~A calmer mind becomes stronger. I would like mine to stop organizing imaginary emergencies first.|
N~The same preparation improves both special offense and special defense. Timing remains important.|
N~Give it a safe turn to prepare. Calm is easier when the plan makes room for it.|
S~I like a move that treats quiet as something powerful.|
N~Taking time to settle can be part of caring for the team, too.|
S~A moment of stillness changes both what the performer can give and what they can withstand.|
S~A battle move that rewards not immediately doing the loudest thing available. Promising.|
N~Two useful properties improve together. Choose someone who benefits from both.|
S~Still water can hold more than the surface suggests.|
S~Composure can protect someone as much as it impresses the room.|
N~I would watch the difference in the next few turns, not only the quiet moment itself.
''')
add('viridian_earthquake_tm','ViridianCity_Gym_Text_ExplainTM26',
    'Giovanni gives Earthquake and recalls making it during his earlier time at the Gym.', '''
N~He made a move that shakes the ground. An unusually literal way to leave a mark on a place.|
N~A powerful technique from an earlier part of his life. We should understand its reach before using it.|
N~A strong gift does not erase what we know about him. Use our own judgment with it.|
N~It is strange hearing him remember a quieter part of his life.|
N~The move is ours to use responsibly now. That choice belongs to us.|
N~An old chapter has survived inside the object he is handing us.|
N~People leave complicated things behind. We do not need to inherit the rest of his choices.|
N~I would check the targeting before a double battle. A broad effect needs careful planning.|
N~The earth carries an old lesson without choosing the person who learns it next.|
N~A gift can be useful without buying forgiveness.|
N~I wonder what he remembers when he thinks of this room before everything else happened.
''')
add('vermilion_guide_warning','VermilionCity_Gym_Text_GymGuyAdvice',
    'The guide warns about Electric matchups, paralysis and Surge locked door.', '''
N~Strong electricity, paralysis, and a locked door. The welcome brochure has become a threat assessment.|
N~Avoid the poor matchups, prepare for paralysis, and solve access separately from the battle.|
N~Check the team's condition and our remedies before starting.|
N~Knowing what can go wrong is better than being surprised by every part of it.|
N~I would like everyone comfortable before we go searching the bins.|
M~A tactical briefing has doubled as a warning about the building's hostility to visitors.|
M~I came prepared for a battle. The rubbish puzzle was an unexpected social obligation.|
N~Type disadvantage, status risk, physical barrier. Three separate problems to prepare for.|
N~A storm and a locked gate ask for different kinds of patience.|
N~The advice helps. I still wish the door were less interested in proving a point.|
N~I would watch how the staff pass through the room before assuming every barrier is obvious.
''')
add('vermilion_guide_victory','VermilionCity_Gym_Text_GymGuyPostVictory',
    'The guide calls the victory electric.', '''
M~Electric! I am choosing to celebrate from a respectful distance from the wiring.|
S~A good result. Let us check the team before enjoying it too loudly.|
S~We did it. Time to get everyone healed.|
S~I can finally stop thinking about where all the electricity might be going.|
S~A win feels better once we know everyone is all right.|
M~The critic has summarized an entire battle in the building's preferred adjective.|
M~A charged review. I am carefully resisting the rest of that joke.|
S~The team passed the test. The doors are somebody else's problem for a while.|
S~The thunder has passed. We can hear ourselves again.|
S~You earned the moment. Let yourself enjoy it before packing for the next one.|
S~His excitement makes it feel like someone was waiting for our good news.
''')
add('fuchsia_guide_invisible_walls','FuchsiaCity_Gym_Text_GymGuyAdvice',
    'The guide explains invisible walls and the need to find gaps to reach Koga.', '''
M~The walls are invisible. I was prepared to be lost, but not aesthetically.|
N~The apparent distance is misleading. We need to map the actual accessible path.|
N~Move slowly and remember what blocks us. Do not keep testing the same wall.|
N~I would like to sketch the route once we understand it.|
N~We can take our time. Nobody needs a bruised nose as part of the challenge.|
M~The leader is visible, the scenery is not, and the audience is expected to applaud the distinction.|
M~A room designed by someone who enjoys watching people apologize to empty air.|
N~Treat the collisions as boundary data. Then trace the gaps.|
N~What we cannot see still changes where we can go.|
N~I prefer a visible obstacle. At least it has the courtesy to announce itself.|
N~I am looking at people's routes rather than the empty-looking spaces.
''')
add('fuchsia_guide_after_victory','FuchsiaCity_Gym_Text_GymGuyPostVictory',
    'The guide remarks that ninjas remain terrifying even now.', '''
M~Terrifying, yes. Also surprisingly committed to inconvenient interior design.|
N~Preparation and concealed information can create an intimidating advantage.|
N~He is skilled. We still found a way through.|
N~I would like the next quiet room to be quiet for less tactical reasons.|
N~Let us make sure the team is well after all those lingering effects.|
M~The ninja has impressed the audience and given the cleaning staff a difficult floor plan.|
M~The frightening part is over. I would now like to discover a chair that is visible.|
N~Good concealment makes the unfamiliar feel more dangerous. Understanding it helped.|
N~A hidden path becomes less frightening once our feet know it.|
N~I can respect the skill while preferring a more straightforward welcome.|
N~I would remember the little signs that helped us find our way despite the fear.
''')
add('saffron_guide_matchup_warning','SaffronCity_Gym_Text_GymGuyAdvice',
    'The guide warns Fighting Pokemon about Sabrina Psychic team.', '''
N~The warning is vivid. Our Fighting teammates would prefer a plan to becoming the example.|
N~That is a poor matchup. We should choose a lead suited to the actual opponent.|
N~Keep the vulnerable teammate out of that situation. There are other ways to use their strength.|
N~I am glad we heard it before somebody had to learn by getting hurt.|
N~A partner can sit out a bad matchup without being less valuable to the team.|
N~A promising action scene has been correctly rejected at the planning stage.|
M~I appreciate advice that arrives before the dramatic mistake rather than after it.|
N~Do not test a known vulnerability just because a teammate is strong in other situations.|
N~A fist need not answer every question.|
N~A good team lets different partners handle the rooms that suit them.|
N~I will watch for what changes when we choose a different kind of approach.
''')
add('saffron_guide_slots_plan','SaffronCity_Gym_Text_GymGuyPostVictory',
    'The guide imagines using psychic powers to win money at slot machines.', '''
M~A miracle of the mind, immediately assigned to improving the coin case.|
M~He has jumped from an untested ability to a projected income. Several steps are missing.|
M~Good thing that is still an imaginary budget.|
N~I wonder whether he would still enjoy the game if the uncertainty disappeared.|
N~I would rather he kept money for the journey than trusted a sudden winning theory.|
M~Human potential has reached the grand vision of a very profitable afternoon indoors.|
M~The future of the mind, apparently managed by the nearest slot machine.|
M~I would not fund the plan until the claimed ability passes a test outside the casino.|
N~A glimpse of possibility does not always tell us what is worth wanting.|
M~It is impressive how quickly wonder can become a shopping list.|
N~I would ask what he would do with that power when there was nobody counting coins.
''')
add('cinnabar_guide_burn_preparation','CinnabarIsland_Gym_Text_GymGuyAdvice',
    'The guide recommends Water attacks and Burn Heals against Blaine.', '''
N~Water for the battle, Burn Heals for the mistakes. A reasonably complete weather forecast.|
N~A useful matchup and a status remedy. We should check quantities before proceeding.|
N~Good advice. Make sure we actually have the remedies he mentioned.|
N~I would rather carry something we never need than wish we had it afterward.|
N~Keeping the team comfortable matters as much as finding a strong attack.|
N~The briefing includes both the action plan and the rather important aftercare.|
M~I have a great deal of respect for advice that includes treating the consequences.|
N~Counter the main hazard and prepare for residual damage. Sensible checklist.|
N~Bring something to soothe the flame as well as something to challenge it.|
N~I like a warning that ends with an actual thing we can do.|
N~We should look after the team between battles instead of letting the excitement rush us onward.
''')
add('cinnabar_guide_victory','CinnabarIsland_Gym_Text_GymGuyPostVictory',
    'The guide celebrates defeating Blaine.', '''
S~The firebrand has been beaten. I would like to celebrate somewhere the air is less enthusiastic.|
S~A successful challenge. Check for lingering burns before we leave.|
S~Good fight. The team has earned recovery, not another immediate test.|
S~It is nice to hear the win said plainly after all that heat.|
S~Let us get everyone comfortable, then find something good to eat.|
S~The fiery main attraction has received its final bow for today.|
M~I am pleased with the victory and ready to stop feeling gently toasted.|
N~The objective is complete. Now inspect the team rather than assuming the damage ended with the match.|
S~The fierce part is over. We can let the warmth become gentle again.|
S~You can enjoy this without immediately searching for a harder thing to prove.|
S~I would keep the team together for a moment before we leave this room behind.
''')
add('viridian_guide_unknown_leader','ViridianCity_Gym_Text_GymGuyAdvice',
    'The guide does not know the leader identity but warns about difficulty and Ground Pokemon.', '''
M~He knows the department, the danger level, and absolutely none of the management.|
N~He separated his uncertainty about the identity from his information about the team. Useful distinction.|
N~Ground Pokemon. Start there, and keep watching what is actually in the room.|
N~I would feel better with an ordinary introduction, but we can prepare without it.|
N~Let us make sure the team is well before meeting someone everyone describes as difficult.|
M~The final local mystery has a tactical briefing but no cast announcement.|
M~Even the adviser has not met the person he is advising us about. Reassuring.|
N~Known specialty, uncertain personnel. Build a flexible plan.|
N~A hidden name still leaves footprints. We can attend to what is here.|
N~I appreciate him saying what he does not know instead of inventing the rest.|
N~I am watching the staff. Their reactions may tell us what the missing name does not.
''')
add('viridian_guide_identity_revealed','ViridianCity_Gym_Text_GymGuyPostVictory',
    'The guide is astonished to learn Giovanni was the leader.', '''
U~The workplace mystery has become a workplace problem.|
N~That is a significant gap in local oversight. I hope the town learns what happened here.|
N~People deserve to know who had that authority over the Gym.|
N~I wonder how many ordinary days happened in this room without anyone knowing.|
N~I hope the people who trusted this place are given clear answers.|
N~The secret identity has escaped the dramatic scene and entered the staff meeting.|
M~I would have several questions for whoever handles hiring.|
N~We should find out how that information remained hidden from the person greeting every challenger.|
N~The room looks the same. Knowing its story makes it different.|
N~Surprise is understandable. Someone still needs to explain what happens next.|
N~I would rather hear what the town needs now than keep replaying the reveal.
''')

add('pewter_tm_bag_full','PewterCity_Gym_Text_DontHaveRoomForThis',
    'Brock cannot give the TM because we lack bag space.', '''
F~We defeated the rocks and were stopped by the contents of a pocket.|
N~The TM has not transferred. We need space before returning.|
N~Sort the bag somewhere safe. We can collect it afterward.|
F~I am glad he is willing to wait while we sort this out.|
N~No need to discard something useful in a hurry. Check the options first.|
M~The victory gift awaits the less celebrated triumph of inventory management.|
M~A whole badge earned, and no room for a very small lesson.|
N~Capacity failed. The reward itself is still available here.|
N~Even a small gift asks for a place to rest.|
N~We can make room thoughtfully instead of abandoning something valuable.|
N~Let us remember to return. It would be easy to leave the gift behind in the excitement.
''')
add('cerulean_tm_bag_full','CeruleanCity_Gym_Text_BetterMakeRoomForThis',
    'Misty asks us to make bag room for her TM.', '''
M~Our bag has resisted Water Pulse without even being a type.|
N~We have not received the TM. Clearing a slot is the next practical step.|
N~We will come back. Check what can be stored or used first.|
F~She sounds certain the gift is worth returning for. I do want to remember it.|
N~Let us find a quiet place to sort things instead of spreading them around the pool.|
M~A promising aquatic lesson has been delayed by a rather terrestrial bag problem.|
M~The real final opponent was the thing I packed just in case.|
N~A capacity limit is not a refusal. The transfer can be retried.|
N~A crowded bag can still be rearranged without losing its journey.|
N~I would rather reorganize properly than throw away the wrong thing to be quick.|
N~We should keep a little space for the next unexpected kindness, too.
''')
add('vermilion_tm_bag_full','VermilionCity_Gym_Text_MakeRoomInYourBag',
    'Surge tells us to clear space before he can give the TM.', '''
F~The commander has discovered our most vulnerable position: packing.|
N~The gift remains here until the bag has capacity for it.|
N~Clear a slot sensibly. Do not turn a small delay into a wasted item.|
F~I would like to sort the bag without everyone watching, please.|
N~Let us step somewhere comfortable and see what actually needs carrying.|
M~A military triumph has encountered a failure in the baggage division.|
M~I fear the inspection of our bag will reveal an alarming quantity of optimism.|
N~An obvious storage constraint. No electrical intervention required.|
N~A full pocket can delay a gift without losing the welcome behind it.|
N~We can return prepared. The bag does not need a dramatic solution.|
N~I would remember where he is waiting before we start the next errand.
''')
add('celadon_tm_bag_full','CeladonCity_Gym_Text_ShouldMakeRoomForThis',
    'Erika asks us to make room before receiving her TM.', '''
F~A garden full of flowers, and somehow the most overgrown thing here is our bag.|
N~The reward has not been received. We should clear space and return.|
N~No hurry. Decide what belongs in storage before removing anything.|
N~She made the correction gently. I appreciate that.|
N~Let us sort what we carry without making a mess of her floor.|
M~The gift waits patiently while our supporting luggage undergoes a much-needed edit.|
M~An elegant refusal from a very inelegantly packed problem.|
N~A little reorganization should resolve the blocked transfer.|
N~We can make a place for something new without casting away something dear.|
N~I knew we needed a better arrangement in that pocket.|
N~It is nice that the offer remains open while we work it out.
''')
add('fuchsia_tm_bag_full','FuchsiaCity_Gym_Text_MakeSpaceForThis',
    'Koga cannot hand over the TM until we have bag space.', '''
M~The secret technique has been defeated by an openly visible packing problem.|
N~The centuries-old technique can wait while we resolve the current storage limit.|
N~Make space, then return. The team deserves care before we sort souvenirs.|
N~I am relieved this obstacle does not require another invisible corridor.|
N~We can handle the bag after checking everyone is well.|
M~The ancient inheritance is briefly suspended pending a mundane administrative correction.|
M~A ninja can hide many things. Apparently not the state of our bag.|
N~The transfer failed cleanly. No need to guess whether we received it.|
N~A secret is still here, waiting for a little room.|
N~I would sort things in good light. We have had enough invisible complications.|
N~Let us remember the unfinished exchange before leaving the town.
''')
add('saffron_tm_bag_full','SaffronCity_Gym_Text_BagFullOfOtherItems',
    'Sabrina cannot give her TM because our bag is full.', '''
M~Can the bag become larger if we concentrate? No? Back to ordinary tidying.|
N~Psychic ability has not removed the capacity constraint. We need a free slot.|
N~Sort the bag. Thinking very hard about it is not the same task.|
F~I hope she cannot also see everything I thought would be useful to pack.|
N~We can make space without rushing. She is still offering the gift.|
M~The mental discipline prize has met the physical consequences of our packing decisions.|
M~My mind is full of possibilities. So, regrettably, is the bag.|
N~We can solve this with ordinary storage. A useful baseline method.|
N~A quiet mind may help us choose what to carry. The choosing still matters.|
N~I would like to reorganize before someone describes the contents out loud.|
N~Let us come back rather than allow a small inconvenience to become a forgotten gift.
''')
add('cinnabar_tm_bag_full','CinnabarIsland_Gym_Text_MakeSpaceForThis',
    'Blaine asks for bag space before giving his TM.', '''
M~No room for Fire Blast. Probably the safest sentence our bag has ever produced.|
N~The TM remains with Blaine. We should make space before attempting the transfer again.|
N~We can collect it after sorting the bag. Heal the team first.|
N~I would prefer to unpack somewhere cooler than this room.|
N~Let us take care of everyone before turning the bag inside out.|
M~The explosive final gift has been postponed by the luggage department.|
M~An entirely nonflammable obstacle. I am almost grateful.|
N~A capacity issue rather than a failed reward. Easy to correct deliberately.|
N~The flame can wait while we find a safe place for its lesson.|
N~A little room and a little order. We can manage that.|
N~We should return before the next destination pulls all our attention away.
''')
add('viridian_tm_bag_full','ViridianCity_Gym_Text_YouDoNotHaveSpace',
    'Giovanni cannot give the TM because we have no bag space.', '''
N~A dramatic victory, followed by the extremely ordinary problem of too much stuff.|
N~We have not received the TM. Its availability and the badge result are separate.|
N~Sort the bag carefully. Do not let the pressure of the room rush the choice.|
N~I would rather think about the bag once we have a quieter place to stand.|
N~The team comes first. We can return for an item after everyone is cared for.|
N~The grand scene has paused for a small but unavoidable logistical fact.|
M~I am relieved to have one problem in this room that can be solved by tidying.|
N~The transfer was blocked before the item changed hands. Keep that distinction clear.|
N~Not every unfinished thing asks to be settled in the same breath.|
N~We can make room without treating any old possession as suddenly worthless.|
N~Let us remember what is unfinished here without forgetting everything we have already done.
''')

