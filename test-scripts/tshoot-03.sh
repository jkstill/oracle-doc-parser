#!/usr/bin/env bash


python3 -c "
from bs4 import BeautifulSoup
from pathlib import Path
import json

no_col_names = []
with open('output/19c/oracle_docs.jsonl') as f:
    for line in f:
        obj = json.loads(line)
        if obj['object_type'] == 'data_dictionary_view' and not obj['columns']:
            no_col_names.append(obj['name'])

docs_path = Path('/mnt/zips/zips/oracle/oracle_docs/19c-all-docs/oracle-database_19_20230703/content/refrn')
categories = {'synonym': [], 'has_formalwide': [], 'has_other_table': [], 'no_table': [], 'not_found': []}

for name in no_col_names:
    candidates = list(docs_path.rglob(f'{name}.html'))
    if not candidates:
        categories['not_found'].append(name)
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
    print(f'{cat}: {len(items)}')
"

