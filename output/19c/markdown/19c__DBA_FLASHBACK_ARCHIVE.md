---
id: 19c__DBA_FLASHBACK_ARCHIVE
name: DBA_FLASHBACK_ARCHIVE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dba]
source_file: DBA_FLASHBACK_ARCHIVE.html
---

# DBA_FLASHBACK_ARCHIVE

DBA_FLASHBACK_ARCHIVE describes all flashback archives available in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER_NAME | VARCHAR2(255) | Name of the creator of the flashback archive |
| FLASHBACK_ARCHIVE_NAME | VARCHAR2(255) | Name of the flashback archive |
| FLASHBACK_ARCHIVE# | NUMBER | Number of the flashback archive |
| RETENTION_IN_DAYS | NUMBER | Maximum duration (in days) for which data is retained in the flashback archive |
| CREATE_TIME | TIMESTAMP(9) | Time at which the flashback archive was created |
| LAST_PURGE_TIME | TIMESTAMP(9) | Time at which the data in the flashback archive was last purged by the system |
| STATUS | VARCHAR2(7) | Indicates whether the flashback archive is a default flashback archive for the system ( DEFAULT ) or not (NULL) |

## Usage Notes

Related View USER_FLASHBACK_ARCHIVE describes the flashback archives available to the current user. See Also: " USER_FLASHBACK_ARCHIVE " See Also: " USER_FLASHBACK_ARCHIVE "