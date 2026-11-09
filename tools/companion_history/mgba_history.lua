-- mGBA 0.10+ host adapter, bridge ABI 1. Development module, not a ROM patch.
-- attach(emu, callbacks, existing_directory) returns its frame handler for QA.
-- Never writes the .sav, ROM, PC, party or arbitrary memory addresses.
local M = {}
local K = {
  0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,
  0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,
  0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,
  0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,
  0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,
  0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,
  0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,
  0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2,
}
local function ror(x,n) return ((x >> n) | (x << (32-n))) & 0xffffffff end
function M.sha256(data)
  local h = {0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19}
  local length = #data
  data = data .. '\128' .. string.rep('\0', (55-length)%64) .. string.pack('>I8', length*8)
  for start=1,#data,64 do
    local w = {}
    for i=1,16 do w[i] = string.unpack('>I4',data,start+(i-1)*4) end
    for i=17,64 do
      local x,y=w[i-15],w[i-2]
      w[i]=(w[i-16]+(ror(x,7)~ror(x,18)~(x>>3))+w[i-7]+(ror(y,17)~ror(y,19)~(y>>10))) & 0xffffffff
    end
    local a,b,c,d,e,f,g,j=table.unpack(h)
    for i=1,64 do
      local t1=(j+(ror(e,6)~ror(e,11)~ror(e,25))+((e&f)~((~e)&g))+K[i]+w[i]) & 0xffffffff
      local t2=((ror(a,2)~ror(a,13)~ror(a,22))+((a&b)~(a&c)~(b&c))) & 0xffffffff
      j,g,f,e,d,c,b,a=g,f,e,(d+t1)&0xffffffff,c,b,a,(t1+t2)&0xffffffff
    end
    local v={a,b,c,d,e,f,g,j}
    for i=1,8 do h[i]=(h[i]+v[i])&0xffffffff end
  end
  return string.pack('>I4I4I4I4I4I4I4I4',table.unpack(h))
end
local function hex(s) return (s:gsub('.',function(c) return string.format('%02x',c:byte()) end)) end
local function inRam(p,n) return p>=0x02000000 and p+n<=0x02040000 and p%4==0 end
local function readFile(path)
  local f=assert(io.open(path,'rb'))
  local data=f:read('a'); assert(f:close()); return data
end
local function persist(directory,blob)
  local digest=M.sha256(blob)
  local path=directory..'/'..hex(digest)..'.history'
  local exists=io.open(path,'rb')
  if exists then
    local old=exists:read('a'); exists:close()
    assert(old==blob,'Existing history snapshot is corrupt')
    return digest
  end
  -- A process crash before rename leaves only an unreferenced temporary file.
  -- Lua flush/close is not a Windows FlushFileBuffers power-loss guarantee.
  local temp=path..'.pending'
  local f=assert(io.open(temp,'wb'))
  assert(f:write(blob)); assert(f:flush()); assert(f:close())
  assert(readFile(temp)==blob,'History write verification failed')
  assert(os.rename(temp,path))
  return digest
end
local function validSnapshot(blob,identity)
  assert(#blob==16928,'History length mismatch')
  assert(blob:sub(1,8)=='ECHOMEM1','History magic mismatch')
  local version,voices,contexts=string.unpack('<I2I2I4',blob,9)
  assert(version==1 and voices==11 and contexts==12288,'History format mismatch')
  assert(blob:sub(17,32)==identity,'History belongs to a different game')
end

function M.attach(emu,callbacks,directory)
  assert(type(directory)=='string' and #directory>0,'History directory required')
  local descriptor=nil
  -- Descriptor is ROM data, never an address supplied by a save or a file.
  local size=emu:romSize()
  for offset=0,size-28,65536 do
    local bytes=emu:readRange(0x08000000+offset,math.min(65536+27,size-offset))
    local pos=bytes:find('ECHOBRD1',1,true)
    while pos do
      if (offset+pos-1)%4==0 and pos+27<=#bytes then
        local version,mailbox,snapshot,length,frame=string.unpack('<I4I4I4I4I4',bytes,pos+8)
        if version==1 and length==16928 and inRam(mailbox,92) and inRam(snapshot,length)
          and inRam(frame,4) and (mailbox+92<=snapshot or snapshot+length<=mailbox) then
          assert(descriptor==nil or descriptor.address==offset+pos-1,'Ambiguous history descriptor')
          descriptor={address=offset+pos-1,mailbox=mailbox,snapshot=snapshot,frame=frame}
        end
      end
      pos=bytes:find('ECHOBRD1',pos+1,true)
    end
  end
  assert(descriptor,'This ROM has no supported companion history bridge')
  local b,p=descriptor.mailbox,descriptor.snapshot
  local function writeBytes(address,data)
    for i=1,#data do emu:write8(address+i-1,data:byte(i)) end
  end
  local function frame()
    if emu:read32(b)~=0x314d4345 or emu:read32(b+4)~=1 then return end
    -- Revalidate every request: another ROM or restored state must not turn this
    -- into an arbitrary memory/file writer. Data files never supply addresses.
    if emu:read32(b+20)~=p or emu:read32(b+24)~=16928 then return end
    emu:write32(b+8,(emu:read32(descriptor.frame)+1)&0xffffffff)
    local request=emu:read32(b+12)
    if request==0 or emu:read32(b+16)~=0 then return end
    local ok,err=pcall(function()
      local blob=emu:readRange(p,16928)
      local identity=blob:sub(17,32)
      validSnapshot(blob,identity)
      if request==1 then
        local digest=emu:readRange(b+28,32)
        local loaded=readFile(directory..'/'..hex(digest)..'.history')
        assert(M.sha256(loaded)==digest,'History checksum mismatch')
        validSnapshot(loaded,identity)
        writeBytes(p,loaded)
      elseif request==2 then
        writeBytes(b+60,persist(directory,blob))
      else error('Unsupported history request') end
    end)
    emu:write32(b+16,ok and 1 or 2) -- Acknowledge only after all IO/validation.
    if not ok and console then console:error('Companion history: '..tostring(err)) end
  end
  callbacks:add('frame',frame)
  return frame
end
return M
