#!/usr/bin/env bash


python3 -c "
from bs4 import BeautifulSoup
from pathlib import Path

arpls = Path('/mnt/zips/zips/oracle/oracle_docs/19c-all-docs/oracle-database_19_20230703/content/arpls')
files = sorted(arpls.glob('*.html'))
print(f'Found {len(files)} html files')
print(f'First few: {[f.name for f in files[:5]]}')
print()

# Skip index/toc/preface -- find first real package page
for p in files:
    if any(x in p.name for x in ['index', 'toc', 'preface', 'release', 'introduction']):
        continue
    print(f'Inspecting: {p.name}')
    soup = BeautifulSoup(p.read_text(encoding='utf-8', errors='ignore'), 'lxml')

    print('=== TITLE ===')
    print(soup.title.get_text().strip() if soup.title else 'none')

    print()
    print('=== ALL DIV CLASSES ===')
    divs = soup.find_all('div', class_=True)
    classes = sorted(set(c for d in divs for c in d.get('class', [])))
    print(classes)

    print()
    print('=== HEADINGS (first 20) ===')
    for h in soup.find_all(['h1','h2','h3','h4','h5'])[:20]:
        cls = h.get('class', [])
        print(f'  <{h.name} class={cls}>: {h.get_text(strip=True)[:80]}')

    print()
    print('=== TABLES (first 2) ===')
    for i, tbl in enumerate(soup.find_all('table')[:2]):
        cls = tbl.get('class', [])
        print(f'  Table {i} class={cls}')
        for row in tbl.find_all('tr')[:4]:
            cells = [td.get_text(strip=True)[:40] for td in row.find_all(['th','td'])]
            print(f'    {cells}')

    print()
    print('=== FIRST 120 LINES OF BODY HTML ===')
    body = soup.find('body')
    if body:
        lines = body.decode_contents().splitlines()
        for line in lines[:120]:
            if line.strip():
                print(line)
    break  # just the first matching file
"


