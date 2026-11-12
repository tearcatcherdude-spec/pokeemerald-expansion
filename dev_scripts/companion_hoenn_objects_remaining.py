"""Further exact Hoenn object endings, including native painting captions."""
ROWS = []
EMOTIONS = dict(N='neutral', S='soft_smile', A='annoyed', F='flustered', D='sad', U='surprised', M='smug', L='laughing')

def add(key, labels, subject, lines):
    replies = [x.strip() for x in lines.strip().split('|')]
    replies = [EMOTIONS[x[0]] + x[1:] for x in replies]
    assert len(replies) == 11, (key, len(replies))
    ROWS.append(dict(key='hor_'+key, labels=labels.split(), subject=subject, replies=replies))

add('cool_nonstop', 'gMuseumPaintingCaption_Cool0', 'A museum caption praises the pictured Pokemon as endlessly cool and inestimable.', '''
L~Nonstop coolness sounds tiring. Does it get a little blanket during closing hours?|
S~Inestimable is a convenient assessment. It spares the curator from specifying units.|
N~The caption's impressed. I'll let the painting make its own case.|
S~That's a lot of confidence for a small card under a picture.|
L~Even cool Pokemon deserve an occasional warm lunch.|
M~The curator has abolished moderation. A bold editorial decision.|
N~Endlessly cool. At last, an occupation suited to a drafty museum.|
U~I'd enjoy comparing what each painter chooses to make a Pokemon look cool.|
S~Perhaps coolness stays longer when someone puts a frame around it.|
S~A confident caption can help a portrait. This one gives it an entire entourage.|
S~I'd ask the curator which detail made that description feel right.
''')

add('cool_looks', 'gMuseumPaintingCaption_Cool1', 'The museum caption greets viewers and compliments the Pokemon good looks.', '''
S~A painting that says hello first! Very considerate of the wall.|
S~An informal greeting makes the display unusually approachable.|
N~Friendly caption. No need to stand stiffly just because it's a museum.|
F~It almost feels like being introduced to someone. That's rather sweet.|
S~A welcome and a compliment. The little card has good manners.|
L~The portrait's publicist appears to be an enthusiastic friend.|
S~A cheerful greeting from a still image. I've met less welcoming living people.|
S~That opening draws you closer before you even study the picture. Clever.|
N~A small hello has been left here for every visitor.|
S~Looking good and making people comfortable. That's an excellent combination.|
S~I like a gallery label that sounds as though someone actually enjoyed meeting its subject.
''')

add('cool_great', 'gMuseumPaintingCaption_Cool2', 'The museum caption heaps marvelous, wonderful and great praise on the Pokemon.', '''
L~Three compliments! That Pokemon has won the adjective buffet.|
S~The description offers three positive judgments and remarkably little measurement.|
N~Someone really liked this Pokemon. Hard to miss that part.|
S~Whoever wrote the label sounds delighted. I like finding that in a museum.|
L~They didn't ration the praise. An admirably generous serving.|
M~One adjective entered the draft. Two friends followed it through the door.|
S~Occasionally excessive praise is simply someone having a good day.|
S~The enthusiasm comes through perfectly. Now I want to examine what inspired it.|
S~A small card can hold a surprisingly large fondness.|
L~The label has dressed the portrait in every compliment it owns.|
S~I'd be curious whether the artist or the curator chose those words. Both sound proud.
''')

add('beauty_venus', 'gMuseumPaintingCaption_Beauty0', 'A museum caption likens the beautiful Pokemon to the century last Venus.', '''
U~The last one this century? I'd better appreciate it before the calendar gets ideas.|
N~That is a sweeping historical claim for a portrait label. Beautifully ambitious.|
N~Quite a title to put under a picture. No pressure on the subject.|
S~They wanted the beauty to feel rare. The words make you slow down a little.|
S~Someone gave this portrait the grandest compliment they could find.|
M~The curator has declared the century's remaining beauty contest closed.|
S~An extravagant title. Even museums occasionally get carried away by a pretty face.|
N~I'd compare the framing and lighting before deciding what makes this portrait stand out.|
N~The century can keep counting. The picture has its own quiet time.|
S~That label promises something extraordinary. It certainly knows how to draw attention.|
S~I wonder how visitors from different years would respond to that same claim.
''')

add('beauty_smile', 'gMuseumPaintingCaption_Beauty1', 'The caption celebrates the Pokemon dazzling smile.', '''
S~A smile saved in paint. Useful for days when everyone outside is being a raincloud.|
S~A fleeting expression becomes available for repeated observation. A lovely use of portraiture.|
S~A good smile can carry a whole picture.|
S~I like that they noticed its smile, rather than only calling it beautiful.|
S~That sounds like the sort of expression that makes strangers smile back.|
S~The caption chooses one small expression and lets it outshine the room.|
S~A glittering smile. I can appreciate that without becoming personally glittery.|
U~Capturing a smile before it changes must take careful observation.|
S~A brief kindness can leave a long reflection. Even in paint.|
S~An expression gives beauty somewhere to live. Otherwise it's just a list of features.|
S~Smiles change so quickly. I like thinking the artist caught one worth keeping.
''')

add('beauty_idol', 'gMuseumPaintingCaption_Beauty2', 'The caption calls its Pokemon an incomparable Pokemon Center idol.', '''
U~A Pokemon Center idol! Does the waiting room have a fan club under the chairs?|
S~An interesting setting for celebrity. Regular visitors would certainly recognize a familiar face.|
S~Nice to have something cheerful around a place people visit when they're worried.|
F~A familiar Pokemon could make a Center feel less strange. I understand the affection.|
S~A little local celebrity at the Center. That sounds like a pleasant regular to have.|
L~From Center favorite to museum subject. An impressive expansion of the audience.|
S~An idol with a practical venue. Admirers can recover while being overwhelmed.|
S~The caption gives this portrait a connection to an everyday place. I like that.|
S~Some faces become part of a place before anyone notices.|
S~Local affection makes a different kind of fame. Usually a warmer one.|
U~I'd love to hear which visitors first started calling it the Center's idol.
''')

add('cute_sweet', 'gMuseumPaintingCaption_Cute0', 'The museum caption describes a lovely sweet Pokemon.', '''
S~Sweet without being sticky. A very convenient sort of portrait.|
S~A brief description, but the intended affection is quite clear.|
S~Simple praise. It doesn't need to shout to work.|
S~That label feels gentle. It leaves room to enjoy the picture.|
S~Lovely and sweet. Two things that don't require a complicated explanation.|
S~A modest caption has slipped past the museum's supply of superlatives.|
S~A small, uncomplicated kindness on a wall. I approve.|
S~A short label lets the expression and pose do more of the work.|
S~Some pictures ask for very little beyond a soft moment.|
S~The caption knows when to stop accessorizing. A useful skill.|
S~I'd be interested in what different visitors notice as sweet about the same portrait.
''')

add('cute_winner', 'gMuseumPaintingCaption_Cute1', 'The museum identifies the pretty Pokemon winning portrait.', '''
S~A winning portrait! I wonder whether the frame gets to share a tiny bit of the pride.|
S~The caption identifies a winning work without giving us its whole contest history.|
N~Good to see the result displayed where people can enjoy it.|
S~A prize can pass quickly. A portrait gives the proud moment somewhere to stay.|
S~Someone must have been pleased to see that portrait hanging here.|
S~A victory has acquired a frame and visiting hours. Rather civilized.|
S~A win preserved without requiring anyone to keep clapping forever.|
S~I'd enjoy comparing the choices that made this portrait stand out to the judges.|
S~The busy day has settled into a quiet picture.|
S~A winning look has to read beyond the first glance. A gallery gives it that chance.|
S~Seeing a winning work up close gives you time to notice what a quick announcement misses.
''')

