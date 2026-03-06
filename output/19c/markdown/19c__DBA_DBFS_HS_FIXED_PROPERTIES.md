---
id: 19c__DBA_DBFS_HS_FIXED_PROPERTIES
name: DBA_DBFS_HS_FIXED_PROPERTIES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_DBFS_HS_FIXED_PROPERTIES.html
---

# DBA_DBFS_HS_FIXED_PROPERTIES

DBA_DBFS_HS_FIXED_PROPERTIES shows non-modifiable properties of all Database File System (DBFS) hierarchical stores.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| STORE_NAME | VARCHAR2(128) | Name of store |
| STORE_OWNER | VARCHAR2(128) | Owner of store |
| PROP_NAME | VARCHAR2(256) | Property name |
| PROP_VALUE | VARCHAR2(256) | Property value |

## Usage Notes

Related View USER_DBFS_HS_FIXED_PROPERTIES shows non-modifiable properties of all DBFS hierarchical stores owned by current user. This view does not display the STORE_OWNER column. See Also: " USER_DBFS_HS_FIXED_PROPERTIES " See Also: " USER_DBFS_HS_FIXED_PROPERTIES "