---
id: 19c__DBMS_UTILITY.FORMAT_CALL_STACK
name: DBMS_UTILITY.FORMAT_CALL_STACK
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_UTILITY
tags: [dbms_utility]
source_file: DBMS_UTILITY.html
---

# DBMS_UTILITY.FORMAT_CALL_STACK

This function formats the current call stack. This can be used on any stored procedure or trigger to access the call stack. This can be useful for debugging.

## Syntax

```sql
DBMS_UTILITY.FORMAT_CALL_STACK 
  RETURN VARCHAR2;
```

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_UTILITY.FORMAT_CALL_STACK RETURN VARCHAR2; Pragmas pragma restrict_references(format_call_stack,WNDS); Return Values This returns the call stack, up to 2000 bytes.