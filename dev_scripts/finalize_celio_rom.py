"""Pad the opt-in Celio target to its required exact 64 MiB file size."""
from pathlib import Path
import sys

SIZE = 64 * 1024 * 1024

def finalize(path):
    path = Path(path)
    length = path.stat().st_size
    if length > SIZE:
        raise ValueError('Game exceeds the 64 MiB Celio target; refusing to truncate')
    with path.open('ab') as stream:
        stream.write(b'\xff' * (SIZE - length))
    print(f'Celio ROM: {SIZE:,} bytes; requires Celio rom128-compatible emulator')

if __name__ == '__main__':
    finalize(sys.argv[1])
