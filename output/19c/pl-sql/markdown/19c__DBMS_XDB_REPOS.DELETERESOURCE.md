---
id: 19c__DBMS_XDB_REPOS.DELETERESOURCE
name: DBMS_XDB_REPOS.DELETERESOURCE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_REPOS
tags: [dbms_xdb_repos]
source_file: DBMS_XDB_REPOS.html
---

# DBMS_XDB_REPOS.DELETERESOURCE

This procedure deletes a resource from the hierarchy.

## Syntax

```sql
DBMS_XDB_REPOS.DELETERESOURCE(
   path          IN      VARCHAR2,
   delete_option IN      PLS_INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| path | VARCHAR2 | IN | Path name of the resource to delete |
| delete_option | PLS_INTEGER) | IN | The option that controls how a a resource is deleted: DELETE_RESOURCE DELETE_RECURSIVE DELETE_FORCE DELETE_RECURSIVE_FORCE |

## Usage Notes

Syntax DBMS_XDB_REPOS.DELETERESOURCE( path IN VARCHAR2, delete_option IN PLS_INTEGER); Parameters Table 198-11 DELETERESOURCE Procedure Parameters Parameter Description path Path name of the resource to delete delete_option The option that controls how a a resource is deleted: DELETE_RESOURCE DELETE_RECURSIVE DELETE_FORCE DELETE_RECURSIVE_FORCE