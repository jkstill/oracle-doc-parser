---
id: 19c__DBMS_DBFS_SFS.CREATEFILESYSTEM
name: DBMS_DBFS_SFS.CREATEFILESYSTEM
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_SFS
tags: [dbms_dbfs_sfs]
source_file: DBMS_DBFS_SFS.html
---

# DBMS_DBFS_SFS.CREATEFILESYSTEM

This procedure creates a file system store.

## Syntax

```sql
DBMS_DBFS_SFS.CREATEFILESYSTEM (
   store_name         IN     VARCHAR2,
   schema_name        IN     VARCHAR2    DEFAULT NULL,
   tbl_name           IN     VARCHAR2    DEFAULT NULL,
   tbl_tbs            IN     VARCHAR2    DEFAULT NULL,
   lob_tbs            IN     VARCHAR2    DEFAULT NULL,
   use_bf             IN     BOOLEAN     DEFAULT FALSE,
   properties         IN     DBMS_DBFS_CONTENT_PROPERTIES_T DEFAULT NULL,
   create_only        IN     BOOLEAN     FALSE,
   use_objects        IN     BOOLEAN     DEFAULT FALSE,
   with_grants        IN     BOOLEAN     DEFAULT FALSE,
   do_dedup           IN     BOOLEAN     DEFAULT FALSE,
   do_compress        IN     BOOLEAN     DEFAULT FALSE
   compression        IN     VARCHAR2    DEFAULT COMPRESSION_DEFAULT,
   do_encrypt         IN     BOOLEAN     DEFAULT FALSE,
   encryption         IN     VARCHAR2    DEFAULT ENCRYPTION_DEFAULT,
   do_partition       IN     BOOLEAN     DEFAULT FALSE,
   npartitions        IN     NUMBER      DEFAULTDEFAULT_PARTITIONS,
   partition_key      IN     NUMBER      DEFAULT PARTITION_BY_ITEM,
   partition_guidi    IN     BOOLEAN     DEFAULT FALSE,
   partition_pathi    IN     BOOLEAN     DEFAULT FALSE,
   partition_prop     IN     BOOLEAN     DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2 | IN | Name of store |
| schema_name | VARCHAR2 | IN | Schema for the store, defaulting to the current schema |
| tbl_name | VARCHAR2 | IN | Table for store entries. If not specified, an internally generated name is used. |
| tbl_tb |  |  | Tablespace for the store, defaulting to the schema's default tablespace |
| lob_tbs | VARCHAR2 | IN | Tablespace in which to create the LOB segment. It defaults to the user's default tablespace. |
| use_bf | BOOLEAN | IN | If TRUE , a BasicFile LOB is used; otherwise a SecureFile LOB is used. |
| properties | DBMS_DBFS_CONTENT_PROPERTIES_T | IN | Table of (name, value, typecode) tuples used to configure the store properties. Currently no such properties are defined or used. |
| create_only | BOOLEAN | IN | If TRUE , the file system is created, but not registered with the current user |
| use_objects | BOOLEAN | IN | If TRUE , a single base-table with an object-type column (using a nested table) is created to backup the new file system. Otherwise, a pair of (parent, child) tables is used to backup the file system. In both cases, the object type nested table or the child table is used only for user-defined properties. |
| with_grants | BOOLEAN | IN | If TRUE , DML and query access permissions are granted to the DBFS_ROLE as part of creating the file system. Otherwise, explicit grants (or existing permissions) are required to access the file system. |
| do_dedup | BOOLEAN | IN | If TRUE , do deduplication the underlying SecureFile column |
| do_compress | BOOLEAN | IN | If TRUE , do compression the underlying SecureFile column |
| compression | VARCHAR2 | IN | Compression algorithm to use (see Table 55-1 ) |
| do_encrypt | BOOLEAN | IN | If TRUE , encrypt the underlying SecureFile column |
| encryption | VARCHAR2 | IN | encryption algorithm to use (see Table 55-2 ) |
| do_partition | BOOLEAN | IN | If TRUE , partition the table used for storage |
| npartitions | NUMBER | IN | Number of partitions to create for the table (see Table 55-3 ). |
| partition_key | NUMBER | IN | How to partition the table: by item name, by path name, or by GUID (see Table 55-4 ). |
| partition_guidi | BOOLEAN | IN | If TRUE , build an index on GUID |
| partition_pathi | BOOLEAN | IN | If TRUE , build an index on path name |
| partition_prop | BOOLEAN | IN | If TRUE , partition the properties table |

## Usage Notes

Syntax DBMS_DBFS_SFS.CREATEFILESYSTEM ( store_name IN VARCHAR2, schema_name IN VARCHAR2 DEFAULT NULL, tbl_name IN VARCHAR2 DEFAULT NULL, tbl_tbs IN VARCHAR2 DEFAULT NULL, lob_tbs IN VARCHAR2 DEFAULT NULL, use_bf IN BOOLEAN DEFAULT FALSE, properties IN DBMS_DBFS_CONTENT_PROPERTIES_T DEFAULT NULL, create_only IN BOOLEAN FALSE, use_objects IN BOOLEAN DEFAULT FALSE, with_grants IN BOOLEAN DEFAULT FALSE, do_dedup IN BOOLEAN DEFAULT FALSE, do_compress IN BOOLEAN DEFAULT FALSE compression IN VARCHAR2 DEFAULT COMPRESSION_DEFAULT, do_encrypt IN BOOLEAN DEFAULT FALSE, encryption IN VARCHAR2 DEFAULT ENCRYPTION_DEFAULT, do_partition IN BOOLEAN DEFAULT FALSE, npartitions IN NUMBER DEFAULTDEFAULT_PARTITIONS, partition_key IN NUMBER DEFAULT PARTITION_BY_ITEM, partition_guidi IN BOOLEAN DEFAULT FALSE, partition_pathi IN BOOLEAN DEFAULT FALSE, partition_prop IN BOOLEAN DEFAULT TRUE); Parameters Table 55-6 CREATEFILESYSTEM Procedure Parameters Parameter Description store_name Name of store schema_name Schema for the store, defaulting to the current schema tbl_name Table for store entries. If not specified, an internally generated name is used. tbl_tb Tablespace for the store, defaulting to the schema's default tablespace lob_tbs Tablespace in which to create the LOB segment. It defaults to the user's default tablespace. use_bf If TRUE , a BasicFile LOB is used; otherwise a SecureFile LOB is used. properties Table of (name, value, typecode) tuples used to configure the store properties. Currently no such properties are defined or used. create_only If TRUE , the file system is created, but not registered with the current user use_objects If TRUE , a single base-table with an object-type column (using a nested table) is created to backup the new file system. Otherwise, a pair of (parent, child) tables is used to backup the file system. In both cases, the object type nested table or the child table is used only for user-defined properties. with_grants If TRUE , DML and query access permissions are granted to the DBFS_ROLE as part of creating the file system. Otherwise, explicit grants (or existing permissions) are required to access the file system. do_dedup If TRUE , do deduplication the underlying SecureFile column do_compress If TRUE , do compression the underlying SecureFile column compression Compression algorithm to use (see Table 55-1 ) do_encrypt If TRUE , encrypt the underlying SecureFile column encryption encryption algorithm to use (see Table 55-2 ) do_partition If TRUE , partition the table used for storage npartitions Number of partitions to create for the table (see Table 55-3 ). partition_key How to partition the table: by item name, by path name, or by GUID (see Table 55-4 ). partition_guidi If TRUE , build an index on GUID partition_pathi If TRUE , build an index on path name partition_prop If TRUE , partition the properties table Usage Notes The procedure executes like a DDL in that it auto-commits before and after its execution.