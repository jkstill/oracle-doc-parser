---
id: 19c__DBMS_DBFS_CONTENT_SPI.CREATEFILE
name: DBMS_DBFS_CONTENT_SPI.CREATEFILE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT_SPI
tags: [dbms_dbfs_content_spi]
source_file: DBMS_DBFS_CONTENT_SPI.html
---

# DBMS_DBFS_CONTENT_SPI.CREATEFILE

This procedure creates a file.

## Syntax

```sql
DBMS_DBFS_CONTENT_SPI.CREATEFILE (
   store_name    IN              VARCHAR2,
   path          IN              VARCHAR2,
   properties    IN OUT NOCOPY   DBMS_DBFS_CONTENT_PROPERTIES_T,
   content       IN OUT NOCOPY   BLOB,
   prop_flags    IN              INTEGER,
   ctx           IN              DBMS_DBFS_CONTENT_CONTEXT_T);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2 | IN | Name of store |
| path | VARCHAR2 | IN | Name of path to the file |
| properties | NOCOPY | IN OUT | One or more properties and their values to be set, returned or both depending, or both on prop_flags (see DBMS_DBFS_CONTENT_PROPERTIES_T Table Type ) |
| content | NOCOPY | IN OUT | BLOB holding data with which to populate the file (optional) |
| prop_flags | INTEGER | IN | Determines which properties are set, returned, or both. Default is PROP_STD . Specify properties to be returned by setting prop_spec , and providing an instance of the DBMS_DBFS_CONTENT_PROPERTIES_T Table Type with properties whose values are of interest. |
| ctx | DBMS_DBFS_CONTENT_CONTEXT_T) | IN | Context with which to create the file (see DBMS_DBFS_CONTENT_CONTEXT_T Object Type ) |

## Usage Notes

Syntax DBMS_DBFS_CONTENT_SPI.CREATEFILE ( store_name IN VARCHAR2, path IN VARCHAR2, properties IN OUT NOCOPY DBMS_DBFS_CONTENT_PROPERTIES_T, content IN OUT NOCOPY BLOB, prop_flags IN INTEGER, ctx IN DBMS_DBFS_CONTENT_CONTEXT_T); Parameters Table 53-5 CREATEFILE Procedure Parameters Parameter Description store_name Name of store path Name of path to the file properties One or more properties and their values to be set, returned or both depending, or both on prop_flags (see DBMS_DBFS_CONTENT_PROPERTIES_T Table Type ) content BLOB holding data with which to populate the file (optional) prop_flags Determines which properties are set, returned, or both. Default is PROP_STD . Specify properties to be returned by setting prop_spec , and providing an instance of the DBMS_DBFS_CONTENT_PROPERTIES_T Table Type with properties whose values are of interest. ctx Context with which to create the file (see DBMS_DBFS_CONTENT_CONTEXT_T Object Type )