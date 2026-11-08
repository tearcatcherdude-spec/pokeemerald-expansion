#!/usr/bin/env python3
"""Build/check the twelve original NPC assets. Requires Pillow; no ROM tools.

python tools/hoenn_originals.py build
python tools/hoenn_originals.py check
"""
from pathlib import Path
import argparse
import hashlib
import json
import struct
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
PICS = ROOT / 'graphics/object_events/pics/people/hoenn_originals'
PALS = ROOT / 'graphics/object_events/palettes/hoenn_originals'
DOCS = ROOT / 'docs/hoenn_originals'
NAMES = 'emi rex nova silas miko jax vera kade lume bran poppy morph'.split()
VIEWS = {'south': [3, 0, 4, 0], 'north': [5, 1, 6, 1],
         'west': [7, 2, 8, 2], 'east': [7, 2, 8, 2]}
DIGITS = '0123456789ABCDEF'

def source(name):
    data = json.loads((PICS / (name + '.json')).read_text())
    assert data['name'] == name
    assert len(data['palette']) == 16
    assert len(data['rows']) == 32
    assert all(len(row) == 144 and set(row) <= set(DIGITS) for row in data['rows'])
    return data

def paltext(palette):
    return 'JASC-PAL\n0100\n16\n' + ''.join(' '.join(map(str, c)) + '\n' for c in palette)

def packed_tiles(im):
    """GBA 4bpp, nine 2x4-tile metatiles, low nibble = left pixel."""
    result = bytearray()
    for frame in range(9):
        for ty in range(4):
            for tx in range(2):
                for y in range(8):
                    for x in range(0, 8, 2):
                        px = frame * 16 + tx * 8 + x
                        py = ty * 8 + y
                        result.append(im.getpixel((px, py)) | im.getpixel((px + 1, py)) << 4)
    return bytes(result)

