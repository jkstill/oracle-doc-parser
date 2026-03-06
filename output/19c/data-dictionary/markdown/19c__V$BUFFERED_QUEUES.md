---
id: 19c__V$BUFFERED_QUEUES
name: V$BUFFERED_QUEUES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-BUFFERED_QUEUES.html
---

# V$BUFFERED_QUEUES

V$BUFFERED_QUEUES displays information about all buffered queues in the instance. There is one row per queue.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| QUEUE_ID | NUMBER |  |
| QUEUE_SCHEMA | VARCHAR2(128) |  |
| QUEUE_NAME | VARCHAR2(128) |  |
| STARTUP_TIME | DATE |  |
| NUM_MSGS | NUMBER |  |
| SPILL_MSGS | NUMBER |  |
| CNUM_MSGS | NUMBER |  |
| CSPILL_MSGS | NUMBER |  |
| EXPIRED_MSGS | NUMBER |  |
| OLDEST_MSGID | RAW(16) |  |
| OLDEST_MSG_ENQTM | TIMESTAMP(3) |  |
| QUEUE_STATE | VARCHAR2(25) |  |
| ELAPSED_ENQUEUE_TIME | NUMBER |  |
| ELAPSED_DEQUEUE_TIME | NUMBER |  |
| ELAPSED_TRANSFORMATION_TIME | NUMBER |  |
| ELAPSED_RULE_EVALUATION_TIME | NUMBER |  |
| ENQUEUE_CPU_TIME | NUMBER |  |
| DEQUEUE_CPU_TIME | NUMBER |  |
| AVG_MSG_AGE | NUMBER |  |
| LAST_ENQUEUE_TIME | TIMESTAMP(3) WITH TIME ZONE |  |
| LAST_DEQUEUE_TIME | TIMESTAMP(3) WITH TIME ZONE |  |
| QUEUE_SIZE | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content