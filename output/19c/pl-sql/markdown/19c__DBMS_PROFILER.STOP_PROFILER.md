---
id: 19c__DBMS_PROFILER.STOP_PROFILER
name: DBMS_PROFILER.STOP_PROFILER
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PROFILER
tags: [dbms_profiler]
source_file: DBMS_PROFILER.html
---

# DBMS_PROFILER.STOP_PROFILER

This function stops profiler data collection in the user's session.

## Syntax

```sql
DBMS_PROFILER.STOP_PROFILER 
  RETURN BINARY_INTEGER; 

DBMS_PROFILER.STOP_PROFILER;
```

**Returns:** `BINARY_INTEGER`

## Usage Notes

This function has the side effect of flushing data collected so far in the session, and it signals the end of a run. Syntax DBMS_PROFILER.STOP_PROFILER RETURN BINARY_INTEGER; DBMS_PROFILER.STOP_PROFILER;