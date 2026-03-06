---
id: 19c__DBMS_RESUMABLE.ABORT
name: DBMS_RESUMABLE.ABORT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESUMABLE
tags: [dbms_resumable]
source_file: DBMS_RESUMABLE.html
---

# DBMS_RESUMABLE.ABORT

This procedure aborts a suspended resumable space allocation.

## Syntax

```sql
DBMS_RESUMABLE.ABORT (
   session_id  IN NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| session_id | NUMBER) | IN | The session identifier of the resumable space allocation. |

## Usage Notes

The parameter session_id is the session ID in which the statement is executed. For a parallel DML/DDL, session_id is any session ID that participates in the parallel DML/DDL. This operation is guaranteed to succeed. The procedure can be called either inside or outside of the AFTER SUSPEND trigger. Syntax DBMS_RESUMABLE.ABORT ( session_id IN NUMBER); Parameters Table 145-2 ABORT Procedure Parameters Parameter Description session_id The session identifier of the resumable space allocation. Usage Notes To call an ABORT procedure, you must be the owner of the session with session_id, have ALTER SYSTEM privileges, or be a DBA.