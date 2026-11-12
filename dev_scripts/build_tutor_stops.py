"""Place optional travelling tutor stops without cutting native walkable routes."""
from variety_map_tools import ROOT,grid,neighbors,component
import json,copy
def main():
    stops=[]
    for name,anchor in [('OldaleTown',(9,8)),('Route110',(16,30)),('Route120',(10,8)),('KantoRoute2',(9,12)),('KantoRoute8',(12,10)),('KantoRoute15',(15,10))]:
        p=ROOT/f'data/maps/{name}/map.json';m=json.loads(p.read_text());m['object_events']=[o for o in m['object_events'] if o.get('local_id')!='LOCALID_ROAMING_TUTOR']
        _,l,floor=grid(name);blocked={(o['x'],o['y']) for o in m['object_events']}
        occupied=blocked|{(o['x'],o['y']) for k in ['warp_events','coord_events','bg_events'] for o in m[k]}
        candidates=sorted(floor,key=lambda p:abs(p[0]-anchor[0])+abs(p[1]-anchor[1]))
        for at in candidates:
            if at in occupied:continue
            ns=[n for n in neighbors(at) if n in floor and n not in blocked]
            if len(ns)<2:continue
            reach=component(floor,ns[0],blocked|{at})
            if len(reach)<30 or not all(n in reach for n in ns):continue
            if any(abs(at[0]-p[0])+abs(at[1]-p[1])<2 for p in occupied):continue
            break
        else:raise AssertionError(('No safe tutor position',name))
        actor=dict(local_id='LOCALID_ROAMING_TUTOR',type='object',graphics_id='OBJ_EVENT_GFX_VARIETY_COSMO',x=at[0],y=at[1],elevation=floor[at],movement_type='MOVEMENT_TYPE_FACE_DOWN',movement_range_x=0,movement_range_y=0,trainer_type='TRAINER_TYPE_NONE',trainer_sight_or_berry_tree_id='0',script='RoamingTutor_EventScript_Meet',flag='0')
        m['object_events'].append(actor);p.write_text(json.dumps(m,indent=2)+'\n');stops.append(dict(map=name,actor=actor))
    (ROOT/'data/venues/tutor_stops.json').write_text(json.dumps(stops,indent=2)+'\n')
    print('Placed six safe travelling tutor stops')
if __name__=='__main__':main()
