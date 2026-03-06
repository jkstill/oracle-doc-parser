---
id: 19c__V$SQL_CS_SELECTIVITY
name: V$SQL_CS_SELECTIVITY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dynamic_performance]
source_file: V-SQL_CS_SELECTIVITY.html
---

# V$SQL_CS_SELECTIVITY

Address of the handle to the parent for this cursor

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ADDRESS | RAW(4 | 8) |  |
| HASH_VALUE | NUMBER |  |
| SQL_ID | VARCHAR2(13) |  |
| CHILD_NUMBER | NUMBER |  |
| PREDICATE | VARCHAR2(40) |  |
| RANGE_ID | NUMBER |  |
| LOW | VARCHAR2(10) |  |
| HIGH | VARCHAR2(10) |  |
| CON_ID | NUMBER |  |