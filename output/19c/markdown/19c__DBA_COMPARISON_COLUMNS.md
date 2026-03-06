---
id: 19c__DBA_COMPARISON_COLUMNS
name: DBA_COMPARISON_COLUMNS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [dba]
source_file: DBA_COMPARISON_COLUMNS.html
---

# DBA_COMPARISON_COLUMNS

DBA_COMPARISON_COLUMNS displays information about the columns for all comparison objects in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the comparison |
| COMPARISON_NAME | VARCHAR2(128) | Name of the comparison |
| COLUMN_POSITION | NUMBER | Position of the column |
| COLUMN_NAME | VARCHAR2(128) | Name of the column |
| INDEX_COLUMN | VARCHAR2(1) | Indicates whether the column is an index column ( Y ) or not ( N ) |

## Usage Notes

Related View USER_COMPARISON_COLUMNS displays information about the columns for the comparison objects owned by the current user. This view does not display the OWNER column. See Also: " USER_COMPARISON_COLUMNS " See Also: " USER_COMPARISON_COLUMNS "