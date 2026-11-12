"""Source-reviewed Hoenn exhibits, fixed object descriptions, and public notices."""
ROWS = []
EMOTIONS = dict(N='neutral', S='soft_smile', A='annoyed', F='flustered', D='sad', U='surprised', M='smug', L='laughing')

def add(key, labels, subject, lines):
    replies = [x.strip() for x in lines.strip().split('|')]
    replies = [EMOTIONS[x[0]] + x[1:] for x in replies]
    assert len(replies) == 11, (key, len(replies))
    ROWS.append(dict(key='hob_'+key, labels=labels.split(), subject=subject, replies=replies))

add('whirlpool', 'SlateportCity_OceanicMuseum_1F_Text_WhirlpoolExperiment', 'Wind drives blue fluid into an artificial whirlpool in a glass vessel.', '''
U~A little whirlpool with no boats to trouble. A surprisingly well-behaved version.|
S~The contained model makes the effect of wind easier to observe. Elegant demonstration.|
N~Good place to learn what the motion looks like. Better than from inside it.|
N~I could watch that turn for a while. It's calmer with glass between us.|
S~A large danger made small enough to understand over a quiet afternoon.|
S~The sea's dramatic habits have been persuaded to perform in a jar.|
S~A contained spiral. My preferred arrangement for things that pull you under.|
U~I'd like to see how changing the airflow changes the shape.|
N~The little current keeps circling a place it never quite reaches.|
S~The blue makes the motion easy to follow. A good display choice.|
N~I'd watch where the spiral starts and compare it with the air above it.
''')
add('waterfall', 'SlateportCity_OceanicMuseum_1F_Text_WaterfallExperiment', 'A bobbing red ball demonstrates buoyancy in a waterfall model.', '''
S~That ball has a very busy afternoon and absolutely no progress to show for it.|
N~Buoyancy provides a visible way to follow the flow. The red contrast helps.|
N~A useful model. We can watch without getting swept anywhere.|
S~It keeps coming back up. There's something quietly pleasing about that.|
S~That little red ball is working harder than most of the visitors.|
S~A hardworking performer, committed to the same entrance several hundred times.|
S~An endless cycle, attractively presented and mercifully happening to a ball.|
U~The tracer makes the forces visible. I'd like to examine the circulation.|
N~Down and up again, with the water deciding the route.|
S~They chose the red well. Nothing else competes for the eye.|
N~I'd follow one full cycle rather than just catch the movement at a glance.
''')
add('ocean_soil', 'SlateportCity_OceanicMuseum_1F_Text_OceanSoilDisplay', 'Layered ocean sediment preserves remains that reveal the ancient past.', '''
U~A handful of seabed turns out to be an extremely untidy old diary.|
S~Successive layers preserve different periods. Their order is part of the evidence.|
N~Easy to overlook dirt. Harder once you know what it remembers.|
N~I like the thought of a quiet layer keeping something small from being forgotten.|
N~Something that looks ordinary can hold a very long story.|
S~The past has filed its records under the sea, an inconvenient but effective archive.|
S~History, compressed beneath water and considerable patience.|
U~I'd want to see how they collect a sample without mixing the layers.|
N~Small lives settle into the same dark, and time makes room above them.|
N~The plain sample becomes more interesting after the label gives us a way to look.|
N~I'd ask what this particular layer revealed, not just what samples can reveal generally.
''')
add('beach_sand', 'SlateportCity_OceanicMuseum_1F_Text_BeachSandDisplay', 'The sand display traces beach grains back to mountain rocks carried by rivers.', '''
U~The beach is full of extremely well-traveled bits of mountain. I owe it more respect.|
S~Transport and abrasion connect the mountain material to these much smaller grains.|
N~Long journey for something we usually shake out of a shoe.|
N~I hadn't thought of sand as something that came all that way.|
S~The river does a lot of preparation before the beach ever sees the result.|
S~A mountain has spent years arriving at the shore in very small installments.|
S~Even the sand has gone on a longer trip than it admits.|
U~I'd compare the grain shapes with samples farther upstream.|
N~A hard thing becomes small enough for the water to carry gently.|
N~Texture has a history. That makes even plain sand feel less interchangeable.|
S~I'd like to see the whole route, from the rocks to the beach, through a few careful samples.
''')
add('sea_blue', 'SlateportCity_OceanicMuseum_1F_Text_OceanicMinifact1', 'A museum panel explains the blue appearance of seawater through light passing through it.', '''
N~The sea borrowed a whole lesson about light just to choose an outfit. Thorough.|
N~The explanation concerns how light behaves in water. Color carries information about the medium.|
N~Useful reminder that what we see depends on what the light passed through.|
N~I like knowing a little more without having to stop finding it beautiful.|
S~A familiar blue has a lot going on beneath it. Nice reason to look again.|
S~The ocean's famous color has submitted an explanation instead of simply accepting compliments.|
S~A beautiful effect with a perfectly serious mechanism underneath. Relatable.|
U~I'd enjoy a display that lets us compare light through different depths of water.|
N~A color can belong partly to the distance it traveled.|
S~Knowing how the blue happens doesn't make me want to use it any less.|
N~I'd watch how the water's color changes near shore after reading that.
''')
add('sea_salt', 'SlateportCity_OceanicMuseum_1F_Text_OceanicMinifact2', 'The panel describes dissolved salts carried from rocks into the sea.', '''
U~So the sea has been collecting tiny rock ingredients this whole time. No wonder it tastes ambitious.|
N~The panel connects dissolved ions with material transported from land. A useful large-scale link.|
N~Water carries things we can't see. Worth remembering.|
N~It's strange how something invisible can change the whole taste of a place.|
S~A little salt goes a long way. The ocean has been taking that advice very generously.|
S~The rocks have contributed to the sea's seasoning over an impressively long preparation time.|
S~A planetary collection of dissolved leftovers. Surprisingly photogenic result.|
U~I'd compare samples where rivers enter the sea with samples farther out.|
N~The land leaves a trace even in water that seems to have gone beyond it.|
N~An invisible ingredient changes an enormous impression. I like that detail.|
N~I'd ask what varies between the samples upstairs. This gives us a good question to carry there.
''')
add('sea_area', 'SlateportCity_OceanicMuseum_1F_Text_OceanicMinifact3', 'The panel says sea covers about seventy percent of the planet.', '''
U~All that land we've walked on is the smaller part. My feet are taking the news personally.|
N~The stated proportion makes the ocean the dominant surface environment. Perspective changes quickly.|
N~Most of the world is water. Good reason to respect the people who know it.|
N~That makes the horizon feel a little farther away than it did before.|
N~A small patch of dry ground can feel enormous until somebody shows the whole picture.|
N~The land has been rather successful at making itself feel like the main attraction.|
N~A mostly aquatic planet with a remarkably opinionated dry minority.|
U~I'd like to compare the ocean coverage with a globe rather than a flat panel.|
N~We stand on the smaller part and name the larger part the edge.|
N~It's an easy proportion to read and a difficult scale to really imagine.|
U~I'd love to ask a sailor what that number feels like after days beyond sight of land.
''')
add('ripple_fossil', 'SlateportCity_OceanicMuseum_1F_Text_FossilDisplay', 'Fossilized ripples preserve marks left by ancient flowing seawater.', '''
U~The water left, but its little wrinkles stayed behind. That's very stubborn evidence.|
S~The preserved structure records a process, even without preserving the water itself.|
N~You can learn what moved here from the mark it left. Useful.|
N~It looks almost soft until I remember it's stone.|
N~A moment of movement has lasted far longer than anyone standing in this room.|
S~The ancient current has provided a signed impression in lieu of attending the exhibition.|
S~A wave that finally agreed to sit still. It took becoming rock.|
U~I'd want to compare the ridges with patterns forming in a shallow tray of moving water.|
N~A passing thing can leave a shape that refuses to pass.|
S~The repeated ridges make such a quiet pattern. Knowing their age gives it weight.|
N~I'd look along the ridges from a lower angle. Their shape deserves more than a quick glance.
''')
add('depth_machine', 'SlateportCity_OceanicMuseum_1F_Text_DepthMeasuringMachine', 'An unidentified rotating machine under glass may measure depth.', '''
N~It looks very busy. I wish its explanation had clocked in for the same shift.|
N~Depth measurement is only a guess here. We'd need a label or mechanism to identify its purpose.|
N~Don't touch it to find out. Ask someone who knows.|
N~I like watching it turn, even though I don't understand what it's doing.|
N~Someone keeps it running. I'd ask them what we're meant to notice.|
N~An industrious mystery, earning its place beneath glass through sheer commitment to rotating.|
S~The mechanism remains secret. The rotation is very forthcoming.|
U~I'd love a diagram showing what connects to what. The motion alone doesn't explain the job.|
N~A little machine works inside a clear shell, keeping its purpose to itself.|
N~The display catches attention well. It seems to have misplaced the next step of communication.|
N~I'd ask the staff what it's measuring before deciding what the movement means.
''')
add('water_sample1', 'SlateportCity_OceanicMuseum_2F_Text_WaterQualitySample1', 'Regional seawater samples show that connected seas can have different water characteristics.', '''
N~One connected sea, several different little personalities in jars.|
N~Connection doesn't imply immediate uniformity. Local conditions can preserve differences.|
N~Same sea doesn't mean the same conditions everywhere.|
N~I like that a small sample can make a huge place feel less like one blank blue.|
N~Different shores leave different things in the water. The samples make that easier to notice.|
N~The sea has declined to become identical merely because the map gives it a connected shape.|
S~A collection of water, each sample refusing to be simply more water.|
U~I'd want the collection sites and sampling dates beside them for a useful comparison.|
N~Things can touch for a long time and still keep traces of where they came from.|
N~The plain jars ask us to notice differences instead of relying on a dramatic display.|
N~I'd ask what difference they measured first. The label has made me curious enough to want details.
''')
add('water_sample2', 'SlateportCity_OceanicMuseum_2F_Text_WaterQualitySample2', 'The second water sample asks whether seawater saltiness varies by region.', '''
N~I would like the answer without arranging a museum-wide tasting session.|
N~Salinity can be compared by measurement. Sampling conditions would help interpret the result.|
N~Measure it. Don't drink the exhibit.|
N~I wonder how different two samples can be while looking so similar.|
S~My tongue has opinions about salt, but I think the museum has a better method here.|
N~An intriguing comparison that does not, I trust, require us to lick the evidence.|
S~The water looks innocent. The proposed tasting experiment should remain theoretical.|
U~I'd like the measurements displayed together rather than have visitors guess from appearance.|
N~A small invisible difference can tell you where a current has been.|
N~It's a good question. I wish the answer were beside it instead of leaving us to imagine.|
N~I'd ask the staff how they compare the samples. That sounds worth learning.
''')
add('pressure_ball', 'SlateportCity_OceanicMuseum_2F_Text_PressureExperiment', 'A changing rubber ball illustrates increasing pressure in deep water.', '''
U~That poor ball is trying on several sizes of itself for our education.|
N~The deformation makes otherwise invisible pressure changes observable. A clear model.|
N~Deep water is heavy. Good reason to trust proper equipment.|
N~Watching it shrink makes the depth feel more real than a large number does.|
N~I'm glad a rubber ball gets to demonstrate this instead of a living partner.|
N~A humble ball has accepted the difficult role of making an enormous force look understandable.|
S~An exhibit about being under pressure. The ball is handling the publicity better than expected.|
U~I'd like to see the pressure scale synchronized with the change in volume.|
N~The weight of all that unseen water finds a shape our eyes can follow.|
N~A simple shape changing tells the story quickly. That's thoughtful display design.|
N~I'd watch the ball through a full cycle before looking back at the numbers.
''')
add('hoenn_model', 'SlateportCity_OceanicMuseum_2F_Text_HoennModel', 'A miniature Hoenn diorama prompts the player to locate Littleroot.', '''
S~Littleroot must be a very small little Littleroot from up here. I'll look gently.|
S~The model trades detail for regional context. Finding a familiar location anchors the scale.|
N~Find home first. Then the rest of the route starts making sense.|
S~A place can look tiny on a model and still hold most of someone's beginning.|
S~I'd trace the trip from Littleroot slowly. We've covered more ground than it sometimes feels like.|
S~The entire region has agreed to fit inside a room, with modest reductions to everyone's importance.|
S~A whole journey made small enough to inspect without acquiring new blisters.|
U~I'd compare the elevation and transport routes. A model makes those relationships much clearer.|
S~A little place stays large in memory, even when the map barely has room for it.|
S~Finding somewhere familiar gives the whole display a more personal shape.|
S~I'd ask each of us to point out the place that feels biggest in our own memory.
''')
add('deep_current', 'SlateportCity_OceanicMuseum_2F_Text_DeepSeawaterDisplay', 'Deep currents are driven by differences including temperature and salinity.', '''
N~The sea keeps moving down where the wind can't reach to give it a nudge. Industrious.|
S~Temperature and salinity affect water density, providing a mechanism distinct from surface wind.|
N~Deep water has its own currents. Surface calm won't tell the whole story.|
N~It's strange imagining all that movement under something that looks still from a boat.|
N~A quiet surface doesn't mean the whole place has settled. Worth remembering at sea.|
N~The depths have their own arrangements, apparently requiring no assistance from the weather overhead.|
N~Even the bottom of the sea has somewhere it insists on going.|
U~I'd love to see the layers shown with different colors so the circulation becomes visible.|
N~Below the light, small differences can keep an enormous darkness moving.|
N~The display changes how I picture the sea. There are several motions under one surface.|
N~I'd ask how people measure something moving so far below them.
''')
add('surface_current', 'SlateportCity_OceanicMuseum_2F_Text_SurfaceSeawaterDisplay', 'The display explains wind-driven currents near the surface.', '''
S~The wind doesn't stop at ruffling our hair. Apparently it has much larger chores.|
S~Wind transfers motion to surface water. The display connects two familiar observations.|
N~Watch the wind and the water together. Both affect a crossing.|
N~I like seeing a connection between two movements I usually notice separately.|
N~A pleasant breeze on shore might mean a harder trip for somebody farther out.|
S~The wind has been pushing the scenery around while pretending to be merely atmospheric.|
S~The sea has received instructions from something nobody can see. Very cooperative.|
U~I'd compare the current direction with the airflow instead of looking at the water alone.|
N~A passing breath can set a much heavier thing in motion.|
N~The invisible force becomes easier to imagine once the water gives it a visible effect.|
N~I'd ask a sailor how they recognize those patterns without a museum diagram.
''')
add('tidal_replica', 'SlateportCity_OceanicMuseum_2F_Text_SSTidalReplica', 'A scale replica depicts the S.S. Tidal, described as under construction at Stern shipyard.', '''
S~A little ship previewing a very big trip. It must be impatient to grow into its own plans.|
N~The model represents the proposed vessel. Its construction label may precede the actual service status.|
N~Good way to see the ship's shape before standing beside the real hull.|
S~I like imagining all the people who might eventually travel on it.|
S~A ferry means a lot of ordinary reunions as well as grand journeys.|
S~The ship has arrived at the museum ahead of its larger, considerably less portable counterpart.|
S~A sea voyage reduced to a convenient shelf-sized commitment.|
U~I'd love to compare this with the yard plans and see what changed during construction.|
S~A route can exist first as something small enough to lift in two hands.|
N~The model gives the ship a presence before passengers have their own memories of it.|
S~I'd ask the builders which part was hardest to capture at this scale.
''')
add('submarine_replica', 'SlateportCity_OceanicMuseum_2F_Text_SubmarineReplica', 'A replica shows the Submarine Explorer 1 designed for ocean-floor exploration.', '''
U~A little submarine for a very deep idea. I'm glad the glass case isn't the ocean-sized version.|
N~The replica presents a vessel intended for seafloor work, not an actual pressure-tested exhibit.|
N~Real exploration depends on more than the impressive shape. Good crews matter.|
N~I wonder what it feels like to leave daylight behind inside something that small.|
N~I'd want to know how the people inside stay comfortable and supplied during a long descent.|
N~A journey to the ocean floor, thoughtfully offered in a form that doesn't require us to descend.|
S~The miniature version has a much more forgiving pressure requirement.|
U~I'd like to see a cutaway showing the hull, controls, and occupied space.|
N~A small shell is built so people can enter a place their bodies cannot bear alone.|
N~The shape looks purposeful. I'd be curious which features came from the conditions below.|
N~I'd ask what the first explorers most wanted to see from its windows.
''')
add('submersible_pod', 'SlateportCity_OceanicMuseum_2F_Text_SumbersibleReplica', 'A model depicts an unmanned compact pod for exploring the seafloor.', '''
S~A tiny underwater scout. It gets the first look without needing a packed lunch.|
S~An unmanned design allows observation without placing an occupant in the same environment.|
N~Send a purpose-built pod where people can't safely go. Sensible.|
N~I'd like to see what comes back through its eyes.|
S~Someone can learn about the deep and still come home to supper without the descent.|
S~A compact envoy sent to endure the uncomfortable portion of scientific curiosity.|
S~An excellent volunteer for a job nobody asked a person to fit inside.|
U~I'd love to know how it sends information back and how they recover it.|
N~A small made thing carries human curiosity where human breath cannot follow.|
S~Being compact changes the whole silhouette. Nothing is shaped around a passenger.|
U~I'd ask what its first images showed. The moment of seeing something new must be wonderful.
''')
add('anne_replica', 'SlateportCity_OceanicMuseum_2F_Text_SSAnneReplica', 'A replica depicts the globe-circling luxury liner S.S. Anne.', '''
S~A ship that circles the world sounds like a very elaborate way to return something borrowed.|
S~Its stated purpose combines long-distance travel with passenger comfort. Different priorities from the research models.|
N~Luxury or not, I'd still check the weather before boarding.|
S~I wonder how many different goodbyes the real ship has heard.|
S~I'd be curious about the galley. A long voyage asks a lot from whoever feeds everyone.|
S~A floating promise that distance need not prevent people from insisting on excellent chairs.|
S~A voyage around the world, provided the world doesn't disturb the upholstery.|
U~I'd compare how much space is devoted to passengers versus operating the ship.|
N~A circle around the world must gather a strange collection of small homesicknesses.|
S~The luxury details make this one feel very different from the working vessels beside it.|
S~I'd ask a passenger which port stayed in their mind long after the trip ended.
''')
add('fantasy_landscape', 'LilycoveCity_LilycoveMuseum_1F_Text_OddLandscapeFantasticScenery', 'A painting shows an odd landscape with fantastic scenery.', '''
U~I can't tell which way I'd walk through it. That may be the landscape winning.|
N~The unusual forms make familiar spatial expectations unreliable. Interesting effect.|
N~Looks strange. I'd need a better route before walking into a place like that.|
S~I like that it feels like somewhere I haven't learned how to describe yet.|
N~I'd want a familiar little place to sit inside all that strangeness.|
S~A landscape that has declined most of geography's more restrictive suggestions.|
S~An excellent place to get lost without leaving the room.|
U~I'd like to see the first sketches. Those shapes must have developed in an interesting order.|
N~It looks like a place remembered by something that dreams differently from us.|
S~The unfamiliar shapes still feel deliberate. That's what keeps me looking.|
U~I'd ask everyone which part they noticed first. I suspect we'd point in different directions.
''')
add('berry_painting', 'LilycoveCity_LilycoveMuseum_1F_Text_PaintingOfBerries', 'A realistic Berry painting looks delicious enough to provoke hunger.', '''
S~The artist has painted a very convincing argument for lunch.|
S~The visual detail evokes a familiar taste expectation. An effective still life.|
N~Good painting. Still need actual food if we're hungry.|
S~I like how a quiet picture can make the room feel warmer.|
U~That's dangerously good. I want to know which Berries they arranged and whether anyone ate them afterward.|
S~A still life has successfully created a highly active appetite.|
S~A painting that refuses to feed the hunger it caused. Art can be cruel.|
N~I'd like to compare the colors they used for the shine with the actual Berry skins.|
S~A painted harvest can offer the memory of sweetness, if not the sweetness itself.|
S~The arrangement makes the shapes feel generous. It's difficult not to want one.|
S~I'd look closer at the surface, then find something real to eat before visiting the next room.
''')
add('old_paint', 'LilycoveCity_LilycoveMuseum_1F_Text_VeryOldPainting', 'An old painting shows patches of peeling paint.', '''
D~It's coming apart in tiny places. I hope somebody here knows how to help it hold together.|
N~The deteriorating paint warrants conservation. Age and physical condition aren't the same as artistic value.|
N~Don't touch the loose parts. Let someone trained handle it.|
D~I keep wondering what the missing little patches used to show.|
N~It has lasted a long time. I'd like it to have the care it needs for a little longer.|
D~The painting has survived history and is now losing a quiet argument with its own surface.|
N~Time has developed an alarming interest in the edges.|
N~I'd ask what conservation method suits the materials before attempting any repair.|
D~A picture can fade unevenly, leaving some parts to remember the others.|
N~The damage changes how we see it. I'd still want to know what the artist meant before it happened.|
N~I'd ask whether an older photograph records the parts that are beginning to peel.
''')
add('woman_partner', 'LilycoveCity_LilycoveMuseum_1F_Text_PaintingOfBeautifulWoman', 'A portrait shows a smiling woman with a Pokemon resting on her lap.', '''
S~That lap looks thoroughly claimed. A very small throne with an unusually comfortable ruler.|
S~The shared posture makes the relationship central to the portrait.|
S~They look comfortable together. That tells a story by itself.|
S~Her smile seems quieter because the Pokemon is right there with her.|
S~I like pictures of ordinary contentment. Nobody has to be doing something impressive.|
S~A formal portrait quietly taken over by the person occupying the best seat.|
S~The companion appears to have negotiated excellent living conditions.|
N~I'd look at how the artist positioned their hands and the Pokemon to show trust.|
S~A small weight can make a person look more settled in the world.|
S~The relationship makes the portrait warmer than a smile aimed only at the viewer.|
S~I'd ask whether the artist knew them. The moment feels comfortably observed.
''')
add('bird_sculpture', 'LilycoveCity_LilycoveMuseum_Text_BirdPokemonSculptureReplica', 'A replica preserves the form of a famous ancient bird Pokemon sculpture.', '''
N~A copy of a very old bird. Its migration route has apparently included several workshops.|
N~The replica lets people examine the form without requiring the original object to travel.|
N~A copy can still show good work. No need to pretend it's the original.|
N~I wonder which detail made the first sculpture famous.|
S~I'm glad more people can see it without risking the older piece on every journey.|
S~The ancient bird has sent a competent representative rather than attend personally.|
S~A replica with excellent credentials and much less historical anxiety.|
U~I'd like to know which materials and methods were used to reproduce the surface.|
N~A shape can travel farther than the stone that first held it.|
N~I'd compare it with an image of the original. Small differences can change the whole feeling.|
N~I'd ask where the original stands and what people see around it there.
''')
add('grass_breeze', 'LilycoveCity_LilycoveMuseum_1F_Text_PaintingOfGrassPokemon', 'A painting depicts Grass Pokemon enjoying a gentle breeze.', '''
S~They look as though the breeze told a very small joke and everyone leaned over to hear it.|
S~The repeated postures imply a common direction of motion. A convincing effect.|
S~Peaceful scene. Nice to see Pokemon simply enjoying the day.|
S~I can almost feel the quiet around them. I'd stay beside this one a little longer.|
S~That looks like an afternoon where nobody needs anything urgently. Lovely.|
S~The painter has persuaded a still surface to spend the afternoon moving gently.|
S~A peaceful day, preserved before anyone arrived with a schedule.|
N~I'd look at the leaf angles and how the artist makes them share the same wind.|
S~A breeze becomes visible in the little bodies that welcome it.|
S~The shared movement ties the whole picture together without making every Pokemon identical.|
S~I'd want to visit a place like that quietly, so the scene could keep happening around us.
''')
add('ancient_tablet', 'LilycoveCity_LilycoveMuseum_1F_Text_StoneTabletWithAncientText', 'A large tablet depicts Pokemon beside dense unreadable ancient writing.', '''
N~A huge message, and we don't know where to begin. Stone has excellent patience for confused readers.|
N~We can describe the symbols without claiming a translation. Documentation comes before interpretation.|
N~Don't guess the meaning and call it fact. The tablet can wait.|
N~Someone worked so carefully to say something. It's sad not knowing what they wanted heard.|
N~I'd like to know who can study the writing without damaging the surface.|
N~An enormous statement from the past, currently refusing all requests for clarification.|
N~The old words remain. Our understanding has failed to keep its appointment.|
U~I'd compare repeated signs and the layout around the Pokemon figures. Patterns could matter.|
N~Words can survive their voices and still wait for another one to reach them.|
N~The dense arrangement is striking even before we understand what any of it says.|
N~I'd ask what researchers have actually established and where the uncertainty begins.
''')
add('imagined_legend', 'LilycoveCity_LilycoveMuseum_1F_Text_PaintingOfLegendaryPokemon', 'The artist imagined a legendary Pokemon from the distant past.', '''
S~The artist hasn't met the Pokemon, but they've certainly arranged an impressive introduction.|
N~This is an imaginative reconstruction, not evidence of the creature's exact appearance.|
N~Enjoy the picture. Keep the distinction between imagination and a sighting.|
N~I like seeing what someone hoped the creature would feel like to encounter.|
N~A legend can give people something to imagine together, even when the details differ.|
S~A portrait completed without the awkward business of persuading the subject to sit still.|
S~The subject was unavailable. Imagination has supplied a remarkably confident replacement.|
N~I'd be curious which details came from old accounts and which were the artist's choices.|
N~An unseen thing can take many shapes in the space people leave for it.|
S~The choices reveal the artist as much as the imagined subject. That's part of the interest.|
N~I'd ask what detail the artist settled on first. It might explain the rest of the image.
''')
add('festival_ball', 'LilycoveCity_LilycoveMuseum_1F_Text_BigPokeBallCarvedFromStone', 'A large black-stone Poke Ball was apparently used in old festivals.', '''
U~A Poke Ball with a very serious carrying problem. The festival must have supplied strong volunteers.|
N~Its apparent ceremonial use differs from an ordinary functional ball. The material reinforces that.|
N~Heavy object. I'd like to know how they moved it safely.|
N~I wonder what it looked like with people gathered around it instead of museum walls.|
S~A festival object makes me imagine the ordinary work of getting everyone ready for the day.|
N~A Poke Ball intended to hold an occasion rather than a Pokemon. An intriguing promotion.|
S~A festive symbol with an extremely un-festive lifting requirement.|
U~I'd examine the carving marks and ask how they shaped such a large piece.|
N~A dark stone has outlasted the voices that once circled it.|
N~The familiar shape changes when the material gives it so much weight and permanence.|
N~I'd ask whether any account of the festival survives. The object leaves a very large question.
''')
add('pink_frame', 'LilycoveCity_LilycoveMuseum_2F_Text_ItsPinkPictureFrame', 'A pink-adorned picture frame waits without a painting.', '''
S~An empty pink frame. It's already dressed for somebody's very cheerful arrival.|
N~The frame supplies a visual tone before a subject occupies it. Interesting anticipation.|
N~A place waiting for a picture. No need to invent what's inside.|
S~The little pink details make the empty space feel less abandoned.|
S~Someone has made a welcoming place before the guest is here. I like that.|
S~A carefully dressed entrance patiently awaiting the thing meant to make it famous.|
S~An absence with pink trim. Surprisingly optimistic.|
N~The adornments establish the border. The future picture will need to work with them.|
S~A soft edge can change the shape of waiting.|
S~Pink sets an expectation without choosing the whole image. I'd keep the balance in mind.|
S~I'd like to see how the room changes when something finally fills it.
''')
add('yellow_frame', 'LilycoveCity_LilycoveMuseum_2F_Text_ItsYellowPictureFrame', 'An empty frame has yellow-colored adornments.', '''
S~That's a remarkably sunny welcome for a picture that hasn't arrived yet.|
N~The yellow border will affect how neighboring colors are perceived in a future composition.|
N~Empty for now. The bright frame makes the space easy to notice.|
S~I like the warmth around it. Even the blank center seems less cold.|
S~A little yellow can make a waiting place feel ready instead of forgotten.|
S~The frame has begun celebrating a guest whose invitation is still being arranged.|
S~A blank space enjoying excellent weather at the edges.|
N~I'd consider the intended lighting along with the yellow trim before choosing a picture.|
S~Light has gathered around an unwritten little space.|
S~Yellow is a bold choice for something meant to sit around another image. It needs confidence.|
N~I'd compare it under daylight and the room's lamps. The color may feel quite different.
''')
add('red_frame', 'LilycoveCity_LilycoveMuseum_2F_Text_ItsRedPictureFrame', 'A red-adorned frame has no painting yet.', '''
S~The empty frame has made a very firm announcement about the color red.|
N~The strong border draws attention even before a subject is present.|
N~Bold frame. Whatever goes inside will have to hold its own.|
N~It feels expectant in a louder way than the others.|
S~A bright welcome can be nice. I'd want the picture to feel at home in it.|
S~An empty frame that has declined to be overlooked while awaiting its principal attraction.|
S~Nothing inside yet. The edges have compensated with enthusiasm.|
N~We'd need to consider how much contrast the future image should have against that trim.|
N~A red boundary makes the silence inside it seem deliberate.|
U~That border has presence. I'd want the picture and frame to share the attention gracefully.|
N~I'd step back across the room to see how strongly it pulls the eye from a distance.
''')
add('blue_frame', 'LilycoveCity_LilycoveMuseum_2F_Text_ItsBluePictureFrame', 'An empty picture frame is adorned in blue.', '''
S~The blue frame looks patient. I suspect it would wait more gracefully than I would.|
N~A cool-colored border may establish a different mood from the warmer frames.|
N~Quiet color. The empty space stands out without shouting.|
S~This one feels calm enough that I don't mind the waiting.|
S~I'd like a picture here that still gives your eyes somewhere to rest.|
S~A dignified blue introduction, currently waiting for the person it was meant to introduce.|
S~A very composed absence. It appears to have practiced.|
N~The room's lighting will matter to how that blue relates to the eventual image.|
S~A cool edge can make a little emptiness feel like open air.|
S~I like how it changes the pace beside the brighter borders. The group needs that.|
N~I'd compare where my attention lands in this frame and the red one.
''')
add('green_frame', 'LilycoveCity_LilycoveMuseum_2F_Text_ItsGreenPictureFrame', 'Green adornments border an empty place for a painting.', '''
S~A little green border, waiting for something interesting to grow in the middle.|
N~The frame establishes a color relationship that the eventual picture will need to answer.|
N~A prepared space. We'll see what earns the place inside.|
S~I keep imagining leaves around it, even though that's only the color suggesting things.|
S~The green makes the empty space feel like a beginning rather than a gap.|
S~A promising border has been installed before anyone has supplied its central argument.|
S~A vacant plot, attractively landscaped at the edges.|
N~I'd compare the trim with the surrounding wall before selecting colors for the picture.|
S~Some waiting places resemble seeds more than holes.|
S~Green can be quiet or sharp depending on what sits beside it. The image will decide a lot.|
N~I'd be curious whether everyone imagines the same sort of picture for this frame.
''')
add('birch_machine', 'LittlerootTown_ProfessorBirchsLab_Text_SeriousLookingMachine', 'An imposing laboratory machine appears intended for Birch research, with no identified function.', '''
N~That machine has a very serious face. I wonder whether it knows what all its buttons do.|
N~The setting suggests research use, but appearance alone doesn't identify the apparatus.|
N~Ask Birch what it does before putting a hand near it.|
N~I think I'd feel as though it could tell I hadn't understood the label.|
N~Something that complicated probably took a lot of ordinary patient work to make.|
N~An imposing piece of equipment, looking fully prepared to disapprove of an uninformed question.|
S~The machinery appears serious. Whether it has a sense of humor remains untested.|
U~I'd love a diagram. A complicated exterior only makes me want to know the job inside.|
N~A room can hold a large question in the shape of a machine.|
N~It communicates importance very efficiently. Its purpose is less forthcoming.|
N~I'd ask the professor what observation it helps him make.
''')
add('birch_research_pc', 'LittlerootTown_ProfessorBirchsLab_Text_PCUsedForResearch', 'Birch research computer is left undisturbed.', '''
N~Important research is in there. My curiosity can survive a closed keyboard.|
N~Unknown work may depend on its current state. Asking before using it is sensible.|
N~His work. Leave it as we found it.|
N~I'd feel awful if a curious glance changed something he'd spent hours doing.|
N~We can ask about the research without treating the computer like a public toy.|
N~An invitation to be curious, with the sensible restriction that we use our mouths first.|
N~The research has survived us noticing it. Let's preserve that success.|
N~I'd ask for a demonstration when he has time, so we understand the setup properly.|
N~Other people's unfinished thoughts deserve a door we knock on.|
N~A useful boundary. Interest doesn't make every workspace open for handling.|
N~I'd rather hear the story from Birch than try to piece it together from a screen.
''')
add('birch_full_shelf', 'LittlerootTown_ProfessorBirchsLab_Text_CrammedWithBooksOnPokemon', 'A densely packed shelf holds books about Pokemon.', '''
S~That's a lot of Pokemon knowledge. The shelf is doing a very strenuous amount of knowing.|
S~A substantial reference collection. I'd start with a particular question rather than attempt every volume.|
N~Plenty to learn here. Pick one useful book first.|
S~I like a room where people keep things they might want to understand better.|
N~I'd ask which volume gets used most. The worn one may be the best place to begin.|
S~A great many answers have been placed shoulder to shoulder, awaiting the right troublesome question.|
S~The shelf appears one new discovery away from requiring reinforcement.|
N~I'd want an index. A useful collection needs a way to find what you're looking for.|
S~A crowded shelf is a quiet gathering of people trying to leave something behind.|
N~The variety matters more to me than the impressive quantity. I'd look at the subjects.|
N~I'd ask Birch which book changed how he looked at Pokemon.
''')
add('birch_hard_book', 'LittlerootTown_ProfessorBirchsLab_Text_BookTooHardToRead', 'A research book is beyond the player present understanding.', '''
N~The book has defeated me without even using a move. I think it had several syllables equipped.|
S~Difficulty often means prerequisites are missing. A simpler introduction could bridge the gap.|
N~Not yet understood. That's different from impossible.|
N~I'd like someone patient enough to explain the first page without making me feel foolish.|
N~No shame in starting with a clearer explanation. Everybody learned the words somewhere.|
N~An impressive defense made entirely from terminology. We may require a glossary to breach it.|
S~The book has declined casual acquaintance and requested several years of preparation.|
N~I'd identify the first unfamiliar term instead of trying to swallow the entire chapter.|
N~An unopened understanding can still have a path leading toward it.|
N~Hard to read can be a matter of experience, or of how clearly someone chose to write.|
N~I'd ask the professor which easier book would help us approach this one.
''')
add('devon_products', 'RustboroCity_DevonCorp_1F_Text_ProductDisplay', 'Devon display connects industrial work with everyday products, medicines, and trainer tools.', '''
U~Devon has found quite a few ways to make itself useful in our pockets.|
N~The display describes diversification from industry into consumer and trainer products.|
N~Wide range. I'd judge each thing by how well it does its own job.|
N~It's interesting seeing the early versions of things people now use without thinking.|
N~A useful product becomes part of a very ordinary day. That's a worthwhile ambition.|
N~A company with a notably broad interpretation of the phrase we make things.|
S~The prototype cabinet is full of objects hoping to become indispensable.|
U~I'd love to compare the test pieces with the finished designs. What changed, and why?|
N~A small object can carry a surprising amount of someone's time in its shape.|
N~I'd look for the difference between something that attracts attention and something easy to use.|
N~I'd ask a tester which product improved most between its first and final versions.
''')
add('devon_raw_materials', 'RustboroCity_DevonCorp_1F_Text_RocksMetalDisplay', 'Devon history began with quarried stone and iron obtained from sand.', '''
U~All that machinery began with rocks and sand. The sand has done very well for itself.|
N~The exhibit connects raw-material production with the company's later industrial development.|
N~Useful to remember where finished equipment actually begins.|
N~I like seeing the plain beginning beside everything the company became.|
N~A long chain of work sits between a handful of material and something useful in a home.|
N~An impressive corporate history beginning with the modest discovery that the ground contains things.|
S~The raw materials have escaped the ground and acquired a remarkable career.|
U~I'd want to see the steps between these samples and the finished metal parts.|
N~Something quiet underfoot can become the bones of an entire changing town.|
N~Showing the material makes the company's story less abstract. It's a good choice.|
N~I'd ask whether any of the oldest quarry workers' accounts were kept.
''')
add('president_stones', 'RustboroCity_DevonCorp_3F_Text_RareRocksDisplay', 'The Devon president displays a personal rare-rock collection.', '''
S~He makes all sorts of complicated things and still leaves room to admire a good rock.|
S~The collection reflects interest beyond the company's immediate production work.|
S~A personal collection. Leave it where he arranged it.|
S~I wonder which one he picked up himself instead of acquiring through someone else.|
S~It's nice seeing something he keeps because it interests him, not because it has a job.|
S~A room full of responsibilities has retained one respectable corner for interesting stones.|
S~The president has provided evidence that a rock can succeed without becoming a product.|
U~I'd ask how he chose the display order: origin, material, shape, or simple affection.|
N~A stone can be rare in the world or simply rare in one person's memory.|
S~I'd want to know whether the arrangement reflects his favorites or the specimens themselves.|
S~I'd ask which piece has the best story attached to finding it.
''')
add('steven_stones', 'MossdeepCity_StevensHouse_Text_CollectionOfRareRocks', 'Steven keeps a collection of unusual rocks and stones at home.', '''
S~A house with room for important rocks. I respect a host who gives his pebbles a proper address.|
S~The selected specimens could reflect geology, appearance, or collecting history. I'd ask which.|
S~Something he cares about. Handle it only if he offers.|
S~The collection makes the room feel more like someone actually lives here.|
S~I'd ask which stone he found on a good day and which one helped rescue a bad one.|
S~A perfectly legitimate reason to return from a long walk carrying considerably more weight.|
S~The stones appear comfortably settled. Travel evidently suited them.|
U~I'd compare the textures and ask where each formed. There's a lot of variety to study.|
S~He has gathered pieces of far places into one quiet room.|
S~The choices tell us something about his eye. Not all rare things attract the same person.|
S~I'd ask which one he'd show a first-time visitor and why.
''')
add('shiny_trash', 'AbandonedShip_HiddenFloorRooms_Text_BrightShinyTrash', 'A promising glint in the ship turns out to be ordinary trash.', '''
N~The sparkle had excellent publicity. The treasure itself has filed for a downgrade.|
N~Reflectivity doesn't establish value. The inspection corrected our initial expectation.|
N~Trash. Watch our footing and keep looking.|
N~For a second I thought we'd found something. The light made it look special.|
N~At least we checked. I'd leave the sharp bits alone while sorting what it actually is.|
N~A brilliant entrance from an object with absolutely no qualifications for being treasure.|
S~A reminder that rubbish can possess exceptional presentation skills.|
N~We should identify the material before handling it. Shiny scrap can have sharp edges.|
N~Light can make a discarded thing ask to be noticed again.|
N~A strong first impression isn't the same as something worth carrying home.|
N~I'd remember the difference between a glint and a find before calling everyone over next time.
''')
add('storage_unlocked', 'AbandonedShip_Corridors_B1F_Text_InsertedStorageKey', 'The storage key jams in the lock but opens the ship storage-room door.', '''
U~The key has decided to live here permanently. At least it remembered to let us through first.|
N~The door opened despite the jammed key. The key is no longer available for reuse.|
N~Door open. Don't wrench the stuck key and break something else.|
N~That little moment when it stuck must have felt awful before the door moved.|
N~One problem solved, and we don't need to force the mechanism any farther.|
N~A successful entry, accompanied by the key's unexpected decision to retire in place.|
S~The lock has accepted the key as a permanent resident.|
N~The mechanism released before seizing. We should inspect the doorway rather than keep twisting.|
N~A small thing stays behind so the way ahead can open.|
N~I like a clear outcome, even if the key's departure from our plans was a little dramatic.|
N~I'd check what the room contains before celebrating too loudly on an old ship.
''')
add('room_key_jammed', 'AbandonedShip_HiddenFloorCorridors_Text_InsertedKey', 'A room key sticks after unlocking one of the hidden ship doors.', '''
N~Another key has developed a powerful attachment to its door. The ship seems to encourage commitment.|
N~The unlocking succeeded. The jam means we should not plan on retaining that key.|
N~Open now. Leave the key rather than damage the lock further.|
N~I'm glad it worked before it stuck. I don't enjoy that uncertain pause.|
N~No need to keep struggling with a problem the open door has already solved.|
N~The key completed its assignment and promptly became part of the architecture.|
S~A one-way career transition from useful key to very small door ornament.|
N~The next useful check is the condition of the room beyond the threshold.|
N~An old lock can hold one thing fast while finally releasing another.|
N~We should remember which door opened rather than assume the key is still with us.|
N~I'd take a moment to get our bearings before moving through another similar-looking room.
''')
add('storage_locked', 'AbandonedShip_Corridors_B1F_Text_DoorIsLocked', 'A locked ship door is marked as storage.', '''
N~The door has provided the room's job description and refused all introductions.|
N~The label identifies the room, but not the means of access. A suitable key is still needed.|
N~Locked storage. Find the key instead of forcing old wood.|
N~I wonder what somebody thought was worth keeping behind it.|
N~A locked room on a wreck may hold supplies, or simply more trouble. Carefully either way.|
N~An informative welcome, followed by an extremely firm refusal of admission.|
N~The room is storage. Our curiosity has nowhere to store itself yet.|
N~We should look for the correct key before putting stress on the deteriorating structure.|
N~A name on a closed door leaves plenty of room for wondering.|
N~The faded purpose is still clear, even though the people using the room are gone.|
N~I'd check nearby rooms for a clue rather than guess at what the lock wants.
''')
add('generator_heat', 'NewMauville_Inside_Text_GeneratorRadiatingHeat', 'An overheating generator radiates heat from a distance and needs shutting down.', '''
N~If we can feel it from here, the generator is being much too generous with the warmth.|
N~The heat is evident at a distance. We should follow the intended shutdown method rather than approach carelessly.|
N~Keep back. Find the proper control.|
N~The whole space feels tense around it. I'd like the heat to stop.|
N~I'd check that our partners stay clear while we look for the control.|
N~An unwanted demonstration of just how much warmth a machine can contribute to a conversation.|
N~The generator has mistaken alarming for productive.|
N~We need the designed shutdown control. Touching the housing is not a useful diagnostic step.|
N~The air carries the machine's distress farther than we ought to walk toward it.|
N~The warning is plain enough without leaning closer to prove it.|
N~I'd keep track of the safe route out while we find the way to stop it.
''')
add('generator_quiet', 'NewMauville_Inside_Text_GeneratorQuietedDown', 'The generator has quieted after being switched off.', '''
S~That's a much better conversation with a machine. It has stopped shouting heat at us.|
N~The reduced activity is consistent with shutdown. Residual heat may still remain.|
N~Quiet now. Give the machinery space while it settles.|
S~I didn't realize how tense I'd been until the sound changed.|
S~A quieter room makes it easier to check how everyone's doing.|
S~The generator has accepted a less demanding role in the local atmosphere.|
S~A machine discovering the considerable social benefits of silence.|
N~The immediate shutdown is complete. I'd still avoid the housing until it's cooled.|
S~A harsh presence has loosened its hold on the room.|
S~The difference is noticeable. It's good to have a result we can actually hear.|
N~I'd take one last look from a safe distance, then tell Wattson what changed.
''')
add('moving_box', 'InsideOfTruck_Text_BoxPrintedWithMonLogo', 'A box identifies a Pokemon-branded moving and delivery service.', '''
S~Even the boxes have Pokemon on the job. I wonder whether the logo gets a rest break.|
N~The logo identifies the delivery service. It doesn't tell us the contents of this particular box.|
N~Delivery box. Best leave somebody else's packing sealed.|
N~Moving boxes make a place feel temporary, even when everything inside matters.|
N~I hope whoever packed it remembered where the everyday essentials went.|
S~A branded promise that one's belongings will travel in a more organized fashion than one's nerves.|
S~The box has a clearer travel plan than most of its passengers.|
N~Good labeling should help identify the shipment without opening it.|
N~A sealed box can hold a surprising amount of the place someone left behind.|
N~A simple logo has to remain recognizable on a battered box. Practical design.|
N~I'd ask where the delivery is headed before assuming the box has reached its final home.
''')
add('faraway_faded', 'FarawayIsland_Entrance_Text_Sign', 'A faded old inscription hopes a future human visitor will be kindhearted.', '''
D~Most of the words are going, but the wish for kindness is still holding on.|
N~The surviving fragments support that wish. They don't establish a complete date or author.|
N~We can honor the clear part. Be gentle with what's here.|
D~Someone left hoping a stranger would be kind. I want that part to be answered well.|
N~A careful visit seems like the least we can give that old request.|
D~Time has damaged the sentence without managing to erase the most important request.|
N~An old warning with a surprisingly modest demand: try not to be awful.|
N~I'd document the remaining marks without filling the missing text with guesses.|
D~A stranger's hope has survived long enough to become our responsibility for a moment.|
N~The missing words make the remaining ones feel more deliberate. I wouldn't embellish them.|
D~I'd record exactly what's legible, then leave the place as gently as the writer asked.
''')
add('southern_memory', 'SouthernIsland_Exterior_Text_Sign', 'An island inscription links fading memories with keeping them in the heart.', '''
N~A sign about remembering. It has volunteered to do some of the remembering for us.|
N~The inscription contrasts fading recall with enduring personal significance. A thoughtful metaphor.|
N~Keep what matters. It doesn't all need to stay perfectly sharp.|
D~I know how a small detail can fade while the feeling stays very clear.|
N~Sometimes remembering means doing the kind thing again, rather than repeating every word exactly.|
N~A brief inscription asking a much larger question than its surface has room to hold.|
N~Memory is unreliable. Apparently the heart has been assigned supplementary storage.|
N~A written marker can support memory without replacing the person who gives it meaning.|
N~Some things become less clear and no less present.|
N~I like that it leaves room for a personal answer instead of telling us what to remember.|
N~I'd ask what place each of us remembers most clearly even when the details have softened.
''')
add('white_rock', 'MossdeepCity_Text_ItsAWhiteRock', 'A simple description identifies the pale rock in Mossdeep.', '''
N~A white rock. It has supplied exactly one fact and refuses to become more mysterious for us.|
N~We know its appearance, not its composition or origin. No further conclusion follows yet.|
N~A rock. We can look without giving it a legend.|
N~I like its plainness. Not everything has to ask for a grand explanation.|
S~Something ordinary can still make a nice place to stop and look around.|
N~A remarkably concise introduction from an object surrounded by our temptation to speculate.|
S~White. Rocky. An exemplary commitment to giving no unnecessary information.|
N~I'd examine the texture before guessing at the material. Color alone isn't enough.|
N~Sometimes a pale stone is allowed to be only a pale stone.|
N~Its contrast with the surroundings catches the eye. That's already something to notice.|
N~I'd ask whether locals know where it came from, without assuming the answer will be extraordinary.
''')
add('peculiar_rocks', 'Route114_FossilManiacsHouse_Text_RocksFillDisplayCase', 'The Fossil Maniac displays rocks with unusual shapes.', '''
S~An entire case of rocks that refused the ordinary-rock silhouette.|
N~Unusual shapes may reflect different formation or weathering histories. I'd want specimen details.|
N~Interesting collection. Keep the case closed unless the owner offers.|
S~I wonder which shape made him stop in the middle of a walk.|
N~I'd ask which one took the most patience to find.|
S~A gathering of stones selected for their ability to make a person say hang on a moment.|
S~An exhibition of very slow, very committed eccentricity.|
U~I'd compare the surfaces for clues about how each shape formed.|
N~Water and time can leave a hard thing looking surprisingly uncertain of its own edges.|
S~The different outlines make the whole case lively without any bright colors.|
S~I'd ask what each one looked like before it was cleaned for display.
''')
add('geology_shelf', 'Route114_FossilManiacsHouse_Text_CrammedWithBooks', 'Books about strata, rain-shaped land, and rocks fill the Fossil Maniac shelf.', '''
S~He doesn't just collect rocks. He's collected several ways to ask the ground questions.|
S~The subjects link material, layered deposits, and erosion. A coherent reference collection.|
N~Good to learn what you're digging through before digging farther.|
N~I like that the books make rain sound like something that can write on the land.|
N~Understanding the place probably makes every find more meaningful to him.|
S~A shelf prepared to explain why the landscape looks the way it does, given enough time.|
S~The ground has a complicated biography. He appears to own the reference edition.|
U~I'd start with the erosion book and compare its diagrams with the terrain outside.|
N~Rain makes marks so slowly that a book helps us notice the hand.|
N~The shelf makes his interest feel deeper than simply wanting unusual objects.|
N~I'd ask which subject he thought was dull until he saw it happen outdoors.
''')
add('bill_email', 'Route114_LanettesHouse_Text_EmailFromBill', 'Bill praises Lanette storage-system improvements and encourages further research.', '''
S~A lovely message from someone pleased to see another person's work grow beyond his own part in it.|
S~He credits the improved usability while acknowledging their shared development history. Collegial and precise.|
S~Good to see someone proud of a colleague doing better work.|
S~That kind of encouragement would make a difficult day feel much less lonely.|
S~He remembered to say the work helps people. That's a useful compliment to carry back to it.|
S~A predecessor has encountered an improvement and chosen pride over wounded importance. Admirable.|
S~A professional message containing actual generosity. Worth preserving.|
U~I'd love to hear which user-friendly features he noticed first. Good feedback can guide the next iteration.|
S~A hand in the beginning needn't hold everything that grows afterward.|
S~He recognizes her choices instead of only reminding her where the work began.|
S~I'd ask Lanette which part of the message meant most to her.
''')
add('student_notebook', 'RustboroCity_PokemonSchool_Text_StudentsNotes', 'A student notebook summarizes catching, traveling with, raising, and battling Pokemon.', '''
S~A whole trainer's beginning, packed into a notebook. I hope there's room left for the surprising bits.|
N~A concise outline of the conventional trainer role. The actual practice will add nuance.|
N~Useful basics. How we treat the partners matters alongside the checklist.|
S~I'd like to see the little notes the student adds after trying those things themselves.|
N~The notes say how to begin. Everyday care will fill a lot of the space between the steps.|
S~An entire profession has been compressed into a few determined lines of student handwriting.|
S~The adventure fits on paper. The blisters are supplied separately.|
N~It's a starting framework. Experience should help connect the listed tasks rather than leave them isolated.|
N~A small page can point toward a much larger life without knowing all its turns.|
S~I like seeing what someone chose to write down as important at the beginning.|
N~I'd ask which lesson they've tried outside the classroom and what surprised them.
''')
add('porthole', 'SSTidalCorridor_Text_HorizonSpreadsBeyondPorthole', 'The ship porthole frames the distant horizon.', '''
S~A tiny round window trying to hold an enormous straight line. Brave little window.|
S~A fixed frame makes the scale beyond it particularly striking.|
N~Good view. Keep the corridor clear for people walking through.|
S~I could stand here a while. The distance makes my thoughts feel less crowded.|
S~A quiet look outside can help settle a busy journey.|
S~The ship has thoughtfully framed a landscape far too large to bring aboard.|
S~A small circle containing an unreasonable amount of outside.|
N~I'd watch how the line shifts with the ship's motion. A simple view reveals quite a bit.|
N~The far edge keeps its distance while the whole room moves beneath us.|
S~That round border changes the scene completely. It makes the open sea feel intimate.|
S~I'd wait for a change in the light rather than hurry past the window.
''')
add('shard_board', 'Route124_DivingTreasureHuntersHouse_Text_ShardTradeBoard', 'A posted board lists colored shards accepted in exchange for evolution stones.', '''
S~A very colorful answer to the question of what those little bits are worth to somebody.|
N~The board defines the exchange mapping. It doesn't indicate that any trade has occurred.|
N~Check the color before offering a shard. Clear terms.|
N~It's nice when a collection of little found things has a purpose you can actually read.|
N~I'd choose the stone we need rather than trade every shard just because the board is there.|
S~A neatly organized proposal to turn the sea's fragments into somebody else's next beginning.|
S~The broken pieces have unexpectedly good career prospects.|
N~The mapping is explicit. We can plan which shard to keep before making an exchange.|
N~A small fragment can open a larger possibility when it reaches the right hands.|
N~The colors make the matching easier to follow. Useful information presented well.|
N~I'd ask which shards are hardest to find and how the hunter learned to identify them.
''')
add('seedot_record', 'SootopolisCity_LotadAndSeedotHouse_Text_BiggestSeedotInHistory', 'The posted Seedot size record celebrates a giant specimen and invites larger examples.', '''
U~An exceptionally large little acorn. Seedot has found a wonderfully confusing career.|
N~This is a recorded specimen measurement, not evidence that the player has just set a new record.|
N~A big Seedot. Still needs treating like a partner, not a measuring trophy.|
S~I wonder what its trainer first noticed about it before somebody reached for a ruler.|
S~I'd be more curious about its habits than how much space its size takes on the sign.|
S~A modest species has acquired a magnificently immodest entry in the local record book.|
S~The acorn has outgrown expectations and several people's vocabulary for small.|
N~I'd check how they standardize the measurement before comparing another specimen.|
N~A small creature can become large in a room through size, or through what people make of it.|
N~It's a memorable record. I'd want the individual to remain more than the number.|
S~I'd ask the trainer how people react when they first see it.
''')
add('lotad_record', 'SootopolisCity_LotadAndSeedotHouse_Text_BiggestLotadInHistory', 'A posted record celebrates an unusually large Lotad and seeks a still larger one.', '''
U~That's a lot of Lotad. The leaf must cast a very respectable little patch of shade.|
N~The record concerns the measured individual. It doesn't establish a new result from this inspection.|
N~Impressive size. No need to chase a larger one just to keep the sign busy.|
S~I wonder whether it knows how much conversation follows it around.|
S~A very large partner still has ordinary preferences. I'd start by asking about those.|
S~A colossus in the specific and delightful field of being a Lotad.|
S~The pond's modest resident has become a considerable local event.|
N~We'd need the same measurement method to compare another Lotad fairly.|
N~A broad leaf can make a quiet little creature suddenly hard to overlook.|
N~The competitive sign is funny. I'd want the trainer's affection to remain less competitive.|
S~I'd ask where its trainer found it and what made them notice it first.
''')
add('trend_shelf', 'DewfordTown_Hall_Text_BooksAboutTrend', 'The hall shelf contains multiple books organized around the current local trend.', '''
U~They've filled an entire shelf already. That trend has a terrifyingly efficient publishing department.|
N~The books repeat the current phrase across several subjects. Popularity doesn't establish a real connection.|
N~A lot of books about one fad. I'd check what they actually say.|
N~I wonder whether anyone still reads them after the town finds its next favorite thing.|
N~A full shelf can still leave a simple question unanswered: is any of this useful?|
S~The fashionable phrase has acquired scholarship with astonishing speed and questionable necessity.|
S~A shelf full of certainty, all apparently printed before anyone asked why.|
N~I'd compare the contents instead of assuming different titles mean different information.|
N~A passing word has made itself a very permanent-looking little house.|
N~The books make the trend look established. That's part of how the room keeps it alive.|
N~I'd ask which one somebody has actually read. The answer might change how I see the shelf.
''')
add('frontier_tower_sign', 'BattleFrontier_OutsideEast_Text_BattleTowerSign', 'The Tower sign challenges trainers to sustain a winning streak.', '''
N~A tall building asking for a long streak. It seems to appreciate matching proportions.|
N~The stated goal emphasizes consecutive wins rather than a single impressive match.|
N~Consistency matters here. Prepare for more than one good opening.|
N~The sign makes the first battle feel like the beginning of a much longer thought.|
N~I'd want a plan the team can sustain, not just one dramatic burst.|
N~The Tower has chosen endurance with a competitive number attached.|
N~A building advertising several opportunities to discover a flaw in your plan.|
N~We should plan for varied opponents across the whole round.|
N~A straight tower, a long chain of moments. Both can seem smaller from the bottom.|
N~The emphasis is clear. Every match contributes to the impression, not just the first.|
N~I'd ask a regular challenger which ordinary decision kept their streak alive.
''')
add('frontier_palace_sign', 'BattleFrontier_OutsideEast_Text_BattlePalaceSign', 'The Palace sign invites visitors to observe Pokemon battles.', '''
N~A battle sign asking us to keep our eyes open. Sensible advice before the rules get stranger.|
N~Observation is emphasized here. We'd need the guide's explanation for the full battle format.|
N~Look carefully. Knowing what the Pokemon choose matters.|
N~I like an invitation that begins with paying attention.|
N~Watching well can be a way of looking after the partners, too.|
N~The Palace offers spectacle with a surprisingly useful instruction to actually notice it.|
N~A sign politely recommending the underused skill of looking.|
N~We should learn the exact format instead of inferring every rule from the slogan.|
N~A quiet eye can find things a loud command would miss.|
N~It's a restrained invitation compared with some of the island's louder promises.|
N~I'd watch one match before deciding what to make of the place.
''')
add('frontier_arena_sign', 'BattleFrontier_OutsideEast_Text_BattleArenaSign', 'The Arena sign calls for the toughest teams to gather.', '''
S~A meeting notice for tough teams. I wonder whether anybody brings the quiet snacks.|
N~The sign emphasizes team strength. The actual judging rules need separate explanation.|
N~A tough team still needs the right order. Let's check the rules.|
N~Gather sounds friendlier than prove yourselves, even on a battle sign.|
N~A team is more than three individually impressive partners. I'd remember that here.|
N~An open invitation to assemble the local competition in one conveniently intimidating room.|
N~A gathering where the introductions may involve quite a lot of impact.|
N~We should understand how the Arena evaluates a team before choosing ours.|
N~Several strengths can share a direction without being the same strength.|
N~I like that the sign names the team, rather than only the person leading it.|
N~I'd ask what makes a team work well here beyond simply looking formidable.
''')
add('frontier_pyramid_sign', 'BattleFrontier_OutsideEast_Text_BattlePyramidSign', 'The Pyramid sign advertises an advancing Battle Quest.', '''
S~A quest with its own very large roof. That's a confident amount of adventure to promise indoors.|
N~The sign presents progression as exploration. The facility rules will define the constraints.|
N~Learn the supply rules before starting a climb.|
N~Quest makes it sound like there could be something around every corner.|
N~I'd want everyone rested before accepting a challenge that might take a while.|
S~A grand promise of adventure, helpfully stored in one conspicuously solid landmark.|
N~A quest housed in a pyramid. Subtle invitations were apparently not available.|
N~We should ask what resources remain with us during the exploration.|
N~An upward path can hold many sideways uncertainties.|
N~The name promises a journey instead of simply another room of matches.|
N~I'd ask an explorer what they wish they'd known before the first floor.
''')
add('frontier_exchange_sign', 'BattleFrontier_OutsideEast_Text_ExchangeCornerSign', 'The sign directs visitors to exchange Battle Points for prizes.', '''
S~The place where all those difficult decisions become a very soft doll, if we want.|
N~A designated point-redemption service. We should compare terms before selecting a reward.|
N~Points for prizes. Decide what we actually want first.|
S~I like having something to look forward to that isn't another opponent.|
N~A useful item or a small joy can both be worth saving for.|
S~The island's efforts conclude here in an admirably tangible selection of consequences.|
S~A counter prepared to turn competence into cushions. Excellent civilization.|
N~We can check the full list and prices without committing immediately.|
S~Hard-won effort can change shape when it reaches a different pair of hands.|
N~I'd pick one thing I truly wanted before the display persuaded me to need five.|
S~I'd ask everybody which prize they noticed first. The answers could be entertaining.
''')
add('frontier_rank_sign', 'BattleFrontier_OutsideEast_Text_RankingHallSign', 'The Ranking Hall sign encourages new records.', '''
N~A sign asking us to improve the wall's reading material. Ambitious little sign.|
N~The hall recognizes measurable results. A specific category gives that ambition clearer shape.|
N~Set a realistic goal before chasing somebody else's number.|
N~I wonder how it feels to find your own name where you used to read others.|
N~A record is nice. I'd still want the work getting there to be something we can live with.|
N~A public invitation to become somebody else's intimidating benchmark.|
S~Posterity has installed directional signage. Very organized.|
N~We can inspect the categories and compare them with our current results.|
N~A name waits beyond a great many ordinary attempts.|
N~The promise of being remembered is powerful. I'd choose what I wanted remembered for.|
N~I'd like to hear a record holder describe the attempt before the successful one.
''')
add('frontier_dome_sign', 'BattleFrontier_OutsideWest_Text_BattleDomeSign', 'The Dome sign promises a path toward becoming an invincible superstar.', '''
N~Invincible superstar is quite a destination. I hope the path has somewhere to sit halfway.|
N~The language is promotional. A tournament can establish a winner, not literal invincibility.|
N~Good slogan. Still need to win the actual matches.|
N~I'd rather learn the format before imagining all those eyes on us.|
N~A good team can have an ordinary bad day. The sign doesn't get to forbid that.|
S~A modest promise from a building devoted to the completely reasonable ambition of universal acclaim.|
S~A path to invincibility, subject to several awkwardly capable opponents.|
N~We should prepare for selection and matchups, not rely on the advertised feeling.|
N~A bright word at the entrance doesn't light every difficult step inside.|
N~The sign understands what people dream about. I wonder how the actual experience supports them.|
N~I'd ask a visitor what surprised them once the grand first impression wore off.
''')
add('frontier_pike_sign', 'BattleFrontier_OutsideWest_Text_BattlePikeSign', 'The Pike sign presents its defining choice among three paths.', '''
N~Three paths. My uncertainty has been given a small but respectable menu.|
N~The sign establishes the branching choice, not the consequences behind each route.|
N~Three doors. Learn what hints are available before guessing.|
N~I'd probably stand at the entrance longer than I meant to.|
N~Whatever we choose, I'd like the team ready for more than one possibility.|
N~A remarkably concise invitation to consider how little a doorway tells you.|
N~Three opportunities to wonder whether the other two were better.|
N~Preparation should cover different outcomes rather than depend on choosing a perfect door.|
N~A choice can look simple when the walls are doing most of the hiding.|
N~The sign is honest about the choice and very quiet about everything after it.|
N~I'd ask how much information the attendants can actually provide.
''')
add('frontier_factory_sign', 'BattleFrontier_OutsideWest_Text_BattleFactorySign', 'The Factory sign asks visitors to seek the toughest Pokemon.', '''
N~A tough-Pokemon search inside a factory. I hope they aren't all queued behind one enormous clipboard.|
N~The slogan emphasizes selection. The rental and swap rules determine how that selection works.|
N~Find the right partners, not just the strongest-looking ones.|
N~I'd want to learn a little about the Pokemon before deciding what toughness means for them.|
N~A partner should fit the plan and be understood, even if we're only together briefly.|
N~A grand search whose practical beginning is likely to involve reading several move lists.|
N~The toughest choice may be the choosing itself. Convenient theme.|
N~We should assess combinations rather than rank each offered partner in isolation.|
N~Strength can hide in the way two unfamiliar things meet.|
N~I'd look past the first impressive outline. Useful qualities don't all announce themselves.|
N~I'd ask an experienced visitor what they learned to notice after their first few rentals.
''')
add('victory_road_sign', 'EverGrandeCity_Text_EnteringVictoryRoad', 'The sign marks the entrance to Victory Road.', '''
N~Victory Road. A very confident name for a place before we've walked through it.|
N~A destination marker, not a statement that the journey has already succeeded.|
N~Check supplies before entering. The name doesn't make it a short walk.|
N~It feels like a threshold even before taking the next step.|
N~I'd make sure everyone is ready instead of letting the name hurry us.|
N~An encouraging title placed strategically before the inconvenient work.|
N~A road named after the thing it has no obligation to provide.|
N~We should review the team's condition before committing to the route.|
N~A hopeful name can wait at the mouth of a very demanding path.|
N~It's a strong introduction. I'd let the actual route teach us what it means.|
N~I'd want to remember how this entrance felt before knowing what waited beyond it.
''')
add('league_gate_sign', 'EverGrandeCity_Text_EnteringPokemonLeague', 'The sign identifies the Pokemon League center gate.', '''
S~The League entrance. Even the ordinary act of walking through a gate has dressed up for the occasion.|
N~The marker identifies the League approach. Admission and readiness remain separate questions.|
N~We're at the gate. Take a breath and check the team.|
N~It looks official in a way that makes every little sound feel clearer.|
N~I'd like a quiet moment before going from the journey to the challenge itself.|
N~A short sign with an impressively large amount of expectation waiting behind it.|
N~The gate is ordinary architecture doing extraordinary psychological work.|
N~This is a useful point to review preparations before proceeding.|
N~A boundary can make all the road behind it feel suddenly present.|
N~The simple wording gives the place its own weight. It doesn't need much decoration.|
S~I'd ask what everyone thought this entrance would feel like before we reached it.
''')
add('tent_fallarbor', 'FallarborTown_Text_BattleTentSign', 'The Fallarbor Battle Tent sign calls great teams to gather.', '''
S~A tent with a very ambitious guest list. I wonder if the pegs know how important the visitors are.|
N~The invitation emphasizes teams. We'd need the guide to explain the actual event rules.|
N~A strong team needs more than a strong introduction. Check the format.|
N~Gathering sounds friendly. I'd like it to feel that way to somebody entering for the first time.|
N~I'd want a team comfortable working together before worrying about being called great.|
S~A lightweight building making a heavyweight invitation. Admirable confidence in the canvas.|
S~A gathering of greatness, presumably subject to available tent space.|
N~We should ask which team skills this particular site evaluates.|
N~A small shelter can hold an intention much larger than its roof.|
N~I like the focus on the whole team. I'd hope the experience follows through on it.|
N~I'd ask a participant what made their teammates work better together here.
''')
add('move_tutor_house', 'FallarborTown_Text_MoveTutorSign', 'The sign advertises a house where Pokemon can learn new moves.', '''
S~A house full of new ideas for Pokemon. I hope the furniture has learned to keep up.|
N~A local source of instruction. We'd need to ask which moves and conditions apply.|
N~Useful lead. Ask before making a plan around a particular lesson.|
S~I like places where learning something new is the whole reason for opening the door.|
N~A new move should be something that suits the partner, not just something impressive to collect.|
S~A modest house advertising the possibility of leaving with a considerably less modest technique.|
S~An educational address with potentially severe consequences for the furniture.|
N~We can compare the lesson options with the current team before committing.|
S~An old room can hold the beginning of a new habit.|
N~The plain sign does a useful job. I'd rather learn the details from the teacher.|
S~I'd ask what they enjoy most about seeing a Pokemon understand a new move.
''')
add('herb_shop_sign', 'LavaridgeTown_Text_HerbShopSign', 'The herb shop sign advertises bitter-tasting remedies.', '''
N~The sign has bravely put the bad taste right in the invitation. Honest shopkeeping.|
N~Bitterness is a stated property, not proof of greater effectiveness by itself.|
N~Ask what each remedy does. Don't choose only by the slogan.|
N~I'd want our partners to know we're trying to help, even if the taste isn't pleasant.|
N~Bitter isn't a virtue on its own. I'd ask about the intended use before buying anything.|
N~An unusually candid advertisement, allowing one's tongue to object before entering.|
S~A shop confident enough to warn the taste buds in advance.|
N~We should compare the actual item effects and the partner's response.|
N~A helpful thing can still be unpleasant to receive. That deserves noticing.|
N~I appreciate the honesty. I'd still want more than a neat phrase before making the choice.|
N~I'd ask the shopkeeper how they advise trainers choosing between the remedies.
''')
add('lily_store_sign', 'LilycoveCity_Text_DepartmentStoreSign', 'The department store sign promises abundant merchandise and excitement.', '''
S~Overflowing excitement sounds fun. I hope they've left enough room for the stairs.|
N~The promise of abundance is promotional. A specific need will make the selection easier.|
N~Decide what we're looking for before the displays do it for us.|
N~That much choice can make me want a quiet corner before I buy anything.|
N~A good trip to the store can end with one useful thing instead of several new errands.|
S~A building offering the rare opportunity to become overwhelmed on several consecutive floors.|
S~An enormous collection of things waiting to explain why we need them.|
N~I'd use the floor guide and compare options rather than wander until something persuades us.|
N~An abundance of objects doesn't make a missing wish easier to name.|
U~I'd like to see how each floor presents its range. A clear layout matters with this much choice.|
N~I'd ask everyone what they came for before we get distracted by the first display.
''')
add('cove_lily_sign', 'LilycoveCity_Text_MotelSign', 'The motel sign emphasizes remembering Cove Lily in Lilycove.', '''
S~Cove Lily, Lilycove. The name has put on its shoes backward and decided it looks splendid.|
S~The reversed place-name structure makes the association easy to recall. Effective mnemonic.|
N~Easy name to remember. We'd still want to know whether the rooms are comfortable.|
S~It's a playful little name for somewhere people might arrive very tired.|
S~A memorable name helps. A good night's sleep would make the stronger recommendation.|
S~A name with enough symmetry to give a tired traveler a brief argument with their own memory.|
S~An establishment that has rearranged the town and installed beds inside the result.|
N~I'd check the practical details after enjoying the wordplay.|
S~A borrowed name turned gently around can feel like a place of its own.|
S~The sign understands recognition. I'd want the inside to feel just as welcoming.|
S~I'd ask a guest what they actually remembered about staying there.
''')
add('lily_harbor_pending', 'LilycoveCity_Text_HarborSignUnderConstruction', 'A harbor notice says the S.S. Tidal is still being built in Slateport before service begins.', '''
N~The ferry is coming. At the moment it's taking the longer route through being assembled.|
N~The notice describes planned service, not proof that the vessel is ready now.|
N~No crossing promised yet. Check the actual sailing status.|
N~It's strange seeing a route people are already waiting for before the ship is finished.|
N~I'd rather the builders take the time they need than hurry just to satisfy the sign.|
N~The journey is scheduled to exist shortly. Construction has retained final approval.|
N~The ferry is currently traveling from parts to ship. A necessary first voyage.|
N~We should ask for current status rather than rely on an undated promise of shortly.|
N~A future crossing has left a small place for itself on the shore.|
N~The notice gives a useful location for the work. The timing is less precise.|
N~I'd ask the harbor staff when the board was last updated before arranging a trip.
''')
add('trainer_fan_sign', 'LilycoveCity_Text_TrainerFanClubSign', 'Trainer names have been scribbled across the fan-club sign.', '''
S~The sign introduced the club, then the club introduced quite a few extra names to the sign.|
N~The accumulated names show visitor participation beyond the original posted message.|
N~People are proud of their favorites. Best not cover someone else's name.|
N~I wonder which small name was written first and then nearly disappeared under the others.|
S~It's nice that people want to cheer somebody on. I hope the welcome stays readable.|
S~An official notice has surrendered most of its territory to enthusiastic unofficial endorsements.|
S~A public surface has become a crowded argument in handwriting.|
N~A separate message board might preserve both the club name and the visitors' enthusiasm.|
N~A name written in a crowd is still someone asking that it be seen.|
N~The layers tell a social story, even if the sign's original design has lost the conversation.|
N~I'd ask who started the tradition and whether their name can still be found.
''')
add('move_deleter_sign', 'LilycoveCity_Text_MoveDeletersHouseSign', 'A house sign advertises removing unwanted Pokemon moves.', '''
N~A house for letting go of moves. I hope the old techniques get a polite little farewell.|
N~The service concerns a learned move. We should understand the consequences before choosing one.|
N~Be sure which move we're dropping. No rushed decisions.|
N~Letting go can be useful, but I'd want a good reason first.|
N~Making room for something new doesn't mean the old thing never helped us.|
N~A remarkably direct address for the delicate business of editing one's practical habits.|
N~Unwanted moves have an official exit. Very considerate urban planning.|
N~We should consider the whole moveset before deciding which option is expendable.|
N~An empty place can be useful, if we know why we're clearing it.|
N~The sign makes it sound simple. I'd still want the decision to be deliberate.|
N~I'd ask how trainers usually realize a move no longer fits their partner.
''')
add('birch_lab_sign', 'LittlerootTown_Text_ProfBirchsLab', 'The sign identifies Professor Birch Pokemon laboratory.', '''
S~Professor Birch's lab. A small sign for a building with a lot of questions inside.|
S~A named research location. We can ask about the work instead of guessing from outside.|
N~Right place to find Birch or someone who knows his work.|
S~I like knowing whose door we're approaching. It makes asking a question easier.|
S~A lab is a good place to begin by admitting what we don't know.|
S~An address for curiosity, neatly attached to the person most likely to encourage it.|
S~A building officially dedicated to not knowing everything yet. Respectable purpose.|
U~I'd be curious what equipment is available inside and what questions it helps answer.|
S~A little doorway can open onto more than the room immediately behind it.|
N~A clear, useful sign. It gives the important information without making a grand promise.|
S~I'd ask which question the lab is working on this week.
''')
add('wally_house_sign', 'PetalburgCity_Text_WallyHouseSign', 'The house sign identifies Wally home.', '''
S~A familiar name makes an ordinary house feel a little easier to approach.|
N~A clear household marker. It identifies the address, not whether anyone is home.|
N~Wally's house. We should knock before going farther.|
S~I like seeing a person's name where they can come back and be expected.|
S~A home is more than the place someone starts from. It's somewhere to ask how the trip went.|
S~A small sign doing the very useful work of making a name into somewhere we can visit.|
S~An address with none of the battle rankings attached. Pleasant change.|
N~We can check whether it's a convenient time to visit rather than assume.|
S~A person's name can make a doorway feel warmer than its paint.|
S~The sign feels personal in a way a public building's name doesn't.|
S~I'd rather begin with a hello than arrive needing something immediately.
''')
add('wanda_house_sign', 'VerdanturfTown_Text_WandasHouse', 'A sign marks Wanda house.', '''
S~Wanda's house. A nice straightforward answer to the wandering-about-looking-for-Wanda problem.|
N~The named address provides useful orientation. We still need to respect the household.|
N~Found the right place. Knock first.|
S~A name on a home always makes me wonder what ordinary afternoon is happening inside.|
S~I'd ask whether this is a good time before turning up with the whole day's business.|
S~A pleasantly concise sign with no attempt to advertise the residents' virtues.|
S~The house has been successfully introduced. The people remain entitled to do that themselves.|
N~Useful landmark. We can remember the location without bothering anyone now.|
S~An ordinary name can anchor a whole part of town for someone who knows it.|
S~It's nice when a sign helps a visitor without turning a home into an attraction.|
S~I'd ask how the neighborhood knows the place. Homes collect more stories than their signs show.
''')
add('school_sign', 'RustboroCity_Text_TrainersSchoolSign', 'The school sign promises to teach anything about Pokemon.', '''
S~Anything about Pokemon is an enormous syllabus. I hope the chalk gets holidays.|
N~The promise is broad. A specific question would help us find the right lesson.|
N~Good place to ask the basics without pretending we know them.|
S~I like a sign that makes asking seem welcome.|
N~I'd want room for practical care as well as the battle lessons.|
S~A brave educational institution has publicly challenged the word anything to a prolonged duel.|
S~An ambitious promise supported by an alarming future demand for notebooks.|
N~We should ask which lessons fit our current experience.|
S~A place can become welcoming by saying questions belong there.|
N~The promise should help nervous beginners feel allowed to come in. I hope it does.|
S~I'd ask a student which lesson they used outside the classroom first.
''')
add('devon_sign', 'RustboroCity_Text_DevonCorpSign', 'Devon sign claims a wide range of products for everyday living.', '''
N~All our living needs? That's a bold sign. I wonder if it can manufacture a quiet afternoon.|
N~A broad corporate claim rather than a precise product inventory. We'd need examples.|
N~Big promise. I'd check what they actually make.|
N~I wonder how many people inside work on one small part of that enormous sentence.|
N~Useful everyday things are worth making well. The slogan doesn't tell us how well.|
N~A modest little ambition to become responsible for practically everything people might want.|
S~A company attempting to fit the entire day into its product catalogue.|
N~I'd ask which actual need guided the design of a particular product.|
N~A large promise rests on many small things doing their work reliably.|
N~The message is memorable. I would still look for the useful details behind it.|
N~I'd ask an employee which product they're proudest of seeing used in ordinary life.
''')
add('cutter_house_sign', 'RustboroCity_Text_CuttersHouse', 'The sign identifies the Cutter house.', '''
S~The Cutter's house. I hope the hedges don't feel personally threatened by the address.|
N~An occupational household name. It suggests a useful contact, not a service guarantee.|
N~We can ask inside. Best not assume the sign is an open invitation to borrow tools.|
N~I wonder whether the name came first or people started calling the house that.|
S~A neighborhood can remember somebody by the help they give. That's rather nice.|
S~An exceptionally practical title, spared the clutter of unnecessary adjectives.|
S~An address with a sharp reputation. Probably terrible news for unruly branches.|
N~We should ask what help is available and what conditions apply.|
N~A familiar task can become the name of the hands that do it.|
N~It's easy to remember. I'd still want to meet the person instead of knowing only the role.|
S~I'd ask how the house came by that name. Somebody probably has a story.
''')
add('rydel_sign', 'MauvilleCity_Text_BikeShopSign', 'Rydel Cycles advertises riding over gravel with an energetic slogan.', '''
S~The sign promises gravel for the wheels and something much harder to repair for the soul.|
N~The slogan emphasizes an energetic riding experience. Actual bicycle suitability needs checking.|
N~Choose the bike for the ground, not the size of the promise.|
N~I'd start with a quiet stretch before finding out how much shaking I enjoy.|
N~A comfortable fit matters before any grand claim about the ride.|
S~A bicycle shop offering both transport and an unsolicited emotional transformation.|
S~The gravel has been promoted to an agent of personal growth.|
N~We should compare handling and intended terrain before selecting a model.|
N~A road can change the feeling of a day without needing to announce what it does to the soul.|
N~It's a lively invitation. I hope the practical advice inside is just as clear.|
S~I'd ask a customer where their first ride took them after leaving the shop.
''')
add('mauville_game_sign', 'MauvilleCity_Text_GameCornerSign', 'The Game Corner sign advertises a play spot for everyone.', '''
N~A play spot for all. I hope all includes the people who only want to look around.|
N~The broad welcome doesn't explain the costs or rules of the activities inside.|
N~Set a limit before playing anything with a price.|
N~I'd like to know whether there's somewhere quiet to watch without being hurried to join.|
N~Having fun should still leave the rest of the day manageable.|
N~An inclusive invitation with several practical details wisely postponed until after the doorway.|
N~Everyone is welcome. The coins may have a less generous return policy.|
N~We should learn the rules and costs before deciding what to try.|
N~A bright room can offer a little escape. It shouldn't decide how long we stay.|
N~I'd notice whether people seem comfortable leaving, as well as excited to enter.|
N~I'd ask what somebody enjoys about the place besides the possibility of winning.
''')
add('name_rater_sign', 'SlateportCity_Text_NameRatersHouseSign', 'The Name Rater sign advertises Pokemon nickname assessments.', '''
S~An official opinion on nicknames. My imaginary name committee suddenly feels underqualified.|
N~A name can be evaluated for sound or fit, but its personal meaning isn't fully observable.|
N~An opinion can help. The nickname still belongs to the partnership.|
N~I'd be nervous having a name that mattered to me judged by somebody I'd just met.|
N~A silly little name can still carry a lot of affection. I'd want that treated kindly.|
S~A professional appointment for the delicate business of deciding whether Fluffles sounds distinguished.|
S~Someone has established formal authority over affectionate nonsense. Fascinating institution.|
N~I'd ask what criteria the rater uses before treating the result as definitive.|
N~A name can mean more in the voice that calls it than on the page where it's written.|
N~A useful service if it helps the name feel right, rather than simply fashionable.|
S~I'd ask a trainer how their partner got its name before asking anyone to rate it.
''')
add('slateport_harbor_pending', 'SlateportCity_Text_HarborFerryUnderConstruction', 'The harbor notice says the S.S. Tidal is being built at the nearby shipyard.', '''
N~The ferry is close, but some of it may still be in the not-quite-ferry stage.|
N~The notice identifies the construction location. Shortly is not a precise service date.|
N~Check with the harbor before planning a crossing.|
N~I wonder how many people stop here hoping today is the day the notice changes.|
N~The first trip should happen when the ship is ready, even if the waiting feels long.|
N~An enthusiastic forecast from a sign that has delegated all difficult work to the shipyard.|
S~A ship in progress, surrounded by several people's completed travel plans.|
N~We can ask for the actual status rather than infer it from the optimistic wording.|
N~A journey can begin as a space somebody keeps looking at across the water.|
N~I appreciate knowing where the work is happening. It makes the promise less abstract.|
N~I'd ask a yard worker what still needs finishing before passengers can board.
''')
add('slateport_market_sign', 'SlateportCity_Text_MarketSign', 'The market sign promises unusual goods unavailable elsewhere.', '''
S~Nowhere else is a very persuasive place to put on a shopping list.|
N~The claim emphasizes exclusivity. We should inspect the actual goods before accepting it.|
N~Unusual doesn't always mean useful. Look carefully.|
S~I'd like to see things with a little of the maker's personality left in them.|
N~A local market is more interesting when somebody can tell us how the item was made.|
S~An announcement designed to make leaving empty-handed feel like poor geographical judgment.|
S~A sign suggesting our future regret can be prevented through shopping. Crafty.|
N~I'd compare craftsmanship and purpose rather than rarity alone.|
S~A place can leave small traces of itself in what people make there.|
U~I'd look for a distinctive material or shape instead of simply the loudest display.|
S~I'd ask each seller which object they enjoy explaining most.
''')
add('ocean_museum_sign', 'SlateportCity_Text_OceanicMuseumSign', 'The museum sign celebrates the sea role in sustaining life.', '''
S~An enormous thank-you to the sea, written on something reassuringly dry.|
S~The message frames the ocean as central to life rather than merely a route between towns.|
N~Good reason to respect what happens offshore, even when we can't see it.|
S~I like being reminded that the water beyond town is more than empty distance.|
N~A place that feeds and connects so much deserves care, not just admiration.|
S~The sea has received a grand acknowledgment and a building full of supporting exhibits.|
N~A tribute to the enormous thing most of us still try very hard not to fall into.|
U~I'd like the exhibits to show the connections clearly, from small organisms to the whole coastline.|
N~A shore can feel like an ending when it is also where so much begins.|
N~The wording invites a wider kind of attention than simply collecting beautiful views.|
S~I'd ask what visitors notice differently about the sea after leaving the museum.
''')
add('pokemon_fan_sign', 'SlateportCity_Text_PokemonFanClubSign', 'The fan-club sign calls Pokemon admirers together.', '''
S~A gathering for people likely to understand an extremely long story about one adorable nose.|
S~Shared interest gives strangers a clear starting point for conversation.|
S~A friendly reason to meet. Let other people finish their stories, too.|
S~I'd like a room where being fond of a small ordinary thing isn't embarrassing.|
S~Everyone probably has a story about a partner they think nobody has heard properly yet.|
S~An official venue for enthusiasm that has long exceeded what one's neighbors can reasonably absorb.|
S~A building devoted to talking about Pokemon when people finally stop asking us to change the subject.|
N~I'd enjoy hearing what different people notice about the same species.|
S~Affection can make strangers recognize something familiar in one another.|
S~A good fan club leaves room for different kinds of love, not only the loudest one.|
S~I'd start by asking somebody what their partner did that made them laugh recently.
''')
add('slateport_tent_sign', 'SlateportCity_Text_BattleTentSign', 'The Slateport Battle Tent sign encourages finding the ultimate Pokemon.', '''
N~The ultimate Pokemon is a very large thing to look for under a tent.|
N~Ultimate is promotional. The event rules will determine which qualities matter here.|
N~Find the right partner for the format. No single label solves every match.|
N~I'd like the partners already beside us not to feel like placeholders for something better.|
N~A good team starts with understanding what a Pokemon can do, not just wanting the best-sounding one.|
N~A small venue has issued a very grand search warrant.|
S~The ultimate Pokemon has apparently been asked to report to a tent in Slateport.|
N~We should inspect the available choices and their interactions before selecting.|
N~The perfect thing in an advertisement can hide the good thing in front of us.|
N~I'd want to know what makes a choice successful here before chasing the superlative.|
N~I'd ask somebody what they learned to notice after their first attempt.
''')
add('shipyard_wanted_sign', 'SlateportCity_Text_SternsShipyardWantedSign', 'Stern shipyard seeks a sailor able to handle all currents.', '''
N~All currents is a big interview question. I hope the applicant is allowed to say let's check the weather.|
N~The wording seeks extensive navigational skill, though no sailor controls every condition.|
N~Good sailors know when not to sail, too.|
N~I wonder what journeys the person answering this sign would have to tell.|
N~Keeping everyone safe matters more than proving the sign wasn't exaggerating.|
N~An ambitious recruitment notice from a yard attempting to hire an argument with the entire sea.|
N~A sailor wanted; the ocean has declined to provide a consistent job description.|
N~I'd ask about experience, judgment, and emergency preparation rather than accept a confident yes.|
N~A current is something to understand, not something one defeats by claiming never to yield.|
N~The sign sounds impressive. I'd want a workplace that values caution as much as bravery.|
N~I'd ask the crew which decision made them trust a captain most.
''')
add('museum_player_exhibit', 'LilycoveCity_Text_MuseumSignPlayersExhibit', 'The museum public sign advertises the player Pokemon collection on exhibit.', '''
U~Our name is on the museum sign. I wasn't prepared for the building to introduce us.|
S~The sign records a public exhibit connected with our Pokemon. A tangible form of recognition.|
S~Good work earned a place here. Take a moment to enjoy it.|
F~Seeing the name outside feels different from hearing a compliment in a room.|
S~I'd be happy if it helps visitors notice something lovely about the partners.|
S~A familiar name has been promoted to public attraction. I recommend standing here until the surprise passes.|
S~The sign has made the achievement official enough for passersby to ignore on their own schedule.|
S~The exhibit is available for others to experience now. That's a satisfying next step.|
S~Something we shared has found a place where strangers can pause beside it.|
S~I like seeing the partners recognized in a place built for looking carefully.|
U~I'd want to hear what a visitor notices without telling them what they're supposed to admire.
''')
add('beauty_stage', 'LilycoveCity_ContestHall_Text_BeautyContestStage', 'The Beauty Contest stage sign invites admiration of beautiful Pokemon.', '''
S~A stage with permission to simply look lovely. The difficult part is apparently making that look easy.|
N~The sign identifies the Beauty category. Presentation criteria still need a fuller explanation.|
N~A place to show the partner well. Make sure they're comfortable with it.|
N~Being watched for beauty sounds exciting and rather frightening at the same time.|
S~I'd want the preparation to be something the Pokemon enjoys, too.|
S~A formal arena for the deceptively difficult business of looking effortlessly splendid.|
S~Beauty has acquired a competitive schedule and an allocated stage.|
N~We should learn the category's practical judging system before choosing an approach.|
N~An ordinary creature can hold a quiet beauty before anyone announces where to look.|
S~A strong presentation should help the Pokemon's own qualities come through.|
N~I'd ask a participant how they keep the performance feeling natural for their partner.
''')
add('cute_stage', 'LilycoveCity_ContestHall_Text_CuteContestStage', 'The Cuteness Contest stage advertises charming Pokemon performances.', '''
S~Competitive cuteness. My heart has apparently entered without completing any registration.|
N~The category emphasizes a particular presentation quality, not the Pokemon's entire value.|
N~Cute can still take careful preparation. Keep the partner happy.|
F~I suspect I'd be smiling before I remembered I was trying to watch seriously.|
S~A playful partner can make a whole room feel lighter. I'd like that part to stay genuine.|
S~A highly organized institution for the sudden inability of sensible people to stop smiling.|
S~Cuteness, with rules. A startling attempt to regulate a powerful force.|
N~We should find out which performance choices the actual scoring rewards.|
S~A small gesture can change the shape of every face looking at it.|
S~Charm works best when it feels like the Pokemon rather than a costume swallowing it.|
S~I'd ask what little habit made the trainer first think this category suited their partner.
''')
add('smart_stage', 'LilycoveCity_ContestHall_Text_SmartContestStage', 'The Smartness Contest stage invites impressive intelligent Pokemon performances.', '''
S~A place for clever little partners to show their work. I hope someone applauds the planning.|
S~The category highlights an intelligent impression through performance. We'd need the actual criteria.|
N~A clever routine needs a clear plan and practice.|
N~I like the idea of something quiet and careful earning everyone's attention.|
N~I'd want the routine to suit the way the partner actually learns.|
S~A stage where looking thoughtful has finally been given a competitive venue.|
S~Intelligence has agreed to perform in public. A brave departure from its usual preference.|
U~I'd enjoy seeing how trainers make a complicated sequence clear to the audience.|
N~A small choice can reveal a mind more gently than a grand declaration.|
S~The presentation needs to make the idea visible without explaining away all the surprise.|
N~I'd ask what part of the routine took the most work to make seem effortless.
''')
add('tunnel_red_x', 'RustboroCity_Text_TunnelNearingCompletion', 'An optimistic tunnel-completion notice has been crossed out in red.', '''
N~The original sign had plans. The red paint has arrived with a fairly decisive update.|
N~The cancellation mark supersedes the optimistic wording, though it doesn't explain the cause.|
N~Don't plan around the old promise. Find out what's actually open.|
N~It feels sad seeing somebody's hopeful notice left up only to be crossed through.|
N~I'd rather know the route is uncertain now than discover it after a long walk.|
N~A cheerful construction forecast has received an exceptionally concise editorial response.|
N~The paint has defeated the schedule in one large letter.|
N~We should verify the current passage instead of assuming nearing completion still applies.|
N~A red mark can make an unfinished place look more final than the words beneath it.|
N~The correction is visible. A short explanation would have been kinder to travelers.|
N~I'd ask someone nearby what changed rather than invent a story from the crossed-out promise.
''')
add('r101_oldale', 'Route101_Text_RouteSign', 'Route 101 points north toward Oldale Town.', '''
S~Oldale ahead. The arrow seems considerably more certain than my sense of direction.|
N~A northbound marker for Oldale. Useful confirmation of our route.|
N~North for Oldale. Check everyone is ready to keep walking.|
S~A named destination makes the stretch ahead feel less unfamiliar.|
N~Oldale is the next clear target. We can plan the rest after arriving.|
S~A small arrow bravely accepting responsibility for our geography.|
S~The sign knows where it's going. An enviable quality.|
N~That confirms the northward route. We can stop guessing at the turn.|
N~A little word can draw the far end of a path closer.|
N~Plain lettering and a useful arrow. Exactly enough information.|
S~I'd remember this little marker when thinking back on the first part of the journey.
''')
add('r102_oldale', 'Route102_Text_RouteSignOldale', 'The eastbound Route 102 sign directs travelers to Oldale.', '''
N~Oldale to the right. A helpful correction before my feet invent a different plan.|
N~This marker places Oldale eastward along Route 102.|
N~East if we're heading for Oldale. Simple enough.|
N~It's comforting having a familiar name at one end of the road.|
N~A clear return direction is useful, even when we're continuing elsewhere.|
S~Oldale has supplied written instructions for finding it again. Considerate town.|
S~The route offers an answer without requiring a local argument.|
N~We can use this as an orientation point before choosing the next stretch.|
N~A way back can make a way onward feel less lonely.|
N~The direction is clear. I'd keep the junction itself easy to recognize.|
N~I'd look once behind us, so the return view won't seem unfamiliar later.
''')
add('r102_petalburg', 'Route102_Text_RouteSignPetalburg', 'The westbound Route 102 marker points to Petalburg City.', '''
S~Petalburg left. My wandering has been given a proper assignment.|
N~The westward direction leads toward Petalburg along this route.|
N~West for Petalburg. We have our bearing.|
N~I like reaching a sign that confirms we haven't quietly drifted off course.|
N~We can head toward Petalburg without making this junction a whole discussion.|
S~A concise invitation from Petalburg, delivered by an arrow.|
S~The sign has solved the immediate mystery of left.|
N~Good reference point. I'd note the route number as well as the destination.|
N~A city begins as a name waiting at the end of a smaller path.|
N~Clear directions make a place feel more welcoming before you arrive.|
N~I'd ask someone coming from that way how the walk has been today.
''')
add('r103_oldale', 'Route103_Text_RouteSign', 'Route 103 points south toward Oldale.', '''
N~Oldale below us on the sign. I appreciate a town willing to be found from several directions.|
N~The marker establishes a southbound route to Oldale.|
N~South gets us toward Oldale. Keep that in mind.|
N~Knowing where the nearby town is helps me relax a little.|
N~A clear stop to return to is useful when plans change.|
S~Oldale has left a polite arrow here in case the landscape becomes unpersuasive.|
S~A small direction with none of the usual dramatic warnings attached.|
N~We can anchor the return route to this marker.|
N~Some paths feel steadier once the way back has a name.|
N~The simple sign does its job without making the place sound bigger than it is.|
N~I'd notice the surroundings here, not only the words, so we can recognize the spot again.
''')
add('briney_cottage', 'Route104_Text_MrBrineysCottage', 'A roadside sign identifies Mr. Briney cottage.', '''
S~Mr. Briney's cottage. A small home deserves an easy way for visitors to find it.|
N~The sign identifies a private residence, not a general service counter.|
N~We found the cottage. Best begin by knocking.|
S~Cottage is such a gentle word to meet after a stretch of walking.|
S~I'd ask whether it's a good time before arriving with an errand.|
S~A modest address, resisting the local tendency to promise greatness on a sign.|
S~The cottage has been introduced without exaggeration. Refreshing.|
N~Useful landmark. We can note it even if we're not visiting now.|
S~A little home can hold a very large place in someone's traveling plans.|
S~It's personal without being showy. The name is enough.|
S~I'd like to hear how long people have used the cottage as a landmark.
''')
add('r104_petalburg', 'Route104_Text_RouteSignPetalburg', 'Route 104 directs travelers east to Petalburg City.', '''
N~Petalburg to the right. The sign has saved us a very elaborate wrong turn.|
N~Eastward travel leads toward Petalburg from this marker.|
N~Right for Petalburg. No need to overthink the arrow.|
N~A familiar city name makes it easier to picture where the path ends.|
N~We can decide whether Petalburg fits the day before walking all the way there.|
S~A short written message from a city unwilling to leave its location to rumor.|
S~An arrow doing dependable work for very little recognition.|
N~I'd use both the route number and destination to check our position.|
N~A known place can make an unfamiliar crossing feel smaller.|
N~The layout makes the choice easy to see at a glance.|
N~I'd ask a traveler from that direction whether anything has changed along the path.
''')
add('r104_rustboro', 'Route104_Text_RouteSignRustboro', 'The northbound Route 104 sign points toward Rustboro.', '''
S~Rustboro ahead. Good to know where our feet are holding their next meeting.|
N~The marker identifies the northward approach to Rustboro.|
N~North for Rustboro. Let's keep the group together.|
N~I like when a long walk starts gathering around one clear destination.|
N~We can use Rustboro as the next place to take stock.|
S~A city has sent a small arrow to collect visitors from the road.|
S~The northward option has acquired a reassuringly specific name.|
N~This gives us a clear route reference instead of relying on a guess.|
N~A far place becomes a little more real when its name appears beside the path.|
N~I appreciate directions that stay readable while you're still walking.|
S~I'd like to hear what someone expected from Rustboro before seeing it for themselves.
''')
add('petal_shop_sign', 'Route104_Text_PrettyPetalFlowShop', 'The roadside sign identifies the Pretty Petal Flower Shop.', '''
S~Pretty Petal is a lovely name. I hope the flowers approve of being advertised so confidently.|
S~A clearly named specialist shop. We'd need to ask which plants and supplies are available.|
N~Flower shop here. We can stop if there's something we need.|
S~The name makes the doorway feel a little softer than the road.|
S~I'd like to ask which plants do well in an ordinary traveler's care.|
S~A shop name that has sensibly entrusted most of the charm to the flowers.|
S~An establishment promising petals rather than personal transformation. Sensible.|
N~I'd ask about the growing conditions before choosing something to bring home.|
S~A small shop can give passing people a reason to look down gently.|
S~The name is bright without feeling noisy. It suits the invitation.|
S~I'd ask the staff which flower visitors most often stop to admire.
''')
add('seashore_house_sign', 'Route109_Text_SeashoreHouseSign', 'The beach house sign advertises hot battles for enthusiastic trainers.', '''
N~The sands, the battles, the trainers. Somebody here has an extremely limited temperature setting.|
N~The repeated heat imagery advertises energetic competition, not precise event rules.|
N~Sounds lively. Check what they're offering before jumping in.|
N~I'd probably want a quieter patch of beach after reading all that.|
N~Hot weather and hot competition both go better with enough water.|
S~A vigorous advertisement written by someone determined that no part of the visit remain lukewarm.|
N~A house that appears personally offended by a comfortable temperature.|
N~We should find out the actual challenge and our readiness before accepting.|
N~A bright shore can hold plenty of noise without asking everyone to become part of it.|
N~The sign knows its audience. I'd like it to leave room for a calmer visitor, too.|
N~I'd ask what people enjoy about the house once the shouting about heat has finished.
''')
add('r110_slateport', 'Route110_Text_SlateportCitySign', 'The Route 110 sign points south toward Slateport City.', '''
S~Slateport southward. The road is being very clear about where the next city has gone.|
N~The marker identifies the southbound route toward Slateport.|
N~South for Slateport. Good point to check our direction.|
N~A city name on the road always makes me think of the people still going about their day there.|
N~If we need a proper stop, we know which direction to choose.|
S~Slateport has delegated its roadside welcome to a dependable arrow.|
S~A clear route to a place with considerably more conversations than this sign.|
N~I'd compare this marker with where we last turned before proceeding.|
N~A busy place can feel distant until a little board brings its name back.|
N~The destination is easy to pick out. That's good sign work.|
N~I'd ask a person coming from Slateport what caught their attention there today.
''')
add('cycling_road_sign', 'Route110_Text_CyclingRoadSign', 'The sign identifies Seaside Cycling Road.', '''
S~A whole road named for bicycles. I hope the wheels feel properly appreciated.|
N~The name identifies a cycling route. We should check access conditions separately.|
N~Cycling Road here. Watch for riders before stepping across.|
N~I wonder how different the same view feels when you're moving quickly past it.|
N~A ride is nicer when there's room to travel at a comfortable pace.|
S~A road with a very clear opinion about the preferred method of arriving.|
S~The route has declared allegiance to wheels. Feet may wish to consult the rules.|
N~I'd check the surface and traffic flow before setting off.|
N~A long line of road can change the rhythm of a journey without changing its destination.|
N~The name is useful. I'd still want the entry and exit clearly marked.|
S~I'd ask a regular rider which part of the route makes them slow down and look.
''')
add('rival_graffiti', 'Route110_Text_AquaWasHere', 'Team Magma has painted over Team Aqua graffiti on a sign.', '''
N~Two teams, one sign, and neither has apparently considered a separate piece of paper.|
N~The layers establish a sequence of markings. They don't demonstrate control of the route.|
N~Paint isn't ownership. I wish they'd leave travelers' signs useful.|
N~It's an oddly small argument to leave behind after making such grand claims.|
N~Somebody else has to clean that up. Rivalry doesn't make the work disappear.|
N~A contest for supremacy has reduced itself to borrowing the same stationary board.|
S~A struggle for dominance conducted through competitive vandalism. Dignified.|
N~The original directions may be obscured. I'd verify the route with another source.|
N~One loud mark covers another, and the wood is left carrying both.|
A~They've treated a public sign as a place for their argument. Poor manners.|
N~I'd ask a local whether the original message is still known before trusting what's left.
''')
add('r110_to103', 'Route110_Text_Route103Sign', 'A Route 110 marker points west to Route 103.', '''
N~A route pointing to another route. The journey has developed a helpful little chain of addresses.|
N~The westward connection leads toward Route 103 rather than directly naming a town.|
N~West for Route 103. Check that connection fits where we're heading.|
N~Numbers are harder for me to remember than places. I'd pause to get this one straight.|
N~We should decide whether this is our turn before the path makes the decision for us.|
N~A concise introduction to the road next door. Efficient local diplomacy.|
S~One numbered path has supplied directions to its numbered acquaintance.|
N~I'd connect this turn with the larger route plan before taking it.|
N~A junction can be clear nearby and still leave the far destination uncertain.|
N~The route number is the useful part here. I'd make sure it stays legible.|
N~I'd ask where travelers usually go after taking that turn.
''')
add('seaside_parking', 'Route110_Text_SeasideParkingSign', 'The sign marks a seaside parking area.', '''
S~Even the parked vehicles get a seaside visit. A remarkably pleasant place to wait.|
N~A designated stopping area helps distinguish waiting space from the through route.|
N~A place to stop. Keep the route itself clear.|
S~I like a spot where pausing doesn't mean being in anybody's way.|
N~A planned stop can make the rest of a journey easier.|
S~A humble notice recognizing that even purposeful travel occasionally needs to stand still.|
S~A location officially permitted to make no progress for a while.|
N~I'd check the marked boundaries before using the area.|
S~A place for waiting can still have a view worth arriving for.|
N~Useful information, especially where several kinds of travelers share the same space.|
S~I'd look out toward the water for a moment rather than treat the stop as wasted time.
''')
add('r110_mauville', 'Route110_Text_MauvilleCitySign', 'The Route 110 marker directs travelers north toward Mauville City.', '''
S~Mauville ahead. The arrow has given this stretch a very definite purpose.|
N~The northward route leads toward Mauville from this marker.|
N~North for Mauville. Keep an eye on the next junction.|
N~It's nice when the destination stops being a guess and becomes a name beside the path.|
N~We can take stock on reaching Mauville instead of making every decision on the road.|
S~A short invitation from Mauville, spared the trouble of sending anyone out to wave.|
S~The sign has maintained its position while directing everyone else onward. Dedicated work.|
N~I'd note the route number so the next marker can confirm our progress.|
N~A city's name can pull a long path gently into focus.|
N~The arrow and place name do their jobs without competing for attention.|
N~I'd ask someone returning from Mauville which landmark helped them find their way.
''')
add('trick_house_sign', 'Route110_Text_TrickHouseSign', 'The Trick House sign gives precise small-step directions to the entrance.', '''
S~Three steps right, two up. The sign is oddly precise for a place announcing tricks.|
N~The directions are explicit. Their playful framing doesn't make them a guarantee about the interior.|
N~Find the house first. Expect the useful instructions to become less simple inside.|
N~I think the word wondrous is doing its best to distract me from trick.|
N~I'd like to know whether we're ready for a puzzle before letting curiosity take over the afternoon.|
S~A suspiciously helpful opening from a host whose profession appears to be making things less straightforward.|
S~The first trick is apparently persuading us that all the instructions will be this clear.|
N~We can test the stated steps without making assumptions about the next challenge.|
N~A very small path leads toward a promise of much larger confusion.|
N~The directions feel like part of the invitation's personality. That's rather effective.|
S~I'd ask a visitor whether the house was what they expected after following such a tidy little route.
''')
add('r111_mauville', 'Route111_Text_RouteSignMauville', 'Route 111 points south toward Mauville City.', '''
N~Mauville southward. It's comforting when a city stays where the last sign said it would.|
N~A southbound confirmation for Mauville along Route 111.|
N~South takes us toward Mauville. Remember this marker.|
N~I like having a clear townward direction when the road starts feeling long.|
N~A return route is useful even when we aren't taking it yet.|
S~Mauville has submitted its whereabouts in writing. Excellent civic cooperation.|
S~The sign remains helpfully certain about one thing in the landscape.|
N~I'd connect this marker to the previous junction so the route stays clear.|
N~A way back can be a comfort rather than a change of plan.|
N~Clear orientation makes a simple roadside stop feel less uncertain.|
N~I'd ask how far someone coming this way has already walked, rather than assume the city is close.
''')
add('winstrate_sign', 'Route111_Text_WinstrateHouseSign', 'The Winstrate house sign proclaims family unity.', '''
S~One heartbeat for the whole family sounds efficient, though I hope everyone agrees about bedtime.|
N~The wording expresses solidarity. It doesn't establish identical views on every subject.|
N~Close family. Still good for each person to have a say.|
N~I like the warmth in it. I wonder how quietly they show that feeling when nobody's visiting.|
N~Unity can mean helping with the ordinary chores as much as making a proud declaration.|
S~A household announcing complete coordination. I would love to hear the discussion about supper.|
S~One shared heartbeat, several separate opinions. I assume the usual arrangement survives.|
N~Working together requires communication, not merely matching enthusiasm.|
N~Several lives can share a home without needing to become one life.|
N~It's a confident family introduction. I'd want each person's voice to fit inside it.|
S~I'd ask what the family most enjoys doing together when they aren't making an impression on visitors.
''')
add('r111_to112', 'Route111_Text_RouteSign112', 'Route 111 directs travelers west toward Route 112.', '''
N~Route 112 to the left. The numbers have agreed on a perfectly sensible next introduction.|
N~This marks the westward connection from Route 111 to Route 112.|
N~West for 112. Check the destination beyond it before turning.|
N~I like reading the number twice instead of realizing later I remembered it wrong.|
N~A clear junction is a good place to decide the plan, not hurry past it.|
S~A numbered road politely handing the journey to its immediate numerical successor.|
S~The next route is conveniently numbered. Geography rarely offers such tidy manners.|
N~We should connect this turn to the larger route we're following.|
N~A small arrow can change a long stretch of the day.|
N~Useful sign. I'd also remember which way we approached the junction.|
N~I'd ask someone using that turn what landmark they expect to reach next.
''')
add('r111_to113', 'Route111_Text_RouteSign113', 'A Route 111 marker points west toward Route 113.', '''
N~Left for Route 113. The sign has skipped a number without appearing remotely troubled.|
N~The westward connection here leads to Route 113, so the marker's position matters.|
N~Route 113 this way. Don't confuse it with another westward turn farther back.|
N~This is why I like a clear number beside the arrow. Left alone wouldn't tell enough.|
N~I'd pause here to make sure this is our intended turn.|
N~A useful reminder that roads are under no obligation to arrange themselves like a counting lesson.|
S~The numbers are labels, mercifully free of a duty to stand in a straight queue.|
N~We should note this particular junction rather than remember only west.|
N~Similar choices can lead to very different stretches of sky.|
N~The small distinction between route numbers is doing important work here.|
N~I'd look back after the turn so the return junction is easier to recognize.
''')
add('rest_stop_sign', 'Route111_Text_OldLadysRestStopSign', 'An old woman rest-stop sign welcomes weary travelers.', '''
S~My bones have never felt so personally invited by a sign.|
S~A clearly identified rest stop. We should ask about the available accommodation before assuming.|
S~A place to rest. Worth checking in before pushing farther.|
S~That wording feels kind after a long stretch of road.|
S~I'd rather stop while a break is pleasant than wait until everyone is miserable.|
S~An invitation addressed directly to the part of us most qualified to appreciate it.|
S~At last, roadside publicity acknowledging the existence of tired joints.|
N~A planned rest can improve the rest of the route. We should see what's available.|
S~A little shelter can change the weight of every step that came before it.|
S~The personal wording is warmer than a list of services. It feels like someone means it.|
S~I'd ask our host about the travelers she remembers, if she felt like talking.
''')
add('trainer_hill_sign', 'Route111_Text_TrainerHillSign', 'A sign points to Trainer Hill and challenges enthusiastic trainers to climb.', '''
N~Trainer Hill has challenged our enthusiasm before we've even reached its entrance.|
N~The sign identifies an eastward entrance. The actual challenge rules need separate checking.|
N~Hill entrance to the right. Learn the format before committing.|
N~I hope being quiet doesn't make someone seem less welcome there.|
N~A climb is better begun with enough energy than with a loud promise.|
S~A spirited invitation to ascend, written by someone comfortably remaining at ground level.|
N~The sign is very excited about our legs doing additional work.|
N~We should establish the challenge's scope and expected time before entering.|
N~A height can call to people without asking every heart to burn the same way.|
N~The message knows its eager audience. I'd still like clear practical details inside.|
N~I'd ask a recent challenger what was harder than they'd expected.
''')
add('cable_car_arrow', 'Route112_Text_MtChimneyCableCarSign', 'A sign points a short way north to the Mt. Chimney cable car.', '''
S~A short walk to a ride. I appreciate this very modest first installment of mountain climbing.|
N~The marker gives both direction and a qualitative distance to the cable-car access.|
N~North a short way. Check the service when we reach it.|
S~It's nice when the next part doesn't require guessing which slope to follow.|
N~A ride can save the team some effort if the route suits our plans.|
S~The mountain has arranged for most of the ascent to happen while we remain comparatively still.|
S~A promising alliance between a small walk and a large lifting mechanism.|
U~I'd like to see how the cable system handles the gradient once we arrive.|
S~A little path leads to a different way of leaving the ground behind.|
N~Short and directional. The sign respects a traveler's immediate question.|
N~I'd ask the attendant about the trip before deciding where we're headed afterward.
''')
add('chimney_transport', 'Route112_Text_MtChimneySign', 'The mountain sign directs travelers toward the cable car for the summit or Lavaridge.', '''
N~The mountain has supplied instructions instead of simply looming at us. Thoughtful.|
N~The notice recommends the cable-car route for the summit and Lavaridge approach.|
N~Use the marked route. No need to improvise a climb.|
N~I like being told how the destinations connect before starting uphill.|
N~We can plan the next stage without using the team's energy on an uncertain shortcut.|
N~An impressive landmark briefly setting aside grandeur to explain the transport arrangements.|
S~The summit is available without us arguing personally with every slope.|
N~We should confirm the connection and operating status at the station.|
N~A high place can feel nearer when someone explains the ordinary way toward it.|
N~The destination choices are clear. I'd check which one fits the rest of our day.|
N~I'd ask a returning visitor where the ride left them and what came afterward.
''')
add('r112_lavaridge', 'Route112_Text_RouteSignLavaridge', 'Route 112 points west toward Lavaridge Town.', '''
S~Lavaridge to the left. A clear townward arrow is a very pleasant roadside invention.|
N~The westbound marker leads toward Lavaridge from Route 112.|
N~West for Lavaridge. Good to have the next direction settled.|
N~The town name gives me something familiar to picture beyond the path.|
N~We can make Lavaridge the next proper stopping point if that suits everyone.|
S~A modest little arrow has done more for our route than several dramatic horizons.|
S~The sign has successfully narrowed the world to one useful direction.|
N~I'd check the route number again at the next junction.|
N~A destination can make the empty stretch ahead feel inhabited already.|
N~I appreciate a marker that answers the immediate question cleanly.|
N~I'd ask a traveler coming from Lavaridge how the approach feels from this side.
''')
add('r113_to111', 'Route113_Text_RouteSign111', 'An eastward Route 113 sign leads back toward Route 111.', '''
N~Route 111 rightward. The numbers have left us a way to put the journey back in order.|
N~This marker confirms the eastward connection to Route 111.|
N~East for 111. Useful return direction.|
N~I like knowing how to retrace a stretch without having to remember every bend.|
N~A clear way back helps if someone needs a shorter day than planned.|
S~The route has supplied a written return address. Excellent manners for a road.|
S~A number we recognize, doing the comforting work of a familiar name.|
N~We should note the junction's appearance as well as the numbered connection.|
N~A road back isn't always a retreat. Sometimes it's simply another chosen direction.|
N~The marker makes the route relationship easy to follow.|
N~I'd ask which landmark near the turn is easiest to recognize in poorer light.
''')
add('r113_fallarbor', 'Route113_Text_RouteSignFallarbor', 'Route 113 directs travelers west toward Fallarbor Town.', '''
S~Fallarbor left. That's a lovely amount of certainty to fit on a little board.|
N~The marker establishes the westbound approach toward Fallarbor.|
N~West for Fallarbor. Keep that direction through the next stretch.|
N~A townward sign makes me notice how tired I've been pretending not to feel.|
N~We can think about a proper break once we reach Fallarbor.|
S~Fallarbor has placed a polite invitation at the end of an arrow.|
S~The leftward option has become less abstract and considerably more welcoming.|
N~I'd use this marker to confirm the planned approach before continuing.|
N~A named place can feel like a resting hand before the buildings appear.|
N~The sign does a quiet job well. I appreciate that on a long walk.|
S~I'd like to hear how someone described Fallarbor before they first visited it.
''')
add('glass_workshop_sign', 'Route113_Text_GlassWorkshopSign', 'The Glass Workshop sign advertises turning volcanic ash into objects.', '''
U~The ash has a second career waiting. That's a splendid result for something so good at getting everywhere.|
S~The workshop connects a local material with a useful manufacturing process. I'd like to see the steps.|
N~Useful work. Ask before wandering near anything hot.|
S~I like the thought of something carried by the wind becoming a thing someone keeps.|
N~Making something useful out of the local mess seems like practical kindness.|
S~An establishment offering volcanic ash a more distinguished future than settling on our clothes.|
S~The mountain's leftovers have found a respectable trade.|
U~I'd love to see the preparation and heating stages, from raw ash to finished surface.|
N~Something that once drifted freely can learn to hold a shape.|
U~I'd look at how the material changes the color and texture of the finished pieces.|
S~I'd ask the maker which design best shows what this particular ash can do.
''')
add('meteor_to_rustboro', 'Route114_Text_MeteorFallsSign', 'A Meteor Falls sign identifies a route through toward Rustboro City.', '''
N~Rustboro through Meteor Falls. The directions have acquired a much grander middle name.|
N~The sign identifies a connection, not the conditions or length of the passage.|
N~Through there for Rustboro. Check supplies before choosing that route.|
N~Through here always makes a place feel like a story with another side waiting.|
N~I'd want to know what the crossing asks of the team before calling it a shortcut.|
N~A cityward route presented with an unexpectedly atmospheric intermediate appointment.|
N~A connection on a sign may still be a considerable undertaking underfoot.|
N~We should learn the passage conditions rather than infer convenience from the word through.|
N~A place can be both somewhere to arrive and somewhere others pass across.|
N~The sign gives the endpoint. I'd still want the useful details in between.|
N~I'd ask someone who's just crossed what part required the most attention.
''')
add('fossil_house_sign', 'Route114_Text_FossilManiacsHouseSign', 'The Fossil Maniac house sign welcomes fossil donations.', '''
S~Fossils gratefully accepted. That's a very polite way for a house to request extremely old visitors.|
S~The invitation identifies a specific collecting interest, not a promise about any specimen we bring.|
N~Ask before handing over anything valuable. Clear up the terms.|
S~I like that the sign sounds grateful before anyone has even knocked.|
N~I'd ask what information about the find would help, not just bring the object without its story.|
S~A welcome addressed to prehistoric remains and the living people carrying them.|
S~A household with exceptionally relaxed expectations about the age of its guests.|
N~The context of a fossil's discovery may be as useful as the specimen itself.|
N~An old life has traveled a long way to become somebody's present fascination.|
S~The enthusiasm comes through plainly. I'd like the care inside to match it.|
N~I'd ask what the owner hopes to learn from a new fossil, rather than only which ones they want.
''')
add('lanette_house_sign', 'Route114_Text_LanettesHouse', 'A sign identifies Lanette house.', '''
S~Lanette's house. A place to find the person, if the work hasn't persuaded her to lose track of the door.|
N~A useful named address. We should respect that it's also her home.|
N~Found the house. Let's knock and ask if she's free.|
N~I'd like to visit without making her feel obliged to stop what she's doing immediately.|
N~We can begin by asking whether she wants company before bringing a question.|
S~A personal address, helpfully distinguishing the resident from the many things she may be working on.|
S~The house appears properly labeled. Finding its occupant's attention may be a separate task.|
N~I'd be glad to hear about her work when she has time to explain it.|
N~A home should leave some room for the person beyond the work people visit to discuss.|
S~A simple name can make a remote address feel approachable.|
S~I'd ask what she enjoys about living here before turning the whole visit into an interview.
''')
add('r115_rustboro', 'Route115_Text_RouteSignRustboro', 'Route 115 points south toward Rustboro City.', '''
N~Rustboro southward. The city seems well supplied with roads willing to introduce it.|
N~This is a southbound marker toward Rustboro on Route 115.|
N~South for Rustboro. Good direction to keep straight.|
N~I like a clear cityward sign when several stretches of road look alike.|
N~We can use Rustboro as a proper point to reassess what comes next.|
S~Rustboro has provided another concise answer to where do our feet belong now.|
S~A useful arrow with no ambition to become a motivational speech.|
N~I'd compare the route number with the planned approach before moving.|
N~A familiar place can wait at the far end of a path we haven't learned yet.|
N~The marker is useful precisely because it doesn't ask us to remember more than necessary.|
N~I'd ask someone from that direction whether the route is clear today.
''')
add('meteor_to_fallarbor', 'Route115_Text_MeteorFallsSign', 'A Meteor Falls marker identifies the passage toward Fallarbor.', '''
N~Fallarbor through Meteor Falls. A useful answer with quite a lot left between the words.|
N~The sign describes a regional connection, not an assurance of easy passage.|
N~Through there for Fallarbor. Make sure we're ready for the crossing.|
N~I'd want to know what the way feels like before treating the name as just another turn.|
N~A route can be useful without being the best choice for a tired team today.|
N~A calm little sign has filed a potentially complicated journey under through here.|
N~The map connection is concise. The actual walking may be less so.|
N~We should confirm which parts of the passage are accessible before committing.|
N~An opening in the land can make two places feel nearer than the journey between them.|
N~The endpoint helps. I'd still ask about the stretch the sign leaves undescribed.|
N~I'd ask a recent traveler what made them stop and look while crossing.
''')
add('r116_rustboro', 'Route116_Text_RouteSignRustboro', 'The Route 116 sign points west toward Rustboro.', '''
S~Rustboro to the left. A small sign has done its part to keep us from becoming a local mystery.|
N~The marker confirms the westward direction toward Rustboro.|
N~West for Rustboro. Remember where this sign stands.|
N~I like having something clear to look for if we come back this way.|
N~We can decide whether to return to the city before walking farther past the junction.|
S~A dependable roadside answer, requiring no dramatic discovery or complicated introduction.|
S~The sign has provided clarity without even standing up. Efficient.|
N~I'd connect the marker with our last turn so the whole route remains coherent.|
N~A clear way back can loosen the feeling of being far from anywhere.|
N~The direction is easy to read. That matters more than making a sign memorable.|
N~I'd note what the junction looks like from both approaches.
''')
add('rusturf_cancel_route', 'Route116_Text_RusturfTunnelSign', 'The Rusturf Tunnel notice names its intended connection and says construction was canceled.', '''
N~The sign promises two towns and then apologizes to the whole plan. That's a difficult second paragraph.|
N~The intended link and canceled construction are separate facts. Current access still needs checking.|
N~Don't assume a through route from the name. Find out what's actually passable.|
N~I wonder how people felt when the notice changed from a promise to a cancellation.|
N~A canceled project can still leave travelers planning around an old hope. Better to ask.|
N~An ambitious connection followed by a remarkably final piece of administrative punctuation.|
N~The tunnel has two destinations and an unfortunately uncertain middle.|
N~We should verify present conditions instead of treating the proposed link as completed.|
N~An unfinished path can keep the shape of the lives people hoped it would join.|
N~It's useful that the cancellation is explicit. The reason would help make the notice clearer.|
N~I'd ask someone nearby how people travel between the towns now.
''')
add('tunneler_rest', 'Route116_Text_TunnelersRestHouse', 'A sign identifies the tunnel workers rest house.', '''
S~A rest house for people digging a road. Good to know the planning included somewhere to stop.|
N~A dedicated rest location acknowledges the support needed alongside the construction itself.|
S~Hard work needs proper breaks. Good place for one.|
N~I wonder what the workers talk about when they finally come back into the light.|
S~I'd like the room to have good chairs and something warm after that kind of work.|
S~A modest building performing the essential task omitted from most grand construction announcements.|
S~An architectural endorsement of sitting down. Excellent civic work.|
N~Rest belongs in a working system, not outside the schedule as an afterthought.|
N~A place to lay down the weight before lifting it again.|
N~The plain name puts the people doing the work ahead of the impressive project.|
N~I'd ask which part of the house workers appreciate most after a shift.
''')
add('r117_verdanturf', 'Route117_Text_RouteSignVerdanturf', 'Route 117 points west toward Verdanturf Town.', '''
S~Verdanturf leftward. A clear destination makes the road feel a little less like wandering.|
N~This marks the westbound approach toward Verdanturf.|
N~West for Verdanturf. Check the next junction as we go.|
N~The town name feels easier to carry in my head than a series of turns.|
N~We can make Verdanturf the next planned stop instead of walking until someone is exhausted.|
S~A tidy invitation from the town, issued in arrow form.|
S~The sign has made one branch of the world a little less ambiguous.|
N~I'd note both the route and destination to keep the approach clear.|
N~A place begins to draw near when its name keeps appearing beside the path.|
N~Good direction work doesn't need much decoration. This is enough.|
N~I'd ask a traveler from Verdanturf what they noticed on the walk out.
''')
add('r117_mauville', 'Route117_Text_RouteSignMauville', 'The eastward Route 117 marker leads toward Mauville.', '''
N~Mauville rightward. The road has politely declined to let us call every direction roughly that way.|
N~The sign identifies the eastbound connection toward Mauville.|
N~East for Mauville. Useful direction to keep in mind.|
N~I like seeing a destination we can recognize instead of only another route number.|
N~A cityward turn can be useful when the team needs a proper stop.|
S~A concise correction to the adventurous strategy of following whichever way looks convincing.|
S~The arrow has settled one debate before our feet could start it.|
N~We can use this marker to check the larger route plan.|
N~A familiar name gives the path ahead a small center of gravity.|
N~The sign is easy to read without stopping in the middle of the junction.|
N~I'd look back once after turning so the way home has a familiar shape, too.
''')
add('day_care_sign', 'Route117_Text_DayCareSign', 'The Day Care sign offers to raise travelers Pokemon.', '''
S~A place for Pokemon to spend time without us. I wonder what stories they'd bring back.|
N~The advertised service concerns care and growth. The specific conditions deserve checking.|
N~Ask how they care for the partners before leaving anyone.|
N~I'd want to know the little one feels comfortable with the people there first.|
N~Good care starts with learning the partner's habits, not merely taking a name.|
N~A generous offer involving considerably more daily work than its short sign suggests.|
S~A household volunteering to receive several other households' peculiar little routines.|
N~We should understand the arrangement and any consequences before making a deposit.|
N~Being cared for by different hands can still begin with a gentle introduction.|
N~I'd watch how the staff greet a nervous Pokemon. That would tell me more than the sign.|
N~I'd ask what the partners spend an ordinary afternoon doing here.
''')
add('r118_mauville', 'Route118_Text_RouteSignMauville', 'Route 118 points west toward Mauville City.', '''
N~Mauville to the left. The sign has supplied an answer before we could invent a scenic mistake.|
N~Westward travel leads toward Mauville from this route marker.|
N~Left for Mauville. No need to second-guess the clear part.|
N~It's nice having a cityward direction even when we aren't taking it yet.|
N~A known place to return to helps us choose how far to go today.|
S~A city extending a very economical roadside introduction.|
S~The destination remains helpfully specific while the rest of the horizon does whatever it likes.|
N~I'd connect this with the route we approached from before moving on.|
N~A way back can sit quietly beside a way toward something new.|
N~The useful detail is clear at a glance. That's a kindness to a tired traveler.|
N~I'd ask someone coming from Mauville whether the route behind them is clear.
''')
add('r118_to119', 'Route118_Text_RouteSign119', 'A Route 118 marker directs travelers north toward Route 119.', '''
N~Route 119 ahead. The numbered roads are continuing their surprisingly long introduction.|
N~The northward connection leads to Route 119. Its onward destination is not specified here.|
N~North for 119. Check the next part of the plan before continuing.|
N~I like knowing the next number, though I'd still want a place name farther along.|
N~Let's make sure everyone wants to continue rather than follow the arrow automatically.|
N~A helpful handover to the next road, which will presumably provide its own explanation.|
S~The route has named its successor and retained no further responsibility.|
N~We should relate this connection to our intended destination before taking it.|
N~A small beginning can point toward a much longer unfamiliar stretch.|
N~The sign answers the junction's question. It doesn't need to answer the whole journey.|
N~I'd ask a returning traveler what the next useful landmark is.
''')
add('r119_fortree', 'Route119_Text_RouteSignFortree', 'Route 119 points east toward Fortree City.', '''
S~Fortree rightward. That's a very welcome name to give the next part of the walk.|
N~The sign confirms the eastward approach toward Fortree.|
N~East for Fortree. Keep the team together through the turn.|
N~Seeing the city named makes the road feel less endless.|
N~We can decide what needs doing after a proper stop in Fortree.|
S~A small arrow doing the encouraging work of a much larger welcome.|
S~The city has sent a concise reminder that the road does eventually reach somewhere.|
N~I'd check this marker against our last turn before continuing.|
N~A place can begin to feel close before the first building appears.|
N~The name stands out well. That's the detail a traveler is looking for.|
N~I'd ask someone who just left Fortree what view told them they'd reached the city.
''')
add('weather_institute_sign', 'Route119_Text_WeatherInstitute', 'The sign identifies the Weather Institute.', '''
S~An entire institute for the sky's changing moods. I hope the clouds answer their correspondence.|
S~A dedicated research site suggests sustained observations rather than a single forecast.|
N~Weather Institute here. Useful people to ask before a difficult trip.|
N~I wonder whether they have a favorite kind of weather to study.|
N~A good forecast helps a lot of ordinary people plan an ordinary day. Worthwhile work.|
S~A building devoted to persuading the atmosphere to explain itself. Ambitious employment.|
S~The sky has acquired an official audience and several persistent questions.|
U~I'd love to know which measurements they gather here and how the instruments are placed.|
N~Some people spend their days noticing what everyone else calls simply the sky.|
N~A plain name for work that changes how a whole region plans.|
N~I'd ask what weather event made one of the researchers choose this field.
''')
add('r120_fortree', 'Route120_Text_RouteSignFortree', 'Route 120 directs travelers west toward Fortree.', '''
N~Fortree to the left. A useful reminder that the town hasn't vanished behind our last turn.|
N~This marker identifies the westward connection back toward Fortree.|
N~West for Fortree. Keep that return direction clear.|
N~A familiar city name makes the path feel less isolated.|
N~We have a clear option if the day calls for going back instead of pushing farther.|
S~Fortree has supplied a written return invitation. A thoughtful roadside habit.|
S~The sign offers certainty in a conveniently readable quantity.|
N~I'd remember the junction's appearance alongside the name.|
N~A road back can make the road onward feel easier to choose.|
N~The marker does what it needs to without making the route sound like an advertisement.|
N~I'd look at the path from both directions before leaving the junction behind.
''')
add('r120_to121', 'Route120_Text_RouteSign121', 'A junction sign distinguishes westward Route 120 from eastward Route 121.', '''
N~One sign, two route numbers. A small committee has successfully agreed which way everything is.|
N~The marker contrasts Route 120 westward with Route 121 eastward. Useful relational information.|
N~120 west, 121 east. Choose before the feet choose for us.|
N~I like a junction that tells both sides of the choice.|
N~We can talk through the next stop here instead of discovering later we followed different plans.|
N~A concise diplomatic agreement between neighboring roads.|
S~Two paths, clearly labeled. A luxurious amount of honesty for a junction.|
N~We should map both branches to our intended destination rather than choose by number alone.|
N~A dividing place can still be clear without deciding for us.|
N~The paired arrows make the relationship easy to understand. Good layout.|
N~I'd ask everyone which way they thought we were going before making the turn.
''')
add('pyre_pier_worn', 'Route121_Text_MtPyrePierSign', 'An old, worn pier sign barely identifies the way toward Mt. Pyre.', '''
D~The sign is working very hard to remain a sign. I think it deserves a careful reader.|
N~The surviving text identifies the pier, but wear limits how much else can be recovered.|
N~Read what's still clear. Don't invent the missing directions.|
N~I wonder how many people have stopped here with something difficult on their minds.|
N~A worn sign still needs to guide the next traveler. Somebody should look after it.|
N~A long-serving notice approaching retirement without a replacement visibly arranged.|
N~Time has edited the directions rather more aggressively than is useful.|
N~I'd confirm the route elsewhere instead of guessing at illegible portions.|
D~A place of parting has nearly lost the words that lead toward it.|
N~The wear carries history, but readability still matters to people arriving now.|
N~I'd record only what remains legible and ask someone nearby about the missing part.
''')
add('safari_sign', 'Route121_Text_SafariZoneSign', 'The Safari Zone sign advertises many rare Pokemon.', '''
U~A place full of rare Pokemon. That's a very loud invitation to bring our quietest manners.|
N~The claim concerns species uncommon elsewhere. It doesn't guarantee any particular encounter.|
N~Look carefully and respect the rules. Rare doesn't mean ours to grab.|
S~I'd like seeing something unfamiliar without making it afraid of us.|
N~A good visit should leave the Pokemon comfortable after we've gone.|
S~A sign confidently suggesting that unusual neighbors have all selected the same address.|
S~A rare concentration of rare things, apparently prepared for common visitors.|
N~We should learn the area's encounter rules before entering.|
N~A creature can be rare to us and entirely ordinary in its own home.|
N~I'd want the excitement of seeing them to leave room for respecting where they live.|
U~I'd ask a guide what visitors most often overlook while searching for the obvious rare sight.
''')
add('r123_junction', 'Route123_Text_RouteSign', 'A sign points east along Route 123 and west toward Route 118.', '''
N~Route 123 one way, 118 the other. The road has become less consecutive and more informative.|
N~The east-west distinction connects Route 123 with Route 118 rather than a named settlement.|
N~123 east, 118 west. Check the larger route before choosing.|
N~I like seeing both options at once. It makes the choice feel less like a guess.|
N~We should agree on where we're trying to end the day before following an arrow.|
N~The routes have declined numerical order in favor of the inconvenient shape of the actual land.|
S~A useful reminder that geography isn't doing arithmetic.|
N~I'd compare this junction with the next planned destination, not merely the nearest number.|
N~Two directions can both be clear while the reason for choosing remains ours.|
N~The paired layout works well. I'd keep the numbers easy to distinguish at a distance.|
N~I'd ask a traveler where the western connection leads after Route 118.
''')
add('mt_pyre_warning', 'Route123_Text_RouteSignMtPyre', 'A sign directs travelers north to Mt. Pyre with a warning to the fainthearted.', '''
N~The sign has checked our courage before bothering to check whether we brought supplies.|
N~The warning conveys an intimidating reputation, not a measured account of the route.|
N~North for Mt. Pyre. Prepare properly instead of trying to look fearless.|
N~Being nervous doesn't mean someone has no right to go there.|
N~I'd rather respect a difficult place than treat the warning as a dare.|
N~An ominous invitation relying on the reliable tendency of people to dislike being called fainthearted.|
N~A warning and a challenge sharing an inconveniently small piece of wood.|
N~We should learn the actual conditions rather than interpret the wording as a test of pride.|
N~Some thresholds deserve a quiet heart more than a loud claim of courage.|
N~I'd want people to feel allowed to turn back without believing they've failed the sign.|
N~I'd ask someone familiar with the place what a respectful visitor should know.
''')
add('berry_master_house_sign', 'Route123_Text_BerryMastersHouse', 'A sign identifies the Berry Master home.', '''
S~The Berry Master's house. An excellent address for anyone with fruit-related questions and respectful shoes.|
N~The title identifies a specialist. We should ask what guidance is available rather than assume.|
N~A home as well as a useful contact. Knock first.|
S~I wonder which Berry first made someone want to learn that much about them.|
S~I'd ask what grows well for a beginner before planning a magnificent harvest.|
S~A modest home attached to an impressively specific professional distinction.|
S~An address suggesting the fruit may be better organized than the visitors.|
N~We can begin with one practical growing question instead of requesting every answer at once.|
S~A person's patience with small growing things can become the name people know them by.|
S~The title makes me curious about the person who earned it.|
S~I'd ask which part of caring for Berries still surprises him after all this time.
''')
add('hunter_house_sign', 'Route124_Text_HuntersHouse', 'A sign marks the hunter house on Route 124.', '''
N~The hunter's house. I'd like to meet the person before deciding what the title means.|
N~The occupational name alone doesn't specify the work. We can ask inside.|
N~Found the house. Ask before treating the place as a service stop.|
N~A short title can leave a surprisingly large space for guesses.|
N~I'd start with a hello instead of arriving already certain what someone does.|
N~A remarkably brief introduction, leaving most of the actual person for the conversation.|
N~The title has arrived ahead of its explanation. A familiar arrangement.|
N~We should find out what the resident actually offers before planning around the name.|
N~A word on a doorway can be smaller than the life it points toward.|
N~I'd rather hear the resident describe the work in their own terms.|
N~I'd ask what a typical day brings back to this house.
''')
