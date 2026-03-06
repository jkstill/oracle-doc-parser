---
id: 19c__DBMS_CUBE_LOG.TYPE_DIMENSION_COMPILE
name: DBMS_CUBE_LOG.TYPE_DIMENSION_COMPILE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CUBE_LOG
tags: [dbms_cube_log]
source_file: DBMS_CUBE_LOG.html
---

# DBMS_CUBE_LOG.TYPE_DIMENSION_COMPILE

This function returns the integer value of the Cube Dimension Compile log.

## Syntax

```sql
DBMS_CUBE_LOG.TYPE_DIMENSION_COMPILE ()
     RETURN BINARY_INTEGER;
```

**Returns:** `BINARY_INTEGER`

## Usage Notes

Syntax DBMS_CUBE_LOG.TYPE_DIMENSION_COMPILE () RETURN BINARY_INTEGER; Usage Notes Use this function instead of its binary integer equivalent for the LOG_TYPE parameter in DBMS_CUBE_LOG subprograms. See " Logging Types " . Example This query returns the default name of a Cube Dimension Compile log: SELECT dbms_cube_log.default_name(dbms_cube_log.type_dimension_compile) - "Log Name" FROM dual; Log Name ------------------------- CUBE_DIMENSION_COMPILE