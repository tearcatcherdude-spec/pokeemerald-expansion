"""Guard accepted artwork, persistent dialogue IDs and the silent-watch story rule."""
from pathlib import Path
import hashlib,json,re,struct

ROOT=Path(__file__).resolve().parents[1]

def require(ok,message):
    if not ok:raise SystemExit('BASELINE FAILURE: '+message)

def main():
    state=json.loads((ROOT/'data/project_baseline.json').read_text(encoding='utf-8'))
    for path,expected in state['pip_sprite']['files'].items():
        data=(ROOT/path).read_bytes()
        if path.endswith('.pal'):data=data.replace(b'\r\n',b'\n')
        actual=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
        require(actual==expected,f'{path} differs from accepted Morph/Pip artwork in PR #6')
    if 'persistent_map_groups' in state:
        groups=json.loads((ROOT/'data/maps/map_groups.json').read_text(encoding='utf-8'))
        for index,old in enumerate(state['persistent_map_groups']):
            require(index < len(groups['group_order']) and groups['group_order'][index]==old['name'],
                    'Do not reorder saved map groups; append new groups')
            current=groups[old['name']]
            require(current[:len(old['maps'])]==old['maps'],
                    old['name']+': do not reorder saved map numbers; append new maps')
    pointers=(ROOT/'src/data/object_events/object_event_graphics_info_pointers.h').read_text(encoding='utf-8')
    require(re.search(r'\[OBJ_EVENT_GFX_PIP\]\s*=\s*&gObjectEventGraphicsInfo_Pip',pointers),'Pip graphics ID must retain his own graphics info')
    info=(ROOT/'src/data/object_events/object_event_graphics_info.h').read_text(encoding='utf-8').split('gObjectEventGraphicsInfo_Pip =',1)[1].split('};',1)[0]
    require('sPicTable_Pip' in info and 'OBJ_EVENT_PAL_TAG_PIP' in info,'Pip must retain his own frame table and palette tag')
    png=(ROOT/'graphics/object_events/pics/people/pip.png').read_bytes()
    require(png[:8]==b'\x89PNG\r\n\x1a\n','Pip PNG signature')
    require(struct.unpack('>IIBB',png[16:26])==(144,32,4,3),'Pip must retain nine indexed 16x32 frames')
    for path,expected in state['starter_files_sha256'].items():
        data=(ROOT/path).read_bytes().replace(b'\r\n',b'\n')
        require(hashlib.sha256(data).hexdigest()==expected,f'{path}: preserve accepted starter-selection implementation')
    catalogue=(ROOT/'src/data/pip_memory_catalogue.h').read_text(encoding='utf-8')
    body=catalogue.split('sPipMemoryCatalogue[] = {',1)[1].split('};',1)[0]
    slots=re.findall(r'^\s*(\w+),',body,re.M)
    require(slots[:len(state['pip_memory_slots'])]==state['pip_memory_slots'],'Do not reorder or reuse accepted dialogue IDs; append new entries')
    require(len(slots)<=512,'Pip memory capacity exceeded')
    require(all(x=='NULL' for x in slots[248:254]),'Former watch-exposition IDs must stay retired')
    source=(ROOT/'data/scripts/parallel_watch.inc').read_text(encoding='utf-8')
    current='';checked=0
    banned=re.compile(r'\b(?:watch|worlds?|universe|dimension|teleport|storage network|home region|usual boxes)\b',re.I)
    for line in source.splitlines():
        label=re.match(r'^(\w+):',line)
        if label:current=label[1]
        if '.string ' not in line:continue
        if current.startswith('ParallelWatch_Watch') or current in {'ParallelWatch_Text_Heal','ParallelWatch_Text_Healed'}:
            text=line.split('.string ',1)[1]
            require(not banned.search(text),f'{current}: NPCs must not explain or acknowledge the watch')
            checked+=1
    require(checked>=10,'NPC mystery checks unexpectedly lost their coverage')
    dialogue=(ROOT/'src/data/pip_living_dialogue.h').read_text(encoding='utf-8')
    lines=re.findall(r'^static const u8 sPipKanto_.*$',dialogue,re.M)
    require(len(lines)==6,'Six neutral Kanto Pip lines must remain registered')
    for line in lines:require(not banned.search(line.split('= ',1)[1]),'Pip must not explain the watch or world switching')
    print(f'PASS: exact Morph sprite/palette, accepted starters, {len(slots)} stable memory slots, {checked} silent-mystery NPC texts')

if __name__=='__main__':main()
