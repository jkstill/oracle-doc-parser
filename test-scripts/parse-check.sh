#!/usr/bin/env bash

python3 -c "
from bs4 import BeautifulSoup
from pathlib import Path
import sys

# Change this to any view page from your docs
p = Path('/mnt/zips/zips/oracle/oracle_docs/19c-all-docs/oracle-database_19_20230703/content/refrn/DBA_CHANGE_NOTIFICATION_REGS.html')
soup = BeautifulSoup(p.read_text(encoding='utf-8', errors='ignore'), 'lxml')

print('=== TITLE ===')
print(soup.title.get_text() if soup.title else 'none')

print()
print('=== ALL DIV CLASSES ===')
divs = soup.find_all('div', class_=True)
classes = sorted(set(c for d in divs for c in d.get('class', [])))
print(classes)

print()
print('=== HEADINGS (first 15) ===')
for h in soup.find_all(['h1','h2','h3','h4','h5'])[:15]:
    cls = h.get('class', [])
    print(f'  <{h.name} class={cls}>: {h.get_text(strip=True)[:80]}')

print()
print('=== TABLES (first 3) ===')
for i, tbl in enumerate(soup.find_all('table')[:3]):
    cls = tbl.get('class', [])
    print(f'  Table {i} class={cls}')
    for row in tbl.find_all('tr')[:4]:
        cells = [td.get_text(strip=True)[:30] for td in row.find_all(['th','td'])]
        print(f'    {cells}')

print()
print('=== FIRST 100 LINES OF BODY HTML ===')
body = soup.find('body')
if body:
    lines = body.decode_contents().splitlines()
    for line in lines[:100]:
        if line.strip():
            print(line)
"

