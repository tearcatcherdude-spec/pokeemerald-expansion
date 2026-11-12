"""Protect native neighbor graphics visible during seamless map connections."""
import json
from render_venues import ROOT, LAYOUTS, bank

def main():
    maps={m['id']:m for p in (ROOT/'data/maps').glob('*/map.json') for m in [json.loads(p.read_text())]}
    count=0
    for site in json.loads((ROOT/'data/venues/sites.json').read_text()):
        original=json.loads((ROOT/'data/venues/originals'/(site['city']+'.json')).read_text())
        layout=LAYOUTS[site['original_layout']]
        before=bank(layout['secondary_tileset']);after=bank(LAYOUTS[site['layout']]['secondary_tileset'])
        primary=bank(layout['primary_tileset']);split=640 if site['region']=='kanto' else 512
        for connection in original.get('connections') or []:
            neighbor=maps[connection['map']]
            snap=ROOT/'data/venues/originals'/(neighbor['name']+'.json')
            if snap.exists():neighbor=json.loads(snap.read_text())
            nl=LAYOUTS[neighbor['layout']]
            mids=set()
            for key in ['blockdata_filepath','border_filepath']:
                raw=(ROOT/nl[key]).read_bytes()
                mids.update(int.from_bytes(raw[i:i+2],'little')&1023 for i in range(0,len(raw),2))
            for mid in mids:
                if mid>=split:
                    index=mid-split
                    if index>=len(before[1]):continue
                    assert (before[1][index]==after[1][index]).all(),(site['city'],neighbor['name'],'metatile',mid)
                    row=before[1][index]
                else:row=primary[1][mid]
                for value in row:
                    value=int(value);tile=(value&1023)-split
                    if tile>=0 and tile<len(before[0]):
                        assert (before[0][tile]==after[0][tile]).all(),(site['city'],neighbor['name'],'tile',tile)
                    pal=value>>12
                    assert (before[2][pal]==after[2][pal]).all(),(site['city'],neighbor['name'],'palette',pal)
            count+=1
    print(f'PASS: native graphics, metatiles and palettes preserved for all {count} connected-map views around 12 venues')

if __name__=='__main__':main()
