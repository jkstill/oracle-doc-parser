---
id: 19c__DBMS_DBFS_CONTENT.GETSTOREBYPATH
name: DBMS_DBFS_CONTENT.GETSTOREBYPATH
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.GETSTOREBYPATH

This function returns a store by way of its path.

## Syntax

```sql
DBMS_DBFS_CONTENT.GETSTOREBYPATH (
   path       IN      PATH_T)
  RETURN STORE_T;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| path | PATH_T) | IN | PATH_T s |

**Returns:** `STORE_T`

## Usage Notes

Syntax DBMS_DBFS_CONTENT.GETSTOREBYPATH ( path IN PATH_T) RETURN STORE_T; Parameters Table 52-45 GETSTOREBYPATH Function Parameters Parameter Description path PATH_T s Return Values STORE_T Record Type