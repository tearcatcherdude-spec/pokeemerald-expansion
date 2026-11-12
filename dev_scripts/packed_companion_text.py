"""Lossless GBA LZ77 blocks for permanent, independently indexed companion text.

The catalogue IDs, voices and expressions stay unchanged. No dialogue is removed.
Use --audit OUTPUT for a reversible proof before --build updates generated assets.
"""
from pathlib import Path
import argparse,collections,hashlib,json,re,struct
from build_cast import wrapped
ROOT=Path(__file__).resolve().parents[1]
BLOCK=4096
NONE=0xFFFFFFFF
VOICES=['pip','silas','kade','ashe','nico','riven','emi','vera','lume','mochi','zuri']
EXPRESSIONS=['neutral','soft_smile','annoyed','flustered','sad','surprised','smug','laughing']

def charset():
    result={}
    for line in (ROOT/'charmap.txt').read_text(encoding='utf-8').splitlines():
        m=re.match(r"^'(.*?)'\s*=\s*((?:[0-9A-F]{2}(?:\s+|$))+)",line)
        if m:
            token=m[1]
            token={r"\'":"'",r'\"':'"',r'\\':'\\'}.get(token,token)
            result[token]=bytes.fromhex(m[2])
        else:
            m=re.match(r'^(\w+)\s*=\s*((?:[0-9A-F]{2}(?:\s+|$))+)',line)
            if m:result['{'+m[1]+'}']=bytes.fromhex(m[2])
    pattern=re.compile('|'.join(re.escape(k) for k in sorted(result,key=len,reverse=True)))
    def encode(text):
        out=bytearray();at=0
        while at<len(text):
            m=pattern.match(text,at)
            if m is None:raise ValueError(('Unmapped GBA text',text[at:at+40]))
            out.extend(result[m[0]]);at=m.end()
        assert out[-1]==255 and 255 not in out[:-1]
        return bytes(out)
    return encode

def compress(data):
    out=bytearray([0x10])+len(data).to_bytes(3,'little');chains=collections.defaultdict(list);at=0
    while at<len(data):
        flagat=len(out);out.append(0);flags=0
        for bit in range(7,-1,-1):
            if at>=len(data):break
            best=0;distance=0;key=data[at:at+3]
            if len(key)==3:
                for prev in reversed(chains[key][-96:]):
                    if at-prev>4096:break
                    n=3
                    while n<18 and at+n<len(data) and data[prev+n]==data[at+n]:n+=1
                    if n>best:best=n;distance=at-prev
                    if best==18:break
            length=best if best>=3 else 1
            if best>=3:
                flags|=1<<bit;value=((best-3)<<12)|(distance-1);out.extend(value.to_bytes(2,'big'))
            else:out.append(data[at])
            for p in range(at,at+length):
                if p+3<=len(data):chains[data[p:p+3]].append(p)
            at+=length
        out[flagat]=flags
    return bytes(out)

def decompress(data):
    assert data[0]==0x10
    size=int.from_bytes(data[1:4],'little');out=bytearray();at=4
    while len(out)<size:
        flags=data[at];at+=1
        for bit in range(7,-1,-1):
            if len(out)>=size:break
            if flags&(1<<bit):
                v=int.from_bytes(data[at:at+2],'big');at+=2;length=(v>>12)+3;distance=(v&4095)+1
                assert distance<=len(out)
                for _ in range(length):out.append(out[-distance])
            else:out.append(data[at]);at+=1
    assert len(out)==size
    return bytes(out)

def fnv(data,value=2166136261):
    for b in data:value=((value^b)*16777619)&0xFFFFFFFF
    return value

def prepare():
    catalogue=json.loads((ROOT/'data/companion_dialogue/contexts.json').read_text());encode=charset();blocks=[];current=bytearray();refs=[];golden=2166136261;decoded=bytearray();count=0;unique={};maxlen=0
    for row in catalogue['contexts']:
        entries=[]
        for voice in VOICES:
            if row.get('retired'):entries.append((NONE,0));continue
            reply=next(r for r in row['replies'] if r['voice']==voice);data=encode(wrapped(reply['text'],voice));expr=EXPRESSIONS.index(reply['expression']);maxlen=max(maxlen,len(data));assert len(data)<1000
            if data in unique:ref=unique[data]
            else:
                if len(current)+len(data)>BLOCK:blocks.append(bytes(current));current=bytearray()
                ref=(len(blocks)<<12)|len(current);current.extend(data);unique[data]=ref
            entries.append((ref,expr));decoded.extend(data);decoded.append(expr);golden=fnv(data+bytes([expr]),golden);count+=1
        refs.append(entries)
    if current:blocks.append(bytes(current))
    blob=bytearray();offsets=[]
    for raw in blocks:
        while len(blob)%4:blob.append(0)
        offsets.append(len(blob));compressed=compress(raw);assert decompress(compressed)==raw;blob.extend(compressed)
    while len(blob)%4:blob.append(0)
    # Every reference, voice, expression and terminator is checked independently.
    rebuilt=bytearray()
    for row in refs:
        for ref,expr in row:
            if ref==NONE:continue
            b,off=ref>>12,ref&4095;payload=blocks[b][off:];data=payload[:payload.index(255)+1];rebuilt.extend(data);rebuilt.append(expr)
    assert rebuilt==decoded
    report=dict(format='GBA BIOS LZ77, separately indexed blocks <=4096 bytes',contexts=len(refs),voices=VOICES,replies=count,unique_replies=len(unique),block_count=len(blocks),max_reply_bytes=maxlen,uncompressed_text_bytes=sum(map(len,blocks)),packed_text_bytes=len(blob)+len(offsets)*4,bytes_reclaimed=sum(map(len,blocks))-len(blob)-len(offsets)*4,decoded_catalogue_sha256=hashlib.sha256(decoded).hexdigest(),native_golden_fnv=golden,roundtrip_all_replies=True,rom_tested=False)
    return refs,blocks,bytes(blob),offsets,report

def write(output,build=False):
    refs,blocks,blob,offsets,report=prepare();output.mkdir(parents=True,exist_ok=True)
    (output/'packed_text.bin').write_bytes(blob);(output/'packed_text.json').write_text(json.dumps(report,indent=2)+'\n')
    if build:
        p=ROOT/'src/data/companion_contexts.h';s=p.read_text(encoding='utf-8');start=s.index('static const struct ContextReply sContextReplies');end=s.index('\n};',start)+3
        table='static const struct ContextReply sContextReplies[][COMPANION_VOICE_COUNT] = {\n'+''.join(' {'+', '.join('{0x%08X, %d}'%(ref,expr) for ref,expr in row)+'},\n' for row in refs)+'};'
        p.write_text(s[:start]+table+s[end:],encoding='utf-8')
        header='const u32 gCompanionPackedText[] = INCBIN_U32("data/companion_dialogue/packed/packed_text.bin");\nconst u32 gCompanionPackedTextOffsets[] = {\n'+''.join(' 0x%08X,\n'%v for v in offsets)+'};\n'
        (ROOT/'src/data/companion_packed_text.h').write_text(header)
        (ROOT/'include/companion_packed_text_golden.h').write_text('#define PACKED_CONTEXT_COUNT %d\n#define PACKED_REPLY_COUNT %d\n#define PACKED_REPLY_FNV 0x%08Xu\n'%(len(refs),report['replies'],report['native_golden_fnv']))
    print(json.dumps(report))
    return report
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--audit',type=Path);p.add_argument('--build',action='store_true');a=p.parse_args();write(ROOT/'data/companion_dialogue/packed' if a.build else a.audit,a.build)
