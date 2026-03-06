---
id: 19c__ALL_TAB_PENDING_STATS
name: ALL_TAB_PENDING_STATS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [all]
source_file: ALL_TAB_PENDING_STATS.html
---

# ALL_TAB_PENDING_STATS

ALL_TAB_PENDING_STATS describes pending statistics for tables, partitions, and subpartitions accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the table |
| TABLE_NAME | VARCHAR2(128) | Name of the table |
| PARTITION_NAME | VARCHAR2(128) | Name of the partition |
| SUBPARTITION_NAME | VARCHAR2(128) | Name of the subpartition |
| NUM_ROWS | NUMBER | Number of rows |
| BLOCKS | NUMBER | Number of blocks |
| AVG_ROW_LEN | NUMBER | Average row length |
| IM_IMCU_COUNT | NUMBER | Number of In-Memory Compression Units (IMCUs) in the table. |
| IM_BLOCK_COUNT | NUMBER | Number of In-Memory blocks in the table. |
| SCAN_RATE | NUMBER | Scan rate for the table in megabytes per second. This statistic is only relevant or meaningful for external tables. |
| SAMPLE_SIZE | NUMBER | Sample size |
| LAST_ANALYZED | DATE | Time of last analyze operation |

## Usage Notes

Related Views DBA_TAB_PENDING_STATS describes pending statistics for tables, partitions, and subpartitions in the database. USER_TAB_PENDING_STATS describes pending statistics for tables, partitions, and subpartitions owned by the current user. This view does not display the OWNER column. See Also: " DBA_TAB_PENDING_STATS " " USER_TAB_PENDING_STATS " See Also: " DBA_TAB_PENDING_STATS " " USER_TAB_PENDING_STATS "