---
id: 19c__DBMS_CUBE_LOG.GET_LOG_SPEC
name: DBMS_CUBE_LOG.GET_LOG_SPEC
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CUBE_LOG
tags: [dbms_cube_log]
source_file: DBMS_CUBE_LOG.html
---

# DBMS_CUBE_LOG.GET_LOG_SPEC

This function retrieves a description of all active Cube Operations logs, Cube Rejected Records logs, and Cube Dimension Compile logs.

## Syntax

```sql
DBMS_CUBE_LOG.GET_LOG_SPEC ( )
     RETURN VARCHAR2;
```

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_CUBE_LOG.GET_LOG_SPEC ( ) RETURN VARCHAR2; Returns The type and target of all active logs. Usage Notes You can use the output from this function as the input to SET_LOG_SPEC . Examples The following example shows that the Cube Operations log, Cube Rejected Records log, and Cube Dimension Compile log are active. The Cube Operations log is stored in the session trace file and the other logs are stored in tables. SELECT dbms_cube_log.get_log_spec FROM dual; GET_LOG_SPEC -------------------------------------------------------------------------------- OPERATIONS(TABLE, TRACE) REJECTED_RECORDS(TABLE[DEBUG])