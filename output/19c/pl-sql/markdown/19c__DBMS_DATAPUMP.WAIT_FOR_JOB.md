---
id: 19c__DBMS_DATAPUMP.WAIT_FOR_JOB
name: DBMS_DATAPUMP.WAIT_FOR_JOB
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATAPUMP
tags: [dbms_datapump]
source_file: DBMS_DATAPUMP.html
---

# DBMS_DATAPUMP.WAIT_FOR_JOB

This procedure runs a job until it either completes normally or stops for some other reason.

## Syntax

```sql
DBMS_DATAPUMP.WAIT_FOR_JOB (
  handle      IN   NUMBER,
  job_state   OUT  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| handle | NUMBER | IN | The handle of the job. The current session must have previously attached to the handle through a call to either the OPEN or ATTACH function. At the end of the procedure, the user is detached from the handle. |
| job_state | VARCHAR2) | OUT | The state of the job when it has stopped executing; either STOPPED or COMPLETED . |

## Usage Notes

Syntax DBMS_DATAPUMP.WAIT_FOR_JOB ( handle IN NUMBER, job_state OUT VARCHAR2); Parameters Table 49-28 WAIT_FOR_JOB Procedure Parameters Parameter Description handle The handle of the job. The current session must have previously attached to the handle through a call to either the OPEN or ATTACH function. At the end of the procedure, the user is detached from the handle. job_state The state of the job when it has stopped executing; either STOPPED or COMPLETED . Exceptions SUCCESS_WITH_INFO . The procedure succeeded, but further information is available through the GET_STATUS API. INVALID_HANDLE . The job handle is no longer valid. Usage Notes This procedure provides the simplest mechanism for waiting for the completion of a Data Pump job. The job should be started before calling WAIT_FOR_JOB . When WAIT_FOR_JOB returns, the job will no longer be executing. If the job completed normally, the final status will be COMPLETED . If the job stopped executing because of a STOP_JOB request or an internal error, the final status will be STOPPED .