---
id: 19c__DBA_HIST_OPTIMIZER_ENV
name: DBA_HIST_OPTIMIZER_ENV
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HIST_OPTIMIZER_ENV.html
---

# DBA_HIST_OPTIMIZER_ENV

DBA_HIST_OPTIMIZER_ENV displays the optimizer environments that have been captured in the Workload Repository.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DBID | NUMBER | Database ID |
| OPTIMIZER_ENV_HASH_VALUE | NUMBER | Hash value for the optimizer environment |
| OPTIMIZER_ENV | RAW(2000) | Optimizer environment |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

This view is used with the DBA_HIST_SQLSTAT view. See Also: " DBA_HIST_SQLSTAT " See Also: " DBA_HIST_SQLSTAT "