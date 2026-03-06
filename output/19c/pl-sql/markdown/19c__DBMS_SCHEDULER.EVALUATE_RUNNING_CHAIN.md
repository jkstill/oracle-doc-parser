---
id: 19c__DBMS_SCHEDULER.EVALUATE_RUNNING_CHAIN
name: DBMS_SCHEDULER.EVALUATE_RUNNING_CHAIN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.EVALUATE_RUNNING_CHAIN

This procedure forces reevaluation of the rules of a running chain to trigger any rules for which the conditions have been satisfied. The job passed as an argument must point to a chain and must be running. If the job is not running, an error is thrown. ( RUN_JOB can be used to start the job.)

## Syntax

```sql
DBMS_SCHEDULER.EVALUATE_RUNNING_CHAIN (
   job_name              IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| job_name | VARCHAR2) | IN | The name of the running job (pointing to a chain) to reevaluate the rules for |

## Usage Notes

If any of the steps of the chain are themselves running chains, another EVALUATE_RUNNING_CHAIN is performed on each of the nested running chains. Syntax DBMS_SCHEDULER.EVALUATE_RUNNING_CHAIN ( job_name IN VARCHAR2); Parameters Table 151-62 EVALUATE_RUNNING_CHAIN Procedure Parameter Parameter Description job_name The name of the running job (pointing to a chain) to reevaluate the rules for Usage Notes Running EVALUATE_RUNNING_CHAIN on a job requires alter privileges on the job (either as the owner, or as a user with ALTER privileges on the job or the CREATE ANY JOB system privilege). Note: The Scheduler automatically evaluates a chain: At the start of the chain job When a chain step completes When an event occurs that is associated with an event step in the chain For most chains, this is sufficient. EVALUATE_RUNNING_CHAIN should be used only under the following circumstances: After manual intervention of a running chain with the ALTER_RUNNING_CHAIN procedure When chain rules use SQL syntax and the rule conditions contain elements that are not under the control of the Scheduler. In these cases, EVALUATE_RUNNING_CHAIN may not be needed if you set the evaluation_interval attribute when you created the chain. Note: The Scheduler automatically evaluates a chain: At the start of the chain job When a chain step completes When an event occurs that is associated with an event step in the chain For most chains, this is sufficient. EVALUATE_RUNNING_CHAIN should be used only under the following circumstances: After manual intervention of a running chain with the ALTER_RUNNING_CHAIN procedure When chain rules use SQL syntax and the rule conditions contain elements that are not under the control of the Scheduler. In these cases, EVALUATE_RUNNING_CHAIN may not be needed if you set the evaluation_interval attribute when you created the chain.