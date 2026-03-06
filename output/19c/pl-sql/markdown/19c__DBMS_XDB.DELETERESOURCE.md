---
id: 19c__DBMS_XDB.DELETERESOURCE
name: DBMS_XDB.DELETERESOURCE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB
tags: [dbms_xdb]
source_file: DBMS_XDB.html
---

# DBMS_XDB.DELETERESOURCE

This deprecated procedure deletes a resource from the hierarchy.

## Syntax

```sql
DBMS_XDB.DELETERESOURCE(
   path          IN      VARCHAR2,
   delete_option IN      PLS_INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| path | VARCHAR2 | IN | Path name of the resource to delete |
| delete_option | PLS_INTEGER) | IN | The option that controls how a a resource is deleted; defined in Table 194-1 : DELETE_RESOURCE DELETE_RECURSIVE DELETE_FORCE DELETE_RECURSIVE_FORCE |

## Usage Notes

Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the DELETERESOURCE Procedure . Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the DELETERESOURCE Procedure . Syntax DBMS_XDB.DELETERESOURCE( path IN VARCHAR2, delete_option IN PLS_INTEGER); Parameters Table 194-11 DELETERESOURCE Procedure Parameters Parameter Description path Path name of the resource to delete delete_option The option that controls how a a resource is deleted; defined in Table 194-1 : DELETE_RESOURCE DELETE_RECURSIVE DELETE_FORCE DELETE_RECURSIVE_FORCE