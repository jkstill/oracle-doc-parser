---
id: 19c__DBA_HIST_STREAMS_POOL_ADVICE
name: DBA_HIST_STREAMS_POOL_ADVICE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HIST_STREAMS_POOL_ADVICE.html
---

# DBA_HIST_STREAMS_POOL_ADVICE

DBA_HIST_STREAMS_POOL_ADVICE displays historical information about the estimated count of spilled or unspilled messages and the associated time spent in the spill or unspill activity for different Streams pool sizes.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID of the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number of the snapshot |
| SIZE_FOR_ESTIMATE | NUMBER | Pool size for the estimate (in megabytes) |
| SIZE_FACTOR | NUMBER | Size factor with respect to the current pool size |
| ESTD_SPILL_COUNT | NUMBER | Estimated count of messages spilled from the Streams pool |
| ESTD_SPILL_TIME | NUMBER | Estimated elapsed time (in seconds) to spill |
| ESTD_UNSPILL_COUNT | NUMBER | Estimated count of unspills (read back from disk) |
| ESTD_UNSPILL_TIME | NUMBER | Estimated elapsed time (in seconds) to unspill |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

This view is intended for use with Automatic Workload Repository (AWR).