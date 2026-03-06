---
id: 19c__ALL_EXTERNAL_TABLES
name: ALL_EXTERNAL_TABLES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [all]
source_file: ALL_EXTERNAL_TABLES.html
---

# ALL_EXTERNAL_TABLES

ALL_EXTERNAL_TABLES describes the external tables accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the external table |
| TABLE_NAME | VARCHAR2(128) | Name of the external table |
| TYPE_OWNER | CHAR(3) | Owner of the implementation type for the external table access driver |
| TYPE_NAME | VARCHAR2(128) | Name of the implementation type for the external table access driver |
| DEFAULT_DIRECTORY_OWNER | CHAR(3) | Owner of the default directory for the external table |
| DEFAULT_DIRECTORY_NAME | VARCHAR2(128) | Name of the default directory for the external table |
| REJECT_LIMIT | VARCHAR2(40) | Reject limit for the external table, or UNLIMITED |
| ACCESS_TYPE | VARCHAR2(7) | Type of access parameters for the external table: BLOB CLOB |
| ACCESS_PARAMETERS | CLOB | Access parameters for the external table |
| PROPERTY | VARCHAR2(10) | Property of the external table: REFERENCED - Referenced columns ALL - All columns |
| INMEMORY | VARCHAR2(8) | Indicates whether the In-Memory Column Store (IM column store) is enabled ( ENABLED ) or disabled ( DISABLED ) for this table |
| INMEMORY_COMPRESSION | VARCHAR2(17) | Indicates the compression level for the IM column store: NO MEMCOMPRESS FOR DML FOR CAPACITY [ HIGH | LOW ] FOR QUERY [ HIGH | LOW ] NULL This column has a value based on where the segments lie for a table. For example, if the table is partitioned and is enabled for the IM column store, the value is NULL for ALL_EXTERNAL_TABLES but non- NULL for ALL_XTERNAL_TAB_PARTITIONS . |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_EXTERNAL_TABLES describes all external tables in the database. USER_EXTERNAL_TABLES describes the external tables owned by the current user. This view does not display the OWNER column. See Also: " DBA_EXTERNAL_TABLES " " USER_EXTERNAL_TABLES " See Also: " DBA_EXTERNAL_TABLES " " USER_EXTERNAL_TABLES "