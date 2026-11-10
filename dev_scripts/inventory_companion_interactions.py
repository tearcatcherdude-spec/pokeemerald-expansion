"""Full Hoenn/Kanto interaction inventory and explicit capacity accounting.

This is a writing/hook worklist, not a coverage claim. A reachable text label is
not necessarily a final message; native printers and variable text need review.
Byte-identical source lines are candidates for aliases, never approved aliases.
"""
from pathlib import Path
from collections import defaultdict, Counter
import hashlib, json, re
from build_companion_contexts import ROOT, text_blocks, global_c_text_blocks

OUT=ROOT/'data/companion_dialogue/full_game'

def read_sources():
    paths=[p for p in sorted((ROOT/'data/maps').rglob('scripts.inc')) if not p.parent.name.endswith('_Frlg')]
    for folder in ['data/scripts','data/text','data/kanto','data/cast','data/bonds']:
        paths+=sorted((ROOT/folder).rglob('*.inc'))
    paths += [ROOT/'data/event_scripts.s']
    blocks={}
    for path in paths:
        source=path.read_text(encoding='utf-8')
        labels=list(re.finditer(r'^(\w+)::?[^\n]*\n',source,re.M))
        for i,label in enumerate(labels):
            body=source[label.end():labels[i+1].start() if i+1<len(labels) else len(source)]
            clean=re.sub(r'"[^"\n]*"|@[^\n]*','',body)
            blocks[label[1]]=dict(path=path.relative_to(ROOT).as_posix(),body=body,
                is_text=bool(re.match(r'\s*\.string',body)),
                refs=set(re.findall(r'\b\w+\b',clean)),
                native_calls=sorted(set(re.findall(r'\b(?:callnative|gotonative|special|specialvar)\s+(?:\w+,\s*)?(\w+)',clean))))
    for label,value in global_c_text_blocks().items():
        blocks[label]=dict(path=value['path'],body='',is_text=True,refs=set(),native_calls=[])
    return blocks

def collect_roots(blocks):
    groups=json.loads((ROOT/'data/maps/map_groups.json').read_text())
    roots=defaultdict(list); maps=0
    for gi,group in enumerate(groups['group_order']):
        if 34<=gi<75:continue # unused vanilla FRLG copies, not the imported campaign
        for mi,name in enumerate(groups[group]):
            path=ROOT/'data/maps'/name/'map.json'
            if not path.exists():continue
            maps+=1;data=json.loads(path.read_text())
            region='Kanto' if data.get('parallel_watch') or data.get('kanto_campaign') else 'Hoenn'
            for i,obj in enumerate(data.get('object_events',[])):
                script=obj.get('script')
                if script in [None,'NULL','0x0']:continue
                roots[script].append(dict(kind='actor',region=region,map=name,group=gi,map_num=mi,
                    local_id=obj.get('local_id',i+1),x=obj['x'],y=obj['y']))
            for i,obj in enumerate(data.get('coord_events',[])):
                script=obj.get('script')
                if script in [None,'NULL','0x0']:continue
                roots[script].append(dict(kind='coordinate_story',region=region,map=name,group=gi,map_num=mi,
                    event_index=i,x=obj['x'],y=obj['y'],var=obj.get('var'),value=obj.get('var_value')))
            lifecycle=name+'_MapScripts'
            if lifecycle in blocks:
                roots[lifecycle].append(dict(kind='map_lifecycle',region=region,map=name,group=gi,map_num=mi))
            for i,obj in enumerate(data.get('bg_events',[])):
                script=obj.get('script')
                if script in ['NULL','0x0']:continue
                if script is None:
                    if obj.get('type')=='hidden_item':script='EventScript_HiddenItemScript'
                    else:continue
                roots[script].append(dict(kind='background',region=region,map=name,group=gi,map_num=mi,
                    event_index=i,x=obj['x'],y=obj['y'],event_type=obj.get('type')))
    avatar=(ROOT/'src/field_control_avatar.c').read_text()
    dispatch=avatar.split('static const u8 *GetInteractedMetatileScript(',2)[-1].split('static const u8 *GetInteractedWaterScript',1)[0]
    for script in sorted(set(re.findall(r'\breturn\s+(\w+);',dispatch))):
        if script not in ['NULL','FALSE','TRUE']:
            roots[script].append(dict(kind='shared_metatile_dispatch',region='Both',map=None))
    return maps,roots

