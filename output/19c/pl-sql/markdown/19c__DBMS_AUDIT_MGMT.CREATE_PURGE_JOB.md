---
id: 19c__DBMS_AUDIT_MGMT.CREATE_PURGE_JOB
name: DBMS_AUDIT_MGMT.CREATE_PURGE_JOB
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AUDIT_MGMT
tags: [dbms_audit_mgmt]
source_file: DBMS_AUDIT_MGMT.html
---

# DBMS_AUDIT_MGMT.CREATE_PURGE_JOB

This procedure creates a purge job for periodically deleting the audit trail records.

## Syntax

```sql
DBMS_AUDIT_MGMT.CREATE_PURGE_JOB(
   audit_trail_type            IN PLS_INTEGER,
   audit_trail_purge_interval  IN PLS_INTEGER,
   audit_trail_purge_name      IN VARCHAR2,
   use_last_arch_timestamp     IN BOOLEAN DEFAULT TRUE,
   container                   IN PLS_INTEGER DEFAULT CONTAINER_CURRENT) ;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| audit_trail_type | PLS_INTEGER | IN | The audit trail type for which the purge job needs to be created. Audit trail types are listed in Table 27-1 . |
| audit_trail_purge_interval | PLS_INTEGER | IN | The interval, in hours, at which the clean up procedure is called. A lower value means that the cleanup is performed more often. |
| audit_trail_purge_name | VARCHAR2 | IN | A name to identify the purge job. |
| use_last_arch_timestamp | BOOLEAN | IN | Specifies whether the last archived timestamp should be used for deciding on the records that should be deleted. A value of TRUE indicates that only audit records created before the last archive timestamp should be deleted. A value of FALSE indicates that all audit records should be deleted. The default value is TRUE . |
| container | PLS_INTEGER | IN | Values: CONTAINER_CURRENT for the connected pluggable database (PDB) or CONTAINER_ALL for all pluggable databases (PDBs). When CONTAINER is set to CONTAINER_ALL , it creates one job in the Root PDB and the invocation of this job will invoke cleanup in all the PDBs. |

## Usage Notes

This procedure carries out the cleanup operation at intervals specified by the user. It calls the CLEAN_AUDIT_TRAIL Procedure to perform the cleanup operation. The SET_PURGE_JOB_INTERVAL Procedure is used to modify the frequency of the purge job. The SET_PURGE_JOB_STATUS Procedure is used to enable or disable the purge job. The DROP_PURGE_JOB Procedure is used to drop a purge job created with the CREATE_PURGE_JOB procedure. Syntax DBMS_AUDIT_MGMT.CREATE_PURGE_JOB( audit_trail_type IN PLS_INTEGER, audit_trail_purge_interval IN PLS_INTEGER, audit_trail_purge_name IN VARCHAR2, use_last_arch_timestamp IN BOOLEAN DEFAULT TRUE, container IN PLS_INTEGER DEFAULT CONTAINER_CURRENT) ; Parameters Table 27-12 CREATE_PURGE_JOB Procedure Parameters Parameter Description audit_trail_type The audit trail type for which the purge job needs to be created. Audit trail types are listed in Table 27-1 . audit_trail_purge_interval The interval, in hours, at which the clean up procedure is called. A lower value means that the cleanup is performed more often. audit_trail_purge_name A name to identify the purge job. use_last_arch_timestamp Specifies whether the last archived timestamp should be used for deciding on the records that should be deleted. A value of TRUE indicates that only audit records created before the last archive timestamp should be deleted. A value of FALSE indicates that all audit records should be deleted. The default value is TRUE . container Values: CONTAINER_CURRENT for the connected pluggable database (PDB) or CONTAINER_ALL for all pluggable databases (PDBs). When CONTAINER is set to CONTAINER_ALL , it creates one job in the Root PDB and the invocation of this job will invoke cleanup in all the PDBs. Usage Notes Use this procedure to schedule the CLEAN_AUDIT_TRAIL Procedure for your audit trail records. Examples The following example calls the CREATE_PURGE_JOB procedure to create a cleanup job called CLEANUP , for all audit trail types. It sets the audit_trail_purge_interval parameter to 100. This means that the cleanup job is invoked every 100 hours. It also sets the use_last_arch_timestamp parameter value to TRUE . This means that all audit records older than the last archive timestamp are deleted. BEGIN DBMS_AUDIT_MGMT.CREATE_PURGE_JOB( audit_trail_type => DBMS_AUDIT_MGMT.AUDIT_TRAIL_ALL, audit_trail_purge_interval => 100 /* hours */, audit_trail_purge_name => 'CLEANUP', use_last_arch_timestamp => TRUE); END;