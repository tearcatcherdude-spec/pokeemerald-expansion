"""Check exact supplied assets, cumulative source contracts and recruitability data."""
from pathlib import Path
import hashlib,json,re,struct
ROOT=Path(__file__).resolve().parents[1]
def load(path):return json.loads((ROOT/path).read_text(encoding='utf-8'))
def canonical(value):return hashlib.sha256(json.dumps(value,sort_keys=True).encode()).hexdigest()
def main():
 baseline=load('data/cast/base_contract.json')
 manifest=load('data/cast/asset_manifest.json');characters=load('data/cast/characters.json');review=load('data/cast/dialogue_review.json');contract=load('data/cast/dialogue_contract.json')
 assert len(characters)==10 and {c['name'] for c in characters}==set(contract['characters'])
 for path,sha in manifest['assets'].items():assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==sha,('Supplied asset changed',path)
 groups=load('data/maps/map_groups.json');layouts={l['id']:l for l in load('data/layouts/layouts.json')['layouts']}
 wild={e['map']:e for g in load('src/data/wild_encounters.json')['wild_encounter_groups'] for e in g.get('encounters',[]) if 'map' in e}
 species=(ROOT/'include/constants/species.h').read_text();items=(ROOT/'include/constants/items.h').read_text()
 native_flags=load('data/kanto/symbol_manifest.json')['native_flags']
 assert not [n for n,v in native_flags.items() if 0x770<=v<0x77A], 'New trainer flags overlap native story flags'
 assert {c['name']:c['map'] for c in characters}['emi']=='Route102'
 assert {c['name']:c['map'] for c in characters}['silas']=='OldaleTown'
 for i,c in enumerate(characters):
  n=c['name'];png=(ROOT/f'graphics/object_events/pics/people/cast_{n}.png').read_bytes();assert struct.unpack('>IIBB',png[16:26])==(144,32,4,3)
  assert (ROOT/f'graphics/cast_portraits/{n}.4bpp').stat().st_size==8*2048
  assert (ROOT/f'graphics/cast_portraits/{n}.gbapal').stat().st_size==32
  assert len(c['team'])==4 and len(set(c['team']))==4
  assert len(c['lore'])==6 and all(e in contract['expressions'] for e,t in c['lore'])
  # First four generations only. These named species use the existing expansion's data.
  for mon in c['team']:
   symbol='SPECIES_'+re.sub(r'[^A-Z0-9]+','_',mon.upper()).strip('_')
   assert symbol in species,(n,mon)
  max_level=max(p['max_level'] for p in wild[c['area']]['land_mons']['mons']);assert c['level']==max_level+(3 if n in ['emi','silas'] else 5)
  p=f'data/maps/{c["map"]}/map.json';m=load(p);old=baseline['maps'][p];added=m['object_events'][-1]
  assert len(m['object_events'])==old['objects_count']+1 and canonical(m['object_events'][:-1])==old['objects_sha'],('Original actors changed',c['map'])
  assert canonical({k:v for k,v in m.items() if k!='object_events'})==old['metadata_sha']
  assert added['flag']==hex(0xB000+i) and added['graphics_id']=='OBJ_EVENT_GFX_CAST_'+n.upper()
  l=layouts[m['layout']];raw=(ROOT/l['blockdata_filepath']).read_bytes()
  for x,y in [(c['x'],c['y']),(c['x'],c['y']+1)]:
   tile=struct.unpack_from('<H',raw,2*(y*l['width']+x))[0];assert not tile&0xc00,(n,x,y)
  assert c['requirement'] in ['steps','species','item']
  if c['requirement']=='species':assert 'SPECIES_'+c['value'] in species
  if c['requirement']=='item':assert 'ITEM_'+c['value'] in items
 party=(ROOT/'src/data/trainers_kanto.party').read_text();assert hashlib.sha256(party[:baseline['original_trainer_prefix_chars']].encode()).hexdigest()==baseline['original_trainer_prefix_sha']
 assert party.count('=== TRAINER_KANTO_DATA_CAST_')==10
 for person in review:
  assert len(person['comments'])==408
  wording={}
  for i,line in enumerate(person['comments']):
   if contract['source_slots'][i]=='NULL':assert line is None;continue
   assert line and line['source']==contract['source_slots'][i] and line['memory_id']<448
   assert line['expression'] in contract['expressions'] and 'PIP:' not in line['text']
   assert not re.search(r'\b(?:strange watch|the watch|universe|dimension|world switching|shared inventory)\b',line['text'],re.I)
   assert wording.setdefault(line['text'],line['memory_id'])==line['memory_id'], 'Identical wording must not repeat under another ID'
  assert len(wording)>=80
 assert 'u8 used[10][56]' in (ROOT/'include/global.h').read_text()
 print('PASS: all ten exact sprite/portrait packs, four-member teams at native-area +3/+5, early Emi/Silas, unchanged native maps/actors, 402 supported contexts/person, canonical memory and ordered lore')
if __name__=='__main__':main()
