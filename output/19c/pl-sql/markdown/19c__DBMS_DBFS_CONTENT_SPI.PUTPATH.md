---
id: 19c__DBMS_DBFS_CONTENT_SPI.PUTPATH
name: DBMS_DBFS_CONTENT_SPI.PUTPATH
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT_SPI
tags: [dbms_dbfs_content_spi]
source_file: DBMS_DBFS_CONTENT_SPI.html
---

# DBMS_DBFS_CONTENT_SPI.PUTPATH

This procedure creates a new path item.

## Syntax

```sql
DBMS_DBFS_CONTENT_SPI.PUTPATH (
   store_name    IN              VARCHAR2,
   path          IN              VARCHAR2,
   properties    IN OUT NOCOPY   DBMS_DBFS_CONTENT_PROPERTIES_T,
   content       IN OUT NOCOPY   BLOB,
   item_type     OUT             INTEGER,
   prop_flags    IN              INTEGER,
   ctx           IN              DBMS_DBFS_CONTENT_CONTEXT_T);

DBMS_DBFS_CONTENT_SPI.PUTPATH (
   store_name    IN              VARCHAR2,
   path          IN              VARCHAR2,
   properties    IN OUT NOCOPY   DBMS_DBFS_CONTENT_PROPERTIES_T,
   amount        IN              NUMBER,
   offset        IN              NUMBER,
   buffer        IN              RAW,
   prop_flags    IN              INTEGER,
   ctx           IN              DBMS_DBFS_CONTENT_CONTEXT_T);

DBMS_DBFS_CONTENT_SPI.PUTPATH (
   store_name    IN              VARCHAR2,
   path          IN              VARCHAR2,
   properties    IN OUT NOCOPY   DBMS_DBFS_CONTENT_PROPERTIES_T,
   written       OUT             NUMBER,
   offset        IN              NUMBER,
   buffers       IN              DBMS_DBFS_CONTENT_RAW_T,
   prop_flags    IN              INTEGER,
   ctx           IN              DBMS_DBFS_CONTENT_CONTEXT_T);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2 | IN | Name of store |
| path | VARCHAR2 | IN | Path name of item to be put |
| properties | NOCOPY | IN OUT | One or more properties and their values to be set depending on prop_flags (see DBMS_DBFS_CONTENT_PROPERTIES_T Table Type ) |
| content | NOCOPY | IN OUT | BLOB holding data which populates the file (optional) |
| item_type | INTEGER | OUT | Type of the path item specified (see Table 52-4 ) |
| amount | NUMBER | IN | Number of bytes to be read |
| written | NUMBER | OUT | Number of bytes written |
| offset | NUMBER | IN | Byte offset from which to begin reading |
| buffer | RAW | IN | Buffer to which to write |
| buffers | DBMS_DBFS_CONTENT_RAW_T | IN | Buffers to which to write |
| prop_flags | INTEGER | IN | Determines which properties are set. Default is PROP_STD . Specify properties to be returned by setting prop_spec , and providing an instance of the DBMS_DBFS_CONTENT_PROPERTIES_T Table Type with properties whose values are of interest. |
| ctx | DBMS_DBFS_CONTENT_CONTEXT_T) | IN | Context with which to access the path items (see DBMS_DBFS_CONTENT_CONTEXT_T Object Type ) |

## Usage Notes

Syntax DBMS_DBFS_CONTENT_SPI.PUTPATH ( store_name IN VARCHAR2, path IN VARCHAR2, properties IN OUT NOCOPY DBMS_DBFS_CONTENT_PROPERTIES_T, content IN OUT NOCOPY BLOB, item_type OUT INTEGER, prop_flags IN INTEGER, ctx IN DBMS_DBFS_CONTENT_CONTEXT_T); DBMS_DBFS_CONTENT_SPI.PUTPATH ( store_name IN VARCHAR2, path IN VARCHAR2, properties IN OUT NOCOPY DBMS_DBFS_CONTENT_PROPERTIES_T, amount IN NUMBER, offset IN NUMBER, buffer IN RAW, prop_flags IN INTEGER, ctx IN DBMS_DBFS_CONTENT_CONTEXT_T); DBMS_DBFS_CONTENT_SPI.PUTPATH ( store_name IN VARCHAR2, path IN VARCHAR2, properties IN OUT NOCOPY DBMS_DBFS_CONTENT_PROPERTIES_T, written OUT NUMBER, offset IN NUMBER, buffers IN DBMS_DBFS_CONTENT_RAW_T, prop_flags IN INTEGER, ctx IN DBMS_DBFS_CONTENT_CONTEXT_T); Parameters Table 53-22 PUTPATH Procedure Parameters Parameter Description store_name Name of store path Path name of item to be put properties One or more properties and their values to be set depending on prop_flags (see DBMS_DBFS_CONTENT_PROPERTIES_T Table Type ) content BLOB holding data which populates the file (optional) item_type Type of the path item specified (see Table 52-4 ) amount Number of bytes to be read written Number of bytes written offset Byte offset from which to begin reading buffer Buffer to which to write buffers Buffers to which to write prop_flags Determines which properties are set. Default is PROP_STD . Specify properties to be returned by setting prop_spec , and providing an instance of the DBMS_DBFS_CONTENT_PROPERTIES_T Table Type with properties whose values are of interest. ctx Context with which to access the path items (see DBMS_DBFS_CONTENT_CONTEXT_T Object Type ) Usage Notes All path names allow their metadata (properties) to be read and modified. On completion of the call, the client can access specific properties using prop_flags (see Table 52-9 ). On completion of the call, the client can request a new BLOB locator that can be used to continue data access using the prop_data bitmask in prop_flags (see Table 52-9 ). Files can also be written without using BLOB locators, by explicitly specifying logical offsets or buffer-amounts, and a suitably sized buffer.