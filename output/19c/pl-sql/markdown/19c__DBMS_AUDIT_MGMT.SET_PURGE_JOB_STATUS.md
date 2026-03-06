---
id: 19c__DBMS_AUDIT_MGMT.SET_PURGE_JOB_STATUS
name: DBMS_AUDIT_MGMT.SET_PURGE_JOB_STATUS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AUDIT_MGMT
tags: [dbms_audit_mgmt]
source_file: DBMS_AUDIT_MGMT.html
---

# DBMS_AUDIT_MGMT.SET_PURGE_JOB_STATUS

This procedure enables or disables the specified purge job.

## Syntax

```sql
DBMS_AUDIT_MGMT.SET_PURGE_JOB_STATUS(
   audit_trail_purge_name    IN VARCHAR2,
   audit_trail_status_value  IN PLS_INTEGER) ;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| audit_trail_purge_name | VARCHAR2 | IN | The name of the purge job for which the status is being set. This is the purge job name that you specified with the CREATE_PURGE_JOB Procedure . |
| audit_trail_status_value | PLS_INTEGER) | IN | One of the values specified in Table 27-3 . The value PURGE_JOB_ENABLE enables the specified purge job. The value PURGE_JOB_DISABLE disables the specified purge job. |

## Usage Notes

The purge job must have already been created using the CREATE_PURGE_JOB Procedure . Syntax DBMS_AUDIT_MGMT.SET_PURGE_JOB_STATUS( audit_trail_purge_name IN VARCHAR2, audit_trail_status_value IN PLS_INTEGER) ; Parameters Table 27-26 SET_PURGE_JOB_STATUS Procedure Parameters Parameter Description audit_trail_purge_name The name of the purge job for which the status is being set. This is the purge job name that you specified with the CREATE_PURGE_JOB Procedure . audit_trail_status_value One of the values specified in Table 27-3 . The value PURGE_JOB_ENABLE enables the specified purge job. The value PURGE_JOB_DISABLE disables the specified purge job. Examples The following example calls the SET_PURGE_JOB_STATUS procedure to enable the CLEANUP purge job. BEGIN DBMS_AUDIT_MGMT.SET_PURGE_JOB_STATUS( audit_trail_purge_name => 'CLEANUP', audit_trail_status_value => DBMS_AUDIT_MGMT.PURGE_JOB_ENABLE); END;