"""Append Kanto encounters on accessible native tiles without editing terrain."""
from pathlib import Path
from collections import deque
import hashlib,json,re,struct,textwrap
from kanto_rare_content import ROWS
ROOT=Path(__file__).resolve().parents[1]
def digest(v):return hashlib.sha256(json.dumps(v,sort_keys=True).encode()).hexdigest()
def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def grid_for(m):
    layout=next(l for l in load('data/layouts/layouts.json')['layouts'] if l['id']==m['layout'])
    source=(ROOT/'src/data/tilesets/kanto.h').read_text(encoding='utf-8');banks=[]
    for key in ['primary_tileset','secondary_tileset']:
        body=re.search(r'const struct Tileset '+layout[key]+r' =\s*\{(.*?)\};',source,re.S)[1]
        symbol=re.search(r'\.metatileAttributes = (\w+)',body)[1]
        path=re.search(r'const u16 '+symbol+r'\[\] = INCBIN_U16\("([^"]+)"',source)[1]
        raw=(ROOT/path).read_bytes();banks.append(struct.unpack('<'+'I'*(len(raw)//4),raw))
    raw=(ROOT/layout['blockdata_filepath']).read_bytes();grid=struct.unpack('<'+'H'*(len(raw)//2),raw)
    def behavior(x,y):
        idx=grid[y*layout['width']+x]&1023;bank=idx>=640;idx-=640 if bank else 0
        return banks[bank][idx]&0x1ff
    return layout,grid,behavior

def place(m,water):
    layout,grid,behavior=grid_for(m);w,h=layout['width'],layout['height']
    valid={(x,y) for y in range(1,h-1) for x in range(1,w-1)
           if not grid[y*w+x]&0xc00 and behavior(x,y) in ([0x10,0x15] if water else [0,2,3,8])}
    occupied={(o['x'],o['y']) for o in m['object_events']}
    original_events=occupied|{(o['x'],o['y']) for k in ['warp_events','coord_events','bg_events'] for o in m[k]}
    remaining=valid-occupied;components=[]
    while remaining:
        first=min(remaining);part={first};queue=deque([first]);remaining.remove(first)
        while queue:
            x,y=queue.popleft()
            for v in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if v in remaining:remaining.remove(v);part.add(v);queue.append(v)
        components.append(part)
    assert components,('No reachable terrain',m['name'],water)
    component=max(components,key=len);candidates=[]
    for x,y in sorted(component):
        if not (3<=x<w-3 and 3<=y<h-3):continue
        if any(abs(x-a)+abs(y-b)<3 for a,b in original_events):continue
        if m['name']=='WatchViridian' and y<h//2:continue
        adjacent=[v for v in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)] if v in component]
        if len(adjacent)<3:continue
        if any((x==o['x'] or y==o['y']) and abs(x-o['x'])+abs(y-o['y'])<=int(o.get('trainer_sight_or_berry_tree_id','0'))+1
               for o in m['object_events'] if o.get('trainer_type')=='TRAINER_TYPE_NORMAL'):continue
        available=component-{(x,y)};seen={min(available)};queue=deque(seen)
        while queue:
            a,b=queue.popleft()
            for v in [(a+1,b),(a-1,b),(a,b+1),(a,b-1)]:
                if v in available and v not in seen:seen.add(v);queue.append(v)
        if len(seen)!=len(available):continue
        near=sum(abs(o['x']-x)<=10 and abs(o['y']-y)<=8 for o in m['object_events'])
        if near>11:continue
        score=abs(x-w*.37)+abs(y-h*.65)
        candidates.append((score,x,y,adjacent[0]))
    assert candidates,('No safe placement',m['name'],len(component))
    _,x,y,approach=min(candidates)
    return dict(x=x,y=y,elevation=grid[y*w+x]>>12,approach=list(approach),behavior=behavior(x,y),component_tiles=len(component))

def main():
    assert len(ROWS)==16 and len({r['map'] for r in ROWS})==16
    base_path=ROOT/'data/kanto/rare_base_maps.json';base=load('data/kanto/rare_base_maps.json') if base_path.exists() else {}
    scripts=['@ Optional Kanto rare Pokemon. Capture flags use reserved Kanto bits only.'];records=[];definitions=[];flags=[]
    def text(label,s):
        lines=textwrap.wrap(s,33,break_long_words=False)
        value=lines[0]+''.join(('\\n' if i==1 else '\\l')+line for i,line in enumerate(lines[1:],1))+'$'
        scripts.extend([label+'::','\t.string "'+value.replace('"','\\"')+'"',''])
    for i,r in enumerate(ROWS):
        name=r['species'];path=ROOT/'data/maps'/r['map']/'map.json';m=json.loads(path.read_text())
        m['object_events']=[o for o in m['object_events'] if not o.get('script','').startswith('KantoRare_')]
        before=digest(m)
        if r['map'] in base:assert base[r['map']]==before,('Original map changed',r['map'])
        else:base[r['map']]=before
        spot=place(m,r['water']);prefix='KantoRare_'+name;flag='KANTO_FLAG_CAUGHT_RARE_'+name;numeric=0xa8f0+i
        flags.append('#define '+flag+' (KANTO_FLAG_BASE + '+hex(numeric-0xa000)+')')
        local='LOCALID_KANTO_RARE_'+name
        m['object_events'].append(dict(local_id=local,graphics_id='OBJ_EVENT_GFX_SPECIES('+name+')',x=spot['x'],y=spot['y'],elevation=spot['elevation'],
          movement_type='MOVEMENT_TYPE_FACE_DOWN',movement_range_x=0,movement_range_y=0,trainer_type='TRAINER_TYPE_NONE',trainer_sight_or_berry_tree_id='0',script=prefix+'_Interact',flag=hex(numeric)))
        path.write_text(json.dumps(m,indent=2)+'\n',encoding='utf-8')
        scripts.extend([prefix+'_Interact::','\tlock','\tfaceplayer','\tgoto_if_set '+flag+', '+prefix+'_Gone',
          '\tgoto_if_set FLAG_TEMP_10, '+prefix+'_Rest','\tmsgbox '+prefix+'_Intro, MSGBOX_DEFAULT',
          '\tmsgbox KantoRare_Text_Invite, MSGBOX_YESNO','\tgoto_if_eq VAR_RESULT, NO, '+prefix+'_Decline',
          '\tsetvar VAR_0x8004, '+str(16+i),'\tcallnative Script_CozyWorldPrepareRare',
          '\tgoto_if_eq VAR_RESULT, FALSE, KantoRare_NoHealthyTeam','\tmsgbox '+prefix+'_Accept, MSGBOX_DEFAULT',
          '\tsetwildbattle SPECIES_'+name+', '+str(r['level']),'\tcallnative Script_CozyWorldTrainRare','\tdowildbattle',
          '\tspecialvar VAR_RESULT, GetBattleOutcome','\tgoto_if_eq VAR_RESULT, B_OUTCOME_CAUGHT, '+prefix+'_Caught',
          '\tsetflag FLAG_TEMP_10','\tgoto '+prefix+'_Rest',prefix+'_Caught:',
          '\tsetflag '+flag,'\tremoveobject '+local,'\tmsgbox '+prefix+'_CaughtText, MSGBOX_DEFAULT','\trelease','\tend',
          prefix+'_Decline:','\tmsgbox '+prefix+'_DeclineText, MSGBOX_DEFAULT','\trelease','\tend',
          prefix+'_Rest:','\tmsgbox '+prefix+'_RestText, MSGBOX_DEFAULT','\trelease','\tend',
          prefix+'_Gone:','\trelease','\tend',''])
        for field,suffix in [('intro','Intro'),('accept','Accept'),('decline','DeclineText'),('rest','RestText'),('caught','CaughtText')]:text(prefix+'_'+suffix,r[field])
        definitions.append('    {SPECIES_'+name+', '+str(r['level'])+', {'+', '.join(map(str,r['evs']))+'}},')
        records.append({k:r[k] for k in ['species','map','level','evs','water']}|spot|dict(index=i,rare_index=16+i,flag=flag,flag_id=numeric,local_id=local,object_id=len(m['object_events']),script=prefix+'_Interact'))
    scripts.extend(['KantoRare_NoHealthyTeam:','\tmsgbox KantoRare_Text_NoHealthyTeam, MSGBOX_DEFAULT','\trelease','\tend',''])
    text('KantoRare_Text_Invite','Ask it to join you?')
    text('KantoRare_Text_NoHealthyTeam','Bring a Pokemon able to battle before offering a tryout.')
    (ROOT/'data/kanto/rare_encounters.inc').write_text('\n'.join(scripts)+'\n',encoding='utf-8')
    (ROOT/'data/kanto/rare_encounters.json').write_text(json.dumps(records,indent=2)+'\n')
    base_path.write_text(json.dumps(base,indent=2)+'\n')
    (ROOT/'src/data/kanto_rare_definitions.h').write_text('// Appended after the sixteen released Hoenn encounters.\n'+'\n'.join(definitions)+'\n')
    (ROOT/'include/constants/kanto_rare.h').write_text('#ifndef GUARD_KANTO_RARE_H\n#define GUARD_KANTO_RARE_H\n// Reserved unused Kanto flags, separate from story and living-scene rewards.\n'+'\n'.join(flags)+'\n#endif\n')
    print('Built 16 Kanto encounters; native terrain and all original events preserved.')
if __name__=='__main__':main()
