"""Replies to exact Hoenn town mottos and named public signs."""
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

add('sign_littleroot_no_hue','LittlerootTown_Text_TownSign',
    'Littleroot motto says the town cannot be shaded any hue.', '''
M~No hue? The grass has been making a rather persuasive case for green.|
N~An unusual motto. Perhaps they mean the town cannot be reduced to one impression.|
N~A place can be small without being easy to sum up.|
S~I like thinking home has room for more than the version we first remember.|
S~I would remember the people here before choosing a color for them.|
M~The town has politely declined the artist's entire palette.|
S~A town refusing to be neatly categorized. I can appreciate that.|
N~Literal reading fails immediately. We will have to allow the sign some poetry.|
S~A familiar place keeps changing colors when we return to it.|
M~A bold statement for a town with this much visible green.|
S~I would like to see the same street in different light before choosing its color.
''')
add('sign_oldale_scarce_start','OldaleTown_Text_TownSign',
    'Oldale advertises itself as a place where things begin scarce.', '''
M~An admirably honest slogan. Most towns make you visit the shops before discovering that part.|
N~A modest beginning still gives us useful points from which to learn.|
N~We can start with what is here. More is not always the first thing we need.|
S~A small beginning can leave room to notice who is beside you.|
N~A few good supplies and somewhere safe to rest can be enough to begin.|
M~The opening chapter has declared its limited production budget.|
S~Low expectations, plainly stated. Oddly reassuring.|
N~Scarcity makes planning important. Check what we need before heading out.|
S~A small first step is still a step into the world.|
N~Simple is fine. I hope nobody mistakes it for having nothing to offer.|
S~I like finding the details a grander slogan would overlook.
''')
add('sign_petalburg_nature','PetalburgCity_Text_CitySign',
    'Petalburg motto describes people mingling with nature.', '''
S~Mingling with nature. I hope the trees are better at small talk than I am.|
N~Living alongside something is different from treating it as background. A worthwhile idea.|
N~Then people should leave room for more than their own plans.|
S~I like a town that makes the natural world sound like company.|
S~A good neighborhood should have room for the creatures that were already here.|
S~Nature has been invited to the gathering rather than hired as scenery.|
M~I can manage a social event with trees. They rarely ask what my plans are.|
N~I would like to see how the city makes that motto practical.|
S~Roots and footsteps sharing a little ground.|
S~I hope they keep it as a habit, not only a nice phrase on a sign.|
S~I would look for the small places where people have made room for something growing.
''')
add('sign_rustboro_nature_science','RustboroCity_Text_CitySign',
    'Rustboro motto connects nature and science.', '''
M~Nature and science together. I hope science remembered to wipe its feet before coming in.|
S~Understanding nature should help us live with it, not give us an excuse to ignore it.|
N~Good aim. The results should be good for the people and Pokemon living here.|
N~I like the idea of learning about something because we want to care for it better.|
N~Useful work ought to remember who has to live beside it.|
S~The city has placed a very large question on a very small sign.|
N~A good partnership, provided nobody appoints themselves the only one allowed to speak.|
S~I would like to ask the people building things here what they have learned from the living parts.|
N~Knowing a thing's name is a beginning, not the whole of knowing it.|
N~I hope the attractive words have practical work behind them.|
N~I would look for the places where the two actually meet, rather than just photograph the slogan.
''')
add('sign_dewford_small_island','DewfordTown_Text_TownSign',
    'Dewford calls itself a tiny island in the blue sea.', '''
S~Tiny island, enormous amount of sea. Very sensible of the town to mark its location.|
N~A small place can have strong connections beyond its immediate shoreline.|
S~Small enough to learn the streets. Plenty of world beyond them.|
S~A little place surrounded by room to breathe.|
S~I like imagining how many people know each other's ordinary routines here.|
S~A small stage with an extravagant blue backdrop.|
S~A modest introduction. I appreciate a town that does not oversell itself.|
N~The limited land must make every useful bit of space matter.|
S~A little ground can hold a whole life.|
S~Tiny does not need to mean lacking. It depends what you want nearby.|
S~I would like to see which small corner someone here considers the whole heart of the place.
''')
add('sign_slateport_crossing_paths','SlateportCity_Text_CitySign',
    'Slateport calls itself a port where people and Pokemon cross paths.', '''
S~A whole city built around bumping into someone interesting. I hope apologizing counts as networking.|
S~Ports gather people with different routes and different reasons for traveling.|
N~Then keep an eye on the team. A busy place is still full of individuals.|
S~I like thinking a brief meeting can stay with someone after the paths separate.|
S~Some crossings become friendships. Some become directions to a good meal. Both useful.|
S~An ambitious intersection has grown streets, shops, and an audience.|
N~A busy place to be quiet in. I will stay near you.|
N~A lot of different journeys share the same infrastructure here. I would like to see how it works.|
S~Two roads can meet for a moment without becoming the same road.|
S~I like a city whose welcome leaves room for people who will not stay.|
S~I would ask visitors what they are carrying away besides what fits in their bags.
''')
add('sign_mauville_bright_fun','MauvilleCity_Text_CitySign',
    'Mauville advertises a bright shiny city of fun.', '''
M~Bright, shiny, fun. I hope the pavement is not expected to satisfy all three at once.|
N~A confident promise. I am curious which kind of fun the residents themselves prefer.|
N~We can enjoy it without doing everything the city offers.|
N~I would like to find the quieter sort of fun before the lights exhaust me.|
S~Somewhere to sit with a good snack would satisfy the slogan for me.|
M~Three enthusiastic adjectives have been elected to represent the whole city.|
M~I will look for the dim, matte corner where the fun has reasonable opening hours.|
S~Bright and shiny are easy to specify. Fun will need user testing.|
N~Even a city of light needs somewhere gentle to rest.|
S~Shiny can be lovely. It still helps to know what is underneath.|
N~I would ask a resident where they go when they do not feel like being entertained.
''')
add('sign_verdanturf_grass_fragrance','VerdanturfTown_Text_TownSign',
    'Verdanturf celebrates its windswept highlands and grass fragrance.', '''
S~A slogan for the nose. Finally, a sign working with the wind instead of against it.|
N~The air seems central to how people describe this place. I would like to hear what they notice.|
S~Fresh air and room to slow down. A good reason to stop.|
S~I like that the town introduces itself with a feeling before a list of achievements.|
S~A place where opening a window sounds like part of the attraction.|
S~The wind has been given a permanent role in the town's introduction.|
S~A breeze doing promotional work without asking anyone to smile.|
N~I wonder which plants contribute most to the scent people recognize.|
S~A familiar wind can make a place feel like home before the houses appear.|
S~A pleasant impression that does not need to be polished.|
S~I would want to remember the movement of the grass, not only its color.
''')
add('sign_fallarbor_small_gardens','FallarborTown_Text_TownSign',
    'Fallarbor describes a farming community with small gardens.', '''
S~Small gardens. Sensible. A giant garden would keep asking us to have a giant afternoon.|
S~Small plots can reflect a great deal of accumulated local knowledge.|
S~People tending something together. A good foundation for a town.|
S~I would like to know what someone planted because it reminded them of home.|
S~A good meal begins with somebody doing ordinary work in a garden.|
S~A modest setting with a great many patient stories growing inside it.|
S~Small gardens leave room to know each plant's particular complaints.|
N~I would ask which methods suit the conditions here. Practical local experience matters.|
S~A small patch tended often can hold more care than a broad field ignored.|
S~I like a place proud of something that needs regular attention.|
S~I would ask a gardener which corner they would show a visitor first.
''')
add('sign_lavaridge_relaxation','LavaridgeTown_Text_TownSign',
    'Lavaridge advertises the Pokemon Center hot springs as a place to relax.', '''
S~An entire town recommending sitting in warm water. I feel understood by the local government.|
N~A chance to rest is useful. We should not confuse relaxing with staying in the heat indefinitely.|
S~A break sounds good. We have earned one.|
S~I like a destination that does not immediately ask us to improve at something.|
S~Warm water, then a proper meal. I could make a very complete afternoon of that.|
S~The itinerary has generously included an intermission.|
S~A public invitation to stop being productive for a little while. Excellent civic policy.|
N~I would like to know how they maintain the springs. After we enjoy the sitting part.|
S~A place that offers warmth without asking us to burn.|
S~Relaxing should not feel like another thing to perform correctly. We can just enjoy it.|
S~I would leave the camera put away for a little while and remember being there.
''')
add('sign_fortree_treetop_life','FortreeCity_Text_CitySign',
    'Fortree describes a treetop city frolicking with nature.', '''
M~Frolicking in the treetops. I will begin with the less ambitious art of using the walkway.|
N~A city built among living things must keep adapting as those things grow.|
N~Watch your footing. Admire the view after finding a steady place.|
S~I like hearing the town described as part of the trees instead of above them.|
N~I hope everybody gets help carrying the awkward things up to their homes.|
M~The scenery has accepted the entire cast into its branches.|
M~I am available for a restrained frolic near a reliable railing.|
S~I would like to inspect the supports. Living foundations make an interesting design problem.|
S~A home can be held by something still growing.|
N~A lovely idea. I am choosing shoes for the walkways rather than the slogan.|
S~I would like to see what a resident sees when they step outside before the city wakes.
''')
add('sign_lilycove_land_and_sea','LilycoveCity_Text_CitySign',
    'Lilycove motto marks where the land ends and sea begins.', '''
M~The land ends here. Very helpful of the sign to warn my shoes.|
N~The boundary is also a connection. Much of a coast's life comes from both sides.|
N~A good place to stop and decide which way we want to go next.|
S~An ending from one direction is a beginning from the other. I like that.|
S~I would like to share a meal somewhere we can hear both the town and the water.|
S~The edge of one setting opens directly into another. An economical transition.|
S~A place with permission to look unfinished in one direction.|
N~I wonder how the city plans around a boundary that never sits perfectly still.|
S~A shore belongs to the meeting, not only to either side.|
S~I like a place that gives the horizon a little room.|
S~I would want the town in the picture, too, not just the view it looks out on.
''')
add('sign_mossdeep_cherish_pokemon','MossdeepCity_Text_CitySign',
    'Mossdeep slogan asks people to cherish Pokemon.', '''
S~Cherish Pokemon. A short slogan with enough work inside it to fill the whole day.|
N~A worthwhile principle. I would judge it by the everyday care it produces.|
S~Good words. Keep them true when the Pokemon is tired or inconvenient, too.|
S~I like that the welcome asks something kind instead of something impressive.|
S~Care should include the ordinary days when nobody is watching.|
S~The city has given itself a simple line and a lifelong performance to match.|
S~A promise I would like to see kept on the difficult afternoons.|
N~A clear goal. The practical details are where it becomes real.|
S~A small creature should feel the truth of those words without needing to read them.|
S~I hope the slogan includes the ones who are not especially cute or useful.|
S~I would look for a quiet act of care that nobody expected a visitor to notice.
''')
add('sign_sootopolis_sleeping_history','SootopolisCity_Text_CitySign',
    'Sootopolis calls itself a mystical city where history slumbers.', '''
M~History is sleeping. We should probably stop reading the sign so loudly.|
N~An evocative motto. I would like to know which parts of the history residents still live with.|
N~We can respect an old place without treating its people like part of an exhibit.|
S~I wonder what ordinary memories sit beside the stories visitors come to hear.|
N~Someone still has to make breakfast in a city with a grand past.|
S~A setting has promised an old story while keeping its first page carefully closed.|
S~Sleeping history. A much gentler arrangement than history knocking on the door.|
N~I would separate what is documented from what is remembered as legend. Both deserve clear names.|
S~Old things can rest beneath the shape of an ordinary day.|
N~Mystery is lovely. So is letting the residents have a life beyond it.|
S~I would ask what a person here hopes future visitors will remember about their time.
''')
add('sign_pacifidlog_morning_sun','PacifidlogTown_Text_TownSign',
    'Pacifidlog celebrates morning sunlight smiling on the water.', '''
S~A smiling morning sun. Mine usually arrives with a much less polite announcement from my stomach.|
S~Light on moving water changes constantly. It must make familiar mornings feel different.|
S~A good view to wake up to. Watch the boards before admiring it.|
S~I would like one morning with no hurry except getting outside before the light changes.|
S~Breakfast beside that water sounds like a very good start.|
S~The town has hired the sunrise to deliver its daily opening scene.|
M~I would appreciate the smile more if it arrived slightly later in the morning.|
N~I wonder how much the changing light helps residents read the water.|
S~The same sun finds a new path across the waves each day.|
S~Some views do not need an elaborate introduction. This one still got a nice one.|
S~I would get up early for that. Quietly, so nobody mistakes it for a new habit.
''')
add('sign_ever_grande_paradise','EverGrandeCity_Text_CitySign',
    'Ever Grande describes a paradise of flowers, sea and Pokemon.', '''
S~Flowers, sea, Pokemon. A very persuasive list missing only the place to have lunch.|
S~A memorable setting. I hope people leave room to enjoy it alongside the challenge ahead.|
N~Take a moment to look around. We did not come this far only to hurry past it.|
S~I like having something gentle waiting beside something that matters so much.|
S~We should give the team a peaceful moment here before asking anything more.|
S~The final approach has remembered that beauty can matter beside ambition.|
S~A paradise placed beside a test. I vote we notice both.|
N~A pleasant environment does not remove the need for preparation. We can appreciate it while checking.|
S~Even at the edge of a great challenge, flowers are allowed to bloom for no reason at all.|
S~We are allowed to remember the place, not only the result we hope to earn here.|
S~I would like a picture of the team before the next door, with the flowers still part of it.
''')

