---
id: 19c__DBMS_PROFILER.INTERNAL_VERSION_CHECK
name: DBMS_PROFILER.INTERNAL_VERSION_CHECK
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PROFILER
tags: [dbms_profiler]
source_file: DBMS_PROFILER.html
---

# DBMS_PROFILER.INTERNAL_VERSION_CHECK

This function verifies that this version of the DBMS_PROFILER package can work with the implementation in the database.

## Syntax

```sql
DBMS_PROFILER.INTERNAL_VERSION_CHECK 
  RETURN BINARY_INTEGER;
```

**Returns:** `BINARY_INTEGER`

## Usage Notes

Syntax DBMS_PROFILER.INTERNAL_VERSION_CHECK RETURN BINARY_INTEGER;