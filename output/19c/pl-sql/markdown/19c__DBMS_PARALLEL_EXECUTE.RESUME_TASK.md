---
id: 19c__DBMS_PARALLEL_EXECUTE.RESUME_TASK
name: DBMS_PARALLEL_EXECUTE.RESUME_TASK
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PARALLEL_EXECUTE
tags: [dbms_parallel_execute]
source_file: DBMS_PARALLEL_EXECUTE.html
---

# DBMS_PARALLEL_EXECUTE.RESUME_TASK

This procedure retries the specified the task if the RUN_TASK Procedure finished with an error, or resumes the task if a crash occurred.

## Syntax

```sql
DBMS_PARALLEL_EXECUTE.RESUME_TASK (
   task_name                     IN  VARCHAR2,
   sql_stmt                      IN  CLOB,   
   language_flag                 IN  NUMBER,
   edition                       IN  VARCHAR2  DEFAULT NULL,
   apply_crossedition_trigger    IN  VARCHAR2  DEFAULT NULL,
   fire_apply_trigger            IN  BOOLEAN   DEFAULT TRUE,
   parallel_level                IN  NUMBER    DEFAULT 0,
   job_class                     IN  VARCHAR2  DEFAULT 'DEFAULT_JOB_CLASS',
   force                         IN  BOOLEAN   DEFAULT FALSE);

DBMS_PARALLEL_EXECUTE.RESUME_TASK (
   task_name                     IN  VARCHAR2,
   force                         IN  BOOLEAN   DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN | Name of the task |
| sql_stmt | CLOB | IN | SQL statement; must have :start_id and :end_id placeholders |
| language_flag | NUMBER | IN | Determines how Oracle handles the SQL statement. The following options are recognized: V6 (or 0) specifies version 6 behavior NATIVE (or 1) specifies normal behavior for the database to which the program is connected V7 (or 2) specifies Oracle database version 7 behavior |
| edition | VARCHAR2 | IN | Specifies the edition in which to run the statement. Default is the current edition. |
| apply_crossedition_trigger | VARCHAR2 | IN | Specifies the unqualified name of a forward crossedition trigger that is to be applied to the specified SQL. The name is resolved using the edition and current_schema setting in which the statement is to be executed. The trigger must be owned by the user who executes the statement. |
| fire_apply_trigger | BOOLEAN | IN | Indicates whether the specified apply_crossedition_trigger is itself to be executed, or only to used as be a guide in selecting other triggers |
| parallel_level | NUMBER | IN | Number of parallel jobs; zero if run in serial; NULL uses the default parallelism |
| job_class | VARCHAR2 | IN | If running in parallel, the jobs all belong to the specified job class |
| force | BOOLEAN | IN | If TRUE , do not raise an error if the status is PROCESSING . |

## Usage Notes

You can only invoke this procedure if the task is in a CRASHED or FINISHED_WITH_ERROR state. For a crashed serial execution, the state remains in PROCESSING . The FORCE option allows you to resume any task in PROCESSING state. However, it is your responsibility to determine that a crash has occurred. The procedure resumes processing the chunks which have not been processed. Also, chunks which are in PROCESSED_WITH_ERROR or ASSIGNED (due to crash) state are processed because those chunks did not commit. This procedure takes the same argument as the RUN_TASK Procedure . The overload which takes task_name as the only input argument re-uses the arguments provided in the previous invoking of the RUN_TASK Procedure or RESUME_TASK Procedures . See Also: Table 121-2 See Also: Table 121-2 Syntax DBMS_PARALLEL_EXECUTE.RESUME_TASK ( task_name IN VARCHAR2, sql_stmt IN CLOB, language_flag IN NUMBER, edition IN VARCHAR2 DEFAULT NULL, apply_crossedition_trigger IN VARCHAR2 DEFAULT NULL, fire_apply_trigger IN BOOLEAN DEFAULT TRUE, parallel_level IN NUMBER DEFAULT 0, job_class IN VARCHAR2 DEFAULT 'DEFAULT_JOB_CLASS', force IN BOOLEAN DEFAULT FALSE); DBMS_PARALLEL_EXECUTE.RESUME_TASK ( task_name IN VARCHAR2, force IN BOOLEAN DEFAULT FALSE); Parameters Table 121-19 RESUME_TASK Procedure Parameters Parameter Description task_name Name of the task sql_stmt SQL statement; must have :start_id and :end_id placeholders language_flag Determines how Oracle handles the SQL statement. The following options are recognized: V6 (or 0) specifies version 6 behavior NATIVE (or 1) specifies normal behavior for the database to which the program is connected V7 (or 2) specifies Oracle database version 7 behavior edition Specifies the edition in which to run the statement. Default is the current edition. apply_crossedition_trigger Specifies the unqualified name of a forward crossedition trigger that is to be applied to the specified SQL. The name is resolved using the edition and current_schema setting in which the statement is to be executed. The trigger must be owned by the user who executes the statement. fire_apply_trigger Indicates whether the specified apply_crossedition_trigger is itself to be executed, or only to used as be a guide in selecting other triggers parallel_level Number of parallel jobs; zero if run in serial; NULL uses the default parallelism job_class If running in parallel, the jobs all belong to the specified job class force If TRUE , do not raise an error if the status is PROCESSING . Examples Suppose the chunk table contains the following chunk ranges: START_ID END_ID --------------------------- --------------------------- 1 10 11 20 21 30 And the specified SQL statement is: UPDATE employees SET salary = salary + 10 WHERE e.employee_id BETWEEN :start_id AND :end_id This procedure executes the following statements in parallel: UPDATE employees SET salary =.salary + 10 WHERE employee_id BETWEEN 1 and 10; COMMIT; UPDATE employees SET salary =.salary + 10 WHERE employee_id between 11 and 20; COMMIT; UPDATE employees SET salary =.salary + 10 WHERE employee_id between 21 and 30; COMMIT;