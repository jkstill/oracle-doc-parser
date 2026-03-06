---
id: 19c__DBMS_XDB_REPOS.RENAMERESOURCE
name: DBMS_XDB_REPOS.RENAMERESOURCE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_REPOS
tags: [dbms_xdb_repos]
source_file: DBMS_XDB_REPOS.html
---

# DBMS_XDB_REPOS.RENAMERESOURCE

This procedure renames the XDB resource.

## Syntax

```sql
DBMS_XDB_REPOS.RENAMERESOURCE(
   srcpath    IN  VARCHAR2,
   destfolder IN  CARCHAR2,
   newname    IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| srcpath | VARCHAR2 | IN | Absolute path in the Hierarchy for the source resource destination folder |
| destfolder | CARCHAR2 | IN | Absolute path in the Hierarchy for the destination folder |
| newname | VARCHAR2) | IN | Name of the child in the destination folder |

## Usage Notes

Syntax DBMS_XDB_REPOS.RENAMERESOURCE( srcpath IN VARCHAR2, destfolder IN CARCHAR2, newname IN VARCHAR2); Parameters Table 198-32 RENAMERESOURCE Procedure Parameters Parameter Description srcpath Absolute path in the Hierarchy for the source resource destination folder destfolder Absolute path in the Hierarchy for the destination folder newname Name of the child in the destination folder