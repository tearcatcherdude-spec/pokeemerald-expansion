"""Verify the host bridge survived linking and points to the actual ABI symbols."""
from pathlib import Path
import re
import struct
import sys


def verify(rom_path, map_path):
    rom = Path(rom_path).read_bytes()
    text = Path(map_path).read_text(encoding='utf-8')
    symbols = {name: int(address, 16) for address, name in
               re.findall(r'^\s+(0x[0-9a-fA-F]+)\s+(\w+)\s*$', text, re.M)}
    marker = b'ECHOBRD1'
    offset = rom.find(marker)
    assert offset >= 0 and offset % 4 == 0, 'Missing/alignment-invalid ROM descriptor'
    assert rom.find(marker, offset + 1) < 0, 'Ambiguous ROM descriptor'
    version, mailbox, snapshot, length, frame = struct.unpack_from('<IIIII', rom, offset + 8)
    assert version == 1 and length == 16928
    assert mailbox == symbols['gCompanionHistoryMailbox']
    assert snapshot == symbols['gCompanionHistorySnapshot']
    assert 0x02000000 <= mailbox and mailbox + 92 <= 0x02040000
    assert 0x02000000 <= snapshot and snapshot + length <= 0x02040000
    assert frame == symbols['gMain'] + 0x20
    assert 0x03000000 <= frame < 0x03008000
    assert 0x08000000 + offset == symbols['gCompanionHistoryDescriptor']
    print('PASS: compiled ROM bridge descriptor, exact RAM symbols, snapshot ABI and IWRAM frame counter')


if __name__ == '__main__':
    verify(sys.argv[1], sys.argv[2])
