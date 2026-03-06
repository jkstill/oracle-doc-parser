---
id: 19c__DBMS_DBFS_CONTENT.GETTRACE
name: DBMS_DBFS_CONTENT.GETTRACE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.GETTRACE

This function returns whether DBMS_DBFS_CONTENT tracing is turned on or not.

## Syntax

```sql
DBMS_DBFS_CONTENT.GETTRACE
  RETURN INTEGER.
```

**Returns:** `INTEGER.`

## Usage Notes

Syntax DBMS_DBFS_CONTENT.GETTRACE RETURN INTEGER. Return Values Returns zero if tracing is off, non-zero if tracing is on.