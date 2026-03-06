---
id: 19c__DBA_HIST_STAT_NAME
name: DBA_HIST_STAT_NAME
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_HIST_STAT_NAME.html
---

# DBA_HIST_STAT_NAME

DBA_HIST_STAT_NAME displays decoded statistic names for the statistics captured in the Workload Repository.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DBID | NUMBER | Database ID |
| STAT_ID | NUMBER | Statistic identifier |
| STAT_NAME | VARCHAR2(64) | Statistic name |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This includes OLAP statisitics and OLAP timed events. This view captures information from V$STATNAME and is used with DBA_HIST_SYSSTAT and DBA_HIST_SYS_TIME_MODEL . See Also: " V$STATNAME " " DBA_HIST_SYSSTAT " " DBA_HIST_SYS_TIME_MODEL " See Also: " V$STATNAME " " DBA_HIST_SYSSTAT " " DBA_HIST_SYS_TIME_MODEL "