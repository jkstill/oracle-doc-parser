---
id: 19c__DBMS_AQADM.ALTER_QUEUE
name: DBMS_AQADM.ALTER_QUEUE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQADM
tags: [dbms_aqadm]
source_file: DBMS_AQADM.html
---

# DBMS_AQADM.ALTER_QUEUE

This procedure alters existing properties of a queue. The parameters max_retries , retention_time , and retry_delay are not supported for nonpersistent queues.

## Syntax

```sql
DBMS_AQADM.ALTER_QUEUE (
   queue_name        IN    VARCHAR2,
   max_retries       IN    NUMBER   DEFAULT NULL,
   retry_delay       IN    NUMBER   DEFAULT NULL,
   retention_time    IN    NUMBER   DEFAULT NULL,
   auto_commit       IN    BOOLEAN  DEFAULT TRUE,
   comment           IN    VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| queue_name | VARCHAR2 | IN | Name of the queue that is to be altered |
| max_retries | NUMBER | IN | Limits the number of times a dequeue with REMOVE mode can be attempted on a message. The maximum value of max_retries is 2**31 -1. A message is moved to an exception queue if RETRY_COUNT is greater than MAX_RETRIES . RETRY_COUNT is incremented when the application issues a rollback after executing the dequeue. If a dequeue transaction fails because the server process dies (including ALTER SYSTEM KILL SESSION ) or SHUTDOWN ABORT on the instance, then RETRY_COUNT is not incremented. Note that max_retries is supported for all single consumer queues and 8.1-compatible or higher multiconsumer queues but not for 8.0-compatible multiconsumer queues. |
| retry_delay | NUMBER | IN | Delay time in seconds before this message is scheduled for processing again after an application rollback. The default is NULL , which means that the value will not be altered. Note that retry_delay is supported for single consumer queues and 8.1-compatible or higher multiconsumer queues but not for 8.0-compatible multiconsumer queues. |
| retention_time | NUMBER | IN | Retention time in seconds for which a message is retained in the queue table after being dequeued. The default is NULL , which means that the value will not be altered. |
| auto_commit | BOOLEAN | IN | TRUE causes the current transaction, if any, to commit before the ALTER_QUEUE operation is carried out. The ALTER_QUEUE operation become persistent when the call returns. This is the default. FALSE means the operation is part of the current transaction and becomes persistent only when the caller enters a commit. Caution: This parameter has been deprecated. |
| comment | VARCHAR2 | IN | User-specified description of the queue. This user comment is added to the queue catalog. The default value is NULL , which means that the value will not be changed. |

## Usage Notes

Syntax DBMS_AQADM.ALTER_QUEUE ( queue_name IN VARCHAR2, max_retries IN NUMBER DEFAULT NULL, retry_delay IN NUMBER DEFAULT NULL, retention_time IN NUMBER DEFAULT NULL, auto_commit IN BOOLEAN DEFAULT TRUE, comment IN VARCHAR2 DEFAULT NULL); Parameters Table 23-15 ALTER_QUEUE Procedure Parameters Parameter Description queue_name Name of the queue that is to be altered max_retries Limits the number of times a dequeue with REMOVE mode can be attempted on a message. The maximum value of max_retries is 2**31 -1. A message is moved to an exception queue if RETRY_COUNT is greater than MAX_RETRIES . RETRY_COUNT is incremented when the application issues a rollback after executing the dequeue. If a dequeue transaction fails because the server process dies (including ALTER SYSTEM KILL SESSION ) or SHUTDOWN ABORT on the instance, then RETRY_COUNT is not incremented. Note that max_retries is supported for all single consumer queues and 8.1-compatible or higher multiconsumer queues but not for 8.0-compatible multiconsumer queues. retry_delay Delay time in seconds before this message is scheduled for processing again after an application rollback. The default is NULL , which means that the value will not be altered. Note that retry_delay is supported for single consumer queues and 8.1-compatible or higher multiconsumer queues but not for 8.0-compatible multiconsumer queues. retention_time Retention time in seconds for which a message is retained in the queue table after being dequeued. The default is NULL , which means that the value will not be altered. auto_commit TRUE causes the current transaction, if any, to commit before the ALTER_QUEUE operation is carried out. The ALTER_QUEUE operation become persistent when the call returns. This is the default. FALSE means the operation is part of the current transaction and becomes persistent only when the caller enters a commit. Caution: This parameter has been deprecated. comment User-specified description of the queue. This user comment is added to the queue catalog. The default value is NULL , which means that the value will not be changed.