add('cute_wink', 'gMuseumPaintingCaption_Cute2', 'The caption playfully asks the cute Pokemon for a wink.', '''
L~We'll be waiting a while for that wink. Paint is famously stubborn about blinking.|
S~The request makes the subject feel responsive, despite the obvious limitations of paint.|
S~Cheerful label. We'll spare the portrait a staring contest.|
F~Asking a portrait to wink is a little silly. I smiled anyway.|
L~If it actually winks, I'm checking how much sleep we've had.|
M~The caption requests audience participation from the least mobile person in the room.|
L~An unanswered wink request. At last, a social difficulty I share with a painting.|
U~A playful line can make a still picture feel lively. No moving parts needed.|
S~Perhaps the wink waits until everyone looks away.|
S~Cute, direct, and just cheeky enough. The label understands its assignment.|
L~That's exactly the sort of thing someone says a moment before a subject refuses to cooperate.
''')

add('smart_wise', 'gMuseumPaintingCaption_Smart0', 'The caption praises the Pokemon wisdom and mastery of smartness.', '''
U~A master of smartness! I still occasionally lose arguments to doors marked pull.|
S~Wisdom and quick thinking aren't identical. The caption seems pleased to credit both.|
N~A clever Pokemon deserves recognition too. Strength isn't the whole story.|
S~I like seeing a quiet quality given a place on the wall.|
S~Being wise might include knowing when to stop showing off. A useful talent.|
M~Smartness has acquired a maestro. I await the appointment of a deputy.|
S~A wise portrait would probably let us finish our observations without correcting us.|
U~I'd like to know how the artist makes intelligence visible in a still image.|
N~Wisdom can be hard to paint. You mostly see what someone does with it.|
S~An intelligent expression is more interesting than simply adding a serious pose.|
S~I'd ask what the subject did that made people think of wisdom in the first place.
''')

add('smart_chosen', 'gMuseumPaintingCaption_Smart1', 'The museum caption gives its Pokemon singular praise as chosen above all others.', '''
U~Above all Pokemon is a very tall compliment. I hope the frame has sturdy hooks.|
N~An absolute claim, with no selection method attached. Clearly this is praise, not a census.|
N~Someone chose a favorite and committed to it.|
F~That's a grand thing to say about one Pokemon. It must mean a lot to someone.|
S~Favorites have a way of becoming the best in the whole world to their people.|
M~The caption has politely dismissed every other contender on the planet.|
N~Universal supremacy. Museums occasionally have remarkably enthusiastic handwriting.|
N~I'd want to hear what set this subject apart for whoever chose it.|
S~One Pokemon can fill someone's whole view for a moment.|
N~A dramatic claim catches attention. The portrait still has to hold it.|
S~That sounds like a story someone would tell with a lot of pride. I'd listen.
''')

add('smart_elegance', 'gMuseumPaintingCaption_Smart2', 'The caption preserves a moment of elegance for an excellent Pokemon.', '''
S~A moment of elegance. Good thing nobody painted the moment just after a sneeze.|
S~Selecting one moment is part of the portrait's interpretation, not merely its timing.|
S~A good moment to keep. They don't all announce themselves beforehand.|
S~I like the word moment there. It lets the Pokemon have other moods too.|
S~Nobody has to be graceful all day to have a graceful moment.|
S~The caption wisely limits perfection to a manageable interval.|
S~A moment of elegance is plenty. Sustained elegance sounds exhausting.|
S~The artist had to choose the pose that would make that brief quality last.|
N~Something passing has found a place to rest.|
S~Elegance often depends on restraint. The caption leaves a little breathing room.|
S~One good instant can tell a story without pretending it was the subject's whole day.
''')

add('tough_speed', 'gMuseumPaintingCaption_Tough0', 'The caption praises a muscular fast Pokemon.', '''
U~Muscles and speed! Even its compliments have somewhere urgent to be.|
S~Power and speed are distinct attributes. An effective portrait can suggest both.|
N~Strong and quick is a useful combination. The picture gets to stand still, at least.|
S~Trying to show speed in something still must be an interesting challenge.|
L~That sounds like a Pokemon with a healthy appetite after practice.|
S~The caption promises momentum while the frame heroically prevents any escape.|
S~A speedster obliged to remain on a wall. A quiet little irony.|
U~I'd study how the pose carries motion without actually moving.|
N~A moving strength, caught briefly between one place and the next.|
S~A powerful pose needs a clear shape. Otherwise all that energy gets lost.|
S~A still portrait of a fast subject makes me curious about the moments on either side.
''')

add('tough_strongest', 'gMuseumPaintingCaption_Tough1', 'The museum caption escalates its praise from strong to strongest.', '''
L~Strong, stronger, strongest! The label has done three little push-ups.|
S~A complete progression of comparison, though the comparison group remains unspecified.|
N~We understood strong the first time. The extra two make their point.|
S~It sounds like the writer got more excited as the sentence went on.|
L~That's three helpings of strong. Nobody's leaving this label hungry.|
M~The adjective climbed its own podium before the sentence ended.|
S~A very short escalation. Considerably tidier than most arguments about strength.|
S~Repeating the word with increasing force is a surprisingly efficient bit of emphasis.|
N~The picture stays still while its description keeps growing.|
L~Even the praise has layers. This label arrived fully styled.|
S~I'd enjoy hearing the writer read that aloud. I suspect the last word gets some volume.
''')

add('tough_hyper', 'gMuseumPaintingCaption_Tough2', 'The museum caption enthusiastically calls its Pokemon mighty tough and hyper.', '''
U~Hyper and mighty! I suddenly appreciate the fence a picture frame provides.|
N~The caption conveys intensity very clearly, even without a precise definition of hyper.|
S~Plenty of energy in that description. The gallery's managing to contain it.|
S~A lively subject in a quiet room. That contrast is rather nice.|
L~That caption sounds ready for an afternoon run. I am ready for an afternoon snack.|
L~The label has burst through three adjectives and is approaching the wall.|
S~So much energy preserved somewhere it cannot rearrange the furniture. Thoughtful.|
U~I'd like to see which visual details match all that force in the wording.|
N~A fierce little weather system, held inside a rectangle.|
S~That description needs a bold portrait beside it. Subtlety has already left the room.|
S~It sounds like a subject people remember. I'd ask the artist how sitting for it went.
''')

add('contest_hall_caption', 'gContestHallPaintingCaption', 'A contest hall painting caption identifies its contest, rank, trainer and Pokemon.', '''
S~A name, a Pokemon, and a place in the contest's story. A tidy little proud corner.|
S~The caption records category, rank, and participants. Useful context for the portrait.|
S~Good to give the trainer and Pokemon credit together.|
S~Seeing the names beneath it makes the picture feel more personal.|
S~It's nice that the display remembers the pair behind the performance.|
S~A compact credit for a partnership. No oversized speech required.|
S~Names under a picture keep admiration from becoming entirely anonymous.|
N~The category and rank help explain the setting without crowding out the subject.|
S~Two names share the space beneath one remembered moment.|
S~A clear caption lets the portrait have its personality and its proper credit.|
S~Now there's enough context to ask a good question about the Pokemon's contest experience.
''')

