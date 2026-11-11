"""Exact shared-object states and source-reviewed contact confirmations."""
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

add('roxanne_contact_added','RustboroCity_Gym_Text_RegisteredRoxanne RustboroCity_Gym_Text_RoxanneRegisterCall',
    'Roxanne has been registered as a PokeNav contact after inviting future challenges.', '''
S~Roxanne has joined the contacts. I hope the next call does not come with a surprise exam.|
S~I would enjoy hearing which part of her training she is reconsidering.|
S~We can keep in touch and give her a proper rematch when both teams are ready.|
S~It is nice to know someone from an earlier part of the journey still remembers us.|
S~A battle has become a way to stay acquainted. I like that.|
S~The first Gym chapter has retained a speaking part in the rest of the story.|
S~A rematch invitation sounds much nicer than a grudge.|
N~It will be useful to hear when her revised team is ready for testing.|
S~A place we left behind has kept a thread tied to the road.|
S~I like that she reached out instead of waiting to be forgotten.|
S~I wonder how different both teams will look when we meet again.
''')
add('brawly_contact_added','DewfordTown_Gym_Text_RegisteredBrawly',
    'Brawly is now a registered PokeNav contact.', '''
S~Brawly is in the contacts. I hope the signal can carry that much enthusiasm without getting wet.|
S~Keeping contact gives us a chance to compare progress rather than remember only one result.|
S~Good opponent to keep in touch with. He takes a challenge seriously.|
S~The sea between towns feels a little smaller when somebody can call.|
S~I would like to hear how his team is doing after some rest.|
S~Our island encounter has acquired an ongoing correspondence.|
M~I expect the sea metaphors to travel very well over the phone.|
N~A direct way to arrange another test when both teams have changed.|
S~A friendly voice can cross water without needing a boat.|
S~It is nice leaving with a way to say hello again.|
S~I hope a future call catches him enjoying an ordinary day by the sea.
''')
add('wattson_contact_added','MauvilleCity_Gym_Text_RegisteredWattson',
    'Wattson is now a registered PokeNav contact.', '''
M~Wattson can call us now. I trust the little speaker has been tested against his laugh.|
S~I would be interested in hearing how he improves his next team.|
S~Good. We can hear when he is ready without trying every door in Mauville again.|
S~His laugh would be a nice thing to hear on an unfamiliar road.|
S~I hope we get to tell him the team is doing well.|
M~A memorable guest has been granted future access to the sound system.|
M~I am prepared to hear the phone laugh before it rings.|
N~A useful contact. I also have several unanswered questions about his switch circuits.|
S~A bright voice has found a small place in our pocket.|
S~I like having a reason to remember him beyond the electrical obstacles.|
S~I wonder what ordinary part of the city he would talk about if we asked.
''')
add('flannery_contact_added','LavaridgeTown_Gym_1F_Text_RegisteredFlannery',
    'Flannery is now a registered PokeNav contact.', '''
S~Flannery is in the contacts. A much cooler way to keep in touch than standing in the sand.|
S~I would like to hear how her approach changes as she settles into leading the Gym.|
S~We can give her another good challenge when she is ready.|
S~It is nice to leave her with a familiar voice to call, not just a challenger who passed through.|
S~I hope she has people to talk to when leading the Gym feels difficult.|
S~A new leader has gained one more connection beyond the room she is trying to fill.|
S~I hope the next conversation feels a little less like something she has to perform correctly.|
N~Her next team will show what she learned from this one. Worth keeping in contact.|
S~A warm welcome can continue after we leave the heat behind.|
S~She seems more comfortable when she can simply be enthusiastic. I hope we hear that again.|
S~I would like to know what she feels proud of in her own work next time.
''')
add('winona_contact_added','FortreeCity_Gym_Text_RegisteredWinona',
    'Winona is now a registered PokeNav contact.', '''
S~Winona can call us. I hope we do not have to rotate the phone through three doors to answer.|
S~A chance to hear how the bird team develops between visits.|
S~We can keep in touch without turning every visit into a challenge.|
S~I would like to hear what Fortree sounds like on an ordinary afternoon.|
S~I hope she gets to talk about the birds she loves, not only their battle record.|
S~The road has carried away the visitors without quite ending the scene.|
S~A quiet call from somewhere high in the trees sounds rather nice.|
N~It will be useful to compare how her team adjusts after new opponents.|
S~A voice can travel farther than wings and still find a familiar place.|
S~I like leaving a place with a connection instead of only a keepsake.|
S~I wonder which view she misses when she travels away from Fortree.
''')
add('twins_contact_added','MossdeepCity_Gym_Text_RegisteredTateAndLiza',
    'Tate and Liza are now registered PokeNav contacts.', '''
M~Two leaders, one contact entry. I hope they have agreed who says hello first.|
S~It will be interesting to hear how they discuss a plan outside the battle itself.|
S~Good pair to keep in touch with. They take teamwork seriously.|
F~I wonder whether they finish each other's sentences over the phone, too.|
S~I hope both of them get to tell us how their Pokemon are doing.|
M~The double act has booked future appearances through one very economical listing.|
M~I will try not to lose my place if the greeting arrives in two voices.|
N~Two coordinated perspectives could make reviewing a rematch quite useful.|
S~Two voices can make a familiar place feel near again.|
S~I like the idea of hearing the little differences between them as we get to know them.|
S~I would ask what each remembers differently about the same battle.
''')
add('juan_contact_added','SootopolisCity_Gym_1F_Text_RegisteredJuan',
    'Juan is now a registered PokeNav contact.', '''
M~Juan has our number. I am budgeting several extra minutes for the greeting.|
S~I would be interested in the training choices behind all that practiced elegance.|
S~We can keep in touch. It need not become a ceremony every time.|
S~I hope the next conversation feels a little less like standing in a grand room.|
S~I would like to hear which part of teaching he enjoys most.|
M~A man with a splendid sense of occasion has acquired access to the portable stage.|
M~I will dress my voice appropriately before answering.|
N~He has a great deal of experience. A specific question might uncover something useful.|
S~A distant city can return in the sound of someone who belongs to it.|
M~I am prepared for the call to arrive wearing a very impressive coat.|
S~I wonder what he notices about Sootopolis when he has a quiet moment to himself.
''')

