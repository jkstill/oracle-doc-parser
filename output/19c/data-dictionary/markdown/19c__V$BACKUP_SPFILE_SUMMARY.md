---
id: 19c__V$BACKUP_SPFILE_SUMMARY
name: V$BACKUP_SPFILE_SUMMARY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-BACKUP_SPFILE_SUMMARY.html
---

# V$BACKUP_SPFILE_SUMMARY

V$BACKUP_SPFILE_SUMMARY provides summary information for input SP file, based on either a backup job or time range applicable to jobs.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| NUM_FILES_BACKED | NUMBER |  |
| NUM_DISTINCT_FILES_BACKED | NUMBER |  |
| MIN_MODIFICATION_TIME | DATE |  |
| MAX_MODIFICATION_TIME | DATE |  |
| INPUT_BYTES | NUMBER |  |
| INPUT_BYTES_DISPLAY | VARCHAR2(4000) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content