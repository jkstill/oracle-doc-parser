---
id: 19c__V$TABLESPACE
name: V$TABLESPACE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: storage
tags: [dynamic_performance]
source_file: V-TABLESPACE.html
---

# V$TABLESPACE

V$TABLESPACE displays tablespace information from the control file.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TS# | NUMBER |  |
| NAME | VARCHAR2(30) |  |
| INCLUDED_IN_DATABASE_BACKUP | VARCHAR2(3) |  |
| BIGFILE | VARCHAR2(3) |  |
| FLASHBACK_ON | VARCHAR2(3) |  |
| ENCRYPT_IN_BACKUP | VARCHAR2(3) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content