---
id: 19c__DBMS_PROFILER.FLUSH_DATA
name: DBMS_PROFILER.FLUSH_DATA
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PROFILER
tags: [dbms_profiler]
source_file: DBMS_PROFILER.html
---

# DBMS_PROFILER.FLUSH_DATA

This function flushes profiler data collected in the user's session. The data is flushed to database tables, which are expected to preexist.

## Syntax

```sql
DBMS_PROFILER.FLUSH_DATA 
  RETURN BINARY_INTEGER;

DBMS_PROFILER.FLUSH_DATA;
```

**Returns:** `BINARY_INTEGER`

## Usage Notes

Note: Use the PROFTAB . SQL script to create the tables and other data structures required for persistently storing the profiler data. Note: Use the PROFTAB . SQL script to create the tables and other data structures required for persistently storing the profiler data. Syntax DBMS_PROFILER.FLUSH_DATA RETURN BINARY_INTEGER; DBMS_PROFILER.FLUSH_DATA;