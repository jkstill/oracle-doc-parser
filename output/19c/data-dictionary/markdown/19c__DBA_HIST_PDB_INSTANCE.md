---
id: 19c__DBA_HIST_PDB_INSTANCE
name: DBA_HIST_PDB_INSTANCE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HIST_PDB_INSTANCE.html
---

# DBA_HIST_PDB_INSTANCE

DBA_HIST_PDB_INSTANCE displays the pluggable databases (PDBs) and instances in the Workload Repository.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DBID | NUMBER | Database ID |
| INSTANCE_NUMBER | NUMBER | Instance number |
| STARTUP_TIME | TIMESTAMP(3) | Startup time of the instance |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| OPEN_TIME | TIMESTAMP(3) | Time the PDB was last opened |
| OPEN_MODE | VARCHAR2(16) | Open mode of the database |
| PDB_NAME | VARCHAR2(128) | PDB name |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |
| SNAP_ID | NUMBER | The unique snapshot identifier of the snapshot that flushed the corresponding row |
| STARTUP_TIME_TZ | TIMESTAMP(3) WITH TIME ZONE | Startup time of the instance |
| OPEN_TIME_TZ | TIMESTAMP(3) WITH TIME ZONE | Time the PDB was last opened |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content