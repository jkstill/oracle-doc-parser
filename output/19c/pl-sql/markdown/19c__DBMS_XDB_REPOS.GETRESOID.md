---
id: 19c__DBMS_XDB_REPOS.GETRESOID
name: DBMS_XDB_REPOS.GETRESOID
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_REPOS
tags: [dbms_xdb_repos]
source_file: DBMS_XDB_REPOS.html
---

# DBMS_XDB_REPOS.GETRESOID

The GETRESOID function returns the object ID of the resource from its absolute path.

## Syntax

```sql
DBMS_XDB_REPOS.GETRESOID(
   abspath IN VARCHAR2)
RETURN RAW;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| abspath_path |  |  | Absolute path of the resource |

**Returns:** `RAW`

## Usage Notes

Syntax DBMS_XDB_REPOS.GETRESOID( abspath IN VARCHAR2) RETURN RAW; Parameters Table 198-22 GETRESOID Function Parameters Parameter Description abspath_path Absolute path of the resource Return Values NULL if the resource is not present.