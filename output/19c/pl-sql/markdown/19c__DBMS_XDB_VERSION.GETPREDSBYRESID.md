---
id: 19c__DBMS_XDB_VERSION.GETPREDSBYRESID
name: DBMS_XDB_VERSION.GETPREDSBYRESID
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_VERSION
tags: [dbms_xdb_version]
source_file: DBMS_XDB_VERSION.html
---

# DBMS_XDB_VERSION.GETPREDSBYRESID

This function retrieves the list of predecessors by resource id.

## Syntax

```sql
DBMS_XDB_VERSION.GETPREDSBYRESID(
   resid      resid_type) 
 RETURN resid_list_type;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| resid | resid_type) | IN | The resource id. |

**Returns:** `resid_list_type`

## Usage Notes

Syntax DBMS_XDB_VERSION.GETPREDSBYRESID( resid resid_type) RETURN resid_list_type; Parameters Table 199-8 GETPREDSBYRESID Function Parameters Parameter Description resid The resource id. Usage Notes Getting predecessors by RESID is more efficient than by pathname . Exceptions An exception is raised if the RESID is illegal.