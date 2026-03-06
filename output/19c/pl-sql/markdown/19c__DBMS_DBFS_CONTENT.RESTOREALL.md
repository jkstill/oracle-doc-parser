---
id: 19c__DBMS_DBFS_CONTENT.RESTOREALL
name: DBMS_DBFS_CONTENT.RESTOREALL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.RESTOREALL

This procedure restores all soft-deleted path items meeting the path and optional filter criteria.

## Syntax

```sql
DBMS_DBFS_CONTENT.RESTOREALL (
   path           IN      VARCHAR2,
   filter         IN      VARCHAR2    DEFAULT NULL,
   store_name     IN      VARCHAR2    DEFAULT NULL,
   principal      IN      VARCHAR2    DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| path | VARCHAR2 | IN | Name of path to file items |
| filter | VARCHAR2 | IN | A filter, if any, to be applied |
| store_name | VARCHAR2 | IN | Name of store |
| principal | VARCHAR2 | IN | Agent (principal) invoking the current operation |

## Usage Notes

Syntax DBMS_DBFS_CONTENT.RESTOREALL ( path IN VARCHAR2, filter IN VARCHAR2 DEFAULT NULL, store_name IN VARCHAR2 DEFAULT NULL, principal IN VARCHAR2 DEFAULT NULL); Parameters Table 52-64 RESTOREALL Procedure Parameters Parameter Description path Name of path to file items filter A filter, if any, to be applied store_name Name of store principal Agent (principal) invoking the current operation