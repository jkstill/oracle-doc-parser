---
id: 19c__DBMS_DBFS_CONTENT_SPI.SETPATH
name: DBMS_DBFS_CONTENT_SPI.SETPATH
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT_SPI
tags: [dbms_dbfs_content_spi]
source_file: DBMS_DBFS_CONTENT_SPI.html
---

# DBMS_DBFS_CONTENT_SPI.SETPATH

This procedure assigns a path name to a path item represented by contentID.

## Syntax

```sql
DBMS_DBFS_CONTENT_SPI.SETPATH (
   store_name    IN              VARCHAR2,
   contentID     IN              RAW,
   path          IN              VARCHAR2,
   properties    IN OUT NOCOPY   DBMS_DBFS_CONTENT_PROPERTIES_T,
   ctx           IN              DBMS_DBFS_CONTENT_CONTEXT_T);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2 | IN | Name of the store |
| contentID | RAW | IN | Unique identifier for the item to be associated |
| path | VARCHAR2 | IN | Name of path to path item |
| properties | NOCOPY | IN OUT | One or more properties and their values to be set depending on prop_flags (see DBMS_DBFS_CONTENT_PROPERTIES_T Table Type ) |
| ctx | DBMS_DBFS_CONTENT_CONTEXT_T) | IN | Context with which to access the path items (seE DBMS_DBFS_CONTENT_CONTEXT_T Object Type ) |

## Usage Notes

Stores and their providers that support contentID-based access and lazy path name binding also support the SETPATH Procedure that associates an existing contentID with a new path. Note: See Oracle Database SecureFiles and Large Objects Developer's Guide for further information on Rename and Move operations Note: See Oracle Database SecureFiles and Large Objects Developer's Guide for further information on Rename and Move operations Syntax DBMS_DBFS_CONTENT_SPI.SETPATH ( store_name IN VARCHAR2, contentID IN RAW, path IN VARCHAR2, properties IN OUT NOCOPY DBMS_DBFS_CONTENT_PROPERTIES_T, ctx IN DBMS_DBFS_CONTENT_CONTEXT_T); Parameters Table 53-27 SETPATH Procedure Parameters Parameter Description store_name Name of the store contentID Unique identifier for the item to be associated path Name of path to path item properties One or more properties and their values to be set depending on prop_flags (see DBMS_DBFS_CONTENT_PROPERTIES_T Table Type ) ctx Context with which to access the path items (seE DBMS_DBFS_CONTENT_CONTEXT_T Object Type )