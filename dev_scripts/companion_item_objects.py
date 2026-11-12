"""Standalone successful item notices; NPC or unknown dialogue always takes precedence."""
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

add('object_single_item_found','gText_PlayerFoundOneItem',
    'A standalone item discovery succeeds before any NPC or unknown field text.', '''
M~A useful discovery! I was going to contribute, but the object had already done all the hiding.|
N~Worth checking what it does before deciding how to use it.|
N~Stow it safely. We can work out where it belongs when we stop.|
S~I like a small discovery that changes the feeling of an ordinary path.|
N~We should see whether it helps the team now or is better saved for later.|
M~A quiet bit of scenery has unexpectedly joined the inventory.|
M~An object with an excellent strategy for getting our attention: being worth picking up.|
N~Let us inspect its purpose before assigning it a job.|
S~The road has left a small, tangible surprise in our hands.|
N~We can appreciate the find without immediately using it.|
S~I would remember where we noticed it. The little discoveries become part of the route.
''')
add('object_multiple_items_found','gText_PlayerFoundItems',
    'A standalone discovery of multiple items succeeds before any NPC or unknown field text.', '''
U~More than one! My talent for discovering something by accident is developing a quantity bonus.|
N~A useful supply. Check the count and purpose before relying on it.|
N~Good find. Keep track of what we have instead of assuming it will last forever.|
S~A small surprise became a slightly larger one. I like that sort of escalation.|
N~We can plan around the extra supplies without needing to spend them immediately.|
M~The scenery has made a more generous contribution than its speaking role suggested.|
M~A discovery with enough commitment to arrive in the plural.|
N~Additional stock changes our options. It does not tell us which option is best yet.|
S~A handful of possibilities where we expected none.|
N~Let us arrange them properly before the bag turns into a guessing game.|
S~I wonder how many other useful little details we walked past before learning to look.
''')
add('object_standalone_item_received','gText_ObtainedTheItem gText_ObtainedTheItems',
    'A successful item receipt is the first field message; no NPC topic has been replaced.', '''
S~Something new to carry. I will try not to give our bag another encouraging pat at the worst moment.|
N~We have received it. Understanding its use is a separate step worth taking.|
N~Check what it is for, then keep it somewhere we can find again.|
S~I like having something small and real to mark a moment.|
N~We can decide how it helps after making sure it is safely put away.|
S~A new object has entered the story without requiring an elaborate introduction.|
M~Another possession joins the ongoing argument about which pocket has room.|
N~Receipt confirmed. Now identify its function before experimenting.|
N~A thing can be useful without needing to be used immediately.|
N~It deserves a proper place in the bag rather than a dramatic disappearance into it.|
S~I would like to remember the moment as well as the object we take away from it.
''')

