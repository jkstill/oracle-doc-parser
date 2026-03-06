---
id: 19c__DBMS_XDB_REPOS.GETLOCKTOKEN
name: DBMS_XDB_REPOS.GETLOCKTOKEN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_REPOS
tags: [dbms_xdb_repos]
source_file: DBMS_XDB_REPOS.html
---

# DBMS_XDB_REPOS.GETLOCKTOKEN

Given a path to a resource, this procedure returns that resource's lock token for the current user.

## Syntax

```sql
DBMS_XDB_REPOS.GETLOCKTOKEN(
   path         IN      VARCHAR2,
   locktoken    OUT     VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| path | VARCHAR2 | IN | Path name to the resource |
| locktoken | VARCHAR2) | OUT | Logged-in user's lock token for the resource |

## Usage Notes

Syntax DBMS_XDB_REPOS.GETLOCKTOKEN( path IN VARCHAR2, locktoken OUT VARCHAR2); Parameters Table 198-20 GETLOCKTOKEN Procedure Parameters Parameter Description path Path name to the resource locktoken Logged-in user's lock token for the resource Usage Notes The user must have READPROPERTIES privilege on the resource.