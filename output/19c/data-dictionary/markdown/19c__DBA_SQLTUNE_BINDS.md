---
id: 19c__DBA_SQLTUNE_BINDS
name: DBA_SQLTUNE_BINDS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dba]
source_file: DBA_SQLTUNE_BINDS.html
---

# DBA_SQLTUNE_BINDS

DBA_SQLTUNE_BINDS displays the bind values associated with all tuned SQL statements in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TASK_ID | NUMBER(38) | Tuning task identifier |
| OBJECT_ID | NUMBER(38) | Advisor framework object identifier |
| POSITION | NUMBER(38) | Bind position |
| VALUE | ANYDATA | Bind value. This column is NULL for PL/SQL bind types. |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View USER_SQLTUNE_BINDS displays the bind values associated with the tuned SQL statements owned by the current user. See Also: " USER_SQLTUNE_BINDS " See Also: " USER_SQLTUNE_BINDS "