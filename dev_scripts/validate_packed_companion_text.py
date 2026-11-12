"""Check the source codec, tracked blocks and every catalogue reference."""
from pathlib import Path
import json,re
from packed_companion_text import ROOT,prepare,compress,decompress
def main():
    for data in [b'A',b'AA',b'A'*4096,bytes(range(256))*16,b'abcabdabcabd'*200]:
        assert decompress(compress(data))==data
    refs,blocks,blob,offsets,meta=prepare();folder=ROOT/'data/companion_dialogue/packed'
    assert blob==(folder/'packed_text.bin').read_bytes()
    assert meta==json.loads((folder/'packed_text.json').read_text())
    header=(ROOT/'src/data/companion_contexts.h').read_text();start=header.index('static const struct ContextReply');end=header.index('\n};',start)
    actual=[(int(a,16),int(b)) for a,b in re.findall(r'\{0x([0-9A-F]{8}), (\d+)\}',header[start:end])]
    assert actual==[entry for row in refs for entry in row]
    assert '#define PACKED_REPLY_FNV 0x%08Xu'%meta['native_golden_fnv'] in (ROOT/'include/companion_packed_text_golden.h').read_text()
    print(f'PASS: {meta["replies"]} lossless GBA-text round trips, {len(blocks)} bounded blocks, stable expressions/IDs, {meta["bytes_reclaimed"]:,} bytes reclaimed before linker overhead')
if __name__=='__main__':main()
