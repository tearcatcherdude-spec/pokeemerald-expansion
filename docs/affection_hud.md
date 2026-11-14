# Companion affection display

The top-center notification uses the existing saved bond EXP and level curve.
It shows a heart, companion name, level, awarded EXP (for example +10), and
current-level progress as numbers (for example 35/80 EXP) above a filling bar.
At level 20 it shows MAX 3040 EXP and a full bar.

Every successful Bonds_AddExp award queues a notification. Repeated gains for
the same companion combine while queued or animating; all ten companions have
independent slots. A full bar pauses for a pulsing heart and gold sparkle,
then advances the level and animates any remaining EXP, including multiple
levels. The notification holds briefly and dissolves without input.

Dialogue, menus, map-name popups and fades hide/pause it. Sprite resets release
its own tiles and palette and retain pending progress for the next field frame.
It uses two 64x32 OBJ sprites, 2048 tile bytes and one palette, with no BG windows,
script locks, input interception, new save fields or global blending changes.

Validation: focused native unit tests cover all level boundaries, all-companion
queuing, capped/invalid awards and saved EXP preservation. Runtime visual and
movement checks must be recorded against the packaged ROM before delivery.
