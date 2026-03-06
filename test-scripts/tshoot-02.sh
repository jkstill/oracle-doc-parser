#!/usr/bin/env bash


python3 -c "
from bs4 import BeautifulSoup
from pathlib import Path

for name in ['ALL_HISTOGRAMS', 'ALL_JOBS']:
    candidates = list(Path('/mnt/zips/zips/oracle/oracle_docs/19c-all-docs/oracle-database_19_20230703/content/refrn').rglob(f'{name}.html'))
    if not candidates:
        print(f'{name}: file not found')
        continue
    soup = BeautifulSoup(candidates[0].read_text(encoding='utf-8', errors='ignore'), 'lxml')
    ind = soup.find('div', class_='ind')
    if ind:
        # Print all text content - should reveal a 'see also' reference
        print(f'=== {name} ===')
        for p in ind.find_all('p')[:5]:
            print(' ', p.get_text(strip=True)[:120])
    print()
"

