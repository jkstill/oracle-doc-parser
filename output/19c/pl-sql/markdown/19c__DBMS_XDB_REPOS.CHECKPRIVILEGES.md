---
id: 19c__DBMS_XDB_REPOS.CHECKPRIVILEGES
name: DBMS_XDB_REPOS.CHECKPRIVILEGES
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_REPOS
tags: [dbms_xdb_repos]
source_file: DBMS_XDB_REPOS.html
---

# DBMS_XDB_REPOS.CHECKPRIVILEGES

This function checks access privileges granted to the current user on the specified resource.

## Syntax

```sql
DBMS_XDB_REPOS.CHECKPRIVILEGES(
   res_path   IN  VARCHAR2,
   privs      IN  xmltype)
 RETURN PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res_path | VARCHAR2 | IN | Absolute path in the Hierarchy for resource |
| privs | xmltype) | IN | An XMLType instance of the privilege element specifying the requested set of access privileges |

**Returns:** `PLS_INTEGER`

## Usage Notes

Syntax DBMS_XDB_REPOS.CHECKPRIVILEGES( res_path IN VARCHAR2, privs IN xmltype) RETURN PLS_INTEGER; Parameters Table 198-7 CHECKPRIVILEGES Function Parameters Parameter Description res_path Absolute path in the Hierarchy for resource privs An XMLType instance of the privilege element specifying the requested set of access privileges Return Values A positive integer if all requested privileges granted.