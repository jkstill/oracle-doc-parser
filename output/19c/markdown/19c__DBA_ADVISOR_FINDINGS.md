---
id: 19c__DBA_ADVISOR_FINDINGS
name: DBA_ADVISOR_FINDINGS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_ADVISOR_FINDINGS.html
---

# DBA_ADVISOR_FINDINGS

DBA_ADVISOR_FINDINGS displays the findings discovered by all advisors in the database.

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

## Usage Notes

Related View USER_ADVISOR_FINDINGS displays the findings discovered by the advisors owned by the current user. This view does not display the OWNER column. See Also: " USER_ADVISOR_FINDINGS " See Also: " USER_ADVISOR_FINDINGS "