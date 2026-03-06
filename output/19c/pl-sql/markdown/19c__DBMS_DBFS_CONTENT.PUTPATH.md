---
id: 19c__DBMS_DBFS_CONTENT.PUTPATH
name: DBMS_DBFS_CONTENT.PUTPATH
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.PUTPATH

This procedure creates a new path item.

## Syntax

```sql
DBMS_DBFS_CONTENT.PUTPATH (
   path        IN              VARCHAR2,
   properties  IN OUT NOCOPY   DBMS_DBFS_CONTENT_PROPERTIES_T,
   content     IN OUT NOCOPY   BLOB,
   item_type   OUT             INTEGER,
   prop_flags  IN              INTEGER     DEFAULT (PROP_STD +
                                                         PROP_OPT +
                                                         PROP_DATA),
   store_name  IN              VARCHAR2    DEFAULT NULL,
   principal   IN              VARCHAR2    DEFAULT NULL);

DBMS_DBFS_CONTENT.PUTPATH (
   path        IN              VARCHAR2,
   properties  IN OUT NOCOPY   PROPERTIES_T,
   content     IN OUT NOCOPY   BLOB,
   item_type   OUT             INTEGER,
   prop_flags  IN              INTEGER     DEFAULT (PROP_STD +
                                                         PROP_OPT +
                                                         PROP_DATA),
   store_name  IN              VARCHAR2    DEFAULT NULL,
   principal   IN              VARCHAR2    DEFAULT NULL);

DBMS_DBFS_CONTENT.PUTPATH (
   path        IN              VARCHAR2,
   properties  IN OUT NOCOPY   DBMS_DBFS_CONTENT_PROPERTIES_T,
   amount      IN              NUMBER,
   offset      IN              NUMBER,
   buffer      IN              RAW,
   prop_flags  IN              INTEGER     DEFAULT (PROP_STD +
                                                         PROP_OPT),
   store_name  IN              VARCHAR2    DEFAULT NULL,
   principal   IN              VARCHAR2    DEFAULT NULL);

DBMS_DBFS_CONTENT.PUTPATH (
   path        IN              VARCHAR2,
   properties  IN OUT NOCOPY   PROPERTIES_T,
   amount      IN              NUMBER,
   offset      IN              NUMBER,
   buffer      IN              RAW,
   prop_flags  IN              INTEGER     DEFAULT (PROP_STD +
                                                         PROP_OPT),
   store_name  IN              VARCHAR2    DEFAULT NULL,
   principal   IN              VARCHAR2    DEFAULT NULL);

DBMS_DBFS_CONTENT.PUTPATH (
   path        IN              VARCHAR2,
   properties  IN OUT NOCOPY   DBMS_DBFS_CONTENT_PROPERTIES_T,
   written     OUT             NUMBER,
   offset      IN              NUMBER,
   buffers     IN             DBMS_DBFS_CONTENT_RAW_T,
   prop_flags  IN              INTEGER     DEFAULT (PROP_STD +
                                                         PROP_OPT),
   store_name  IN              VARCHAR2    DEFAULT NULL,
   principal   IN              VARCHAR2    DEFAULT NULL);

DBMS_DBFS_CONTENT.PUTPATH (
   path        IN              VARCHAR2,
   properties  IN OUT NOCOPY   PROPERTIES_T,
   written     OUT             NUMBER,
   offset      IN              NUMBER,
   buffers     IN              DBMS_DBFS_CONTENT_RAW_T,
   prop_flags  IN              INTEGER     DEFAULT (PROP_STD +
                                                         PROP_OPT),
   store_name  IN              VARCHAR2    DEFAULT NULL,
   principal   IN              VARCHAR2    DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| path | VARCHAR2 | IN | Name of path to file items |
| properties | NOCOPY | IN OUT | One or more properties and their values to be set depending on prop_flags (see DBMS_DBFS_CONTENT_PROPERTIES_T Table Type ) |
| content | NOCOPY | IN OUT | BLOB holding data which populates the file (optional) |
| item_type | INTEGER | OUT | Type of the path item specified (see Table 52-4 ) |
| amount | NUMBER | IN | Number of bytes to be read |
| offset | NUMBER | IN | Byte offset from which to begin reading |
| buffer | RAW | IN | Buffer to which to write |
| buffers | DBMS_DBFS_CONTENT_RAW_T | IN | Buffers to which to write |
| prop_flags | INTEGER | IN | Determines which properties are set. Default is PROP_STD . Specify properties to be returned by setting prop_spec , and providing an instance of the DBMS_DBFS_CONTENT_PROPERTIES_T Table Type with properties whose values are of interest. |
| store_name | VARCHAR2 | IN | Name of store |
| principal | VARCHAR2 | IN | Agent (principal) invoking the current operation |

## Usage Notes

Syntax DBMS_DBFS_CONTENT.PUTPATH ( path IN VARCHAR2, properties IN OUT NOCOPY DBMS_DBFS_CONTENT_PROPERTIES_T, content IN OUT NOCOPY BLOB, item_type OUT INTEGER, prop_flags IN INTEGER DEFAULT (PROP_STD + PROP_OPT + PROP_DATA), store_name IN VARCHAR2 DEFAULT NULL, principal IN VARCHAR2 DEFAULT NULL); DBMS_DBFS_CONTENT.PUTPATH ( path IN VARCHAR2, properties IN OUT NOCOPY PROPERTIES_T, content IN OUT NOCOPY BLOB, item_type OUT INTEGER, prop_flags IN INTEGER DEFAULT (PROP_STD + PROP_OPT + PROP_DATA), store_name IN VARCHAR2 DEFAULT NULL, principal IN VARCHAR2 DEFAULT NULL); DBMS_DBFS_CONTENT.PUTPATH ( path IN VARCHAR2, properties IN OUT NOCOPY DBMS_DBFS_CONTENT_PROPERTIES_T, amount IN NUMBER, offset IN NUMBER, buffer IN RAW, prop_flags IN INTEGER DEFAULT (PROP_STD + PROP_OPT), store_name IN VARCHAR2 DEFAULT NULL, principal IN VARCHAR2 DEFAULT NULL); DBMS_DBFS_CONTENT.PUTPATH ( path IN VARCHAR2, properties IN OUT NOCOPY PROPERTIES_T, amount IN NUMBER, offset IN NUMBER, buffer IN RAW, prop_flags IN INTEGER DEFAULT (PROP_STD + PROP_OPT), store_name IN VARCHAR2 DEFAULT NULL, principal IN VARCHAR2 DEFAULT NULL); DBMS_DBFS_CONTENT.PUTPATH ( path IN VARCHAR2, properties IN OUT NOCOPY DBMS_DBFS_CONTENT_PROPERTIES_T, written OUT NUMBER, offset IN NUMBER, buffers IN DBMS_DBFS_CONTENT_RAW_T, prop_flags IN INTEGER DEFAULT (PROP_STD + PROP_OPT), store_name IN VARCHAR2 DEFAULT NULL, principal IN VARCHAR2 DEFAULT NULL); DBMS_DBFS_CONTENT.PUTPATH ( path IN VARCHAR2, properties IN OUT NOCOPY PROPERTIES_T, written OUT NUMBER, offset IN NUMBER, buffers IN DBMS_DBFS_CONTENT_RAW_T, prop_flags IN INTEGER DEFAULT (PROP_STD + PROP_OPT), store_name IN VARCHAR2 DEFAULT NULL, principal IN VARCHAR2 DEFAULT NULL); Parameters Table 52-61 PUTPATH Procedure Parameters Parameter Description path Name of path to file items properties One or more properties and their values to be set depending on prop_flags (see DBMS_DBFS_CONTENT_PROPERTIES_T Table Type ) content BLOB holding data which populates the file (optional) item_type Type of the path item specified (see Table 52-4 ) amount Number of bytes to be read offset Byte offset from which to begin reading buffer Buffer to which to write buffers Buffers to which to write prop_flags Determines which properties are set. Default is PROP_STD . Specify properties to be returned by setting prop_spec , and providing an instance of the DBMS_DBFS_CONTENT_PROPERTIES_T Table Type with properties whose values are of interest. store_name Name of store principal Agent (principal) invoking the current operation