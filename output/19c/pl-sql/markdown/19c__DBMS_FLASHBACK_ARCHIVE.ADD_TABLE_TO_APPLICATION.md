---
id: 19c__DBMS_FLASHBACK_ARCHIVE.ADD_TABLE_TO_APPLICATION
name: DBMS_FLASHBACK_ARCHIVE.ADD_TABLE_TO_APPLICATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_FLASHBACK_ARCHIVE
tags: [dbms_flashback_archive]
source_file: DBMS_FLASHBACK_ARCHIVE.html
---

# DBMS_FLASHBACK_ARCHIVE.ADD_TABLE_TO_APPLICATION

This procedure takes an application name and adds a table to the application as a security table. If the application is enabled for Flashback Time Travel, then this table will also be enabled for Flashback Time Travel.

## Syntax

```sql
DBMS_FLASHBACK_ARCHIVE.ADD_TABLE_TO_APPLICATION (
   application_name           IN   VARCHAR2,
   table_name                 IN   VARCHAR2,
   schema_name                IN   VARCHAR2 := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| application_name | VARCHAR2 | IN | Name of the application for which a table has been added as a security table |
| table_name | VARCHAR2 | IN | Name of the table to add as a security table for the given application |
| schema_name | VARCHAR2 | IN | Name of the schema containing the desired table. If no schema name is specified, the current schema is used. |

## Usage Notes

Syntax DBMS_FLASHBACK_ARCHIVE.ADD_TABLE_TO_APPLICATION ( application_name IN VARCHAR2, table_name IN VARCHAR2, schema_name IN VARCHAR2 := NULL); Parameters Table 73-3 ADD_TABLE_TO_APPLICATION Procedure Parameters Parameter Description application_name Name of the application for which a table has been added as a security table table_name Name of the table to add as a security table for the given application schema_name Name of the schema containing the desired table. If no schema name is specified, the current schema is used.