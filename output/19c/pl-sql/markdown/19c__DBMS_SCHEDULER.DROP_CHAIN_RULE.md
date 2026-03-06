---
id: 19c__DBMS_SCHEDULER.DROP_CHAIN_RULE
name: DBMS_SCHEDULER.DROP_CHAIN_RULE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.DROP_CHAIN_RULE

This procedure removes a rule from an existing chain. The rule object corresponding to this rule will also be dropped. The chain will not be disabled. If dropping this rule makes the chain invalid, the user should first disable the chain to ensure that it does not run.

## Syntax

```sql
DBMS_SCHEDULER.DROP_CHAIN_RULE (
   chain_name              IN VARCHAR2,
   rule_name               IN VARCHAR2,
   force                   IN BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| chain_name | VARCHAR2 | IN | The name of the chain to alter |
| rule_name | VARCHAR2 | IN | The name of the rule to drop |
| force | BOOLEAN | IN | If force is set to TRUE , the drop operation proceeds even if the chain is currently running. The running chain is not stopped or interrupted. If force is set to FALSE and the chain is running, an error is generated. |

## Usage Notes

Syntax DBMS_SCHEDULER.DROP_CHAIN_RULE ( chain_name IN VARCHAR2, rule_name IN VARCHAR2, force IN BOOLEAN DEFAULT FALSE); Parameters Table 151-45 DROP_CHAIN_RULE Procedure Parameters Parameter Description chain_name The name of the chain to alter rule_name The name of the rule to drop force If force is set to TRUE , the drop operation proceeds even if the chain is currently running. The running chain is not stopped or interrupted. If force is set to FALSE and the chain is running, an error is generated. Usage Notes Dropping a chain rule requires alter privileges on the chain (either as the owner or as a user with ALTER privileges on the chain or the CREATE ANY JOB system privilege). Dropping a chain rule also drops the underlying rule database object so you must have the privileges to drop this rule object. See the DBMS_RULE_ADM.DROP_RULE procedure for more information.