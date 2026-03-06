---
id: 19c__DBMS_CUBE_LOG.TYPE_BUILD
name: DBMS_CUBE_LOG.TYPE_BUILD
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CUBE_LOG
tags: [dbms_cube_log]
source_file: DBMS_CUBE_LOG.html
---

# DBMS_CUBE_LOG.TYPE_BUILD

This function returns the integer value of the Cube Build log.

## Syntax

```sql
DBMS_CUBE_LOG.TYPE_BUILD ()
     RETURN BINARY_INTEGER;
```

**Returns:** `BINARY_INTEGER`

## Usage Notes

Syntax DBMS_CUBE_LOG.TYPE_BUILD () RETURN BINARY_INTEGER; Usage Notes Use this function instead of its binary integer equivalent for the LOG_TYPE parameter in DBMS_CUBE_LOG subprograms. See " Logging Types " . Example This query returns the default name of a Cube Build log: SELECT dbms_cube_log.default_name(dbms_cube_log.type_build) "Log Name" - FROM dual; Log Name ------------------------- CUBE_BUILD_LOG