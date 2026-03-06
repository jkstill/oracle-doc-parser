---
id: 19c__DBMS_DATAPUMP.ATTACH
name: DBMS_DATAPUMP.ATTACH
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATAPUMP
tags: [dbms_datapump]
source_file: DBMS_DATAPUMP.html
---

# DBMS_DATAPUMP.ATTACH

This function provides access to a previously created job.

## Syntax

```sql
DBMS_DATAPUMP.ATTACH(
   job_name    IN VARCHAR2 DEFAULT NULL,
   job_owner    IN VARCHAR2 DEFAULT NULL) 
 RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| job_name | VARCHAR2 | IN | The name of the job. The default is the job name owned by the user who is specified in the job_owner parameter (assuming that user has only one job in the Defining, Executing, or Idling states). |
| job_owner | VARCHAR2 | IN | The user who originally started the job. If NULL , then the value defaults to the owner of the current session. To specify a job owner other than yourself, you must have either the DATAPUMP_EXP_FULL_DATABASE role (for export operations) or the DATAPUMP_IMP_FULL_DATABASE role (for import and SQL_FILE operations). Being a privileged user allows you to monitor another user's job, but you cannot restart another user's job. |

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_DATAPUMP.ATTACH( job_name IN VARCHAR2 DEFAULT NULL, job_owner IN VARCHAR2 DEFAULT NULL) RETURN NUMBER; Parameters Table 49-4 ATTACH Function Parameters Parameter Description job_name The name of the job. The default is the job name owned by the user who is specified in the job_owner parameter (assuming that user has only one job in the Defining, Executing, or Idling states). job_owner The user who originally started the job. If NULL , then the value defaults to the owner of the current session. To specify a job owner other than yourself, you must have either the DATAPUMP_EXP_FULL_DATABASE role (for export operations) or the DATAPUMP_IMP_FULL_DATABASE role (for import and SQL_FILE operations). Being a privileged user allows you to monitor another user's job, but you cannot restart another user's job. Return Values An opaque handle for the job. This handle is used as input to the following procedures: ADD_FILE , DATA_FILTER , DETACH , GET_STATUS , LOG_ENTRY , METADATA_FILTER , METADATA_REMAP , METADATA_TRANSFORM , SET_PARALLEL , SET_PARAMETER,START_JOB , STOP_JOB , and WAIT_FOR_JOB . Exceptions INVALID_ARGVAL . An invalid value was supplied for an input parameter. OBJECT_NOT_FOUND . The specified job no longer exists or the user specified a job owned by another schema, but the user did not have the DATAPUMP_EXP_FULL_DATABASE or DATAPUMP_IMP_FULL_DATABASE role. SUCCESS_WITH_INFO . The function succeeded, but further information is available through the GET_STATUS procedure. NO_SUCH_JOB . The specified job does not exist. Usage Notes If the job was in the Stopped state, then the job is placed into the Idling state. After the ATTACH succeeds, you can monitor the progress of the job or control the job. The stream of KU$_STATUS_WIP and KU$_STATUS_JOB_ERROR messages returned through the GET_STATUS procedure will be returned to the newly attached job starting at the approximate time of the client's attachment. There will be no repeating of status and error messages that were processed before the client attached to a job. If you want to perform a second attach to a job, then you must do so from a different session. If the ATTACH fails, then use a null handle in a subsequent call to GET_STATUS for more information about the failure.