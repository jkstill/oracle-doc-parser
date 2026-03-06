---
id: 19c__DBA_HIST_DATAFILE
name: DBA_HIST_DATAFILE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HIST_DATAFILE.html
---

# DBA_HIST_DATAFILE

DBA_HIST_DATAFILE displays a history of the data file information from the control file.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DBID | NUMBER | Database ID |
| FILE# | NUMBER | File identification number |
| CREATION_CHANGE# | NUMBER | Change number at which the data file was created |
| FILENAME | VARCHAR2(513) | Name of the data file |
| TS# | NUMBER | Tablespace number |
| TSNAME | VARCHAR2(30) | Name of the tablespace |
| BLOCK_SIZE | NUMBER | Block size of the data file |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

This view contains snapshots of V$DATAFILE . See Also: " V$DATAFILE " See Also: " V$DATAFILE "