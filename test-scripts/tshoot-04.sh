#!/usr/bin/env bash

python3 -c "
from bs4 import BeautifulSoup
from pathlib import Path
import json

# Use the same path you pass to scraper.py --path
# docs_path = Path('/home/jkstill/ai/doc-parser/docs/19c')  # adjust as needed
docs_path = Path('/mnt/zips/zips/oracle/oracle_docs/19c-all-docs/oracle-database_19_20230703/content/refrn')

no_col_names = []
with open('output/19c/oracle_docs.jsonl') as f:
    for line in f:
        obj = json.loads(line)
        if obj['object_type'] == 'data_dictionary_view' and not obj['columns']:
            no_col_names.append((obj['name'], obj['source_file']))

print(f'Checking {len(no_col_names)} empty-column chunks')

categories = {'synonym': [], 'has_formalwide': [], 'has_other_table': [], 'no_table': [], 'not_found': []}

for name, source_file in no_col_names:
    # Use source_file from the chunk -- we know this path worked during parsing
    candidates = list(docs_path.rglob(source_file))
    if not candidates:
        categories['not_found'].append((name, source_file))
        continue
    soup = BeautifulSoup(candidates[0].read_text(encoding='utf-8', errors='ignore'), 'lxml')
    text = soup.get_text()
    if 'synonym' in text.lower() or 'same as' in text.lower():
        categories['synonym'].append(name)
    elif soup.find('table', class_='FormalWide'):
        categories['has_formalwide'].append(name)
    elif soup.find('table'):
        tbls = soup.find_all('table')
        classes = [str(t.get('class')) for t in tbls]
        categories['has_other_table'].append((name, classes))
    else:
        categories['no_table'].append(name)

for cat, items in categories.items():
    print(f'{len(items):4d}  {cat}')

# Show sample of any that have a FormalWide we missed -- shouldn't happen
if categories['has_formalwide']:
    print('UNEXPECTED - has FormalWide but no columns extracted:')
    for n in categories['has_formalwide'][:5]:
        print(f'  {n}')

# Show table classes for other-table category
if categories['has_other_table']:
    print('Other table classes found:')
    from collections import Counter
    all_classes = [c for _, classes in categories['has_other_table'] for c in classes]
    for cls, count in Counter(all_classes).most_common(10):
        print(f'  {count:4d}  {cls}')
"

