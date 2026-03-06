---
id: 19c__V$BACKUP_DATAFILE_SUMMARY
name: V$BACKUP_DATAFILE_SUMMARY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-BACKUP_DATAFILE_SUMMARY.html
---

# V$BACKUP_DATAFILE_SUMMARY

V$BACKUP_DATAFILE_SUMMARY provides summary information for a specific criteria set, based on a backup job, a time range applicable to jobs, or a specific data file).

## Columns

| Column | Type | Description |
|--------|------|-------------|
| NUM_FILES_BACKED | NUMBER |  |
| NUM_DISTINCT_FILES_BACKED | NUMBER |  |
| NUM_DISTINCT_TS_BACKED | NUMBER |  |
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