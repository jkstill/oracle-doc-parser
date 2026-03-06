---
id: 19c__V$BACKUP_SPFILE_DETAILS
name: V$BACKUP_SPFILE_DETAILS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-BACKUP_SPFILE_DETAILS.html
---

# V$BACKUP_SPFILE_DETAILS

V$BACKUP_SPFILE_DETAILS displays information about all restorable SP files backed up in the backup set.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SESSION_KEY | NUMBER |  |
| SESSION_RECID | NUMBER |  |
| SESSION_STAMP | NUMBER |  |
| BS_KEY | NUMBER |  |
| SET_STAMP | NUMBER |  |
| SET_COUNT | NUMBER |  |
| MODIFICATION_TIME | DATE |  |
| FILESIZE | NUMBER |  |
| FILESIZE_DISPLAY | VARCHAR2(4000) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content