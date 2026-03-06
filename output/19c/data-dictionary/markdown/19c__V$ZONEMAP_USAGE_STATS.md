---
id: 19c__V$ZONEMAP_USAGE_STATS
name: V$ZONEMAP_USAGE_STATS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-ZONEMAP_USAGE_STATS.html
---

# V$ZONEMAP_USAGE_STATS

V$ZONEMAP_USAGE_STATS displays zone map usage statistics.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ZONEMAP | VARCHAR2(257) |  |
| PRUNING_TYPE | VARCHAR2(11) |  |
| EXECUTIONS | NUMBER |  |
| BASE_COUNT | NUMBER |  |
| PRUNED_COUNT | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content The ratio ( PRUNED_COUNT / BASE_COUNT ) shows the fraction of data pruned by the zone map.