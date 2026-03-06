---
id: 19c__DBMS_FLASHBACK_ARCHIVE.LOCK_DOWN_APPLICATION
name: DBMS_FLASHBACK_ARCHIVE.LOCK_DOWN_APPLICATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_FLASHBACK_ARCHIVE
tags: [dbms_flashback_archive]
source_file: DBMS_FLASHBACK_ARCHIVE.html
---

# DBMS_FLASHBACK_ARCHIVE.LOCK_DOWN_APPLICATION

This procedure takes an application name and makes all the security tables read-only. The group called SYSTEM cannot be locked.

## Syntax

```sql
DBMS_FLASHBACK_ARCHIVE.LOCK_DOWN_APPLICATION (
   application_name           IN   VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| application_name | VARCHAR2) | IN | Name of the application for which a table has been added as a security table |

## Usage Notes

Syntax DBMS_FLASHBACK_ARCHIVE.LOCK_DOWN_APPLICATION ( application_name IN VARCHAR2); Parameters Table 73-13 LOCK_DOWN_APPLICATION Procedure Parameters Parameter Description application_name Name of the application for which a table has been added as a security table