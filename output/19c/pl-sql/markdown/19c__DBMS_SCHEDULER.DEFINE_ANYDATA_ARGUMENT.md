---
id: 19c__DBMS_SCHEDULER.DEFINE_ANYDATA_ARGUMENT
name: DBMS_SCHEDULER.DEFINE_ANYDATA_ARGUMENT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.DEFINE_ANYDATA_ARGUMENT

This procedure defines a name or default value for a program argument that is of a complex type and must be encapsulated within an ANYDATA object. A job that references the program can override the default value.

## Syntax

```sql
DBMS_SCHEDULER.DEFINE_ANYDATA_ARGUMENT (
   program_name            IN VARCHAR2,
   argument_position       IN PLS_INTEGER,
   argument_name           IN VARCHAR2 DEFAULT NULL,
   argument_type           IN VARCHAR2,
   default_value           IN SYS.ANYDATA,
   out_argument            IN BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| program_name | VARCHAR2 | IN | The name of the program to be altered. A program with this name must exist. |
| argument_position | PLS_INTEGER | IN | The position of the argument as it is passed to the executable. Argument numbers go from one to the number_of_arguments specified for the program. This must be unique, so it can replace any argument already defined at this position. |
| argument_name | VARCHAR2 | IN | The name to assign to the argument. It is optional, but must be unique for the program if it is specified. If you assign a name, the name can then be used by other package procedures, including the SET_JOB_ANYDATA_VALUE Procedure . |
| argument_type | VARCHAR2 | IN | The datatype of the argument being defined. This is not verified or used by the Scheduler. It is only used by the user of the program when deciding what value to assign to the argument. |
| default_value | SYS.ANYDATA | IN | The default value to be assigned to the argument encapsulated within an AnyData object. This is optional. |
| out_argument | BOOLEAN | IN | This parameter is reserved for future use. It must be set to FALSE . |

## Usage Notes

Syntax DBMS_SCHEDULER.DEFINE_ANYDATA_ARGUMENT ( program_name IN VARCHAR2, argument_position IN PLS_INTEGER, argument_name IN VARCHAR2 DEFAULT NULL, argument_type IN VARCHAR2, default_value IN SYS.ANYDATA, out_argument IN BOOLEAN DEFAULT FALSE); Parameters Table 151-35 DEFINE_ANYDATA_ARGUMENT Procedure Parameters Parameter Description program_name The name of the program to be altered. A program with this name must exist. argument_position The position of the argument as it is passed to the executable. Argument numbers go from one to the number_of_arguments specified for the program. This must be unique, so it can replace any argument already defined at this position. argument_name The name to assign to the argument. It is optional, but must be unique for the program if it is specified. If you assign a name, the name can then be used by other package procedures, including the SET_JOB_ANYDATA_VALUE Procedure . argument_type The datatype of the argument being defined. This is not verified or used by the Scheduler. It is only used by the user of the program when deciding what value to assign to the argument. default_value The default value to be assigned to the argument encapsulated within an AnyData object. This is optional. out_argument This parameter is reserved for future use. It must be set to FALSE . Usage Notes All program arguments from one to the number_of_arguments value must be defined before a program can be enabled. If a default value for an argument is not defined with this procedure, a value must be defined in the job. Defining a program argument requires that you be the owner of the program or have ALTER privileges on that program. You can also define a program argument if you have the CREATE ANY JOB privilege. See Also: " DEFINE_PROGRAM_ARGUMENT Procedure " " SET_JOB_ANYDATA_VALUE Procedure " See Also: " DEFINE_PROGRAM_ARGUMENT Procedure " " SET_JOB_ANYDATA_VALUE Procedure "