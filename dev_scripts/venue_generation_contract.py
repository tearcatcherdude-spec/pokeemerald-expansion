"""Refuse to regenerate maps over subsequent unrelated project work."""
from pathlib import Path
import hashlib,json
def fingerprint(path):
    if path.suffix=='.json':
        value=json.loads(path.read_text(encoding='utf-8'))
        if 'object_events' in value:
            value['object_events']=[o for o in value['object_events'] if not o.get('local_id','').startswith('LOCALID_ROAMING_TUTOR_')]
        data=json.dumps(value,sort_keys=True,separators=(',',':')).encode()
    else:data=path.read_bytes().replace(b'\r\n',b'\n')
    return hashlib.sha256(data).hexdigest()
def check(root):
    path=root/'data/venues/generated_map_hashes.json'
    if not path.exists():raise RuntimeError('Missing venue generation contract; review the source before authoring.')
    for rel,sha in json.loads(path.read_text()).items():
        if fingerprint(root/rel)!=sha:
            raise RuntimeError('Map changed since venue generation; refusing to overwrite: '+rel)
def record(root):
    paths=[root/'data/maps'/p.stem/'map.json' for p in (root/'data/venues/originals').glob('*.json')]
    for site in json.loads((root/'data/venues/sites.json').read_text()):
        if site.get('open_lot'):paths.extend([root/'data/maps'/site['house']/'map.json',root/'data/maps'/site['house']/'scripts.inc'])
    data={p.relative_to(root).as_posix():fingerprint(p) for p in paths}
    (root/'data/venues/generated_map_hashes.json').write_text(json.dumps(data,indent=2)+'\n')
