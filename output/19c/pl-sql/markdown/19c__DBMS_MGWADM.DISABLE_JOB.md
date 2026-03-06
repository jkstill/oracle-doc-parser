---
id: 19c__DBMS_MGWADM.DISABLE_JOB
name: DBMS_MGWADM.DISABLE_JOB
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGWADM
tags: [dbms_mgwadm]
source_file: DBMS_MGWADM.html
---

# DBMS_MGWADM.DISABLE_JOB

This procedure disables a propagation job.

## Syntax

```sql
DBMS_MGWADM.DISABLE_JOB (
   job_name  IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| job_name | VARCHAR2) | IN | Identifies the propagation job |

## Usage Notes

Syntax DBMS_MGWADM.DISABLE_JOB ( job_name IN VARCHAR2); Parameters Table 110-33 DISABLE_JOB Procedure Parameters Parameter Description job_name Identifies the propagation job