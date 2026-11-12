"""Prepare the one-file mGBA helper beside a development ROM.

Does not launch/control mGBA or open/change any .sav or history snapshot.
The generated helper finds its own folder through Lua's source filename, as
provided by mGBA's file loader. It remains portable when the game folder moves.
Python is used by development packaging, not while playing.
"""
import argparse
from pathlib import Path


def install(directory):
    directory = Path(directory).resolve()
    if not directory.is_dir():
        raise ValueError('Choose the existing folder containing your ROM')
    history = directory / 'companion-history'
    history.mkdir(exist_ok=True)
    source = Path(__file__).with_name('mgba_history.lua').read_text(encoding='utf-8')
    helper = directory / 'load-companion-history.lua'
    content = ('-- Generated Emerald companion history helper.\n'
               'local adapter = (function()\n' + source + '\nend)()\n'
               'assert(emu, "Open the matching Emerald ROM before loading this helper.")\n'
               'local filename = debug.getinfo(1, "S").source\n'
               'assert(filename:sub(1,1) == "@", "Load this helper from its Lua file.")\n'
               'filename = filename:sub(2):gsub("\\\\", "/")\n'
               'local directory = filename:match("^(.*)/") or "."\n'
               'adapter.attach(emu, callbacks, directory .. "/companion-history")\n'
               'console:log("Emerald companion history helper attached.")\n')
    helper.write_text(content, encoding='utf-8')
    return helper


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('rom_directory', type=Path)
    args = parser.parse_args()
    print(install(args.rom_directory))
