# Void World: Hollow Oldale preview

First visual slice on top of the tested front-wall fix dd581a40. Original Oldale,
Kanto, companions, dialogue histories and save record sizes remain unchanged.
Five private maps append to a new map group and layout tail.

The four Oldale building sites become a crescent cottage, candle workshop,
moth-wing rest house and lost-and-found shop. All four interiors have new furniture.
The native background compiler reuses terrain metatiles and supplies private
512+512 tile banks. Backgrounds and actors are indexed 4bpp with RGB5 palettes.
Source renders are not emulator screenshots; deliver only actual emulator captures
as in-game previews. Full source prompts are in graphics/void_oldale/prompts.json.
Built-in ImageGen supplied the source art; the compiler produces real game assets.
The mood reference was https://neverwaygame.com/; no Neverway assets are imported.

Eight original hollow creatures: Wispit, Buttonmoth, Teacup, Sootling, Bellhop,
Puddle, Wick and Umbrel. Walk sheets contain front/back/left views plus simple
two-pose hovering/bobbing cycles. East is mirrored by Emerald's standard animation.
Their dialogue is deliberately odd and light; nobody explains the watch.

The watch retains its ordinary cross-region route and adds Hollow Oldale as a
destination. The Void uses a fixed town entry; return goes to the last validated
Hoenn anchor, with a safe original Oldale fallback. The existing two-world anchor
format is reused without a save resize. This first slice is a separate side-world,
not a third complete regional campaign with its own gyms or progression.
Indoor use remains blocked; enter/return from ordinary safe outdoor floor only.
No native NPC building, save file, trainer, old map number or history ID is replaced.

This is a review build. Do not deploy it over the user's running game merely to
show pictures. The already prepared front-wall fix remains a separate pending
delivery until the user saves and closes. Full-world quests, battles, unique
healing/shop services and expansion beyond Oldale remain future work.
