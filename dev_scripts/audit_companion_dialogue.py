"""Conservative source inventory, not a claim of executed-branch coverage."""
from pathlib import Path
import json,re
from build_companion_contexts import ROOT

def main():
    content=json.loads((ROOT/'data/companion_dialogue/contexts.json').read_text())
    covered={label for row in content['contexts'] for label in row['sources']}
    old=(ROOT/'src/data/pip_kanto_objects.h').read_text()
    covered.update(re.findall(r'\{(\w+), sPipKantoObject_\d+\}',old))
    covered.update(['Text_PictureBookShelf','Text_BookShelf','Text_PokemonCenterBookShelf',
                    'Text_Vase','Text_EmptyTrashCan','Text_ShopShelf','Text_Blueprint'])
    covered.update(f"LivingKanto_Scene{i}_After" for i in range(12))
    graph={};text_labels=set()
    paths=[p for p in (ROOT/'data/maps').rglob('scripts.inc') if not p.parent.name.endswith('_Frlg')]
    for folder in ['data/scripts','data/text','data/kanto','data/cast','data/bonds']:
        paths+=sorted((ROOT/folder).rglob('*.inc'))
    for p in paths:
        s=p.read_text(encoding='utf-8')
        matches=list(re.finditer(r'^(\w+)::?[^\n]*\n',s,re.M))
        for i,m in enumerate(matches):
            body=s[m.end():matches[i+1].start() if i+1<len(matches) else len(s)]
            if re.match(r'\s*\.string',body):
                text_labels.add(m[1]);graph[m[1]]=set()
            else:
                body=re.sub(r'"[^"\n]*"|@[^\n]*','',body)
                graph[m[1]]=set(re.findall(r'\b\w+\b',body))
    groups=json.loads((ROOT/'data/maps/map_groups.json').read_text());actors=[]
    def texts_for(root):
        todo=[root];visited=set();texts=set()
        while todo:
            name=todo.pop()
            if name in visited:continue
            visited.add(name)
            if name in text_labels:texts.add(name)
            else:todo.extend(n for n in graph.get(name,[]) if n in graph and n not in visited)
        return texts
    cache={}
    for gi,group in enumerate(groups['group_order']):
        # Vanilla FRLG groups 34..74 are not the imported Emerald campaign.
        if 34<=gi<75:continue
        for name in groups[group]:
            p=ROOT/'data/maps'/name/'map.json'
            if not p.exists():continue
            for obj in json.loads(p.read_text()).get('object_events',[]):
                root=obj.get('script')
                if root in [None,'NULL','0x0']:continue
                if root not in cache:cache[root]=texts_for(root)
                texts=cache[root];matched=texts&covered
                actors.append(dict(map=name,local_id=obj.get('local_id',obj.get('id')),script=root,
                                   reachable_texts=len(texts),bound_texts=sorted(matched),
                                   unbound_texts=sorted(texts-covered)))
    result=dict(method='Static direct label references including all branches. Does not resolve native printers, runtime pointers or prove execution/semantic quality.',
                authored_contexts=len(content['contexts']),new_replies=len(content['contexts'])*11,
                exact_known_text_labels=len(covered),scripted_actor_placements=len(actors),
                placements_with_at_least_one_bound_text=sum(bool(a['bound_texts']) for a in actors),
                placements_with_unbound_text=sum(bool(a['unbound_texts']) for a in actors),
                actors=actors)
    out=ROOT/'data/companion_dialogue/coverage.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='actors'},indent=2))

if __name__=='__main__':main()
