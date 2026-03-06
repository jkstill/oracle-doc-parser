---
id: 19c__V$AQ_NONDUR_SUBSCRIBER
name: V$AQ_NONDUR_SUBSCRIBER
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-AQ_NONDUR_SUBSCRIBER.html
---

# V$AQ_NONDUR_SUBSCRIBER

V$AQ_NONDUR_SUBSCRIBER provides information about the non-durable subscriptions on sharded queues.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| QUEUE_ID | NUMBER |  |
| SUBSCRIBER_ID | NUMBER |  |
| SUBSCRIBER_NAME | VARCHAR2(128) |  |
| RULE_CONDITION | VARCHAR2(4000) |  |
| TRANSFORMATION_OWNER | VARCHAR2(128) |  |
| TRANSFORMATION_NAME | VARCHAR2(128) |  |
| CREATION_TIME | TIMESTAMP(1) WITH TIME ZONE |  |
| FLAGS | NUMBER |  |
| SUBSCRIBER_TYPE | NUMBER |  |
| BITPOS | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

See Also: Oracle Database Advanced Queuing User's Guide for more information about Oracle Database Advanced Queueing See Also: Oracle Database Advanced Queuing User's Guide for more information about Oracle Database Advanced Queueing