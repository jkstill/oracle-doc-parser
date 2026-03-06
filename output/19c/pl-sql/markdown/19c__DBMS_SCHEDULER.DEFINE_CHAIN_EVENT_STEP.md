---
id: 19c__DBMS_SCHEDULER.DEFINE_CHAIN_EVENT_STEP
name: DBMS_SCHEDULER.DEFINE_CHAIN_EVENT_STEP
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.DEFINE_CHAIN_EVENT_STEP

This procedure adds or replaces a chain step and associates it with an event schedule or an inline event.

## Syntax

```sql
DBMS_SCHEDULER.DEFINE_CHAIN_EVENT_STEP (
   chain_name              IN VARCHAR2,
   step_name               IN VARCHAR2,
   event_schedule_name     IN VARCHAR2,
   timeout                 IN INTERVAL DAY TO SECOND DEFAULT NULL);

DBMS_SCHEDULER.DEFINE_CHAIN_EVENT_STEP (
   chain_name              IN VARCHAR2,
   step_name               IN VARCHAR2,
   event_condition         IN VARCHAR2,
   queue_spec              IN VARCHAR2,
   timeout                 IN INTERVAL DAY TO SECOND DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| chain_name | VARCHAR2 | IN | The name of the chain that the step is in |
| step_name | VARCHAR2 | IN | The name of the step |
| event_schedule_name | VARCHAR2 | IN | The name of the event schedule that the step waits for |
| timeout | INTERVAL | IN | This parameter is reserved for future use |
| event_condition | VARCHAR2 | IN | See the CREATE_EVENT_SCHEDULE Procedure |
| queue_spec | VARCHAR2 | IN | See the CREATE_EVENT_SCHEDULE Procedure |

## Usage Notes

Once started in a running chain, this step does not complete until the specified event has occurred. Every step in a chain must be defined before the chain can be enabled and used. Defining a step gives it a name and specifies what happens during the step. If a step already exists with this name, the new step replaces the old one. Syntax DBMS_SCHEDULER.DEFINE_CHAIN_EVENT_STEP ( chain_name IN VARCHAR2, step_name IN VARCHAR2, event_schedule_name IN VARCHAR2, timeout IN INTERVAL DAY TO SECOND DEFAULT NULL); DBMS_SCHEDULER.DEFINE_CHAIN_EVENT_STEP ( chain_name IN VARCHAR2, step_name IN VARCHAR2, event_condition IN VARCHAR2, queue_spec IN VARCHAR2, timeout IN INTERVAL DAY TO SECOND DEFAULT NULL); Parameters Table 151-36 DEFINE_CHAIN_EVENT_STEP Procedure Parameters Parameter Description chain_name The name of the chain that the step is in step_name The name of the step event_schedule_name The name of the event schedule that the step waits for timeout This parameter is reserved for future use event_condition See the CREATE_EVENT_SCHEDULE Procedure queue_spec See the CREATE_EVENT_SCHEDULE Procedure Usage Notes Defining a chain step requires ALTER privileges on the chain either as the owner of the chain, or as a user with the ALTER object privilege on the chain or the CREATE ANY JOB system privilege. You can base a chain step on a file watcher as well. To do this, provide the file watcher name directly in the queue_spec parameter, or use a file watcher schedule for the event_schedule_name parameter. See Also: " DEFINE_CHAIN_STEP Procedure " See Also: " DEFINE_CHAIN_STEP Procedure "