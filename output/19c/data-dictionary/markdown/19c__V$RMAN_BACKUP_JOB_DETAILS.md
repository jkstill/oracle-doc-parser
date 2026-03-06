---
id: 19c__V$RMAN_BACKUP_JOB_DETAILS
name: V$RMAN_BACKUP_JOB_DETAILS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-RMAN_BACKUP_JOB_DETAILS.html
---

# V$RMAN_BACKUP_JOB_DETAILS

V$RMAN_BACKUP_JOB_DETAILS displays details about backup jobs.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SESSION_KEY | NUMBER |  |
| SESSION_RECID | NUMBER |  |
| SESSION_STAMP | NUMBER |  |
| COMMAND_ID | VARCHAR2(33) |  |
| START_TIME | DATE |  |
| END_TIME | DATE |  |
| INPUT_BYTES | NUMBER |  |
| OUTPUT_BYTES | NUMBER |  |
| STATUS_WEIGHT | NUMBER |  |
| OPTIMIZED_WEIGHT | NUMBER |  |
| OBJECT_TYPE_WEIGHT | NUMBER |  |
| OUTPUT_DEVICE_TYPE | VARCHAR2(17) |  |
| AUTOBACKUP_COUNT | NUMBER |  |
| BACKED_BY_OSB | VARCHAR2(3) |  |
| AUTOBACKUP_DONE | VARCHAR2(3) |  |
| STATUS | VARCHAR2(23) |  |
| INPUT_TYPE | VARCHAR2(13) |  |
| OPTIMIZED | VARCHAR2(3) |  |
| ELAPSED_SECONDS | NUMBER |  |
| COMPRESSION_RATIO | NUMBER |  |
| INPUT_BYTES_PER_SEC | NUMBER |  |
| OUTPUT_BYTES_PER_SEC | NUMBER |  |
| INPUT_BYTES_DISPLAY | VARCHAR2(4000) |  |
| OUTPUT_BYTES_DISPLAY | VARCHAR2(4000) |  |
| INPUT_BYTES_PER_SEC_DISPLAY | VARCHAR2(4000) |  |
| OUTPUT_BYTES_PER_SEC_DISPLAY | VARCHAR2(4000) |  |
| TIME_TAKEN_DISPLAY | VARCHAR2(4000) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content