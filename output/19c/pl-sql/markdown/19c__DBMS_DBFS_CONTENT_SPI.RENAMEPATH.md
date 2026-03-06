---
id: 19c__DBMS_DBFS_CONTENT_SPI.RENAMEPATH
name: DBMS_DBFS_CONTENT_SPI.RENAMEPATH
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT_SPI
tags: [dbms_dbfs_content_spi]
source_file: DBMS_DBFS_CONTENT_SPI.html
---

# DBMS_DBFS_CONTENT_SPI.RENAMEPATH

This procedure renames or moves a path. This operation can be performed across directory hierarchies and mount-points as long as it is within the same store.

## Syntax

```sql
DBMS_DBFS_CONTENT_SPI.RENAMEPATH (
   store_name    IN              VARCHAR2,
   oldPath       IN              VARCHAR2,
   newPath       IN              VARCHAR2,
   properties    IN OUT NOCOPY   DBMS_DBFS_CONTENT_PROPERTIES_T,
   ctx           IN              DBMS_DBFS_CONTENT_CONTEXT_T);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2 | IN | Name of store, must be unique |
| oldPath | VARCHAR2 | IN | Name of path prior to renaming |
| newPath | VARCHAR2 | IN | Name of path after renaming |
| properties | NOCOPY | IN OUT | One or more properties and their values to be set depending on prop_flags (see DBMS_DBFS_CONTENT_PROPERTIES_T Table Type ) |
| ctx | DBMS_DBFS_CONTENT_CONTEXT_T) | IN | Context with which to access the path items (see DBMS_DBFS_CONTENT_CONTEXT_T Object Type ) |

## Usage Notes

Note: See Oracle Database SecureFiles and Large Objects Developer's Guide for further information on Rename and Move operations Note: See Oracle Database SecureFiles and Large Objects Developer's Guide for further information on Rename and Move operations Syntax DBMS_DBFS_CONTENT_SPI.RENAMEPATH ( store_name IN VARCHAR2, oldPath IN VARCHAR2, newPath IN VARCHAR2, properties IN OUT NOCOPY DBMS_DBFS_CONTENT_PROPERTIES_T, ctx IN DBMS_DBFS_CONTENT_CONTEXT_T); Parameters Table 53-23 RENAMEPATH Procedure Parameters Parameter Description store_name Name of store, must be unique oldPath Name of path prior to renaming newPath Name of path after renaming properties One or more properties and their values to be set depending on prop_flags (see DBMS_DBFS_CONTENT_PROPERTIES_T Table Type ) ctx Context with which to access the path items (see DBMS_DBFS_CONTENT_CONTEXT_T Object Type )