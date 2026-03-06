---
id: 19c__ALL_SQLSET
name: ALL_SQLSET
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [all]
source_file: ALL_SQLSET.html
---

# ALL_SQLSET

ALL_SQLSET displays information about all SQL tuning sets accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| NAME | VARCHAR2(128) | Name of the SQL tuning set |
| ID | NUMBER | SQL tuning set identifier |
| CON_DBID | NUMBER | The database ID of the PDB |
| OWNER | VARCHAR2(128) | Owner of the SQL tuning set |
| DESCRIPTION | VARCHAR2(256) | Description of the SQL tuning set |
| CREATED | DATE | Date the SQL tuning set was created |
| LAST_MODIFIED | DATE | Date the SQL tuning set was last modified |
| STATEMENT_COUNT | NUMBER | Number of statements in the SQL tuning set |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_SQLSET displays information about all SQL tuning sets in the database. USER_SQLSET displays information about the SQL tuning sets owned by the current user. This view does not display the OWNER column. See Also: " DBA_SQLSET " " USER_SQLSET " See Also: " DBA_SQLSET " " USER_SQLSET "