---
id: 19c__DBA_INDEX_USAGE
name: DBA_INDEX_USAGE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: index
tags: [dba]
source_file: DBA_INDEX_USAGE.html
---

# DBA_INDEX_USAGE

DBA_INDEX_USAGE displays cumulative statistics for each index.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OBJECT_ID | NUMBER | Object ID for the index |
| NAME | VARCHAR2(128) | Index name |
| OWNER | VARCHAR2(128) | Index owner |
| TOTAL_ACCESS_COUNT | NUMBER | Total number of times the index has been accessed |
| TOTAL_EXEC_COUNT | NUMBER | Total executions the index has participated in |
| TOTAL_ROWS_RETURNED | NUMBER | Total rows returned by the index. Index usage is categorized into buckets of different ranges. Each bucket has a range of values for access count and rows returned. An entry is placed into a bucket if the rows returned or access counts falls within the range of that bucket. |
| BUCKET_0_ACCESS_COUNT | NUMBER | The index has not been accessed |
| BUCKET_1_ACCESS_COUNT | NUMBER | The index has been accessed once |
| BUCKET_2_10_ACCESS_COUNT | NUMBER | The index has been accessed between 2 and 10 times |
| BUCKET_2_10_ROWS_RETURNED | NUMBER | The index has returned between 2 and 10 rows |
| BUCKET_11_100_ACCESS_COUNT | NUMBER | The index has been accessed between 11 and 100 times |
| BUCKET_11_100_ROWS_RETURNED | NUMBER | The index has returned between 11 and 100 rows |
| BUCKET_101_1000_ACCESS_COUNT | NUMBER | The index has been accessed between 101 and 1000 times |
| BUCKET_101_1000_ROWS_RETURNED | NUMBER | The index has returned between 101 and 1000 rows |
| BUCKET_1000_PLUS_ACCESS_COUNT | NUMBER | The index has been accessed more than 1000 times |
| BUCKET_1000_PLUS_ROWS_RETURNED | NUMBER | The index has returned more than 1000 rows |
| LAST_USED | DATE | Time that the index was last used |

## Usage Notes

See Also: " V$INDEX_USAGE_INFO " See Also: " V$INDEX_USAGE_INFO "