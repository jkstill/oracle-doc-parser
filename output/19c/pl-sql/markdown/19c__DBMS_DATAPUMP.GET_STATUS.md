---
id: 19c__DBMS_DATAPUMP.GET_STATUS
name: DBMS_DATAPUMP.GET_STATUS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATAPUMP
tags: [dbms_datapump]
source_file: DBMS_DATAPUMP.html
---

# DBMS_DATAPUMP.GET_STATUS

This procedure monitors the status of a job or waits for the completion of a job.

## Syntax

```sql
DBMS_DATAPUMP.GET_STATUS(
   handle    IN NUMBER,
   mask      IN BINARY_INTEGER,
   timeout   IN NUMBER DEFAULT NULL,
   job_state OUT VARCHAR2,
   status    OUT ku$_Status);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| handle | NUMBER | IN | The handle of a job. The current session must have previously attached to the handle through a call to either the OPEN or ATTACH function. A null handle can be used to retrieve error information after OPEN and ATTACH failures. |
| mask | BINARY_INTEGER | IN | A bit mask that indicates which of four types of information to return: KU$_STATUS_WIP KU$_STATUS_JOB_DESC KU$_STATUS_JOB_STATUS KU$_STATUS_JOB_ERROR Each status has a numerical value. You can request multiple types of information by adding together different combinations of values. |
| timeout | NUMBER | IN | Maximum number of seconds to wait before returning to the user. A value of 0 requests an immediate return. A value of -1 requests an infinite wait. If KU$_STATUS_WIP or KU$_STATUS_JOB_ERROR information is requested and becomes available during the timeout period, then the procedure returns before the timeout period is over. |
| job_state | VARCHAR2 | OUT | Current state of the job. If only the job state is needed, it is much more efficient to use this parameter than to retrieve the full ku$_Status structure. |
| status | ku$_Status) | OUT | A ku$_Status is returned. The ku$_Status mask indicates what kind of information is included. This could be none if only KU$_STATUS_WIP or KU$_STATUS_JOB_ERROR information is requested and the timeout period expires. |

## Usage Notes

Syntax DBMS_DATAPUMP.GET_STATUS( handle IN NUMBER, mask IN BINARY_INTEGER, timeout IN NUMBER DEFAULT NULL, job_state OUT VARCHAR2, status OUT ku$_Status); Parameters Table 49-12 GET_STATUS Procedure Parameters Parameter Description handle The handle of a job. The current session must have previously attached to the handle through a call to either the OPEN or ATTACH function. A null handle can be used to retrieve error information after OPEN and ATTACH failures. mask A bit mask that indicates which of four types of information to return: KU$_STATUS_WIP KU$_STATUS_JOB_DESC KU$_STATUS_JOB_STATUS KU$_STATUS_JOB_ERROR Each status has a numerical value. You can request multiple types of information by adding together different combinations of values. timeout Maximum number of seconds to wait before returning to the user. A value of 0 requests an immediate return. A value of -1 requests an infinite wait. If KU$_STATUS_WIP or KU$_STATUS_JOB_ERROR information is requested and becomes available during the timeout period, then the procedure returns before the timeout period is over. job_state Current state of the job. If only the job state is needed, it is much more efficient to use this parameter than to retrieve the full ku$_Status structure. status A ku$_Status is returned. The ku$_Status mask indicates what kind of information is included. This could be none if only KU$_STATUS_WIP or KU$_STATUS_JOB_ERROR information is requested and the timeout period expires. Exceptions INVALID_HANDLE . The specified handle is not attached to a Data Pump job. INVALID_VALUE . The mask or timeout contains an illegal value. SUCCESS_WITH_INFO . The procedure succeeded, but further information is available through the GET_STATUS procedure. NO_SUCH_JOB . The specified job does not exist. Usage Notes The GET_STATUS procedure is used to monitor the progress of an ongoing job and to receive error notification. You can request various type of information using the mask parameter. The KU$_STATUS_JOB_DESC and KU$_STATUS_JOB_STATUS values are classified as synchronous information because the information resides in the master table. The KU$_STATUS_WIP and KU$_STATUS_JOB_ERROR values are classified as asynchronous because the messages that embody these types of information can be generated at any time by various layers in the Data Pump architecture. If synchronous information only is requested, the interface will ignore the timeout parameter and simply return the requested information. If asynchronous information is requested, the interface will wait a maximum of timeout seconds before returning to the client. If a message of the requested asynchronous information type is received, the call will complete prior to timeout seconds. If synchronous information was also requested, it will be returned whenever the procedure returns. If the job_state returned by GET_STATUS does not indicate a terminating job, it is possible that the job could still terminate before the next call to GET_STATUS . This would result in an INVALID_HANDLE exception. Alternatively, the job could terminate during the call to GET_STATUS , which would result in a NO_SUCH_JOB exception. Callers should be prepared to handle these cases. Error Handling There are two types of error scenarios that need to be handled using the GET_STATUS procedure: Errors resulting from other procedure calls: For example, the SET_PARAMETER procedure may produce an INCONSISTENT_ARGS exception. The client should immediately call GET_STATUS with mask=8 (errors) and timeout=0 . The returned ku$_Status.error will contain a ku$_LogEntry that describes the inconsistency in more detail. Errors resulting from events asynchronous to the client(s): An example might be Table already exists when trying to create a table. The ku$_Status.error will contain a ku$_LogEntry with all error lines (from all processing layers that added context about the error) properly ordered. After a job has begun, a client's main processing loop will typically consist of a call to GET_STATUS with an infinite timeout (-1) "listening" for KU$_STATUS_WIP and KU$_STATUS_JOB_ERROR messages. If status was requested, then JOB_STATUS information will also be in the request. When the ku$_Status is interpreted, the following guidelines should be used: ku$_Status.ku$_JobStatus.percent_done refers only to the amount of data that has been processed in a job. Metadata is not considered in the calculation. It is determined using the following formulas: EXPORT or network IMPORT-- (bytes_processed/estimated_bytes) * 100 IMPORT-- (bytes_processed/total_expected_bytes) * 100 SQL_FILE or estimate-only EXPORT-- 0.00 if not done or 100 . 00 if done The effects of the QUERY and PARTITION_EXPR data filters are not considered in computing percent_done . It is expected that the status returned will be transformed by the caller into more user-friendly status. For example, when percent done is not zero, an estimate of completion time could be produced using the following formula: ((SYSDATE - start time) / ku$_Status.ku$_JobStatus.percent_done) * 100 The caller should not use ku$_Status.ku$_JobStatus.percent_done for determining whether the job has completed. Instead, the caller should only rely on the state of the job as found in job_state .