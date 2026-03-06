---
id: 19c__DBMS_DEBUG.GET_VALUE
name: DBMS_DEBUG.GET_VALUE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DEBUG
tags: [dbms_debug]
source_file: DBMS_DEBUG.html
---

# DBMS_DEBUG.GET_VALUE

This function gets a value from the currently-running program. There are two overloaded GET_VALUE functions.

## Syntax

```sql
DBMS_DEBUG.GET_VALUE (
   variable_name  IN  VARCHAR2,
   frame#         IN  BINARY_INTEGER,
   scalar_value   OUT VARCHAR2,
   format         IN  VARCHAR2 := NULL)
RETURN BINARY_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| variable_name | VARCHAR2 | IN | Name of the variable or parameter |
| frame# | BINARY_INTEGER | IN | Frame in which it lives; 0 means the current procedure |
| scalar_value | VARCHAR2 | OUT | Value |
| format | VARCHAR2 | IN | Optional date format to use, if meaningful |

**Returns:** `BINARY_INTEGER`

## Usage Notes

Syntax DBMS_DEBUG.GET_VALUE ( variable_name IN VARCHAR2, frame# IN BINARY_INTEGER, scalar_value OUT VARCHAR2, format IN VARCHAR2 := NULL) RETURN BINARY_INTEGER; Parameters Table 57-33 GET_VALUE Function Parameters Parameter Description variable_name Name of the variable or parameter frame# Frame in which it lives; 0 means the current procedure scalar_value Value format Optional date format to use, if meaningful Return Values Table 57-34 GET_VALUE Function Return Values Return Description success A successful completion error_bogus_frame Frame does not exist error_no_debug_info Entrypoint has no debug information error_no_such_object variable_name does not exist in frame# error_unknown_type The type information in the debug information is illegible error_nullvalue Value is NULL error_indexed_table The object is a table, but no index was provided This form of GET_VALUE is for fetching package variables. Instead of a frame#, it takes a handle, which describes the package containing the variable. Syntax DBMS_DEBUG.GET_VALUE ( variable_name IN VARCHAR2, handle IN program_info, scalar_value OUT VARCHAR2, format IN VARCHAR2 := NULL) RETURN BINARY_INTEGER; Parameters Table 57-35 GET_VALUE Function Parameters Parameter Description variable_name Name of the variable or parameter handle Description of the package containing the variable scalar_value Value format Optional date format to use, if meaningful