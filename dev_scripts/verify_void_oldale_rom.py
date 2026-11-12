"""Reject missing creature registrations or mismatched compiled Void map arrays."""
from pathlib import Path
import json,re,struct,sys
from verify_kanto_rom import graphics_ids
from verify_pip_rom import expected_frames,expected_palette
ROOT=Path(__file__).resolve().parents[1]
def verify(romfile,mapfile):
 rom=Path(romfile).read_bytes();syms={n:int(a,16) for a,n in re.findall(r'0x([0-9a-fA-F]{8,16})\s+(\w+)\s*$',Path(mapfile).read_text(errors='replace'),re.M)}
 ids=graphics_ids();manifest=json.loads((ROOT/'data/void_oldale/manifest.json').read_text())
 def at(n,data):
  a=syms[n]-0x08000000;assert rom[a:a+len(data)]==data,('Compiled asset mismatch',n)
 for n in manifest['creatures']:
  p=syms['gObjectEventGraphicsInfoPointers']-0x08000000+ids['OBJ_EVENT_GFX_VOID_'+n.upper()]*4
  assert struct.unpack_from('<I',rom,p)[0]==syms['gObjectEventGraphicsInfo_Void'+n],('Creature not registered',n)
  at('gObjectEventPic_Void'+n,expected_frames(ROOT/f'graphics/void_oldale/{n.lower()}/walker.png'))
  at('gObjectEventPal_Void'+n,expected_palette(ROOT/f'graphics/void_oldale/{n.lower()}/palette.pal'))
 for name in ['Town','Cottage','Workshop','RestHouse','Shop']:
  for bank in ['Primary','Secondary']:
   for kind in ['Metatiles','Attributes']:at('gVoid'+name+bank+kind,(ROOT/f'data/void_oldale/{name}/{bank}{kind}.bin').read_bytes())
 print('PASS: eight exact registered Void creatures and all five compiled map metatile/attribute banks')
if __name__=='__main__':verify(*sys.argv[1:])
