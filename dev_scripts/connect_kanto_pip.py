from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
def main():
 count=0
 for p in (ROOT/'data/kanto').rglob('*.inc'):
  s=p.read_text(encoding='utf-8');s,n=re.subn(r'(\trelease\n)(\tend\b)',r'\1\tcall Pip_EventScript_NPCReaction\n\2',s);count+=n
  if n:p.write_text(s,encoding='utf-8',newline='\n')
 print('Connected',count,'scripted NPC conversation endings to optional remembered Pip reactions')
if __name__=='__main__':main()
