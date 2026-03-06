---
id: 19c__DBA_HIST_FILESTATXS
name: DBA_HIST_FILESTATXS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_HIST_FILESTATXS.html
---

# DBA_HIST_FILESTATXS

DBA_HIST_FILESTATXS displays information about file read/write statistics.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| FILE# | NUMBER | File identification number |
| CREATION_CHANGE# | NUMBER | Change number at which the data file was created |
| FILENAME | VARCHAR2(513) | Name of the data file |
| TS# | NUMBER | Tablespace number |
| TSNAME | VARCHAR2(30) | Name of the tablespace |
| BLOCK_SIZE | NUMBER | Block size of the data file |
| PHYRDS | NUMBER | Number of physical reads done |
| PHYWRTS | NUMBER | Number of times DBWR is required to write |
| SINGLEBLKRDS | NUMBER | Number of single block reads |
| READTIM | NUMBER | Time (in hundredths of a second) spent doing reads if the TIMED_STATISTICS parameter is true ; 0 if TIMED_STATISTICS is false |
| WRITETIM | NUMBER | Time (in hundredths of a second) spent doing writes if the TIMED_STATISTICS parameter is true ; 0 if TIMED_STATISTICS is false |
| SINGLEBLKRDTIM | NUMBER | Cumulative single block read time (in hundredths of a second) |
| PHYBLKRD | NUMBER | Number of physical blocks read |
| PHYBLKWRT | NUMBER | Number of blocks written to disk, which may be the same as PHYWRTS if all writes are single blocks |
| WAIT_COUNT | NUMBER | Shows the number of waits at the file level for contended buffers. This value includes the individual wait events that are included in the buffer busy waits wait event. See Also: " buffer busy waits " |
| TIME | NUMBER | Time spent waiting for the wait events in the WAIT_COUNT column |
| OPTIMIZED_PHYBLKRD | NUMBER | Number of physical reads from Database Smart Flash Cache blocks |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This view contains snapshots of V$FILESTAT . See Also: " V$FILESTAT " See Also: " V$FILESTAT "