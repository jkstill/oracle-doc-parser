---
id: 19c__V$AQ_NONDUR_SUBSCRIBER_LWM
name: V$AQ_NONDUR_SUBSCRIBER_LWM
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-AQ_NONDUR_SUBSCRIBER_LWM.html
---

# V$AQ_NONDUR_SUBSCRIBER_LWM

V$AQ_NONDUR_SUBSCRIBER_LWM projects the low watermarks (LWMs) of non-durable subscribers in a sharded queue. The LWM of a non-durable subscriber is a combination of shard, priority and LWM (subshard).

## Columns

| Column | Type | Description |
|--------|------|-------------|
| QUEUE_ID | NUMBER |  |
| SUBSCRIBER_ID | NUMBER |  |
| SHARD_ID | NUMBER |  |
| PRIORITY | NUMBER |  |
| LWM | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

See Also: Oracle Database Advanced Queuing User's Guide for more information about Oracle Database Advanced Queueing See Also: Oracle Database Advanced Queuing User's Guide for more information about Oracle Database Advanced Queueing