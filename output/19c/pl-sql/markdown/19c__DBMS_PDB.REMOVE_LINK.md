---
id: 19c__DBMS_PDB.REMOVE_LINK
name: DBMS_PDB.REMOVE_LINK
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PDB
tags: [dbms_pdb]
source_file: DBMS_PDB.html
---

# DBMS_PDB.REMOVE_LINK

This procedure specifies that a database object is not an application common object. In an application container, application common objects are shared between multiple containers.

## Syntax

```sql
DBMS_PDB.REMOVE_LINK (
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

Syntax DBMS_PDB.REMOVE_LINK ( schema_name IN VARCHAR2, object_name IN VARCHAR2, namespace IN NUMBER, edition_name IN VARCHAR2 DEFAULT NULL); Parameters Table 124-7 REMOVE_LINK Procedure Parameters Parameter Description schema_name The name of the schema that owns the database object. object_name The name of the database object. namespace The namespace of the database object. The NAMESPACE column of the DBA_OBJECTS view shows the namespace of an object. edition_name The name of the edition for the database object. See Also: Oracle Database Administrator’s Guide for information about migrating an application to an application container See Also: Oracle Database Administrator’s Guide for information about migrating an application to an application container