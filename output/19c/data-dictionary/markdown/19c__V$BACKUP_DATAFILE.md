---
id: 19c__V$BACKUP_DATAFILE
name: V$BACKUP_DATAFILE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-BACKUP_DATAFILE.html
---

# V$BACKUP_DATAFILE

V$BACKUP_DATAFILE displays information about control files and data files in backup sets from the control file.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| RECID | NUMBER |  |
| STAMP | NUMBER |  |
| SET_STAMP | NUMBER |  |
| SET_COUNT | NUMBER |  |
| FILE# | NUMBER |  |
| CREATION_CHANGE# | NUMBER |  |
| CREATION_TIME | DATE |  |
| RESETLOGS_CHANGE# | NUMBER |  |
| RESETLOGS_TIME | DATE |  |
| INCREMENTAL_LEVEL | NUMBER |  |
| INCREMENTAL_CHANGE# | NUMBER |  |
| CHECKPOINT_CHANGE# | NUMBER |  |
| CHECKPOINT_TIME | DATE |  |
| ABSOLUTE_FUZZY_CHANGE# | NUMBER |  |
| MARKED_CORRUPT | NUMBER |  |
| MEDIA_CORRUPT | NUMBER |  |
| LOGICALLY_CORRUPT | NUMBER |  |
| DATAFILE_BLOCKS | NUMBER |  |
| BLOCKS | NUMBER |  |
| BLOCK_SIZE | NUMBER |  |
| OLDEST_OFFLINE_RANGE | NUMBER |  |
| COMPLETION_TIME | DATE |  |
| CONTROLFILE_TYPE | VARCHAR2(1) |  |
| USED_CHANGE_TRACKING | VARCHAR2(3) |  |
| BLOCKS_READ | NUMBER |  |
| USED_OPTIMIZATION | VARCHAR2(3) |  |
| FOREIGN_DBID | NUMBER |  |
| PLUGGED_READONLY | VARCHAR2(3) |  |
| PLUGIN_CHANGE# | NUMBER |  |
| PLUGIN_RESETLOGS_CHANGE# | NUMBER |  |
| PLUGIN_RESETLOGS_TIME | DATE |  |
| SECTION_SIZE | NUMBER |  |
| UNDO_OPTIMIZED | VARCHAR2(3) |  |
| BLOCKS_SKIPPED_IN_CELL | NUMBER |  |
| CON_ID | NUMBER |  |
| BACKED_BY_PDB | VARCHAR2(3) |  |
| SPARSE_BACKUP | VARCHAR2(3) |  |
| GUID | RAW(16) |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content