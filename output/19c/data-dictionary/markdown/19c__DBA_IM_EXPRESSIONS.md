---
id: 19c__DBA_IM_EXPRESSIONS
name: DBA_IM_EXPRESSIONS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_IM_EXPRESSIONS.html
---

# DBA_IM_EXPRESSIONS

DBA_IM_EXPRESSIONS provides information about the list of expressions (SYS_IME virtual columns) that are currently enabled for in-memory storage.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(129) | Table owner |
| TABLE_NAME | VARCHAR2(129) | Table name |
| OBJECT_NUMBER | NUMBER | Object number of the table |
| COLUMN_NAME | VARCHAR2(128) | Column name of the expression added to the table (with SYS_IME prefix) |
| SQL_EXPRESSION | LONG | SQL representation of the expression |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View Typically, you can query this view after invoking the DBMS_INMEMORY_ADMIN.IME_CAPTURE_EXPRESSIONS PL/SQL procedure to see the list of hot expressions added to different tables across the database. Based on this view, you can: Populate expressions on a particular table immediately Drop certain expressions that are marked for in-memory but not desired by users USER_IM_EXPRESSIONS provides information about the list of expressions (SYS_IME virtual columns) that are currently enabled for in-memory storage in schemas owned by the current user. This view does not display the OWNER column. See Also: " USER_IM_EXPRESSIONS " See Also: " USER_IM_EXPRESSIONS "