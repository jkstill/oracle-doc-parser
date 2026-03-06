---
id: 19c__DBMS_CUBE_LOG.TARGET_LOB
name: DBMS_CUBE_LOG.TARGET_LOB
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CUBE_LOG
tags: [dbms_cube_log]
source_file: DBMS_CUBE_LOG.html
---

# DBMS_CUBE_LOG.TARGET_LOB

This function returns the integer value of a LOB target.

## Syntax

```sql
DBMS_CUBE_LOG.TARGET_LOB ()
     RETURN BINARY_INTEGER;
```

**Returns:** `BINARY_INTEGER`

## Usage Notes

Syntax DBMS_CUBE_LOG.TARGET_LOB () RETURN BINARY_INTEGER; Usage Notes Use this function instead of its binary integer equivalent for the LOG_LEVEL parameter in DBMS_CUBE_LOG subprograms. See " Logging Targets " . Example This command disables the Cube Operations log LOB: EXECUTE dbms_cube_log.disable - (dbms_cube_log.type_operations, dbms_cube_log.target_lob);