---
id: 19c__V$BACKUP_SET
name: V$BACKUP_SET
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-BACKUP_SET.html
---

# V$BACKUP_SET

V$BACKUP_SET displays information about backup sets from the control file.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| RECID | NUMBER |  |
| STAMP | NUMBER |  |
| SET_STAMP | NUMBER |  |
| SET_COUNT | NUMBER |  |
| BACKUP_TYPE | VARCHAR2(1) |  |
| CONTROLFILE_INCLUDED | VARCHAR2(3) |  |
| INCREMENTAL_LEVEL | NUMBER |  |
| PIECES | NUMBER |  |
| START_TIME | DATE |  |
| COMPLETION_TIME | DATE |  |
| ELAPSED_SECONDS | NUMBER |  |
| BLOCK_SIZE | NUMBER |  |
| INPUT_FILE_SCAN_ONLY | VARCHAR2(3) |  |
| KEEP | VARCHAR2(3) |  |
| KEEP_UNTIL | DATE |  |
| KEEP_OPTIONS | VARCHAR2(11) |  |
| MULTI_SECTION | VARCHAR2(3) |  |
| FOR_XTTS | VARCHAR2(3) |  |
| SAME_ENDIAN | VARCHAR2(3) |  |
| INC_DMPFILE | VARCHAR2(3) |  |
| CON_ID | NUMBER |  |
| GUID | RAW(16) |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content A backup set record is inserted after the backup set is successfully completed.