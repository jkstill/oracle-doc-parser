---
id: 19c__V$AQ_MESSAGE_CACHE_ADVICE
name: V$AQ_MESSAGE_CACHE_ADVICE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-AQ_MESSAGE_CACHE_ADVICE.html
---

# V$AQ_MESSAGE_CACHE_ADVICE

V$AQ_MESSAGE_CACHE_ADVICE shows simulated metrics for a range of potential message cache sizes. This view assists in cache sizing by providing information in the form of metrics as described below.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SIZE_FOR_ESTIMATE | NUMBER |  |
| SIZE_FACTOR | NUMBER |  |
| ESTD_SIZE_TYPE | VARCHAR2(9) |  |
| ESTD_CACHED_SUBSHARDS | NUMBER |  |
| ESTD_UNCACHED_SUBSHARDS | NUMBER |  |
| ESTD_EVICTIONS | NUMBER |  |
| ESTD_EVICTION_RATE | NUMBER |  |
| ESTD_FG_UNEVICTIONS | NUMBER |  |
| ESTD_FG_UNEVICTION_RATE | NUMBER |  |
| ESTD_BG_UNEVICTIONS | NUMBER |  |
| ESTD_BG_UNEVICTION_RATE | NUMBER |  |
| ESTD_BG_PROCESSES | NUMBER |  |
| TOTAL_ENQUEUE_RATE | NUMBER |  |
| TOTAL_DEQUEUE_RATE | NUMBER |  |
| AVG_SUBSHARD_SIZE | NUMBER |  |
| AVG_SUBSHARD_MEMORY | NUMBER |  |
| AVG_EVICTION_TIME | NUMBER |  |
| AVG_UNEVICTION_TIME | NUMBER |  |
| FLAGS | NUMBER |  |
| SIMULATION_TIME | NUMBER |  |
| CON_ID | NUMBER |  |