---
id: 19c__DBA_FLASHBACK_ARCHIVE_TABLES
name: DBA_FLASHBACK_ARCHIVE_TABLES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [dba]
source_file: DBA_FLASHBACK_ARCHIVE_TABLES.html
---

# DBA_FLASHBACK_ARCHIVE_TABLES

DBA_FLASHBACK_ARCHIVE_TABLES displays information about all tables in the database that are enabled for Flashback Archive.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TABLE_NAME | VARCHAR2(128) | Name of the table enabled for Flashback Archive |
| OWNER_NAME | VARCHAR2(128) | Owner name of the table enabled for Flashback Archive |
| FLASHBACK_ARCHIVE_NAME | VARCHAR2(255) | Name of the flashback archive |
| ARCHIVE_TABLE_NAME | VARCHAR2(53) | Name of the archive table containing the historical data for the user table |
| STATUS | VARCHAR2(13) | Status of whether flashback archive is enabled or being disabled on the table |

## Usage Notes

Related View USER_FLASHBACK_ARCHIVE_TABLES displays information about the tables owned by the current user that are enabled for Flashback Archive. See Also: " USER_FLASHBACK_ARCHIVE_TABLES " See Also: " USER_FLASHBACK_ARCHIVE_TABLES "