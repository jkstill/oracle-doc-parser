---
id: 19c__DBMS_PDB.DESCRIBE
name: DBMS_PDB.DESCRIBE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PDB
tags: [dbms_pdb]
source_file: DBMS_PDB.html
---

# DBMS_PDB.DESCRIBE

This procedure generates an XML file describing the specified pluggable database (PDB). This file can then be passed to the CHECK_PLUG_COMPATIBILITY Function to determine if the PDB described by the XML file may be plugged into a given multitenant container database (CDB).

## Syntax

```sql
DBMS_PDB.DESCRIBE (
   pdb_descr_file    IN   VARCHAR2, 
   pdb_name          IN   VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| pdb_descr_file | VARCHAR2 | IN | Path of the XML file that will contain description of a PDB |
| pdb_name | VARCHAR2 | IN | Name of a PDB to be described. A remote database is specified by including @dblink . |

## Usage Notes

Syntax DBMS_PDB.DESCRIBE ( pdb_descr_file IN VARCHAR2, pdb_name IN VARCHAR2 DEFAULT NULL); Parameters Table 124-4 DESCRIBE Procedure Parameters Parameter Description pdb_descr_file Path of the XML file that will contain description of a PDB pdb_name Name of a PDB to be described. A remote database is specified by including @dblink . Usage Notes If pdb_name is omitted, the PDB to which the session is connected will be described. If pdb_name is omitted, and the session is connected to the Root, an error will be returned.