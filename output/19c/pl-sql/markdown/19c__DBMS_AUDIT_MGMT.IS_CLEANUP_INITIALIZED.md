---
id: 19c__DBMS_AUDIT_MGMT.IS_CLEANUP_INITIALIZED
name: DBMS_AUDIT_MGMT.IS_CLEANUP_INITIALIZED
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AUDIT_MGMT
tags: [dbms_audit_mgmt]
source_file: DBMS_AUDIT_MGMT.html
---

# DBMS_AUDIT_MGMT.IS_CLEANUP_INITIALIZED

This function checks to see if the INIT_CLEANUP Procedure has been run for an audit trail type.

## Syntax

```sql
DBMS_AUDIT_MGMT.IS_CLEANUP_INITIALIZED(
   audit_trail_type  IN PLS_INTEGER
   container         IN PLS_INTEGER DEFAULT CONTAINER_CURRENT)
 RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| audit_trail_type | PLS_INTEGER | IN | The audit trail type for which the function needs to be called. Note that this does not apply to AUDIT_TRAIL_UNIFIED . Audit trail types are listed in Table 27-1 |
| container | PLS_INTEGER | IN | Values: CONTAINER_CURRENT for the connected pluggable database (PDB) or CONTAINER_ALL for all pluggable databases (PDBs). When CONTAINER is set to CONTAINER_ALL , this function returns the initialization status of all the pluggable databases. The function returns FALSE even if one of the PDBs is not initialized. When CONTAINER is set to CONTAINER_CURRENT , this returns the initialization status of the connected PDB. |

**Returns:** `BOOLEAN`

## Usage Notes

The IS_CLEANUP_INITIALIZED function returns TRUE if the procedure has already been run for the audit trail type. It returns FALSE if the procedure has not been run for the audit trail type. This function is currently not relevant for the AUDIT_TRAIL_OS , AUDIT_TRAIL_XML , and AUDIT_TRAIL_FILES audit trail types. The function always returns TRUE for these audit trail types. No preliminary set up is required for these audit trail types. See Also: Table 27-1 for a list of all audit trail types See Also: Table 27-1 for a list of all audit trail types Syntax DBMS_AUDIT_MGMT.IS_CLEANUP_INITIALIZED( audit_trail_type IN PLS_INTEGER container IN PLS_INTEGER DEFAULT CONTAINER_CURRENT) RETURN BOOLEAN; Parameters Table 27-20 IS_CLEANUP_INITIALIZED Function Parameters Parameter Description audit_trail_type The audit trail type for which the function needs to be called. Note that this does not apply to AUDIT_TRAIL_UNIFIED . Audit trail types are listed in Table 27-1 container Values: CONTAINER_CURRENT for the connected pluggable database (PDB) or CONTAINER_ALL for all pluggable databases (PDBs). When CONTAINER is set to CONTAINER_ALL , this function returns the initialization status of all the pluggable databases. The function returns FALSE even if one of the PDBs is not initialized. When CONTAINER is set to CONTAINER_CURRENT , this returns the initialization status of the connected PDB. Examples The following example checks to see if the standard database audit trail type has been initialized for cleanup operation. If the audit trail type has not been initialized, then it calls the INIT_CLEANUP Procedure to initialize the audit trail type. BEGIN IF NOT DBMS_AUDIT_MGMT.IS_CLEANUP_INITIALIZED(DBMS_AUDIT_MGMT.AUDIT_TRAIL_AUD_STD) THEN DBMS_AUDIT_MGMT.INIT_CLEANUP( audit_trail_type => DBMS_AUDIT_MGMT.AUDIT_TRAIL_AUD_STD, default_cleanup_interval => 12 /* hours */); END IF; END;