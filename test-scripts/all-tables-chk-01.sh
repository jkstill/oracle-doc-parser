#!/usr/bin/env bash


python3 -c "
import sqlite3, json
con = sqlite3.connect('output/19c/data-dictionary/oracle_docs.db')

row = con.execute('''
    SELECT name, description, column_names, columns_json
    FROM chunks WHERE name = 'ALL_TABLES'
''').fetchone()

if row:
    name, desc, col_names, cols_json = row
    cols = json.loads(cols_json)
    print(f'Name: {name}')
    print(f'Description: {desc[:120]}')
    print(f'Column count: {len(cols)}')
    print(f'Column names: {col_names[:200]}')
else:
    print('ALL_TABLES not found')
con.close()
"

