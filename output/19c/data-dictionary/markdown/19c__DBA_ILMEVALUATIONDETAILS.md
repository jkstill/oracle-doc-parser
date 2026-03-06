---
id: 19c__DBA_ILMEVALUATIONDETAILS
name: DBA_ILMEVALUATIONDETAILS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_ILMEVALUATIONDETAILS.html
---

# DBA_ILMEVALUATIONDETAILS

DBA_ILMEVALUATIONDETAILS displays details on evaluation of Automatic Data Optimization policies considered for Automatic Data Optimization tasks.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TASK_ID | NUMBER | Number that uniquely identifies a specific Automatic Data Optimization task |
| POLICY_NAME | VARCHAR2(128) | Name of the Automatic Data Optimization policy |
| OBJECT_OWNER | VARCHAR2(128) | Owner of the object associated with the Automatic Data Optimization policy |
| OBJECT_NAME | VARCHAR2(128) | Name of the object associated with the Automatic Data Optimization policy |
| SUBOBJECT_NAME | VARCHAR2(128) | Name of the subobject associated with the Automatic Data Optimization policy |
| OBJECT_TYPE | VARCHAR2(18) | Object type. Valid values include TABLE , TABLE PARTITION , and TABLE SUBPARTITION . |
| SELECTED_FOR_EXECUTION | VARCHAR2(42) | Indicates whether the policy has been selected for execution on the object. If not, the reason for not being selected is listed. Possible values: POLICY DISABLED SELECTED FOR EXECUTION POLICY OVERRULED INHERITED POLICY OVERRULED PRECONDITION NOT SATISFIED JOB ALREADY EXISTS NO OPERATION SINCE LAST ILM ACTION TABLE HAS MATERIALIZED VIEW TARGET COMPRESSION NOT HIGHER THAN CURRENT STATISTICS NOT AVAILABLE The value SELECTED FOR EXECUTION means a job was created for this policy on the object. The other values state the reason why the policy on the object was selected for execution. |
| JOB_NAME | VARCHAR2(128) | Name of the job in the case where the policy is selected for execution on this object |
| COMMENTS | VARCHAR2(4000) | Reserved for future use |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content It also shows the job name that executes the policy, in case the policy was selected for execution. If the policy was not selected for execution, this view provides a reason. Related View USER_ILMEVALUATIONDETAILS displays details on evaluation of Automatic Data Optimization policies considered for Automatic Data Optimization tasks for a user. It also shows the job name that executes the policy, in case the policy was selected for execution. If the policy was not selected for execution, this view provides a reason. Note: Automatic Data Optimization is supported in Oracle Database 12 c Release 2 multitenant environments. Note: Automatic Data Optimization is supported in Oracle Database 12 c Release 2 multitenant environments.