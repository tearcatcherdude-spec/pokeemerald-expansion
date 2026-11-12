"""Enforce appended content, exact artwork, geometry and encounter contracts."""
import hashlib,json,re,struct
from pathlib import Path
from variety_map_tools import ROOT,grid,neighbors,component
from build_variety_music import SCORES,make_score

DATA=ROOT/'data/trainer_variety'
def load(path):return json.loads((ROOT/path).read_text(encoding='utf-8'))

def main():
    roster=load('data/trainer_variety/roster.json');encounters=load('data/trainer_variety/encounters.json')
    assert len(roster)==32 and len(encounters)==64
    for path,sha in load('data/trainer_variety/asset_manifest.json').items():
        raw=(ROOT/path).read_bytes()
        if path.endswith('.pal'):raw=raw.replace(b'\r\n',b'\n')
        assert hashlib.sha256(raw).hexdigest()==sha,('Artwork changed',path)
        if path.endswith('.png'):
            expected=(64,64,4,3) if '/front_pics/' in path else (144,32,4,3)
            assert struct.unpack('>IIBB',raw[16:26])==expected,path
    contract=load('data/trainer_variety/map_contract.json')
    for path,old in contract.items():
        m=load(path);original=old['original'];added=[o for o in m['object_events'] if o.get('script','').startswith('Variety_EventScript_')]
        m['object_events']=[o for o in m['object_events'] if o not in added]
        assert m==original,('Existing map content changed',path)
        _,layout,floor=grid(original['name'])
        assert hashlib.sha256((ROOT/layout['blockdata_filepath']).read_bytes()).hexdigest()==old['geometry_sha']
        blocked={(o['x'],o['y']) for o in original['object_events']+added}
        for actor in added:
            p=actor['x'],actor['y']
            assert p in floor and actor['elevation']==floor[p]
            assert actor['trainer_type']=='TRAINER_TYPE_NONE' and actor['trainer_sight_or_berry_tree_id']=='0'
            assert sum(o['x']==p[0] and o['y']==p[1] for o in original['object_events']+added)==1
            adjacent=[n for n in neighbors(p) if n in floor and n not in blocked]
            assert adjacent,('Cannot talk to actor',path,p)
            reachable=component(floor,adjacent[0],blocked)
            assert len(reachable)>=30 and all(n in reachable for n in adjacent),('Actor cuts route',path,p)
            assert not any((e['x'],e['y'])==p for kind in ('warp_events','coord_events','bg_events') for e in original[kind])
    ids=[r['trainer_data_id'] for r in encounters]
    assert ids==list(range(674,738)) and len(set(ids))==64
    native=load('data/kanto/symbol_manifest.json')['native_flags']
    assert not [(n,v) for n,v in native.items() if 0x500+674<=v<0x500+738]
    for r in roster:
        appearances=[e for e in encounters if e['character']==r['id']]
        assert {e['region'] for e in appearances}=={'hoenn','kanto'} and len(appearances)==2
        for e in appearances:
            assert 8<=e['level']<=36 and len(e['team']) in (2,3,4)
    cafe=[e for e in encounters if e['map']=='KantoCeladonCity_Restaurant']
    assert {e['character'] for e in cafe}=={'hugo','otis','bastian','monty','florian','orson'}
    assert len({(e['x'],e['y']) for e in cafe})==6
    text=(DATA/'encounters.inc').read_text(encoding='utf-8')
    assert text.count('\ttrainerbattle_single VARIETY_TRAINER_')==64
    assert 'MSGBOX_YESNO' not in text
    assert not re.search(r'\b(?:the watch|universe|world switching|shared PC)\b',text,re.I)
    context=load('data/companion_dialogue/contexts.json')['contexts']
    rows=[r for r in context if r['key'].startswith('variety_')]
    assert len(rows)==32 and all(len(r['replies'])==11 for r in rows)
    for score in SCORES:
        expected,report=make_score(score)
        assert (ROOT/f'sound/songs/midi/mus_variety_{score[0]}.mid').read_bytes()==expected
        assert 100<=report['bpm']<160 and report['loop_end']-report['loop_start']==32*96
    assert len({hashlib.sha256(make_score(s)[0]).hexdigest() for s in SCORES})==7
    print('PASS: 32 exact indexed artwork sets, 64 independent talk battles, unchanged maps/actors/geometry, reachable approaches, Celadon club, 352 companion replies and seven reproducible original scores')

if __name__=='__main__':main()
