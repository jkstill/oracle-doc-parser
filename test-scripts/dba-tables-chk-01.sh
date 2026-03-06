#!/usr/bin/env bash

python3 -c "
from bs4 import BeautifulSoup
from pathlib import Path

p = list(Path('/mnt/zips/zips/oracle/oracle_docs/19c-all-docs/oracle-database_19_20230703/content/refrn').rglob('DBA_TABLES.html'))[0]
soup = BeautifulSoup(p.read_text(encoding='utf-8', errors='ignore'), 'lxml')

# Show full text content
ind = soup.find('div', class_='ind')
if ind:
    print('=== TEXT CONTENT ===')
    print(ind.get_text()[:1000])

print()
print('=== ALL LINKS ===')
for a in soup.find_all('a', href=True)[:20]:
    href = a.get('href','')
    if '.html' in href or '.htm' in href:
        print(f'  {href}')
"

