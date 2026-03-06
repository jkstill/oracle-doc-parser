---
id: 19c__DBA_SQLTUNE_RATIONALE_PLAN
name: DBA_SQLTUNE_RATIONALE_PLAN
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dba]
source_file: DBA_SQLTUNE_RATIONALE_PLAN.html
---

# DBA_SQLTUNE_RATIONALE_PLAN

DBA_SQLTUNE_RATIONALE_PLAN displays the association between rationales and operations in the execution plan of all SQL statements in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TASK_ID | NUMBER(38) | Tuning task identifier |
| EXECUTION_NAME | VARCHAR2(128) | The name of the task execution with which this entry (row) is associated |
| RATIONALE_ID | NUMBER(38) | Rationale identifier |
| OBJECT_ID | NUMBER(38) | Advisor framework object identifier |
| OPERATION_ID | NUMBER(38) | Operation identifier |
| PLAN_ATTRIBUTE | VARCHAR2(34) | Type of the execution plan: Original - Original plan of the query Original with adjusted cost - Same as Original but with adjusted cost Using SQL profile - Plan with SQL profile applied Using new indices - Plan with indexes applied |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View USER_SQLTUNE_RATIONALE_PLAN displays the association between rationales and operations in the execution plan of the SQL statements owned by the current user. See Also: " USER_SQLTUNE_RATIONALE_PLAN " See Also: " USER_SQLTUNE_RATIONALE_PLAN "