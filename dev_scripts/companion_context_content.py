"""Authored replies in Pip/Silas/Kade/Ashe/Nico/Riven/Emi/Vera/Lume/Mochi/Zuri order.

Bindings are exact text labels, never runtime keywords or NPC graphics. Aliases
may share a context only when the same response is true for every alias.
"""
ROWS = []
def add(key, labels, subject, lines):
    replies = [s.strip() for s in lines.strip().split('|')]
    assert len(replies) == 11, (key, len(replies))
    ROWS.append(dict(key=key, labels=labels.split(), subject=subject, replies=replies))

add('oldale_save', 'OldaleTown_Text_SavingMyProgress', 'She is saving before taking a rest.', '''
She is saving before her rest. I usually just trust the pillow.|
soft_smile~Recording progress before resting. Sensible fieldwork; excellent pillow management.|
Rest first, mistakes later. Saving gives the mistakes less authority.|
She saved before resting. I should write down tunes before naps eat them.|
Save, then rest. Like covering dough before leaving it alone. Less chance of disaster.|
A pause with a carefully prepared return. Even an intermission needs planning.|
She is saving her progress. I save my poems. Unfortunately, all the drafts too.|
Save before shutting down. My workshop could learn from her.|
A rest with a way back to where she stopped. A kind little ritual.|
Saving before a rest. A sensible fastening on the end of the day.|
She is keeping her progress safe. I photograph a wall before the weather gets ambitious.
''')
add('oldale_footprints_search', 'OldaleTown_Text_DiscoveredFootprints OldaleTown_Text_WaitDontComeInHere', 'He asks for space to sketch supposedly rare footprints.', '''
He needs room to sketch those footprints. I shall contribute by keeping my feet out of the evidence.|
Sketch first, identify later. Let us avoid adding eleven new theories with our shoes.|
Give him space. Nobody solves a mystery while we are standing on it.|
Those prints have an audience now. Let us not turn the sketch into crowd noise.|
I can wait. Stepping on the tracks would be a very poor contribution to science.|
The footprints are having their portrait done. We must respect the sitting.|
Rare footprints. At last, a celebrity who cannot ask me what my poem means.|
He is documenting the tracks. Good. Measurements before dramatic conclusions, preferably.|
Someone passed here. For now, that is the part of the story we actually know.|
Let him finish the sketch. Even an excellent shoe can trample evidence.|
He is drawing the prints before they fade. I understand the hurry. We can go around.
''')
add('oldale_footprints_reveal', 'OldaleTown_Text_FinishedSketchingFootprints', 'The supposedly rare footprints were his own.', '''
laughing~They were his own footprints. At least the rare creature has agreed to an interview.|
laughing~His own tracks. A useful correction, and an unusually convenient research subject.|
laughing~Tracked himself down. Tough suspect. Knew every move he was going to make.|
laughing~His own footprints. A solo performance with a very surprising encore.|
laughing~He found himself. Usually I need breakfast before managing that.|
smug~The investigator was the mysterious creature. A twist with remarkably little travel expense.|
laughing~His own footprints. A moving portrait of a man going absolutely nowhere.|
laughing~His own tracks! Excellent reason to check the measuring equipment attached to your ankles.|
soft_smile~He corrected the story when the evidence changed. That is worth keeping, too.|
laughing~His own footprints. His shoes have finally received professional recognition.|
laughing~A self-portrait in mud. Unexpected medium. Very committed artist.
''')
add('potion_use', 'OldaleTown_Text_PotionExplanation', 'Potions can heal away from a Center.', '''
A POTION means we can help before reaching a CENTER. I prefer emergencies with fewer walking directions.|
A portable treatment. Useful, though it does not make pushing a tired team sensible.|
Keep a POTION handy. Being tough is no reason to limp to town.|
A little healing on the road. Much better than telling a tired friend to keep the tempo.|
POTIONS for the team, lunch for us. Travelling goes better when care is already packed.|
A POTION can help out here. We need not turn every injury into an endurance performance.|
A POTION works on the road. Finally, a bottle that makes a problem smaller.|
Field repairs for Pokemon. Unlike my tools, the POTION comes with useful instructions.|
Care we can carry. A small bottle is allowed to matter.|
A POTION belongs somewhere reachable. A pocket is only useful if you can find its contents.|
Healing before the next town. Good supplies make room for a better journey.
''')
add('party_order', 'OldaleTown_House1_Text_LeftPokemonGoesOutFirst', 'The first party member enters battle first.', '''
First in the party, first into battle. I shall stop calling it the snack queue.|
The first slot determines the opening. We can change the order before choosing a strategy.|
Pick the lead on purpose. Whoever is first gets the first problem.|
The first Pokemon sets the opening note. Best choose one ready to play it.|
First in line gets the battle, not the bread. Important distinction.|
Choose your opening performer carefully. The rest of the cast still matters.|
First in the party means first into battle. An extremely literal opening line.|
Reorder the team for the job. Tools work better when the right one is within reach.|
The first companion steps forward first. We can make that a choice rather than an accident.|
Put the right Pokemon first. Arrangement should serve the wearer. Or the battler, here.|
The first slot sets the opening shape. We can rearrange without leaving anyone out.
''')
add('battle_growth', 'OldaleTown_House2_Text_PokemonLevelUp', 'Battles help Pokemon gain levels.', '''
Battles help Pokemon grow. My experience mostly teaches me where the benches are.|
Experience builds strength. Rest is still part of the work, even if it earns no level announcement.|
Practice makes them stronger. Pick battles they can learn from.|
Battles are practice, then. With more dramatic feedback than scales.|
They grow through experience. I grow through trying a recipe again after a very flat loaf.|
Rehearsal with consequences. Let us make sure our team gets recovery time between performances.|
They gain levels by battling. I gain revisions by reading my work aloud. Less cheering.|
Repeated practice improves performance. Preferably without setting the practice equipment on fire.|
Growing stronger takes experience. No need to pretend the beginning was embarrassing.|
Practice gives strength a better fit. Everyone starts with some awkward seams.|
Battles leave lessons. We should notice the Pokemon doing the learning, too.
''')
add('strength_travel', 'OldaleTown_House2_Text_YoullGoFurtherWithStrongPokemon', 'A stronger team can travel farther.', '''
A stronger team can go farther. I hope farther also has lunch.|
More capable partners open safer routes. Distance is not the only measure of progress.|
Get stronger, go farther. Come back for a rest before farther becomes a problem.|
A stronger team means a longer road. Plenty of time to finish that travelling tune.|
Farther away means more provisions. That is not fear. That is sandwiches.|
Strength opens the next act. We still choose the pace of the performance.|
Grow stronger, travel farther. My legs would like to submit a footnote.|
Capability changes the route. We should improve supplies along with the team.|
The road gets longer as we grow. Coming home remains a perfectly good ending to a day.|
Stronger partners, farther journeys. I am adding reinforced soles to that plan.|
A stronger team opens more places. I wonder what colours we have not seen yet.
''')
add('center_oldale', 'Route101_Text_TakeTiredPokemonToPokeCenter', 'Tired Pokemon can recover at the nearby Oldale Center.', '''
OLDALE has a CENTER nearby. Excellent. A helpful direction that ends in sitting down.|
The nearby CENTER is our recovery point. Let us use it before tired becomes hurt.|
OLDALE is close. Take the team in if they need it; the road can wait.|
The CENTER is just ahead. Even a good travelling song needs a rest.|
Healing in OLDALE, then. I can plan lunch while the team gets proper care.|
A nearby place to recover. We need not make a dramatic collapse our next entrance.|
A CENTER close by. Hope has a roof and very practical opening hours.|
OLDALE has recovery facilities. Better than testing how far a tired team can hobble.|
There is somewhere nearby to rest them. That is good news worth saying plainly.|
Let us take the team to OLDALE if they are tired. Comfort should not be postponed for appearances.|
OLDALE's CENTER is close. A good route includes somewhere to recover.
''')
add('wild_grass', 'Route101_Text_WildPokemonInTallGrass', 'Searching tall grass leads to wild Pokemon encounters.', '''
Tall grass is where we meet wild Pokemon. My shoes were hoping for a quieter introduction.|
The grass is habitat, not an empty shortcut. We should enter prepared to meet its residents.|
Want to meet wild Pokemon? Into the grass. Keep the team ready.|
The grass has surprise performers. None appear to need an announcement.|
Wild Pokemon in the grass. Let us secure the food before making introductions.|
The grass conceals the next entrance. Good staging. Unreliable ticketing.|
Tall grass: where a peaceful walk develops a supporting cast.|
Searching the grass brings encounters. Supplies first; improvisation second.|
The grass has residents. A path through somebody's home deserves some attention.|
Tall grass means Pokemon, and possibly seeds in every hem. Both require preparation.|
We step into the grass and the scene changes. There are lives here we have not met.
''')
add('grass_sneeze', 'Route102_Text_ImNotVeryTall', 'The grass reaches his nose and makes him sneeze.', '''
The grass reaches his nose. I support his campaign for a shorter lawn.|
At his height, that grass is a very different environment. A tissue seems more useful than advice.|
Give him a bit of room. Sneezing in tall grass sounds miserable.|
The grass is playing his nose like an instrument. Not one I would put in the band.|
Grass up the nose. I have flour days like that. A clean handkerchief helps more than laughing.|
A sneeze with excellent projection. An unfortunate venue for the performance.|
The grass goes up his nose. Nature has become an intrusive editor.|
That path is poorly suited to his height. A shorter route would beat a lecture about endurance.|
The same grass is a meadow to us and a thicket to him. Perspective is quite physical.|
Grass at face height. This is why comfort cannot be designed for one body.|
He is walking through what looks like a wall from down there. We can give him space.
''')
add('catch_many', 'Route102_Text_CatchWholeBunchOfPokemon', 'He wants to catch many Pokemon.', '''
A whole bunch of Pokemon. I hope he has also planned a whole bunch of meals.|
An ambitious collection. Each new partner still needs individual care.|
Catch plenty if you can care for them. A team is more than a number.|
A whole bunch. That is less a solo act and more an orchestra with teeth.|
Many Pokemon means many appetites. I respect the ambition and fear the shopping list.|
A large cast. Someone will need to learn every name, not just count the entrances.|
A whole bunch of Pokemon. The phrase has concealed an enormous amount of responsibility.|
He has a target count. I would also like to see the care plan.|
I hope each one becomes a someone to him, rather than another mark on a list.|
Quite a collection planned. No matching outfit can substitute for knowing each partner.|
A whole bunch of new lives in one plan. I hope he leaves room to know them.
''')
add('reflection', 'PetalburgCity_Text_WaterReflection', 'He wonders whether his reflected face shows hope or fear.', '''
He sees hope or fear in the water. I see somebody asking a rather brave question.|
A reflection gives little evidence of what someone feels. Asking is better than guessing.|
Hope and fear can share a face. You do not have to choose just one.|
You can be hopeful and frightened. I have performed several entire songs in that arrangement.|
Both can be true. A warm meal does not fix everything, but it helps me talk about it.|
A face can carry more than one feeling. That is not a failed performance.|
Hope and fear in the same reflection. The water is a better poet than I expected.|
Same face, different feelings. We should not mistake the surface for a complete reading.|
Water shows a face. The person gets to tell us what is behind it.|
Hope does not need a particular face. Neither does fear. We should leave him room for both.|
The light can show his outline. It cannot choose his meaning for him.
''')
add('storage_seventh', 'PetalburgCity_Text_FullPartyExplanation', 'A seventh caught Pokemon is sent to a PC box.', '''
The seventh Pokemon goes to a BOX. Sensible. My proposed second backpack had several design flaws.|
A full party sends the next catch to storage. We should check on our boxed partners, too.|
Six travelling, the next one in a BOX. Remember where everyone went.|
Six on the road, the seventh waiting in a BOX. We should make time for the whole ensemble.|
The BOX handles the seventh catch. It does not handle remembering everybody's favourite food. I can help.|
The travelling cast has six places. A partner waiting backstage still belongs to the company.|
The seventh goes to a BOX. A surprisingly orderly ending to a wild encounter.|
Automatic storage prevents an overcrowded party. We should still check the destination ourselves.|
A BOX is a place to wait, not a reason to forget somebody.|
The seventh goes to storage. Extra pockets are useful, but this is beyond my tailoring.|
Only six travel at once. That need not make the others background characters.
''')
add('gym_first', 'PetalburgCity_Text_AreYouRookieTrainer', 'He recommends checking a new town gym.', '''
Check the GYM first? I had the bakery pencilled in. We can negotiate.|
Checking the local GYM tells us what training lies ahead. A sensible first survey.|
Check the GYM, learn what we are facing. Nobody said we have to fight immediately.|
He checks the GYM first. I usually listen for somebody practising with a window open.|
GYM first, supplies close behind. Hungry strategy is rarely my best strategy.|
Look at the venue before taking the stage. At last, a trainer tip I can wholeheartedly endorse.|
The GYM is the first stop. My shoes were hoping towns had introductions before examinations.|
Reconnaissance before a challenge. I approve of a plan containing an actual inspection.|
Learning what a place asks of us is useful. So is meeting the people outside its GYM.|
Checking the GYM is sensible. We can prepare without pretending we are ready for everything.|
The GYM tells one part of a town's story. I want to see what surrounds it, too.
''')
add('kanto_coffee', 'ViridianCity_Text_GrandpaHasntHadCoffeeYet', 'His granddaughter explains his rudeness as lack of coffee.', '''
He has not had coffee. I understand the tiredness. The road still belongs to other people.|
The missing coffee explains his mood. It does not make his granddaughter responsible for it.|
No coffee is rough. Making it everyone else's problem is optional.|
I get quiet before breakfast. He has chosen a much louder arrangement.|
I sympathise with an empty cup. Less with making somebody else apologise for it.|
A caffeine shortage has become public theatre. His granddaughter deserves a quieter morning.|
No coffee, therefore no road. A startling contribution to municipal planning.|
Coffee is fuel, not a permit to block the route. Very important distinction.|
She is trying to smooth things over. I hope someone asks how her morning is going.|
Being uncomfortable is real. Making everyone accommodate rudeness is a separate choice.|
One empty cup, an entire blocked street. The proportions need work.
''')
add('kanto_gym_closed', 'ViridianCity_Text_GymClosedWonderWhoLeaderIs', 'Viridian gym is closed and its leader is unknown.', '''
Closed GYM, mysterious LEADER. I hope this is a schedule problem rather than a secret basement problem.|
No LEADER identified and no access. We need more information, not a theory presented as fact.|
Closed for now. We can come back when somebody is actually running the place.|
A GYM with no announced LEADER. That is an unusually long silent introduction.|
If the GYM stays closed, we can use the time to restock. Waiting is easier with provisions.|
An absent lead and a locked venue. Even my rehearsals have clearer notices.|
The LEADER is a mystery. The door has made its position extremely clear.|
No opening notice? A small sign would solve several people's afternoon.|
An unanswered question is allowed to remain one until we learn more. The lock is not evidence of a ghost.|
A closed door and no explanation. Information should not be an exclusive accessory.|
The building is there; the person is missing from the picture. We can look elsewhere for now.
''')
add('kanto_gym_returned', 'ViridianCity_Text_ViridiansGymLeaderReturned', 'Viridian leader has returned.', '''
The LEADER is back. The door can retire from being the strongest opponent here.|
The situation has changed: the LEADER returned. We can reassess our plans.|
LEADER is back. Now we can prepare for a real challenge.|
The LEADER has returned. Long introduction. Let us see how the actual performance goes.|
The GYM has its LEADER again. We should make sure our team is ready before heading in.|
The missing lead has arrived. I trust the entrance was worth the wait.|
The LEADER returned. At last, the mystery has developed opening hours.|
Someone is running the GYM again. Good time to check our team rather than the lock.|
A return changes the story. Let us pay attention to what happens next.|
The LEADER is back. We can prepare properly instead of dressing for a locked door.|
The empty place has a person in it again. That changes what we can do here.
''')
add('caterpie_weedle', 'ViridianCity_Text_ExplainCaterpieWeedle', 'Caterpie is not poisonous; Weedle has Poison Sting.', '''
CATERPIE and WEEDLE: similar shapes, very different reasons not to grab the pointy end.|
Useful distinction: WEEDLE has POISON STING. Resemblance is not a safe identification method.|
Watch for WEEDLE's sting. Looking a bit like CATERPIE does not make it harmless.|
WEEDLE brings POISON STING. I will admire the caterpillars without requesting a demonstration.|
CATERPIE and WEEDLE need different caution. Let us check antidotes before the forest.|
Two similar silhouettes, one poisonous entrance. Casting by appearance has consequences.|
CATERPIE does not have the poison. WEEDLE supplies the sharp critique.|
Identify first, touch never without cause. WEEDLE is an excellent safety instructor at a terrible hourly rate.|
Two small creatures, different defences. Their stories deserve more care than a shared outline.|
A similar shape does not mean the same needs. WEEDLE's sting makes that point emphatically.|
Look closely: the differences matter. That sting is more than a detail in the sketch.
''')
add('forest_shopping', 'ViridianCity_Text_GoShoppingInPewterOccasionally', 'Her shopping trip to Pewter takes the winding forest trail.', '''
Her shopping trip goes through the forest. I hope she buys everything on the first visit.|
The winding forest path is part of her routine. A useful reminder that our adventure is somebody's errand.|
Through the forest for shopping. I would check the list twice before leaving.|
A forest walk just to shop. I hope the route has a good rhythm once you know it.|
That is a long trip for a forgotten ingredient. I would make a very careful list.|
Through the forest for groceries. A surprisingly elaborate set change for an ordinary day.|
A winding forest between her and the shops. My shopping list has become a survival document.|
An everyday route with several bends and wild Pokemon. Good argument for durable carrying straps.|
To us, a forest adventure. To her, the way to the shops. Places hold more than one kind of story.|
That shopping route needs shoes made for walking, and a bag made to carry the whole list.|
The forest is part of her daily map. I wonder which turns she has stopped noticing.
''')
add('catch_weaken', 'ViridianCity_Text_WeakenMonsFirstToCatch', 'He advises weakening Pokemon before catching them and mentions strong coffee.', '''
Weaken the Pokemon first. And apparently weaken the coffee too, judging by his headache.|
Lowering a wild Pokemon's HP helps capture. His coffee has independently demonstrated the risks of overdoing things.|
Weaken it without knocking it out. Coffee strength appears to need a similar adjustment.|
Gentler battle, gentler coffee. He has given us two lessons for the price of a headache.|
Weaken the Pokemon before a catch. Dilute the coffee before the next lecture. Different recipes, same restraint.|
He recommends restraint in catching. His coffee has filed a dissenting review.|
Weaken the Pokemon first. The coffee has already defeated its trainer.|
Controlled force improves capture. Controlled brewing might improve his morning.|
He can offer useful advice and still be having a difficult morning. Both parts are visible here.|
Enough damage to help a catch, not enough to knock it out. Proportion matters. Especially in that coffee.|
A little restraint helps the capture. The headache is a rather vivid footnote.
''')
add('ledge_jump', 'Route1_Text_CanJumpFromLedges', 'Ledges allow a one-way shortcut back toward Pallet.', '''
Jump down the ledges to get back faster. The climb back up remains rudely unavailable.|
One-way shortcuts change a return route. Let us check where we land before choosing one.|
Down is the shortcut. Up is the long way. Worth remembering before jumping.|
A quicker way back. My knees would like a moment to review the arrangement.|
Jumping down saves time on the return. Secure the bread before testing it.|
A quick exit with no matching entrance. Useful staging, provided we know the landing.|
The ledge is a shortcut in one direction. A path with a very firm opinion.|
Gravity-powered transport. Efficient, with a disappointingly limited reverse gear.|
A shorter return, not a shorter journey both ways. The ground keeps its own rules.|
One-way shortcut. I am checking the bag closures before we turn walking into a landing.|
The way home can follow a different line. Let us see where this one comes down.
''')
add('pallet_sign_copy', 'PalletTown_Text_PressStartToOpenMenuCopy', 'She repeats the Trainer Tips sign about the Start menu.', '''
She copied the sign into conversation. The sign has found a publicist.|
The same instructions, delivered personally. Repetition can be useful when somebody actually needs it.|
Same tip as the sign. She is making sure nobody misses it.|
The sign has a vocalist now. Quite committed to the original lyrics.|
She copied the tip exactly. I appreciate someone who labels the recipe instead of improvising instructions.|
A faithful adaptation of a sign. Minimal scenery. Excellent availability.|
She has performed a reading of a menu instruction. I am suddenly less nervous about my poems.|
Exact reproduction of the operating instructions. I wish every borrowed tool came back with that.|
A written tip becomes something she can share. That is how small bits of knowledge travel.|
She kept the useful part of the sign intact. A practical adaptation, if a very enthusiastic one.|
She brought the words off the board. Now they have a person attached to them.
''')
add('pallet_sign_read', 'PalletTown_Text_PressStartToOpenMenu', 'A sign explains how to open the Start menu.', '''
START opens the MENU. A useful sign; I had been trying a meaningful glance.|
A clear instruction for the MENU. Short enough to consult without losing the rest of the afternoon.|
START, then MENU. Straightforward. I appreciate that.|
The MENU has an opening cue. That makes two of us.|
START opens the MENU. Let us check our supplies while it is open.|
A single button for the opening. I have overcomplicated several entrances.|
START opens the MENU. Concise prose. Disturbingly employable.|
One clear instruction. Excellent labelling; no ominous diagram required.|
A small sign that helps someone find their way through the controls. Useful things need not be grand.|
A MENU instruction where people can find it. Function has been allowed to lead the design.|
Simple lettering, useful message. Not every sign needs a dramatic flourish.
''')
add('pokemon_portable', 'ViridianCity_Text_CanCarryMonsAnywhere', 'Poke Balls let people carry their Pokemon with them.', '''
Pokemon can come with us in POKE BALLS. My bag still somehow loses a single pencil.|
A compact way to travel together. Convenient equipment does not replace looking after the occupants.|
They travel with us. Let us give them reasons to enjoy the trip.|
A whole team, ready to travel. I cannot fit my instrument case that neatly.|
Partners travel in POKE BALLS. Their lunch, regrettably, remains full size.|
Such compact travelling arrangements. My costume trunk has refused all similar negotiations.|
A POKE BALL carries a Pokemon. My pocket cannot reliably carry a folded receipt.|
A remarkable piece of portable technology. I am resisting the urge to suggest extra compartments.|
We can take them with us. I like the together part more than the anywhere part.|
POKE BALLS make room for partners. My designs mostly make room for keys. I respect the scale.|
They come with us wherever we go. I hope we notice what they make of the scenery.
''')
add('hidden_items', 'PetalburgWoods_Text_HiddenItemsExplanation', 'Some items on the ground are invisible and must be searched for.', '''
Some items are hidden from view. At last, an explanation for every pencil I have owned.|
We may need to examine a place rather than just look at it. Evidence can be easy to miss.|
Hidden items. Check carefully; do not tear the whole forest apart over a suspicion.|
Not everything useful announces itself. Quiet instruments have taught me that.|
Invisible items on the ground. I am still keeping food off it.|
The prop is there even when the audience cannot see it. Search carefully, not theatrically.|
Some useful things are invisible. Like my confidence, but with a better chance of being found.|
A closer inspection can find what a quick look misses. No shovel required for every question.|
Look again without assuming the first glance told the whole story. That is useful beyond finding items.|
Something can be there without catching the eye. Decorative sparkle is a poor inventory system.|
The scene has details we missed. Worth looking closely before deciding it is empty.
''')
add('miracle_seed', 'PetalburgWoods_Text_MiracleSeedExplanation', 'Miracle Seed strengthens Grass-type moves when held.', '''
A held MIRACLE SEED helps GRASS moves. I shall not test whether it improves a salad.|
Give the MIRACLE SEED to a partner using GRASS moves. The benefit depends on the match.|
Good held item for GRASS attacks. Put it with someone who can use it.|
A small seed backing up GRASS moves. A very quiet supporting musician.|
This seed is for holding, not baking. I appreciate the clarification before the experiment.|
A small prop with a specific purpose. Give it to the right performer.|
A MIRACLE SEED improves GRASS moves. My garden seeds mostly improve the pigeons' afternoon.|
Match the held item to the moves. An upgrade is only useful when it fits the job.|
A seed carried for strength. Useful and symbolic; it is allowed to be both.|
A useful accessory for a GRASS attacker. The wearer determines whether the design works.|
Something this small can change a battle. Details matter when they belong in the right place.
''')
add('bug_out_of_balls', 'PetalburgWoods_Text_ImOutOfPokeBalls', 'The bug catcher has run out of Poke Balls.', '''
Out of POKE BALLS. An ambitious catching plan has met a very round supply problem.|
An empty supply of POKE BALLS limits the survey. Worth checking before the next expedition.|
Out of POKE BALLS. Time to restock, not blame the bugs.|
He has found the end of his supplies before the end of his enthusiasm. Familiar rehearsal problem.|
No POKE BALLS left. A list before leaving town could save another long walk.|
Plenty of ambition, no equipment. The production has encountered its budget.|
Out of POKE BALLS. The forest has won on a technicality.|
Inventory failure. A wonderfully unglamorous reason to check the bag before an expedition.|
The desire to catch more has outlasted the supplies. A pause is sensible here.|
No POKE BALLS left. Even the best bag needs someone to check what is inside.|
He still sees possibilities everywhere. The empty bag has a more limited interpretation.
''')
add('picture_books', 'Text_PictureBookShelf', 'The shelf contains Pokemon picture books.', '''
Pokemon picture books. I can finally research without losing my place in the long words.|
Illustrations make species easier to recognise. I should compare the drawings with what we actually meet.|
Picture books. Good way to learn what to look for before heading out.|
I like the illustrated ones. There is room to linger without racing the next sentence.|
Picture books about Pokemon. I wonder whether the berry illustrations are accurate. Purely practical interest.|
A whole shelf of illustrated creatures. Someone has already done the costume research.|
Picture books. A story that trusts the drawing to do some of the work. I should try that.|
Pictures and labels together. More useful than a diagram labelled with another mysterious diagram.|
Someone can meet a Pokemon here before seeing one outside. A gentle first introduction.|
The pictures help you notice differences. Good design makes looking easier.|
Someone chose how each Pokemon would be seen. I like checking what the artist noticed first.
''')
add('pokemon_magazines', 'Text_PokemonCenterBookShelf', 'The Center has Pokemon Pal, Pokemon Handbook and Adorable Pokemon magazines.', '''
ADORABLE POKEMON. Finally, a publication brave enough to state its position.|
A HANDBOOK beside ADORABLE POKEMON. Research and enthusiasm appear to share a shelf.|
Pokemon care and cute pictures. Could do worse while waiting for the team.|
Pokemon magazines for the waiting room. Better background company than worrying in perfect silence.|
ADORABLE POKEMON beside the HANDBOOK. I hope one has a feeding guide. Ideally both.|
Several magazines, three very clear editorial directions. I admire a publication that knows its audience.|
ADORABLE POKEMON. A title that has already delivered its entire argument.|
The HANDBOOK might be useful while we wait. I shall resist annotating somebody else's magazine.|
A waiting room leaves people with questions. It is kind to leave something helpful to read.|
Care guides and affectionate pictures. Both have a place; neither substitutes for the other.|
A shelf for learning, and a shelf for loving the pictures. Fortunately, the same shelf can do both.
''')
add('empty_vase', 'Text_Vase', 'An expensive-looking vase is empty.', '''
Expensive vase. Empty inside. I will demonstrate wisdom by moving my elbows away.|
An empty vase tells us very little about its price. We can inspect it without testing its durability.|
Looks expensive. Leave it where it is; our luck does not need exercise.|
An expensive vase with nothing in it. I shall not fill the silence by dropping it.|
Empty vase. Still not a bread basket. I am behaving impeccably.|
An empty vase demanding this much presence. A performer could learn from it.|
Expensive and empty. I have attended readings with a similar atmosphere.|
Empty, expensive, breakable. Three strong arguments against a hands-on demonstration.|
Nothing inside. That need not be a mystery; sometimes a vase is waiting for flowers.|
The empty space is part of the design. My elbows will respect the designer's intentions.|
The shape holds the light even without flowers. We can admire it without picking it up.
''')
add('empty_bin', 'Text_EmptyTrashCan Text_TrashBin', 'The examined trash can has nothing in it.', '''
Empty. Excellent news for the cleaner, less exciting news for our investigation.|
Nothing in the bin. A negative result is still a result. We can stop looking now.|
Empty. Mystery solved. Hands washed next.|
An empty bin. I am choosing to hear that as a very short rest.|
Nothing there. Good. Food scraps belong in a proper disposal plan, not a pocket.|
An empty bin. An admirably restrained set.|
Empty. Even the rubbish has found somewhere else to be.|
No contents, no repair required. I rarely receive such a concise maintenance report.|
It is empty. We do not have to give it a hidden meaning.|
Nothing in it. Let us avoid making a new mess to justify the inspection.|
Empty space can be useful. Particularly when it means someone already cleaned up.
''')
add('town_map', 'Text_ATownMap', 'The object is a town map.', '''
A TOWN MAP. A second opinion on where I was confidently heading.|
A map lets us compare the route before walking it. I approve of research with landmarks.|
Check the route now. Cheaper than discovering the wrong turn with our feet.|
A map of the town. Useful when every unfamiliar street starts looking like a chorus repeat.|
A TOWN MAP. We can plan supplies around the distance instead of optimistic hunger.|
A map. The stage plan for an entrance that actually reaches the right building.|
A map. My preferred genre of writing when we are lost.|
A useful overview. Let us identify the destination before redesigning the journey.|
A map holds one version of a place. The streets will have the rest of the details.|
Routes, buildings, useful distances. Good layout is a form of kindness.|
Someone made this place legible. I like seeing which landmarks they chose.
''')
add('polished_window', 'Text_PolishedWindow', 'The window has been carefully polished.', '''
A very clean window. I shall keep my investigative fingerprints to myself.|
A clear window is somebody's work. We can appreciate it without adding a handprint.|
Someone cleaned that properly. Let us not immediately undo it.|
A window clear enough to forget it is there. I have walked into that particular criticism.|
Polished glass. My flour-covered hands are remaining firmly over here.|
Immaculate glass. A fine invisible member of the scenery.|
A polished window. At last, a transparent conversation.|
Clean surface, clear view. Maintenance making itself almost invisible.|
Someone made it easier to see outside. Quiet work counts.|
Very clean glass. A reminder that a good finish is also somebody's time.|
No smears between us and the light. Someone took care with this.
''')
add('sky_window', 'Text_BeautifulSkyWindow', 'The window gives a beautiful view of the sky.', '''
That sky deserves a longer look. I can postpone my next important remark about snacks.|
A clear view of the sky. No measurement needed for enjoying it.|
Good view. We can spare a minute.|
That sky makes me want to write something with a little more room between the notes.|
A beautiful sky through the window. Even better with somewhere to sit and share lunch.|
Excellent lighting. For once I have no improvements to propose.|
I would describe that sky, but it is already doing a rather good job.|
A good view with no adjustments required. I am practising leaving it that way.|
The sky is allowed to be beautiful without becoming an omen. We can just look.|
Those colours work without asking anyone to wear them. A generous arrangement.|
I want to remember that light. A sketch might keep the colours, if I am quick.
''')
add('tool_display', 'Text_NeatlyLinedUpTools', 'The tools have been neatly arranged.', '''
Every tool in its place. My bag is quietly applying for a different owner.|
An orderly set of tools makes missing equipment easier to notice. Even my notebook could improve here.|
Tools put back properly. Saves searching when something actually goes wrong.|
All the tools lined up. I should arrange my spare strings before they arrange themselves into a knot.|
Every tool has a place. Like a kitchen before I start being creative with flour.|
The props are ready. An excellent production begins long before anyone notices the stage.|
Neatly arranged tools. My desk has requested that we stop looking at this.|
Everything visible and reachable. Whoever arranged this understands the glorious luxury of finding the correct wrench.|
Tools waiting where their owner expects them. There is comfort in a familiar arrangement.|
An organised kit. Functionally beautiful, and less likely to eat your afternoon.|
Each tool has room. Somebody composed this for the hands that will use it.
''')
add('dewford_trends', 'DewfordTown_Text_TinyIslandCommunity', 'Trends spread rapidly through the small island community.', '''
A trend reaches the whole island quickly. I shall be very careful where I debut my new hat.|
A small community shares information quickly. Popularity still does not establish whether something is true.|
News travels fast here. Best make sure it is worth passing on.|
A tune could cross this island before I finished it. That is encouraging and alarming.|
One successful loaf could become an island tradition. No pressure on breakfast, then.|
A ready audience for every new fashion. I should distinguish applause from everyone merely noticing.|
A whole island catches a trend. Finally, a poem could spread faster than my regret.|
Rapid adoption. I hope somebody tests a new invention before the entire island buys one.|
A story can travel quickly where people know one another. So can a misunderstanding.|
Trends spread fast here. I hope people still feel free to wear what suits them.|
A small island shares its colours quickly. I would like to know who starts them.
''')
add('devon_products', 'RustboroCity_Text_WeShortenItToDevon', 'Devon makes convenient products and locals shorten the company name.', '''
DEVON makes convenient products. I hope one keeps receipts from dissolving in my pocket.|
A company making useful equipment. I would judge each product by what it does, not the size of the building.|
DEVON, then. A shorter name leaves more time to ask whether the thing actually works.|
They shorten the name to DEVON. Good. The full version has too many beats for a casual introduction.|
Convenient products. If they invent a bread bag that never crushes the crust, I have suggestions.|
A short name for a large production. Let us see whether the props live up to the billing.|
They shortened the company name. Corporate poetry has finally discovered editing.|
DEVON makes equipment. I would very much like to see the testing bench before the sales pitch.|
A familiar name can stand for many people's work. I wonder whose names are not on the sign.|
Convenient products should make somebody's day easier. That is a useful design brief.|
Everyone knows the short name. I am curious about the people making things behind it.
''')
add('fortree_blocked', 'FortreeCity_Text_SomethingBlockingGym', 'An unseen obstruction blocks the route to Fortree gym.', '''
Something is blocking the GYM. I was hoping invisible obstacles were only a figure of speech.|
There is an obstruction we cannot identify yet. We should investigate rather than charge at empty-looking space.|
Something is there. Pushing harder is not always the answer.|
An unseen obstacle before the GYM. My stage fright has become architecture.|
He trained all that way and cannot get through. We can help look before suggesting more effort.|
An invisible obstruction. Effective stagecraft, inconvenient entrance policy.|
The path looks open and refuses us anyway. An uncomfortably accomplished metaphor.|
Unseen does not mean absent. Let us identify the obstruction before modifying the path.|
Something blocks the way. We do not need a supernatural explanation before checking what lives here.|
He prepared for a battle, not this barrier. Access matters as much as the challenge beyond it.|
The gap in the picture is occupied. We need a closer way of seeing.
''')
add('aqua_loot', 'LilycoveCity_Text_MovedLootIntoHideoutToday', 'An Aqua grunt blurts out that stolen goods entered the hideout.', '''
More loot in the HIDEOUT. That confession was considerably louder than his secrecy.|
He said they moved more loot into the HIDEOUT. That is actual information, not just a suspicious outfit.|
He mentioned stolen goods and the HIDEOUT. Worth remembering exactly what he said.|
That was a very public verse about a supposedly private operation.|
More stolen goods. Somewhere, somebody is missing what he is bragging about.|
An unsolicited confession followed by surprise at having an audience. Weak rehearsal discipline.|
He was talking to himself. Unfortunately for his secret, he has excellent projection.|
They moved more loot inside. A concrete lead; no need to improve it with guesses.|
Loot means belongings taken from people. His little boast has somebody else's loss behind it.|
He has explained the theft more clearly than he intended. We should remember the details.|
His secret HIDEOUT is receiving stolen things. There are people outside this picture who deserve them back.
''')
add('sootopolis_steps', 'SootopolisCity_Text_PhysicallyFitLivingHere', 'Diving and constant stairs make life in Sootopolis physically demanding.', '''
Stairs and diving every day. Even the errands have a training montage.|
The terrain shapes daily life. It may build fitness, but it also asks a lot of anyone who struggles with stairs.|
That is a lot of climbing just to get around. We can take breaks.|
All those stairs. The town has written percussion for my knees.|
Diving and stairs before lunch. I would pack a second lunch for the return trip.|
Daily life with this many entrances and ascents. The scenery demands an athletic cast.|
The stairs keep people fit. My legs have described the policy in less flattering language.|
That is a demanding route for ordinary errands. A better handrail would be a worthwhile invention.|
The town asks different things of different bodies. We should not mistake difficulty for a virtue everyone chose.|
All those stairs need practical shoes. And practical alternatives for anyone who cannot climb them.|
Beautiful buildings, demanding routes. A town is also the distance between its doorways.
''')
add('moon_rumour', 'PewterCity_Text_ClefairyCameFromMoon', 'The speaker calls Clefairy coming from the moon a rumor.', '''
CLEFAIRY from the moon. I shall wait for a return address before buying a ticket.|
They called it a rumour. The MOON STONES are interesting evidence, not a complete proof of where CLEFAIRY began.|
Maybe from the moon. We can be curious without pretending we already know.|
CLEFAIRY from the moon. That would explain the excellent night-time atmosphere, if the rumour is true.|
A rumour about the moon. I can supply star-shaped biscuits without claiming they prove anything.|
A lunar origin story. Splendid premise; I would still like to hear the witnesses.|
CLEFAIRY may be from the moon. I write poems about it, not travel guides.|
An intriguing theory. I would like measurements before adding lunar landing gear to a POKE BALL.|
They said rumour, and that distinction matters. We can enjoy the story without presenting it as a finding.|
A moon story suits CLEFAIRY beautifully. A flattering story can still need evidence.|
Moonlight, stones, CLEFAIRY. A wonderful composition. It does not automatically become a historical record.
''')
add('garden_repel', 'PewterCity_Text_SprayingRepelToKeepWildMonsOut', 'The gardener sprays Repel to keep wild Pokemon away.', '''
REPEL for the garden. The vegetables have hired a very small security service.|
REPEL keeps wild visitors away. I hope the gardener follows its instructions rather than treating more as automatically better.|
Keeping Pokemon out of the garden. Fair enough; they still need somewhere else to forage.|
The garden has a boundary now. A very quiet way of asking the audience to remain outside.|
Protecting the vegetables with REPEL. I understand wanting the harvest to reach the kitchen.|
The garden is closed to unsolicited performers. At least the notice is being delivered without a battle.|
REPEL for the garden. A strongly worded letter in spray form.|
A purpose-made deterrent. Much better than testing an alarming homemade fence on the local wildlife.|
People need gardens; wild Pokemon need food. Keeping one boundary does not solve the whole relationship.|
REPEL keeps visitors off the plants. I appreciate a boundary with a practical purpose.|
The garden is somebody's work. The Pokemon outside it are somebody's neighbours, too.
''')
add('lavender_white_hand', 'LavenderTown_Text_JustImaginingWhiteHand', 'The speaker teases the player about a white hand on their shoulder.', '''
annoyed~The white hand was a joke. My shoulders would appreciate advance notice next time.|
That is a teasing claim, not evidence of a ghost. I refuse to put it in my notebook as a sighting.|
They are trying to scare you. You do not owe them a convincing reaction.|
surprised~A white hand on my shoulder is not a cue I rehearsed. I would prefer a polite tap.|
Startling people is easy. Making sure they are all right afterwards is the useful part.|
An effective scare, perhaps. I prefer an audience that agreed to the performance.|
A white hand on the shoulder. Mine is probably trying to return an overdue book.|
I would like the alleged hand to provide a repeatable demonstration. Preferably somewhere other than my neck.|
An old ghost joke. I would rather ask who taught it to them than insist we have seen a ghost.|
That joke fits some people badly. We can ask them to stop if it makes us uncomfortable.|
A few words and suddenly the whole scene feels different. That is a reason to use them carefully.
''')
add('harbour_pollution', 'VermilionCity_Text_GrimerMultipliesInSludge', 'The town tries to prevent pollution and mentions Grimer in toxic sludge.', '''
Keeping sludge out of the harbour. A plan with benefits well beyond less alarming shoes.|
Clean water matters regardless of the GRIMER report. We should not make a Pokemon the excuse to ignore the pollution itself.|
Keep the harbour clean. People and Pokemon both have to live with what goes into it.|
Toxic sludge is a poor accompaniment to a seaside town. I would rather hear the waves.|
Clean water matters to the whole food chain. That includes lunch, but not only lunch.|
Pollution is more than an unattractive backdrop. The people living here cannot simply leave the scene.|
A harbour should not require a warning label. Cleaning it seems a sensible editorial decision.|
Preventing the waste is better than inventing a machine to move the smell somewhere else.|
GRIMER is part of the story, but the sludge came from somewhere. We should ask about that, too.|
A clean-looking waterfront can still have polluted water. Appearance is not the whole inspection.|
Water carries what the town puts into it. A harbour belongs to more than the view from the shore.
''')
add('ss_anne_departed', 'VermilionCity_Text_SSAnneHasDepartedForYear', 'The S.S. Anne has left and is expected next year.', '''
The S.S. ANNE has gone for the year. I shall stop pretending a brisk walk can catch it.|
The ship has departed. We should plan around the actual timetable rather than the one we would prefer.|
Gone until next year. No point chasing the wake. We have roads to travel.|
The ship has left. Some departures do not wait for us to find the perfect last note.|
Back next year. Plenty of time to improve a packed lunch, though a little inconvenient for today's plans.|
The ship has made its exit. We can appreciate it without trying to demand an encore from the harbour.|
Back next year. An unusually strict booking policy for something we can no longer see.|
A yearly return. I am making a note instead of attempting an emergency boat design.|
It left, and people expect it again. A departure can hold both an ending and a promise.|
Gone for the year. We can make another plan without calling this one a personal failure.|
The harbour has changed shape without it. I wonder what the crew will see before returning.
''')
add('koffing_temper', 'CeladonCity_Text_GotMyKoffingInCinnabar', 'The owner says Koffing is usually nice but releases poison when angry.', '''
Usually nice, poisonous when angry. I shall introduce myself from a respectful breathing distance.|
Recognising KOFFING's warning signs matters. We should give it space rather than provoke a demonstration.|
Give it room when it is angry. That is good manners and very practical lung care.|
KOFFING can be kind and still need space. I would prefer our introduction to stay a quiet passage.|
A nice Pokemon with dangerous fumes. Let us keep the food sealed and the introductions considerate.|
No need to test the angry performance. The owner has already supplied the relevant warning.|
Nice until angry, then poison. I shall not read my experimental poems to it without permission.|
The fumes are a real hazard. Good ventilation and a calm approach beat testing its patience.|
It has limits. Being usually gentle does not mean it must tolerate everything.|
A friendly nature does not remove a need for boundaries. Especially breathable ones.|
The owner knows another side of it. We can respect both the affection and the warning.
''')
add('saffron_threat', 'SaffronCity_Text_DontGetDefiantOrIllHurtYou', 'A Rocket grunt threatens to hurt the player.', '''
annoyed~That was a threat. Let us stay together and look for a safe way through this.|
annoyed~They threatened harm. We should take that seriously without accepting their right to control us.|
annoyed~Stay close. They do not get to make a threat sound like a rule.|
sad~That is frightening. I am here. We can decide our next move without doing it alone.|
annoyed~Threatening people is not strength. Let us keep the team safe and think before moving.|
annoyed~That was no harmless performance. Stay with me; we should choose our next step carefully.|
annoyed~I have no clever line for that. It was cruel, and I am staying beside you.|
annoyed~A credible hazard. We need a plan and a clear route, not a test of pride.|
sad~A threat is meant to shrink your choices. We can take a moment and look for the ones still open.|
annoyed~You do not deserve that. Let us keep each other safe before worrying about looking brave.|
annoyed~They are trying to decide who belongs in this street. We should not have to face that alone.
''')

