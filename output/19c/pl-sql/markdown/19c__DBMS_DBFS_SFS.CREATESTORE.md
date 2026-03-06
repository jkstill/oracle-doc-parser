---
id: 19c__DBMS_DBFS_SFS.CREATESTORE
name: DBMS_DBFS_SFS.CREATESTORE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_SFS
tags: [dbms_dbfs_sfs]
source_file: DBMS_DBFS_SFS.html
---

# DBMS_DBFS_SFS.CREATESTORE

This procedure creates a new DBFS SFS store owned by the invoking session user.

## Syntax

```sql
DBMS_DBFS_SFS.CREATESTORE  (
   store_name     IN     VARCHAR2,
   tbl_name       IN     VARCHAR2  DEFAULT NULL,
   tbs_name       in     VARCHAR2  DEFAULT NULL,
   use_bf         in     BOOLEAN   DEFAULT FALSE,
   stgopts        in     VARCHAR2 DEFAULT '');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2 | IN | Name of store |
| store_type |  |  | STORETYPE_TAPE or STORETYPE_AMAZONS3 |
| tbl_name | VARCHAR2 | IN | Placeholder for the store content cached in database |
| tbs_name | VARCHAR2 | in | Named tablespace |
| use_bf | BOOLEAN | in | If TRUE , a BasicFile LOB is used; otherwise a SecureFile LOB is used. |
| stgopts | VARCHAR2 | in | Currently non-operational, reserved for future use |

## Usage Notes

Syntax DBMS_DBFS_SFS.CREATESTORE ( store_name IN VARCHAR2, tbl_name IN VARCHAR2 DEFAULT NULL, tbs_name in VARCHAR2 DEFAULT NULL, use_bf in BOOLEAN DEFAULT FALSE, stgopts in VARCHAR2 DEFAULT ''); Parameters Table 55-7 CREATESTORE Procedure Parameters Parameter Description store_name Name of store store_type STORETYPE_TAPE or STORETYPE_AMAZONS3 tbl_name Placeholder for the store content cached in database tbs_name Named tablespace use_bf If TRUE , a BasicFile LOB is used; otherwise a SecureFile LOB is used. stgopts Currently non-operational, reserved for future use