---
id: 19c__DBMS_CUBE_LOG.SET_LOG_SPEC
name: DBMS_CUBE_LOG.SET_LOG_SPEC
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CUBE_LOG
tags: [dbms_cube_log]
source_file: DBMS_CUBE_LOG.html
---

# DBMS_CUBE_LOG.SET_LOG_SPEC

This procedure sets all logging to the values specified in the input string.

## Syntax

```sql
DBMS_CUBE_LOG.SET_LOG_SPEC (
          LOG_SPEC       IN   VARCHAR2 );
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| log_spec | VARCHAR2 | IN | A string consisting of type ( target ) pairs. Type can be: OPERATIONS REJECTED_RECORDS DIMENSION_COMPILE Target can be: TABLE TRACE FILE LOB |

## Usage Notes

Syntax DBMS_CUBE_LOG.SET_LOG_SPEC ( LOG_SPEC IN VARCHAR2 ); Parameters Table 46-7 SET_LOG_SPEC Procedure Parameters Parameter Description log_spec A string consisting of type ( target ) pairs. Type can be: OPERATIONS REJECTED_RECORDS DIMENSION_COMPILE Target can be: TABLE TRACE FILE LOB Usage Notes The GET_LOG_SPEC function returns a properly formatted string for SET_LOG_SPEC . Examples This PL/SQL procedure disables all logs, verifies that they are disabled, then activates the Cube Operations log and the Cube Rejected Records log. BEGIN dbms_cube_log.disable; dbms_output.put_line('Cube Logs: ' || dbms_cube_log.get_log_spec); dbms_cube_log.set_log_spec('OPERATIONS(TRACE) REJECTED_RECORDS(TABLE)'); dbms_output.put_line('Cube Logs: ' || dbms_cube_log.get_log_spec); END; / The output from the procedure verifies that the DISABLE function de-activated all logs, and the SET_LOG_SPEC function activated two logs: Cube Logs: Cube Logs: OPERATIONS(TRACE) REJECTED_RECORDS(TABLE)