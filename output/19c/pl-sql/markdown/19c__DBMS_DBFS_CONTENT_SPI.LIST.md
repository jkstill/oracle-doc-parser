---
id: 19c__DBMS_DBFS_CONTENT_SPI.LIST
name: DBMS_DBFS_CONTENT_SPI.LIST
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT_SPI
tags: [dbms_dbfs_content_spi]
source_file: DBMS_DBFS_CONTENT_SPI.html
---

# DBMS_DBFS_CONTENT_SPI.LIST

This function lists the contents of a directory path name.

## Syntax

```sql
DBMS_DBFS_CONTENT_SPI.LIST (
   store_name    IN     VARCHAR2,
   path          IN     VARCHAR2,
   filter        IN     VARCHAR2,
   recurse       IN     INTEGER,
   ctx           IN     DBMS_DBFS_CONTENT_CONTEXT_T)
  RETURN  DBMS_DBFS_CONTENT_LIST_ITEMS_T PIPELINED;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2 | IN | Name of repository |
| path | VARCHAR2 | IN | Name of path to directories |
| filter | VARCHAR2 | IN | A filter, if any, to be applied |
| recurse | INTEGER | IN | If 0, do not execute recursively. Otherwise, recursively list the contents of directories and files below the given directory. |
| ctx | DBMS_DBFS_CONTENT_CONTEXT_T) | IN | Context with which to access the path items (see DBMS_DBFS_CONTENT_CONTEXT_T Object Type ) |

**Returns:** `DBMS_DBFS_CONTENT_LIST_ITEMS_T`

## Usage Notes

The invoker of the subprogram has the option to investigate recursively into sub-directories, to make soft-deleted items visible, to use a flashback "as of" a specified timestamp, and to filter items within the store based on list predicates. Syntax DBMS_DBFS_CONTENT_SPI.LIST ( store_name IN VARCHAR2, path IN VARCHAR2, filter IN VARCHAR2, recurse IN INTEGER, ctx IN DBMS_DBFS_CONTENT_CONTEXT_T) RETURN DBMS_DBFS_CONTENT_LIST_ITEMS_T PIPELINED; Parameters Table 53-18 LIST Function Parameters Parameter Description store_name Name of repository path Name of path to directories filter A filter, if any, to be applied recurse If 0, do not execute recursively. Otherwise, recursively list the contents of directories and files below the given directory. ctx Context with which to access the path items (see DBMS_DBFS_CONTENT_CONTEXT_T Object Type ) Return Values Path items found that match the path, filter and criteria for executing recursively (see DBMS_DBFS_CONTENT_LIST_ITEMS_T Table Type ) Usage Notes This function returns only list items; the client is expected to explicitly use one of the GETPATH Procedures to access the properties or content associated with an item.