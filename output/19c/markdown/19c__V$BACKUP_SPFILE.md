---
id: 19c__V$BACKUP_SPFILE
name: V$BACKUP_SPFILE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-BACKUP_SPFILE.html
---

# V$BACKUP_SPFILE

V$BACKUP_SPFILE displays information about server parameter files in backup sets from the control file.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| RECID | NUMBER |  |
| STAMP | NUMBER |  |
| SET_STAMP | NUMBER |  |
| SET_COUNT | NUMBER |  |
| MODIFICATION_TIME | DATE |  |
| BYTES | NUMBER |  |
| COMPLETION_TIME | DATE |  |
| DB_UNIQUE_NAME | VARCHAR2(30) |  |
| CON_ID | NUMBER |  |
| GUID | RAW(16) |  |