---
id: 19c__DBA_ADVISOR_SQLA_WK_MAP
name: DBA_ADVISOR_SQLA_WK_MAP
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dba]
source_file: DBA_ADVISOR_SQLA_WK_MAP.html
---

# DBA_ADVISOR_SQLA_WK_MAP

DBA_ADVISOR_SQLA_WK_MAP displays the workload references for all tasks in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the task |
| TASK_ID | NUMBER | Unique identifier of the task |
| TASK_NAME | VARCHAR2(128) | Name of the task |
| WORKLOAD_ID | NUMBER | Unique identifier of the workload object |
| WORKLOAD_NAME | VARCHAR2(128) | Name of the workload |
| IS_STS | NUMBER | Type of workload source: 0 - SQL workload object 1 - SQL Tuning Set |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Workload references are necessary to allow the SQL Access Advisor to find required workload data. Related View USER_ADVISOR_SQLA_WK_MAP displays the workload references for the tasks owned by the current user. This view does not display the OWNER column. See Also: " USER_ADVISOR_SQLA_WK_MAP "