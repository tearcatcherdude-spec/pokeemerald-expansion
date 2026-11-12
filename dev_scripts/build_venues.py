"""Install private tilesets/layouts; keep original resources and native events.
Run once against the pinned parent. Rebuilding requires the saved original map
snapshots in data/venues/originals, never a reset of a user's checkout.
"""
from pathlib import Path
import json,re,struct,hashlib,sys,copy
import numpy as np
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
PACK=ROOT/'graphics/custom_buildings/pastel_pack'
DATA=ROOT/'data/venues';DATA.mkdir(exist_ok=True)
HEAD='\n'.join(p.read_text(encoding='utf-8') for p in (ROOT/'src/data/tilesets').glob('*.h') if p.name!='venues.h')
LAY=json.loads((ROOT/'data/layouts/layouts.json').read_text())
LAYS={l['id']:l for l in LAY['layouts']}
DEFS=[];DECL=[];REPORT=[]
SITES=[
 ('hoenn','tutor','PetalburgCity','PetalburgCity_House1',10,19),
 ('hoenn','bakery','RustboroCity','RustboroCity_House3',26,46),
 ('hoenn','tea','SlateportCity','SlateportCity_House',21,44),
 ('hoenn','glitch','MauvilleCity','MauvilleCity_House2',19,14),
 ('hoenn','bloom','VerdanturfTown','VerdanturfTown_House',17,15),
 ('hoenn','rave','LilycoveCity','LilycoveCity_House1',42,6),
 ('kanto','bakery','KantoPewterCity','KantoPewterCity_House2',9,30),
 ('kanto','glitch','KantoCeruleanCity','KantoCeruleanCity_House4',23,28),
 ('kanto','tea','KantoVermilionCity','KantoVermilionCity_House1',9,6),
 ('kanto','tutor','KantoLavenderTown','KantoLavenderTown_House2',10,16),
 ('kanto','rave','KantoFuchsiaCity','KantoFuchsiaCity_House1',14,31),
 ('kanto','bloom','KantoSaffronCity','KantoSaffronCity_House',27,21),
]
OPEN_LOTS={('hoenn','bakery'):('Route104',7,22),('kanto','bakery'):('WatchViridian',35,21),('kanto','glitch'):('KantoPewterCity',7,22),('kanto','tea'):('KantoVermilionCity',24,9),('kanto','tutor'):('KantoRoute4',78,12),('kanto','rave'):('KantoRoute11',48,6),('kanto','bloom'):('KantoRoute18',10,2)}
def read(path):return json.loads((ROOT/path).read_text(encoding='utf-8'))
def save(path,obj):
 p=ROOT/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
def original(name):
 rel=f'data/venues/originals/{name}.json';p=ROOT/rel
 if not p.exists():
  m=read(f'data/maps/{name}/map.json');m['object_events']=[o for o in m['object_events'] if not o.get('local_id','').startswith('LOCALID_ROAMING_TUTOR')];save(rel,m)
 return read(rel)
