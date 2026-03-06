---
id: 19c__DBMS_DATAPUMP.START_JOB
name: DBMS_DATAPUMP.START_JOB
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATAPUMP
tags: [dbms_datapump]
source_file: DBMS_DATAPUMP.html
---

# DBMS_DATAPUMP.START_JOB

This procedure begins or resumes job execution.

## Syntax

```sql
DBMS_DATAPUMP.START_JOB (
   handle       IN NUMBER,
   skip_current    IN  NUMBER DEFAULT 0,
   abort_step      IN  NUMBER DEFAULT 0,
   cluster_ok      IN  NUMBER DEFAULT 1,
   service_name    IN  VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| handle | NUMBER | IN | The handle of a job. The current session must have previously attached to the handle through a call to either the OPEN or ATTACH function. |
| skip_current | NUMBER | IN | If nonzero, causes actions that were 'in progress' on a previous execution of the job to be skipped when the job restarts. The skip will only be honored for Import jobs. This mechanism allows the user to skip actions that trigger fatal bugs and cause the premature termination of a job. Multiple actions can be skipped on a restart. The log file will identify which actions are skipped. If a domain index was being processed, all pieces of the domain index are skipped even if the error occurred in only a subcomponent of the domain index. A description of the actions skipped is entered into the log file. skip_current is ignored for the initial START_JOB in a job. If zero, no data or metadata is lost upon a restart. |
| abort_step | NUMBER | IN | Value must be 0. Inserting values other than 0 into this argument will have unintended consequences. |
| cluster_ok | NUMBER | IN | If = 0, all workers are started on the current instance. Otherwise, workers are started on instances usable by the job. |
| service_name | VARCHAR2 | IN | If specified, indicates a service name used to constrain the job to specific instances or to a specific resource group. |

## Usage Notes

Syntax DBMS_DATAPUMP.START_JOB ( handle IN NUMBER, skip_current IN NUMBER DEFAULT 0, abort_step IN NUMBER DEFAULT 0, cluster_ok IN NUMBER DEFAULT 1, service_name IN VARCHAR2 DEFAULT NULL); Parameters Table 49-26 START_JOB Procedure Parameters Parameter Description handle The handle of a job. The current session must have previously attached to the handle through a call to either the OPEN or ATTACH function. skip_current If nonzero, causes actions that were 'in progress' on a previous execution of the job to be skipped when the job restarts. The skip will only be honored for Import jobs. This mechanism allows the user to skip actions that trigger fatal bugs and cause the premature termination of a job. Multiple actions can be skipped on a restart. The log file will identify which actions are skipped. If a domain index was being processed, all pieces of the domain index are skipped even if the error occurred in only a subcomponent of the domain index. A description of the actions skipped is entered into the log file. skip_current is ignored for the initial START_JOB in a job. If zero, no data or metadata is lost upon a restart. abort_step Value must be 0. Inserting values other than 0 into this argument will have unintended consequences. cluster_ok If = 0, all workers are started on the current instance. Otherwise, workers are started on instances usable by the job. service_name If specified, indicates a service name used to constrain the job to specific instances or to a specific resource group. Exceptions INVALID_HANDLE . The specified handle is not attached to a Data Pump job. INVALID_STATE . The causes of this exception can be any of the following: No files have been defined for an Export, non-network Import, or SQL_FILE job An ADD_FILE procedure has not been called to define the output for a SQL_FILE job A TABLESPACE_DATAFILE parameter has not been defined for a Transportable Import job A TABLESPACE_EXPR metadata filter has not been defined for a Transportable or Tablespace mode Export or Network job The dump file set on an Import or SQL_FILE job was either incomplete or missing a master table specification INVALID_OPERATION . Unable to restore master table from a dump file set. INTERNAL_ERROR . An inconsistency was detected when the job was started. Additional information may be available through the GET_STATUS procedure. SUCCESS_WITH_INFO . The procedure succeeded, but further information is available through the GET_STATUS procedure. NO_SUCH_JOB . The specified job does not exist. Usage Notes When this procedure is called to request that the corresponding job be started or restarted, the state of the job is changed from either the Defining or Idling state to the Executing state. If the SET_PARALLEL procedure was not called prior to the START_JOB procedure, the initial level of parallelism used in the job will be 1. If SET_PARALLEL was called prior to the job starting, the degree specified by the last SET_PARALLEL call determines the parallelism for the job. On restarts, the parallelism is determined by the previous parallel setting for the job, unless it is overridden by another SET_PARALLEL call. To restart a stopped job, an ATTACH function must be performed prior to executing the START_JOB procedure.