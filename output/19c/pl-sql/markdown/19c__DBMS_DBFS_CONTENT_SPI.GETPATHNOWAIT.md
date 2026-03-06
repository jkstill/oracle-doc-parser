---
id: 19c__DBMS_DBFS_CONTENT_SPI.GETPATHNOWAIT
name: DBMS_DBFS_CONTENT_SPI.GETPATHNOWAIT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT_SPI
tags: [dbms_dbfs_content_spi]
source_file: DBMS_DBFS_CONTENT_SPI.html
---

# DBMS_DBFS_CONTENT_SPI.GETPATHNOWAIT

This procedure implies that the operation is for an update, and, if implemented, allows providers to return an exception ( ORA-00054 ) rather than wait for row locks.

## Syntax

```sql
DBMS_DBFS_CONTENT_SPI.GETPATHNOWAIT (
   store_name  IN              VARCHAR2,
   path        IN              VARCHAR2,
   properties  IN OUT NOCOPY   DBMS_DBFS_CONTENT_PROPERTIES_T,
   content     OUT    NOCOPY   BLOB,
   item_type   OUT             INTEGER,
   prop_flags  IN              INTEGER,
   deref       IN              INTEGER,
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
| prop_flags | INTEGER | IN | Determines which properties are returned. Default is PROP_STD . Specify properties to be returned by setting prop_spec , and providing an instance of the DBMS_DBFS_CONTENT_PROPERTIES_T Table Type with properties whose values are of interest. |
| deref | INTEGER | IN | If nonzero, attempts to resolve the given path item to actual data provided it is a reference (symbolic link) |
| ctx | DBMS_DBFS_CONTENT_CONTEXT_T) | IN | Context with which to access the path items (see DBMS_DBFS_CONTENT_CONTEXT_T Object Type ) |

## Usage Notes

See FEATURE_NOWAIT in Table 52-5 for more information. Syntax DBMS_DBFS_CONTENT_SPI.GETPATHNOWAIT ( store_name IN VARCHAR2, path IN VARCHAR2, properties IN OUT NOCOPY DBMS_DBFS_CONTENT_PROPERTIES_T, content OUT NOCOPY BLOB, item_type OUT INTEGER, prop_flags IN INTEGER, deref IN INTEGER, ctx IN DBMS_DBFS_CONTENT_CONTEXT_T); Parameters Table 53-14 GETPATHNOWAIT Procedure Parameters Parameter Description store_name Name of store path Name of path to path items properties One or more properties and their values to be returned depending on prop_flags (see DBMS_DBFS_CONTENT_PROPERTIES_T Table Type ) content BLOB holding data which populates the file (optional) item_type Type of the path item specified (see Table 52-4 ) prop_flags Determines which properties are returned. Default is PROP_STD . Specify properties to be returned by setting prop_spec , and providing an instance of the DBMS_DBFS_CONTENT_PROPERTIES_T Table Type with properties whose values are of interest. deref If nonzero, attempts to resolve the given path item to actual data provided it is a reference (symbolic link) ctx Context with which to access the path items (see DBMS_DBFS_CONTENT_CONTEXT_T Object Type )