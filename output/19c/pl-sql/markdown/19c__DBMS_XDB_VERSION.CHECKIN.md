---
id: 19c__DBMS_XDB_VERSION.CHECKIN
name: DBMS_XDB_VERSION.CHECKIN
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_VERSION
tags: [dbms_xdb_version]
source_file: DBMS_XDB_VERSION.html
---

# DBMS_XDB_VERSION.CHECKIN

This function checks in a checked-out VCR and returns the resource id of the newly-created version.

## Syntax

```sql
DBMS_XDB_VERSION.CHECKIN(
   pathname VARCHAR2) 
 RETURN DBMS_XDB.resid_type;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| pathname | VARCHAR2) | IN | The path name of the checked-out resource. |

**Returns:** `DBMS_XDB.resid_type`

## Usage Notes

Syntax DBMS_XDB_VERSION.CHECKIN( pathname VARCHAR2) RETURN DBMS_XDB.resid_type; Parameters Table 199-2 CHECKIN Function Parameters Parameter Description pathname The path name of the checked-out resource. Usage Notes This is not an auto-commit SQL operation. CHECKIN Function doesn't have to take the same path name that was passed to CHECKOUT Procedure operation. However, the CHECKIN Function path name and the CHECKOUT Procedure path name must be of the same resource for the operations to function correctly. If the resource has been renamed, the new name must be used to CHECKIN Function because the old name is either invalid or is currently bound with a different resource. Exception is raised if the path name does not exist. If the path name has been changed, the new path name must be used to CHECKIN Function the resource.