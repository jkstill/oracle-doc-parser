---
id: 19c__DBA_HIST_SGA
name: DBA_HIST_SGA
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HIST_SGA.html
---

# DBA_HIST_SGA

DBA_HIST_SGA displays historical summary information about the system global area (SGA).

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| NAME | VARCHAR2(64) | SGA component group |
| VALUE | NUMBER | Memory size (in bytes) |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This view contains snapshots of V$SGA . See Also: " V$SGA " See Also: " V$SGA "