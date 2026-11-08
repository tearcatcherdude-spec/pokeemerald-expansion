"""Import the existing Kanto campaign with isolated persistent IDs.
Original source maps remain untouched for alternate builds. Watch map IDs stay stable.
"""
from pathlib import Path
import json,re,copy
ROOT=Path(__file__).resolve().parents[1]
def load(p): return json.loads((ROOT/p).read_text(encoding='utf-8'))
def save(p,v):
 p=ROOT/p;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,indent=2)+'\n',encoding='utf-8',newline='\n')
def main():
 groups=load('data/maps/map_groups.json')
 originals={}
 for group in groups['group_order']:
  if group.startswith('gMapGroup_KantoCampaign'): continue
  for name in groups[group]:
   p=ROOT/'data/maps'/name/'map.json'
   m=json.loads(p.read_text(encoding='utf-8'))
   if m.get('region')=='REGION_KANTO' and not m.get('parallel_watch'): originals[name]=m
 stable={'PalletTown_Frlg':'WatchPallet','Route1_Frlg':'WatchRoute1','ViridianCity_Frlg':'WatchViridian','PalletTown_PlayersHouse_1F_Frlg':'WatchHouse1F','PalletTown_PlayersHouse_2F_Frlg':'WatchHouse2F','PalletTown_RivalsHouse_Frlg':'WatchNeighbor','PalletTown_ProfessorOaksLab_Frlg':'WatchLab','ViridianCity_PokemonCenter_1F_Frlg':'WatchCenter','ViridianCity_Mart_Frlg':'WatchMart','ViridianCity_House_Frlg':'WatchHouse','ViridianCity_School_Frlg':'WatchSchool'}
 assert set(stable)<=set(originals),set(stable)-set(originals)
 names={n:stable.get(n,'Kanto'+n.removesuffix('_Frlg')) for n in originals}
 ids={m['id']:(load('data/maps/'+stable[n]+'/map.json')['id'] if n in stable else 'MAP_KANTO_'+m['id'][4:]) for n,m in originals.items()}
 symbols=load('data/kanto/symbol_manifest.json')['renamed']|ids
 pattern=re.compile(r'\b(?:'+ '|'.join(map(re.escape,sorted(symbols,key=len,reverse=True)))+r')\b')
 def rewrite(s):return pattern.sub(lambda m:symbols[m[0]],s)
 layouts=load('data/layouts/layouts.json'); oldlayouts={l['id']:l for l in layouts['layouts'] if l.get('layout_version')=='frlg' and not l.get('parallel_watch')}
 used={m['layout'] for m in originals.values()}
 layoutids={i:'LAYOUT_KANTO_'+i[7:] for i in used}
 layouts['layouts']=[l for l in layouts['layouts'] if not l.get('kanto_campaign')]
 for i in sorted(used):
  l=copy.deepcopy(oldlayouts[i]);l['id']=layoutids[i];l['name']='Kanto'+l['name'];l['parallel_watch']=True;l['kanto_campaign']=True
  l['primary_tileset']=l['primary_tileset'].replace('gTileset_','gTileset_Kanto_');l['secondary_tileset']=l['secondary_tileset'].replace('gTileset_','gTileset_Kanto_');layouts['layouts'].append(l)
 save('data/layouts/layouts.json',layouts)
 count=0
 for n,m in originals.items():
  d=json.loads(rewrite(json.dumps(m)));d['id']=ids[m['id']];d['name']=names[n];d['layout']=layoutids[m['layout']];d['parallel_watch']=True;d['kanto_campaign']=True
  # The Emerald shop interface uses its own employee preview graphic.
  for o in d.get('object_events',[]):
   if o.get('graphics_id')=='OBJ_EVENT_GFX_CLERK':o['graphics_id']='OBJ_EVENT_GFX_MART_EMPLOYEE'
  save('data/maps/'+names[n]+'/map.json',d)
  src=ROOT/'data/maps'/n/'scripts.inc'
  target=ROOT/'data/kanto/maps'/n/'scripts.inc';target.parent.mkdir(parents=True,exist_ok=True)
  target.write_text(rewrite(src.read_text(encoding='utf-8')).replace(n+'_MapScripts',names[n]+'_MapScripts'),encoding='utf-8',newline='\n');count+=len(d.get('object_events',[]))
 # Append groups; never reorder any existing map or group.
 existing=[g for g in groups['group_order'] if not g.startswith('gMapGroup_KantoCampaign')]
 for g in list(groups):
  if g.startswith('gMapGroup_KantoCampaign'):del groups[g]
 groups['group_order']=existing
 for g in existing:
  imported=[names[n] for n in groups[g] if n in originals and n not in stable]
  if imported:
   new='gMapGroup_KantoCampaign'+g.removeprefix('gMapGroup_');groups['group_order'].append(new);groups[new]=imported
 assert len(groups['group_order'])<128
 save('data/maps/map_groups.json',groups)
 # Copy campaign-only common scripts, preserving their unique native labels.
 events=(ROOT/'data/event_scripts.s').read_text(encoding='utf-8'); start=events.index('.if IS_FRLG\n\n@ FRLG scripts');end=events.index('\n.endif',start)
 includes=[]
 for path in re.findall(r'\.include "([^"]+)"',events[start:end]):
  if path.startswith('data/maps/'):
   name=path.split('/')[2];includes.append('data/kanto/maps/'+name+'/scripts.inc');continue
  dst='data/kanto/'+path.removeprefix('data/');target=ROOT/dst;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(rewrite((ROOT/path).read_text(encoding='utf-8')),encoding='utf-8',newline='\n');includes.append(dst)
 (ROOT/'data/kanto/campaign.inc').write_text('\n'.join('\t.include "'+p+'"' for p in includes)+'\n',encoding='utf-8',newline='\n')
 save('data/kanto/maps_manifest.json',{'maps':names,'map_ids':ids,'layouts':layoutids,'object_count':count,'map_count':len(names),'group_count':len(groups['group_order'])})
 print(f'Imported {len(names)} maps, {count} existing actors, {len(used)} layouts; {len(groups["group_order"])} stable groups')
if __name__=='__main__':main()
