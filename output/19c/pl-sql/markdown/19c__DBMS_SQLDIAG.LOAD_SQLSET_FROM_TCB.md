---
id: 19c__DBMS_SQLDIAG.LOAD_SQLSET_FROM_TCB
name: DBMS_SQLDIAG.LOAD_SQLSET_FROM_TCB
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLDIAG
tags: [dbms_sqldiag]
source_file: DBMS_SQLDIAG.html
---

# DBMS_SQLDIAG.LOAD_SQLSET_FROM_TCB

This function loads a SQLSET from a Test Case Builder file.

## Syntax

```sql
DBMS_SQLDIAG.LOAD_SQLSET_FROM_TCB (
    directory        IN     VARCHAR2,
    filename         IN     VARCHAR2,
    sqlset_name      IN     VARCHAR2 DEFAULT NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| directory | VARCHAR2 | IN | Name of directory |
| filename | VARCHAR2 | IN | Name of file |
| sqlset_name | VARCHAR2 | IN | Name of SQLSET |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_SQLDIAG.LOAD_SQLSET_FROM_TCB ( directory IN VARCHAR2, filename IN VARCHAR2, sqlset_name IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Parameters Table 165-28 LOAD_SQLSET_FROM_TCB Function Parameters Parameter Description directory Name of directory filename Name of file sqlset_name Name of SQLSET