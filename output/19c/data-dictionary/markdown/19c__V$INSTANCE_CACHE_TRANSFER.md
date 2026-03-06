---
id: 19c__V$INSTANCE_CACHE_TRANSFER
name: V$INSTANCE_CACHE_TRANSFER
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-INSTANCE_CACHE_TRANSFER.html
---

# V$INSTANCE_CACHE_TRANSFER

V$INSTANCE_CACHE_TRANSFER displays statistics for the cache blocks transferred among instances.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| INSTANCE | NUMBER |  |
| CLASS | VARCHAR2(18) |  |
| LOST | NUMBER |  |
| LOST_TIME | NUMBER |  |
| CR_BLOCK | NUMBER |  |
| CR_BLOCK_TIME | NUMBER |  |
| CR_2HOP | NUMBER |  |
| CR_2HOP_TIME | NUMBER |  |
| CR_3HOP | NUMBER |  |
| CR_3HOP_TIME | NUMBER |  |
| CR_BUSY | NUMBER |  |
| CR_BUSY_TIME | NUMBER |  |
| CR_CONGESTED | NUMBER |  |
| CR_CONGESTED_TIME | NUMBER |  |
| CURRENT_BLOCK | NUMBER |  |
| CURRENT_BLOCK_TIME | NUMBER |  |
| CURRENT_2HOP | NUMBER |  |
| CURRENT_2HOP_TIME | NUMBER |  |
| CURRENT_3HOP | NUMBER |  |
| CURRENT_3HOP_TIME | NUMBER |  |
| CURRENT_BUSY | NUMBER |  |
| CURRENT_BUSY_TIME | NUMBER |  |
| CURRENT_CONGESTED | NUMBER |  |
| CURRENT_CONGESTED_TIME | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Oracle keeps multiple versions of data buffered in the buffer cache. The current buffer (or block), CURRENT_BLOCK , is the most up-to-date copy, containing all recent modifications. A consistent read buffer (or block), CR_BLOCK , contains the version of the data at a particular time prior to the current buffer. It is read-consistent (that is, all the data shown in that buffer are consistent for the start time of a query). Therefore, for the same data block there can be multiple copies in the buffer cache: one current copy, and one or more consistent read copies with data consistent as of different snapshot times.