add('experience_tip', 'PetalburgWoods_Text_TrainerTipsExperience', 'A sign explains gaining battle experience by participating then switching out.', '''
S~A tiny turn at the front, then back to safety. Like testing a puddle with one toe.|
N~Participation can provide experience without requiring the weakest member to finish the battle.|
N~Give them a chance to learn. Have a safe switch ready first.|
S~A brief turn can still count. That's a comforting way to start learning.|
S~Small portions of practice are easier to manage than being thrown in all at once.|
S~An entrance needn't last long to become part of the story.|
N~Brief exposure, followed by a sensible retreat. I respect this educational model.|
N~That takes planning the team order before the battle starts. A useful detail.|
S~You can leave the difficult place and still carry something learned from it.|
S~A little confidence looks better than being pushed far past your limits.|
N~I'd pay attention to how the new Pokemon responds to those first short turns.
''')

add('pp_tip', 'PetalburgWoods_Text_TrainerTipsPP', 'The sign explains move PP as well as HP and recommends a Pokemon Center.', '''
U~Being healthy and having moves left are two different cupboards. Better check both.|
N~Physical condition and remaining move uses are separate limits. Both need monitoring.|
N~Don't judge readiness by health alone. An empty move list can end a plan quickly.|
N~You can look fine and still have nothing left to give. It's good the sign mentions it.|
N~A Center stop is useful before the last useful move runs dry.|
S~Even an excellent move cannot be asked for an unlimited encore.|
N~A reminder that looking alive is not the same as being prepared.|
N~Two indicators, two possible shortages. Checking both avoids a very preventable problem.|
N~Strength can run out along a quieter path than injury.|
N~There's more to readiness than what you can see at a glance.|
N~I'd ask a new trainer to check both before we headed farther into the woods.
''')

add('double_order_tip', 'Route104_Text_TrainerTipsDoubleBattles', 'A sign explains Double Battles and the importance of the first two team positions.', '''
S~The first two are a pair! Better introduce them before somebody starts calling orders.|
N~Team arrangement determines the opening pair. Compatibility matters before the first move.|
N~Check the first two positions now. Better here than after the challenge starts.|
N~Two Pokemon need room to work together. I'd think about both before choosing.|
S~Like sending out two dishes together. Timing and a sensible pairing help.|
S~A partnership begins with a very practical casting decision. Who goes first?|
N~Two at once. Twice as much reason to avoid improvising the entire plan.|
N~The list order is doing real work here. A small adjustment can change the opening.|
N~Being beside someone changes what either one can do alone.|
N~A good pair needs more than two individually impressive members.|
S~I'd be curious which two seem most comfortable taking the field together.
''')

add('fishing_tip', 'Route106_Text_TrainerTips', 'A sign tells anglers to respond with A when something bites.', '''
S~The fish gives the cue. We provide the very small burst of panic.|
N~Fishing combines waiting with a short response window. Quite a change of pace.|
N~Stay ready when the line moves. That's the part you can't do afterward.|
F~The waiting seems peaceful. I'd probably still jump when something bites.|
S~Patience first, quick hands second. A familiar combination.|
L~The rod offers a long pause followed by an extremely urgent punctuation mark.|
N~A quiet activity with a surprise deadline. How considerate.|
N~Keeping your hand ready seems more useful than staring harder at the water.|
S~Something below notices you before you can see it.|
S~Relaxed, but prepared. Fishing appears to have a very specific posture.|
S~That first tug must feel different once you've learned what you're waiting for.
''')

add('stats_tip', 'Route109_Text_TrainerTipsSign', 'A sign explains that equal levels need not mean identical stats and training matters.', '''
U~Same level, different strengths. So the number isn't the whole Pokemon after all.|
N~Level is a useful summary, not a complete description of individual capability.|
N~Know the Pokemon you've got. Don't rely on matching numbers.|
S~I like that two Pokemon can reach the same level in different ways.|
S~Training leaves its own mark. Time spent together isn't just a number.|
N~The tidy label conceals a rather untidy collection of individual differences.|
S~A reassuring warning against treating everyone with the same number as interchangeable.|
N~Comparing the individual stats will tell us more than the level alone.|
S~Two paths can reach the same marker without being the same path.|
N~A matching size tag never promised a matching fit. This makes sense to me.|
S~I'd ask about the training behind the numbers. That's where the interesting differences begin.
''')

add('status_tip', 'Route110_Text_TrainerTipsPrlzSleep', 'A sign explains sleep and paralysis as battle techniques.', '''
N~A battle plan can involve fewer attacks rather than bigger ones. Sneaky little sign.|
N~Restricting an opponent's actions changes the battle even without immediate damage.|
N~Remember status effects when planning. Power won't solve every situation.|
N~A battle can turn on who gets the chance to act. That makes me pay attention.|
N~It's useful advice. I'd keep the recovery supplies where we can find them too.|
N~The sign suggests depriving the opponent of their next contribution. Efficiently rude.|
N~Sleep as a tactic. Finally, a battle concept with a familiar appeal.|
N~Controlling the opponent's opportunities gives the rest of the plan room to work.|
N~Sometimes the most important move changes the space between the others.|
N~An opening can matter more than an impressive display of strength.|
N~I'd want to learn the signs of both conditions before trying to build a plan around them.
''')

add('bag_order_tip', 'Route110_Text_TrainerTipsRegisterItems', 'A sign explains reorganizing items inside the bag.', '''
L~An organized bag! A place where a Potion doesn't have to introduce itself to every pocket.|
S~Reducing search time is a modest improvement that becomes valuable through repetition.|
N~Put the useful things where your hand finds them first.|
S~Knowing where something is makes a hurried moment feel a little less loud.|
S~The same rule as a good cupboard: often-used things within easy reach.|
L~At last, a victory over the small chaos living at the bottom of a bag.|
S~Order inside the bag. A limited but achievable ambition.|
S~A simple reordering saves repeated effort later. Excellent small-scale design.|
N~Things are easier to find when they aren't hiding behind everything else.|
S~A useful arrangement should suit the person carrying it. Make it yours.|
S~Everyone organizes a bag differently. I'd be interested in what you put first.
''')

add('special_stats_tip', 'Route111_Text_TrainerTipsSpAtkSpDef', 'The sign expands the Special Attack and Special Defense abbreviations.', '''
S~Good. Two mysterious little labels have agreed to use their full names.|
S~Abbreviations are efficient once defined. Before that, they're merely compact obstacles.|
N~Useful to know which number you're looking at before trusting it.|
N~It's easier to ask about something once you know what it's called.|
S~A small explanation saves a lot of pretending you already understood.|
S~The sign generously unpacks two very tightly folded words.|
N~An abbreviation explained without another abbreviation. A rare courtesy.|
S~Clear labels make the whole set of information easier to use.|
S~A name made shorter can still need a longer introduction.|
N~A compact label works best when everyone knows what it means.|
S~This is the kind of basic question people hesitate to ask. Glad the sign answers it.
''')

