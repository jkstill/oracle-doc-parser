---
id: 19c__V$LOADISTAT
name: V$LOADISTAT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-LOADISTAT.html
---

# V$LOADISTAT

V$LOADISTAT contains errors that occurred when updating indexes on a table during a load using the Direct Path API.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(31) |  |
| TABNAME | VARCHAR2(31) |  |
| INDEXNAME | VARCHAR2(31) |  |
| SUBNAME | VARCHAR2(31) |  |
| MESSAGE_NUM | NUMBER |  |
| MESSAGE | VARCHAR2(4000) |  |
| CON_ID | NUMBER |  |