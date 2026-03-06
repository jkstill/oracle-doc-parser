---
id: 19c__ALL_XTERNAL_PART_TABLES
name: ALL_XTERNAL_PART_TABLES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [all]
source_file: ALL_XTERNAL_PART_TABLES.html
---

# ALL_XTERNAL_PART_TABLES

ALL_XTERNAL_PART_TABLES describes object-level information for partitioned external tables accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the partitioned external table |
| TABLE_NAME | VARCHAR2(128) | Name of the partitioned external table |
| TYPE_OWNER | CHAR(3) | Owner of the implementation type for the external table access driver |
| TYPE_NAME | VARCHAR2(128) | Name of the implementation type for the external table access driver |
| DEFAULT_DIRECTORY_OWNER | CHAR(3) | Owner of the default directory for the external table |
| DEFAULT_DIRECTORY_NAME | VARCHAR2(128) | Name of the default directory for the external table |
| REJECT_LIMIT | VARCHAR2(40) | Reject limit for the external table, or UNLIMITED |
| ACCESS_TYPE | VARCHAR2(7) | Type of access parameters for the external table ( BLOB , CLOB ) |
| ACCESS_PARAMETERS | CLOB | Access parameters for the external table |
| PROPERTY | VARCHAR2(10) | Property of the external table ( REFERENCED , ALL ) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_XTERNAL_PART_TABLES describes object-level information for partitioned external tables in the database USER_XTERNAL_PART_TABLES describes object-level information for partitioned external tables owned by the current user. This view does not display the OWNER column. See Also: " DBA_XTERNAL_PART_TABLES " " USER_XTERNAL_PART_TABLES " See Also: " DBA_XTERNAL_PART_TABLES " " USER_XTERNAL_PART_TABLES "