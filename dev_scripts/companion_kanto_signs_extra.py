"""Additional exact Kanto Gym, exhibit and public-sign descriptions."""
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

add('sign_chansey_chance','FuchsiaCity_Text_ChanseySign',
    'The Chansey exhibit sign jokes that catching one is up to chance.', '''
M~Chance and Chansey. The sign has done its wordplay and is now refusing further practical assistance.|
N~An amusing label. Chance is still easier to manage with preparation and patience.|
N~A joke is not a catching plan. We can prepare before trying.|
S~I like a sign that gives itself permission to be a little silly.|
N~If we meet one, I hope we remember the creature rather than only the challenge.|
M~The exhibit's educational mission has paused to enjoy its own pun.|
M~A scientific notice written by someone briefly possessed by a dad joke.|
N~It identifies uncertainty without providing a useful procedure. A charmingly incomplete specification.|
S~Some meetings arrive as a gift rather than an appointment.|
M~A small pun, confidently presented. I cannot fault the commitment.|
N~I would want to remember a real encounter more than the story of how difficult it was.
''')
add('sign_voltorb_ball','FuchsiaCity_Text_VoltorbSign',
    'The Voltorb sign compares it with a Poke Ball.', '''
U~A Poke Ball that has its own opinions about being picked up. Important distinction.|
N~Resemblance is not identity. We should observe the living creature before assuming it is an object.|
N~Look before grabbing. A familiar shape is not always a familiar situation.|
N~It would be strange having people mistake you for something they can simply take.|
N~I hope visitors remember it deserves space and care, not only a funny comparison.|
M~A prop-shaped character has arrived with every right to object to the casting.|
M~I support any apparent possession capable of telling someone to stop touching it.|
N~A useful warning against classifying something from its silhouette alone.|
N~A living thing can hide inside the shape our habits expect.|
N~A familiar design does not tell us whether the thing wants to be handled.|
N~I would watch for the little movement that changes how we understand what we are seeing.
''')
add('sign_kangaskhan_pouch','FuchsiaCity_Text_KangaskhanSign',
    'The exhibit explains Kangaskhan carries and raises its young in a belly pouch.', '''
S~A parent with a built-in place to keep the small adventurer from wandering off. Very practical.|
N~The pouch keeps a developing young one close while the parent moves. An interesting arrangement.|
N~Give them room. There is a young one involved as well as the adult.|
S~I like the thought of seeing the world while knowing exactly where home is.|
S~Caring for someone travels with the parent. I hope both get enough rest.|
S~One character makes an entrance while quietly carrying another's whole beginning.|
S~A small companion who can retreat from the world without being left behind. Sensible.|
N~I would be interested in how the youngster's needs change as it grows.|
S~A first shelter moves with the life that made it.|
S~It is a practical kind of closeness. There is nothing small about that care.|
S~I would want to notice the little exchanges between them, not just the striking shape.
''')
add('sign_slowpoke_friendly_slow','FuchsiaCity_Text_SlowpokeSign',
    'The exhibit calls Slowpoke friendly and very slow moving.', '''
S~Friendly and slow. I have found the ideal person to wait for me while I tie a shoe.|
N~A slow pace does not tell us how much it notices. I would watch before assuming.|
N~Give it time. There is no need to turn every meeting into a hurry.|
S~That sounds like comfortable company. No rush to fill every pause.|
S~We can match its pace for a moment instead of making it keep ours.|
S~A character confident enough to let the scene wait for its arrival.|
S~At last, a creature whose social timetable I feel qualified to meet.|
N~Slow response is still response. It deserves time to become clear.|
S~A gentle presence does not need to move quickly to be felt.|
S~Friendly is a lovely first impression. Slow is not an apology.|
S~I would stay long enough to see the change somebody rushing past would miss.
''')
add('sign_lapras_seas','FuchsiaCity_Text_LaprasSign',
    'The Lapras exhibit gives it the title king of the seas.', '''
M~King of the seas. I hope the coronation included a very comfortable place to sit.|
N~A grand title. I am more curious about the creature's actual behavior than the rank people gave it.|
N~Respect the Pokemon, not only the impressive name on the sign.|
S~I wonder what a creature like that notices about the people watching it.|
S~An impressive title should come with ordinary care, too.|
M~The exhibit has promoted its subject directly to aquatic royalty.|
S~A regal introduction. I hope it is also allowed to have a rather unregal nap.|
N~I would like to know which observations made people choose that title.|
N~A sea does not need a throne for a life to belong to it.|
N~A beautiful image. I still want the actual Pokemon to have room beyond it.|
S~I would rather remember one quiet movement than ask it to perform being a king.
''')
add('sign_omanyte_restored','FuchsiaCity_Text_OmanyteSign',
    'The exhibit describes an extremely rare Omanyte regenerated from a fossil.', '''
U~A fossil became a Pokemon again. My old crumbs have been given entirely unrealistic hopes.|
N~Revival turns an object of study into a living creature with needs of its own.|
N~It is alive now. Care for it as a partner, not only as a discovery.|
N~I wonder what an unfamiliar world feels like to something brought back into it.|
S~I hope someone has learned what makes it comfortable in its new surroundings.|
S~A very old chapter has opened into a life that still gets to have tomorrow.|
N~Being extraordinary must be tiring when everyone keeps pointing at the label.|
N~The process is remarkable. Understanding the revived creature is the continuing work.|
S~Something kept in stone has found a little movement again.|
N~I hope rare does not become the only thing anybody bothers to know about it.|
N~I would want to see the little ordinary habits it develops here, not only record that it returned.
''')
add('sign_kabuto_restored','FuchsiaCity_Text_KabutoSign',
    'The exhibit describes an extremely rare Kabuto regenerated from a fossil.', '''
U~An ancient life has returned, and we have introduced it with a small board. A lot to fit.|
N~A fossil can preserve evidence of a life. This one has become a living source of new observations.|
N~Give it room to settle into the world we brought it into.|
N~I hope being watched does not become the whole of its new life.|
N~Somebody should learn what a good ordinary day looks like for it now.|
S~The past has become a character who still needs a future.|
N~A remarkable return. I hope it is allowed to be unimpressive when it wants to rest.|
N~Restoration answers one question and creates a great many care requirements.|
S~The stone kept a shape. Now there is a life moving within it.|
N~A rarity can still want simple things. We should notice those, too.|
N~I would look for the first little sign that this unfamiliar place is becoming familiar to it.
''')

