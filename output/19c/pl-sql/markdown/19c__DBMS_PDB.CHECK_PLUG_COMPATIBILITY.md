---
id: 19c__DBMS_PDB.CHECK_PLUG_COMPATIBILITY
name: DBMS_PDB.CHECK_PLUG_COMPATIBILITY
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PDB
tags: [dbms_pdb]
source_file: DBMS_PDB.html
---

# DBMS_PDB.CHECK_PLUG_COMPATIBILITY

This function uses an XML file describing a pluggable database (PDB) to determine whether it may be plugged into a given multitenant container database (CDB).

## Syntax

```sql
DBMS_PDB.CHECK_PLUG_COMPATIBILITY (
   pdb_descr_file    IN   VARCHAR2, 
   pdb_name          IN   VARCHAR2 DEFAULT NULL) 
 RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| pdb_descr_file | VARCHAR2 | IN | Path of the XML file that will contain description of a PDB |
| pdb_name | VARCHAR2 | IN | Name which will be given to the PDB represented by pdb_descr_file when plugged into a given CDB. If not specified, the name will be extracted from pdb_descr_file . |

**Returns:** `BOOLEAN`

## Usage Notes

Syntax DBMS_PDB.CHECK_PLUG_COMPATIBILITY ( pdb_descr_file IN VARCHAR2, pdb_name IN VARCHAR2 DEFAULT NULL) RETURN BOOLEAN; Parameters Table 124-2 CHECK_PLUG_COMPATIBILITY Procedure Parameters Parameter Description pdb_descr_file Path of the XML file that will contain description of a PDB pdb_name Name which will be given to the PDB represented by pdb_descr_file when plugged into a given CDB. If not specified, the name will be extracted from pdb_descr_file . Return Values TRUE if the PDB described by pdb_descr_file is compatible with the given CDB, FALSE otherwise. If this function returns FALSE , then query the PDB_PLUG_IN_VIOLATIONS data dictionary view to find information about the errors that are found. See Also: Oracle Database Reference for information about the PDB_PLUG_IN_VIOLATIONS view See Also: Oracle Database Reference for information about the PDB_PLUG_IN_VIOLATIONS view