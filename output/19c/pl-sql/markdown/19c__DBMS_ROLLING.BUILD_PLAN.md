---
id: 19c__DBMS_ROLLING.BUILD_PLAN
name: DBMS_ROLLING.BUILD_PLAN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ROLLING
tags: [dbms_rolling]
source_file: DBMS_ROLLING.html
---

# DBMS_ROLLING.BUILD_PLAN

This procedure validates plan parameters and creates or modifies a rolling operation plan.

## Syntax

```sql
DBMS_ROLLING.BUILD_PLAN ();
```

## Usage Notes

A successfully constructed plan is required in order to perform a rolling operation. This procedure must return successfully before the START_PLAN procedure can be called to start the rolling operation. Parameter changes made after a plan has been created may require calling the BUILD_PLAN procedure to modify the existing plan. The DBA_ROLLING_EVENTS view will indicate if any invocation of the SET_PARAMETER procedure requires a plan rebuild. Failure to rebuild the plan will result in an ORA-45416 error when attempting to resume the rolling operation. Syntax DBMS_ROLLING.BUILD_PLAN (); Parameters This procedure has no parameters. Exceptions ORA-45400 : operation not permitted on current database ORA-45403 : database %s must be specified in the DG_CONFIG ORA-45414 : could not connect to a remote database ORA-45419 : DB_UNIQUE_NAME parameter must be specified ORA-45433 : failover was detected on an unsupported database ORA-45434 : multiple failovers of the same type detected ORA-65040 : operation not allowed from within a pluggable database Usage Notes This procedure connects to databases specified as plan parameters. These instances must be mounted or open, and must be reachable via the network.