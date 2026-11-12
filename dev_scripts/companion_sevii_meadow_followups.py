"""Registered Five Island Meadow Rocket trainers' final speech."""
ROWS=[]
EMOTIONS=dict(N='neutral',S='soft_smile',A='annoyed',F='flustered',D='sad',U='surprised',M='smug',L='laughing')
def add(key,label,subject,lines):
    replies=[]
    for line in lines.strip().split('|'):
        line=line.strip()
        if len(line)>1 and line[1]=='~' and line[0] in EMOTIONS:line=EMOTIONS[line[0]]+line[1:]
        replies.append(line)
    assert len(replies)==11,(key,len(replies))
    ROWS.append(dict(key='sevii_meadow_end_'+key,labels=[label],subject=subject,replies=replies))
add('dismissal','FiveIsland_Meadow_Text_Rocket1PostBattle',
    'The defeated Rocket orders the player to leave and insists they have no business here.','''
N~He has lost the battle and is trying to win the argument by assigning us a destination.|
N~His assertion supplies no reason to accept that Rocket activity is legitimate.|
N~He does not get to decide who belongs here. Stay alert.|
N~That sounds more like wanting us gone than having anything useful to say.|
N~A rude order does not make the place his to control.|
N~The defeated guard has promoted himself to authority over our travel plans.|
N~An unpleasant welcome is not the same as a convincing boundary.|
N~He has supplied an instruction without a useful explanation.|
N~The word home is doing rather ugly work in his mouth.|
A~He could have stopped at being unpleasant without pretending to own the place.|
N~I wonder what he is so anxious to keep visitors from noticing.
''')
add('warning','FiveIsland_Meadow_Text_Rocket2PostBattle',
    'A Rocket warns that knowing what is inside the warehouse would be dangerous.','''
N~He has made the warehouse sound less like storage and more like a very bad secret.|
N~The warning implies a risk, but offers no trustworthy account of what creates it.|
N~Take the danger seriously. His claim to be helping us is another matter.|
N~He is trying to make curiosity feel like a mistake.|
N~A threat dressed as advice still deserves a careful step back and a clear head.|
N~A sinister invitation to remain uninformed. The courtesy is doing no convincing work.|
N~He has put a very thin polite coat over that warning.|
N~We should assess the actual risk rather than letting his tone make the decision.|
N~A closed room gathers darker possibilities when its guard speaks like that.|
N~For our own sake is a polished little handle on an ugly message.|
N~That makes the warehouse more concerning, though it tells us little about what is inside.
''')
add('passwords','FiveIsland_Meadow_Text_Rocket3PostBattle',
    'A Rocket says the warehouse cannot be entered without its passwords.','''
S~He has helpfully told us the obstacle has more than one password-shaped piece.|
N~The plural is useful information. Entry appears to require more than a single credential.|
N~Good to know the barrier. No reason to tell him what we already know.|
N~His confidence depends on assuming we will stop at the locked door.|
N~We can remember the information without giving him the satisfaction of an argument.|
M~A guard who volunteers the shape of the solution has a questionable sense of secrecy.|
N~An unhelpful man has accidentally supplied something useful.|
S~Multiple passwords narrow down the access mechanism. That is a start.|
N~A secret door is less secret once its keeper starts explaining the lock.|
M~He seems terribly pleased with a detail he probably ought to have kept to himself.|
N~I wonder how carefully they protect the passwords compared with the fact that they exist.
''')
