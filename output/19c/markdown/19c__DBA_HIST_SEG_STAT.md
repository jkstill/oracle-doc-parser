---
id: 19c__DBA_HIST_SEG_STAT
name: DBA_HIST_SEG_STAT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_HIST_SEG_STAT.html
---

# DBA_HIST_SEG_STAT

DBA_HIST_SEG_STAT displays historical information about segment-level statistics.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| TS# | NUMBER | Tablespace number |
| OBJ# | NUMBER | Dictionary object number |
| DATAOBJ# | NUMBER | Data object number |
| LOGICAL_READS_TOTAL | NUMBER | Cumulative value for logical reads |
| LOGICAL_READS_DELTA | NUMBER | Delta value for logical reads |
| BUFFER_BUSY_WAITS_TOTAL | NUMBER | Cumulative value for buffer busy waits |
| BUFFER_BUSY_WAITS_DELTA | NUMBER | Delta value for buffer busy waits |
| DB_BLOCK_CHANGES_TOTAL | NUMBER | Cumulative value for db block changes (in blocks) |
| DB_BLOCK_CHANGES_DELTA | NUMBER | Delta value for db block changes (in blocks) |
| PHYSICAL_READS_TOTAL | NUMBER | Cumulative value for physical reads (in blocks) |
| PHYSICAL_READS_DELTA | NUMBER | Delta value for physical reads (in blocks) |
| PHYSICAL_WRITES_TOTAL | NUMBER | Cumulative value for physical writes (in blocks) |
| PHYSICAL_WRITES_DELTA | NUMBER | Delta value for physical writes (in blocks) |
| PHYSICAL_READS_DIRECT_TOTAL | NUMBER | Cumulative value for physical reads direct (in blocks) |
| PHYSICAL_READS_DIRECT_DELTA | NUMBER | Delta value for physical reads direct (in blocks) |
| PHYSICAL_WRITES_DIRECT_TOTAL | NUMBER | Cumulative value for physical writes direct (in blocks) |
| PHYSICAL_WRITES_DIRECT_DELTA | NUMBER | Delta value for physical writes direct (in blocks) |
| ITL_WAITS_TOTAL | NUMBER | Cumulative value for ITL waits |
| ITL_WAITS_DELTA | NUMBER | Delta value for ITL waits |
| ROW_LOCK_WAITS_TOTAL | NUMBER | Cumulative value for row lock waits |
| ROW_LOCK_WAITS_DELTA | NUMBER | Delta value for row lock waits |
| GC_CR_BLOCKS_SERVED_TOTAL | NUMBER | Cumulative value for global cache CR blocks served |
| GC_CR_BLOCKS_SERVED_DELTA | NUMBER | Delta value for global cache CR blocks served |
| GC_CU_BLOCKS_SERVED_TOTAL | NUMBER | Cumulative value for global cache current blocks served |
| GC_CU_BLOCKS_SERVED_DELTA | NUMBER | Delta value for global cache current blocks served |
| GC_BUFFER_BUSY_TOTAL | NUMBER | Cumulative value for global cache buffer busy |
| GC_BUFFER_BUSY_DELTA | NUMBER | Delta value for global cache buffer busy |
| GC_CR_BLOCKS_RECEIVED_TOTAL | NUMBER | Cumulative value for global cache CR blocks received |
| GC_CR_BLOCKS_RECEIVED_DELTA | NUMBER | Delta value for global cache CR blocks received |
| GC_CU_BLOCKS_RECEIVED_TOTAL | NUMBER | Cumulative value for global cache current blocks received |
| GC_CU_BLOCKS_RECEIVED_DELTA | NUMBER | Delta value for global cache current blocks received |
| SPACE_USED_TOTAL | NUMBER | Number of bytes used by user data |
| SPACE_USED_DELTA | NUMBER | Delta value for space used by user data (in bytes). A negative value indicates the number of bytes deleted in the segment. |
| SPACE_ALLOCATED_TOTAL | NUMBER | The number of bytes that are allocated |
| SPACE_ALLOCATED_DELTA | NUMBER | Delta value for the space allocated (in bytes). A negative value indicates the number of bytes deallocated to the tablespace. |
| TABLE_SCANS_TOTAL | NUMBER | Cumulative value for table scans |
| TABLE_SCANS_DELTA | NUMBER | Delta value for table scans |
| CHAIN_ROW_EXCESS_TOTAL | NUMBER | Cumulative value of number of chained row pieces that can be eliminated by table reorganization |
| CHAIN_ROW_EXCESS_DELTA | NUMBER | Delta value of number of chained row pieces that can be eliminated by table reorganization |
| PHYSICAL_READ_REQUESTS_TOTAL | NUMBER | Cumulative value of number of physical read I/O requests issued for the monitored segment |
| PHYSICAL_READ_REQUESTS_DELTA | NUMBER | Delta value of number of physical read I/O requests issued for the monitored segment |
| PHYSICAL_WRITE_REQUESTS_TOTAL | NUMBER | Cumulative value of number of physical write I/O requests issued for the monitored segment |
| PHYSICAL_WRITE_REQUESTS_DELTA | NUMBER | Delta value of number of physical write I/O requests issued for the monitored segment |
| OPTIMIZED_PHYSICAL_READS_TOTAL | NUMBER | Cumulative value of number of physical reads from Database Smart Flash Cache for the monitored segment |
| OPTIMIZED_PHYSICAL_READS_DELTA | NUMBER | Delta value of number of physical reads from Database Smart Flash Cache for the monitored segment |
| IM_SCANS_TOTAL | NUMBER | Count of segment statistics |
| IM_SCANS_DELTA | NUMBER | Delta values for in-memory scans |
| POPULATE_CUS_TOTAL | NUMBER | Count of compression units (CUs) populated per segment |
| POPULATE_CUS_DELTA | NUMBER | Delta value for compression unit (CU) populate operations |
| REPOPULATE_CUS_TOTAL | NUMBER | Count of CUs repopulated per segment |
| REPOPULATE_CUS_DELTA | NUMBER | Delta value for compression unit (CU) repopulate operations |
| IM_DB_BLOCK_CHANGES_TOTAL | NUMBER | The total number of changes that were part of an update or delete operation that were made to segment blocks |
| IM_DB_BLOCK_CHANGES_DELTA | NUMBER | Delta value for database block changes |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

This view captures the top segments based on a set of criteria and captures information from V$SEGSTAT . The total value is the value of the statistics since instance startup. The delta value is the value of the statistics from the BEGIN_INTERVAL_TIME to the END_INTERVAL_TIME in the DBA_HIST_SNAPSHOT view. See Also: " V$SEGSTAT " " DBA_HIST_SNAPSHOT " See Also: " V$SEGSTAT " " DBA_HIST_SNAPSHOT "