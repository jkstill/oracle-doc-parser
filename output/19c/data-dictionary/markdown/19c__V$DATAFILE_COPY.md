---
id: 19c__V$DATAFILE_COPY
name: V$DATAFILE_COPY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-DATAFILE_COPY.html
---

# V$DATAFILE_COPY

V$DATAFILE_COPY displays data file copy information from the control file.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| RECID | NUMBER |  |
| STAMP | NUMBER |  |
| NAME | VARCHAR2(513) |  |
| TAG | VARCHAR2(32) |  |
| FILE# | NUMBER |  |
| RFILE# | NUMBER |  |
| CREATION_CHANGE# | NUMBER |  |
| CREATION_TIME | DATE |  |
| RESETLOGS_CHANGE# | NUMBER |  |
| RESETLOGS_TIME | DATE |  |
| INCREMENTAL_LEVEL | NUMBER |  |
| CHECKPOINT_CHANGE# | NUMBER |  |
| CHECKPOINT_TIME | DATE |  |
| ABSOLUTE_FUZZY_CHANGE# | NUMBER |  |
| RECOVERY_FUZZY_CHANGE# | NUMBER |  |
| RECOVERY_FUZZY_TIME | DATE |  |
| ONLINE_FUZZY | VARCHAR2(3) |  |
| BACKUP_FUZZY | VARCHAR2(3) |  |
| MARKED_CORRUPT | NUMBER |  |
| MEDIA_CORRUPT | NUMBER |  |
| LOGICALLY_CORRUPT | NUMBER |  |
| BLOCKS | NUMBER |  |
| BLOCK_SIZE | NUMBER |  |
| OLDEST_OFFLINE_RANGE | NUMBER |  |
| DELETED | VARCHAR2(3) |  |
| STATUS | VARCHAR2(1) |  |
| COMPLETION_TIME | DATE |  |
| CONTROLFILE_TYPE | VARCHAR2(1) |  |
| KEEP | VARCHAR2(3) |  |
| KEEP_UNTIL | DATE |  |
| KEEP_OPTIONS | VARCHAR2(11) |  |
| SCANNED | VARCHAR2(3) |  |
| IS_RECOVERY_DEST_FILE | VARCHAR2(3) |  |
| RMAN_STATUS_RECID | NUMBER |  |
| RMAN_STATUS_STAMP | NUMBER |  |
| CONVERTED_FILE | VARCHAR2(3) |  |
| SAME_ENDIAN | VARCHAR2(3) |  |
| FOREIGN_DBID | NUMBER |  |
| PLUGGED_READONLY | VARCHAR2(3) |  |
| PLUGIN_CHANGE# | NUMBER |  |
| PLUGIN_RESETLOGS_CHANGE# | NUMBER |  |
| PLUGIN_RESETLOGS_TIME | DATE |  |
| BACKED_BY_VSS | VARCHAR2(3) |  |
| CON_ID | NUMBER |  |
| BACKED_BY_PDB | VARCHAR2(3) |  |
| SPARSE_BACKUP | VARCHAR2(3) |  |
| GUID | RAW(16) |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content