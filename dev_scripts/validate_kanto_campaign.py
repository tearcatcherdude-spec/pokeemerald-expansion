"""Validate imported campaign topology and cumulative-save source contracts."""
from pathlib import Path
import json,re,struct
ROOT=Path(__file__).resolve().parents[1]
def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def main():
 manifest=load('data/kanto/maps_manifest.json');groups=load('data/maps/map_groups.json');layouts={l['id']:l for l in load('data/layouts/layouts.json')['layouts']};maps={}
 assert len(groups['group_order'])<128
 for g in groups['group_order']:assert len(groups[g])<128,g
 for original,name in manifest['maps'].items():
  m=load('data/maps/'+name+'/map.json');source=load('data/maps/'+original+'/map.json');maps[m['id']]=m;l=layouts[m['layout']]
  assert m['parallel_watch'] and l['parallel_watch'] and l['layout_version']=='frlg'
  assert len((ROOT/l['blockdata_filepath']).read_bytes())==l['width']*l['height']*2,name
  assert (ROOT/'data/kanto/maps'/original/'scripts.inc').is_file()
  for field in ['object_events','warp_events','coord_events','bg_events']:
   # Original scripts intentionally park some hidden actors offscreen.
   for e in m[field]:
    if not 0<=e['x']<l['width'] or not 0<=e['y']<l['height']:
     assert any(o['x']==e['x'] and o['y']==e['y'] for o in source[field]),(name,field,e)
 for m in maps.values():
  for w in m['warp_events']:
   if w['dest_map'] in ['MAP_DYNAMIC','MAP_UNDEFINED']:continue
   assert w['dest_map'] in maps,(m['name'],w)
   num=int(w['dest_warp_id']);assert num<0 or num<len(maps[w['dest_map']]['warp_events']),(m['name'],w)
  for c in m['connections'] or []:assert c['map'] in maps,(m['name'],c)
 labels={}
 for p in (ROOT/'data/kanto').rglob('*.inc'):
  for label in re.findall(r'^(\w+)::?',p.read_text(encoding='utf-8'),re.M):
   assert label not in labels,(label,p,labels.get(label));labels[label]=p
 for m in maps.values():assert m.get('shared_scripts_map',m['name'])+'_MapScripts' in labels,m['name']
 for gym in ['PewterCity','CeruleanCity','VermilionCity','CeladonCity','FuchsiaCity','SaffronCity','CinnabarIsland','ViridianCity']:
  assert any(n.startswith('Kanto'+gym+'_Gym') for n in manifest['maps'].values()),gym
 print(f'PASS: {len(maps)} campaign maps, all warp/connection destinations, layouts, eight gyms, script roots and unique labels')
if __name__=='__main__':main()
