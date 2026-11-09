"""Authoring/build entry point for the recruitable cast. Never rewrites base maps wholesale."""
from pathlib import Path
import json,re,textwrap,hashlib,struct
ROOT=Path(__file__).resolve().parents[1]
NAMES=['silas','kade','ashe','nico','riven','emi','vera','lume','mochi','zuri']
EXPRESSIONS=['neutral','soft_smile','annoyed','flustered','sad','surprised','smug','laughing']

def save(path,value):
 p=ROOT/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(value,indent=2)+'\n',encoding='utf-8')

def wrapped(text,name=None):
 text=(name.upper()+': ' if name else '')+text
 lines=textwrap.wrap(text,32,break_long_words=False,break_on_hyphens=False)
 return lines[0]+''.join(('\\n' if i==1 else '\\l')+line for i,line in enumerate(lines[1:],1))+'$'

def ctext(text,name=None):
 return 'COMPOUND_STRING("'+wrapped(text,name).replace('"','\\"')+'")'

def profiles():
 # Team levels use the maximum native land encounter of the nearby route + 3 or + 5.
 # Requirements are checked again before committing a gift; shown Pokemon stay in the party.
 return [
 dict(name='silas',personality='Earnest field scientist; precise, unintentionally funny, learning to listen.',map='OldaleTown',area='MAP_ROUTE103',level=7,requirement='species',value='WURMPLE',team=['Magnemite','Porygon','Ralts','Budew'],
 intro='I am Silas. My field seminar has one attendee: a WURMPLE. It has eaten the attendance sheet. Could you show me one? Yours stays with you.',request='A WURMPLE from the nearby grass will do. I need to observe it, not borrow it. My lecture has already suffered enough.',ready='Excellent antennae. Better attention span than my supervisor. May I test a four-Pokemon field team against yours?',defeat='The hypothesis has been thoroughly tackled.',join='I kept predicting your choices instead of watching you. Lesson received. Could I travel with you? I can take notes and occasionally hints.',
 lore=[('soft_smile','My mother repaired radios in OLDALE. I liked finding voices inside things people thought were broken.'),('laughing','My first experiment was teaching a MAGNEMITE to ring the dinner bell. It invited every spoon in town.'),('sad','I won a laboratory placement. Then I stopped going outside. Every report was perfect. I was terribly lonely.'),('neutral','My supervisor called fieldwork a distraction. I believed him until a patient RALTS refused to enter the lab.'),('soft_smile','I came here to prove my research mattered. Now I think noticing who needs help is research too.'),('laughing','I wrote home about you. Mother asked whether my new colleague eats properly. Congratulations. You have passed peer review.')]),
 dict(name='kade',personality='Dry courier with a protective streak; treats ridiculous logistics very seriously.',map='KantoRoute2',area='MAP_KANTO_ROUTE2',level=10,requirement='species',value='RATTATA',team=['Sandshrew','Rattata','Houndour','Machop'],
 intro='Kade. Courier. A RATTATA keeps stealing my delivery straps. Show me one and I might finally negotiate with management. No, I am not keeping yours.',request='RATTATA live on ROUTE 1. Just show me one in your party. I have prepared a stern but nutritionally fair speech.',ready='Your RATTATA looks innocent. Suspicious. Want a four-Pokemon battle? I need someone who can keep moving when a plan falls apart.',defeat='Signed for. By every member of your team.',join='You looked after your team even while winning. That matters. Want company? I know roads, repairs, and when to stop asking questions.',
 lore=[('neutral','I used to deliver medicine with my older sister. She knew every shortcut. I knew every bakery.'),('laughing','She made me practice smiling at customers. A child asked why the parcel looked frightened.'),('sad','Once I was late with an important delivery. Nobody blamed me. I kept hearing blame anyway.'),('neutral','I started taking every job alone. It is hard to disappoint a partner if you never let one join you.'),('soft_smile','A HOUNDOUR followed me through a storm. I told it to go home. It sat on my boots until I asked for help.'),('soft_smile','Travelling with you feels less like making up for a mistake. More like going somewhere. I could get used to that.')]),
 dict(name='ashe',personality='Soft-spoken musician; observant, awkward jokes, understated warmth.',map='KantoRoute3',area='MAP_KANTO_ROUTE3',level=13,requirement='steps',value=160,team=['Kricketot','Whismur','Chingling','Zubat'],
 intro='I am Ashe. I am recording a walking song. Could you take 160 steps after this chat? I need a rhythm that is not my own nervous pacing.',request='Still collecting the footsteps. Keep walking; your normal travels count. Please do not buy a drum just for me.',ready='That rhythm works. Want to try a four-Pokemon battle? My band practices being loud without being cruel.',defeat='We may need to rehearse the winning part.',join='You gave everyone room to move. I like that. Could I come along? I am better at listening than introductions.',
 lore=[('neutral','I played in my uncle\'s cafe. Mostly when the washing machine was loud enough to cover my mistakes.'),('laughing','WHISMUR was my first audience. It applauded by knocking every cup off a shelf. Mixed reviews.'),('sad','I froze at a festival audition. I still remember the silence more clearly than any song I have written.'),('soft_smile','My uncle kept my name on the cafe noticeboard. No deadline. Just a place to return when I was ready.'),('neutral','I thought confidence had to arrive before the music. You keep doing brave things while admitting you are nervous.'),('soft_smile','I am writing a song I might actually play for people. There is a part for footsteps. Yours, if that is all right.')]),
 dict(name='nico',personality='Playful baker; irreverent food metaphors, generous without treating people as projects.',map='Route104',area='MAP_ROUTE104',level=10,requirement='item',value='ORAN_BERRY',team=['Slugma','Shroomish','Cherubi','Munchlax'],
 intro='Nico! Baker, traveller, occasional smoke alarm. Bring me one ORAN BERRY and I will demonstrate a recipe with an actual success rate.',request='One ORAN BERRY. The nearby berry trees can help. The recipe specifically says not to substitute a blue rock.',ready='Trade me one ORAN BERRY and a four-Pokemon battle? The berry goes into trail bread. The battle settles who gets the heroic slice.',defeat='Well. That is my humble pie sorted.',join='Your team shares the work. I like your kitchen. Metaphorical kitchen. Want me to come along? I pack food and terrible timing.',
 lore=[('laughing','My grandmother taught me to bake by feel. She meant the dough. I thought she meant dramatic instinct.'),('soft_smile','Her shop had a spare chair for anyone who needed somewhere warm. Sometimes the chair made more money than the bread.'),('sad','When she closed the shop, I rushed into opening my own. I wanted to keep everything exactly the same.'),('neutral','I burned through my savings trying to copy her life. She told me a recipe is a beginning, not an obligation.'),('soft_smile','Now I collect meals and the stories attached to them. Travelling with you has improved both the menu and the stories.'),('laughing','When I open a place again, there will be a spare chair. And a smoke alarm with union representation.')]),
 dict(name='riven',personality='Theatrical street magician; flamboyant wordplay, honest about consent and misdirection.',map='KantoVermilionCity',area='MAP_KANTO_ROUTE6',level=21,requirement='species',value='ABRA',team=['Kadabra','Sableye','Misdreavus','Mr. Mime'],
 intro='Riven, at your service! I seek an ABRA for a study of disappearing before introductions. Show me one. It remains your mysterious associate.',request='ABRA can be found north of CERULEAN. I only need to see yours. Apparently shouting STAY is not a successful research method.',ready='A splendid assistant, entirely yours. Care for a four-Pokemon exhibition battle? Nothing up my sleeve except a concerning amount of lint.',defeat='A disappearing victory! Unfortunately, it was mine.',join='You saw through the trick and still treated the performers kindly. May I join you? I promise to announce any dramatic entrances in advance.',
 lore=[('smug','My father performed little card tricks at the docks. He could make an exhausting day feel briefly impossible.'),('laughing','He taught me the grand gesture first. I spent a week bowing before I was allowed to touch a card.'),('sad','I once used a trick to hide a mistake from a friend. It worked beautifully. That was the worst part.'),('neutral','She found out. We are talking again, slowly. Being forgiven is not the same thing as skipping the work.'),('soft_smile','Now I tell an audience when a trick begins. Wonder is nicer when everyone has agreed to be fooled.'),('soft_smile','You never ask me to be impressive all the time. It is an unusual luxury. I am considering a less dramatic thank-you.')]),
 dict(name='emi',personality='Goth poet with bone-dry humour; attentive to small kindnesses, quietly courageous.',map='Route102',area='MAP_ROUTE102',level=7,requirement='steps',value=64,team=['Hoothoot','Ralts','Murkrow','Buneary'],
 intro='Emi. I am trying to write about a journey without leaving this sign. Walk 64 steps after we talk? I need evidence that beginnings survive movement.',request='Take a little walk. Your ordinary steps count. I tried outsourcing this to MURKROW. It submitted a twig.',ready='You returned. The poem now has a second line. Want a four-Pokemon battle? My team insists I experience a plot.',defeat='A tragic ending. For my winning streak of zero.',join='You were kind to your team when things got messy. I would like to see where you go next. Want me to travel with you?',
 lore=[('neutral','I grew up above my aunt\'s bookshop. Every customer thought a quiet child was a spare bookmark.'),('laughing','I wrote my first poem about the moon. It was actually a streetlamp. Strong opening. Weak astronomy.'),('sad','I stopped showing people my work after someone laughed at a serious poem. I decided every poem had to be a joke first.'),('neutral','My aunt kept the original in her till. She said a clumsy honest thing can still be worth keeping.'),('soft_smile','Sometimes I make a joke before saying I care. You are getting very inconveniently good at hearing the second part.'),('soft_smile','I sent her a new poem. No disguise, no punchline. I would like to read it to you one day. When my knees stop writing their own review.')]),
 dict(name='vera',personality='Enthusiastic mechanic; bold problem solver, gadget comedy, respects boundaries.',map='SlateportCity',area='MAP_ROUTE110',level=18,requirement='item',value='PARALYZE_HEAL',team=['Electrike','Magnemite','Voltorb','Pachirisu'],
 intro='Vera! I repair things. Sometimes the thing is my confidence after a repair. Bring one PARALYZE HEAL for the workshop first-aid kit?',request='The MART sells PARALYZE HEAL. One is enough. Safety equipment comes before the impressive sparks. I am learning.',ready='Donate one PARALYZE HEAL to the kit and try a four-Pokemon test battle? No prototypes attached to you, I promise.',defeat='Excellent stress test. The stress was me.',join='You adapted instead of blaming your team. That is good engineering. Want a mechanic along? I can promise effort and label the experimental bits.',
 lore=[('laughing','My father fixed fishing reels. I improved one until it could retrieve a hat from three streets away.'),('soft_smile','He never said I was too much. He asked what problem I actually wanted to solve. Infuriatingly useful question.'),('sad','I built a motor too quickly and frightened my ELECTRIKE. Nothing broke. Its trust still needed repairing.'),('neutral','Now I ask before trying new equipment around Pokemon. Being clever does not make someone else a test bench.'),('soft_smile','I want to make travelling easier for people whose bodies need different routes. That is a problem worth taking slowly.'),('laughing','I have drawn a folding rest seat. You are listed as a consultant. Payment is one extremely official sit-down.')]),
 dict(name='lume',personality='Gentle folklorist; eerie deadpan, patient curiosity, distinguishes stories from evidence.',map='VerdanturfTown',area='MAP_ROUTE117',level=19,requirement='species',value='NINCADA',team=['Nincada','Duskull','Spoink','Hoothoot'],
 intro='Lume. I collect local stories. A farmer says NINCADA can hear roots gossip. Show me one from ROUTE 116? We can ask politely. It stays yours.',request='A NINCADA from ROUTE 116, in your party. I am recording a story, not asking you to prove a ghost exists.',ready='It is listening. Possibly to roots. Possibly to lunch. Shall we have a four-Pokemon battle before writing the conclusion?',defeat='The witnesses agree: you won.',join='You let a strange story be strange without laughing at its teller. I appreciate that. Could I join your travels?',
 lore=[('neutral','My grandmother told stories to keep children close on foggy roads. I used to think she knew every ghost personally.'),('laughing','She admitted one haunted gate was just a badly oiled hinge. She still charged it rent in her stories.'),('sad','After she died, I tried to write down every word. I was frightened that forgetting a sentence meant losing her again.'),('soft_smile','A neighbour remembered a different ending. It was hers too. People leave pieces of themselves with more than one person.'),('neutral','I ask who a story helps, and who it leaves out. An old story can deserve affection and still need a better ending.'),('soft_smile','I am writing one about these travels. You do not have to do anything legendary. Someone remembering you kindly is enough.')]),
 dict(name='mochi',personality='Cheerful designer; precise fashion wit, practical empathy, refuses appearance-based judgement.',map='KantoCeruleanCity',area='MAP_KANTO_ROUTE24',level=19,requirement='item',value='POKE_BALL',team=['Buneary','Skitty','Combee','Roselia'],
 intro='Mochi! I am making a travelling outfit with real pockets. Could you spare one POKE BALL for a clasp test? Unused, please. No surprise tenants.',request='Just one ordinary POKE BALL from the MART. I am testing the fastening, not borrowing anyone inside it.',ready='Let me use one POKE BALL for the test, then a four-Pokemon battle? Clothing should survive actual movement. So should my sales pitch.',defeat='A clean victory. Mine has a loose seam.',join='You noticed effort instead of appearances. Excellent taste. Want company? I can mend sleeves and offer opinions with a reasonable return policy.',
 lore=[('soft_smile','My first designs were for a shy friend who hated being photographed. I learned to ask how clothes felt before asking how they looked.'),('laughing','My first bag had decorative pockets. My friend returned it with a drawing of an angry sandwich.'),('sad','I once changed my style to fit a fashion contest. I placed well and could not recognise a single thing I had made.'),('neutral','My friend asked when I would make something with an actual place for her lunch. That was a very good review.'),('soft_smile','I want people to feel like themselves, with room to move. Beautiful is allowed to be comfortable.'),('laughing','I have a sketch of our travelling clothes. Every pocket works. The angry sandwich has finally approved the collection.')]),
 dict(name='zuri',personality='Charismatic mural artist; playful visual wit, community-minded, candid about uncertainty.',map='KantoCeladonCity',area='MAP_KANTO_ROUTE7',level=27,requirement='item',value='POTION',team=['Smeargle','Chatot','Aipom','Spinda'],
 intro='Zuri! I am planning a community mural. Before the paint, a first-aid kit. Could you bring one POTION? My crew includes very ambitious elbows.',request='One POTION for the crew. The MART has them. I want us prepared, not auditioning for an accident.',ready='Donate one POTION and try a four-Pokemon battle? I need a partner who can improvise without treating everyone else as scenery.',defeat='Bold composition. Devastating use of my mistakes.',join='You gave your team space to shine. Want me along? I collect colours, stories, and occasionally permission forms.',
 lore=[('soft_smile','I painted with my brother behind our old home. He made enormous skies. I filled them with birds that looked like bent spoons.'),('laughing','He called it my signature bird. I sold one sketch before learning which end of a wing was which.'),('sad','When the building was sold, our wall was painted over. I was angrier about that than I knew how to explain.'),('neutral','I started asking people what they wanted remembered before planning a mural. A wall belongs to more than the person holding a brush.'),('soft_smile','I still miss that sky. But the neighbours remember it. I am learning that paint is one way to keep something, not the only way.'),('laughing','There is a new mural in my sketchbook. Everyone we have helped gets a little space. Yes, the bent-spoon birds are staying.')]),
 ]

