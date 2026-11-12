"""Compile the first Void World town into native indexed tiles, maps and actors."""
from pathlib import Path
import copy,json,re,struct
import numpy as np
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
ART=ROOT/'graphics/void_oldale';DATA=ROOT/'data/void_oldale'
NAMES=['Wispit','Buttonmoth','Teacup','Sootling','Bellhop','Puddle','Wick','Umbrel']
ROOMS=[('Cottage','cottage','OldaleTown_House1',(160,144),(5,7),0),('Workshop','workshop','OldaleTown_House2',(176,128),(15,16),1),('RestHouse','rest','OldaleTown_PokemonCenter_1F',(224,144),(6,16),2),('Shop','shop','OldaleTown_Mart',(176,128),(14,6),3)]
RECTS=[(4,4,4,4),(14,13,4,4),(4,13,5,4),(13,3,4,4)]
def read(p):return json.loads((ROOT/p).read_text())
def save(p,d):
 p=ROOT/p;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,indent=2)+'\n')
def append(p,s):
 p=ROOT/p;t=p.read_text();p.write_text(t if s.strip() in t else t+'\n'+s+'\n')
def words(p):return np.frombuffer((ROOT/p).read_bytes(),dtype='<u2').copy()
def palette(path,colors):path.write_text('JASC-PAL\n0100\n16\n'+'\n'.join(' '.join(map(str,c)) for c in colors)+'\n')
def indexed(im):
 im=im.convert('RGB').quantize(colors=15,dither=Image.Dither.NONE)
 raw=np.array(im,dtype='uint8')+1;colors=np.array(im.getpalette()[:45]).reshape(15,3)
 colors=((colors.astype('uint16')*31+127)//255)*255//31
 colors=np.vstack([[0,0,0],colors]).astype('uint8')
 return raw,colors
def pimage(raw,colors,path):
 im=Image.fromarray(raw.astype('uint8'));im=im.convert('P');im.putpalette(list(colors.flatten())+[0]*(768-48));im.save(path,bits=4,transparency=0)
def packed(tiles):
 a=np.array(tiles,dtype='uint8').flatten();return (a[::2]|(a[1::2]<<4)).tobytes()
def compile_map(name,art,size,blocks):
 out=DATA/name;out.mkdir(parents=True,exist_ok=True)
 pixels,colors=indexed(Image.open(ART/'source'/f'{art}.png').resize(size,Image.Resampling.NEAREST))
 w,h=size[0]//16,size[1]//16
 if name=='Town':
  # True tile reuse: repeated terrain uses the same native Oldale metatile.
  # Buildings remain individually authored; no whole-map bitmap in VRAM.
  native=words('data/layouts/OldaleTown/map.bin').reshape(20,20)&1023
  protected=np.zeros((20,20),dtype=bool)
  for x,y,ww,hh in RECTS:protected[y:y+hh,x:x+ww]=True
  terrain={}
  for y in range(20):
   for x in range(20):
    if not protected[y,x]:
     key=int(native[y,x]);tile=pixels[y*16:y*16+16,x*16:x*16+16]
     if key not in terrain:terrain[key]=tile.copy()
     else:tile[:]=terrain[key]
 tiles=[np.zeros((8,8),dtype='uint8')];lookup={tiles[0].tobytes():0};mts=[];attrs=[];mapwords=[]
 for y in range(h):
  for x in range(w):
   row=[0]*4
   for q in range(4):
    tile=pixels[y*16+q//2*8:y*16+q//2*8+8,x*16+q%2*8:x*16+q%2*8+8];key=tile.tobytes()
    if key not in lookup:lookup[key]=len(tiles);tiles.append(tile.copy())
    row.append(lookup[key])
   mts.append(row);attrs.append(0x1000);mapwords.append((3<<12)|(0xC00 if blocks[y,x] else 0)|len(mts)-1)
 assert len(tiles)<=1024,(name,'Too many tiles',len(tiles))
 # Non-animated door behavior uses the standard map warp without native door DMA.
 if name=='Town':
  for _,_,_,_,(x,y),_ in ROOMS:attrs[y*w+x]=0x1060;mapwords[y*w+x]&=~0xC00
  for x,y,ww,hh in RECTS:
   for yy in range(y,y+hh-1):
    for xx in range(x,x+ww):attrs[yy*w+xx]&=0xFFF
 else:
  ex=7 if name=='RestHouse' else 4
  attrs[(h-1)*w+ex]=0x1065;mapwords[(h-1)*w+ex]&=~0xC00
 # A dedicated blank metatile prevents small rooms repeating their top-left art
 # in the camera border outside the actual map.
 blank=len(mts);mts.append([0]*8);attrs.append(0x1000)
 # Both private banks are padded; tile indices retain the 512-tile split.
 while len(tiles)<1024:tiles.append(np.zeros((8,8),dtype='uint8'))
 for bank,start in [('Primary',0),('Secondary',512)]:
  (out/(bank+'.4bpp')).write_bytes(packed(tiles[start:start+512]))
  m=mts if bank=='Primary' else [[0]*8]
  a=attrs if bank=='Primary' else [0x1000]
  (out/(bank+'Metatiles.bin')).write_bytes(np.array(m,dtype='<u2').tobytes())
  (out/(bank+'Attributes.bin')).write_bytes(np.array(a,dtype='<u2').tobytes())
 (out/'map.bin').write_bytes(np.array(mapwords,dtype='<u2').tobytes())
 (out/'border.bin').write_bytes(struct.pack('<4H',*([0x3C00|blank]*4)))
 palette(out/'palette.pal',colors);pimage(pixels,colors,out/'native-preview.png')
 definitions=[]
 for bank in ['Primary','Secondary']:
  label='Void'+name+bank;prefix='data/void_oldale/'+name+'/'
  definitions += [f'const u32 g{label}Tiles[] = INCBIN_U32("{prefix}{bank}.4bpp.smol");',f'const u16 g{label}Metatiles[] = INCBIN_U16("{prefix}{bank}Metatiles.bin");',f'const u16 g{label}Attributes[] = INCBIN_U16("{prefix}{bank}Attributes.bin");']
  definitions += [f'const struct Tileset gTileset_{label} = {{.isCompressed=TRUE,.isSecondary={"FALSE" if bank=="Primary" else "TRUE"},.tiles=g{label}Tiles,.palettes=gVoid{name}Palettes,.metatiles=g{label}Metatiles,.metatileAttributes=g{label}Attributes,.callback=NULL}};']
 paldef=f'const u16 gVoid{name}Palettes[][16] = {{\n'+''.join(f'    INCGFX_U16("data/void_oldale/{name}/palette.pal", ".gbapal"),\n' for _ in range(16))+'};\n'
 return paldef+'\n'.join(definitions)+'\n',dict(id='LAYOUT_VOID_OLDALE_'+name.upper(),name='VoidOldale'+name+'_Layout',width=w,height=h,primary_tileset='gTileset_Void'+name+'Primary',secondary_tileset='gTileset_Void'+name+'Secondary',border_filepath=f'data/void_oldale/{name}/border.bin',blockdata_filepath=f'data/void_oldale/{name}/map.bin',layout_version='emerald')

def creatures():
 atlas=Image.open(ART/'source/creatures.png').convert('RGBA');a=np.array(atlas);allcolors=a[:,:,:3][a[:,:,3]>128]
 _,colors=indexed(Image.fromarray(allcolors.reshape(-1,1,3)))
 palimg=Image.new('P',(1,1));palimg.putpalette(list(colors.flatten())+[0]*(768-48))
 graphics=[];pics=[];infos=[]
 for col,name in enumerate(NAMES):
  views=[]
  for row in range(3):
   cell=atlas.crop((round(col*atlas.width/8),round(row*atlas.height/3),round((col+1)*atlas.width/8),round((row+1)*atlas.height/3)))
   alpha=np.array(cell)[:,:,3]>128;ys,xs=np.where(alpha);assert len(xs)
   cell=cell.crop((int(xs.min()),int(ys.min()),int(xs.max()+1),int(ys.max()+1)))
   scale=min(14/cell.width,26/cell.height);cell=cell.resize((max(1,round(cell.width*scale)),max(1,round(cell.height*scale))),Image.Resampling.NEAREST)
   rgb=cell.convert('RGB').quantize(palette=palimg,dither=Image.Dither.NONE);raw=np.array(rgb);raw[np.array(cell)[:,:,3]<128]=0
   frame=np.zeros((32,16),dtype='uint8');x=(16-cell.width)//2;y=30-cell.height;frame[y:y+cell.height,x:x+cell.width]=raw;views.append(frame)
  frames=views.copy()
  for frame in views:
   up=np.zeros_like(frame);up[:-1]=frame[1:];down=np.zeros_like(frame);down[1:]=frame[:-1];frames.extend([up,down])
  out=ART/name.lower();out.mkdir(exist_ok=True);pimage(np.concatenate(frames,axis=1),colors,out/'walker.png');palette(out/'palette.pal',colors)
  graphics += [f'const u32 gObjectEventPic_Void{name}[] = INCGFX_U32("graphics/void_oldale/{name.lower()}/walker.png", ".4bpp", "-mwidth 2 -mheight 4");',f'const u16 gObjectEventPal_Void{name}[] = INCGFX_U16("graphics/void_oldale/{name.lower()}/palette.pal", ".gbapal");']
  pics += [f'static const struct SpriteFrameImage sPicTable_Void{name}[] = {{ overworld_ascending_frames(gObjectEventPic_Void{name}, 2, 4), }};']
  infos += [f'const struct ObjectEventGraphicsInfo gObjectEventGraphicsInfo_Void{name} = {{.tileTag=TAG_NONE,.paletteTag=OBJ_EVENT_PAL_TAG_VOID_{name.upper()},.reflectionPaletteTag=OBJ_EVENT_PAL_TAG_NONE,.size=256,.width=16,.height=32,.paletteSlot=PALSLOT_NPC_SPECIAL,.shadowSize=SHADOW_SIZE_M,.inanimate=FALSE,.compressed=FALSE,.tracks=TRACKS_NONE,.oam=&gObjectEventBaseOam_16x32,.subspriteTables=sOamTables_16x32,.anims=sAnimTable_Standard,.images=sPicTable_Void{name}}};']
 for file,lines in [('graphics',graphics),('pics',pics),('info',infos)]:
  (ROOT/f'src/data/object_events/void_{file}.h').write_text('\n'.join(lines)+'\n')
 for file,inc in [('object_event_graphics.h','void_graphics.h'),('object_event_pic_tables.h','void_pics.h'),('object_event_graphics_info.h','void_info.h')]:append('src/data/object_events/'+file,f'#include "{inc}"')
 p=ROOT/'include/constants/event_objects.h';s=p.read_text()
 if 'OBJ_EVENT_GFX_VOID_WISPIT' not in s:
  s=s.replace('    NUM_OBJ_EVENT_GFX,',''.join(f'    OBJ_EVENT_GFX_VOID_{n.upper()},\n' for n in NAMES)+'    NUM_OBJ_EVENT_GFX,')
  s+='\n'+''.join(f'#define OBJ_EVENT_PAL_TAG_VOID_{n.upper()} 0x{0x7D00+i:04X}\n' for i,n in enumerate(NAMES));p.write_text(s)
 p=ROOT/'src/data/object_events/object_event_graphics_info_pointers.h';s=p.read_text()
 if 'extern const struct ObjectEventGraphicsInfo gObjectEventGraphicsInfo_VoidWispit;' not in s:s=''.join(f'extern const struct ObjectEventGraphicsInfo gObjectEventGraphicsInfo_Void{n};\n' for n in NAMES)+s
 s=re.sub(r'^\s*\[OBJ_EVENT_GFX_VOID_\w+\].*\n','',s,flags=re.M)
 start=s.index('gObjectEventGraphicsInfoPointers[NUM_OBJ_EVENT_GFX]');at=s.index('};',start)
 s=s[:at]+''.join(f'    [OBJ_EVENT_GFX_VOID_{n.upper()}] = &gObjectEventGraphicsInfo_Void{n},\n' for n in NAMES)+s[at:];p.write_text(s)
 p=ROOT/'src/event_object_movement.c';s=p.read_text();needle='static const struct SpritePalette sObjectEventSpritePalettes[] = {'
 if '{gObjectEventPal_VoidWispit' not in s:s=s.replace(needle,needle+'\n'+''.join(f'    {{gObjectEventPal_Void{n}, OBJ_EVENT_PAL_TAG_VOID_{n.upper()}}},\n' for n in NAMES));p.write_text(s)

def actor(name,x,y):return dict(type='object',graphics_id='OBJ_EVENT_GFX_VOID_'+name.upper(),x=x,y=y,elevation=3,movement_type='MOVEMENT_TYPE_FACE_DOWN',movement_range_x=0,movement_range_y=0,trainer_type='TRAINER_TYPE_NONE',trainer_sight_or_berry_tree_id='0',script='VoidOldale_Talk_'+name,flag='0')
def main():
 DATA.mkdir(exist_ok=True);definitions=[];newlayouts=[]
 town=read('data/maps/OldaleTown/map.json');layouts=read('data/layouts/layouts.json');oldlay=next(l for l in layouts['layouts'] if l['id']==town['layout'])
 blocked=(words(oldlay['blockdata_filepath']).reshape(20,20)&0xC00)!=0;blocked[[0,-1],:]=True;blocked[:,[0,-1]]=True
 for x,y,w,h in RECTS:blocked[y:y+h,x:x+w]=True
 d,l=compile_map('Town','town',(320,320),blocked);definitions.append(d);newlayouts.append(l)
 newtown=copy.deepcopy(town);newtown.update(id='MAP_VOID_OLDALE_TOWN',name='VoidOldaleTown',layout=l['id'],music='MUS_MT_PYRE',connections=None,coord_events=[],bg_events=[],show_map_name=False,object_events=[actor('Wispit',9,10),actor('Sootling',12,8),actor('Bellhop',10,15),actor('Umbrel',17,11)])
 mapnames=['VoidOldaleTown'];newtown['warp_events']=[]
 roomactors={'Cottage':[actor('Buttonmoth',7,6),actor('Teacup',1,6)],'Workshop':[actor('Wick',8,5)],'Shop':[actor('Bellhop',4,3)],'RestHouse':[actor('Puddle',10,5),actor('Wispit',4,5)]}
 for suffix,art,original,size,door,warp in ROOMS:
  w,h=size[0]//16,size[1]//16;b=np.zeros((h,w),dtype=bool);b[:2]=True;b[:,[0,-1]]=True;b[-1]=True
  furniture={'Cottage':[(0,1,4,2),(8,1,2,2),(2,4,3,2),(9,7,1,1)],'Workshop':[(0,1,3,2),(7,1,4,2),(3,4,4,2),(0,6,1,1),(10,6,1,1)],'Shop':[(0,2,3,3),(6,4,2,3),(10,4,1,3),(10,2,1,1)],'RestHouse':[(2,1,10,3),(1,5,2,1),(11,5,2,2)]}[suffix]
  for x,y,ww,hh in furniture:b[y:y+hh,x:x+ww]=True
  d,l=compile_map(suffix,art,size,b);definitions.append(d);newlayouts.append(l)
  name='VoidOldale'+suffix;mapnames.append(name);m=read('data/maps/'+original+'/map.json')
  ex=7 if suffix=='RestHouse' else 4
  m.update(id='MAP_VOID_OLDALE_'+suffix.upper(),name=name,layout=l['id'],music='MUS_MT_PYRE',region='REGION_HOENN',region_map_section='MAPSEC_OLDALE_TOWN',map_type='MAP_TYPE_INDOOR',weather='WEATHER_NONE',connections=None,object_events=roomactors[suffix],coord_events=[],bg_events=[],show_map_name=False,warp_events=[dict(x=ex,y=h-1,elevation=0,dest_map='MAP_VOID_OLDALE_TOWN',dest_warp_id=str(warp))])
  save('data/maps/'+name+'/map.json',m);(ROOT/'data/maps'/name/'scripts.inc').write_text(name+'_MapScripts::\n\t.byte 0\n');append('data/event_scripts.s',f'\t.include "data/maps/{name}/scripts.inc"')
  newtown['warp_events'].append(dict(x=door[0],y=door[1],elevation=0,dest_map=m['id'],dest_warp_id='0'))
 # Keep room ordering identical to original town warp ordering.
 save('data/maps/VoidOldaleTown/map.json',newtown);(ROOT/'data/maps/VoidOldaleTown/scripts.inc').write_text('VoidOldaleTown_MapScripts::\n\t.byte 0\n');append('data/event_scripts.s','\t.include "data/maps/VoidOldaleTown/scripts.inc"')
 group=read('data/maps/map_groups.json');key='gMapGroup_VoidOldale'
 if key not in group['group_order']:group['group_order'].append(key)
 group[key]=mapnames;save('data/maps/map_groups.json',group)
 p=ROOT/'src/data/kanto_map_group_counts.h';s=p.read_text();line=f'    0, // {group["group_order"].index(key)}: {key}\n'
 if line not in s:p.write_text(s+line)
 for l in newlayouts:
  if not any(v['id']==l['id'] for v in layouts['layouts']):layouts['layouts'].append(l)
 save('data/layouts/layouts.json',layouts)
 (ROOT/'src/data/tilesets/void_oldale.h').write_text('#if !IS_FRLG\n'+''.join(definitions)+'#endif\n');append('src/tilesets.c','#include "data/tilesets/void_oldale.h"')
 append('include/tilesets.h','\n'.join(f'extern const struct Tileset gTileset_Void{n}{b};' for n in ['Town','Cottage','Workshop','RestHouse','Shop'] for b in ['Primary','Secondary']))
 creatures()
 texts={
 'Wispit':'I am not haunting you.\\nI am supervising your posture.',
 'Buttonmoth':'I ate a cardigan in my sleep.\\nNow I dream in cable knit.',
 'Teacup':'Please do not put tea in my head.\\nI already have a lot on my mind.',
 'Sootling':'I swallowed my own echo.\\nIt keeps asking for snacks.',
 'Bellhop':'I am the doorbell.\\nPlease knock. I get stage fright.',
 'Puddle':'I tried being ominous.\\nSomeone offered me a towel.',
 'Wick':'I am burning with ambition.\\nMostly at the top.',
 'Umbrel':'Forecast: a small chance of ghosts.\\nWe prefer to be called neighbors.'}
 lines=[]
 for n,t in texts.items():lines += [f'VoidOldale_Talk_{n}::',f'\tmsgbox VoidOldale_Text_{n}, MSGBOX_NPC','\tend',f'VoidOldale_Text_{n}:',f'\t.string "{t}$"']
 (DATA/'dialogue.inc').write_text('\n'.join(lines)+'\n');append('data/event_scripts.s','\t.include "data/void_oldale/dialogue.inc"')
 save('data/void_oldale/manifest.json',dict(maps=mapnames,creatures=NAMES,world='Void World: Hollow Oldale',scope='First playable visual preview; not a full world',source_resolution='Town320x320; rooms native Emerald dimensions',npc_frames='Front, back, left; three bob pairs. East mirrored by engine.',base='dd581a405516688bd0d0eef305d03b26fa73f19a'))
 print('Compiled five private maps, four fully redrawn rooms and eight native nine-frame creatures')
if __name__=='__main__':main()
