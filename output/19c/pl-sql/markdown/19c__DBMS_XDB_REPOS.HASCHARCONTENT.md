---
id: 19c__DBMS_XDB_REPOS.HASCHARCONTENT
name: DBMS_XDB_REPOS.HASCHARCONTENT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_REPOS
tags: [dbms_xdb_repos]
source_file: DBMS_XDB_REPOS.html
---

# DBMS_XDB_REPOS.HASCHARCONTENT

This function returns TRUE if the resource has character content.

## Syntax

```sql
DBMS_XDB_REPOS.HASCHARCONTENT 
     abspath    IN     VARCHAR2)
 RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| abspath_path |  |  | Absolute path of the resource |

**Returns:** `BOOLEAN`

## Usage Notes

Syntax DBMS_XDB_REPOS.HASCHARCONTENT abspath IN VARCHAR2) RETURN BOOLEAN; Parameters Table 198-24 HASCHARCONTENT Function Parameters Parameter Description abspath_path Absolute path of the resource Return Values TRUE if the resource has character content.