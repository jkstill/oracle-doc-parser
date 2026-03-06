---
id: 19c__DBMS_DBFS_CONTENT.GETPATH
name: DBMS_DBFS_CONTENT.GETPATH
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.GETPATH

This procedure returns existing path items (such as files and directories). This includes both data and metadata (properties).

## Syntax

```sql
DBMS_DBFS_CONTENT.GETPATH (
        path        IN              VARCHAR2,
        properties  IN OUT NOCOPY   DBMS_DBFS_CONTENT_PROPERTIES_T,
        content     OUT    NOCOPY   BLOB,
        item_type   OUT             INTEGER,
        prop_flags  IN              INTEGER     DEFAULT (PROP_STD +
                                                         PROP_OPT +
                                                         PROP_DATA),
        asof        IN              TIMESTAMP   DEFAULT NULL,
        forUpdate   IN              BOOLEAN     DEFAULT FALSE,
        deref       IN              BOOLEAN     DEFAULT FALSE,
        store_name  IN              VARCHAR2    DEFAULT NULL,
        principal   IN              VARCHAR2    DEFAULT NULL);

DBMS_DBFS_CONTENT.GETPATH (
        path        IN              VARCHAR2,
        properties  IN OUT NOCOPY   PROPERTIES_T,
        content     OUT    NOCOPY   BLOB,
        item_type   OUT             INTEGER,
        prop_flags  IN              INTEGER     DEFAULT (PROP_STD +
                                                         PROP_OPT +
                                                         PROP_DATA),
        asof        IN              TIMESTAMP   DEFAULT NULL,
        forUpdate   IN              BOOLEAN     DEFAULT FALSE,
        deref       IN              BOOLEAN     DEFAULT FALSE,
        store_name  IN              VARCHAR2    DEFAULT NULL,
        principal   IN              VARCHAR2    DEFAULT NULL);

DBMS_DBFS_CONTENT.GETPATH (
        path        IN              VARCHAR2,
        properties  IN OUT NOCOPY   DBMS_DBFS_CONTENT_PROPERTIES_T,
        amount      IN OUT          NUMBER,
        offset      IN              NUMBER,
        buffers     OUT    NOCOPY   RAW,
        prop_flags  IN              INTEGER     DEFAULT (PROP_STD +
                                                         PROP_OPT +
                                                         PROP_DATA),
        asof        IN              TIMESTAMP   DEFAULT NULL,
        store_name  IN              VARCHAR2    DEFAULT NULL,
        principal   IN              VARCHAR2    DEFAULT NULL);

DBMS_DBFS_CONTENT.GETPATH (
        path        IN              VARCHAR2,
        properties  IN OUT NOCOPY   PROPERTIES_T,
        amount      IN OUT          NUMBER,
        offset      IN              NUMBER,
        buffers     OUT    NOCOPY   RAW,
        prop_flags  IN              INTEGER     DEFAULT (PROP_STD +
                                                         PROP_OPT +
                                                         PROP_DATA),
        asof        IN              TIMESTAMP   DEFAULT NULL,
        store_name  IN              VARCHAR2    DEFAULT NULL,
        principal   IN              VARCHAR2    DEFAULT NULL);

DBMS_DBFS_CONTENT.GETPATH (
        path        IN              VARCHAR2,
        properties  IN OUT NOCOPY   DBMS_DBFS_CONTENT_PROPERTIES_T,
        amount      IN OUT          NUMBER,
        offset      IN              NUMBER,
        buffers     OUT    NOCOPY   DBMS_DBFS_CONTENT_RAW_T,
        prop_flags  IN              INTEGER     DEFAULT (PROP_STD +
                                                         PROP_OPT +
                                                         PROP_DATA),
        asof        IN              TIMESTAMP   DEFAULT NULL,
        store_name  IN              VARCHAR2    DEFAULT NULL,
        principal   IN              VARCHAR2    DEFAULT NULL);

DBMS_DBFS_CONTENT.GETPATH (
        path        IN              VARCHAR2,
        properties  IN OUT NOCOPY   PROPERTIES_T,
        amount      IN OUT          NUMBER,
        offset      IN              NUMBER,
        buffers     OUT    NOCOPY   DBMS_DBFS_CONTENT_RAW_T,
        prop_flags  IN              INTEGER     DEFAULT (PROP_STD +
                                                         PROP_OPT +
                                                         PROP_DATA),
        asof        IN              TIMESTAMP   DEFAULT NULL,
        store_name  IN              VARCHAR2    DEFAULT NULL,
        principal   IN              VARCHAR2    DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| path | VARCHAR2 | IN | Name of path to path items |
| properties | NOCOPY | IN OUT | One or more properties and their values to be returned depending on prop_flags (see DBMS_DBFS_CONTENT_PROPERTIES_T Table Type ) |
| content | NOCOPY | OUT | BLOB holding data which populates the file (optional) |
| item_type | INTEGER | OUT | Type of the path item specified (see Table 52-4 ) |
| amount | NUMBER | IN OUT | On input, number of bytes to be read. On output, number of bytes read |
| offset | NUMBER | IN | Byte offset from which to begin reading |
| buffer |  |  | Buffer to which to write |
| buffers | NOCOPY | OUT | Buffers to which to write |
| prop_flags | INTEGER | IN | Determines which properties are set, returned, or both. Default is PROP_STD . Specify properties to be returned by setting prop_spec , and providing an instance of the DBMS_DBFS_CONTENT_PROPERTIES_T Table Type with properties whose values are of interest. |
| asof | TIMESTAMP | IN | The "as of" timestamp at which the underlying read-only operation (or its read-only sub-components) executes |
| forUpdate | BOOLEAN | IN | Specifies that a lock should be taken to signify exclusive write access to the path item |
| deref | BOOLEAN | IN | If nonzero, attempts to resolve the given path item to actual data provided it is a reference |
| store_name | VARCHAR2 | IN | Name of store |
| principal | VARCHAR2 | IN | Agent (principal) invoking the current operation |

## Usage Notes

The client can request (using prop_flags ) that specific properties be returned. File path names can be read either by specifying a BLOB locator using the prop_data bitmask in prop_flags (see Table 52-9 ) or by passing one or more RAW buffers. When forUpdate is 0, this procedure also accepts a valid asof timestamp parameter as part of ctx that can be used by stores to implement "as of" style flashback queries. Mutating versions of the GETPATH Procedures do not support these modes of operation. Syntax DBMS_DBFS_CONTENT.GETPATH ( path IN VARCHAR2, properties IN OUT NOCOPY DBMS_DBFS_CONTENT_PROPERTIES_T, content OUT NOCOPY BLOB, item_type OUT INTEGER, prop_flags IN INTEGER DEFAULT (PROP_STD + PROP_OPT + PROP_DATA), asof IN TIMESTAMP DEFAULT NULL, forUpdate IN BOOLEAN DEFAULT FALSE, deref IN BOOLEAN DEFAULT FALSE, store_name IN VARCHAR2 DEFAULT NULL, principal IN VARCHAR2 DEFAULT NULL); DBMS_DBFS_CONTENT.GETPATH ( path IN VARCHAR2, properties IN OUT NOCOPY PROPERTIES_T, content OUT NOCOPY BLOB, item_type OUT INTEGER, prop_flags IN INTEGER DEFAULT (PROP_STD + PROP_OPT + PROP_DATA), asof IN TIMESTAMP DEFAULT NULL, forUpdate IN BOOLEAN DEFAULT FALSE, deref IN BOOLEAN DEFAULT FALSE, store_name IN VARCHAR2 DEFAULT NULL, principal IN VARCHAR2 DEFAULT NULL); DBMS_DBFS_CONTENT.GETPATH ( path IN VARCHAR2, properties IN OUT NOCOPY DBMS_DBFS_CONTENT_PROPERTIES_T, amount IN OUT NUMBER, offset IN NUMBER, buffers OUT NOCOPY RAW, prop_flags IN INTEGER DEFAULT (PROP_STD + PROP_OPT + PROP_DATA), asof IN TIMESTAMP DEFAULT NULL, store_name IN VARCHAR2 DEFAULT NULL, principal IN VARCHAR2 DEFAULT NULL); DBMS_DBFS_CONTENT.GETPATH ( path IN VARCHAR2, properties IN OUT NOCOPY PROPERTIES_T, amount IN OUT NUMBER, offset IN NUMBER, buffers OUT NOCOPY RAW, prop_flags IN INTEGER DEFAULT (PROP_STD + PROP_OPT + PROP_DATA), asof IN TIMESTAMP DEFAULT NULL, store_name IN VARCHAR2 DEFAULT NULL, principal IN VARCHAR2 DEFAULT NULL); DBMS_DBFS_CONTENT.GETPATH ( path IN VARCHAR2, properties IN OUT NOCOPY DBMS_DBFS_CONTENT_PROPERTIES_T, amount IN OUT NUMBER, offset IN NUMBER, buffers OUT NOCOPY DBMS_DBFS_CONTENT_RAW_T, prop_flags IN INTEGER DEFAULT (PROP_STD + PROP_OPT + PROP_DATA), asof IN TIMESTAMP DEFAULT NULL, store_name IN VARCHAR2 DEFAULT NULL, principal IN VARCHAR2 DEFAULT NULL); DBMS_DBFS_CONTENT.GETPATH ( path IN VARCHAR2, properties IN OUT NOCOPY PROPERTIES_T, amount IN OUT NUMBER, offset IN NUMBER, buffers OUT NOCOPY DBMS_DBFS_CONTENT_RAW_T, prop_flags IN INTEGER DEFAULT (PROP_STD + PROP_OPT + PROP_DATA), asof IN TIMESTAMP DEFAULT NULL, store_name IN VARCHAR2 DEFAULT NULL, principal IN VARCHAR2 DEFAULT NULL); Parameters Table 52-39 GETPATH Procedure Parameters Parameter Description path Name of path to path items properties One or more properties and their values to be returned depending on prop_flags (see DBMS_DBFS_CONTENT_PROPERTIES_T Table Type ) content BLOB holding data which populates the file (optional) item_type Type of the path item specified (see Table 52-4 ) amount On input, number of bytes to be read. On output, number of bytes read offset Byte offset from which to begin reading buffer Buffer to which to write buffers Buffers to which to write prop_flags Determines which properties are set, returned, or both. Default is PROP_STD . Specify properties to be returned by setting prop_spec , and providing an instance of the DBMS_DBFS_CONTENT_PROPERTIES_T Table Type with properties whose values are of interest. asof The "as of" timestamp at which the underlying read-only operation (or its read-only sub-components) executes forUpdate Specifies that a lock should be taken to signify exclusive write access to the path item deref If nonzero, attempts to resolve the given path item to actual data provided it is a reference store_name Name of store principal Agent (principal) invoking the current operation