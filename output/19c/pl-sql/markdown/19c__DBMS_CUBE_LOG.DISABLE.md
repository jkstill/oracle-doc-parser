---
id: 19c__DBMS_CUBE_LOG.DISABLE
name: DBMS_CUBE_LOG.DISABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CUBE_LOG
tags: [dbms_cube_log]
source_file: DBMS_CUBE_LOG.html
---

# DBMS_CUBE_LOG.DISABLE

This procedure turns logging off for the duration of a session, unless logging is explicitly turned on again with the ENABLE procedure.

## Syntax

```sql
DBMS_CUBE_LOG.DISABLE (
          LOG_TYPE       IN   BINARY_INTEGER  DEFAULT,
          LOG_TARGET     IN   BINARY_INTEGER  DEFAULT);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| log_type | BINARY_INTEGER | IN | One of the following log types: 1 : TYPE_OPERATIONS 2 : TYPE_REJECTED_RECORDS 3 : TYPE_DIMENSION_COMPILE Note : You cannot disable the Cube Build log with this procedure. See " Logging Types " . |
| log_target | BINARY_INTEGER | IN | One of the following destinations for the logging records. The logs are sent to a table unless you previously specified a different target using the ENABLE procedure. 1 : TARGET_TABLE 2 : TARGET_TRACE 3 : TARGET_FILE 4 : TARGET_LOB See " Logging Targets " |

## Usage Notes

Syntax DBMS_CUBE_LOG.DISABLE ( LOG_TYPE IN BINARY_INTEGER DEFAULT, LOG_TARGET IN BINARY_INTEGER DEFAULT); Parameters Table 46-3 DISABLE Procedure Parameters Parameter Description log_type One of the following log types: 1 : TYPE_OPERATIONS 2 : TYPE_REJECTED_RECORDS 3 : TYPE_DIMENSION_COMPILE Note : You cannot disable the Cube Build log with this procedure. See " Logging Types " . log_target One of the following destinations for the logging records. The logs are sent to a table unless you previously specified a different target using the ENABLE procedure. 1 : TARGET_TABLE 2 : TARGET_TRACE 3 : TARGET_FILE 4 : TARGET_LOB See " Logging Targets " Example This command disables the dimension compilation error log table: EXECUTE dbms_cube_log.disable(dbms_cube_log.type_dimension_compile);