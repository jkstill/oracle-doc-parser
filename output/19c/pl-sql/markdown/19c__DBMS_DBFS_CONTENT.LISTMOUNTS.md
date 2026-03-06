---
id: 19c__DBMS_DBFS_CONTENT.LISTMOUNTS
name: DBMS_DBFS_CONTENT.LISTMOUNTS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.LISTMOUNTS

This function lists all available mount points, their backing stores, and the store features.

## Syntax

```sql
DBMS_DBFS_CONTENT.LISTMOUNTS 
  RETURN MOUNTS_T PIPELINED;
```

**Returns:** `MOUNTS_T`

## Usage Notes

Syntax DBMS_DBFS_CONTENT.LISTMOUNTS RETURN MOUNTS_T PIPELINED; Return Values MOUNTS_T Table Type Usage Notes A single mount results in a single returned row, with its store_mount field of the returned records set to NULL .