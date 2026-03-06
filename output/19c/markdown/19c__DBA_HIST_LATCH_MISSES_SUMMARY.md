---
id: 19c__DBA_HIST_LATCH_MISSES_SUMMARY
name: DBA_HIST_LATCH_MISSES_SUMMARY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HIST_LATCH_MISSES_SUMMARY.html
---

# DBA_HIST_LATCH_MISSES_SUMMARY

DBA_HIST_LATCH_MISSES_SUMMARY displays historical summary statistics about missed attempts to acquire a latch.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| PARENT_NAME | VARCHAR2(50) | Latch name of a parent latch |
| WHERE_IN_CODE | VARCHAR2(64) | Location that attempted to acquire the latch |
| NWFAIL_COUNT | NUMBER | Number of times that no-wait acquisition of the latch failed |
| SLEEP_COUNT | NUMBER | Number of times that acquisition attempts caused sleeps |
| WTR_SLP_COUNT | NUMBER | Number of times a waiter slept |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

This view contains snapshots of V$LATCH_MISSES . See Also: " V$LATCH_MISSES " See Also: " V$LATCH_MISSES "