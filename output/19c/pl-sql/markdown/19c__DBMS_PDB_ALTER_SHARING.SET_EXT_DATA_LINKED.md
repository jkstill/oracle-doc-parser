---
id: 19c__DBMS_PDB_ALTER_SHARING.SET_EXT_DATA_LINKED
name: DBMS_PDB_ALTER_SHARING.SET_EXT_DATA_LINKED
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PDB_ALTER_SHARING
tags: [dbms_pdb_alter_sharing]
source_file: DBMS_PDB_ALTER_SHARING.html
---

# DBMS_PDB_ALTER_SHARING.SET_EXT_DATA_LINKED

This procedure sets a database object to an extended data-linked application common object. In an application container, for an extended data-linked object, each application PDB can create its own specific data while sharing the common data in the application root. Therefore, only the data stored in the application root is common for all application PDBs.

## Syntax

```sql
DBMS_PDB_ALTER_SHARING.SET_EXT_DATA_LINKED (
   schema_name  IN VARCHAR2, 
   object_name  IN VARCHAR2, 
   namespace    IN NUMBER, 
   edition_name IN VARCHAR2  DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema_name | VARCHAR2 | IN | The name of the schema that owns the database object. |
| object_name | VARCHAR2 | IN | The name of the database object. |
| namespace | NUMBER | IN | The namespace of the database object. The NAMESPACE column of the DBA_OBJECTS view shows the namespace of an object. |
| edition_name | VARCHAR2 | IN | The name of the edition for the database object. |

## Usage Notes

You can use this procedure to set extended data-linked application common objects when you migrate an application that is installed in a PDB to an application container. The application can be migrated to the application root or to an application PDB. For example, you can migrate an application installed in a PDB plugged into an Oracle Database 12 c Release 1 (12.1) CDB to an application container in an Oracle Database 12 c Release 2 (12.2) CDB. Syntax DBMS_PDB_ALTER_SHARING.SET_EXT_DATA_LINKED ( schema_name IN VARCHAR2, object_name IN VARCHAR2, namespace IN NUMBER, edition_name IN VARCHAR2 DEFAULT NULL); Parameters Table 125-4 SET_EXT_DATA_LINKED Procedure Parameters Parameter Description schema_name The name of the schema that owns the database object. object_name The name of the database object. namespace The namespace of the database object. The NAMESPACE column of the DBA_OBJECTS view shows the namespace of an object. edition_name The name of the edition for the database object. See Also: Oracle Database Administrator’s Guide for information about migrating an application to an application container See Also: Oracle Database Administrator’s Guide for information about migrating an application to an application container