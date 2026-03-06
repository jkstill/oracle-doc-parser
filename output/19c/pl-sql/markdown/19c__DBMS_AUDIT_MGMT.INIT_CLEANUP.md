---
id: 19c__DBMS_AUDIT_MGMT.INIT_CLEANUP
name: DBMS_AUDIT_MGMT.INIT_CLEANUP
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AUDIT_MGMT
tags: [dbms_audit_mgmt]
source_file: DBMS_AUDIT_MGMT.html
---

# DBMS_AUDIT_MGMT.INIT_CLEANUP

This procedure sets up the audit management infrastructure and a default cleanup interval for the audit trail records.

## Syntax

```sql
DBMS_AUDIT_MGMT.INIT_CLEANUP(
   audit_trail_type          IN PLS_INTEGER,
   default_cleanup_interval  IN PLS_INTEGER
   container                 IN PLS_INTEGER DEFAULT CONTAINER_CURRENT);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| audit_trail_type | PLS_INTEGER | IN | The audit trail type for which the clean up operation needs to be initialized. Audit trail types are listed in Table 27-1 except AUDIT_TRAIL_UNIFIED |
| default_cleanup_interval | PLS_INTEGER | IN | The default time interval, in hours, after which the cleanup procedure should be called. The minimum value is 1 and the maximum is 999. |
| container | PLS_INTEGER | IN | Values: CONTAINER_CURRENT for the connected pluggable database (PDB) or CONTAINER_ALL for all Open and Available pluggable databases (PDBs). When CONTAINER is set to CONTAINER_ALL , this initializes the audit trails for clean up in all the Open and Available pluggable databases, otherwise this initializes the audit trail in the connected PDB only. When you add a new PDB you need to initialize the audit trails for clean up in the new PDB using the CONTAINER_CURRENT option. |

## Usage Notes

If the audit trail tables are in the SYSTEM tablespace, then the procedure moves them to the SYSAUX tablespace. If you are using unified auditing, you do not need to run this procedure because the unified audit trail tables are in the SYSAUX tablespace by default. If you are not using unified auditing, refer to Oracle Database Upgrade Guide for documentation which references an environment without unified auditing. Moving the audit trail tables out of the SYSTEM tablespace enhances overall database performance. The INIT_CLEANUP procedure moves the audit trail tables to the SYSAUX tablespace. If the SET_AUDIT_TRAIL_LOCATION Procedure has already moved the audit tables elsewhere, then no tables are moved. The SET_AUDIT_TRAIL_LOCATION Procedure enables you to specify an alternate target tablespace for the database audit tables. The INIT_CLEANUP procedure is currently not relevant for the AUDIT_TRAIL_OS , AUDIT_TRAIL_XML , and AUDIT_TRAIL_FILES audit trail types. No preliminary set up is required for these audit trail types. See Also: Table 27-1 for a list of all audit trail types This procedure also sets a default cleanup interval for the audit trail records. See Also: Table 27-1 for a list of all audit trail types Syntax DBMS_AUDIT_MGMT.INIT_CLEANUP( audit_trail_type IN PLS_INTEGER, default_cleanup_interval IN PLS_INTEGER container IN PLS_INTEGER DEFAULT CONTAINER_CURRENT); Parameters Table 27-19 INIT_CLEANUP Procedure Parameters Parameter Description audit_trail_type The audit trail type for which the clean up operation needs to be initialized. Audit trail types are listed in Table 27-1 except AUDIT_TRAIL_UNIFIED default_cleanup_interval The default time interval, in hours, after which the cleanup procedure should be called. The minimum value is 1 and the maximum is 999. container Values: CONTAINER_CURRENT for the connected pluggable database (PDB) or CONTAINER_ALL for all Open and Available pluggable databases (PDBs). When CONTAINER is set to CONTAINER_ALL , this initializes the audit trails for clean up in all the Open and Available pluggable databases, otherwise this initializes the audit trail in the connected PDB only. When you add a new PDB you need to initialize the audit trails for clean up in the new PDB using the CONTAINER_CURRENT option. Usage Notes The following usage notes apply: This procedure may involve data movement across tablespaces. This can be a resource intensive operation especially if your database audit trail tables are already populated. Oracle recommends that you invoke the procedure during non-peak hours. You should ensure that the SYSAUX tablespace, into which the audit trail tables are being moved, has sufficient space to accommodate the audit trail tables. You should also optimize the SYSAUX tablespace for frequent write operations. You can change the default_cleanup_interval later using the SET_AUDIT_TRAIL_PROPERTY Procedure . If you do not wish to move the audit trail tables to the SYSAUX tablespace, then you should use the DBMS_AUDIT_MGMT.SET_AUDIT_TRAIL_LOCATION procedure to move the audit trail tables to another tablespace before calling the INIT_CLEANUP procedure. Invoking this procedure with AUDIT_TRAIL_UNIFIED results in ORA-46250 . It requires no initializations for cleanup since it is cleanup-ready by default.