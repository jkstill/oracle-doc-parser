---
id: 19c__DBMS_FLASHBACK_ARCHIVE.CREATE_TEMP_HISTORY_TABLE
name: DBMS_FLASHBACK_ARCHIVE.CREATE_TEMP_HISTORY_TABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_FLASHBACK_ARCHIVE
tags: [dbms_flashback_archive]
source_file: DBMS_FLASHBACK_ARCHIVE.html
---

# DBMS_FLASHBACK_ARCHIVE.CREATE_TEMP_HISTORY_TABLE

This procedure creates a table called TEMP_HISTORY with the correct definition in schema.

## Syntax

```sql
DBMS_FLASHBACK_ARCHIVE.CREATE_TEMP_HISTORY_TABLE (
   owner_name1      IN   VARCHAR2, 
   table_name1      IN   VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| owner_name 1 |  |  | Schema of the Flashback Time Travel-enabled table |
| table_name 1 |  |  | Name of the Flashback Time Travel-enabled table |

## Usage Notes

Syntax DBMS_FLASHBACK_ARCHIVE.CREATE_TEMP_HISTORY_TABLE ( owner_name1 IN VARCHAR2, table_name1 IN VARCHAR2); Parameters Table 73-4 CREATE_TEMP_HISTORY_TABLE Procedure Parameters Parameter Description owner_name 1 Schema of the Flashback Time Travel-enabled table table_name 1 Name of the Flashback Time Travel-enabled table