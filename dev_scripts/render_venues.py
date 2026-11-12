"""Render installed map resources and prove unchanged pixels outside each building.
These previews are source renders, never labelled as emulator captures.
"""
from pathlib import Path
import json,re,struct,sys
import numpy as np
from PIL import Image,ImageDraw
from variety_map_tools import ROOT,LAYOUTS
HEAD='\n'.join(p.read_text(encoding='utf-8') for p in (ROOT/'src/data/tilesets').glob('*.h'))
HEAD+='\n'+(ROOT/'src/graphics.c').read_text(encoding='utf-8')
def array(symbol,macro):
 return re.search(r'\b'+symbol+r'\[\](?:\[16\])?\s*=\s*'+macro+r'\("([^"]+)"',HEAD)[1]
def bank(symbol):
 b=re.search(r'const struct Tileset '+symbol+r'\s*=\s*\{(.*?)\};',HEAD,re.S)[1]
 fields={n:re.search(r'\.'+n+r'\s*=\s*(\w+)',b)[1] for n in ['tiles','palettes','metatiles']}
 m=np.frombuffer((ROOT/array(fields['metatiles'],'INCBIN_U16')).read_bytes(),dtype='<u2').reshape(-1,8)
 raw=re.search(r'\b'+fields['tiles']+r'\[\]\s*=\s*INCBIN_U32\("([^"]+)"',HEAD)
 if raw:
  packed=np.frombuffer((ROOT/raw[1].removesuffix('.smol')).read_bytes(),dtype='uint8');a=np.empty(len(packed)*2,dtype='uint8');a[::2]=packed&15;a[1::2]=packed>>4;ts=a.reshape(-1,8,8)
 else:
  p=array(fields['tiles'],'INCGFX_U32');im=Image.open(ROOT/p);a=np.array(im)&15;ts=np.array([a[y:y+8,x:x+8] for y in range(0,im.height,8) for x in range(0,im.width,8)])
 pbody=re.search(r'\b'+fields['palettes']+r'\[\]\[16\]\s*=\s*\{(.*?)\};',HEAD,re.S)[1]
 paths=re.findall(r'INCGFX_U16\("([^"]+)"',pbody)
 pals=np.array([[list(map(int,line.split())) for line in (ROOT/p).read_text().splitlines()[3:19]] for p in paths],dtype='uint8')
 return ts,m,pals
def render(l):
 banks=[bank(l[k]) for k in ['primary_tileset','secondary_tileset']];split=640 if l.get('layout_version')=='frlg' else 512;palfirst=7 if split==640 else 6
 raw=np.frombuffer((ROOT/l['blockdata_filepath']).read_bytes(),dtype='<u2').reshape(l['height'],l['width']);rgb=np.zeros((l['height']*16,l['width']*16,3),dtype='uint8');cache={}
 for y in range(l['height']):
  for x in range(l['width']):
   mid=int(raw[y,x])&1023
   if mid not in cache:
    row=banks[mid>=split][1][mid-split if mid>=split else mid];out=np.zeros((16,16,3),dtype='uint8')
    for i,v in enumerate(row):
     v=int(v);t=v&1023;a=banks[t>=split][0][t-split if t>=split else t]
     if v&1024:a=a[:,::-1]
     if v&2048:a=a[::-1]
     px=(i%2)*8;py=((i%4)//2)*8;pal=banks[(v>>12)>=palfirst][2][v>>12];mask=(a!=0) if i>=4 else np.ones((8,8),dtype=bool)
     out[py:py+8,px:px+8][mask]=pal[a][mask]
    cache[mid]=out
   rgb[y*16:y*16+16,x*16:x*16+16]=cache[mid]
 return Image.fromarray(rgb)
def main(out):
 out=Path(out);out.mkdir(parents=True,exist_ok=True)
 sites=json.loads((ROOT/'data/venues/sites.json').read_text());contact=Image.new('RGB',(960,12*190),'#f2f0e8');d=ImageDraw.Draw(contact)
 for i,s in enumerate(sites):
  old=render(LAYOUTS[s['original_layout']]);new=render(LAYOUTS[s['layout']]);a=np.array(old);b=np.array(new);x,y,w,h=s['rect'];mask=np.ones(a.shape[:2],dtype=bool);mask[y*16:(y+h)*16,x*16:(x+w)*16]=False
  assert np.array_equal(a[mask],b[mask]),('Pixels outside building changed',s['city'])
  new.save(out/(s['city']+'.png'));room=render(LAYOUTS[s['room_layout']]);room.save(out/(s['house']+'.png'))
  crop=new.crop((max(0,x-2)*16,max(0,y-1)*16,min(new.width,(x+w+2)*16),min(new.height,(y+h+2)*16)))
  crop=crop.resize((crop.width*2,crop.height*2),Image.Resampling.NEAREST);room=room.resize((room.width*2,room.height*2),Image.Resampling.NEAREST)
  d.text((8,i*190+5),f'{s["city"]}: {s["theme"]} | source render',fill='#223333');contact.paste(crop,(8,i*190+24));contact.paste(room,(390,i*190+24))
 contact.save(out/'venue-lineup.png')
 f=json.loads((ROOT/'data/venues/facades.json').read_text());old=np.array(render(LAYOUTS[f['original_layout']]));new=render(LAYOUTS[f['layout']]);mask=np.ones(old.shape[:2],dtype=bool)
 for p in f['placements']:
  x,y,w,h=p['rect'];mask[y*16:(y+h)*16,x*16:(x+w)*16]=False
 assert np.array_equal(old[mask],np.array(new)[mask])
 new.save(out/'Saffron-facades.png')
 print('PASS: all 14 installed exterior source renders preserve every pixel outside their building rectangles')
if __name__=='__main__':main(sys.argv[1])
