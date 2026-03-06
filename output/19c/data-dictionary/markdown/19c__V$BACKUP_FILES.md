---
id: 19c__V$BACKUP_FILES
name: V$BACKUP_FILES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-BACKUP_FILES.html
---

# V$BACKUP_FILES

V$BACKUP_FILES displays information about all RMAN backups (both image copies and backup sets) and archived logs.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| PKEY | NUMBER |  |
| BACKUP_TYPE | VARCHAR2(32) |  |
| FILE_TYPE | VARCHAR2(32) |  |
| KEEP | VARCHAR2(3) |  |
| KEEP_UNTIL | DATE |  |
| KEEP_OPTIONS | VARCHAR2(13) |  |
| STATUS | VARCHAR2(16) |  |
| FNAME | VARCHAR2(1024) |  |
| TAG | VARCHAR2(32) |  |
| MEDIA | VARCHAR2(80) |  |
| RECID | NUMBER |  |
| STAMP | NUMBER |  |
| DEVICE_TYPE | VARCHAR2(255) |  |
| BLOCK_SIZE | NUMBER |  |
| COMPLETION_TIME | DATE |  |
| COMPRESSED | VARCHAR2(3) |  |
| OBSOLETE | VARCHAR2(3) |  |
| BYTES | NUMBER |  |
| BS_KEY | NUMBER |  |
| BS_COUNT | NUMBER |  |
| BS_STAMP | NUMBER |  |
| BS_TYPE | VARCHAR2(32) |  |
| BS_INCR_TYPE | VARCHAR2(32) |  |
| BS_PIECES | NUMBER |  |
| BS_COPIES | NUMBER |  |
| BS_COMPLETION_TIME | DATE |  |
| BS_STATUS | VARCHAR2(16) |  |
| BS_BYTES | NUMBER |  |
| BS_COMPRESSED | VARCHAR2(3) |  |
| BS_TAG | VARCHAR2(1024) |  |
| BS_DEVICE_TYPE | VARCHAR2(255) |  |
| BP_PIECE# | NUMBER |  |
| BP_COPY# | NUMBER |  |
| DF_FILE# | NUMBER |  |
| DF_TABLESPACE | VARCHAR2(30) |  |
| DF_RESETLOGS_CHANGE# | NUMBER |  |
| DF_CREATION_CHANGE# | NUMBER |  |
| DF_CHECKPOINT_CHANGE# | NUMBER |  |
| DF_CKP_MOD_TIME | DATE |  |
| RL_THREAD# | NUMBER |  |
| RL_SEQUENCE# | NUMBER |  |
| RL_RESETLOGS_CHANGE# | NUMBER |  |
| RL_FIRST_CHANGE# | NUMBER |  |
| RL_FIRST_TIME | DATE |  |
| RL_NEXT_CHANGE# | NUMBER |  |
| RL_NEXT_TIME | DATE |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This view simulates the LIST BACKUP and LIST COPY RMAN commands. This view requires that the database be set using the DBMS_RCVMAN.SETDATABASE procedure. See Also: Oracle Database Backup and Recovery User’s Guide for more information about the DBMS_RCVMAN.SETDATABASE procedure See Also: Oracle Database Backup and Recovery User’s Guide for more information about the DBMS_RCVMAN.SETDATABASE procedure