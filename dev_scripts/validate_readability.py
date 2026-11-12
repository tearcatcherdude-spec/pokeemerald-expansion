"""Guard native sprite formats, original assets and the retired route overlays."""
from pathlib import Path
import json,struct
import numpy as np
from PIL import Image
from asset_revision import digest
ROOT=Path(__file__).resolve().parents[1]
def main():
    revision=json.loads((ROOT/'graphics/readability_v2/revision.json').read_text())
    for rel,row in revision['files'].items():
        assert digest(ROOT/row['original'])==row['original_sha256'],('Original lost',rel)
        assert digest(ROOT/rel)==row['revised_sha256'],('Revision changed',rel)
    for pattern,folder,size,count in [('cast_*.png','trainers/front_pics',(64,64),11),('variety_*.png','trainers/front_pics',(64,64),32),('cast_*.png','object_events/pics/people',(144,32),10),('variety_*.png','object_events/pics/people',(144,32),32)]:
        paths=list((ROOT/'graphics'/folder).glob(pattern));assert len(paths)==count
        for p in paths:
            im=Image.open(p);assert im.mode=='P' and im.size==size and p.read_bytes()[24]==4
            assert np.array(im).max()<16 and im.info['transparency']==0
            palette=ROOT/'graphics'/('trainers/palettes' if folder.startswith('trainers') else 'object_events/palettes')/p.with_suffix('.pal').name
            colors=[int(v) for line in palette.read_text().splitlines()[3:19] for v in line.split()]
            assert len(colors)==48 and colors==im.getpalette()[:48],('PNG/palette mismatch',p)
            if size==(144,32):
                original=ROOT/revision['files'][p.relative_to(ROOT).as_posix()]['original']
                assert np.array_equal(np.array(im),np.array(Image.open(original))),'Walking frame geometry changed'
    layouts={l['id']:l for l in json.loads((ROOT/'data/layouts/layouts.json').read_text())['layouts']}
    for name in ['Route104','KantoRoute11']:
        old=json.loads((ROOT/f'data/venues/originals/{name}.json').read_text());new=json.loads((ROOT/f'data/maps/{name}/map.json').read_text())
        assert new==old,('Retired route not fully restored',name)
    for site in json.loads((ROOT/'data/venues/sites.json').read_text()):
        if site.get('replacement_warp') is None:continue
        a=(ROOT/layouts[site['layout']]['blockdata_filepath']).read_bytes();b=(ROOT/layouts[site['original_layout']]['blockdata_filepath']).read_bytes()
        av=np.frombuffer(a,dtype='<u2');bv=np.frombuffer(b,dtype='<u2');assert np.array_equal(av&0xFC00,bv&0xFC00),'Existing-house walking collision changed'
        x,y=site['entrance'];width=layouts[site['layout']]['width'];assert av[y*width+x]==bv[y*width+x],'Native doorway changed'
    print('PASS: 43 indexed battle sprites, 42 exact nine-frame walking layouts, retained originals; two routes restored and replacement-house collision/doors unchanged')
if __name__=='__main__':main()