add('register_key_tip', 'Route113_Text_TrainerTipsRegisterKeyItems', 'The sign explains assigning a key item to SELECT for convenient use.', '''
S~One favorite tool gets a shortcut. The rest will have to queue politely in the bag.|
N~A dedicated shortcut is most useful for the item with the highest repeated use.|
N~Choose something you reach for often. That's what makes the shortcut worth it.|
S~One less thing to search for when you're already concentrating. That sounds useful.|
S~Keep the regular tool close. The occasional one can stay packed.|
S~A frequently used item has been promoted to a very convenient address.|
N~One shortcut. Naturally, choosing it may take longer than using it.|
S~Saving a few steps on a repeated action adds up quickly. I like this feature.|
N~A familiar thing becomes easier to call when you give it a place.|
S~Convenience is personal. The best choice is the one that suits your routine.|
S~I'd ask which item keeps coming out of your bag. There's your likely answer.
''')

add('evolution_cancel_tip', 'Route116_Text_TrainerTipsBToStopEvolution', 'The sign explains stopping an evolution with B.', '''
U~You can interrupt it! That's a big change to leave with no little pause button.|
N~Evolution can be interrupted during the process. Timing is essential to that choice.|
N~Good to know before it happens. That's a decision to make with care.|
N~A big change can arrive suddenly. Knowing there's a way to pause it is comforting.|
N~Being able to stop doesn't make it a choice to rush. Pay attention to your Pokemon.|
N~A transformation has a moment in which the ending can still be reconsidered.|
N~Even a dramatic transformation permits an interruption. More considerate than most speeches.|
N~It's an important control to know before the process starts, rather than during it.|
N~A change can be near without having to happen this instant.|
N~Keeping a familiar form is a decision too. The sign makes that option clear.|
N~I'd want to know how the Pokemon felt about the change, not just how it looked.
''')

add('bag_pockets_tip', 'Route116_Text_TrainerTipsBagHasPockets', 'A sign explains the bag separate pockets and automatic item placement.', '''
S~Pockets with jobs! Finally, some reliable employees in this traveling collection of lumps.|
S~Sorting items by category reduces confusion as the collection grows. A sensible system.|
N~Different pockets for different uses. Learn where things go before you need them.|
S~It's reassuring to know something small won't disappear among everything else.|
S~Separate the supplies and finding one won't mean unpacking your whole life.|
L~An entire organizational philosophy disguised as a bag with extra pockets.|
S~A bag that sorts its contents. It has outperformed several desks I've encountered.|
S~Built-in categories save a lot of manual sorting. A good piece of everyday design.|
N~Everything has a small place to wait until it is needed.|
S~Practical pockets are a design feature I will always defend.|
S~A well-used bag says a lot about someone's journey. The pocket system helps it stay readable.
''')

add('base_decor_tip', 'Route119_Text_TrainerTipsDecoration', 'The sign gives the sixteen-item Secret Base decoration limit.', '''
U~Sixteen decorations! Seventeen would apparently be an interior-design emergency.|
N~A fixed limit makes selection part of the design. Each addition has an opportunity cost.|
N~Leave room to walk. A base should still be usable after it's decorated.|
S~A few things chosen carefully could make the place feel familiar.|
S~Somewhere to sit ought to survive the first fifteen exciting choices.|
S~Sixteen objects with which to explain your taste to anyone who wanders in.|
S~A decorating limit. A small mercy for both visitors and the floor.|
U~I'd sketch the arrangement first. Then the sixteen pieces can actually work together.|
S~A hidden place can become yours through a handful of chosen things.|
U~Sixteen is plenty for a strong idea. Decide what you want the room to feel like first.|
S~I'd enjoy visiting bases with the same limit and seeing how differently people use it.
''')

add('safari_block_tip', 'Route121_SafariZoneEntrance_Text_TrainerTip', 'A sign explains that PokeBlocks reduce the likelihood of Safari Pokemon fleeing.', '''
S~A snack can persuade someone to stay a little longer. I respect this discovery.|
N~The sign describes a change in fleeing probability, not a guarantee of capture.|
N~Useful to know. Keep the difference between better odds and a sure thing clear.|
S~Giving it a reason to stay seems gentler than simply hoping it won't leave.|
S~A well-timed treat has helped plenty of awkward meetings along.|
S~Hospitality enters the encounter with a surprisingly practical effect.|
N~Food reduces the urge to leave. Not an exclusively Pokemon observation.|
N~I'd compare how long encounters last with and without a block. Carefully, of course.|
S~An offered sweetness gives a wild moment a little more time.|
S~Making the first meeting pleasant can change its direction. A useful social principle.|
S~I'd pay attention to whether different Pokemon linger over different blocks.
''')

add('store_directory', 'LilycoveCity_DepartmentStore_1F_Text_FloorNamesSign', 'The department store directory lists services and merchandise on each floor.', '''
U~A whole floor for dolls! The directory has successfully endangered my concentration.|
S~A floor directory prevents a great deal of unnecessary searching. Particularly in a building this large.|
N~Pick the floor before climbing. Saves a few trips.|
N~It's nice to know where we're going before the stairs get involved.|
S~Useful things downstairs, dolls upstairs, and somewhere to pause on the roof. Sensible trip.|
S~An entire shopping expedition reduced to a few well-placed lines.|
N~A guide to ascending through increasingly optional purchases.|
S~Grouping each department by floor makes the route much easier to plan.|
N~Several little destinations stacked beneath one roof.|
S~A directory is part of the welcome. Nobody should need detective skills to find a department.|
S~I'd ask which floor people head for first. That probably tells you plenty about them.
''')

add('home_notebook', 'PlayersHouse_2F_Text_Notebook', 'The adventure notebook lists menu and saving rules before blank pages.', '''
S~Two rules, then all that blank paper. The notebook is leaving room for us to get interesting.|
S~A short operational guide followed by space for records. A practical beginning.|
S~Good basics. The rest can be written as you go.|
S~Blank pages can feel inviting when nobody has decided what belongs on them yet.|
S~Two useful reminders and plenty of room for whatever happens next.|
S~A remarkably restrained opening chapter. The remaining pages have confidence in you.|
S~An unfinished notebook is less intimidating when the first two rules are manageable.|
S~Essential instructions first, then room to extend the record. I like that arrangement.|
S~The empty pages haven't become memories yet.|
S~A clear beginning and generous space. That's a good notebook design.|
S~I like seeing what someone chooses to put on the first blank page.
''')

add('gamecube', 'PlayersHouse_2F_Text_ItsAGameCube', 'A Game Boy Advance is connected to a Nintendo GameCube as its controller.', '''
U~A little game machine helping a bigger game machine! Very cooperative electronics.|
S~The handheld doubles as an input device. An interesting reuse of existing hardware.|
S~Useful setup. One device gets another job.|
S~That looks like a comfortable way to spend a quiet afternoon at home.|
L~Everything connected and ready. That's how a short break becomes a long afternoon.|
S~Two machines have negotiated a partnership beneath one television.|
S~A controller with its own ambitions. I respect the versatility.|
U~I love seeing a portable device take on a second role in a larger system.|
N~The little machine stays connected to something it could usually leave behind.|
S~A clever arrangement, provided the cable doesn't take over the entire floor.|
S~I'd ask what games someone picks when they've finally got an afternoon free.
''')

add('space_center_sign', 'MossdeepCity_Text_SpaceCenterSign', 'The Space Center sign calls it the closest place to space.', '''
U~Closest to space! I suppose the roof gets a very small head start.|
S~The claim is more aspirational than geographical. An effective invitation, though.|
N~Good sign. Tells you what they're aiming for.|
S~It makes a huge distance feel a little less unreachable.|
S~A place where very far away becomes someone's daily work. I like that.|
S~An excellent promise for a building that remains firmly attached to the ground.|
S~A reassuringly short journey to an unsettlingly large distance.|
U~Inside are the plans and equipment that make that slogan more than a nice thought.|
N~One door away from people who spend their days thinking beyond the sky.|
S~Short, clear, and full of ambition. That's a sign people will remember.|
U~I'd ask someone here what first made space feel like a place they could actually reach.
''')

