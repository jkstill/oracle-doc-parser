---
id: 19c__UTL_RPADV.IS_MONITORING
name: UTL_RPADV.IS_MONITORING
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_RPADV
tags: [utl_rpadv]
source_file: UTL_RPADV.html
---

# UTL_RPADV.IS_MONITORING

This function checks whether a monitoring job is currently running. This function either returns TRUE if a monitoring job is currently running or FALSE if a monitoring job is not currently running.

## Syntax

```sql
UTL_RPADV.IS_MONITORING(
   job_name    IN VARCHAR2  DEFAULT 'STREAMS$_MONITORING_JOB',
   client_name IN VARCHAR2  DEFAULT NULL) 
RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| job_name | VARCHAR2 | IN | The name of the job for which to check. |
| client_name | VARCHAR2 | IN | The name of the client that submitted the job. |

**Returns:** `BOOLEAN`

## Usage Notes

A monitoring job is submitted using the START_MONITORING procedure. See Also: " START_MONITORING Procedure " See Also: " START_MONITORING Procedure " Syntax UTL_RPADV.IS_MONITORING( job_name IN VARCHAR2 DEFAULT 'STREAMS$_MONITORING_JOB', client_name IN VARCHAR2 DEFAULT NULL) RETURN BOOLEAN; Parameters Table 275-17 IS_MONITORING Function Parameters Parameter Description job_name The name of the job for which to check. client_name The name of the client that submitted the job.