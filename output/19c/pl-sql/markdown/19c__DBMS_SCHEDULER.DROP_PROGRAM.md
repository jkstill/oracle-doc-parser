---
id: 19c__DBMS_SCHEDULER.DROP_PROGRAM
name: DBMS_SCHEDULER.DROP_PROGRAM
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.DROP_PROGRAM

This procedure drops a program. Any arguments that pertain to the program are also dropped when the program is dropped.

## Syntax

```sql
DBMS_SCHEDULER.DROP_PROGRAM (
   program_name            IN VARCHAR2,
   force                   IN BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| program_name | VARCHAR2 | IN | The name of the program to be dropped. Can be a comma-delimited list. |
| force | BOOLEAN | IN | If force is set to FALSE , the program must not be referenced by any job, otherwise an error occurs. If force is set to TRUE , all jobs referencing the program are disabled before the program is dropped. Running jobs that point to the program are not affected by the DROP_PROGRAM call and are allowed to continue. |

## Usage Notes

Syntax DBMS_SCHEDULER.DROP_PROGRAM ( program_name IN VARCHAR2, force IN BOOLEAN DEFAULT FALSE); Parameters Table 151-54 DROP_PROGRAM Procedure Parameters Parameter Description program_name The name of the program to be dropped. Can be a comma-delimited list. force If force is set to FALSE , the program must not be referenced by any job, otherwise an error occurs. If force is set to TRUE , all jobs referencing the program are disabled before the program is dropped. Running jobs that point to the program are not affected by the DROP_PROGRAM call and are allowed to continue. Usage Notes Dropping a program requires that you be the owner of the program or have ALTER privileges on that program. You can also drop a program if you have the CREATE ANY JOB privilege.