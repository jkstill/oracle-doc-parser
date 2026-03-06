---
id: 19c__V$BACKUP_ARCHIVELOG_DETAILS
name: V$BACKUP_ARCHIVELOG_DETAILS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dynamic_performance]
source_file: V-BACKUP_ARCHIVELOG_DETAILS.html
---

# V$BACKUP_ARCHIVELOG_DETAILS

V$BACKUP_ARCHIVELOG_DETAILS contains information about all restorable archive logs.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| BTYPE | CHAR(9) |  |
| BTYPE_KEY | NUMBER |  |
| SESSION_KEY | NUMBER |  |
| SESSION_RECID | NUMBER |  |
| SESSION_STAMP | NUMBER |  |
| ID1 | NUMBER |  |
| ID2 | NUMBER |  |
| THREAD# | NUMBER |  |
| SEQUENCE# | NUMBER |  |
| RESETLOGS_CHANGE# | NUMBER |  |
| RESETLOGS_TIME | DATE |  |
| FIRST_CHANGE# | NUMBER |  |
| FIRST_TIME | DATE |  |
| NEXT_CHANGE# | NUMBER |  |
| NEXT_TIME | DATE |  |
| FILESIZE | NUMBER |  |
| COMPRESSION_RATIO | NUMBER |  |
| FILESIZE_DISPLAY | VARCHAR2(4000) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content It will include all archived logs backed up in a backup set or proxy copies.