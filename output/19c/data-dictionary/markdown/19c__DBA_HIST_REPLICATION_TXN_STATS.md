---
id: 19c__DBA_HIST_REPLICATION_TXN_STATS
name: DBA_HIST_REPLICATION_TXN_STATS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_HIST_REPLICATION_TXN_STATS.html
---

# DBA_HIST_REPLICATION_TXN_STATS

DBA_HIST_REPLICATION_TXN_STATS displays replication transaction statistics for Oracle GoldenGate and XStream sessions.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| OBJECT_NAME | VARCHAR2(128) | Object name |
| SESSION_TYPE | VARCHAR2(64) | Type of session |
| SESSION_MODULE | VARCHAR2(64) | Session module. Valid values: XStream GoldenGate |
| SOURCE_DATABASE | VARCHAR2(128) | Database where the transaction originated |
| SOURCE_TXN_ID | VARCHAR2(128) | Original transaction ID at the source database |
| FIRST_LCR_TIME | DATE | Time of the first LCR (message in an error transaction) |
| TOTAL_LCRS_COUNT | NUMBER | Total number of LCRs for this replication transaction |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content