def write(name,data):
    (OUT/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

def native_text_edges():
    # Reviewed static-pointer path: ShowPokedexRatingMessage ->
    # GetPokedexRatingText -> sBirchDexRatingTexts. This does not infer text
    # from arbitrary C identifiers or claim the National-Dex branch displays it.
    source=(ROOT/'src/birch_pc.c').read_text(encoding='utf-8')
    array=re.search(r'sBirchDexRatingTexts\[BIRCH_DEX_STRINGS\]\s*=\s*\{(.*?)\};',source,re.S)
    assert array is not None, 'Review changed Birch native rating table'
    labels=re.findall(r'\bgBirchDexRatingText_\w+\b',array[1])
    assert len(labels)==len(set(labels))==21
    return {'ShowPokedexRatingMessage': labels}

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    blocks=read_sources(); sources=text_blocks(); maps,roots=collect_roots(blocks)
    # Assembly-selected variants are text addresses, not executable scripts.
    for label in sources:
        if label in blocks:blocks[label]['is_text']=True
    native_edges=native_text_edges()
    catalogue=json.loads((ROOT/'data/companion_dialogue/contexts.json').read_text())
    approved={label:row['id'] for row in catalogue['contexts'] for label in row['sources']}
    pilot={label:row['id'] for row in catalogue['contexts'][:47] for label in row['sources']}
    users=defaultdict(list); native_users=defaultdict(set); root_rows=[]
    for root,placements in sorted(roots.items()):
        todo=[root];visited=set();texts=set();native=set()
        while todo:
            label=todo.pop()
            if label in visited:continue
            visited.add(label);block=blocks.get(label)
            if block is None:continue
            if block['is_text']:texts.add(label)
            else:
                native.update(block['native_calls'])
                todo.extend(n for n in block['refs'] if n in blocks and n not in visited)
                for function in block['native_calls']:
                    todo.extend(n for n in native_edges.get(function,[]) if n in blocks and n not in visited)
        for text in texts:users[text].append(root)
        for name in native:native_users[name].add(root)
        root_rows.append(dict(script=root,placements=placements,text_labels=sorted(texts),
                              native_calls=sorted(native),script_found=root in blocks,
                              review_status='unreviewed',terminal_messages_reviewed=False))
    source_rows=[]; identical=defaultdict(list)
    for label in sorted(users):
        original=sources.get(label)
        if original is None:
            source_rows.append(dict(label=label,roots=users[label],status='source_parser_gap'))
            continue
        identical[original['text']].append(label)
        source_rows.append(dict(label=label,**original,roots=users[label],
            status='pilot_binding' if label in pilot else 'authored_binding' if label in approved else 'needs_semantic_review',
            authored_context=approved.get(label),proposed_context=None,
            final_message_eligibility='unreviewed',native_printer_eligibility='unreviewed'))
    write('interaction_roots.json',root_rows)
    write('message_worklist.json',source_rows)
    write('identical_source_candidates.json',[dict(labels=labels,text=text,approved_alias=False)
         for text,labels in sorted(identical.items(),key=lambda p:(-len(p[1]),p[0])) if len(labels)>1])
    write('native_hook_worklist.json',[dict(function=name,roots=sorted(rs),review_status='unreviewed',
                                         static_text_labels=native_edges.get(name,[]))
         for name,rs in sorted(native_users.items())])
    counts=Counter(p['kind'] for row in root_rows for p in row['placements'])
    summary=dict(method='Static explicit label references, all branches. No automatic semantic grouping or terminal-message claim.',
        maps=maps,**dict(counts),unique_interaction_roots=len(root_rows),reachable_text_labels=len(users),
        source_texts_found=sum('text' in r for r in source_rows),
        distinct_raw_source_texts=len(identical),pilot_bound_labels=sum(label in pilot for label in users),
        authored_bound_labels=sum(label in approved for label in users),
        native_functions_requiring_review=len(native_users),
        missing_script_roots=sum(not r['script_found'] for r in root_rows))
    write('inventory_summary.json',summary)
    # Accounting uses the compiled ARM ABI that the released source tests guard.
    slots=dict(save_block_1=dict(used=15568,capacity=4*3968),save_block_2=dict(used=3884,capacity=3968),
               save_block_3=dict(used=1608,capacity=14*116),pokemon_storage=dict(used=35580,capacity=9*3968))
    for value in slots.values():value['unused']=value['capacity']-value['used']
    n=len(users); raw_bytes=11*((n+7)//8);free=sum(s['unused'] for s in slots.values())
    capacity=dict(released_commit='79ec91c79bd03c426c64f824415befdfe99d351d',slots=slots,
        unused_bytes_per_save_slot=free,released_pilot_memory_bytes=1012,
        raw_independent_history_for_reachable_labels_bytes=raw_bytes,
        additional_raw_bytes_needed=max(0,raw_bytes-1012),
        caveat='Reachable labels are an upper-bound worklist, not approved distinct response contexts. Exact semantic aliases and final-message review are still required. Compression cannot guarantee fitting arbitrary independent histories into a smaller fixed bit budget.',
        safe_unchanged_layout_policy='No PC/fusion shrinking, legacy progress clearing, Hall of Fame/special-sector reuse, or removal of the backup save slot.',
        maximum_dense_contexts_per_voice_using_all_unused_space_and_8_byte_extension_header=736+((free-8)//11)*8)
    write('capacity_accounting.json',capacity)
    print(json.dumps(summary,indent=2));print(json.dumps(capacity,indent=2))

if __name__=='__main__':main()
