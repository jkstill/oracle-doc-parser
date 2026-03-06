---
id: 19c__DBA_FLASHBACK_ARCHIVE_TS
name: DBA_FLASHBACK_ARCHIVE_TS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dba]
source_file: DBA_FLASHBACK_ARCHIVE_TS.html
---

# DBA_FLASHBACK_ARCHIVE_TS

DBA_FLASHBACK_ARCHIVE_TS describes all tablespaces in the flashback archives available in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FLASHBACK_ARCHIVE_NAME | VARCHAR2(255) | Name of the flashback archive |
| FLASHBACK_ARCHIVE# | NUMBER | Number of the flashback archive |
| TABLESPACE_NAME | VARCHAR2(30) | Name of a tablespace in the flashback archive |
| QUOTA_IN_MB | VARCHAR2(40) | Maximum space (in MB) that can be used for Flashback Archive from the tablespace; NULL indicates no Quota restriction |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content