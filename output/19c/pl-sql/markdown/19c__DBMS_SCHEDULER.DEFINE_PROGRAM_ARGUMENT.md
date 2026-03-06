---
id: 19c__DBMS_SCHEDULER.DEFINE_PROGRAM_ARGUMENT
name: DBMS_SCHEDULER.DEFINE_PROGRAM_ARGUMENT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.DEFINE_PROGRAM_ARGUMENT

This procedure defines a name or default value for a program argument. If no default value is defined for a program argument, the job that references the program must supply an argument value. (The job can also override a default value.)

## Syntax

```sql
PROCEDURE define_program_argument(
   program_name            IN VARCHAR2,
   argument_position       IN PLS_INTEGER,
   argument_name           IN VARCHAR2 DEFAULT NULL,
   argument_type           IN VARCHAR2,
   out_argument            IN BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| program_name | VARCHAR2 | IN | The name of the program to be altered. A program with this name must exist. |
| argument_position | PLS_INTEGER | IN | The position of the argument as it is passed to the executable. Argument numbers go from one to the number_of_arguments specified for the program. This must be unique so it replaces any argument already defined at this position. |
| argument_name | VARCHAR2 | IN | The name to assign to the argument. It is optional, but must be unique for the program if specified. If you assign a name, the name can then be used by other package procedures, including the SET_JOB_ARGUMENT_VALUE Procedure . |
| argument_type | VARCHAR2 | IN | The datatype of the argument being defined. This is not verified or used by the Scheduler. The program user uses argument_type when deciding what value to assign to the argument. Any valid SQL datatype is allowed. |
| default_value |  |  | The default value to be assigned to the argument if none is specified by the job. |
| out_argument | BOOLEAN | IN | This parameter is reserved for future use. It must be set to FALSE . |

## Usage Notes

This procedure is overloaded. Syntax Defines a program argument without a default value: PROCEDURE define_program_argument( program_name IN VARCHAR2, argument_position IN PLS_INTEGER, argument_name IN VARCHAR2 DEFAULT NULL, argument_type IN VARCHAR2, out_argument IN BOOLEAN DEFAULT FALSE); Defines a program argument with a default value: PROCEDURE define_program_argument( program_name IN VARCHAR2, argument_position IN PLS_INTEGER, argument_name IN VARCHAR2 DEFAULT NULL, argument_type IN VARCHAR2, default_value IN VARCHAR2, out_argument IN BOOLEAN DEFAULT FALSE); Parameters Table 151-41 DEFINE_PROGRAM_ARGUMENT Procedure Parameters Parameter Description program_name The name of the program to be altered. A program with this name must exist. argument_position The position of the argument as it is passed to the executable. Argument numbers go from one to the number_of_arguments specified for the program. This must be unique so it replaces any argument already defined at this position. argument_name The name to assign to the argument. It is optional, but must be unique for the program if specified. If you assign a name, the name can then be used by other package procedures, including the SET_JOB_ARGUMENT_VALUE Procedure . argument_type The datatype of the argument being defined. This is not verified or used by the Scheduler. The program user uses argument_type when deciding what value to assign to the argument. Any valid SQL datatype is allowed. default_value The default value to be assigned to the argument if none is specified by the job. out_argument This parameter is reserved for future use. It must be set to FALSE . Usage Notes All program arguments from 1 to the number_of_arguments value must be defined before a program can be enabled. If a default value for an argument is not defined with this procedure, a value must be defined in the job. Defining a program argument requires that you be the owner of the program or have ALTER privileges on that program. You can also define a program argument if you have the CREATE ANY JOB privilege. DEFINE_PROGRAM_ARGUMENT only supports arguments of SQL type. Therefore, argument values that are not of SQL type, such as booleans, are not supported as program or job arguments. See Also: " DEFINE_ANYDATA_ARGUMENT Procedure " " SET_JOB_ARGUMENT_VALUE Procedure " See Also: " DEFINE_ANYDATA_ARGUMENT Procedure " " SET_JOB_ARGUMENT_VALUE Procedure "