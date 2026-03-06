---
id: 19c__DBMS_PDB.RECOVER
name: DBMS_PDB.RECOVER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PDB
tags: [dbms_pdb]
source_file: DBMS_PDB.html
---

# DBMS_PDB.RECOVER

This procedure generates an XML file describing a pluggable database by using data files belonging to the pluggable database. This XML file can then be used to plug the pluggable database into a multitenant container database (CDB) using the CREATE PLUGGABLE DATABASE statement.

## Syntax

```sql
DBMS_PDB.RECOVER (
   pdb_descr_file    IN   VARCHAR2, 
   pdb_name          IN   VARCHAR2,
   filenames         IN   VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| pdb_descr_file | VARCHAR2 | IN | Path of the XML file that contains description of a pluggable database |
| pdb_name | VARCHAR2 | IN | Name of a pluggable database |
| filenames | VARCHAR2) | IN | Comma-separated list of datafile paths and/or directories containing datafiles for the pluggable database |

## Usage Notes

Use this procedure when an XML file describing a pluggable database is corrupted or lost. Syntax DBMS_PDB.RECOVER ( pdb_descr_file IN VARCHAR2, pdb_name IN VARCHAR2, filenames IN VARCHAR2); Parameters Table 124-6 RECOVER Procedure Parameters Parameter Description pdb_descr_file Path of the XML file that contains description of a pluggable database pdb_name Name of a pluggable database filenames Comma-separated list of datafile paths and/or directories containing datafiles for the pluggable database