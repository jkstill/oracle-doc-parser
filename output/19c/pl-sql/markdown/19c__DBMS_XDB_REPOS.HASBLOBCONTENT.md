---
id: 19c__DBMS_XDB_REPOS.HASBLOBCONTENT
name: DBMS_XDB_REPOS.HASBLOBCONTENT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_REPOS
tags: [dbms_xdb_repos]
source_file: DBMS_XDB_REPOS.html
---

# DBMS_XDB_REPOS.HASBLOBCONTENT

This function returns TRUE if the resource has BLOB content.

## Syntax

```sql
DBMS_XDB_REPOS.HASBLOBCONTENT 
     abspath    IN     VARCHAR2)
 RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| abspath_path |  |  | Absolute path of the resource |

**Returns:** `BOOLEAN`

## Usage Notes

Syntax DBMS_XDB_REPOS.HASBLOBCONTENT abspath IN VARCHAR2) RETURN BOOLEAN; Parameters Table 198-23 HASBLOBCONTENT Function Parameters Parameter Description abspath_path Absolute path of the resource Return Values TRUE if the resource has BOB content.