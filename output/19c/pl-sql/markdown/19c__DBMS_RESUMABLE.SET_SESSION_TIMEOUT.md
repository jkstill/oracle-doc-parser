---
id: 19c__DBMS_RESUMABLE.SET_SESSION_TIMEOUT
name: DBMS_RESUMABLE.SET_SESSION_TIMEOUT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESUMABLE
tags: [dbms_resumable]
source_file: DBMS_RESUMABLE.html
---

# DBMS_RESUMABLE.SET_SESSION_TIMEOUT

This procedure sets the timeout of resumable space allocations for a session with session_id .

## Syntax

```sql
DBMS_RESUMABLE.SET_SESSION_TIMEOUT (
   session_id  IN NUMBER,
   timeout     IN NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| session_id | NUMBER | IN | The session identifier of the resumable space allocation. |
| timeout | NUMBER) | IN | The timeout of the resumable space allocation. |

## Usage Notes

The new timeout setting applies to the session immediately. If session_id does not exist, no operation occurs. Syntax DBMS_RESUMABLE.SET_SESSION_TIMEOUT ( session_id IN NUMBER, timeout IN NUMBER); Parameters Table 145-6 SET_SESSION_TIMEOUT Procedure Parameters Parameter Description session_id The session identifier of the resumable space allocation. timeout The timeout of the resumable space allocation.