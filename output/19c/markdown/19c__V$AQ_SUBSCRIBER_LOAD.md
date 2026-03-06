---
id: 19c__V$AQ_SUBSCRIBER_LOAD
name: V$AQ_SUBSCRIBER_LOAD
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-AQ_SUBSCRIBER_LOAD.html
---

# V$AQ_SUBSCRIBER_LOAD

V$AQ_SUBSCRIBER_LOAD describes the load of all subscribers of sharded queues in terms of latency at every instance in an Oracle RAC environment.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| QUEUE_ID | NUMBER |  |
| QUEUE_SCHEMA | VARCHAR2(128) |  |
| QUEUE_NAME | VARCHAR2(128) |  |
| SUBSCRIBER_ID | NUMBER |  |
| SUBSCRIBER_NAME | VARCHAR2(128) |  |
| LATENCY_STATE | VARCHAR2(8) |  |
| LATENCY | NUMBER |  |
| DEQUEUE_REQUESTS | NUMBER |  |
| ACTIVE_SHARDS | NUMBER |  |
| ACTIVE_LISTENER | VARCHAR2(5) |  |
| DEQUEUE_SESSIONS Foot 1 | NUMBER |  |
| FLAGS | NUMBER |  |
| MANDATORY_AFF_SWITCHES | NUMBER |  |
| OPTIONAL_AFF_SWITCHES | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Latency denotes the predicted amount of time (in seconds) required from the current time to drain all the messages for that subscriber at each respective instance. The latency calculation considers past enqueue/dequeue rates and future enqueue/dequeue rates based on history. See Also: Oracle Database Advanced Queuing User's Guide for more information about Oracle Database Advanced Queueing See Also: Oracle Database Advanced Queuing User's Guide for more information about Oracle Database Advanced Queueing