"""Kanto binocular views and remaining fixed inspection outcomes."""
ROWS=[]
E=dict(N='neutral',S='soft_smile',A='annoyed',F='flustered',D='sad',U='surprised',M='smug',L='laughing')
def add(key,labels,subject,lines):
    replies=[]
    for s in lines.strip().split('|'):
        s=s.strip()
        if len(s)>1 and s[1]=='~'and s[0]in E:s=E[s[0]]+s[1:]
        replies.append(s)
    assert len(replies)==11,(key,len(replies))
    ROWS.append(dict(key='kanto_view_'+key,labels=labels.split(),subject=subject,replies=replies))
add('sleeping_road','Route11_EastEntrance_2F_Text_BigMonAsleepOnRoad',
    "Binoculars reveal a large Pokemon asleep on a road.",'''
S~From here the roadblock looks rather peaceful. I expect the people walking around it disagree.|
N~The distant view confirms a sleeping obstacle without telling us how best to resolve it.|
N~Useful to know before choosing the route. Do not rush there without a plan.|
S~It is strange how something inconvenient can look so calm from far away.|
N~We can prepare an alternative route rather than arrive annoyed at a sleeping creature.|
S~The distant landscape has acquired a very substantial resting protagonist.|
S~A magnificent nap is quietly rearranging several people's afternoons.|
N~A view from above can reveal a route problem before we commit to it.|
S~The road has been borrowed by a little island of sleep.|
N~It is better to notice the obstruction now than blame the sleeper when we reach it.|
S~I wonder how many people have looked through here and recognized the reason for their detour.
''')
add('wide_view','Route11_EastEntrance_2F_Text_WhatABreathtakingView',
    "The gatehouse binoculars offer a breathtaking view.",'''
S~The world was doing all of that while we were busy looking at our own shoes.|
S~A broader view can make relationships between familiar landmarks much easier to see.|
S~Worth stopping for. We have time to look.|
S~Some views make me want to be quiet without feeling shy about it.|
S~A little pause can be a proper part of the journey, not merely a delay.|
S~The scenery has earned its extravagant establishing shot.|
S~A large enough view gives an ordinary worry a little less room.|
S~I like seeing how the separate pieces of the route fit together.|
S~The distance has made a little space inside the afternoon.|
S~It is lovely to find something that holds attention without demanding it.|
S~I would like to notice what changes in the scene while we stand still.
''')
add('tunnel_route_view','Route11_EastEntrance_2F_Text_RockTunnelGoodRouteToLavender',
    "The binocular view suggests Rock Tunnel as a route between Cerulean and Lavender.",'''
N~A distant route can look wonderfully simple until you remember it goes through a mountain.|
N~The view helps with orientation, though it does not show the conditions inside the tunnel.|
N~Useful route. Check our supplies before taking it.|
N~It is easier to picture the journey once the distant places belong on the same horizon.|
N~We should plan for the tunnel itself, not only the towns it connects.|
N~The landscape has provided the outline of a chapter while discreetly withholding its difficult middle.|
N~A line between two places can contain a surprising amount of darkness.|
N~A useful overview needs closer practical information before becoming a complete plan.|
N~The mountain is a bridge in the map's language and a mountain in ours.|
N~Distance makes almost every route look tidier than it feels underfoot.|
S~I wonder which landmark will look familiar from the road after seeing it from here.
''')
add('fisher_view','Route12_NorthEntrance_2F_Text_TheresManFishing',
    "The binoculars show a man fishing.",'''
S~A whole person somewhere is having a very different pace of afternoon from us.|
S~A distant ordinary activity can be as interesting as a dramatic landmark.|
S~Let him enjoy the quiet. We can move on after a look.|
S~I like noticing that the world carries on gently in places we are not walking through.|
S~A patient afternoon by the water sounds like a perfectly good plan.|
S~A small human scene has taken precedence over the grand landscape.|
S~Someone else's unhurried day has briefly entered ours.|
S~It is useful to remember the landscape is lived in, not just travelled across.|
S~A still figure has made the distant shore feel less empty.|
S~The ordinary little moment gives the view something warm to settle around.|
S~I wonder what he has noticed by staying in one place that we miss while moving.
''')
add('tower_view','Route12_NorthEntrance_2F_Text_ItsPokemonTower',
    "The binoculars show Pokemon Tower in the distance.",'''
N~The tower is easy to spot from here. A landmark can carry more than directions.|
N~Its height makes it useful for orientation, even though the building has a more personal meaning to visitors.|
N~A clear landmark. Treat the place with respect when we get there.|
N~It is strange seeing a place that means so much to people look so small in the distance.|
N~We can remember what the building is for while using it to find our way.|
N~A distant silhouette has brought a quieter kind of story into the view.|
N~A tall building can hold a great deal that the skyline does not show.|
N~A recognizable shape helps us understand where we are in relation to the town.|
N~The tower keeps its place on the horizon and many other places in memory.|
N~Not every striking landmark is simply scenery for visitors.|
N~I wonder how different that outline feels to someone who has a reason to return there.
''')
add('shining_bird','Route15_WestEntrance_2F_Text_LargeShiningBird',
    "A large shining bird is seen flying toward the sea through the binoculars.",'''
U~Oh! That is a very impressive piece of the sky to catch moving past.|
U~A brief sighting can be valuable without supplying a destination or a complete account of the bird.|
S~A remarkable sight. No need to chase it just because we saw it.|
S~I am glad we stopped long enough for that little moment to happen.|
S~A surprise like that can make the whole walk feel richer.|
U~The scenery has briefly admitted a guest far too striking to remain background.|
S~A bright shape has crossed the distance and improved the afternoon without staying for applause.|
U~The glimpse is worth remembering carefully before excitement adds details we did not see.|
S~The sky has let a small bright secret pass where we could notice it.|
S~Some things are lovelier for not stopping to belong to the person watching.|
U~I would remember the direction and the light, then let the sight stay exactly as surprising as it was.
''')
add('island_horizon','Route15_WestEntrance_2F_Text_SmallIslandOnHorizon',
    "A small island can be seen on the horizon.",'''
S~A tiny bit of land has found an excellent way to make us wonder what is over there.|
S~The visible outline establishes land in that direction, not a safe or accessible route to it.|
N~Interesting view. Check proper travel information before making a plan.|
S~A small distant place can leave a surprisingly large space in the imagination.|
N~It would take more than enthusiasm and a pointed finger to visit safely.|
S~The horizon has supplied a very small invitation with an impressively large unwritten sequel.|
S~A little shape far away can make the familiar shore feel less final.|
N~Distance and transport matter as much as spotting the destination.|
S~The sea has kept a small place just inside the edge of seeing.|
S~It is a lovely possibility to think about without having to decide anything today.|
S~I wonder which familiar place on our shore looks just as small to someone standing there.
''')
add('store_view','Route16_NorthEntrance_2F_Text_ItsCeladonDeptStore',
    "The Celadon Department Store can be seen through the binoculars.",'''
S~Even from here the store manages to look like it has several more errands to offer us.|
S~A prominent building is useful for orienting ourselves relative to the city.|
S~Good landmark. We know where to find supplies if we need them.|
S~It is funny how a familiar stop looks like part of a much bigger place from here.|
N~A useful reminder to finish the supply check before leaving the city behind.|
S~The great palace of shopping has secured its own place in the establishing view.|
S~A very large collection of little reasons to spend money is visible from an impressive distance.|
S~A recognizable landmark makes the layout of the surrounding area easier to understand.|
S~A familiar doorway has become a small solid shape in a much larger afternoon.|
S~Its place in the skyline makes all those little browsing trips feel connected to the city.|
S~I wonder how many people looking this way recognize the floor they last spent too long on.
''')
add('path_over_water','Route16_NorthEntrance_2F_Text_LongPathOverWater',
    "A long path over the water is visible in the distance.",'''
S~Somebody looked at all that water and decided the walk should continue anyway.|
S~The elevated view shows the route's extent much more clearly than standing on it would.|
N~A long exposed stretch deserves a supply and weather check before we take it.|
S~I like how a path can turn an open space into somewhere people meet.|
N~Worth knowing where we can stop before committing to the whole length.|
S~A determined line has been drawn across a landscape that preferred being water.|
S~Distance has made a long piece of human stubbornness look rather graceful.|
S~A substantial structure must solve a lot of practical problems that are invisible from here.|
S~A little road has learned to keep company with the sea.|
S~It looks elegant from here, though I expect tired feet measure it differently.|
S~I wonder which part of that long crossing gives people the best excuse to pause.
''')
add('pallet_view','Route18_EastEntrance_2F_Text_PalletTownInWest',
    "The binocular view places Pallet Town to the west.",'''
S~A familiar name has found a small place on a very large view.|
S~Recognizing a distant town helps connect the route to a broader mental map.|
S~Useful bearing. Good to know where the familiar ground lies.|
S~Seeing somewhere familiar from far away makes me think about the people carrying on there.|
S~A place can feel close in memory while being quite a walk away.|
S~The earlier setting has made a quiet return at the edge of the current scene.|
S~A small town can occupy rather more space in a person than it does on a horizon.|
S~Landmarks are easier to remember when there is already a personal reason to recognize them.|
S~The distance has made a familiar place into a little steady point of light.|
S~It is lovely to see a place we know become part of a wider view.|
S~I wonder what somebody standing there would recognize first if they looked back this way.
''')
add('swimming_view','Route18_EastEntrance_2F_Text_PeopleSwimming',
    "People can be seen swimming in the distance.",'''
S~The water is holding a completely different afternoon from the one on this road.|
S~A few moving figures make the distance feel inhabited rather than merely scenic.|
N~Hope they are staying in the safe water. We need not watch for long.|
S~It is nice to see people simply enjoying the place we are travelling past.|
S~A bit of leisure makes the coast feel like somebody's home rather than only a route.|
S~The grand seascape has added a small and cheerful human subplot.|
S~An ordinary pleasant day becomes rather lovely when seen as part of a larger one.|
S~A landscape changes character when we notice how people actually use it.|
S~Small moving shapes have given the blue distance a warmer scale.|
S~The best view often includes somebody enjoying it from a completely different angle.|
S~I wonder which part of the coastline they would call their familiar place to return to.
''')
add('magikarp_record','Route12_FishingHouse_Text_MostGiganticMagikarpXSize',
    "A fisherman's chart records the largest Magikarp measured so far.",'''
S~A fish has earned a rather impressive place in somebody's highly specialized record book.|
S~The record is limited to what this observer has witnessed, which is a useful qualification.|
S~A clear record beats arguing from memory about the biggest one.|
S~I like thinking about the excited little moment that made someone write the number down.|
S~A hobby can turn one unexpected catch into a story that lasts for years.|
S~The celebrated aquatic giant has been commemorated with admirably precise publicity.|
S~A fisherman's story has been given the discipline of a measurement. A bold development.|
S~A written record makes the next comparison much easier to check.|
S~One bright life in the water has left a small permanent mark on the wall.|
S~It is a charmingly specific thing for a person to care about.|
S~I wonder which detail of the actual encounter the tidy number fails to capture.
''')
add('magikarp_blank','Route12_FishingHouse_Text_BlankChartOfSomeSort',
    "An empty chart has room for future fishing records.",'''
S~A blank chart is a very patient way to announce optimistic plans for future fish.|
S~The format is prepared, but the observations have not yet filled it. A sensible distinction.|
N~No record yet. Let the first entry be an honest one.|
S~It is nice to see someone make room for a discovery before knowing when it will arrive.|
S~Anticipation can be a pleasant part of a hobby even on the quiet days.|
S~The wall has booked space for a future champion with no confirmed date of appearance.|
S~An empty box has been appointed custodian of somebody's hopes.|
S~A consistent recording method is useful before the excitement of an unusual catch.|
S~A little white space is waiting for the water to offer it a story.|
S~A neatly prepared chart says quite a lot about how much this person enjoys the subject.|
S~I wonder how long it will be before the owner has an excuse to fill in the first line.
''')
add('bicycle_display','CeruleanCity_BikeShop_Text_ShinyNewBicycle',
    "A new bicycle gleams in the shop display.",'''
S~Those wheels are making a very persuasive argument against our feet.|
S~An attractive display encourages interest; suitability still depends on the rider's actual needs.|
N~Worth looking at the fit before being persuaded by the shine.|
S~A new bicycle makes all the roads outside seem a little different.|
S~A practical way to travel can also be something somebody is simply excited about.|
S~The shop has displayed a remarkably elegant solution to the problem of repeated walking.|
S~Two shiny circles have suggested a whole afternoon of getting somewhere faster.|
S~The mechanics are worth a closer look. A bicycle packs a lot of useful design into a small frame.|
S~A still little machine is carrying the shape of movement.|
S~A clean design can be lovely without needing much decoration.|
S~I wonder what the first familiar road feels like when someone rides it instead of walks it.
''')
add('rocket_exit_hole','CeruleanCity_House2_Text_TeamRocketLeftWayOut',
    "Damage left by Team Rocket provides a way out of the robbed house.",'''
N~An extra exit is not much of a silver lining when somebody had to break the house to make it.|
N~The opening may be usable, but it remains evidence of an intrusion and damage to a home.|
N~Watch the broken edges. The residents should not have to live around this.|
N~It is sad when someone else's ordinary room becomes part of a frightening story.|
N~Getting outside is useful. Putting the home right afterward still matters.|
N~The criminals have supplied an architectural shortcut nobody here asked to receive.|
N~A useful gap can still be a very ugly thing to have forced into a person's life.|
N~Damage can create access without making it a well-designed or safe doorway.|
N~A home's boundary has been broken in more than one way.|
N~I would rather remember the people who have to stay here than admire the convenience.|
N~I wonder how long it will take before the room feels like theirs again.
''')
add('vending_decline','CeladonCity_DepartmentStore_Roof_Text_NotThirsty',
    "The player leaves the vending machine without buying a drink.",'''
S~The machine has survived a visit without persuading our pockets to hydrate.|
N~The interaction ended without a purchase. No drink has been dispensed.|
N~Nothing needed. We can move on.|
S~It is nice to look at an option and leave it as an option.|
S~No need to buy something simply because we stopped beside it.|
S~The vending machine has received a brief audience and no commercial resolution.|
S~A transaction has been gracefully spared the effort of existing.|
N~Choosing not to use a service is a complete outcome.|
S~A small unopened possibility can stay behind without troubling the rest of the day.|
S~A little restraint is easier when nobody insists every stop must produce a purchase.|
S~I wonder how many people come up here more for the view than the drinks.
''')
add('slots_case','CeladonCity_GameCorner_Text_CoinCaseIsRequired',
    "The slot machine cannot be used without a Coin Case.",'''
N~The machine has found a very specific reason not to begin its argument with our money.|
N~The required Coin Case is missing, so the game cannot start.|
N~No game here right now. Plenty of other ways to spend the afternoon.|
N~A practical pause gives us room to decide whether we actually wanted to play.|
N~We do not have to turn every missing requirement into an urgent shopping errand.|
N~The entertainment has been postponed before it could become an expensive commitment.|
N~An absent little container has briefly become excellent financial advice.|
N~The access requirement is clear. It does not make participation necessary.|
N~A closed small door can leave a more peaceful path open beside it.|
N~It is all right to let this remain an activity we walked past.|
N~I wonder how different the room feels once we stop treating every bright machine as an invitation.
''')
add('mansion_switch_decline','PokemonMansion_Text_NotQuiteYet',
    "The player decides not to press the Mansion's secret switch yet.",'''
N~An unknown button has been asked to wait until we have thought past the satisfying click.|
N~Deferring an unfamiliar mechanism is reasonable while its effects remain unclear.|
N~Look at the surroundings before pressing it.|
S~I like that not yet can be a thoughtful answer instead of a failure of curiosity.|
N~A little patience can prevent a lot of wandering back to fix an avoidable choice.|
N~The dramatic mechanism has been denied its cue pending a closer reading of the scene.|
N~A mysterious switch is not owed the pleasure of being pushed immediately.|
N~Try to understand what might move before deciding to activate it.|
N~A small dormant thing can keep its promise of movement a little longer.|
N~A measured pause looks better than treating every mechanism as a dare.|
N~I wonder which detail nearby will tell us most about what that switch controls.
''')
add('mansion_switch_press','PokemonMansion_Text_WhoWouldnt',
    "The player presses a secret Mansion switch and changes the mechanism's state.",'''
U~The temptation has won. I hope we were paying attention to what the rooms looked like before.|
N~The switch changes a mechanism state. We should compare the surroundings rather than assume every change helps.|
N~Check what moved before choosing the next route.|
N~A familiar room feels less certain once something inside it has changed.|
N~Worth remembering the way back while we work out the new arrangement.|
S~The concealed control has received its cue and rearranged the practical scenery.|
N~A click is a small sound for something that can make a whole route unfamiliar.|
N~Observe the result carefully so the change becomes information instead of only surprise.|
N~An old house has shifted one of its quiet little choices.|
N~Curiosity is more useful when it remembers to inspect the result.|
S~I wonder which doorway will make the effect clearest when we look around again.
''')
add('elevator_key','RocketHideout_Elevator_Text_AppearsToNeedAKey',
    "The hideout elevator cannot be used without its key.",'''
N~The elevator has declined to go anywhere until a very particular small object joins us.|
N~A missing key is the indicated obstacle. The control panel alone cannot resolve it.|
N~Find the key. Stay alert while we look.|
N~It helps to have a clear next question when the whole place feels unfamiliar.|
N~We can check the route systematically instead of wearing ourselves out searching the same corner.|
N~The building's vertical progress has been withheld pending a minor but essential prop.|
N~A surprisingly small piece of absence can immobilize a large machine.|
N~Look for the intended access method rather than experiment with the mechanism.|
N~The lower places remain where they are while the threshold asks for its little tooth.|
N~At least the problem is more specific than an unhelpful refusal to move.|
N~I wonder who was meant to keep track of the key before our visit made that inconvenient.
''')
add('warehouse_unlock','FiveIsland_Meadow_Text_EnteredPasswordDoorOpened',
    "The two required passwords are entered and the warehouse door opens.",'''
S~Two very peculiar phrases have persuaded a very serious door. Language is doing odd work today.|
N~Both credentials have been supplied and the mechanism has confirmed access.|
N~Open now. Stay prepared for what is inside.|
N~It is a relief to finish the puzzle, even if the place beyond still feels uncertain.|
N~A clear entrance is a good moment to check we are ready rather than rush.|
S~The guarded threshold has accepted its two absurdly memorable lines of dialogue.|
N~A secret can sound ridiculous and still do an effective job of keeping a door shut.|
S~A completed two-part check has produced the intended mechanical response.|
N~A little knot of words has loosened the place's outer boundary.|
N~A successful entry is progress, not a reason to stop paying attention.|
N~I wonder whether anyone choosing those passwords ever imagined a stranger patiently putting them together.
''')
add('seafoam_boulders','SeafoamIslands_B4F_Text_BouldersMightChangeWaterFlow',
    "A hint suggests that boulders may alter the flow of water.",'''
N~The water may be asking for a much larger conversation piece than we first expected.|
N~An obstruction can alter a current, but we should examine the geometry before moving anything.|
N~Work out where the water will go before shifting a boulder.|
N~It is a little daunting to realize the path and the problem are the same moving water.|
N~A careful plan matters when a change can affect the whole route.|
N~The cavern has supplied a stage direction for rearranging a rather forceful piece of scenery.|
N~An inconvenient stone may be less inconvenient somewhere else. A dangerous amount of optimism, perhaps.|
N~Watch the channels and compare possible routes for the flow. Movement should follow understanding.|
N~The mountain may lend one of its still things to quiet a moving one.|
N~A useful hint still deserves patience before being treated as a complete plan.|
N~I wonder which small detail makes the intended flow visible once somebody knows to look for it.
''')
add('canyon_plants','SevenIsland_SevaultCanyon_Entrance_Text_RouteSign',
    "A canyon entrance notice asks trainers not to damage the plants.",'''
N~A canyon visit should not leave the plants wishing the path had stayed less popular.|
N~Plants can be damaged by repeated small disturbances even when no one visitor notices the cumulative effect.|
N~Watch our feet and leave the plants where they are.|
N~It is nice to see a welcome that remembers the things already living here.|
N~We can enjoy the place without treating every growing thing as something to push through.|
N~The destination has included a modest request that the audience not destroy the scenery.|
N~A plant does not become disposable merely because it is standing beside a useful shortcut.|
N~Choosing a sensible route reduces unnecessary damage before anyone has to repair it.|
N~The green small lives have no other canyon to go home to.|
N~A good visit should not make the next person's view worse.|
N~I wonder which delicate little plant people miss when they only look up at the cliffs.
''')
add('green_path_clean','SixIsland_GreenPath_Text_RightRouteSign',
    "A Green Path sign asks visitors to keep nature clean.",'''
S~An excellent agreement: the path supplies the green, and we refrain from supplying the litter.|
N~Leaving nothing behind is a practical way to avoid adding harm to the habitat.|
N~Carry our rubbish out. Simple enough.|
S~I like when a place asks for care without needing to make a grand speech.|
N~Anything we brought in can make the return trip with us.|
S~The sign has proposed a very reasonable bargain with the visiting cast.|
N~The woods are under no obligation to become our discarded packaging department.|
N~Preventing a mess takes much less work than collecting it afterward.|
N~The path should keep only the brief shape of our footsteps.|
N~Leaving a beautiful place beautiful is a rather basic form of good manners.|
S~I wonder how different the path looks after a busy day when every visitor follows that little request.
''')
add('berry_forest_warning','ThreeIsland_BerryForest_Text_BewareWildBerryLovingMons',
    "A forest notice warns that wild Pokemon are drawn to Berries.",'''
N~A Berry forest attracts Berry enthusiasts. We should probably have allowed for that in the guest list.|
N~A food-rich habitat gives a clear reason to expect Pokemon in the area.|
N~Stay aware and keep the team ready. We are not the only visitors here.|
N~It helps to remember that a lovely place can also be somebody else's busy feeding ground.|
N~We should notice what the local Pokemon are doing before reaching for everything that looks ripe.|
N~The setting has warned us that its most attractive props come with an interested resident cast.|
N~The forest has a pantry, and we are hardly its only customers.|
N~Food availability influences where animals gather. That makes the warning practical.|
N~A patch of sweetness can gather more footsteps than the ones we see.|
N~A warning is useful when it reminds us to share a place rather than act as though we own it.|
N~I wonder which small movement in the leaves will be the first clue to who else is enjoying the Berries.
''')
add('berry_forest_sharing','ThreeIsland_BerryForest_Text_WelcomeToBerryForest',
    "The Berry Forest welcome asks visitors to share with other people and Pokemon.",'''
S~A forest welcome that includes the important instruction not to become the entire Berry supply's owner.|
S~Sharing the resource helps a pleasant place remain useful to more than the first person through it.|
N~Take reasonably and leave enough for the others.|
S~I like a welcome that makes us part of the company rather than the centre of it.|
S~A sweet thing is often nicer when somebody else gets some, too.|
S~The hospitality is generous enough to include both the visiting and resident cast.|
S~A modest reminder that finding something first is not the same as needing all of it.|
N~A shared resource works better when each visitor considers what remains after them.|
S~A little sweetness can travel between several lives without becoming smaller in memory.|
S~Good company begins with remembering there are others in the place.|
S~I wonder which ordinary shared Berry becomes somebody's favourite memory of the walk.
''')
add('bridge_quiet','ThreeIsland_BondBridge_Text_BondBridgeSign',
    "A Bond Bridge sign asks people to cross quietly on the way toward Berry Forest.",'''
S~The bridge has requested that we arrive in the forest with our voices still on their indoor setting.|
N~Reducing noise can make the crossing less disruptive to the surrounding habitat.|
N~Keep it quiet. We can listen while we walk.|
S~A quiet crossing sounds like a lovely way to notice what is around the path.|
S~There is something pleasant about a group deciding it does not need to fill every silence.|
S~The entrance to the next setting has requested a gentler opening performance.|
S~A little restraint is an excellent travelling companion near a forest.|
N~Less noise gives us better information about the surroundings as well.|
S~A bridge can carry footsteps without needing to carry a whole argument.|
S~It is a considerate request, and an easy way to be a good visitor.|
S~I wonder what small sounds become noticeable once nobody is talking over the crossing.
''')
add('horn_notice','SixIsland_WaterPath_Text_WantedUltimateHorn',
    "A notice advertises a search for the ultimate horn.",'''
L~Somebody has given a very particular bug obsession the magnificent title it clearly feels it deserves.|
N~An ambitious superlative needs a clear measurement if people are expected to compare examples.|
N~A very specific interest. We can read it without taking on a new obligation.|
S~I like how boldly someone has let a favourite subject occupy a little piece of the path.|
S~A hobby can make a whole ordinary island feel full of promising encounters.|
S~The quest announcement has selected the grandest possible title for a remarkably specialized subject.|
S~A small notice has put a very large hat on an enthusiast's question.|
S~I would ask what makes a horn ultimate before treating it as an engineering specification.|
S~A single unusual shape has become someone's bright little horizon.|
S~That is a person who knows exactly which detail catches their eye.|
S~I wonder whether the search is more fun to them than ever declaring the final winner.
''')
add('discarded_items','Route17_Text_WatchOutForDiscardedItems',
    "A Cycling Road notice warns riders about discarded items.",'''
N~Things left on a cycling route are a much less charming surprise when the ground is moving quickly past.|
N~Loose objects can become hazards when riders have limited time to react.|
N~Watch the path and keep control of the bike.|
N~It is frustrating when one person's forgotten rubbish becomes another person's sudden problem.|
N~Anything we bring should stay securely packed until there is a proper place for it.|
N~The scenic route has acquired an unfortunate scattering of unscheduled obstacles.|
N~Somebody else's carelessness has a remarkable talent for appearing under our wheels.|
N~Good visibility and a manageable pace help us respond without a sudden dangerous correction.|
N~The path should not have to keep catching what people failed to carry.|
N~A little care with belongings would spare everyone else this warning.|
N~I wonder how many riders have learned to scan the road because of one small object in the wrong place.
''')
add('throw_balls_notice','Route17_Text_DontThrowGameThrowBalls',
    "A playful notice tells readers to throw Poke Balls rather than throw the game.",'''
L~A notice has wandered onto the cycling road specifically to make a pun. I respect the dedication.|
S~Wordplay is a useful way to make a short message memorable, even if it supplies little practical detail.|
S~A harmless joke. At least the sign is trying.|
S~I like finding a little silliness in the middle of ordinary directions.|
S~A small joke can make a long stretch of road feel more human.|
M~The signwriter has delivered a compact double meaning and retired before the reviews arrive.|
S~A public notice has been briefly relieved of its duty to sound important.|
S~A memorable phrase can work better than a long instruction nobody remembers reading.|
S~A little twist of words has been left beside the road for passing minds to catch.|
S~It is charming that someone spent time making a routine notice playful.|
S~I wonder who first laughed enough at that line to decide it needed a permanent sign.
''')
add('fanclub_signatures','SaffronCity_Text_TrainerFanClubSign',
    "Many trainers have scribbled their names on the Fan Club sign.",'''
S~The sign has become a guest book with rather more confidence than available space.|
S~The accumulated names suggest people want to leave evidence of having been part of the place.|
N~No need to add ours just because the surface is already crowded.|
S~It is sweet in a slightly untidy way that people wanted to be remembered here.|
S~A shared interest can make a little doorway feel like somewhere people belong.|
S~The audience has collectively promoted itself into the credits.|
S~A small sign has been asked to carry an unnecessarily ambitious amount of identity.|
N~A designated guest book might do the job without making the directions harder to read.|
S~A crowd of little names has gathered around one ordinary entrance.|
S~Wanting a trace of yourself in a favourite place is understandable, though the sign could use some mercy.|
S~I wonder which name belongs to somebody who still stops and smiles every time they walk past.
''')
add('silph_new_product','SaffronCity_Text_SilphsLatestProduct',
    "An advertisement announces a forthcoming Silph product without a release date.",'''
N~A bold announcement that has thoughtfully left the part where it happens blank.|
N~The notice states intent, not a confirmed release schedule or demonstrated result.|
N~We can wait for real details before getting attached to the promise.|
S~There is a little excitement in something unfinished, as long as nobody mistakes it for ready.|
N~A future possibility does not need money or worry from us today.|
S~The premiere has been announced with impressive confidence and no date whatsoever.|
N~A promise has taken a very comfortable seat where a fact might eventually arrive.|
N~I would rather hear what has been tested than how impressive the announcement is.|
N~A bright blank space has been put on display before anything has grown into it.|
N~Anticipation is pleasant; vague advertising is not the same as useful information.|
S~I wonder how different the finished thing will be from what people imagine after reading that little notice.
''')
