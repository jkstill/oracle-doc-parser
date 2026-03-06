---
id: 19c__DBMS_DBFS_CONTENT.RENAMEPATH
name: DBMS_DBFS_CONTENT.RENAMEPATH
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.RENAMEPATH

This procedure renames or moves a path. This operation can be performed across directory hierarchies and mount-points as long as it is within the same store.

## Syntax

```sql
DBMS_DBFS_CONTENT.RENAMEPATH (
   oldPath     IN              VARCHAR2,
   newPath     IN              VARCHAR2,
   properties  IN OUT NOCOPY   DBMS_DBFS_CONTENT_PROPERTIES_T,
   store_name  IN              VARCHAR2    DEFAULT NULL,
   principal   IN              VARCHAR2    DEFAULT NULL);

DBMS_DBFS_CONTENT.RENAMEPATH (
   oldPath     IN              VARCHAR2,
   newPath     IN              VARCHAR2,
   properties  IN OUT NOCOPY   PROPERTIES_T,
   store_name  IN              VARCHAR2    DEFAULT NULL,
   principal   IN              VARCHAR2    DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| oldPath | VARCHAR2 | IN | Name of path prior to renaming |
| newPath | VARCHAR2 | IN | Name of path after renaming |
| properties | NOCOPY | IN OUT | One or more properties and their values to be set depending on prop_flags (see DBMS_DBFS_CONTENT_PROPERTIES_T Table Type ) |
| store_name | VARCHAR2 | IN | Name of store, must be unique |
| principal | VARCHAR2 | IN | Agent (principal) invoking the current operation |

## Usage Notes

Note: See Oracle Database SecureFiles and Large Objects Developer's Guide for Rename and Move operations Note: See Oracle Database SecureFiles and Large Objects Developer's Guide for Rename and Move operations Syntax DBMS_DBFS_CONTENT.RENAMEPATH ( oldPath IN VARCHAR2, newPath IN VARCHAR2, properties IN OUT NOCOPY DBMS_DBFS_CONTENT_PROPERTIES_T, store_name IN VARCHAR2 DEFAULT NULL, principal IN VARCHAR2 DEFAULT NULL); DBMS_DBFS_CONTENT.RENAMEPATH ( oldPath IN VARCHAR2, newPath IN VARCHAR2, properties IN OUT NOCOPY PROPERTIES_T, store_name IN VARCHAR2 DEFAULT NULL, principal IN VARCHAR2 DEFAULT NULL); Parameters Table 52-63 RENAMEPATH Procedure Parameters Parameter Description oldPath Name of path prior to renaming newPath Name of path after renaming properties One or more properties and their values to be set depending on prop_flags (see DBMS_DBFS_CONTENT_PROPERTIES_T Table Type ) store_name Name of store, must be unique principal Agent (principal) invoking the current operation