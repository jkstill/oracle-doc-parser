---
id: 19c__DBA_HIST_SYSMETRIC_SUMMARY
name: DBA_HIST_SYSMETRIC_SUMMARY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: internal
tags: [dba]
source_file: DBA_HIST_SYSMETRIC_SUMMARY.html
---

# DBA_HIST_SYSMETRIC_SUMMARY

DBA_HIST_SYSMETRIC_SUMMARY displays a history of statistical summary of all metric values in the System Metrics Long Duration group.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| BEGIN_TIME | DATE | Begin time of the interval |
| END_TIME | DATE | End time of the interval |
| INTSIZE | NUMBER | Interval size (in hundredths of a second) |
| GROUP_ID | NUMBER | Group ID |
| METRIC_ID | NUMBER | Metric ID |
| METRIC_NAME | VARCHAR2(64) | Metric name |
| METRIC_UNIT | VARCHAR2(64) | Unit of measurement |
| NUM_INTERVAL | NUMBER | Number of intervals observed |
| MINVAL | NUMBER | Minimum value observed |
| MAXVAL | NUMBER | Maximum value observed |
| AVERAGE | NUMBER | Average over the period |
| STANDARD_DEVIATION | NUMBER | One standard deviation |
| SUM_SQUARES | NUMBER | Sum of the squared deviations from the mean |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This view contains snapshots of V$SYSMETRIC_SUMMARY . See Also: " V$SYSMETRIC_SUMMARY " " DBA_HIST_CON_SYSMETRIC_SUMM " " V$CON_SYSMETRIC_SUMMARY " See Also: " V$SYSMETRIC_SUMMARY " " DBA_HIST_CON_SYSMETRIC_SUMM " " V$CON_SYSMETRIC_SUMMARY "