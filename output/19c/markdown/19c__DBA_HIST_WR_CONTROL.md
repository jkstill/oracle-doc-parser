---
id: 19c__DBA_HIST_WR_CONTROL
name: DBA_HIST_WR_CONTROL
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HIST_WR_CONTROL.html
---

# DBA_HIST_WR_CONTROL

DBA_HIST_WR_CONTROL displays the control information for the Workload Repository.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DBID | NUMBER | Database ID |
| SNAP_INTERVAL | INTERVAL DAY(5) TO SECOND(1) | Snapshot interval; how often to automatically take snapshots |
| RETENTION | INTERVAL DAY(5) TO SECOND(1) | Retention setting for the snapshots; amount of time to keep the snapshots |
| TOPNSQL | VARCHAR2(10) | The number of Top SQL flushed for each SQL criteria (elapsed time, CPU time, parse calls, sharable memory, version count) |
| CON_ID | NUMBER | The ID of the container to which the data pertains. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |
| SRC_DBID | NUMBER | Database ID of the non-CDB, CDB, or PDB where the AWR snapshot data was collected |
| SRC_DBNAME | VARCHAR2(128) | Database name of the non-CDB, CDB, or PDB where the AWR snapshot data was collected |