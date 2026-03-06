---
id: 19c__DBMS_XDB_VERSION.GETRESOURCEBYRESID
name: DBMS_XDB_VERSION.GETRESOURCEBYRESID
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_VERSION
tags: [dbms_xdb_version]
source_file: DBMS_XDB_VERSION.html
---

# DBMS_XDB_VERSION.GETRESOURCEBYRESID

This function obtains the resource as an XMLType , given the resource object ID. Because the system does not create a path name for versions, this function is useful for retrieving the resource using its resource id.

## Syntax

```sql
DBMS_XDB_VERSION.GETRESOURCEBYRESID(
   resid      resid_type) 
 RETURN XMLType;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| resid | resid_type) | IN | The resource id. |

**Returns:** `XMLType`

## Usage Notes

Syntax DBMS_XDB_VERSION.GETRESOURCEBYRESID( resid resid_type) RETURN XMLType; Parameters Table 199-9 GETRESOURCEBYRESID Function Parameters Parameter Description resid The resource id.