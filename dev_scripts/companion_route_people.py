"""Route trainers' actual post-battle dialogue, including distinct rematch lines."""
ROWS=[]
EMOTIONS=dict(N='neutral',S='soft_smile',A='annoyed',F='flustered',D='sad',
              U='surprised',M='smug',L='laughing')
def add(key,labels,subject,lines):
    replies=[]
    for line in lines.strip().split('|'):
        line=line.strip()
        if len(line)>1 and line[1]=='~' and line[0] in EMOTIONS:line=EMOTIONS[line[0]]+line[1:]
        replies.append(line)
    assert len(replies)==11,(key,len(replies))
    ROWS.append(dict(key=key,labels=labels.split(),subject=subject,replies=replies))

add('route103_amy_double_battles','Route103_Text_AmyPostBattle Route103_Text_AmyRematchPostBattle',
    'Amy says fighting two trainers requires thinking about many things.','''
M~Two trainers, several Pokemon, and my own internal commentary. A busy afternoon for your attention.|
N~The interactions between the partners matter as much as the individual moves.|
N~We can prepare together instead of expecting one person to notice everything at once.|
N~Following two parts becomes easier once you hear what they are doing together.|
N~It helps to know what each partner needs before the noise begins.|
M~A crowded scene rewards somebody who remembers to look beyond the nearest dramatic gesture.|
N~I appreciate her admitting that there is a lot to keep track of.|
N~Two working plans can produce a third, unexpected problem when they meet.|
N~Cooperation asks us to notice someone else's needs alongside our own.|
N~I would rather have a clear shared plan than two impressive performances getting in each other's way.|
N~I would pay attention to the moments when one partner changes what the other can do.
''')

add('route103_andrew_angry','Route103_Text_AndrewPostBattle',
    'Andrew remains angry after the battle.','''
N~He is still boiling. I would give that kettle a little space.|
N~Another argument is unlikely to help him think clearly about the battle.|
N~We do not have to stand here until he is ready to be pleasant.|
N~I would like the next sound we hear to be somewhere a little quieter.|
N~I hope he takes a break before asking his team to carry that mood into another battle.|
M~The battle has ended, but the dramatic temperature remains impressively high.|
N~He can have his feelings without making us responsible for fixing them.|
N~I would let everything cool before trying to identify what went wrong.|
N~Some space might be kinder to everybody involved.|
N~I hope his Pokemon are getting a gentler reception than the rest of the world.|
N~I would not ask him for a portrait at this particular moment.
''')

add('route103_daisy_fragrances','Route103_Text_DaisyPostBattle',
    'Daisy describes aromatherapy and calming fragrances.','''
S~I like a conversation about smells that does not end with somebody noticing our laundry.|
N~People find different things calming. I would ask which fragrances she particularly enjoys.|
S~It is good to have something quiet you can turn to after a busy day.|
S~A familiar scent can bring a whole room back to mind.|
S~I like the way a kitchen can start feeling welcoming before anybody reaches the table.|
S~A room can establish its mood before anyone says the first line.|
S~I have a few scents I would happily carry a little farther into a difficult day.|
S~I would label everything clearly before beginning any investigation involving fragrant bottles.|
S~A small comforting ritual can make space to breathe.|
S~I would like to know what she chooses for herself when nobody else is there to impress.|
S~That is something a photograph cannot keep by itself. I would write the memory beside it.
''')

add('route103_isabelle_swimming_apology','Route103_Text_IsabellePostBattle',
    'Isabelle apologizes for nearly colliding with us while practicing swimming.','''
S~She apologized. I am happy for our next meeting to involve rather less accidental momentum.|
N~Practicing is easier with enough space and appropriate support. I hope she has both.|
S~We are all right. She can keep learning without feeling that one mistake defines the afternoon.|
S~It is nice that she stopped to make sure the awkward moment ended kindly.|
S~I hope she is comfortable and has someone looking out for her while she practices.|
M~An accidental entrance, gracefully acknowledged. We can leave the collision out of the review.|
S~I appreciate the apology. Learning something in public can feel very exposed.|
N~I would rather give her more room than stand close and critique every movement.|
S~A little patience is a useful thing to offer someone who is still learning.|
S~Nobody needs to make the apology more embarrassing than it already feels.|
S~I would rather remember her stopping to check on us than the moment before it.
''')

