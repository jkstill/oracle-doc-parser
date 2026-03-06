---
id: 19c__DBMS_DBFS_HS.CREATESTORE
name: DBMS_DBFS_HS.CREATESTORE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_HS
tags: [dbms_dbfs_hs]
source_file: DBMS_DBFS_HS.html
---

# DBMS_DBFS_HS.CREATESTORE

This procedure creates a new hierarchical store store_name of type STORE_TYPE ( STORETYPE_TAPE or STORETYPE_AMAZONS3 ) in schema schema_name (defaulting to the current schema) under the ownership of the invoking session user.

## Syntax

```sql
DBMS_DBFS_HS.CREATESTORE  (
   store_name              IN     VARCHAR2,
   store_type              IN     VARCHAR2,
   tbl_name                IN     VARCHAR2,
   tbs_name                IN     VARCHAR2,
   cache_size              IN     NUMBER,
   lob_cache_quota         IN     NUMBER DEFAULT NULL,
   optimal_tarball_size    IN     NUMBER DEFAULT NULL,
   schema_name             IN     VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2 | IN | Name of store |
| store_type | VARCHAR2 | IN | STORETYPE_TAPE or STORETYPE_AMAZONS3 |
| tbl_name | VARCHAR2 | IN | Table for store entries |
| tbs_name | VARCHAR2 | IN | Tablespace for the store |
| cache_size | NUMBER | IN | Amount of space used by the store to cache content in given tablespace |
| lob_cache_quota | NUMBER | IN | Fraction of the cache_size which is allocated for level 1 cache. The default value of this parameter is NULL which means that 0.8 (= 80%) of the cache_size is used for level 1 cache. |
| optimal_tarball_size | NUMBER | IN | Maximum possible size of the archive file. Multiple content files are bundled together into one archive file, and then the archive file is transferred to tape or Amazon S3. This is because creating one file on tape or Amazon S3 for every content file in the store is a prohibitively expensive operation. The value of is set by default to 10GB for tape and to 100MB for Amazon S3. |
| schema_name | VARCHAR2 | IN | Schema for the store |

## Usage Notes

Syntax DBMS_DBFS_HS.CREATESTORE ( store_name IN VARCHAR2, store_type IN VARCHAR2, tbl_name IN VARCHAR2, tbs_name IN VARCHAR2, cache_size IN NUMBER, lob_cache_quota IN NUMBER DEFAULT NULL, optimal_tarball_size IN NUMBER DEFAULT NULL, schema_name IN VARCHAR2 DEFAULT NULL); Parameters Table 54-8 CREATESTORE Procedure Parameters Parameter Description store_name Name of store store_type STORETYPE_TAPE or STORETYPE_AMAZONS3 tbl_name Table for store entries tbs_name Tablespace for the store cache_size Amount of space used by the store to cache content in given tablespace lob_cache_quota Fraction of the cache_size which is allocated for level 1 cache. The default value of this parameter is NULL which means that 0.8 (= 80%) of the cache_size is used for level 1 cache. optimal_tarball_size Maximum possible size of the archive file. Multiple content files are bundled together into one archive file, and then the archive file is transferred to tape or Amazon S3. This is because creating one file on tape or Amazon S3 for every content file in the store is a prohibitively expensive operation. The value of is set by default to 10GB for tape and to 100MB for Amazon S3. schema_name Schema for the store Usage Notes CREATESTORE() sets certain properties of the store to default values. The user can use the methods SETSTOREPROPERTY() and RECONFIGCACHE() to appropriately change the property values and to set other properties of the store. Store names must be unique for an owner. The same store names can be used for different stores owned by different owners. Once a table space has been specified to store the store's content in a database, it cannot be changed later. This subprogram will execute like a DDL statement, performing an automatic COMMIT before and after execution. Stores using DBMS_DBFS_HS must not use singleton mount. This means that the singleton parameter should be FALSE and the store_mount parameter should have a non- NULL value in a call to the DBMS_DBFS_CONTENT . MOUNTSTORE procedure.