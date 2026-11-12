"""Stage a verified package, carry the latest normal save/history, archive old builds.

Default is a read-only plan. --apply commits the prepared delivery. No emulator
states are migrated, no save bytes are edited, and no archived build is deleted.
"""
from pathlib import Path
import argparse
import datetime as dt
import hashlib
import json
import os
import shutil
import struct
import subprocess
import urllib.request
import uuid
import zipfile

CURRENT = 'Emerald Current Build'
ARCHIVE = 'past emerald builds'
SIGNATURE = 0x08012025
OFFSETS = [0, 0, 3968, 7936, 11904, 0, 3968, 7936, 11904, 15872, 19840, 23808, 27776, 31744]

def digest(path):
    with Path(path).open('rb') as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()

def desktop_path():
    if os.name == 'nt':
        import winreg
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders') as key:
            return Path(os.path.expandvars(winreg.QueryValueEx(key, 'Desktop')[0])).resolve()
    return (Path.home() / 'Desktop').resolve()

def beneath(path, parent):
    path, parent = Path(path).resolve(), Path(parent).resolve()
    if path == parent or parent not in path.parents:
        raise ValueError(f'Unsafe target outside intended directory: {path}')
    return path

def layout_sizes(rom):
    raw = Path(rom).read_bytes()
    pattern = struct.pack('<6H', 0, 3968, 3968, 3968, 7936, 3968)
    matches, at = set(), 0
    while True:
        at = raw.find(pattern, at)
        if at < 0:
            break
        start = at - 4
        if start >= 0 and start + 56 <= len(raw):
            values = struct.unpack_from('<28H', raw, start)
            if list(values[::2]) == OFFSETS and all(0 < n <= 3968 and n % 4 == 0 for n in values[1::2]):
                matches.add(tuple(values[1::2]))
        at += 1
    if len(matches) != 1:
        raise ValueError(f'Cannot establish the save checksum layout for {rom}')
    return next(iter(matches))

