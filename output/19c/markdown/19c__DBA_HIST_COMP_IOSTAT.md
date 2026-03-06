---
id: 19c__DBA_HIST_COMP_IOSTAT
name: DBA_HIST_COMP_IOSTAT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_HIST_COMP_IOSTAT.html
---

# DBA_HIST_COMP_IOSTAT

DBA_HIST_COMP_IOSTAT displays information about I/O statistics aggregated on the component level.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| COMPONENT | VARCHAR2(64) | Component name |
| FILE_TYPE | VARCHAR2(64) | File type |
| IO_TYPE | CHAR(5) | The type of I/O performed |
| OPERATION | CHAR(5) | Operation name |
| BYTES | NUMBER | Number of bytes |
| IO_COUNT | NUMBER | Number of I/Os that were performed |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |