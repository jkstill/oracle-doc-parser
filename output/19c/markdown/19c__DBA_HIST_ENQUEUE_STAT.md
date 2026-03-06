---
id: 19c__DBA_HIST_ENQUEUE_STAT
name: DBA_HIST_ENQUEUE_STAT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_HIST_ENQUEUE_STAT.html
---

# DBA_HIST_ENQUEUE_STAT

DBA_HIST_ENQUEUE_STAT displays historical statistics on the number of enqueue (lock) requests for each type of lock.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| EQ_TYPE | VARCHAR2(2) | Type of enqueue requested |
| REQ_REASON | VARCHAR2(64) | Reason for the enqueue request |
| TOTAL_REQ# | NUMBER | Total number of enqueue requests or enqueue conversions for this type of enqueue |
| TOTAL_WAIT# | NUMBER | Total number of times an enqueue request or conversion resulted in a wait |
| SUCC_REQ# | NUMBER | Number of times an enqueue request or conversion was granted |
| FAILED_REQ# | NUMBER | Number of times an enqueue request or conversion failed |
| CUM_WAIT_TIME | NUMBER | Total amount of time (in milliseconds) spent waiting for the enqueue or enqueue conversion |
| EVENT# | NUMBER | Event number |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

This view contains snapshots of V$ENQUEUE_STATISTICS . See Also: " V$ENQUEUE_STATISTICS " See Also: " V$ENQUEUE_STATISTICS "