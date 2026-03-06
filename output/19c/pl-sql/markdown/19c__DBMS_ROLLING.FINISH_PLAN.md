---
id: 19c__DBMS_ROLLING.FINISH_PLAN
name: DBMS_ROLLING.FINISH_PLAN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ROLLING
tags: [dbms_rolling]
source_file: DBMS_ROLLING.html
---

# DBMS_ROLLING.FINISH_PLAN

This procedure finalizes the rolling operation.

## Syntax

```sql
DBMS_ROLLING.FINISH_PLAN ();
```

## Usage Notes

It configures the former primary (also known as the TGM) as a physical standby, and configures remaining physical standbys to recover the upgrade redo from the future primary. Syntax DBMS_ROLLING.FINISH_PLAN (); Parameters This procedure has no parameters. Exceptions ORA-45400 : operation not permitted on current database ORA-45414 : could not connect to a remote database ORA-45415 : instruction execution failure ORA-45416 : operation cannot start until plan rebuild ORA-45417 : operation not permitted since current phase was not %s ORA-45422 : operation requires existing plan ORA-45426 : managed recovery process was not running ORA-45427 : logical standby Redo Apply process was not running ORA-45428 : database was not in expected database role ORA-45435 : managed recovery process was running ORA-45436 : logical standby Redo Apply process was running ORA-45438 : database is not in mounted mode ORA-45439 : database is not in open read/write mode ORA-45486 : database update progress is inconsistent ORA-65040 : operation not allowed from within a pluggable database Usage Notes This procedure can only be called after you have remounted the former primary and remaining physical standbys on the higher Oracle Database version.