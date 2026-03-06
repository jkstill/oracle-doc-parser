---
id: 19c__DBMS_XDB_REPOS.PURGERESOURCEMETADATA
name: DBMS_XDB_REPOS.PURGERESOURCEMETADATA
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_REPOS
tags: [dbms_xdb_repos]
source_file: DBMS_XDB_REPOS.html
---

# DBMS_XDB_REPOS.PURGERESOURCEMETADATA

This procedure deletes all user metadata from a resource. Schema-based metadata is removed in cascade mode, rows being deleted from the corresponding metadata tables.

## Syntax

```sql
DBMS_XDB_REPOS.PURGERESOURCEMETADATA(  
 abspath  IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| abspath | VARCHAR2) | IN | Absolute path of the resource |

## Usage Notes

Syntax DBMS_XDB_REPOS.PURGERESOURCEMETADATA( abspath IN VARCHAR2); Parameters Table 198-31 PURGERESOURCEMETADATA Procedure Parameters Parameter Description abspath Absolute path of the resource