add('route103_liv_partnership_loss','Route103_Text_LivPostBattle',
    'Liv is puzzled that she and her big sister lost despite working well together.','''
M~A perfect partnership can still encounter a thoroughly inconvenient us.|
N~Coordination is valuable, but a particular matchup may still require a different plan.|
N~Their teamwork was not wasted because they lost. They should keep what worked.|
N~Playing together well does not mean every song ends where you expected.|
N~I hope they are kind to each other while deciding what to try next.|
S~A good cast can have a difficult performance without ceasing to be a good cast.|
N~It is easier to learn from a loss when it does not become a reason to blame the person beside you.|
N~The parts can work together and still need a different overall arrangement.|
S~The trust between them is something they can carry into the next attempt.|
N~I hope they notice the things they did well as clearly as the result they wanted.|
N~I would like to hear them work out the next plan together.
''')

add('route103_liv_rematch_loss','Route103_Text_LivRematchPostBattle',
    'After another loss, Liv again questions why the sisters\' partnership did not win.','''
N~They still have each other. I hope the next revision involves the plan rather than the partnership.|
N~A repeated result is a reason to examine which part of the approach has stayed the same.|
N~They should change something useful, not decide the friendship itself was the mistake.|
N~Sometimes it helps to stop rehearsing the whole piece and listen to the bit where it keeps coming apart.|
N~I hope they take a break before trying to solve it while both are upset.|
N~Another difficult performance calls for a useful note, not a declaration that the company is doomed.|
N~They are allowed to feel disappointed without turning it against one another.|
N~I would look for the same failure occurring twice. That is more useful than starting everything over blindly.|
N~A patient conversation between them may do more good than another immediate challenge.|
N~I hope they keep some confidence in each other while changing the parts that need work.|
N~I would compare this attempt with the last one before deciding that nothing improved.
''')

add('route103_marcos_guitar_fans','Route103_Text_MarcosPostBattle',
    'Marcos gained listeners while playing guitar privately and wonders about going professional.','''
S~He went looking for somewhere quiet and accidentally acquired an audience. A very musical navigation error.|
S~People stopping to listen is encouraging. I hope he decides what he wants from the music himself.|
S~He can enjoy being heard without deciding his entire future this afternoon.|
S~I would like to hear what he was playing before he noticed everyone listening.|
S~I hope he keeps some time to play simply because he enjoys it.|
M~An accidental audience is a lovely review. It is not yet a complete employment contract.|
S~I hope the attention feels good to him, rather than making his quiet place feel borrowed.|
S~He should learn what professional work involves before mistaking encouragement for the whole plan.|
S~Something he enjoyed alone has become something he can share. He gets to choose what happens next.|
S~I hope he can hear his own preferences as clearly as the applause.|
S~I would like to record a little performance if he actually wanted it recorded.
''')

add('route103_miguel_fainted_partner','Route103_Text_MiguelPostBattle',
    'Miguel calls his Pokemon darling even while it has fainted.','''
N~It can remain adorable on the way to getting some care. I suggest making that the next activity.|
N~Affection is good. Attending to the Pokemon's condition should accompany it.|
N~I hope admiration is followed promptly by looking after the partner who needs help.|
N~It is nice to love a Pokemon through a loss. I would also like it to feel better.|
N~It needs care more urgently than another compliment right now.|
N~The performer deserves a comfortable recovery before the audience supplies further reviews.|
N~I hope being loved means being noticed when something is wrong, too.|
N~The affection is clear. Now I would like to see the practical response to the damage.|
N~Care should do something for the one receiving it.|
N~I would rather hear how comfortable the Pokemon is than how lovely it still looks.|
N~This is a good time to put the attention into helping, rather than admiring.
''')

add('route103_miguel_growing_affection','Route103_Text_MiguelRematchPostBattle',
    'Miguel says his Pokemon becomes more adorable as they spend time together.','''
S~The Pokemon has discovered the most reliable beauty treatment: being someone's favorite.|
S~Familiarity gives him more little things to notice and enjoy.|
S~It is good when spending time together makes the ordinary parts matter more.|
S~I like how a familiar face can become more interesting the longer you know it.|
S~I hope the Pokemon feels that affection in its everyday care.|
S~A long-running role with an increasingly enthusiastic audience of one.|
S~I understand that. Knowing somebody gives you more reasons to be fond of them.|
S~He has made a strong case for actually spending time with a partner.|
S~Love can keep becoming more particular as you learn someone.|
S~The best details are often the ones a first glance would have missed.|
S~That is why I like taking another picture years later. You know what to notice differently.
''')

add('route103_pete_trust_and_surf','Route103_Text_PetePostBattle',
    'Pete understands wanting to Surf with a particularly trusted Pokemon.','''
S~A trustworthy partner does make the sea look rather more inviting. I would still secure the sandwiches.|
N~Trust matters when we depend on a partner so directly. It should be supported by preparation and care.|
S~I like hearing the partnership noticed, rather than only the distance we can travel.|
S~It must feel different to cross the water with someone whose movements you already know.|
N~I hope the Pokemon gets the same confidence that we will look after it in return.|
S~The journey has a companion built into it. That is a rather lovely reason to go.|
S~I would like to feel that secure beside the water.|
N~Trust and a well-secured bag seem like an excellent combination for the crossing.|
S~Depending on someone should make us attentive to them, not forgetful of their effort.|
S~It is nice when somebody notices what makes a partnership feel comfortable.|
S~I would like a memory of the crossing that includes the Pokemon doing the carrying.
''')

