---
id: 19c__DBMS_XDB_VERSION.GETCONTENTSXMLBYRESID
name: DBMS_XDB_VERSION.GETCONTENTSXMLBYRESID
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_VERSION
tags: [dbms_xdb_version]
source_file: DBMS_XDB_VERSION.html
---

# DBMS_XDB_VERSION.GETCONTENTSXMLBYRESID

This function obtains contents as an XMLType .

## Syntax

```sql
DBMS_XDB_VERSION.GETCONTENTSXMLBYRESID(
   resid      DBMS_XDB.resid_type)
 RETURN XMLType;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| resid | DBMS_XDB.resid_type) | IN | The resource id. |

**Returns:** `XMLType`

## Usage Notes

Syntax DBMS_XDB_VERSION.GETCONTENTSXMLBYRESID( resid DBMS_XDB.resid_type) RETURN XMLType; Parameters Table 199-6 GETCONTENTSXMLBYRESID Function Parameters Parameter Description resid The resource id. Return Values If the contents are not valid XML, returns NULL .