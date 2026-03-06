---
id: 19c__V$BACKUP_REDOLOG
name: V$BACKUP_REDOLOG
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dynamic_performance]
source_file: V-BACKUP_REDOLOG.html
---

# V$BACKUP_REDOLOG

V$BACKUP_REDOLOG displays information about archived logs in backup sets from the control file.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| RECID | NUMBER |  |
| STAMP | NUMBER |  |
| SET_STAMP | NUMBER |  |
| SET_COUNT | NUMBER |  |
| THREAD# | NUMBER |  |
| SEQUENCE# | NUMBER |  |
| RESETLOGS_CHANGE# | NUMBER |  |
| RESETLOGS_TIME | DATE |  |
| FIRST_CHANGE# | NUMBER |  |
| FIRST_TIME | DATE |  |
| NEXT_CHANGE# | NUMBER |  |
| NEXT_TIME | DATE |  |
| BLOCKS | NUMBER |  |
| BLOCK_SIZE | NUMBER |  |
| TERMINAL | VARCHAR2(3) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Note that online redo logs cannot be backed up directly; they must be archived first to disk and then backed up. An archive log backup set can contain one or more archived logs.