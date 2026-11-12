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
DEFS=[];DECL=[];REPORT=[];EXTRA_ALIASES=[];PAL_OVERRIDES=[]
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
 nativefolder=palpaths[0].parent
 pattern=r'const u16 (?:ALIGNED\(4\) )?(\w+)\[\]\[16\]\s*=\s*\{\s*INCGFX_U16\("'+re.escape(palpaths[0].as_posix())+r'"'
 choices=re.findall(pattern,HEAD)
 basepal=next((n for n in choices if n.startswith('gTilesetPalettes_Kanto_')),choices[0]) if 'Kanto' in label else choices[0]
 for i,p in enumerate(palpaths):
  if p!=nativefolder/f'{i:02}.pal':PAL_OVERRIDES.append(dict(tileset=label,slot=i,path=p.as_posix()))
 DEFS.append(f'const u32 {label}Tiles[] = INCBIN_U32("{path.as_posix()}/tiles.bin.smol");\n'+f'const u16 {label}Metatiles[] = INCBIN_U16("{path.as_posix()}/metatiles.bin");\nconst u16 {label}Attributes[] = INCBIN_U16("{path.as_posix()}/attributes.bin");\nconst struct Tileset {label} = {{.isCompressed=TRUE, .isSecondary=TRUE, .tiles={label}Tiles, .palettes={basepal}, .metatiles={label}Metatiles, .metatileAttributes={label}Attributes, .callback={callback}}};\n')
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
 attrs=words(cityfolder/'metatile_attributes.bin',4 if frlg else 2);original_mt_count=len(mts)
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
 if oldlay['secondary_tileset']=='gTileset_Kanto_CeladonCity':usedtiles.update(range(104,112))
 # Door DMA owns the last sixteen tiles, even when they look unused at rest.
 free=[i for i in range(1008-split) if i not in usedtiles]
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
 limit=max(original_mt_count,max(free_mt[:size*size])+1)
 write_tileset(label,out,ts,mts[:limit],attrs[:limit],palpaths,callback)
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
def saffron_facades():
 city='KantoSaffronCity';m=original(city);l=LAYS[m['layout']];pf=folder(l['primary_tileset']);sf=folder(l['secondary_tileset'])
 pts=tiles(pf);sts=tiles(sf);pm=words(pf/'metatiles.bin');pm=[pm[i:i+8] for i in range(0,len(pm),8)];sm=words(sf/'metatiles.bin');sm=[sm[i:i+8] for i in range(0,len(sm),8)]
 pa=words(pf/'metatile_attributes.bin',4);sa=words(sf/'metatile_attributes.bin',4)
 a=np.array(words(l['blockdata_filepath'])).reshape(l['height'],l['width']);before=a.copy();rects=[(19,25),(43,25)];mask=np.ones(a.shape,dtype=bool)
 for x,y in rects:mask[y:y+6,x:x+5]=False
 usedp=set(range(416,512));useds=set();usedpal=set()
 for name in [city,'KantoRoute5','KantoRoute6','KantoRoute7','KantoRoute8']:
  events=original(name);nl=LAYS[events['layout']];npf=folder(nl['primary_tileset']);nsf=folder(nl['secondary_tileset']);pmt=words(npf/'metatiles.bin');pmt=[pmt[i:i+8] for i in range(0,len(pmt),8)];smt=words(nsf/'metatiles.bin');smt=[smt[i:i+8] for i in range(0,len(smt),8)]
  block=words(nl['blockdata_filepath']) if name!=city else list(a[mask]);block+=words(nl['border_filepath'])
  for mid in {int(v)&1023 for v in block}:
   for v in smt[mid-640] if mid>=640 else pmt[mid]:
    t=v&1023
    if t<640:usedp.add(t)
    if name==city:
     usedpal.add(v>>12)
     if t>=640:useds.add(t-640)
 assert 7 not in usedpal
 free=[640+i for i in range(368) if i not in useds]+[i for i in range(640) if i not in usedp]
 # Reuse identical index patterns; palette numbers belong to references, not tiles.
 patterns={t.tobytes():640+i for i,t in enumerate(sts) if i in useds};patterns.update({t.tobytes():i for i,t in enumerate(pts) if i in usedp and i<len(pts)})
 while len(pts)<640:pts.append(np.zeros((8,8),dtype='uint8'))
 while len(sts)<384:sts.append(np.zeros((8,8),dtype='uint8'))
 usedmid={int(v)&1023 for v in a[mask]};slots=[i for i in range(384) if i+640 not in usedmid]
 while len(sm)<384:sm.append([0]*8);sa.append(0)
 allocations=[];cursor=0;mtcursor=0
 for theme,(x,y) in zip(['glitch','bloom'],rects):
  mod=PACK/f'modules/saffron/{theme}/exterior';meta=json.loads((mod/'module.json').read_text());src=json.loads((mod/'editable_source.json').read_text());raw=(mod/'tiles.4bpp').read_bytes();pix=np.empty(len(raw)*2,dtype='uint8');pix[::2]=np.frombuffer(raw,dtype='uint8')&15;pix[1::2]=np.frombuffer(raw,dtype='uint8')>>4;ids=[]
  for t in pix.reshape(-1,8,8):
   key=t.tobytes()
   if key not in patterns:
    assert cursor<len(free);idx=free[cursor];cursor+=1;patterns[key]=idx
    (sts if idx>=640 else pts)[idx-640 if idx>=640 else idx]=t.copy()
   ids.append(patterns[key])
  rowids=[]
  for i,row in enumerate(src['metatiles']):
   out=[]
   for j,v in enumerate(row):
    if src['custom_reference_masks'][i]&(1<<j):v=(v&~1023)|ids[v&1023]
    if src['custom_palette_masks'][i]&(1<<j):v=(v&4095)|(7<<12)
    out.append(v)
   rowids.append(out)
  for i,v in enumerate(src['map_words']):
   at=y+i//5, x+i%5;oldmid=int(before[at])&1023;idx=slots[mtcursor];mtcursor+=1;sm[idx]=rowids[v&1023];sa[idx]=(words(sf/'metatile_attributes.bin',4)[oldmid-640] if oldmid>=640 else pa[oldmid]);a[at]=(int(before[at])&0xFC00)|(640+idx)
  allocations.append(dict(theme=theme,rect=[x,y,5,6],tile_ids=ids))
 out=Path('data/venues/SaffronFacades');(ROOT/out).mkdir(parents=True,exist_ok=True)
 pp=[pf/'palettes'/f'{i:02}.pal' for i in range(16)];sp=[sf/'palettes'/f'{i:02}.pal' for i in range(16)];sp[7]=Path('graphics/custom_buildings/pastel_pack/modules/saffron/glitch/exterior/palette-00.pal')
 assert (ROOT/sp[7]).read_bytes()==(PACK/'modules/saffron/bloom/exterior/palette-00.pal').read_bytes()
 write_tileset('gTileset_VenueKantoSaffronPrimary',out/'primary',pts,pm,pa,pp,'InitTilesetAnim_General_Frlg')
 base=body(l['primary_tileset']);refs={key:re.search(r'\.'+key+r'\s*=\s*(\w+)',base)[1] for key in ['palettes','metatiles','metatileAttributes']}
 DEFS[-1]='const u32 gTileset_VenueKantoSaffronPrimaryTiles[] = INCBIN_U32(\"data/venues/SaffronFacades/primary/tiles.bin.smol\");\nconst struct Tileset gTileset_VenueKantoSaffronPrimary = {.isCompressed=TRUE, .isSecondary=FALSE, .tiles=gTileset_VenueKantoSaffronPrimaryTiles, .palettes='+refs['palettes']+', .metatiles='+refs['metatiles']+', .metatileAttributes='+refs['metatileAttributes']+', .callback=InitTilesetAnim_General_Frlg};\n'
 limit=max(len(words(sf/'metatiles.bin'))//8,max(slots[:mtcursor])+1)
 write_tileset('gTileset_VenueKantoSaffronSecondary',out/'secondary',sts,sm[:limit],sa[:limit],sp)
 nl=copy.deepcopy(l);nl.update(id='LAYOUT_VENUE_SAFFRON_FACADES',name='VenueSaffronFacades_Layout',primary_tileset='gTileset_VenueKantoSaffronPrimary',secondary_tileset='gTileset_VenueKantoSaffronSecondary',blockdata_filepath=(out/'map.bin').as_posix());binary(out/'map.bin',list(a.reshape(-1)));LAY['layouts'].append(nl);m['layout']=nl['id'];save(f'data/maps/{city}/map.json',m)
 EXTRA_ALIASES.extend([('gTileset_VenueKantoSaffronPrimary',l['primary_tileset']),('gTileset_VenueKantoSaffronSecondary',l['secondary_tileset'])])
 save('data/venues/facades.json',dict(city=city,original_layout=l['id'],layout=nl['id'],placements=allocations,allocated_tiles=free[:cursor],reserved_primary_animation_tiles=list(range(416,512)),door_reserved_start=1008))
def main():
 from venue_generation_contract import check,record
 check(ROOT)
 old_order=[l['id'] for l in LAY['layouts']]
 # Restore only our explicitly recorded parent snapshots before deterministic rebuild.
 for p in (DATA/'originals').glob('*.json'):save('data/maps/'+p.stem+'/map.json',json.loads(p.read_text()))
 # Do not duplicate generated layouts on a repeated authoring run.
 LAY['layouts'][:]=[l for l in LAY['layouts'] if not l['id'].startswith('LAYOUT_VENUE_')]
 for site in SITES:install(*site)
 saffron_facades()
 # Published layout IDs are save data: update descriptors in place, append only.
 rebuilt={l['id']:l for l in LAY['layouts']}
 LAY['layouts']=[rebuilt.pop(k) for k in old_order]+list(rebuilt.values())
 save('data/layouts/layouts.json',LAY);save('data/venues/sites.json',REPORT)
 groups=read('data/maps/map_groups.json')
 for region in ['hoenn','kanto']:
  key='gMapGroup_Venues'+region.title()
  if key not in groups['group_order']:groups['group_order'].append(key)
  groups[key]=[s['house'] for s in REPORT if s['region']==region and s['open_lot']]
 save('data/maps/map_groups.json',groups)
 p=ROOT/'data/event_scripts.s';s=p.read_text();s=s.split('\n@ Generated venue map roots')[0]
 p.write_text(s+'\n@ Generated venue map roots\n'+''.join('\t.include "data/maps/'+r['house']+'/scripts.inc"\n' for r in REPORT if r['open_lot']))
 pals=''
 for i,row in enumerate(PAL_OVERRIDES):pals+=f'const u16 sVenuePalette{i}[] = INCGFX_U16("{row["path"]}", ".gbapal");\n'
 pals+='static const struct { const struct Tileset *tileset; const u16 *palette; u16 slot; } sVenuePalettes[] = {\n'
 for i,row in enumerate(PAL_OVERRIDES):pals+=f' {{&{row["tileset"]}, sVenuePalette{i}, {row["slot"]}}},\n'
 pals+='};\n'
 loader='void Venues_LoadPaletteOverrides(const struct Tileset *tileset, bool32 skipFaded)\n{\n#if !IS_FRLG\n    u32 i;\n    for (i=0; i<ARRAY_COUNT(sVenuePalettes); i++)\n        if (sVenuePalettes[i].tileset == tileset)\n        {\n            if (skipFaded) CpuCopy16(sVenuePalettes[i].palette, &gPlttBufferUnfaded[sVenuePalettes[i].slot * 16], 32);\n            else LoadPalette(sVenuePalettes[i].palette, sVenuePalettes[i].slot * 16, 32);\n        }\n#endif\n}\n'
 (ROOT/'src/data/tilesets/venues.h').write_text('#if !IS_FRLG\n'+''.join(DEFS)+pals+'#endif\n'+loader)
 save('data/venues/palette_overrides.json',PAL_OVERRIDES)
 aliases='#include "global.h"\n#include "fieldmap.h"\n#include "tilesets.h"\n#include "venues.h"\nconst struct Tileset *Venue_BaseTileset(const struct Tileset *tileset)\n{\n#if !IS_FRLG\n'
 for site in REPORT:
  tag=site['region'].title()+site['theme'].title();aliases+=f'    if (tileset == &gTileset_Venue{tag}) return &{site["base_tileset"]};\n'
 for target,base in EXTRA_ALIASES:aliases+=f'    if (tileset == &{target}) return &{base};\n'
 aliases+='#endif\n    return tileset;\n}\n'
 aliases+='\n#if !IS_FRLG\nstatic void ReloadSavedVenue(void)\n{\n    CpuFill16(0, gSaveBlock1Ptr->mapView, sizeof(gSaveBlock1Ptr->mapView));\n    if (!UseContinueGameWarp())\n    {\n        gSaveBlock1Ptr->continueGameWarp = gSaveBlock1Ptr->location;\n        gSaveBlock1Ptr->continueGameWarp.warpId = WARP_ID_NONE;\n        gSaveBlock1Ptr->continueGameWarp.x = gSaveBlock1Ptr->pos.x;\n        gSaveBlock1Ptr->continueGameWarp.y = gSaveBlock1Ptr->pos.y;\n        SetContinueGameWarpStatus();\n    }\n}\n'
 aliases+='#endif\n'
 aliases+='\nvoid Venues_MigrateSavedLayout(void)\n{\n#if !IS_FRLG\n'
 for site in REPORT:
  aliases+=f'    if (gMapHeader.mapLayoutId == {site["layout"]} && gSaveBlock1Ptr->mapLayoutId == {site["original_layout"]})\n    {{\n        gSaveBlock1Ptr->mapLayoutId = {site["layout"]};\n'
  if site['open_lot']:
   x,y,w,h=site['rect'];dx,dy=site['entrance'];aliases+=f'        if (gSaveBlock1Ptr->pos.x >= {x} && gSaveBlock1Ptr->pos.x < {x+w} && gSaveBlock1Ptr->pos.y >= {y} && gSaveBlock1Ptr->pos.y < {y+h})\n        {{ gSaveBlock1Ptr->pos.x = {dx}; gSaveBlock1Ptr->pos.y = {dy+1}; }}\n'
  aliases+='        ReloadSavedVenue();\n        return;\n    }\n'
  if not site['open_lot']:
   room=read(f'data/maps/{site["house"]}/map.json');warp=room['warp_events'][0]
   aliases+=f'    if (gMapHeader.mapLayoutId == {site["room_layout"]} && gSaveBlock1Ptr->mapLayoutId == {site["original_room_layout"]})\n    {{\n        gSaveBlock1Ptr->mapLayoutId = {site["room_layout"]};\n        gSaveBlock1Ptr->pos.x = {warp["x"]}; gSaveBlock1Ptr->pos.y = {warp["y"]-1};\n        ReloadSavedVenue();\n        return;\n    }}\n'
 facade=read('data/venues/facades.json')
 aliases+=f'    if (gMapHeader.mapLayoutId == {facade["layout"]} && gSaveBlock1Ptr->mapLayoutId == {facade["original_layout"]})\n    {{ gSaveBlock1Ptr->mapLayoutId = {facade["layout"]}; ReloadSavedVenue(); return; }}\n'
 for stop in read('data/venues/tutor_stops.json'):
  mid=read(f'data/maps/{stop["map"]}/map.json')['id'];local=stop['actor']['local_id']
  aliases+=f'    if (gSaveBlock1Ptr->location.mapGroup == MAP_GROUP({mid}) && gSaveBlock1Ptr->location.mapNum == MAP_NUM({mid}))\n    {{\n        u32 at = gMapHeader.events->objectEventCount - 1;\n        if (gMapHeader.events->objectEvents[at].localId == {local} && gSaveBlock1Ptr->objectEventTemplates[at].localId != {local}) ReloadSavedVenue();\n    }}\n'
 aliases+='#endif\n}\n'
 aliases=aliases.replace('#include "venues.h"','#include "venues.h"\n#include "overworld.h"\n#include "load_save.h"\n#include "constants/layouts.h"\n#include "constants/maps.h"\n#include "constants/map_event_ids.h"')
 (ROOT/'src/venues.c').write_text(aliases)
 p=ROOT/'src/tilesets.c';s=p.read_text();inc='#include "data/tilesets/venues.h"';p.write_text(s if inc in s else s+'\n'+inc+'\n')
 p=ROOT/'include/tilesets.h';s=p.read_text();s=re.sub(r'#endif\s*//\s*GUARD_tilesets_H','',s.split('// Private venue tilesets')[0]).rstrip();p.write_text(s+'\n// Private venue tilesets\n'+'\n'.join(DECL)+'\n#endif // GUARD_tilesets_H\n')
 record(ROOT)
 print('Installed',len(REPORT),'venues')
if __name__=='__main__':main()
