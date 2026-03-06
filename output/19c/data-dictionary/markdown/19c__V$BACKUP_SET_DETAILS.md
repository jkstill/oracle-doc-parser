---
id: 19c__V$BACKUP_SET_DETAILS
name: V$BACKUP_SET_DETAILS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-BACKUP_SET_DETAILS.html
---

# V$BACKUP_SET_DETAILS

V$BACKUP_SET_DETAILS provides detailed information about the backup set.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SESSION_KEY | NUMBER |  |
| SESSION_RECID | NUMBER |  |
| SESSION_STAMP | NUMBER |  |
| BS_KEY | NUMBER |  |
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
| KEEP | VARCHAR2(3) |  |
| KEEP_UNTIL | DATE |  |
| KEEP_OPTIONS | VARCHAR2(11) |  |
| DEVICE_TYPE | VARCHAR2(17) |  |
| COMPRESSED | VARCHAR2(3) |  |
| NUM_COPIES | NUMBER |  |
| OUTPUT_BYTES | NUMBER |  |
| ORIGINAL_INPUT_BYTES | NUMBER |  |
| COMPRESSION_RATIO | NUMBER |  |
| STATUS | CHAR(1) |  |
| ORIGINAL_INPRATE_BYTES | NUMBER |  |
| OUTPUT_RATE_BYTES | NUMBER |  |
| ORIGINAL_INPUT_BYTES_DISPLAY | VARCHAR2(4000) |  |
| OUTPUT_BYTES_DISPLAY | VARCHAR2(4000) |  |
| ORIGINAL_INPRATE_BYTES_DISPLAY | VARCHAR2(4000) |  |
| OUTPUT_RATE_BYTES_DISPLAY | VARCHAR2(4000) |  |
| TIME_TAKEN_DISPLAY | VARCHAR2(4000) |  |
| ENCRYPTED | VARCHAR2(3) |  |
| BACKED_BY_OSB | VARCHAR2(3) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This view will contain an extra row for each backup session that invokes BACKUP BACKUPSET (that is, creates new copies for the same backup set or copies backup set information from disk to tape). However, the remaining values of other columns belong to the complete backup set. See Also: " V$BACKUP_SET " See Also: " V$BACKUP_SET "