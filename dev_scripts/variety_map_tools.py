"""Source-map floor/route checks shared by placement authoring and validation."""
from pathlib import Path
import json,re,struct
from collections import deque
ROOT=Path(__file__).resolve().parents[1]
LAYOUTS={l['id']:l for l in json.loads((ROOT/'data/layouts/layouts.json').read_text())['layouts']}
HEADERS='\n'.join(p.read_text() for p in (ROOT/'src/data/tilesets').glob('*.h'))

def words(path):
    raw=(ROOT/path).read_bytes()
    return struct.unpack('<'+'H'*(len(raw)//2),raw)

def tileset(symbol, frlg):
    body=re.search(r'const struct Tileset '+symbol+r'\s*=\s*\{(.*?)\};',HEADERS,re.S).group(1)
    attr=re.search(r'\.metatileAttributes\s*=\s*(\w+)',body).group(1)
    path=re.search(r'const u16 '+attr+r'\[\]\s*=\s*INCBIN_U16\("([^"]+)"',HEADERS).group(1)
    raw=(ROOT/path).read_bytes()
    unit=4 if frlg else 2
    return struct.unpack("<"+("I" if frlg else "H")*(len(raw)//unit),raw)

def grid(name):
    m=json.loads((ROOT/f'data/maps/{name}/map.json').read_text())
    l=LAYOUTS[m['layout']];w,h=l['width'],l['height'];raw=words(l['blockdata_filepath'])
    frlg=l.get('layout_version')=='frlg'
    split=640 if frlg else 512
    attrs=[tileset(l[k],frlg) for k in ('primary_tileset','secondary_tileset')]
    floor={};safe={0,2,3,6,7,8,10,11,0x21,0x24,0x25,0xD0,0xD1}
    # Imported FRLG maps retain their native u32 attributes and 640-tile split.
    for y in range(h):
        for x in range(w):
            v=raw[y*w+x];mid=v&1023;si=int(mid>=split);mi=mid-split*si
            behavior=attrs[si][mi]&(511 if frlg else 255)
            if not v&0xC00 and behavior in safe:
                floor[x,y]=v>>12
    return m,l,floor

def neighbors(p):
    x,y=p
    return [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]

def component(floor,start,blocked=()):
    blocked=set(blocked);seen=set();q=deque([start])
    while q:
        p=q.popleft()
        if p in seen or p not in floor or p in blocked:continue
        seen.add(p)
        q.extend(n for n in neighbors(p) if n not in seen and n in floor and n not in blocked and (floor[p]==floor[n] or 0 in (floor[p],floor[n])))
    return seen

if __name__=='__main__':
    import sys
    m,l,f=grid(sys.argv[1]);objects={(o['x'],o['y']):str(i%10) for i,o in enumerate(m['object_events'])}
    for y in range(l['height']):
        print(f'{y:2} '+''.join(objects.get((x,y),'.' if (x,y) in f else '#') for x in range(l['width'])))
