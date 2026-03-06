---
id: 19c__DBMS_SQLTUNE.RESUME_TUNING_TASK
name: DBMS_SQLTUNE.RESUME_TUNING_TASK
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLTUNE
tags: [dbms_sqltune]
source_file: DBMS_SQLTUNE.html
---

# DBMS_SQLTUNE.RESUME_TUNING_TASK

This procedure resumes a previously interrupted task that was created to process a SQL tuning set.

## Syntax

```sql
DBMS_SQLTUNE.RESUME_TUNING_TASK(
 task_name         IN VARCHAR2,
 basic_filter      IN VARCHAR2 := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN | The name of the tuning task to resume. |
| basic_filter | VARCHAR2 | IN | A SQL predicate to filter the SQL from the SQL tuning set. Note that this filter is applied in conjunction with the parameter basic_filter i when calling CREATE_TUNING_TASK Functions . |

## Usage Notes

See Also: DBMS_SQLTUNE SQL Tuning Advisor Subprograms for other subprograms in this group See Also: DBMS_SQLTUNE SQL Tuning Advisor Subprograms for other subprograms in this group Syntax DBMS_SQLTUNE.RESUME_TUNING_TASK( task_name IN VARCHAR2, basic_filter IN VARCHAR2 := NULL); Parameters Table 169-38 RESUME_TUNING_TASK Procedure Parameters Parameter Description task_name The name of the tuning task to resume. basic_filter A SQL predicate to filter the SQL from the SQL tuning set. Note that this filter is applied in conjunction with the parameter basic_filter i when calling CREATE_TUNING_TASK Functions . Usage Notes Resuming a single SQL tuning task (a task that was created to tune a single SQL statement as compared to a SQL tuning set) is not supported.