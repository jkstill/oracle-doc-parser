---
id: 19c__DBMS_SCHEDULER.ADD_EVENT_QUEUE_SUBSCRIBER
name: DBMS_SCHEDULER.ADD_EVENT_QUEUE_SUBSCRIBER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.ADD_EVENT_QUEUE_SUBSCRIBER

This procedure adds a user as a subscriber to the Scheduler event queue SYS.SCHEDULER$_EVENT_QUEUE , and grants the user permission to dequeue from this queue using the designated agent.

## Syntax

```sql
DBMS_SCHEDULER.ADD_EVENT_QUEUE_SUBSCRIBER (
   subscriber_name         IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| subscriber_name | VARCHAR2 | IN | Name of the Oracle Advanced Queuing (AQ) agent to be used to subscribe to the Scheduler event queue. If NULL , an agent is created and assigned the user name of the calling user. |

## Usage Notes

Syntax DBMS_SCHEDULER.ADD_EVENT_QUEUE_SUBSCRIBER ( subscriber_name IN VARCHAR2 DEFAULT NULL); Parameters Table 151-12 ADD_EVENT_QUEUE_SUBSCRIBER Procedure Parameters Parameter Description subscriber_name Name of the Oracle Advanced Queuing (AQ) agent to be used to subscribe to the Scheduler event queue. If NULL , an agent is created and assigned the user name of the calling user. Usage Notes The subscription is rule-based. The rule permits the user to see only events raised by jobs that the user owns, and filters out all other messages. If an AQ agent with the same name already exists, an error is raised.