---
id: 19c__DBA_HIST_TEMPFILE
name: DBA_HIST_TEMPFILE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HIST_TEMPFILE.html
---

# DBA_HIST_TEMPFILE

DBA_HIST_TEMPFILE displays a history of the temp file information from the control file. This view contains snapshots of V$TEMPFILE .

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DBID | NUMBER | Database ID |
| FILE# | NUMBER | File identification number |
| CREATION_CHANGE# | NUMBER | Change number at which the temp file was created |
| FILENAME | VARCHAR2(513) | Name of the temp file |
| TS# | NUMBER | Tablespace number |
| TSNAME | VARCHAR2(30) | Name of the tablespace |
| BLOCK_SIZE | NUMBER | Block size of the temp file |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: " V$TEMPFILE " See Also: " V$TEMPFILE "