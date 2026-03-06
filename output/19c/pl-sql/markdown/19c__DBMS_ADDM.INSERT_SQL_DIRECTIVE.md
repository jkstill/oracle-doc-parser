---
id: 19c__DBMS_ADDM.INSERT_SQL_DIRECTIVE
name: DBMS_ADDM.INSERT_SQL_DIRECTIVE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADDM
tags: [dbms_addm]
source_file: DBMS_ADDM.html
---

# DBMS_ADDM.INSERT_SQL_DIRECTIVE

This procedure creates a directive to limit reporting of actions on specific SQL. The directive can be created for a specific task (only when the task is in INITIAL status), or for all subsequently created ADDM tasks (such as a system directive).

## Syntax

```sql
DBMS_ADDM.INSERT_SQL_DIRECTIVE (
   task_name             IN VARCHAR2,
   dir_name              IN VARCHAR2,
   sql_id                IN VARCHAR2,
   min_active_sessions   IN NUMBER := 0,
   min_response_time     IN NUMBER := 0);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN | Name of the task this directive applies to. If the value is NULL , it applies to all subsequently created ADDM Tasks. |
| dir_name | VARCHAR2 | IN | Name of the directive. All directives must be given unique names. |
| sql_id | VARCHAR2 | IN | Identifies which SQL statement to filter. A valid value contains exactly 13 characters from '0' to '9' and 'a' to 'z'. |
| min_active_sessions | NUMBER | IN | Minimal number of active sessions for the SQL. If a SQL action has less than this number, it is filtered from the ADDM result. |
| min_response_time | NUMBER | IN | Minimal value for response time of the SQL (in microseconds). If the SQL had lower response time, it is filtered from the ADDM result. |

## Usage Notes

Syntax DBMS_ADDM.INSERT_SQL_DIRECTIVE ( task_name IN VARCHAR2, dir_name IN VARCHAR2, sql_id IN VARCHAR2, min_active_sessions IN NUMBER := 0, min_response_time IN NUMBER := 0); Parameters Table 14-19 INSERT_SQL_DIRECTIVE Procedure Parameters Parameter Description task_name Name of the task this directive applies to. If the value is NULL , it applies to all subsequently created ADDM Tasks. dir_name Name of the directive. All directives must be given unique names. sql_id Identifies which SQL statement to filter. A valid value contains exactly 13 characters from '0' to '9' and 'a' to 'z'. min_active_sessions Minimal number of active sessions for the SQL. If a SQL action has less than this number, it is filtered from the ADDM result. min_response_time Minimal value for response time of the SQL (in microseconds). If the SQL had lower response time, it is filtered from the ADDM result. Examples A new ADDM task is created to analyze a local instance. However, it has special treatment for SQL with id 'abcd123456789'. The result of GET_REPORT shows only actions for that SQL (actions to tune the SQL, or to investigate application using it) if the SQL is responsible for at least 2 average active sessions during the analysis period, and the average response time was at least 1 second. var tname VARCHAR2(60); BEGIN DBMS_ADDM.INSERT_SQL_DIRECTIVE( NULL, 'my SQL directive', 'abcd123456789', 2, 1000000); :tname := 'my_instance_analysis_mode_task'; DBMS_ADDM.ANALYZE_INST(:tname, 1, 2); END; To see a report containing all actions regardless of the directive: SELECT DBMS_ADVISOR.GET_TASK_REPORT(:tname, 'TEXT', 'ALL') FROM DUAL;