---
id: 19c__DBMS_DATAPUMP.STOP_JOB
name: DBMS_DATAPUMP.STOP_JOB
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATAPUMP
tags: [dbms_datapump]
source_file: DBMS_DATAPUMP.html
---

# DBMS_DATAPUMP.STOP_JOB

This procedure terminates a job, but optionally, preserves the state of the job.

## Syntax

```sql
DBMS_DATAPUMP.STOP_JOB (
   handle      IN NUMBER,
   immediate   IN NUMBER DEFAULT 0,
   keep_master IN NUMBER DEFAULT NULL,
   delay       IN NUMBER DEFAULT 60);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| handle | NUMBER | IN | The handle of a job. The current session must have previously attached to the handle through a call to either the OPEN or ATTACH function. At the end of the procedure, the user is detached from the handle. |
| immediate | NUMBER | IN | If nonzero, the worker processes are aborted immediately. This halts the job quickly, but parts of the job will have to be rerun if the job is ever restarted. If zero, the worker processes are allowed to complete their current work item (either metadata or table data) before they are terminated. The job is placed in a Stop Pending state while the workers finish their current work. |
| keep_master | NUMBER | IN | If nonzero, the master table is retained when the job is stopped. If zero, the master table is dropped when the job is stopped. If the master table is dropped, the job will not be restartable. If the master table is dropped during an export job, the created dump files are deleted. |
| delay | NUMBER | IN | The number of seconds to wait until other attached sessions are forcibly detached. The delay allows other sessions attached to the job to be notified that a stop has been performed. The job keeps running until either all clients have detached or the delay has been satisfied. If no delay is specified, then the default delay is 60 seconds. If a shorter delay is used, clients might not be able to retrieve the final messages for the job through the GET_STATUS procedure. |

## Usage Notes

Syntax DBMS_DATAPUMP.STOP_JOB ( handle IN NUMBER, immediate IN NUMBER DEFAULT 0, keep_master IN NUMBER DEFAULT NULL, delay IN NUMBER DEFAULT 60); Parameters Table 49-27 STOP_JOB Procedure Parameters Parameter Description handle The handle of a job. The current session must have previously attached to the handle through a call to either the OPEN or ATTACH function. At the end of the procedure, the user is detached from the handle. immediate If nonzero, the worker processes are aborted immediately. This halts the job quickly, but parts of the job will have to be rerun if the job is ever restarted. If zero, the worker processes are allowed to complete their current work item (either metadata or table data) before they are terminated. The job is placed in a Stop Pending state while the workers finish their current work. keep_master If nonzero, the master table is retained when the job is stopped. If zero, the master table is dropped when the job is stopped. If the master table is dropped, the job will not be restartable. If the master table is dropped during an export job, the created dump files are deleted. delay The number of seconds to wait until other attached sessions are forcibly detached. The delay allows other sessions attached to the job to be notified that a stop has been performed. The job keeps running until either all clients have detached or the delay has been satisfied. If no delay is specified, then the default delay is 60 seconds. If a shorter delay is used, clients might not be able to retrieve the final messages for the job through the GET_STATUS procedure. Exceptions INVALID_HANDLE . The specified handle is not attached to a Data Pump job. INVALID STATE . The job is already in the process of being stopped or completed. SUCCESS_WITH_INFO . The procedure succeeded, but further information is available through the GET_STATUS procedure. NO_SUCH_JOB . The specified job does not exist. Usage Notes This procedure is used to request that the corresponding job stop executing. The termination of a job that is in an Executing state may take several minutes to complete in an orderly fashion. For jobs in the Defining, Idling, or Completing states, this procedure is functionally equivalent to the DETACH procedure. Once a job is stopped, it can be restarted using the ATTACH function and START_JOB procedures, provided the master table and the dump file set are left intact. If the KEEP_MASTER parameter is not specified, and the job is in the Defining state or has a mode of Transportable, the master table is dropped. Otherwise, the master table is retained.