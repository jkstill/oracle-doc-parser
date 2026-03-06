---
id: 19c__DBMS_MGWADM.RESET_JOB
name: DBMS_MGWADM.RESET_JOB
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGWADM
tags: [dbms_mgwadm]
source_file: DBMS_MGWADM.html
---

# DBMS_MGWADM.RESET_JOB

This procedure resets the propagation error state for a propagation job.

## Syntax

```sql
DBMS_MGWADM.RESET_JOB (
   job_name   IN   VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| job_name | VARCHAR2) | IN | Identifies the propagation job |

## Usage Notes

Syntax DBMS_MGWADM.RESET_JOB ( job_name IN VARCHAR2); Parameters Table 110-43 RESET_JOB Procedure Parameters Parameter Description job_name Identifies the propagation job Usage Notes This procedure can be used to reset a propagation job that has been set to a failed state and propagation activities have been stopped. The administrator should correct the problem and then call this procedure to allow the agent to retry the propagation job. The STATUS field of the MGW_JOBS view indicates the job status.