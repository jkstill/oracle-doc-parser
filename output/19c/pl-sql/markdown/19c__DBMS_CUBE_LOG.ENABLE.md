---
id: 19c__DBMS_CUBE_LOG.ENABLE
name: DBMS_CUBE_LOG.ENABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CUBE_LOG
tags: [dbms_cube_log]
source_file: DBMS_CUBE_LOG.html
---

# DBMS_CUBE_LOG.ENABLE

This procedure turns on logging for the duration of a session or until it is turned off using the DISABLE procedure.

## Syntax

```sql
DBMS_CUBE_LOG.ENABLE (
          LOG_TYPE       IN     BINARY_INTEGER  DEFAULT NULL,
          LOG_TARGET     IN     BINARY_INTEGER  DEFAULT NULL,
          LOG_LEVEL      IN     BINARY_INTEGER  DEFAULT NULL);

DBMS_CUBE_LOG.ENABLE (
          LOG_TYPE       IN     BINARY_INTEGER  DEFAULT NULL,
          LOG_TARGET     IN     BINARY_INTEGER  DEFAULT NULL,
          LOG_LEVEL      IN     BINARY_INTEGER  DEFAULT NULL, 
          LOG_LOCATION   IN     VARCHAR2        DEFAULT NULL);

DBMS_CUBE_LOG.ENABLE (
          LOG_TYPE       IN     BINARY_INTEGER  DEFAULT NULL,
          LOG_TARGET     IN     BINARY_INTEGER  DEFAULT NULL,
          LOG_LEVEL      IN     BINARY_INTEGER  DEFAULT NULL, 
          LOG_LOCATION   IN/OUT CLOB );
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| log_type | BINARY_INTEGER | IN | One of the following log types: 1 : TYPE_OPERATIONS 2 : TYPE_REJECTED_RECORDS 3 : TYPE_DIMENSION_COMPILE Note : You cannot disable the Cube Build log with this procedure. See " Logging Types " . |
| log_target | BINARY_INTEGER | IN | One of the following destinations for the logging records. The logs are sent to a table unless you previously specified a different target using the ENABLE procedure. 1 : TARGET_TABLE 2 : TARGET_TRACE 3 : TARGET_FILE 4 : TARGET_LOB See " Logging Targets " |
| log_level | BINARY_INTEGER | IN | One of the following log verbosity levels. Each level adds new types of messages to the previous level. 1 : LEVEL_LOWEST 2 : LEVEL_LOW 3 : LEVEL_MEDIUM 4 : LEVEL_HIGH 5 : LEVEL_HIGHEST See " Verbosity Levels " . |
| log_location | VARCHAR2 | IN | The full identity of the log, such as owner.table_name when log_target is a table. |

## Usage Notes

The ENABLE procedure also allows you to direct logging to additional output types and to change the amount of detail in the logs. You can enable a log type to each of the log targets. For example, you can enable the Cube Operations log to the trace file, a table, and a file at different verbosity levels, but you cannot enable the Cube Operations log to two files at the same time. This procedure also checks the format of the logs and updates them if necessary. Syntax DBMS_CUBE_LOG.ENABLE ( LOG_TYPE IN BINARY_INTEGER DEFAULT NULL, LOG_TARGET IN BINARY_INTEGER DEFAULT NULL, LOG_LEVEL IN BINARY_INTEGER DEFAULT NULL); DBMS_CUBE_LOG.ENABLE ( LOG_TYPE IN BINARY_INTEGER DEFAULT NULL, LOG_TARGET IN BINARY_INTEGER DEFAULT NULL, LOG_LEVEL IN BINARY_INTEGER DEFAULT NULL, LOG_LOCATION IN VARCHAR2 DEFAULT NULL); DBMS_CUBE_LOG.ENABLE ( LOG_TYPE IN BINARY_INTEGER DEFAULT NULL, LOG_TARGET IN BINARY_INTEGER DEFAULT NULL, LOG_LEVEL IN BINARY_INTEGER DEFAULT NULL, LOG_LOCATION IN/OUT CLOB ); Parameters Table 46-4 ENABLE Procedure Parameters Parameter Description log_type One of the following log types: 1 : TYPE_OPERATIONS 2 : TYPE_REJECTED_RECORDS 3 : TYPE_DIMENSION_COMPILE Note : You cannot disable the Cube Build log with this procedure. See " Logging Types " . log_target One of the following destinations for the logging records. The logs are sent to a table unless you previously specified a different target using the ENABLE procedure. 1 : TARGET_TABLE 2 : TARGET_TRACE 3 : TARGET_FILE 4 : TARGET_LOB See " Logging Targets " log_level One of the following log verbosity levels. Each level adds new types of messages to the previous level. 1 : LEVEL_LOWEST 2 : LEVEL_LOW 3 : LEVEL_MEDIUM 4 : LEVEL_HIGH 5 : LEVEL_HIGHEST See " Verbosity Levels " . log_location The full identity of the log, such as owner.table_name when log_target is a table. Examples The following command enables all cube logs: EXECUTE dbms_cube_log.enable; The following PL/SQL procedure sets the log level to LEVEL_LOWEST : BEGIN dbms_cube_log.disable(dbms_cube_log.type_rejected_records); dbms_cube_log.enable(dbms_cube_log.type_rejected_records, dbms_cube_log.target_table, dbms_cube_log.level_lowest); END; /