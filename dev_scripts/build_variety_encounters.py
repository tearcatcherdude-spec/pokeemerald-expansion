"""Compile reviewed encounter data without rewriting any existing map content."""
from pathlib import Path
import copy,hashlib,json,textwrap
from variety_map_tools import ROOT,grid,neighbors,component

DATA=ROOT/'data/trainer_variety'

def digest(v):return hashlib.sha256(json.dumps(v,sort_keys=True).encode()).hexdigest()

def text(label,value):
    pages=value.split('\n\n');formatted=[]
    for page in pages:
        # Wrap at conservative native dialogue width; preserve authored page breaks.
        lines=[]
        for line in page.splitlines():lines+=textwrap.wrap(line,34,break_long_words=False)
        formatted.append('\\n'.join(lines[:2])+''.join('\\l'+l for l in lines[2:]))
    return label+'::\n\t.string "'+'\\p'.join(formatted).replace('"','\"')+'$"\n\n'

def choose_position(name, ident, current, cafe_index):
    m,l,f=grid(name)
    old=[o for o in current if not o.get('script','').startswith('Variety_EventScript_')]
    blocked={(o['x'],o['y']) for o in current}
    forbidden=set(blocked)
    for typ in ('warp_events','coord_events','bg_events'):
        for e in m[typ]:
            p=e['x'],e['y'];forbidden.update([p]+neighbors(p))
    for e in json.loads((ROOT/'data/bonds/events.json').read_text())['events']:
        if e['map_folder']==name and e.get('marker_tile'):
            forbidden.add((e['marker_tile']['x'],e['marker_tile']['y']))
    if name=='KantoCeladonCity_Restaurant':
        p=[(4,3),(6,3),(8,3),(4,5),(6,5),(8,5)][cafe_index]
        assert p in f and p not in forbidden,(name,p)
        return p,f[p]
    candidates=[]
    for p in f:
        x,y=p
        if p in forbidden or x<2 or y<2 or x>=l['width']-2 or y>=l['height']-2:continue
        if name=='Route104' and ((ident=='barnaby' and y<50) or (ident=='dahlia' and y>35)):continue
        if name=='Route115' and y<70:continue
        if name=='Route109' and y>24:continue
        if name=='Route111' and y<105:continue
        if any(n not in f or n in blocked for n in neighbors(p)):continue
        if any(abs(x-o['x'])+abs(y-o['y'])<3 for o in current):continue
        # Keep room for player, human companion, and Pokemon follower on screen.
        crowd=sum(abs(x-o['x'])<=10 and abs(y-o['y'])<=8 for o in current)
        if crowd>9:continue
        nearby=min((abs(x-o['x'])+abs(y-o['y']) for o in old),default=8)
        if nearby<3:continue
        area=component(f,p)
        if len(area)<40:continue
        after=component(f,neighbors(p)[0],blocked|{p})
        # No new actor may cut a corridor or make its own neighbors inaccessible.
        if not all(n in after for n in neighbors(p)):continue
        # Stable tie-break distributes separate characters instead of piling them up.
        bias=int(hashlib.sha256(f'{ident}:{name}:{x},{y}'.encode()).hexdigest()[:6],16)/0x1000000
        score=crowd*5+abs(nearby-5)+bias
        candidates.append((score,p,f[p]))
    assert candidates,('No safe placement',name,ident)
    _,p,e=min(candidates)
    return p,e

