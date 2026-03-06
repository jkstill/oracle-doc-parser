---
id: 19c__DBA_DBFS_HS
name: DBA_DBFS_HS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_DBFS_HS.html
---

# DBA_DBFS_HS

DBA_DBFS_HS shows all Database File System (DBFS) hierarchical stores.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| STORENAME | VARCHAR2(256) | Name of store |
| STOREOWNER | VARCHAR2(64) | Owner of store |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View USER_DBFS_HS shows all Database File System hierarchical stores owned by the current user. This view does not display the STOREOWNER column. See Also: " USER_DBFS_HS " See Also: " USER_DBFS_HS "