---
id: 19c__DBA_ILMRESULTS
name: DBA_ILMRESULTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_ILMRESULTS.html
---

# DBA_ILMRESULTS

DBA_ILMRESULTS displays information on data movement-related Automatic Data Optimization jobs in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TASK_ID | NUMBER | Number that uniquely identifies a specific Automatic Data Optimization task |
| JOB_NAME | VARCHAR2(128) | Name of the Automatic Data Optimization job |
| JOB_STATE | VARCHAR2(35) | State of the job. Possible values: JOB CREATED COMPLETED SUCCESSFULLY FAILED STOPPED JOB CREATION FAILED DEPENDENT OBJECTS BEING REBUILT FAILED TO REBUILD DEPENDENT OBJECTS |
| START_TIME | TIMESTAMP(6) | Start time of the Automatic Data Optimization job |
| COMPLETION_TIME | TIMESTAMP(6) | Completion time of the Automatic Data Optimization job |
| COMMENTS | VARCHAR2(4000) | Additional information in cases where the Automatic Data Optimization job execution fails |
| STATISTICS | CLOB | Job specific statistics, such as space saved via compression. This column is in the form of comma separated name / value pairs, with each pair representing a particular statistic name and value. |

## Usage Notes

Related View USER_ILMRESULTS displays information on data movement-related Automatic Data Optimization jobs for tasks created by the user. Note: Automatic Data Optimization is supported in Oracle Database 12 c Release 2 multitenant environments. Note: Automatic Data Optimization is supported in Oracle Database 12 c Release 2 multitenant environments. See Also: " USER_ILMRESULTS " See Also: " USER_ILMRESULTS "