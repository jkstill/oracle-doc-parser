---
id: 19c__DBMS_FLASHBACK_ARCHIVE.REMOVE_TABLE_FROM_APPLICATION
name: DBMS_FLASHBACK_ARCHIVE.REMOVE_TABLE_FROM_APPLICATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_FLASHBACK_ARCHIVE
tags: [dbms_flashback_archive]
source_file: DBMS_FLASHBACK_ARCHIVE.html
---

# DBMS_FLASHBACK_ARCHIVE.REMOVE_TABLE_FROM_APPLICATION

This procedure takes an application name and marks a table in it as no longer being a security table.

## Syntax

```sql
DBMS_FLASHBACK_ARCHIVE.REMOVE_TABLE_TO_APPLICATION (
   application_name           IN   VARCHAR2,
   table_name                 IN   VARCHAR2,
   schema_name                IN   VARCHAR2 := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| application_name | VARCHAR2 | IN | Name of the application for which a table is being removed from the list of security tables |
| table_name | VARCHAR2 | IN | Name of the table to mark as being no longer a security table for the given application |
| schema_name | VARCHAR2 | IN | Name of the schema containing the desired table. If no schema name is specified, the current schema is used. |

## Usage Notes

If the application is already enabled for Flashback Archive, Flashback Archive will be disabled for this table. Syntax DBMS_FLASHBACK_ARCHIVE.REMOVE_TABLE_TO_APPLICATION ( application_name IN VARCHAR2, table_name IN VARCHAR2, schema_name IN VARCHAR2 := NULL); Parameters Table 73-17 REMOVE_TABLE_FROM_APPLICATION Procedure Parameters Parameter Description application_name Name of the application for which a table is being removed from the list of security tables table_name Name of the table to mark as being no longer a security table for the given application schema_name Name of the schema containing the desired table. If no schema name is specified, the current schema is used.