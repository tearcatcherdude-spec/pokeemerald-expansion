"""Final actor followups, including exact idle Pokemon speech and receipt-safe Warden thanks."""
ROWS=[]
EMOTIONS=dict(N='neutral',S='soft_smile',A='annoyed',F='flustered',D='sad',U='surprised',M='smug',L='laughing')
def add(key,labels,subject,lines):
    replies=[]
    for line in lines.strip().split('|'):
        line=line.strip()
        if len(line)>1 and line[1]=='~' and line[0] in EMOTIONS:line=EMOTIONS[line[0]]+line[1:]
        replies.append(line)
    assert len(replies)==11,(key,len(replies))
    ROWS.append(dict(key='kanto_actor_end_'+key,labels=labels.split(),subject=subject,replies=replies))
add('warden_thanks_son','FuchsiaCity_WardensHouse_Text_ThanksSonGiveYouSomething',
    "The Warden thanks the male player for returning his teeth and relieving his embarrassment.",'''
S~We helped his words come back out properly. That is a much nicer victory than winning an argument.|
S~The restored speech matters socially as well as practically. His relief is quite understandable.|
S~Good that he can speak comfortably again. Nobody should feel trapped at home by shame.|
S~It sounds as though being understood matters more to him than the object itself.|
S~A familiar part of the day has become possible for him again.|
S~The thank-you is wonderfully clear after the trouble he had getting any words across.|
S~It is a relief to hear a person come back into his own voice.|
S~A small recovered piece has restored a much larger part of his daily life.|
S~Something missing has returned, and the room has found its ordinary voice again.|
S~He should never have needed to feel ashamed, but I am glad the embarrassment has eased.|
S~I wonder how good the first ordinary conversation at his office will feel.
''')
add('warden_thanks_lass','FuchsiaCity_WardensHouse_Text_ThanksLassieGiveYouSomething',
    "The Warden thanks the female player for recovering his teeth after he had avoided the office in embarrassment.",'''
S~A whole thank-you without a single guessed syllable. I am happy for him.|
S~Restoring intelligible speech has removed a barrier that had been limiting his social confidence.|
S~He can get back to his day without struggling to explain every word.|
S~I am glad we get to hear the warmth that was stuck behind all the frustration.|
S~Being able to ask an ordinary question again must feel surprisingly good.|
S~The rescued voice has used its first clear opportunity to be generous.|
S~An awkward silence has ended in something much kinder than a joke at his expense.|
S~The practical repair has made a real difference to how comfortable he feels around people.|
S~A familiar voice can feel newly precious after being so hard to reach.|
S~His relief makes this feel far more important than an errand completed.|
S~I wonder who he most wants to speak to now that the words will come out properly.
''')
add('gamecorner_erika','CeladonCity_GameCorner_Text_GymGuyAdvice',
    "The Gym guide warns that Erika's gentle manner should not lead the player to underestimate her.",'''
S~Flower arranging and being formidable apparently fit into the same afternoon just fine.|
S~A gentle presentation does not determine a trainer's tactical ability.|
N~Take Erika seriously. A quiet manner is no weakness.|
S~I like hearing someone point out that gentleness can be part of strength.|
N~A peaceful interest tells us little about how demanding the battle will be.|
S~The graceful introduction contains an entirely credible warning about the next act.|
S~Softness has been mistaken for frailty often enough to deserve its own warning sign.|
N~Prepare for her actual team instead of forming a plan around her manner.|
S~A garden can be beautifully tended and still refuse careless footsteps.|
S~Underestimating someone because she seems gentle is an excellent way to embarrass yourself.|
S~I wonder which detail first taught the guide not to judge her by appearances.
''')
add('gamecorner_prizes','CeladonCity_GameCorner_Text_RareMonsForCoins',
    "A gambler wants the rare Pokemon prizes but cannot seem to win enough Coins.",'''
N~The prize has become a very convincing excuse to keep arguing with a machine.|
N~An appealing reward does not improve the odds of the next attempt.|
N~Set a limit. Chasing the prize can cost more than it feels like.|
N~I hope wanting the Pokemon does not make every loss feel like a reason to stay.|
N~Keep enough for ordinary needs instead of putting everything into another try.|
N~The glittering final act is keeping the audience seated through a very expensive opening.|
N~Desire is doing the machine's persuasive work for it.|
N~The reward and the chance of reaching it need judging separately.|
N~A bright thing beyond the glass can make the hand forget what it is letting go.|
N~A tempting prize is not a good reason to ignore how the afternoon is actually going.|
N~I wonder whether stepping outside would make the next decision feel less urgent.
''')
add('prize_coins','CeladonCity_GameCorner_PrizeRoom_Text_NeedMoreCoins',
    "The prize clerk cannot complete the exchange because the player lacks enough Coins.",'''
N~The display is still full of possibilities. Our Coin total has a much shorter opinion.|
N~The required exchange amount exceeds the available Coins, so no prize has been awarded.|
N~Not enough for this exchange. We can pass without chasing the difference.|
N~It is better to decide calmly whether the prize is worth pursuing at all.|
N~A shortfall does not have to become the rest of the day's project.|
N~The coveted prop remains behind the counter pending a larger budget.|
N~A small number can be a useful place to stop before a larger mistake.|
N~We should assess the cost before treating the missing Coins as something to obtain immediately.|
N~A wanted thing can remain wanted without being brought home today.|
N~A polite refusal is better than being urged to keep spending toward it.|
N~I wonder which part of the prize still feels appealing once we leave the display behind.
''')
add('nurse_farewell','Text_WeHopeToSeeYouAgain_Frlg',
    "The Pokemon Center nurse closes the visit with a courteous farewell.",'''
S~A kind goodbye makes a busy Center feel a little less like a stop on a checklist.|
S~The farewell expresses goodwill; by itself it does not identify which service was used.|
S~Good people to have along the road, even for a brief visit.|
S~I like how an ordinary greeting can make a place feel safe to return to.|
S~Care includes the way people are sent back into the day.|
S~The reception ends with a small kindness rather than a grand flourish.|
S~A familiar farewell can become a surprisingly comforting sound.|
S~A clear, friendly closing makes the visit feel properly finished.|
S~A warm doorway remains behind us when the next road begins.|
S~Good hospitality has a quiet way of making itself memorable.|
S~I wonder how many tired travellers have left feeling better just for being welcomed.
''')
add('warden_gift_room','FuchsiaCity_WardensHouse_Text_HM04NoRoom',
    "There is no room for the Warden's gift, so the player keeps the Gold Teeth until the exchange can be completed.",'''
N~We found the missing teeth and managed to bring them back to a very full Bag. One more bit to sort.|
N~The exchange has not completed. Making room will allow the teeth and gift to be handed over together.|
N~Clear some space, then try again. We still have the teeth.|
N~A small practical delay. We can fix it without guessing at what he is trying to say.|
N~A quick sorting stop will make the whole handover much easier.|
N~The happy resolution is waiting on a surprisingly mundane luggage revision.|
N~The missing piece is here; the empty space is not. An inconvenient little symmetry.|
N~Good that the exchange waits until both sides can actually receive what is intended.|
N~A doorway has found its key and is waiting for room to turn it.|
N~Better to complete the arrangement properly than leave him with another awkward problem.|
N~I wonder what we can put away so the next visit ends with him speaking clearly again.
''')
add('celadon_clefairy','CeladonCity_Condominiums_1F_Text_Clefairy',
    "A Clefairy in the Celadon condominium answers with a bright little cry.",'''
S~That is an excellent tiny greeting. I feel we have been received by the important local resident.|
S~A short vocal response is enough for a pleasant encounter without assigning it a translation.|
S~A friendly little interruption to the visit.|
S~The sound makes the room feel a little less formal.|
S~There is something cheerful about being noticed by the Pokemon as well as the people.|
S~The smallest host has delivered an entirely memorable introduction.|
S~A few bright syllables have improved the room considerably.|
S~I like how much character a little vocal greeting can carry.|
S~A small voice has put a little light around the doorway.|
S~Clefairy has made a very good first impression with very little fuss.|
S~I wonder who in this building gets that greeting every morning.
''')
add('celadon_meowth','CeladonCity_Condominiums_1F_Text_Meowth',
    "The condominium's Meowth responds to the player.",'''
S~A clear meow. I appreciate a resident who keeps the introductions wonderfully concise.|
N~We have a vocal response, though no reliable basis for a detailed interpretation.|
S~Meowth has noticed us. Keep the visit calm.|
S~I like the little pause when a Pokemon decides to answer.|
S~A familiar sound can make a new building feel oddly homely.|
S~The resident has issued a brief statement and declined further questions.|
S~A single syllable can possess an impressive amount of personality.|
S~No complicated interface needed for that particular introduction.|
S~The room has a voice close to the floor.|
S~A short greeting, delivered with all the assurance of someone who lives here.|
S~I wonder whether this Meowth has a favourite place to watch everyone come and go.
''')
add('celadon_nidoran','CeladonCity_Condominiums_1F_Text_Nidoran',
    "The female Nidoran in the condominium gives a little cry.",'''
S~That little cry is a very effective reminder that the room has more than human company.|
S~She has responded to our approach. Best allow her space to choose the rest of the interaction.|
N~Give the little one enough room. We do not need to crowd her.|
S~I like being able to notice a small resident without turning the meeting into a fuss.|
S~A gentle hello is plenty; no need to insist on more attention.|
S~The quiet visitor has received an introduction from the smallest part of the household.|
S~Small does not mean a presence goes unnoticed.|
S~A calm approach gives us a better chance to observe without startling her.|
S~A little life has lent its voice to the room.|
S~She deserves the same courtesy as any other resident we came to see.|
S~I wonder how different her voice sounds to the people who know her well.
''')
add('slowbro_sleep','CeruleanCity_Text_SlowbroTookSnooze',
    "Slowbro takes a snooze during the interaction.",'''
L~Our conversation has been defeated by a nap with no warning and excellent timing.|
S~Sleep appears to have taken priority over the interaction. There is no need to wake it.|
S~Let Slowbro rest. We can move along quietly.|
S~There is something reassuring about a creature that can settle so completely.|
S~A nap is a perfectly good use of a quiet moment.|
S~The principal participant has left the conversation by the most comfortable exit available.|
S~A remarkable commitment to ending the scene without saying anything cruel.|
S~We can avoid adding unnecessary disturbance while it is resting.|
S~The afternoon has folded itself around one sleeping shape.|
S~An impressively relaxed way to let the world carry on without you.|
S~I wonder what details of the busy town disappear when it drifts off like that.
''')
add('slowbro_loaf','CeruleanCity_Text_SlowbroLoafingAround',
    "Slowbro loafs around instead of doing anything in particular.",'''
S~Slowbro has scheduled absolutely nothing and seems very committed to seeing it through.|
S~An idle period is not necessarily evidence of a problem that requires intervention.|
S~Nothing wrong with a quiet pause. Leave it be.|
S~It looks like the sort of afternoon that becomes nicer when nobody hurries it.|
S~Not every moment needs to turn into a useful task.|
S~The resident has declined the pressure to advance the day's plot.|
S~A beautifully unambitious little scene. I respect the restraint.|
S~Sometimes a system is simply resting rather than failing to perform.|
S~Time can pass through a place without demanding to be filled.|
S~There is a certain confidence in making no attempt to look busy.|
S~I wonder how much more of the town we would notice if we stopped hurrying past it.
''')
add('slowbro_away','CeruleanCity_Text_SlowbroTurnedAway',
    "Slowbro turns away from the interaction.",'''
N~A very clear demonstration of the other direction being more interesting right now.|
N~Turning away is sufficient reason to stop pressing for attention.|
N~Give Slowbro room. We can leave it there.|
N~It is all right if the meeting ends before we expected it to.|
N~A greeting does not obligate anyone to keep us entertained.|
N~The audience has politely rotated out of the performance.|
N~A boundary can be expressed with very little movement.|
N~We should respond to the visible cue instead of trying to override it.|
N~The creature has turned a small quiet door toward us.|
N~An elegant enough signal that the visit has reached its natural end.|
N~I wonder what caught its attention away from us, but we need not follow to find out.
''')
add('slowbro_orders','CeruleanCity_Text_SlowbroIgnoredOrders',
    "Slowbro ignores the orders given to it.",'''
N~The command has arrived at Slowbro and failed to obtain a forwarding address.|
N~A missed response alone does not explain the cause. More observation would be needed.|
N~Do not turn frustration into shouting. That will not explain the problem.|
N~I would rather someone try understanding the silence before blaming it.|
N~A different approach may help more than repeating the same demand.|
N~The instruction has received the silent review of a participant with other priorities.|
N~An unanswered order can contain more than simple stubbornness.|
N~Check the conditions and the cue before assuming the same instruction will work next time.|
N~A voice has crossed the space without finding a place to settle.|
N~The interaction would look better with less insistence and more attention.|
N~I wonder what cue would make sense to Slowbro instead of only to the person giving it.
''')
add('lavender_cubone','LavenderTown_House1_Text_Cubone',
    "The Cubone in a Lavender home responds to the player.",'''
S~A little voice in a quiet house. We can make this a gentle visit.|
N~We should observe Cubone's response without assuming a detailed meaning from the cry alone.|
N~Stay calm around the little one. It does not owe us a performance.|
S~I would rather sit nearby quietly than try too hard to get another reaction.|
S~A gentle greeting can be enough company for a short visit.|
S~The smallest resident has acknowledged the visitor without a need for further ceremony.|
S~A quiet meeting need not be an empty one.|
N~Give Cubone space to choose whether to stay near us.|
S~A small voice belongs fully to the room without needing to explain itself.|
S~Tenderness works better when it does not make a spectacle of somebody.|
S~I wonder what familiar things in this house make Cubone feel most at ease.
''')
add('volunteer_nidorino','LavenderTown_VolunteerPokemonHouse_Text_Nidorino',
    "Nidorino greets a visitor at Lavender's volunteer Pokemon house.",'''
S~That is a proper resident's greeting. The house has quite a varied welcoming committee.|
S~A direct vocal response gives us a small opportunity to observe without intruding.|
S~Good to see the Pokemon getting visitors who can keep things calm.|
S~A home feels different when its smallest occupants get noticed, too.|
S~A gentle visit seems a fair return for the people doing the daily care.|
S~The house has introduced another of the residents it exists to look after.|
S~There is a quiet pleasure in being welcomed without being important.|
N~We can enjoy the interaction without crowding Nidorino.|
S~A warm place contains more stories than its human voices can tell.|
S~The care here shows in the room being a place to live rather than a display.|
S~I wonder which familiar volunteer Nidorino recognizes first each morning.
''')
add('volunteer_psyduck','LavenderTown_VolunteerPokemonHouse_Text_Psyduck',
    "Psyduck responds inside the volunteer Pokemon house.",'''
S~Gwappa is a very satisfying contribution to the conversation, whatever the full dictionary says.|
S~An interesting vocalization. Interpretation should remain modest without further behavioural evidence.|
N~A quiet hello is enough. No need to fuss over Psyduck.|
S~I like hearing the different little voices that make this house feel lived in.|
S~There is something comforting about a place where every resident gets looked after.|
S~A memorable supporting voice has made a brief but distinctive entrance.|
S~A single odd syllable can improve a quiet afternoon considerably.|
S~I would rather notice the actual response than invent a complicated explanation for it.|
S~The room has made space for another small and unmistakable voice.|
S~A pleasant encounter need not become a demand for a clever trick.|
S~I wonder whether the people caring for Psyduck know a different sound for every mood.
''')
add('pewter_nidoran','PewterCity_House1_Text_Nidoran',
    "The male Nidoran in a Pewter home responds to the visitor.",'''
S~Bowbow! A very small resident has delivered a wonderfully sturdy little greeting.|
S~The response is distinct enough to be memorable without assuming we understand its meaning.|
S~A quiet hello back. Give Nidoran room to settle.|
S~It is nice to be noticed by someone so much closer to the floor.|
S~Small residents can make a house feel especially full of life.|
S~A tiny host has taken charge of the opening line.|
S~The room has found a rather compact source of personality.|
N~A calm approach lets Nidoran decide how much interaction it wants.|
S~A little voice can make a large doorway feel less imposing.|
S~Being small has not stopped Nidoran from making an introduction.|
S~I wonder who in the household recognizes that cry from the next room.
''')
add('jiggly_song','PewterCity_PokemonCenter_1F_Text_Jigglypuff',
    "The Center's Jigglypuff sings during the interaction before the normal music resumes.",'''
S~We have been treated to a very small concert in a very practical waiting room.|
S~A sustained vocal performance changes the atmosphere quite effectively without any explanation.|
S~A quiet moment to listen. No need to hurry it.|
S~I like how a little voice can make a busy place pause.|
S~Waiting feels nicer when there is something gentle to pay attention to.|
S~The waiting room has unexpectedly acquired a resident soloist.|
S~A little sweetness in a room where people often arrive worried.|
S~A short performance makes the space feel different before the familiar sounds return.|
S~A small voice has put a soft edge around the afternoon.|
S~An unassuming performance can be much more charming than a grand introduction.|
S~I wonder how many travellers remember this little pause more clearly than the road around it.
''')
add('fearow_home','Route16_House_Text_Fearow',
    "The Fearow in the secluded Route 16 house responds to a visitor.",'''
S~An impressive voice for a house tucked this quietly out of the way.|
S~The strong vocal response makes the otherwise secluded room feel distinctly occupied.|
N~Give Fearow enough space. We are visitors here.|
S~A hidden house feels less empty once one of its residents answers.|
S~A little respect for the household includes not crowding the Pokemon.|
S~The secluded residence has supplied a rather formidable welcoming voice.|
S~An out-of-the-way place can still have a very definite presence.|
N~We can keep the visit calm without needing to test Fearow's patience.|
S~The quiet little house contains a voice larger than its doorway suggests.|
S~A resident with that much presence hardly needs an elaborate introduction.|
S~I wonder what Fearow notices from this quiet place that the road below never sees.
''')
add('wigglytuff_cabin','SSAnne_1F_Room3_Text_Wigglytuff',
    "A Wigglytuff in an S.S. Anne cabin responds to the player.",'''
S~A cabin greeting with excellent round syllables. The passenger list is improving by the room.|
S~A Pokemon companion can make temporary accommodation feel more familiar.|
S~A pleasant little stop. Respect the passenger's space.|
S~It makes the cabin seem less like somewhere borrowed for a trip.|
S~A familiar companion can turn even a short stay into something homely.|
S~The ship's guest list has revealed another memorable cabin resident.|
S~A small domestic sound does a lot against the scale of a large ship.|
S~I like noticing the ordinary living details inside such an impressive vessel.|
S~A warm little voice has found its way into a room far from shore.|
S~The cabin feels more personal with a resident willing to answer.|
S~I wonder which part of travelling Wigglytuff finds most interesting.
''')
add('machoke_cabin','SSAnne_B1F_Room5_Text_Machoke',
    "The Machoke in an S.S. Anne cabin gives a hearty response.",'''
S~That greeting has shoulders. I had not realized a greeting could have shoulders.|
S~A forceful vocal response is certainly an effective way to make a small cabin feel occupied.|
S~Plenty of presence. We can still keep the visit courteous.|
S~I like how different every cabin feels once somebody answers.|
S~A hearty hello is a nice thing to find below deck.|
S~The supporting cast below deck is refusing to remain quietly in the background.|
S~A surprisingly substantial voice for a conversation held in passing.|
N~Leave enough space rather than making a small room feel crowded.|
S~The ship has a whole little world speaking beneath its polished upper rooms.|
S~An assured greeting can make a plain cabin memorable.|
S~I wonder which sounds of the ship have become familiar to Machoke during the voyage.
''')
add('copycat_chansey','SaffronCity_CopycatsHouse_1F_Text_Chansey',
    "Chansey responds from the ground floor of Copycat's home.",'''
S~A lovely little greeting before we get anywhere near the household's elaborate conversations.|
S~A direct response is a pleasant contrast to trying to interpret everybody else's expectations.|
S~A calm hello. Good way to enter somebody's home.|
S~I like the warmth a familiar Pokemon brings to a lived-in room.|
S~A soft welcome can make visitors relax without anyone making a fuss.|
S~The house has introduced a resident whose greeting requires no complicated performance.|
S~A simple sound is quite enough to make the doorway friendlier.|
S~It is nice to notice the quiet part of a busy household.|
S~A little warmth has been waiting at the bottom of the stairs.|
S~Chansey makes an appealing first impression without trying to hold the whole conversation.|
S~I wonder which family member this Chansey likes greeting first at the end of the day.
''')
add('copycat_doduo','SaffronCity_CopycatsHouse_2F_Text_Doduo',
    "Copycat's Doduo recites a rhyme about admiring itself in a mirror.",'''
L~The bird has acquired a vanity poem. This household has very enthusiastic educational standards.|
S~The recited phrase demonstrates learned vocal imitation, not necessarily an account of its beliefs.|
S~A memorable trick. Hope the bird enjoys the attention as much as the household does.|
F~It is a very particular sort of verse to hear unexpectedly upstairs.|
L~Someone has been generously seasoning the bird's vocabulary.|
M~The resident has delivered a vanity monologue with admirable commitment to the rhyme.|
S~Two heads, one poem, and a remarkably self-assured reflection.|
S~I would love to know how the repeated phrase was taught.|
S~A borrowed little rhyme has grown feathers and learned to look back.|
M~An unabashed mirror speech. I cannot fault the consistency of the theme.|
S~I wonder who first laughed when the rhyme came back in that voice.
''')
add('pidgey_greetings','SaffronCity_House_Text_Pidgey VermilionCity_House3_Text_Pidgey',
    "A household Pidgey answers the visitor with its familiar cry.",'''
S~A little bird has supplied the house with a very respectable greeting of its own.|
S~A familiar vocal response can be recognizable even without a detailed interpretation.|
S~Give Pidgey a calm hello and enough room.|
S~Small everyday voices are part of what makes a home feel like a home.|
S~It is nice to greet the Pokemon instead of treating them as part of the furniture.|
S~The household's feathered resident has contributed a short but distinctive introduction.|
S~A tiny voice can make an otherwise ordinary visit stay in the memory.|
S~I like the small differences we notice when we actually pause to listen.|
S~A little sound has put wings around the quiet room.|
S~A household feels warmer when every resident gets noticed.|
S~I wonder which sounds of the family this Pidgey recognizes before anyone enters the room.
''')
add('canyon_chansey','SevenIsland_SevaultCanyon_House_Text_Chansey',
    "The Chansey in the canyon rest house responds to the player.",'''
S~A small greeting feels especially welcome after the canyon's much bigger scenery.|
S~The encounter adds a familiar, gentle note to an otherwise isolated stop.|
S~A good place to ease the pace and be a considerate guest.|
S~It is nice to hear a little voice when the walk has been quiet for so long.|
S~A welcoming resident can make a simple shelter feel like a proper break.|
S~The canyon retreat has introduced another member of its unusually warm reception.|
S~A tiny domestic sound can be remarkably effective against a long empty walk.|
S~A calm rest stop does not need much equipment to make a difference.|
S~A warm little presence has gathered where the rough path pauses.|
S~The contrast between the hard walk and the gentle greeting is rather lovely.|
S~I wonder how many travellers have been unexpectedly cheered by meeting Chansey here.
''')
add('three_doduo','ThreeIsland_Text_Doduo',
    "A Doduo on Three Island answers the player's greeting.",'''
S~A short response from a bird with enough heads to make greetings feel like a group activity.|
S~An interesting sound to notice without needing to turn it into a precise translation.|
S~A calm greeting is enough. Let Doduo keep its space.|
S~I like the little everyday encounters that make an island feel lived in.|
S~Not every pleasant stop needs to become an errand or a battle.|
S~The island has introduced one of its less talkative but very distinctive residents.|
S~A bird can improve an ordinary street simply by being unmistakably itself.|
N~We can watch without trying to provoke another response.|
S~Two familiar shapes share a small patch of the island afternoon.|
S~A brief encounter can be charming without needing a performance attached.|
S~I wonder how much of the island's daily routine this Doduo recognizes.
''')
add('fanclub_pikachu','VermilionCity_PokemonFanClub_Text_Pikachu',
    "The Fan Club's Pikachu greets the player.",'''
S~The club has finally introduced a member who can be its own entire enthusiastic announcement.|
S~A short interaction lets us notice the Pokemon rather than only hear the admirers discussing them.|
S~A welcome little change from people explaining how much they like Pokemon.|
S~It is nice to meet the companions at the centre of all that affection.|
S~A cheerful greeting can be more convincing than a whole speech about charm.|
S~The subject of the admiration has stepped briefly into its own spotlight.|
S~A fan club is improved by the actual presence of someone worth being fond of.|
S~The little encounter makes the club feel less abstract and more alive.|
S~The room's enthusiasm has found a small bright voice of its own.|
S~Pikachu hardly needs a promotional campaign in a room this devoted.|
S~I wonder which familiar club member gets the most excited greeting.
''')
add('fanclub_seel','VermilionCity_PokemonFanClub_Text_Seel',
    "Seel responds inside the Pokemon Fan Club.",'''
S~That is a very good sound. The club's case for being fond of Pokemon keeps getting stronger.|
S~A direct encounter offers something a long description from an admirer cannot quite substitute for.|
S~Nice to have a quiet moment with the Pokemon themselves.|
S~I like hearing the small voices underneath all the enthusiastic conversation.|
S~The room feels warmer when the companions are part of the visit.|
S~A brief appearance from the actual subject has improved the club's lengthy programme.|
S~Sometimes affection has a rather better argument than words prepared for it.|
S~An unforced interaction tells us more than asking for a trick on demand.|
S~A small round sound has settled pleasantly among the human chatter.|
S~The enthusiasm is much more appealing when it leaves the Pokemon room to be themselves.|
S~I wonder how different the club sounds when the people fall quiet for a moment.
''')
