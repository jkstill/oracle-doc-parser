---
id: 19c__DBA_HIST_THREAD
name: DBA_HIST_THREAD
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HIST_THREAD.html
---

# DBA_HIST_THREAD

DBA_HIST_THREAD displays historical thread information from the control file.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| THREAD# | NUMBER | Thread number |
| THREAD_INSTANCE_NUMBER | NUMBER | Instance number of the thread |
| STATUS | VARCHAR2(6) | Thread status ( OPEN ) or ( CLOSED ) |
| OPEN_TIME | DATE | Last time the thread was opened |
| CURRENT_GROUP# | NUMBER | Current log group |
| SEQUENCE# | NUMBER | Sequence number of the current log |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content