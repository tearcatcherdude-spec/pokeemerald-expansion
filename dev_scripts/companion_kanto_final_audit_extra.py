"""Additional fixed Kanto actor terminals; prior audit modules stay frozen."""
ROWS=[]
EMOTIONS=dict(N='neutral',S='soft_smile',A='annoyed',F='flustered',D='sad',U='surprised',M='smug',L='laughing')
def add(key,labels,subject,lines):
    replies=[]
    for line in lines.strip().split('|'):
        line=line.strip()
        if len(line)>1 and line[1]=='~' and line[0] in EMOTIONS:line=EMOTIONS[line[0]]+line[1:]
        replies.append(line)
    assert len(replies)==11,(key,len(replies))
    ROWS.append(dict(key='kanto_auditx_'+key,labels=labels.split(),subject=subject,replies=replies))

add('roof_expert','CeladonCity_Condominiums_RoofRoom_Text_TheresNothingIDontKnow',
    "A self-proclaimed expert recommends enjoying Pokemon trades with friends.",'''
L~Nothing he does not know? I could probably confuse him with a sufficiently ordinary sandwich.|
N~The trading advice is sensible. The claim of unlimited knowledge is less defensible.|
N~Useful advice can survive a little less boasting.|
S~I like the part about enjoying something with friends.|
S~Shared interests make good reasons to spend an afternoon together.|
M~The authority has announced his expertise and generously allowed the audience to mingle.|
N~Knowing everything would leave a person very little to be curious about.|
S~Trading with friends can turn separate discoveries into a shared project.|
N~A full cup is not always evidence of an endless well.|
S~The confidence is rather large, but the social advice has some charm.|
S~I wonder which question he most enjoys being asked.
''')
add('union_room','CinnabarIsland_PokemonCenter_1F_Text_VisitUnionRoom',
    "A visitor recommends the Union Room as a chance to meet new friends.",'''
S~A room where today's stranger might become tomorrow's familiar wave. That sounds nice.|
S~A shared activity can make meeting unfamiliar people feel more approachable.|
N~We can have a look when we feel like company.|
S~Knowing there is a reason to start talking makes a new room less frightening.|
S~There is room for new friends without making old ones any less important.|
S~The established cast need not be the final cast of the journey.|
S~A meeting place can do some of the awkward introductory work for everyone.|
S~A common interest gives the first conversation something practical to begin with.|
S~An unfamiliar doorway may hold a voice that eventually feels familiar.|
S~A little openness can make a familiar routine feel fresh again.|
S~I wonder what first brings people in, and what makes them return.
''')
add('bill_not_ready','CinnabarIsland_PokemonCenter_1F_Text_OhNotDoneYet',
    "Bill accepts that the player is not ready to leave on the island trip.",'''
S~A trip can wait while the unfinished things stop waving at us from the doorstep.|
N~Deferring departure allows existing plans to be completed before adding another journey.|
N~We will go when we are ready. Good that he understands.|
S~It is easier to enjoy an invitation when there is room to finish saying goodbye first.|
N~A little time to prepare can make the actual trip much smoother.|
S~The next chapter has agreed to wait for the loose ends to be tied.|
S~An invitation is kinder when it does not become a countdown.|
N~We can check the team and supplies before choosing to depart.|
S~A waiting boat need not make every other task suddenly urgent.|
S~It is nice when someone hears not yet as a real answer.|
S~I wonder which last errand we will remember just before we finally set off.
''')
add('fossil_no','CinnabarIsland_PokemonLab_ExperimentRoom_Text_NoIsTooBad',
    "The fossil researcher is disappointed when the player declines the offer.",'''
N~The scientist has discovered that enthusiasm is not a substitute for permission.|
N~A declined offer remains a valid choice, even when the researcher is disappointed.|
N~No is enough. We need not make the experiment happen today.|
N~It is all right to leave something unusual undecided for a while.|
N~A curious opportunity deserves thought rather than being accepted to avoid awkwardness.|
N~The proposed marvel has encountered the entirely ordinary right to decline.|
N~A disappointing answer is still an answer, not a research obstacle to overcome.|
N~We can return if the proposal fits our plans later.|
N~Some doors can remain closed without being lost forever.|
N~His disappointment does not need to become our responsibility.|
N~I wonder whether he hears many refusals with an offer that unusual.
''')
add('dark_tunnel','DiglettsCave_NorthEntrance_RockTunnelPitchBlack',
    "A traveller found Rock Tunnel dark and frightening and wishes for Flash.",'''
N~A tunnel is much less inviting when the dark seems to have arrived before you.|
N~Limited visibility makes navigation and identifying hazards substantially harder.|
N~Get a reliable way to see before entering. No need to stumble through.|
N~I understand feeling frightened when you cannot tell what the next sound belongs to.|
N~Preparing for the darkness is better than hoping nerves will do the lighting.|
N~The traveller has delivered an unusually persuasive review of inadequate illumination.|
N~Darkness is quite capable of making an ordinary rock feel personally ominous.|
N~A light source turns many frightening unknowns back into manageable terrain.|
N~An unseen path asks too much trust from a tired pair of feet.|
N~There is nothing embarrassing about wanting to see where you are going.|
N~I wonder how far into the tunnel the traveller got before deciding to turn back.
''')
add('sticker_repeat','FourIsland_House2_Text_ComeBackWithBetterStoryEggs FourIsland_House2_Text_ComeBackWithBetterStoryHoF FourIsland_House2_Text_ComeBackWithBetterStoryLinkWins',
    "The sticker collector asks for a new achievement rather than hearing the same record again.",'''
N~The sticker economy requires fresh bragging material. Repeats do not pass inspection.|
N~The claimed achievement has not increased beyond the record already recognized.|
N~Nothing new for him to reward. We can leave it there.|
N~An old achievement still matters even when it no longer earns another sticker.|
N~We need not turn every good memory into a fresh transaction.|
S~The audience has requested new material before issuing another review sticker.|
N~A familiar triumph has become yesterday's news in a remarkably tiny awards office.|
N~A one-time reward system needs to distinguish a new record from a repeated claim.|
N~Yesterday's bright thing does not dim because today's drawer stays shut.|
N~He could ask for an update with a little less dismissal of what came before.|
N~I wonder whether he enjoys the stories or handing out recognition more.
''')
add('sticker_legend','FourIsland_House2_Text_LivingLegendEggs FourIsland_House2_Text_LivingLegendHoF FourIsland_House2_Text_LivingLegendLinkWins',
    "The sticker collector calls the player a living legend and has no further stickers to offer.",'''
L~We have outgrown the available sticker supply. A very specific sort of fame.|
S~The reward scheme has reached its upper limit; the achievement exceeds any remaining award.|
S~No more prizes needed. The work still happened.|
F~Living legend is a very large phrase to be handed in such a small room.|
S~It is all right for a milestone to stand on its own without another prize.|
S~The awards committee has exhausted its stationery and resorted to extravagant acclaim.|
S~A career has become too large for its designated decorative label.|
S~A reward system can end without making further achievements meaningless.|
S~The small drawer is empty; the story has not become smaller to fit it.|
S~There is something charming about running out of decoration before running out of admiration.|
S~I wonder how many people have ever reached the end of his sticker collection.
''')
add('sticker_offer','FourIsland_House2_Text_BragAboutSomethingForMe FourIsland_House2_Text_GiveYouStickerIfYouBrag',
    "The sticker collector invites a future story about something the player has accomplished.",'''
S~A man has built a tiny awards ceremony out of wanting to hear people boast.|
S~The offer establishes a future reward, not an achievement already verified today.|
N~We can come back with a real accomplishment. No need to invent one.|
S~It is an unusual way of inviting someone to talk about what they are proud of.|
S~A little recognition can make someone want to share a good story.|
S~A willing audience and adhesive applause. The arrangement has a certain elegance.|
S~Bragging has found a very modest patron of the arts.|
N~We should understand what he counts before making the reward the goal.|
S~A small bright square is waiting for a story worth carrying.|
S~He clearly enjoys giving people a reason to talk about themselves.|
S~I wonder which tale he would enjoy even if there were no sticker left to give.
''')
add('journal_delay','FourIsland_PokemonCenter_1F_Text_NewPokemonJournalHasntArrived',
    "A reader is surprised that the newest Pokemon Journal has not reached Four Island.",'''
N~The latest news has apparently decided to take a slower boat.|
N~Distribution delays are more noticeable when a reader is expecting a regular arrival.|
N~It will arrive when it arrives. No reason to blame the people here.|
S~Waiting for the next issue can make a small delay feel strangely long.|
S~There is a particular disappointment in looking for something familiar and finding an empty place.|
S~The devoted audience has encountered an unscheduled gap in publication.|
N~The island is being made to practise patience by the postal schedule.|
N~Distance makes a regular delivery schedule harder to keep perfectly even.|
N~News travels less quickly than the wish to read it.|
S~The surprise tells me the journal is a real part of this reader's routine.|
S~I wonder what feature they were most looking forward to reading.
''')
add('indigo_agatha','IndigoPlateau_PokemonCenter_1F_Text_AgathaWhuppedUs',
    "A defeated challenger explains that a powerful Fighting team was not enough against Agatha.",'''
N~All that muscle met a problem it could not solve by being more muscle.|
N~The result illustrates why strength alone cannot replace attention to type interactions.|
N~A hard lesson. Adjust the plan instead of only pushing the same team harder.|
N~It sounds rough to arrive that confident and leave so shaken.|
N~Preparation includes knowing what the team will struggle to handle.|
N~A carefully trained cast has discovered that the script asks for a different approach.|
N~Confidence had an unpleasant appointment with a mismatch.|
N~Review the matchup before adding more effort to the same plan.|
N~Force can meet a door that opens only to a different question.|
N~Blaming Agatha's temper will not do much to repair the battle plan.|
N~I wonder which moment made the challenger realize the expected advantage was not there.
''')
add('indigo_cousin','IndigoPlateau_PokemonCenter_1F_Text_LancesCousinGymLeaderFarAway',
    "A visitor has heard that Lance has a cousin who leads a distant Gym.",'''
S~An impressive family anecdote, though I expect both cousins have done a fair bit of work.|
N~A family connection does not establish that skill is inherited rather than developed.|
N~A strong relative does not do the training for you.|
S~I wonder whether they get to talk about ordinary things when they meet.|
S~A family can share an interest without every accomplishment coming from the same place.|
S~The rumour has supplied a distant relative and immediately drafted a theory of greatness.|
N~A bloodline is a very tidy explanation for something that usually takes untidy effort.|
N~Shared background could matter, but it would not tell us the whole story.|
N~Two strong branches do not show us all the weather the tree endured.|
N~I would rather hear about their work than reduce them both to a surname.|
S~I wonder which of them first made the other interested in serious battling.
''')
add('nugget_value','Route10_PokemonCenter_1F_Text_NuggetUselessSoldFor5000',
    "A traveller sold a Nugget for five thousand because it had no practical use to them.",'''
L~A useless thing that becomes five thousand coins has discovered a rather useful second career.|
S~Utility depends on context. A valuable material need not have a direct travelling use.|
S~Sold something unnecessary for money they could use. Sensible enough.|
N~It is funny how a thing can mean nothing to one person and quite a lot to another.|
S~That could buy a very respectable amount of travelling supplies.|
S~The allegedly useless object has financed the next chapter admirably.|
S~A little gold has declined employment as a burden and applied to become money instead.|
S~Converting an unused resource into something practical is a sound choice.|
S~Value sometimes lives in what a thing can become rather than what it does in your hand.|
S~Knowing what you actually need is better than carrying something simply because it shines.|
S~I wonder whether the traveller already knows what they want to spend it on.
''')
add('type_advice','Route10_PokemonCenter_1F_Text_EveryTypeStrongerThanOthers',
    "A trainer explains that Pokemon types have different matchup strengths and weaknesses.",'''
N~There is usually another side to the type chart waiting to spoil a confident grin.|
N~Matchups depend on the specific types involved; no single broad advantage answers every situation.|
N~Know the opponent before assuming the matchup favours us.|
N~It helps to remember that a difficult match is not proof the team is bad.|
N~A different approach can help more than insisting on the same advantage.|
N~The strongest-looking entrance can still meet an awkwardly chosen opponent.|
N~A useful reminder that superiority rarely remains universal for long.|
N~Coverage and alternatives make a team less dependent on one favourable matchup.|
N~Every familiar strength casts a shape that something else can step around.|
N~Good advice, provided we keep room for the exceptions in an actual matchup.|
S~I wonder which unexpected type interaction first made the lesson stick.
''')
add('lavender_rumour','Route10_PokemonCenter_1F_Text_HeardGhostsHauntLavender',
    "A traveller repeats a rumour that ghosts haunt Lavender Town.",'''
N~A town can collect a lot of spooky introductions before you have even reached its sign.|
N~That is a report of a rumour, not direct evidence about what we will encounter.|
N~We can see for ourselves and treat the people there respectfully.|
N~I hope the rumour does not make visitors forget it is somebody's home.|
N~A place deserves more than being treated as a frightening story over lunch.|
S~The town's reputation has arrived ahead of the town itself.|
S~A haunting is a very efficient way for a place to occupy people's imaginations.|
N~We should distinguish what people have seen from what they have heard repeated.|
N~Some places carry both grief and stories. Best not mistake one for entertainment.|
N~Curiosity travels better when it brings decent manners with it.|
S~I wonder who first told the story and what they were actually trying to describe.
''')
add('gate_effort','Route16_NorthEntrance_1F_Text_HowdYouGetInGoodEffort',
    "A gate visitor is surprised and impressed that the player found a way in.",'''
S~We have earned a small compliment for the sophisticated technique of getting here.|
S~The surprise suggests the approach is less obvious than the destination makes it look.|
S~We found the way. Nice that someone noticed.|
S~It is a small thing, but being recognized for figuring it out feels good.|
S~Sometimes arriving is an accomplishment before anything else happens.|
S~The entrance has received a favourable review from its accidental audience.|
S~A little recognition for the journey instead of only the destination.|
S~An indirect route can reward a bit of practical problem-solving.|
S~A threshold can mark more effort than the room beyond it suggests.|
S~An honest, surprised compliment can be rather charming.|
S~I wonder how many travellers miss the approach entirely.
''')
add('misty_coast','Route20_Text_MistyTrainsHere',
    "A local says strong Water teams gather here and that Misty trains in the area.",'''
S~A good seaside training spot apparently has a reputation among people with very splashy teams.|
S~Suitable habitats can attract both particular Pokemon and trainers specializing in them.|
N~A useful warning about the sort of matches we may meet.|
S~It is nice to imagine her having a familiar place to practise away from the Gym.|
N~Worth preparing for Water teams before choosing challenges along this coast.|
S~The stretch of sea has secured a distinguished professional endorsement.|
S~A place can acquire character from the people who keep returning to it.|
N~The terrain makes it sensible to anticipate Water specialists here.|
S~A shoreline holds its regular visitors as well as its tides.|
S~I like hearing about the work behind a Gym Leader's polished public role.|
S~I wonder which part of the coast she finds best for training.
''')
add('cape_misty','Route25_Text_MistyHighHopesAboutThisPlace',
    "A local describes the cape as a date spot and says Misty has hopes for it.",'''
S~The cape has a reputation for romance and apparently a very optimistic local supporter.|
N~Its reputation tells us how people use the place, not what every visitor must want from it.|
N~A pleasant view works fine without anyone arranging our plans.|
F~It does seem like the sort of place people might remember visiting together.|
S~A good place can give people a reason to linger after the walk.|
S~The scenery has been confidently assigned a romantic genre.|
S~A quiet view has somehow become responsible for several people's expectations.|
S~A welcoming spot can serve plenty of purposes beyond its advertised one.|
S~The water does not mind whether the people watching it arrived as a pair.|
S~A little local hope can make a place feel fondly looked after.|
S~I wonder which ordinary detail makes the cape memorable to the people who return.
''')
add('cape_alone','Route25_Text_AreYouHereAlone',
    "A man assumes the cape should only be visited as a couple.",'''
N~The cape has not asked us for a second ticket to enjoy the view.|
N~A reputation as a date spot does not exclude other perfectly valid reasons to visit.|
N~We can be here however we like. It is a view, not a requirement.|
N~Sometimes a quiet walk is exactly the company a person wants.|
N~There is nothing wrong with enjoying a pleasant place on your own terms.|
N~The self-appointed curator has mistaken a popular genre for an admission rule.|
N~A solitary visitor is not a failed couple. Remarkable that this needs saying.|
N~A place can support more than one use without needing redesign.|
N~The sea has no particular opinion about how many people arrive together.|
N~A friendly question becomes less friendly when it tells us which answer is acceptable.|
N~I would rather ask what someone likes about the cape than whether they came correctly.
''')
add('bill_collection','Route25_SeaCottage_Text_CheckOutRareMonsOnPC',
    "Bill invites the player to view his rare Pokemon collection on the PC.",'''
S~Bill has reached the delighted host stage of showing us his favourite things.|
S~A collection can be especially informative when its curator explains what makes each entry notable.|
S~A generous invitation. We can take a look when we like.|
S~It is sweet how pleased he is to share the interest itself.|
S~Somebody happily showing you a collection can make a short visit stretch pleasantly.|
S~The curator has opened the private exhibition to a very small visiting audience.|
S~Enthusiasm is often more interesting than the impressive thing it is pointing at.|
S~I would enjoy comparing the details Bill considers unusual.|
S~A person's favourite things make little windows into how they see the world.|
S~The collection matters to him, and he trusts a visitor enough to share it.|
S~I wonder which entry he would choose first if we asked him to explain just one.
''')
add('bill_ticket','Route25_SeaCottage_Text_SSAnnePartyYouGoInstead',
    "Bill prefers research to a party and invites the player to enjoy the S.S. Anne in his place.",'''
S~He has found the elegant solution of not attending the party he does not want to attend.|
S~He recognizes his own preference and offers the opportunity to someone who may enjoy it more.|
S~Fair arrangement. He can keep working while we decide about the ship.|
S~I appreciate someone admitting a party is not where he would rather be.|
S~A good invitation does not have to be enjoyed by the person who first received it.|
S~The reluctant guest has delegated his society appearance with admirable efficiency.|
S~A party avoided can be an excellent evening, from a certain point of view.|
S~Different people can find the same opportunity useful in entirely different ways.|
S~One person's unwanted crowd becomes another person's open doorway.|
S~Knowing what suits you is rather more appealing than attending out of obligation.|
S~I wonder whether Bill feels relieved the moment somebody else agrees to consider it.
''')
add('magikarp_refund','Route4_PokemonCenter_1F_Text_IDontGiveRefunds',
    "The Magikarp seller firmly refuses refunds after the sale.",'''
N~The salesman's friendliness has developed a very abrupt financial boundary.|
N~The statement establishes his refund policy, not whether the purchase was good value.|
N~The sale is done. The Pokemon still deserves proper care.|
N~I hope any frustration stays with the seller rather than the Magikarp.|
N~A living companion should not become the target of buyer's regret.|
N~The promotional warmth has ended precisely where the money changed hands.|
N~A remarkably brisk closing of the door behind the customer.|
N~We can learn from the transaction without treating the Pokemon as a faulty component.|
N~An awkward bargain has still brought a life within our care.|
N~A clear policy would have looked better before the persuasive speech.|
N~I wonder how differently he sounds when the next customer walks up.
''')
add('magikarp_decline','Route4_PokemonCenter_1F_Text_OnlyDoingThisAsFavorToYou',
    "The Magikarp seller claims a declined sale was a special favour.",'''
N~A favour that comes with a price and protests when declined is doing some suspicious stretching.|
N~Describing a transaction as a favour does not establish that it benefits the buyer.|
A~We declined. His sales pitch does not get to turn that into a debt.|
N~I dislike being asked to feel guilty for deciding not to buy something.|
N~A real kindness should survive the other person not wanting it.|
N~The merchant has dressed the invoice as generosity and demanded applause.|
N~An unaccepted bargain has wounded a very commercial sort of benevolence.|
N~We should judge the offer by its actual terms rather than the seller's chosen label.|
N~A gift-shaped shadow does not make the coin in his hand disappear.|
A~How tiresome to make refusing a purchase sound like rejecting someone's kindness.|
N~I wonder how many travellers hear that same supposedly personal favour.
''')
add('rocket_news','Route4_PokemonCenter_1F_Text_TeamRocketAttacksCerulean',
    "A reader is troubled by reports of Rocket attacks on Cerulean residents.",'''
N~That is not the sort of familiar face anybody wants appearing in the news every day.|
N~Repeated reports suggest a serious ongoing problem, though this reader is citing the news.|
N~People should be able to live there without being threatened.|
N~It must be tiring to keep seeing your town described through what is hurting it.|
N~I hope the residents have people nearby they can rely on.|
N~A repeated headline can become familiar without becoming any less ugly.|
N~The city deserves ordinary days that nobody needs to report.|
N~Worth taking care as we approach rather than treating it as a distant story.|
N~Newsprint carries an event lightly compared with the people who lived it.|
N~Concern is a better response than treating the trouble as local colour.|
N~I wonder which details never make it into the short newspaper account.
''')
add('lance_fan','SaffronCity_Text_HowCanClubNotRecognizeLance',
    "A Lance admirer is frustrated that the fan club does not share their enthusiasm.",'''
S~This fan has brought enough enthusiasm for the whole club and is annoyed about doing all the carrying.|
N~Admiration is personal. The other members are not obliged to rank the same traits highest.|
N~They can like Lance without starting an argument about everyone else's choice.|
N~It can feel lonely when nobody shares an interest that means a lot to you.|
N~Enthusiasm is easier to share when it is not served as a correction.|
S~The passionate critic has declared the rest of the audience unqualified to appreciate the star.|
N~A fan club can contain the astonishing complication of more than one favourite.|
N~Explaining what they admire may work better than insisting the others lack judgment.|
N~A bright devotion need not put out the lamps beside it.|
N~The affection for Lance is charming; the contempt for the club rather less so.|
S~I wonder what Lance did that made this fan feel so strongly about him.
''')
add('dojo_greedy','SaffronCity_Dojo_Text_BetterNotGetGreedy',
    "The Dojo master reminds the player not to take a second prize Pokemon.",'''
N~One generous offer does not turn the rest of the room into a take-home display.|
N~The original offer covered one choice. The remaining Pokemon was not included.|
N~We made our choice. Respect the limit.|
N~A gift should not make someone feel they must give everything else, too.|
N~Accepting something kindly includes knowing when to stop asking.|
N~The awards ceremony has ended before the winner can annex the remaining cast.|
N~Gratitude looks better when it leaves something on the table.|
N~A clear limit keeps the original agreement from expanding after the fact.|
N~An open hand need not empty itself to prove it was generous.|
N~He should not have to defend the other gift after making the first.|
N~I wonder how often a generous offer gets mistaken for an unlimited one.
''')
add('ruin_discovery','SixIsland_RuinValley_Text_IFoundThisPlace',
    "The Ruin Valley researcher claims discovery of the site.",'''
N~He found the place. I suspect the stones had already noticed they were here.|
N~Locating a site and establishing its history are different kinds of knowledge.|
N~His discovery does not make the place his property.|
N~I understand being excited to find something before you have the words to explain it.|
N~A discovery deserves care before it deserves a victory speech.|
S~The explorer has announced his claim to the opening credit.|
N~An old place has become new to one person and immediately acquired an ownership problem.|
N~Record the find carefully before letting excitement outrun the evidence.|
N~The first person to name a threshold is rarely the first life to cross it.|
N~Pride in noticing something is better than pretending it began with you.|
S~I wonder what first caught his eye about this particular site.
''')
add('slowbro_attention','CeruleanCity_Text_SlowbroPayAttention',
    "A trainer asks Slowbro to pay attention after it fails to follow a command.",'''
N~The instruction arrived, but Slowbro appears to have left its attention somewhere else.|
N~A failed response can have several causes. Repeating the demand alone may not resolve it.|
N~Try a calmer approach before raising the voice.|
N~I wonder whether the trainer is noticing what Slowbro actually responds to.|
N~A little patience might do more than another sharp instruction.|
N~The intended scene has stalled because one performer is considering a different production.|
N~Attention is an awkward thing to command by sounding increasingly annoyed.|
N~Check whether the instruction is understood rather than simply increasing the volume.|
N~Two lives are standing close while their thoughts remain rather far apart.|
N~Frustration is understandable, but it is not an explanation Slowbro can follow.|
N~I would watch what happens before the missed cue as carefully as what happens after.
''')
add('slowbro_blame','CeruleanCity_Text_NoYouBlewItAgain',
    "A trainer sharply blames Slowbro after another failed instruction.",'''
N~That sentence has a lot of blame and not much help packed inside it.|
N~Naming failure does not identify its cause or show the Pokemon how to respond differently.|
A~Blaming Slowbro again will not make the instruction clearer.|
N~It is hard to learn when every mistake arrives with that voice attached.|
N~A calmer reset would be more useful than serving the disappointment back at it.|
N~The director has announced the failed take without offering any direction.|
N~Again is a heavy little word to keep dropping on someone.|
N~Change the approach and observe the result before repeating the same criticism.|
N~A repeated sharp word can become the only thing a companion learns to expect.|
N~It would look better to ask what went wrong than announce whose fault it was.|
N~I wonder whether the trainer has ever tried a cue that matters to Slowbro.
''')
add('warden_yes','FuchsiaCity_WardensHouse_Text_AhHowheeHoHoo',
    "The toothless Warden gives an excited but unintelligible response after the player agrees.",'''
N~I caught the enthusiasm. The actual words have escaped through a different door.|
N~His articulation makes the response difficult to interpret. We should not pretend to have a translation.|
N~Let him finish. Not understanding is no reason to laugh at him.|
N~He sounds eager to be understood. That makes the missing words feel more frustrating.|
N~A bit of patience is more useful than nodding confidently at something we did not catch.|
N~The emotion is legible, even if the dialogue is temporarily unavailable.|
N~There is a person trying quite hard behind the incomprehensible syllables.|
N~Gestures or a written note might help where spoken words are not getting through.|
N~A voice can carry intent even when the shape of the message is missing.|
N~We can be honest about not understanding without making him feel foolish.|
N~I would look at his expression before deciding what that answer means.
''')
add('warden_no','FuchsiaCity_WardensHouse_Text_HeOhayHeHaHoo',
    "The toothless Warden responds in frustration after the player declines.",'''
N~We are having the sort of conversation where everybody has words and nobody has the same words.|
N~The response remains unintelligible. Inferring detailed instructions would be unwarranted.|
N~He is struggling to explain. Give him a moment.|
N~It must feel awful to know exactly what you mean and have nobody else catch it.|
N~Maybe a gesture or something to write with would make the exchange easier.|
N~The communication problem has survived the attempted answer quite intact.|
N~A misunderstanding is much less funny from inside the person it keeps happening to.|
N~We need another way to exchange information rather than more guesses.|
N~The message keeps reaching the edge of the mouth and losing its shape.|
N~An awkward conversation still deserves decent manners from everyone in it.|
N~I wonder what simple detail would let us stop guessing at what he needs.
''')
add('aide_decline','Aide_Text_GetEnoughMonsComeBackForItem',
    "Oak's aide invites the player to return once the research requirement is met.",'''
N~An errand with a research condition. We know what to work toward before returning.|
N~The reward is conditional on a measured collection milestone, not merely accepting the offer.|
N~We can come back when the requirement is met.|
N~A clear goal makes the next visit feel less uncertain.|
N~We can fit the research into the journey instead of rushing it for a prize.|
N~The professor's assistant has supplied a future appointment with a measurable entrance condition.|
N~An unfinished task has been given a rather practical bookmark.|
N~We can compare the required milestone with the actual record before returning.|
N~The next step is out on the road rather than in this conversation.|
N~A straightforward explanation keeps a delayed reward from feeling arbitrary.|
S~I wonder how many travellers have made this promise and arrived back proudly later.
''')
add('aide_short','Aide_Text_HaventCaughtEnoughMonsForItem',
    "Oak's aide checks the Pokedex and finds the reward requirement is not yet met.",'''
N~The notebook has been inspected and asked to grow a little more before payday.|
N~The measured record remains below the stated threshold. The check has not awarded the item.|
N~Not enough yet. We can keep exploring and return later.|
N~It is a little disappointing, but at least the goal is something we can understand.|
N~No need to turn the next few encounters into a frantic shopping list.|
N~The progress report has found the right direction and an unfinished distance.|
N~Not yet is a smaller word than never, even if it is inconvenient today.|
N~We know the remaining gap exists without needing to guess at the hidden criteria.|
N~An empty place in the record can still be an invitation rather than a reproach.|
N~The aide can be precise without making the shortfall a judgment of us.|
N~I wonder which next discovery will make the return visit feel different.
''')
add('aide_room','Aide_Text_DontHaveAnyRoomForItem',
    "Oak's aide cannot give the promised reward because the Bag has no room.",'''
N~We have managed the research and been defeated by the luggage.|
N~The reward condition is distinct from the capacity condition; the handover has not completed.|
N~Make room before asking for the item again.|
N~An awkward delay after the harder part was already done.|
N~A little sorting can make the next visit much less frustrating.|
N~The accomplished researcher has encountered a stern review of their packing.|
N~Even a deserved prize needs somewhere physical to go.|
N~Capacity is a separate practical constraint. We can resolve it directly.|
N~A full bag can close a very small door at an inconvenient moment.|
N~Better to notice now than pretend the reward somehow fitted.|
N~I wonder what has been sitting untouched at the bottom of that Bag.
''')
add('coin_case_missing','CeladonCity_GameCorner_PrizeRoom_Text_CoinCaseRequired',
    "The prize clerk requires a Coin Case before an exchange can begin.",'''
N~The prize counter has a prerequisite before it has a conversation about prizes.|
N~A Coin Case is the specified access requirement for the exchange service.|
N~We need the case first. No exchange happened.|
N~At least the missing requirement is clear.|
N~We can sort the practical part before getting attached to a particular prize.|
N~The glittering display has been interrupted by a very ordinary equipment check.|
N~An exciting reward can still come with distinctly unexciting preliminaries.|
N~We should gather the required equipment before planning the exchange.|
N~The counter has drawn its first small boundary around an absent object.|
N~A direct explanation is easier to work with than a vague refusal.|
N~I wonder how often the clerk has to stop an enthusiastic visitor at that first step.
''')
add('coin_case_bag','CeladonCity_Restaurant_Text_MakeRoomForThis',
    "The restaurant patron asks for Bag space before handing over his Coin Case.",'''
N~A man trying to part with something has discovered our Bag is not cooperating.|
N~His offer cannot complete until the item has space in the Bag.|
N~Clear some room, then return. He has not given it yet.|
N~I hope the delay does not make the conversation feel more awkward for him.|
N~A practical bit of sorting will let the offer proceed without fuss.|
N~The proposed transfer of a small regrettable legacy has stalled at the luggage.|
N~A fresh beginning has been briefly obstructed by an overfull pocket.|
N~The capacity problem is ours to fix before the handover can happen.|
N~He is ready to let something go; we need to be ready to carry it.|
N~We can make room without making him repeat the whole story.|
N~I wonder whether handing it over will feel like relief when the practical part is done.
''')
add('grunt_return_bag','CeruleanCity_Text_MakeRoomForThisCantRun',
    "The defeated Rocket cannot leave until there is space to return the stolen TM.",'''
M~He has found the one escape route that leads directly through our untidy Bag.|
N~The attempted restitution has not completed because the item cannot fit.|
N~Make room. He still needs to return what he stole.|
N~His impatience does not make the missing item any less important.|
N~We can sort the Bag without pretending he has already put things right.|
M~The fleeing criminal has been detained by a remarkably domestic obstacle.|
N~A man in a hurry has become dependent on somebody else's packing habits.|
N~A free slot resolves the handover problem. His desire to leave is secondary.|
N~A stolen thing waits at the narrow mouth of an overfull bag.|
N~His predicament would be easier to sympathize with if he had not stolen the TM.|
N~I wonder how much longer he imagined this encounter lasting before he met the capacity problem.
''')
add('karp_capacity','Route4_PokemonCenter_1F_Text_NoRoomForMorePokemon',
    "The Magikarp seller cannot complete the sale because the party has no room.",'''
N~Even the enthusiastic salesman has run out of room to keep the pitch moving.|
N~The transaction has encountered the party-capacity requirement before completion.|
N~No room, no sale. We can decide later whether to return.|
N~A pause gives us time to think beyond the salesman's urgency.|
N~We should choose responsibly rather than rearrange the team just to keep the pitch going.|
N~The commercial momentum has been stopped by an unexpectedly full cast list.|
N~A small administrative interruption can rescue a decision from a very fast talker.|
N~The capacity check does not tell us whether the purchase is worth making.|
N~An unopened place in the journey remains unopened for now.|
N~We do not have to solve the seller's problem simply because he wants a sale.|
N~I wonder how differently the offer will feel after we step away for a moment.
''')
add('karp_money','Route4_PokemonCenter_1F_Text_YoullNeedMoreMoney',
    "The Magikarp seller refuses the sale because the player lacks the asking price.",'''
N~The special favour has a very firm minimum price attached to it.|
N~The stated payment condition is unmet, so the sale has not completed.|
N~We cannot afford it now. No reason to rush into finding the money.|
N~It might be useful to think about whether we wanted the purchase or just felt pushed.|
N~Keeping money for travelling needs is a fair reason to walk away.|
N~The generous-sounding pitch has returned abruptly to its central concern.|
N~A salesman has discovered the limits of persuading an empty pocket.|
N~We should assess the value of the offer before treating the shortfall as a problem to solve.|
N~An empty purse has said no more firmly than the conversation did.|
N~A price is clearer than all the talk about doing us a favour.|
N~I wonder how often the prospect sounds less urgent once the traveller has left the counter.
''')
add('ship_departed','VermilionCity_Text_TheShipSetSail',
    "The harbour sailor explains that the ship has already sailed.",'''
N~The harbour has reached the part of the story where the ship is elsewhere.|
N~The response confirms departure rather than offering a current boarding option.|
N~It has gone. We can make another plan.|
N~An empty berth can feel oddly final when you came expecting a ship.|
N~We can check the other travel options before spending the day waiting here.|
N~The setting has retained the dock and removed the principal attraction.|
N~Ships are inconsiderately committed to leaving once they have set sail.|
N~We need current transport information rather than relying on the earlier schedule.|
N~The water has closed the space where a departure used to be.|
N~A clear answer is kinder than letting visitors keep hoping at the gate.|
S~I wonder what the harbour feels like on the morning the ship arrives again.
''')
add('ship_welcome','VermilionCity_Text_WelcomeToTheSSAnne',
    "A harbour sailor welcomes the player to the S.S. Anne.",'''
S~A proper shipboard welcome. I feel slightly more nautical already.|
S~A clear welcome helps a visitor know they have reached the correct entrance.|
S~Friendly start. We can take our time looking around.|
S~It is nice when someone makes a large unfamiliar place feel easy to enter.|
S~A warm greeting does a lot before the visit has even begun.|
S~The voyage's grand venue has appointed a pleasantly direct welcoming voice.|
S~A little courtesy makes a threshold much less imposing.|
S~Knowing where to begin saves wandering around the dock uncertainly.|
S~A welcome can make a large hull feel briefly like a familiar doorway.|
S~Simple hospitality suits a busy entrance rather well.|
S~I wonder how many different journeys arrive at this same greeting.
''')
add('harbour_sighting','VermilionCity_Text_DidYouSeeSSAnneInHarbor',
    "A local asks whether the player has noticed the S.S. Anne in the harbour.",'''
S~A ship large enough to become the neighbourhood's favourite opening question.|
S~A prominent visitor can become a shared point of interest throughout a port.|
S~Hard to blame the interest. It is quite a sight.|
S~I like hearing people sound pleased about something arriving in their own town.|
S~A busy harbour must have a different sort of energy while the ship is here.|
S~The town has acquired an impressive guest and an immediate conversation starter.|
S~A familiar place can still be surprised by what comes to rest beside it.|
S~A large ship brings plenty of interesting movement into an ordinary dockside day.|
S~The horizon has delivered something the whole town can point toward.|
S~Shared excitement makes an ordinary local question rather charming.|
S~I wonder which part of its arrival the people here look forward to most.
''')
add('trade_growth','Trade_Text_HasTradedMonGrownStronger',
    "A former trading partner asks whether the Pokemon they traded away has grown stronger.",'''
S~The trade did not make them stop wondering how their old companion is doing.|
S~A follow-up question shows continuing interest beyond the completed exchange.|
S~They still care about the Pokemon. Good to hear.|
S~It feels kind to remember the life that left with somebody else.|
S~A handover does not have to end all interest in what happens afterward.|
S~The former supporting character has requested news of an old cast member.|
S~An exchange can finish while a small thread of concern remains.|
S~We could describe actual progress without inventing improvements to be polite.|
S~A familiar life has travelled away, but not entirely out of mind.|
S~I like that the question is about the Pokemon rather than whether the deal was clever.|
S~I wonder what little detail they would be happiest to hear about.
''')
add('trade_decline','Trade_Text_WellIfYouDontWantTo Trade_Text_AwwOhWell Trade_Text_ThatsTooBad',
    "A prospective trading partner accepts that the player does not want the exchange.",'''
N~The trade has stayed an offer instead of becoming an argument. Good.|
N~A fair exchange requires willing agreement from both trainers. That condition was not met.|
N~We can decline. No Pokemon needs to change hands.|
N~A little disappointment is all right if the choice is still respected.|
N~Better to keep the team we want than accept something to avoid an awkward moment.|
N~The proposed cast exchange has been cancelled without requiring a second act.|
N~An unwelcome deal is allowed to remain an unfinished sentence.|
N~We can consider future trades separately from this decision.|
N~Two roads may meet without exchanging the lives that travel them.|
N~An accepted refusal is the most important courtesy in a negotiation.|
N~I wonder how long they have been looking for a suitable willing partner.
''')
add('trade_thanks','Trade_Text_Thanks Trade_Text_HeyThanks Trade_Text_ThanksYoureAPal',
    "A trading partner thanks the player after a completed Pokemon exchange.",'''
S~A new chapter on both sides of a very small handshake.|
S~The gratitude closes the exchange after the trade sequence has completed.|
S~Deal settled. Time to get to know the new companion properly.|
S~A simple thank-you makes the handover feel a little warmer.|
S~The real part begins with caring for the Pokemon after the excitement of trading.|
S~The exchange has concluded with a short and entirely satisfactory curtain call.|
S~Two little journeys have changed direction with surprisingly few words.|
S~Now we can learn how the new team member fits our actual plans.|
S~A familiar path has been offered a new pair of footsteps.|
S~A pleasant ending to the arrangement is a good beginning for what follows.|
S~I wonder what each trainer will notice first about the companion arriving with them.
''')
add('trade_wrong_polite','Trade_Text_ThisIsntMon Trade_Text_ThisIsNoMon',
    "A trading partner explains that the selected Pokemon is not the species requested and leaves the offer open.",'''
N~The introduction was a little off target. No exchange has happened.|
N~The selected Pokemon does not match the stated species requirement.|
N~Wrong match for this offer. We can leave it there.|
N~It is good to have the mismatch explained without anyone treating the Pokemon as a mistake.|
N~A specific request can remain unmet without anyone needing to feel insulted.|
N~The casting call has received an enthusiastic but unsuitable audition.|
N~The offer was narrow; the world of perfectly good Pokemon is much wider.|
N~We should check the actual requested species before trying the selection again.|
N~A closed exchange is not a closed future for the companion beside us.|
N~There is no need to make a practical mismatch sound like a personal failure.|
N~I wonder what makes that particular species so important to the person asking.
''')
add('trade_wrong_abrupt','Trade_Text_WhatThatsNoMon',
    "A trader abruptly points out that the offered Pokemon is not the requested species.",'''
N~A mismatch has apparently startled the whole sales pitch out of them.|
N~The species requirement is unmet. The surprised tone adds no further information.|
N~Wrong selection. We can correct it without making a fuss.|
N~I would rather the Pokemon not have to listen to that much disappointment about itself.|
N~A clear request does not need a sharp response when somebody misses it.|
N~The audition has gone off-script and the director has chosen volume over tact.|
N~A small error has acquired an unnecessarily dramatic reception.|
N~We can check the requirement again rather than reacting to the tone.|
N~A thing can be wrong for a bargain and still entirely right in itself.|
N~A little courtesy would make the correction easier to receive.|
N~I wonder whether they hear how abrupt that sounds from the other side.
''')
add('trade_old_great','Trade_Text_IsntMyOldMonGreat',
    "A trader proudly asks whether their former Pokemon is impressive.",'''
S~That sounds like fondness trying to wear the disguise of a confident review.|
S~They still take pride in the Pokemon even after the exchange.|
S~A good sign that the former trainer remembers it warmly.|
S~I like hearing someone sound pleased about a companion who went to another home.|
S~A little praise can keep the handover from feeling purely transactional.|
S~The former agent remains an enthusiastic publicist for the departed star.|
S~Affection has survived the practical arrangement and returned as a boast.|
S~Knowing what the previous trainer valued might help us notice useful traits.|
S~Something once cared for is still shining in the memory that kept it.|
S~It is charming when the pride feels generous rather than possessive.|
S~I wonder which familiar habit they are picturing while they ask.
''')
add('trade_both_well','Trade_Text_HowIsMyOldMon',
    "A trader asks about their former Pokemon and says the received Pokemon is doing well.",'''
S~A little news exchanged after the Pokemon. The conversation has a life beyond the deal.|
S~The update concerns both sides of the trade, which is a useful and considerate follow-up.|
S~Good to hear the other Pokemon is settling in.|
S~It is lovely to know the care continued after we stopped watching.|
S~A reassuring update can make a trade feel like two good beginnings.|
S~The exchanged cast members have prompted a brief reunion of their former managers.|
S~An arrangement feels warmer when nobody forgets to ask how the lives involved are going.|
S~A real report tells us more than simply assuming the exchange worked out.|
S~Two paths can stay lightly connected by news of those travelling them.|
S~The question makes room for care on both sides instead of only satisfaction with the bargain.|
S~I wonder what story we would each choose first if there were time for a proper conversation.
''')
