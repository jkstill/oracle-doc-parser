---
id: 19c__DBMS_XDB_REPOS.PROCESSLINKS
name: DBMS_XDB_REPOS.PROCESSLINKS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_REPOS
tags: [dbms_xdb_repos]
source_file: DBMS_XDB_REPOS.html
---

# DBMS_XDB_REPOS.PROCESSLINKS

This procedure processes document links in the specified resource.

## Syntax

```sql
DBMS_XDB_REPOS.PURGERESOURCEMETADATA( 
 abspath  IN  VARCHAR2,
 recurse  IN  BOOLEAN := FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| abspath | VARCHAR2 | IN | Absolute path of the resource. If the path is a folder, use the recurse flag. |
| recurse | BOOLEAN | IN | Used only if abspath specifies a folder. If TRUE , process links of all resources in the folder hierarchy rooted at the specified resource. If FALSE , process links of all documents in this folder only. |

## Usage Notes

Syntax DBMS_XDB_REPOS.PURGERESOURCEMETADATA( abspath IN VARCHAR2, recurse IN BOOLEAN := FALSE); Parameters Table 198-30 PROCESSLINKS Procedure Parameters Parameter Description abspath Absolute path of the resource. If the path is a folder, use the recurse flag. recurse Used only if abspath specifies a folder. If TRUE , process links of all resources in the folder hierarchy rooted at the specified resource. If FALSE , process links of all documents in this folder only.