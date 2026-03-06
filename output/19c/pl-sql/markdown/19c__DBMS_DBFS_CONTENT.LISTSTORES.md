---
id: 19c__DBMS_DBFS_CONTENT.LISTSTORES
name: DBMS_DBFS_CONTENT.LISTSTORES
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.LISTSTORES

This function lists all available stores and their features.

## Syntax

```sql
DBMS_DBFS_CONTENT.LISTSTORES 
  RETURN STORES_T PIPELINED;
```

**Returns:** `STORES_T`

## Usage Notes

Syntax DBMS_DBFS_CONTENT.LISTSTORES RETURN STORES_T PIPELINED; Return Values STORES_T Table Type Usage Notes The store_mount field of the returned records is set to NULL (since mount-points are separate from stores themselves).