---
id: 19c__DBMS_ROLLING.SWITCHOVER
name: DBMS_ROLLING.SWITCHOVER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ROLLING
tags: [dbms_rolling]
source_file: DBMS_ROLLING.html
---

# DBMS_ROLLING.SWITCHOVER

This procedure performs a switchover between the current primary database (also known as the TGM) and the transient logical standby database (also known as the LGM).

## Syntax

```sql
DBMS_ROLLING.SWITCHOVER ();
```

## Usage Notes

At the successful completion of the procedure, the LGM assumes the primary role for the Data Guard configuration. Syntax DBMS_ROLLING.SWITCHOVER (); Parameters This procedure has no parameters. Exceptions ORA-45400 : operation not permitted on current database ORA-45414 : could not connect to a remote database ORA-45415 : instruction execution failure ORA-45416 : operation cannot start until plan rebuild ORA-45417 : operation not permitted since current phase was not %s ORA-45422 : operation requires existing plan ORA-45426 : managed recovery process was not running ORA-45427 : logical standby Redo Apply process was not running ORA-45428 : database was not in expected database role ORA-45435 : managed recovery process was running ORA-45436 : logical standby Redo Apply process was running ORA-45438 : database is not in mounted mode ORA-45439 : database is not in open read/write mode ORA-45486 : database update progress is inconsistent ORA-65040 : operation not allowed from within a pluggable database Usage Notes This procedure can only be called after you have manually upgraded the transient logical standby and opened it on the higher Oracle Database version.