def words(path,width=2):
 raw=(ROOT/path).read_bytes();return list(struct.unpack('<'+('H' if width==2 else 'I')*(len(raw)//width),raw))
def binary(path,values,width=2):
 (ROOT/path).write_bytes(struct.pack('<'+('H' if width==2 else 'I')*len(values),*values))
def body(symbol):return re.search(r'const struct Tileset '+symbol+r'\s*=\s*\{(.*?)\};',HEAD,re.S)[1]
def folder(symbol):
 b=body(symbol);sym=re.search(r'\.metatiles\s*=\s*(\w+)',b)[1]
 return Path(re.search(r'const u16 '+sym+r'\[\]\s*=\s*INCBIN_U16\("([^"]+)"',HEAD)[1]).parent
def tiles(p):
 im=Image.open(ROOT/p/'tiles.png');a=np.array(im)&15
 return [a[y:y+8,x:x+8].copy() for y in range(0,im.height,8) for x in range(0,im.width,8)]
def packed(ts):
 a=np.array(ts,dtype='uint8').reshape(-1);return bytes(a[::2]|(a[1::2]<<4))
def write_tileset(label,path,ts,mts,attrs,palpaths,callback='NULL'):
 path=Path(path);(ROOT/path).mkdir(parents=True,exist_ok=True)
 ts=list(ts)
 while len(ts)<(384 if 'Kanto' in label else 512):ts.append(np.zeros((8,8),dtype='uint8'))
 (ROOT/path/'tiles.bin').write_bytes(packed(ts));binary(path/'metatiles.bin',sum(mts,[]));binary(path/'attributes.bin',attrs,4 if 'Kanto' in label else 2)
 DEFS.append(f'const u32 {label}Tiles[] = INCBIN_U32("{path.as_posix()}/tiles.bin");\nconst u16 {label}Palettes[][16] = {{\n'+''.join(f' INCGFX_U16("{p.as_posix()}", ".gbapal"),\n' for p in palpaths)+'};\n'+f'const u16 {label}Metatiles[] = INCBIN_U16("{path.as_posix()}/metatiles.bin");\nconst u16 {label}Attributes[] = INCBIN_U16("{path.as_posix()}/attributes.bin");\nconst struct Tileset {label} = {{.isCompressed=FALSE, .isSecondary=TRUE, .tiles={label}Tiles, .palettes={label}Palettes, .metatiles={label}Metatiles, .metatileAttributes={label}Attributes, .callback={callback}}};\n')
 DECL.append(f'extern const struct Tileset {label};')
def install(region,theme,city,house,dx,dy):
 openlot=OPEN_LOTS.get((region,theme));oldhouse=house
 room=original(house)
 if openlot:
  city,x,y=openlot;size=5 if region=='kanto' else 4;dx=x+(2 if region=='kanto' else 1);dy=y+size-1
 citymap=original(city);oldlay=LAYS[citymap['layout']];oldroomlay=LAYS[room['layout']]
 frlg=region=='kanto';split=640 if frlg else 512;firstpal=7 if frlg else 6
 tag=('Kanto' if frlg else 'Hoenn')+theme.title();size=5 if frlg else 4;x=dx-(2 if frlg else 1);y=dy-size+1
 cityfolder=folder(oldlay['secondary_tileset']);primaryfolder=folder(oldlay['primary_tileset']);ts=tiles(cityfolder)
 mts0=words(cityfolder/'metatiles.bin');mts=[mts0[i:i+8] for i in range(0,len(mts0),8)]
 attrs=words(cityfolder/'metatile_attributes.bin',4 if frlg else 2)
 blocks=words(oldlay['blockdata_filepath']);oldblocks=blocks.copy();border=words(oldlay['border_filepath']);w=oldlay['width']
 used={v&1023 for v in blocks+border};usedtiles=set();usedpals=set()
 primarymts=words(primaryfolder/'metatiles.bin');primarymts=[primarymts[i:i+8] for i in range(0,len(primarymts),8)]
 for mid in used:
  for v in (mts[mid-split] if mid>=split else primarymts[mid]):
   usedpals.add(v>>12)
   if v&1023>=split:usedtiles.add((v&1023)-split)
 # Callback DMA destinations remain at native addresses, including off-map frames.
 if city=='RustboroCity':usedtiles.update(range(128,164));usedtiles.update(range(448,452))
 if city=='SlateportCity':usedtiles.update(range(224,228))
 if city in ['MauvilleCity','VerdanturfTown']:usedtiles.update(range(96,160))
 free=[i for i in range(1024-split) if i not in usedtiles]
 freepal=[i for i in range(firstpal,13) if i not in usedpals]
 module=PACK/f'modules/{region}/{theme}/exterior';m=json.loads((module/'module.json').read_text());s=json.loads((module/'editable_source.json').read_text())
 assert freepal,(city,'no unused palette');assert len(free)>=m['tile_count'],(city,'tile capacity',len(free),m['tile_count'])
 while len(ts)<1024-split:ts.append(np.zeros((8,8),dtype='uint8'))
 raw=(module/'tiles.4bpp').read_bytes();pix=np.empty(len(raw)*2,dtype='uint8');pix[::2]=np.frombuffer(raw,dtype='uint8')&15;pix[1::2]=np.frombuffer(raw,dtype='uint8')>>4
 tileids=free[:m['tile_count']]
 for i,idx in enumerate(tileids):ts[idx]=pix[i*64:i*64+64].reshape(8,8)
 free_mt=[i for i in range(1024-split) if i+split not in used];assert len(free_mt)>=len(s['metatiles'])
 while len(mts)<1024-split:mts.append([0]*8);attrs.append(0)
 customattrs=words(module.relative_to(ROOT)/'metatile_attributes.bin',4 if frlg else 2)
 for i,row in enumerate(s['metatiles']):
  row=row.copy()
  for j,v in enumerate(row):
   if s['custom_reference_masks'][i]&(1<<j):v=(v&~1023)|(split+tileids[v&1023])
   if s['custom_palette_masks'][i]&(1<<j):v=(v&4095)|(freepal[v>>12]<<12)
   row[j]=v
  mts[free_mt[i]]=row;attrs[free_mt[i]]=customattrs[i]
 customrows=[mts[free_mt[i]].copy() for i in range(len(s['metatiles']))]
 # On new lots, transparent roof corners show THIS map's ground. The source
 # fragments retained Saffron pavement, which must never be pasted onto grass.
 art=np.array(Image.open(module/'art.png').convert('RGBA'))
 custompal=[tuple(map(int,v.split())) for v in (module/'palette-00.pal').read_text().splitlines()[3:19]]
 artindices=np.zeros(art.shape[:2],dtype='uint8')
 for yy in range(art.shape[0]):
  for xx in range(art.shape[1]):
   if openlot and (yy//16)*size+xx//16 not in m['native_cells'] and art[yy,xx,3]:artindices[yy,xx]=custompal.index(tuple(art[yy,xx,:3]))
 patterns={};nexttile=0
 for i,v in enumerate(s['map_words']):
  at=(y+i//size)*w+x+i%size
  if i not in m['native_cells']:
   # Preserve every target collision/elevation bit, not just the template's.
   # A per-cell metatile also preserves the target's native behavior/layer type.
   oldmid=oldblocks[at]&1023
   targetattr=(words(cityfolder/'metatile_attributes.bin',4 if frlg else 2)[oldmid-split]
               if oldmid>=split else words(primaryfolder/'metatile_attributes.bin',4 if frlg else 2)[oldmid])
   row=customrows[v&1023].copy()
   if openlot:
    oldrow=(mts0[8*(oldmid-split):8*(oldmid-split)+8] if oldmid>=split else primarymts[oldmid])
    row=oldrow[:4]
    for q in range(4):
     ax=(i%size)*16+(q%2)*8;ay=(i//size)*16+(q//2)*8;tile=artindices[ay:ay+8,ax:ax+8];key=tile.tobytes()
     if key not in patterns:
      assert nexttile<len(free);idx=free[nexttile];nexttile+=1;ts[idx]=tile.copy();patterns[key]=idx
     row.append((freepal[0]<<12)|(split+patterns[key]))
   mts[free_mt[i]]=row;attrs[free_mt[i]]=customattrs[v&1023] if openlot else targetattr
   blocks[at]=((v if openlot else oldblocks[at])&0xFC00)|(split+free_mt[i])
  elif openlot:
   blocks[at]=0x43D if frlg else 0x421 # Existing primary generic door and animation.
 palpaths=[cityfolder/'palettes'/f'{i:02}.pal' for i in range(16)]
 palpaths[freepal[0]]=module.relative_to(ROOT)/'palette-00.pal'
 out=Path('data/venues')/tag/'exterior';label='gTileset_Venue'+tag
 callback=re.search(r'\.callback\s*=\s*(\w+)',body(oldlay['secondary_tileset']))[1]
 write_tileset(label,out,ts,mts,attrs,palpaths,callback)
 newlay=copy.deepcopy(oldlay);newlay.update(id='LAYOUT_VENUE_'+tag.upper(),name='Venue'+tag+'_Layout',secondary_tileset=label,blockdata_filepath=(out/'map.bin').as_posix())
 binary(out/'map.bin',blocks);LAY['layouts'].append(newlay);citynew=copy.deepcopy(citymap);citynew['layout']=newlay['id'];save(f'data/maps/{city}/map.json',citynew)
 # Each room gets its own secondary bank: no global shared-house recolouring.
 module=PACK/f'modules/{region}/{theme}/interior';m=json.loads((module/'module.json').read_text());s=json.loads((module/'editable_source.json').read_text());pal=[7,8] if frlg else [7,11]
 out=Path('data/venues')/tag/'interior';(ROOT/out).mkdir(parents=True,exist_ok=True)
 import subprocess
 subprocess.run([sys.executable,str(PACK/'tools/relocate.py'),str(module),str(ROOT/out),'--tile-base',str(split),'--metatile-base',str(split),'--palette-slots',*map(str,pal)],check=True,stdout=subprocess.DEVNULL)
 raw=(out and ROOT/out/'tiles.4bpp').read_bytes();pix=np.empty(len(raw)*2,dtype='uint8');pix[::2]=np.frombuffer(raw,dtype='uint8')&15;pix[1::2]=np.frombuffer(raw,dtype='uint8')>>4
 its=list(pix.reshape(-1,8,8));imts=words(out/'metatiles.bin');imts=[imts[i:i+8] for i in range(0,len(imts),8)];ia=words(out/'metatile_attributes.bin',4 if frlg else 2)
 native=Path(m['native_secondary_tileset'].replace('\\','/'));pals=[native/'palettes'/f'{i:02}.pal' for i in range(16)]
 for i,slot in enumerate(pal):pals[slot]=out/f'{slot:02}.pal'
 label='gTileset_Venue'+tag+'Room';write_tileset(label,out,its,imts,ia,pals)
 il=copy.deepcopy(m['native_layout']);il.update(id='LAYOUT_VENUE_'+tag.upper()+'_ROOM',name='Venue'+tag+'Room_Layout',secondary_tileset=label,primary_tileset=oldroomlay['primary_tileset'],blockdata_filepath=(out/'map-fragment.bin').as_posix())
 if frlg:il['parallel_watch']=True
 LAY['layouts'].append(il);newroom=copy.deepcopy(room);newroom['layout']=il['id']
 # Keep original scripts, flags, warp IDs and destinations; only room coordinates change.
 exits=m['native_events']['warp_events']
 for i,warp in enumerate(newroom['warp_events']):
  e=exits[min(i,len(exits)-1)];warp.update(x=e['x'],y=e['y'],elevation=e['elevation'])
 roomwords=words(out/'map-fragment.bin');rw=il['width'];rh=il['height']
 floor={(x,y) for y in range(1,rh-1) for x in range(1,rw-1) if not roomwords[y*rw+x]&0xC00}
 preferred=[(7,4),(4,4),(6,2),(2,2),(8,5),(2,6),(8,3),(5,2),(1,5)]
 positions=[p for p in preferred if p in floor]
 assert len(positions)>=len(newroom['object_events'])+2
 for i,o in enumerate(newroom['object_events']):
  o.update(x=positions[i][0],y=positions[i][1],movement_type='MOVEMENT_TYPE_FACE_DOWN',movement_range_x=0,movement_range_y=0,elevation=3)
 added=guests(tag,theme)
 for i,o in enumerate(added):o.update(x=positions[len(room['object_events'])+i][0],y=positions[len(room['object_events'])+i][1])
 newroom['object_events']+=added
 if openlot:
  house='Venue'+tag
  newroom.update(id='MAP_VENUE_'+re.sub(r'([a-z])([A-Z])',r'\1_\2',tag).upper(),name=house,object_events=added,coord_events=[],bg_events=[],connections=None,music=citymap['music'],region_map_section=citymap['region_map_section'])
  cityid=citymap['id'];warpid=len(citymap['warp_events'])
  citynew['warp_events'].append(dict(x=dx,y=dy,elevation=0,dest_map=newroom['id'],dest_warp_id='0'))
  for warp in newroom['warp_events']:warp.update(dest_map=cityid,dest_warp_id=str(warpid))
  save(f'data/maps/{city}/map.json',citynew)
  save(f'data/maps/{oldhouse}/map.json',original(oldhouse))
  d=ROOT/f'data/maps/{house}';d.mkdir(exist_ok=True)
  (d/'scripts.inc').write_text(house+'_MapScripts::\n\t.byte 0\n')
 save(f'data/maps/{house}/map.json',newroom)
 REPORT.append(dict(region=region,theme=theme,city=city,house=house,open_lot=bool(openlot),original_house=oldhouse,entrance=[dx,dy],rect=[x,y,size,size],original_layout=oldlay['id'],layout=newlay['id'],original_room_layout=oldroomlay['id'],room_layout=il['id'],base_tileset=oldlay['secondary_tileset'],palette=freepal[0],tile_slots=tileids,metatile_slots=free_mt[:size*size],native_map_sha256=hashlib.sha256(struct.pack('<'+'H'*len(oldblocks),*oldblocks)).hexdigest()))

GUESTS={'bakery':['otis','taffy'],'bloom':['florian','dahlia'],'glitch':['echo','fen'],'rave':['roux','zephyr'],'tea':['nettle','orson'],'tutor':['cosmo','mosswick']}
def guests(tag,theme):
 result=[]
 for i,n in enumerate(GUESTS[theme]):
  result.append(dict(local_id='LOCALID_VENUE_'+tag.upper()+'_'+n.upper(),type='object',graphics_id='OBJ_EVENT_GFX_VARIETY_'+n.upper(),x=6+i*2,y=6,elevation=3,movement_type='MOVEMENT_TYPE_FACE_DOWN',movement_range_x=0,movement_range_y=0,trainer_type='TRAINER_TYPE_NONE',trainer_sight_or_berry_tree_id='0',script='RoamingTutor_EventScript_Meet' if theme=='tutor' and i==0 else 'Venue_EventScript_'+n.title(),flag='0'))
 return result
def main():
 # Restore only our explicitly recorded parent snapshots before deterministic rebuild.
 for p in (DATA/'originals').glob('*.json'):save('data/maps/'+p.stem+'/map.json',json.loads(p.read_text()))
 # Do not duplicate generated layouts on a repeated authoring run.
 LAY['layouts'][:]=[l for l in LAY['layouts'] if not l['id'].startswith('LAYOUT_VENUE_')]
 for site in SITES:install(*site)
 save('data/layouts/layouts.json',LAY);save('data/venues/sites.json',REPORT)
 groups=read('data/maps/map_groups.json')
 for region in ['hoenn','kanto']:
  key='gMapGroup_Venues'+region.title()
  if key not in groups['group_order']:groups['group_order'].append(key)
  groups[key]=[s['house'] for s in REPORT if s['region']==region and s['open_lot']]
 save('data/maps/map_groups.json',groups)
 p=ROOT/'data/event_scripts.s';s=p.read_text();s=s.split('\n@ Generated venue map roots')[0]
 p.write_text(s+'\n@ Generated venue map roots\n'+''.join('\t.include "data/maps/'+r['house']+'/scripts.inc"\n' for r in REPORT if r['open_lot']))
 (ROOT/'src/data/tilesets/venues.h').write_text('#if !IS_FRLG\n'+''.join(DEFS)+'#endif\n')
 aliases='#include "global.h"\n#include "fieldmap.h"\n#include "tilesets.h"\n#include "venues.h"\nconst struct Tileset *Venue_BaseTileset(const struct Tileset *tileset)\n{\n#if !IS_FRLG\n'
 for site in REPORT:
  tag=site['region'].title()+site['theme'].title();aliases+=f'    if (tileset == &gTileset_Venue{tag}) return &{site["base_tileset"]};\n'
 (ROOT/'src/venues.c').write_text(aliases+'#endif\n    return tileset;\n}\n')
 p=ROOT/'src/tilesets.c';s=p.read_text();inc='#include "data/tilesets/venues.h"';p.write_text(s if inc in s else s+'\n'+inc+'\n')
 p=ROOT/'include/tilesets.h';s=p.read_text();s=re.sub(r'#endif\s*//\s*GUARD_tilesets_H','',s.split('// Private venue tilesets')[0]).rstrip();p.write_text(s+'\n// Private venue tilesets\n'+'\n'.join(DECL)+'\n#endif // GUARD_tilesets_H\n')
 print('Installed',len(REPORT),'venues')
if __name__=='__main__':main()
