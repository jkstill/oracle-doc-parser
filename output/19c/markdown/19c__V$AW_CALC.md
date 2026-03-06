---
id: 19c__V$AW_CALC
name: V$AW_CALC
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-AW_CALC.html
---

# V$AW_CALC

V$AW_CALC reports on the effectiveness of various caches used by Oracle OLAP during dynamic aggregation.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SESSION_ID | NUMBER |  |
| AGGREGATE_CACHE_HITS | NUMBER |  |
| AGGREGATE_CACHE_MISSES | NUMBER |  |
| SESSION_CACHE_HITS | NUMBER |  |
| SESSION_CACHE_MISSES | NUMBER |  |
| POOL_HITS | NUMBER |  |
| POOL_MISSES | NUMBER |  |
| POOL_NEW_PAGES | NUMBER |  |
| POOL_RECLAIMED_PAGES | NUMBER |  |
| CACHE_WRITES | NUMBER |  |
| POOL_SIZE | NUMBER |  |
| CURR_DML_COMMAND | VARCHAR2(64) |  |
| PREV_DML_COMMAND | VARCHAR2(64) |  |
| AGGR_FUNC_LOGICAL_NA | NUMBER |  |
| AGGR_FUNC_PRECOMPUTE | NUMBER |  |
| AGGR_FUNC_CALCS | NUMBER |  |
| CON_ID | NUMBER |  |