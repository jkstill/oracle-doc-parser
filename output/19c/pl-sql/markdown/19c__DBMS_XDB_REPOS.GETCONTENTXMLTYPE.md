---
id: 19c__DBMS_XDB_REPOS.GETCONTENTXMLTYPE
name: DBMS_XDB_REPOS.GETCONTENTXMLTYPE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_REPOS
tags: [dbms_xdb_repos]
source_file: DBMS_XDB_REPOS.html
---

# DBMS_XDB_REPOS.GETCONTENTXMLTYPE

This function retrieves the contents of a resource returned as an XMLTYPE .

## Syntax

```sql
DBMS_XDB_REPOS.GETCONTENTXMLTYPE(
     abspath    IN     VARCHAR2,
  RETURN SYS.XMLTYPE;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| abspath | VARCHAR2 | IN | Absolute path of the resource |

**Returns:** `SYS.XMLTYPE`

## Usage Notes

Syntax DBMS_XDB_REPOS.GETCONTENTXMLTYPE( abspath IN VARCHAR2, RETURN SYS.XMLTYPE; Parameters Table 198-19 GETCONTENTXMLTYPE Function Parameters Parameter Description abspath Absolute path of the resource Return Values The contents of the resource as an XMLTYPE.