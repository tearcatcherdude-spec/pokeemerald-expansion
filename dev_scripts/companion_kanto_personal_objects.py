"""Personal Kanto objects and a written family message, reviewed exact sources."""
ROWS=[]
E=dict(N='neutral',S='soft_smile',A='annoyed',F='flustered',D='sad',U='surprised',M='smug',L='laughing')
def add(key,label,subject,lines):
    replies=[]
    for s in lines.strip().split('|'):
        s=s.strip()
        if len(s)>1 and s[1]=='~' and s[0] in E:s=E[s[0]]+s[1:]
        replies.append(s)
    assert len(replies)==11,(key,len(replies))
    ROWS.append(dict(key='kanto_personal_object_'+key,labels=[label],subject=subject,replies=replies))
add('mom_letter','PewterCity_Text_RunningShoesLetterFromMom',
    "Mom's attached letter cheers the player on and sends Running Shoes for the journey.",'''
S~Shoes and a cheering section small enough to fold up beside them. She packed both kinds of support.|
S~The practical gift and the written encouragement address rather different needs. Both were thoughtfully chosen.|
S~She wants us ready for the road, and to know somebody is on our side.|
S~I would keep the letter somewhere dry, even after the shoes feel familiar.|
S~A useful gift keeps helping all day. The note might help on the days the walking feels harder.|
S~The expedition has received equipment and a beautifully unambiguous endorsement from home.|
S~A small piece of paper can make the distance back home feel less absolute.|
S~Good equipment matters. So does having someone who wants to see what you manage with it.|
S~Her words can travel farther than her voice, tucked quietly into the journey.|
S~She has put love into something we can actually wear out through living. That is a lovely gift.|
S~I wonder what ordinary moment will make us unfold the letter and read it again.
''')
add('copycat_doll','SaffronCity_CopycatsHouse_2F_Text_RareMonOnlyDoll',
    "A convincing Pokemon doll is briefly mistaken for a rare Pokemon.",'''
L~An exceptionally successful doll. It has completed a whole encounter without moving a stitch.|
S~The resemblance was convincing enough to produce a mistaken first identification. Closer inspection helped.|
S~A good imitation. Leave it where its owner put it.|
S~The little surprise makes me appreciate how carefully somebody made it.|
S~Only a doll seems a little unfair after it worked that hard to fool us.|
S~A remarkably accomplished understudy has secured the audience's attention while remaining entirely stuffed.|
S~A brief disappointment, followed by respect for a very persuasive piece of fabric.|
S~The proportions and details must be doing their job. That is effective design.|
S~A small made thing has borrowed the shape of wonder for a moment.|
S~Only a doll? That is a rather good compliment to the person who designed it.|
S~I would like to know which detail fooled us before we looked closely.
''')
add('lorelei_dolls','FourIsland_LoreleisHouse_Text_StuffedMonDollsGalore',
    "Lorelei's house contains a large collection of stuffed Pokemon dolls.",'''
S~That is a magnificent amount of soft company. A difficult day would have trouble finding an empty chair.|
S~A personal collection can reveal interests that a public role leaves little opportunity to show.|
S~Her home. She is allowed somewhere comfortable to return to.|
S~I like seeing a room that holds something its owner simply enjoys.|
S~A home should have room for delights that do not have to earn their place.|
S~The formidable public figure has a private supporting cast made almost entirely of stuffing.|
S~An admirable refusal to make the living room uphold a severe reputation.|
S~There must be interesting little differences between all the designs collected here.|
S~A strong person's quiet room can still be full of soft things.|
S~A collection this fondly kept says more than a carefully managed public image.|
S~I wonder which doll started the collection, before it became a whole roomful of favourites.
''')
add('museum_amber','PewterCity_Museum_1F_Text_BeautifulPieceOfAmber',
    "The museum displays a clear gold-coloured piece of amber.",'''
S~It looks as though somebody persuaded a little sunlight to sit still for the museum.|
S~Its clarity lets us appreciate the material itself, quite apart from anything it might contain.|
S~Worth a quiet look. The display does not need us tapping on it.|
S~I like the warmth of that colour against the stillness of the case.|
S~A beautiful small thing can make a slow walk through a museum worthwhile.|
S~A modest exhibit with an exceptionally accomplished lighting effect supplied by the object itself.|
S~A little gold-coloured stillness. It need not contain a grand secret to be worth keeping.|
S~The transparency is lovely. It would be interesting to see how the surface scatters light.|
S~An old piece of the world has kept a warm-looking corner of itself.|
S~A single clear colour can hold attention better than an overcrowded display.|
S~I wonder how different it looks as the light shifts across the room.
''')
