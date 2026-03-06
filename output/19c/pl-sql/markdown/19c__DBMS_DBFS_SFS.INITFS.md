---
id: 19c__DBMS_DBFS_SFS.INITFS
name: DBMS_DBFS_SFS.INITFS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_SFS
tags: [dbms_dbfs_sfs]
source_file: DBMS_DBFS_SFS.html
---

# DBMS_DBFS_SFS.INITFS

This procedure initialize a POSIX file system store. The table associated with the POSIX file system store store_name is truncated and reinitialized with a single "root" directory entry.

## Syntax

```sql
DBMS_DBFS_SFS.INITFS (
   store_name     IN      VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2) | IN | Name of store |

## Usage Notes

Syntax DBMS_DBFS_SFS.INITFS ( store_name IN VARCHAR2); Parameters Table 55-9 INITFS Procedure Parameters Parameter Description store_name Name of store Usage Notes The procedure executes like a DDL in that it auto-commits before and after its execution.