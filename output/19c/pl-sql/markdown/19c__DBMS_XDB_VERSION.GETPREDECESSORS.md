---
id: 19c__DBMS_XDB_VERSION.GETPREDECESSORS
name: DBMS_XDB_VERSION.GETPREDECESSORS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_VERSION
tags: [dbms_xdb_version]
source_file: DBMS_XDB_VERSION.html
---

# DBMS_XDB_VERSION.GETPREDECESSORS

This function retrieves the list of predecessors by the path name.

## Syntax

```sql
DBMS_XDB_VERSION.GETPREDECESSORS(
   pathname       VARCHAR2) 
 RETURN resid_list_type;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| pathname | VARCHAR2) | IN | The path name of the resource. |

**Returns:** `resid_list_type`

## Usage Notes

Syntax DBMS_XDB_VERSION.GETPREDECESSORS( pathname VARCHAR2) RETURN resid_list_type; Parameters Table 199-7 GETPREDECESSORS Function Parameters Parameter Description pathname The path name of the resource. Return Values An exception is raised if pathname is illegal.