"""Check bond content, append-only layout, thresholds and safe static placement."""
from pathlib import Path
import json,re,struct
ROOT=Path(__file__).resolve().parents[1]
def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def main():
    content=load('data/bonds/events.json');events=content['events'];review=load('data/bonds/dialogue_review.json')
    assert len(events)==50 and len({e['id'] for e in events})==50
    layouts={l['id']:l for l in load('data/layouts/layouts.json')['layouts']}
    assert len(review['scenes'])==50
    for name in {e['character'] for e in events}:
        rows=[e for e in events if e['character']==name]
        assert [e['stage'] for e in rows]==[1,2,3,4,5]
        assert [e['total_bond_exp'] for e in rows]==[240,700,1320,2100,3040]
        for e in rows:
            assert e['missable'] is False and e['time_window']=='None'
            tile=e['marker_tile'];assert tile is not None
            m=load(f'data/maps/{e["map_folder"]}/map.json');l=layouts[m['layout']]
            x,y=tile['x'],tile['y'];assert 0<=x<l['width'] and 0<=y<l['height']
            raw=(ROOT/l['blockdata_filepath']).read_bytes()
            assert not struct.unpack_from('<H',raw,2*(y*l['width']+x))[0]&0xC00,(e['id'],tile)
            for kind in ['object_events','warp_events','coord_events','bg_events']:
                assert (x,y) not in {(a['x'],a['y']) for a in m.get(kind,[])},(e['id'],kind)
    text=json.dumps(review,ensure_ascii=False)
    assert not re.search(r'\b(?:the watch|universe|world switching|shared (?:party|PC))\b',text,re.I)
    for row in review['scenes']:
        count=3 if row['stage']==4 or (row['character']=='zuri' and row['stage']==2) else 1
        assert len(row['options'])==len(row['responses'])==count
        assert all(len(a)==len(b) for a,b in zip(row['options'],row['responses']))
    teams=load('data/bonds/trial_teams.json');assert len(teams)==40
    native_flags=load('data/kanto/symbol_manifest.json')['native_flags']
    assert not [n for n,v in native_flags.items() if 0x77A<=v<=0x7A1]
    for t in teams:
        assert len(t['team'])==4 and t['level'] in [40,50,60,70]
        assert all(len(m['moves'])==4 and m['ivs']==20 and m['evs']==0 and m['held_item'] is None for m in t['team'])
    header=(ROOT/'include/pokemon_storage_system.h').read_text()
    assert header.index('struct Pokemon fusions')<header.index('struct BondProgress bonds;')
    assert 'struct BondProgress bonds;' not in (ROOT/'include/global.h').read_text()
    for c in load('data/cast/characters.json'): assert c['life_stage']=='adult'
    party=(ROOT/'src/data/trainers_kanto.party').read_text()
    assert len(re.findall(r'^=== TRAINER_KANTO_DATA_BOND_',party,re.M))==40
    scenes=(ROOT/'src/data/bond_scenes.h').read_text()
    assert scenes.count('.intro =')==50
    assert 'Bonds_EventScript_Journal' in (ROOT/'data/cast/recruitment.inc').read_text()
    print('PASS: 50 ordered bond events, safe static marker tiles, authored choices, 40 four-member trials, silent mystery, adult framing and separate save suffix')
if __name__=='__main__':main()
