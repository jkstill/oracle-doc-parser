---
id: 19c__DBMS_XDB_REPOS.EXISTSRESOURCE
name: DBMS_XDB_REPOS.EXISTSRESOURCE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_REPOS
tags: [dbms_xdb_repos]
source_file: DBMS_XDB_REPOS.html
---

# DBMS_XDB_REPOS.EXISTSRESOURCE

This function indicates if a resource is in the hierarchy. It matches the resource by a string that represents its absolute path.

## Syntax

```sql
DBMS_XDB_REPOS.EXISTSRESOURCE(
   abspath    IN    VARCHAR2)
 RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| abspath | VARCHAR2) | IN | Path name of the resource whose ACL document is required |

**Returns:** `BOOLEAN`

## Usage Notes

Syntax DBMS_XDB_REPOS.EXISTSRESOURCE( abspath IN VARCHAR2) RETURN BOOLEAN; Parameters Table 198-13 EXISTSRESOURCE Function Parameters Parameter Description abspath Path name of the resource whose ACL document is required Return Values TRUE if the resource is found.