def register(characters):
 retries=[
  "I remember your WURMPLE. No need to repeat the observation. Would you like another four-Pokemon field test?",
  "Your RATTATA has already cleared the interview. Ready to try that four-Pokemon battle again?",
  "The footsteps are safely recorded. No extra walking assignment. Shall we try our battle again?",
  "Your berry is already in the trail bread. No more ingredients needed. Want a rematch?",
  "Your ABRA has passed the audition. No need for another disappearing act. Shall we rehearse our battle again?",
  "I kept the rhythm you brought back. I am not making you walk in circles forever. Want another battle?",
  "The first-aid kit is stocked, thanks to you. No second donation. Shall we run the battle test again?",
  "We already asked NINCADA about the roots. I have kept the notes. Another four-Pokemon battle?",
  "The clasp test is done. You do not owe me another POKE BALL. Ready for a rematch?",
  "Your POTION is in the crew kit. That part is done. Want to try the four-Pokemon battle again?",
 ]
 rejoins=[
  "Ready for more fieldwork together? I have left room in the notebook for unexpected lunches.",
  "Heading out? I can walk with you. The roads are better with somebody worth talking to.",
  "Want company again? I have a new tune. You are under no obligation to pretend the humming is finished.",
  "Need a travelling baker? I have packed enough to make getting lost a catering decision.",
  "Shall we travel together again? I have rehearsed a perfectly ordinary entrance. It was difficult.",
  "Going somewhere? I would like to come along. That is the unedited version of the sentence.",
  "Ready to head out together? The tools are packed and the more alarming prototypes are staying here.",
  "Would you like company? I have questions about a local story, and no urgent need to invent the answers.",
  "Shall we go together again? I have mended the useful things. We can admire the unnecessary ones on the way.",
  "Want company on the road? I saved a blank page. We can decide what belongs on it together.",
 ]
 farewells=[
  "I will be in OLDALE. If a bush appears to be covered in notes, please check whether it is me.",
  "I will be back on ROUTE 2. Take your time. That is not courier advice; it is friend advice.",
  "I will be on ROUTE 3. If you hear humming, the song may have acquired a second line.",
  "Find me on ROUTE 104. I will save you something, unless MUNCHLAX has filed an exceptionally persuasive appeal.",
  "Back to VERMILION for me. No smoke, no vanishing. Just a rather grateful goodbye.",
  "I will be on ROUTE 102. Same sign, slightly less stationary poem. See you soon.",
  "I will be in SLATEPORT. Knock before entering anything labelled experimental. Especially my lunch box.",
  "Back to VERDANTURF. I will keep listening. Bring me a story if you feel like sharing one.",
  "I will be in CERULEAN. If a sleeve tears, you know where to find me. For other reasons too.",
  "I will be in CELADON. Keep noticing things. You do not have to turn every good moment into a masterpiece.",
 ]
 for i,c in enumerate(characters):c.update(retry=retries[i],rejoin=rejoins[i],farewell=farewells[i])
 # Retain trainer IDs 0..623 byte-for-byte; use previously unused defeat bits 0x770..779.
 p=ROOT/'src/data/trainers_kanto.party';s=p.read_text();s=s.split('\n=== TRAINER_KANTO_DATA_CAST_')[0].rstrip()+'\n'
 for i,c in enumerate(characters):
  n=c['name'];s+='\n=== TRAINER_KANTO_DATA_CAST_'+n.upper()+' ===\nName: '+n.upper()+'\nClass: Pkmn Trainer 1\nPic: Cast '+n.title()+'\nGender: '+('Male' if i<5 else 'Female')+'\nMusic: '+('Male' if i<5 else 'Female')+'\nDouble Battle: No\nAI: Check Bad Move / Try To Faint\n\n'
  for species in c['team']:
   s+=species+'\nLevel: '+str(c['level'])+'\nIVs: 15 HP / 15 Atk / 15 Def / 15 SpA / 15 SpD / 15 Spe\n'
   if species=='Smeargle':s+='- Tackle\n- Quick Attack\n- Sand Attack\n- Swift\n'
   s+='\n'
 p.write_text(s.rstrip()+"\n")
 # Native walkable placement: do not edit terrain or existing actors/scripts.
 layouts={l['id']:l for l in json.loads((ROOT/'data/layouts/layouts.json').read_text())['layouts']}
 headers=(ROOT/'src/data/tilesets/headers.h').read_text();attrs=(ROOT/'src/data/tilesets/metatiles.h').read_text()
 preferred=[(8,14),(12,60),(12,9),(20,60),(15,18),(40,10),(20,20),(13,9),(21,21),(21,20)]
 for i,c in enumerate(characters):
  p=ROOT/'data/maps'/c['map']/'map.json';m=json.loads(p.read_text());l=layouts[m['layout']];w,h=l['width'],l['height'];grid=struct.unpack('<'+'H'*(w*h),(ROOT/l['blockdata_filepath']).read_bytes());frlg=l.get('layout_version')=='frlg';banks=[]
  for key in ['primary_tileset','secondary_tileset']:
   symbol=l[key].replace('gTileset_Kanto_','gTileset_');block=re.search(r'const struct Tileset '+symbol+r' =\s*\{(.*?)\};',headers,re.S)[1];attribute=re.search(r'\.metatileAttributes = (\w+)',block)[1];path=re.search(r'const u16 '+attribute+r'\[\] = INCBIN_U16\("([^"]+)"',attrs)[1];raw=(ROOT/path).read_bytes();banks.append(struct.unpack('<'+('I' if frlg else 'H')*(len(raw)//(4 if frlg else 2)),raw))
  m['object_events']=[o for o in m['object_events'] if not o.get('script','').startswith('Cast_EventScript_Meet_')]
  occupied=set()
  for kind in ['object_events','warp_events','coord_events','bg_events']:
   for o in m[kind]:
    rx=max(2,int(o.get('movement_range_x',0)));ry=max(2,int(o.get('movement_range_y',0)))
    occupied.update((o['x']+dx,o['y']+dy) for dx in range(-rx,rx+1) for dy in range(-ry,ry+1))
  def walk(x,y):
   if not(2<=x<w-2 and 2<=y<h-2) or (x,y) in occupied:return False
   tile=grid[y*w+x];index=tile&1023;split=640 if frlg else 512;bank=index>=split;index-=split if bank else 0
   return not(tile&0xC00) and index<len(banks[bank]) and banks[bank][index]&(0x1ff if frlg else 0xff)==0
  choices=[(x,y) for y in range(3,h-3) for x in range(3,w-3) if all(walk(x+dx,y+dy) for dx in [0,1] for dy in [0,1])]
  assert choices,('No clear recruitment space',c['name'],c['map'])
  px,py=preferred[i];x,y=min(choices,key=lambda xy:abs(xy[0]-px)+abs(xy[1]-py));c['x']=x;c['y']=y;c['local_id']=len(m['object_events'])+1
  m['object_events'].append(dict(local_id='LOCALID_CAST_'+c['name'].upper(),type='object',graphics_id='OBJ_EVENT_GFX_CAST_'+c['name'].upper(),x=x,y=y,elevation=grid[y*w+x]>>12,movement_type='MOVEMENT_TYPE_FACE_DOWN',movement_range_x=0,movement_range_y=0,trainer_type='TRAINER_TYPE_NONE',trainer_sight_or_berry_tree_id='0',script='Cast_EventScript_Meet_'+c['name'].title(),flag=hex(0xB000+i)))
  p.write_text(json.dumps(m,indent=2)+'\n')
 save('data/cast/characters.json',characters)
 # All eight expressions retain their supplied tile and palette order.
 rows=[];graphics=[]
 for i,c in enumerate(characters):
  n=c['name'];N=n.title();graphics += [f'const u8 ALIGNED(4) gCastPortrait_{N}[] = INCBIN_U8("graphics/cast_portraits/{n}_expressions.bin");',f'const u16 gCastPalette_{N}[] = INCBIN_U16("graphics/cast_portraits/{n}_palette.bin");']
  fields=[f'.graphics = OBJ_EVENT_GFX_CAST_{n.upper()}',f'.trainer = CAST_TRAINER_{n.upper()}',f'.requirement = CAST_REQ_{c["requirement"].upper()}',f'.value = '+(str(c['value']) if c['requirement']=='steps' else ('SPECIES_' if c['requirement']=='species' else 'ITEM_')+c['value']),f'.walkSlot = {0 if n=="ashe" else 1}']
  for key in ['name','intro','request','ready','retry','join','rejoin','farewell']:fields.append('.'+key+' = '+ctext(n.upper() if key=='name' else c[key],None if key=='name' else n))
  fields += ['.lore = {'+', '.join(ctext(t,n) for e,t in c['lore'])+'}', '.loreExpression = {'+', '.join(str(EXPRESSIONS.index(e)) for e,t in c['lore'])+'}']
  rows.append('    {'+',\n     '.join(fields)+'},')
 (ROOT/'src/data/cast_characters.h').write_text('\n'.join(graphics)+'\nstatic const u8 *const sCastPortraits[] = {'+', '.join('gCastPortrait_'+n.title() for n in NAMES)+'};\nstatic const u16 *const sCastPortraitPalettes[] = {'+', '.join('gCastPalette_'+n.title() for n in NAMES)+'};\nstatic const struct CastCharacter sCastCharacters[] = {\n'+'\n'.join(rows)+'\n};\n')
 scripts=[]
 for i,c in enumerate(characters):
  N=c['name'].title();prefix='Cast_EventScript_Meet_'+N
  scripts += [prefix+'::','\tlock','\tfaceplayer',f'\tsetvar VAR_0x8004, {i}','\tcallnative Script_CastRecruitStatus','\tgoto_if_eq VAR_RESULT, 2, Cast_EventScript_AfterBattle',f'\tgoto_if_eq VAR_RESULT, 1, {prefix}_Challenge','\tmsgbox gStringVar4, MSGBOX_DEFAULT','\tgoto Cast_EventScript_End',prefix+'_Challenge::','\tmsgbox gStringVar4, MSGBOX_YESNO','\tgoto_if_eq VAR_RESULT, NO, Cast_EventScript_End','\tcallnative Script_CastCommitRequirement','\tgoto_if_eq VAR_RESULT, FALSE, Cast_EventScript_End',f'\ttrainerbattle_no_intro CAST_TRAINER_{N.upper()}, Cast_Text_{N}_Defeat','\tgoto Cast_EventScript_AfterBattle',f'Cast_Text_{N}_Defeat::','\t.string "'+wrapped(c['defeat']).replace('"','\\"')+'"','']
 scripts += ['Cast_EventScript_AfterBattle::','\tcallnative Script_CastAfterBattle','\tgoto_if_eq VAR_RESULT, FALSE, Cast_EventScript_End','\tmsgbox gStringVar4, MSGBOX_YESNO','\tgoto_if_eq VAR_RESULT, NO, Cast_EventScript_End','\tcallnative Script_CastJoin','\tgoto_if_eq VAR_RESULT, FALSE, Cast_EventScript_Unavailable','\tgoto Cast_EventScript_End',
 'Cast_EventScript_Unavailable::','\tmsgbox Cast_Text_Unavailable, MSGBOX_DEFAULT','Cast_EventScript_End::','\tcallnative Script_CastHidePortrait','\trelease','\tend',
 'Cast_EventScript_Companion::','\tlockall','\tfacefollowernpc','\tmultichoice 0, 0, MULTI_PIP_COMPANION, FALSE','\tgoto_if_eq VAR_RESULT, 2, Cast_EventScript_Roster','\tgoto_if_eq VAR_RESULT, 1, Cast_EventScript_Dismiss','\tgoto_if_ne VAR_RESULT, 0, Cast_EventScript_Stay','\tcallnative Script_PipChooseDialogue','\tgoto_if_eq VAR_RESULT, FALSE, Cast_EventScript_Stay','\tmsgbox gStringVar4, MSGBOX_DEFAULT','\tgoto Cast_EventScript_Stay',
 'Cast_EventScript_Dismiss::','\tmsgbox Cast_Text_Dismiss, MSGBOX_YESNO','\tgoto_if_eq VAR_RESULT, NO, Cast_EventScript_Stay','\tcallnative Script_CastFarewell','\tmsgbox gStringVar4, MSGBOX_DEFAULT','\tcallnative Script_CastDismiss','\tgoto Cast_EventScript_Stay',
 'Cast_EventScript_Roster::','\tmultichoicegrid 0, 0, MULTI_CAST_ROSTER, 3, FALSE','\tgoto_if_eq VAR_RESULT, MULTI_B_PRESSED, Cast_EventScript_Stay','\tgoto_if_eq VAR_RESULT, 11, Cast_EventScript_Stay','\tcallnative Script_CastSwitchRoster','\tgoto_if_ne VAR_RESULT, FALSE, Cast_EventScript_Stay','\tmsgbox Cast_Text_Locked, MSGBOX_DEFAULT','Cast_EventScript_Stay::','\tcallnative Script_CastHidePortrait','\treleaseall','\tend',
 'Cast_Text_Unavailable::','\t.string "Your current escort needs you.\\nThere is no room to change company\\lright now.$"','Cast_Text_Locked::','\t.string "Befriend that trainer first.\\nYour current companion will stay.$"','Cast_Text_Dismiss::','\t.string "Part ways for now?\\nThey will return to where you met.$"']
 if (ROOT/'data/bonds/journal.inc').exists():
  scripts.insert(scripts.index('\tmultichoice 0, 0, MULTI_PIP_COMPANION, FALSE')+1,'\tgoto_if_eq VAR_RESULT, 4, Bonds_EventScript_Journal')
 (ROOT/'data/cast/recruitment.inc').write_text('\n'.join(scripts)+'\n')

def dialogue(characters):
 from cast_voices import VOICE
 source=(ROOT/'src/data/pip_memory_catalogue.h').read_text().split('sPipMemoryCatalogue[] = {',1)[1].split('};',1)[0]
 symbols=re.findall(r'^\s*(\w+),',source,re.M)
 assert len(symbols)==408
 objects=['food','game','computer','machine','blueprint','burglary','dishes','food','privacy','food','art','phone','machine','shop','food','cup','machine','tools','book','shop']
 world=['home','food','cave','bike','food','privacy','rest','home','privacy','home','food','legend','scientist','phone','progress','scientist','sea','burglary','grass','art','sea']
 towns=[k for k in VOICE if k.isupper()]
 def subject(symbol):
  if symbol=='NULL':return None
  if symbol.startswith('sPipLivingKanto_'):return 'scene'+symbol.rsplit('_',1)[1]
  if symbol.startswith('sPipKantoObject_'):return objects[int(symbol.rsplit('_',1)[1])]
  if symbol.startswith('World_Pip_'):
   n=int(symbol.rsplit('_',1)[1]);return world[n] if n<21 else 'wild_offer'
  for town in sorted(towns,key=len,reverse=True):
   if town in symbol:return town
  if symbol.startswith('sPipProgress'):
   return 'progress' if int(symbol.removeprefix('sPipProgress'))<4 else 'later_progress'
  if symbol=='sPipChampion':return 'champion'
  if 'PipNPC' in symbol:return ['road','hiker','fisher','nurse','scientist','sailor'][int(symbol[-1])]
  mappings={'PictureBook':'picturebook','Book':'book','Vase':'vase','Trash':'trash','Shop':'shop','Blueprint':'blueprint','Hiker':'hiker','Fisher':'fisher','Sailor':'sailor','Scientist':'scientist','Nurse':'nurse','Underwater':'underwater','Bike':'bike','Surf':'sea'}
  for word,key in mappings.items():
   if word in symbol:return key
  if 'sPipAdventure_' in symbol:
   person=symbol.removeprefix('sPipAdventure_')
   if person in VOICE:return person
  upper=symbol.upper()
  if 'ROUTE' in upper:
   match=re.search(r'(?:ROUTE_|ROUTE)(\d+)',upper);n=int(match[1]) if match else 0
   if n in [105,106,107,108,109,118,122,123,124,125,126,127,128,129,130,131,132,133,134,19,20,21]:return 'sea'
   if n in [119,120,121]:return 'rain'
   if n in [111,113]:return 'sand' if n==111 else 'road'
   return 'grass' if upper.endswith('_1') else 'road'
  if any(x in upper for x in ['PYRE','TOWER','MANSION']):return 'grave'
  if any(x in upper for x in ['AQUA_HIDEOUT','MAGMA_HIDEOUT','ROCKET','SILPH_CO']):return 'rocket'
  if any(x in upper for x in ['WOODS','FOREST','SAFARI']):return 'forest'
  if any(x in upper for x in ['FIERY','CHIMNEY','JAGGED']):return 'heat'
  if any(x in upper for x in ['SHIP','ISLAND','SHOAL']):return 'sea'
  if any(x in upper for x in ['ORIGIN','PILLAR','SEALED']):return 'legend'
  if 'NEW_MAUVILLE' in upper or 'POWER_PLANT' in upper:return 'machine'
  if 'VICTORY' in upper:return 'later_progress'
  if any(x in upper for x in ['CAVE','TUNNEL','FALLS','MT_MOON']):return 'cave'
  return 'rest'
 keys=[subject(s) for s in symbols]
 topicNames=['road','home','work','art','care','people','rest','book','food','privacy','grave']
 def topic(key):
  if key in topicNames:return key
  if key in ['LITTLEROOT_TOWN','OLDALE_TOWN','PALLET_TOWN','FORTREE_CITY','SOOTOPOLIS_CITY','PACIFIDLOG_TOWN']:return 'home'
  if key in ['computer','machine','blueprint','tools','scientist','RUSTBORO_CITY','MAUVILLE_CITY','MOSSDEEP_CITY','CINNABAR_ISLAND']:return 'work'
  if key in ['game','LILYCOVE_CITY','DEWFORD_TOWN','CERULEAN_CITY','CELADON_CITY','scene2']:return 'art'
  if key in ['nurse','progress','later_progress','champion','EVER_GRANDE_CITY','INDIGO_PLATEAU','scene3']:return 'care'
  if key in ['VERDANTURF_TOWN','LAVARIDGE_TOWN','scene11']:return 'rest'
  if key in ['book','picturebook','PEWTER_CITY']:return 'book'
  if key in ['food','SLATEPORT_CITY','scene0']:return 'food'
  if key in ['burglary','rocket','privacy']:return 'privacy'
  if key=='LAVENDER_TOWN':return 'grave'
  if key in ['hiker','fisher','sailor','gym','wild_offer','SAFFRON_CITY'] or key in ['BROCK','MISTY','LT_SURGE','ERIKA','KOGA','SABRINA','BLAINE','GIOVANNI','PROF_OAK','BLUE','LORELEI','BRUNO','AGATHA','LANCE']:return 'people'
  return 'road'
 triggers=[['home','work','rest','people','care','home'],['home','road','people','rest','care','road'],['art','food','art','home','people','art'],['food','home','work','food','people','food'],['art','people','privacy','care','art','people'],['book','art','people','home','care','art'],['work','home','work','privacy','care','rest'],['book','art','grave','people','book','road'],['art','work','people','food','care','art'],['home','art','grave','people','art','road']]
 code=['#define CAST_SOURCE_COUNT '+str(len(symbols)), 'static const struct CastComment sCastComments[CAST_COUNT][CAST_SOURCE_COUNT] = {'];memory=[];review=[]
 for who,c in enumerate(characters):
  records=[];ids=[];first={};code.append(' {')
  for i,key in enumerate(keys):
   if key is None:
    code.append('  {NULL, 0, 0},');ids.append(i);records.append(None);continue
   emotion,text=VOICE[key][who];t=topic(key);bit=1<<topicNames.index(t)
   if '~' in text:
    emotion,text=text.split('~',1)
   code.append('  {'+ctext(text,c['name'])+', '+str(EXPRESSIONS.index(emotion))+', '+hex(bit)+'}, // '+str(i)+' '+symbols[i])
   ids.append(first.setdefault(text,i));records.append(dict(source_id=i,source=symbols[i],subject=key,expression=emotion,text=text,memory_id=ids[-1],topic=t))
  code.append(' },');memory.append(ids);review.append(dict(character=c['name'],unique_comments=len(first),comments=records))
 code += ['};','static const u16 sCastContextMemoryId[CAST_COUNT][CAST_SOURCE_COUNT] = {']+[' {'+', '.join(map(str,ids))+'},' for ids in memory]+['};','static const u16 sCastLoreTriggers[CAST_COUNT][6] = {']+[' {'+', '.join(hex(1<<topicNames.index(k)) for k in row)+'},' for row in triggers]+['};']
 (ROOT/'src/data/cast_dialogue.h').write_text('\n'.join(code)+'\n')
 save('data/cast/dialogue_review.json',review)
 save('data/cast/dialogue_contract.json',dict(source_slots=symbols,expressions=EXPRESSIONS,characters=NAMES,topics=topicNames,memory_capacity=448,semantics='Each character has an independent spent bit. Offering/declining spends the canonical wording; accepting a pending offer is allowed once. No generic cycling.'))
 print('Built',sum(c['unique_comments'] for c in review),'distinct voiced reactions across',len(symbols)-symbols.count('NULL'),'supported Pip contexts per character, plus 60 ordered lore revelations.')

if __name__=='__main__':
 characters=profiles()
 for c in characters:c['life_stage']='adult'
 register(characters);dialogue(characters)
 if (ROOT/'data/bonds/journal.inc').exists():
  import build_bonds
  build_bonds.main()

