---
id: 19c__DBA_HIST_PDB_IN_SNAP
name: DBA_HIST_PDB_IN_SNAP
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HIST_PDB_IN_SNAP.html
---

# DBA_HIST_PDB_IN_SNAP

DBA_HIST_PDB_IN_SNAP captures a list of open pluggable databases (PDBs) at the time of the Automatic Workload Repository (AWR) snapshot. This view can be used with other DBA_HIST_ views to construct the number of opened PDBs at the time of the snapshot.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | AWR snapshot ID |
| DBID | NUMBER | Database ID of the database that took this snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number of the instance that took this snapshot |
| CON_DBID | NUMBER | DBID of an open PDB at the time of the snapshot |
| FLAG | NUMBER | Flag field in capture properties of the PDB. Not used at this time. |
| CON_ID | NUMBER | The ID of the container to which the data pertains. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |
| OPEN_TIME_TZ | TIMESTAMP(3) WITH TIME ZONE | Time the PDB was last opened |