# Whole-game expansion; preserve the released first 47 IDs above.
from companion_world_objects import ROWS as WORLD_OBJECT_ROWS
ROWS.extend(WORLD_OBJECT_ROWS)
from companion_world_people import ROWS as WORLD_PEOPLE_ROWS
ROWS.extend(WORLD_PEOPLE_ROWS)
from companion_hoenn_people import ROWS as HOENN_PEOPLE_ROWS
ROWS.extend(HOENN_PEOPLE_ROWS)
from companion_kanto_people import ROWS as KANTO_PEOPLE_ROWS
ROWS.extend(KANTO_PEOPLE_ROWS)
from companion_route_people import ROWS as ROUTE_PEOPLE_ROWS
ROWS.extend(ROUTE_PEOPLE_ROWS)
from companion_kanto_interiors_routes import ROWS as KANTO_INTERIOR_ROUTE_ROWS
ROWS.extend(KANTO_INTERIOR_ROUTE_ROWS)
from companion_gym_people import ROWS as GYM_PEOPLE_ROWS
ROWS.extend(GYM_PEOPLE_ROWS)
from companion_hoenn_interiors import ROWS as HOENN_INTERIOR_ROWS
ROWS.extend(HOENN_INTERIOR_ROWS)
from companion_gym_people_extra import ROWS as GYM_EXTRA_ROWS
ROWS.extend(GYM_EXTRA_ROWS)
from companion_routes_105_119 import ROWS as HOENN_ROUTE_ROWS
ROWS.extend(HOENN_ROUTE_ROWS)
from companion_kanto_interiors_routes_extra import ROWS as KANTO_INTERIOR_ROUTE_EXTRA_ROWS
ROWS.extend(KANTO_INTERIOR_ROUTE_EXTRA_ROWS)
from companion_route_registrations import ROWS as ROUTE_REGISTRATION_ROWS
ROWS.extend(ROUTE_REGISTRATION_ROWS)
from companion_hoenn_interiors_extra import ROWS as HOENN_INTERIOR_EXTRA_ROWS
ROWS.extend(HOENN_INTERIOR_EXTRA_ROWS)
from companion_kanto_gym_people import ROWS as KANTO_GYM_ROWS
ROWS.extend(KANTO_GYM_ROWS)
from companion_kanto_interiors_final import ROWS as KANTO_INTERIOR_FINAL_ROWS
ROWS.extend(KANTO_INTERIOR_FINAL_ROWS)
from companion_shared_objects import ROWS as SHARED_OBJECT_ROWS
ROWS.extend(SHARED_OBJECT_ROWS)
from companion_routes_120_134 import ROWS as HOENN_LATE_ROUTE_ROWS
ROWS.extend(HOENN_LATE_ROUTE_ROWS)
from companion_berry_objects import ROWS as BERRY_OBJECT_ROWS
ROWS.extend(BERRY_OBJECT_ROWS)
from companion_hoenn_interiors_final import ROWS as HOENN_INTERIOR_FINAL_ROWS
ROWS.extend(HOENN_INTERIOR_FINAL_ROWS)
from companion_kanto_interiors_remaining import ROWS as KANTO_INTERIOR_REMAINING_ROWS
ROWS.extend(KANTO_INTERIOR_REMAINING_ROWS)
