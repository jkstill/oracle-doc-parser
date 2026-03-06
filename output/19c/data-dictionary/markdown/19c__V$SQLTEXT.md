---
id: 19c__V$SQLTEXT
name: V$SQLTEXT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dynamic_performance]
source_file: V-SQLTEXT.html
---

# V$SQLTEXT

V$SQLTEXT displays the text of SQL statements belonging to shared SQL cursors in the SGA.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ADDRESS | RAW(4 | 8) |  |
| HASH_VALUE | NUMBER |  |
| SQL_ID | VARCHAR2(13) |  |
| COMMAND_TYPE | NUMBER |  |
| PIECE | NUMBER |  |
| SQL_TEXT | VARCHAR2(64) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content