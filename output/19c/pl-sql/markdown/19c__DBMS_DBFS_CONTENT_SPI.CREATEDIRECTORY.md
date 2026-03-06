---
id: 19c__DBMS_DBFS_CONTENT_SPI.CREATEDIRECTORY
name: DBMS_DBFS_CONTENT_SPI.CREATEDIRECTORY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT_SPI
tags: [dbms_dbfs_content_spi]
source_file: DBMS_DBFS_CONTENT_SPI.html
---

# DBMS_DBFS_CONTENT_SPI.CREATEDIRECTORY

This procedure creates a directory.

## Syntax

```sql
DBMS_DBFS_CONTENT_SPI.CREATEDIRECTORY (
   store_name  IN              VARCHAR2,
   path        IN              VARCHAR2,
   properties  IN OUT NOCOPY   DBMS_DBFS_CONTENT_PROPERTIES_T,
   prop_flags  IN              INTEGER,
   recurse     IN              INTEGER,
   ctx         IN              DBMS_DBFS_CONTENT_CONTEXT_T);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2 | IN | Name of store |
| path | VARCHAR2 | IN | Name of path to the directory |
| properties | NOCOPY | IN OUT | One or more properties and their values to be set, returned, or both, depending on prop_flags (see DBMS_DBFS_CONTENT_PROPERTIES_T Table Type ) |
| prop_flags | INTEGER | IN | Determines which properties are set, returned, or both. Default is PROP_STD . Specify properties to be returned by setting PROP_SPC (see Table 52-9 ), and providing an instance of the DBMS_DBFS_CONTENT_PROPERTIES_T Table Type with properties whose values are of interest. |
| recurse | INTEGER | IN | If 0, do not execute recursively; otherwise, recursively create the directories above the given directory |
| ctx | DBMS_DBFS_CONTENT_CONTEXT_T) | IN | Context with which to create the directory (see DBMS_DBFS_CONTENT_CONTEXT_T Object Type ) |

## Usage Notes

Syntax DBMS_DBFS_CONTENT_SPI.CREATEDIRECTORY ( store_name IN VARCHAR2, path IN VARCHAR2, properties IN OUT NOCOPY DBMS_DBFS_CONTENT_PROPERTIES_T, prop_flags IN INTEGER, recurse IN INTEGER, ctx IN DBMS_DBFS_CONTENT_CONTEXT_T); Parameters Table 53-4 CREATEDIRECTORY Procedure Parameters Parameter Description store_name Name of store path Name of path to the directory properties One or more properties and their values to be set, returned, or both, depending on prop_flags (see DBMS_DBFS_CONTENT_PROPERTIES_T Table Type ) prop_flags Determines which properties are set, returned, or both. Default is PROP_STD . Specify properties to be returned by setting PROP_SPC (see Table 52-9 ), and providing an instance of the DBMS_DBFS_CONTENT_PROPERTIES_T Table Type with properties whose values are of interest. recurse If 0, do not execute recursively; otherwise, recursively create the directories above the given directory ctx Context with which to create the directory (see DBMS_DBFS_CONTENT_CONTEXT_T Object Type )