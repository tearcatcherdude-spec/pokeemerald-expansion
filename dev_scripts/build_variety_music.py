"""Reproducible, original eight-part trainer scores using the native FRLG bank.

No MIDI libraries or new samples are required. 24 PPQ, two-bar introduction,
32-bar loop. Program numbers refer to the game's bank, not General MIDI.
"""
from pathlib import Path
import json
import struct

ROOT = Path(__file__).resolve().parents[1]
START, END = 192, 3264
SCORES = [
    # slug, title, BPM, tonic, scale, harmonic roots, lead voice, rhythm
    ('steady', 'Friendly Rivalry', 136, 62, [0,2,3,5,7,8,10], [0,5,3,4,0,2,5,4], 62, [0,12,24,42,48,60,72,84]),
    ('brisk', 'Running on Sparks', 154, 64, [0,2,3,5,7,9,10], [0,3,5,4,0,6,3,4], 29, [0,6,18,24,36,42,54,60,72,78,84]),
    ('wistful', 'One More Try', 104, 60, [0,2,3,5,7,8,10], [0,5,3,6,0,2,5,4], 5, [0,24,60,72]),
    ('cheerful', 'Pocketful of Sunshine', 124, 65, [0,2,4,5,7,9,11], [0,4,5,3,0,1,3,4], 21, [0,18,24,36,54,60,78]),
    ('silly', 'Absolutely According to Plan', 112, 67, [0,2,4,5,7,9,10], [0,0,3,4,5,1,4,0], 17, [0,12,36,42,66,84]),
    ('tense', 'A Narrow Escape', 120, 61, [0,1,3,5,7,8,10], [0,1,0,5,3,1,4,0], 48, [0,12,24,36,48,66,72,84]),
    ('laidback', 'No Need to Rush', 108, 69, [0,2,4,5,7,9,10], [0,5,1,4,0,3,1,4], 24, [6,24,42,66,84]),
]

def vlq(n):
    b = [n & 127]
    while n >> 7:
        n >>= 7
        b.insert(0, 128 | (n & 127))
    return bytes(b)

def encode(events):
    b, last = bytearray(), 0
    for tick, priority, event in sorted(events):
        b += vlq(tick-last) + event
        last = tick
    return b'MTrk' + struct.pack('>I',len(b)) + b

def meta(t, kind, value):
    return (t,0,bytes([255,kind])+vlq(len(value))+value)

def make_score(score):
    slug,title,bpm,key,scale,roots,voice,rhythm = score
    metadata = [meta(0,3,title.encode()),meta(0,81,round(60000000/bpm).to_bytes(3,'big')),
                meta(0,88,bytes([4,2,24,8])),meta(START,6,b'['),meta(END,6,b']'),meta(END,47,b'')]
    programs = [voice,81,33,5 if slug!='wistful' else 48,3,0,127,82]
    volumes = [100,54,95,48,45,82,42,35]
    pans = [64,42,64,83,95,64,58,30]
    tracks=[]
    for ch,pgm in enumerate(programs):
        tracks.append([(0,1,bytes([0xc0|ch,pgm])),(0,1,bytes([0xb0|ch,7,volumes[ch]])),
                       (0,1,bytes([0xb0|ch,10,pans[ch]])),meta(END,47,b'')])
    count=0
    def note(ch,t,d,p,v):
        nonlocal count
        assert 0<=p<128 and t+d<=END
        tracks[ch] += [(t,3,bytes([0x90|ch,p,v])),(t+d,2,bytes([0x80|ch,p,0]))]
        count+=1
    def degree(d):
        return key + scale[d%7] + 12*(d//7)
    # Original rising answer; no quotation or reused source sequence.
    for bar in range(2):
        for j in range(4):
            note(0,bar*96+j*24,18,degree([0,2,4,6,7,6,4,1][bar*4+j]),90)
            note(2,bar*96+j*24,19,key-24+(7 if j%2 else 0),88)
            note(5,bar*96+j*24,4,36 if j%2==0 else 41,85)
    for bar in range(32):
        t=START+bar*96
        root=roots[bar%8]
        section=bar//8
        for j,offset in enumerate(rhythm):
            # Phrase identities and an eight-bar cadence, not a transposed loop.
            motif = ([0,2,4,3,2,1,4,2] if slug=='steady' else
                     [0,4,2,5,4,6,5,2,1,4,3] if slug=='brisk' else
                     [4,2,1,0] if slug=='wistful' else
                     [2,4,5,4,2,1,0] if slug=='cheerful' else
                     [0,4,1,5,2,0] if slug=='silly' else
                     [0,1,0,4,3,1,2,0] if slug=='tense' else [2,4,6,5,2])
            d=root+motif[j%len(motif)]+(7 if section==2 else 0)
            if bar%8==7:
                d=[4,3,2,1,0][min(j,4)]
            nextoff=rhythm[j+1] if j+1<len(rhythm) else 96
            duration=max(3,nextoff-offset-(7 if slug=='silly' else 2))
            note(0,t+offset,duration,degree(d),100 if offset%24==0 else 85)
        # Countervoice rests through the first phrase, enters as an answer.
        if section in (1,3):
            for j,off in enumerate((12,48,78)):
                note(1,t+off,14,degree(root+[4,2,0][j])-12,70)
        bass_pattern=(0,36,60) if slug=='laidback' else (0,24,48,72)
        for j,off in enumerate(bass_pattern):
            p=degree(root)-24+(7 if j%2 else 0)
            note(2,t+off,18 if slug!='silly' else 8,p,94)
        for off in ((0,48) if slug in ('wistful','tense') else (24,72)):
            for d in (root,root+2,root+4):
                note(3,t+off,40 if slug=='wistful' else 12,degree(d)-12,56)
        for j,off in enumerate(range(0,96,12)):
            if slug=='silly' and j in (2,3,6):continue
            note(4,t+off,7,degree(root+[0,2,4,2][j%4]),52)
        for off in (0,48):note(5,t+off,4,36,92)
        for off in (24,72):note(5,t+off,4,41,80)
        if bar%4==3:
            for off in (84,90):note(5,t+off,3,41,64)
        for off in range(0,96,12 if slug=='brisk' else 24):note(6,t+off,3,91,50)
        if section==2:
            for off in (0,48):note(7,t+off,28,degree(root+4),45)
    midi=b'MThd'+struct.pack('>IHHH',6,1,9,24)+encode(metadata)+b''.join(encode(t) for t in tracks)
    return midi,dict(slug=slug,title=title,bpm=bpm,ppq=24,loop_start=START,loop_end=END,notes=count,voicegroup='rg_vs_trainer')

def main():
    reports=[]
    for s in SCORES:
        midi,report=make_score(s)
        (ROOT/'sound/songs/midi'/f'mus_variety_{s[0]}.mid').write_bytes(midi)
        reports.append(report)
    target=ROOT/'data/trainer_variety'
    target.mkdir(parents=True,exist_ok=True)
    (target/'music.json').write_text(json.dumps(reports,indent=2)+'\n')
    print('Generated seven original scores,',sum(x['notes'] for x in reports),'notes')

if __name__=='__main__':main()
