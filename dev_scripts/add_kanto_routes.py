from pathlib import Path
import json,textwrap
ROOT=Path(__file__).resolve().parents[1]
ROUTES='''2|The forest has two entrances. My sense of direction has neither.|That tree is doing an excellent job of being in the way.
3|A hike toward a mountain. The route name left out the uphill part.|Everybody packed for adventure. I hope somebody packed lunch.
4|Those ledges are very certain about which way we should go.|We left a mountain and found more rocks. They are following us.
5|A daycare and an underpass. Two good places to avoid a schedule.|The path is narrow, but my complaints travel single file.
6|That pond looks restful. I am trying not to envy a pond.|We are nearly at the harbor. My legs have filed the paperwork.
7|A short road between big cities. An excellent place to catch a breath.|The underpass is a useful invention. It avoids so many conversations.
8|Everyone is walking toward something. I am currently walking toward dinner.|A gate, a road, and people with opinions. Travel is consistent.
9|The rocks make this route interesting. I had requested boring.|If we take another turn, please tell my knees in advance.
10|A power plant by the water. Do the engineers worry about that?|The tunnel entrance is dark. It is making a very clear first impression.
11|Lots of trainers here. None of them has challenged me to a picnic.|I like routes with a view. The view asks fewer questions.
12|Fishing requires patience. I brought the snack component of patience.|A bridge over quiet water. We can stand here for a minute.
13|The fences make a maze. Somebody landscaped this with intent.|A bird flew over every turn. It has found an unfair shortcut.
14|The birds seem comfortable. I would also like portable seating.|A long road is better with company. Even company that needs a rest.
15|Nearly at FUCHSIA. Please let there be a bench with no entry fee.|I have counted enough bird calls to start recognizing complaints.
16|A bicycle route. My walking shoes feel underappreciated.|That downhill sign is promising. The return journey is withholding comment.
17|This hill is doing most of the cycling. I appreciate its contribution.|Please brake before admiring the scenery. In that order.
18|We made it down the hill. I was very brave about the handlebars.|A city ahead. I can hear my feet cheering quietly.
19|Sand, sea, and wet socks. Two out of three are pleasant.|The swimmers look relaxed. I am negotiating with a wave.
20|An island between two stretches of sea. A well-placed breather.|The ocean keeps going. I admire its stamina.
21|The coast looks familiar from a different direction. That helps.|Water on both sides. The route is very committed to the theme.
22|The League is that way. I am practicing an encouraging expression.|We can train a little more if you want. I am coming either way.
23|Every gate asks for a badge. Nobody has asked to see my snack permit.|One more road. We have done so many roads. We can do this one.
24|Five trainers on a bridge. Someone organized a queue for battling.|A golden prize for crossing. My usual prize is more road.
25|A quiet cape and a house at the end. A good place to stop running.|People come here on dates. We came here with a backpack full of medicine.'''
def main():
 sections={s['id'] for s in json.loads((ROOT/'src/data/region_map/region_map_sections.json').read_text())['map_sections']};rows={v[0]:v[1:] for l in ROUTES.splitlines() if (v:=l.split('|')) and 'MAPSEC_ROUTE_'+v[0] in sections};lines=['// Route-specific Kanto observations, append-only.'];entries=[]
 for route,comments in rows.items():
  for j,t in enumerate(comments):
   name='sPipKantoRoute_'+route+'_'+str(j);entries.append(name);parts=textwrap.wrap('PIP: '+t,33);text=parts[0]+''.join(('\\n' if k==1 else '\\l')+x for k,x in enumerate(parts[1:],1))+'$';lines.append('static const u8 '+name+'[] = _("'+text+'");')
 lines+=['static const struct PipLocationDialogue sPipKantoRoutes[] = {']
 for r in rows:lines.append('    {MAPSEC_ROUTE_'+r+', {sPipKantoRoute_'+r+'_0, sPipKantoRoute_'+r+'_1}},')
 lines+=['};'];(ROOT/'src/data/pip_kanto_routes.h').write_text('\n'.join(lines)+'\n',newline='\n')
 p=ROOT/'src/data/pip_memory_catalogue.h';s=p.read_text();idx=s.index('\n};',s.index('sPipMemoryCatalogue[]'));s=s[:idx]+''.join('\n    '+name+', // '+str(356+i) for i,name in enumerate(entries))+s[idx:];p.write_text(s,newline='\n')
 p=ROOT/'src/pip.c';s=p.read_text().replace('#include "data/pip_memory_catalogue.h"','#include "data/pip_kanto_routes.h"\n#include "data/pip_memory_catalogue.h"');a=s.index('static const u8 *FreshKantoLocation(void)');b=s.index('static const u8 *FreshLocation(void)',a);chunk=s[a:b];chunk=chunk.replace('    return NULL;','''    for (u32 i = 0; i < ARRAY_COUNT(sPipKantoRoutes); i++)
        if (sPipKantoRoutes[i].section == gMapHeader.regionMapSectionId)
            for (u32 j = 0; j < 2; j++)
                if (Fresh(sPipKantoRoutes[i].lines[j]) != NULL)
                    return sPipKantoRoutes[i].lines[j];
    return NULL;''');s=s[:a]+chunk+s[b:];p.write_text(s,newline='\n');print('Added',len(entries),'comments for',len(rows),'routes')
if __name__=='__main__':main()
