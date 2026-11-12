"""Package clean CI files and the verified emulator, never a player's folder."""
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import tempfile
import zipfile

EMULATOR_SHA256 = '12e5a1c5c803e4750f454fd20d1d715de755510c070f906eb665fc7ca127b7dd'
PLAY = '''@echo off
cd /d "%~dp0"
start "" "%~dp0emulator\\mgba-celio.exe" --script "%~dp0load-companion-history.lua" "%~dp0pokeemerald.gba"
'''
README = '''Expanded Emerald — Celio edition

Double-click Play.cmd, or use the desktop Play Emerald shortcut.
Desktop delivery copies the latest valid normal save and matching companion
history unless you ask to start fresh. Old build folders remain intact under
"past emerald builds". Save and close the emulator before an update.

Keep companion-history and emulator with the game. Normal saves are preserved
byte-for-byte, including RTC data. Do not load older builds' emulator save states.
See verification.json for the tested build and remaining gameplay checks.
The target is 64 MiB; 128 MiB resource banking is not implemented.
Upstream emulator licenses and source patch are retained under emulator/.
'''

def package_build(artifact, emulator, verification, output):
    emulator = Path(emulator)
    if hashlib.sha256(emulator.read_bytes()).hexdigest() != EMULATOR_SHA256:
        raise ValueError('Emulator archive does not match the verified publisher release')
    record = json.loads(Path(verification).read_text())
    with zipfile.ZipFile(artifact) as source:
        rom = source.read('pokeemerald.gba')
    if len(rom) != 64*1024*1024 or hashlib.sha256(rom).hexdigest() != record['compiled_game']['sha256']:
        raise ValueError('CI artifact differs from the tested ROM')
    helper_path = Path(__file__).resolve().parents[1]/'companion_history/install_helper.py'
    spec = importlib.util.spec_from_file_location('history_installer', helper_path)
    helper = importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
    output = Path(output).resolve();output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as temp:
        generated = helper.install(temp).read_bytes()
    with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as dest:
        with zipfile.ZipFile(emulator) as source:
            for item in source.infolist():
                parts = Path(item.filename).parts
                if item.is_dir() or len(parts) < 2:
                    continue
                relative = Path(*parts[1:])
                if relative.is_absolute() or '..' in relative.parts or ':' in str(relative):
                    raise ValueError('Unsafe emulator archive path')
                dest.writestr('emulator/'+relative.as_posix(), source.read(item))
        dest.writestr('pokeemerald.gba',rom)
        dest.writestr('load-companion-history.lua',generated)
        dest.writestr('Play.cmd',PLAY)
        dest.writestr('Readme.txt',README)
        dest.writestr('verification.json',json.dumps(record,indent=2)+'\n')
        dest.writestr('companion-history/Keep-this-folder.txt','Companion history snapshots are stored here.\n')
    with zipfile.ZipFile(output) as check:
        assert 'emulator/mgba-celio.exe' in check.namelist()
        assert not any(n.lower().endswith(('.sav','.history')) for n in check.namelist())
        assert hashlib.sha256(check.read('pokeemerald.gba')).hexdigest() == record['compiled_game']['sha256']
    return dict(package=str(output),sha256=hashlib.sha256(output.read_bytes()).hexdigest())

if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    for option in ('artifact','emulator','verification','output'):
        p.add_argument('--'+option,required=True)
    a=p.parse_args()
    print(json.dumps(package_build(a.artifact,a.emulator,a.verification,a.output),indent=2))
