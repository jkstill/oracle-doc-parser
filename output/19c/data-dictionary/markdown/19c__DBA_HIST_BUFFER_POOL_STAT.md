---
id: 19c__DBA_HIST_BUFFER_POOL_STAT
name: DBA_HIST_BUFFER_POOL_STAT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_HIST_BUFFER_POOL_STAT.html
---

# DBA_HIST_BUFFER_POOL_STAT

DBA_HIST_BUFFER_POOL_STAT displays historical statistics about all buffer pools available for the instance.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| ID | NUMBER | Buffer pool identifier number |
| NAME | VARCHAR2(20) | Name of the buffer pool |
| BLOCK_SIZE | NUMBER | Block Size |
| SET_MSIZE | NUMBER | Buffer pool maximum set size |
| CNUM_REPL | NUMBER | Number of buffers on the replacement list |
| CNUM_WRITE | NUMBER | Number of buffers on the write list |
| CNUM_SET | NUMBER | Number of buffers in the set |
| BUF_GOT | NUMBER | Number of buffers gotten by the set |
| SUM_WRITE | NUMBER | Number of buffers written by the set |
| SUM_SCAN | NUMBER | Number of buffers scanned in the set |
| FREE_BUFFER_WAIT | NUMBER | Free buffer wait statistic |
| WRITE_COMPLETE_WAIT | NUMBER | Write complete wait statistic |
| BUFFER_BUSY_WAIT | NUMBER | Buffer busy wait statistic |
| FREE_BUFFER_INSPECTED | NUMBER | Free buffer inspected statistic |
| DIRTY_BUFFERS_INSPECTED | NUMBER | Dirty buffers inspected statistic |
| DB_BLOCK_CHANGE | NUMBER | Database blocks changed statistic |
| DB_BLOCK_GETS | NUMBER | Database blocks gotten statistic |
| CONSISTENT_GETS | NUMBER | Consistent gets statistic |
| PHYSICAL_READS | NUMBER | Physical reads statistic |
| PHYSICAL_WRITES | NUMBER | Physical writes statistic |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This view contains snapshots of V$BUFFER_POOL_STATISTICS . See Also: " V$BUFFER_POOL_STATISTICS " See Also: " V$BUFFER_POOL_STATISTICS "