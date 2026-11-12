from pathlib import Path
import sys,subprocess,json,numpy as np
from PIL import Image
sys.path.insert(0,str(Path(__file__).parent))
from native_map import NativeMap,ROOT

def tile_array(m,raw):
    tid=raw&1023;si=int(tid>=m.primary);tid-=si*m.primary;im=m.images[si]
    ar=np.array(im.crop((tid%(im.width//8)*8,tid//(im.width//8)*8,tid%(im.width//8)*8+8,tid//(im.width//8)*8+8)))&15
    if raw&1024:ar=ar[:,::-1]
    if raw&2048:ar=ar[::-1]
    return ar

P=ROOT
results=[]
for d in sorted((P/'modules').glob('*/*/*')):
 m=json.loads((d/'module.json').read_text());s=json.loads((d/'editable_source.json').read_text());native=NativeMap(m['native_map']);boundary=m['primary_tile_boundary']
 if m['kind']=='exterior' and m['family']!='saffron':
  tilebase=boundary+(native.images[1].width*native.images[1].height//64);metabase=boundary+len(native.mts[1]);slots=[7]
 else:tilebase=boundary;metabase=boundary;slots=([7] if m['family']=='saffron' else [7,11] if m['family']=='hoenn' else [7,8])
 out=ROOT/'.validation-work/relocated'/m['family']/m['theme']/m['kind']
 subprocess.run([sys.executable,str(P/'tools/relocate.py'),str(d),str(out),'--tile-base',str(tilebase),'--metatile-base',str(metabase),'--palette-slots',*map(str,slots)],check=True,stdout=subprocess.DEVNULL)
 rows=np.frombuffer((out/'metatiles.bin').read_bytes(),dtype='<u2').reshape(-1,8)
 b=np.frombuffer((out/'tiles.4bpp').read_bytes(),dtype='uint8');tiles=np.stack([b&15,b>>4],axis=1).reshape(-1,8,8)
 palettes=native.pals.copy()
 for i,slot in enumerate(slots):palettes[slot]=s['palette_banks'][i]
 w,h=m['metatiles'];rgb=np.zeros((h*16,w*16,3),dtype='uint8')
 for my in range(h):
  for mx in range(w):
   mi=my*w+mx
   if mi in m['native_cells']:
    word=np.frombuffer((d/'map.source.bin').read_bytes(),dtype='<u2')[mi];row=native.mts[int((word&1023)>=boundary)][(word&1023)%boundary]
   else:row=rows[mi]
   for layer in range(2):
    for q in range(4):
     raw=int(row[layer*4+q]);tid=raw&1023
     if tid>=tilebase and tid<tilebase+len(tiles) and mi not in m['native_cells']:
      a=tiles[tid-tilebase].copy()
      if raw&1024:a=a[:,::-1]
      if raw&2048:a=a[::-1]
     else:a=tile_array(native,raw)
     visible=a!=0 if layer else np.ones((8,8),bool);x,y=mx*16+q%2*8,my*16+q//2*8
     dst=rgb[y:y+8,x:x+8];dst[visible]=np.array(palettes[raw>>12],dtype='uint8')[a][visible]
 assert np.array_equal(rgb,np.array(Image.open(d/'preview.png'))),str(d)+' relocated render mismatch'
 results.append({'module':str(d.relative_to(P)),'tile_base':tilebase,'metatile_base':metabase,'palette_slots':slots,'render_matches':True})
(P/'relocation-validation.json').write_text(json.dumps({'checked':len(results),'actual_game_installation':False,'modules':results},indent=2)+'\n')
print('PASS:',len(results),'relocated modules render identically; no game installation performed')
