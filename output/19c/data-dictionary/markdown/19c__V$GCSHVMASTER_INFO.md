---
id: 19c__V$GCSHVMASTER_INFO
name: V$GCSHVMASTER_INFO
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-GCSHVMASTER_INFO.html
---

# V$GCSHVMASTER_INFO

V$GCSHVMASTER_INFO describes the current and previous master instances and the number of re-masterings of Global Cache Service resources except those belonging to files mapped to a particular master.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| HV_ID | NUMBER |  |
| CURRENT_MASTER | NUMBER |  |
| PREVIOUS_MASTER | NUMBER |  |
| REMASTER_CNT | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content