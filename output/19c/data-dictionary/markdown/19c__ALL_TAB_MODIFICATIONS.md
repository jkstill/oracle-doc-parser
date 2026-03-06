---
id: 19c__ALL_TAB_MODIFICATIONS
name: ALL_TAB_MODIFICATIONS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_TAB_MODIFICATIONS.html
---

# ALL_TAB_MODIFICATIONS

ALL_TAB_MODIFICATIONS describes tables accessible to the current user that have been modified since the last time statistics were gathered on the tables.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TABLE_OWNER | VARCHAR2(128) | Owner of the modified table |
| TABLE_NAME | VARCHAR2(128) | Name of the modified table |
| PARTITION_NAME | VARCHAR2(128) | Name of the modified partition |
| SUBPARTITION_NAME | VARCHAR2(128) | Name of the modified subpartition |
| INSERTS | NUMBER | Approximate number of inserts since the last time statistics were gathered |
| UPDATES | NUMBER | Approximate number of updates since the last time statistics were gathered |
| DELETES | NUMBER | Approximate number of deletes since the last time statistics were gathered |
| TIMESTAMP | DATE | Indicates the last time the table was modified |
| TRUNCATED | VARCHAR2(3) | Indicates whether the table has been truncated since the last analyze ( YES ) or not ( NO ) |
| DROP_SEGMENTS | NUMBER | Number of partition and subpartition segments dropped since the last analyze |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_TAB_MODIFICATIONS describes such information for all tables in the database. USER_TAB_MODIFICATIONS describes such information for tables owned by the current user. This view does not display the TABLE_OWNER column. See Also: " DBA_TAB_MODIFICATIONS " " USER_TAB_MODIFICATIONS " See Also: " DBA_TAB_MODIFICATIONS " " USER_TAB_MODIFICATIONS "