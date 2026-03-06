---
id: 19c__V$ARCHIVED_LOG
name: V$ARCHIVED_LOG
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dynamic_performance]
source_file: V-ARCHIVED_LOG.html
---

# V$ARCHIVED_LOG

V$ARCHIVED_LOG displays archived log information from the control file, including archive log names.

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
| STANDBY_DEST | VARCHAR2(3) |  |
| ARCHIVED | VARCHAR2(3) |  |
| APPLIED | VARCHAR2(9) |  |
| DELETED | VARCHAR2(3) |  |
| STATUS | VARCHAR2(1) |  |
| COMPLETION_TIME | DATE |  |
| DICTIONARY_BEGIN | VARCHAR2(3) |  |
| DICTIONARY_END | VARCHAR2(3) |  |
| END_OF_REDO | VARCHAR2(3) |  |
| BACKUP_COUNT | NUMBER |  |
| ARCHIVAL_THREAD# | NUMBER |  |
| ACTIVATION# | NUMBER |  |
| IS_RECOVERY_DEST_FILE | VARCHAR2(3) |  |
| COMPRESSED | VARCHAR2(3) |  |
| FAL | VARCHAR2(3) |  |
| END_OF_REDO_TYPE | VARCHAR2(10) |  |
| BACKED_BY_VSS | VARCHAR2(3) |  |
| CON_ID | NUMBER |  |

## Usage Notes

An archive log record is inserted after the online redo log is successfully archived or cleared (name column is NULL if the log was cleared). If the log is archived twice, there will be two archived log records with the same THREAD# , SEQUENCE# , and FIRST_CHANGE# , but with a different name. An archive log record is also inserted when an archive log is restored from a backup set or a copy and whenever a copy of a log is made with the RMAN COPY command.