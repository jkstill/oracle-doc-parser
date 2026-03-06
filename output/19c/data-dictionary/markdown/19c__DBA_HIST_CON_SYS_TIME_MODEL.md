---
id: 19c__DBA_HIST_CON_SYS_TIME_MODEL
name: DBA_HIST_CON_SYS_TIME_MODEL
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: internal
tags: [dba]
source_file: DBA_HIST_CON_SYS_TIME_MODEL.html
---

# DBA_HIST_CON_SYS_TIME_MODEL

DBA_HIST_CON_SYS_TIME_MODEL displays historical system time model statistics, including OLAP timed stastistics. This view contains snapshots of V$SYS_TIME_MODEL .

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
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: When queried from a non-CDB, the statistics for that instance are returned, and the CON_ID value is 0 . When queried from the root of a CDB, the statistics in every container are returned, and the CON_ID value indicates the container to which the statistics belong. When queried from a PDB, statistics from that PDB are returned, and the CON_ID value is the container ID for that PDB. |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: " V$CON_SYSMETRIC " " DBA_HIST_SYS_TIME_MODEL " " V$SYS_TIME_MODEL " See Also: " V$CON_SYSMETRIC " " DBA_HIST_SYS_TIME_MODEL " " V$SYS_TIME_MODEL "