#!/usr/bin/env bash

python3 -c "
import sqlite3
con = sqlite3.connect('output/19c/data-dictionary/oracle_docs.db')

# Verify column_names field is populated
print('=== column_names spot check ===')
rows = con.execute('''
    SELECT name, column_names FROM chunks
    WHERE name IN ('DBA_TABLES', 'DBA_SEGMENTS', 'V\$SESSION', 'DBA_SYS_PRIVS')
''').fetchall()
for name, col_names in rows:
    print(f'  {name}: {col_names[:100]}')

# Check why query 4 misses DBA_TABLES
print()
print('=== DBA_TABLES FTS match test ===')
for term in ['num_rows', 'blocks', 'statistics', 'table']:
    rows = con.execute('''
        SELECT c.name FROM chunks_fts f
        JOIN chunks c ON c.rowid = f.rowid
        WHERE chunks_fts MATCH ? LIMIT 3
    ''', (term,)).fetchall()
    print(f'  {term!r}: {[r[0] for r in rows]}')

# Check query 5 - try simpler terms
print()
print('=== privilege query breakdown ===')
for term in ['privilege', 'grant', 'SYS_PRIVS', 'TAB_PRIVS']:
    rows = con.execute('''
        SELECT c.name FROM chunks_fts f
        JOIN chunks c ON c.rowid = f.rowid
        WHERE chunks_fts MATCH ? LIMIT 3
    ''', (term,)).fetchall()
    print(f'  {term!r}: {[r[0] for r in rows]}')
con.close()
"

