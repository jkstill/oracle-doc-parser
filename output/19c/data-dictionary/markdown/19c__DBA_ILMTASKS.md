---
id: 19c__DBA_ILMTASKS
name: DBA_ILMTASKS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_ILMTASKS.html
---

# DBA_ILMTASKS

DBA_ILMTASKS displays information on Automatic Data Optimization execution.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TASK_ID | NUMBER | Number that uniquely identifies a specific Automatic Data Optimization task |
| TASK_OWNER | VARCHAR2(128) | User who initiates the task |
| STATE | VARCHAR2(9) | Possible values: INACTIVE : Indicates that the task was created for previewing ACTIVE : Indicates that jobs have been created for the qualifying policies in the task COMPLETE : Indicates that the task has completed |
| CREATION_TIME | TIMESTAMP(6) | The time that the task was created |
| START_TIME | TIMESTAMP(6) | Start time of a specific task |
| COMPLETION_TIME | TIMESTAMP(6) | Completion time of a specific task |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View USER_ILMTASKS displays information on Automatic Data Optimization tasks created by a user. Note: Automatic Data Optimization is supported in Oracle Database 12 c Release 2 multitenant environments. Note: Automatic Data Optimization is supported in Oracle Database 12 c Release 2 multitenant environments. See Also: " USER_ILMTASKS "