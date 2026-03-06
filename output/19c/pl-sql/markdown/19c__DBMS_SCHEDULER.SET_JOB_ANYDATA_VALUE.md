---
id: 19c__DBMS_SCHEDULER.SET_JOB_ANYDATA_VALUE
name: DBMS_SCHEDULER.SET_JOB_ANYDATA_VALUE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.SET_JOB_ANYDATA_VALUE

This procedure sets the value for an argument of the associated program for a job, encapsulated in an AnyData object.

## Syntax

```sql
DBMS_SCHEDULER.SET_JOB_ANYDATA_VALUE (
   job_name                IN VARCHAR2,
   argument_position       IN PLS_INTEGER,
   argument_value          IN SYS.ANYDATA);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| job_name | VARCHAR2 | IN | The name of the job to be altered |
| argument_name |  |  | The name of the program argument being set |
| argument_position | PLS_INTEGER | IN | The position of the program argument being set |
| argument_value | SYS.ANYDATA) | IN | The new value to be assigned to the program argument, encapsulated in an AnyData object |

## Usage Notes

It overrides any default value set for the program argument. NULL is a valid assignment for a program argument. The argument can be specified by position or by name. You can specify by name only when: The job points to a saved program object The argument was assigned a name with the DEFINE_ANYDATA_ARGUMENT Procedure Scheduler does no type checking of the argument at any time. SET_JOB_ANYDATA_VALUE is overloaded. Syntax Sets a program argument by its position. DBMS_SCHEDULER.SET_JOB_ANYDATA_VALUE ( job_name IN VARCHAR2, argument_position IN PLS_INTEGER, argument_value IN SYS.ANYDATA); Sets a program argument by its name. DBMS_SCHEDULER.SET_JOB_ANYDATA_VALUE ( job_name IN VARCHAR2, argument_name IN VARCHAR2, argument_value IN SYS.ANYDATA); Parameters Table 151-97 SET_JOB_ANYDATA_VALUE Procedure Parameters Parameter Description job_name The name of the job to be altered argument_name The name of the program argument being set argument_position The position of the program argument being set argument_value The new value to be assigned to the program argument, encapsulated in an AnyData object Usage Notes SET_JOB_ANYDATA_VALUE requires that you own the job or have ALTER privileges on that job. You can also set a job argument value if you have the CREATE ANY JOB privilege. SET_JOB_ANYDATA_VALUE does not apply to lightweight jobs because lightweight jobs cannot take AnyData arguments. See Also: " SET_JOB_ARGUMENT_VALUE Procedure " " DEFINE_ANYDATA_ARGUMENT Procedure " See Also: " SET_JOB_ARGUMENT_VALUE Procedure " " DEFINE_ANYDATA_ARGUMENT Procedure "