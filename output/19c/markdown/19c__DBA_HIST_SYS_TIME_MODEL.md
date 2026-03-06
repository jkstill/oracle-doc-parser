---
id: 19c__DBA_HIST_SYS_TIME_MODEL
name: DBA_HIST_SYS_TIME_MODEL
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: internal
tags: [dba]
source_file: DBA_HIST_SYS_TIME_MODEL.html
---

# DBA_HIST_SYS_TIME_MODEL

DBA_HIST_SYS_TIME_MODEL displays historical system time model statistics, including OLAP timed stastistics.

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

This view contains snapshots of V$SYS_TIME_MODEL . See Also: " V$SYS_TIME_MODEL " " DBA_HIST_CON_SYS_TIME_MODEL " " V$CON_SYSMETRIC " See Also: " V$SYS_TIME_MODEL " " DBA_HIST_CON_SYS_TIME_MODEL " " V$CON_SYSMETRIC "