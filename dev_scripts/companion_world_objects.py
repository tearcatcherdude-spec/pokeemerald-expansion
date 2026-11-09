"""Whole-game shared-object replies; exact observed descriptions, eleven voices.

This is part of the full expansion, not a separate pilot or release. These
bindings apply wherever the real object script is used in either region.
"""
ROWS=[]
def add(key,labels,subject,lines):
    replies=[v.strip() for v in lines.strip().split('|')]
    assert len(replies)==11,(key,len(replies))
    ROWS.append(dict(key=key,labels=labels.split(),subject=subject,replies=replies))

add('general_books','Text_BookShelf','A bookshelf contains books on many subjects.','''
All sorts of books. I could become informed about several things before lunch. One thing, realistically.|
Different subjects together. I like a shelf that lets one question lead somewhere unexpected.|
A lot of books. We can browse without pretending we understand every spine.|
All sorts of books. A whole room of people saying things without having to raise their voices.|
I would check for recipes. Not every mystery requires me to develop a new personality.|
Somewhere on that shelf is an author who thought their first draft was hopeless. Comforting company.|
Books on every subject. My collection has narrowed to poetry and things I was using as bookmarks.|
I would like to read the manuals before touching the machinery. A developing habit.|
Different subjects can disagree on a shelf without anyone being thrown out. People might try that.|
I like useful books beside beautiful ones. Some manage both without announcing the achievement.|
A shelf is a little map of someone's interests. We are only seeing the spines.
''')
add('pokemon_reference_books','Text_Bookshelf','A shelf is crammed with Pokemon books.','''
Pokemon books all the way along. Somebody has been doing the reading I hoped the pictures would cover.|
Pokemon references. I would compare editions; one old mistake can become very well cited.|
Books about Pokemon. Useful preparation, provided we still notice the actual Pokemon in front of us.|
I wonder if any discuss their calls. Written music never quite captures what a living voice does.|
I would look up feeding advice. A surprisingly large part of friendship involves knowing who can eat what.|
A whole shelf of Pokemon studies. More convincing research than announcing a discovery before opening a book.|
Pokemon books. Twelve volumes and not one explaining why my team stares when I practise a reading.|
Species guides first. I would prefer to learn which Pokemon dislikes sparks before demonstrating sparks.|
I would read the field notes as well as the conclusions. The unanswered questions tell us something, too.|
Someone has collected a great deal about Pokemon. I hope the care chapters are as well used as the pictures.|
I like comparing the illustrations with the real creature. An artist notices some things and misses others.
''')
add('shop_stock','Text_ShopShelf Text_PokeMartShelf','Shop shelves are stocked with Pokemon merchandise.','''
All those supplies. I came in for one thing and can already feel myself forgetting which thing.|
Stocked shelves are reassuring. A list would help us distinguish preparation from an expensive mood.|
Buy what we will use. The team cannot hold a brave-looking receipt.|
Everything arranged to catch the eye. I should check the price before falling in love with the packaging.|
Supplies first. Snacks are supplies, but I accept that they are not the only supplies.|
Excellent display. I am trying to remember that being persuaded is not the same as needing the prop.|
The shelves promise adventure. The prices would like a private conversation with my wallet.|
Before buying the impressive tool, check which problem it solves. Yes, I am speaking to myself.|
There is comfort in finding supplies on a long trip. We need not carry the entire shop to appreciate it.|
Good packaging tells us what is inside. The decorative shine can wait until after that part.|
Look how the bright labels pull us toward the shelf. Someone planned that little journey very carefully.
''')
add('blueprint_plans','Text_Blueprint Text_Blueprints','An intricate blueprint is covered in plans or diagrams.','''
A blueprint. I can identify the paper confidently. The rest deserves someone with training.|
Plans are useful, but I would want the legend before claiming to understand those marks.|
A lot of detail. Ask the person who drew it before deciding a line means optional wall.|
It is rather like a score. A useful set of instructions, not proof the performance will go to plan.|
My recipes also look mysterious without the measurements. We should leave the original where its owner expects it.|
The plan before the finished thing. There is always much more work here than an audience sees.|
A complicated blueprint. My drafts have arrows too, but mostly pointing at the word no.|
I would start with the labels and measurements. Knowing how to read a plan includes knowing what to ask.|
A drawing of something intended. It interests me how much hope can be disguised as a straight line.|
A pattern needs clear instructions. An attractive diagram can still leave the maker with difficult questions.|
Someone worked out the shape before making it real. I would like to see which parts changed along the way.
''')
add('plates_arranged','Text_DishesPlatesNeatlyLinedUp','Dishes and plates are neatly arranged.','''
All the plates lined up. My cupboard relies on a system called shut the door gently.|
The arrangement makes each piece easy to find. A small practical kindness for whoever sets the table.|
Neat dishes. Let us leave them neat. That is the entire assignment.|
The plates are ready before anyone arrives. I like that quiet part of preparing for company.|
Clean plates within reach. A kitchen can look simple when someone has already done the work.|
The tableware is ready for its entrance. Unlike certain actors, it is not asking where to stand.|
Every plate in its place. My desk has refused to attend this discussion.|
Stable stacks, reachable shelves. I appreciate engineering that does not introduce itself as engineering.|
Someone expects there will be people to feed. Ordinary preparations can be rather hopeful.|
An arrangement made for use. It can be pleasing without making someone afraid to touch a plate.|
All those repeated shapes, and the room feels settled. Someone found a rhythm for the cupboard.
''')
add('cooking_smell','Text_Kitchen','Someone has been cooking; the kitchen smells delicious.','''
Something smells wonderful. I am practising admiring a kitchen without inviting myself to dinner.|
Cooking has left a pleasant clue. We can enjoy it without treating someone else's kitchen as a sample station.|
Smells good. Ask before helping yourself. A revolutionary dining strategy.|
Someone has been cooking. A room can feel welcoming before anyone says a word.|
I would like to ask what they made. Ask is the important ingredient in that sentence.|
The kitchen has made an excellent entrance without leaving its room. I respect that.|
That smells like a poem someone can actually eat. An unfair advantage over my work.|
Very good aroma. I shall not ask how the oven works until after asking about the food.|
A cooking smell can make a place feel lived in. No grand history required.|
Good food smells wonderful before anyone arranges it for a picture. Comfort has excellent taste.|
You can almost see the room becoming warmer when you notice the cooking. I wish I could sketch a smell.
''')
add('sturdy_dresser','Text_Dresser','A well-made dresser has plenty of storage.','''
A nicely made dresser. It can hold a lot of things. None of them need to become our things.|
Plenty of storage, and it looks well made. We can inspect the craftsmanship without inspecting someone's belongings.|
Sturdy dresser. The drawers still belong to whoever lives here.|
Enough room for folded clothes and all the socks that have lost their duet partner.|
A good dresser keeps things where you expect them. My flour apron would benefit from that certainty.|
A generous wardrobe. I shall admire the furniture without volunteering to reorganise its cast.|
A handsome dresser. An excellent place for an owner to put things we do not need to investigate.|
I like a drawer that opens cleanly and stays on its runners. Very underrated technical achievement.|
A place to keep ordinary belongings safe. We do not need to make a mystery out of closed drawers.|
Storage that works is a kindness. Clothing deserves somewhere better than the chair-shaped mountain in my room.|
Good woodwork. Somebody thought about how this would feel to use, not only how it would look.
''')
add('snack_pile','Text_Snacks','There is a pile of snacks.','''
A pile of snacks. I shall demonstrate tremendous character by remembering whose house this is.|
A well-stocked snack supply. Our findings do not require opening the packets.|
Snacks. Belonging to someone. We have successfully identified both important facts.|
A whole pile of snacks. I am trying to make my stomach's response sound like background music.|
Those are very promising provisions. I can admire them without pretending we have been invited to a tasting.|
A generous selection of props for a picnic scene. We have not been cast in it yet.|
A pile of snacks. My attention has found a subject it can sustain.|
Ready-to-eat supplies. No assembly required. I am bravely resisting the urge to improve that.|
Someone has made sure there will be something to eat. We can leave that reassurance intact.|
Snacks within reach. An excellent arrangement, provided the person reaching is meant to be here.|
All those packets make a very persuasive little still life. We should leave the composition complete.
''')
add('mart_service_sign','Text_PokemartSign gText_PokemartSign','A Mart sign advertises item supplies.','''
The MART. A very useful building that still does not sell sandwiches.|
A useful place to restock. We should check what we need before asking the sign to decide for us.|
MART supplies. We can go in, buy what the team needs, and avoid making it a financial adventure.|
The sign knows its part: tell travellers where the supplies are. A short, successful performance.|
Item supplies here. I would still check our bag before buying another thing we already packed.|
A clear invitation to a shop. Much better than a mysterious slogan with no opening hours.|
All our item needs, apparently. I shall not embarrass anyone by asking for a completed poem.|
Supplies, clearly labelled. Good signs prevent people from wandering into the wrong workshop.|
A place to replace what the road used up. A little preparation can make the next stretch gentler.|
A supply shop should be easy to recognise. This sign has understood the assignment.|
The sign gives the building a purpose you can see from the street. Practical lettering deserves some credit.
''')
add('center_service_sign','Text_PokecenterSign gText_PokemonCenterSign','A Center sign offers Pokemon healing.','''
Pokemon healing here. A sign that does not need to oversell its benefits.|
A recovery point. Worth remembering before the team has to depend on it.|
Healing here. We can take care of the team before planning the next challenge.|
A place for the team to recover. The road can wait for a proper rest.|
Healing for our partners. We can sort out the provisions while they are being looked after.|
A reassuring announcement. Not every doorway needs a dramatic introduction.|
A sign promising care. I find its lack of dramatic metaphor deeply reassuring.|
Clear directions to proper care. Better than inventing a questionable solution beside the road.|
Someone arriving worried can read that and know where to go. Small signs matter.|
Healing should be easy to find. It is good to see the sign put function first.|
A familiar promise in a new town. The lettering makes the street feel a little less strange.
''')
add('packed_food','Text_Food','The container appears to hold plenty of food.','''
That looks well supplied. I admire someone who plans for the emergency of it being lunchtime.|
There seems to be plenty packed. We can appreciate the preparation without checking the contents ourselves.|
Food packed and ready. Someone thought ahead. Let us not become the flaw in their plan.|
Enough food for a proper break, by the look of it. The rest is as important as the travelling.|
A promising food supply. I appreciate a plan with provisions rather than inspirational speeches about hunger.|
Provisions prepared in advance. A production survives on rather more than dramatic confidence.|
Food, apparently well supplied. My stomach has submitted a favourable review from a distance.|
A practical reserve. Not everything needs a motor to count as good preparation.|
Someone has left a future meal waiting. It is a kind thing to do for your later self.|
Well-packed food deserves a bag that keeps it that way. A crushed lunch is a design failure I take personally.|
It looks ready for sharing when the owner chooses. We can admire it without joining the guest list uninvited.
''')
add('happy_pokemon_painting','Text_Painting','A picture shows a Pokemon looking happy.','''
That Pokemon looks happy in the picture. I hope it liked having its good side declared on paper.|
The artist caught an expression of ease. I wonder what helped the Pokemon feel comfortable.|
Looks happy. That matters more to me than whether it stood perfectly still.|
There is a nice feeling in that face. I like work that leaves someone looking relaxed.|
A contented Pokemon. I would like to know whether a snack was involved in the sitting. Professional curiosity.|
A good expression can make a picture feel alive. It need not be a grand pose.|
A Pokemon having a nice moment. Art has been allowed to enjoy itself.|
It looks comfortable. I appreciate a subject that has not been frightened into cooperating.|
A happy expression is worth remembering. Ordinary contentment belongs in pictures, too.|
The Pokemon looks at ease. A flattering portrait can begin with letting the subject be itself.|
Look at the expression. Whoever painted this paid attention to a small, lovely moment.
''')
add('unfamiliar_power_machine','Text_PowerPlantMachine','An unfamiliar power-plant machine should be left alone.','''
An unfamiliar machine. I shall contribute to public safety by not finding out what the large buttons do.|
We do not know its function. Observation first; touching an unfamiliar machine is not a research method.|
Leave it alone. Not knowing what it does is a good reason to keep our hands clear.|
I prefer a humming machine when someone can explain the hum. We can listen from here.|
Not kitchen equipment. Even if it were, I would still ask before turning it on.|
An impressive machine is not an invitation to improvise a demonstration. That lesson applies to stage equipment, too.|
An unfamiliar machine. At last, a mystery improved by our complete lack of interference.|
No labels we understand, no reason to touch it. Expertise includes resisting the interesting-looking switch.|
We can leave a question unanswered without putting our hands inside it.|
We do not know how it works. Looking confident beside it would not change that.|
The machine has a purpose somewhere beyond its appearance. We should leave that purpose to the people responsible for it.
''')
add('private_telephone','Text_Telephone','A telephone is available but should not be used by the visitor.','''
A telephone. I am not calling anyone from someone else's house to explain why I am in their house.|
A private telephone. Knowing how to use something is different from having permission.|
Leave the phone. Whoever owns it can decide who makes calls here.|
A telephone waiting quietly. We need not make it part of our afternoon's noise.|
If we need to call someone, we can ask. I recommend asking before ordering any emergency bread.|
A telephone. I have enough difficulty with my own calls without borrowing somebody else's audience.|
A telephone. We could contact anyone willing to ask why we are using this telephone.|
Useful equipment, someone else's line. I shall not investigate the wiring either.|
A voice can cross a long distance through that. We can respect the person who pays for the connection.|
A private phone. Access to a room does not make every object in it ours to use.|
Someone could be waiting for a call. We can leave the line and the room as we found them.
''')
add('complicated_computer','Text_Computer','A computer displays complicated words and numbers.','''
The screen is full of complicated things. I understand the part where we stop poking it.|
We lack the context for those numbers. A screen full of detail is not an explanation by itself.|
Someone else's work. We can admit it is complicated and leave it intact.|
A lot of words and numbers. I know the feeling of showing someone a score without teaching them the notation.|
That is beyond my recipe notes. I shall admire the desk rather than offer a confident guess.|
An impressive-looking screen. I refuse to perform understanding I do not actually possess.|
Words and numbers together. The computer is trying two separate methods of intimidating me.|
I would want the documentation before changing anything. Especially when the current work belongs to someone else.|
There is a person who knows what those numbers are for. We can ask instead of making the mystery larger.|
Complicated information needs a clear explanation. Making someone feel foolish is not an interface feature.|
All that information, and we do not yet know how to read its shape. Looking longer is not always the same as understanding.
''')
add('product_poster','Text_AdvertisingPoster','A poster advertises several products.','''
A poster full of products. I am trying to remember what I wanted before the poster became involved.|
Advertising tells us what the seller wants noticed. We should still ask what we actually need.|
A lot of things for sale. Not all of them need to travel home with us.|
Someone chose those colours to make us stop. I can appreciate the arrangement without buying the chorus.|
If I bought everything that looked good on a poster, I would need a larger kitchen and a smaller sense of shame.|
An excellent pitch is still a pitch. I would like to know what the product does after the applause.|
The poster has discovered several urgent needs I did not have a minute ago.|
Every invention looks finished in an advertisement. I would like to see the instruction sheet.|
The poster offers a very tidy story about wanting something. Real people are usually less tidy.|
Attractive presentation. Now tell me whether the thing holds together when somebody uses it.|
The lettering guides the eye before we notice it happening. Clever work; still an advertisement.
''')
add('tasty_aroma','Text_TastyFood','The food smells good enough to make a stomach growl.','''
That smells excellent. If my stomach speaks first, please do not interpret it as an invitation we received.|
A persuasive aroma. We can notice it without making someone else's meal part of our research.|
Smells good. We can find our own lunch without disturbing this one.|
My stomach is considering a solo. I would prefer it waited for a quieter venue.|
That is a lovely smell. I would ask about the seasoning before asking for a taste. Priorities, apparently.|
The food has captured the audience without saying a word. A formidable competitor.|
The smell has reached my stomach, which has elected a rather loud spokesperson.|
That smells like a successful process. I am behaving well enough not to ask for every measurement immediately.|
A good smell can make a long day feel shorter. We should still leave the meal to its owner.|
That aroma needs no decorative garnish to make its argument. I respect an honest presentation.|
I cannot put the smell in a sketchbook. That seems like a serious limitation of my profession.
''')
add('pokemon_emblem_cup','Text_Cup','A cup is decorated with a Pokemon mark.','''
A Pokemon on the cup. It has secured a position in the beverage industry.|
A Pokemon mark makes this cup recognisable. We can admire it without testing the contents.|
Nice cup. I am leaving it where someone can find it again.|
A little Pokemon beside somebody's drink. A pleasant bit of company for a quiet morning.|
A decorated cup. The important question remains whether the drink has been allowed to go cold.|
A Pokemon has obtained a very small stage. Excellent view of the tea.|
A Pokemon on a cup. At last, an audience contract with a handle.|
A familiar mark on an everyday tool. Good design can make ordinary equipment feel personal.|
Someone chose a cup with that Pokemon on it. We do not know why; we can still notice the affection.|
A small decoration on something used every day. I like design that gets to live with its owner.|
The little mark changes the whole cup. A small picture does not have to do a small job.
''')
add('indicator_lights','Text_BlinkingLights','Different-coloured lights flash on and off.','''
The lights are blinking. I hope that means something more useful than looking busy.|
Different colours usually carry information. Without the key, we should not invent a reading.|
Flashing lights. We can leave the interpretation to someone who knows the equipment.|
There is a rhythm to the blinking. Enjoying it does not qualify me to adjust the machine.|
Colour-coded equipment. My kitchen signals an emergency by smelling unmistakably wrong.|
Very effective lighting. I would like to know whether this is the intended performance.|
The lights are saying something. I am choosing the dignity of not supplying a translation.|
Those colours need a legend before they become useful information. Blinking is not documentation.|
A pattern can feel meaningful before we understand it. We can wait for an explanation.|
Clear signals need more than attractive colours. I hope there are labels for the people using this.|
The colours move our attention in a little sequence. I would still ask what the sequence is meant to say.
''')
add('impressive_machine','Text_ImpressiveMachine','An unidentified machine looks impressive.','''
An impressive machine. My evaluation ends just before the part where someone asks what it does.|
Impressive appearance, unknown function. A perfectly reasonable point to stop and ask.|
Looks impressive. We do not need to touch it to prove we noticed.|
A very confident-looking machine. I wonder how much quiet work went into making it behave.|
Impressive. I have no evidence that it makes lunch, and will not be testing the theory.|
Excellent presence. I would still like the practical demonstration to be given by someone authorised.|
An impressive machine. It has mastered the appearance of knowing what it is doing.|
I would like to know its purpose before proposing an improvement. Please note this considerable personal progress.|
People put a great deal of work into unfamiliar things. Understanding can begin with asking a respectful question.|
Impressive is a first impression. Useful is a question for the person who actually needs the thing.|
It has a striking shape. I wonder which parts came from function and which came from somebody's sense of style.
''')
add('new_video_game','Text_VideoGame','The latest video game looks fun.','''
The latest game. I am very mature about waiting until we have permission to play it.|
A new game. There is probably a fascinating set of rules beneath the first impression of fun.|
Looks fun. We can finish what we came here to do before losing an entire afternoon.|
A new game always makes me curious about the music. The rest of my afternoon should be worried.|
Games and a properly planned snack break. I am dangerously close to considering this an itinerary.|
A whole performance waiting for someone to take part. Games have an unfair advantage over monologues.|
The latest game. My unread books have heard this excuse before.|
I would like to see how the controls feel before examining the hardware. Both require the owner's permission.|
A new game can become an old favourite someday. It is pleasant to catch the beginning of that possibility.|
It looks fun. I hope the controls are as welcoming as the box is persuasive.|
Someone has made a whole little world you can move through. I like seeing what they chose to make noticeable.
''')
add('burglary_damage','Text_Burglary','There are clear signs that this place was burgled.','''
sad~Someone has already had their things disturbed. We can help without disturbing anything else.|
sad~Signs of a burglary. We should leave the evidence and the belongings where they are.|
annoyed~Someone broke in. Their things are not an invitation for us to start searching too.|
sad~This was somebody's safe place. I do not want to add our footsteps to the damage.|
sad~Someone will have to make this feel like home again. Let us ask what would help before doing anything.|
sad~There is no clever performance to make out of this. Someone's privacy was violated.|
sad~I do not have a joke for this. Their belongings and their peace both deserved better.|
annoyed~We should not move anything. Fixing damage comes after the owner and the investigation have had a say.|
sad~A room can feel different after someone forces their way in. What happened matters even if the broken things are replaced.|
annoyed~These were someone's belongings. Their value does not depend on whether a stranger thinks they were expensive.|
sad~Somebody will remember how this room used to look. We can be careful with what is still here.
''')
add('pokemon_tv_programme','Text_PlayerFacingTVScreen','A Pokemon on television appears to be having fun.','''
A Pokemon enjoying itself on TV. I support this important use of broadcasting.|
It looks at ease on screen. I hope the people making the programme keep it comfortable between takes, too.|
Looks like it is having a good time. That is a better show than watching somebody make it miserable.|
A happy Pokemon on television. I would like to hear the sounds it makes between the music.|
It seems to be enjoying itself. A perfectly good reason for a programme to exist.|
A performer having fun. I hope the off-camera work is just as considerate.|
A Pokemon enjoying itself. Finally, a broadcast with achievable emotional goals.|
It looks comfortable with what it is doing. I appreciate a demonstration that does not depend on frightening the subject.|
A little happy moment broadcast to strangers. I hope it leaves some of that happiness with them.|
It looks relaxed. I like a programme where the subject is allowed more than looking impressive.|
You can feel the enjoyment even through a screen. A small, lively moment makes a surprisingly good picture.
''')
add('league_destination','Text_Indigo_UltimateGoal Text_Indigo_HighestAuthority','The sign identifies Indigo Plateau as Pokemon League headquarters.','''
League headquarters. The sign sounds certain about the goal. My knees are taking a little longer.|
The League is a major destination, not the only measure of what these travels have meant.|
The League. We can respect the challenge without letting the sign decide our whole worth.|
A grand destination. I am trying to think of the next note rather than the entire performance at once.|
The League matters. So do the meals, rests and care that got the team here.|
A formidable venue. Being able to stand here already took more work than the sign can list.|
The ultimate goal, says the sign. My goals currently include remembering how to breathe normally.|
A serious challenge ahead. Let us check the team and supplies instead of relying on dramatic momentum.|
A destination with a great deal of meaning attached. We are allowed to bring our own meaning, too.|
A big title on a big destination. The people arriving here still deserve room to feel nervous.|
The League is a powerful landmark. It does not erase the smaller places that made this journey ours.
''')
