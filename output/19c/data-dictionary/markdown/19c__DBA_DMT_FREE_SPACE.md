---
id: 19c__DBA_DMT_FREE_SPACE
name: DBA_DMT_FREE_SPACE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_DMT_FREE_SPACE.html
---

# DBA_DMT_FREE_SPACE

DBA_DMT_FREE_SPACE describes the free extents in all dictionary managed tablespaces in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TABLESPACE_ID | NUMBER | Identifier number of the tablespace containing the extent |
| FILE_ID | NUMBER | File identifier number of the file containing the extent |
| BLOCK_ID | NUMBER | Starting block number of the extent |
| BLOCKS | NUMBER | Size of the extent (in Oracle blocks) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content