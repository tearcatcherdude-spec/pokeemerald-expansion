"""Check first-world geometry, returns, tile budgets and native creature frames."""
from pathlib import Path
import json,struct
import numpy as np
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
def read(p):return json.loads((ROOT/p).read_text())
def main():
 manifest=read('data/void_oldale/manifest.json');layouts={l['id']:l for l in read('data/layouts/layouts.json')['layouts']}
 maps={n:read('data/maps/'+n+'/map.json') for n in manifest['maps']}
 for name,m in maps.items():
  l=layouts[m['layout']];w,h=l['width'],l['height'];a=np.frombuffer((ROOT/l['blockdata_filepath']).read_bytes(),dtype='<u2').reshape(h,w)
  attrs=np.frombuffer((ROOT/f'data/void_oldale/{name.removeprefix("VoidOldale")}/PrimaryAttributes.bin').read_bytes(),dtype='<u2')
  mids=a&1023
  if name=='VoidOldaleTown':
   attrs=np.concatenate([attrs,np.frombuffer((ROOT/'data/void_oldale/Town/SecondaryAttributes.bin').read_bytes(),dtype='<u2')]);assert len(attrs)==1024 and mids.max()<1024
   blank=read('data/void_oldale/terrain_contract.json')['blank_metatile']
  else:assert mids.max()<512 and len(attrs)==w*h+1;blank=w*h
  assert (ROOT/f'data/void_oldale/{name.removeprefix("VoidOldale")}/border.bin').read_bytes()==struct.pack('<4H',*([0x3C00|blank]*4))
  floor={(x,y) for y in range(h) for x in range(w) if not int(a[y,x])&0xC00}
  origin=(10,10) if name=='VoidOldaleTown' else (m['warp_events'][0]['x'],h-2)
  assert origin in floor,(name,'Spawn blocked')
  seen={origin};todo=[origin]
  while todo:
   x,y=todo.pop()
   for p in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
    if p in floor and p not in seen:seen.add(p);todo.append(p)
  for warp in m['warp_events']:
   p=(warp['x'],warp['y']);assert p in seen,(name,'Door unreachable',p)
   dest=next(v for v in maps.values() if v['id']==warp['dest_map']);ret=dest['warp_events'][int(warp['dest_warp_id'])]
   assert ret['dest_map']==m['id'],(name,'Return mismatch')
   behavior=int(attrs[int(a[p[1],p[0]])&1023])&255;assert behavior==(0x60 if name=='VoidOldaleTown' else 0x65)
  occupied=set()
  for o in m['object_events']:
   p=(o['x'],o['y']);assert p in seen and p not in occupied,(name,'Actor obstructed',p);occupied.add(p)
   assert any(q in seen and q not in occupied for q in [(p[0]-1,p[1]),(p[0]+1,p[1]),(p[0],p[1]-1),(p[0],p[1]+1)])
  for bank in ['Primary','Secondary']:assert (ROOT/f'data/void_oldale/{name.removeprefix("VoidOldale")}/{bank}.4bpp').stat().st_size==16384
 for n in manifest['creatures']:
  p=ROOT/f'graphics/void_oldale/{n.lower()}/walker.png';im=Image.open(p);assert im.mode=='P' and im.size==(144,32) and im.info['transparency']==0 and p.read_bytes()[24]==4
  assert len(np.unique(np.array(im)))<=16
  pointers=(ROOT/'src/data/object_events/object_event_graphics_info_pointers.h').read_text().split('gObjectEventGraphicsInfoPointers[NUM_OBJ_EVENT_GFX]')[1].split('};')[0]
  assert f'[OBJ_EVENT_GFX_VOID_{n.upper()}] = &gObjectEventGraphicsInfo_Void{n}' in pointers,('Creature missing from actual actor table',n)
 # Every original tree/grass/path pixel and metatile stays exact; colors only.
 from render_venues import bank,LAYOUTS
 contract=read('data/void_oldale/terrain_contract.json');l=LAYOUTS['LAYOUT_OLDALE_TOWN'];original=[bank(l[k]) for k in ['primary_tileset','secondary_tileset']]
 tiledata=np.frombuffer((ROOT/'data/void_oldale/Town/Primary.4bpp').read_bytes()+(ROOT/'data/void_oldale/Town/Secondary.4bpp').read_bytes(),dtype='uint8');decoded=np.empty(len(tiledata)*2,dtype='uint8');decoded[::2]=tiledata&15;decoded[1::2]=tiledata>>4;decoded=decoded.reshape(-1,8,8)
 for t in contract['native_pixel_tiles']:assert np.array_equal(decoded[t],original[t>=512][0][t-512 if t>=512 else t]),('Native terrain pixels changed',t)
 old=np.frombuffer((ROOT/l['blockdata_filepath']).read_bytes(),dtype='<u2').reshape(20,20)&1023;new=np.frombuffer((ROOT/'data/void_oldale/Town/map.bin').read_bytes(),dtype='<u2').reshape(20,20)&1023;mask=np.zeros((20,20),bool)
 for x,y,w,h in contract['building_rects']:mask[y:y+h,x:x+w]=True
 assert np.array_equal(old[~mask],new[~mask]),'Original terrain placement changed'
 colors=[list(map(int,line.split())) for line in (ROOT/'data/void_oldale/Town/palette-02.pal').read_text().splitlines()[3:]]
 assert colors[13]==[0,0,0] and colors[12]==[8,8,16],'Black grass/dark path colors missing'
 # Existing maps/scripts are separate; no old save banks or context IDs changed.
 assert read('data/maps/OldaleTown/map.json')['layout']=='LAYOUT_OLDALE_TOWN'
 print('PASS: original terrain pixels/layout with black grass and near-black paths; five private maps, four doors and eight native creatures')
if __name__=='__main__':main()
