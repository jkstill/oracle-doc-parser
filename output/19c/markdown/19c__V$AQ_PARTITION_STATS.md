---
id: 19c__V$AQ_PARTITION_STATS
name: V$AQ_PARTITION_STATS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-AQ_PARTITION_STATS.html
---

# V$AQ_PARTITION_STATS

V$AQ_PARTITION_STATS displays usage statistics for the queue partition cache and the dequeue log partition cache.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| INST_ID | NUMBER |  |
| QUEUE_ID | NUMBER |  |
| QUEUE_TABLE_ID | NUMBER |  |
| QUEUE_SCHEMA | VARCHAR2(128) |  |
| QUEUE_NAME | VARCHAR2(128) |  |
| PT_TUNED_SIZ_QT | NUMBER |  |
| PT_CACHED_PTNS_QT | NUMBER |  |
| PT_OVER_CACHED_PTNS_QT | NUMBER |  |
| PT_TOTAL_UPTUNE_QT | NUMBER |  |
| PT_NO_OF_UPTUNES_QT | NUMBER |  |
| PT_TOTAL_DOWNTUNE_QT | NUMBER |  |
| PT_NO_OF_DOWNTUNES_QT | NUMBER |  |
| PT_CACHE_MISS_QT | NUMBER |  |
| PT_CACHE_HIT_QT | NUMBER |  |
| PT_TOTAL_CACH_GET_QT | NUMBER |  |
| PT_TOTAL_CACH_PUT_QT | NUMBER |  |
| PT_UNBOUNDINGS_QT | NUMBER |  |
| PT_TUNED_SIZ_DQ | NUMBER |  |
| PT_CACHED_PTNS_DQ | NUMBER |  |
| PT_OVER_CACHED_PTNS_DQ | NUMBER |  |
| PT_TOTAL_UPTUNE_DQ | NUMBER |  |
| PT_NO_OF_UPTUNES_DQ | NUMBER |  |
| PT_TOTAL_DOWNTUNE_DQ | NUMBER |  |
| PT_NO_OF_DOWNTUNES_DQ | NUMBER |  |
| PT_CACHE_MISS_DQ | NUMBER |  |
| PT_CACHE_HIT_DQ | NUMBER |  |
| PT_TOTAL_CACH_GET_DQ | NUMBER |  |
| PT_TOTAL_CACH_PUT_DQ | NUMBER |  |
| PT_UNBOUNDINGS_DQ | NUMBER |  |
| ADD_PARTITION_FG_QT | NUMBER |  |
| ADD_PARTITION_BG_QT | NUMBER |  |
| ADD_PARTITION_FG_DQLOG | NUMBER |  |
| ADD_PARTITION_BG_DQLOG | NUMBER |  |
| TRUNC_PARTITION_QT | NUMBER |  |
| TRUNC_PARTITION_DQLOG | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Note: This view is available starting with Oracle Database release 19c, version 19.1. Note: This view is available starting with Oracle Database release 19c, version 19.1.