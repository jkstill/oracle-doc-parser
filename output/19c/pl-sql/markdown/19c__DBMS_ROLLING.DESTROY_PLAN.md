---
id: 19c__DBMS_ROLLING.DESTROY_PLAN
name: DBMS_ROLLING.DESTROY_PLAN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ROLLING
tags: [dbms_rolling]
source_file: DBMS_ROLLING.html
---

# DBMS_ROLLING.DESTROY_PLAN

This procedure destroys any existing upgrade plan, its parameters, and all resources associated with a rolling operation.

## Syntax

```sql
DBMS_ROLLING.DESTROY_PLAN ();
```

## Usage Notes

Syntax DBMS_ROLLING.DESTROY_PLAN (); Parameters This procedure has no parameters. Exceptions ORA-45422 : operation requires existing plan ORA-65040 : operation not allowed from within a pluggable database Usage Notes When a rolling operation is complete, this procedure can be called to completely purge all states related to a rolling operation.