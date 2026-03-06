---
id: 19c__DBMS_PARALLEL_EXECUTE.RUN_TASK
name: DBMS_PARALLEL_EXECUTE.RUN_TASK
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PARALLEL_EXECUTE
tags: [dbms_parallel_execute]
source_file: DBMS_PARALLEL_EXECUTE.html
---

# DBMS_PARALLEL_EXECUTE.RUN_TASK

This procedure executes the specified statement ( sql_stmt ) on the chunks in parallel.

## Syntax

```sql
DBMS_PARALLEL_EXECUTE.RUN_TASK (
   task_name                     IN  VARCHAR2,
   sql_stmt                      IN  CLOB,
   language_flag                 IN  NUMBER,
   edition                       IN  VARCHAR2  DEFAULT NULL,
   apply_crossedition_trigger    IN  VARCHAR2  DEFAULT NULL,
   fire_apply_trigger            IN  BOOLEAN   DEFAULT TRUE,
   parallel_level                IN  NUMBER    DEFAULT 0,
   job_class                     IN  VARCHAR2  DEFAULT 'DEFAULT_JOB_CLASS');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN | Name of the task |
| sql_stmt | CLOB | IN | SQL statement; must have :start_id and :end_id placeholders |
| language_flag | NUMBER | IN | Determines how Oracle handles the SQL statement. The following options are recognized: V6 (or 0) specifies version 6 behavior NATIVE (or 1) specifies normal behavior for the database to which the program is connected V7 (or 2) specifies Oracle database version 7 behavior |
| edition | VARCHAR2 | IN | Specifies the edition in which to run the statement. Default is the current edition. |
| apply_crossedition_trigger | VARCHAR2 | IN | Specifies the unqualified name of a forward crossedition trigger that is to be applied to the specified SQL. The name is resolved using the edition and current_schema setting in which the statement is to be executed. The trigger must be owned by the user executes the statement. |
| fire_apply_trigger | BOOLEAN | IN | Indicates whether the specified apply_crossedition_trigger is itself to be executed, or only a guide to be used in selecting other triggers. |
| parallel_level | NUMBER | IN | Number of parallel jobs; zero if run in serial; NULL uses the default parallelism. |
| job_class | VARCHAR2 | IN | If running in parallel, the jobs belong to the specified job class |

## Usage Notes

It commits after processing each chunk. The specified statement must have two placeholders called start_id and end_id, respectively, which represent the range of the chunk to be processed. The type of each placeholder must be ROWID where ROWID -based chunking was used, or NUMBER where NUMBER -based chunking was used. Syntax DBMS_PARALLEL_EXECUTE.RUN_TASK ( task_name IN VARCHAR2, sql_stmt IN CLOB, language_flag IN NUMBER, edition IN VARCHAR2 DEFAULT NULL, apply_crossedition_trigger IN VARCHAR2 DEFAULT NULL, fire_apply_trigger IN BOOLEAN DEFAULT TRUE, parallel_level IN NUMBER DEFAULT 0, job_class IN VARCHAR2 DEFAULT 'DEFAULT_JOB_CLASS'); Parameters Table 121-20 RUN_TASK Procedure Parameters Parameter Description task_name Name of the task sql_stmt SQL statement; must have :start_id and :end_id placeholders language_flag Determines how Oracle handles the SQL statement. The following options are recognized: V6 (or 0) specifies version 6 behavior NATIVE (or 1) specifies normal behavior for the database to which the program is connected V7 (or 2) specifies Oracle database version 7 behavior edition Specifies the edition in which to run the statement. Default is the current edition. apply_crossedition_trigger Specifies the unqualified name of a forward crossedition trigger that is to be applied to the specified SQL. The name is resolved using the edition and current_schema setting in which the statement is to be executed. The trigger must be owned by the user executes the statement. fire_apply_trigger Indicates whether the specified apply_crossedition_trigger is itself to be executed, or only a guide to be used in selecting other triggers. parallel_level Number of parallel jobs; zero if run in serial; NULL uses the default parallelism. job_class If running in parallel, the jobs belong to the specified job class Usage Notes The SQL statement is executed as the current user. Since this subprogram is subject to reexecution on error, you need to take great care in submitting a statement to RUN_TASK that is not idempotent. Chunks can be executed in parallel by DBMS_SCHEDULER job slaves. Therefore, parallel execution requires CREATE JOB system privilege. The job slaves is created under the current user. The default number of job slaves is computed as the product of Oracle parameters cpu_count and parallel_threads_per_cpu . On a Real Application Clusters installation, the number of job slaves is the sum of individual settings on each node in the cluster. This procedure returns only when all the chunks are processed. In parallel cases, this procedure returns only when all the job slaves finished. Examples Suppose the chunk table contains the following chunk ranges: START_ID END_ID --------------------------- --------------------------- 1 10 11 20 21 30 And the specified SQL statement is: UPDATE employees SET salary = salary + 10 WHERE e.employee_id BETWEEN :start_id AND :end_id This procedure executes the following statements in parallel: UPDATE employees SET salary =.salary + 10 WHERE employee_id BETWEEN 1 and 10; COMMIT; UPDATE employees SET salary =.salary + 10 WHERE employee_id between 11 and 20; COMMIT; UPDATE employees SET salary =.salary + 10 WHERE employee_id between 21 and 30; COMMIT;