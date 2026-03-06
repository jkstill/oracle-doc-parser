---
id: 19c__V$AQ_MESSAGE_CACHE_STAT
name: V$AQ_MESSAGE_CACHE_STAT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-AQ_MESSAGE_CACHE_STAT.html
---

# V$AQ_MESSAGE_CACHE_STAT

V$AQ_MESSAGE_CACHE_STAT displays statistics about memory management for sharded queues in the Streams pool within the System Global Area (SGA). Sharded queues use the Streams pool in units of subshards. Thus, columns of this view shows statistics at subshard level. This view shows statistics across all sharded queues.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| NUM_EVICTED | NUMBER |  |
| NUM_PREFETCHED | NUMBER |  |
| NUM_UNEVICTION | NUMBER |  |
| NUM_UNCACHED | NUMBER |  |
| NUM_TRACKED | NUMBER |  |
| NUM_CACHED | NUMBER |  |
| MAX_SUBSH_SIZE | NUMBER |  |
| MIN_SUBSH_SIZE | NUMBER |  |
| MEAN_SUBSH_SIZE | NUMBER |  |
| AVG_EVICTION_RATE | NUMBER |  |
| AVG_LOAD_RATE | NUMBER |  |
| AVG_EVICTION_TIME | NUMBER |  |
| AVG_LOAD_TIME | NUMBER |  |
| AVG_MISS_RATIO | NUMBER |  |
| AVG_THRASH_RATIO | NUMBER |  |
| MANDATORY_AFF_SWITCH_ATTEMPTS | NUMBER |  |
| OPTIONAL_AFF_SWITCH_ATTEMPTS | NUMBER |  |
| MIN_EVICT_PERCENT | NUMBER |  |
| LAST_AVG_CACHED_HORIZON | NUMBER |  |
| LAST_AVG_MEMORY_HORIZON | NUMBER |  |
| LAST_AVG_SUBSHARD_HORIZON | NUMBER |  |
| LAST_LEEWAY_SHIFT | NUMBER |  |
| AVG_OPTTIME_DRIFT | NUMBER |  |
| NUM_THRESHOLD_DRIFT | NUMBER |  |
| MAX_OPT_TIME_DRIFT | NUMBER |  |
| MIN_OPT_TIME_DRIFT | NUMBER |  |
| AVG_OPT_TIME_ERROR | NUMBER |  |
| MAX_OPT_TIME_ERROR | NUMBER |  |
| MIN_OPT_TIME_ERROR | NUMBER |  |
| CON_ID | NUMBER |  |