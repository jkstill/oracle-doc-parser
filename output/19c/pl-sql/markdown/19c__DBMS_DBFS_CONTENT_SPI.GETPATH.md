---
id: 19c__DBMS_DBFS_CONTENT_SPI.GETPATH
name: DBMS_DBFS_CONTENT_SPI.GETPATH
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT_SPI
tags: [dbms_dbfs_content_spi]
source_file: DBMS_DBFS_CONTENT_SPI.html
---

# DBMS_DBFS_CONTENT_SPI.GETPATH

This procedure returns existing path items (such as files and directories). This includes both data and metadata (properties).

## Syntax

```sql
DBMS_DBFS_CONTENT_SPI.GETPATH (
   store_name  IN              VARCHAR2,
   path        IN              VARCHAR2,
   properties  IN OUT NOCOPY   DBMS_DBFS_CONTENT_PROPERTIES_T,
   content     OUT    NOCOPY   BLOB,
   item_type   OUT             INTEGER,
   prop_flags  IN              INTEGER,
   forUpdate   IN              INTEGER,
   deref       IN              INTEGER,
   ctx         IN              DBMS_DBFS_CONTENT_CONTEXT_T);

DBMS_DBFS_CONTENT_SPI.GETPATH (
   store_name  IN              VARCHAR2,
   path        IN              VARCHAR2,
   properties  IN OUT NOCOPY   DBMS_DBFS_CONTENT_PROPERTIES_T,
   amount      IN OUT          NUMBER,
   offset      IN              NUMBER,
   buffer      OUT    NOCOPY   RAW,
   prop_flags  IN              INTEGER,
   ctx         IN              DBMS_DBFS_CONTENT_CONTEXT_T);

DBMS_DBFS_CONTENT_SPI.GETPATH (
   store_name  IN              VARCHAR2,
   path        IN              VARCHAR2,
   properties  IN OUT NOCOPY   DBMS_DBFS_CONTENT_PROPERTIES_T,
   amount      IN OUT          NUMBER,
   offset      IN              NUMBER,
   buffers     OUT    NOCOPY   DBMS_DBFS_CONTENT_RAW_T,
   prop_flags  IN              INTEGER,
   ctx         IN              DBMS_DBFS_CONTENT_CONTEXT_T);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2 | IN | Name of store |
| path | VARCHAR2 | IN | Name of path to path items |
| properties | NOCOPY | IN OUT | One or more properties and their values to be returned depending on prop_flags (see DBMS_DBFS_CONTENT_PROPERTIES_T Table Type ) |
| content | NOCOPY | OUT | BLOB holding data which populates the file (optional) |
| item_type | INTEGER | OUT | Type of the path item specified (see Table 52-4 ) |
| amount | NUMBER | IN OUT | On input, number of bytes to be read. On output, number of bytes read |
| offset | NUMBER | IN | Byte offset from which to begin reading |
| buffer | NOCOPY | OUT | Buffer to which to write |
| buffers | NOCOPY | OUT | Buffers to which to write |
| prop_flags | INTEGER | IN | Determines which properties are set, returned, or both. Default is PROP_STD . Specify properties to be returned by setting prop_spec , and providing an instance of the DBMS_DBFS_CONTENT_PROPERTIES_T Table Type with properties whose values are of interest. |
| forUpdate | INTEGER | IN | Specifies that a lock should be taken to signify exclusive write access to the path item |
| deref | INTEGER | IN | If nonzero, attempts to resolve the given path item to actual data provided it is a reference (symbolic link) |
| ctx | DBMS_DBFS_CONTENT_CONTEXT_T) | IN | Context with which to access the path items (see DBMS_DBFS_CONTENT_CONTEXT_T Object Type ) |

## Usage Notes

The client can request (using prop_flags ) that specific properties be returned. File path names can be read either by specifying a BLOB locator using the prop_data bitmask in prop_flags (see Table 52-9 ) or by passing one or more RAW buffers. When forUpdate is 0, this procedure also accepts a valid "as of" timestamp parameter as part of ctx that can be used by stores to implement "as of" style flashback queries. Mutating versions of the GETPATH Procedures do not support these modes of operation. Syntax DBMS_DBFS_CONTENT_SPI.GETPATH ( store_name IN VARCHAR2, path IN VARCHAR2, properties IN OUT NOCOPY DBMS_DBFS_CONTENT_PROPERTIES_T, content OUT NOCOPY BLOB, item_type OUT INTEGER, prop_flags IN INTEGER, forUpdate IN INTEGER, deref IN INTEGER, ctx IN DBMS_DBFS_CONTENT_CONTEXT_T); DBMS_DBFS_CONTENT_SPI.GETPATH ( store_name IN VARCHAR2, path IN VARCHAR2, properties IN OUT NOCOPY DBMS_DBFS_CONTENT_PROPERTIES_T, amount IN OUT NUMBER, offset IN NUMBER, buffer OUT NOCOPY RAW, prop_flags IN INTEGER, ctx IN DBMS_DBFS_CONTENT_CONTEXT_T); DBMS_DBFS_CONTENT_SPI.GETPATH ( store_name IN VARCHAR2, path IN VARCHAR2, properties IN OUT NOCOPY DBMS_DBFS_CONTENT_PROPERTIES_T, amount IN OUT NUMBER, offset IN NUMBER, buffers OUT NOCOPY DBMS_DBFS_CONTENT_RAW_T, prop_flags IN INTEGER, ctx IN DBMS_DBFS_CONTENT_CONTEXT_T); Parameters Table 53-12 GETPATH Procedure Parameters Parameter Description store_name Name of store path Name of path to path items properties One or more properties and their values to be returned depending on prop_flags (see DBMS_DBFS_CONTENT_PROPERTIES_T Table Type ) content BLOB holding data which populates the file (optional) item_type Type of the path item specified (see Table 52-4 ) amount On input, number of bytes to be read. On output, number of bytes read offset Byte offset from which to begin reading buffer Buffer to which to write buffers Buffers to which to write prop_flags Determines which properties are set, returned, or both. Default is PROP_STD . Specify properties to be returned by setting prop_spec , and providing an instance of the DBMS_DBFS_CONTENT_PROPERTIES_T Table Type with properties whose values are of interest. forUpdate Specifies that a lock should be taken to signify exclusive write access to the path item deref If nonzero, attempts to resolve the given path item to actual data provided it is a reference (symbolic link) ctx Context with which to access the path items (see DBMS_DBFS_CONTENT_CONTEXT_T Object Type )