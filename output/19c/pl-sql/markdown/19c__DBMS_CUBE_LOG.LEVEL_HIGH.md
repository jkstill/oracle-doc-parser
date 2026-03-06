---
id: 19c__DBMS_CUBE_LOG.LEVEL_HIGH
name: DBMS_CUBE_LOG.LEVEL_HIGH
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CUBE_LOG
tags: [dbms_cube_log]
source_file: DBMS_CUBE_LOG.html
---

# DBMS_CUBE_LOG.LEVEL_HIGH

This function returns the integer value of the high verbosity level.

## Syntax

```sql
DBMS_CUBE_LOG.LEVEL_HIGH ()
     RETURN BINARY_INTEGER;
```

**Returns:** `BINARY_INTEGER`

## Usage Notes

Syntax DBMS_CUBE_LOG.LEVEL_HIGH () RETURN BINARY_INTEGER; Usage Notes Use this function instead of its binary integer equivalent for the LOG_LEVEL parameter in DBMS_CUBE_LOG subprograms. See " Verbosity Levels " . Example This command sets the verbosity level of the cube operations table to high: EXECUTE dbms_cube_log.enable(dbms_cube_log.type_operations, - dbms_cube_log.target_table, dbms_cube_log.level_high);