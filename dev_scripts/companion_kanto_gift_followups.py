"""Gift-speaker followups whose exact success receipts preserve NPC identity.

Custom receipts must be individually recognized by CompanionDialogue; a failed
handoff's separate NPC/error line must supersede the earlier success candidate.
"""
ROWS=[]
EMOTIONS=dict(N='neutral',S='soft_smile',A='annoyed',F='flustered',D='sad',U='surprised',M='smug',L='laughing')
def add(key,labels,subject,lines):
    replies=[]
    for line in lines.strip().split('|'):
        line=line.strip()
        if len(line)>1 and line[1]=='~' and line[0]in EMOTIONS:line=EMOTIONS[line[0]]+line[1:]
        replies.append(line)
    assert len(replies)==11,(key,len(replies))
    ROWS.append(dict(key='kanto_gf_'+key,labels=labels.split(),subject=subject,replies=replies))

add('old_amber_handoff','PewterCity_Museum_1F_Text_WantYouToGetAmberExamined',
    'The scientist entrusts us with Old Amber for laboratory examination; his custom success receipt preserves this request.','''
S~A little piece of old sunlight, and a very hopeful errand. We should carry it carefully.|
S~He has a hypothesis and a sample that needs independent examination. The lab visit is the next useful step.|
N~Keep the amber safe. Someone trusted us with more than an ordinary parcel.|
S~It sounds important to him that somebody will finally take the idea seriously.|
N~A careful journey matters when a find cannot simply be replaced.|
S~The overlooked researcher has found a courier for a story that might yet change its ending.|
S~A small ancient thing carrying a very new kind of hope.|
S~Physical sample secured for external analysis. Good next step, fascinating question.|
S~An old tree's little golden secret has begun another journey.|
N~He needs a careful examination, not somebody promising the answer he wants.|
S~I wonder what the first lab observation will reveal about the amber.
''')
add('coin_case_handoff','CeladonCity_Restaurant_Text_TakeThisImBusted',
    'The ruined gambler gives away his Coin Case and resolves to stop playing; the custom receipt preserves his speech.','''
N~He is trying to make leaving easier by giving away the thing that brought him back. I hope it helps.|
N~Removing a familiar cue may support his decision to stop. The loss clearly affected him deeply.|
N~No laughing at him. Deciding to stop is worth respecting.|
D~It is painful when a bad day has to become a lesson about what you can trust yourself with.|
N~I hope his next meal is a quiet one without another promise from the slots in his head.|
N~The speaker hands over a prop because he wants a genuinely different next chapter.|
D~An empty case can hold quite a lot of regret. I am glad he is putting it down.|
N~He has identified a behavior he wants to end and made a concrete change around it.|
N~A small box is leaving his hands so the rest of the day might return to them.|
N~That was a vulnerable thing to say out loud. We should let him keep his dignity.|
N~I wonder who he can spend time with once he steps away from the machines.
''')
add('fisher_ten_coins','CeladonCity_GameCorner_Text_DoYouWantToPlay',
    'The fisher gives ten coins after his invitation; case absence and overflow print different terminal lines.','''
S~A small handful of welcome, from someone who decided to include a stranger.|
N~The ten coins were freely offered. Accepting them need not determine how long we stay.|
N~Kind of him. A gift is still no reason to spend the whole afternoon here.|
S~He made the introduction simple and friendly.|
N~We can appreciate a little generosity without letting the machines choose the rest of the day.|
S~A modest patron opens the next scene with a few coins and an uncomplicated invitation.|
N~A gift can remain a small gift, rather than the start of a long obligation.|
N~Transfer completed within the case limit. Keep the original spending plan in mind.|
S~A few little circles have made the conversation warmer.|
S~A friendly gesture, with no need to turn it into a grand event.|
S~I wonder how often he welcomes new visitors like this.
''')
add('scientist_twenty_coins','CeladonCity_GameCorner_Text_WantSomeCoins',
    'The scientist gives twenty coins; the checked success receipt preserves his offer.','''
S~He has shared a little of his supply without making a speech of it. Nice.|
S~A voluntary gift, distinct from buying coins at the counter. The handoff is complete.|
N~Thanks to him. We can still choose where to spend our time.|
S~It is lovely when an unfamiliar room includes someone willing to be casually kind.|
S~A small welcome is often easier to accept than an elaborate favor.|
S~The quiet benefactor gives the scene a warmer opening than the machines manage.|
S~A little generosity, offered without needing to look important.|
N~Clear offer, completed transfer, no extra commitment specified.|
S~A stranger's small bright kindness can fit in a very ordinary box.|
S~He made the gift feel friendly instead of making us perform gratitude for it.|
S~I wonder whether he remembers the person who first helped him feel welcome here.
''')
add('gentleman_twenty_coins','CeladonCity_GameCorner_Text_HereAreSomeCoinsShoo',
    'The distracted gentleman gives twenty coins mainly to make us stop interrupting him.','''
M~A gift with a very clear please go elsewhere attached. Unusually expensive privacy policy.|
N~The transfer is generous in amount, though his stated purpose is ending the interruption.|
N~He wants quiet. Take the hint and leave him space.|
F~It is awkward to be thanked with money for going away.|
N~We can accept the boundary without standing here to ask why he gave the coins.|
M~The patron purchases the shortest possible ending to our guest appearance.|
M~A small donation to the cause of not talking to us. Efficiently expressed.|
N~He has allocated a resource to remove a distraction. Clear, if socially clumsy.|
N~A handful of metal has drawn a little quiet circle around his chair.|
N~The manners are poor, but the preference is clear. We should move on.|
N~I wonder how absorbed he was before we stopped beside the machine.
''')
add('moon_stone_thanks','TwoIsland_JoyfulGameCorner_Text_OhThisIsFromBill',
    'Lostelle\'s father thanks Bill for the Meteorite and gives us a Moon Stone; only initial success preserves this actual speech.','''
S~The Meteorite reached the right hands, and the return kindness has a little moonlight in it.|
S~The delivery and his subsequent reward are distinct successful parts of this exchange.|
S~Good. The stone is safe with him, and Bill's greeting got through.|
S~It is lovely to see somebody enjoy a thoughtful gift after such a frightening day.|
S~A friend's remembered interest makes the present feel personal.|
S~The long errand closes with a grateful owner and an unexpectedly luminous little thank-you.|
S~One interesting stone has found a home; another has begun traveling beside us.|
N~Delivery completed and reward received. Clear handoff in both directions.|
S~A piece of distant sky has met a familiar friendship here.|
S~He remembers the giver while thanking the person who carried it. Thoughtful.|
S~I wonder where he will display the Meteorite now that the worrying part of the day is over.
''')
add('news_new_report','CeruleanCity_House4_Text_NewNewsInformativeHaveThis',
    'The enthusiast enjoys an informative new report and successfully gives a reward using generic success receipts.','''
S~A little new information has made his chair a much more interesting place to sit.|
S~He values the report and acknowledges the effort of bringing it. A pleasant information exchange.|
N~Glad he enjoyed it. Good news should still be checked before being passed on.|
S~It is lovely hearing curiosity make an ordinary afternoon feel different.|
S~A small reward is a kind way to say the conversation mattered to him.|
S~The formerly bored reader has found something worthy of an enthusiastic review.|
S~A few new words have opened a little window in the room.|
S~Useful input received, appreciation returned. Good little feedback loop.|
S~A small story has made the day less closed around him.|
S~He remembered to thank the person who brought it, not just enjoy the report.|
S~I wonder which part of the news made him lean forward to keep reading.
''')
add('news_amazing_report','CeruleanCity_House4_Text_IncredibleNewsHaveBerries',
    'The enthusiast is astonished by an exceptional report and successfully rewards us with extra Berries.','''
U~The news has nearly launched him out of the chair. That must have been a remarkable read.|
S~He is responding to a report he finds unusually significant, without yet telling us which detail mattered.|
S~Good to see him so delighted. The Berries are a generous thank-you.|
S~It is lovely when somebody forgets to sound composed because they are simply happy.|
S~He has turned a good reading moment into something sweet to share.|
U~A rave review delivered with the dignity of a man being happily overtaken by the material.|
S~An old interest becoming bright enough to surprise its owner again.|
S~High-value new information, unusually strong positive response. Memorable result.|
S~A small piece of the outside world has made the whole room brighter.|
S~The excitement looks real before the extra reward even appears.|
S~I wonder what earlier report he is comparing this one with in his memory.
''')
add('news_shared_once','CeruleanCity_House4_Text_ThanksForSpreadingNewsTakeThis',
    'The enthusiast rewards us for sharing his news with others.','''
S~The story has gone visiting, and he is glad it did not stay shut in one room.|
S~He values dissemination as well as receiving the original information.|
N~Good to pass on something accurate and welcome. The reward is a kind extra.|
S~It is nice when one person's curiosity becomes a conversation for someone else.|
S~A little shared interest can make the day warmer on more than one doorstep.|
S~The delighted reader has promoted the courier to the story's distribution department.|
S~A bright thing feels different once it is no longer enjoyed alone.|
N~Information distributed. Accuracy should travel with it.|
S~A little lamp has been carried from one room to another.|
S~He is grateful for the work beyond his own chair. A thoughtful detail.|
S~I wonder who was happiest to hear the story when it reached them.
''')
add('news_shared_widely','CeruleanCity_House4_Text_MagnificentNewsSpreadHaveBerries',
    'The enthusiast celebrates further sharing and gives a larger Berry reward.','''
S~The news now has a social life busier than mine, and he is feeding the delivery service.|
S~He recognizes repeated sharing with a larger reward. The report itself still deserves careful context.|
N~A generous thank-you. Keep the story accurate as it travels farther.|
S~I like how he imagines the news being pleased to go somewhere new.|
S~A happy habit has given him a reason to be generous again.|
S~The once-confined story has become a touring success with a remarkably affectionate producer.|
S~An enthusiasm that keeps finding a little more room beyond its original window.|
N~Wider distribution confirmed. Good time to check that the message has not changed in the telling.|
S~A small bright thread has joined a few more rooms together.|
S~He has made a simple shared pleasure feel like something worth celebrating.|
S~I wonder whether anyone has sent their own reaction back to him yet.
''')
