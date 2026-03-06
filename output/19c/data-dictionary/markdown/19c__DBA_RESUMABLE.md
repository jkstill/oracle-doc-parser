---
id: 19c__DBA_RESUMABLE
name: DBA_RESUMABLE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_RESUMABLE.html
---

# DBA_RESUMABLE

DBA_RESUMABLE displays all resumable statements executed in the system.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| USER_ID | NUMBER | User ID Number of the Resumable Statement Owner |
| SESSION_ID | NUMBER | Session Identifier of the Resumable Statement |
| INSTANCE_ID | NUMBER | Instance Number of the Resumable Statement |
| COORD_INSTANCE_ID | NUMBER | Instance Number on which the Parallel Coordinator is Running |
| COORD_SESSION_ID | NUMBER | Session Identifier of the Parallel Coordinator |
| STATUS | VARCHAR2(9) | Status of the resumable statement: RUNNING SUSPENDED TIMEOUT ERROR ABORTED |
| TIMEOUT | NUMBER | Timeout of the resumable statement |
| START_TIME | VARCHAR2(20) | Start time of the resumable statement |
| SUSPEND_TIME | VARCHAR2(20) | Last time the resumable statement was suspended (initialized to NULL) |
| RESUME_TIME | VARCHAR2(20) | Last time the suspended resumable statement was resumed (initialized to NULL) |
| NAME | VARCHAR2(4000) | Name given in the resumable clause of the resumable statement |
| SQL_TEXT | VARCHAR2(1000) | Resumable statement, selected from the V$SQL view |
| ERROR_NUMBER | NUMBER | Error code of the last correctable error. When STATUS is set to RUNNING , its value will be 0. |
| ERROR_PARAMETER1 | VARCHAR2(80) | First parameter for the error message (NULL if no error) |
| ERROR_PARAMETER2 | VARCHAR2(80) | Second parameter for the error message (NULL if no error) |
| ERROR_PARAMETER3 | VARCHAR2(80) | Third parameter for the error message (NULL if no error) |
| ERROR_PARAMETER4 | VARCHAR2(80) | Forth parameter for the error message (NULL if no error) |
| ERROR_PARAMETER5 | VARCHAR2(80) | Fifth parameter for the error message (NULL if no error) |
| ERROR_MSG | VARCHAR2(4000) | Error message corresponding to ERROR_NUMBER . It will be NULL when ERROR_NUMBER is 0. |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View USER_RESUMABLE displays the resumable statements executed by the current user. This view does not display the USER_ID column. See Also: " USER_RESUMABLE " See Also: " USER_RESUMABLE "