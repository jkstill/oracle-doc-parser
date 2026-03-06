---
id: 19c__DBA_HIST_METRIC_NAME
name: DBA_HIST_METRIC_NAME
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HIST_METRIC_NAME.html
---

# DBA_HIST_METRIC_NAME

DBA_HIST_METRIC_NAME describes attributes of the set of RDBMS metrics.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DBID | NUMBER | Database ID |
| GROUP_ID | NUMBER | Metric Group ID |
| GROUP_NAME | VARCHAR2(64) | Metric group name |
| METRIC_ID | NUMBER | Metric ID |
| METRIC_NAME | VARCHAR2(64) | Metric name |
| METRIC_UNIT | VARCHAR2(64) | Unit of measurement |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

This view contains a snapshot of V$METRICNAME . See Also: " V$METRICNAME " See Also: " V$METRICNAME "