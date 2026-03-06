---
id: 19c__ALL_GG_AUTO_CDR_TABLES
name: ALL_GG_AUTO_CDR_TABLES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [all]
source_file: ALL_GG_AUTO_CDR_TABLES.html
---

# ALL_GG_AUTO_CDR_TABLES

ALL_GG_AUTO_CDR_TABLES provides details about tables configured for Oracle GoldenGate automatic conflict detection and resolution (CDR) that are owned by the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TABLE_OWNER | VARCHAR2(128) | Owner of the table |
| TABLE_NAME | VARCHAR2(128) | Table name |
| RESOLUTION_GRANULARITY | VARCHAR2(6) | Resolution granularity: ROW COLUMN |
| FETCHCOLS | VARCHAR2(3) | Extract fetchcols configuration: Yes : Extract will fetch non-scalar data No : Extract will not fetch non-scalar data |
| RECORD_CONFLICTS | VARCHAR2(3) | Monitoring of conflicts: Yes : Conflict info is recorded No : Conflict info is not recorded |
| USE_CUSTOM_HANDLERS | VARCHAR2(4) | Use of customized or automatic conflict handlers: All : If using custom handlers None : If using automatic handlers |
| TOMBSTONE_TABLE | VARCHAR2(128) | Tombstone table name (if table has delete tombstoning enabled) |
| ROW_RESOLUTION_COLUMN | VARCHAR2(128) | Name of row-level timestamp column |
| EXISTING_DATA_TIMESTAMP | TIMESTAMP(6) | Timestamp to give existing rows when a new timestamp column is added |

## Usage Notes

Related View DBA_GG_AUTO_CDR_TABLES provides details about all the tables configured for Oracle GoldenGate automatic conflict detection and resolution (CDR). See Also: " DBA_GG_AUTO_CDR_TABLES " See Also: " DBA_GG_AUTO_CDR_TABLES "