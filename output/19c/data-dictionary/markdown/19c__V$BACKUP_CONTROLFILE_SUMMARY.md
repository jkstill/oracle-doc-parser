---
id: 19c__V$BACKUP_CONTROLFILE_SUMMARY
name: V$BACKUP_CONTROLFILE_SUMMARY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-BACKUP_CONTROLFILE_SUMMARY.html
---

# V$BACKUP_CONTROLFILE_SUMMARY

V$BACKUP_CONTROLFILE_SUMMARY provides control file summary information, based on either a backup set of files, image copies, or proxy copies.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| NUM_FILES_BACKED | NUMBER |  |
| NUM_DISTINCT_FILES_BACKED | NUMBER |  |
| MIN_CHECKPOINT_CHANGE# | NUMBER |  |
| MAX_CHECKPOINT_CHANGE# | NUMBER |  |
| MIN_CHECKPOINT_TIME | DATE |  |
| MAX_CHECKPOINT_TIME | DATE |  |
| INPUT_BYTES | NUMBER |  |
| OUTPUT_BYTES | NUMBER |  |
| COMPRESSION_RATIO | NUMBER |  |
| INPUT_BYTES_DISPLAY | VARCHAR2(4000) |  |
| OUTPUT_BYTES_DISPLAY | VARCHAR2(4000) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content