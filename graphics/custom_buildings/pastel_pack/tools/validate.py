"""Validate the standalone tile pack, without claiming a ROM play test."""
from pathlib import Path
import json,struct,hashlib,sys
from collections import deque
import numpy as np
from PIL import Image
PACK=Path(__file__).resolve().parents[1]
report=[]
for family in ['hoenn','kanto','saffron']:
 for theme in (['bloom','glitch'] if family=='saffron' else ['bakery','tutor','glitch','rave','bloom','tea']):
  for kind in (['exterior'] if family=='saffron' else ['exterior','interior']):
   d=PACK/'modules'/family/theme/kind
   if '--partial' in sys.argv and not (d/'module.json').exists():continue
   m=json.loads((d/'module.json').read_text());s=json.loads((d/'editable_source.json').read_text());w,h=m['metatiles'];n=w*h
   assert len(s['metatiles'])==n and len(s['attributes'])==n
   assert len((d/'metatile_attributes.bin').read_bytes())==n*m['attribute_width']
   tilebytes=(d/'tiles.4bpp').read_bytes();assert len(tilebytes)==m['tile_count']*32
   decoded=np.array([[v&15,v>>4] for v in tilebytes],dtype='uint8').reshape(-1,64)
   assert all(bytes(row)==bytes.fromhex(src) for row,src in zip(decoded,s['tiles']))
   atlas=Image.open(d/'tiles.png');assert atlas.mode=='P' and (d/'tiles.png').read_bytes()[24]==4
   for i,src in enumerate(s['tiles']):
    assert bytes(np.array(atlas.crop((i%16*8,i//16*8,i%16*8+8,i//16*8+8))).ravel())==bytes.fromhex(src)
   for i,row in enumerate(s['metatiles']):
    for j,v in enumerate(row):
     if s['custom_reference_masks'][i]&(1<<j):assert (v&1023)<m['tile_count']
     if s['custom_palette_masks'][i]&(1<<j):assert (v>>12)<m['palette_count']
     if kind=='interior' and not s['custom_reference_masks'][i]&(1<<j):assert (v&1023)<m['primary_tile_boundary']
   assert m['tile_count']<=1024-m['primary_tile_boundary']
   assert len(s['palette_banks'])==m['palette_count']
   expected=b''.join(struct.pack('<H',(r>>3)|((g>>3)<<5)|((b>>3)<<10)) for pal in s['palette_banks'] for r,g,b in pal)
   assert expected==(d/'palette.gbapal').read_bytes()
   art=Image.open(d/'art.png');assert art.mode=='P' and art.size==(w*16,h*16)
   preview=np.array(Image.open(d/'preview.png'));native=np.array(Image.open(PACK/'templates'/family/('exterior-with-ground.png' if kind=='exterior' else 'interior.png')))
   words=np.array(s['map_words'],dtype='uint16').reshape(h,w)
   if kind=='exterior':
    mask=np.array(Image.open(PACK/'templates'/family/'silhouette-mask.png'))>0
    assert np.array_equal(np.array(art.convert('RGBA'))[:,:,3]>0,mask),'indexed exterior alpha differs from native silhouette'
    assert np.array_equal(preview[~mask],native[~mask]),'outer silhouette/background changed'
    door=json.loads((PACK/'templates'/family/'geometry.json').read_text())['door']
    if door is not None:
     dx,dy=door
     assert np.array_equal(preview[dy*16:dy*16+16,dx*16:dx*16+16],native[dy*16:dy*16+16,dx*16:dx*16+16]),'door changed'
    source=np.frombuffer((d/'map.source.bin').read_bytes(),dtype='<u2').reshape(h,w)
    assert np.array_equal(words&0xFC00,source&0xFC00)
   else:
    grid=np.array(Image.open(PACK/'templates'/family/'collision-grid.png'))>0
    lock=np.array(Image.open(PACK/'templates'/family/'interior-warp-lock.png'))>0
    assert np.array_equal(preview[lock],native[lock])
    free=((words>>10)&3)==0
    exits=[(e['x'],e['y']) for e in m['native_events']['warp_events']]
    assert all(free[y,x] for x,y in exits)
    seen=set(exits);q=deque(exits)
    while q:
     x,y=q.popleft()
     for nx,ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
      if 0<=nx<w and 0<=ny<h and free[ny,nx] and (nx,ny) not in seen:seen.add((nx,ny));q.append((nx,ny))
    assert len(seen)==int(free.sum()),'unreachable clear floor'
    for e in m['native_events']['object_events']:
     if e.get('graphics_id')!='OBJ_EVENT_GFX_CLIPBOARD':assert (e['x'],e['y']) in seen
    mask=np.zeros((h*16,w*16),dtype=bool)
    for oi,obj in enumerate(json.loads((PACK/'templates'/family/'furniture-layout.json').read_text())):
     a=np.array(Image.open(PACK/'templates/furniture'/(obj['source_object']+'.png')))[:,:,3]>0;x,y=obj['x'],obj['y'];hh,ww=a.shape;mask[y:y+hh,x:x+ww]|=a
     assert grid[y//16:(y+hh)//16,x//16:(x+ww)//16].all()
     exported=np.array(Image.open(d/'furniture'/f'{oi:02}-{obj["source_object"]}.png'))[:,:,3]>0
     assert np.array_equal(exported,a),'exported furniture silhouette changed'
    assert np.array_equal(mask,np.array(Image.open(PACK/'templates'/family/'furniture-mask.png'))>0)
   report.append({'module':f'{family}/{theme}/{kind}','tiles':m['tile_count'],'palette_banks':m['palette_count'],'passed':True})
(PACK/('validation-partial.json' if '--partial' in sys.argv else 'validation.json')).write_text(json.dumps({'module_count':len(report),'checks':['4bpp and indexed-PNG round trip','tile/palette reference bounds','Emerald/FRLG secondary capacity','attribute widths','unchanged exterior silhouette/background and native door','native exit pixels and warp positions','native furniture silhouettes and blocked footprints','all clear floor and original actor positions reachable from exits'],'rom_build_tested':False,'emulator_tested':False,'modules':report},indent=2)+'\n')
print('PASS:',len(report),'modules; no ROM build or emulator test claimed')
