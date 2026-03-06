---
id: 19c__DBMS_UTILITY.FORMAT_ERROR_STACK
name: DBMS_UTILITY.FORMAT_ERROR_STACK
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_UTILITY
tags: [dbms_utility]
source_file: DBMS_UTILITY.html
---

# DBMS_UTILITY.FORMAT_ERROR_STACK

This function formats the current error stack. This can be used in exception handlers to look at the full error stack.

## Syntax

```sql
DBMS_UTILITY.FORMAT_ERROR_STACK 
  RETURN VARCHAR2;
```

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_UTILITY.FORMAT_ERROR_STACK RETURN VARCHAR2; Return Values This returns the error stack, up to 2000 bytes.