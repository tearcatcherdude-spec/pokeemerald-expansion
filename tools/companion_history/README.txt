DEVELOPMENT HELPER -- NOT A COMPLETE FULL-GAME DIALOGUE RELEASE

Requires the matching bridge-enabled Emerald ROM and desktop mGBA 0.10+.
Do not load it for the earlier pilot ROM: that ROM has no bridge descriptor.

Development packaging (the release ZIP will include the prepared helper):
  python install_helper.py "C:/path/to/your/ROM/folder"

Open the matching Emerald ROM in mGBA. Open Tools > Scripting, then load the
generated load-companion-history.lua. The script logs that it attached. Load it
each time you start mGBA. This does not require a patched emulator or Python
while playing. The helper locates the history folder beside its own Lua file;
keep that folder with it when moving the game.

Keep a pre-upgrade copy of the accepted ROM and .sav in a separate folder.
Migration is forward: after this build writes the extended SaveBlock2 checksum,
older ROMs cannot reliably read that save. Revert using the pre-upgrade .sav.
To migrate an old emulator save state, load it in its original ROM and use the
in-game Save first, then copy that .sav to the new build. Do not load an old
ROM's emulator state directly into the new ROM: its code and RAM layout differ.

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
Native migration, both save slots, backup recovery and matching-ROM save-state
rollback passed prepared-fixture checks on commit c38a6b059f. Desktop Scripting
UI operation and hard-power-loss durability are not verified. Full-game dialogue
coverage is unfinished; keep the accepted playing build and its backups.
