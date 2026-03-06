---
id: 19c__DBA_HIST_SESSMETRIC_HISTORY
name: DBA_HIST_SESSMETRIC_HISTORY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HIST_SESSMETRIC_HISTORY.html
---

# DBA_HIST_SESSMETRIC_HISTORY

DBA_HIST_SESSMETRIC_HISTORY displays the history of several important session metrics.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| BEGIN_TIME | DATE | Begin time of the interval |
| END_TIME | DATE | End time of the interval |
| SESSID | NUMBER | Session ID |
| SERIAL# | NUMBER | Session serial number |
| INTSIZE | NUMBER | Interval size (in hundredths of a second) |
| GROUP_ID | NUMBER | Group ID |
| METRIC_ID | NUMBER | Metric ID |
| METRIC_NAME | VARCHAR2(64) | Metric name |
| VALUE | NUMBER | Metric Value |
| METRIC_UNIT | VARCHAR2(64) | Unit of measurement |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Note: This view is populated only if a session metric exceeds a server metric threshold that was configured using the DBMS_SERVER_ALERT package. Note: This view is populated only if a session metric exceeds a server metric threshold that was configured using the DBMS_SERVER_ALERT package. See Also: The DBMS_SERVER_ALERT package in Oracle Database PL/SQL Packages and Types Reference See Also: The DBMS_SERVER_ALERT package in Oracle Database PL/SQL Packages and Types Reference