add('jagged_path_sign', 'MtChimney_Text_RouteSign', 'A sign points down Jagged Path toward Lavaridge Town.', '''
S~Jagged Path, then Lavaridge. The name seems to be doing some responsible warning.|
N~The sign provides the descent and destination. We'll still need to judge the footing.|
N~Downhill doesn't mean easy. Keep an eye on the path.|
N~It's nice knowing where the descent leads before starting it.|
S~A rough path with a town at the end. Enough reason to take our time getting there.|
S~A concise itinerary: uneven ground, followed by civilization.|
N~A path honest enough to advertise its own sharp edges.|
N~I'd check the way down before committing to a ledge. The destination can wait.|
N~The mountain gives us a downward road and a name to follow.|
N~Practical directions. Sensible shoes remain our department.|
S~A destination sign feels particularly welcome when the road starts dropping away.
''')

add('meteorite_removed', 'MtChimney_Text_PlayerRemovedMeteorite', 'The Meteorite has been removed from the mountain machine and successfully received.', '''
S~One space rock, freed from a very suspicious job. A better career move already.|
N~Removing the Meteorite separates it from the machine's energy arrangement.|
N~Keep it secure. That machine has had enough access to it.|
N~I'm glad it's out of there. It feels easier to breathe around the machine now.|
N~A valuable object is better packed safely than left in that contraption.|
S~The Meteorite has resigned from a disastrous position. Effective immediately.|
N~A rock with fewer alarming responsibilities. An improvement.|
N~Now the machine can't keep using that component. That's a concrete change.|
N~The fallen stone is separate from the thing that wanted to use it.|
N~Safely put away is a much better look for that Meteorite.|
N~I'd remember where it came from. The rock has already had a complicated journey.
''')

add('frontier_records_one', 'BattleFrontier_RankingHall_Text_DomePikeFactoryRecords', 'A Ranking Hall sign identifies Dome, Pike and Factory records.', '''
S~Three facilities' records in one place. A concentrated supply of impressive numbers.|
N~The heading distinguishes these facilities' records from the other displays.|
N~Dome, Pike, Factory. Good to know which results we're comparing.|
N~A clear label makes it easier to take time with each set of results.|
S~Three different challenges, and room to remember the people who did well.|
S~A small sign announcing a rather large collection of hard-earned bragging rights.|
N~An index to other people's exceptional afternoons.|
N~Keeping the facility names visible prevents very misleading comparisons.|
N~Different paths have left their numbers together here.|
N~A clear heading gives a busy display some order.|
S~I'd be interested in which of the three draws the longest look from visitors.
''')

add('frontier_records_two', 'BattleFrontier_RankingHall_Text_PalaceArenaPyramidRecords', 'A Ranking Hall sign identifies Palace, Arena and Pyramid records.', '''
U~Palace, Arena, Pyramid. Those names make a records board sound like an enormous holiday.|
N~Another group of facility-specific results. The distinctions matter when reading the records.|
N~Three challenges with their own records. Treat each on its own terms.|
N~It's easier to appreciate the numbers when you know which challenge produced them.|
S~Different kinds of effort all get their own place on the board.|
S~Three grand names sheltering some very determined competitors' results.|
N~Palace, Arena, Pyramid. An unusually architectural collection of accomplishments.|
N~The grouping gives the record display a sensible structure. Now we can inspect the details.|
N~Each place leaves a different mark on the people who pass through it.|
N~Matching headings make the hall feel considered rather than crowded.|
S~I'd ask a visitor which facility name means the most to them, and why.
''')

add('safari_rest_sign', 'SafariZone_Southwest_Text_RestHouseSign', 'A Safari Zone sign directs tired visitors to the Rest House.', '''
S~A sign that understands feet. Finally, representation for the bottom of the expedition.|
S~A rest stop is most useful when visitors can find it before they're exhausted.|
S~Good place to stop before tired feet turn into a bad decision.|
S~It's reassuring when a place gives you permission to slow down.|
S~Rest first. Exploring is much more enjoyable when every step isn't an argument.|
S~The invitation lacks grandeur but possesses excellent timing.|
S~A building advertised through fatigue. An audience I understand.|
N~Putting the rest sign where people are walking is a small but useful choice.|
S~Even an exciting place needs somewhere to be still.|
S~A welcome that starts with people's comfort. That's good hospitality.|
S~A rest stop is also where people finally have time to tell you what they've seen.
''')

add('verdanturf_tent_sign', 'VerdanturfTown_Text_BattleTentSign', 'Verdanturf Battle Tent sign invites visitors to enjoy watching battles.', '''
S~A feast for the eyes. Mine were expecting sandwiches, but they'll adjust.|
N~The sign emphasizes the spectacle of the battles rather than their particular rules.|
S~An invitation to look around. We'll learn the rules before joining anything.|
S~Watching first might make the place feel less overwhelming.|
L~A feast for the eyes is fine. I'll still want an actual meal afterward.|
S~The sign offers spectacle with the confidence of someone who knows their audience.|
N~A feast requiring no plates. Convenient cleanup.|
N~It gets attention. The practical details will need a separate look inside.|
N~A canvas building holding many people's brief, fierce moments.|
S~It's a vivid promise for a small sign. A little excitement suits the tent.|
S~I'd ask spectators which moment made them glad they stopped to watch.
''')

add('tunnel_cancelled_sign', 'VerdanturfTown_Text_RusturfTunnelSign', 'A sign records the cancelled tunnel project between Rustboro and Verdanturf.', '''
N~A sign for a road that didn't turn out as planned. Even signs can have awkward histories.|
N~The cancellation notice records the project's status, not necessarily everything that happened afterward.|
N~Plans on a sign can fall behind what people actually do. Check the way itself.|
N~A cancelled project still leaves something behind. Even if it's only a sign.|
N~A promised shortcut matters to the people at both ends. I'd want to hear their side.|
N~The sign preserves the official ending. Roads are less tidy than official endings.|
N~A monument to a plan encountering reality. A familiar architectural genre.|
N~I'd want to know what stopped the project before judging the people who worked on it.|
N~Two town names remain linked here, even in a notice of cancellation.|
N~The wording tells us what was decided. It doesn't tell us how everyone felt about it.|
N~I'd ask a local what they remember about the project. A notice can only hold so much.
''')

add('cycling_record', 'Route110_Text_BestRecord', 'A sign displays the recorded Cycling Road collision count and elapsed time.', '''
S~Speed and collisions on the same board. A useful reminder that fences count too.|
N~Time and collision count measure different aspects of a ride. Both deserve attention.|
N~Fast is good. Fast without hitting things is better.|
N~I like that it remembers more than the clock. A smooth ride matters too.|
S~A little care around the turns belongs beside the speed.|
S~The record includes both the sprint and its less graceful punctuation.|
N~A public collision count. The road refuses to let dignity obscure the data.|
N~Two measurements give us a clearer target than time alone.|
N~The ride is gone, but its haste and bumps have left a small trace.|
N~A good result should look smooth as well as quick.|
S~I'd ask the rider which stretch cost them the most concentration.
''')

