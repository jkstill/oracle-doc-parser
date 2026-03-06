---
id: 19c__DBMS_DESCRIBE.DESCRIBE_
name: DBMS_DESCRIBE.DESCRIBE_
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DESCRIBE
tags: [dbms_describe]
source_file: DBMS_DESCRIBE.html
---

# DBMS_DESCRIBE.DESCRIBE_

The procedure DESCRIBE_PROCEDURE provides a brief description of a PL/SQL stored procedure.

## Syntax

```sql
DBMS_DESCRIBE.DESCRIBE_PROCEDURE(
   object_name                   IN  VARCHAR2,
   reserved1                     IN  VARCHAR2,
   reserved2                     IN  VARCHAR2,
   overload                      OUT NUMBER_TABLE,
   position                      OUT NUMBER_TABLE,
   level                         OUT NUMBER_TABLE,
   argument_name                 OUT VARCHAR2_TABLE,
   datatype                      OUT NUMBER_TABLE,
   default_value                 OUT NUMBER_TABLE,
   in_out                        OUT NUMBER_TABLE,
   length                        OUT NUMBER_TABLE,
   precision                     OUT NUMBER_TABLE,
   scale                         OUT NUMBER_TABLE,
   radix                         OUT NUMBER_TABLE,
   spare                         OUT NUMBER_TABLE
   include_string_constraints    OUT BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| object_name | VARCHAR2 | IN | Name of the procedure being described. The syntax for this parameter follows the rules used for identifiers in SQL. The name can be a synonym. This parameter is required and may not be null. The total length of the name cannot exceed 197 bytes. An incorrectly specified OBJECT_NAME can result in one of the following exceptions: ORA-20000 - A package was specified. You can only specify a stored procedure, stored function, packaged procedure, or packaged function. ORA-20001 - The procedure or function that you specified does not exist within the given package. ORA-20002 - The object that you specified is a remote object. This procedure cannot currently describe remote objects. ORA-20003 - The object that you specified is invalid and cannot be described. ORA-20004 - The object was specified with a syntax error. |
| reserved1 reserved2 |  |  | Reserved for future use -- must be set to NULL or the empty string. |
| overload | NUMBER_TABLE | OUT | A unique number assigned to the procedure's signature. If a procedure is overloaded, then this field holds a different value for each version of the procedure. |
| position | NUMBER_TABLE | OUT | Position of the argument in the parameter list. Position 0 returns the values for the return type of a function. |
| level | NUMBER_TABLE | OUT | If the argument is a composite type, such as record, then this parameter returns the level of the datatype. See the Oracle Call Interface Programmer's Guide for a description of the ODESSP call for an example. |
| argument_name | VARCHAR2_TABLE | OUT | Name of the argument associated with the procedure that you are describing. |
| datatype | NUMBER_TABLE | OUT | Oracle datatype of the argument being described. The datatypes and their numeric type codes are: 0 placeholder for procedures with no arguments 1 VARCHAR, VARCHAR, STRING 2 NUMBER, INTEGER, SMALLINT, REAL, FLOAT, DECIMAL 3 BINARY_INTEGER, PLS_INTEGER, POSITIVE, NATURAL 8 LONG 11 ROWID 12 DATE 23 RAW 24 LONG RAW 58 OPAQUE TYPE 96 CHAR (ANSI FIXED CHAR), CHARACTER 106 MLSLABEL 121 OBJECT 122 NESTED TABLE 123 VARRAY 178 TIME 179 TIME WITH TIME ZONE 180 TIMESTAMP 181 TIMESTAMP WITH TIME ZONE 231 TIMESTAMP WITH LOCAL TIME ZONE 250 PL/SQL RECORD 251 PL/SQL TABLE 252 PL/SQL BOOLEAN |
| default_value | NUMBER_TABLE | OUT | 1 if the argument being described has a default value; otherwise, the value is 0. |
| in_out | NUMBER_TABLE | OUT | Describes the mode of the parameter: 0 IN 1 OUT 2 IN OUT |
| length | NUMBER_TABLE | OUT | For %rowtype formal arguments, the length constraint is returned, otherwise 0 is returned.If the include_string_constraints parameter is set to TRUE, the argument's formal length constraint is passed back if it is of the appropriate type. Those are the string types: 1;8;23;24;96 |
| precision | NUMBER_TABLE | OUT | If the argument being described is of datatype 2 ( NUMBER ), then this parameter is the precision of that number. |
| scale | NUMBER_TABLE | OUT | If the argument being described is of datatype 2 ( NUMBER ), then this parameter is the scale of that number. |
| radix | NUMBER_TABLE | OUT | If the argument being described is of datatype 2 ( NUMBER ), then this parameter is the radix of that number. |
| spare | NUMBER_TABLE | OUT | Reserved for future functionality. |
| include_string_constraints | BOOLEAN | OUT | The default is FALSE . If the parameter is set to TRUE , the arguments' formal type constraints is passed back if it is of the appropriate type.Those are the string types: 1;8;23;24;96 |

## Usage Notes

It takes the name of a stored procedure and returns information about each parameter of that procedure. Syntax DBMS_DESCRIBE.DESCRIBE_PROCEDURE( object_name IN VARCHAR2, reserved1 IN VARCHAR2, reserved2 IN VARCHAR2, overload OUT NUMBER_TABLE, position OUT NUMBER_TABLE, level OUT NUMBER_TABLE, argument_name OUT VARCHAR2_TABLE, datatype OUT NUMBER_TABLE, default_value OUT NUMBER_TABLE, in_out OUT NUMBER_TABLE, length OUT NUMBER_TABLE, precision OUT NUMBER_TABLE, scale OUT NUMBER_TABLE, radix OUT NUMBER_TABLE, spare OUT NUMBER_TABLE include_string_constraints OUT BOOLEAN DEFAULT FALSE); Parameters Table 60-3 DBMS_DESCRIBE.DESCRIBE_PROCEDURE Parameters Parameter Description object_name Name of the procedure being described. The syntax for this parameter follows the rules used for identifiers in SQL. The name can be a synonym. This parameter is required and may not be null. The total length of the name cannot exceed 197 bytes. An incorrectly specified OBJECT_NAME can result in one of the following exceptions: ORA-20000 - A package was specified. You can only specify a stored procedure, stored function, packaged procedure, or packaged function. ORA-20001 - The procedure or function that you specified does not exist within the given package. ORA-20002 - The object that you specified is a remote object. This procedure cannot currently describe remote objects. ORA-20003 - The object that you specified is invalid and cannot be described. ORA-20004 - The object was specified with a syntax error. reserved1 reserved2 Reserved for future use -- must be set to NULL or the empty string. overload A unique number assigned to the procedure's signature. If a procedure is overloaded, then this field holds a different value for each version of the procedure. position Position of the argument in the parameter list. Position 0 returns the values for the return type of a function. level If the argument is a composite type, such as record, then this parameter returns the level of the datatype. See the Oracle Call Interface Programmer's Guide for a description of the ODESSP call for an example. argument_name Name of the argument associated with the procedure that you are describing. datatype Oracle datatype of the argument being described. The datatypes and their numeric type codes are: 0 placeholder for procedures with no arguments 1 VARCHAR, VARCHAR, STRING 2 NUMBER, INTEGER, SMALLINT, REAL, FLOAT, DECIMAL 3 BINARY_INTEGER, PLS_INTEGER, POSITIVE, NATURAL 8 LONG 11 ROWID 12 DATE 23 RAW 24 LONG RAW 58 OPAQUE TYPE 96 CHAR (ANSI FIXED CHAR), CHARACTER 106 MLSLABEL 121 OBJECT 122 NESTED TABLE 123 VARRAY 178 TIME 179 TIME WITH TIME ZONE 180 TIMESTAMP 181 TIMESTAMP WITH TIME ZONE 231 TIMESTAMP WITH LOCAL TIME ZONE 250 PL/SQL RECORD 251 PL/SQL TABLE 252 PL/SQL BOOLEAN default_value 1 if the argument being described has a default value; otherwise, the value is 0. in_out Describes the mode of the parameter: 0 IN 1 OUT 2 IN OUT length For %rowtype formal arguments, the length constraint is returned, otherwise 0 is returned.If the include_string_constraints parameter is set to TRUE, the argument's formal length constraint is passed back if it is of the appropriate type. Those are the string types: 1;8;23;24;96 precision If the argument being described is of datatype 2 ( NUMBER ), then this parameter is the precision of that number. scale If the argument being described is of datatype 2 ( NUMBER ), then this parameter is the scale of that number. radix If the argument being described is of datatype 2 ( NUMBER ), then this parameter is the radix of that number. spare Reserved for future functionality. include_string_constraints The default is FALSE . If the parameter is set to TRUE , the arguments' formal type constraints is passed back if it is of the appropriate type.Those are the string types: 1;8;23;24;96 Return Values All values from DESCRIBE_PROCEDURE are returned in its OUT parameters. The datatypes for these are PL/SQL tables, to accommodate a variable number of parameters.