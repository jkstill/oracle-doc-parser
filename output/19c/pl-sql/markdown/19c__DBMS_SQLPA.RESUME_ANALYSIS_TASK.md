---
id: 19c__DBMS_SQLPA.RESUME_ANALYSIS_TASK
name: DBMS_SQLPA.RESUME_ANALYSIS_TASK
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLPA
tags: [dbms_sqlpa]
source_file: DBMS_SQLPA.html
---

# DBMS_SQLPA.RESUME_ANALYSIS_TASK

This procedure resumes a previously interrupted or FAILED (with a fatal error) task execution.

## Syntax

```sql
DBMS_SQLPA.RESUME_ANALYSIS_TASK(
 task_name         IN VARCHAR2,
 basic_filter      IN VARCHAR2 := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN | Identifier of the analysis task to resume |
| basic_filter | VARCHAR2 | IN | A SQL predicate to filter the SQL from the SQL tuning set. Note that this filter will be applied in conjunction with the basic filter (parameter basic_filter ) that was specified when calling the CREATE_ANALYSIS_TASK Functions . |

## Usage Notes

Syntax DBMS_SQLPA.RESUME_ANALYSIS_TASK( task_name IN VARCHAR2, basic_filter IN VARCHAR2 := NULL); Parameters Table 166-9 RESUME_ANALYSIS_TASK Procedure Parameters Parameter Description task_name Identifier of the analysis task to resume basic_filter A SQL predicate to filter the SQL from the SQL tuning set. Note that this filter will be applied in conjunction with the basic filter (parameter basic_filter ) that was specified when calling the CREATE_ANALYSIS_TASK Functions . Usage Notes Resuming a single SQL analysis task (a task that was created to analyze a single SQL statement as compared to a SQL Tuning Set) is not supported. Examples -- Interrupt the task EXEC DBMS_SQLPA.INTERRUPT_ANALYSIS_TASK(:conc_task); -- Once a task is interrupted, we can elect to reset it, resume it, or check -- out its results and then decide. For this example we will just resume. EXEC DBMS_SQLPA.RESUME_ANALYSIS_TASK(:conc_task);