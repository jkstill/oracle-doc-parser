---
id: 19c__DBA_MVREF_STMT_STATS
name: DBA_MVREF_STMT_STATS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_MVREF_STMT_STATS.html
---

# DBA_MVREF_STMT_STATS

DBA_MVREF_STMT_STATS shows information associated with each refresh statement of a materialized view in a refresh run.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| MV_OWNER | VARCHAR2(128) | Owner of the materialized view |
| MV_NAME | VARCHAR2(128) | Name of the materialized view |
| REFRESH_ID | NUMBER | The refresh ID of the refresh run |
| STEP | NUMBER | A number indicating the step in the refresh process in which the statement is executed for the materialized view. Steps are numbered consecutively starting at 1. |
| SQLID | VARCHAR2(14) | The SQL ID of the statement |
| STMT | CLOB | The text of the SQL statement |
| EXECUTION_TIME | NUMBER | The time it took to execute the statement (in seconds) |
| EXECUTION_PLAN | XMLTYPE STORAGE BINARY | For internal use only |

## Usage Notes

Related View USER_MVREF_STMT_STATS shows information associated with each refresh statement of a materialized view accessible to the current user in a refresh run. See Also: " USER_MVREF_STMT_STATS " See Also: " USER_MVREF_STMT_STATS "