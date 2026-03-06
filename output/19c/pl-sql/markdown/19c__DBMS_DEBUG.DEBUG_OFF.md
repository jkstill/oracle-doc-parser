---
id: 19c__DBMS_DEBUG.DEBUG_OFF
name: DBMS_DEBUG.DEBUG_OFF
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DEBUG
tags: [dbms_debug]
source_file: DBMS_DEBUG.html
---

# DBMS_DEBUG.DEBUG_OFF

This procedure notifies the target session that debugging should no longer take place in that session. It is not necessary to call this function before ending the session.

## Syntax

```sql
DBMS_DEBUG.DEBUG_OFF;
```

## Usage Notes

WARNING: There must be a debug session waiting if immediate is TRUE . WARNING: There must be a debug session waiting if immediate is TRUE . Syntax DBMS_DEBUG.DEBUG_OFF; Usage Notes The server does not handle this entrypoint specially. Therefore, it attempts to debug this entrypoint.