DEVELOPMENT HELPER -- NOT A COMPLETE FULL-GAME DIALOGUE RELEASE

Requires the matching bridge-enabled Emerald ROM and desktop mGBA 0.10+.
Do not load it for the earlier pilot ROM: that ROM has no bridge descriptor.

Setup:
  python install_helper.py "C:/path/to/your/ROM/folder"

Open the matching Emerald ROM in mGBA. Open Tools > Scripting, then load the
generated load-companion-history.lua. The script logs that it attached. Load it
each time you start mGBA. This does not require a patched emulator or Python
while playing. After moving the game folder, run the setup command again.

Keep the companion-history folder together with your game's .sav and save
states. Back up all of them together. Old saves and save states can refer to
older .history files, so do not delete individual snapshots. Copying only the
.sav does not copy the expanded history. Ordinary original game progress and
the released pilot history remain in the .sav.

The helper never writes your .sav. It stores a verified snapshot before the ROM
offers an expanded observation. Normal game saving stores its reference. If a
snapshot is missing or corrupt, new expanded comments remain quiet; the stored
reference is preserved. Restore the matching history folder and restart/load
the normal save to retry. Existing dialogue, NPCs, battles and saving still work.

The current implementation uses about 17 KB per newly offered expanded comment.
Snapshot retention and hard-power-loss durability are still under review.
Native ROM migration, both save slots and save-state recovery need final tests.
Host tests alone do not establish these guarantees. Do not replace your accepted
playing build or delete its backups with this development prototype.
