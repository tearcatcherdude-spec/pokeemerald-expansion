from pathlib import Path
root=Path(__file__).resolve().parents[1]
pixels=bytearray(2048)
def pixel(x,y,c):
 tile=(x//64)*32+(y//8)*8+(x%64)//8
 at=tile*32+(y%8)*4+(x%8)//2;shift=(x&1)*4
 pixels[at]=(pixels[at]&~(15<<shift))|(c<<shift)
def rect(x,y,w,h,c):
 for yy in range(y,y+h):
  for xx in range(x,x+w):pixel(xx,yy,c)
for y in range(32):
 for x in range(128):
  if (x<3 or x>=125) and (y<3 or y>=29):continue
  pixel(x,y,1 if x in (0,127) or y in (0,31) else 2)
rect(4,1,120,1,9);rect(4,30,120,1,3)
heart=[0x66,0xff,0xff,0xff,0x7e,0x3c,0x18,0]
for y in range(8):
 for x in range(8):
  if heart[y]&(1<<(7-x)):pixel(4+x,3+y,6)
rect(6,23,116,6,1);rect(8,24,112,4,8)
text='// Generated native 4bpp OBJ panel; python dev_scripts/build_affection_hud_panel.py\nstatic const u8 ALIGNED(4) sPanelTiles[2048] = {\n'
text+=''.join('    '+','.join(f'0x{v:02X}' for v in pixels[i:i+32])+',\n' for i in range(0,2048,32))+'};\n'
(root/'src/data/affection_hud_panel.h').write_text(text)
