---
id: 19c__DBMS_TRACE.GET_PLSQL_TRACE_LEVEL
name: DBMS_TRACE.GET_PLSQL_TRACE_LEVEL
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_TRACE
tags: [dbms_trace]
source_file: DBMS_TRACE.html
---

# DBMS_TRACE.GET_PLSQL_TRACE_LEVEL

This procedure returns the current trace level as the sum of one or more DBMS_TRACE constants.

## Syntax

```sql
DBMS_TRACE.GET_PLSQL_TRACE_LEVEL 
  RETURN BINARY_INTEGER;
```

**Returns:** `BINARY_INTEGER`

## Usage Notes

See Table 178-1 for a list of the constants. Syntax DBMS_TRACE.GET_PLSQL_TRACE_LEVEL RETURN BINARY_INTEGER;