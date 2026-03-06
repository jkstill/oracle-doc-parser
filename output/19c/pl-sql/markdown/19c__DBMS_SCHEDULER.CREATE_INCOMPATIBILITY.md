---
id: 19c__DBMS_SCHEDULER.CREATE_INCOMPATIBILITY
name: DBMS_SCHEDULER.CREATE_INCOMPATIBILITY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.CREATE_INCOMPATIBILITY

This procedure creates an incompatibility definition.

## Syntax

```sql
DBMS_SCHEDULER.CREATE_INCOMPATIBILITY (
   incompatibility_name    IN VARCHAR2,
   object_name             IN VARCHAR2,
   constraint_level        IN VARCHAR2 DEFAULT 'JOB_LEVEL',
   enabled                 IN BOOLEAN DEFAULT TRUE,
   comments                IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| incompatibility_name | VARCHAR2 | IN | The name of the incompatibility definition. |
| object_name | VARCHAR2 | IN | One or more (comma-separated) programs or jobs. |
| constraint_level | VARCHAR2 | IN | One or more (comma-separated) programs or jobs. |
| enabled | BOOLEAN | IN | Specifies whether the constraint is initially enabled ( true ) or not enabled ( false ). |
| comments | VARCHAR2 | IN | Optional descriptive comment. |

## Usage Notes

Syntax DBMS_SCHEDULER.CREATE_INCOMPATIBILITY ( incompatibility_name IN VARCHAR2, object_name IN VARCHAR2, constraint_level IN VARCHAR2 DEFAULT 'JOB_LEVEL', enabled IN BOOLEAN DEFAULT TRUE, comments IN VARCHAR2 DEFAULT NULL); Parameters Table 151-27 CREATE_INCOMPATIBILITY Procedure Parameters Parameter Description incompatibility_name The name of the incompatibility definition. object_name One or more (comma-separated) programs or jobs. constraint_level One or more (comma-separated) programs or jobs. enabled Specifies whether the constraint is initially enabled ( true ) or not enabled ( false ). comments Optional descriptive comment. Usage Notes If object_name contains multiple (comma-separated) values, they must be either all programs or all jobs that are incompatible with each other (that is, they cannot be run at the same time). For jobs, the list must consist of two or more jobs, and constraint_level must be ‘JOB_LEVEL’. For programs, constraint_level can be either 'JOB_LEVEL' or ' PROGRAM_LEVEL' . When set to the default value 'JOB_LEVEL’ , only a single job that is based on the program (or programs) mentioned in object_name can run at the same time. When constraint_level is set to 'PROGRAM_LEVEL' , the programs are incompatible, but the jobs based on the same program are not incompatible. For example, if the value of object_name is 'P1,P2,P3' and constraint_level is 'PROGRAM_LEVEL’ , many jobs based on P1 can be running at the same time, but if any P1 based job is running, none based on P2 or P3 can be running. Or, similarly, many jobs based on P3 can be running at the same time, but none based on P1 or P2. If constraint_level is set to 'JOB_LEVEL' , then only a single job out of all the jobs based on programs P1, P2 and P3 can be running at a time. See Also: Using Incompatibility Definitions in Oracle Database Administrator’s Guide See Also: Using Incompatibility Definitions in Oracle Database Administrator’s Guide