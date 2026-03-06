---
id: 19c__DBMS_DBFS_HS.DROPSTORE
name: DBMS_DBFS_HS.DROPSTORE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_HS
tags: [dbms_dbfs_hs]
source_file: DBMS_DBFS_HS.html
---

# DBMS_DBFS_HS.DROPSTORE

This procedure deletes a previously created hierarchical store specified by name and owned by the invoking session user.

## Syntax

```sql
DBMS_DBFS_HS.DROPSTORE  (
   store_name   IN     VARCHAR2,
   opt_flags    IN     INTEGER DEFAULT 0);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2 | IN | Name of store owned by the invoking session user |
| opt_flags | INTEGER | IN | User can specify optional flags. If DISABLE_CLEANUPBACKUPFILES is specified as one of the optional flags, the call to the CLEANUPUNUSEDBACKUPFILES Procedure is not issued. By default, when this flag is not set, the procedure implicitly cleans-up all unused backup files. |

## Usage Notes

Syntax DBMS_DBFS_HS.DROPSTORE ( store_name IN VARCHAR2, opt_flags IN INTEGER DEFAULT 0); Parameters Table 54-10 DROPSTORE Procedure Parameters Parameter Description store_name Name of store owned by the invoking session user opt_flags User can specify optional flags. If DISABLE_CLEANUPBACKUPFILES is specified as one of the optional flags, the call to the CLEANUPUNUSEDBACKUPFILES Procedure is not issued. By default, when this flag is not set, the procedure implicitly cleans-up all unused backup files. Usage Notes The procedure executes like a DDL in that it auto-commits before and after its execution. If CLEANUPBACKUPFILES is disabled during the procedure, the user must resort to out-of-band techniques to cleanup unused backup files. No further invocations of CLEANUPBACKFILES for a dropped store are possible through hierarchical store. This subprogram will un-register the store from DBMS_DBFS_CONTENT package. All files in the given store are deleted from the store (Tape or Amazon S3 Web service). The database table holding the store's entries in the database, is also dropped by this subprogram.