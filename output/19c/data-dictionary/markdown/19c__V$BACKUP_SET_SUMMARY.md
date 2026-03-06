---
id: 19c__V$BACKUP_SET_SUMMARY
name: V$BACKUP_SET_SUMMARY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-BACKUP_SET_SUMMARY.html
---

# V$BACKUP_SET_SUMMARY

V$BACKUP_SET_SUMMARY provides summary information for a backup set.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| NUM_BACKUPSETS | NUMBER |  |
| OLDEST_BACKUP_TIME | DATE |  |
| NEWEST_BACKUP_TIME | DATE |  |
| OUTPUT_BYTES | NUMBER |  |
| ORIGINAL_INPUT_BYTES | NUMBER |  |
| ORIGINAL_INPRATE_BYTES | NUMBER |  |
| OUTPUT_RATE_BYTES | NUMBER |  |
| COMPRESSION_RATIO | NUMBER |  |
| ORIGINAL_INPUT_BYTES_DISPLAY | VARCHAR2(4000) |  |
| OUTPUT_BYTES_DISPLAY | VARCHAR2(4000) |  |
| ORIGINAL_INPRATE_BYTES_DISPLAY | VARCHAR2(4000) |  |
| OUTPUT_RATE_BYTES_DISPLAY | VARCHAR2(4000) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content