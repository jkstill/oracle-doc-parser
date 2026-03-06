---
id: 19c__DBMS_AUDIT_MGMT.LOAD_UNIFIED_AUDIT_FILES
name: DBMS_AUDIT_MGMT.LOAD_UNIFIED_AUDIT_FILES
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AUDIT_MGMT
tags: [dbms_audit_mgmt]
source_file: DBMS_AUDIT_MGMT.html
---

# DBMS_AUDIT_MGMT.LOAD_UNIFIED_AUDIT_FILES

This procedure loads the data from the spillover OS audit files in a unified audit trail into the designated unified audit trail tablespace.

## Syntax

```sql
DBMS_AUDIT_MGMT.LOAD_UNIFIED_AUDIT_FILES (
   load_batch_size IN PLS_INTEGER
   container       IN BINARY_INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| load_batch_size | PLS_INTEGER | IN | Specifies the number of spillover OS audit files to be loaded into the designated unified audit trail tablespace. The load_batch_size parameter can have a minimum value of 1 and maximum value of 32767. The default value is equivalent to DEFAULT_FILE_LOAD_BATCH_SIZE . |
| container | BINARY_INTEGER) | IN | Values: CONTAINER_CURRENT for the connected pluggable database (PDB) or CONTAINER_ALL for all pluggable databases (PDBs). CONTAINER_CURRENT - loads the unified audit files from $ORACLE_BASE/audit/$ORACLE_SID OS directory to the tables in only current PDB CONTAINER_ALL - loads the unified audit files from $ORACLE_BASE/audit/$ORACLE_SID OS directory to the tables in the respective PDBs, but for all the active PDBs |

## Usage Notes

See Also: Oracle Database Security Guide for information about moving the OS audit trail records into the unified audit trail See Also: Oracle Database Security Guide for information about moving the OS audit trail records into the unified audit trail Syntax DBMS_AUDIT_MGMT.LOAD_UNIFIED_AUDIT_FILES ( load_batch_size IN PLS_INTEGER container IN BINARY_INTEGER); Parameters Table 27-21 LOAD_UNIFIED_AUDIT_FILES Procedure Parameters Parameter Description load_batch_size Specifies the number of spillover OS audit files to be loaded into the designated unified audit trail tablespace. The load_batch_size parameter can have a minimum value of 1 and maximum value of 32767. The default value is equivalent to DEFAULT_FILE_LOAD_BATCH_SIZE . container Values: CONTAINER_CURRENT for the connected pluggable database (PDB) or CONTAINER_ALL for all pluggable databases (PDBs). CONTAINER_CURRENT - loads the unified audit files from $ORACLE_BASE/audit/$ORACLE_SID OS directory to the tables in only current PDB CONTAINER_ALL - loads the unified audit files from $ORACLE_BASE/audit/$ORACLE_SID OS directory to the tables in the respective PDBs, but for all the active PDBs