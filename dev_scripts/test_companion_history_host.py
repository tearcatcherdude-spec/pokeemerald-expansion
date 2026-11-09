"""Exercise actual Lua adapter with a mocked documented mGBA memory API.

Requires lupa; this is host-protocol validation, not an emulator/ROM smoke test.
"""
import hashlib
from pathlib import Path
import struct
import sys
import tempfile

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'history-test-deps'))
from lupa.lua54 import LuaRuntime
from companion_history_snapshots import encode, PAYLOAD_BYTES

ROOT = Path(__file__).resolve().parents[1]
BASE = 0x02000000
MAILBOX = BASE + 0x100
SNAPSHOT = BASE + 0x1000
FRAME = 0x030066DC # Actual game's frame counter resides in IWRAM.


def run():
    lua = LuaRuntime(encoding=None, unpack_returned_tuples=True)
    adapter = lua.execute((ROOT / 'tools/companion_history/mgba_history.lua').read_bytes())
    for value in (b'', b'abc', bytes(range(256)), b'a' * 16928):
        assert adapter[b'sha256'](value) == hashlib.sha256(value).digest()
    ram = bytearray(0x40000)
    rom = bytearray(65536)
    struct.pack_into('<8sIIIII', rom, 64, b'ECHOBRD1', 1, MAILBOX, SNAPSHOT, 16928, FRAME)
    writes = []

    def read(address, length):
        if address == FRAME and length == 4:
            return bytes(4)
        if 0x08000000 <= address < 0x08000000 + len(rom):
            return bytes(rom[address - 0x08000000:address - 0x08000000 + length])
        assert BASE <= address and address + length <= BASE + len(ram)
        return bytes(ram[address - BASE:address - BASE + length])

    def write(address, data):
        assert MAILBOX <= address < MAILBOX + 92 or SNAPSHOT <= address < SNAPSHOT + 16928
        ram[address - BASE:address - BASE + len(data)] = data
        writes.append((address, data))

    def word(offset, value):
        struct.pack_into('<I', ram, offset - BASE, value)

    emu = lua.table()
    emu[b'romSize'] = lambda _: len(rom)
    emu[b'readRange'] = lambda _, address, length: read(address, length)
    emu[b'read32'] = lambda _, address: int.from_bytes(read(address, 4), 'little')
    emu[b'write8'] = lambda _, address, value: write(address, bytes([value]))
    emu[b'write32'] = lambda _, address, value: write(address, struct.pack('<I', value))
    callbacks = lua.table()
    callbacks[b'add'] = lambda _, name, fn: 1
    word(MAILBOX, 0x314D4345)
    word(MAILBOX + 4, 1)
    word(MAILBOX + 20, SNAPSHOT)
    word(MAILBOX + 24, 16928)
    identity = bytes(range(16))

    def request(frame, kind, blob, digest=bytes(32)):
        ram[SNAPSHOT - BASE:SNAPSHOT - BASE + len(blob)] = blob
        ram[MAILBOX - BASE + 28:MAILBOX - BASE + 60] = digest
        word(MAILBOX + 12, kind)
        word(MAILBOX + 16, 0)
        writes.clear()
        frame()
        status = int.from_bytes(read(MAILBOX + 16, 4), 'little')
        assert writes[-1][0] == MAILBOX + 16, 'ACK must be last'
        return status

    with tempfile.TemporaryDirectory() as directory:
        frame = adapter[b'attach'](emu, callbacks, directory.encode())
        dense = encode(identity, bytes([255]) * PAYLOAD_BYTES)
        assert request(frame, 2, dense) == 1
        anchor = read(MAILBOX + 60, 32)
        assert anchor == hashlib.sha256(dense).digest()
        path = Path(directory) / (anchor.hex() + '.history')
        assert path.read_bytes() == dense
        zero = encode(identity, bytes(PAYLOAD_BYTES))
        assert request(frame, 2, zero) == 1
        old_anchor = read(MAILBOX + 60, 32)
        assert old_anchor != anchor
        assert request(frame, 1, zero, anchor) == 1
        assert read(SNAPSHOT, len(dense)) == dense
        assert request(frame, 1, dense, old_anchor) == 1
        assert read(SNAPSHOT, len(zero)) == zero
        # Missing/corrupt/cross-game history must never zero the live buffer.
        assert request(frame, 1, zero, bytes([7]) * 32) == 2
        assert read(SNAPSHOT, len(zero)) == zero
        path.write_bytes(dense[:-1])
        assert request(frame, 1, zero, anchor) == 2
        assert read(SNAPSHOT, len(zero)) == zero
        path.write_bytes(dense)
        other = encode(bytes(16), bytes(PAYLOAD_BYTES))
        assert request(frame, 1, other, anchor) == 2
        assert read(SNAPSHOT, len(other)) == other
        # An altered destination pointer is ignored, with no ACK or payload writes.
        word(MAILBOX + 20, BASE)
        writes.clear()
        frame()
        assert not writes
        word(MAILBOX + 20, SNAPSHOT)
        # A file creation failure is explicitly rejected before success ACK.
        failed = adapter[b'attach'](emu, callbacks, (directory + '/absent/subdir').encode())
        assert request(failed, 2, dense) == 2
    print('PASS: actual Lua SHA-256, prepare/load, both anchors, dense history, missing/corrupt/wrong-game rejection, pointer guard, IO failure, ACK ordering. Mock API only.')


if __name__ == '__main__':
    run()
