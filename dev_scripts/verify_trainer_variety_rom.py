"""Check compiled walker bytes, palettes, front-picture pointers and seven songs."""
import json,re,struct,sys
from pathlib import Path
from verify_pip_rom import expected_frames,expected_palette
from verify_kanto_rom import graphics_ids
ROOT=Path(__file__).resolve().parents[1]

def verify(rom_path,map_path):
    rom=Path(rom_path).read_bytes();text=Path(map_path).read_text(encoding='utf-8',errors='replace')
    symbols={n:int(a,16) for a,n in re.findall(r'0x([0-9a-fA-F]{8,16})\s+(\w+)\s*$',text,re.M)}
    def word(address):return struct.unpack_from('<I',rom,address-0x08000000)[0]
    source=(ROOT/'include/constants/trainers.h').read_text()
    body=re.search(r'enum TrainerPicID\s*\{(.*?)\};',source,re.S)[1]
    body=re.sub(r'/\*.*?\*/|//[^\n]*','',body,flags=re.S)
    pics={};value=-1
    for token in body.split(','):
        token=token.strip()
        if not token:continue
        if '=' in token:
            name,expr=map(str.strip,token.split('=',1));value=int(expr,0)
        else:name=token;value+=1
        pics[name]=value
    ids=graphics_ids()
    for r in json.loads((ROOT/'data/trainer_variety/roster.json').read_text()):
        ident=r['id'];symbol=r['symbol'];u=ident.upper()
        assert word(symbols['gObjectEventGraphicsInfoPointers']+4*ids['OBJ_EVENT_GFX_VARIETY_'+u])==symbols['gObjectEventGraphicsInfo_'+symbol]
        expected=[(f'gObjectEventPic_{symbol}',expected_frames(ROOT/f'graphics/object_events/pics/people/variety_{ident}.png')),
                  (f'gObjectEventPal_{symbol}',expected_palette(ROOT/f'graphics/object_events/palettes/variety_{ident}.pal')),
                  (f'gTrainerPalette_{symbol}',expected_palette(ROOT/f'graphics/trainers/palettes/variety_{ident}.pal'))]
        for name,data in expected:
            at=symbols[name]-0x08000000
            assert rom[at:at+len(data)]==data,('Compiled artwork differs',name)
        front=word(symbols['gTrainerPicInfo']+8*pics['TRAINER_PIC_VARIETY_'+u])
        assert word(front)==symbols['gTrainerFrontPic_'+symbol]
        assert word(front+4)==symbols['gTrainerPalette_'+symbol]
    for i,name in enumerate(('steady','brisk','wistful','cheerful','silly','tense','laidback')):
        song=symbols['mus_variety_'+name]
        assert word(symbols['gSongTable']+(610+i)*8)==song,('Unregistered music',name)
        at=song-0x08000000
        assert rom[at]==8,('Unexpected native track count',name,rom[at])
        assert word(song+4)==symbols['voicegroup_rg_vs_trainer']
        for track in range(8):assert 0x08000000<=word(song+8+track*4)<0x08000000+len(rom)
    print('PASS: all 32 compiled nine-frame walkers, exact palettes, battle-picture registrations and seven native eight-track songs')

if __name__=='__main__':verify(*sys.argv[1:])
