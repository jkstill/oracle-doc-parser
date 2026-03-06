---
id: 19c__V$SQL_JOIN_FILTER
name: V$SQL_JOIN_FILTER
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dynamic_performance]
source_file: V-SQL_JOIN_FILTER.html
---

# V$SQL_JOIN_FILTER

V$SQL_JOIN_FILTER displays performance information about the characteristics of join filters when they are used for a parallel cursor. (A join filter is a bitmap filter applied to table rows before a join operation in order to avoid parallel communication.)

## Columns

| Column | Type | Description |
|--------|------|-------------|
| QC_SESSION_ID | NUMBER |  |
| QC_INSTANCE_ID | NUMBER |  |
| SQL_PLAN_HASH_VALUE | NUMBER |  |
| FILTER_ID | NUMBER |  |
| LENGTH | NUMBER |  |
| BITS_SET | NUMBER |  |
| FILTERED | NUMBER |  |
| PROBED | NUMBER |  |
| ACTIVE | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content