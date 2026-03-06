---
id: 19c__DBMS_DBFS_CONTENT.CREATEFILE
name: DBMS_DBFS_CONTENT.CREATEFILE
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.CREATEFILE

This procedure creates a file.

## Syntax

```sql
DBMS_DBFS_CONTENT.CREATEFILE (
   path        IN              VARCHAR2,
   properties  IN OUT NOCOPY   DBMS_DBFS_CONTENT_PROPERTIES_T,
   content     IN OUT NOCOPY   BLOB,
   prop_flags  IN              INTEGER     DEFAULT (PROP_STD + PROP_DATA),
   store_name  IN              VARCHAR2    DEFAULT NULL,
   principal   IN              VARCHAR2    DEFAULT NULL);

DBMS_DBFS_CONTENT.CREATEFILE (
   path        IN              VARCHAR2,
   properties  IN OUT NOCOPY   PROPERTIES_T,
   content     IN OUT NOCOPY   BLOB,
   prop_flags  IN              INTEGER     DEFAULT (PROP_STD + PROP_DATA),
   store_name  IN              VARCHAR2    DEFAULT NULL,
   principal   IN              VARCHAR2    DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| path | VARCHAR2 | IN | Name of path to the file |
| properties | NOCOPY | IN OUT | One or more properties and their values to be set, returned, or both, depending on prop_flags (see DBMS_DBFS_CONTENT_PROPERTIES_T Table Type ) |
| content | NOCOPY | IN OUT | BLOB holding data with which to populate the file (optional) |
| prop_flags | INTEGER | IN | Determines which properties are set, returned, or both. Default is PROP_STD . Specify properties to be returned by setting prop_spec , and providing an instance of the DBMS_DBFS_CONTENT_PROPERTIES_T Table Type with properties whose values are of interest. |
| store_name | VARCHAR2 | IN | Name of store |
| principal | VARCHAR2 | IN | File system user for whom the access check is made |

## Usage Notes

Syntax DBMS_DBFS_CONTENT.CREATEFILE ( path IN VARCHAR2, properties IN OUT NOCOPY DBMS_DBFS_CONTENT_PROPERTIES_T, content IN OUT NOCOPY BLOB, prop_flags IN INTEGER DEFAULT (PROP_STD + PROP_DATA), store_name IN VARCHAR2 DEFAULT NULL, principal IN VARCHAR2 DEFAULT NULL); DBMS_DBFS_CONTENT.CREATEFILE ( path IN VARCHAR2, properties IN OUT NOCOPY PROPERTIES_T, content IN OUT NOCOPY BLOB, prop_flags IN INTEGER DEFAULT (PROP_STD + PROP_DATA), store_name IN VARCHAR2 DEFAULT NULL, principal IN VARCHAR2 DEFAULT NULL); Parameters Table 52-23 CREATEFILE Procedure Parameters Parameter Description path Name of path to the file properties One or more properties and their values to be set, returned, or both, depending on prop_flags (see DBMS_DBFS_CONTENT_PROPERTIES_T Table Type ) content BLOB holding data with which to populate the file (optional) prop_flags Determines which properties are set, returned, or both. Default is PROP_STD . Specify properties to be returned by setting prop_spec , and providing an instance of the DBMS_DBFS_CONTENT_PROPERTIES_T Table Type with properties whose values are of interest. store_name Name of store principal File system user for whom the access check is made