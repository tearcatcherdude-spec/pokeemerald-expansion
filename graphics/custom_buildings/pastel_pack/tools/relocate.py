"""Relocate one checked module; this does not modify a game repository."""
from pathlib import Path
import argparse,json,struct
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('module',type=Path);p.add_argument('output',type=Path)
p.add_argument('--tile-base',type=int,required=True);p.add_argument('--metatile-base',type=int,required=True)
p.add_argument('--palette-slots',type=int,nargs='+',required=True)
a=p.parse_args();m=json.loads((a.module/'module.json').read_text());s=json.loads((a.module/'editable_source.json').read_text())
assert m['primary_tile_boundary']<=a.tile_base and a.tile_base+m['tile_count']<=1024,'tile allocation exceeds secondary bank'
assert m['primary_tile_boundary']<=a.metatile_base and a.metatile_base+len(s['metatiles'])<=1024,'metatile allocation exceeds secondary bank'
assert len(a.palette_slots)==m['palette_count'] and len(set(a.palette_slots))==len(a.palette_slots)
assert all(0<=n<13 for n in a.palette_slots),'normal background palette slots are 0..12'
rows=[]
for i,row in enumerate(s['metatiles']):
 out=[]
 for j,v in enumerate(row):
  if s['custom_reference_masks'][i]&(1<<j):v=(v&~1023)|((v&1023)+a.tile_base)
  if s['custom_palette_masks'][i]&(1<<j):v=(v&4095)|(a.palette_slots[v>>12]<<12)
  out.append(v)
 rows.extend(out)
words=[v if i in m['native_cells'] else (v&0xFC00)|((v&1023)+a.metatile_base) for i,v in enumerate(s['map_words'])]
a.output.mkdir(parents=True,exist_ok=True)
(a.output/'tiles.4bpp').write_bytes((a.module/'tiles.4bpp').read_bytes())
(a.output/'metatiles.bin').write_bytes(struct.pack('<'+'H'*len(rows),*rows))
(a.output/'map-fragment.bin').write_bytes(struct.pack('<'+'H'*len(words),*words))
(a.output/'metatile_attributes.bin').write_bytes((a.module/'metatile_attributes.bin').read_bytes())
for i,slot in enumerate(a.palette_slots):(a.output/f'{slot:02}.pal').write_bytes((a.module/f'palette-{i:02}.pal').read_bytes())
(a.output/'allocation.json').write_text(json.dumps({'tile_base':a.tile_base,'metatile_base':a.metatile_base,'palette_slots':a.palette_slots,'module':str(a.module)},indent=2)+'\n')
print('Relocated into',a.output,'; confirm unused destination allocations before installing.')
