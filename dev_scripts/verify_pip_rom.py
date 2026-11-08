"""Compare all nine compiled Pip frames and RGB555 palette with accepted source assets."""
from pathlib import Path
import hashlib,re,struct,sys,zlib
ROOT=Path(__file__).resolve().parents[1]

def png_indices(path):
    data=path.read_bytes();pos=8;packed=b''
    while pos<len(data):
        size=struct.unpack_from('>I',data,pos)[0];kind=data[pos+4:pos+8];body=data[pos+8:pos+8+size];pos+=12+size
        if kind==b'IHDR':width,height,depth,color=struct.unpack('>IIBB',body[:10])
        if kind==b'IDAT':packed+=body
    assert (width,height,depth,color)==(144,32,4,3)
    raw=zlib.decompress(packed);stride=width//2;rows=[];at=0;previous=bytearray(stride)
    def paeth(a,b,c):
        p=a+b-c;pa,pb,pc=abs(p-a),abs(p-b),abs(p-c)
        return a if pa<=pb and pa<=pc else b if pb<=pc else c
    for _ in range(height):
        filter=raw[at];at+=1;row=bytearray(raw[at:at+stride]);at+=stride
        for x in range(stride):
            a=row[x-1] if x else 0;b=previous[x];c=previous[x-1] if x else 0
            predict=[0,a,b,(a+b)//2,paeth(a,b,c)][filter]
            row[x]=(row[x]+predict)&255
        rows.append([n for byte in row for n in (byte>>4,byte&15)]);previous=row
    return rows

def expected_frames(path=None):
    pixels=png_indices(path or ROOT/'graphics/object_events/pics/people/pip.png');out=bytearray()
    for frame in range(9):
        for tile_y in range(4):
            for tile_x in range(2):
                for y in range(8):
                    for x in range(0,8,2):
                        px=frame*16+tile_x*8+x;row=pixels[tile_y*8+y]
                        out.append(row[px]|row[px+1]<<4)
    return bytes(out)

def expected_palette(path=None):
    lines=(path or ROOT/'graphics/object_events/palettes/pip.pal').read_text().splitlines();assert lines[:3]==['JASC-PAL','0100','16']
    rgb=[tuple(map(int,s.split())) for s in lines[3:19]]
    return struct.pack('<16H',*[r>>3|(g>>3)<<5|(b>>3)<<10 for r,g,b in rgb])

def verify(rom_path,map_path):
    rom=Path(rom_path).read_bytes();text=Path(map_path).read_text(encoding='utf-8',errors='replace')
    symbols={n:int(a,16) for a,n in re.findall(r'0x([0-9a-fA-F]{8,16})\s+(\w+)\s*$',text,re.M)}
    for name,expected in [('gObjectEventPic_Pip',expected_frames()),('gObjectEventPal_Pip',expected_palette())]:
        start=symbols[name]-0x08000000;actual=rom[start:start+len(expected)]
        if actual!=expected:raise SystemExit('ROM ARTWORK FAILURE: '+name+' differs from accepted Morph artwork')
    print('PASS: actual ROM contains all nine Morph/Pip frames and the matching 16-color palette')
    return {'rom_sha256':hashlib.sha256(rom).hexdigest(),'pip_frames':9,'pip_graphics_bytes':2304,'pip_palette_bytes':32}

if __name__=='__main__':
    if len(sys.argv)!=3:raise SystemExit('usage: verify_pip_rom.py ROM.gba ROM.map')
    print(verify(sys.argv[1],sys.argv[2]))
