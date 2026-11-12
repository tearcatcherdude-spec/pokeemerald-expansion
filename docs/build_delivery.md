# Desktop build delivery

The user's standing preference is automatic delivery after each new playable
Emerald build: put the current build on the Windows desktop, archive the previous
build intact under `past emerald builds`, and copy the chosen normal save plus
its matching companion history unless the user explicitly opts out.

Use `tools/build_delivery/deploy.py`. It first produces a read-only plan. It can
consume a local complete play-package ZIP or download one using `--download-url`
and a required `--package-sha256`. Private GitHub artifacts must be retrieved via
the authorized connector; do not extract credentials into a helper script.
The desktop path is resolved through Windows, including redirected desktops.

Example from the repository root:

```
python tools/build_delivery/deploy.py --package ABSOLUTE_PACKAGE_ZIP
python tools/build_delivery/deploy.py --package ABSOLUTE_PACKAGE_ZIP --apply
```

Current delivery folder: `Desktop/Emerald Current Build`; play using `Play.cmd`.
Archive folder: `Desktop/past emerald builds`. Old folders are renamed intact;
their original ROMs, saves, history, instructions and other files are retained.

Save selection uses the newest modification time among checksum-valid normal
saves in recognized current/previous desktop builds and the archive. It uses
the adjacent ROM's actual save-sector layout, validates both save slots, and
preserves the entire file including an optional RTC tail. It never chooses an
emulator save state. `--save` explicitly selects another validated save.
`--furthest` prioritizes recorded play time; play time is not proof of story
completion and is not the default. No different playthroughs are merged.

Copy the matching source history folder as a whole, preserving all snapshots.
If the selected normal save references extended history, its required snapshot
must exist, have the correct hash and match the save identity. Missing history
blocks replacement instead of silently losing memory. `--skip-save` explicitly
omits both save and history for that delivery; it does not change future defaults.

The updater refuses to replace folders while an emulator is open. Packages are
staged and hash-checked before activation. Any interrupted folder activation
attempt restores moved old folders. An already-current build is not re-archived.
Every delivery records its chosen save hash, copied history file hashes, ROM
hash, source commit and archive destinations in local `delivery.json`. These
private delivery records must not be committed to the repository.

This automates the handoff when a build is delivered in this project. It is not
a scheduled paid Codex poller or a background service watching GitHub.
Run `python -m unittest discover -s tools/build_delivery -p test_deploy.py -v`
after changing the delivery tool. The tests use isolated temporary desktops.
