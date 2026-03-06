---
id: 19c__ALL_XSTREAM_OUT_SUPPORT_MODE
name: ALL_XSTREAM_OUT_SUPPORT_MODE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_XSTREAM_OUT_SUPPORT_MODE.html
---

# ALL_XSTREAM_OUT_SUPPORT_MODE

ALL_XSTREAM_OUT_SUPPORT_MODE displays information about the level of XStream capture process support for the tables accessible to the current user in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Table owner |
| OBJECT_NAME | VARCHAR2(128) | Table name |
| SUPPORT_MODE | VARCHAR2(6) | Capture process support level for the table: FULL - A capture process can capture changes made to all of the columns in the table. ID KEY - A capture process can capture changes made to the key columns and any other columns in the table that are supported by the capture process, except for LOB, LONG , LONG RAW , and XMLType columns. NONE - A capture process cannot capture changes made to any columns in the table. |

## Usage Notes

Related View DBA_XSTREAM_OUT_SUPPORT_MODE displays information about the level of XStream capture process support for the tables in the database. See Also: " DBA_XSTREAM_OUT_SUPPORT_MODE " See Also: " DBA_XSTREAM_OUT_SUPPORT_MODE "