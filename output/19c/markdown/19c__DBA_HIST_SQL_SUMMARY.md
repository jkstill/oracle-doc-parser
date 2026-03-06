---
id: 19c__DBA_HIST_SQL_SUMMARY
name: DBA_HIST_SQL_SUMMARY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dba]
source_file: DBA_HIST_SQL_SUMMARY.html
---

# DBA_HIST_SQL_SUMMARY

DBA_HIST_SQL_SUMMARY displays historical SQL summary information.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| TOTAL_SQL | NUMBER | Total number of SQLs |
| TOTAL_SQL_MEM | NUMBER | Total sharable memory in bytes for SQLs |
| SINGLE_USE_SQL | NUMBER | Total number of single execution SQLs |
| SINGLE_USE_SQL_MEM | NUMBER | Total sharable memory in bytes for single execution SQLs |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |