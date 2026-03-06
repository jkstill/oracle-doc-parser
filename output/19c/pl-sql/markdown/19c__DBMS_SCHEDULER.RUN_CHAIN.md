---
id: 19c__DBMS_SCHEDULER.RUN_CHAIN
name: DBMS_SCHEDULER.RUN_CHAIN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.RUN_CHAIN

This procedure immediately runs a chain or part of a chain by creating a run-once job with the job name given.

## Syntax

```sql
DBMS_SCHEDULER.RUN_CHAIN (
   chain_name                IN VARCHAR2,
   start_steps               IN VARCHAR2,
   job_name                  IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| chain_name | VARCHAR2 | IN | The name of the chain to run |
| job_name | VARCHAR2 | IN | The name of the job to create to run the chain |
| start_steps | VARCHAR2 | IN | Comma-separated list of the steps to start when the chain starts running |
| step_state_list |  |  | List of chain steps with an initial state ( SUCCEEDED or FAILED ) to set for each. Set the attributes of sys.scheduler$_step_type as follows: step_name The name of the step step_type ' SUCCEEDED ' or ' FAILED error_number ' where error_number is a positive or negative integer. |

## Usage Notes

If no job_name is given, one is generated of the form RUN_CHAIN$_ chainname N , where chainname is the first 8 characters of the chain name and N is an integer. If a list of start steps is given, only those steps are started when the chain begins running. Steps not in the list that would normally have started are skipped and paused (so that they or the steps after them do not run). If start_steps is NULL , then the chain starts normally—that is, it performs an initial evaluation to see which steps to start running). If a list of initial step states is given, the newly created chain job sets every listed step to the state specified for that step before evaluating the chain rules to see which steps to start. (Steps in the list are not started.) Syntax Runs a chain, with a list of start steps. DBMS_SCHEDULER.RUN_CHAIN ( chain_name IN VARCHAR2, start_steps IN VARCHAR2, job_name IN VARCHAR2 DEFAULT NULL); Runs a chain, with a list of initial step states. DBMS_SCHEDULER.RUN_CHAIN ( chain_name IN VARCHAR2, step_state_list IN SYS.SCHEDULER$_STEP_TYPE_LIST, job_name IN VARCHAR2 DEFAULT NULL); Parameters Table 151-78 RUN_CHAIN Procedure Parameters Parameter Description chain_name The name of the chain to run job_name The name of the job to create to run the chain start_steps Comma-separated list of the steps to start when the chain starts running step_state_list List of chain steps with an initial state ( SUCCEEDED or FAILED ) to set for each. Set the attributes of sys.scheduler$_step_type as follows: step_name The name of the step step_type ' SUCCEEDED ' or ' FAILED error_number ' where error_number is a positive or negative integer. Usage Notes Running a chain requires CREATE JOB if the job is being created in the user's schema, or CREATE ANY JOB otherwise. In addition, the owner of the job being created needs execute privileges on the chain (as the owner of the chain, or as a user with the EXECUTE privilege on the chain or the EXECUTE ANY PROGRAM system privilege). Examples The following example illustrates how to start a chain in the middle by providing the initial state of some chain steps. declare initial_step_states sys.scheduler$_step_type_list; begin initial_step_states := sys.scheduler$_step_type_list( sys.scheduler$_step_type('step1', 'SUCCEEDED'), sys.scheduler$_step_type('step2', 'FAILED 27486'), sys.scheduler$_step_type('step3', 'SUCCEEDED'), sys.scheduler$_step_type('step5', 'SUCCEEDED')); dbms_scheduler.run_chain('my_chain', initial_step_states); end; /