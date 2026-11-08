import json,struct,subprocess,re
from pathlib import Path
r=Path(__file__).resolve().parents[1]
g=json.loads((r/'data/maps/map_groups.json').read_text());layouts={l['id']:l for l in json.loads((r/'data/layouts/layouts.json').read_text())['layouts']};names=g['gMapGroup_ParallelWatch'];maps={}
for n in names:
 m=json.loads((r/f'data/maps/{n}/map.json').read_text());maps[m['id']]=m;l=layouts[m['layout']]
 assert m['parallel_watch'] and l['parallel_watch'] and l['layout_version']=='frlg'
 assert len((r/l['blockdata_filepath']).read_bytes())==l['width']*l['height']*2
 assert len(m['object_events'])<=12
 for e in m['object_events']+m['warp_events']+m['bg_events']:
  assert 0<=e['x']<l['width'] and 0<=e['y']<l['height'],(n,e)
 for e in m['object_events']:
  tile=struct.unpack_from('<H',(r/l['blockdata_filepath']).read_bytes(),(e['y']*l['width']+e['x'])*2)[0]
  assert not tile&0xc00,(n,'NPC over blocked tile',e)
  assert e['elevation']==tile>>12,(n,'NPC elevation',e)
 assert not m['coord_events']
for m in maps.values():
 for w in m['warp_events']:
  assert w['dest_map'] in maps,(m['name'],w)
  assert 0<=int(w['dest_warp_id'])<len(maps[w['dest_map']]['warp_events']),(m['name'],w)
 for c in m['connections'] or []:
  other=maps[c['map']];opposite={'up':'down','down':'up','left':'right','right':'left'}[c['direction']]
  assert any(o['map']==m['id'] and o['direction']==opposite and o['offset']==-c['offset'] for o in other['connections'] or [])
for p in ['src/starter_choose.c','src/starter_choose_expanded.c','src/battle_setup.c']:
 assert (r/p).read_bytes()==subprocess.check_output(['git','show','HEAD:'+p],cwd=r),p
print(f'PASS: {len(maps)} maps, valid reciprocal connections, all warps resolve, event limits, original starters unchanged')
