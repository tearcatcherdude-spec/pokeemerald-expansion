"""Author living-world pairs on verified native walkable tiles; no terrain edits."""
from pathlib import Path
import json,re,struct,textwrap
ROOT=Path(__file__).resolve().parents[1]
# map, premise, partner before, resolution, return dialogue, reward, Pip
SCENES=[
('KantoPewterCity','I am sorting rocks by how much they look like BROCK. Ask my sister if this one counts.','He has brought me seventeen rocks and one potato.','That is definitely a potato. Take this. He tried to put it in the rock collection.','The potato has been moved to the lunch collection.','POKE_BALL','Science has made an important distinction. Lunch is not a mineral.'),
('KantoCeruleanCity','I am inventing a waterproof umbrella. My friend is handling testing.','I am waiting for a non-waterproof umbrella for comparison.','We tested it. It is an umbrella. Please take our emergency drying supplies.','Our next invention is a towel with fewer features.','POTION','An umbrella that stops rain. They could be onto something.'),
('KantoVermilionCity','I wrote a sea shanty. Ask my friend why nobody sings the second verse.','The second verse is just directions to his house.','We replaced the second verse with humming. Here, thanks for listening.','The chorus is now legally distinct from my address.','SUPER_POTION','I learned the tune and where he keeps the spare key.'),
('KantoLavenderTown','We are planting flowers for an old friend. Could you ask what color she liked?','She loved yellow flowers. She said they looked like little suns.','Yellow it is. Thank you for asking. Please take a berry for the road.','The flowers are doing well. We come by every week.','ORAN_BERRY','We can help water them before we go.'),
('KantoCeladonCity','I am teaching my friend to save money. Please ask how lesson one went.','I bought a very expensive notebook to track my savings.','We have agreed to use both sides of the paper. Here, this was our stationery budget.','Lesson two is walking past the department store.','GREAT_BALL','The notebook has to work very hard now.'),
('KantoFuchsiaCity','I made a nature guide. Ask my friend which animal I missed.','There is no entry for people who lose their nature guides.','A common local species! Thanks. Take one of our field supplies.','The guide now includes a map back to this bench.','REPEL','I hope our entry says mostly harmless.'),
('KantoSaffronCity','My friend claims to predict the future. Ask what I am having for lunch.','Lunch. I predict lunch. I am starting with the reliable visions.','An excellent prediction. Please accept this peer-review sample.','Tomorrow we are predicting breakfast.','FRESH_WATER','I predict that I will also want lunch.'),
('KantoCinnabarIsland_PokemonLab_Entrance','My friend says the volcano is asleep. Ask if we should whisper.','It is geology. It cannot hear us. I still said good morning.','We agreed to be polite anyway. Here is something for the heat.','Good manners cost nothing. Unlike volcano insurance.','BURN_HEAL','I will keep my geological opinions quiet.'),
('KantoRoute3','I packed everything for this hike. Ask my brother what I forgot.','He packed three pillows and no water.','Water! Right. We have a spare snack, though. Please take it.','We are walking back to buy water. The pillows are staying.','ORAN_BERRY','Three pillows is an ambitious hiking strategy.'),
('KantoRoute6','I challenged my friend to a staring contest. Ask who is winning.','Neither of us remembers who started. I think it was Tuesday.','We declared a draw. Take this prize before somebody asks for a rematch.','We are trying a blinking contest. Much faster.','AWAKENING','Finally, a battle I am qualified to lose.'),
('KantoRoute15','My friend is making bird calls. Please ask which bird that was.','That was a bicycle brake. I am still practicing the birds.','The PIDGEY seemed impressed. Here, take this for being our audience.','We have perfected the rare squeaking bicycle.','GREAT_BALL','Somewhere a bicycle is answering.'),
('KantoOneIsland_PokemonCenter_1F','I started a relaxing club. Ask our treasurer how membership is going.','We have two members. Neither remembers which one is treasurer.','We voted to have no dues. Here, take the entire refreshment fund.','The next meeting is whenever we sit down again.','SODA_POP','This club has a very reasonable attendance policy.')]
def main():
 def read(p):return (ROOT/p).read_text(encoding='utf-8')
 layouts={l['id']:l for l in json.loads(read('data/layouts/layouts.json'))['layouts']}
 headers=read('src/data/tilesets/headers.h');attrs=read('src/data/tilesets/metatiles.h')
 scripts=[];records=[];pip=[]
 def text(label,t):
  wrapped=textwrap.wrap(t,33,break_long_words=False);s=wrapped[0]+''.join(('\\n' if i==1 else '\\l')+line for i,line in enumerate(wrapped[1:],1))+'$';scripts.extend([label+'::','\t.string "'+s.replace('"','\\"')+'"',''])
 for i,row in enumerate(SCENES):
  name,intro,before,resolved,after,item,comment=row;p=ROOT/'data/maps'/name/'map.json';m=json.loads(p.read_text(encoding='utf-8'));m['object_events']=[o for o in m['object_events'] if not o.get('script','').startswith('LivingKanto_Scene')];l=layouts[m['layout']];grid=struct.unpack('<'+'H'*(l['width']*l['height']),(ROOT/l['blockdata_filepath']).read_bytes());w,h=l['width'],l['height'];banks=[]
  for key in ['primary_tileset','secondary_tileset']:
   original=l[key].replace('gTileset_Kanto_','gTileset_');block=re.search(r'const struct Tileset '+original+r' =\s*\{(.*?)\};',headers,re.S)[1];symbol=re.search(r'\.metatileAttributes = (\w+)',block)[1];path=re.search(r'const u16 '+symbol+r'\[\] = INCBIN_U16\("([^"]+)"',attrs)[1];b=(ROOT/path).read_bytes();banks.append(struct.unpack('<'+'I'*(len(b)//4),b))
  occupied={(e['x']+dx,e['y']+dy) for typ in ['object_events','warp_events','coord_events','bg_events'] for e in m[typ] for dx in range(-1,2) for dy in range(-1,2)}
  def walk(x,y):
   if not (2<=x<w-2 and 2<=y<h-2) or (x,y) in occupied:return False
   tile=grid[y*w+x];idx=tile&1023;bank=idx>=640;idx-=640 if bank else 0
   return not(tile&0xC00) and idx<len(banks[bank]) and banks[bank][idx]&0x1FF==0
  candidates=[(x,y) for y in range(3,h-3) for x in range(3,w-4) if all(walk(x+dx,y+dy) for dx in [0,1] for dy in [0,1])]
  assert candidates, name
  x,y=min(candidates,key=lambda xy:abs(xy[0]-w//2)+abs(xy[1]-h//2));prefix='LivingKanto_Scene'+str(i);seen=hex(0xA8D0+i);done=hex(0xA8E0+i)
  for j,gfx in enumerate(['OBJ_EVENT_GFX_YOUNGSTER_FRLG','OBJ_EVENT_GFX_WOMAN_1_FRLG']):
   m['object_events'].append({'local_id':'LOCALID_LIVING_KANTO_'+str(i)+'_'+str(j),'graphics_id':gfx,'x':x+j,'y':y,'elevation':grid[y*w+x+j]>>12,'movement_type':'MOVEMENT_TYPE_FACE_RIGHT' if j==0 else 'MOVEMENT_TYPE_FACE_LEFT','movement_range_x':0,'movement_range_y':0,'trainer_type':'TRAINER_TYPE_NONE','trainer_sight_or_berry_tree_id':'0','script':prefix+('_A' if j==0 else '_B'),'flag':'0'})
  p.write_text(json.dumps(m,indent=2)+'\n',encoding='utf-8',newline='\n')
  scripts.extend([prefix+'_A::','\tlock','\tfaceplayer','\tgoto_if_set '+done+', '+prefix+'_Done','\tsetflag '+seen,'\tmsgbox '+prefix+'_Intro, MSGBOX_DEFAULT','\trelease','\tend','',prefix+'_B::','\tlock','\tfaceplayer','\tgoto_if_set '+done+', '+prefix+'_Done','\tgoto_if_unset '+seen+', '+prefix+'_Before','\tmsgbox '+prefix+'_Resolve, MSGBOX_DEFAULT','\tgiveitem ITEM_'+item+', 1','\tgoto_if_eq VAR_RESULT, FALSE, LivingKanto_BagFull','\tsetflag '+done,'\trelease','\tend','',prefix+'_Before::','\tmsgbox '+prefix+'_BeforeText, MSGBOX_DEFAULT','\trelease','\tend','',prefix+'_Done::','\tmsgbox '+prefix+'_After, MSGBOX_DEFAULT','\trelease','\tend',''])
  for label,t in [('Intro',intro),('BeforeText',before),('Resolve',resolved),('After',after)]:text(prefix+'_'+label,t)
  records.append({'map':name,'x':x,'y':y,'seen_flag':seen,'reward_flag':done,'reward':'ITEM_'+item,'pip':comment});pip.append((prefix,comment))
 scripts.extend(['LivingKanto_BagFull::','\tmsgbox LivingKanto_BagFullText, MSGBOX_DEFAULT','\trelease','\tend','']);text('LivingKanto_BagFullText','Your BAG looks full. Come back when there is room. I will keep this for you.')
 (ROOT/'data/kanto/living_scenes.inc').write_text('\n'.join(scripts),newline='\n');(ROOT/'data/kanto/living_scenes.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf-8')
 p=ROOT/'data/event_scripts.s';s=p.read_text(encoding='utf-8');inc='\t.include "data/kanto/living_scenes.inc"\n'
 if inc not in s:s=s.replace('\t.include "data/kanto/campaign.inc"','\t.include "data/kanto/campaign.inc"\n'+inc.rstrip());p.write_text(s,encoding='utf-8',newline='\n')
 print('Added',len(records),'paired scenes,',len(records)*2,'actors, and one-time rewards on verified walkable tiles')
if __name__=='__main__':main()
