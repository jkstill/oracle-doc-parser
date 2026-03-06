---
id: 19c__DBMS_SCHEDULER.RESET_JOB_ARGUMENT_VALUE
name: DBMS_SCHEDULER.RESET_JOB_ARGUMENT_VALUE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.RESET_JOB_ARGUMENT_VALUE

This procedure resets (clears) the value previously set to an argument for a job.

## Syntax

```sql
DBMS_SCHEDULER.RESET_JOB_ARGUMENT_VALUE (
   job_name                IN VARCHAR2,
   argument_position       IN PLS_INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| job_name | VARCHAR2 | IN | The name of the job being altered |
| argument_position | PLS_INTEGER) | IN | The position of the program argument being reset |
| argument_name |  |  | The name of the program argument being reset |

## Usage Notes

RESET_JOB_ARGUMENT_VALUE is overloaded. Syntax Clears a previously set job argument value by argument position: DBMS_SCHEDULER.RESET_JOB_ARGUMENT_VALUE ( job_name IN VARCHAR2, argument_position IN PLS_INTEGER); Clears a previously set job argument value by argument name: DBMS_SCHEDULER.RESET_JOB_ARGUMENT_VALUE ( job_name IN VARCHAR2, argument_name IN VARCHAR2); Parameters Table 151-77 RESET_JOB_ARGUMENT_VALUE Procedure Parameters Parameter Description job_name The name of the job being altered argument_position The position of the program argument being reset argument_name The name of the program argument being reset Usage Notes If the corresponding program argument has no default value, the job is disabled. Resetting a program argument of a job belonging to another user requires ALTER privileges on that job. Arguments can be specified by position or by name. RESET_JOB_ARGUMENT_VALUE requires that you be the owner of the job or have ALTER privileges on that job. You can also reset a job argument value if you have the CREATE ANY JOB privilege. RESET_JOB_ARGUMENT_VALUE only supports arguments of SQL type. Therefore, argument values that are not of SQL type, such as booleans, are not supported as program or job arguments.