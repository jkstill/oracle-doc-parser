---
id: 19c__V$GCSPFMASTER_INFO
name: V$GCSPFMASTER_INFO
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-GCSPFMASTER_INFO.html
---

# V$GCSPFMASTER_INFO

V$GCSPFMASTER_INFO describes the current and previous master instances and the number of re-masterings of Global Cache Service resources belonging to files mapped to instances.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FILE_ID | NUMBER |  |
| DATA_OBJECT_ID | NUMBER |  |
| GC_MASTERING_POLICY | VARCHAR2(11) |  |
| CURRENT_MASTER | NUMBER |  |
| PREVIOUS_MASTER | NUMBER |  |
| REMASTER_CNT | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content