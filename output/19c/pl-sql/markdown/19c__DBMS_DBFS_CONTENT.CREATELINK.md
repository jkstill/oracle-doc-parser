---
id: 19c__DBMS_DBFS_CONTENT.CREATELINK
name: DBMS_DBFS_CONTENT.CREATELINK
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.CREATELINK

This procedure creates a new link element srcPath with the value of dstPath . The value of dstPath is not validated or interpreted in any way by this procedure. This is analogous to a UNIX file system symbolic link.

## Syntax

```sql
DBMS_DBFS_CONTENT.CREATELINK (
   srcPath     IN              VARCHAR2,
   dstPath     IN              VARCHAR2,
   properties  IN OUT NOCOPY   DBMS_DBFS_CONTENT_PROPERTIES_T,
   prop_flags  IN              INTEGER     DEFAULT PROP_STD,
   store_name  IN              VARCHAR2    DEFAULT NULL,
   principal   IN              VARCHAR2    DEFAULT NULL);

DBMS_DBFS_CONTENT.CREATELINK (
   srcPath     IN              VARCHAR2,
   dstPath     IN              VARCHAR2,
   properties  IN OUT NOCOPY   PROPERTIES_T,
   prop_flags  IN              INTEGER     DEFAULT PROP_STD,
   store_name  IN              VARCHAR2    DEFAULT NULL,
   principal   IN              VARCHAR2    DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| srcPath | VARCHAR2 | IN | File system entry to create. |
| dstPath | VARCHAR2 | IN | Value to associate with srcPath . |
| properties | NOCOPY | IN OUT | One or more properties and their values to be set, returned depending, or both, on prop_flags (see DBMS_DBFS_CONTENT_PROPERTIES_T Table Type ) |
| prop_flags | INTEGER | IN | Determines which properties are set, returned, or both. Default is PROP_STD . Specify properties to be returned by setting prop_spec , and providing an instance of the DBMS_DBFS_CONTENT_PROPERTIES_T Table Type with properties whose values are of interest. |
| store_name | VARCHAR2 | IN | Name of store |
| principal | VARCHAR2 | IN | File system user for whom the access check is made |

## Usage Notes

Syntax DBMS_DBFS_CONTENT.CREATELINK ( srcPath IN VARCHAR2, dstPath IN VARCHAR2, properties IN OUT NOCOPY DBMS_DBFS_CONTENT_PROPERTIES_T, prop_flags IN INTEGER DEFAULT PROP_STD, store_name IN VARCHAR2 DEFAULT NULL, principal IN VARCHAR2 DEFAULT NULL); DBMS_DBFS_CONTENT.CREATELINK ( srcPath IN VARCHAR2, dstPath IN VARCHAR2, properties IN OUT NOCOPY PROPERTIES_T, prop_flags IN INTEGER DEFAULT PROP_STD, store_name IN VARCHAR2 DEFAULT NULL, principal IN VARCHAR2 DEFAULT NULL); Parameters Table 52-24 CREATELINK Procedure Parameters Parameter Description srcPath File system entry to create. dstPath Value to associate with srcPath . properties One or more properties and their values to be set, returned depending, or both, on prop_flags (see DBMS_DBFS_CONTENT_PROPERTIES_T Table Type ) prop_flags Determines which properties are set, returned, or both. Default is PROP_STD . Specify properties to be returned by setting prop_spec , and providing an instance of the DBMS_DBFS_CONTENT_PROPERTIES_T Table Type with properties whose values are of interest. store_name Name of store principal File system user for whom the access check is made