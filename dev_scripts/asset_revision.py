"""Validate a specifically authorized art revision without erasing old contracts."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
def digest(p):
    b=p.read_bytes()
    return hashlib.sha256(b.replace(b'\r\n',b'\n') if p.suffix in ('.pal','.json') else b).hexdigest()
def verify_expected(path,expected):
    current=ROOT/path
    if digest(current)==expected:return
    revision=json.loads((ROOT/'graphics/readability_v2/revision.json').read_text())
    assert revision['base_commit']=='240f43430e1078faef5174c6c93563f8aafa0a66'
    row=revision['files'][path];old=(ROOT/row['original']).resolve()
    assert (ROOT/'graphics/readability_v2/originals').resolve() in old.parents
    assert digest(old)==row['original_sha256']==expected,('Original art contract changed',path)
    assert digest(current)==row['revised_sha256'],('Unreviewed artwork changed',path)
