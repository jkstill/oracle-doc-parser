---
id: 19c__V$SQL_CS_HISTOGRAM
name: V$SQL_CS_HISTOGRAM
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dynamic_performance]
source_file: V-SQL_CS_HISTOGRAM.html
---

# V$SQL_CS_HISTOGRAM

Address of the handle to the parent for this cursor

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ADDRESS | RAW(4 | 8) |  |
| HASH_VALUE | NUMBER |  |
| SQL_ID | VARCHAR2(13) |  |
| CHILD_NUMBER | NUMBER |  |
| BUCKET_ID | NUMBER |  |
| COUNT | NUMBER |  |
| CON_ID | NUMBER |  |