add('cycling_no_record', 'Route110_Text_ThereIsNoRecord', 'The Cycling Road board has no recorded challenge result.', '''
U~No record yet! The board is having a very patient first day.|
N~An empty record offers no baseline for comparison. The first completed result would establish one.|
N~No result to beat yet. Still worth riding carefully.|
N~An empty board feels less intimidating. It hasn't started comparing anyone yet.|
S~Someone has to be first. They might as well enjoy the ride.|
S~A vacant place in local sporting history. Currently accepting applicants.|
N~No record, no embarrassing collision count. An unusually peaceful scoreboard.|
N~The first result will give future riders something concrete to compare against.|
N~A space is waiting for a journey to leave its numbers.|
N~A blank display needs one clear result before it can tell much of a story.|
S~It would be interesting to hear from whoever first decides to put a result here.
''')

add('meteorite_left', 'MtChimney_Text_PlayerLeftMeteorite', 'The player leaves the Meteorite in the machine after declining removal.', '''
N~The rock stays put. It has not, however, become any less suspicious-looking.|
N~Leaving the component in place preserves the current arrangement. We can reconsider later.|
N~Left it alone for now. Keep track of where it is.|
N~I don't quite trust that machine, even when we're only looking at it.|
N~No need to pretend we've packed something that's still sitting right there.|
N~The Meteorite retains its questionable accommodation for another visit.|
N~An ominous object left exactly where we found it. At least the inventory is simple.|
N~We haven't changed the machine's components. I'd remember that distinction.|
N~The stone waits where someone fitted it. The choice remains beside it.|
N~Leaving it in place is easy to see. Understanding the machine is another matter.|
N~I'd remember this spot if we decide to come back for a closer look.
''')

add('machine_inert', 'MtChimney_Text_MachineMakesNoResponse', 'The mysterious mountain machine gives no response.', '''
N~No response. A pleasant change from mysterious machines doing far too much.|
N~Lack of response tells us its current behavior, not the full state of every component.|
N~Quiet is good. Let's leave it that way.|
S~I prefer it silent. This is one mystery I don't need to hear humming.|
N~A machine that isn't asking anything of us. Fine place to stop investigating.|
N~The contraption declines to provide a dramatic development. Thank you, contraption.|
S~Unresponsive machinery. For once, that feels like a favorable report.|
N~No output to observe. I'd avoid treating that as an invitation to start pressing things.|
N~Whatever stirred in it isn't answering now.|
N~The absence of a response is enough information for this visit.|
N~An inactive machine can still have a history. We don't need to restart it to acknowledge that.
''')

add('machine_meteorite', 'MtChimney_Text_MeteoriteFittedOnMachine', 'A mysterious machine appears to store energy in its fitted Meteorite.', '''
U~A space rock attached to a mountain machine. Someone has very alarming hobbies.|
N~The visible description suggests energy storage, though it doesn't explain the mechanism.|
N~Leave the controls alone. We don't know what they're connected to.|
N~That doesn't look like a harmless display. I'd keep a little distance.|
N~Something storing energy on a volcano deserves more caution than curiosity.|
N~A mysterious machine and a Meteorite. The arrangement hardly inspires domestic confidence.|
N~A rock has been given a position of alarming technical importance.|
U~I'd want a diagram and a safe way to measure it before making any claims about that system.|
N~A fallen thing is being asked to hold something that isn't still.|
N~Whatever the design is meant to do, it hasn't made its purpose welcoming.|
N~I'd ask who built it before trusting anyone's account of what it can safely do.
''')

add('lanette_notes_closed', 'Route114_LanettesHouse_Text_ClosedTheNotebook', 'The player closes Lanette research notebook without continuing to its next page.', '''
S~Notebook closed. The next page will have to keep its clever thoughts to itself for now.|
N~We've stopped reading here. The remaining notes shouldn't be mistaken for something we've reviewed.|
N~Leave the notes tidy. They're still someone else's work.|
N~We can close it without pretending we've understood everything in it.|
S~Back where it belongs. Research notes are easy enough to lose under ordinary clutter.|
S~A brief reading ends with a neatly closed cover. Perfectly respectable pacing.|
N~The notebook has returned to being mysterious on the outside.|
N~Stopping here leaves the rest available for a more focused look another time.|
N~The unwritten part of our visit stays between its closed pages.|
S~A clean place to pause. No need to leave somebody's notebook sprawled open.|
N~If a question comes up later, we'll know where the notes are.
''')

add('lanette_last_box', 'Route114_LanettesHouse_Text_ResearchNotesPage3', 'Lanette notes explain sending stored Pokemon to the last inspected Box or the next available one.', '''
S~The last Box you looked at gets the next arrival. A surprisingly attentive little filing system.|
S~The system uses the last inspected Box as the current destination, with overflow to the next.|
N~Check the Box you want first. Saves searching for the arrival afterward.|
N~That explains why looking at a Box matters even without moving anything.|
S~A chosen place first, then the next if it's full. Easy enough to remember.|
S~A quiet administrative decision happens the moment someone looks inside a Box.|
N~Inspection counts as selection. A detail with excellent potential to confuse the unwarned.|
S~Using the last inspected Box as a default saves an extra selection. Good to document it.|
N~The place you last considered becomes the next place something arrives.|
N~A useful default becomes much friendlier when someone explains it clearly.|
N~I'd point this out to anyone who keeps wondering where a newly stored Pokemon went.
''')

add('cabin_one', 'SSTidalCorridor_Text_Cabin1', 'The ship corridor sign identifies Cabin 1.', '''
S~Cabin one. An excellent number to start the cabin collection with.|
N~A simple number is sufficient identification when the corridor follows a clear order.|
N~Cabin one. Easy enough to remember if we need the way back.|
N~A little number makes an unfamiliar corridor less confusing.|
S~Useful sign. No wandering into the wrong doorway to ask where we are.|
S~The first cabin receives a suitably economical introduction.|
N~One. A door label refreshingly free of nautical riddles.|
N~Clear numbering is one of those small details a busy corridor needs.|
N~A small marker divides this stretch of ship from the next.|
N~Plain lettering is right for a cabin sign. Finding the door comes first.|
N~I'd remember the number before getting distracted by everything else aboard.
''')

add('cabin_two', 'SSTidalCorridor_Text_Cabin2', 'The ship corridor sign identifies Cabin 2.', '''
S~Cabin two! The numbering system remains reassuringly undefeated.|
N~The next numbered cabin. Consistency makes navigation easier on an unfamiliar ship.|
N~Cabin two. Mark the number before choosing a door.|
N~The corridor feels easier to follow once you notice the numbers.|
S~A number worth remembering. Much easier than describing which identical door we meant.|
S~Cabin two makes its presence known without demanding a speech.|
N~Two. The sign has resisted the temptation to overcomplicate things.|
N~Repeating the same clear format keeps the whole corridor readable.|
N~Another small address traveling across a very large sea.|
N~The right number in the right place. Sometimes design should be this straightforward.|
N~I'd check the sign twice before confidently knocking on the wrong cabin.
''')

