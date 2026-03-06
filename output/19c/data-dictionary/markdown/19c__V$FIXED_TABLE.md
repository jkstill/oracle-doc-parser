---
id: 19c__V$FIXED_TABLE
name: V$FIXED_TABLE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [dynamic_performance]
source_file: V-FIXED_TABLE.html
---

# V$FIXED_TABLE

V$FIXED_TABLE displays all dynamic performance tables, views, and derived tables in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| NAME | VARCHAR2(128) |  |
| OBJECT_ID | NUMBER |  |
| TYPE | VARCHAR2(5) |  |
| TABLE_NUM | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Some V$ tables (for example, V$ROLLNAME ) refer to real tables and are therefore not listed.