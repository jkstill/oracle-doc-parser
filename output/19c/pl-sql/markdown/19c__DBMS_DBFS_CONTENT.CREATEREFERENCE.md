---
id: 19c__DBMS_DBFS_CONTENT.CREATEREFERENCE
name: DBMS_DBFS_CONTENT.CREATEREFERENCE
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.CREATEREFERENCE

This procedure creates a physical link, srcPath , to an already existing file system element, dstPath (such as file or directory). The resulting entry shares the same metadata structures as the value of the dstPath parameter, and so is similar to incrementing a reference count on the file system element. This is analogous to a UNIX file system hard link.

## Syntax

```sql
DBMS_DBFS_CONTENT.CREATEREFERENCE (
   srcPath     IN              VARCHAR2,
   dstPath     IN              VARCHAR2,
   properties  IN OUT NOCOPY   DBMS_DBFS_CONTENT_PROPERTIES_T,
   prop_flags  IN              INTEGER     DEFAULT PROP_STD,
   store_name  IN              VARCHAR2    DEFAULT NULL,
   principal   IN              VARCHAR2    DEFAULT NULL);

DBMS_DBFS_CONTENT.CREATEREFERENCE (
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
| dstPath | VARCHAR2 | IN | Path that is the reference to srcPath . |
| properties | NOCOPY | IN OUT | One or more properties and their values to be set, returned, or both, depending on prop_flags (see DBMS_DBFS_CONTENT_PROPERTIES_T Table Type ) |
| prop_flags | INTEGER | IN | Determines which properties are set, returned. Default is PROP_STD . Specify properties to be returned by setting prop_spec , and providing an instance of the DBMS_DBFS_CONTENT_PROPERTIES_T Table Type with properties whose values are of interest. |
| store_name | VARCHAR2 | IN | Name of store |
| principal | VARCHAR2 | IN | File system user for whom the access check is made |

## Usage Notes

Syntax DBMS_DBFS_CONTENT.CREATEREFERENCE ( srcPath IN VARCHAR2, dstPath IN VARCHAR2, properties IN OUT NOCOPY DBMS_DBFS_CONTENT_PROPERTIES_T, prop_flags IN INTEGER DEFAULT PROP_STD, store_name IN VARCHAR2 DEFAULT NULL, principal IN VARCHAR2 DEFAULT NULL); DBMS_DBFS_CONTENT.CREATEREFERENCE ( srcPath IN VARCHAR2, dstPath IN VARCHAR2, properties IN OUT NOCOPY PROPERTIES_T, prop_flags IN INTEGER DEFAULT PROP_STD, store_name IN VARCHAR2 DEFAULT NULL, principal IN VARCHAR2 DEFAULT NULL); Parameters Table 52-25 CREATEREFERENCE Procedure Parameters Parameter Description srcPath File system entry to create. dstPath Path that is the reference to srcPath . properties One or more properties and their values to be set, returned, or both, depending on prop_flags (see DBMS_DBFS_CONTENT_PROPERTIES_T Table Type ) prop_flags Determines which properties are set, returned. Default is PROP_STD . Specify properties to be returned by setting prop_spec , and providing an instance of the DBMS_DBFS_CONTENT_PROPERTIES_T Table Type with properties whose values are of interest. store_name Name of store principal File system user for whom the access check is made