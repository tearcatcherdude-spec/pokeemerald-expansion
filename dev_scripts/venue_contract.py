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
            m=copy.deepcopy(m);m['layout']=site['original_layout'];return m
    return m
