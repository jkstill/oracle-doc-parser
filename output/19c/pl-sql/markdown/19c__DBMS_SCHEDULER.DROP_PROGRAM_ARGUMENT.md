---
id: 19c__DBMS_SCHEDULER.DROP_PROGRAM_ARGUMENT
name: DBMS_SCHEDULER.DROP_PROGRAM_ARGUMENT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.DROP_PROGRAM_ARGUMENT

This procedure drops a program argument. An argument can be specified by either name (if one has been given) or position.

## Syntax

```sql
DBMS_SCHEDULER.DROP_PROGRAM_ARGUMENT (
   program_name            IN VARCHAR2,
   argument_position       IN PLS_INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| program_name | VARCHAR2 | IN | The name of the program to be altered. A program with this name must exist. |
| argument_name |  |  | The name of the argument being dropped |
| argument_position | PLS_INTEGER) | IN | The position of the argument to be dropped |

## Usage Notes

The procedure is overloaded. Syntax Drops a program argument by position: DBMS_SCHEDULER.DROP_PROGRAM_ARGUMENT ( program_name IN VARCHAR2, argument_position IN PLS_INTEGER); Drops a program argument by name: DBMS_SCHEDULER.DROP_PROGRAM_ARGUMENT ( program_name IN VARCHAR2, argument_name IN VARCHAR2); Parameters Table 151-55 DROP_PROGRAM_ARGUMENT Procedure Parameters Parameter Description program_name The name of the program to be altered. A program with this name must exist. argument_name The name of the argument being dropped argument_position The position of the argument to be dropped Usage Notes Dropping a program argument requires that you be the owner of the program or have ALTER privileges on that program. You can also drop a program argument if you have the CREATE ANY JOB privilege.