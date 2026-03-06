---
id: 19c__V$LOADPSTAT
name: V$LOADPSTAT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-LOADPSTAT.html
---

# V$LOADPSTAT

V$LOADPSTAT contains statistics about the number of rows loaded into a partition, or subpartition, during a load using the Direct Path API.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(31) |  |
| TABNAME | VARCHAR2(31) |  |
| PARTNAME | VARCHAR2(31) |  |
| LOADED | NUMBER |  |
| CON_ID | NUMBER |  |