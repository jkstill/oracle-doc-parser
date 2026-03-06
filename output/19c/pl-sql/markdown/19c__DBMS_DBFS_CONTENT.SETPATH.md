---
id: 19c__DBMS_DBFS_CONTENT.SETPATH
name: DBMS_DBFS_CONTENT.SETPATH
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DBFS_CONTENT
tags: [dbms_dbfs_content]
source_file: DBMS_DBFS_CONTENT.html
---

# DBMS_DBFS_CONTENT.SETPATH

This procedure assigns a path name to a path item represented by contentID.

## Syntax

```sql
DBMS_DBFS_CONTENT.SETPATH (
   store_name  IN              VARCHAR2,
   contentID   IN              RAW,
   path        IN              VARCHAR2,
   properties  IN OUT NOCOPY   DBMS_DBFS_CONTENT_PROPERTIES_T,
   principal   IN              VARCHAR2    DEFAULT NULL);

DBMS_DBFS_CONTENT.SETPATH (
   store_name  IN              VARCHAR2,
   contentID   IN              RAW,
   path        IN              VARCHAR2,
   properties  IN OUT NOCOPY   PROPERTIES_T,
   principal   IN              VARCHAR2    DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| store_name | VARCHAR2 | IN | Name of the store |
| contentID | RAW | IN | Unique identifier for the item to be associated |
| path | VARCHAR2 | IN | Name of path to path item |
| properties | NOCOPY | IN OUT | One or more properties and their values to be set depending on prop_flags (see DBMS_DBFS_CONTENT_PROPERTIES_T Table Type ) |
| principal | VARCHAR2 | IN | Agent (principal) invoking the current operation |

## Usage Notes

Stores and their providers that support contentID-based access and lazy path name binding also support the SETPATH Procedure that associates an existing contentID with a new path. Note: See Oracle Database SecureFiles and Large Objects Developer's Guide for Rename and Move operations Note: See Oracle Database SecureFiles and Large Objects Developer's Guide for Rename and Move operations Syntax DBMS_DBFS_CONTENT.SETPATH ( store_name IN VARCHAR2, contentID IN RAW, path IN VARCHAR2, properties IN OUT NOCOPY DBMS_DBFS_CONTENT_PROPERTIES_T, principal IN VARCHAR2 DEFAULT NULL); DBMS_DBFS_CONTENT.SETPATH ( store_name IN VARCHAR2, contentID IN RAW, path IN VARCHAR2, properties IN OUT NOCOPY PROPERTIES_T, principal IN VARCHAR2 DEFAULT NULL); Parameters Table 52-71 SETPATH Procedure Parameters Parameter Description store_name Name of the store contentID Unique identifier for the item to be associated path Name of path to path item properties One or more properties and their values to be set depending on prop_flags (see DBMS_DBFS_CONTENT_PROPERTIES_T Table Type ) principal Agent (principal) invoking the current operation