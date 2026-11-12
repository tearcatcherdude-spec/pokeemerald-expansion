"""Decode the published ROM's actual reply table and compare every original byte."""
from pathlib import Path
import hashlib,json,re,struct,sys
from packed_companion_text import ROOT,decompress,charset,VOICES,EXPRESSIONS
from build_cast import wrapped
def verify(rom_path,map_path):
    rom=Path(rom_path).read_bytes();mp=Path(map_path).read_text(encoding='utf-8',errors='replace')
    syms={n:int(a,16) for a,n in re.findall(r'0x([0-9a-fA-F]{8,16})\s+(\w+)\s*$',mp,re.M)}
    def at(n):return syms[n]-0x8000000
    meta=json.loads((ROOT/'data/companion_dialogue/packed/packed_text.json').read_text());source=(ROOT/'data/companion_dialogue/packed/packed_text.bin').read_bytes();blobat=at('gCompanionPackedText')
    assert rom[blobat:blobat+len(source)]==source
    offsets=struct.unpack_from('<'+'I'*meta['block_count'],rom,at('gCompanionPackedTextOffsets'))
    blocks=[decompress(rom[blobat+v:]) for v in offsets]
    magic,version,ptr,contexts,voices,size=struct.unpack_from('<6I',rom,at('gCompanionPackedCatalogue'))
    assert (magic,version,contexts,voices,size)==(0x50435458,1,meta['contexts'],11,8)
    encode=charset();catalogue=json.loads((ROOT/'data/companion_dialogue/contexts.json').read_text())['contexts'];decoded=bytearray();count=0
    for i,row in enumerate(catalogue):
        for j,voice in enumerate(VOICES):
            ref,expression=struct.unpack_from('<IB',rom,ptr-0x8000000+(i*11+j)*size)
            if row.get('retired'):assert ref==0xFFFFFFFF;continue
            reply=next(r for r in row['replies'] if r['voice']==voice);b,off=ref>>12,ref&4095
            raw=blocks[b][off:];raw=raw[:raw.index(255)+1]
            assert raw==encode(wrapped(reply['text'],voice)),('Compiled reply differs',i,voice)
            assert expression==EXPRESSIONS.index(reply['expression'])
            decoded.extend(raw);decoded.append(expression);count+=1
    assert hashlib.sha256(decoded).hexdigest()==meta['decoded_catalogue_sha256']
    print(f'PASS: all {count} actual-ROM packed replies, voice/context indices, expressions and retired slots match the original catalogue')
if __name__=='__main__':verify(*sys.argv[1:])
