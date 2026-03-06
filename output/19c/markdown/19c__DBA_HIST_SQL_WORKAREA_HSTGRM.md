---
id: 19c__DBA_HIST_SQL_WORKAREA_HSTGRM
name: DBA_HIST_SQL_WORKAREA_HSTGRM
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dba]
source_file: DBA_HIST_SQL_WORKAREA_HSTGRM.html
---

# DBA_HIST_SQL_WORKAREA_HSTGRM

DBA_HIST_SQL_WORKAREA_HSTGRM displays the historical cumulative work area execution statistics (cumulated since instance startup) for different work area groups.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| LOW_OPTIMAL_SIZE | NUMBER | Lower bound for the optimal memory requirement of work areas included in the row (in bytes) |
| HIGH_OPTIMAL_SIZE | NUMBER | Upper bound for the optimal memory requirement of work areas included in the row (in bytes) |
| OPTIMAL_EXECUTIONS | NUMBER | Number of work areas with an optimal memory requirement comprised between LOW_OPTIMAL_SIZE and HIGH_OPTIMAL_SIZE which have been executed in optimal mode since instance startup |
| ONEPASS_EXECUTIONS | NUMBER | Number of work areas with an optimal memory requirement comprised between LOW_OPTIMAL_SIZE and HIGH_OPTIMAL_SIZE which have been executed in one-pass mode since instance startup |
| MULTIPASSES_EXECUTIONS | NUMBER | Number of work areas with an optimal memory requirement comprised between LOW_OPTIMAL_SIZE and HIGH_OPTIMAL_SIZE which have been executed in multi-pass mode since instance startup |
| TOTAL_EXECUTIONS | NUMBER | Sum of OPTIMAL_EXECUTIONS , ONEPASS_EXECUTIONS , and MULTIPASSES_EXECUTIONS |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

This view contains snapshots of V$SQL_WORKAREA_HISTOGRAM . See Also: " V$SQL_WORKAREA_HISTOGRAM " See Also: " V$SQL_WORKAREA_HISTOGRAM "