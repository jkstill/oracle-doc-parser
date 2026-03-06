---
id: 19c__V$BACKUP_CONTROLFILE_DETAILS
name: V$BACKUP_CONTROLFILE_DETAILS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-BACKUP_CONTROLFILE_DETAILS.html
---

# V$BACKUP_CONTROLFILE_DETAILS

V$BACKUP_CONTROLFILE_DETAILS contains information about restorable control files.

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
| CREATION_TIME | DATE |  |
| RESETLOGS_CHANGE# | NUMBER |  |
| RESETLOGS_TIME | DATE |  |
| CHECKPOINT_CHANGE# | NUMBER |  |
| CHECKPOINT_TIME | DATE |  |
| FILESIZE | NUMBER |  |
| COMPRESSION_RATIO | NUMBER |  |
| FILESIZE_DISPLAY | VARCHAR2(4000) |  |
| CON_ID | NUMBER |  |

## Usage Notes

It will include all the control files backed up in the backup set, image copies, and proxy copies.