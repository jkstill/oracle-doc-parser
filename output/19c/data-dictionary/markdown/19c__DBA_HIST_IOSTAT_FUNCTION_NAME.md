---
id: 19c__DBA_HIST_IOSTAT_FUNCTION_NAME
name: DBA_HIST_IOSTAT_FUNCTION_NAME
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_HIST_IOSTAT_FUNCTION_NAME.html
---

# DBA_HIST_IOSTAT_FUNCTION_NAME

DBA_HIST_IOSTAT_FUNCTION_NAME displays historical I/O statistics by function names.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DBID | NUMBER | Database ID for the snapshot |
| FUNCTION_ID | NUMBER | Function ID |
| FUNCTION_NAME | VARCHAR2(128) | Function name |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This view contains snapshots of V$IOSTAT_FUNCTION . See Also: " V$IOSTAT_FUNCTION " See Also: " V$IOSTAT_FUNCTION "