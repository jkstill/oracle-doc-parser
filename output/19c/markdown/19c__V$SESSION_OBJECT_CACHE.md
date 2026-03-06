---
id: 19c__V$SESSION_OBJECT_CACHE
name: V$SESSION_OBJECT_CACHE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-SESSION_OBJECT_CACHE.html
---

# V$SESSION_OBJECT_CACHE

V$SESSION_OBJECT_CACHE displays object cache statistics for the current user session on the local server (instance).

## Columns

| Column | Type | Description |
|--------|------|-------------|
| PINS | NUMBER |  |
| HITS | NUMBER |  |
| TRUE_HITS | NUMBER |  |
| HIT_RATIO | NUMBER |  |
| TRUE_HIT_RATIO | NUMBER |  |
| OBJECT_REFRESHES | NUMBER |  |
| CACHE_REFRESHES | NUMBER |  |
| OBJECT_FLUSHES | NUMBER |  |
| CACHE_FLUSHES | NUMBER |  |
| CACHE_SHRINKS | NUMBER |  |
| CACHED_OBJECTS | NUMBER |  |
| PINNED_OBJECTS | NUMBER |  |
| CACHE_SIZE | NUMBER |  |
| OPTIMAL_SIZE | NUMBER |  |
| MAXIMUM_SIZE | NUMBER |  |
| CON_ID | NUMBER |  |