---
id: 19c__DBMS_DBFS_CONTENT_SPI.SEARCH
name: DBMS_DBFS_CONTENT_SPI.SEARCH
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT_SPI
tags: [dbms_dbfs_content_spi]
source_file: DBMS_DBFS_CONTENT_SPI.html
---

# DBMS_DBFS_CONTENT_SPI.SEARCH

This function searches for path items matching the given path and filter criteria.

## Syntax

```sql
DBMS_DBFS_CONTENT_SPI.SEARCH (
   store_name     IN      VARCHAR2,
   path           IN      VARCHAR2,
   filter         IN      VARCHAR2,
   recurse        IN      INTEGER,
   ctx            IN      DBMS_DBFS_CONTENT_CONTEXT_T)
 RETURN  DBMS_DBFS_CONTENT_LIST_ITEMS_T PIPELINED;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2 | IN | Name of store |
| path | VARCHAR2 | IN | Name of path to the path items |
| filter | VARCHAR2 | IN | A filter, if any, to be applied |
| recurse | INTEGER | IN | If 0, do not execute recursively. Otherwise, recursively search the contents of directories and files below the given directory. |
| ctx | DBMS_DBFS_CONTENT_CONTEXT_T) | IN | Context with which to access the path items (see DBMS_DBFS_CONTENT_CONTEXT_T Object Type ) |

**Returns:** `DBMS_DBFS_CONTENT_LIST_ITEMS_T`

## Usage Notes

Syntax DBMS_DBFS_CONTENT_SPI.SEARCH ( store_name IN VARCHAR2, path IN VARCHAR2, filter IN VARCHAR2, recurse IN INTEGER, ctx IN DBMS_DBFS_CONTENT_CONTEXT_T) RETURN DBMS_DBFS_CONTENT_LIST_ITEMS_T PIPELINED; Parameters Table 53-26 LIST Function Parameters Parameter Description store_name Name of store path Name of path to the path items filter A filter, if any, to be applied recurse If 0, do not execute recursively. Otherwise, recursively search the contents of directories and files below the given directory. ctx Context with which to access the path items (see DBMS_DBFS_CONTENT_CONTEXT_T Object Type ) Return Values Path items matching the given path and filter criteria (see DBMS_DBFS_CONTENT_LIST_ITEMS_T Table Type )