---
id: 19c__DBA_ADVISOR_FDG_BREAKDOWN
name: DBA_ADVISOR_FDG_BREAKDOWN
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_ADVISOR_FDG_BREAKDOWN.html
---

# DBA_ADVISOR_FDG_BREAKDOWN

DBA_ADVISOR_FDG_BREAKDOWN describes the contribution from the different instances to the findings for each ADDM task.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TASK_ID | NUMBER | Unique identifier of the task (see DBA_ADVISOR_TASKS and DBA_ADDM_TASKS ) |
| FINDING_ID | NUMBER | Identifier of the finding to which this breakdown applies (see DBA_ADVISOR_FINDINGS and DBA_ADDM_FINDINGS ) |
| INSTANCE_NUMBER | NUMBER | The number of the instance for the breakdown |
| IMPACT | NUMBER | The database time (in microseconds) of the finding in the instance |
| PERC_IMPACT | NUMBER | Percentage of the contribution of the instance to the overall finding's impact |
| EXECUTION_NAME | VARCHAR2(128) | The name of the task execution with which this entry (row) is associated |

## Usage Notes

This view is populated only with ADDM tasks that are analyzing multiple instances (that is, the ACTUAL_ANALYSIS column in the task's row in DBA_ADDM_TASKS is set to DATABASE or PARTIAL ). Related View USER_ADVISOR_FDG_BREAKDOWN describes the contribution from the different instances to the findings for each ADDM task owned by the current user. See Also: " USER_ADVISOR_FDG_BREAKDOWN " See Also: " USER_ADVISOR_FDG_BREAKDOWN "