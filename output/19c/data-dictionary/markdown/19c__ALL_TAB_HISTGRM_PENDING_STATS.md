---
id: 19c__ALL_TAB_HISTGRM_PENDING_STATS
name: ALL_TAB_HISTGRM_PENDING_STATS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [all]
source_file: ALL_TAB_HISTGRM_PENDING_STATS.html
---

# ALL_TAB_HISTGRM_PENDING_STATS

ALL_TAB_HISTGRM_PENDING_STATS describes pending statistics for tables, partitions, and subpartitions accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the table |
| TABLE_NAME | VARCHAR2(128) | Name of the table |
| PARTITION_NAME | VARCHAR2(128) | Name of the partition |
| SUBPARTITION_NAME | VARCHAR2(128) | Name of the subpartition |
| COLUMN_NAME | VARCHAR2(128) | Name of the column |
| ENDPOINT_NUMBER | NUMBER | Endpoint number |
| ENDPOINT_VALUE | NUMBER | Normalized endpoint value |
| ENDPOINT_ACTUAL_VALUE | VARCHAR2(4000) | Actual endpoint value |
| ENDPOINT_ACTUAL_VALUE_RAW | RAW(1000) | Endpoint actual value in raw format |
| ENDPOINT_REPEAT_COUNT | NUMBER | Frequency of the endpoint (applies only to hybrid histograms, and is set to 0 for other histogram types) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_TAB_HISTGRM_PENDING_STATS describes pending statistics for tables, partitions, and subpartitions in the database. USER_TAB_HISTGRM_PENDING_STATS describes pending statistics for tables, partitions, and subpartitions owned by the current user. This view does not display the OWNER column. See Also: " DBA_TAB_HISTGRM_PENDING_STATS " " USER_TAB_HISTGRM_PENDING_STATS " See Also: " DBA_TAB_HISTGRM_PENDING_STATS " " USER_TAB_HISTGRM_PENDING_STATS "