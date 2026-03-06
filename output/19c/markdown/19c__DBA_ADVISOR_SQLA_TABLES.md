---
id: 19c__DBA_ADVISOR_SQLA_TABLES
name: DBA_ADVISOR_SQLA_TABLES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [dba]
source_file: DBA_ADVISOR_SQLA_TABLES.html
---

# DBA_ADVISOR_SQLA_TABLES

DBA_ADVISOR_SQLA_TABLES displays cross references between the workload statements and the tables referenced in the statement.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the workload object |
| TASK_ID | NUMBER | Unique identifier of the task |
| TASK_NAME | VARCHAR2(128) | Name of the task |
| SQL_ID | VARCHAR2(13) | SQL identifier of the parent cursor in the library cache |
| STMT_ID | NUMBER | Statement ID |
| TABLE_OWNER | VARCHAR2(128) | Owner of the table |
| TABLE_NAME | VARCHAR2(128) | Table name |

## Usage Notes

Related View USER_ADVISOR_SQLA_TABLES displays cross references between the workload statements and the tables referenced in the statement for the current user. This view does not display the OWNER column. See Also: " USER_ADVISOR_SQLA_TABLES " See Also: " USER_ADVISOR_SQLA_TABLES "