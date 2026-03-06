---
id: 19c__DBMS_AUDIT_MGMT.SET_PURGE_JOB_INTERVAL
name: DBMS_AUDIT_MGMT.SET_PURGE_JOB_INTERVAL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AUDIT_MGMT
tags: [dbms_audit_mgmt]
source_file: DBMS_AUDIT_MGMT.html
---

# DBMS_AUDIT_MGMT.SET_PURGE_JOB_INTERVAL

This procedure sets the interval at which the CLEAN_AUDIT_TRAIL Procedure is called for the purge job specified.

## Syntax

```sql
DBMS_AUDIT_MGMT.SET_PURGE_JOB_INTERVAL(
   audit_trail_purge_name      IN VARCHAR2,
   audit_trail_interval_value  IN PLS_INTEGER) ;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| audit_trail_purge_name | VARCHAR2 | IN | The name of the purge job for which the interval is being set. This is the purge job name that you specified with the CREATE_PURGE_JOB Procedure . |
| audit_trail_interval_value | PLS_INTEGER) | IN | The interval, in hours, at which the clean up procedure should be called. This value modifies the audit_trail_purge_interval parameter set using the CREATE_PURGE_JOB Procedure |

## Usage Notes

The purge job must have already been created using the CREATE_PURGE_JOB Procedure . Syntax DBMS_AUDIT_MGMT.SET_PURGE_JOB_INTERVAL( audit_trail_purge_name IN VARCHAR2, audit_trail_interval_value IN PLS_INTEGER) ; Parameters Table 27-25 SET_PURGE_JOB_INTERVAL Procedure Parameters Parameter Description audit_trail_purge_name The name of the purge job for which the interval is being set. This is the purge job name that you specified with the CREATE_PURGE_JOB Procedure . audit_trail_interval_value The interval, in hours, at which the clean up procedure should be called. This value modifies the audit_trail_purge_interval parameter set using the CREATE_PURGE_JOB Procedure Usage Notes Use this procedure to modify the audit_trail_purge_interval parameter set using the CREATE_PURGE_JOB Procedure . Examples The following example calls the SET_PURGE_JOB_INTERVAL procedure to change the frequency at which the purge job called CLEANUP is invoked. The new interval is set to 24 hours. BEGIN DBMS_AUDIT_MGMT.SET_PURGE_JOB_INTERVAL( AUDIT_TRAIL_PURGE_NAME => 'CLEANUP', AUDIT_TRAIL_INTERVAL_VALUE => 24 ); END;