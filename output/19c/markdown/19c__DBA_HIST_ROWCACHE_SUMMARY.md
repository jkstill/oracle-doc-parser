---
id: 19c__DBA_HIST_ROWCACHE_SUMMARY
name: DBA_HIST_ROWCACHE_SUMMARY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HIST_ROWCACHE_SUMMARY.html
---

# DBA_HIST_ROWCACHE_SUMMARY

DBA_HIST_ROWCACHE_SUMMARY displays historical summary statistics for data dictionary activity.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| PARAMETER | VARCHAR2(32) | Name of the initialization parameter that determines the number of entries in the data dictionary cache |
| TOTAL_USAGE | NUMBER | Sum of the total number of entries in the cache |
| USAGE | NUMBER | Number of cache entries that contain valid data |
| GETS | NUMBER | Total number of requests for information on the data object |
| GETMISSES | NUMBER | Number of data requests resulting in cache misses |
| SCANS | NUMBER | Number of scan requests |
| SCANMISSES | NUMBER | Number of times a scan failed to find the data in the cache |
| SCANCOMPLETES | NUMBER | For a list of subordinate entries, the number of times the list was scanned completely |
| MODIFICATIONS | NUMBER | Number of inserts, updates, and deletions |
| FLUSHES | NUMBER | Number of times flushed to disk |
| DLM_REQUESTS | NUMBER | Number of DLM requests |
| DLM_CONFLICTS | NUMBER | Number of DLM conflicts |
| DLM_RELEASES | NUMBER | Number of DLM releases |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

This view contains snapshots of V$ROWCACHE . See Also: " V$ROWCACHE " See Also: " V$ROWCACHE "