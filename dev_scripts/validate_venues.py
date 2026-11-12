"""Check installation boundaries, retained residents, routes and lesson safety."""
import json,re,struct,hashlib
from pathlib import Path
from venue_contract import before_venue_layout
from variety_map_tools import ROOT,grid,neighbors,component,tileset,words,LAYOUTS
def load(p):return json.loads((ROOT/p).read_text())
def main():
    sites=load('data/venues/sites.json');assert len(sites)==12
    assert {(s['region'],s['theme']) for s in sites}=={(r,t) for r in ['hoenn','kanto'] for t in ['bakery','tutor','tea','bloom','glitch','rave']}
    for s in sites:
        city=load(f'data/maps/{s["city"]}/map.json');old=load(f'data/venues/originals/{s["city"]}.json')
        copy=before_venue_layout(city);assert copy==old,('Native city events changed',s['city'])
        l=LAYOUTS[city['layout']];ol=LAYOUTS[old['layout']];a=words(l['blockdata_filepath']);b=words(ol['blockdata_filepath'])
        x,y,w,h=s['rect'];assert len(a)==len(b);split=640 if s['region']=='kanto' else 512
        newattrs=[tileset(l[k],split==640) for k in ['primary_tileset','secondary_tileset']]
        oldattrs=[tileset(ol[k],split==640) for k in ['primary_tileset','secondary_tileset']]
        for i,(av,bv) in enumerate(zip(a,b)):
            if not (x<=i%l['width']<x+w and y<=i//l['width']<y+h):assert av==bv
            if s.get('open_lot') and x<=i%l['width']<x+w and y<=i//l['width']<y+h:continue
            assert av&0xFC00==bv&0xFC00,('Collision/elevation changed',s['city'],i)
            am=av&1023;bm=bv&1023
            assert newattrs[am>=split][am%split if am<split else am-split]==oldattrs[bm>=split][bm%split if bm<split else bm-split],('Native behavior changed',s['city'],i)
        dx,dy=s['entrance']
        if not s.get('open_lot'):assert a[dy*l['width']+dx]==b[dy*l['width']+dx]
        else:
            assert a[dy*l['width']+dx]==(0x43D if split==640 else 0x421)
            # A complete, level, empty ring guarantees that the lot is bypassable.
            oldmap,oldlayout,oldfloor=grid(s['city'])
            saved=oldmap['layout'];oldmap['layout']=s['original_layout']
            from variety_map_tools import tileset as getattrs
            oldraw=b
            oldfloor={(i%ol['width'],i//ol['width']):v>>12 for i,v in enumerate(oldraw) if not v&0xC00 and (oldattrs[(v&1023)>=split][(v&1023)-split if (v&1023)>=split else v&1023]&(511 if split==640 else 255)) in {0,2,3,6,7,8,10,11,0x21,0x24,0x25,0xD0,0xD1}}
            rectangle={(xx,yy) for yy in range(y,y+h) for xx in range(x,x+w)}
            ring={(xx,yy) for yy in range(y-1,y+h+1) for xx in range(x-1,x+w+1)}
            assert ring<=oldfloor.keys()
            blocked={(o['x'],o['y']) for o in old['object_events']}
            assert not ring&blocked
            start=(x-1,y-1);before=component(oldfloor,start,blocked);after=component(oldfloor,start,blocked|rectangle)
            assert after==before-rectangle,('New lot cuts walking routes',s['city'])
        room=load(f'data/maps/{s["house"]}/map.json');oldroom=load(f'data/venues/originals/{s["original_house"]}.json')
        if s.get('open_lot'):
            assert load(f'data/maps/{s["original_house"]}/map.json')==oldroom
            oldroom=dict(room) # New room has no displaced residents or original events.
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
    facades=load('data/venues/facades.json')
    city=load(f'data/maps/{facades["city"]}/map.json');old=load(f'data/venues/originals/{facades["city"]}.json')
    assert before_venue_layout(city)==old
    a=words(LAYOUTS[city['layout']]['blockdata_filepath']);b=words(LAYOUTS[old['layout']]['blockdata_filepath']);w=LAYOUTS[city['layout']]['width']
    changed={(x+xx,y+yy) for p in facades['placements'] for x,y,sw,sh in [p['rect']] for yy in range(sh) for xx in range(sw)}
    for i,(av,bv) in enumerate(zip(a,b)):
        assert av&0xFC00==bv&0xFC00
        if (i%w,i//w) not in changed:assert av==bv
    assert all(t<1008 and t not in range(416,512) for t in facades['allocated_tiles'])
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
    print('PASS: 12 private venues and two Saffron facades; protected native events and doors, bypassable new lots, connected rooms and six tutor stops; supplied battle artwork and Gen-IV lesson whitelist')
if __name__=='__main__':main()
