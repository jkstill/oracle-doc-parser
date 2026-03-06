---
id: 19c__V$AQ_SHARDED_SUBSCRIBER_STAT
name: V$AQ_SHARDED_SUBSCRIBER_STAT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-AQ_SHARDED_SUBSCRIBER_STAT.html
---

# V$AQ_SHARDED_SUBSCRIBER_STAT

V$AQ_SHARDED_SUBSCRIBER_STAT displays basic statistical information about the subscribers of sharded queues. There is one row per queue per shard per subscriber.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| QUEUE_ID | NUMBER |  |
| SUBSCRIBER_ID | NUMBER |  |
| SHARD_ID | NUMBER |  |
| PRIORITY | NUMBER |  |
| DEQUEUE_SUBSHARD | NUMBER |  |
| ENQUEUED_MSGS | NUMBER |  |
| DEQUEUED_MSGS | NUMBER |  |
| ELAPSED_DEQUEUE_TIME | NUMBER |  |
| CPU_DEQUEUE_TIME | NUMBER |  |
| DEQUEUE_RATE | NUMBER |  |
| TIME_SINCE_LAST_DEQUEUE | NUMBER |  |
| ESTD_TIME_TO_DRAIN | NUMBER |  |
| ESTD_TIME_TO_DRAIN_NO_ENQ | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content