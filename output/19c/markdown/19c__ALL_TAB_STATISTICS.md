---
id: 19c__ALL_TAB_STATISTICS
name: ALL_TAB_STATISTICS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [all]
source_file: ALL_TAB_STATISTICS.html
---

# ALL_TAB_STATISTICS

ALL_TAB_STATISTICS displays optimizer statistics for the tables accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the object |
| TABLE_NAME | VARCHAR2(128) | Name of the table |
| PARTITION_NAME | VARCHAR2(128) | Name of the partition |
| PARTITION_POSITION | NUMBER | Position of the partition within the table |
| SUBPARTITION_NAME | VARCHAR2(128) | Name of the subpartition |
| SUBPARTITION_POSITION | NUMBER | Position of the subpartition within the partition |
| OBJECT_TYPE | VARCHAR2(12) | Type of the object: TABLE PARTITION SUBPARTITION |
| NUM_ROWS | NUMBER | Number of rows in the object |
| BLOCKS | NUMBER | Number of used blocks in the object |
| EMPTY_BLOCKS | NUMBER | Number of empty blocks in the object |
| AVG_SPACE | NUMBER | Average available free space in the object |
| CHAIN_CNT | NUMBER | Number of chained rows in the object |
| AVG_ROW_LEN | NUMBER | Average row length, including row overhead |
| AVG_SPACE_FREELIST_BLOCKS | NUMBER | Average freespace of all blocks on a freelist |
| NUM_FREELIST_BLOCKS | NUMBER | Number of blocks on the freelist |
| AVG_CACHED_BLOCKS | NUMBER | Average number of blocks in the buffer cache |
| AVG_CACHE_HIT_RATIO | NUMBER | Average cache hit ratio for the object |
| IM_IMCU_COUNT | NUMBER | Number of In-Memory Compression Units (IMCUs) in the table |
| IM_BLOCK_COUNT | NUMBER | Number of In-Memory blocks in the table |
| IM_STAT_UPDATE_TIME | TIMESTAMP(9) | The timestamp of the most recent update to the In-Memory statistics |
| SCAN_RATE | NUMBER | Scan rate for the object in megabytes per second. This statistic is only relevant or meaningful for external tables. |
| SAMPLE_SIZE | NUMBER | Sample size used in analyzing the table |
| LAST_ANALYZED | DATE | Date of the most recent time the table was analyzed |
| GLOBAL_STATS | VARCHAR2(3) | GLOBAL_STATS will be YES if statistics are gathered or incrementally maintained, otherwise it will be NO |
| USER_STATS | VARCHAR2(3) | Indicates whether statistics were entered directly by the user ( YES ) or not ( NO ) |
| STATTYPE_LOCKED | VARCHAR2(5) | Type of statistics lock: DATA CACHE ALL |
| STALE_STATS | VARCHAR2(7) | Indicates whether statistics for the object are stale ( YES ) or not ( NO ) |
| NOTES Foot 1 | VARCHAR2(25) | Describes some additional properties of the statistics. For example, a value of STATS_ON_CONVENTIONAL_LOAD indicates that the statistics are obtained by online statistics gathering for conventional DML. |
| SCOPE | VARCHAR2(7) | The value is SHARED for statistics gathered on any table other than global temporary tables. For a global temporary table, the possible values are: SESSION - Indicates that the statistics are session-specific SHARED - Indicates that the statistics are shared across all sessions See Oracle Database PL/SQL Packages and Types Reference for information about using the GLOBAL_TEMP_TABLE_STATS preference of the DBMS_STATS package to control whether to gather session or shared statistics for global temporary tables. |

## Usage Notes

Related Views DBA_TAB_STATISTICS displays optimizer statistics for all tables in the database. USER_TAB_STATISTICS displays optimizer statistics for the tables owned by the current user. This view does not display the OWNER column. See Also: " DBA_TAB_STATISTICS " " USER_TAB_STATISTICS " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_STATS package See Also: " DBA_TAB_STATISTICS " " USER_TAB_STATISTICS " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_STATS package