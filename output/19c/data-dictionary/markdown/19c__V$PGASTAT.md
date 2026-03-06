---
id: 19c__V$PGASTAT
name: V$PGASTAT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-PGASTAT.html
---

# V$PGASTAT

V$PGASTAT displays PGA memory usage statistics as well as statistics about the automatic PGA memory manager when it is enabled (that is, when PGA_AGGREGATE_TARGET is set). Cumulative values in V$PGASTAT are accumulated since instance startup.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| NAME | VARCHAR2(64) |  |
| VALUE | NUMBER |  |
| UNIT | VARCHAR2(12) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: " PGA_AGGREGATE_TARGET " See Also: " PGA_AGGREGATE_TARGET "