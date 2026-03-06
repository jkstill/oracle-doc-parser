---
id: 19c__V$PERSISTENT_SUBSCRIBERS
name: V$PERSISTENT_SUBSCRIBERS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-PERSISTENT_SUBSCRIBERS.html
---

# V$PERSISTENT_SUBSCRIBERS

V$PERSISTENT_SUBSCRIBERS displays information about all active subscribers of the persistent queues in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| QUEUE_ID | NUMBER |  |
| QUEUE_SCHEMA | VARCHAR2(128) |  |
| QUEUE_NAME | VARCHAR2(128) |  |
| SUBSCRIBER_ID | NUMBER |  |
| SUBSCRIBER_NAME | VARCHAR2(512) |  |
| SUBSCRIBER_ADDRESS | VARCHAR2(1024) |  |
| PROTOCOL | NUMBER |  |
| SUBSCRIBER_TYPE | VARCHAR2(128) |  |
| FIRST_ACTIVITY_TIME | TIMESTAMP(6) |  |
| ENQUEUED_MSGS | NUMBER |  |
| DEQUEUED_MSGS | NUMBER |  |
| AVG_MSG_AGE | NUMBER |  |
| BROWSED_MSGS | NUMBER |  |
| EXPIRED_MSGS | NUMBER |  |
| DEQUEUED_MSG_LATENCY | NUMBER |  |
| LAST_ENQUEUE_TIME | TIMESTAMP(6) |  |
| LAST_DEQUEUE_TIME | TIMESTAMP(6) |  |
| ELAPSED_DEQUEUE_TIME | NUMBER |  |
| DEQUEUE_CPU_TIME | NUMBER |  |
| DEQUEUE_TRANSACTIONS | NUMBER |  |
| EXECUTION_COUNT | NUMBER |  |
| DEQUEUE_MEMORY_LOCKS | NUMBER |  |
| DEQUEUE_DISK_LOCKS | NUMBER |  |
| DEQUEUE_DISK_DELETES | NUMBER |  |
| OLDEST_MSGID | RAW(16) |  |
| OLDEST_MSG_ENQTM | TIMESTAMP(6) |  |
| PARENT_SUBSCRIBER_ID | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content There is one row per instance per queue per subscriber. The rows are deleted when the database (or instance in an Oracle RAC environment) restarts. Note: This view does not display information about sharded queues. For information about sharded queues, refer to the " V$AQ_SHARDED_SUBSCRIBER_STAT " view. Note: This view does not display information about sharded queues. For information about sharded queues, refer to the " V$AQ_SHARDED_SUBSCRIBER_STAT " view.