add('sign_norman_power','PetalburgCity_Text_GymSign',
    'Norman Gym sign describes him as pursuing power.', '''
M~A man in pursuit of power. It would be a much stranger motto over the kitchen door.|
N~Power is a broad goal. I am more interested in what he wants to do with it.|
N~We can meet the trainer behind the words instead of arguing with the sign.|
N~It is strange seeing someone familiar introduced as a public figure.|
N~I hope he makes room for the people who want his company as well as his skill.|
N~A father's ordinary name has acquired a rather formidable subtitle.|
M~Your family introduction comes with a competitive warning label.|
N~I would ask him what measure of progress he actually uses.|
N~A pursuit can lead somewhere, or keep someone from seeing what is already beside them.|
N~He gets to be more than the slogan. So do you.|
N~I wonder how differently you read that sign from a visitor who has never met him.
''')
add('sign_roxanne_student','RustboroCity_Text_GymSign',
    'Roxanne Gym sign celebrates a Rock-loving honors student.', '''
M~An honors student who gets to drop rocks on the examiners. An ambitious education.|
S~Her studies became a way to work with the Pokemon she loves. That is a good connection.|
N~Good credentials. We will still pay attention to how she actually battles.|
S~I like that loving something and studying it belong in the same introduction.|
S~I hope she gets to enjoy the work without feeling she must always be the best student.|
S~A distinguished academic record has found a very practical examination room.|
M~She has put her interests on the sign. An effective filter for people bored by rocks.|
S~Applying study in the field. I would like to know which lesson surprised her most.|
S~She has followed a small fascination far enough to build a place around it.|
S~A confident introduction that still lets her be enthusiastic about what she likes.|
N~I would look for the little signs that she still enjoys learning, not only being accomplished.
''')
add('sign_brawly_big_wave','DewfordTown_Text_GymSign',
    'Brawly Gym sign calls him a big wave in fighting.', '''
M~A big wave in fighting. I hope the entrance fee does not include getting splashed.|
N~The metaphor promises force and momentum. I would like to see the technique behind it.|
N~We can prepare for a strong fighter without letting the sign intimidate us.|
N~I would rather know the person before deciding how frightening the wave is.|
N~A strong challenge still needs a team that feels ready for it.|
M~The local action hero has a suitably dramatic coastal billing.|
M~I will approach with the quiet dignity of someone checking where the exits are.|
N~An energetic introduction. It is not a substitute for a tactical briefing.|
N~Even a large wave has a rhythm. We can learn to see it.|
N~A vivid image. I would like to meet the person who gets to live with it every day.|
N~I wonder whether the town chose that phrase or he did.
''')
add('sign_wattson_cheerful_electric','MauvilleCity_Text_GymSign',
    'Wattson sign calls him cheerfully electrifying.', '''
M~Cheerfully electrifying. Two words I would prefer kept apart when somebody shakes my hand.|
S~A bright personality can make a difficult challenge feel more welcoming.|
N~He sounds friendly. We should still take the electrical part seriously.|
S~I like the thought of a strong opponent who is happy we came.|
S~Someone who enjoys the work can make everyone around them more comfortable.|
M~The comedy and the special effects appear to share one enthusiastic operator.|
M~A cheerful man with access to electricity. The sign has responsibly warned us.|
N~I am interested in the systems. I am cautiously optimistic about the host.|
S~A warm welcome does not always arrive quietly.|
S~He sounds like someone who will be difficult to forget.|
S~I wonder whether his ordinary laugh is as memorable as the sign wants us to expect.
''')
add('sign_flannery_passion','LavaridgeTown_Text_GymSign',
    'Flannery sign celebrates her burning passion.', '''
M~A fiery passion that burns. The sign has left very little room for a cooling interpretation.|
N~Enthusiasm matters. I would like to see how she turns it into good decisions for the team.|
N~Take the passion seriously. Do not mistake excitement for a lack of skill.|
N~I hope she gets to have quieter days without disappointing the sign.|
S~It is good to love the work. It is also good to have someone make sure you rest.|
M~An energetic lead has been introduced with enough fire for three promotional posters.|
N~That is a lot of intensity to be asked to embody before breakfast.|
N~Heat makes a vivid metaphor. The practical test is how she uses it.|
N~A flame needs care if it is going to last.|
N~She should get to be more than the loudest description of her.|
N~I would like to hear her describe herself without the slogan doing it first.
''')
add('sign_winona_world_flight','FortreeCity_Text_GymSign',
    'Winona sign describes a bird user taking flight into the world.', '''
S~Taking flight into the world. I will start by taking the stairs without embarrassing myself.|
S~A fitting image for someone whose work centers on Flying Pokemon.|
N~A wide world ahead. We still need to watch the next step.|
S~I like the possibility in that phrase. It sounds like she is still going somewhere.|
S~A home can be a place to return to without being a place that holds you still.|
S~Her introduction has given the horizon a part in the story.|
S~A lovely ambition. I hope she is allowed a quiet landing now and then.|
N~I would like to know how working with birds changed her idea of distance.|
S~A wing belongs to the sky and to the creature that chooses where to go.|
S~It leaves room for her to keep growing beyond the title. I like that.|
S~I wonder what she hopes to see when she is the traveler instead of the person welcoming one.
''')
add('sign_twins_mystic_combination','MossdeepCity_Text_GymSign',
    'The twins sign calls Liza and Tate a mystic combination.', '''
M~A mystic combination. I hope the door does not ask us to provide an equally impressive partner title.|
N~A partnership is part of their public identity. Coordination will be worth watching.|
N~Two leaders. We should think about how the whole team works together.|
N~I wonder what it feels like to be introduced as half of something before anyone meets you.|
N~I hope both of them have space to be themselves inside the partnership.|
M~A double billing with a shared promise of the inexplicable.|
M~We should prepare a combination of our own. I suggest you, me, and a sensible plan.|
N~The interaction between two systems can matter more than their individual outputs.|
N~Two lights can meet without becoming one flame.|
N~A memorable pair should still have room for two distinct people.|
N~I would like to notice the differences as carefully as the similarities.
''')
add('sign_juan_water_beauty','SootopolisCity_Text_GymSign',
    'Juan sign praises his beauty as pure water.', '''
M~The beauty of pure water. I have mostly encountered water looking suspiciously like my own wet face.|
N~A graceful image. I would still judge his training by more than presentation.|
N~An elegant introduction does not tell us the whole battle plan.|
N~I hope he enjoys being himself as much as everyone enjoys describing him.|
N~Water can be gentle and strong. I would like to see both given their due.|
M~The leading man has received an exceptionally flattering contribution from the sign writer.|
M~An enviable review. My own reflection has been less cooperative.|
N~Presentation is clearly part of the experience. I am interested in the method beneath it.|
N~Clear water can show depth without making a sound.|
S~A beautiful image. It leaves a little room to decide what beauty means for ourselves.|
N~I would like to see him in an ordinary moment before asking him to match the portrait.
''')
add('sign_gym_symbol_lesson','PetalburgCity_Text_ThisIsGymSign',
    'The explanation identifies the sign used for Pokemon Gyms.', '''
S~A sign explaining how to find signs. We have reached the foundations of adventuring.|
N~A recognizable symbol is useful when the town and its layout are unfamiliar.|
N~Good to know what to look for when we need the next Gym.|
N~I like instructions that assume we might be new without making it embarrassing.|
N~A clear landmark can save a tired team a lot of wandering.|
M~The tutorial has briefly introduced the scenery's own method of introducing itself.|
M~I appreciate a symbol that does not change its mind in every town.|
S~Consistent signage. Quietly important design work.|
N~A small familiar mark can make a new road less uncertain.|
N~Useful, clear, and easy to remember. A good sign doing its job.|
N~I will watch for that shape before trying to memorize every street.
''')
add('sign_dewford_hall_exchange','DewfordTown_Text_HallSign',
    'Dewford Hall advertises an information exchange for everyone.', '''
M~An information exchange. I hope my vague recollections qualify as a useful contribution.|
N~Sharing information is valuable. Knowing where it came from helps keep it valuable.|
N~Listen first. We do not need to believe every confident voice in the room.|
S~I like a place where somebody can come just to hear what other people have noticed.|
S~A familiar room to talk in can be as important as the things people say.|
M~A public stage on which gossip has requested the more dignified title of information.|
M~Everyone's exchange. Including the person who is completely certain about something completely wrong.|
N~I would start by asking how they check the facts they pass along.|
S~A small town can send one thought through a great many lives.|
N~I hope there is room for the person who has not found the right words yet.|
S~I would like to hear the conversation before deciding which voice describes the whole room.
''')
add('sign_lilycove_contest_gathering','LilycoveCity_Text_ContestHallSign',
    'The Contest Hall sign calls it a gathering place for trainers.', '''
S~A gathering of trainers. I hope the waiting room has enough space for everyone's dramatic entrance.|
N~A shared venue lets people compare very different ways of working with their Pokemon.|
N~We can watch and learn without having to enter immediately.|
S~I would like to see the quiet preparation as well as the big performance.|
S~I hope the teams get encouragement when they are done, whatever the result.|
S~A hall devoted to people who have decided their partners deserve an audience.|
N~I am prepared to admire from somewhere that does not require introducing myself.|
N~I would be interested in the practical preparation behind an apparently effortless performance.|
N~A bright moment rests on many small, unseen ones.|
S~Now that is a place to notice how personality changes the same basic idea.|
S~I would want a picture of a trainer looking proudly at their partner after the performance.
''')

