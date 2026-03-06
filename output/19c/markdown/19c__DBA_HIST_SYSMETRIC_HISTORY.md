---
id: 19c__DBA_HIST_SYSMETRIC_HISTORY
name: DBA_HIST_SYSMETRIC_HISTORY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: internal
tags: [dba]
source_file: DBA_HIST_SYSMETRIC_HISTORY.html
---

# DBA_HIST_SYSMETRIC_HISTORY

DBA_HIST_SYSMETRIC_HISTORY externalizes all available history of the system metric values for the entire set of data kept in the database.

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
| VALUE | NUMBER | Metric Value |
| METRIC_UNIT | VARCHAR2(64) | Unit of measurement |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

This view contains snapshots of V$SYSMETRIC_HISTORY . See Also: " V$SYSMETRIC_HISTORY " " DBA_HIST_CON_SYSMETRIC_HIST " " V$CON_SYSMETRIC_HISTORY " See Also: " V$SYSMETRIC_HISTORY " " DBA_HIST_CON_SYSMETRIC_HIST " " V$CON_SYSMETRIC_HISTORY "