---
id: 19c__DBMS_AQADM.GET_QUEUE_PARAMETER
name: DBMS_AQADM.GET_QUEUE_PARAMETER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQADM
tags: [dbms_aqadm]
source_file: DBMS_AQADM.html
---

# DBMS_AQADM.GET_QUEUE_PARAMETER

This procedure allows user to get different parameters for sharded queues at queue or database level.

## Syntax

```sql
PROCEDURE  GET_QUEUE_PARAMETER(
    queue_name          IN VARCHAR2,
    param_name          IN VARCHAR2,
    param_value         OUT NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| queue_name | VARCHAR2 | IN | The name of the sharded queue. |
| param_name | VARCHAR2 | IN | The name of the parameter. Table 23-38 and Table 23-39 describe the valid parameter names. |
| param_value | NUMBER) | OUT | The value of the parameter. |

## Usage Notes

For database level the queue_name should be NULL . Note that queue overrides database level parameter values. See Also: Oracle® Database Advanced Queuing User's Guide for information about sharded queues See Also: Oracle® Database Advanced Queuing User's Guide for information about sharded queues Syntax PROCEDURE GET_QUEUE_PARAMETER( queue_name IN VARCHAR2, param_name IN VARCHAR2, param_value OUT NUMBER); Parameters Table 23-37 GET_QUEUE_PARAMETER Procedure Parameters Parameter Description queue_name The name of the sharded queue. param_name The name of the parameter. Table 23-38 and Table 23-39 describe the valid parameter names. param_value The value of the parameter. Table 23-38 Sharded queue parameters Parameter Name Scope Allowed Values Description SHARD_NUM Queue level [1, UB4MAXVAL] Maximum number of shards allowed for the queue. KEY_BASED_ENQUEUE Queue level [0,1] When set, the shard to which a message gets enqueued is determined by the key value specified in the message. Refer to key-based sharding (link) for more details. This parameter cannot be unset once set. When this parameter is not set (default), a session is bound to a shard at the time of first enqueue to the queue. All messages enqueued by the session will go to the same shard to which the session is bound. STICKY_DEQUEUE Queue level [0,1] When set, dequeue session sticks to a shard in the queue. A session is bound to a shard on first dequeue from the queue. All messages dequeued by the session come from the same shard to which it is bound. This parameter cannot be unset once set. When this parameter is not set, messages dequeued by a session can spread across multiple shards of the queue. Table 23-39 Key-based Parameters Parameter Name Scope Description AQ$KEY_TO_SHARD_MAP Queue level Shard number to which a given key is mapped. When key-based sharding is enabled, this parameter is used to establish mapping between a key and a shard number or retrieve the shard number to which given key is mapped. AQ$GET_KEY_SHARD_INST Queue level Instance number that owns the shard to which a given key is mapped. Applicable only when key-based sharding is enabled. It is a read-only parameter.