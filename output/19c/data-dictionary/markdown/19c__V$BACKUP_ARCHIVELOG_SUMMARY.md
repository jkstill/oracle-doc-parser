---
id: 19c__V$BACKUP_ARCHIVELOG_SUMMARY
name: V$BACKUP_ARCHIVELOG_SUMMARY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dynamic_performance]
source_file: V-BACKUP_ARCHIVELOG_SUMMARY.html
---

# V$BACKUP_ARCHIVELOG_SUMMARY

V$BACKUP_ARCHIVELOG_SUMMARY provides archive log summary information based on archive logs in the backup set or on proxy copies.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| NUM_FILES_BACKED | NUMBER |  |
| NUM_DISTINCT_FILES_BACKED | NUMBER |  |
| MIN_FIRST_CHANGE# | NUMBER |  |
| MAX_NEXT_CHANGE# | NUMBER |  |
| MIN_FIRST_TIME | DATE |  |
| MAX_NEXT_TIME | DATE |  |
| INPUT_BYTES | NUMBER |  |
| OUTPUT_BYTES | NUMBER |  |
| COMPRESSION_RATIO | NUMBER |  |
| INPUT_BYTES_DISPLAY | VARCHAR2(4000) |  |
| OUTPUT_BYTES_DISPLAY | VARCHAR2(4000) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content