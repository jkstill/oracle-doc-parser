---
id: 19c__DBMS_DBFS_CONTENT.GETPATHNOWAIT
name: DBMS_DBFS_CONTENT.GETPATHNOWAIT
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.GETPATHNOWAIT

This procedure implies that the operation is for an update, and, if implemented, allows providers to return an exception ( ORA-00054 ) rather than wait for row locks.

## Syntax

```sql
DBMS_DBFS_CONTENT.GETPATHNOWAIT (
        path        IN              VARCHAR2,
        properties  IN OUT NOCOPY   DBMS_DBFS_CONTENT_PROPERTIES_T,
        content     OUT    NOCOPY   BLOB,
        item_type   OUT             INTEGER,
        prop_flags  IN              INTEGER     DEFAULT (PROP_STD +
                                                         PROP_OPT +
                                                         PROP_DATA),
        deref       IN              BOOLEAN     DEFAULT FALSE,
        store_name  IN              VARCHAR2    DEFAULT NULL,
        principal   IN              VARCHAR2    DEFAULT NULL);

DBMS_DBFS_CONTENT.GETPATHNOWAIT (
        path        IN              VARCHAR2,
        properties  IN OUT NOCOPY   PROPERTIES_T,
        content     OUT    NOCOPY   BLOB,
        item_type   OUT             INTEGER,
        prop_flags  IN              INTEGER     DEFAULT (PROP_STD +
                                                         PROP_OPT +
                                                         PROP_DATA),
        deref       IN              BOOLEAN     DEFAULT FALSE,
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
| prop_flags | INTEGER | IN | Determines which properties are returned. Default is PROP_STD . Specify properties to be returned by setting prop_spec , and providing an instance of the DBMS_DBFS_CONTENT_PROPERTIES_T Table Type with properties whose values are of interest. |
| asof |  |  | The "as of" timestamp at which the underlying read-only operation (or its read-only sub-components) executes |
| deref | BOOLEAN | IN | If nonzero, attempts to resolve the given path item to actual data provided it is a reference |
| store_name | VARCHAR2 | IN | Name of store |
| principal | VARCHAR2 | IN | Agent (principal) invoking the current operation |

## Usage Notes

See FEATURE_NOWAIT in Table 52-5 for more information. Syntax DBMS_DBFS_CONTENT.GETPATHNOWAIT ( path IN VARCHAR2, properties IN OUT NOCOPY DBMS_DBFS_CONTENT_PROPERTIES_T, content OUT NOCOPY BLOB, item_type OUT INTEGER, prop_flags IN INTEGER DEFAULT (PROP_STD + PROP_OPT + PROP_DATA), deref IN BOOLEAN DEFAULT FALSE, store_name IN VARCHAR2 DEFAULT NULL, principal IN VARCHAR2 DEFAULT NULL); DBMS_DBFS_CONTENT.GETPATHNOWAIT ( path IN VARCHAR2, properties IN OUT NOCOPY PROPERTIES_T, content OUT NOCOPY BLOB, item_type OUT INTEGER, prop_flags IN INTEGER DEFAULT (PROP_STD + PROP_OPT + PROP_DATA), deref IN BOOLEAN DEFAULT FALSE, store_name IN VARCHAR2 DEFAULT NULL, principal IN VARCHAR2 DEFAULT NULL); Parameters Table 52-42 GETPATHNOWAIT Procedure Parameters Parameter Description path Name of path to path items properties One or more properties and their values to be returned depending on prop_flags (see DBMS_DBFS_CONTENT_PROPERTIES_T Table Type ) content BLOB holding data which populates the file (optional) item_type Type of the path item specified (see Table 52-4 ) prop_flags Determines which properties are returned. Default is PROP_STD . Specify properties to be returned by setting prop_spec , and providing an instance of the DBMS_DBFS_CONTENT_PROPERTIES_T Table Type with properties whose values are of interest. asof The "as of" timestamp at which the underlying read-only operation (or its read-only sub-components) executes deref If nonzero, attempts to resolve the given path item to actual data provided it is a reference store_name Name of store principal Agent (principal) invoking the current operation