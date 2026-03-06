---
id: 19c__DBMS_XDB_VERSION.MAKEVERSIONED
name: DBMS_XDB_VERSION.MAKEVERSIONED
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_VERSION
tags: [dbms_xdb_version]
source_file: DBMS_XDB_VERSION.html
---

# DBMS_XDB_VERSION.MAKEVERSIONED

This function turns a regular resource whose path name is given into a version-controlled resource. This new resource is then put under version control. All other path names continue to refer to the original resource.

## Syntax

```sql
DBMS_XDB_VERSION.MAKEVERSIONED(
   pathname   VARCHAR2) 
 RETURN DBMS_XDB.resid_type;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| pathname | VARCHAR2) | IN | The path name of the resource to be put under version control. |

**Returns:** `DBMS_XDB.resid_type`

## Usage Notes

Syntax DBMS_XDB_VERSION.MAKEVERSIONED( pathname VARCHAR2) RETURN DBMS_XDB.resid_type; Parameters Table 199-12 MAKEVERSIONED Function Parameters Parameter Description pathname The path name of the resource to be put under version control. Return Values This function returns the resource ID of the first version, or root, of the VCR. Usage Notes If two or more path names are bound with the same resource, a copy of the resource is created, and the given path name is bound with the newly-created copy. This is not an auto-commit SQL operation. An exception is raised if the resource doesn't exist. This call is legal for VCR, and neither exception nor warning is raised. This call is illegal for folder, version history, version resource, and ACL. No support for Schema-based resources is provided.