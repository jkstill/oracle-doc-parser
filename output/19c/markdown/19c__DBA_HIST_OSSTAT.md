---
id: 19c__DBA_HIST_OSSTAT
name: DBA_HIST_OSSTAT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_HIST_OSSTAT.html
---

# DBA_HIST_OSSTAT

DBA_HIST_OSSTAT displays historical operating system statistics.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| STAT_ID | NUMBER | Statistic ID |
| STAT_NAME | VARCHAR2(64) | Statistic name |
| VALUE | NUMBER | Statistic value |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

This view contains snapshots of V$OSSTAT . See Also: " V$OSSTAT " See Also: " V$OSSTAT "