---
id: 19c__DBA_ADVISOR_SQLA_REC_SUM
name: DBA_ADVISOR_SQLA_REC_SUM
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dba]
source_file: DBA_ADVISOR_SQLA_REC_SUM.html
---

# DBA_ADVISOR_SQLA_REC_SUM

DBA_ADVISOR_SQLA_REC_SUM displays recommendation rollup information for all workload objects in the database after an Access Advisor analysis operation.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the task |
| TASK_ID | NUMBER | Unique identifier of the task |
| TASK_NAME | VARCHAR2(128) | Name of the task |
| REC_ID | NUMBER | Identifier of the recommendation |
| TOTAL_STMTS | NUMBER | Total number of statements processed during analysis |
| TOTAL_PRECOST | NUMBER | Total cost of executing the statements in which the recommended object will be used, before the recommendations |
| TOTAL_POSTCOST | NUMBER | Total cost of executing the statements in which the recommended object will be utilized, after the recommendations have been implemented |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View USER_ADVISOR_SQLA_REC_SUM displays recommendation rollup information for the workload objects owned by the current user. This view does not display the OWNER column. See Also: " USER_ADVISOR_SQLA_REC_SUM " See Also: " USER_ADVISOR_SQLA_REC_SUM "