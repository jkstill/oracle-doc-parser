---
id: 19c__DBMS_RESUMABLE.SET_TIMEOUT
name: DBMS_RESUMABLE.SET_TIMEOUT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESUMABLE
tags: [dbms_resumable]
source_file: DBMS_RESUMABLE.html
---

# DBMS_RESUMABLE.SET_TIMEOUT

This procedure sets the timeout of resumable space allocations for the current session. The new timeout setting applies to the session immediately.

## Syntax

```sql
DBMS_RESUMABLE.SET_TIMEOUT (
   timeout  IN NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| timeout | NUMBER) | IN | The timeout of the resumable space allocation. |

## Usage Notes

Syntax DBMS_RESUMABLE.SET_TIMEOUT ( timeout IN NUMBER); Parameters Table 145-7 SET_TIMEOUT Procedure Parameters Parameter Description timeout The timeout of the resumable space allocation.