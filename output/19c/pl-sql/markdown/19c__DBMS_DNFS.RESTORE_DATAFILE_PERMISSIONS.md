---
id: 19c__DBMS_DNFS.RESTORE_DATAFILE_PERMISSIONS
name: DBMS_DNFS.RESTORE_DATAFILE_PERMISSIONS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DNFS
tags: [dbms_dnfs]
source_file: DBMS_DNFS.html
---

# DBMS_DNFS.RESTORE_DATAFILE_PERMISSIONS

This procedure restores the file permissions for the data files belonging to the PDB to read write . PDB data files are converted to read only when one or more clones are created using this source PDB. This procedure must be invoked after the last clone is dropped to restore the data file permissions for the source PDB files.

## Syntax

```sql
DBMS_DNFS.RESTORE_DATAFILE_PERMISSIONS (
   pdb_name       IN         VARCHAR2  DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| pdb_name | VARCHAR2 | IN | Name of pluggable database whose file permissions need to be restored. |

## Usage Notes

Syntax DBMS_DNFS.RESTORE_DATAFILE_PERMISSIONS ( pdb_name IN VARCHAR2 DEFAULT NULL); Parameters Table 64-3 RESTORE_DATAFILE_PERMISSIONS Procedure Parameters Parameter Description pdb_name Name of pluggable database whose file permissions need to be restored.