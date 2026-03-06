---
id: 19c__DBA_DBFS_HS_PROPERTIES
name: DBA_DBFS_HS_PROPERTIES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_DBFS_HS_PROPERTIES.html
---

# DBA_DBFS_HS_PROPERTIES

DBA_DBFS_HS_PROPERTIES shows modifiable properties of all Database File System (DBFS) hierarchical stores.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| STORENAME | VARCHAR2(256) | Name of store |
| STOREOWNER | VARCHAR2(64) | Owner of store |
| PROPERTYNAME | VARCHAR2(256) | Property name |
| PROPERTYVALUE | VARCHAR2(256) | Property value |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View USER_DBFS_HS_PROPERTIES shows modifiable properties of all DBFS hierarchical stores owned by current user. This view does not display the STOREOWNER column. See Also: " USER_DBFS_HS_PROPERTIES " See Also: " USER_DBFS_HS_PROPERTIES "