def unpacked_tiles(raw):
    im = Image.new('P', (144, 32))
    # Decode independently from the encoder's nested tile loops.
    for y in range(32):
        for x in range(144):
            frame, local_x = divmod(x, 16)
            tile = (y // 8) * 2 + local_x // 8
            byte = raw[frame * 256 + tile * 32 + (y % 8) * 4 + (local_x % 8) // 2]
            im.putpixel((x, y), (byte >> (4 * (x % 2))) & 15)
    return im

def frames(im):
    return [im.crop((i * 16, 0, i * 16 + 16, 32)) for i in range(9)]

def bbox(im):
    return Image.frombytes('L', im.size, im.tobytes()).point(lambda v: 255 if v else 0).getbbox()

def preview_frame(frame, size=6):
    bg = Image.new('RGBA', (16, 32), (115, 197, 156, 255))
    bg.alpha_composite(frame.convert('RGBA'))
    return bg.convert('RGB').resize((16 * size, 32 * size), Image.Resampling.NEAREST)

def build():
    PALS.mkdir(parents=True, exist_ok=True)
    (DOCS / 'previews').mkdir(parents=True, exist_ok=True)
    contact = Image.new('RGB', (1010, 12 * 150 + 40), '#f0f2e8')
    draw = ImageDraw.Draw(contact)
    draw.text((12, 12), 'HOENN ORIGINALS | 16x32 cells, shown at 4x | S N W S1 S2 N1 N2 W1 W2', fill='#16382d')
    gallery = []
    all_frames = {}
    for row, name in enumerate(NAMES):
        data = source(name)
        im = Image.new('P', (144, 32))
        im.putdata([DIGITS.index(c) for line in data['rows'] for c in line])
        im.putpalette([v for c in data['palette'] for v in c])
        im.save(PICS / (name + '.png'), bits=4, transparency=0)
        (PALS / (name + '.pal')).write_text(paltext(data['palette']), newline='\n')
        fs = frames(im)
        all_frames[name] = fs
        y = 40 + row * 150
        draw.text((12, y + 50), name.title(), fill='#16382d')
        for i, frame in enumerate(fs):
            x = 105 + i * 98
            contact.paste(preview_frame(frame, 4), (x, y))
            draw.text((x + 28, y + 130), str(i), fill='#16382d')
        sequence = []
        for step in range(4):
            strip = Image.new('RGB', (4 * 110, 218), '#f0f2e8')
            sd = ImageDraw.Draw(strip)
            for col, (view, order) in enumerate(VIEWS.items()):
                frame = fs[order[step]]
                if view == 'east': frame = frame.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
                strip.paste(preview_frame(frame), (col * 110 + 7, 20))
                sd.text((col * 110 + 12, 4), view, fill='#16382d')
            sequence.append(strip)
        sequence[0].save(DOCS / 'previews' / (name + '.gif'), save_all=True,
                         append_images=sequence[1:], duration=134, loop=0, disposal=2)
    contact.save(DOCS / 'previews/contact.png')
    # One simultaneous gallery: each row shows south/north/west/east.
    for step in range(4):
        gallery_frame = Image.new('RGB', (840, 3 * 145), '#f0f2e8')
        gd = ImageDraw.Draw(gallery_frame)
        for i, name in enumerate(NAMES):
            x, y = (i % 4) * 210, (i // 4) * 145
            gd.text((x + 8, y + 8), name.title() + '  S N W E', fill='#16382d')
            for col, (view, order) in enumerate(VIEWS.items()):
                f = all_frames[name][order[step]]
                if view == 'east': f = f.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
                gallery_frame.paste(preview_frame(f, 3), (x + col * 51 + 2, y + 30))
        gallery.append(gallery_frame)
    gallery[0].save(DOCS / 'previews/walking.gif', save_all=True,
                    append_images=gallery[1:], duration=134, loop=0, disposal=2)

def check():
    report = {'status': 'pass', 'rom_build_tested': False, 'emulator_tested': False, 'assets': []}
    distinct = set()
    for name in NAMES:
        data = source(name)
        path = PICS / (name + '.png')
        raw_png = path.read_bytes()
        assert raw_png[:8] == b'\x89PNG\r\n\x1a\n'
        assert raw_png[24:26] == bytes([4, 3]), f'{name}: expected 4-bit indexed PNG'
        # PNG must physically contain exactly 16 palette entries.
        pos = 8
        while raw_png[pos+4:pos+8] != b'PLTE':
            pos += 12 + struct.unpack('>I', raw_png[pos:pos+4])[0]
        assert struct.unpack('>I', raw_png[pos:pos+4])[0] == 48
        im = Image.open(path)
        assert im.size == (144, 32) and im.mode == 'P'
        assert im.info['transparency'] == 0
        assert list(im.tobytes()) == [DIGITS.index(c) for row in data['rows'] for c in row]
        assert im.getpalette()[:48] == [v for c in data['palette'] for v in c]
        assert (PALS / (name + '.pal')).read_text() == paltext(data['palette'])
        for color in data['palette']:
            assert all(0 <= c <= 255 and c == ((c >> 3) * 255 // 31) for c in color), (name, color)
        assert max(im.tobytes()) <= 15
        fs = frames(im)
        boxes = [bbox(f) for f in fs]
        assert all(box for box in boxes), f'{name}: empty frame'
        assert all(box[3] == (31 if i < 3 else 32) for i, box in enumerate(boxes)), (name, boxes)
        assert len({f.tobytes() for f in fs}) == 9, f'{name}: duplicate poses'
        cut = (12 if name == 'poppy' else 11) + 13
        for i, standing in ((3,0),(4,0),(5,1),(6,1),(7,2),(8,2)):
            assert fs[i].crop((0,1,16,cut+1)).tobytes() == fs[standing].crop((0,0,16,cut)).tobytes(), f'{name}: head drift'
        packed = packed_tiles(im)
        assert len(packed) == 9 * 256
        assert unpacked_tiles(packed).tobytes() == im.tobytes()
        digest = hashlib.sha256(raw_png).hexdigest()
        assert digest not in distinct
        distinct.add(digest)
        report['assets'].append({'name':name, 'png_sha256':digest, 'visible_colors':len(set(im.tobytes())-{0}),
                                 'frame_bboxes':boxes, 'four_bpp_bytes':len(packed),
                                 'four_bpp_roundtrip':'pass', 'palette_match':'pass', 'head_registration':'pass'})
    DOCS.mkdir(exist_ok=True)
    (DOCS / 'validation.json').write_text(json.dumps(report, indent=2)+'\n')
    print('PASS: 12 indexed PNGs, 108 distinct poses, 16-entry matching palettes, anchors, head registration, 4bpp round trips.')
    print('ROM compilation, graphics registration, palette allocation and in-emulator validation: NOT RUN.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['build', 'check'])
    args = parser.parse_args()
    if args.action == 'build': build()
    else: check()
