"""Narrow exception for reviewed private venue layouts; all old fields stay checked."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def before_venue_layout(m):
    m=copy.deepcopy(m)
    travel=ROOT/'data/venues/tutor_stops.json'
    if travel.exists():
        for stop in json.loads(travel.read_text()):
            if stop['map']==m['name']:
                assert m['object_events'].count(stop['actor'])==1
                m['object_events'].remove(stop['actor'])
    sites=ROOT/'data/venues/sites.json'
    if not sites.exists():return m
    for site in json.loads(sites.read_text()):
        if site['city']==m['name']:
            assert m['layout']==site['layout'],('Unexpected venue layout',m['name'])
            if site.get('open_lot'):
                old=json.loads((ROOT/f'data/venues/originals/{m["name"]}.json').read_text())
                assert len(m['warp_events'])==len(old['warp_events'])+1
                assert m['warp_events'][-1]==dict(x=site['entrance'][0],y=site['entrance'][1],elevation=0,dest_map=json.loads((ROOT/f'data/maps/{site["house"]}/map.json').read_text())['id'],dest_warp_id='0')
                m['warp_events'].pop()
            m['layout']=site['original_layout'];return m
    return m
