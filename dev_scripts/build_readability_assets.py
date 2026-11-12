"""Compile reviewed art sources to indexed game assets; retain every prior file.

Generated paintings are source material only. This compiler establishes the
native pixel dimensions, silhouette/door masks, 4bpp indices and GBA palettes.
Never re-run over later edits: the revision ledger pins the compiled results.
"""
from pathlib import Path
import json,hashlib,shutil,struct
from collections import deque
import numpy as np
from PIL import Image,ImageDraw

ROOT=Path(__file__).resolve().parents[1]
REV=ROOT/'graphics/readability_v2'
ORIGINALS=REV/'originals'
LEDGER={}

def sha(p):return hashlib.sha256(p.read_bytes().replace(b'\r\n',b'\n') if p.suffix in ('.pal','.json') else p.read_bytes()).hexdigest()
def retain(p):
    rel=p.relative_to(ROOT);backup=ORIGINALS/rel
    if not backup.exists():backup.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,backup)
    LEDGER[rel.as_posix()]={'original':backup.relative_to(ROOT).as_posix(),'original_sha256':sha(backup)}
    return backup
def writepal(p,colors):p.write_text('JASC-PAL\n0100\n16\n'+'\n'.join(' '.join(map(str,c)) for c in colors)+'\n')
def gba(colors):return [[round(int(c)/8)*8 if int(c)<248 else 248 for c in row] for row in colors]

def foreground(im):
    a=np.array(im.convert('RGB'));lo=a.min(2);spread=a.max(2)-lo
    # Flood only the pale neutral source-sheet background; enclosed whites stay.
    background=(lo>=178)&(spread<65)&(a[:,:,1]>=a[:,:,0]-5)
    seen=np.zeros(background.shape,dtype=bool);h,w=seen.shape;q=deque()
    for x in range(w):q.append((x,0));q.append((x,h-1))
    for y in range(h):q.append((0,y));q.append((w-1,y))
    while q:
        x,y=q.popleft()
        if not(0<=x<w and 0<=y<h) or seen[y,x] or not background[y,x]:continue
        seen[y,x]=True;q.extend(((x-1,y),(x+1,y),(x,y-1),(x,y+1)))
    return ~seen

def indexed(rgb,mask,forced_colors=None):
    a=np.array(rgb.convert('RGB'));values=a[mask]
    strip=Image.fromarray(values.reshape(1,-1,3));q=strip.quantize(colors=15,method=Image.Quantize.MEDIANCUT,dither=Image.Dither.NONE)
    colors=gba(np.array(q.getpalette()[:45]).reshape(15,3).tolist())
    # Index zero is transparency, never a visible black or magenta pixel.
    colors=forced_colors or [[255,0,255]]+colors
    distances=((a.astype('int32')[:,:,None,:]-np.array(colors[1:])[None,None,:,:])**2).sum(3)
    indices=distances.argmin(2).astype('uint8')+1;indices[~mask]=0
    out=Image.fromarray(indices,'P');out.putpalette(sum(colors,[])+[0]*(768-48));out.info['transparency']=0
    return out,colors

def palette_polish(colors):
    out=[colors[0]]
    for c in colors[1:]:
        a=np.array(c,dtype=float);l=float(a@[.2126,.7152,.0722])
        gain=(.75 if l<35 else 1.25 if l<100 else 1.07 if l<180 else 1)
        out.append(np.clip(np.rint(a*gain/8)*8,0,248).astype(int).tolist())
    return out