add('sign_brock_rock_solid','PewterCity_Text_GymSign',
    'Brock sign calls him the rock-solid Pokemon Trainer.', '''
M~Rock-solid. A reassuring reference, unless we need him to move out of a doorway.|
N~A reputation for steadiness is useful. We should still observe the decisions that earned it.|
N~A strong introduction. We will take the actual trainer seriously.|
S~I like the idea of somebody people can depend on.|
S~Being reliable is worth celebrating alongside being powerful.|
M~The leading man has been given an impressively load-bearing description.|
M~A firm reputation. I hope he is also allowed to have a soft chair.|
N~Stability is a good quality in a design and a person. Neither means refusing every adjustment.|
N~Even a steady stone has a different face from another side.|
N~A memorable phrase. I would like to meet the ordinary person behind it.|
N~I wonder what a resident would say he did that made the title fit.
''')
add('sign_misty_mermaid','CeruleanCity_Text_GymSign',
    'Misty sign gives her the title Tomboyish Mermaid.', '''
M~A mermaid running a Gym. I hope the interview included how she planned to handle the stairs.|
N~A colorful title. I would rather learn how she trains than infer everything from it.|
N~We can meet her without expecting her to act like the sign.|
N~I wonder whether she chose that description or just got used to seeing it.|
N~A leader has ordinary days, too. The title need not do all the introducing.|
M~The local star has received an aquatic billing with a rather specific character note.|
M~A lot of personality has been assigned before anyone says hello.|
N~The sign gives us an image, not a technical account of the team.|
N~A name given by a town can fit differently from the name someone gives themselves.|
N~I hope she gets to decide what that image means when people meet her.|
N~I would want to notice the part of her the introduction did not prepare us to see.
''')
add('sign_surge_lightning_american','VermilionCity_Text_GymSign',
    'Surge sign introduces the Lightning American.', '''
M~Lightning American. A very efficient introduction if the handshake is also a warning.|
N~A striking public identity. It tells us little about his actual training method.|
N~Take the electrical part seriously. The nickname does not change how we prepare.|
N~I would like an ordinary conversation before deciding how intimidating that has to be.|
N~I hope he makes room for nervous challengers as well as the bold ones.|
M~A compact title with the promise of considerable sound and lighting.|
M~I am pleased the sign has warned us before we attempt polite proximity.|
N~I would be interested in how his experience shapes the equipment and the team.|
N~A loud name can travel ahead of a person and fill the doorway first.|
N~He has certainly made an impression. I wonder which parts he wants people to keep.|
N~I would listen for the quieter habit that belongs to the person rather than the title.
''')
add('sign_erika_nature_princess','CeladonCity_Text_GymSign',
    'Erika sign describes the nature-loving princess.', '''
S~Nature-loving princess. I hope the royal duties include letting the plants finish their naps.|
S~An affection for nature sounds like a better starting point than a wish merely to control it.|
N~The care behind the title matters more than how elegant it sounds.|
S~I like an introduction that lets gentleness belong beside strength.|
S~I hope loving nature includes the awkward little creatures as well as the beautiful ones.|
S~A graceful title has brought the garden into the leading role.|
S~A quieter sort of royalty. I could tolerate a court with more leaves than speeches.|
N~I would like to see the everyday care that supports the polished appearance.|
S~A garden can be loved without being made to stand perfectly still.|
S~A lovely image. I hope she has room to be a person outside it.|
S~I would look for how she treats a small, unremarkable growing thing when nobody asks her to pose.
''')
add('sign_koga_poison_ninja','FuchsiaCity_Text_GymSign',
    'Koga sign introduces a poisonous ninja master.', '''
M~Poisonous ninja master. A refreshingly direct explanation of why I should keep my hands to myself.|
N~Concealment and poison both reward careful preparation from an opponent.|
N~Check the remedies before we go in. Respect the warning.|
N~I would feel better knowing how to leave safely before learning how to enter dramatically.|
N~We should make sure the team is comfortable and supplied before starting.|
M~The local host has announced the genre and most of the hazards in one line.|
M~A title with very little interest in sounding approachable.|
N~I appreciate a hazard declaration. I would also appreciate a visible floor plan.|
N~The hidden thing has left a clear warning at its door.|
N~An intimidating introduction can still be useful if it helps us arrive prepared.|
N~I would watch the small details instead of waiting for the dramatic part to announce itself.
''')
add('sign_sabrina_psychic_master','SaffronCity_Text_GymSign',
    'Sabrina sign calls her the master of Psychic Pokemon.', '''
M~A master of Psychic Pokemon. I will attempt to arrange my thoughts somewhere less cluttered.|
N~A strong claim of expertise. I would like to see how she understands her team's particular needs.|
N~We can respect the skill without giving the title our whole confidence.|
F~I hope meeting her does not mean having to explain every thought that arrives at the wrong time.|
N~A powerful team still deserves ordinary patience and care.|
M~The introduction has promised an unusually direct interest in what is going through our heads.|
M~I have prepared several reasonable thoughts. I cannot promise they will be the ones available.|
N~Expertise is interesting when someone can show how it works, not only name it.|
N~A mind can be strong and still have places it keeps private.|
N~I would like the person behind that title to get a proper introduction of her own.|
N~I wonder which moment with her Pokemon first made her decide this was the work she wanted.
''')
add('sign_blaine_quiz_master','CinnabarIsland_Text_GymSign',
    'Blaine sign calls him the hotheaded quiz master.', '''
U~A quiz and a hot temper. I hope the wrong answers are marked in ordinary ink.|
N~Questions can test understanding. The quality of the questions will matter.|
N~We can take a moment to think. A loud examiner does not change the answer.|
N~I hope he likes curiosity more than he likes catching people out.|
N~A good lesson leaves someone able to try again without being afraid.|
M~The master of ceremonies has announced both the game format and the expected temperature.|
M~I am revising for the practical art of remaining calm while somebody else is very pleased with a question.|
N~I will reserve judgment until I see whether the quiz measures useful knowledge.|
N~A question can be a door or a trap. I prefer the first kind.|
N~I hope a thoughtful answer matters more than how confidently it is delivered.|
N~I would watch his face when someone surprises him with a good answer.
''')
add('sign_viridian_spare_title','ViridianCity_Text_GymSign',
    'Viridian Gym sign gives the building title without a leader name or epithet.', '''
M~A Gym. The sign has completed its entire introduction and declined the usual flourish.|
N~A deliberately sparse notice. It tells us the purpose, not the person responsible.|
N~We will learn more from the people here than the sign.|
N~It feels strange after all the signs that want to tell us exactly whom to imagine.|
N~A clear name is useful. A welcoming person would be better.|
M~The playbill has listed the venue and withheld the cast.|
M~An unusually restrained sign. Almost suspiciously considerate of my attention span.|
N~Basic identification, little operational information. We will need to observe the rest ourselves.|
N~A door can carry a simple name and still open onto a complicated story.|
N~It leaves an impression through what it does not bother to say.|
N~I would look at the room beyond it before deciding what kind of place the title describes.
''')

