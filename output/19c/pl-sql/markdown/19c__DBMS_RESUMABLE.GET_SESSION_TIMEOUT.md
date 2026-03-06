---
id: 19c__DBMS_RESUMABLE.GET_SESSION_TIMEOUT
name: DBMS_RESUMABLE.GET_SESSION_TIMEOUT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESUMABLE
tags: [dbms_resumable]
source_file: DBMS_RESUMABLE.html
---

# DBMS_RESUMABLE.GET_SESSION_TIMEOUT

This function returns the current timeout value of resumable space allocations for a session with session_id.

## Syntax

```sql
DBMS_RESUMABLE.GET_SESSION_TIMEOUT (
   session_id  IN NUMBER)
RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| session_id | NUMBER) | IN | The session identifier of the resumable space allocation. |

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_RESUMABLE.GET_SESSION_TIMEOUT ( session_id IN NUMBER) RETURN NUMBER; Parameters Table 145-3 GET_SESSION_TIMEOUT Function Parameters Parameter Description session_id The session identifier of the resumable space allocation. Return Values Table 145-4 GET_SESSION_TIMEOUT Function Return Values Return Value Description NUMBER The current timeout value of resumable space allocations for a session with session_id. The timeout is returned in seconds. Usage Notes If session_id does not exist, the GET_SESSION_TIMEOUT function returns -1.