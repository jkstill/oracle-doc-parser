---
id: 19c__DBMS_ROLLING.ROLLBACK_PLAN
name: DBMS_ROLLING.ROLLBACK_PLAN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ROLLING
tags: [dbms_rolling]
source_file: DBMS_ROLLING.html
---

# DBMS_ROLLING.ROLLBACK_PLAN

This procedure rolls back the configuration-wide rolling operation.

## Syntax

```sql
DBMS_ROLLING.ROLLBACK_PLAN;
```

## Usage Notes

Once completed, all of the databases in the leading group become physical standbys of the original primary database. This procedure can only be called if the configuration has not yet gone through a switchover operation since the START_PLAN procedure was invoked. Syntax DBMS_ROLLING.ROLLBACK_PLAN; Parameters This procedure has no parameters. Exceptions ORA-45400 : operation not permitted on current database ORA-45414 : could not connect to a remote database ORA-45415 : instruction execution failure ORA-45441 : no databases eligible for rollback ORA-45442 : rollback is not permitted after a role change ORA-65040 : operation not allowed from within a pluggable database Usage Notes You must manually restart media recovery on the lower Oracle Database version if the upgrade of the transient logical standby has already been performed.