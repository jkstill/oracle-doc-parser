---
id: 19c__DBMS_CUBE_LOG.TYPE_REJECTED_RECORDS
name: DBMS_CUBE_LOG.TYPE_REJECTED_RECORDS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CUBE_LOG
tags: [dbms_cube_log]
source_file: DBMS_CUBE_LOG.html
---

# DBMS_CUBE_LOG.TYPE_REJECTED_RECORDS

This function returns the integer value of the cube Cube Rejected Records log.

## Syntax

```sql
DBMS_CUBE_LOG.TYPE_REJECTED_RECORDS ()
     RETURN BINARY_INTEGER;
```

**Returns:** `BINARY_INTEGER`

## Usage Notes

Syntax DBMS_CUBE_LOG.TYPE_REJECTED_RECORDS () RETURN BINARY_INTEGER; Usage Notes Use this function instead of its binary integer equivalent for the LOG_TYPE parameter in DBMS_CUBE_LOG subprograms. See " Logging Types " . Example This query returns the default name of a Cube Rejected Records log: SELECT dbms_cube_log.default_name(dbms_cube_log.type_rejected_records) - "Log Name" FROM dual; Log Name ------------------------- CUBE_REJECTED_RECORDS