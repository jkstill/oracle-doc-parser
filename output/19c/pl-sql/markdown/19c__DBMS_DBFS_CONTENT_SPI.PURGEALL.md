---
id: 19c__DBMS_DBFS_CONTENT_SPI.PURGEALL
name: DBMS_DBFS_CONTENT_SPI.PURGEALL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT_SPI
tags: [dbms_dbfs_content_spi]
source_file: DBMS_DBFS_CONTENT_SPI.html
---

# DBMS_DBFS_CONTENT_SPI.PURGEALL

This procedure purges all soft-deleted entries matching the path and optional filter criteria.

## Syntax

```sql
DBMS_DBFS_CONTENT_SPI.PURGEALL (
   store_name     IN      VARCHAR2,
   path           IN      VARCHAR2,
   filter         IN      VARCHAR2,
   ctx            IN      DBMS_DBFS_CONTENT_CONTEXT_T);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2 | IN | Name of store |
| path | VARCHAR2 | IN | Name of path to file items |
| filter | VARCHAR2 | IN | A filter, if any, to be applied based on specified criteria |
| ctx | DBMS_DBFS_CONTENT_CONTEXT_T) | IN | Context with which to access the path items (see DBMS_DBFS_CONTENT_CONTEXT_T Object Type ) |

## Usage Notes

Syntax DBMS_DBFS_CONTENT_SPI.PURGEALL ( store_name IN VARCHAR2, path IN VARCHAR2, filter IN VARCHAR2, ctx IN DBMS_DBFS_CONTENT_CONTEXT_T); Parameters Table 53-20 PURGEALL Procedure Parameters Parameter Description store_name Name of store path Name of path to file items filter A filter, if any, to be applied based on specified criteria ctx Context with which to access the path items (see DBMS_DBFS_CONTENT_CONTEXT_T Object Type )