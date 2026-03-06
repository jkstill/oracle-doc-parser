---
id: 19c__DBMS_SCHEDULER.DROP_CHAIN
name: DBMS_SCHEDULER.DROP_CHAIN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.DROP_CHAIN

This procedure drops an existing chain.

## Syntax

```sql
DBMS_SCHEDULER.DROP_CHAIN (
   chain_name              IN VARCHAR2,
   force                   IN BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| chain_name | VARCHAR2 | IN | The name of the chain to drop. Can also be a comma-delimited list of chains. |
| force | BOOLEAN | IN | If force is set to FALSE , the chain must not be referenced by any job, otherwise an error will occur. If force is set to TRUE , all jobs pointing to the chain are disabled before the chain is dropped.Running jobs that point to this chain are stopped before the chain is dropped. |

## Usage Notes

Syntax DBMS_SCHEDULER.DROP_CHAIN ( chain_name IN VARCHAR2, force IN BOOLEAN DEFAULT FALSE); Parameters Table 151-44 DROP_CHAIN Procedure Parameters Parameter Description chain_name The name of the chain to drop. Can also be a comma-delimited list of chains. force If force is set to FALSE , the chain must not be referenced by any job, otherwise an error will occur. If force is set to TRUE , all jobs pointing to the chain are disabled before the chain is dropped.Running jobs that point to this chain are stopped before the chain is dropped. Usage Notes Dropping a chain requires alter privileges on the chain (either as the owner, or a user with ALTER privileges on the chain or the CREATE ANY JOB system privilege). All steps associated with the chain are dropped. If no rule set was specified when the chain was created, then the automatically created rule set and evaluation context associated with the chain are also dropped, so the user must have the privileges required to do this. See the DBMS_RULE_ADM.DROP_RULE_SET and DBMS_RULE_ADM.DROP_EVALUATION_CONTEXT procedures for more information. If force is FALSE , no jobs may be using this chain. If force is TRUE , any jobs that use this chain are disabled before the chain is dropped (and any of these jobs that are running will be stopped).