---
id: 19c__DBMS_SCHEDULER.SET_JOB_ARGUMENT_VALUE
name: DBMS_SCHEDULER.SET_JOB_ARGUMENT_VALUE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.SET_JOB_ARGUMENT_VALUE

This procedure sets the value of an argument for a job.

## Syntax

```sql
DBMS_SCHEDULER.SET_JOB_ARGUMENT_VALUE (
   job_name                IN VARCHAR2,
   argument_position       IN PLS_INTEGER,
   argument_value          IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| job_name | VARCHAR2 | IN | The name of the job to be altered |
| argument_name |  |  | The name of the program argument being set |
| argument_position | PLS_INTEGER | IN | The position of the program argument being set |
| argument_value | VARCHAR2) | IN | The new value to be set for the program argument. To set a non- VARCHAR value, use the SET_JOB_ANYDATA_VALUE procedure. |

## Usage Notes

It overrides any default value set for the corresponding program or stored procedure argument. The argument can be specified by position or by name. You can specify by name only when: The job points to a saved program object The argument was assigned a name with the DEFINE_PROGRAM_ARGUMENT Procedure or the DEFINE_METADATA_ARGUMENT Procedure Scheduler does no type checking of the argument at any time. SET_JOB_ARGUMENT_VALUE is overloaded. Syntax Sets an argument value by position: DBMS_SCHEDULER.SET_JOB_ARGUMENT_VALUE ( job_name IN VARCHAR2, argument_position IN PLS_INTEGER, argument_value IN VARCHAR2); Sets an argument value by name: DBMS_SCHEDULER.SET_JOB_ARGUMENT_VALUE ( job_name IN VARCHAR2, argument_name IN VARCHAR2, argument_value IN VARCHAR2); Parameters Table 151-98 SET_JOB_ARGUMENT_VALUE Procedure Parameters Parameter Description job_name The name of the job to be altered argument_name The name of the program argument being set argument_position The position of the program argument being set argument_value The new value to be set for the program argument. To set a non- VARCHAR value, use the SET_JOB_ANYDATA_VALUE procedure. Usage Notes SET_JOB_ARGUMENT_VALUE requires that you be the owner of the job or have ALTER privileges on that job. You can also set a job argument value if you have the CREATE ANY JOB privilege. SET_JOB_ARGUMENT_VALUE only supports arguments of SQL type. Therefore, argument values that are not of SQL type, such as booleans, are not supported as program or job arguments. SET_JOB_ARGUMENT_VALUE can be used to set arguments of lightweight jobs but only if the argument is of type VARCHAR2 . See Also: " SET_JOB_ANYDATA_VALUE Procedure " " DEFINE_PROGRAM_ARGUMENT Procedure " See Also: " SET_JOB_ANYDATA_VALUE Procedure " " DEFINE_PROGRAM_ARGUMENT Procedure "