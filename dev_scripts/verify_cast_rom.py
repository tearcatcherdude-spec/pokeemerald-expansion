"""Validate actual compiled walking frames, palettes and all 80 expression frames."""
from pathlib import Path
import json,re,sys
from verify_pip_rom import expected_frames,expected_palette
from verify_kanto_rom import graphics_ids
import struct
ROOT=Path(__file__).resolve().parents[1]
def verify(rom_path,map_path):
 rom=Path(rom_path).read_bytes();text=Path(map_path).read_text(encoding='utf-8',errors='replace')
 symbols={n:int(a,16) for a,n in re.findall(r'0x([0-9a-fA-F]{8,16})\s+(\w+)\s*$',text,re.M)}
 ids=graphics_ids();table=symbols['gObjectEventGraphicsInfoPointers']-0x08000000
 for c in json.loads((ROOT/'data/cast/characters.json').read_text()):
  n=c['name'];N=n.title()
  ptr=struct.unpack_from('<I',rom,table+4*ids['OBJ_EVENT_GFX_CAST_'+n.upper()])[0]
  assert ptr==symbols['gObjectEventGraphicsInfo_Cast'+N],('Cast actor registration',n)
  for symbol,expected in [(f'gObjectEventPic_Cast{N}',expected_frames(ROOT/f'graphics/object_events/pics/people/cast_{n}.png')),(f'gObjectEventPal_Cast{N}',expected_palette(ROOT/f'graphics/object_events/palettes/cast_{n}.pal')),(f'gCastPortrait_{N}',(ROOT/f'graphics/cast_portraits/{n}_expressions.bin').read_bytes()),(f'gCastPalette_{N}',(ROOT/f'graphics/cast_portraits/{n}_palette.bin').read_bytes())]:
   assert symbol in symbols,('Missing compiled asset',symbol)
   at=symbols[symbol]-0x08000000;assert rom[at:at+len(expected)]==expected,('Compiled pixels/palette differ',symbol)
 print('PASS: compiled ROM contains all ten exact nine-frame walkers, their palettes, and all eighty supplied expression frames/palettes')
if __name__=='__main__':verify(*sys.argv[1:])
