---
id: 19c__DBMS_DBFS_CONTENT_SPI.UNLOCKPATH
name: DBMS_DBFS_CONTENT_SPI.UNLOCKPATH
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT_SPI
tags: [dbms_dbfs_content_spi]
source_file: DBMS_DBFS_CONTENT_SPI.html
---

# DBMS_DBFS_CONTENT_SPI.UNLOCKPATH

This procedure unlocks path items that were previously locked with the LOCKPATH Procedure.

## Syntax

```sql
DBMS_DBFS_CONTENT_SPI.UNLOCKPATH (
   store_name     IN     VARCHAR2,
   path           IN     VARCHAR2,
   who            IN     VARCHAR2,
   waitForRowLock IN     INTEGER,
   ctx            IN     DBMS_DBFS_CONTENT_CONTEXT_T);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2 | IN | Name of store |
| path | VARCHAR2 | IN | Name of path to the path items |
| who | VARCHAR2 | IN | Transaction identifier that has locked the path |
| waitForRowLock | INTEGER | IN | Determines if a row is locked by a transaction or not |
| ctx | DBMS_DBFS_CONTENT_CONTEXT_T) | IN | Context with which to access the path items (see DBMS_DBFS_CONTENT_CONTEXT_T Object Type ) |

## Usage Notes

Syntax DBMS_DBFS_CONTENT_SPI.UNLOCKPATH ( store_name IN VARCHAR2, path IN VARCHAR2, who IN VARCHAR2, waitForRowLock IN INTEGER, ctx IN DBMS_DBFS_CONTENT_CONTEXT_T); Parameters Table 53-29 UNLOCKPATH Procedure Parameters Parameter Description store_name Name of store path Name of path to the path items who Transaction identifier that has locked the path waitForRowLock Determines if a row is locked by a transaction or not ctx Context with which to access the path items (see DBMS_DBFS_CONTENT_CONTEXT_T Object Type )