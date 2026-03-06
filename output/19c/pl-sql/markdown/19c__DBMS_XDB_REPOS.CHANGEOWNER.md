---
id: 19c__DBMS_XDB_REPOS.CHANGEOWNER
name: DBMS_XDB_REPOS.CHANGEOWNER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_REPOS
tags: [dbms_xdb_repos]
source_file: DBMS_XDB_REPOS.html
---

# DBMS_XDB_REPOS.CHANGEOWNER

This procedure changes the owner of the resource/s to the specified owner.

## Syntax

```sql
DBMS_XDB_REPOS.CHANGEOWNER(
     abspath    IN   VARCHAR2,
     owner      IN   VARCHAR2,
     recurse    IN   BOOLEAN := FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| abspath | VARCHAR2 | IN | Absolute path of the resource |
| owner | VARCHAR2 | IN | New owner for the resource |
| recurse | BOOLEAN | IN | If TRUE , recursively change owner of all resources in the folder tree |

## Usage Notes

Syntax DBMS_XDB_REPOS.CHANGEOWNER( abspath IN VARCHAR2, owner IN VARCHAR2, recurse IN BOOLEAN := FALSE); Parameters Table 198-5 CHANGEOWNER Procedure Parameters Parameter Description abspath Absolute path of the resource owner New owner for the resource recurse If TRUE , recursively change owner of all resources in the folder tree