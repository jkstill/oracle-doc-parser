---
id: 19c__DBA_HIST_IOSTAT_FILETYPE_NAME
name: DBA_HIST_IOSTAT_FILETYPE_NAME
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_HIST_IOSTAT_FILETYPE_NAME.html
---

# DBA_HIST_IOSTAT_FILETYPE_NAME

DBA_HIST_IOSTAT_FILETYPE_NAME displays historical I/O statistics for file type names.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DBID | NUMBER | Database ID for the snapshot |
| FILETYPE_ID | NUMBER | Type of file (for example, log file, data file, and so on) |
| FILETYPE_NAME | VARCHAR2(30) | Name of the file, in the case of a data file or temp file. For all other files, a corresponding string to be displayed (for example, ARCHIVELOG ). |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This view contains snapshots of V$IOSTAT_FILE . See Also: " V$IOSTAT_FILE " See Also: " V$IOSTAT_FILE "