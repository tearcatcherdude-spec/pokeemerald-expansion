"""Reject a ROM with unregistered imported NPC graphics before artifact upload."""
from pathlib import Path
import json,re,struct,sys
ROOT=Path(__file__).resolve().parents[1]
def verify(rom_path,map_path):
 rom=Path(rom_path).read_bytes();text=Path(map_path).read_text(encoding='utf-8',errors='replace');symbols={n:int(a,16) for a,n in re.findall(r'0x([0-9a-fA-F]{8,16})\s+(\w+)\s*$',text,re.M)}
 source=(ROOT/'include/constants/event_objects.h').read_text();body=re.search(r'enum\s*\{(.*?)\};',source,re.S)[1];body=re.sub(r'/\*.*?\*/|//[^\n]*','',body,flags=re.S);ids={n.strip():i for i,n in enumerate(body.split(',')) if n.strip()}
 expected=dict(re.findall(r'\[(OBJ_EVENT_GFX_\w+)\]\s*=\s*&(gObjectEventGraphicsInfo_\w+)',(ROOT/'src/data/object_events/object_event_graphics_info_pointers.h').read_text()))
 manifest=json.loads((ROOT/'data/kanto/maps_manifest.json').read_text());graphics=set()
 for name in manifest['maps'].values():
  m=json.loads((ROOT/'data/maps'/name/'map.json').read_text())
  graphics.update(o['graphics_id'] for o in m['object_events'] if o['graphics_id'] in ids)
 table=symbols['gObjectEventGraphicsInfoPointers']-0x08000000
 for name in sorted(graphics):
  ptr=struct.unpack_from('<I',rom,table+ids[name]*4)[0]
  assert expected[name] in symbols,f'{name}: compiled graphics definition is missing'
  assert ptr==symbols[expected[name]],f'{name}: missing or incorrect compiled graphics registration ({ptr:#x})'
  assert 0x08000000<=ptr<0x08000000+len(rom),name
 print(f'PASS: {len(graphics)} imported NPC graphics resolve to their actual compiled definitions')
 return len(graphics)
if __name__=='__main__':verify(*sys.argv[1:])
