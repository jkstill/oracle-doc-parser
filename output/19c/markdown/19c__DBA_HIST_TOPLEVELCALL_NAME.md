---
id: 19c__DBA_HIST_TOPLEVELCALL_NAME
name: DBA_HIST_TOPLEVELCALL_NAME
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HIST_TOPLEVELCALL_NAME.html
---

# DBA_HIST_TOPLEVELCALL_NAME

DBA_HIST_TOPLEVELCALL_NAME displays the mapping between Oracle top level calls and names.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DBID | NUMBER | Database ID |
| TOP_LEVEL_CALL# | NUMBER | Oracle top level call number |
| TOP_LEVEL_CALL_NAME | VARCHAR2(64) | Oracle top level call name |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |