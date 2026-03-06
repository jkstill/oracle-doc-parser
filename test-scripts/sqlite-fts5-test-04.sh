#!/usr/bin/env bash

python3 -c "
from bs4 import BeautifulSoup
from pathlib import Path

p = list(Path('/mnt/zips/zips/oracle/oracle_docs/19c-all-docs/oracle-database_19_20230703/content/refrn').rglob('DBA_TABLES.html'))[0]
soup = BeautifulSoup(p.read_text(encoding='utf-8', errors='ignore'), 'lxml')

print('Tables found:', len(soup.find_all('table')))
for i, tbl in enumerate(soup.find_all('table')):
    cls = tbl.get('class', [])
    headers = [th.get_text(strip=True) for th in tbl.find_all('th')]
    print(f'  Table {i}: class={cls} headers={headers[:4]}')
"


