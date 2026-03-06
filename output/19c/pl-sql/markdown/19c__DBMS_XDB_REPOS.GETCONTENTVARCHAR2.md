---
id: 19c__DBMS_XDB_REPOS.GETCONTENTVARCHAR2
name: DBMS_XDB_REPOS.GETCONTENTVARCHAR2
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_REPOS
tags: [dbms_xdb_repos]
source_file: DBMS_XDB_REPOS.html
---

# DBMS_XDB_REPOS.GETCONTENTVARCHAR2

This function gets the contents of a resource returned as a string.

## Syntax

```sql
DBMS_XDB_REPOS.GETCONTENTVARCHAR2(
     abspath    IN     VARCHAR2,
  RETURN BLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| abspath | VARCHAR2 | IN | Absolute path of the resource |

**Returns:** `BLOB`

## Usage Notes

Syntax DBMS_XDB_REPOS.GETCONTENTVARCHAR2( abspath IN VARCHAR2, RETURN BLOB; Parameters Table 198-17 GETCONTENTVARCHAR2 Function Parameters Parameter Description abspath Absolute path of the resource Return Values The contents of the resource as a string.