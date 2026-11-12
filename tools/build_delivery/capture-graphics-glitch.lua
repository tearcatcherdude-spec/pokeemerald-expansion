-- Load this once in Tools > Scripting while the graphics fault is visible.
-- Writes a diagnostic screenshot/state beside the game; never overwrites .sav.
assert(emu, 'Open the game with the glitch visible first.')
local filename = debug.getinfo(1, 'S').source:sub(2):gsub('\\', '/')
local folder = assert(filename:match('^(.*)/'))
local base = folder .. '/graphics-diagnostics/glitch-' .. os.date('!%Y%m%d-%H%M%S')
local number, stem = 0, base
while true do
    local existing = io.open(stem .. '.ss0', 'rb')
    if not existing then break end
    existing:close()
    number = number + 1
    stem = base .. '-' .. number
end
emu:screenshot(stem .. '.png')
assert(emu:saveStateFile(stem .. '.ss0', 31), 'Could not capture diagnostic state.')
local info = assert(io.open(stem .. '.txt', 'w'))
info:write('Graphics diagnostic; ROM bytes: ' .. emu:romSize() .. '\n')
info:write('This is an emulator diagnostic, not a replacement normal save.\n')
info:close()
console:log('Captured the graphics fault in: ' .. stem)
