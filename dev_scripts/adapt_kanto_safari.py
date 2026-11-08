from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]
def main():
 source=(ROOT/'data/scripts/safari_zone.inc').read_text();out=[];active=True;stack=[]
 for line in source.splitlines():
  if line=='#if IS_FRLG':stack.append(active);active=active and True
  elif line=='#else' and stack:active=stack[-1] and not active
  elif line=='#endif' and stack:active=stack.pop()
  elif active:out.append(line)
 text='\n'.join(out)+'\n';labels=re.findall(r'^(\w+)::?',text,re.M);renames={l:'Kanto'+l for l in labels}
 renames.update(json.loads((ROOT/'data/kanto/symbol_manifest.json').read_text())['renamed']);renames.update(json.loads((ROOT/'data/kanto/maps_manifest.json').read_text())['map_ids']);pat=re.compile(r'\b(?:'+'|'.join(map(re.escape,sorted(renames,key=len,reverse=True)))+r')\b');text=pat.sub(lambda m:renames[m[0]],text);(ROOT/'data/kanto/safari.inc').write_text(text,newline='\n')
 p=ROOT/'data/event_scripts.s';s=p.read_text();s=s.replace('\t.include "data/kanto/living_scenes.inc"','\t.include "data/kanto/living_scenes.inc"\n\t.include "data/kanto/safari.inc"');p.write_text(s,newline='\n')
 p=ROOT/'src/safari_zone.c';s=p.read_text().replace('#include "global.h"','#include "global.h"\n#include "parallel_watch.h"');names=['TimesUp','RetirePrompt','OutOfBallsMidBattle','OutOfBalls'];declarations='\n#if !IS_FRLG\n'+''.join('extern const u8 KantoSafariZone_EventScript_'+n+'[];\n' for n in names)+'''#endif
static bool32 IsKantoSafari(void)
{
    return IS_FRLG || ParallelWatch_IsKanto(gSaveBlock1Ptr->location.mapGroup, gSaveBlock1Ptr->location.mapNum);
}
''';marker='EWRAM_DATA u8 gNumSafariBalls';s=s.replace(marker,declarations+'\n'+marker);s=s.replace('if (IS_FRLG)\n        gSafariZoneStepCounter','if (IsKantoSafari())\n        gSafariZoneStepCounter')
 for n in names:
  old='SafariZone_EventScript_'+n
  for call in ['ScriptContext_SetupScript','RunScriptImmediately']:
   s=s.replace(call+'('+old+');','#if !IS_FRLG\n        '+call+'(IsKantoSafari() ? Kanto'+old+' : '+old+');\n#else\n        '+call+'('+old+');\n#endif')
 p.write_text(s,newline='\n');print('Added regional Safari entry, timeout, retire and out-of-balls paths')
if __name__=='__main__':main()
