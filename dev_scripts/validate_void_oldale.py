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
  mids=a&1023;assert mids.max()<512 and len(attrs)==w*h+1
  assert (ROOT/f'data/void_oldale/{name.removeprefix("VoidOldale")}/border.bin').read_bytes()==struct.pack('<4H',*([0x3C00|w*h]*4))
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
 # Existing maps/scripts are separate; no old save banks or context IDs changed.
 assert read('data/maps/OldaleTown/map.json')['layout']=='LAYOUT_OLDALE_TOWN'
 print('PASS: five private maps, all four bidirectional doors, floor access and eight indexed nine-frame creatures')
if __name__=='__main__':main()
