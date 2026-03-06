---
id: 19c__DBMS_DBFS_CONTENT.GETVERSION
name: DBMS_DBFS_CONTENT.GETVERSION
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.GETVERSION

This function marks each version of the DBMS_DBFS_CONTENT interface.

## Syntax

```sql
DBMS_DBFS_CONTENT.GETVERSION (
  RETURN VARCHAR2;
```

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_DBFS_CONTENT.GETVERSION ( RETURN VARCHAR2; Return Values A string enumerating the version of the DBMS_DBFS_CONTENT interface in standard naming convention: string: a.b.c corresponding to major , minor , and patch components.