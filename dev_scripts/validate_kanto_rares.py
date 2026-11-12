from venue_contract import before_venue_layout
"""Verify the new actors, legal stats, preserved native maps and capture lifecycle."""
from pathlib import Path
import json,re
from build_kanto_rares import ROOT,digest,grid_for
from kanto_rare_content import ROWS

def main():
    records=json.loads((ROOT/'data/kanto/rare_encounters.json').read_text())
    base=json.loads((ROOT/'data/kanto/rare_base_maps.json').read_text())
    assert len(records)==len(ROWS)==16
    assert records[0]['species']=='BELDUM' and records[0]['map']=='WatchViridian' and records[0]['level']==6
    assert [r['rare_index'] for r in records]==list(range(16,32))
    assert [r['flag_id'] for r in records]==list(range(0xa8f0,0xa900))
    native=json.loads((ROOT/'data/kanto/symbol_manifest.json').read_text())['native_flags']
    assert not [n for n,v in native.items() if 0x8f0<=v<0x900 and 'UNUSED' not in n and not re.fullmatch(r'FLAG_0x[0-9A-F]+',n)]
    for folder in ['data/kanto','src']:
        for p in (ROOT/folder).rglob('*'):
            if p.suffix in ['.c','.h','.inc']:
                assert not re.search(r'\b(?:KANTO_)?FLAG_0x8F[0-9A-F]\b',p.read_text(encoding='utf-8')), ('Reserved flag in use',p)
    script=(ROOT/'data/kanto/rare_encounters.inc').read_text()
    old=(ROOT/'src/cozy_world.c').read_text().split('sRareEncounters[] = {')[1].split('#include')[0]
    assert re.findall(r'\{SPECIES_(\w+),',old)==['SENTRET','SHINX','EEVEE','MAREEP','RIOLU','TOGEPI','WOOPER','HOUNDOUR','GIBLE','MUNCHLAX','DRATINI','CROAGUNK','PORYGON','ELEKID','LARVITAR','DEINO']
    for r,authored in zip(records,ROWS):
        assert r['species']==authored['species'] and r['level']==authored['level'] and r['evs']==authored['evs']
        assert 5<=r['level']<=42 and sum(r['evs'])==510 and all(0<=v<=252 for v in r['evs'])
        m=before_venue_layout(json.loads((ROOT/'data/maps'/r['map']/'map.json').read_text()));actors=[o for o in m['object_events'] if o.get('script','').startswith('KantoRare_')]
        assert len(actors)==1
        actor=actors[0];assert actor['graphics_id']=='OBJ_EVENT_GFX_SPECIES('+r['species']+')'
        assert actor['flag']==hex(r['flag_id']) and actor['script']==r['script']
        assert (actor['x'],actor['y'],actor['elevation'])==(r['x'],r['y'],r['elevation'])
        m['object_events']=[o for o in m['object_events'] if o not in actors and not o.get('script','').startswith('Variety_EventScript_')]
        assert digest(m)==base[r['map']],('Native event/map changed',r['map'])
        layout,grid,behavior=grid_for(m);x,y=r['x'],r['y'];w=layout['width']
        assert not grid[y*w+x]&0xc00 and behavior(x,y)==r['behavior']
        assert r['behavior'] in ([0x10,0x15] if r['water'] else [0,2,3,8])
        ax,ay=r['approach'];assert abs(ax-x)+abs(ay-y)==1 and not grid[ay*w+ax]&0xc00
        assert (grid[ay*w+ax]>>12)==r['elevation']
        block=script.split(r['script']+'::',1)[1].split('KantoRare_'+r['species']+'_Intro::',1)[0]
        assert '\tsetwildbattle SPECIES_'+r['species']+', '+str(r['level']) in block
        assert block.index('B_OUTCOME_CAUGHT')<block.index('\tsetflag '+r['flag'])
        assert block.count('\tremoveobject ')==1 and '\tsetflag FLAG_TEMP_10' in block
        assert 'Script_CozyWorldPrepareRare' in block and 'Script_CozyWorldTrainRare' in block
        assert not re.search(r'\b(?:watch|world switching|shared (?:PC|party))\b',authored['intro'],re.I)
        assert (ROOT/'graphics/pokemon'/r['species'].lower()/'overworld.png').is_file()
    assert '\t.include "data/kanto/rare_encounters.inc"' in (ROOT/'data/event_scripts.s').read_text()
    print('PASS: 16 actual Pokemon sprites, 16 preserved native maps, legal 31-IV/510-EV definitions, separate capture flags and retry branches; early Viridian Beldum')
if __name__=='__main__':main()
