---
id: 19c__DBMS_DBFS_CONTENT.LIST
name: DBMS_DBFS_CONTENT.LIST
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.LIST

This function lists the path items in the specified path meeting the specified filter and other criteria.

## Syntax

```sql
DBMS_DBFS_CONTENT.LIST (
   path          IN     VARCHAR2,
   filter        IN     VARCHAR2    DEFAULT NULL,
   recurse       IN     INTEGER     DEFAULT 0,
   asof          IN     TIMESTAMP   DEFAULT NULL,
   store_name    IN     VARCHAR2    DEFAULT NULL,
   principal     IN     VARCHAR2    DEFAULT NULL)
  RETURN  DBMS_DBFS_CONTENT_LIST_ITEMS_T PIPELINED;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| path | VARCHAR2 | IN | Name of path to directories |
| filter | VARCHAR2 | IN | A filter, if any, to be applied |
| recurse | INTEGER | IN | If 0, do not execute recursively. Otherwise, recursively list the contents of directories and files below the given directory. |
| asof | TIMESTAMP | IN | The "as of" timestamp at which the underlying read-only operation (or its read-only sub-components) executes |
| store_name | VARCHAR2 | IN | Name of repository |
| principal | VARCHAR2 | IN | Agent (principal) invoking the current operation |

**Returns:** `DBMS_DBFS_CONTENT_LIST_ITEMS_T`

## Usage Notes

Syntax DBMS_DBFS_CONTENT.LIST ( path IN VARCHAR2, filter IN VARCHAR2 DEFAULT NULL, recurse IN INTEGER DEFAULT 0, asof IN TIMESTAMP DEFAULT NULL, store_name IN VARCHAR2 DEFAULT NULL, principal IN VARCHAR2 DEFAULT NULL) RETURN DBMS_DBFS_CONTENT_LIST_ITEMS_T PIPELINED; Parameters Table 52-48 LIST Function Parameters Parameter Description path Name of path to directories filter A filter, if any, to be applied recurse If 0, do not execute recursively. Otherwise, recursively list the contents of directories and files below the given directory. asof The "as of" timestamp at which the underlying read-only operation (or its read-only sub-components) executes store_name Name of repository principal Agent (principal) invoking the current operation Return Values DBMS_DBFS_CONTENT_LIST_ITEMS_T Table Type