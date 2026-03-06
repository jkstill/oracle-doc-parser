---
id: 19c__V$SQL_WORKAREA_HISTOGRAM
name: V$SQL_WORKAREA_HISTOGRAM
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dynamic_performance]
source_file: V-SQL_WORKAREA_HISTOGRAM.html
---

# V$SQL_WORKAREA_HISTOGRAM

For each work area group, the V$SQL_WORKAREA_HISTOGRAM view shows how many work areas in that group were able to run in optimal mode, how many were able to run in one-pass mode, and finally how many ran in multi-pass mode. The DBA can take a snapshot at the beginning and the end of a desired time interval to derive the same statistics for that interval.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| LOW_OPTIMAL_SIZE | NUMBER |  |
| HIGH_OPTIMAL_SIZE | NUMBER |  |
| OPTIMAL_EXECUTIONS | NUMBER |  |
| ONEPASS_EXECUTIONS | NUMBER |  |
| MULTIPASSES_EXECUTIONS | NUMBER |  |
| TOTAL_EXECUTIONS | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: Oracle Database Performance Tuning Guide for detailed information on how to monitor automatic PGA memory performance using this view See Also: Oracle Database Performance Tuning Guide for detailed information on how to monitor automatic PGA memory performance using this view