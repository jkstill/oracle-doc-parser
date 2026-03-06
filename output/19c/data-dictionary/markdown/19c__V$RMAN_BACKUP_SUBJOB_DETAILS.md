---
id: 19c__V$RMAN_BACKUP_SUBJOB_DETAILS
name: V$RMAN_BACKUP_SUBJOB_DETAILS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-RMAN_BACKUP_SUBJOB_DETAILS.html
---

# V$RMAN_BACKUP_SUBJOB_DETAILS

SESSION_KEY

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SESSION_KEY | NUMBER |  |
| SESSION_RECID | NUMBER |  |
| SESSION_STAMP | NUMBER |  |
| OPERATION | VARCHAR2(33) |  |
| COMMAND_ID | VARCHAR2(33) |  |
| START_TIME | DATE |  |
| END_TIME | DATE |  |
| INPUT_BYTES | NUMBER |  |
| OUTPUT_BYTES | NUMBER |  |
| STATUS_WEIGHT | NUMBER |  |
| OBJECT_TYPE_WEIGHT | NUMBER |  |
| OPTIMIZED_WEIGHT | NUMBER |  |
| OUTPUT_DEVICE_TYPE | VARCHAR2(17) |  |
| BACKED_BY_OSB | VARCHAR2(3) |  |
| AUTOBACKUP_DONE | VARCHAR2(3) |  |
| STATUS | VARCHAR2(23) |  |
| INPUT_TYPE | VARCHAR2(13) |  |
| OPTIMIZED | VARCHAR2(3) |  |
| AUTOBACKUP_COUNT | NUMBER |  |
| COMPRESSION_RATIO | NUMBER |  |
| INPUT_BYTES_DISPLAY | VARCHAR2(4000) |  |
| OUTPUT_BYTES_DISPLAY | VARCHAR2(4000) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content