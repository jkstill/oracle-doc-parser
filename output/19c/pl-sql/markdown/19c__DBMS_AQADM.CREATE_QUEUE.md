---
id: 19c__DBMS_AQADM.CREATE_QUEUE
name: DBMS_AQADM.CREATE_QUEUE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQADM
tags: [dbms_aqadm]
source_file: DBMS_AQADM.html
---

# DBMS_AQADM.CREATE_QUEUE

This procedure creates a queue in the specified queue table.

## Syntax

```sql
DBMS_AQADM.CREATE_QUEUE (
   queue_name          IN       VARCHAR2,
   queue_table         IN       VARCHAR2,
   queue_type          IN       BINARY_INTEGER DEFAULT NORMAL_QUEUE,
   max_retries         IN       NUMBER         DEFAULT NULL,
   retry_delay         IN       NUMBER         DEFAULT 0,
   retention_time      IN       NUMBER         DEFAULT 0,
   dependency_tracking IN       BOOLEAN        DEFAULT FALSE,
   comment             IN       VARCHAR2       DEFAULT NULL,
   auto_commit         IN       BOOLEAN        DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| queue_name | VARCHAR2 | IN | Name of the queue that is to be created. The name must be unique within a schema and must follow object name guidelines in Oracle Database SQL Language Reference with regard to reserved characters. |
| queue_table | VARCHAR2 | IN | Name of the queue table that will contain the queue. |
| queue_type | BINARY_INTEGER | IN | Specifies whether the queue being created is an exception queue or a normal queue. NORMAL_QUEUE means the queue is a normal queue. This is the default. EXCEPTION_QUEUE means it is an exception queue. Only the dequeue operation is allowed on the exception queue. |
| max_retries | NUMBER | IN | Limits the number of times a dequeue with the REMOVE mode can be attempted on a message. The maximum value of max_retries is 2**31 -1. A message is moved to an exception queue if RETRY_COUNT is greater than MAX_RETRIES . RETRY_COUNT is incremented when the application issues a rollback after executing the dequeue. If a dequeue transaction fails because the server process dies (including ALTER SYSTEM KILL SESSION ) or SHUTDOWN ABORT on the instance, then RETRY_COUNT is not incremented. Note that max_retries is supported for all single consumer queues and 8.1-compatible or higher multiconsumer queues but not for 8.0-compatible multiconsumer queues. |
| retry_delay | NUMBER | IN | Delay time, in seconds, before this message is scheduled for processing again after an application rollback. The default is 0, which means the message can be retried as soon as possible. This parameter has no effect if max_retries is set to 0. Note that retry_delay is supported for single consumer queues and 8.1-compatible or higher multiconsumer queues but not for 8.0-compatible multiconsumer queues. |
| retention_time | NUMBER | IN | Number of seconds for which a message is retained in the queue table after being dequeued from the queue. INFINITE means the message is retained forever. NUMBER is the number of seconds for which to retain the messages. The default is 0, no retention. |
| dependency_tracking | BOOLEAN | IN | Reserved for future use. FALSE is the default. TRUE is not permitted in this release. |
| comment | VARCHAR2 | IN | User-specified description of the queue. This user comment is added to the queue catalog. |
| auto_commit | BOOLEAN | IN | TRUE causes the current transaction, if any, to commit before the CREATE_QUEUE operation is carried out. The CREATE_QUEUE operation becomes persistent when the call returns. This is the default. FALSE means the operation is part of the current transaction and becomes persistent only when the caller enters a commit. Caution: This parameter has been deprecated. |

## Usage Notes

Syntax DBMS_AQADM.CREATE_QUEUE ( queue_name IN VARCHAR2, queue_table IN VARCHAR2, queue_type IN BINARY_INTEGER DEFAULT NORMAL_QUEUE, max_retries IN NUMBER DEFAULT NULL, retry_delay IN NUMBER DEFAULT 0, retention_time IN NUMBER DEFAULT 0, dependency_tracking IN BOOLEAN DEFAULT FALSE, comment IN VARCHAR2 DEFAULT NULL, auto_commit IN BOOLEAN DEFAULT TRUE); Parameters Table 23-21 CREATE_QUEUE Procedure Parameters Parameter Description queue_name Name of the queue that is to be created. The name must be unique within a schema and must follow object name guidelines in Oracle Database SQL Language Reference with regard to reserved characters. queue_table Name of the queue table that will contain the queue. queue_type Specifies whether the queue being created is an exception queue or a normal queue. NORMAL_QUEUE means the queue is a normal queue. This is the default. EXCEPTION_QUEUE means it is an exception queue. Only the dequeue operation is allowed on the exception queue. max_retries Limits the number of times a dequeue with the REMOVE mode can be attempted on a message. The maximum value of max_retries is 2**31 -1. A message is moved to an exception queue if RETRY_COUNT is greater than MAX_RETRIES . RETRY_COUNT is incremented when the application issues a rollback after executing the dequeue. If a dequeue transaction fails because the server process dies (including ALTER SYSTEM KILL SESSION ) or SHUTDOWN ABORT on the instance, then RETRY_COUNT is not incremented. Note that max_retries is supported for all single consumer queues and 8.1-compatible or higher multiconsumer queues but not for 8.0-compatible multiconsumer queues. retry_delay Delay time, in seconds, before this message is scheduled for processing again after an application rollback. The default is 0, which means the message can be retried as soon as possible. This parameter has no effect if max_retries is set to 0. Note that retry_delay is supported for single consumer queues and 8.1-compatible or higher multiconsumer queues but not for 8.0-compatible multiconsumer queues. retention_time Number of seconds for which a message is retained in the queue table after being dequeued from the queue. INFINITE means the message is retained forever. NUMBER is the number of seconds for which to retain the messages. The default is 0, no retention. dependency_tracking Reserved for future use. FALSE is the default. TRUE is not permitted in this release. comment User-specified description of the queue. This user comment is added to the queue catalog. auto_commit TRUE causes the current transaction, if any, to commit before the CREATE_QUEUE operation is carried out. The CREATE_QUEUE operation becomes persistent when the call returns. This is the default. FALSE means the operation is part of the current transaction and becomes persistent only when the caller enters a commit. Caution: This parameter has been deprecated. Usage Notes All queue names must be unique within a schema. After a queue is created with CREATE_QUEUE , it can be enabled by calling START_QUEUE . By default, the queue is created with both enqueue and dequeue disabled.