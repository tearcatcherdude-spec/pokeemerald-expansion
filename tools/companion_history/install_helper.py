"""Prepare the one-file mGBA helper beside a development ROM.

Does not launch/control mGBA or open/change any .sav or history snapshot.
Run again after moving the folder, because the generated helper has an absolute
history path. Python is needed for setup only, not while playing.
"""
import argparse
import json
from pathlib import Path


def install(directory):
    directory = Path(directory).resolve()
    if not directory.is_dir():
        raise ValueError('Choose the existing folder containing your ROM')
    history = directory / 'companion-history'
    history.mkdir(exist_ok=True)
    source = Path(__file__).with_name('mgba_history.lua').read_text(encoding='utf-8')
    helper = directory / 'load-companion-history.lua'
    # Lua accepts these JSON-style escapes for Windows paths and ordinary Unicode.
    quoted = json.dumps(history.as_posix(), ensure_ascii=False)
    content = ('-- Generated Emerald companion history helper.\n'
               'local adapter = (function()\n' + source + '\nend)()\n'
               'adapter.attach(emu, callbacks, ' + quoted + ')\n'
               'console:log("Emerald companion history helper attached.")\n')
    helper.write_text(content, encoding='utf-8')
    return helper


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('rom_directory', type=Path)
    args = parser.parse_args()
    print(install(args.rom_directory))
