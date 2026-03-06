---
id: 19c__V$BACKUP_COPY_SUMMARY
name: V$BACKUP_COPY_SUMMARY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-BACKUP_COPY_SUMMARY.html
---

# V$BACKUP_COPY_SUMMARY

V$BACKUP_COPY_SUMMARY provides summary information for the output data file and control file copy.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| NUM_COPIES | NUMBER |  |
| NUM_DISTINCT_COPIES | NUMBER |  |
| MIN_CHECKPOINT_CHANGE# | NUMBER |  |
| MAX_CHECKPOINT_CHANGE# | NUMBER |  |
| MIN_CHECKPOINT_TIME | DATE |  |
| MAX_CHECKPOINT_TIME | DATE |  |
| OUTPUT_BYTES | NUMBER |  |
| OUTPUT_BYTES_DISPLAY | VARCHAR2(4000) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content