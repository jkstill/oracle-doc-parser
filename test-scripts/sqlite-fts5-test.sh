#!/usr/bin/env bash

python3 -c "
import sqlite3

con = sqlite3.connect('output/19c/data-dictionary/oracle_docs.db')

tests = [
    ('segment storage bytes blocks',       'DBA_SEGMENTS'),
    ('redo log sequence archived',          'V\$LOG or V\$ARCHIVED_LOG'),
    ('session wait event time',             'V\$SESSION_WAIT or V\$SESSION'),
    ('table statistics num_rows blocks',    'DBA_TABLES or DBA_TAB_STATISTICS'),
    ('user privilege system object grant',  'DBA_SYS_PRIVS or DBA_TAB_PRIVS'),
]

for query, expected in tests:
    rows = con.execute(
        '''SELECT c.name, c.description
           FROM chunks_fts f
           JOIN chunks c ON c.rowid = f.rowid
           WHERE chunks_fts MATCH ?
           ORDER BY rank LIMIT 3''',
        (query,)
    ).fetchall()
    print(f'Query: {query!r}')
    print(f'Expected near: {expected}')
    for name, desc in rows:
        print(f'  -> {name}: {desc[:80]}')
    print()
con.close()
"

