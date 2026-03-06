---
id: 19c__DBMS_FLASHBACK_ARCHIVE.ENABLE_APPLICATION
name: DBMS_FLASHBACK_ARCHIVE.ENABLE_APPLICATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_FLASHBACK_ARCHIVE
tags: [dbms_flashback_archive]
source_file: DBMS_FLASHBACK_ARCHIVE.html
---

# DBMS_FLASHBACK_ARCHIVE.ENABLE_APPLICATION

This procedure takes an application name and enables Flashback Time Travel on all the security tables for this application. Once an application is enabled, every change to an Flashback Time Travel enabled table will be tracked.

## Syntax

```sql
DBMS_FLASHBACK_ARCHIVE.ENABLE_APPLICATION (
   application_name           IN   VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| application_name | VARCHAR2) | IN | Name of the application for which to enable Flashback Time Travel on all its security tables |

## Usage Notes

Syntax DBMS_FLASHBACK_ARCHIVE.ENABLE_APPLICATION ( application_name IN VARCHAR2); Parameters Table 73-9 ENABLE_APPLICATION Procedure Parameters Parameter Description application_name Name of the application for which to enable Flashback Time Travel on all its security tables