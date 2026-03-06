---
id: 19c__V$INDEXED_FIXED_COLUMN
name: V$INDEXED_FIXED_COLUMN
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: index
tags: [dynamic_performance]
source_file: V-INDEXED_FIXED_COLUMN.html
---

# V$INDEXED_FIXED_COLUMN

V$INDEXED_FIXED_COLUMN displays the columns in dynamic performance tables that are indexed ( X$ tables).

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TABLE_NAME | VARCHAR2(128) |  |
| INDEX_NUMBER | NUMBER |  |
| COLUMN_NAME | VARCHAR2(128) |  |
| COLUMN_POSITION | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content The X$ tables can change without notice. Use this view only to write queries against fixed views ( V$ views) more efficiently.