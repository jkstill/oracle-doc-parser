---
id: 19c__DBMS_DBFS_CONTENT.LISTALLCONTENT
name: DBMS_DBFS_CONTENT.LISTALLCONTENT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.LISTALLCONTENT

This function lists all path items in all mounts.

## Syntax

```sql
DBMS_DBFS_CONTENT.LISTALLCONTENT 
  RETURN  PATH_ITEMS_T PIPELINED;
```

**Returns:** `PATH_ITEMS_T`

## Usage Notes

Syntax DBMS_DBFS_CONTENT.LISTALLCONTENT RETURN PATH_ITEMS_T PIPELINED; Return Values PATH_ITEMS_T Table Type