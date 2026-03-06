---
id: 19c__V$PERSISTENT_QUEUES
name: V$PERSISTENT_QUEUES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-PERSISTENT_QUEUES.html
---

# V$PERSISTENT_QUEUES

QUEUE_ID

## Columns

| Column | Type | Description |
|--------|------|-------------|
| QUEUE_ID | NUMBER |  |
| QUEUE_TABLE_ID | NUMBER |  |
| QUEUE_SCHEMA | VARCHAR2(128) |  |
| QUEUE_NAME | VARCHAR2(128) |  |
| FIRST_ACTIVITY_TIME | TIMESTAMP(6) |  |
| ENQUEUED_MSGS | NUMBER |  |
| DEQUEUED_MSGS | NUMBER |  |
| BROWSED_MSGS | NUMBER |  |
| ELAPSED_ENQUEUE_TIME | NUMBER |  |
| ELAPSED_DEQUEUE_TIME | NUMBER |  |
| ENQUEUE_CPU_TIME | NUMBER |  |
| DEQUEUE_CPU_TIME | NUMBER |  |
| AVG_MSG_AGE | NUMBER |  |
| DEQUEUED_MSG_LATENCY | NUMBER |  |
| ELAPSED_TRANSFORMATION_TIME | NUMBER |  |
| ELAPSED_RULE_EVALUATION_TIME | NUMBER |  |
| ENQUEUED_EXPIRY_MSGS | NUMBER |  |
| ENQUEUED_DELAY_MSGS | NUMBER |  |
| MSGS_MADE_EXPIRED | NUMBER |  |
| MSGS_MADE_READY | NUMBER |  |
| LAST_ENQUEUE_TIME | TIMESTAMP(6) |  |
| LAST_DEQUEUE_TIME | TIMESTAMP(6) |  |
| LAST_TM_EXPIRY_TIME | TIMESTAMP(6) |  |
| LAST_TM_READY_TIME | TIMESTAMP(6) |  |
| ENQUEUE_TRANSACTIONS | NUMBER |  |
| DEQUEUE_TRANSACTIONS | NUMBER |  |
| EXECUTION_COUNT | NUMBER |  |
| OLDEST_MSGID | RAW(16) |  |
| OLDEST_MSG_ENQTM | TIMESTAMP(6) |  |
| MANDATORY_AFF_SWITCHES_OUT | NUMBER |  |
| OPTIONAL_AFF_SWITCHES_OUT | NUMBER |  |
| AFF_SWITCHES_BACK_IN | NUMBER |  |
| CROSS_STREAM_JOBS | NUMBER |  |
| RESTORE_BITMAP_JOBS | NUMBER |  |
| SHADOW_AFF_SWITCHES_IN | NUMBER |  |
| SHADOW_AFF_SWITCHES_OUT | NUMBER |  |
| SHADOW_SHARDS_RECEIVED | NUMBER |  |
| SHADOW_SHARDS_FREED | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Note: For sharded queues, only the following columns in this view contain accurate information: FIRST_ACTIVITY_TIME , BROWSED_MSGS , LAST_ENQUEUE_TIME , LAST_DEQUEUE_TIME , ENQUEUE_TRANSACTIONS , and DEQUEUE_TRANSACTIONS . The rest of the columns in this view should be ignored when querying information about sharded queues. Note: For sharded queues, only the following columns in this view contain accurate information: FIRST_ACTIVITY_TIME , BROWSED_MSGS , LAST_ENQUEUE_TIME , LAST_DEQUEUE_TIME , ENQUEUE_TRANSACTIONS , and DEQUEUE_TRANSACTIONS . The rest of the columns in this view should be ignored when querying information about sharded queues.