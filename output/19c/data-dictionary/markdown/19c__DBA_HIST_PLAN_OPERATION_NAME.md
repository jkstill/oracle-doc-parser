---
id: 19c__DBA_HIST_PLAN_OPERATION_NAME
name: DBA_HIST_PLAN_OPERATION_NAME
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HIST_PLAN_OPERATION_NAME.html
---

# DBA_HIST_PLAN_OPERATION_NAME

DBA_HIST_PLAN_OPERATION_NAME displays historical information about SQL plan operation names.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DBID | NUMBER | Database identifier |
| OPERATION_ID | NUMBER | Plan operation identifier |
| OPERATION_NAME | VARCHAR2(64) | Plan operation name. This value also appears in the SQL_PLAN_OPERATION column of the DBA_HIST_ACTIVE_SESS_HISTORY view. |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content