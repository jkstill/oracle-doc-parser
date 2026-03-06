---
id: 19c__DBA_ADVISOR_SQLW_TABLES
name: DBA_ADVISOR_SQLW_TABLES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [dba]
source_file: DBA_ADVISOR_SQLW_TABLES.html
---

# DBA_ADVISOR_SQLW_TABLES

DBA_ADVISOR_SQLW_TABLES displays cross references between the workload statements and the tables referenced in the statement.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the workload object |
| WORKLOAD_ID | NUMBER | Unique identifier number of the workload object |
| WORKLOAD_NAME | VARCHAR2(128) | Name of the workload |
| SQL_ID | NUMBER | Identifier of the statement |
| TABLE_OWNER | VARCHAR2(128) | Owner of the table |
| TABLE_NAME | VARCHAR2(128) | Name of the table |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View USER_ADVISOR_SQLW_TABLES displays cross references between the workload statements and the tables referenced in the statement. This view does not display the OWNER column. See Also: " USER_ADVISOR_SQLW_TABLES " See Also: " USER_ADVISOR_SQLW_TABLES "