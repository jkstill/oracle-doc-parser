---
id: 19c__DBMS_XDB_REPOS.UNLOCKRESOURCE
name: DBMS_XDB_REPOS.UNLOCKRESOURCE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_REPOS
tags: [dbms_xdb_repos]
source_file: DBMS_XDB_REPOS.html
---

# DBMS_XDB_REPOS.UNLOCKRESOURCE

This function unlocks the resource given a lock token and a path to the resource.

## Syntax

```sql
DBMS_XDB_REPOS.UNLOCKRESOURCE(
   path     IN  VARCHAR2,
   deltoken IN  VARCHAR2)
 RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| path | VARCHAR2 | IN | Path name to the resource |
| deltoken | VARCHAR2) | IN | Lock token to be removed |

**Returns:** `BOOLEAN`

## Usage Notes

Syntax DBMS_XDB_REPOS.UNLOCKRESOURCE( path IN VARCHAR2, deltoken IN VARCHAR2) RETURN BOOLEAN; Parameters Table 198-36 UNLOCKRESOURCE Function Parameters Parameter Description path Path name to the resource deltoken Lock token to be removed Return Values TRUE if operation successful. Usage Notes The user must have UPDATE privileges on the resource.