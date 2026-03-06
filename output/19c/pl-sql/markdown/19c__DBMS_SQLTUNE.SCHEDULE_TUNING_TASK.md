---
id: 19c__DBMS_SQLTUNE.SCHEDULE_TUNING_TASK
name: DBMS_SQLTUNE.SCHEDULE_TUNING_TASK
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLTUNE
tags: [dbms_sqltune]
source_file: DBMS_SQLTUNE.html
---

# DBMS_SQLTUNE.SCHEDULE_TUNING_TASK

This function creates a tuning task for a single SQL statement and schedules a DBMS_SCHEDULER job to execute the tuning task. One form of the function finds the information about the statement to be tuned in the shared SQL area, whereas the other finds the information in AWR.

## Syntax

```sql
DBMS_SQLTUNE.SCHEDULE_TUNING_TASK(
  sql_id          IN VARCHAR2,
  plan_hash_value IN NUMBER                   := NULL,
  start_date      IN TIMESTAMP WITH TIME ZONE := NULL,   
  scope           IN VARCHAR2                 := SCOPE_COMPREHENSIVE,   
  time_limit      IN NUMBER                   := TIME_LIMIT_DEFAULT,
  task_name       IN VARCHAR2                 := NULL,    
  description     IN VARCHAR2                 := NULL,
  con_name        IN VARCHAR2                 := NULL)
RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| begin_snap |  |  | The beginning snapshot identifier. The range is exclusive, which means that SQL statements in this snapshot ID are not included. |
| end_snap |  |  | The end snapshot identifier. The range is inclusive, which means that SQL statements in this snapshot ID are included. |
| sql_id | VARCHAR2 | IN | The SQL ID of the statement to be tuned. |
| plan_hash_value | NUMBER | IN | The plan hash value of the statement to be tuned. For example, the tuning job fetches captured binds for this SQL plan. |
| start_date | TIMESTAMP | IN | The date on which the schedule becomes valid. If null, then SQL Tuning Advisor immediately executes the task. |
| scope | VARCHAR2 | IN | The scope of the tuning job: limited, or comprehensive. |
| time_limit | NUMBER | IN | The maximum duration in seconds for the SQL tuning session. |
| task_name | VARCHAR2 | IN | Optional SQL tuning task name. |
| description | VARCHAR2 | IN | Description of the SQL tuning session. The description can contain a maximum of 256 characters. |
| con_name | VARCHAR2 | IN | The container from which SQL Tuning Advisor accesses the SQL statement information. |
| dbid |  |  | DBID for imported or PDB-level AWR data. If NULL , then the current database DBID is used. |

**Returns:** `VARCHAR2`

## Usage Notes

See Also: DBMS_SQLTUNE SQL Tuning Advisor Subprograms for other subprograms in this group See Also: DBMS_SQLTUNE SQL Tuning Advisor Subprograms for other subprograms in this group Syntax Shared SQL Area Format: DBMS_SQLTUNE.SCHEDULE_TUNING_TASK( sql_id IN VARCHAR2, plan_hash_value IN NUMBER := NULL, start_date IN TIMESTAMP WITH TIME ZONE := NULL, scope IN VARCHAR2 := SCOPE_COMPREHENSIVE, time_limit IN NUMBER := TIME_LIMIT_DEFAULT, task_name IN VARCHAR2 := NULL, description IN VARCHAR2 := NULL, con_name IN VARCHAR2 := NULL) RETURN VARCHAR2; AWR Format: DBMS_SQLTUNE.SCHEDULE_TUNING_TASK( begin_snap IN NUMBER, end_snap IN NUMBER, sql_id IN VARCHAR2, plan_hash_value IN NUMBER := NULL, start_date IN TIMESTAMP WITH TIME ZONE := NULL, scope IN VARCHAR2 := SCOPE_COMPREHENSIVE, time_limit IN NUMBER := TIME_LIMIT_DEFAULT, task_name IN VARCHAR2 := NULL, description IN VARCHAR2 := NULL, con_name IN VARCHAR2 := NULL, dbid IN NUMBER := NULL) RETURN VARCHAR2; Parameters Table 169-39 SCHEDULE_TUNING_TASK Function Parameters Parameter Description begin_snap The beginning snapshot identifier. The range is exclusive, which means that SQL statements in this snapshot ID are not included. end_snap The end snapshot identifier. The range is inclusive, which means that SQL statements in this snapshot ID are included. sql_id The SQL ID of the statement to be tuned. plan_hash_value The plan hash value of the statement to be tuned. For example, the tuning job fetches captured binds for this SQL plan. start_date The date on which the schedule becomes valid. If null, then SQL Tuning Advisor immediately executes the task. scope The scope of the tuning job: limited, or comprehensive. time_limit The maximum duration in seconds for the SQL tuning session. task_name Optional SQL tuning task name. description Description of the SQL tuning session. The description can contain a maximum of 256 characters. con_name The container from which SQL Tuning Advisor accesses the SQL statement information. dbid DBID for imported or PDB-level AWR data. If NULL , then the current database DBID is used. Security Model The caller must possess the CREATE JOB privilege for the job.