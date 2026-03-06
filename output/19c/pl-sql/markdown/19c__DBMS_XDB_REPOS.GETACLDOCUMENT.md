---
id: 19c__DBMS_XDB_REPOS.GETACLDOCUMENT
name: DBMS_XDB_REPOS.GETACLDOCUMENT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_REPOS
tags: [dbms_xdb_repos]
source_file: DBMS_XDB_REPOS.html
---

# DBMS_XDB_REPOS.GETACLDOCUMENT

This function retrieves ACL document that protects resource given its path name.

## Syntax

```sql
DBMS_XDB_REPOS.GETACLDOCUMENT(
   abspath  IN  VARCHAR2)
  RETURN sys.xmltype;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| abspath | VARCHAR2) | IN | Path name of the resource whose ACL document is required |

**Returns:** `sys.xmltype`

## Usage Notes

Syntax DBMS_XDB_REPOS.GETACLDOCUMENT( abspath IN VARCHAR2) RETURN sys.xmltype; Parameters Table 198-14 GETACLDOCUMENT Function Parameters Parameter Description abspath Path name of the resource whose ACL document is required Return Values The XMLType for ACL document.