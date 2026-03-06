---
id: 19c__DBMS_AQADM.ALTER_SHARDED_QUEUE
name: DBMS_AQADM.ALTER_SHARDED_QUEUE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQADM
tags: [dbms_aqadm]
source_file: DBMS_AQADM.html
---

# DBMS_AQADM.ALTER_SHARDED_QUEUE

This procedure provides user the ability to alter a sharded queue.

## Syntax

```sql
PROCEDURE ALTER_SHARDED_QUEUE(
    queue_name             IN VARCHAR2,
    max_retries            IN NUMBER         DEFAULT NULL,
    comment                IN VARCHAR2       DEFAULT NULL,
    queue_properties       IN QUEUE_PROPS_T  DEFAULT NULL,
    replication_mode       IN BINARY_INTEGER DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| queue_name | VARCHAR2 | IN | This parameter specifies the name of the sharded queue. A maximum of 128 characters are allowed. |
| max_retries | NUMBER | IN | The maximum number of retries allowed. |
| comment | VARCHAR2 | IN | The comment of the queue. |
| queue_properties | QUEUE_PROPS_T | IN | Properties such as Normal or Exception Queue, Retry delay, retention time, sort list and cache hint. Refer to QUEUE_PROPS_T Type for more information about queue_properties . |
| replication_mode | BINARY_INTEGER | IN | Reserved for future use. DBMS_AQADM.REPLICATION_MODE if queue is being altered to be in the Replication Mode or else DBMS_AQADM.NONE . Default is NULL . |

## Usage Notes

See Also: Oracle® Database Advanced Queuing User's Guide for information about sharded queues See Also: Oracle® Database Advanced Queuing User's Guide for information about sharded queues Syntax PROCEDURE ALTER_SHARDED_QUEUE( queue_name IN VARCHAR2, max_retries IN NUMBER DEFAULT NULL, comment IN VARCHAR2 DEFAULT NULL, queue_properties IN QUEUE_PROPS_T DEFAULT NULL, replication_mode IN BINARY_INTEGER DEFAULT NULL); Parameters Table 23-17 ALTER_SHARDED_QUEUE Procedure Parameters Parameter Description queue_name This parameter specifies the name of the sharded queue. A maximum of 128 characters are allowed. max_retries The maximum number of retries allowed. comment The comment of the queue. queue_properties Properties such as Normal or Exception Queue, Retry delay, retention time, sort list and cache hint. Refer to QUEUE_PROPS_T Type for more information about queue_properties . replication_mode Reserved for future use. DBMS_AQADM.REPLICATION_MODE if queue is being altered to be in the Replication Mode or else DBMS_AQADM.NONE . Default is NULL .