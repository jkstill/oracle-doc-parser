---
id: 19c__DBMS_DATAPUMP.SET_PARALLEL
name: DBMS_DATAPUMP.SET_PARALLEL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATAPUMP
tags: [dbms_datapump]
source_file: DBMS_DATAPUMP.html
---

# DBMS_DATAPUMP.SET_PARALLEL

This procedure adjusts the degree of parallelism within a job.

## Syntax

```sql
DBMS_DATAPUMP.SET_PARALLEL(
   handle      IN NUMBER,
   degree      IN NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| handle | NUMBER | IN | The handle of a job. The current session must have previously attached to the handle through a call to either the OPEN or ATTACH function. |
| degree | NUMBER) | IN | The maximum number of worker processes that can be used for the job. You use this parameter to adjust the amount of resources used for a job. |

## Usage Notes

Syntax DBMS_DATAPUMP.SET_PARALLEL( handle IN NUMBER, degree IN NUMBER); Parameters Table 49-23 SET_PARALLEL Procedure Parameters Parameter Description handle The handle of a job. The current session must have previously attached to the handle through a call to either the OPEN or ATTACH function. degree The maximum number of worker processes that can be used for the job. You use this parameter to adjust the amount of resources used for a job. Exceptions INVALID_HANDLE . The specified handle is not attached to a Data Pump job. INVALID_OPERATION . The SET_PARALLEL procedure is only valid for export and import operations. INVALID_ARGVAL . An invalid value was supplied for an input parameter. SUCCESS_WITH_INFO . The procedure succeeded, but further information is available through the GET_STATUS procedure. NO_SUCH_JOB . The specified job does not exist. Usage Notes The SET_PARALLEL procedure is only available in the Enterprise Edition of the Oracle database. The SET_PARALLEL procedure can be executed by any session attached to a job. The job must be in one of the following states: Defining, Idling, or Executing. The effect of decreasing the degree of parallelism may be delayed because ongoing work needs to find an orderly completion point before SET_PARALLEL can take effect. Decreasing the parallelism will not result in fewer worker processes associated with the job. It will only decrease the number of worker processes that will be executing at any given time. Increasing the parallelism will take effect immediately if there is work that can be performed in parallel. The degree of parallelism requested by a user may be decreased based upon settings in the resource manager or through limitations introduced by the PROCESSES or SESSIONS initialization parameters in the init . ora file. To parallelize an Export job to a degree of n , the user should supply n files in the dump file set or specify a substitution variable in a file specification. Otherwise, some of the worker processes will be idle while waiting for files. SQL_FILE operations always operate with a degree of 1. Jobs running in the Transportable mode always operate with a degree of 1.