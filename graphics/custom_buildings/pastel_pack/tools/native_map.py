"""Read the current project's native tiles/maps for geometry-preserving art."""
from pathlib import Path
import json, re, struct, os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parents[1]
GAME=Path(os.environ.get('POKEEMERALD_ROOT',str(ROOT.parents[2])))
OUT=ROOT/'.validation-work'
OUT.mkdir(exist_ok=True)
HEAD=(GAME/'src/data/tilesets/headers.h').read_text(encoding='utf-8')
MTS=(GAME/'src/data/tilesets/metatiles.h').read_text(encoding='utf-8')
LAYOUTS={x['id']:x for x in json.loads((GAME/'data/layouts/layouts.json').read_text())['layouts']}

def words(path):
    b=Path(path).read_bytes();return np.frombuffer(b,dtype='<u2').copy()
def tileset(symbol):
    body=re.search(r'const struct Tileset '+re.escape(symbol)+r'\s*=\s*\{(.*?)\};',HEAD,re.S)[1]
    name=re.search(r'\.metatiles\s*=\s*(\w+)',body)[1]
    path=re.search(r'\b'+re.escape(name)+r'\[\].*?INCBIN_U16\("([^"]+)"\)',MTS)[1]
    p=(GAME/path).parent
    return p

class NativeMap:
    def __init__(self,name):
        self.name=name;self.events=json.loads((GAME/f'data/maps/{name}/map.json').read_text())
        self.layout=LAYOUTS[self.events['layout']];l=self.layout
        self.w,self.h=l['width'],l['height'];self.frlg=l['layout_version']=='frlg'
        self.primary=640 if self.frlg else 512;self.pal_primary=7 if self.frlg else 6
        self.folders=[tileset(l['primary_tileset']),tileset(l['secondary_tileset'])]
        self.images=[Image.open(p/'tiles.png') for p in self.folders]
        self.mts=[words(p/'metatiles.bin').reshape(-1,8) for p in self.folders]
        self.attrs=[np.frombuffer((p/'metatile_attributes.bin').read_bytes(),dtype='<u4' if self.frlg else '<u2').copy() for p in self.folders]
        self.pals=[]
        for i in range(16):
            p=self.folders[int(i>=self.pal_primary)]/'palettes'/f'{i:02}.pal'
            self.pals.append([tuple(map(int,s.split())) for s in p.read_text().splitlines()[3:19]])
        self.blocks=words(GAME/l['blockdata_filepath']).reshape(self.h,self.w)
        self.cache={}
    def attribute(self,mid):
        bank=int(mid>=self.primary);return int(self.attrs[bank][mid-self.primary*bank])
    def metatile(self,mid):
        if mid in self.cache:return self.cache[mid]
        bank=int(mid>=self.primary);row=self.mts[bank][mid-self.primary*bank]
        rgb=np.zeros((16,16,3),dtype='uint8');pb=np.zeros((16,16),dtype='uint8');pi=np.zeros((16,16),dtype='uint8')
        for layer in range(2):
            for q in range(4):
                t=int(row[layer*4+q]);tile=t&1023;si=int(tile>=self.primary);tile-=si*self.primary;im=self.images[si]
                arr=np.array(im.crop(((tile%(im.width//8))*8,(tile//(im.width//8))*8,(tile%(im.width//8))*8+8,(tile//(im.width//8))*8+8)))&15
                if t&1024:arr=arr[:,::-1]
                if t&2048:arr=arr[::-1]
                x,y=(q%2)*8,(q//2)*8;visible=arr!=0 if layer else np.ones((8,8),dtype=bool)
                dest=rgb[y:y+8,x:x+8];dest[visible]=np.array(self.pals[t>>12],dtype='uint8')[arr][visible]
                pb[y:y+8,x:x+8][visible]=t>>12;pi[y:y+8,x:x+8][visible]=arr[visible]
        result=(rgb,pb,pi);self.cache[mid]=result;return result
    def render(self):
        rgb=np.zeros((self.h*16,self.w*16,3),dtype='uint8');banks=np.zeros((self.h*16,self.w*16),dtype='uint8');indices=banks.copy()
        for y in range(self.h):
            for x in range(self.w):
                a,b,c=self.metatile(int(self.blocks[y,x])&1023)
                rgb[y*16:y*16+16,x*16:x*16+16]=a;banks[y*16:y*16+16,x*16:x*16+16]=b;indices[y*16:y*16+16,x*16:x*16+16]=c
        return Image.fromarray(rgb),banks,indices

def main():
    for name in ['PetalburgCity','SaffronCity_Frlg','PetalburgCity_House1','SaffronCity_House_Frlg']:
        m=NativeMap(name);im,b,p=m.render();im.save(OUT/(name+'.png'))
        print(name,im.size,m.folders,m.events.get('warp_events',[]))
        if m.w>20:
            large=im.resize((im.width*2,im.height*2),Image.Resampling.NEAREST);d=ImageDraw.Draw(large)
            for y in range(m.h):
                for x in range(m.w):
                    d.text((x*32+1,y*32+1),f'{x},{y}',fill='#ffffff',stroke_width=1,stroke_fill='#333333')
            large.save(OUT/(name+'-grid.png'))
if __name__=='__main__':main()
