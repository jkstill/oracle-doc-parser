---
id: 19c__V$RESTORE_POINT
name: V$RESTORE_POINT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-RESTORE_POINT.html
---

# V$RESTORE_POINT

V$RESTORE_POINT displays information about restore points.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SCN | NUMBER |  |
| DATABASE_INCARNATION# | NUMBER |  |
| GUARANTEE_FLASHBACK_DATABASE | VARCHAR2(3) |  |
| STORAGE_SIZE | NUMBER |  |
| TIME | TIMESTAMP(9) |  |
| RESTORE_POINT_TIME | TIMESTAMP(9) |  |
| PRESERVED | VARCHAR2(3) |  |
| NAME | VARCHAR2(128) |  |
| PDB_RESTORE_POINT | VARCHAR2(3) |  |
| CLEAN_PDB_RESTORE_POINT | VARCHAR2(3) |  |
| PDB_INCARNATION# | NUMBER |  |
| REPLICATED Foot 1 | VARCHAR2(3) |  |
| CON_ID | NUMBER |  |