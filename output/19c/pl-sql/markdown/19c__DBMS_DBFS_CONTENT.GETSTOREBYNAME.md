---
id: 19c__DBMS_DBFS_CONTENT.GETSTOREBYNAME
name: DBMS_DBFS_CONTENT.GETSTOREBYNAME
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.GETSTOREBYNAME

This function returns a store by way of its name.

## Syntax

```sql
DBMS_DBFS_CONTENT.GETSTOREBYNAME (
   store_name       IN      VARCHAR2)
  RETURN STORE_T;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2) | IN | Name of store |

**Returns:** `STORE_T`

## Usage Notes

Syntax DBMS_DBFS_CONTENT.GETSTOREBYNAME ( store_name IN VARCHAR2) RETURN STORE_T; Parameters Table 52-44 GETSTOREBYNAME Function Parameters Parameter Description store_name Name of store Return Values STORE_T Record Type