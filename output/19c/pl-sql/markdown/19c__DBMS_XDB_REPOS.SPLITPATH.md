---
id: 19c__DBMS_XDB_REPOS.SPLITPATH
name: DBMS_XDB_REPOS.SPLITPATH
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_REPOS
tags: [dbms_xdb_repos]
source_file: DBMS_XDB_REPOS.html
---

# DBMS_XDB_REPOS.SPLITPATH

This procedure splits the path into a parentpath and childpath.

## Syntax

```sql
DBMS_XDB_REPOS.SPLITPATH(
      abspath     IN  VARCHAR2,
      parentpath  OUT VARCHAR2,
     childpath    OUT VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| abspath | VARCHAR2 | IN | Absolute path to be split |
| parentpath | VARCHAR2 | OUT | Parentpath |
| childpath | VARCHAR2) | OUT | Childpath |

## Usage Notes

Syntax DBMS_XDB_REPOS.SPLITPATH( abspath IN VARCHAR2, parentpath OUT VARCHAR2, childpath OUT VARCHAR2); Parameters Table 198-34 SPLITPATH Procedure Parameters Parameter Description abspath Absolute path to be split parentpath Parentpath childpath Childpath