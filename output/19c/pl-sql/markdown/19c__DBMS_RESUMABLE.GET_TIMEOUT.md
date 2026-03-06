---
id: 19c__DBMS_RESUMABLE.GET_TIMEOUT
name: DBMS_RESUMABLE.GET_TIMEOUT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESUMABLE
tags: [dbms_resumable]
source_file: DBMS_RESUMABLE.html
---

# DBMS_RESUMABLE.GET_TIMEOUT

This function returns the current timeout value of resumable space allocations for the current session.

## Syntax

```sql
DBMS_RESUMABLE.GET_TIMEOUT
 RETURN NUMBER;
```

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_RESUMABLE.GET_TIMEOUT RETURN NUMBER; Return Values Table 145-5 GET_TIMEOUT Function Return Values Return Value Description NUMBER The current timeout value of resumable space allocations for the current session. The returned value is in seconds. Usage Notes If the current session is not resumable enabled, the GET_TIMEOUT function returns -1.