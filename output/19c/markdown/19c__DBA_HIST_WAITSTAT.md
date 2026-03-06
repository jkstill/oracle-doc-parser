---
id: 19c__DBA_HIST_WAITSTAT
name: DBA_HIST_WAITSTAT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_HIST_WAITSTAT.html
---

# DBA_HIST_WAITSTAT

DBA_HIST_WAITSTAT displays historical block contention statistics. This view contains snapshots of V$WAITSTAT .

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| CLASS | VARCHAR2(18) | Class of the block |
| WAIT_COUNT | NUMBER | Number of waits by the OPERATION for this CLASS of block |
| TIME | NUMBER | Sum of all wait times for all the waits by the OPERATION for this CLASS of block |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

See Also: " V$WAITSTAT " See Also: " V$WAITSTAT "