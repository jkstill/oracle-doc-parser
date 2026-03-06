---
id: 19c__DBMS_SCHEDULER.REMOVE_EVENT_QUEUE_SUBSCRIBER
name: DBMS_SCHEDULER.REMOVE_EVENT_QUEUE_SUBSCRIBER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.REMOVE_EVENT_QUEUE_SUBSCRIBER

This procedure unsubscribes a user from the Scheduler event queue SYS.SCHEDULER$_EVENT_QUEUE .

## Syntax

```sql
DBMS_SCHEDULER.REMOVE_EVENT_QUEUE_SUBSCRIBER (
   subscriber_name         IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| subscriber_name | VARCHAR2 | IN | Name of the Oracle Advanced Queuing (AQ) agent to remove the subscription from. If NULL , the user name of the calling user is used. |

## Usage Notes

Syntax DBMS_SCHEDULER.REMOVE_EVENT_QUEUE_SUBSCRIBER ( subscriber_name IN VARCHAR2 DEFAULT NULL); Parameters Table 151-73 REMOVE_EVENT_QUEUE_SUBSCRIBER Procedure Parameters Parameter Description subscriber_name Name of the Oracle Advanced Queuing (AQ) agent to remove the subscription from. If NULL , the user name of the calling user is used. Usage Notes After the agent is unsubscribed, it is deleted. If the agent does not exist or is not currently subscribed to the Scheduler event queue, an error is raised.