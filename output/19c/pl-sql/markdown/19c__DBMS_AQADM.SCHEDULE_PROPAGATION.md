---
id: 19c__DBMS_AQADM.SCHEDULE_PROPAGATION
name: DBMS_AQADM.SCHEDULE_PROPAGATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQADM
tags: [dbms_aqadm]
source_file: DBMS_AQADM.html
---

# DBMS_AQADM.SCHEDULE_PROPAGATION

This procedure schedules propagation of messages from a queue to a destination identified by a specific database link.

## Syntax

```sql
DBMS_AQADM.SCHEDULE_PROPAGATION (
   queue_name          IN    VARCHAR2,
   destination         IN    VARCHAR2 DEFAULT NULL,
   start_time          IN    DATE     DEFAULT SYSDATE,
   duration            IN    NUMBER   DEFAULT NULL,
   next_time           IN    VARCHAR2 DEFAULT NULL,
   latency             IN    NUMBER   DEFAULT 60,
   destination_queue   IN    VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| queue_name | VARCHAR2 | IN | Name of the source queue whose messages are to be propagated, including the schema name. If the schema name is not specified, then it defaults to the schema name of the administrative user. |
| destination | VARCHAR2 | IN | Destination database link. Messages in the source queue for recipients at this destination are propagated. If it is NULL , then the destination is the local database and messages are propagated to other queues in the local database. The length of this field is currently limited to 390 bytes, and if the name is not fully qualified, then the default domain name is used. The pattern schema . queue @dblink is used. |
| start_time | DATE | IN | Initial start time for the propagation window for messages from the source queue to the destination. |
| duration | NUMBER | IN | Duration of the propagation window in seconds. A NULL value means the propagation window is forever or until the propagation is unscheduled. |
| next_time | VARCHAR2 | IN | Date function to compute the start of the next propagation window from the end of the current window. If this value is NULL , then propagation is stopped at the end of the current window. For example, to start the window at the same time every day, next_time should be specified as SYSDATE + 1 - duration/86400. |
| latency | NUMBER | IN | Maximum wait, in seconds, in the propagation window for a message to be propagated after it is enqueued. For example, if the latency is 60 seconds and there are no messages to be propagated during the propagation window, then messages from that queue for the destination are not propagated for at least 60 more seconds. It is at least 60 seconds before the queue is checked again for messages to be propagated for the specified destination. If the latency is 600, then the queue is not checked for 10 minutes, and if the latency is 0, then a job queue process will be waiting for messages to be enqueued for the destination. As soon as a message is enqueued, it is propagated. |
| destination_queue | VARCHAR2 | IN | Name of the target queue to which messages are to be propagated in the form of a dblink |

## Usage Notes

Syntax DBMS_AQADM.SCHEDULE_PROPAGATION ( queue_name IN VARCHAR2, destination IN VARCHAR2 DEFAULT NULL, start_time IN DATE DEFAULT SYSDATE, duration IN NUMBER DEFAULT NULL, next_time IN VARCHAR2 DEFAULT NULL, latency IN NUMBER DEFAULT 60, destination_queue IN VARCHAR2 DEFAULT NULL); Parameters Table 23-49 SCHEDULE_PROPAGATION Procedure Parameters Parameter Description queue_name Name of the source queue whose messages are to be propagated, including the schema name. If the schema name is not specified, then it defaults to the schema name of the administrative user. destination Destination database link. Messages in the source queue for recipients at this destination are propagated. If it is NULL , then the destination is the local database and messages are propagated to other queues in the local database. The length of this field is currently limited to 390 bytes, and if the name is not fully qualified, then the default domain name is used. The pattern schema . queue @dblink is used. start_time Initial start time for the propagation window for messages from the source queue to the destination. duration Duration of the propagation window in seconds. A NULL value means the propagation window is forever or until the propagation is unscheduled. next_time Date function to compute the start of the next propagation window from the end of the current window. If this value is NULL , then propagation is stopped at the end of the current window. For example, to start the window at the same time every day, next_time should be specified as SYSDATE + 1 - duration/86400. latency Maximum wait, in seconds, in the propagation window for a message to be propagated after it is enqueued. For example, if the latency is 60 seconds and there are no messages to be propagated during the propagation window, then messages from that queue for the destination are not propagated for at least 60 more seconds. It is at least 60 seconds before the queue is checked again for messages to be propagated for the specified destination. If the latency is 600, then the queue is not checked for 10 minutes, and if the latency is 0, then a job queue process will be waiting for messages to be enqueued for the destination. As soon as a message is enqueued, it is propagated. destination_queue Name of the target queue to which messages are to be propagated in the form of a dblink Usage Notes Messages may also be propagated to other queues in the same database by specifying a NULL destination. If a message has multiple recipients at the same destination in either the same or different queues, the message is propagated to all of them at the same time. Oracle extensions for JMS such as JMS propagation and remote subscribers are not currently supported for sharded queues. Propagation between sharded and non-sharded queues is not supported