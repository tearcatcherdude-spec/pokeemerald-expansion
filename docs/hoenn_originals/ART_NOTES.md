# Art provenance and prompt set

Visual reference: the user-supplied `Hoenn NPC Expansion Pack Sprite Sheet.png`.
The poster is a concept reference; its compatibility labels were not treated as
evidence of usable animation or palette data.

Eleven source strips were created with the built-in image-generation tool using
the poster plus a nearest-neighbor enlargement of the repository's
`woman_1.png` as visual references. Poppy's source generation did not return an
image, so her three small directional reference views were extracted directly
from the supplied poster; her feet were authored as separate step poses. No CLI
image-generation fallback or external API key was used.

The generated strips were **not** submitted as game assets. Workspace processing
separated the poses from their flat background, reduced them to a controlled
native envelope, indexed them without dithering, snapped palette colors to
RGB555-representable values, and fixed head/face registration and foot anchors.
Pixel corrections restored Emi's violet detail, Jax's red nose/grin, Rex's blue
shorts, Morph's green jacket/orange tie, and Poppy's ear continuity and foot poses.
The checked-in JSON pixel matrices are the final editable source of truth;
rebuilding them does not rerun image generation.

## Emi prompt

> Create ONLY Emi's production overworld game sprite sheet. First image is
> character reference; use ONLY Emi, black asymmetrical fringe, purple streak
> and small purple hair clip, purple striped sleeves, black skirt and boots.
> Second image is EXACT Emerald NPC proportion and 9 frame animation layout
> template. Output 9 equally spaced 16x32 logical pixel frames in a single
> horizontal row, magnified exactly 8x nearest neighbor: logical sheet 144x32,
> physical 1152x256 centered on solid flat #78c8a0 background. Frames left to right
> MUST be: south idle, north idle, west idle, south step A, south step B, north
> step A, north step B, west step A, west step B. East obtained by runtime mirror.
> Strict original Pokemon Emerald small squat overworld proportions (head 10
> pixels wide, overall art 14 pixels wide and 22 pixels tall in 16x32 cell with
> empty padding above), no large portrait, no concept illustration, no
> labels/text/grid/shadows. Use exact coherent pixel grid and <=15 solid colors
> plus background. Keep head proportions and silhouette consistent across walk
> poses, feet same baseline. No antialiasing. Adapt clothing and hairstyle only
> to template scale, with distinguishable walking feet and arms.

## Shared prompt for the other initial source strips

> Create ONE production overworld sprite strip ONLY the named character.
> Character identity follows first image concept reference. Second image is
> exact Pokemon Emerald nine-frame layout and small squat NPC proportions.
> Nine equally spaced logical 16x32 pixel cells in ONE horizontal row, big empty
> top margin inside cells, whole sprite 14 pixels wide and 22 pixels tall
> (Poppy 20 tall). Image may be enlarged but pixel art logical grid must remain
> consistent. Frame order: south idle, north idle, west idle, south step A,
> south step B, north step A, north step B, west step A, west step B. East is
> runtime mirror. Feet same baseline, coherent head between animation poses,
> visibly alternating legs and arms in steps. Solid #78c8a0 background, <=15
> flat colors in character, no text, no labels, no illustration/portrait, no
> grids, no cast shadows, no antialiasing.

Each request appended the corresponding design:

| Character | Appended design |
| --- | --- |
| Rex | Skater boy, shaggy brown hair under a backward red and cream cap, red open jacket over charcoal shirt, blue shorts, orange shoes. No skateboard. |
| Nova | Tech girl with cyan twin buns and long side locks, orange goggles above forehead, dark teal outfit with orange utility accents and cyan boots. |
| Silas | Young alchemist man with fluffy spiky white hair, square dark glasses, white open lab coat with blue trim, navy shirt and trousers, brown shoes. |
| Miko | Shrine wanderer girl with black twin tails with red ribbon ties, white wide sleeves and red skirt, black shoes. |
| Jax | Comic performer man, bright lime green tall mohawk, pale face with small red clown nose and grin, yellow sleeves, green vest and navy trousers, orange shoes. |
| Vera | Punk girl, tousled magenta pink bob with one long side, silver goggles resting on head, black sleeveless outfit with purple belt, black boots. |
| Kade | Biker man with spiky charcoal black hair, dark sunglasses, black leather jacket with tiny gold accents, dark trousers and boots. No motorcycle. |
| Lume | Mysterious girl with lilac bob and long side locks under deep purple hood, dark purple cloak with clasp, dark boots. |
| Bran | Fisherman man with wide straw yellow hat and teal hatband, short brown hair, blue overalls over cyan shirt, brown boots, small tan fishing pack. |
| Poppy | Costume kid with bright yellow mouse hood, long ears with black tips, red cheek marks on hood, short black hair showing, yellow romper, dark shorts and orange shoes. Child smaller than adults. |
| Morph | Oddball man with spiky blue hair, enormous red rectangular glasses over eyes, white shirt and green patchwork jacket, orange tie, blue trousers, yellow shoes. |

## Final Morph source request

> Make a game sprite strip using ONLY Morph, the blue spiky-haired NPC with big
> red glasses, green jacket over white shirt, orange tie, blue trousers and yellow
> shoes, in bottom right of reference. Nine small squat Emerald overworld 16x32
> logical pixel frames in one horizontal row in same order as second reference
> template: south idle, north idle, west idle, south walk A, south walk B, north
> walk A, north walk B, west walk A, west walk B. Use solid #78c8a0 background,
> feet aligned, 15 solid colors plus background. No text or labels or ground
> shadows. Each figure 14 logical pixels wide and 20 tall with empty top margin
> in its cell. Keep head consistent across walking poses and clearly alternate
> feet. Exact pixel art, no smoothing or portrait. These are fully clothed tiny
> retro game characters.

The final assets follow measured native 19–20-pixel silhouette heights rather
than the source prompts' approximate 20–22-pixel estimates. Frame and palette
claims are based on the final files and validation, not generator instructions.
