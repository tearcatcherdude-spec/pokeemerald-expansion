# Parallel Watch: playable Kanto trial

Built on the complete Living Hoenn/Pip branch. Existing starters, scenes, rewards,
rare encounters and saved dialogue memory remain in place.

Find the Parallel Watch on the ground in Littleroot at (8,17). Use it from Key
Items, or register it to Select. It needs a healthy non-egg Pokémon and clear
outdoor ground on foot. Say Yes to cross; No leaves both return points alone.

First arrival is Pallet Town. Each successful crossing remembers the departure
map, tile and facing separately for Hoenn and Kanto, including across normal saves.
The party, bag, money and PC are the same data in both worlds. There is no save
exchange, second trainer, starter reset or copied inventory. Existing saves acquire
new watch data on first use; retain a backup of your .sav as usual.

The trial contains Pallet Town, Route 1 and Viridian City, plus both floors of the
Pallet visitor house, the neighboring house, lab, Viridian Center, Mart, house and
school. Route 1 has native grass encounters (Pidgey/Rattata, levels 2–4), ledges and
walkable connections. The Center heals and provides the normal shared PC. The Mart
sells basic supplies. Six new Pip lines are one-shot additions to his catalogue.

This does not yet contain the full Kanto story, gyms, rival, badge progression or
League. Gym and onward roads are closed. Upstairs link rooms are closed. Switching
inside buildings, caves, facilities, special maps or on water/bikes is unavailable.
The trial Center does not replace your Hoenn whiteout/Teleport home: defeat returns
to your existing Hoenn healing location, while the watch retains the Kanto anchor.

Implementation notes:

- New map group and appended layout IDs; original FRLG and Hoenn maps are untouched.
- Selected FRLG layouts opt in to Emerald via parallel_watch, retaining their native
  640-metatile primary tileset/border format. Assets in this repository already use
  unified Emerald behavior IDs; no second behavior conversion is applied.
- New event scripts never run the original Kanto story scripts or flags.
- Item ID and flag are appended/allocated from unused space; old IDs stay stable.
- SaveBlock3's complete 160-byte Living Hoenn prefix stays fixed; version and two
  eight-byte anchors extend it to 180 bytes. SaveBlocks 1/2 and PC size stay fixed.
- Destination anchors are checked against bounds, collision, behavior, warps,
  coordinate scripts and NPC movement ranges before use. Invalid anchors use a
  verified fallback. Coordinate warp API retains signed 16-bit route coordinates.

Validation status: source implementation prepared; build and emulator tests pending.
