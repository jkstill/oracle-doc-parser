---
id: 19c__DBMS_XDB_REPOS.CREATEFOLDER
name: DBMS_XDB_REPOS.CREATEFOLDER
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_REPOS
tags: [dbms_xdb_repos]
source_file: DBMS_XDB_REPOS.html
---

# DBMS_XDB_REPOS.CREATEFOLDER

This function creates a new folder resource in the hierarchy.

## Syntax

```sql
DBMS_XDB_REPOS.CREATEFOLDER(
   path   IN  VARCHAR2)
 RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| path | VARCHAR2) | IN | Path name for the new folder |

**Returns:** `BOOLEAN`

## Usage Notes

Syntax DBMS_XDB_REPOS.CREATEFOLDER( path IN VARCHAR2) RETURN BOOLEAN; Parameters Table 198-8 CREATEFOLDER Function Parameters Parameter Description path Path name for the new folder Return Values TRUE if operation successful; FALSE , otherwise. Usage Notes The given path name's parent folder must already exist in the hierarchy: if '/folder1/folder2' is passed as the path parameter, then '/folder1' must already exist.