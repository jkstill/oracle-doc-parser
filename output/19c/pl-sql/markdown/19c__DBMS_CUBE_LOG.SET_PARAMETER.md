---
id: 19c__DBMS_CUBE_LOG.SET_PARAMETER
name: DBMS_CUBE_LOG.SET_PARAMETER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CUBE_LOG
tags: [dbms_cube_log]
source_file: DBMS_CUBE_LOG.html
---

# DBMS_CUBE_LOG.SET_PARAMETER

This procedure sets options that control various aspects of logging.

## Syntax

```sql
DBMS_CUBE_LOG.SET_PARAMETER (
          LOG_TYPE       IN   BINARY_INTEGER,
          LOG_PARAMETER  IN   BINARY_INTEGER,
          VALUE          IN   BINARY_INTEGER );
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| log_type | BINARY_INTEGER | IN | One of the following log types: 1 : TYPE_OPERATIONS 2 : TYPE_REJECTED_RECORDS 3 : TYPE_DIMENSION_COMPILE 4 : TYPE_BUILD See " Logging Types " . |
| log_parameter | BINARY_INTEGER | IN | One of the following parameters: 1 : MAX_ERRORS Maximum number of records before signalling an end to logging, such as the number of rejected records in the Cube Rejected Records log or the number of compilation errors in the dimension compilation error log. 2 : FLUSH_INTERVAL The number of seconds to buffer the records before writing them to a log. When this parameter is 0, the records are written directly to the logs without buffering. 3 : LOG_FULL_RECORD Controls logging of rejected records. Set this parameter to one of the following constants: 0 : FULL_RECORD_AUTO : Log the full record when no row ID is available. 1 : FULL_RECORD_ALWAYS : Always log the full record. 2 : FULL_RECORD_NEVER : Never log the full record. 4 : LOG_EVERY_N Enters a progress message every n rows during data maintenance. 5 : ALLOW_ERRORS : Displays logging errors, which are initially turned off to allow processing to proceed. |
| value | BINARY_INTEGER | IN | The new value of log_parameter . |

## Usage Notes

To obtain the current value of these options, use the GET_PARAMETER function. Syntax DBMS_CUBE_LOG.SET_PARAMETER ( LOG_TYPE IN BINARY_INTEGER, LOG_PARAMETER IN BINARY_INTEGER, VALUE IN BINARY_INTEGER ); Parameters Table 46-8 SET_PARAMETER Procedure Parameters Parameter Description log_type One of the following log types: 1 : TYPE_OPERATIONS 2 : TYPE_REJECTED_RECORDS 3 : TYPE_DIMENSION_COMPILE 4 : TYPE_BUILD See " Logging Types " . log_parameter One of the following parameters: 1 : MAX_ERRORS Maximum number of records before signalling an end to logging, such as the number of rejected records in the Cube Rejected Records log or the number of compilation errors in the dimension compilation error log. 2 : FLUSH_INTERVAL The number of seconds to buffer the records before writing them to a log. When this parameter is 0, the records are written directly to the logs without buffering. 3 : LOG_FULL_RECORD Controls logging of rejected records. Set this parameter to one of the following constants: 0 : FULL_RECORD_AUTO : Log the full record when no row ID is available. 1 : FULL_RECORD_ALWAYS : Always log the full record. 2 : FULL_RECORD_NEVER : Never log the full record. 4 : LOG_EVERY_N Enters a progress message every n rows during data maintenance. 5 : ALLOW_ERRORS : Displays logging errors, which are initially turned off to allow processing to proceed. value The new value of log_parameter . Examples This PL/SQL procedure sets the two parameters, then uses the GET_PARAMETER function to show the settings: BEGIN dbms_cube_log.set_parameter(dbms_cube_log.type_rejected_records, 1, 150); dbms_cube_log.set_parameter(dbms_cube_log.type_rejected_records, 2, 5); dbms_output.put_line('Max rejected records: ' || dbms_cube_log.get_parameter(dbms_cube_log.type_rejected_records, 1)); dbms_output.put_line('Buffer time: ' || dbms_cube_log.get_parameter(dbms_cube_log.type_rejected_records, 2) || ' seconds'); END; / The procedure displays this information: Max rejected records: 150 Buffer time: 5 seconds