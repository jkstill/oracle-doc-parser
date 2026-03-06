---
id: 19c__DBMS_XDB.GETLOCKTOKEN
name: DBMS_XDB.GETLOCKTOKEN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB
tags: [dbms_xdb]
source_file: DBMS_XDB.html
---

# DBMS_XDB.GETLOCKTOKEN

Given a path to a resource, this deprecated procedure returns that resource's lock token for the current user.

## Syntax

```sql
DBMS_XDB.GETLOCKTOKEN(
   path         IN      VARCHAR2,
   locktoken    OUT     VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| path | VARCHAR2 | IN | Path name to the resource |
| locktoken | VARCHAR2) | OUT | Logged-in user's lock token for the resource |

## Usage Notes

Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the GETLOCKTOKEN Procedure . Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the GETLOCKTOKEN Procedure . Syntax DBMS_XDB.GETLOCKTOKEN( path IN VARCHAR2, locktoken OUT VARCHAR2); Parameters Table 194-21 GETLOCKTOKEN Procedure Parameters Parameter Description path Path name to the resource locktoken Logged-in user's lock token for the resource Usage Notes The user must have READPROPERTIES privilege on the resource.