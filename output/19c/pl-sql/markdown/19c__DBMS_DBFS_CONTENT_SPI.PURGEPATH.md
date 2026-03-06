---
id: 19c__DBMS_DBFS_CONTENT_SPI.PURGEPATH
name: DBMS_DBFS_CONTENT_SPI.PURGEPATH
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT_SPI
tags: [dbms_dbfs_content_spi]
source_file: DBMS_DBFS_CONTENT_SPI.html
---

# DBMS_DBFS_CONTENT_SPI.PURGEPATH

This procedure purges any soft-deleted versions of the given path item.

## Syntax

```sql
DBMS_DBFS_CONTENT_SPI.PURGEPATH (
   path           IN      VARCHAR2,
   filter         IN      VARCHAR2,
   store_name     IN      VARCHAR2,
   ctx            IN      DBMS_DBFS_CONTENT_CONTEXT_T);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2 | IN | Name of store |
| path | VARCHAR2 | IN | Name of path to file items |
| filter | VARCHAR2 | IN | A filter, if any, to be applied |
| ctx | DBMS_DBFS_CONTENT_CONTEXT_T) | IN | Context with which to access the path items (see DBMS_DBFS_CONTENT_CONTEXT_T Object Type ) |

## Usage Notes

Syntax DBMS_DBFS_CONTENT_SPI.PURGEPATH ( path IN VARCHAR2, filter IN VARCHAR2, store_name IN VARCHAR2, ctx IN DBMS_DBFS_CONTENT_CONTEXT_T); Parameters Table 53-21 PURGEPATH Procedure Parameters Parameter Description store_name Name of store path Name of path to file items filter A filter, if any, to be applied ctx Context with which to access the path items (see DBMS_DBFS_CONTENT_CONTEXT_T Object Type )