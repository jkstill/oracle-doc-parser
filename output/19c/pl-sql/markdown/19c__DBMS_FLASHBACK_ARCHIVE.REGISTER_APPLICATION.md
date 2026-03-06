---
id: 19c__DBMS_FLASHBACK_ARCHIVE.REGISTER_APPLICATION
name: DBMS_FLASHBACK_ARCHIVE.REGISTER_APPLICATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_FLASHBACK_ARCHIVE
tags: [dbms_flashback_archive]
source_file: DBMS_FLASHBACK_ARCHIVE.html
---

# DBMS_FLASHBACK_ARCHIVE.REGISTER_APPLICATION

This procedure takes an application name and optionally a Flashback Archive, and registers an application for database hardening.

## Syntax

```sql
DBMS_FLASHBACK_ARCHIVE.REGISTER_APPLICATION (
   application_name           IN   VARCHAR2,
   flashback_archive_name     IN    VARCHAR2 := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| application_name | VARCHAR2 | IN | Name of the application which is being registered. The application SYSTEM is already registered when the package is created and is populated with list of tables needed for database hardening. |
| flashback_archive_name | VARCHAR2 | IN | Name of the Flashback Archive in which the historical data for the security tables for given application is stored. If no Flashback Archive is specified, the default Flashback Archive is used. |

## Usage Notes

When database hardening is enabled, then all the security tables for that application are enabled for Flashback Archive using the given Flashback Archive. If no Flashback Archive is specified, the default Flashback Archive is used. See Also: Using Flashback Time Travel in Oracle Database Development Guide regarding database hardening See Also: Using Flashback Time Travel in Oracle Database Development Guide regarding database hardening Syntax DBMS_FLASHBACK_ARCHIVE.REGISTER_APPLICATION ( application_name IN VARCHAR2, flashback_archive_name IN VARCHAR2 := NULL); Parameters Table 73-16 REGISTER_APPLICATION Procedure Parameters Parameter Description application_name Name of the application which is being registered. The application SYSTEM is already registered when the package is created and is populated with list of tables needed for database hardening. flashback_archive_name Name of the Flashback Archive in which the historical data for the security tables for given application is stored. If no Flashback Archive is specified, the default Flashback Archive is used.