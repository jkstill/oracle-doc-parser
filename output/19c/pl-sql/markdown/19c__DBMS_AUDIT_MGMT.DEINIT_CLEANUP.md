---
id: 19c__DBMS_AUDIT_MGMT.DEINIT_CLEANUP
name: DBMS_AUDIT_MGMT.DEINIT_CLEANUP
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AUDIT_MGMT
tags: [dbms_audit_mgmt]
source_file: DBMS_AUDIT_MGMT.html
---

# DBMS_AUDIT_MGMT.DEINIT_CLEANUP

This procedure undoes the setup and initialization performed by the INIT_CLEANUP Procedure. The DEINIT_CLEANUP procedure clears the value of the default_cleanup_interval parameter. However, when used for audit tables, it does not move the audit trail tables back to their original tablespace.

## Syntax

```sql
DBMS_AUDIT_MGMT.DEINIT_CLEANUP(
   audit_trail_type  IN PLS_INTEGER, 
   container         IN PLS_INTEGER DEFAULT CONTAINER_CURRENT);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| audit_trail_type | PLS_INTEGER | IN | The audit trail type for which the procedure needs to be called. Audit trail types are listed in Table 27-1 |
| container | PLS_INTEGER | IN | Values: CONTAINER_CURRENT for the connected pluggable database (PDB) or CONTAINER_ALL for all pluggable databases (PDBs). When CONTAINER is set to CONTAINER_ALL , this de-initializes the audit trail from cleanup in all the pluggable databases, otherwise it de-initializes the audit trail from cleanup in the connected PDB only. |

## Usage Notes

Syntax DBMS_AUDIT_MGMT.DEINIT_CLEANUP( audit_trail_type IN PLS_INTEGER, container IN PLS_INTEGER DEFAULT CONTAINER_CURRENT); Parameters Table 27-13 DEINIT_CLEANUP Procedure Parameters Parameter Description audit_trail_type The audit trail type for which the procedure needs to be called. Audit trail types are listed in Table 27-1 container Values: CONTAINER_CURRENT for the connected pluggable database (PDB) or CONTAINER_ALL for all pluggable databases (PDBs). When CONTAINER is set to CONTAINER_ALL , this de-initializes the audit trail from cleanup in all the pluggable databases, otherwise it de-initializes the audit trail from cleanup in the connected PDB only. Usage Notes You cannot invoke this procedure for AUDIT_TRAIL_UNIFIED . Doing so it will raise ORA-46250 : Invalid value for argument 'AUDIT_TRAIL_TYPE' Examples The following example clears the default_cleanup_interval parameter setting for the standard database audit trail: BEGIN DBMS_AUDIT_MGMT.DEINIT_CLEANUP( AUDIT_TRAIL_TYPE => DBMS_AUDIT_MGMT.AUDIT_TRAIL_AUD_STD); END;