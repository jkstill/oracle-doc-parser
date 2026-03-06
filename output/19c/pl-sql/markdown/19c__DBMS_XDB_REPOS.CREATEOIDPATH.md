---
id: 19c__DBMS_XDB_REPOS.CREATEOIDPATH
name: DBMS_XDB_REPOS.CREATEOIDPATH
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_REPOS
tags: [dbms_xdb_repos]
source_file: DBMS_XDB_REPOS.html
---

# DBMS_XDB_REPOS.CREATEOIDPATH

This function creates a virtual path to the resource based on object ID.

## Syntax

```sql
DBMS_XDB_REPOS.CREATEOIDPATH(
   oid    IN   RAW)
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| oid | RAW) | IN | Object ID of the resource |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_XDB_REPOS.CREATEOIDPATH( oid IN RAW) RETURN VARCHAR2; Parameters Table 198-9 CREATEOIDPATH Function Parameters Parameter Description oid Object ID of the resource