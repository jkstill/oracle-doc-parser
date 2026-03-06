---
id: 19c__DBA_HIST_SQLTEXT
name: DBA_HIST_SQLTEXT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dba]
source_file: DBA_HIST_SQLTEXT.html
---

# DBA_HIST_SQLTEXT

DBA_HIST_SQLTEXT displays the text of SQL statements belonging to shared SQL cursors captured in the Workload Repository.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DBID | NUMBER | Database ID |
| SQL_ID | VARCHAR2(13) | SQL identifier of the parent cursor in the library cache |
| SQL_TEXT | CLOB | Full text for the SQL statement exposed as a CLOB column |
| COMMAND_TYPE | NUMBER | Oracle command type definition |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

This view captures information from V$SQL and is used with the DBA_HIST_SQLSTAT view. See Also: " V$SQL " " DBA_HIST_SQLSTAT " See Also: " V$SQL " " DBA_HIST_SQLSTAT "