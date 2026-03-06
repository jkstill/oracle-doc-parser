---
id: 19c__V$DATAFILE
name: V$DATAFILE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-DATAFILE.html
---

# V$DATAFILE

V$DATAFILE displays datafile information from the control file.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FILE# | NUMBER |  |
| CREATION_CHANGE# | NUMBER |  |
| CREATION_TIME | DATE |  |
| TS# | NUMBER |  |
| RFILE# | NUMBER |  |
| STATUS | VARCHAR2(7) |  |
| ENABLED | VARCHAR2(10) |  |
| CHECKPOINT_CHANGE# | NUMBER |  |
| CHECKPOINT_TIME | DATE |  |
| UNRECOVERABLE_CHANGE# | NUMBER |  |
| UNRECOVERABLE_TIME | DATE |  |
| LAST_CHANGE# | NUMBER |  |
| LAST_TIME | DATE |  |
| OFFLINE_CHANGE# | NUMBER |  |
| ONLINE_CHANGE# | NUMBER |  |
| ONLINE_TIME | DATE |  |
| BYTES | NUMBER |  |
| BLOCKS | NUMBER |  |
| CREATE_BYTES | NUMBER |  |
| BLOCK_SIZE | NUMBER |  |
| NAME | VARCHAR2(513) |  |
| PLUGGED_IN | NUMBER |  |
| BLOCK1_OFFSET | NUMBER |  |
| AUX_NAME | VARCHAR2(513) |  |
| FIRST_NONLOGGED_SCN | NUMBER |  |
| FIRST_NONLOGGED_TIME | DATE |  |
| FOREIGN_DBID | NUMBER |  |
| FOREIGN_CREATION_CHANGE# | NUMBER |  |
| FOREIGN_CREATION_TIME | DATE |  |
| PLUGGED_READONLY | VARCHAR2(3) |  |
| PLUGIN_CHANGE# | NUMBER |  |
| PLUGIN_RESETLOGS_CHANGE# | NUMBER |  |
| PLUGIN_RESETLOGS_TIME | DATE |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: " V$DATAFILE_HEADER " , which displays information from data file headers See Also: " V$DATAFILE_HEADER " , which displays information from data file headers