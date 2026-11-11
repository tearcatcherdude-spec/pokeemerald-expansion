"""Guard exact-context routing, source drift, voice coverage and save continuity."""
from pathlib import Path
import hashlib, json, re
from build_companion_contexts import text_blocks, VOICES
from companion_context_content import ROWS

ROOT=Path(__file__).resolve().parents[1]

def main():
    data=json.loads((ROOT/'data/companion_dialogue/contexts.json').read_text())
    contexts=data['contexts']; sources=text_blocks(); seen=set(); wording={v:set() for v in VOICES}
    assert data['voices']==VOICES and data['capacity']==12288 and data['legacy_capacity']==736
    assert len(contexts)==len(ROWS)<=12288
    pilot_path=ROOT/'data/companion_dialogue/full_game/released_pilot_contract.json'
    if pilot_path.exists():
        pilot=json.loads(pilot_path.read_text())
        assert data['voices']==pilot['voices']
        for current,old in zip(contexts,pilot['contexts']):
            assert (current['id'],current['key'],current['sources'])==(old['id'],old['key'],old['sources'])
            assert hashlib.sha256(json.dumps(current['replies'],sort_keys=True).encode()).hexdigest()==old['replies_sha256'], 'Released pilot wording or expressions changed'
        assert len(contexts)>=len(pilot['contexts'])
    for i,(row,authored) in enumerate(zip(contexts,ROWS)):
        assert (row['id'],row['key'])==(i,authored['key'])
        assert set(row['sources'])==set(authored['labels'])
        if row.get('retired'):
            assert i>=47 and authored.get('retired')==row['retired'] and not row['sources']
            assert set(row['retired_sources'])==set(authored['retired_sources'])
        for label,original in row['sources'].items():
            assert label not in seen, ('Duplicate binding',label)
            seen.add(label)
            assert original==sources[label], ('NPC text changed; review the reply',label)
        assert [r['voice'] for r in row['replies']]==VOICES
        for r in row['replies']:
            assert r['expression'] in ['neutral','soft_smile','annoyed','flustered','sad','surprised','smug','laughing']
            assert len(r['text'])>=30 and len(r['text'])<320
            assert r['text'] not in wording[r['voice']], ('Repeated authored reply',r)
            wording[r['voice']].add(r['text'])
            assert not re.search(r'\b(?:the watch|strange watch|world switching|shared (?:PC|party))\b',r['text'],re.I)
    pip=(ROOT/'src/pip.c').read_text()
    legacy_labels=set(re.findall(r'\{(Text_\w+),\s*sPipKantoObject_', (ROOT/'src/data/pip_kanto_objects.h').read_text()))
    legacy_labels.update(re.findall(r'original == (Text_\w+)',pip))
    binding_ids={label:row['id'] for row in contexts for label in row['sources']}
    for label in legacy_labels:
        assert label in binding_ids and binding_ids[label]<736, ('Legacy object needs one-time migration within existing banks',label)
    npc=pip.split('void Script_PipBeginNPCReaction')[1].split('const u8 *Pip_GetExactObjectReaction')[0]
    objects=pip.split('void Script_PipBeginObjectReaction')[1].split('void Script_PipChooseObjectDialogue')[0]
    assert 'FreshLocation' not in npc+objects and 'sReactionGraphics' not in pip
    cast=(ROOT/'src/cast.c').read_text().split('bool32 Cast_TrySay')[1].split('void Cast_ClearPending')[0]
    assert 'loreStage' not in cast and 'sCastLoreTriggers' not in cast
    engine=(ROOT/'src/companion_dialogue.c').read_text()
    assert 'sMessage = message;' in engine and 'ScriptContext_IsGlobal(ctx)' in engine
    assert 'sContextMessages[i].message == message' in engine
    assert 'StringCompare' not in engine and 'graphicsId' not in engine
    assert 'Pip_TryOfferExact(sLegacy)' in engine
    assert 'ScriptContext_SetupScript(CompanionDialogue_EventScript_React)' in engine
    assert 'CompanionDialogue_AfterScript();' in (ROOT/'src/script.c').read_text()
    assert 'Pip_GetExactObjectReaction(sMessage)' in engine
    storage=(ROOT/'include/pokemon_storage_system.h').read_text()
    assert storage.index('struct BondProgress bonds;')<storage.index('struct CompanionDialogueProgress companionDialogue;')
    for f in ['data/scripts/cozy_companion.inc','data/cast/recruitment.inc']:
        assert 'goto_if_eq VAR_RESULT, 5, CompanionDialogue_EventScript_Settings' in (ROOT/f).read_text()
    assert 'CompanionDialogue_EventScript_Settings' in (ROOT/'dev_scripts/build_cast.py').read_text()
    active=sum(not r.get('retired') for r in contexts)
    print(f'PASS: {active} active contexts ({len(contexts)} reserved IDs), {len(seen)} exact branch bindings, {active*11} distinct replies; no sprite/place/lore substitution; three saved modes; append-only storage.')

if __name__=='__main__':main()
