"""Capacity model for the pending memory choice. Does not touch a game save.

The shared proposal preserves the released pilot's actual 0..46 independent
bits, plus seventeen reserved bits per voice. It assigns only unused future
pilot bytes and the unused sector tails to new history. It requires an explicit
format migration and the user's gameplay choice before runtime implementation.
"""
VOICES=11
PILOT_BYTES=1020
PILOT_BANK_BYTES=92
PRESERVED_BANK_PREFIX=8
PILOT_CONTEXTS=47
EXTENSION_SIZES=dict(pc=132,sb1=304,sb2=84,sb3=16)
HEADER_BYTES=8

def shared_regions():
    return [('pilot',8+v*PILOT_BANK_BYTES+PRESERVED_BANK_PREFIX,
             PILOT_BANK_BYTES-PRESERVED_BANK_PREFIX) for v in range(VOICES)]+[
        ('pc',HEADER_BYTES,EXTENSION_SIZES['pc']-HEADER_BYTES),
        ('sb1',0,EXTENSION_SIZES['sb1']),('sb2',0,EXTENSION_SIZES['sb2']),
        ('sb3',0,EXTENSION_SIZES['sb3'])]

def shared_capacity():return sum(n for _,_,n in shared_regions())*8

def shared_bit(index):
    if not 0<=index<shared_capacity():raise ValueError(index)
    byte,bit=divmod(index,8)
    for name,start,size in shared_regions():
        if byte<size:return name,start+byte,1<<bit
        byte-=size
    raise AssertionError('Capacity mismatch')

def independent_dense_capacity():
    extra=sum(EXTENSION_SIZES.values())-HEADER_BYTES
    return PILOT_BANK_BYTES*8+(extra//VOICES)*8

def verify():
    sizes=dict(pilot=PILOT_BYTES,**EXTENSION_SIZES)
    buffers={name:bytearray(size) for name,size in sizes.items()}
    # Deliberately nonzero released memory: no reliance on old history being empty.
    for i in range(8):buffers['pilot'][i]=(31+i)&255
    protected=[]
    for v in range(VOICES):
        start=8+v*PILOT_BANK_BYTES
        buffers['pilot'][start:start+PRESERVED_BANK_PREFIX]=bytes([v*7+3]*PRESERVED_BANK_PREFIX)
        protected.append(bytes(buffers['pilot'][start:start+PRESERVED_BANK_PREFIX]))
    metadata=bytes(buffers['pilot'][:8]);locations=set()
    for index in range(shared_capacity()):
        name,byte,mask=shared_bit(index)
        assert byte<sizes[name] and (name,byte,mask) not in locations
        locations.add((name,byte,mask));buffers[name][byte]|=mask
    for v,expected in enumerate(protected):
        start=8+v*PILOT_BANK_BYTES
        assert bytes(buffers['pilot'][start:start+PRESERVED_BANK_PREFIX])==expected
    assert bytes(buffers['pilot'][:8])==metadata
    assert buffers['pc'][:HEADER_BYTES]==bytes(HEADER_BYTES)
    assert independent_dense_capacity()==1120
    assert shared_capacity()==11616
    for invalid in [-1,shared_capacity()]:
        try:shared_bit(invalid)
        except ValueError:pass
        else:raise AssertionError('Out-of-range memory accepted')
    print('PASS: proposal models 11616 shared new states or 1120 dense independent contexts/voice; all released pilot bits/metadata, header and region boundaries remain protected. No save was modified.')

if __name__=='__main__':verify()
