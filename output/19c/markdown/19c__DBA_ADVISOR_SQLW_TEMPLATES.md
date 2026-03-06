---
id: 19c__DBA_ADVISOR_SQLW_TEMPLATES
name: DBA_ADVISOR_SQLW_TEMPLATES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dba]
source_file: DBA_ADVISOR_SQLW_TEMPLATES.html
---

# DBA_ADVISOR_SQLW_TEMPLATES

DBA_ADVISOR_SQLW_TEMPLATES displays an aggregated picture of all SQLWkld template objects in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the workload object |
| WORKLOAD_ID | NUMBER | Unique identifier number of the workload object |
| WORKLOAD_NAME | VARCHAR2(128) | Unique name of the workload |
| DESCRIPTION | VARCHAR2(256) | User-specified description of the workload |
| CREATE_DATE | DATE | Date on which the workload object was created |
| MODIFY_DATE | DATE | Date of last update to the current workload |
| SOURCE | VARCHAR2(128) | Optional object or template on which the object was based |
| READ_ONLY | VARCHAR2(5) | Indicates whether the workload template can be modified or deleted ( TRUE ) or not ( FALSE ) |

## Usage Notes

Related View USER_ADVISOR_SQLW_TEMPLATES displays an aggregated picture of the SQLWkld template objects owned by the current user. This view does not display the OWNER column. See Also: " USER_ADVISOR_SQLW_TEMPLATES " See Also: " USER_ADVISOR_SQLW_TEMPLATES "