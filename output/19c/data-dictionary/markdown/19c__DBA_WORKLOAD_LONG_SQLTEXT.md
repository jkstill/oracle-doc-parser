---
id: 19c__DBA_WORKLOAD_LONG_SQLTEXT
name: DBA_WORKLOAD_LONG_SQLTEXT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dba]
source_file: DBA_WORKLOAD_LONG_SQLTEXT.html
---

# DBA_WORKLOAD_LONG_SQLTEXT

DBA_WORKLOAD_LONG_SQLTEXT displays the captured SQL statements that are longer than 1000 characters. You can load SQL statements longer than 1000 characters to the DBA_WORKLOAD_LONG_SQLTEXT view using the DBMS_WORKLOAD_REPLAY.LOAD_LONG_SQLTEXT procedure.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CAPTURE_ID | NUMBER(38) | Internal key for the workload capture |
| SQL_ID | VARCHAR2(13) | SQL identifier of the parent cursor in the library cache |
| SQL_FULLTEXT | CLOB | Full text for the SQL statement exposed as a CLOB column |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: " DBA_WORKLOAD_CAPTURE_SQLTEXT " Oracle Database PL/SQL Packages and Types Reference for information about the DBMS_WORKLOAD_REPLAY package See Also: " DBA_WORKLOAD_CAPTURE_SQLTEXT " Oracle Database PL/SQL Packages and Types Reference for information about the DBMS_WORKLOAD_REPLAY package