add('cabin_three', 'SSTidalCorridor_Text_Cabin3', 'The ship corridor sign identifies Cabin 3.', '''
S~Cabin three. I'm glad the ship isn't making us solve a puzzle to find the doors.|
N~Numbered doors provide stable references even while the vessel itself is moving.|
N~Third cabin. Now we've got another landmark in the corridor.|
N~It's a small sign, but it gives you somewhere definite to be.|
N~Remember the number and nobody needs to hear a long story about which door.|
S~Cabin three, announced with the confidence of a place that knows its own address.|
N~Three. An entire identity delivered in one very manageable number.|
N~A clear local reference is useful when the outside view doesn't stay put.|
N~The number stays steady while the water passes outside.|
N~No flourish needed. A door number has a practical job.|
N~I'd use this sign as a reference if someone needed directions through the ship.
''')

add('cabin_four', 'SSTidalCorridor_Text_Cabin4', 'The ship corridor sign identifies Cabin 4.', '''
S~Cabin four. Four useful numbers, and I haven't had to name a single door myself.|
N~The label completes another clear reference point in the cabin corridor.|
N~Cabin four. Good, we've kept our bearings.|
N~A familiar number is enough to make the corridor feel less anonymous.|
S~Now if anyone says cabin four, we won't have to open every door to find it.|
S~The fourth cabin preserves the corridor's admirably restrained naming policy.|
N~Four. I appreciate a sign that finishes before I lose my place.|
N~Consistent door labels make giving directions much simpler.|
N~One little numeral holds a place apart from all the others.|
N~A readable sign earns its space without needing to decorate the whole door.|
N~It's worth noticing these signs before the conversation aboard gets distracting.
''')

add('weather_bed', 'Route119_WeatherInstitute_1F_Text_TakeRestInBed', 'The Weather Institute bed interaction provides a completed party rest.', '''
S~A proper rest indoors. Rain may continue its performance without us for a bit.|
S~A recovery stop here is practical, especially with the long wet route outside.|
S~Good stop. Better to continue rested than prove we can stay tired.|
S~A quiet bed feels especially welcome with all that weather outside.|
S~Rested up. Even a busy institute has room for a sensible pause.|
S~A short intermission beneath a reliably dry roof. Excellent accommodation.|
S~A bed at a weather institute. Research has finally produced something immediately restful.|
S~Keeping a rest space beside the working rooms makes this a very useful stop.|
S~For a little while, the rain belongs to the other side of the wall.|
S~Dry shelter and a chance to recover. Nothing needs improving on that combination.|
S~A rest stop changes how the next stretch feels. We can notice more when we're less tired.
''')

add('lilycove_harbor', 'LilycoveCity_Text_HarborSign', 'Lilycove Harbor sign advertises S.S. Tidal cruises.', '''
S~A delightful cruise, says the sign. I'm choosing to believe the sea signed off on that.|
N~The harbor sign identifies the ferry service. Sailing details will require a separate check.|
S~There's our harbor. Worth asking where the ferry's headed before boarding.|
S~A cruise sounds peaceful from here, with both feet still on the ground.|
S~A seat, a sea breeze, and time to enjoy the crossing. That is an appealing promise.|
S~The harbor has compressed the romance of travel into one cheerful invitation.|
N~Delightful is doing some optimistic work on behalf of the ocean.|
S~A ferry turns a long stretch of water into a practical connection between places.|
S~The sign invites us to leave land behind for a little while.|
S~A pleasant promise belongs at a harbor. So do clear boarding directions.|
S~I'd ask returning passengers which part of the crossing they enjoyed most.
''')

add('lilycove_museum_sign', 'LilycoveCity_Text_MuseumSign', 'Lilycove Museum sign advertises its Pokemon masterpiece collection.', '''
U~A whole collection of masterpieces! The ordinary pictures must feel very outnumbered.|
S~The sign identifies both the collection's subject and its artistic emphasis.|
S~Good place to slow down and look at something properly.|
S~I'd like to see which pictures make people stop for a little longer.|
S~A quiet look around sounds good. There's no need to hurry past someone's work.|
S~Masterpieces await inside. The sign has sensibly delegated the evidence to the paintings.|
S~A building full of pictures is a reasonable excuse to avoid a crowded afternoon.|
S~I'd enjoy comparing how different artists approach the same kind of subject.|
S~Many ways of seeing Pokemon have found shelter in one place.|
U~I'd like to look at how the collection is arranged as well as the individual works.|
S~I'd ask a regular visitor which piece keeps bringing them back.
''')

add('home_name_sign', 'LittlerootTown_Text_PlayersHouse', 'The sign identifies the player home by name.', '''
S~Your name on a house. Very official. The doormat must be proud.|
S~A simple name makes the house easy for visitors to identify.|
S~Home. Nice to see a sign that doesn't need further directions.|
S~Seeing your name there makes the place feel more settled.|
S~A house is easier to find when the welcome starts outside.|
S~A modest plaque granting you a starring role in local postal geography.|
S~A useful sign for anyone whose directions end with asking a stranger.|
S~Clear identification. The smallest useful piece of a town's navigation system.|
S~A name gives the doorway a particular kind of belonging.|
S~Personal without being elaborate. A house sign doesn't need much more.|
S~It must feel different reading your own name there than anyone else's.
''')

add('birch_home_sign', 'LittlerootTown_Text_ProfBirchsHouse', 'A sign identifies Professor Birch home.', '''
S~Professor Birch's house. Useful distinction from wherever he has wandered off to study something.|
S~The house is clearly identified. A researcher's home and workplace needn't be the same address.|
N~Birch's home. Worth remembering before going to the wrong building to find him.|
N~A plain house sign makes a professor seem a little less distant.|
S~Even a busy professor has somewhere to come home at the end of the day.|
S~An academic title attached to an ordinary front door. A pleasantly grounded introduction.|
N~The professor has a house. Evidence that fieldwork occasionally pauses.|
N~A clear sign prevents visitors from mistaking the home for the lab.|
N~The name outside belongs to someone with a life inside.|
N~A proper nameplate is helpful when half a town seems to know the same person.|
N~I'd ask a local which building they mean before assuming every Birch errand leads here.
''')

add('running_manual', 'PlayersHouse_1F_Text_RunningShoesManual', 'The Running Shoes booklet explains holding B to run in them.', '''
L~Shoes with instructions! Mine usually settle for suggesting which end the toes go in.|
S~A short manual for a frequently used action. It sensibly avoids unnecessary complication.|
N~Lace them properly before trying the fast part.|
S~It's nice having the instructions nearby. Asking again can feel awkward.|
S~Good laces first, running second. Saves an embarrassing argument with the ground.|
L~The booklet introduces running with the enthusiasm of a shoe salesman late for lunch.|
N~A manual short enough to read before the urge to sit down wins.|
S~One clear instruction and the basic safety of lacing up. Efficient documentation.|
S~A pair of shoes can make the road feel a little more inviting.|
N~Useful shoes still need a proper fit. Speed won't improve a loose lace.|
S~I'd want to try a short stretch first, just to get used to the difference.
''')

add('school_email', 'gText_PokemonTrainerSchoolEmail', 'An email from Pokemon Trainer School explains the four-move limit and choosing movesets.', '''
U~Four moves! That makes choosing harder than remembering which pocket has my snacks.|
N~A four-move limit makes selection a problem of coverage, specialization, and trade-offs.|
N~Choose moves that work together. Four strong choices can still leave a gap.|
N~Leaving something out can be harder than choosing what to keep.|
S~Four places on the menu. Each one should have a reason to be there.|
N~The limit gives every choice weight. Even the omitted move gets a little influence.|
N~Only four moves. A useful defense against decisions becoming literally endless.|
N~I'd check what each move contributes before replacing anything. Overlap can hide a missing option.|
N~A few chosen actions can take a Pokemon in many directions.|
N~A coherent set often does more than four impressive pieces thrown together.|
S~I'd ask a trainer which move they kept changing their mind about, and why.
''')