def main():
    design=json.loads((DATA/'encounter_design.json').read_text())
    reunions=json.loads((DATA/'reunions.json').read_text())
    roster={r['id']:r for r in json.loads((DATA/'roster.json').read_text())}
    baseline_path=DATA/'map_contract.json'
    baseline=json.loads(baseline_path.read_text()) if baseline_path.exists() else {}
    maps={};encounters=[];party=[];defs=[];scripts=[];cafe_index=0
    existing=(ROOT/'src/data/trainers_kanto.party').read_text().split('\n// BEGIN TRAINER VARIETY')[0].rstrip()
    for i,r in enumerate(design):
        ident=r['id'];u=ident.upper();symbol=roster[ident]['symbol']
        for ri,region in enumerate(('hoenn','kanto')):
            name,level=r[region];key=f'{u}_{region.upper()}';trainer_id=674+i*2+ri
            path=f'data/maps/{name}/map.json'
            if name not in maps:
                m=json.loads((ROOT/path).read_text())
                m['object_events']=[o for o in m['object_events'] if not o.get('script','').startswith('Variety_EventScript_')]
                if path not in baseline:
                    _,layout,_=grid(name)
                    baseline[path]={'original':copy.deepcopy(m),'geometry_sha':hashlib.sha256((ROOT/layout['blockdata_filepath']).read_bytes()).hexdigest()}
                maps[name]=m
            m=maps[name];p,elevation=choose_position(name,ident,m['object_events'],cafe_index)
            if name=='KantoCeladonCity_Restaurant':cafe_index+=1
            x,y=p
            actor={'type':'object','local_id':'LOCALID_VARIETY_'+key,'graphics_id':'OBJ_EVENT_GFX_VARIETY_'+u,
                   'x':x,'y':y,'elevation':elevation,'movement_type':'MOVEMENT_TYPE_FACE_DOWN',
                   'movement_range_x':0,'movement_range_y':0,'trainer_type':'TRAINER_TYPE_NONE',
                   'trainer_sight_or_berry_tree_id':'0','script':'Variety_EventScript_'+key,'flag':'0'}
            if name=='KantoCeladonCity_Restaurant' and y==5:actor['movement_type']='MOVEMENT_TYPE_FACE_UP'
            m['object_events'].append(actor)
            defs += [f'#define TRAINER_KANTO_DATA_VARIETY_{key} {trainer_id}',f'#define VARIETY_TRAINER_{key} (KANTO_TRAINER_BASE + {trainer_id})']
            count=2 if level<=14 else 3 if level<=26 else 4
            members=r['team'][:count]
            # Evolve ordinary early forms only in later regional appearances.
            evolve={'Budew':'Roselia','Buizel':'Floatzel','Hoothoot':'Noctowl','Mareep':'Flaaffy','Shinx':'Luxio','Burmy':'Wormadam','Spinarak':'Ariados','Swablu':'Altaria','Gulpin':'Swalot','Wingull':'Pelipper','Electrike':'Manectric','Aipom':'Ambipom','Lombre':'Ludicolo'}
            if level>=30:members=[evolve.get(s,s) for s in members]
            sex='Female' if ident in {'vesper','nyxie','sable','opaline','cinder','dahlia','echo','briar','fable','taffy','roux','juniper','nettle','miri'} else 'Male'
            party.append(f'=== TRAINER_KANTO_DATA_VARIETY_{key} ===\nName: {("CLATTER" if ident=="clatter" else ident.upper())}\nClass: Pkmn Trainer 1\nPic: Variety {ident.title()}\nGender: {sex}\nMusic: {sex}\nDouble Battle: No\nAI: Check Bad Move / Try To Faint\n')
            for j,species in enumerate(members):
                mon_level=level-(1 if j==0 and count>2 else 0)
                party.append(f'{species}\nLevel: {mon_level}\nIVs: 12 HP / 12 Atk / 12 Def / 12 SpA / 12 SpD / 12 Spe\n')
            other=f'{u}_{"KANTO" if region=="hoenn" else "HOENN"}'
            scripts.append(f'Variety_EventScript_{key}::\n\tlock\n\tfaceplayer\n\tgoto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_{key}), Variety_EventScript_{key}_Post\n\tgoto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_{other}), Variety_EventScript_{key}_Battle\n\tmsgbox Variety_Text_{u}_Reunion, MSGBOX_DEFAULT\nVariety_EventScript_{key}_Battle::\n\ttrainerbattle_single VARIETY_TRAINER_{key}, Variety_Text_{u}_Intro, Variety_Text_{u}_Defeat\nVariety_EventScript_{key}_Post::\n\tmsgbox Variety_Text_{u}_Post, MSGBOX_AUTOCLOSE\n\trelease\n\tend\n\n')
            encounters.append({'id':key,'character':ident,'region':region,'map':name,'x':x,'y':y,'elevation':elevation,'level':level,'team':members,'trainer_data_id':trainer_id,'local_id':'LOCALID_VARIETY_'+key,'object_id':len(m['object_events'])})
        scripts += [text('Variety_Text_'+u+'_'+kind.title(),r[kind]) for kind in ('intro','defeat','post')]
        scripts.append(text('Variety_Text_'+u+'_Reunion',reunions[ident]))
    for name,m in maps.items():(ROOT/f'data/maps/{name}/map.json').write_text(json.dumps(m,indent=2)+'\n')
    (DATA/'map_contract.json').write_text(json.dumps(baseline,indent=2)+'\n')
    (DATA/'encounters.json').write_text(json.dumps(encounters,indent=2)+'\n')
    (ROOT/'include/constants/trainer_variety.h').write_text('#ifndef GUARD_TRAINER_VARIETY_H\n#define GUARD_TRAINER_VARIETY_H\n'+'\n'.join(defs)+'\n#endif\n')
    (DATA/'encounters.inc').write_text(''.join(scripts))
    (ROOT/'src/data/trainers_kanto.party').write_text(existing+'\n\n// BEGIN TRAINER VARIETY\n\n'+'\n'.join(party))
    p=ROOT/'include/constants/kanto_progress.h';s=p.read_text().replace('#define KANTO_TRAINER_COUNT 674','#define KANTO_TRAINER_COUNT 738')
    if '#include "constants/trainer_variety.h"' not in s:s=s.replace('#include "constants/kanto_rare.h"','#include "constants/trainer_variety.h"\n#include "constants/kanto_rare.h"')
    p.write_text(s)
    p=ROOT/'data/event_scripts.s';s=p.read_text(encoding='utf-8')
    if 'data/trainer_variety/encounters.inc' not in s:s+='\n#if !IS_FRLG\n\t.include "data/trainer_variety/encounters.inc"\n#endif\n'
    p.write_text(s,encoding='utf-8')
    print('Generated 64 talk-triggered encounters; six friends together in Celadon.')

if __name__=='__main__':main()
