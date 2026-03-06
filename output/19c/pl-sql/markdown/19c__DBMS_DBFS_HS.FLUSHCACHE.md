---
id: 19c__DBMS_DBFS_HS.FLUSHCACHE
name: DBMS_DBFS_HS.FLUSHCACHE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_HS
tags: [dbms_dbfs_hs]
source_file: DBMS_DBFS_HS.html
---

# DBMS_DBFS_HS.FLUSHCACHE

This procedure flushes out dirty contents from level-1 cache, which can be locked, to level-2 cache, thereby freeing-up space in level 1 cache.

## Syntax

```sql
DBMS_DBFS_HS.FLUSHCACHE  (
   store_name    IN     VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2) | IN | Name of store |

## Usage Notes

Syntax DBMS_DBFS_HS.FLUSHCACHE ( store_name IN VARCHAR2); Parameters Table 54-11 FLUSHCACHE Procedure Parameters Parameter Description store_name Name of store