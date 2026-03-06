---
id: 19c__V$BACKUP_PIECE
name: V$BACKUP_PIECE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-BACKUP_PIECE.html
---

# V$BACKUP_PIECE

V$BACKUP_PIECE displays information about backup pieces from the control file. Each backup set consists of one or more backup pieces.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| RECID | NUMBER |  |
| STAMP | NUMBER |  |
| SET_STAMP | NUMBER |  |
| SET_COUNT | NUMBER |  |
| PIECE# | NUMBER |  |
| COPY# | NUMBER |  |
| DEVICE_TYPE | VARCHAR2(17) |  |
| HANDLE | VARCHAR2(513) |  |
| COMMENTS | VARCHAR2(64) |  |
| MEDIA | VARCHAR2(65) |  |
| MEDIA_POOL | NUMBER |  |
| CONCUR | VARCHAR2(3) |  |
| TAG | VARCHAR2(32) |  |
| STATUS | VARCHAR2(1) |  |
| START_TIME | DATE |  |
| COMPLETION_TIME | DATE |  |
| ELAPSED_SECONDS | NUMBER |  |
| DELETED | VARCHAR2(3) |  |
| BYTES | NUMBER |  |
| IS_RECOVERY_DEST_FILE | VARCHAR2(3) |  |
| RMAN_STATUS_RECID | NUMBER |  |
| RMAN_STATUS_STAMP | NUMBER |  |
| COMPRESSED | VARCHAR2(3) |  |
| BACKED_BY_VSS | VARCHAR2(3) |  |
| ENCRYPTED | VARCHAR2(3) |  |
| BACKED_BY_OSB | VARCHAR2(3) |  |
| FOR_XTTS | VARCHAR2(3) |  |
| SAME_ENDIAN | VARCHAR2(3) |  |
| CON_ID | NUMBER |  |
| GUID | RAW(16) |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content