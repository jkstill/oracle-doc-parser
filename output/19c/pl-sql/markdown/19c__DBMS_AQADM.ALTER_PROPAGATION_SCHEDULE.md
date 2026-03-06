---
id: 19c__DBMS_AQADM.ALTER_PROPAGATION_SCHEDULE
name: DBMS_AQADM.ALTER_PROPAGATION_SCHEDULE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQADM
tags: [dbms_aqadm]
source_file: DBMS_AQADM.html
---

# DBMS_AQADM.ALTER_PROPAGATION_SCHEDULE

This procedure alters parameters for a propagation schedule.

## Syntax

```sql
DBMS_AQADM.ALTER_PROPAGATION_SCHEDULE ( 
   queue_name           IN    VARCHAR2, 
   destination          IN    VARCHAR2 DEFAULT NULL,
   duration             IN    NUMBER   DEFAULT NULL, 
   next_time            IN    VARCHAR2 DEFAULT NULL, 
   latency              IN    NUMBER   DEFAULT 60,
   destination_queue    IN    VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| queue_name | VARCHAR2 | IN | Name of the source queue whose messages are to be propagated, including the schema name. If the schema name is not specified, then it defaults to the schema name of the user. |
| destination | VARCHAR2 | IN | Destination database link. Messages in the source queue for recipients at this destination are propagated. If it is NULL , then the destination is the local database and messages are propagated to other queues in the local database. The length of this field is currently limited to 128 bytes, and if the name is not fully qualified, then the default domain name is used. |
| duration | NUMBER | IN | Duration of the propagation window in seconds. A NULL value means the propagation window is forever or until the propagation is unscheduled. |
| next_time | VARCHAR2 | IN | Date function to compute the start of the next propagation window from the end of the current window. If this value is NULL , then propagation is stopped at the end of the current window. For example, to start the window at the same time every day, next_time should be specified as SYSDATE + 1 - duration/86400 . |
| latency | NUMBER | IN | Maximum wait, in seconds, in the propagation window for a message to be propagated after it is enqueued. The default value is 60. Caution: if latency is not specified for this call, then latency will over-write any existing value with the default value. For example, if the latency is 60 seconds and there are no messages to be propagated during the propagation window, then messages from that queue for the destination are not propagated for at least 60 more seconds. It will be at least 60 seconds before the queue will be checked again for messages to be propagated for the specified destination. If the latency is 600, then the queue will not be checked for 10 minutes and if the latency is 0, then a job queue process will be waiting for messages to be enqueued for the destination and as soon as a message is enqueued it will be propagated. |
| destination_queue | VARCHAR2 | IN | Name of the target queue to which messages are to be propagated in the form of a dblink |

## Usage Notes

Syntax DBMS_AQADM.ALTER_PROPAGATION_SCHEDULE ( queue_name IN VARCHAR2, destination IN VARCHAR2 DEFAULT NULL, duration IN NUMBER DEFAULT NULL, next_time IN VARCHAR2 DEFAULT NULL, latency IN NUMBER DEFAULT 60, destination_queue IN VARCHAR2 DEFAULT NULL); Parameters Table 23-14 ALTER_PROPAGATION_SCHEDULE Procedure Parameters Parameter Description queue_name Name of the source queue whose messages are to be propagated, including the schema name. If the schema name is not specified, then it defaults to the schema name of the user. destination Destination database link. Messages in the source queue for recipients at this destination are propagated. If it is NULL , then the destination is the local database and messages are propagated to other queues in the local database. The length of this field is currently limited to 128 bytes, and if the name is not fully qualified, then the default domain name is used. duration Duration of the propagation window in seconds. A NULL value means the propagation window is forever or until the propagation is unscheduled. next_time Date function to compute the start of the next propagation window from the end of the current window. If this value is NULL , then propagation is stopped at the end of the current window. For example, to start the window at the same time every day, next_time should be specified as SYSDATE + 1 - duration/86400 . latency Maximum wait, in seconds, in the propagation window for a message to be propagated after it is enqueued. The default value is 60. Caution: if latency is not specified for this call, then latency will over-write any existing value with the default value. For example, if the latency is 60 seconds and there are no messages to be propagated during the propagation window, then messages from that queue for the destination are not propagated for at least 60 more seconds. It will be at least 60 seconds before the queue will be checked again for messages to be propagated for the specified destination. If the latency is 600, then the queue will not be checked for 10 minutes and if the latency is 0, then a job queue process will be waiting for messages to be enqueued for the destination and as soon as a message is enqueued it will be propagated. destination_queue Name of the target queue to which messages are to be propagated in the form of a dblink