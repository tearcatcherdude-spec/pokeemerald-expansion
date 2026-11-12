"""Check installation boundaries, retained residents, routes and lesson safety."""
import json,re,struct,hashlib
from pathlib import Path
from variety_map_tools import ROOT,grid,neighbors,component,tileset,words,LAYOUTS
def load(p):return json.loads((ROOT/p).read_text())
def main():
    sites=load('data/venues/sites.json');assert len(sites)==12
    assert {(s['region'],s['theme']) for s in sites}=={(r,t) for r in ['hoenn','kanto'] for t in ['bakery','tutor','tea','bloom','glitch','rave']}
    for s in sites:
        city=load(f'data/maps/{s["city"]}/map.json');old=load(f'data/venues/originals/{s["city"]}.json')
        copy=dict(city);copy['layout']=old['layout'];assert copy==old,('Native city events changed',s['city'])
        l=LAYOUTS[city['layout']];ol=LAYOUTS[old['layout']];a=words(l['blockdata_filepath']);b=words(ol['blockdata_filepath'])
        x,y,w,h=s['rect'];assert len(a)==len(b);split=640 if s['region']=='kanto' else 512
        newattrs=[tileset(l[k],split==640) for k in ['primary_tileset','secondary_tileset']]
        oldattrs=[tileset(ol[k],split==640) for k in ['primary_tileset','secondary_tileset']]
        for i,(av,bv) in enumerate(zip(a,b)):
            if not (x<=i%l['width']<x+w and y<=i//l['width']<y+h):assert av==bv
            assert av&0xFC00==bv&0xFC00,('Collision/elevation changed',s['city'],i)
            am=av&1023;bm=bv&1023
            assert newattrs[am>=split][am%split if am<split else am-split]==oldattrs[bm>=split][bm%split if bm<split else bm-split],('Native behavior changed',s['city'],i)
        dx,dy=s['entrance'];assert a[dy*l['width']+dx]==b[dy*l['width']+dx]
        room=load(f'data/maps/{s["house"]}/map.json');oldroom=load(f'data/venues/originals/{s["house"]}.json')
        assert len(room['warp_events'])==len(oldroom['warp_events'])
        for wa,wb in zip(room['warp_events'],oldroom['warp_events']):
            assert wa['dest_map']==wb['dest_map'] and wa['dest_warp_id']==wb['dest_warp_id']
        assert room['coord_events']==oldroom['coord_events'] and room['bg_events']==oldroom['bg_events']
        for a,b in zip(room['object_events'],oldroom['object_events']):
            for key in b:
                if key not in ['x','y','elevation','movement_type','movement_range_x','movement_range_y']:assert a[key]==b[key],(s['house'],key)
        _,rl,floor=grid(s['house']);blocked={(o['x'],o['y']) for o in room['object_events']}
        assert len(blocked)==len(room['object_events'])
        start=(room['warp_events'][0]['x'],room['warp_events'][0]['y']-1)
        reach=component(floor,start,blocked)
        assert len(reach)>20,(s['house'],'exit approach blocked',start)
        for o in room['object_events']:
            pos=o['x'],o['y'];assert pos in floor,(s['house'],'actor in furniture',pos)
            assert any(n in reach for n in neighbors(pos)),(s['house'],'unreachable actor',pos)
        assert set(floor)-blocked<=reach,(s['house'],'disconnected walkable floor')
    for s in load('data/venues/tutor_stops.json'):
        m,l,floor=grid(s['map']);o=s['actor'];assert m['object_events'].count(o)==1
        blocked={(a['x'],a['y']) for a in m['object_events']};pos=o['x'],o['y'];ns=[p for p in neighbors(pos) if p in floor and p not in blocked]
        reach=component(floor,ns[0],blocked);assert len(reach)>=30 and all(p in reach for p in ns)
    for p,record in load('data/venues/battle_revision.json').items():
        raw=(ROOT/p).read_bytes();raw=raw.replace(b'\r\n',b'\n') if p.endswith('.pal') else raw
        assert hashlib.sha256(raw).hexdigest()==record['supplied_sha256']
    source=(ROOT/'src/roaming_tutor.c').read_text();moves=(ROOT/'include/constants/moves.h').read_text()
    gen4=moves[:moves.index('MOVES_COUNT_GEN4')];forbidden={'FISSURE','GUILLOTINE','HORN_DRILL','SHEER_COLD','SONIC_BOOM','DRAGON_RAGE','SPORE','DOUBLE_TEAM','MINIMIZE','SWORDS_DANCE','DRAGON_DANCE','NASTY_PLOT'}
    for move,level in re.findall(r'LESSON\((\w+), (\d+),',source):
        assert 'MOVE_'+move in gen4 and move not in forbidden and 5<=int(level)<=100
    assert 'level >= last - 1 + 20' in source
    assert 'roamingTutorLevelLo:5' in (ROOT/'include/pokemon.h').read_text()
    print('PASS: 12 private venues, exact city collision/elevation/behavior and doors, retained scripts/residents, connected rooms and six tutor stops; supplied battle artwork and Gen-IV lesson whitelist')
if __name__=='__main__':main()