def trainers():
    paths=sorted((ROOT/'graphics/trainers/front_pics').glob('cast_*.png'))+sorted((ROOT/'graphics/trainers/front_pics').glob('variety_*.png'))
    for i,p in enumerate(paths):
        old=retain(p);pal=ROOT/'graphics/trainers/palettes'/p.with_suffix('.pal').name;retain(pal)
        if p.stem in ('cast_pip','variety_barnaby'):
            # Reject generated identity/prop drift; polish the original instead.
            im=Image.open(old);colors=palette_polish(np.array(im.getpalette()[:48]).reshape(16,3).tolist());im.putpalette(sum(colors,[])+[0]*720)
            method='Original silhouette and props retained; palette contrast revision'
        else:
            source=Image.open(REV/f'sources/trainers-{i//8+1:02}.png').convert('RGB');cw=source.width/4;ch=source.height/2;col=i%4;row=(i%8)//4
            cell=source.crop((round(col*cw),round(row*ch+ch*.055),round((col+1)*cw),round(row*ch+ch*.87)))
            mask=foreground(cell);ys,xs=np.where(mask);box=(xs.min(),ys.min(),xs.max()+1,ys.max()+1)
            cell=cell.crop(box);mask=Image.fromarray(mask.astype('uint8')*255).crop(box)
            height=60;width=min(62,round(cell.width*height/cell.height));cell=cell.resize((width,height),Image.Resampling.NEAREST);mask=np.array(mask.resize((width,height),Image.Resampling.NEAREST))>0
            canvas=Image.new('RGB',(64,64),'#ff00ff');canvas.paste(cell,((64-width)//2,62-height));fullmask=np.zeros((64,64),bool);fullmask[62-height:62,(64-width)//2:(64-width)//2+width]=mask
            im,colors=indexed(canvas,fullmask);method='Reviewed generated source compiled at 64x64 with 15 visible GBA colors'
        im.save(p,bits=4,transparency=0);writepal(pal,colors);LEDGER[p.relative_to(ROOT).as_posix()]['method']=method
    for p in sorted((ROOT/'graphics/object_events/pics/people').glob('cast_*.png'))+sorted((ROOT/'graphics/object_events/pics/people').glob('variety_*.png')):
        old=retain(p);im=Image.open(old);colors=palette_polish(np.array(im.getpalette()[:48]).reshape(16,3).tolist());im.putpalette(sum(colors,[])+[0]*720);im.save(p,bits=4,transparency=0)
        pal=ROOT/'graphics/object_events/palettes'/p.with_suffix('.pal').name;retain(pal);writepal(pal,colors)
        assert np.array_equal(np.array(im),np.array(Image.open(old))),'Walking indices/frame geometry must remain exact'

def compile_exterior(d,candidate,forced_colors=None):
    m=json.loads((d/'module.json').read_text());s=json.loads((d/'editable_source.json').read_text());w,h=m['metatiles'];oldart=Image.open(d/'art.png').convert('RGBA');mask=np.array(oldart)[:,:,3]>0
    native=Image.open(ROOT/'graphics/custom_buildings/pastel_pack/templates'/m['family']/'exterior-with-ground.png').convert('RGB')
    candidate=candidate.resize(oldart.size,Image.Resampling.NEAREST);im,colors=indexed(candidate,mask,forced_colors)
    # Keep the native doorway pixels/tiles and masks as an exact locked region.
    rgba=im.convert('RGBA');preview=rgba.convert('RGB');pixels=np.array(preview);nativepixels=np.array(native)
    import sys
    sys.path.insert(0,str(ROOT/'graphics/custom_buildings/pastel_pack/tools'))
    from native_map import NativeMap
    original=NativeMap(m['native_map']);ox,oy,_,_=m['native_rect']
    tiles=[np.zeros((8,8),dtype='uint8')];ids={tiles[0].tobytes():0};rows=[];indices=np.array(im)
    for i in range(w*h):
        if i in m['native_cells']:rows.append(s['metatiles'][i]);continue
        mid=int(original.blocks[oy+i//w,ox+i%w])&1023;bank=int(mid>=original.primary)
        row=list(map(int,original.mts[bank][mid-original.primary*bank][:4]))
        for q in range(4):
            x=i%w*16+q%2*8;y=i//w*16+q//2*8;t=indices[y:y+8,x:x+8];key=t.tobytes()
            if key not in ids:ids[key]=len(tiles);tiles.append(t.copy())
            row.append(ids[key])
        rows.append(row)
    for p in d.iterdir():
        if p.is_file() and p.suffix in ('.png','.pal','.bin','.4bpp','.json'):retain(p)
    for i in m['native_cells']:
        x=i%w*16;y=i//w*16;pixels[y:y+16,x:x+16]=nativepixels[y:y+16,x:x+16]
    pixels[~mask]=nativepixels[~mask]
    s['tiles']=[bytes(t.flatten()).hex() for t in tiles];s['palette_banks']=[colors];s['metatiles']=rows
    s['custom_reference_masks']=[0 if i in m['native_cells'] else 240 for i in range(w*h)];s['custom_palette_masks']=s['custom_reference_masks'].copy();m['tile_count']=len(tiles)
    flat=np.array(tiles).flatten();(d/'tiles.4bpp').write_bytes(bytes(flat[::2]|flat[1::2]<<4))
    atlas=Image.new('P',(128,((len(tiles)+15)//16)*8));atlas.putpalette(sum(colors,[])+[0]*720)
    for i,t in enumerate(tiles):atlas.paste(Image.fromarray(t,'P'),(i%16*8,i//16*8))
    atlas.save(d/'tiles.png',bits=4);im.save(d/'art.png',bits=4,transparency=0);Image.fromarray(pixels).save(d/'preview.png')
    writepal(d/'palette-00.pal',colors);(d/'palette.gbapal').write_bytes(b''.join(struct.pack('<H',(r>>3)|((g>>3)<<5)|((b>>3)<<10)) for r,g,b in colors))
    (d/'editable_source.json').write_text(json.dumps(s,indent=2)+'\n');(d/'module.json').write_text(json.dumps(m,indent=2)+'\n')
    (d/'metatiles.local.bin').write_bytes(struct.pack('<'+'H'*(len(rows)*8),*sum(rows,[])))

def buildings():
    source=Image.open(REV/'sources/buildings.png').convert('RGB');cw=source.width/4;ch=source.height/4
    paths=list((ROOT/'graphics/custom_buildings/pastel_pack/modules').glob('*/*/exterior/art.png'))
    candidates=[]
    for i,p in enumerate(paths):
        col=i%4;row=i//4;cell=source.crop((round(col*cw),round(row*ch+ch*.075),round((col+1)*cw),round((row+1)*ch)))
        mask=foreground(cell);ys,xs=np.where(mask);candidate=cell.crop((xs.min(),ys.min(),xs.max()+1,ys.max()+1));candidates.append(candidate)
    tall=[np.array(c.resize((80,96),Image.Resampling.NEAREST)) for p,c in zip(paths,candidates) if p.parts[-4]=='saffron']
    joint=Image.fromarray(np.concatenate(tall,axis=1));_,shared=indexed(joint,np.ones((96,160),bool))
    for p,candidate in zip(paths,candidates):compile_exterior(p.parent,candidate,shared if p.parts[-4]=='saffron' else None)
    # Interiors retain every authored tile/furniture/warp shape. Edit only native
    # palette source banks to separate furniture outlines from their floors.
    for p in (ROOT/'graphics/custom_buildings/pastel_pack/modules').glob('*/*/interior/editable_source.json'):
        retain(p);s=json.loads(p.read_text());s['palette_banks']=[palette_polish(pal) for pal in s['palette_banks']];p.write_text(json.dumps(s,indent=2)+'\n')
        for i,pal in enumerate(s['palette_banks']):target=p.parent/f'palette-{i:02}.pal';retain(target);writepal(target,pal)
        target=p.parent/'palette.gbapal';retain(target);target.write_bytes(b''.join(struct.pack('<H',(r>>3)|((g>>3)<<5)|((b>>3)<<10)) for pal in s['palette_banks'] for r,g,b in pal))
        export_interior(p.parent,s)

def export_interior(d,s):
    """Render source indices/banks, including retained native exit references."""
    m=json.loads((d/'module.json').read_text());w,h=m['metatiles'];split=m['primary_tile_boundary'];palfirst=7 if split==640 else 6
    paths=[ROOT/Path(m['native_'+part+'_tileset'].replace('\\','/')) for part in ['primary','secondary']]
    native=[]
    for p in paths:
        a=np.array(Image.open(p/'tiles.png'))&15;native.append([a[y:y+8,x:x+8] for y in range(0,a.shape[0],8) for x in range(0,a.shape[1],8)])
    nativepals=[np.array([list(map(int,t.split())) for t in (paths[i>=palfirst]/'palettes'/f'{i:02}.pal').read_text().splitlines()[3:19]],dtype='uint8') for i in range(16)]
    tiles=[np.frombuffer(bytes.fromhex(t),dtype='uint8').reshape(8,8) for t in s['tiles']];rgb=np.zeros((h*16,w*16,3),dtype='uint8')
    for i,row in enumerate(s['metatiles']):
        for j,v in enumerate(row):
            t=v&1023
            tile=tiles[t] if s['custom_reference_masks'][i]&(1<<j) else native[t>=split][t-split if t>=split else t]
            if v&1024:tile=tile[:,::-1]
            if v&2048:tile=tile[::-1]
            pal=np.array(s['palette_banks'][v>>12],dtype='uint8') if s['custom_palette_masks'][i]&(1<<j) else nativepals[v>>12]
            x=i%w*16+j%2*8;y=i//w*16+(j%4)//2*8;mask=np.ones((8,8),bool) if j<4 else tile!=0;rgb[y:y+8,x:x+8][mask]=pal[tile][mask]
    for name in ['preview.png','art.png','tiles.png']:
        target=d/name;retain(target)
        if name=='preview.png':Image.fromarray(rgb).save(target)
        elif name=='art.png':Image.fromarray(rgb).quantize(colors=64,dither=Image.Dither.NONE).save(target)
        else:
            im=Image.open(target);im.putpalette(sum(s['palette_banks'][0],[])+[0]*720);im.save(target,bits=4)
    layout=json.loads((ROOT/'graphics/custom_buildings/pastel_pack/templates'/m['family']/'furniture-layout.json').read_text())
    for i,o in enumerate(layout):
        target=d/'furniture'/f'{i:02}-{o["source_object"]}.png';retain(target);im=Image.open(target).convert('RGBA');a=np.array(im);x,y=o['x'],o['y'];a[:,:,:3]=rgb[y:y+im.height,x:x+im.width];Image.fromarray(a).save(target)

def main():
    assert not (REV/'revision.json').exists(),'Do not overwrite an already compiled revision'
    trainers();buildings()
    for rel,row in LEDGER.items():row['revised_sha256']=sha(ROOT/rel)
    (REV/'revision.json').write_text(json.dumps({'authorized_revision':'User requested all custom buildings/NPCs clearer, 2026-11-12','base_commit':'240f43430e1078faef5174c6c93563f8aafa0a66','files':LEDGER},indent=2)+'\n')
    print('Compiled readability revision; retained',len(LEDGER),'original files')
if __name__=='__main__':main()
