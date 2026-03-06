---
id: 19c__DBMS_UTILITY.GET_ENDIANNESS
name: DBMS_UTILITY.GET_ENDIANNESS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_UTILITY
tags: [dbms_utility]
source_file: DBMS_UTILITY.html
---

# DBMS_UTILITY.GET_ENDIANNESS

This function gets the endianness of the database platform.

## Syntax

```sql
DBMS_UTILITY.GET_ENDIANNESS
   RETURN NUMBER;
```

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_UTILITY.GET_ENDIANNESS RETURN NUMBER; Return Values A NUMBER value indicating the endianness of the database platform: 1 for big-endian or 2 for little-endian.