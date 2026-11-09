"""Candidate host storage; NOT connected to the ROM or any user's save.

Immutable, content-addressed snapshots are prepared before the cartridge anchor
is committed. Keeping every referenced snapshot permits either cartridge slot
to recover its own history. No adapter or emulator support is implied here.
"""
import hashlib
import os
from pathlib import Path
import struct
import tempfile

VOICES = 11
CONTEXTS = 12288
BANK_BYTES = CONTEXTS // 8
PAYLOAD_BYTES = VOICES * BANK_BYTES
HEADER = struct.Struct('<8sHHI16s')
MAGIC = b'ECHOMEM1'


def encode(identity, payload):
    if len(identity) != 16 or len(payload) != PAYLOAD_BYTES:
        raise ValueError('Invalid game identity or independent history size')
    return HEADER.pack(MAGIC, 1, VOICES, CONTEXTS, identity) + payload


def decode(blob, identity):
    if len(blob) != HEADER.size + PAYLOAD_BYTES:
        raise ValueError('Truncated or oversized snapshot')
    magic, version, voices, contexts, owner = HEADER.unpack_from(blob)
    if (magic, version, voices, contexts, owner) != (MAGIC, 1, VOICES, CONTEXTS, identity):
        raise ValueError('Unsupported snapshot or wrong game identity')
    return blob[HEADER.size:]


def prepare(directory, identity, payload):
    """Return a 32-byte candidate anchor only after durable host preparation.

    The caller must still commit the anchor through the game's save transaction.
    Failure leaves the previous anchor valid. Orphan snapshots are harmless.
    Directory-entry durability and adapter behavior require platform validation.
    """
    blob = encode(identity, payload)
    anchor = hashlib.sha256(blob).digest()
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    destination = directory / (anchor.hex() + '.history')
    if destination.exists():
        if destination.read_bytes() != blob:
            raise ValueError('Existing snapshot is corrupt')
        return anchor
    name = None
    try:
        with tempfile.NamedTemporaryFile(dir=directory, delete=False) as output:
            name = output.name
            output.write(blob)
            output.flush()
            os.fsync(output.fileno())
        os.replace(name, destination)
    finally:
        if name is not None and os.path.exists(name):
            os.unlink(name)
    return anchor


def load(directory, identity, anchor):
    if len(anchor) != 32:
        raise ValueError('Invalid anchor')
    blob = (Path(directory) / (anchor.hex() + '.history')).read_bytes()
    if hashlib.sha256(blob).digest() != anchor:
        raise ValueError('Snapshot checksum mismatch')
    return decode(blob, identity)


def verify():
    identity = bytes(range(16))
    before = bytes(PAYLOAD_BYTES)
    independent = bytearray(before)
    for voice in range(VOICES):
        # Different bits in every voice, including both ends of the catalogue.
        for context in (0, 47, 736, 9174, CONTEXTS - 1 - voice):
            independent[voice * BANK_BYTES + context // 8] |= 1 << (context % 8)
    with tempfile.TemporaryDirectory() as directory:
        old = prepare(directory, identity, before)
        new = prepare(directory, identity, independent)
        assert new != old
        assert load(directory, identity, old) == before
        assert load(directory, identity, new) == independent
        assert prepare(directory, identity, independent) == new
        # Simulated cartridge-write failure: old anchor still reads old history.
        assert load(directory, identity, old) == before
        # Worst-case dense history must not depend on compression success.
        full = bytes([255]) * PAYLOAD_BYTES
        assert load(directory, identity, prepare(directory, identity, full)) == full
        try:
            load(directory, bytes(16), new)
        except ValueError:
            pass
        else:
            raise AssertionError('Cross-game history was accepted')
        path = Path(directory) / (new.hex() + '.history')
        path.write_bytes(path.read_bytes()[:-1])
        try:
            load(directory, identity, new)
        except ValueError:
            pass
        else:
            raise AssertionError('Truncated history was accepted')
        path.unlink()
        try:
            load(directory, identity, new)
        except FileNotFoundError:
            pass
        else:
            raise AssertionError('Missing history was silently recreated')
    print('Snapshot model passed: independent banks, both anchors, dense history, corruption and missing-file rejection. No ROM integration tested.')


if __name__ == '__main__':
    verify()
