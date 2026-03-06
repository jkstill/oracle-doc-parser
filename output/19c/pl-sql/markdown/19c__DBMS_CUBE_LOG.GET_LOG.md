---
id: 19c__DBMS_CUBE_LOG.GET_LOG
name: DBMS_CUBE_LOG.GET_LOG
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CUBE_LOG
tags: [dbms_cube_log]
source_file: DBMS_CUBE_LOG.html
---

# DBMS_CUBE_LOG.GET_LOG

This procedure returns the current settings for the level and location of a particular log.

## Syntax

```sql
DBMS_CUBE_LOG.GET_LOG (
          LOG_TYPE       IN   BINARY_INTEGER  DEFAULT TYPE_OPERATIONS,
          LOG_TARGET     IN   BINARY_INTEGER  DEFAULT TARGET_TABLE,
          LOG_LEVEL      OUT  BINARY_INTEGER,
          LOG_LOCATION   OUT  VARCHAR2 );
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| log_type | BINARY_INTEGER | IN | One of the following log types: 1 : TYPE_OPERATIONS 2 : TYPE_REJECTED_RECORDS 3 : TYPE_DIMENSION_COMPILE See " Logging Types " . |
| log_target | BINARY_INTEGER | IN | One of the following destinations for the logging records. The logs are sent to a table unless you previously specified a different target using the ENABLE procedure. 1 : TARGET_TABLE 2 : TARGET_TRACE 3 : TARGET_FILE 4 : TARGET_LOB See " Logging Targets " |
| log_level | BINARY_INTEGER | OUT | One of the following log verbosity levels. Each level adds new types of messages to the previous level. 1 : LEVEL_LOWEST 2 : LEVEL_LOW 3 : LEVEL_MEDIUM 4 : LEVEL_HIGH 5 : LEVEL_HIGHEST See " Verbosity Levels " . |
| log_location | VARCHAR2 | OUT | The full identity of the log, such as owner.table_name when log_target is a table. |

## Usage Notes

Syntax DBMS_CUBE_LOG.GET_LOG ( LOG_TYPE IN BINARY_INTEGER DEFAULT TYPE_OPERATIONS, LOG_TARGET IN BINARY_INTEGER DEFAULT TARGET_TABLE, LOG_LEVEL OUT BINARY_INTEGER, LOG_LOCATION OUT VARCHAR2 ); Parameters Table 46-5 GET_LOG Procedure Parameters Parameter Description log_type One of the following log types: 1 : TYPE_OPERATIONS 2 : TYPE_REJECTED_RECORDS 3 : TYPE_DIMENSION_COMPILE See " Logging Types " . log_target One of the following destinations for the logging records. The logs are sent to a table unless you previously specified a different target using the ENABLE procedure. 1 : TARGET_TABLE 2 : TARGET_TRACE 3 : TARGET_FILE 4 : TARGET_LOB See " Logging Targets " log_level One of the following log verbosity levels. Each level adds new types of messages to the previous level. 1 : LEVEL_LOWEST 2 : LEVEL_LOW 3 : LEVEL_MEDIUM 4 : LEVEL_HIGH 5 : LEVEL_HIGHEST See " Verbosity Levels " . log_location The full identity of the log, such as owner.table_name when log_target is a table. Usage Notes If log_type is not active, then log_level and log_location are null. Use DBMS_CUBE_LOG.ENABLE to activate a log. Examples This PL/SQL procedure provides information about the Cube Rejected Records log: SET serverout ON format wrapped DECLARE myloglevel binary_integer; mylogtarget varchar2(128); BEGIN dbms_cube_log.get_log(dbms_cube_log.type_rejected_records, dbms_cube_log.target_table, myloglevel, mylogtarget); dbms_output.put_line('Log Level: ' || myloglevel); dbms_output.put_line('Log Target: ' || mylogtarget); END; / The procedure generates results like the following: Log Level: 5 Log Target: GLOBAL.CUBE_REJECTED_RECORDS