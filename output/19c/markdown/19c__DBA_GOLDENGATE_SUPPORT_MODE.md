---
id: 19c__DBA_GOLDENGATE_SUPPORT_MODE
name: DBA_GOLDENGATE_SUPPORT_MODE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_GOLDENGATE_SUPPORT_MODE.html
---

# DBA_GOLDENGATE_SUPPORT_MODE

DBA_GOLDENGATE_SUPPORT_MODE displays information about the level of Oracle GoldenGate capture process support for the tables in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Table owner |
| OBJECT_NAME | VARCHAR2(128) | Table name |
| SUPPORT_MODE | VARCHAR2(6) | Capture process support level for the table: FULL - A capture process can capture changes made to all of the columns in the table ID KEY - A capture process can capture changes made to the key columns and any other columns in the table supported by the capture process, except for LOB , LONG , LONG RAW , and XMLType columns. INTERNAL - A capture process cannot capture changes made to any columns in the table because the table is secondary to a user-created table and is updated implicitly when changes are made to the user-created table. Such tables include mapping tables for index-organized tables, storage tables for nested tables, materialized view logs, secondary objects associated with domain indexes, and temporary tables. NONE - A capture process cannot capture changes made to any columns in the table because the table is not supported for replication. |