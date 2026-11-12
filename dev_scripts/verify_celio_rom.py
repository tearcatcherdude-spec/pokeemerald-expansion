"""Measure linked game data separately from the padded Celio cartridge size."""
from pathlib import Path
import hashlib
import json
import re
import sys

def verify(rom_path, map_path):
    rom = Path(rom_path).read_bytes()
    symbols = Path(map_path).read_text(errors='replace')
    end = re.search(r'0x([0-9a-fA-F]+)\s+__rom_end\s*=', symbols)
    assert end, 'Missing linker end marker'
    used = int(end[1], 16) - 0x08000000
    assert len(rom) == 64 * 1024 * 1024, 'Celio requires exactly 64 MiB'
    assert 0 < used <= len(rom)
    assert rom[0xB2] == 0x96
    assert rom[0xBD] == (-sum(rom[0xA0:0xBD]) - 0x19) & 255
    if used > 32 * 1024 * 1024:
        assert len(set(rom[32 * 1024 * 1024:used])) > 1, 'Expanded area contains only padding'
    report = dict(rom_bytes=len(rom), linked_bytes=used,
                  free_bytes=len(rom)-used,
                  linked_beyond_standard_limit=used > 32 * 1024 * 1024,
                  sha256=hashlib.sha256(rom).hexdigest())
    print(json.dumps(report, indent=2))
    return report

if __name__ == '__main__':
    verify(*sys.argv[1:])
