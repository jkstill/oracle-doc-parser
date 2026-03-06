---
id: 19c__ALL_XTERNAL_TAB_SUBPARTITIONS
name: ALL_XTERNAL_TAB_SUBPARTITIONS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: partitioning
tags: [all]
source_file: ALL_XTERNAL_TAB_SUBPARTITIONS.html
---

# ALL_XTERNAL_TAB_SUBPARTITIONS

ALL_XTERNAL_TAB_SUBPARTITIONS describes subpartition-level information for partitioned external tables accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TABLE_OWNER | VARCHAR2(128) | Owner of the partitioned external table |
| TABLE_NAME | VARCHAR2(128) | Name of the partitioned external table |
| PARTITION_NAME | VARCHAR2(128) | Name of the partition |
| SUBPARTITION_NAME | VARCHAR2(128) | Name of the subpartition |
| DEFAULT_DIRECTORY_OWNER | CHAR(3) | Owner of the default directory for the external table partition |
| DEFAULT_DIRECTORY_NAME | VARCHAR2(128) | Name of the default directory for the external table partition |
| ACCESS_TYPE | VARCHAR2(7) | Type of access parameters for the partition ( BLOB , CLOB ) |
| ACCESS_PARAMETERS | CLOB | Access parameters for the external table partition |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_XTERNAL_TAB_SUBPARTITIONS describes subpartition-level information for partitioned external tables in the database. USER_XTERNAL_TAB_SUBPARTITIONS describes subpartition-level information for partitioned external tables owned by the current user. This view does not display the TABLE_OWNER column. See Also: " DBA_XTERNAL_TAB_SUBPARTITIONS " " USER_XTERNAL_TAB_SUBPARTITIONS " See Also: " DBA_XTERNAL_TAB_SUBPARTITIONS " " USER_XTERNAL_TAB_SUBPARTITIONS "