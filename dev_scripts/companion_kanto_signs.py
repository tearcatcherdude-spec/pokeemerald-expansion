"""Exact Kanto mottos, public signs and Pokemon exhibit descriptions."""
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

add('sign_pallet_journey_shades','PalletTown_Text_TownSign',
    'Pallet sign says the shades of our journey await.', '''
S~The journey has shades waiting. I hope one of them is the kind under a nice tree.|
S~A beginning with room for experiences we cannot yet predict.|
N~We will find out what it means by going. No need to have the whole road decided.|
S~I like a welcome that leaves space for us to become different.|
S~Some of the best parts will be ordinary things we did not plan to remember.|
S~A promising first line, with the rest of the page left to the traveler.|
S~A little ambiguity on a sign. I am prepared to call it poetry.|
N~I would keep room in the plan for something we have not thought of yet.|
S~A road changes color through the person who walks it.|
S~I hope we get to choose some of those shades ourselves.|
S~I would like to remember the beginning without making it pose as the whole story.
''')
add('sign_viridian_green_paradise','ViridianCity_Text_CitySign',
    'Viridian calls itself the eternally green paradise.', '''
M~Eternally green. The plants have received a very demanding long-term assignment.|
N~A living landscape needs continual care. Eternally is doing a great deal of work there.|
N~A good aim. Keep the green parts healthy instead of only pointing at them.|
S~A place that wants to keep something gentle about itself. I like that.|
N~I hope the word paradise includes the creatures who have to live beside the streets.|
M~The town has announced an unusually ambitious contract with the seasons.|
S~A green place can make a difficult day feel less sharp around the edges.|
N~I would be interested in how they maintain the planting, not just the promise.|
S~Green is a living thing, not a color that stays because a sign requested it.|
N~A beautiful claim. I hope the ordinary work receives some credit.|
S~I would look for the little corners someone clearly took the time to tend.
''')
add('sign_pewter_stone_gray','PewterCity_Text_CitySign',
    'Pewter introduces itself as a stone gray city.', '''
S~Stone gray. An introduction that has chosen reliability over glitter.|
N~Gray can reveal a surprising range of material and texture when you look closely.|
N~A place does not need bright colors to have something worth noticing.|
S~I like quiet colors. They leave room for small differences to be seen.|
S~The people can provide the warmth. The buildings need not do all of it.|
S~A restrained palette leaves the characters room to arrive in their own colors.|
S~A city with the confidence to look a little overcast. Respectable.|
N~I would like to know which local materials shaped the look of the buildings.|
S~Stone keeps more shades than a hurried glance gives it.|
S~Gray is only dull when nobody bothers with the details.|
S~I would wait for the light to change before deciding the city has shown us its color.
''')
add('sign_cerulean_blue_aura','CeruleanCity_Text_CitySign',
    'Cerulean sign describes a mysterious blue aura around the city.', '''
M~A mysterious blue aura. I had not budgeted for the atmosphere having an opinion.|
N~An evocative description. I would like to see what residents mean by it in everyday terms.|
N~We can enjoy the impression without having to solve the whole town.|
S~I like an introduction that feels more like a mood than an achievement.|
N~I hope the mystery still leaves room for somewhere straightforward to have lunch.|
S~The setting has announced its lighting before introducing its cast.|
M~A blue aura is a pleasant change from my usual aura of having forgotten something.|
N~I would begin by separating a visual effect from the story people attach to it.|
S~Some places feel a color before we find a name for why.|
S~A little mystery can be a good first impression if it does not do all the talking.|
S~I would want to see it in ordinary daylight before chasing the dramatic version.
''')
add('sign_lavender_noble_purple','LavenderTown_Text_TownSign',
    'Lavender calls itself the noble purple town.', '''
S~A noble purple. I will try to walk through it with a reasonably respectable amount of dignity.|
S~A quiet, deliberate introduction. I would like to know what the name means to people here.|
N~A place can be dignified without asking everyone to feel the same way.|
S~Purple can feel gentle without becoming cheerful on command.|
N~I hope visitors remember there are ordinary lives behind the town's reputation.|
S~The town has chosen a color that can hold more than one mood.|
S~A name that does not demand a bright smile from everyone passing through.|
N~I am interested in the local meaning behind that word noble.|
S~Some colors leave room for memory without closing the door to the present.|
S~A quiet richness. It does not need to prove itself by shining.|
N~I would ask a resident which ordinary corner they would want us to remember.
''')
add('sign_vermilion_sunsets','VermilionCity_Text_CitySign',
    'Vermilion advertises exquisite sunsets at its port.', '''
S~Exquisite sunsets. A port that has arranged for the sky to handle the evening entertainment.|
S~Even a familiar view changes with the light and the weather. Worth returning to.|
S~We should leave a little time to see it instead of only reading the promise.|
S~I would like one evening without needing to get somewhere before the light goes.|
S~A simple meal beside the water would do nicely.|
S~The town has given its closing scene a very generous lighting budget.|
S~A public attraction that does not require me to become interesting at it. Excellent.|
N~I would like to see how the port keeps working while the visitors stop to look.|
S~An ending can be a reason to gather instead of a reason to hurry.|
S~Some colors deserve a little of our time instead of a better slogan.|
S~I would stay after the brightest moment. People often leave before the gentler colors arrive.
''')
add('sign_celadon_rainbow_dreams','CeladonCity_Text_CitySign',
    'Celadon calls itself the city of rainbow dreams.', '''
M~Rainbow dreams. I hope the prices do not expect us to pay in actual rainbows.|
N~A place can hold many ambitions. I would like to hear which ones the residents actually chose.|
N~Keep hold of what you want before a busy city starts offering to choose for you.|
S~I like the idea that there is room for more than one kind of dream.|
N~I hope the people doing ordinary work get to have their dreams counted, too.|
S~A bright invitation to arrive with a story that is not yet finished.|
M~A large dream, advertised in a place very good at selling smaller temptations.|
N~I would like to know what practical support sits behind the colorful promise.|
S~A rainbow has room between its brightest colors, too.|
S~I like a city that admits people want different things.|
N~I would ask someone what they came here hoping for, then what they found instead.
''')
add('sign_fuchsia_passion_pink','FuchsiaCity_Text_CitySign',
    'Fuchsia enthusiastically introduces its passion pink color.', '''
M~Passion pink! The sign has arrived with the confidence of an entire parade.|
N~An energetic introduction. I am curious how the town arrived at that particular identity.|
N~A bold welcome. We can find our own pace inside it.|
F~I was not ready to be greeted with an exclamation about a color.|
S~Somebody clearly enjoyed writing that. I hope the town is as welcoming.|
M~The setting has made a very emphatic entrance before anyone could lower the curtain.|
M~I respect a color that introduces itself more decisively than I introduce myself.|
N~High visibility. I can at least say the sign is difficult to overlook.|
S~A bright flower has lent its name to a whole place.|
S~Pink with conviction. I see no reason it should apologize.|
S~I would look for the small detail that makes someone here feel the color belongs to them.
''')
add('sign_saffron_golden_commerce','SaffronCity_Text_CitySign',
    'Saffron advertises a shining golden land of commerce.', '''
M~Golden land of commerce. Even the welcome seems aware of its resale value.|
N~Trade can connect a great many lives. It should not become the only way the city measures them.|
N~Keep track of what we actually need. A confident sales pitch is still a sales pitch.|
N~I would like to find the places people come to without needing to buy something.|
N~Somebody has to make a home here after the shops close. That matters, too.|
M~A city has introduced itself with the polished language of its own business proposal.|
M~An exceptionally well-dressed way of asking whether we brought money.|
N~I would be interested in the systems that move goods through a place this busy.|
N~A shining surface still has quiet lives beneath it.|
N~Gold is striking. I hope there are other colors in the way people treat one another.|
N~I would want to remember the people who keep it running, not only the impressive buildings.
''')
add('sign_cinnabar_burning_desire','CinnabarIsland_Text_IslandSign',
    'Cinnabar describes a fiery town of burning desire.', '''
M~Burning desire. I have a very strong desire to know where the cooler rooms are.|
N~A forceful metaphor. I would like to know what people here actually want to build or learn.|
N~Enthusiasm is fine. Keep enough sense to look after the team.|
N~I hope the town has room for a quiet ambition, too.|
N~A strong appetite for life still needs a proper rest between adventures.|
M~The introduction has used most of the available fire before the actors even arrive.|
M~I will contribute a modest smolder rather than promise more intensity than I have.|
N~I would prefer to understand the local work before adopting its dramatic temperature.|
N~A fire can warm a life or consume it. The tending matters.|
N~I like passion best when it leaves someone comfortable enough to keep enjoying it.|
N~I would ask what somebody here loves on an ordinary afternoon, without the dramatic wording.
''')