add('coin_case_required', 'MauvilleCity_GameCorner_Text_CantPlayWithNoCoinCase', 'A Game Corner machine cannot be played without a Coin Case.', '''
N~No Coin Case, no game. The machine has very specific ideas about pockets.|
N~The required container is missing. The machine can't be used in this state.|
N~Need the case first. No point feeding the machine hopeful looks.|
N~At least it tells us what's missing instead of leaving us guessing.|
S~A clear answer. We can leave this machine alone for now.|
N~Entry has been denied on a technicality involving personal storage.|
N~The machine demands a particular sort of preparedness. We do not possess it.|
N~A requirement stated plainly saves a lot of fruitless button pressing.|
N~The bright machine has one quiet condition we haven't met.|
N~Useful to learn that before settling in front of it.|
N~I'd ask about the case rather than keep trying the same machine.
''')

add('trick_scroll', 'Route110_TrickHouseEntrance_Text_ItsAScroll', 'The Trick House entrance object is simply described as a scroll in this state.', '''
N~A scroll. In this house, that feels like a suspiciously short explanation.|
N~The visible description establishes only that it's a scroll. No further mechanism is revealed here.|
N~Just a scroll for now. Don't assume every object is ready to do something.|
N~It's strange how an ordinary scroll can feel less ordinary in this house.|
N~A scroll isn't much to go on. We can leave it at that for the moment.|
S~A scroll with an admirably restrained introduction, considering its surroundings.|
N~The scroll refuses to elaborate. I understand the impulse.|
N~No additional function is apparent in this state. Observation before experimentation.|
N~Rolled paper can keep a great deal out of sight.|
N~Simple description. The setting supplies quite enough extra speculation.|
N~I'd remember how it looks now before deciding later that it has changed.
''')

add('trick_departure_note', 'Route110_TrickHouseEntrance_Text_LeavingOnJourneyNote', 'The Trick Master note says he has left on a journey and asks not to be sought.', '''
N~He's gone on a journey and left us a note instead of a puzzle. A surprisingly direct trick.|
N~The note states his departure but gives no destination. We shouldn't infer one.|
N~He asked not to be followed. Fair enough.|
S~Leaving a note is kind. It saves someone waiting without knowing.|
S~Everyone gets to head out sometimes. Even the person who builds reasons for others to visit.|
S~An exit note with no riddle attached. Perhaps that's his final surprise for the room.|
N~A request not to search. Remarkably clear for this particular household.|
N~No destination or return date supplied. The only clear instruction is to leave him to it.|
S~Someone who made paths for visitors has taken one of his own.|
N~A plain note can say enough. He seems quite definite about this.|
S~I'd be curious about his journey, but curiosity doesn't require following him.
''')

add('shoal_salt_empty', 'ShoalCave_Text_WasShoalSaltNowNothing', 'A formerly occupied Shoal Salt spot is empty.', '''
N~Salt was here, salt is not here. The cave has delivered a very concise report.|
N~The source is empty at present. That observation doesn't establish its future availability.|
N~Nothing left at this spot. Move on rather than keep searching it.|
N~An empty patch still tells you what used to be there.|
N~No salt to collect here now. At least we checked before promising any.|
N~A former salt deposit has become a short lesson in absence.|
N~The salt has left no forwarding address.|
N~Empty location confirmed. Rechecking it immediately won't add useful information.|
N~A little place remembers what the tide once left there.|
N~The empty space is the important detail this time.|
N~I'd note that it's empty now rather than assume we missed something obvious.
''')

add('shoal_shell_empty', 'ShoalCave_Text_WasShoallShellNowNothing', 'A formerly occupied Shoal Shell spot is empty.', '''
N~A shell used to be here. Now it's a very small exhibition of no shell.|
N~The spot is currently empty. We have no shell to identify or collect from it.|
N~No shell here now. Keep an eye on the footing as we move on.|
N~It feels odd knowing exactly what an empty place is missing.|
N~Nothing to pack from this spot. That keeps the count honest.|
N~The shell's former location has outlasted its appearance in the scene.|
N~An absent shell. Less attractive than a shell, but considerably lighter to carry.|
N~One empty collection point. Better to record that clearly than search it in circles.|
N~The shape of a place can remain after its small occupant leaves.|
N~No shell to admire here at the moment. The cave has other details to look at.|
N~I'd compare what this spot looks like another time before drawing any conclusions.
''')

add('slateport_harbor', 'SlateportCity_Text_HarborSign', 'Slateport Harbor sign advertises S.S. Tidal cruises.', '''
S~The S.S. Tidal has a proper invitation here. Very polite for such a large boat.|
N~A harbor notice for the ferry service. It doesn't specify the current sailing conditions.|
N~Harbor's here. Next step is checking the actual route.|
S~The invitation makes the water feel like a way somewhere, rather than an edge.|
S~A cruise sounds like a pleasant change from walking every mile ourselves.|
S~The sign sells a delightful crossing while the harbor handles the practical business.|
N~A cheerful invitation to trust a very large quantity of water.|
S~A regular ferry gives a busy port another useful connection.|
S~A name on the sign turns the sea into a possible road.|
N~Clear harbor identification first, a little charm second. Sensible order.|
S~I'd ask someone arriving here how different Slateport looks from the water.
''')

add('shipyard_building', 'SlateportCity_Text_SternsShipyardNearsCompletion', 'The shipyard notice says S.S. Tidal construction is nearly complete for the two ports.', '''
U~Nearly a ferry! That's a lot of work hiding inside one small word.|
N~The notice describes the project as nearing completion, not already operating.|
N~Nearly finished still means work left. Let the builders do it properly.|
S~It must be exciting to see something this big getting close to ready.|
S~Almost done is when you check the details, even if everyone is eager to begin.|
S~The shipyard announces an approaching debut while wisely leaving the curtain down.|
N~Nearly complete. A phrase that can contain several extremely important bolts.|
U~I'd love to see which finishing tasks remain before a ferry is ready for passengers.|
N~Two ports are waiting for a road that still has to be built.|
S~A clear progress notice gives people a reason to look forward without promising too much.|
S~I'd ask a worker which part of seeing the finished ship they're most looking forward to.
''')

add('shipyard_boarding', 'SlateportCity_Text_SternsShipyardFerryComplete', 'The shipyard directs S.S. Tidal passengers to board at the harbor.', '''
S~The shipyard builds it; the harbor lets us on. Good to sort that out before waving at cranes.|
N~The notice distinguishes construction facilities from the passenger boarding location.|
N~Board at the harbor. Saves asking the shipwrights for a seat.|
N~I'm glad the sign says where to go. It's easy to feel in the way at a working yard.|
S~Useful directions. Passengers can find the boat without interrupting everyone building things.|
S~The shipyard politely redirects anyone who mistakes the workshop for the departure lounge.|
N~Boarding elsewhere. The workers have escaped becoming an information desk by accident.|
S~A simple routing notice prevents pedestrians from wandering through a working site.|
N~The place where a journey is built isn't always where it begins.|
S~Practical signs spare both visitors and staff a repeated awkward conversation.|
N~I'd pass that direction along if we saw anyone else waiting at the wrong entrance.
''')