add('route103_rhett_cramped_space','Route103_Text_RhettPostBattle',
    'Rhett asks whether we like cramped quarters.','''
M~I prefer my personal space to include a little room for the word personal.|
N~Enough space to move safely is a useful feature in almost any activity.|
N~I like having room to step back when I need it.|
N~A quiet small room can be lovely. A crowded one is quite a different instrument.|
N~I would rather everybody have somewhere comfortable to put themselves.|
M~Intimate staging is best arranged with the consent of the entire cast.|
N~I would like to choose when the walls are close to me.|
N~I usually discover a small room's limitations with my elbows and a toolbox.|
N~A little space can make it easier to be comfortable with other people.|
N~I would rather not arrive at a doorway already negotiating whose shoulder goes first.|
N~Sometimes a narrow view is interesting. I prefer to photograph it without being trapped inside it.
''')

add('route104_billy_footprints','Route104_Text_BillyPostBattle',
    'Billy wants to leave footprints all over the sand but the sea erases them.','''
S~The beach has an extremely efficient tidying policy. Billy seems less enthusiastic about it.|
N~The tide changes the surface continuously. A temporary mark can still tell us that someone was there.|
S~The walk mattered even if the sand did not keep a record.|
S~I like that the next person gets a fresh stretch of beach to begin on.|
S~I hope he enjoys making the footprints while they are his to look at.|
S~A performance that the sea insists on resetting between audiences.|
S~Something does not have to stay forever to be worth doing.|
N~If he wants a lasting record, the beach is a rather uncooperative material.|
S~The sea can change the trace without taking away the day he had here.|
S~I would enjoy the pattern before asking it to last.|
S~A picture could keep the footprints without asking the tide to change its habits.
''')

add('route104_rival_briney_friendship','Route104_Text_BrendanPostBattle Route104_Text_MayPostBattle',
    'Our rival praises our handling of Pokemon and points to Briney as an example of friendship.','''
S~Briney and Peeko have become the local example of doing this properly. I think they would enjoy hearing that.|
S~Skill and friendship should support each other. It is good advice to keep beside the praise.|
N~Our team deserves a life with us outside the moments when we need to win.|
S~I like the part where people remember how somebody treats their partner between adventures.|
S~Meals, quiet company, noticing little needs. Friendship gets built in those ordinary parts too.|
S~Briney has supplied a convincing example without needing to make a speech about it himself.|
S~It is a relief to hear somebody say that being good together matters beyond a result.|
N~A partnership that works needs care as well as an effective plan.|
S~The trust we rely on should also be something our Pokemon get to enjoy.|
S~I hope we are remembered kindly by the ones traveling beside us.|
S~I would like our record of the journey to include ordinary happy days with the team.
''')

add('route104_cindy_hellos','Route104_Text_CindyPostBattle',
    'Cindy links hello and goodbye and hopes we meet again.','''
S~I was prepared for hello to begin a conversation, not ambush me with the entire concept of leaving.|
S~A brief meeting can still give people a reason to welcome the next one.|
S~I hope we do meet again. It is nice to leave someone with a reason to smile.|
S~A good goodbye can leave a little room for the next hello.|
S~I hope she has plenty of pleasant company between now and then.|
M~An unexpectedly melancholy opening, followed by a very agreeable proposal for a sequel.|
S~Saying goodbye does not make meeting someone a mistake.|
S~I like an arrangement that leaves the possibility of checking in later.|
S~A meeting can be worth having even when you cannot keep it still.|
S~I hope she remembers the pleasant part of the encounter while she waits for another.|
S~I would like to hear what changed for her when we next come through.
''')

add('route104_darian_magikarp_name','Route104_Text_DarianPostBattle',
    'Darian complains that Magikarp does not live up to its impressive name.','''
M~The Pokemon did not choose its name. It would like its performance review adjusted accordingly.|
N~A name is a poor basis for setting a partner's abilities. He should learn what Magikarp can actually do.|
N~He has the Pokemon he has, not the one a name persuaded him to imagine.|
N~I hope he finds something to like about the real partner in front of him.|
N~Magikarp deserves care without first having to satisfy an advertising promise.|
M~The performer has been blamed for the title. I would take that complaint to whoever wrote the poster.|
N~It is difficult to live comfortably beside somebody else's disappointment.|
N~He should begin with the actual specifications, rather than what the label suggested.|
N~A partner is more than the expectations someone brought to meeting it.|
N~I would like Magikarp to have someone interested in who it is today.|
N~I would rather record what Magikarp does than what someone insists it ought to do.
''')

