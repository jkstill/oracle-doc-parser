---
id: 19c__DBMS_SCHEDULER.DROP_CHAIN_STEP
name: DBMS_SCHEDULER.DROP_CHAIN_STEP
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.DROP_CHAIN_STEP

This procedure drops a chain step. If this chain step is still used in the chain rules, the chain will be disabled.

## Syntax

```sql
DBMS_SCHEDULER.DROP_CHAIN_STEP (
   chain_name              IN VARCHAR2,
   step_name               IN VARCHAR2,
   force                   IN BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| chain_name | VARCHAR2 | IN | The name of the chain to alter |
| step_name | VARCHAR2 | IN | The name of the step being dropped. Can be a comma-separated list. |
| force | BOOLEAN | IN | If force is set to TRUE , this succeeds even if this chain is currently running. The running chain will not be stopped or interrupted.If force is set to FALSE and this chain is currently running, an error is thrown. |

## Usage Notes

Syntax DBMS_SCHEDULER.DROP_CHAIN_STEP ( chain_name IN VARCHAR2, step_name IN VARCHAR2, force IN BOOLEAN DEFAULT FALSE); Parameters Table 151-46 DROP_CHAIN_STEP Procedure Parameters Parameter Description chain_name The name of the chain to alter step_name The name of the step being dropped. Can be a comma-separated list. force If force is set to TRUE , this succeeds even if this chain is currently running. The running chain will not be stopped or interrupted.If force is set to FALSE and this chain is currently running, an error is thrown. Usage Notes Dropping a chain step requires ALTER privileges on the chain (either as the owner or as a user with ALTER privileges on the chain or the CREATE ANY JOB system privilege).