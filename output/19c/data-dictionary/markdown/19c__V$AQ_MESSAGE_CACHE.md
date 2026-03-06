---
id: 19c__V$AQ_MESSAGE_CACHE
name: V$AQ_MESSAGE_CACHE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-AQ_MESSAGE_CACHE.html
---

# V$AQ_MESSAGE_CACHE

V$AQ_MESSAGE_CACHE provides performance statistics of the message cache for sharded queues at the subshard level in the instance.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| QUEUE_ID | NUMBER |  |
| SHARD_ID | NUMBER |  |
| PRIORITY | NUMBER |  |
| SUBSHARD_ID | NUMBER |  |
| PARTITION_ID | NUMBER |  |
| MAX_MSGS | NUMBER |  |
| ENQUEUED_MSGS | NUMBER |  |
| MSGS_MADE_EXPIRED | NUMBER |  |
| CHUNK_SIZE | NUMBER |  |
| NUM_CHUNKS | NUMBER |  |
| NUM_FREE_CHUNKS | NUMBER |  |
| USED_MEMORY_SIZE | NUMBER |  |
| STATE | VARCHAR2(13) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: Oracle Database Advanced Queuing User's Guide for more information about Oracle Database Advanced Queueing See Also: Oracle Database Advanced Queuing User's Guide for more information about Oracle Database Advanced Queueing