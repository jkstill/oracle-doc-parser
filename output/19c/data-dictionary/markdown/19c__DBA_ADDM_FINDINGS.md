---
id: 19c__DBA_ADDM_FINDINGS
name: DBA_ADDM_FINDINGS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_ADDM_FINDINGS.html
---

# DBA_ADDM_FINDINGS

DBA_ADDM_FINDINGS displays the ADDM findings discovered by all advisors in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the task |
| TASK_ID | NUMBER | Identifier of the task |
| TASK_NAME | VARCHAR2(128) | Name of the task |
| EXECUTION_NAME | VARCHAR2(128) | The name of the task execution with which this entry (row) is associated |
| FINDING_ID | NUMBER | Identifier of the finding |
| FINDING_NAME | VARCHAR2(4000) | Name of the finding |
| TYPE | VARCHAR2(11) | Type of the finding: PROBLEM SYMPTOM ERROR INFORMATION |
| TYPE_ID | NUMBER | Numeric ID for the value in column TYPE |
| PARENT | NUMBER | Identifier of the parent finding |
| OBJECT_ID | NUMBER | Identifier of the associated object, if any |
| IMPACT_TYPE | VARCHAR2(4000) | Impact of the finding on the system |
| IMPACT | NUMBER | Impact value |
| MESSAGE | VARCHAR2(4000) | Message describing the finding |
| MORE_INFO | VARCHAR2(4000) | Additional info associated with the finding |
| FILTERED | VARCHAR2(1) | A value of Y means that the row in the view was filtered out by a directive (or a combination of directives). A value of N means that the row was not filtered. |
| FLAGS | NUMBER | For internal use only by advisor framework clients |
| DATABASE_TIME | NUMBER | The database time, in microseconds, accumulated by this finding |
| ACTIVE_SESSIONS | NUMBER | The average number of active sessions for the finding |
| PERC_ACTIVE_SESS | NUMBER | The percentage of active sessions for this finding out of the total active sessions for the task |
| IS_AGGREGATE | CHAR(1) | A value of Y means that this finding is created for global/continental ADDM as an aggregate of local ADDM findings. Otherwise, the value is N . |
| METER_LEVEL | VARCHAR2(6) | Reserved for future use |
| QUERY_IS_APPROX | CHAR(1) | Indicates whether the ASH SQL associated with the finding is an approximate query ( Y ) or an exact query ( N ). To get the associated query, use the TASK_NAME and FINDING_ID columns from this view and call the PL/SQL function DBMS_ADDM.GET_ASH_QUERY(task_name, finding_id) . |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Each row for ADDM tasks in the related DBA_ADVISOR_FINDINGS view has a corresponding row in this view. Related View USER_ADDM_FINDINGS displays the ADDM findings discovered by the advisors owned by the current user. Each row for ADDM tasks in the related USER_ADVISOR_FINDINGS view has a corresponding row in this view. The USER_ADDM_FINDINGS view does not display the OWNER column. See Also: " USER_ADDM_FINDINGS " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_ADDM.GET_ASH_QUERY procedure