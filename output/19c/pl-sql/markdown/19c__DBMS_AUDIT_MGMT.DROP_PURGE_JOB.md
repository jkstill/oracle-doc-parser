---
id: 19c__DBMS_AUDIT_MGMT.DROP_PURGE_JOB
name: DBMS_AUDIT_MGMT.DROP_PURGE_JOB
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AUDIT_MGMT
tags: [dbms_audit_mgmt]
source_file: DBMS_AUDIT_MGMT.html
---

# DBMS_AUDIT_MGMT.DROP_PURGE_JOB

This procedure drops the purge job created using the CREATE_PURGE_JOB Procedure. The name of the purge job is passed as an argument.

## Syntax

```sql
DBMS_AUDIT_MGMT.DROP_PURGE_JOB(
   audit_trail_purge_name    IN VARCHAR2) ;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| audit_trail_purge_name | VARCHAR2) | IN | The name of the purge job which is being deleted. This is the purge job name that you specified with the CREATE_PURGE_JOB Procedure . |

## Usage Notes

Syntax DBMS_AUDIT_MGMT.DROP_PURGE_JOB( audit_trail_purge_name IN VARCHAR2) ; Parameters Table 27-15 DROP_PURGE_JOB Procedure Parameters Parameter Description audit_trail_purge_name The name of the purge job which is being deleted. This is the purge job name that you specified with the CREATE_PURGE_JOB Procedure . Examples The following example calls the DROP_PURGE_JOB procedure to drop the purge job called CLEANUP . BEGIN DBMS_AUDIT_MGMT.DROP_PURGE_JOB( AUDIT_TRAIL_PURGE_NAME => 'CLEANUP'); END;