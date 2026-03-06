---
id: 19c__DBA_HIST_SYSSTAT
name: DBA_HIST_SYSSTAT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_HIST_SYSSTAT.html
---

# DBA_HIST_SYSSTAT

DBA_HIST_SYSSTAT displays historical system statistics information, including OLAP kernel statistics.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| STAT_ID | NUMBER | Statistic identifier |
| STAT_NAME | VARCHAR2(64) | Statistic name |
| VALUE | NUMBER | Statistic value |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This view contains snapshots of V$SYSSTAT . See Also: " V$SYSSTAT " See Also: " V$SYSSTAT "