---
id: 19c__V$SQL_OPTIMIZER_ENV
name: V$SQL_OPTIMIZER_ENV
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dynamic_performance]
source_file: V-SQL_OPTIMIZER_ENV.html
---

# V$SQL_OPTIMIZER_ENV

Address of the parent cursor

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ADDRESS | RAW(4 | 8) |  |
| HASH_VALUE | NUMBER |  |
| SQL_ID | VARCHAR2(13) |  |
| CHILD_ADDRESS | RAW(4 | 8) |  |
| CHILD_NUMBER | NUMBER |  |
| ID | NUMBER |  |
| NAME | VARCHAR2(40) |  |
| ISDEFAULT | VARCHAR2(3) |  |
| VALUE | VARCHAR2(25) |  |
| CON_ID | NUMBER |  |