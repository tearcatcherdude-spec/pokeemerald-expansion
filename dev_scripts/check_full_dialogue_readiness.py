"""Keep the full-expansion release distinct from successful partial build checks.

Inventory reachability and compiled labels are not reviewed final-message
coverage. Review dispositions must be explicit; missing decisions stay gaps.
This checks content review only, not native testing or literary quality.
"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / 'data/companion_dialogue/full_game'


def assess():
    messages = json.loads((INVENTORY / 'message_worklist.json').read_text(encoding='utf-8'))
    roots = json.loads((INVENTORY / 'interaction_roots.json').read_text(encoding='utf-8'))
    hooks = json.loads((INVENTORY / 'native_hook_worklist.json').read_text(encoding='utf-8'))
    catalogue = json.loads((ROOT / 'data/companion_dialogue/contexts.json').read_text(encoding='utf-8'))
    bindings = {label for row in catalogue['contexts'] for label in row['sources']}
    reviewed = {'eligible_final_message', 'excluded_with_reason'}
    unreviewed = [row['label'] for row in messages
                  if row.get('final_message_eligibility') not in reviewed or not row.get('review_note')]
    missing = [row['label'] for row in messages
               if row.get('final_message_eligibility') == 'eligible_final_message' and row['label'] not in bindings]
    unreviewed_roots = [row['script'] for row in roots
                        if row.get('review_status') != 'reviewed' or not row.get('terminal_messages_reviewed')
                        or not row.get('review_note')]
    unreviewed_hooks = [row['function'] for row in hooks
                        if row.get('review_status') != 'reviewed' or not row.get('review_note')]
    incomplete_voices = [row['key'] for row in catalogue['contexts']
                         if [reply['voice'] for reply in row['replies']] != catalogue['voices']]
    gaps = dict(unreviewed_message_labels=unreviewed,
                reviewed_eligible_labels_without_binding=missing,
                unreviewed_interaction_roots=unreviewed_roots,
                unreviewed_native_hooks=unreviewed_hooks,
                incomplete_voice_sets=incomplete_voices)
    return dict(content_ready=not any(gaps.values()),
                scope='Whole Hoenn/Kanto conservative source worklist; decisions and exact final bindings required.',
                authored_contexts=sum(not row.get('retired') for row in catalogue['contexts']),
                reserved_context_ids=len(catalogue['contexts']),
                authored_replies=sum(len(row['replies']) for row in catalogue['contexts'] if not row.get('retired')),
                inventory_labels=len(messages),
                bound_labels_in_inventory=sum(row['label'] in bindings for row in messages),
                gaps={key:dict(count=len(values),examples=values[:12]) for key,values in gaps.items()},
                caveat='A content-ready result would still require final native tests, build checks and review. Unreviewed inventory labels are not all required response contexts.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report-only', action='store_true', help='Report gaps without failing a development build')
    args = parser.parse_args()
    result = assess()
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result['content_ready'] or args.report_only else 1)
