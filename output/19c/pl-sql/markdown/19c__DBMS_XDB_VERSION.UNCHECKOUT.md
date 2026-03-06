---
id: 19c__DBMS_XDB_VERSION.UNCHECKOUT
name: DBMS_XDB_VERSION.UNCHECKOUT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_VERSION
tags: [dbms_xdb_version]
source_file: DBMS_XDB_VERSION.html
---

# DBMS_XDB_VERSION.UNCHECKOUT

This function checks-in a checked-out resource and returns the resource id of the version before the resource is checked out.

## Syntax

```sql
DBMS_XDB_VERSION.UNCHECKOUT(
   pathname    VARCHAR2) 
 RETURN DBMS_XDB.resid_type;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| pathname | VARCHAR2) | IN | The path name of the checked-out resource. |

**Returns:** `DBMS_XDB.resid_type`

## Usage Notes

Syntax DBMS_XDB_VERSION.UNCHECKOUT( pathname VARCHAR2) RETURN DBMS_XDB.resid_type; Parameters Table 199-13 UNCHECKOUT Function Parameters Parameter Description pathname The path name of the checked-out resource. Usage Notes This is not an auto-commit SQL operation. The UNCHECKOUT Function does not have to take the same path name that was passed to the operation by the CHECKOUT Procedure . However, the UNCHECKOUT Function path name and the CHECKOUT Procedure path name must be of the same resource for the operations to function correctly. If the resource has been renamed, the new name must be used to UNCHECKOUT Function , because the old name is either invalid or is currently bound with a different resource. If the path name has been changed, the new path name must be used to UNCHECKOUT Function the resource. Exceptions An exception is raised if the path name doesn't exist.