---
id: 19c__DBMS_CUBE_LOG.LEVEL_HIGHEST
name: DBMS_CUBE_LOG.LEVEL_HIGHEST
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CUBE_LOG
tags: [dbms_cube_log]
source_file: DBMS_CUBE_LOG.html
---

# DBMS_CUBE_LOG.LEVEL_HIGHEST

This function returns the integer value of the highest verbosity level.

## Syntax

```sql
DBMS_CUBE_LOG.LEVEL_HIGHEST ()
     RETURN BINARY_INTEGER;
```

**Returns:** `BINARY_INTEGER`

## Usage Notes

Syntax DBMS_CUBE_LOG.LEVEL_HIGHEST () RETURN BINARY_INTEGER; Usage Notes Use this function instead of its binary integer equivalent for the LOG_LEVEL parameter in DBMS_CUBE_LOG subprograms. See " Verbosity Levels " . Example This command sets the verbosity level of the cube operations table to highest: EXECUTE dbms_cube_log.enable(dbms_cube_log.type_operations, - dbms_cube_log.target_table, dbms_cube_log.level_highest);