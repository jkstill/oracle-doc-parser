---
id: 19c__V$FILE_HISTOGRAM
name: V$FILE_HISTOGRAM
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-FILE_HISTOGRAM.html
---

# V$FILE_HISTOGRAM

V$FILE_HISTOGRAM displays a histogram of all synchronous single block reads on a per-file basis (for data files). The histogram has buckets of time intervals from < 1 ms, < 2 ms, < 4 ms, < 8 ms, ... < 2 21 ms, < 2 22 ms, and >= 2 22 ms.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FILE# | NUMBER |  |
| SINGLEBLKRDTIM_MILLI | NUMBER |  |
| SINGLEBLKRDS | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content The histogram will not be filled unless the STATISTICS_LEVEL initialization parameter is set to ALL .