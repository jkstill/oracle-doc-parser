---
id: 19c__DBMS_XDB_REPOS.GETCONTENTCLOB
name: DBMS_XDB_REPOS.GETCONTENTCLOB
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_REPOS
tags: [dbms_xdb_repos]
source_file: DBMS_XDB_REPOS.html
---

# DBMS_XDB_REPOS.GETCONTENTCLOB

This function gets the contents of a resource returned as a CLOB .

## Syntax

```sql
DBMS_XDB_REPOS.GETCONTENTCLOB(
     abspath    IN     VARCHAR2,
  RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| abspath | VARCHAR2 | IN | Absolute path of the resource |

**Returns:** `CLOB`

## Usage Notes

Syntax DBMS_XDB_REPOS.GETCONTENTCLOB( abspath IN VARCHAR2, RETURN CLOB; Parameters Table 198-16 GETCONTENTCLOB Function Parameters Parameter Description abspath Absolute path of the resource Return Values The contents of the resource as a CLOB.