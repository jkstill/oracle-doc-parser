---
id: 19c__V$AQ_BMAP_NONDUR_SUBSCRIBERS
name: V$AQ_BMAP_NONDUR_SUBSCRIBERS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-AQ_BMAP_NONDUR_SUBSCRIBERS.html
---

# V$AQ_BMAP_NONDUR_SUBSCRIBERS

V$AQ_BMAP_NONDUR_SUBSCRIBERS can be used to get the available bit positions. The view is queried to get the free bit position during creation of a non-durable subscriber.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| QUEUE_ID | NUMBER |  |
| USED_POS | RAW(128) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: Oracle Database Advanced Queuing User's Guide for more information about Oracle Database Advanced Queueing See Also: Oracle Database Advanced Queuing User's Guide for more information about Oracle Database Advanced Queueing