---
id: 19c__DBMS_DBFS_CONTENT_SPI.LOCKPATH
name: DBMS_DBFS_CONTENT_SPI.LOCKPATH
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT_SPI
tags: [dbms_dbfs_content_spi]
source_file: DBMS_DBFS_CONTENT_SPI.html
---

# DBMS_DBFS_CONTENT_SPI.LOCKPATH

This procedure applies user-level locks to the given valid path name (subject to store feature support), and optionally associates user-data with the lock.

## Syntax

```sql
DBMS_DBFS_CONTENT_SPI.LOCKPATH (
   store_name     IN     VARCHAR2,
   path           IN     VARCHAR2,
   who            IN     VARCHAR2,
   lock_type      IN     INTEGER,
   waitForRowLock IN     INTEGER,
   ctx            IN     DBMS_DBFS_CONTENT_CONTEXT_T);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2 | IN | Name of store |
| path | VARCHAR2 | IN | Path name of items to be locked |
| who | VARCHAR2 | IN | Transaction identifier that has locked the path |
| lock_type | INTEGER | IN | One of the available lock types (see Table 52-6 ) |
| waitForRowLock | INTEGER | IN | Determines if a row is locked by a transaction or not |
| ctx | DBMS_DBFS_CONTENT_CONTEXT_T) | IN | Context with which to access the path items (see DBMS_DBFS_CONTENT_CONTEXT_T Object Type ) |

## Usage Notes

Syntax DBMS_DBFS_CONTENT_SPI.LOCKPATH ( store_name IN VARCHAR2, path IN VARCHAR2, who IN VARCHAR2, lock_type IN INTEGER, waitForRowLock IN INTEGER, ctx IN DBMS_DBFS_CONTENT_CONTEXT_T); Parameters Table 53-19 LOCKPATH Procedure Parameters Parameter Description store_name Name of store path Path name of items to be locked who Transaction identifier that has locked the path lock_type One of the available lock types (see Table 52-6 ) waitForRowLock Determines if a row is locked by a transaction or not ctx Context with which to access the path items (see DBMS_DBFS_CONTENT_CONTEXT_T Object Type ) Usage Notes It is the responsibility of the store and its providers (assuming it supports user-defined lock checking) to ensure that lock and unlock operations are performed in a consistent manner. The status of locked items is available by means of various optional properties (see OPT_LOCK * in Table 52-8 ).