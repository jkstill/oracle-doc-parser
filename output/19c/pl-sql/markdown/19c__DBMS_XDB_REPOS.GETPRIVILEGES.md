---
id: 19c__DBMS_XDB_REPOS.GETPRIVILEGES
name: DBMS_XDB_REPOS.GETPRIVILEGES
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_REPOS
tags: [dbms_xdb_repos]
source_file: DBMS_XDB_REPOS.html
---

# DBMS_XDB_REPOS.GETPRIVILEGES

This function gets all privileges granted to the current user on a specified resource.

## Syntax

```sql
DBMS_XDB_REPOS.GETPRIVILEGES(
   res_path    IN     VARCHAR2)
 RETURN sys.xmltype;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res_path | VARCHAR2) | IN | Absolute path in the hierarchy of the resource |

**Returns:** `sys.xmltype`

## Usage Notes

Syntax DBMS_XDB_REPOS.GETPRIVILEGES( res_path IN VARCHAR2) RETURN sys.xmltype; Parameters Table 198-21 GETPRIVILEGES Function Parameters Parameter Description res_path Absolute path in the hierarchy of the resource Return Values An XMLType instance of <privilege> element, which contains the list of all leaf privileges granted on this resource to the current user.