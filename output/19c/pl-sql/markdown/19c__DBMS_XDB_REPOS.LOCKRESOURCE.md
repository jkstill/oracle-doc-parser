---
id: 19c__DBMS_XDB_REPOS.LOCKRESOURCE
name: DBMS_XDB_REPOS.LOCKRESOURCE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_REPOS
tags: [dbms_xdb_repos]
source_file: DBMS_XDB_REPOS.html
---

# DBMS_XDB_REPOS.LOCKRESOURCE

Given a path to a resource, this function gets a WebDAV-style lock on that resource.

## Syntax

```sql
DBMS_XDB_REPOS.LOCKRESOURCE(
   path      IN  VARCHAR2,
   depthzero IN  BOOLEAN,
   shared    IN  boolean)
RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| path | VARCHAR2 | IN | Path name of the resource to lock. |
| depthzero | BOOLEAN | IN | Currently not supported |
| shared | boolean) | IN | Passing TRUE obtains a shared write lock |

**Returns:** `BOOLEAN`

## Usage Notes

Syntax DBMS_XDB_REPOS.LOCKRESOURCE( path IN VARCHAR2, depthzero IN BOOLEAN, shared IN boolean) RETURN BOOLEAN; Parameters Table 198-29 LOCKRESOURCE Function Parameters Parameter Description path Path name of the resource to lock. depthzero Currently not supported shared Passing TRUE obtains a shared write lock Return Values TRUE if successful. Usage Notes The user must have UPDATE privileges on the resource.