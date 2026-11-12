"""Append Pip's four optional practice teams without rewriting existing trainers."""
from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]
def main():
    levels=[8,18,32,48]
    teams=[['Porygon','Chingling','Voltorb','Smeargle'],['Porygon','Mime Jr.','Rotom','Smeargle'],['Porygon2','Mr. Mime','Rotom','Smeargle'],['Porygon-Z','Mr. Mime','Rotom','Smeargle']]
    p=ROOT/'src/data/trainers_kanto.party';s=p.read_text(encoding='utf-8');prefix=s.split('\n=== TRAINER_KANTO_DATA_PIP_PRACTICE_')[0].rstrip()
    assert prefix.count('=== TRAINER_KANTO_DATA_')==738, 'Review appended trainer IDs before regeneration'
    suffix=''
    for i,(level,team) in enumerate(zip(levels,teams)):
        suffix+=f'\n\n=== TRAINER_KANTO_DATA_PIP_PRACTICE_{i} ===\nName: PIP\nClass: Pkmn Trainer 1\nPic: Cast Pip\nGender: Male\nMusic: Male\nDouble Battle: No\nAI: Check Bad Move / Try To Faint\n\n'
        for species in team:
            suffix+=f'{species}\nLevel: {level}\nIVs: 12 HP / 12 Atk / 12 Def / 12 SpA / 12 SpD / 12 Spe\n'
            if species=='Smeargle':suffix+='- Tackle\n- Growl\n- Sand Attack\n- Helping Hand\n'
            suffix+='\n'
    p.write_text(prefix+suffix.rstrip()+'\n',encoding='utf-8')
    p=ROOT/'include/constants/kanto_progress.h';s=p.read_text();s=re.sub(r'#define KANTO_TRAINER_COUNT \d+','#define KANTO_TRAINER_COUNT 742',s);
    for i in range(4):
        if '#define TRAINER_KANTO_DATA_PIP_PRACTICE_'+str(i) not in s:s=s.replace('\n#endif',f'\n#define TRAINER_KANTO_DATA_PIP_PRACTICE_{i} {738+i}\n#endif')
    p.write_text(s)
    (ROOT/'data/venues/pip_practice.json').write_text(json.dumps(dict(first_trainer_id=738,levels=levels,teams=teams),indent=2)+'\n')
if __name__=='__main__':main()
