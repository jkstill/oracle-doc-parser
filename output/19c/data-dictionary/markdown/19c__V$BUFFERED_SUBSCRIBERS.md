---
id: 19c__V$BUFFERED_SUBSCRIBERS
name: V$BUFFERED_SUBSCRIBERS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-BUFFERED_SUBSCRIBERS.html
---

# V$BUFFERED_SUBSCRIBERS

V$BUFFERED_SUBSCRIBERS displays information about the subscribers for all buffered queues in the instance. There is one row per subscriber per queue.

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
| STARTUP_TIME | DATE |  |
| LAST_BROWSED_SEQ | NUMBER |  |
| LAST_BROWSED_NUM | NUMBER |  |
| LAST_DEQUEUED_SEQ | NUMBER |  |
| LAST_DEQUEUED_NUM | NUMBER |  |
| CURRENT_ENQ_SEQ | NUMBER |  |
| NUM_MSGS | NUMBER |  |
| CNUM_MSGS | NUMBER |  |
| TOTAL_DEQUEUED_MSG | NUMBER |  |
| TOTAL_SPILLED_MSG | NUMBER |  |
| EXPIRED_MSGS | NUMBER |  |
| MESSAGE_LAG | NUMBER |  |
| ELAPSED_DEQUEUE_TIME | NUMBER |  |
| DEQUEUE_CPU_TIME | NUMBER |  |
| AVG_MSG_AGE | NUMBER |  |
| LAST_DEQUEUE_TIME | TIMESTAMP(3) WITH TIME ZONE |  |
| OLDEST_MSGID | RAW(16) |  |
| OLDEST_MSG_ENQTM | TIMESTAMP(3) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content