add('route104_gina_more_training','Route104_Text_GinaPostBattle',
    'Gina praises our strength and resolves to train more.','''
S~She has turned the result into a plan. I hope the plan also contains a snack break.|
S~Training is useful when it has a purpose. I hope she notices which part she wants to improve.|
S~I like that she can respect our team and still feel hopeful about hers.|
S~That sounds like a good note to leave the battle on.|
S~I hope the whole team gets some rest before the next attempt.|
S~An encouraging review and a decision to rehearse. A very healthy response to a difficult performance.|
S~It is nice to hear determination that does not need an excuse attached to the loss.|
N~I would turn that enthusiasm into one clear adjustment before the next practice.|
S~A loss can leave room for admiration and hope at the same time.|
S~I hope she keeps that generosity toward her own team while they learn.|
S~I would enjoy seeing what she does differently when we next meet.
''')

add('route104_haley_own_choices','Route104_Text_HaleyPostBattle',
    'Haley warns against letting other people make decisions we must live with.','''
N~I can supply opinions. I would prefer not to accidentally become the person who chose your entire afternoon.|
N~Advice can clarify a decision without taking ownership of it away from the person affected.|
N~I can stand beside you while you choose. You should still get to choose.|
N~It helps to hear your own reasons clearly beneath everybody else's suggestions.|
N~I want my advice to make things easier for you, not make you feel that you owe me a particular answer.|
N~An adviser is not automatically entitled to the leading role.|
N~It can be difficult to tell what you want when you are busy trying not to disappoint someone.|
N~I would rather explain the trade-offs than pretend there is only one respectable answer.|
N~A kind relationship should leave room for a decision the other person would not have made.|
N~People can mean well and still be very loud about the wrong future for you.|
N~I would like to hear what matters to you before offering a direction.
''')

add('route104_ivan_neglected_training','Route104_Text_IvanPostBattle',
    'Ivan became so absorbed in fishing that he neglected raising his Pokemon.','''
M~The fishing has been excellent at catching his entire attention.|
N~Enjoying an activity should not make a partner's ordinary needs disappear from the plan.|
N~He has noticed the problem. The useful next step is looking after the Pokemon, not only feeling bad about it.|
N~It is easy for a favorite thing to fill more of the day than you meant to give it.|
N~I hope he makes some quiet time for his team before going back to the water.|
N~The supporting cast still needs attention while the main character pursues a hobby.|
N~I hope his Pokemon get more than a guilty apology out of this realization.|
N~A routine might help him remember the work that does not announce itself as loudly as a bite.|
N~What depends on us deserves a place in the day, even when something else is exciting.|
N~He can keep the hobby and become more thoughtful about the people sharing it with him.|
N~I would like to hear what he changes afterward. Noticing is the beginning of the useful part.
''')

add('route104_mia_aspiration','Route104_Text_MiaPostBattle',
    'Mia wants to train her team to become strong like ours.','''
S~I hope she finds her own version of strong. Ours currently includes a surprising amount of walking.|
S~It is good to have an example, and equally useful to understand what makes that example work.|
S~I hope she sees things worth learning without deciding her own team is somehow wrong.|
S~It is lovely to know our journey has given somebody else a little encouragement.|
S~I hope they are patient with one another while they get there.|
S~She has found an inspiring performance. I hope the rehearsal becomes something she enjoys for itself too.|
S~I hope she discovers things her own team does that are worth being proud of already.|
S~Learning from a result is useful. Copying only the visible parts usually misses the interesting work.|
S~Someone else's achievement can open a possibility without having to become an exact blueprint.|
S~I would like her to feel proud of the progress while it is still progress.|
S~I hope we meet again and get to notice how far her team has come.
''')

add('route104_winston_money_limits','Route104_Text_WinstonPostBattle',
    'Winston reflects that some things, including Pokemon, cannot be bought.','''
S~I am glad the money has discovered the limits of its conversational authority.|
N~A genuine partnership requires things a transaction cannot supply on its own.|
N~Trust takes care and time, however impressive someone's wallet is.|
S~It is nice to hear someone noticing what a relationship asks beyond acquiring things.|
S~Having resources can help with care. Deciding to give that care is still a choice somebody has to make.|
M~An expensive education in the existence of other kinds of value.|
N~I hope the thought stays with him after the disappointment wears off.|
N~Good equipment helps. It does not do the work of understanding a partner.|
N~Being able to have something is different from learning to live well with it.|
N~I would like his Pokemon to receive affection that is not measured by what they cost.|
N~I would rather hear what his team has taught him than what it would have been priced at.
''')
