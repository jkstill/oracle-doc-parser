---
id: 19c__DBMS_DEBUG.DETACH_SESSION
name: DBMS_DEBUG.DETACH_SESSION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DEBUG
tags: [dbms_debug]
source_file: DBMS_DEBUG.html
---

# DBMS_DEBUG.DETACH_SESSION

This procedure stops debugging the target program.

## Syntax

```sql
DBMS_DEBUG.DETACH_SESSION;
```

## Usage Notes

This procedure may be called at any time, but it does not notify the target session that the debug session is detaching itself, and it does not terminate execution of the target session. Therefore, care should be taken to ensure that the target session does not hang itself. Syntax DBMS_DEBUG.DETACH_SESSION;