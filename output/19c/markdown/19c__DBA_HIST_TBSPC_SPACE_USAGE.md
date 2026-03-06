---
id: 19c__DBA_HIST_TBSPC_SPACE_USAGE
name: DBA_HIST_TBSPC_SPACE_USAGE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HIST_TBSPC_SPACE_USAGE.html
---

# DBA_HIST_TBSPC_SPACE_USAGE

DBA_HIST_TBSPC_SPACE_USAGE displays historical tablespace usage statistics.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| TABLESPACE_ID | NUMBER | Tablespace ID |
| TABLESPACE_SIZE | NUMBER | Tablespace size (in database blocks) |
| TABLESPACE_MAXSIZE | NUMBER | Maximum size of the tablespace (in database blocks) |
| TABLESPACE_USEDSIZE | NUMBER | Used size of the tablespace (in database blocks) |
| RTIME | VARCHAR2(25) | Runtime |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |