---
id: 19c__ALL_PART_COL_STATISTICS
name: ALL_PART_COL_STATISTICS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [all]
source_file: ALL_PART_COL_STATISTICS.html
---

# ALL_PART_COL_STATISTICS

ALL_PART_COL_STATISTICS displays column statistics and histogram information for the table partitions accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the partitioned table |
| TABLE_NAME | VARCHAR2(128) | Name of the table |
| PARTITION_NAME | VARCHAR2(128) | Name of the table partition |
| COLUMN_NAME | VARCHAR2(4000) | Name of the column |
| NUM_DISTINCT | NUMBER | Number of distinct values in the column |
| LOW_VALUE | RAW(1000) | Low value in the column |
| HIGH_VALUE | RAW(1000) | High value in the column |
| DENSITY | NUMBER | If a histogram is available on COLUMN_NAME , then this column displays the selectivity of a value that spans fewer than 2 endpoints in the histogram. It does not represent the selectivity of values that span 2 or more endpoints. If a histogram is not available on COLUMN_NAME , then the value of this column is 1 / NUM_DISTINCT . |
| NUM_NULLS | NUMBER | Number of NULLs in the column |
| NUM_BUCKETS | NUMBER | Number of buckets in histogram for the column |
| SAMPLE_SIZE | NUMBER | Sample size used in analyzing the column |
| LAST_ANALYZED | DATE | Date on which the column was most recently analyzed |
| GLOBAL_STATS | VARCHAR2(3) | GLOBAL_STATS will be YES if statistics have been gathered or NO if statistics have been aggregated from subpartitions or have not been gathered |
| USER_STATS | VARCHAR2(3) | Indicates whether statistics were entered directly by the user ( YES ) or not ( NO ) |
| NOTES | VARCHAR2(63) | Describes some additional properties of the statistics. Possible values include: INCREMENTAL : Indicates that the column has synopses. INCREMENTAL(HLL) : Indicates that the column has synopses, and that the synopses are in the hyperloglog format introduced in Oracle Database 12 c Release 2 (12.2.0.1). INCREMENTAL(SAMPLING) : Indicates that the column has synopses, and that the synopses are in the adaptive sampling format introduced in Oracle Database 11 g Release 1 (11.1). This column can be used to determine whether synopses in the adaptive sampling format have been phased out entirely and purged properly. |
| AVG_COL_LEN | NUMBER | Average length of the column (in bytes) |
| HISTOGRAM | VARCHAR2(15) | Indicates existence/type of histogram: NONE FREQUENCY HEIGHT BALANCED HYBRID TOP-FREQUENCY |

## Usage Notes

Related Views DBA_PART_COL_STATISTICS displays column statistics and histogram information for all table partitions in the database. USER_PART_COL_STATISTICS displays column statistics and histogram information for the table partitions owned by the current user. This view does not display the OWNER column. See Also: " DBA_PART_COL_STATISTICS " " USER_PART_COL_STATISTICS " See Also: " DBA_PART_COL_STATISTICS " " USER_PART_COL_STATISTICS "