---
id: 19c__DBMS_FLASHBACK_ARCHIVE.DISABLE_APPLICATION
name: DBMS_FLASHBACK_ARCHIVE.DISABLE_APPLICATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_FLASHBACK_ARCHIVE
tags: [dbms_flashback_archive]
source_file: DBMS_FLASHBACK_ARCHIVE.html
---

# DBMS_FLASHBACK_ARCHIVE.DISABLE_APPLICATION

This procedure takes an application name and disables Flashback Time Travel on all of its security tables.

## Syntax

```sql
DBMS_FLASHBACK_ARCHIVE.DISABLE_APPLICATION (
   application_name           IN   VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| application_name | VARCHAR2) | IN | Name of the application whose security tables will be disabled for Flashback Time Travel |

## Usage Notes

Syntax DBMS_FLASHBACK_ARCHIVE.DISABLE_APPLICATION ( application_name IN VARCHAR2); Parameters Table 73-5 DISABLE_APPLICATION Procedure Parameters Parameter Description application_name Name of the application whose security tables will be disabled for Flashback Time Travel