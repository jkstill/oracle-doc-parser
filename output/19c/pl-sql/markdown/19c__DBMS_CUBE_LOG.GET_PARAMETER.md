---
id: 19c__DBMS_CUBE_LOG.GET_PARAMETER
name: DBMS_CUBE_LOG.GET_PARAMETER
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CUBE_LOG
tags: [dbms_cube_log]
source_file: DBMS_CUBE_LOG.html
---

# DBMS_CUBE_LOG.GET_PARAMETER

This function returns the current values of the options that control various aspects of logging. To set these options, use the SET_PARAMETER function.

## Syntax

```sql
DBMS_CUBE_LOG.GET_PARAMETER (
          LOG_TYPE       IN   BINARY_INTEGER,
          LOG_PARAMETER  IN   BINARY_INTEGER )
     RETURN BINARY_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| log_type | BINARY_INTEGER | IN | One of the following log types: 1 : TYPE_OPERATIONS 2 : TYPE_REJECTED_RECORDS 3 : TYPE_DIMENSION_COMPILE See " Logging Types " . |
| log_parameter | BINARY_INTEGER | IN | One of the following options: 1 : MAX_ERRORS 2 : FLUSH_INTERVAL 3 : LOG_FULL_RECORD 4 : LOG_EVERY_N 5 : ALLOW_ERRORS See " SET_PARAMETER Procedure " . |

**Returns:** `BINARY_INTEGER`

## Usage Notes

Syntax DBMS_CUBE_LOG.GET_PARAMETER ( LOG_TYPE IN BINARY_INTEGER, LOG_PARAMETER IN BINARY_INTEGER ) RETURN BINARY_INTEGER; Parameters Table 46-6 GET_PARAMETER Function Parameters Parameter Description log_type One of the following log types: 1 : TYPE_OPERATIONS 2 : TYPE_REJECTED_RECORDS 3 : TYPE_DIMENSION_COMPILE See " Logging Types " . log_parameter One of the following options: 1 : MAX_ERRORS 2 : FLUSH_INTERVAL 3 : LOG_FULL_RECORD 4 : LOG_EVERY_N 5 : ALLOW_ERRORS See " SET_PARAMETER Procedure " . Returns The value of the specified log_parameter . Examples This example shows the current maximum number of errors in the Cube Rejected Records log before logging stops. This parameter was previously set with the SET_PARAMETER procedure. SELECT dbms_cube_log.get_parameter(dbms_cube_log.type_rejected_records, 1) - "Maximum Records" FROM dual; Maximum Records --------------- 100