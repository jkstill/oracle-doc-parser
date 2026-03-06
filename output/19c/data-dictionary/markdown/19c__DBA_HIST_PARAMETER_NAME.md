---
id: 19c__DBA_HIST_PARAMETER_NAME
name: DBA_HIST_PARAMETER_NAME
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: configuration
tags: [dba]
source_file: DBA_HIST_PARAMETER_NAME.html
---

# DBA_HIST_PARAMETER_NAME

DBA_HIST_PARAMETER_NAME displays information about the parameter names captured in the workload repository.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DBID | NUMBER | Database ID |
| PARAMETER_HASH | NUMBER | Parameter hash |
| PARAMETER_NAME | VARCHAR2(64) | Name of the parameter |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This view is used with the DBA_HIST_PARAMETER view. See Also: " DBA_HIST_PARAMETER " See Also: " DBA_HIST_PARAMETER "