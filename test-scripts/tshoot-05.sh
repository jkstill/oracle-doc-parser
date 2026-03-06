#!/usr/bin/env bash

python3 -c "
from bs4 import BeautifulSoup
from pathlib import Path
import json

docs_path = Path('/mnt/zips/zips/oracle/oracle_docs/19c-all-docs/oracle-database_19_20230703/content/refrn')

no_col = []
with open('output/19c/oracle_docs.jsonl') as f:
    for line in f:
        obj = json.loads(line)
        if obj['object_type'] == 'data_dictionary_view' and not obj['columns']:
            no_col.append((obj['name'], obj['source_file']))

for name, source_file in no_col:
    candidates = list(docs_path.rglob(source_file))
    if not candidates:
        continue
    soup = BeautifulSoup(candidates[0].read_text(encoding='utf-8', errors='ignore'), 'lxml')
    if soup.find('table', class_='Formal') and not soup.find('table', class_='FormalWide'):
        tbl = soup.find('table', class_='Formal')
        headers = [th.get_text(strip=True) for th in tbl.find_all('th')]
        first_rows = tbl.find_all('tr')[1:3]
        print(f'=== {name} ===')
        print(f'  headers: {headers}')
        for tr in first_rows:
            cells = [td.get_text(strip=True)[:40] for td in tr.find_all('td')]
            print(f'  row: {cells}')
        print()
" 2>&1 | head -80

