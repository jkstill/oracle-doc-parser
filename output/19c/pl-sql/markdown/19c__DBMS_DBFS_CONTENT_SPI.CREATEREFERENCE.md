---
id: 19c__DBMS_DBFS_CONTENT_SPI.CREATEREFERENCE
name: DBMS_DBFS_CONTENT_SPI.CREATEREFERENCE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT_SPI
tags: [dbms_dbfs_content_spi]
source_file: DBMS_DBFS_CONTENT_SPI.html
---

# DBMS_DBFS_CONTENT_SPI.CREATEREFERENCE

This procedure creates a new reference to the source file system element (such as a file, or directory). The resulting reference points to the source element but does not directly share metadata with the source element. This is analogous to a UNIX file system symbolic link.

## Syntax

```sql
DBMS_DBFS_CONTENT_SPI.CREATEREFERENCE (
   srcPath       IN              VARCHAR2,
   dstPath       IN              VARCHAR2,
   properties    IN OUT NOCOPY   DBMS_DBFS_CONTENT_PROPERTIES_T,
   prop_flags    IN              INTEGER,
   store_name    IN              VARCHAR2,
   ctx           IN              DBMS_DBFS_CONTENT_CONTEXT_T);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2 | IN | Name of store |
| srcPath | VARCHAR2 | IN | File system entry with which to link |
| dstPath | VARCHAR2 | IN | Path of the new link element to be created |
| properties | NOCOPY | IN OUT | One or more properties and their values to be set, returned, or both, depending on prop_flags (see DBMS_DBFS_CONTENT_PROPERTIES_T Table Type ) |
| prop_flags | INTEGER | IN | Determines which properties are set, returned, or both. Default is PROP_STD . Specify properties to be returned by setting prop_spec , and providing an instance of the DBMS_DBFS_CONTENT_PROPERTIES_T Table Type with properties whose values are of interest. |
| ctx | DBMS_DBFS_CONTENT_CONTEXT_T) | IN | Context with which to create the reference (see DBMS_DBFS_CONTENT_CONTEXT_T Object Type ) |

## Usage Notes

Syntax DBMS_DBFS_CONTENT_SPI.CREATEREFERENCE ( srcPath IN VARCHAR2, dstPath IN VARCHAR2, properties IN OUT NOCOPY DBMS_DBFS_CONTENT_PROPERTIES_T, prop_flags IN INTEGER, store_name IN VARCHAR2, ctx IN DBMS_DBFS_CONTENT_CONTEXT_T); Parameters Table 53-7 CREATEREFERENCE Procedure Parameters Parameter Description store_name Name of store srcPath File system entry with which to link dstPath Path of the new link element to be created properties One or more properties and their values to be set, returned, or both, depending on prop_flags (see DBMS_DBFS_CONTENT_PROPERTIES_T Table Type ) prop_flags Determines which properties are set, returned, or both. Default is PROP_STD . Specify properties to be returned by setting prop_spec , and providing an instance of the DBMS_DBFS_CONTENT_PROPERTIES_T Table Type with properties whose values are of interest. ctx Context with which to create the reference (see DBMS_DBFS_CONTENT_CONTEXT_T Object Type )