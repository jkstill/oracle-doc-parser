---
id: 19c__DBMS_XDB_REPOS.TOUCHRESOURCE
name: DBMS_XDB_REPOS.TOUCHRESOURCE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_REPOS
tags: [dbms_xdb_repos]
source_file: DBMS_XDB_REPOS.html
---

# DBMS_XDB_REPOS.TOUCHRESOURCE

This procedure changes the modification time of the resource to the current time.

## Syntax

```sql
DBMS_XDB_REPOS.TOUCHRESOURCE 
     abspath    IN     VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| abspath_path |  |  | Absolute path of the resource |

## Usage Notes

Syntax DBMS_XDB_REPOS.TOUCHRESOURCE abspath IN VARCHAR2); Parameters Table 198-35 TOUCHRESOURCE Procedure Parameters Parameter Description abspath_path Absolute path of the resource