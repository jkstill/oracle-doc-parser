---
id: 19c__DBMS_CUBE_LOG.TARGET_TRACE
name: DBMS_CUBE_LOG.TARGET_TRACE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CUBE_LOG
tags: [dbms_cube_log]
source_file: DBMS_CUBE_LOG.html
---

# DBMS_CUBE_LOG.TARGET_TRACE

This function returns the integer value of a trace file target.

## Syntax

```sql
DBMS_CUBE_LOG.TARGET_TRACE ()
     RETURN BINARY_INTEGER;
```

**Returns:** `BINARY_INTEGER`

## Usage Notes

Syntax DBMS_CUBE_LOG.TARGET_TRACE () RETURN BINARY_INTEGER; Usage Notes Use this function instead of its binary integer equivalent for the LOG_TARGET parameter in DBMS_CUBE_LOG subprograms. See " Logging Targets " . Example This command disables the Cube Operations log trace file: EXECUTE dbms_cube_log.disable - (dbms_cube_log.type_operations, dbms_cube_log.target_trace);