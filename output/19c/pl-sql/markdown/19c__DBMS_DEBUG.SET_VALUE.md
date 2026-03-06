---
id: 19c__DBMS_DEBUG.SET_VALUE
name: DBMS_DEBUG.SET_VALUE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DEBUG
tags: [dbms_debug]
source_file: DBMS_DEBUG.html
---

# DBMS_DEBUG.SET_VALUE

This function sets a value in the currently-running program. There are two overloaded SET_VALUE functions.

## Syntax

```sql
DBMS_DEBUG.SET_VALUE (
   frame#               IN binary_integer,
   assignment_statement IN varchar2) 
  RETURN BINARY_INTEGER;

DBMS_DEBUG.SET_VALUE (
   handle               IN program_info,
   assignment_statement IN VARCHAR2) 
  RETURN BINARY_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| frame# | binary_integer | IN | Frame in which the value is to be set; 0 means the currently executing frame. |
| handle | program_info | IN | Description of the package containing the variable |
| assignment_statement | varchar2) | IN | An assignment statement (which must be legal PL/SQL) to run in order to set the value. For example, 'x := 3;'. Only scalar values are supported in this release. The right side of the assignment statement must be a scalar. |

**Returns:** `BINARY_INTEGER`

## Usage Notes

Syntax DBMS_DEBUG.SET_VALUE ( frame# IN binary_integer, assignment_statement IN varchar2) RETURN BINARY_INTEGER; DBMS_DEBUG.SET_VALUE ( handle IN program_info, assignment_statement IN VARCHAR2) RETURN BINARY_INTEGER; Parameters Table 57-49 SET_VALUE Function Parameters Parameter Description frame# Frame in which the value is to be set; 0 means the currently executing frame. handle Description of the package containing the variable assignment_statement An assignment statement (which must be legal PL/SQL) to run in order to set the value. For example, 'x := 3;'. Only scalar values are supported in this release. The right side of the assignment statement must be a scalar. Return Values Table 57-50 SET_VALUE Function Return Values Return Description success - error_illegal_value Not possible to set it to that value error_illegal_null Cannot set to NULL because object type specifies it as 'not NULL ' error_value_malformed Value is not a scalar error_name_incomplete The assignment statement does not resolve to a scalar. For example, 'x := 3;', if x is a record. error_no_such_object One of the following: - Package does not exist - Package is not instantiated - User does not have privileges to debug the package - Object does not exist in the package Usage Notes In some cases, the PL/SQL compiler uses temporaries to access package variables, and does not guarantee to update such temporaries. It is possible, although unlikely, that modification to a package variable using SET_VALUE might not take effect for a line or two. Examples To set the value of SCOTT . PACK . var to 6: DECLARE handle dbms_debug.program_info; retval BINARY_INTEGER; BEGIN handle.Owner := 'SCOTT'; handle.Name := 'PACK'; handle.namespace := dbms_debug.namespace_pkgspec_or_toplevel; retval := dbms_debug.set_value(handle, 'var := 6;'); END;