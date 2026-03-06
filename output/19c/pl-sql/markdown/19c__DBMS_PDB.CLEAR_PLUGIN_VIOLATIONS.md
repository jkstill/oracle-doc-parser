---
id: 19c__DBMS_PDB.CLEAR_PLUGIN_VIOLATIONS
name: DBMS_PDB.CLEAR_PLUGIN_VIOLATIONS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PDB
tags: [dbms_pdb]
source_file: DBMS_PDB.html
---

# DBMS_PDB.CLEAR_PLUGIN_VIOLATIONS

This procedure is used for cleaning up RESOLVED or PENDING violations in pdb_plug_in_violations .

## Syntax

```sql
DBMS_PDB.CLEAR_PLUGIN_VIOLATIONS (
  pdb_name      IN VARCHAR2 DEFAULT NULL
  clear_pending IN BOOLEAN DEFAULT FALSE
);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| pdb_name | VARCHAR2 | IN | Name of a pluggable database |
| clear_pending | BOOLEAN | IN | Flag indicating whether pending violations need to be cleaned up |

## Usage Notes

Syntax DBMS_PDB.CLEAR_PLUGIN_VIOLATIONS ( pdb_name IN VARCHAR2 DEFAULT NULL clear_pending IN BOOLEAN DEFAULT FALSE ); Parameters Table 124-3 CLEAR_PLUGIN_VIOLATIONS Procedure Parameters Parameter Description pdb_name Name of a pluggable database clear_pending Flag indicating whether pending violations need to be cleaned up Usage Notes When the pdb_name is not given Clear RESOLVED violations for all existing PDBs if clear_pending is either not set or set as FALSE . Clear RESOLVED and PENDING violations for all existing PDBs if clear_pending is set as TRUE . Clear RESOLVED and PENDING violations of PDBs that no longer exist. When the pdb_name name is given Clear RESOLVED violations of the given PDB if it exists and clear_pending is either not set or set as FALSE . Clear RESOLVED and PENDING violations for the given PDB if it exists and clear_pending is set as TRUE . Clear RESOLVED and PENDING violations of the given PDB if it does not exist and the procedure is called from CDB$ROOT . No error is raised if no violations found. Raise ORA-65011 if the given PDB does not exist, users cannot connect or alter the session to the PDB and the procedure cannot be called from the PDB. See Also: Oracle Database Administrator’s Guide for information about migrating an application to an application container. See Also: Oracle Database Administrator’s Guide for information about migrating an application to an application container.