---
id: 19c__DBMS_XDB_VERSION.GETSUCCESSORS
name: DBMS_XDB_VERSION.GETSUCCESSORS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_VERSION
tags: [dbms_xdb_version]
source_file: DBMS_XDB_VERSION.html
---

# DBMS_XDB_VERSION.GETSUCCESSORS

Given a version resource or a VCR, this function retrieves the list of the successors of the resource by the path name.

## Syntax

```sql
DBMS_XDB_VERSION.GETSUCCESSORS( 
   pathname VARCHAR2) 
 RETURN resid_list_type;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| pathname | VARCHAR2) | IN | The path name of the resource. |

**Returns:** `resid_list_type`

## Usage Notes

Syntax DBMS_XDB_VERSION.GETSUCCESSORS( pathname VARCHAR2) RETURN resid_list_type; Parameters Table 199-10 GETSUCCESSORS Function Parameters Parameter Description pathname The path name of the resource. Usage Notes Getting successors by RESID is more efficient than by pathname . Exceptions An exception is raised if the pathname is illegal.