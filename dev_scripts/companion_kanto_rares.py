"""Individual companion reactions to the completed Kanto encounter scenes."""
from kanto_rare_content import ROWS as ENCOUNTERS
ROWS=[dict(key='kanto_rare_'+r['species'].lower()+'_caught',
           labels=['KantoRare_'+r['species']+'_CaughtText'],
           subject=r['caught'],replies=r['replies']) for r in ENCOUNTERS]
