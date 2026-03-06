---
id: 19c__V$AQ_REMOTE_DEQUEUE_AFFINITY
name: V$AQ_REMOTE_DEQUEUE_AFFINITY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: configuration
tags: [dynamic_performance]
source_file: V-AQ_REMOTE_DEQUEUE_AFFINITY.html
---

# V$AQ_REMOTE_DEQUEUE_AFFINITY

V$AQ_REMOTE_DEQUEUE_AFFINITY lists the dequeue affinity instance of the subscribers not dequeuing locally from the shard's owner instance. Cross instance message forwarding is used for these subscribers.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| QUEUE_ID | NUMBER |  |
| SHARD_ID | NUMBER |  |
| SOURCE_INSTANCE_ID | NUMBER |  |
| SUBSCRIBER_ID | NUMBER |  |
| QUEUE_SCHEMA | VARCHAR2(128) |  |
| QUEUE_NAME | VARCHAR2(128) |  |
| CON_ID | NUMBER |  |