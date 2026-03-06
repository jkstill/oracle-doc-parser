---
id: 19c__V$FOREIGN_ARCHIVED_LOG
name: V$FOREIGN_ARCHIVED_LOG
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dynamic_performance]
source_file: V-FOREIGN_ARCHIVED_LOG.html
---

# V$FOREIGN_ARCHIVED_LOG

V$FOREIGN_ARCHIVED_LOG can be queried on a logical standby database to find out the list of foreign archived logs received by a database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| RECID | NUMBER |  |
| STAMP | NUMBER |  |
| NAME | VARCHAR2(513) |  |
| DEST_ID | NUMBER |  |
| THREAD# | NUMBER |  |
| SEQUENCE# | NUMBER |  |
| RESETLOGS_CHANGE# | NUMBER |  |
| RESETLOGS_TIME | DATE |  |
| RESETLOGS_ID | NUMBER |  |
| FIRST_CHANGE# | NUMBER |  |
| FIRST_TIME | DATE |  |
| NEXT_CHANGE# | NUMBER |  |
| NEXT_TIME | DATE |  |
| BLOCKS | NUMBER |  |
| BLOCK_SIZE | NUMBER |  |
| CREATOR | VARCHAR2(7) |  |
| REGISTRAR | VARCHAR2(7) |  |
| ARCHIVED | VARCHAR2(3) |  |
| APPLIED | VARCHAR2(3) |  |
| DELETED | VARCHAR2(3) |  |
| STATUS | VARCHAR2(1) |  |
| COMPLETION_TIME | DATE |  |
| DICTIONARY_BEGIN | VARCHAR2(3) |  |
| DICTIONARY_END | VARCHAR2(3) |  |
| END_OF_REDO | VARCHAR2(3) |  |
| ARCHIVAL_THREAD# | NUMBER |  |
| IS_RECOVERY_DEST_FILE | VARCHAR2(3) |  |
| COMPRESSED | VARCHAR2(3) |  |
| FAL | VARCHAR2(3) |  |
| END_OF_REDO_TYPE | VARCHAR2(10) |  |
| SOURCE_DBID | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content No rows are returned for this view on a physical standby database.