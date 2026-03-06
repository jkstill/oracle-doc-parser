---
id: 19c__DBMS_DBFS_SFS.DROPFILESYSTEM
name: DBMS_DBFS_SFS.DROPFILESYSTEM
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_SFS
tags: [dbms_dbfs_sfs]
source_file: DBMS_DBFS_SFS.html
---

# DBMS_DBFS_SFS.DROPFILESYSTEM

This procedure drops the DBFS SFS store, purging all dictionary information associated with the store, and dropping the underlying file system table.

## Syntax

```sql
DBMS_DBFS_SFS.DROPFILESYSTEM  (
   schema_name    IN      VARCHAR2 DEFAULT NULL,
   tbl_name       IN      INTEGER);

DBMS_DBFS_SFS.DROPFILESYSTEM  (
   store_name     IN      VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema_name | VARCHAR2 | IN | Name of schema |
| tbl_name | INTEGER) | IN | Name of tablespace |
| store_name | VARCHAR2) | IN | Name of store path |

## Usage Notes

Syntax DBMS_DBFS_SFS.DROPFILESYSTEM ( schema_name IN VARCHAR2 DEFAULT NULL, tbl_name IN INTEGER); DBMS_DBFS_SFS.DROPFILESYSTEM ( store_name IN VARCHAR2); Parameters Table 55-8 DROPFILESYSTEM Procedure Parameters Parameter Description schema_name Name of schema tbl_name Name of tablespace store_name Name of store path Usage Notes If the specified store table is registered by the current user, it will be unregistered from the content interface described in the DBMS_DBFS_CONTENT package and the POSIX metadata tables. Subsequent to unregistration, an attempt will be made to store table(s). This operation may fail if other users are currently using this store table. The user attempting a drop of the tables underlying the store must actually have the privileges to complete the drop operation (either as the owner of the tables, or as a sufficiently privileged user for cross-schema operations). The procedure executes like a DDL in that it auto-commits before and after its execution.