def checksum(raw):
    value = sum(struct.unpack('<' + 'I' * (len(raw)//4), raw)) & 0xffffffff
    return ((value >> 16) + value) & 65535

def inspect_save(path, sizes):
    path = Path(path)
    before = path.stat()
    raw = path.read_bytes()
    if len(raw) not in (131072, 131088):
        raise ValueError('Expected a normal 128 KiB Emerald save, optionally with its RTC tail')
    slots = []
    for bank in range(2):
        sectors = {}
        for physical in range(bank*14, bank*14+14):
            sector = raw[physical*4096:(physical+1)*4096]
            sid, check, signature, counter = struct.unpack_from('<HHII', sector, 4084)
            if signature == SIGNATURE and sid < 14 and check == checksum(sector[:sizes[sid]]):
                sectors[sid] = (sector, counter)
        if set(sectors) == set(range(14)):
            sb2 = sectors[0][0]
            hours = struct.unpack_from('<H', sb2, 14)[0]
            play_seconds = hours*3600 + sb2[16]*60 + sb2[17]
            slots.append(dict(bank=bank, counter=sectors[13][1], play_seconds=play_seconds, sb2=sb2))
    if not slots:
        raise ValueError('Neither normal-save slot has all fourteen checksum-valid sectors')
    selected = slots[0]
    for slot in slots[1:]:
        if 0 < ((slot['counter']-selected['counter']) & 0xffffffff) < 0x80000000:
            selected = slot
    if path.stat().st_mtime_ns != before.st_mtime_ns:
        raise ValueError('Save changed while being inspected; close the game before updating')
    return dict(path=str(path.resolve()), sha256=hashlib.sha256(raw).hexdigest(),
                bytes=len(raw), mtime_ns=before.st_mtime_ns,
                play_seconds=selected['play_seconds'], counter=selected['counter'],
                sb2=selected['sb2'])

def recognized_builds(desktop):
    found = []
    for folder in desktop.iterdir():
        if not folder.is_dir() or folder.name == ARCHIVE:
            continue
        if folder.name != CURRENT and not folder.name.startswith('EmeraldCompanions-'):
            continue
        if not any((folder/n).is_file() for n in ('BUILD-INFO.json', 'verification.json', 'delivery.json')):
            continue
        if len(list(folder.glob('*.gba'))) == 1:
            found.append(beneath(folder, desktop))
    return sorted(found)

def history_required(save):
    sb2 = save['sb2']
    magic, version = struct.unpack_from('<II', sb2, 3884)
    if magic == 0x31484345 and version == 1:
        return sb2[3892:3908], sb2[3908:3940].hex()
    return None

def history_folder(save):
    source = Path(save['path']).parent
    # Current deliveries keep save and history adjacent. Older layouts may keep
    # the normal save under a saves/ child, with history beside the ROM.
    for folder in (source/'companion-history', source.parent/'companion-history'):
        if folder.is_dir():
            needed = history_required(save)
            if needed:
                identity, sha = needed
                snapshot = folder/(sha+'.history')
                if not snapshot.is_file() or digest(snapshot) != sha:
                    continue
                blob = snapshot.read_bytes()
                if len(blob) != 16928 or blob[:8] != b'ECHOMEM1' or blob[16:32] != identity:
                    continue
            return folder.resolve()
    if history_required(save):
        raise ValueError('The selected save requires a companion-history snapshot that is missing or corrupt. No build has been replaced.')
    return None

def candidate_saves(builds):
    candidates, rejected = [], []
    for folder in builds:
        rom = next(folder.glob('*.gba'))
        sizes = layout_sizes(rom)
        paths = [folder/(rom.stem+'.sav'), folder/'saves'/(rom.stem+'.sav')]
        for path in paths:
            if path.is_file():
                try:
                    candidates.append(inspect_save(path, sizes))
                except ValueError as error:
                    rejected.append(dict(path=str(path), reason=str(error)))
    return candidates, rejected

def public_save(save):
    return {key:value for key,value in save.items() if key != 'sb2'} if save else None

def running_emulator():
    if os.name != 'nt':
        return False
    result = subprocess.run(['tasklist', '/FO', 'CSV', '/NH'], capture_output=True, text=True, check=True)
    return any(line.lower().startswith(('"mgba', '"visualboyadvance', '"retroarch')) for line in result.stdout.splitlines())

def desktop_shortcut(desktop, current):
    if os.name != 'nt':
        return None
    link = beneath(desktop/'Play Emerald.lnk', desktop)
    target = current/'Play.cmd'
    q = lambda value: "'" + str(value).replace("'", "''") + "'"
    command = (
        '$shell=New-Object -ComObject WScript.Shell;'
        f'$link=$shell.CreateShortcut({q(link)});'
        f'if ($link.TargetPath -and $link.TargetPath -ne {q(target)}) '
        "{throw 'Existing Play Emerald shortcut points elsewhere; leaving it unchanged'};"
        f'$link.TargetPath={q(target)};$link.WorkingDirectory={q(current)};'
        f'$link.IconLocation={q(str(current/"emulator/mgba-celio.exe")+",0")};'
        "$link.WindowStyle=7;$link.Description='Play the current Emerald build';$link.Save()"
    )
    subprocess.run(['powershell','-NoProfile','-NonInteractive','-Command',command], check=True, capture_output=True, text=True)
    return str(link)

def extract_package(package, stage):
    with zipfile.ZipFile(package) as archive:
        for item in archive.infolist():
            if '\\' in item.filename or ':' in item.filename:
                raise ValueError('Unexpected archive path')
            beneath(stage/item.filename, stage)
            if (item.external_attr >> 16) & 0o170000 == 0o120000:
                raise ValueError('Package symlinks are not allowed')
        archive.extractall(stage)
    if len(list(stage.glob('*.gba'))) != 1:
        raise ValueError('Package must contain exactly one root game ROM')
    for file in ('Play.cmd', 'load-companion-history.lua', 'emulator/mgba-celio.exe'):
        if not (stage/file).is_file():
            raise ValueError(f'Incomplete play package: {file}')
    if list(stage.rglob('*.sav')):
        raise ValueError('Release package unexpectedly includes a save')
    report = json.loads((stage/'verification.json').read_text())
    rom = next(stage.glob('*.gba'))
    if digest(rom) != report['compiled_game']['sha256']:
        raise ValueError('Packaged ROM hash does not match its verification record')
    return rom, report

def deliver(args):
    desktop = Path(args.desktop).resolve() if args.desktop else desktop_path()
    if not desktop.is_dir():
        raise ValueError('Desktop directory does not exist')
    cache = Path(args.cache).resolve()
    cache.mkdir(parents=True, exist_ok=True)
    package = Path(args.package).resolve() if args.package else cache/'download.zip'
    if args.download_url:
        if not args.package_sha256:
            raise ValueError('Downloads require --package-sha256')
        partial = cache/('download-'+uuid.uuid4().hex+'.part')
        urllib.request.urlretrieve(args.download_url, partial)
        if digest(partial) != args.package_sha256.lower():
            raise ValueError('Downloaded package checksum differs')
        package = cache/(args.package_sha256.lower()+'.zip')
        partial.replace(package)
    if args.package_sha256 and digest(package) != args.package_sha256.lower():
        raise ValueError('Package checksum differs')
    builds = recognized_builds(desktop)
    archive = beneath(desktop/ARCHIVE, desktop)
    if archive.is_dir():
        builds_for_saves = builds + [beneath(p, archive) for p in archive.iterdir()
            if p.is_dir() and len(list(p.glob('*.gba'))) == 1]
    else:
        builds_for_saves = builds
    candidates, rejected = candidate_saves(builds_for_saves)
    selected = None
    if not args.skip_save:
        if args.save:
            matches = [s for s in candidates if Path(s['path']) == Path(args.save).resolve()]
            if len(matches) != 1:
                raise ValueError('Explicit save is not a validated normal save in a recognized build')
            selected = matches[0]
        elif candidates:
            if args.furthest:
                selected = max(candidates, key=lambda s:(s['play_seconds'],s['mtime_ns'],s['counter']))
            else:
                selected = max(candidates, key=lambda s:(s['mtime_ns'],s['play_seconds'],s['counter']))
        elif rejected:
            raise ValueError('Existing saves were found, but none passed checksum validation; refusing a fresh-game replacement')
    history = history_folder(selected) if selected else None
    plan = dict(current=str(beneath(desktop/CURRENT, desktop)), archive=str(archive),
                archive_builds=[str(p) for p in builds], package=str(package),
                save=public_save(selected), history=str(history) if history else None,
                selection='explicit' if args.save else 'most-played' if args.furthest else 'latest valid normal-save modification',
                skip_save=args.skip_save, rejected_saves=rejected)
    (cache/'latest-plan.json').write_text(json.dumps(plan, indent=2)+'\n')
    if not args.apply:
        return plan
    if running_emulator():
        raise ValueError('Close the emulator after saving before updating. Nothing was replaced.')
    current = beneath(desktop/CURRENT, desktop)
    if current.exists() and current not in builds:
        raise ValueError('Current-build path is occupied by an unrecognized folder; nothing was replaced')
    stage = cache/('staged-'+uuid.uuid4().hex)
    stage.mkdir()
    rom, verification = extract_package(package, stage)
    if (current in builds and not args.skip_save
            and digest(next(current.glob('*.gba'))) == digest(rom)
            and (not selected or Path(selected['path']).parent == current)):
        plan['status'] = 'already_current'
        plan['shortcut'] = desktop_shortcut(desktop, current)
        return plan
    if selected:
        source = Path(selected['path'])
        if digest(source) != selected['sha256'] or source.stat().st_mtime_ns != selected['mtime_ns']:
            raise ValueError('Selected save changed during preparation; nothing was replaced')
        shutil.copy2(source, stage/(rom.stem+'.sav'))
        if digest(stage/(rom.stem+'.sav')) != selected['sha256']:
            raise ValueError('Copied save verification failed')
    history_hashes = {}
    if history:
        for source in history.rglob('*'):
            if source.is_symlink() or source.is_junction():
                raise ValueError('History symlinks are not supported')
            if source.is_file():
                relative = source.relative_to(history)
                target = beneath(stage/'companion-history'/relative, stage)
                target.parent.mkdir(parents=True, exist_ok=True)
                before = digest(source)
                shutil.copy2(source, target)
                if digest(source) != before or digest(target) != before:
                    raise ValueError('History changed during preparation; nothing was replaced')
                history_hashes[str(relative)] = before
    plan.update(source_commit=verification['source_commit'], rom_sha256=digest(rom),
                history_files=history_hashes, installed_utc=dt.datetime.now(dt.timezone.utc).isoformat())
    (stage/'delivery.json').write_text(json.dumps(plan, indent=2)+'\n')
    (stage/'companion-history').mkdir(exist_ok=True)
    if running_emulator():
        raise ValueError('Emulator opened during preparation; nothing was replaced')
    if selected and digest(Path(selected['path'])) != selected['sha256']:
        raise ValueError('Save changed before activation; nothing was replaced')
    archive.mkdir(exist_ok=True)
    moved = []
    try:
        stamp = dt.datetime.now().strftime('%Y-%m-%d_%H%M%S')
        for old in builds:
            old = beneath(old, desktop)
            dest = beneath(archive/(stamp+'_'+old.name), archive)
            if dest.exists():
                dest = beneath(archive/(stamp+'_'+uuid.uuid4().hex[:8]+'_'+old.name), archive)
            old.rename(dest)
            moved.append((old, dest))
        current = beneath(desktop/CURRENT, desktop)
        if current.exists():
            raise ValueError('Current-build path is occupied by an unrecognized folder')
        stage.rename(current)
    except Exception:
        for old,dest in reversed(moved):
            if dest.exists() and not old.exists():
                beneath(dest, archive).rename(beneath(old, desktop))
        raise
    # Archive paths are recorded separately so backups remain easy to locate.
    plan['archived_to'] = [str(dest) for _,dest in moved]
    if selected:
        plan['archived_save'] = selected['path']
        for old,dest in moved:
            if old in Path(selected['path']).parents:
                plan['archived_save'] = str(dest/Path(selected['path']).relative_to(old))
                break
        if digest(Path(plan['archived_save'])) != selected['sha256']:
            raise ValueError('Archived original differs from its verified snapshot')
    plan['status'] = 'installed'
    plan['shortcut'] = desktop_shortcut(desktop, current)
    (current/'delivery.json').write_text(json.dumps(plan, indent=2)+'\n')
    (cache/'latest-delivery.json').write_text(json.dumps(plan, indent=2)+'\n')
    return plan

def parser():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--package')
    p.add_argument('--download-url')
    p.add_argument('--package-sha256')
    p.add_argument('--desktop')
    p.add_argument('--cache', default=str(Path(__file__).resolve().parents[3]/'.delivery-cache'))
    p.add_argument('--save', help='Explicit previously validated save selection')
    p.add_argument('--furthest', action='store_true', help='Prefer longest play time, not proof of story progress')
    p.add_argument('--skip-save', action='store_true', help='Explicitly omit both save and history transfer')
    p.add_argument('--apply', action='store_true')
    return p

if __name__ == '__main__':
    args = parser().parse_args()
    if not args.package and not args.download_url:
        raise SystemExit('Supply --package or --download-url')
    print(json.dumps(deliver(args), indent=2))
