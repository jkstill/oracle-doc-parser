---
id: 19c__DBMS_FLASHBACK_ARCHIVE.DROP_APPLICATION
name: DBMS_FLASHBACK_ARCHIVE.DROP_APPLICATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_FLASHBACK_ARCHIVE
tags: [dbms_flashback_archive]
source_file: DBMS_FLASHBACK_ARCHIVE.html
---

# DBMS_FLASHBACK_ARCHIVE.DROP_APPLICATION

This procedure takes an application name and removes it from the list of applications. As part of this procedure, Flashback Time Travel will be disabled on all security-enabled tables and all history data will be lost. The group called SYSTEM cannot be dropped.

## Syntax

```sql
DBMS_FLASHBACK_ARCHIVE.DROP_APPLICATION (
   application_name           IN   VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| application_name | VARCHAR2) | IN | Name of the application for which a table has been added as a security table |

## Usage Notes

Syntax DBMS_FLASHBACK_ARCHIVE.DROP_APPLICATION ( application_name IN VARCHAR2); Parameters Table 73-8 DROP_APPLICATION Procedure Parameters Parameter Description application_name Name of the application for which a table has been added as a security table