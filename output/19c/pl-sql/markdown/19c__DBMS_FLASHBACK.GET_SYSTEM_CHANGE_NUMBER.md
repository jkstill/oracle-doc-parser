---
id: 19c__DBMS_FLASHBACK.GET_SYSTEM_CHANGE_NUMBER
name: DBMS_FLASHBACK.GET_SYSTEM_CHANGE_NUMBER
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_FLASHBACK
tags: [dbms_flashback]
source_file: DBMS_FLASHBACK.html
---

# DBMS_FLASHBACK.GET_SYSTEM_CHANGE_NUMBER

This function returns the current SCN as an Oracle number datatype. You can obtain the current change number and store it for later use. This helps you retain specific snapshots.

## Syntax

```sql
DBMS_FLASHBACK.GET_SYSTEM_CHANGE_NUMBER
 RETURN NUMBER;
```

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_FLASHBACK.GET_SYSTEM_CHANGE_NUMBER RETURN NUMBER;