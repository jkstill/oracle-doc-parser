---
id: 19c__DBMS_DBFS_CONTENT.GETSTOREBYMOUNT
name: DBMS_DBFS_CONTENT.GETSTOREBYMOUNT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.GETSTOREBYMOUNT

This function returns a store by way of its name.

## Syntax

```sql
DBMS_DBFS_CONTENT.GETSTOREBYMOUNT (
   store_mount       IN      VARCHAR2)
  RETURN STORE_T;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_mount | VARCHAR2) | IN | Location at which the store instance is mounted |

**Returns:** `STORE_T`

## Usage Notes

Syntax DBMS_DBFS_CONTENT.GETSTOREBYMOUNT ( store_mount IN VARCHAR2) RETURN STORE_T; Parameters Table 52-43 GETSTOREBYMOUNT Function Parameters Parameter Description store_mount Location at which the store instance is mounted Return Values STORE_T Record Type