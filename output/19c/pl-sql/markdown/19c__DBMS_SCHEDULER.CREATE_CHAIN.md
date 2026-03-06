---
id: 19c__DBMS_SCHEDULER.CREATE_CHAIN
name: DBMS_SCHEDULER.CREATE_CHAIN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.CREATE_CHAIN

This procedure creates a new chain. The chain name can be optionally qualified with a schema name (for example, myschema.myname ).

## Syntax

```sql
DBMS_SCHEDULER.CREATE_CHAIN (
   chain_name              IN VARCHAR2,
   rule_set_name           IN VARCHAR2 DEFAULT NULL,
   evaluation_interval     IN INTERVAL DAY TO SECOND DEFAULT NULL,
   comments                IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| chain_name | VARCHAR2 | IN | The name to assign to the new chain, which can optionally be qualified with a schema. This must be unique in the SQL namespace, therefore, there cannot already be a table or other object with this name and schema. |
| rule_set_name | VARCHAR2 | IN | In the normal case, no rule set should be passed in. The Scheduler automatically creates a rule set and associated empty evaluation context. You then use DEFINE_CHAIN_RULE to add rules and DROP_CHAIN_RULE to remove them. Advanced users can create a rule set that describes their chain dependencies and pass it in here. This allows greater flexibility in defining rules. For example, conditions can refer to external variables, and tables can be exposed through the evaluation context. If you pass in a rule set, you must ensure that it is in the format of a chain rule set. (For example, all steps must be listed as variables in the evaluation context). If no rule set is passed in, the rule set created is of the form SCHED_RULESET${N} and the evaluation context created is of the form SCHED_EVCTX${N} |
| evaluation_interval | INTERVAL | IN | If this is NULL , reevaluation of the rules of a running chain are performed only when the job starts and when a step completes. A non- NULL value causes rule evaluations to also occur periodically at the specified interval. Because evaluation may be CPU-intensive, this should be conservatively set to the highest possible value or left at NULL if possible. evaluation_interval cannot be less than a minute or greater than a day. |
| comments | VARCHAR2 | IN | An optional comment describing the purpose of the chain |

## Usage Notes

A chain is always created as disabled and must be enabled with the ENABLE Procedure before it can be used. Syntax DBMS_SCHEDULER.CREATE_CHAIN ( chain_name IN VARCHAR2, rule_set_name IN VARCHAR2 DEFAULT NULL, evaluation_interval IN INTERVAL DAY TO SECOND DEFAULT NULL, comments IN VARCHAR2 DEFAULT NULL); Parameters Table 151-21 CREATE_CHAIN Procedure Parameters Parameter Description chain_name The name to assign to the new chain, which can optionally be qualified with a schema. This must be unique in the SQL namespace, therefore, there cannot already be a table or other object with this name and schema. rule_set_name In the normal case, no rule set should be passed in. The Scheduler automatically creates a rule set and associated empty evaluation context. You then use DEFINE_CHAIN_RULE to add rules and DROP_CHAIN_RULE to remove them. Advanced users can create a rule set that describes their chain dependencies and pass it in here. This allows greater flexibility in defining rules. For example, conditions can refer to external variables, and tables can be exposed through the evaluation context. If you pass in a rule set, you must ensure that it is in the format of a chain rule set. (For example, all steps must be listed as variables in the evaluation context). If no rule set is passed in, the rule set created is of the form SCHED_RULESET${N} and the evaluation context created is of the form SCHED_EVCTX${N} evaluation_interval If this is NULL , reevaluation of the rules of a running chain are performed only when the job starts and when a step completes. A non- NULL value causes rule evaluations to also occur periodically at the specified interval. Because evaluation may be CPU-intensive, this should be conservatively set to the highest possible value or left at NULL if possible. evaluation_interval cannot be less than a minute or greater than a day. comments An optional comment describing the purpose of the chain Usage Notes To create a chain in your own schema, you must have the CREATE JOB system privilege. To create a chain in a different schema you must have the CREATE ANY JOB system privilege. If you do not provide a rule_set_name , a rule set and evaluation context is created in the schema that the chain is being created in, so you must have the privileges required to create these objects. See the DBMS_RULE_ADM.CREATE_RULE_SET and DBMS_RULE_ADM.CREATE_EVALUATION_CONTEXT procedures for more information.