---
id: 19c__DBMS_DBFS_CONTENT.CREATEDIRECTORY
name: DBMS_DBFS_CONTENT.CREATEDIRECTORY
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.CREATEDIRECTORY

This procedure creates a directory.

## Syntax

```sql
DBMS_DBFS_CONTENT.CREATEDIRECTORY (
   path        IN              VARCHAR2,
   properties  IN OUT NOCOPY   DBMS_DBFS_CONTENT_PROPERTIES_T,
   prop_flags  IN              INTEGER     DEFAULT PROP_STD,
   recurse     IN              BOOLEAN     DEFAULT FALSE,
   store_name  IN              VARCHAR2    DEFAULT NULL,
   principal   IN              VARCHAR2    DEFAULT NULL);

DBMS_DBFS_CONTENT.CREATEDIRECTORY (
   path        IN              VARCHAR2,
   properties  IN OUT NOCOPY   PROPERTIES_T,
   prop_flags  IN              INTEGER     DEFAULT PROP_STD,
   recurse     IN              BOOLEAN     DEFAULT FALSE,
   store_name  IN              VARCHAR2    DEFAULT NULL,
   principal   IN              VARCHAR2    DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| path | VARCHAR2 | IN | Name of path to the directory |
| properties | NOCOPY | IN OUT | One or more properties and their values to be set, returned, or both, depending on prop_flags (see DBMS_DBFS_CONTENT_PROPERTIES_T Table Type ) |
| prop_flags | INTEGER | IN | Determines which properties are set, returned, or both. Default is PROP_STD . Specify properties to be returned by setting PROP_SPC (see Table 52-9 ), and providing an instance of the DBMS_DBFS_CONTENT_PROPERTIES_T Table Type with properties whose values are of interest. |
| recurse | BOOLEAN | IN | If 0, do not execute recursively; otherwise, recursively create the directories above the given directory |
| store_name | VARCHAR2 | IN | Name of store |
| principal | VARCHAR2 | IN | File system user for whom the access check is made |

## Usage Notes

Syntax DBMS_DBFS_CONTENT.CREATEDIRECTORY ( path IN VARCHAR2, properties IN OUT NOCOPY DBMS_DBFS_CONTENT_PROPERTIES_T, prop_flags IN INTEGER DEFAULT PROP_STD, recurse IN BOOLEAN DEFAULT FALSE, store_name IN VARCHAR2 DEFAULT NULL, principal IN VARCHAR2 DEFAULT NULL); DBMS_DBFS_CONTENT.CREATEDIRECTORY ( path IN VARCHAR2, properties IN OUT NOCOPY PROPERTIES_T, prop_flags IN INTEGER DEFAULT PROP_STD, recurse IN BOOLEAN DEFAULT FALSE, store_name IN VARCHAR2 DEFAULT NULL, principal IN VARCHAR2 DEFAULT NULL); Parameters Table 52-22 CREATEDIRECTORY Procedure Parameters Parameter Description path Name of path to the directory properties One or more properties and their values to be set, returned, or both, depending on prop_flags (see DBMS_DBFS_CONTENT_PROPERTIES_T Table Type ) prop_flags Determines which properties are set, returned, or both. Default is PROP_STD . Specify properties to be returned by setting PROP_SPC (see Table 52-9 ), and providing an instance of the DBMS_DBFS_CONTENT_PROPERTIES_T Table Type with properties whose values are of interest. recurse If 0, do not execute recursively; otherwise, recursively create the directories above the given directory store_name Name of store principal File system user for whom the access check is made