---
id: 19c__V$PROXY_DATAFILE
name: V$PROXY_DATAFILE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-PROXY_DATAFILE.html
---

# V$PROXY_DATAFILE

RECID

## Columns

| Column | Type | Description |
|--------|------|-------------|
| RECID | NUMBER |  |
| STAMP | NUMBER |  |
| DEVICE_TYPE | VARCHAR2(17) |  |
| HANDLE | VARCHAR2(513) |  |
| COMMENTS | VARCHAR2(81) |  |
| MEDIA | VARCHAR2(65) |  |
| MEDIA_POOL | NUMBER |  |
| TAG | VARCHAR2(32) |  |
| STATUS | VARCHAR2(1) |  |
| DELETED | VARCHAR2(3) |  |
| FILE# | NUMBER |  |
| CREATION_CHANGE# | NUMBER |  |
| CREATION_TIME | DATE |  |
| RESETLOGS_CHANGE# | NUMBER |  |
| RESETLOGS_TIME | DATE |  |
| CHECKPOINT_CHANGE# | NUMBER |  |
| CHECKPOINT_TIME | DATE |  |
| ABSOLUTE_FUZZY_CHANGE# | NUMBER |  |
| RECOVERY_FUZZY_CHANGE# | NUMBER |  |
| RECOVERY_FUZZY_TIME | DATE |  |
| INCREMENTAL_LEVEL | NUMBER |  |
| ONLINE_FUZZY | VARCHAR2(3) |  |
| BACKUP_FUZZY | VARCHAR2(3) |  |
| BLOCKS | NUMBER |  |
| BLOCK_SIZE | NUMBER |  |
| OLDEST_OFFLINE_RANGE | NUMBER |  |
| START_TIME | DATE |  |
| COMPLETION_TIME | DATE |  |
| ELAPSED_SECONDS | NUMBER |  |
| CONTROLFILE_TYPE | VARCHAR2(1) |  |
| KEEP | VARCHAR2(3) |  |
| KEEP_UNTIL | DATE |  |
| KEEP_OPTIONS | VARCHAR2(11) |  |
| RMAN_STATUS_RECID | NUMBER |  |
| RMAN_STATUS_STAMP | NUMBER |  |
| FOREIGN_DBID | NUMBER |  |
| PLUGGED_READONLY | VARCHAR2(3) |  |
| PLUGIN_CHANGE# | NUMBER |  |
| PLUGIN_RESETLOGS_CHANGE# | NUMBER |  |
| PLUGIN_RESETLOGS_TIME | DATE |  |
| CON_ID | NUMBER |  |
| BACKED_BY_PDB | VARCHAR2(3) |  |
| GUID | RAW(16) |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content