"""Source-reviewed four-stage Berry interactions and their actual final outcomes."""
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

add('berry_empty_loamy_soil','BerryTree_Text_ItsSoftLoamySoil',
    'The plot is empty soft loamy soil.', '''
S~A little patch of potential. I am trying not to take the dirt personally.|
N~Loose soil like this gives roots space. Something could grow well here.|
N~A good spot to plant when we have something to spare.|
S~I like a place that is waiting without looking abandoned.|
N~We can remember the spot for a berry we would like more of.|
S~A very small stage, currently awaiting its first ambitious seed.|
S~The earth is having a quiet day. I respect that.|
N~A prepared site is useful. The next step still needs the right material.|
S~An empty place can be ready rather than lonely.|
N~We should leave it tidy for whoever plants here next.|
S~I wonder how different this patch will look when we pass again.
''')
add('berry_successfully_planted','BerryTree_Text_PlantedOneBerry',
    'The player successfully planted a Berry in the plot.', '''
S~We have buried a snack with long-term ambitions.|
N~A small investment in a future harvest. We should remember where we planted it.|
N~Good. Come back and care for it rather than just hoping.|
S~I like leaving something that might be growing when we return.|
S~One berry now, with the chance to share more later.|
S~Our newest subplot has been given a quiet opening underground.|
S~A commitment small enough to hold in a hand, then larger than it looks.|
N~Site occupied, planting complete. Now the timetable belongs partly to the plant.|
S~A little life has been trusted to the dark.|
S~I want to remember the place before it becomes easy to overlook.|
S~The return visit will have a little more meaning now.
''')
add('berry_planted_stage','BerryTree_Text_BerryGrowthStage1',
    'A planted Berry is still below the soil, before sprouting.', '''
N~Nothing visible yet. The snack is conducting important underground business.|
N~Early growth is not always visible above the surface. We should allow it time.|
N~It is planted. Leave it room to begin.|
S~I like knowing something can be happening quietly where we cannot see.|
N~We can care for it without digging it up to check.|
N~The opening scene is happening beneath the stage. Patience from the audience, please.|
S~An excellent phase for a plant that prefers not to be perceived.|
N~Do not disturb the process just because there is no visible result yet.|
S~The dark is doing some of the growing.|
N~Not everything needs to look impressive immediately.|
N~I will remember where we looked today, so we notice what changes.
''')
add('berry_sprouted_stage','BerryTree_Text_BerryGrowthStage2',
    'The Berry has sprouted.', '''
S~It has arrived! Very small, very green, and already better at standing in soil than I am.|
S~The first visible growth. A useful sign that the plant has begun establishing itself.|
N~A good start. Small things still need looking after.|
S~That little bit of green makes the whole patch feel different.|
S~I am glad we came back in time to notice the beginning.|
S~The newest member of the garden has finally made its entrance.|
S~A modest arrival. No speech required. I like its style.|
N~Visible progress. We can observe without handling the delicate part.|
S~The earth has offered a small green answer.|
S~A tiny change with a completely different silhouette.|
S~I would like to remember how small it was before the leaves fill this space.
''')
add('berry_taller_stage','BerryTree_Text_BerryGrowthStage3',
    'The Berry plant is growing taller.', '''
S~It is taller! I am being overtaken in the field of standing around productively.|
N~More visible structure now. Steady growth is worth observing, not rushing.|
N~It is coming along. Give it space and keep up the care.|
S~I would not have noticed every little change if we had stayed beside it.|
S~The ordinary visits are starting to add up to something.|
S~The quiet opening has acquired height, leaves, and a clearer sense of purpose.|
S~I admire progress that does not require announcing its goals to passersby.|
N~Its structure is developing. The result takes more than simply planting and leaving.|
S~Small days have been gathering into a larger shape.|
S~It is finding its own shape instead of staying the little sprout we first met.|
S~We should look from the same spot as last time. The difference will be easier to see.
''')
add('berry_blooming_stage','BerryTree_Text_BerryGrowthStage4',
    'The Berry plant is flowering; the displayed care adverb can vary.', '''
S~Flowers! The snack project has briefly become a decoration project.|
S~Flowering is a distinct stage. We should enjoy it without assuming the harvest is ready.|
S~Looking good. It still needs time before picking.|
S~I am glad we did not only come back for what we could take.|
S~A future ingredient has a lovely life before reaching anyone's plate.|
S~The garden has added a brief, generous scene between growth and fruit.|
S~A quiet celebration. Nobody even asked it to smile.|
N~The plant has reached its flowering phase. Another useful observation for the return visit.|
S~The promise has opened into color for a little while.|
S~I like that it gets to be beautiful without the moment needing to last forever.|
S~I would want to remember the flowers, too, not only the full branches later.
''')
add('berry_watered_delighted','BerryTree_Text_PlantIsDelighted',
    'The player watered the plant, which seems delighted.', '''
S~A delighted plant. Finally, an audience that appreciates my very basic pouring skills.|
S~We supplied what it needed. I would be cautious about interpreting the precise emotion.|
S~Small bit of care, properly done. We can move on.|
S~It is nice when helping can be something simple and quiet.|
S~A drink and a little attention. Sometimes that is enough for the moment.|
S~Our modest watering performance has received an excellent review from the foliage.|
S~I believe the plant and I agree about appreciating a low-pressure interaction.|
N~Water delivered. No need to keep adding more just to feel more helpful.|
S~A small kindness found a place to settle.|
S~It seems happier. I will accept a little uncomplicated good news.|
S~I like remembering the care that happened between the more visible changes.
''')
add('berry_harvest_put_away','BerryTree_Text_PutAwayBerry',
    'The harvest was successfully stored and the soil is empty again.', '''
S~Harvest secured. The dirt has returned to waiting for our next snack-related investment.|
N~The berries are stored, and the plot is available again. A complete cycle.|
N~Good haul. Leave the spot ready for another planting.|
S~It feels nice to carry something from a place we watched change.|
S~We can use some and keep some for planting. No need to decide everything now.|
S~The growing chapter has ended with something real in the bag and space for another.|
S~An ending that leaves a little room instead of closing the whole book.|
N~Output collected, site reset. Remember the care that made the process work.|
S~The branches have given, and the soil is waiting again.|
S~A useful harvest, and a tidy place left behind. Good result.|
S~I want to remember the patch as well as what we took from it.
''')
add('berry_full_pocket_failure','BerryTree_Text_BerryPocketFull',
    'The berries cannot be picked because the Berry pocket is full.', '''
F~Our portable fruit collection has defeated the acquisition of more fruit.|
N~The harvest has not entered the bag. We need capacity before trying again.|
N~Sort the Berry pocket first. Leave the plant alone while we do.|
N~At least the berries can stay where they are instead of being dropped.|
N~Let us plan what we can use or store rather than waste something to hurry.|
M~The harvest finale has encountered a rather overcommitted prop cupboard.|
M~We prepared for every possible fruit emergency except this one.|
N~A storage bottleneck. More picking will not fix it.|
N~A branch can wait while we make room for its gift.|
N~We can reorganize without treating the berries we already have as rubbish.|
N~We should remember this spot if we intend to return with space.
''')
add('berry_left_unpicked','BerryTree_Text_BerryLeftUnpicked',
    'The player deliberately leaves the ripe berries on the plant.', '''
S~The berries remain employed as berries. A peaceful outcome.|
N~There is no need to collect a resource simply because it is available.|
N~We can leave them. Not everything needs to fit in our bag.|
S~I like getting to look without needing to take anything.|
S~Somebody else may be glad to find them later.|
S~The fruit has been excused from our inventory and retained its original setting.|
S~A small successful act of leaving something alone.|
N~An available option does not have to become an immediate task.|
S~The branch keeps its color a little longer.|
S~Enough is a perfectly respectable amount to carry.|
S~I would rather remember the full plant than gather more than we need.
''')
add('berry_planting_declined','BerryTree_Text_WantToPlant',
    'The planting prompt was left without a successful planting outcome.', '''
N~We can leave the empty patch for now. The dirt has not demanded a deadline.|
N~We have not planted anything. A decision can wait until we know what we want to grow.|
N~No need to plant just because the option is there.|
N~I would rather choose a little plan we want to return to.|
N~We can keep a berry for the team today and think about planting later.|
N~The possible garden remains a proposal rather than a compulsory new subplot.|
M~An empty patch has made a suggestion. We are allowed to decline gardening homework.|
N~No planting result to record. The site remains available.|
N~An untouched place can still hold a possibility.|
N~We can leave it ready for somebody with a clearer idea.|
N~I would like to remember it if we later find something we really want to grow.
''')
add('berry_watering_declined','BerryTree_Text_WantToWater',
    'The watering choice ended without the successful watered/delighted messages.', '''
N~No watering this time. I will not pretend I saw a tiny grateful leaf wave.|
N~We have not watered it in this interaction. The actual result matters.|
N~We can leave for now. No need to invent a completed chore.|
N~I like being able to pause without making a big explanation.|
N~If we want to tend it later, we should remember where it is.|
N~The watering scene has remained an optional revision.|
M~I was ready to applaud some pouring. I can save the applause.|
N~The proposed action was not completed. Keep that separate from the plant's earlier growth.|
N~The small green life remains here while we choose our next step.|
N~A quiet choice can simply stay a choice.|
N~I would notice what the plant looks like when we return, rather than assume it stayed the same.
''')

