---
id: 19c__DBA_HIST_MUTEX_SLEEP
name: DBA_HIST_MUTEX_SLEEP
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HIST_MUTEX_SLEEP.html
---

# DBA_HIST_MUTEX_SLEEP

DBA_HIST_MUTEX_SLEEP displays mutex sleep summary historical statistics information.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database identifier for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| MUTEX_TYPE | VARCHAR2(32) | Mutex type |
| LOCATION | VARCHAR2(40) | The code location where the waiter slept for the mutex |
| SLEEPS | NUMBER | Number of sleeps for this MUTEX_TYPE and LOCATION |
| WAIT_TIME | NUMBER | Wait time in microseconds |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content